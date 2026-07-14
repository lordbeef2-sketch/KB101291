# NI_LABVIEW_USER_MANUAL

<!--SYSTEM_CORPUS id=NI_LABVIEW_USER_MANUAL format=markdown generated=2026-07-14T12:02:18+00:00 -->
- title: LabVIEW User Manual
- source: https://docs-be.ni.com/bundle/labview/preprocessedpdf/enus
- source_sha256: 725f2ab71da4b9dc3e376db19aaf7717998751735a038907fc0c3e43e4e7ac0b
- versions: 2024 Q1|2024 Q3|2025 Q1|2025 Q3|2026 Q1
- fidelity: full-text-records

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1501 ordinal=1501 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Additional Information Refer to the caveats and recommendations for
      packed project libraries for more information.

Shared Library

    •   Required Configurations
            ◦   Source Files
    •  Recommended Configurations
            ◦   Information
            ◦   Destinations
            ◦   Source Files Settings
    •   Additional Information Refer to the Characteristics of LabVIEW-built shared
        libraries for more information.

Source Distribution

    •   Required Configurations
            ◦   Source Files
    •  Recommended Configurations
            ◦   Information
            ◦   Destinations
            ◦   Source File Settings

Zip File

    •   Required Configurations
            ◦   Source Files
    •  Recommended Configurations
            ◦   Zip Information
            ◦   Zip File Structure
    •   Additional Information
            ◦     If you select the Zip entire project option from the Source Files page
              of the Zip File Properties dialog box, LabVIEW does not automatically
             include outputs from other build specifications in the Included Items
               tree. You must use the arrow buttons to add a source distribution,
            shared library, or application to the zip file.
            ◦   Outputs of zip or installer build specifications do not appear in the
             Project Files tree on the Source Files page. To include another zip file
             or installer in the zip file, add the zip file or installer you want to
             include to the LabVIEW project under the target from which you are
             building the zip file.


                                             © National Instruments Corporation 1501

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1501 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1502 ordinal=1502 -->
## LabVIEW User Manual

LabVIEW User Manual


                                 ◦   You can use the Zip VIs or the Build VI to build zip files
                              programmatically. To use the Zip VIs, you must know the relative path
                                  for every file you want to include in the zip file.
                3.  Explicitly include dynamically loaded VIs in the build specification.
                           If a VI loads other VIs dynamically using the VI Server or calls a dynamically loaded
                    VI through a Call By Reference or Start Asynchronous Call node, you must add those
                   VIs to the Always Included listbox on the Source Files page of the Properties
                  dialog box for your application.

               You also can distribute dynamically loaded VIs for an application by including them
                 within a source distribution.
                4.  Save the updated settings for your build specification. Click the OK button to
               update the build specification in the project and close the dialog box. The build
                   specification name appears in the project under Build Specifications. To save
               changes you make to a build specification, you must save the project that contains
                 the build specification.


          Building the Application

            Right-click the build specification name for the application you want to build, and select
          Build from the shortcut menu. You also can build an application programmatically using
          the Build VI or the ExecuteBuildSpec command line operation.

             NOTE
                You can preview your application to ensure that it appears correctly. From the
                 Preview page of the Properties dialog box for your application, click the Generate
                Preview button to review the generated files for your application.


           Distributing the Built Application

                1.  Ensure that the computer on which you want to run the application has access
                 to the LabVIEW Run-Time Engine. The LabVIEW Run-Time Engine must be installed
              on any computer on which users run an application or shared library. You can
                   distribute the LabVIEW Run-Time Engine with the application or shared library.
                (Windows) You also can include the LabVIEW Run-Time Engine in an installer.
                2.  Distribute legal information for your end user. If you use installers to distribute
                your applications, enter information for a custom license agreement on the Dialog
                 Information page of the Installer Properties dialog box. Review <National
            Instruments>\Legal Information.txt for information about including
                   legal information in installers built with NI products.
                3.  Refer to the following table for tips to assist you with distributing LabVIEW-
                  built applications.


1502  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1502 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1503 ordinal=1503 -->
## LabVIEW User Manual

LabVIEW User Manual


 Action                                                    Benefit

 To verify that the built application
 performs correctly, enable debugging by
 placing a checkmark in the Enable                               When you test a built application, you ensure Debugging checkbox on the Advanced                                            that behavior did not change between the page of the Properties dialog box for                                        development environment and the your application. You also can connect                                                       distribution environment. to a built application by selecting
 Operate»Debug Application or Shared
 Library.

 After you test your application, disable    Disabling debugging for VIs can reduce file size
 debugging for your VIs.                   and increase run-time performance.

                                      Most professional applications include an
 Create an About dialog box for a           About dialog box that provides general
 stand-alone application.                  information about the application, such as
                                             version, copyright, and support information.

                                When you distribute an application, dialog
                                      boxes and menus adopt the spoken language
                                                of the operating system on which the  If your end user has spoken language
                                          application runs, but the text and controls you requirements that differ from the
                                      implement remain in the language of the language of the original application,
                                        operating system on which you originally built adjust the default language settings for
                                                     the application. the application on the Run-Time
 Languages page of the Properties                                   By default, stand-alone application and shared
 dialog box for your application.                                              library build specifications provide support for
                                      Chinese (Simplified), English, French, German,
                                      Japanese, and Korean.

                                                                   If you try to run an application that requires  If your application uses the same VI                                            the VI Server at the same time as the Server port as another application,                                              conflicting application, the VI Server does not create a custom configuration file.                                           run, and LabVIEW does not provide a warning.

                                                                     If you need to ensure that the application
                                           always runs under certain LabVIEW
 Distribute a custom configuration file      environment settings, you can preserve and
 along with your built application.           redistribute those settings by distributing a
                                     custom configuration file, or preference file,
                                                  with your application.

Building a Universal Framework on macOS

A universal framework, or shared library, contains both 64-bit and 32-bit code so that both
64-bit and 32-bit applications can call the framework. You need both 64-bit and 32-bit
versions of LabVIEW to build a universal framework. Complete the following steps to build
a universal framework in LabVIEW:

   1.  Using 64-bit LabVIEW, build the framework that you want to make universal.
      LabVIEW builds the framework with 64-bit VI code.


                                                    © National Instruments Corporation 1503

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1503 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1504 ordinal=1504 -->
## LabVIEW User Manual

LabVIEW User Manual


                2.  Using 32-bit LabVIEW, build the same framework you built in the previous step.
               LabVIEW builds the framework with 32-bit VI code.
                3.  Navigate to the 32-bit framework on disk, and copy the .llb file from the 32-bit
               framework into the 64-bit framework you created in step 1. After you copy the .llb
                        file into the 64-bit framework, you no longer need the 32-bit framework you created
                   in step 2.
                  NOTE
                      You must copy the .llb file from the 32-bit framework into the 64-bit
                       framework. The framework does not work universally if you copy the .llb
                                  file from the 64-bit framework into the 32-bit framework.

         You can now call the framework you built in step 1 from both 32-bit and 64-bit
           applications.


          Related Information

           Building and Distributing Applications

        How to Build a Framework (Shared Library)

         Debugging Applications and Shared Libraries

       Creating Packages for Distribution

         You can create packages and deploy them to clients through NI Package Manager or
          SystemLink.

          Before creating packages, create a source distribution, packed project library, shared
            library,.NET assembly, or executable to include in your packages.

             NOTE
                You cannot distribute stand-alone VIs.

                1.  In the Project Explorer window, right-click Build Specifications and select
              New»Package.
                2.  In the Package Properties dialog box, under Information, enter the name you want
                  to use for your package in Package name. The package name must be all lowercase
              and contain no spaces. NI Package Manager and other packages use this name to
                 reference the package you create.
                3.  Under Destinations, set up any destination folders where you plan to install the
               package in the client.
                4.  Under Source Files, specify which files or build specification outputs you want to
                      install.
                5.  (Windows) Under Shortcuts, you can add a shortcut to the Startup menu if you
               want your application to run as soon as the system starts up. You can also add a


1504  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1504 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1505 ordinal=1505 -->
## LabVIEW User Manual

LabVIEW User Manual


       shortcut to the Desktop or Program Menu on Windows. By default, LabVIEW adds a
       shortcut in the Windows Program menu for each application included in the
      package.
   6.  Under Package, specify the display name and synopsis for your package. The
       display name is what users will see in the Package Manager or NI SystemLink when
      they install your package. The synopsis is the first line of the description that users
      see before they click on a package to see its full description.
   7.  Under Dependencies, specify dependencies on any currently installed packages.
           1.  Configure the relationship of the dependency. You can define a dependency
             as required, recommended, or suggested and specify version ranges.
           2.  To prompt the user to install your package when they install a related
            package, place a checkmark in the Include enhanced relationship
            checkbox.
   8.  Under Version Information, specify the version of your package and what version
      you want to display to the user. If you remove the display version, the user sees the
         full version in the Package Manager.
   9.  Under Advanced, set your package to run executables or scripts while it installs or
       uninstalls. For example, you can specify whether the process for installing or
       uninstalling the package waits for a certain action to complete.
   10. (Optional) Under Package Installer, place a checkmark in the Create a Package
       Installer checkbox to build your distribution into a package installer file (.exe.
   11. (Optional) Under Feed, choose whether to add your package to a local feed or
       publish the package to a feed on the SystemLink server.
   12. Click Build. A (Windows).nipkg file or (NI Linux Real-Time).ipk file appears in the
       destination you specified.

You can distribute the package to clients through Package Manager or SystemLink.
(Windows) Your clients can use Package Manager or SystemLink to subscribe to a feed to
find and install your packages. (NI Linux Real-Time) Your clients can install packages
through SystemLink or from the command line on the NI Linux Real-Time target. Package
Manager does not support.ipk files.

Configuring Run-Time Languages for Applications and
Shared Libraries

You can specify the language or languages to use with a stand-alone application or shared
library. By default, LabVIEW uses the same run-time language as Windows. If LabVIEW
cannot use the Windows run-time language or the platform is non-Windows, LabVIEW


                                                    © National Instruments Corporation 1505

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1505 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1506 ordinal=1506 -->
## LabVIEW User Manual

LabVIEW User Manual


           defaults to English. Change the default behavior by configuring the run-time language
           options.

             NOTE
                              •   Language settings are only available in the 32-bit version of LabVIEW.
                              •   LabVIEW localizes text for items such as default run-time menus, default
                  menu items for custom run-time menus, descriptions of error codes, and
                     LabVIEW dialog boxes. However, you must localize the text for items such as
                         captions and control descriptions.

         You can configure the run-time language options for a stand-alone application using the
           following methods. The methods appear in order of precedence.

                   •   Run the application with the –lang language command-line argument, where
                language is the English name of the language you want to use.
                   •   Add the following line to the configuration file for the application: AppLanguage=
                 language, where language is the English name of the language you want to use.
                 Modifying the configuration file for the application does not modify the project
                   settings.
                   •   (Windows) If you do not specify the language you want to use in the command line
                 or the configuration file of the application, the application uses the operating
                system language. Navigate to Control Panel»Regional and Language Options to
                view the language settings for the operating system. If the application does not
                support the operating system language, the application uses the default language
                    for the application.
                   •   Use the Default language option to configure the default language for the
                  application. In the Project Explorer window, right-click an application under Build
                  Specifications, select Properties from the shortcut menu, and navigate to the Run-
              Time Languages page of the Application Properties dialog box. If you previously hid
                 Build Specifications in the Project Explorer window, you must display the item
                 again to access it.
                   •   Use the Supported Languages option to configure the supported languages for an
                  application in the build specification. In the Project Explorer window, right-click an
                  application under Build Specifications, select Properties from the shortcut menu,
              and navigate to the Run-Time Languages page of the Application Properties dialog
               box to configure language options for the application. The Supported languages
                 option on the Run-Time Languages page lists all supported languages.

                 If you do not specify a language using the previous options, the application uses the first
           available supported language in alphabetical order. The Supported languages option on
          the Run-Time Languages page of the Application Properties dialog box lists all supported
          languages. If the application cannot use any of the supported languages because the
           required language files have been deleted, corrupted, or are not readable, LabVIEW cannot
          load the application.

             NOTE
               The LabVIEW Run-Time Engine is multilingual, so you do not have to include
                  multiple versions of it with an application, shared library, or installer in order to
                 use localized text.


1506  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1506 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1507 ordinal=1507 -->
## LabVIEW User Manual

LabVIEW User Manual


You can use the Application:Language property to determine the default language for an
application programmatically.

Use the Run-Time Languages page of the Shared Library Properties dialog box to configure
language options for a shared library.

Copying LabVIEW Work Environment Options

You can copy the options you set in the LabVIEW work environment to the stand-alone
application you build.

If you use a LabVIEW configuration file with the stand-alone application, you do not need
to manually copy LabVIEW work environment options. The Application Builder
automatically copies the options that you set in the LabVIEW work environment. If you use
a custom configuration file with the stand-alone application and the file does not contain
the LabVIEW work environment options you want, you can manually copy the entries that
specify the LabVIEW work environment options from the LabVIEW configuration file.

Complete the following steps to manually copy LabVIEW work environment options.

   1.  Open the LabVIEW configuration file. Refer to the following table for the name and
       location of the LabVIEW configuration file. In the following table, x is the LabVIEW
       version currently in use.

                                                             LabVIEW
 Platform                                                           Configuration
                                                                                      File
               LabVIEW x \labview.ini
     ~/Library/Preferences/LabVIEW.app x 64-bit
                   Preferences
    /home/<username>/natinst/.config/LabVIEW-
                        x /labview.conf

   2.  In the LabVIEW configuration file, copy the entries that specify the LabVIEW work
      environment options you want. The entries that specify the LabVIEW work
      environment options are in the following format: preference_name = value.
   3.  Paste the entries to the stand-alone application configuration file. Refer to the
       following table for the name of the stand-alone application configuration file. In the
       following table, myapp is the name of the stand-alone application and x is the
      LabVIEW version currently in use.

 Platform                           Stand-Alone Application Configuration File
        myapp .ini
   myapp .app x Preferences
       myapp .conf


                                                    © National Instruments Corporation 1507

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1507 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1508 ordinal=1508 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Save the stand-alone application configuration file.


          Related Information

        How LabVIEW Stores Options

       Creating an About Dialog Box for a Stand-Alone
       Application

         Most applications have an About dialog box that displays general information about the
           application and the user or company that designed it. You can create a VI that LabVIEW
          runs when a user selects Help»About to display information about the stand-alone
           application you create. After the VI runs, LabVIEW closes the dialog box.

         You can have only one About VI per application. If you do not supply an About VI, LabVIEW
           displays a default dialog box similar to the dialog box that appears in the LabVIEW
         development system when you select Help»About.

         Complete the following steps to create an About VI and include it in a stand-alone
           application.

                1.  Build a VI with a front panel window that contains the information you want to
                  display in the About dialog box, such as the version number, company name, and
                 copyright information. The About VI you create can share subVIs with other VIs you
                 include in the application. However, you cannot use the About VI as a subVI because
                 the About VI cannot run while other VIs in the application run.

             NOTE
               The front panel window must include a National Instruments copyright notice.
                   Refer to the National Instruments Software License Agreement located on the
                LabVIEW Platform media for more information about the requirements for any
               About dialog box you create for a LabVIEW application.

                1.  Build the block diagram of the About VI. For example, if you want the About dialog
               box to display until the user clicks a button, use a While Loop with an Event
                  structure on the block diagram.
                2.  Save the VI. The name of the VI must start with About.
                3.  Add the VI to the project from which you are building the application.
                4.  When you configure the application build settings, add the About VI to the Always
                Included list on the Source Files page of the Application Properties dialog box.
                5.  From the Source File Settings page, select the About VI in the Project Files tree. In
                 the Use default save settings section, make sure a checkmark does not appear in
                 the Remove front panel checkbox and that the destination is the application.
                6.  Configure the remaining application build settings and build the application.


1508  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1508 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1509 ordinal=1509 -->
## LabVIEW User Manual

LabVIEW User Manual


Enabling the Web Server in Stand-Alone Applications

To embed the front panel of a stand-alone application in an HTML document, enable and
configure the Web Server in a application as you would in a VI. Include the front panel of
the VI and the HTML file in the installation.

      NOTE
      When you build an application, on the Source File Settings page of the Application
        Properties dialog box, remove the checkmark from the Remove front panel
       checkbox for the VI you want to publish so that you can embed the front panel in
      an HTML document.

After you generate the application, the output folder contains both an .ini configuration
file and a niwebserver.conf configuration file.

In the .ini file, add the line WebServer.Enabled=True if it does not already exist.
You also can copy the WebServer* preferences from the LabVIEW INI file for the LabVIEW
development system to the .ini file for the application. You may need to modify these
preferences to be appropriate for the application.

      Note When running the application, make sure no other application, including the
                LabVIEW development environment, uses the same port.

Use the niwebserver.conf file to configure other Web Server functionality in the
application, such as the root directory of the Web Server.

Retrieving Application and Shared Library Versions
Programmatically (Windows)

You can use the fileVersionInfo.llb located in the labview\vi.lib
\Platform directory to retrieve the version information of a stand-alone application or
shared library programmatically. The VI is not available on the Functions palette.

      NOTE
      The LabVIEW Professional Development System includes the Application Builder. If
       you use the LabVIEW Base Development System or Full Development System, you
       can purchase the Application Builder separately by visiting the National
       Instruments Web site.

Complete the following steps to retrieve the version information of an application or
shared library programmatically.

   1.  In the FileVersionInfo VI, the top-level VI of the LLB, specify in the Application path
       in path control the location on disk of the application or shared library whose
       version information you want to retrieve.


                                                    © National Instruments Corporation 1509

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1509 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1510 ordinal=1510 -->
## LabVIEW User Manual

LabVIEW User Manual


                2.  Run the VI.

         LabVIEW returns the version information in the File Version Info and FileVersionInfo Out
            indicators.

      Using a Configuration File with a Stand-Alone
       Application

         You can use a LabVIEW configuration file or another, custom, configuration file with a
         LabVIEW stand-alone application.


         LabVIEW Configuration Files

                 If you select to use the LabVIEW configuration file with a stand-alone application, LabVIEW
           creates a configuration file that includes a subset of the configuration tokens that appear
            in the LabVIEW configuration file in the labview directory. You can configure additional
           build specification settings using the Application Properties dialog box. For example, if you
            select Enable debugging from the Advanced page of the Application Properties dialog
           box, LabVIEW adds debugging tokens to the configuration file of the stand-alone
           application.

         Complete the following steps to use the LabVIEW configuration file in a stand-alone
           application.

                1.  In the Project Explorer window, right-click Build Specifications and select
               New»Application from the shortcut menu. If you previously created a build
                   specification for the application, double-click the build in the Project Explorer
              window to edit the build.
                2.  On the Advanced page of the Application Properties dialog box, ensure that the
              Use custom configuration file checkbox is not enabled.
                3.  (Optional) Make other selections on the Advanced page. Some of these changes
              add configuration tokens to the configuration file of the stand-alone application.
                4.  Click the OK button to apply the changes and close the dialog box.


        Custom Configuration Files

                 If you use a custom configuration file with a stand-alone application, LabVIEW uses the
           configuration file you specify as a template. LabVIEW adds additional tokens to the
           configuration file you specify depending on the options you select in the Application
          Properties dialog box. For example, if you select Enable debugging from the Advanced
         page of the Application Properties dialog box, LabVIEW adds debugging tokens to the
         custom configuration file you included.

         Complete the following steps to use a custom configuration file in a stand-alone
           application.


1510  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1510 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1511 ordinal=1511 -->
## LabVIEW User Manual

LabVIEW User Manual


   1.  In the Project Explorer window, right-click Build Specifications and select
      New»Application from the shortcut menu. If you previously created a build
       specification for the application, double-click the build in the Project Explorer
     window to edit the build.
   2.  On the Advanced page of the Application Properties dialog box, place a
      checkmark in the Use custom configuration file checkbox. The Select Project File
       dialog box appears.
   3.  Select the configuration file you want to include from the Files in Project list. If the
         file you want to include is not in the project, complete the following steps.
           1.  Click the Add button. A file dialog box appears.
           2.  Browse to the file you want to include and click the Add button. The dialog
            boxes close and the file you selected appears in the Configuration file in
             project text box on the Advanced page of the Application Properties dialog
             box.
   4.  (Optional) Make other selections on the Advanced page. Some of these changes
     add configuration tokens to the custom configuration file.
   5.  Click the OK button to apply the changes and close the dialog box.

Characteristics of LabVIEW-Built .NET Framework
Assemblies

      NOTE
      The following content applies to .NET Framework only. Prior to LabVIEW 2025
       Q1, .NET Framework Assemblies were called .NET Interop Assemblies.


Calling a .NET Framework Assembly from Another Program

After you build a .NET Framework assembly, you can call the assembly from other
programs that support .NET. However, ensure that the computer on which the other
program runs meets the following requirements and recommendations:

    •   The LabVIEW Run-Time Engine must be installed on any computer on which users
      run the .NET Framework assembly. You can distribute the LabVIEW Run-Time Engine
      with the .NET Framework assembly. (Windows) You also can include the LabVIEW
      Run-Time Engine in an installer.
    •   National Instruments recommends that the target computer for the .NET
      Framework assembly have the same or later version of the .NET Framework
       installed as the version that LabVIEW used to build the application.
    •   To call the .NET Framework assembly outside of the LabVIEW development
      environment, you must reference
     NationalInstruments.LabVIEW.Interop.dll in the Microsoft Visual
      Studio project. The LabVIEW Run-Time Engine automatically installs this DLL to the
     National Instruments\Shared\LabVIEW Run-Time directory.
       Optionally, you can manually install
     NationalInstruments.LabVIEW.Interop.dll to the Global Assembly


                                                    © National Instruments Corporation 1511

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1511 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1512 ordinal=1512 -->
## LabVIEW User Manual

LabVIEW User Manual


               Cache (GAC). If you want to install this DLL to the GAC, you must sign the .NET
               assembly with a strong name key file.
                   •  When you create a debuggable .NET Framework assembly, LabVIEW places a
                  configuration (ini) file in the same directory as the assembly. If you want to debug
                 the assembly in other programs, you must distribute the .ini file with the
                assembly.


         LabVIEW Data Types in.NET Framework Assemblies

        When you build a .NET Framework assembly, LabVIEW directly translates simple data types
          such as numerics, booleans, strings, and arrays of simple data types to the
          corresponding .NET data type. However, LabVIEW-specific data types, such as clusters,
          waveforms, complex numbers, refnums, and LabVIEW classes, require LabVIEW to define
        new .NET data types in the generated assembly.

        One way to determine how LabVIEW converts its own data types to .NET data types is to
           build the .NET Framework assembly and then view the manifest of the assembly in a .NET
         programming environment such as Microsoft Visual Studio. You can also use the MSIL
          Disassembler tool available on the Microsoft Developer Network (MSDN) to view the
          generated assembly. However, the following sections explain some basic details about how
         LabVIEW converts clusters, enumeration type controls, and LabVIEW classes to .NET data
           types.


           Clusters and Enumerations

         LabVIEW converts clusters and enumerations to .NET structures whose elements
          correspond to the elements of the cluster or enumeration. LabVIEW uses the following
           rules to name the .NET structure that corresponds to a cluster or enumeration:

                   •   Clusters and enumerations defined as type definitions or strict type definitions—
               LabVIEW uses the label of the type definition or strict type definition as the name of
                 the .NET structure
                   •    All other clusters and enumerations—LabVIEW names the .NET structure
                 LVCluster_# or LVEnum_#


         LabVIEW Classes

         You can export the member VIs of a LabVIEW class. In LabVIEW, these VIs require the
         owning LabVIEW class as an input. Therefore, when you export these VIs to a .NET
         Framework assembly, LabVIEW must create an equivalent .NET class definition in the
          assembly. The .NET class definition contains a static method for each member VI. Each of
          these static methods requires an instance of the newly defined .NET class as a parameter.
         LabVIEW does not export the private data of the owning LabVIEW class.

         LabVIEW also exports the inheritance structure of LabVIEW classes whose method VIs you
           export. The generated.NET classes have the same inheritance structure.


1512  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1512 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1513 ordinal=1513 -->
## LabVIEW User Manual

LabVIEW User Manual


LabVIEW Errors

When LabVIEW generates a .NET method for a VI, LabVIEW does not export the error in and
error out clusters as parameters of the new method. Instead, the new method throws
a .NET exception if an error occurs while the method is executing. This exception contains
the same information as the error cluster.

Characteristics of LabVIEW-Built Shared Libraries

None


LVDLLStatus Function

All DLLs built from LabVIEW, in addition to the functions you export, contain an exported
function called LVDLLStatus, with the following prototype:

MgErr LVDLLStatus(CStr errStr, int32 errStrLen, void *module)
The calling program uses this function to verify that the LabVIEW DLL loaded correctly. If an
error occurs while loading the DLL, the function returns the error. Pass a string buffer to the
errStr parameter to receive additional information about the error. Set the errStrLen
parameter to the number of bytes in the string buffer passed as errStr. You can use the
module parameter to retrieve the handle to the LabVIEW Run-Time Engine being used by
the DLL. Typically, you can leave this parameter as NULL.

The LVDLLStatus function blocks the execution if LabVIEW calls this function while the
LabVIEW Run-Time Engine is still loading.

      NOTE
            If you call a LabVIEW-built DLL from within LabVIEW, LabVIEW automatically calls
       the LVDLLStatus function for you.


SetExecuteVIsInPrivateExecutionSystem Function

All DLLs built from LabVIEW, in addition to the functions you export, contain an exported
function called SetExecuteVIsInPrivateExecutionSystem, with the following
prototype:

Void SetExecuteVIsInPrivateExecutionSystem(Bool32 value)
Use this function to specify whether LabVIEW executes VIs in a multithreaded execution
system when you call LabVIEW-built shared libraries to applications in other languages. If
you pass 1 to the value parameter, LabVIEW executes VIs in a multithreaded execution
system when you call LabVIEW-built shared libraries to applications in other languages. If
you call this function, the value parameter of this function overrides the value of the
Execute VIs in private execution system checkbox in the Advanced page of the Shared
Library Properties Dialog Box.


                                                    © National Instruments Corporation 1513

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1513 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1514 ordinal=1514 -->
## LabVIEW User Manual

LabVIEW User Manual


         (macOS) To build part of a shared library in LabVIEW, Application Builder must use gcc, the
          standard command-line compiler for Unix and macOS operating systems. Use Xcode, the
          standard development environment for Apple computers, to install gcc. You can download
         Xcode for free from the Mac App Store.


        Memory Allocation

         To manage memory allocation for LabVIEW array types exposed as handles, the LabVIEW-
            built shared library provides Allocate, Deallocate, and Resize functions for each
           array type exposed as a handle. Open the generated header file to view the function
          prototypes specific to the generated shared library.

      Caching Installer Distribution Components (Windows)

         A distribution is a collection of files that form an installer. When you use the Application
           Builder to build an installer that contains additional installers or components, the
           Application Builder prompts you to locate the original distribution for the components.
          Caching installer distribution components copies them into a permanent location on the
            local system and eliminates the need to specify a location for the additional components
          each time you build the installer. The next time you build an installer that includes these
         components, the Application Builder automatically copies the components from your local
           drive instead of prompting you for a distribution media.

         Complete the following steps to cache installer distribution components:

                1.  Right-click Build Specifications from the Project Explorer window and select
                New»Installer from the shortcut menu.
                2.  Select Additional Installers from the Category list.
                3.  Place a checkmark in the To minimize media prompts while building your
                   installers, copy the selected installers and all future installers to this computer
                checkbox.
                4.  Click OK.

             NOTE
               The LabVIEW Professional Development System includes the Application Builder. If
                you use the LabVIEW Base Development System or Full Development System, you
                can purchase the Application Builder separately from ni.com.

      Caveats and Recommendations for Building Installers

         The following list describes some of the caveats and recommendations to consider when
         you build an installer.

                   •  When you select files to include in the installer build from the Source Files page of
                 the Installer Properties dialog box, you cannot select part of a build specification.
               You must include build specifications as a whole. The entire specification appears in
                 the Destination View tree.


1514  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1514 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1515 ordinal=1515 -->
## LabVIEW User Manual

LabVIEW User Manual


•     If you want to include a project library in the installer build, make sure the project
    library does not include files on a network or other files with links that will break if
   moved. You cannot copy a project library from the Project Files View directory to
    the Destination View directory if any of the files are on different drives, or if the files
   do not share a common path with the LabVIEW project file .lvproj.
•   Consider building a source distribution that contains the files you want to include in
   an installer build, to reduce the possibility of broken links for files on networks or
    different drives.
•  When you add a National Instruments product installer to the installer build, the
    drivers and components for NI products that you include in the installer contain
    only those features that are installed on the computer on which you build the
     installer. For example, if you have only 10 of a possible 20 features of an NI product
    installed on the build computer and then select to include the full version of that
    product in the installer, the installer will include only the 10 features installed on the
    build computer, not all 20 features available for that product. It is possible for an
     installer you create to uninstall components on the computer on which it is installed
    without reinstalling current versions of those components. This behavior depends
   on the NI products installed on the build computer and those installed on the
   computer on which you run the installer. If the computer on which you run the
     installer has an NI product installed that is not installed on the build computer, that
    product may be removed during the installation. The installer displays information
    to you that explains what features will be removed as part of the installation before
    uninstalling any components and gives you the option to stop the installation.
•   You can include custom error codes in the installer. The [LabVIEW x Run-
   Time] folder in the Destination View directory corresponds to the Shared
   \LabVIEW Run-Time\x.x directory, where xx is the LabVIEW version currently
    in use. If you place a checkmark in the Install custom error code files checkbox on
    the Advanced page, the installer build includes all error code files from labview
   \project\errors and labview\user.lib\errors and installs them in
    the Shared\LabVIEW Run-Time\x.x\errors directory.

    NOTE
    You must manually create an errors folder in the labview\user.lib
     directory to organize your error code files.

•     If you receive an out of memory error when building an application for an installer
    build, consider one of the following solutions:
        ◦     If the application includes large or complex VIs, lower the complexity
          threshold at which LabVIEW prioritizes editor responsiveness over execution
          speed. This change allows LabVIEW to devote more memory to the build
           process.
        ◦   Reduce the number of VIs in your application by dividing portions of the
           application into separate source distributions. The VIs in the application use
          the Call By Reference node to call separate portions.
•  When you test a stand-alone application, shared library,.NET assembly, or Web
    service for an installer build, if the load time takes longer than you expect, remove
    portions of the VIs that other VIs call dynamically once or occasionally. For example,
      if an application has a configuration dialog box that consists of many VIs and the
    user has to choose to load the dialog box, use the VI Call Configuration dialog box to
    configure when the subVI loads by selecting the Reload for each call option. When


                                                 © National Instruments Corporation 1515

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1515 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1516 ordinal=1516 -->
## LabVIEW User Manual

LabVIEW User Manual


               you create applications, shared libraries, and.NET assemblies, modify the build so
                  that it has additional destinations. To reduce load time, configure the VIs that you
                     call dynamically to go into those additional destinations, rather than the main
                  application or shared library.
                   •   Use the [LabVIEW x] folder in the Destination View directory to add files to
                     install in the directory of the latest version of LabVIEW that the user has installed.
                         ◦     If you include the build specification for any type of application within an
                              installer, ensure that the build output of the build specification is relative to
                       the primary destination of the build specification. The primary destination is
                         specified on the Destination page of the Properties dialog box for the
                         application. If the build output includes any files that are not relative to its
                      primary destination, the installer will reorganize the original file hierarchy of
                       the application. In particular, the installer will move any files that are not
                           relative into the primary destination.
                   •   You do not need additional license files when using LabVIEW distribution
               components with LabVIEW-built applications.
                   •  When you add a build specification to a folder in the Destination View tree of the
                Source Files page of the Installer Properties dialog box, the name of the build
                appears in the Destination View tree, even though a folder with the name of the
                  build does not exist.

       Including Additional National Instruments Installers in
      an Installer Build

        When you build an installer, you might need to include installers for devices or other
           National Instruments products in the installer build. For example, if you build an installer
            for a stand-alone application or shared library that uses the Storage/DataPlugin VIs, you
         must include the NI USI installer. By default, LabVIEW automatically adds installers for the
           National Instruments products that you installed on the computer you are using.

              CAUTION
              When you add a National Instruments product installer to the installer build, you
                  are adding only the components of the installer that you installed on the computer
                you are using. When users run the installer you built, the installer might remove
               components of the product from the user computer that are not part of the
                       installer. To minimize the risk of removing product components on user
                 computers, ensure you have a complete and up-to-date installation of the product
               on the computer you are using, including all optional components, before you add
                  the product installer to the build.


         Manually Selecting Additional Installers

         To prevent LabVIEW from selecting installers automatically, remove the checkmark from
          the Automatically select recommended installers checkbox on the Additional Installers
         page of the Installer Properties dialog box for your installer. You can then select the
            installers you want to include with your installer from the National Instruments Installers
          to Include list. This list might include but is not limited to the following installers:


1516  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1516 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1517 ordinal=1517 -->
## LabVIEW User Manual

LabVIEW User Manual


•   NI LabVIEW Run-Time Engine —Include this installer with applications and shared
     libraries. The LabVIEW Run-Time Engine includes 3D graph support and NI Reports,
   which provides support for generating LabVIEW reports in applications and shared
     libraries. You can specify whether to include the following components of the
   LabVIEW Run-Time Engine:
        ◦  Math Kernel Libraries —Include this component for algorithms the Analysis
            VIs use for specific processors.
        ◦   NI ActiveX Container —Include this component to distribute NI ActiveX
           objects, properties, methods, and events with an installer.
        ◦   NI Error Reporting —Include this component to detect application crashes
         and internal warnings. Enabling this component also allows you to create
           reports on disk that contain memory dumps and log files that can help you
          troubleshoot an issue.
        ◦   NI LabVIEW Real-Time NBFifo —Include this component when using
         LabVIEW Real-Time FIFOs on desktop computers.
        ◦   NI LabVIEW Run-Time Engine Non-English Support —Include this
         component to make sure that the LabVIEW Run-Time Engine reports error
         messages in the language of the operating system on which you run an
           application type.
        ◦   NI LabVIEW Run-Time Engine Web Server —Include this component when
          using the Web Server for stand-alone applications and shared libraries.
        ◦   NI System Web Server —Include this component when using Web services
           to communicate between National Instruments software, such as LabVIEW
         and NI Measurement & Automation Explorer.
        ◦   NI Logos 5.4 —Include this component for the network protocol that uses
          network-published shared variables.
        ◦   NI TDM Streaming —Include this component when using TDMS VIs to
         perform file I/O operations.
        ◦   NI VC2008MSMs —Include this component to install Microsoft Visual C++
         Runtime to load and run the LabVIEW Run-Time Engine on computers where
          the Microsoft Visual C++ Runtime has not been previously installed.
        ◦   NI VC2010MSMs —This component installs Microsoft Visual C++ Runtime to
          load and run the LabVIEW Run-Time Engine with .NET Framework support.
          Include this component on computers where the LabVIEW Run-Time Engine
         has not been previously installed.
•   NI LabWindows/CVI; Run-Time Engine —Include this installer with shared libraries
    (DLLs) built in LabWindows™/CVI™.
•   NI USI —Include this installer if the application or shared library uses the Storage/
    DataPlugin VIs.
•   NI LabVIEW DSC Module Runtime —Include this installer if the application or
    shared library uses LabVIEW DSC Module features, including security, alarming, and
    logging.
•   NI DataSocket —Include this installer if the application or shared library uses
    DataSocket. Includes the DataSocket Server, DataSocket Server Manager, and OPC
   Demo Server.
•   NI Measurement & Automation Explorer —Include this installer to configure, test,
   and communicate with National Instruments hardware.


                                                 © National Instruments Corporation 1517

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1517 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1518 ordinal=1518 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   NI TDM Excel Add-In —Include this installer to load .tdm and .tdms files from
                  Microsoft Excel.
                   •   NI Distributed System Manager —Include this installer to create and monitor
                   variables, processes, I/O servers, and Web services, as well as to interact with the
               Shared Variable Engine and manage security and aliases.
                   •   NI Variable Engine —Include this installer for applications in which you want to
                  host, configure, or create shared variables and for applications that read and write
                     live data using shared variables.
                   •   NI Web-based Configuration & Monitoring —Include this installer if you want to
                use NI Web-based Configuration & Monitoring, which allows you to configure and
                  control the Application Web Server, as well as remote devices, such as RT targets.

        Installing LabVIEW-Built Installers Silently

             NOTE
                LabVIEW can build two types of installers: Installer and Package. You can choose to
                   build either of them in Build Specification. For differences between the two types
                   of installers, refer to Using Build Specifications.
                To install a Package, refer to Automating an Installer in Package Manager User
                 Manual.

                To install an Installer silently, refer to the following content.

         You can use the command line window to install LabVIEW-built installers silently. If you use
          the command line window to install a LabVIEW-built installer silently, consider the size of
          the installer. Because the installer does not display a progress bar during installation, it
        may be difficult to determine the progress of the installer. Therefore, a larger installer will
           take more time, and you will not be able to determine how much longer the installer will
           run.

         Complete the following steps to install a LabVIEW-built installer silently.

                1.  Create a LabVIEW-built installer for the LabVIEW-built application.
                2.  Open the command line window.
                3.  Enter the following command to run the installer silently.
            path \install.exe /q /acceptlicenses yes, where path is the path
                  to install.exe.

                           If you have customized the installer name in the installer properties, make sure you
                 replace the install.exe with your installer name.


1518  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1518 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1519 ordinal=1519 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
            If your LabVIEW version does not support customizing the installer name, the
         installer name is setup.exe. You should use the following command: path
      \setup.exe /q /acceptlicenses yes.

      RELATED INFORMATION
       Using Build Specifications on page 390
       Automating an Installer

Uninstalling LabVIEW-Built Installers

You can use the command line window to uninstall a LabVIEW-built installer and the files it
installs. Complete the following steps to uninstall a LabVIEW-built installer.

   1.  Open the command line window and change to the directory containing the
       NIUninstaller, or the uninst.exe file. The uninst.exe file is in the
     C:\Program Files\National Instruments\Shared
     \NIUninstaller directory (Windows 64-bit) C:\Program Files
     (x86)\National Instruments\Shared\NIUninstaller.
   2.  Enter the following command to uninstall the installer. uninst.exe /qb /x "
     product name " where product name is the name of the product you want
       to uninstall.

      NOTE
      product name  is case insensitive. Use the product name that appears in the
       Programs applet in the Control Panel to ensure the correct name. Also, enclose a
       product name that contains spaces in quotation marks.

You can also uninstall a LabVIEW-built installer using the Programs applet in the Control
Panel. Uninstalling the installer using the Programs applet does not remove NI
components that were installed with the installer. You must uninstall the NI components
separately.

Using the TDM Excel Add-In (Windows)

Use the TDM Excel Add-In to load .tdm and .tdms files into Microsoft Excel. From a
toolbar in Excel, choose which properties load into Excel at the file, group, and channel
levels, including custom properties.

Refer to Editing TDM(S) files with the TDM Excel Add-In on ni.com for more information
about the TDM Excel Add-In.

      RELATED INFORMATION
        Editing TDM(S) files with the TDM Excel Add-In


                                                    © National Instruments Corporation 1519

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1519 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1520 ordinal=1520 -->
## LabVIEW User Manual

LabVIEW User Manual


      Working with the Application Manifest

           Microsoft highly recommends that the requested execution level of an application be
        asInvoker. Therefore, asInvoker is the default requested execution level for all
          LabVIEW-built applications. However, there might be occasions where you cannot adhere
           to this recommendation. Complete the following steps to edit the manifest for a stand-
          alone application,.NET interop assembly, or shared library.


          Editing the Application Manifest

                1.  You must verify that you have installed mt.exe on the computer before you can
                   edit the manifest. Use mt.exe to interact with the manifest using command-line
                arguments. If mt.exe is not on the computer, download the Software
               Development Kit from the Microsoft website.
                2.  To edit the manifest, you must first retrieve it. Complete the following steps to
                   retrieve the manifest.
                        1.  Open the command line window.
                       NOTE
                       On most Windows operating systems, you can access the command
                                    line window by selecting Start»Run, entering cmd in the Open text
                           box and clicking the OK button.
                        2.  Enter the following command to retrieve the manifest: mt.exe -
                 inputresource: directory path \ Application Name .exe -out:
                        Application Name .manifest in the command line window where
                         directory path is the path to the built application and Application Name is
                       the name of the application.
          Note If mt.exe is not in the same directory as the application whose manifest you want
                  to retrieve, you must specify the path to mt.exe in the previous command.

                        3.  Press the <Enter> key to run the command. The application manifest with
                       the file extension .manifest appears in the same directory as the
                         application.
                3.  Complete the following steps to edit the manifest.
                        1.  Right-click the manifest in the destination folder and open the file in a text
                         editor or an XML editor.
                        2.  Locate the code <requestedExecutionLevel
                 level="asInvoker" uiAccess="false"/>. Change the value
                 asInvoker to requireAdministrator or highestAvailable
                     depending on the execution level you want the built application to have.
                        3.  Save the manifest file.


1520  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1520 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1521 ordinal=1521 -->
## LabVIEW User Manual

LabVIEW User Manual


Validating the Application Manifest

The tags within the application manifest are case sensitive. It is good practice to validate
the changes you make to the manifest after you edit it. However, validating the manifest
does not find spelling errors. Complete the following steps to validate the manifest.

   1.  In the command line window, enter the following command to validate the
       manifest: mt.exe -manifest Application Name.manifest -
     validate_manifest in the command line window where Application Name is
      the name of the application.
   2.  Press the <Enter> key to run the command.


Embedding the Application Manifest

After you edit and validate the application manifest, you can embed the changes when you
configure the settings for a stand-alone application, .NET Framework assembly, or shared
library.

   1.  On the Windows Security page of the Properties dialog box, place a checkmark in
      the Embed Manifest File checkbox.
   2.  Specify the manifest file using the Select Project File dialog box.

You also can embed the manifest without using the Windows Security page. Complete the
following steps to embed the manifest using the command line window.

   1.  In the command line window, enter the command mt.exe -manifest
     Application Name.manifest -outputresource: directory path
     \Application Name.exe;#1, where directory path is the path to the built
       application and Application Name is the name of the application.
   2.  Press the <Enter> key to run the command.

Running Operations Using the Command Line Interface
for LabVIEW

You can run a predefined set of operations in LabVIEW by executing commands using the
command line interface (CLI) for LabVIEW. For example, use the CLI for LabVIEW to
automate the build process of LabVIEW applications. You can also run custom operations
that you create in LabVIEW.

      NOTE
      The CLI for LabVIEW is available as a separate package. Refer to the NI website for
      more information about downloading the CLI for LabVIEW and compatible
        versions of LabVIEW.


                                                    © National Instruments Corporation 1521

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1521 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1522 ordinal=1522 -->
## LabVIEW User Manual

LabVIEW User Manual


          Before running an operation using the CLI for LabVIEW, configure LabVIEW to communicate
          with the CLI for LabVIEW by selecting Tools»Options»VI Server and placing a checkmark in
          the TCP/IP checkbox.

         To run an operation using the CLI for LabVIEW, execute a command with one or more of the
           following arguments. Required arguments are in bold.


                                 Note All the arguments are case-sensitive.


                  Tip To learn more about getting started using the CLI for LabVIEW, execute the
               LabVIEWCLI -Help command. To learn more about a specific operation, execute the
           LabVIEWCLI -OperationName < operation name > -Help command.
                 For example, execute the LabVIEWCLI -OperationName RunVI -Help
                       command to learn more about the RunVI operation.


          Argument                                                          Description

                                                 Runs the specified operation. If the operation has additi           LabVIEWCLI -OperationName                                                     arguments, append the arguments after the operation na

                                                             Specifies the directory that stores the necessary files for
                                                          operation. This argument is required only if you run a cus
                                                    operation and the necessary files for the operation are not s
                                                        one of the following default directories:
                                                                                 •     (Windows) C:\Program Files (x86)\Nati
        -AdditionalOperationDirectory      Instruments\Shared\LabVIEW CLI\Opera
                                                                                 •            (macOS) /Library/Application
                                              Support/National Instruments/LabV
                                                         CLI/Operations
                                                                                 •   (Linux) /usr/local/natinst/nilvcli/Oper

                                                            Specifies the LabVIEW version to use to run the operation
                                              argument is required on macOS and Linux but optional on W        -LabVIEWPath                                        On Windows, the default value is the version of LabVIEW th
                                                          most recently used on the machine.

                                                          Specifies the port of the VI server. This argument is require        -PortNumber                                                      port number under Tools»Options»VI Server»TCP/IP is no

                                                         Specifies the path of the CLI for LabVIEW log file. The default        -LogFilePath                                                                  the path to the temporary location.


1522  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1522 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1523 ordinal=1523 -->
## LabVIEW User Manual

LabVIEW User Manual


 Argument                                                          Description

                                             Specifies whether to save the output to both the console and
                                                                  file. The value for this argument must be one of the follow
                                                                  •                               true
 -LogToConsole                                                                  •                                  false

                                                     The default value is true.

                                               Specifies the level of details to include in the log file. The va
                                                              this argument must be one of the following:
                                                                  •                          Minimal
                                                                  •                              Default
 -Verbosity                                                                  •                             Detailed
                                                                  •                           Diagnostic

                                                    The default value is Default.

Creating Custom Command Line Operations

To create a custom command line operation to run in the command line interface (CLI) for
LabVIEW, complete the following tasks:

    •   Part 1 : Define the operation name.
    •   Part 2 : Define the operation behavior.
    •   Part 3 (Optional): Define the help for the operation.


Part 1: Defining the Operation Name

In the CLI for LabVIEW, command line operations have a parent class and each operation is
built from a child class of the parent class. To define the name of the operation, you must
create a child class of the parent class and specify the name of the child class.

Complete the following steps to define the name of the operation:

   1.  Navigate to one of the following directories:
             •   (Windows) C:\Program Files (x86)\National Instruments
         \Shared\LabVIEW CLI\Operations
             •   (macOS) /Library/Application Support/National
         Instruments/LabVIEW CLI/Operations
             •   (Linux) /usr/local/natinst/nilvcli/Operations


                                                    © National Instruments Corporation 1523

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1523 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1524 ordinal=1524 -->
## LabVIEW User Manual

LabVIEW User Manual


                2.  Open Operations.lvproj or Toolkit-Operations.lvproj, depending
              on whether the operation requires the LabVIEW development system only or
                  additional LabVIEW modules and toolkits.
                  NOTE
                      To open Toolkit-Operations.lvproj, you must install the
                         following toolkits and library:
                                        •   LabVIEW VI Analyzer Toolkit
                                        •   LabVIEW Unit Test Framework Toolkit
                                        •   UTF JUnit Report library—Install this library using the JKI VI Package
                           Manager (VIPM) software.
                3.  Right-click My Computer and select New»Class.
                4.  In the New Class window, specify the name of the class, such as AddTwoNumbers.
               The class name is the name of the operation you are creating.
                5.  In the project tree, right-click the class that you created and select Properties.
                6.  On the Inheritance page, click Change Parent Class.
                7.  Select CoreOperation.lvclass, click Inherit from Selected, and click OK.


          Part 2: Defining the Operation Behavior

         To define the behavior of the operation, you must override the methods of the class you
          created in the previous section and add code in one of the overridden methods.

         Complete the following steps to define the behavior of the operation:

                1.  In the project tree, right-click the class that you created in the previous section and
                   select New»VI for Override.
                2.  In the New Override window, select GetHelp.vi and RunOperation.vi, and
                    click OK.
                3.  Save the project. When prompted, save the class and the overridden methods in a
                  folder with the same name as the operation.

           Note NI recommends that you put the folder in one of the following directories so that
                      you do not need to specify the path to the folder using the
           −AdditionalOperationDirectory argument when running the operation.
                    •              (Windows) C:\Program Files (x86)\National
                    Instruments\Shared\LabVIEW CLI\Operations
                    •           (macOS) /Library/Application Support/National
                        Instruments/LabVIEW CLI/Operations
                    •              (Linux) /usr/local/natinst/nilvcli/Operations
                4.  Open the block diagram of the RunOperation.vi method.
                5.  Remove and rewire the subVI.


1524  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1524 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1525 ordinal=1525 -->
## LabVIEW User Manual

LabVIEW User Manual


   6.  Add code to define the behavior of the operation and save your changes. Do not
      modify the connector pane, as illustrated in the following figure.


 Terminal                        Data Type                           Description

            LabVIEW object of the class that you created in the previous
                                         section.

          Arguments that users enter in the CLI for LabVIEW when running
              this operation. Each string in the array represents an argument.

            LabVIEW object of the class that you created in the previous
                                         section.

         A code that the CLI for LabVIEW returns to the calling application,
          such as a Jenkins application. For example, you can configure the
            CLI for LabVIEW to return 0 if the operation runs successfully and
                                   -1 if an error occurs.

          Output of the operation or error messages to display in the CLI for
                   LabVIEW console or to save to the log file.

       Refer to RunOperation.vi in one of the following directories for an example of
       defining the behavior of the AddTwoNumbers operation, which adds two input
     numbers and returns the sum in the output.
             •   (Windows) C:\Users\Public\Documents\National
         Instruments\LabVIEW CLI\Examples\AddTwoNumbers
             •   (macOS) /Library/Application Support/National
         Instruments/LabVIEW CLI/Examples/AddTwoNumbers
             •   (Linux) /usr/local/natinst/nilvcli/Examples/
         AddTwoNumbers


Part 3: Defining the Help for the Operation

To help users get started using the operation, you can document the operation by
modifying the GetHelp.vi method that you created in the previous section. Users can
then access the documentation by executing the LabVIEWCLI -OperationName <
operation name > -Help command.

Complete the following steps to document the operation:

   1.  Open the GetHelp.vi method from the project tree.
   2.  On the front panel, create a string control named Help and enter the
      documentation in this control.


                                                    © National Instruments Corporation 1525

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1525 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1526 ordinal=1526 -->
## LabVIEW User Manual

LabVIEW User Manual


                3.  Right-click the Help control and select Data Operation»Make Current Value
                Default to set the current text as the default value of this control. Repeat this step
               each time you edit the text.
                4.  On the block diagram, remove and rewire the subVI.
                5.  Wire the objects in the following way, where AddTwoNumbers is the operation


               name, and save your changes.

      Changing the Default Ports for TCP-Based NI-PSP (NI
       Linux Real-Time, Windows)

         Complete the following steps to create the LogosXT.ini file and use it to modify TCP ports NI
           Publish-Subscribe Protocol (NI-PSP) checks for availability.

                1.  Create a new text document in the appropriate directory for your operating system:
             Windows Directory
                        1.  Configure Windows to show all hidden folders.
                        2.  Navigate to the \National Instruments\Logos XT subfolder in the common
                        application directory. The location of this directory depends on how you
                       configured the installation of LabVIEW. The default location is
                       C:\ProgramData\National Instruments\Logos XT. Create this subfolder if it
                     does not exist.
                        3.  Create a new text document.
                        4.  Name the new text document LogosXT.ini and place it in the Logos XT
                         subfolder.

                NI Linux Real-Time Directory
                        1.  Log in to the RT target with administrator privileges.
                        2.  Navigate to the /etc/natinst/ directory.
                        3.  Create a new text document.
                        4.  Name the new text document LogosXT.ini
                       NOTE
                          The file system is case-sensitive.
                2.  Open LogosXT.ini and enter the following text. [LogosXT] LogosXT_PortBase = 59110
               LogosXT_NumPortsToCheck = 100

            Note LogosXT_PortBase specifies the port where the NI-PSP protocol begins to check
                 availability. LogosXT_NumPortsToCheck specifies the maximum number of ports the
             protocol checks. By default, NI-PSP begins checking port availability at port 59110 and
                                   checks a maximum of 100 ports.


1526  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1526 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1527 ordinal=1527 -->
## LabVIEW User Manual

LabVIEW User Manual


   3.  To modify the first port the NI-PSP protocol checks for availability, delete 59110 and
       enter a different port number for LogosXT_PortBase. To modify the maximum
     number of ports the NI-PSP protocol checks for availability, delete 100 and enter a
       different number for LogosXT_NumPortsToCheck.
   4.  Save and close LogosXT.ini. The changes take effect when you restart LabVIEW.

JSONP Support

To use JSONP in order to avoid the same-origin policy in most browsers, make any request
as normal and add an extra $callback parameter. For example, GET http://
my_server:3580/nivariable/VariableObjects('ni.var.psp://
localhost')/type?$format=json&$callback=my_callback

The JSON data is passed as a parameter to a function called my_callback, which you
supplied with the $callback parameter. JSONP support is only valid when JSON format
is requested. JSONP support is ignored if XML format is requested.


Waveform Representations

Waveforms in LabVIEW are clusters of four components: t0, dt, Y, and attributes. In JSON,
waveforms are represented as the string value of the JSON object representation. In XML,
LabVIEW flattens the values to an XML primitive VI. The "<" and ">" are escaped with " &lt; "
and " &gt; " and stored as the string value of the Value property.

      NOTE
      JSON representation always includes a default error constant.

Using Buffering with DataSocket Functions

Complete the following steps to enable client-side buffering using DataSocket functions.
You must complete these steps for each client connection you establish.

   1.  Open a data connection.
   2.  Specify the buffer size for the data client.
   3.  Read the buffered data a server writes.
   4.  Monitor the buffer size.
   5.  Close the data connection.
   6.  Wire all error in and error out terminals on the block diagram.

You also can enable buffering when sharing data using the DataSocket functions by adding
the string ?maxbytes=1000&maxpackets=10, to the end of the URL, where 1000 is


                                                    © National Instruments Corporation 1527

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1527 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1528 ordinal=1528 -->
## LabVIEW User Manual

LabVIEW User Manual


          the maximum number of bytes the buffer contains and 10 is the maximum number of
          packets the buffer contains.

             NOTE
                   Buffering applies only when you use the DataSocket Read function to read data a
                   server writes. Buffering is not available when you use front panel DataSocket data
                  binding to read data a server writes. Buffering is available for front panel data
                  binding through the Shared Variable Engine if you bind controls to shared
                   variables with buffering enabled on the Network page of the Shared Variable
                 Properties dialog box.

         The following example uses buffering with DataSocket functions.


              RELATED INFORMATION
                   Buffering Data on page 646
                 Programmatically Opening and Closing Data Connections on page 1529
                   Specifying the Buffer Size Using DataSocket Functions on page 1530
                Reading the Buffered Data a Server Writes on page 1530
                  Monitoring the Buffer Size of a Data Connection on page 1531
                 Programmatically Opening and Closing Data Connections on page 1529
                   Setting up Error I/O in a VI on page 1436
                 Sharing Live Data Programmatically on page 641
                Reading Live Data Programmatically on page 1532
                Reading Front Panel Data Using the dstp, opc, ftp, http, or file Protocol on page
                1535
                Reading and Writing Shared Variables with Controls and Indicators on page 633
                 Understanding Shared Variable Technology on page 610


1528  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1528 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1529 ordinal=1529 -->
## LabVIEW User Manual

LabVIEW User Manual


Programmatically Opening and Closing Data
Connections

Use the DataSocket Open and DataSocket Close functions to open and close data
connections programmatically.

Complete the following steps to open and close a data connection programmatically.

   1.  Add the DataSocket Open function to the block diagram.
   2.  Wire a pspURL to the URL input or wire a shared variable control to the URL input.
   3.  Right-click the mode input and select Create»Constant from the shortcut menu.
   4.  Click the mode constant and select Read (0), Write (1), ReadWrite (2),
      BufferedRead (3), or BufferedReadWrite (4). You also can use the
      DataSocket:Mode property to set the data connection mode programmatically.
   5.  Add one of the following functions to the block diagram and create controls or
      constants for the appropriate inputs:
             •   DataSocket Read function
             •   DataSocket Write function
   6.  Wire the connection id output of the DataSocket Open function to the connection
       in input of the DataSocket Read or DataSocket Write function.
   7.  Add a DataSocket Close function to the block diagram.
   8.  Wire the connection out output of the DataSocket Read or DataSocket Write
       function to the connection id input of the DataSocket Close function to close the
      data connection. The connection also closes when the VI stops.
   9.  Wire all error in and error out terminals on the block diagram.

Writing Live Data Programmatically

Write live data programmatically to send live data updates from a VI that is not in a project,
to control and view properties of the data connection, to send live data updates to other
VIs without displaying the data on the front panel of the VI, or to avoid data loss that might
occur if you write data from the front panel.

(Real-Time, Windows) National Instruments recommends that you use a Shared Variable
node to write live data on a block diagram.

Complete the following steps to write live data programmatically.

   1.  Add the DataSocket Write function to the block diagram.
   2.  Specify a pspURL or wire a shared variable control to the connection in input of
      the DataSocket Write function.
   3.  Wire the data you want to write to the data input of the DataSocket Write function.
          If another application reads the live data, convert the data to variant data.


                                                    © National Instruments Corporation 1529

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1529 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1530 ordinal=1530 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Run the VI or continually run the VI to write live data updates to the data
                 connection.

       Specifying the Buffer Size Using DataSocket Functions

         Complete the following steps to specify the client-side buffer size using DataSocket
           functions.

                1.  Add the DataSocket Open function to the block diagram.
                2.  Wire a pspURL to the URL input or wire a shared variable control to the URL input.
                3.  Right-click the mode input and select Create»Constant from the shortcut menu.
                4.  Click the mode constant and select BufferedRead.
                5.  Add a Property Node to the block diagram.
                6.  Right-click the Property Node and select Select Class»DataSocket»DataSocket
               from the shortcut menu.
                7.  Resize the Property Node and add a terminal.
                8.  Click the first white area of the Property Node and select the Buffer Maximum Bytes
                  property.
                9.  Click the second white area of the Property Node and select the Buffer Maximum
                 Packets property.
              10. Right-click the Property Node and select Change All To Write from the shortcut
              menu.
              11. Create constants for each property and enter values for each property, such as
            1024 for Buffer Maximum Bytes and 25 for Buffer Maximum Packets. LabVIEW
                 stops filling the client-side buffer when the first buffer size limit is reached for either
                 the Buffer Maximum Bytes property or the Buffer Maximum Packets property.
              12. Wire the connection id output of the DataSocket Open function to the reference
                 input of the Property Node.

            After you specify the buffer size on the client, you can read the buffered data.

      Reading the Buffered Data a Server Writes

            After you specify a buffer size using DataSocket functions, you can read the buffered data.

         Complete the following steps to read the buffered data a server writes.

                1.  Add a While Loop to the block diagram.
                2.  Add the DataSocket Read function in the While Loop.
                3.  Wire a control or constant to the type input of the DataSocket Read function. The
                data type of the control or constant must match the data type of the data you
                 expect to read. The default data type is the variant data type. If you are unsure of
                 the data type of the data you expect to read or if another application generates the


1530  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1530 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1531 ordinal=1531 -->
## LabVIEW User Manual

LabVIEW User Manual


       data, use the variant data type. You can convert variant data to data that LabVIEW
      can manipulate.
   4.  Wire the connection id output of the Property Node you created when you specified
      the buffer size on the client to the connection in input of the DataSocket Read
       function.

After you read the buffered data, you can monitor the size of the buffer.

      RELATED INFORMATION
        Specifying the Buffer Size Using DataSocket Functions on page 1530
       Sharing Live Data Programmatically on page 641
       Converting Variant Data to LabVIEW Data on page 1172
        Specifying the Buffer Size Using DataSocket Functions on page 1530
       Monitoring the Buffer Size of a Data Connection on page 1531

Monitoring the Buffer Size of a Data Connection

After you read buffered data, you can monitor the buffer size and request diagnostic
information about the buffers you specified.

Complete the following steps to monitor the buffer size.

   1.  Add a While Loop to the block diagram.
   2.  Add a DataSocket Open function to the left of the While Loop to open a data
      connection programmatically.
   3.  Specify the buffer size for the client connection.
   4.  Add a DataSocket Read function inside the While Loop.
   5.  Wire the connection id output of the DataSocket Open function to the connection
       in input of the DataSocket Read function.
   6.  Add a Property Node inside the While Loop to the right of the DataSocket Read
       function.
   7.  Wire the connection out output of the DataSocket Read function to the reference
      input of the Property Node.
   8.  Resize the Property Node and add a terminal.
   9.  Click the first white area of the Property Node and select the Buffer Utilization
       (Bytes) property.
   10. Click the second white area of the Property Node and select the Buffer Utilization
       (Packets) property.
   11. Create indicators for each property to monitor the use of the buffer constraints you
       specified.


                                                    © National Instruments Corporation 1531

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1531 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1532 ordinal=1532 -->
## LabVIEW User Manual

LabVIEW User Manual


         LabVIEW stops filling the client-side buffer when the first buffer size limit is reached for
           either the Buffer Maximum Bytes property or the Buffer Maximum Packets property.

              RELATED INFORMATION
                Reading the Buffered Data a Server Writes on page 1530
                 Programmatically Opening and Closing Data Connections on page 1529
                   Specifying the Buffer Size Using DataSocket Functions on page 1530
                   Resizing Nodes on page 891

      Reading Live Data Programmatically

         Read live data from a data connection to manipulate the data before you add it to the front
          panel or pass the data to a VI or function on the block diagram.

           (Real-Time, Windows) National Instruments recommends that you use a Shared Variable
         node to read live data on a block diagram.

         Complete the following steps to read live data programmatically.

                1.  Add the DataSocket Read function to the block diagram.
                2.  Specify a pspURL in the connection in input of the DataSocket Read function or
                 wire a shared variable control to the connection in input.
                3.  Wire a control or constant to the type input of the DataSocket Read function. The
                data type of the control or constant must match the data type of the data you
                 expect to read. The default data type is the variant data type. If you are unsure of
                 the data type of the data you expect to read or if another application is generating
                 the data, use the variant data type. You can convert variant data to data that
               LabVIEW can manipulate.
                4.  Run the VI or continually run the VI for live data updates.

       Controlling a Front Panel Control Remotely Using the
       dstp, opc, ftp, http, or file Protocol

          Using front panel data binding to control a front panel control remotely through the
          Shared Variable Engine provides faster and more reliable data transmission than dstp as
           well as seamless connections to shared variables and NI Publish-Subscribe Protocol (NI-
          PSP)data items.


1532  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1532 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1533 ordinal=1533 -->
## LabVIEW User Manual

LabVIEW User Manual


Complete the following steps to control a front panel control from another VI using the
opc, ftp, or http protocols on Windows, and the dstp and file protocols on all
LabVIEW-supported platforms.

      NOTE
       You must install the DataSocket Server to control front panel controls remotely
       using the dstp protocol.

   1.   If you are using a dstp connection, launch and configure the DataSocket Server. If
      you are using an opc, ftp, http, or file connection, skip to step 2.
           1.  Open the DataSocket Server by selecting Start»All Programs»National
            Instruments»DataSocket»DataSocket Server.
           2.  Launch the DataSocket Server Manager by selecting Start»All
            Programs»National Instruments»DataSocket»DataSocket Server
           Manager.
           3.  Click the New Item button to create a predefined data item, and place a
           checkmark in the Allow Multiple Writers checkbox. Refer to the NI
            DataSocket Server Help for more information about configuring a
            connection for multiple writers.
   2.  Right-click a front panel object and select Properties from the shortcut menu to
       display the Properties dialog box for the object.
   3.  Click the right arrow button to navigate to the Data Binding page of the Properties
       dialog box.
   4.  Select DataSocket from the Data Binding Selection pull-down menu.
   5.  On Windows, enter an opc, ftp, or httpURL, or on all LabVIEW-supported
      platforms enter a file or dstpURL in the Path text box. You also can select DSTP
      Server or File System on all LabVIEW-supported platforms from the Browse pull-
     down menu to navigate to a URL for the predetermined data item you created in
       step 1c.
   6.  On the Data Binding page, select Read/Write from the Access Type pull-down
     menu.
   7.  Click the OK button.
   8.  Run the VI.
   9.  In a second VI (either on the local computer or on a remote computer), right-click a
       front panel object and select Properties from the shortcut menu to display the
      Properties dialog box for the object.
   10. Click the right arrow button to navigate to the Data Binding page of the Properties
       dialog box.
   11. Select DataSocket from the Data Binding Selection list.
   12. Select DSTP Server or File System from the Browse pull-down menu to navigate to
      the URL you entered in step 5.
   13. On the Data Binding page, select Read/Write from the Access Type pull-down
     menu.
   14. Run or continually run both VIs. While the VI is running, if the connection to the
      DataSocket Server is successful, a small green indicator appears next to the front
      panel object on the VI. If the connection is not successful, a small red indicator


                                                    © National Instruments Corporation 1533

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1533 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1534 ordinal=1534 -->
## LabVIEW User Manual

LabVIEW User Manual


                 appears. Before LabVIEW attempts to connect to the server, a small transparent
                  indicator appears. A status message also appears if you move the cursor over the
                   indicator. You can hide this indicator by right-clicking the front panel object and
                  selecting Visible Items»DataSocket LED from the shortcut menu. You also can use
                 the DataSocket:LED Visible property to hide the indicator programmatically.

         The front panel control in the first VI retrieves the value the second VI passes through the
          DataSocket connection. When a user changes the control value in the second VI, the
          DataSocket connection writes the new value to the front panel control in the first VI. If the
           front panel control has write-only access, the control writes the initial value when the VI
          runs or every time the VI resets if the VI runs continuously. If the front panel control has
           read-only or read/write access, the control reads the initial value when the VI runs.

      Enabling the dstp, opc, ftp, http, or file Connection for a
       Control

          Using front panel data binding to control a front panel control remotely through the
          Shared Variable Engine provides faster and more reliable data transmission than dstp as
           well as seamless connections to shared variables and NI Publish-Subscribe Protocol (NI-
          PSP) data items.

          Enabling an opc, ftp, or http connection for a control on Windows, or a dstp or file
          connection for a control on all LabVIEW-supported platforms lets a control write and read
             live data through the DataSocket Server, and on Windows, through an OPC server, FTP
            server, or Web server. Do not enable a connection for a control if you want to establish or
          save the URL for the object but not write or read data.

         Complete the following steps to enable a control for an opc, ftp, or http connection on
         Windows, or a dstp or file connection on all LabVIEW-supported platforms.

                1.   If you are using a dstp connection, launch and configure the DataSocket Server. If
               you are using an opc, ftp, http, or file connection, skip to step 2. Open the
                DataSocket Server by selecting Start»All Programs»National
               Instruments»DataSocket»DataSocket Server.
                2.  Right-click a front panel object and select Properties from the shortcut menu to
                  display the Properties dialog box for the object.

             NOTE
                You cannot create front panel data connections for type definitions.

                1.  Click the right arrow button to navigate to the Data Binding page of the Properties
                  dialog box.
                2.  Select DataSocket from the Data Binding Selection pull-down menu.
                3.  On Windows, enter an opc, ftp, or httpURL, or on all LabVIEW-supported
                 platforms enter a file or dstpURL in the Path text box. You also can select DSTP
                Server or File System on all LabVIEW-supported platforms from the Browse pull-
             down menu to navigate to a URL.


1534  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1534 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1535 ordinal=1535 -->
## LabVIEW User Manual

LabVIEW User Manual


   4.  Select Read/Write from the Access Type pull-down menu.
   5.  Click the OK button.

Reading Front Panel Data Using the dstp, opc, ftp, http,
or file Protocol

Using front panel data binding to control a front panel control remotely through the
Shared Variable Engine provides faster and more reliable data transmission than dstp as
well as seamless connections to shared variables and NI Publish-Subscribe Protocol (NI-
PSP) data items.

Complete the following steps to read front panel data using the opc, ftp, or http
protocols on Windows, and the dstp and file protocols on all LabVIEW-supported
platforms.

      NOTE
       You must install the DataSocket Server to read dstp front panel data.

   1.   If you are using a dstp connection, launch and configure the DataSocket Server. If
      you are using an opc, ftp, http, or file connection, skip to step 2. Open the
      DataSocket Server by selecting Start»All Programs»National
      Instruments»DataSocket»DataSocket Server.
   2.  Right-click a front panel object and select Properties from the shortcut menu to
       display the Properties dialog box for the object.


          Note You cannot create front panel data connections for type definitions.


   1.  Click the Data Binding tab of the Properties dialog box.
   2.  Select DataSocket from the Data Binding Selection pull-down menu.
   3.  On Windows, enter an opc, ftp, or httpURL, or on all LabVIEW-supported
      platforms enter a file or dstpURL in the Path text box. You also can select DSTP
      Server or File System on all LabVIEW-supported platforms from the Browse pull-
     down menu to navigate to a URL.
   4.  Select Read only from the Access Type pull-down menu.
   5.  Click the OK button.
   6.  On the block diagram, create a While Loop to configure the VI to run continuously.
   7.  Run the VI. LabVIEW retrieves the data from the DataSocket Server and displays it in
      the front panel object of the VI. While the VI is running, if the connection to the
      DataSocket Server is successful, a small green indicator appears next to the front
      panel object on the VI. If the connection is not successful, a small red indicator
      appears. Before LabVIEW attempts to connect to the server, a small transparent
       indicator appears. A status message also appears if you move the cursor over the
       indicator. You can hide this indicator by right-clicking the front panel object and


                                                    © National Instruments Corporation 1535

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1535 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1536 ordinal=1536 -->
## LabVIEW User Manual

LabVIEW User Manual


                  selecting Visible Items»DataSocket LED from the shortcut menu when the VI is not
                 running. You also can use the LED Visible property to hide the indicator
                 programmatically.

       Writing Front Panel Data Using the dstp, opc, ftp, http, or
         file Protocol

          Using front panel data binding to control a front panel control remotely through the
          Shared Variable Engine provides faster and more reliable data transmission than dstp as
           well as seamless connections to shared variables and NI Publish-Subscribe Protocol (NI-
          PSP) data items.

         Complete the following steps to write front panel data using the opc, ftp, or http
           protocols on Windows, and the dstp and file protocols on all LabVIEW-supported
           platforms.

             NOTE
                You must install the DataSocket Server to write front panel data using the dstp
                   protocol. Writing data from the front panel might result in data loss. If you want to
                   write all front panel data instead of only the most recent data, use the DataSocket
                  Write function to write live data programmatically.

                1.   If you are using a dstp connection, launch and configure the DataSocket Server. If
               you are using an opc, ftp, http, or file connection, skip to step 2. Launch the
                DataSocket Server from the National Instruments directory.
                2.  Right-click a front panel object and select Properties from the shortcut menu to
                  display the Properties dialog box for the object.
                3.  On the Data Binding page of the Properties dialog box, select DataSocket from the
               Data Binding Selection pull-down menu.
                4.  On Windows, enter an opc, ftp, or httpURL, or on all LabVIEW-supported
                 platforms enter a file or dstpURL in the Path text box. You also can select DSTP
                Server or File System on all LabVIEW-supported platforms from the Browse pull-
             down menu to navigate to a URL.
                5.  Select Read/Write from the Access Type pull-down menu.
                6.  Click the OK button.
                7.  On the block diagram, create a While Loop to configure the VI to run continuously.
                8.  Run the VI. LabVIEW writes the data from the front panel object to the server
                  destination you entered in the URL. While the VI is running, if the connection to the
                DataSocket Server is successful, a small green indicator appears next to the front
                panel object on the VI. If the connection is not successful, a small red indicator
                 appears. Before LabVIEW attempts to connect to the server, a small transparent
                  indicator appears. A status message also appears if you move the cursor over the
                   indicator. You can hide this indicator by right-clicking the front panel object and
                  selecting Visible Items»DataSocket LED from the shortcut menu when the VI is not
                 running. You also can use the DataSocket:LED Visible property to hide the indicator
                 programmatically.


1536  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1536 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1537 ordinal=1537 -->
## LabVIEW User Manual

LabVIEW User Manual


Web Service

Integrating Static Content into a Web Service (Real-Time,
Windows)

Parent Topic: Developing Web Services

When you build a Web service, you can integrate static content such as HTML files,
JavaScript files, CSS files, images, and videos from within the LabVIEW project. For
example, you can publish stand-alone web pages using Web services or provide a user
interface that interacts with the HTTP method VIs in a Web service.

Complete the following steps to integrate static content into a Web service:

   1.  Organize static content on disk in two main folders: one that contains public
      content and one that contains private content you do not want to expose to users.
   2.  Open the LabVIEW project that contains the Web service files.

   3.  Right-click the Web service project item    in the project tree and select Add Public
      Content Folder or Add Private Content Folder.
   4.  In the browse dialog box that appears, select the folder on disk that contains files
      you want to include in the Web service.
   5.  LabVIEW creates an auto-populating folder named Public Content or Private
      Content under the Web service project item. Any files in the folder on disk appear
      under the folder that you added to the project tree. The following project shows a
       project that contains a Public Content folder. The corresponding folder on disk
       contains the same files and subfolder as in the project tree.


                                                    © National Instruments Corporation 1537

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1537 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1538 ordinal=1538 -->
## LabVIEW User Manual

LabVIEW User Manual


            After you publish the Web service, you can access the static files from a client, such as a
        web browser, by navigating to the URL mapping for the file you want to access.


          Finding the URL Mapping for a Public File

         LabVIEW automatically assigns a URL mapping to each public static file. You cannot change
            this mapping. Complete one of the following steps to view the URL mapping for a public
             static file:

                   •   For a specific static file or folder, right-click the file in the project tree and select
            Show Public URL.
                   •   To view URL mappings for all public static files and folders, right-click the Web
                  service project item and select Properties to display the Web Service Properties
                  dialog box. On the Site Map page, the table contains a row with the URL mapping
                    for each public static file and folder.


           Integrating Default HTML Files

         You can include an index.html file within each public content folder and subfolder in
          the project. When a client sends an HTTP request using a URL such as http://
        localhost/TutorialService/, the Web service returns the index.html file.

         Complete the following steps to integrate a default index.html file for a specific public
          content folder:

                1.  On disk, add a file named index.html to a folder that appears under the Public
               Content folder in the project. In the previous example, you place the file in the
                  folder on disk that you associated with the top-level Public Content folder. The file
                 automatically appears in the project tree unless you stop the folder from auto-
                 populating changes in the corresponding folder on disk.
                             Note The file extension must be .html.

                2.  Right-click the Web service project item and select Properties.
                3.  On the Service Settings page, place a checkmark in the Serve default index.html
                  for public folders checkbox, and click OK.
                4.  In a Web browser, navigate to the URL that corresponds to the folder with the
            index.html file. The HTML file loads in the browser.


           Integrating Private Content in Web Services

           Private static files do not have URL mappings because web clients cannot access private
           content. To programmatically access private static content within Web service source files,
          use the Read Service Attribute VI to return the path to the folder that contains private
          content at run time. With the path to the private content folder, you can build a path to a
            specific file. Refer to the Read Service Attribute VI help for more information.


1538  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1538 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1539 ordinal=1539 -->
## LabVIEW User Manual

LabVIEW User Manual


Related Information

Components of a Web Service: Static Files

Testing and Debugging a Web Service on the NI Web Server
(Windows)

Parent Topic : Developing Web Services

Before you publish a Web service to a target, you might want to test that clients can invoke
and communicate with HTTP method VIs and static content as expected. If you notice
unexpected behavior or errors, you can correct them and then test the Web service again.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
         Full Development System and the LabVIEW Professional Development System.


Workflow for Debugging a Web Service

Testing and debugging a Web service is typically an iterative process you complete in the
LabVIEW project that contains the Web service files. Complete the following steps to test
and debug a Web service on the NI Web Server:

      Note In this topic, you test and debug a Web service on the NI Web Server. You can
          also test your Web service on the Application Web Server, refer to Testing and
                Debugging a Web Service on the Application Web Server.


   1.   If the Web service is part of a stand-alone application, open and run any startup VIs
       for the application from the project.

   2.  Right-click the Web service project item    in the project tree and select Start.
      LabVIEW places the Web service on the NI Web Server, where it behaves as if
      published to a target.
   3.   If you are using the NI Web Server for the first time on your computer, complete the
       following steps to enable and configure the NI Web Server:
           1.  Click Configure NI Web Server in the Start Web Service dialog box to
            launch NI Web Server Configuration.
           2.  For testing and debugging, choose the Simple local access configuration
             preset and click Next.
           3.  On the Authentication page, select Log in using an admin user for server
            administration and create your own password. Click Next.
           4.  Click Finish to apply this configuration.
           5.  Switch back to the LabVIEW project and repeat step 2.


                                                    © National Instruments Corporation 1539

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1539 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1540 ordinal=1540 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Open HTTP method VIs from the project. Use standard LabVIEW debugging
                 techniques, such as probes, breakpoints, and execution highlighting, to observe
                   their behavior when the client invokes them.
                5.  Invoke an HTTP method VI from a client, such as a web browser, using the URL
             mapped to the VI. You can find and copy the appropriate URL directly from the
                   project. Complete the following steps to access an HTTP Method VI:
                        1.  Right-click the HTTP method VI and select Show Method URL to display the
                  HTTP Method URL dialog box.
                        2.  In the Available Servers pull-down menu, select the item that contains NI
                 Web Server, and then click Copy URL.
                        3.  Close the dialog box.

            Note The Web service does not respond to any requests from the client if the HTTP
                              Method URL dialog box is open.
                        4.  Paste the URL into a web browser and replace the {value} variables with
                     numeric values, such as http://127.0.0.1:80/
                  TutorialService/Add?b=2&a=3.
            Note NI Web Server uses 80/443 as the default port in accordance with HTTP/HTTPS
              protocol. However, the port number might change if another application occupies the
                 port. You can customize the port number in NI Web Server Configuration. Refer to
             Configuring NI Web Server in the NI Web Server Manual for more information on server
                            settings like authentication, port, and remote connections.

                        5.  Browse to the URL.
                6.   If you notice an error or finish testing the Web service, right-click the Web service
                  project item in the project tree and select Stop. If startup VIs for a LabVIEW stand-
                alone application are running, you do not have to stop them.

            Note You cannot edit HTTP method VIs until you stop the debugging session because
                       LabVIEW reserves them for execution during debugging.

                7.  Edit the VIs to correct any issues you noticed.
                8.  (Optional) Repeat steps 2-7 to validate your changes to the Web service files.


          Related Information

          Understanding the NI Web Server

        Setting Up the NI Web Server for Web Services (Windows)

          Parent Topic: Hosting Web Services


1540  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1540 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1541 ordinal=1541 -->
## LabVIEW User Manual

LabVIEW User Manual


To host your Web services on the NI Web Server, set up the web server before you run or
publish the Web services.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
         Full Development System and the LabVIEW Professional Development System.

Complete the following steps to enable and configure the NI Web Server for hosting Web
services. If you use the Application Web Server to host Web services, refer to Setting up the
Application Web Server for Web Services for detailed instructions.

   1.  Launch the NI Web Server Configuration:
           1.  In the Project Explorer window, select Tools»Options to display the Options
             dialog box.
           2.  On the Web Server page, click Configure NI Web Server.


 Note LabVIEW launches NI Web Server Configuration when you first use the NI Web Server
                                  to host Web services.

   2.  The first time you launch NI Web Server Configuration, the NI Web Server Guided
      Setup appears.
   3.  Choose a configuration preset according to your needs or select Help me choose a
       preset. Click Next.
   4.  Follow the prompts to choose among configuration options. Click Finish.
   5.  The NI Web Server starts running after you configure it.
   6.  On the Control page, check the server status. You can restart, stop, enable, or
       disable the NI Web Server on this page.

Refer to Configuring NI Web Server for more information on server settings like
authentication, port, and remote connections.

Configuring Web Services Security when Using the NI Web
Server (Windows)

You can use HTTPS and privilege-based authorization to establish secure communication
between Web clients and LabVIEW Web services.

      NOTE
        In this topic, you configure the security settings for the NI Web Server. If you use
       the Application Web Server to host Web services, refer to Configuring Web Services
        Security when Using the Application Web Server for detailed instructions.

Complete the following procedures to establish the different methods of Web services
security:


                                                    © National Instruments Corporation 1541

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1541 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1542 ordinal=1542 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Enabling HTTPS on the NI Web Server
                   •   Assigning User Roles and Privileges


          Enabling HTTPS on the NI Web Server

         You can enable Secure Sockets Layer (SSL) encryption on the NI Web Server for Web
            services. Use SSL encryption to create secure, encrypted connections when sending data
         between clients and the web server.

         Complete the following steps to enable HTTPS connections:

                1.  Launch NI Web Server Configuration using the following steps:
                        1.  In the Project Explorer window, select Tools»Options to display the Options
                        dialog box.
                        2.  On the Web Server page, click Configure NI Web Server.
                2.  On the HTTPS tab in NI Web Server Configuration, choose one of the HTTPS
                  settings. Refer to Choosing an HTTPS Setting in the NI Web Server Manual for more
                 information about each HTTPS setting.
                3.  Follow the instructions to generate a self-signed certificate or to install a certificate
               from a certification authority.
                4.  Configure the Server HTTPS port number.
                5.  Click Apply and Restart. The NI Web Server uses HTTPS to communicate with
                   clients after it restarts.


                 Note LabVIEW automatically updates the HTTP Method URL according to the
                   changes in the settings for HTTP connection and port of the NI Web Server.


          Assigning User Roles and Privileges

         You can define user roles and assign different privileges to each role so that you can control
          each client's access to each HTTP Method VI and NI Web Server applications.


          Defining User Roles and Privileges for NI Web Server Application

           Refer to Defining User Roles and Privileges in the NI Web Server Manual for information on
           defining user roles and assign privileges for NI Web Server applications in NI Web Server
           Configuration.


          Assigning User Roles and Privileges to LabVIEW Web Services

         Complete the following steps in LabVIEW to configure an HTTP Method VI to accept only
           requests from Web clients with valid privileges:


1542  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1542 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1543 ordinal=1543 -->
## LabVIEW User Manual

LabVIEW User Manual


   1.  Right-click the Web service project item    in the project tree and select Properties
       to display the Web Service Properties dialog box.
   2.  On the NI Web Server Privileges page, customize and enter a name for the new
       privilege under the Privilege column to create a privilege.
   3.  Under the Role column, select a user role or enter a customized role that you create
       in NI Web Server Configuration to assign the privilege to the user role you specify.
      For example, you can assign writedata privilege to only admin user role.
   4.  On the HTTP Method VI Settings page, select a VI from the Web Service VI table and
        click the NI Web Server tab in Web Service VI Properties.
   5.  Select a privilege from the Required Privilege pull-down menu.
   6.  Click OK to apply the changes.


Accessing HTTP Method VIs with Privileges

A Web client must provide a valid username and password whenever the client submits an
HTTP request for a VI protected by privileges. Refer to Choosing an Authentication Setting
in the NI Web Server Manual and configure settings on the Authentication tab in NI Web
Server Configuration to group users into different roles.

Publishing a Web Service through a Package (Windows)

Parent Topic : Publishing Web Services

You can publish a Web service to the NI Web Server through an NI package.nipkg. The
Web service starts/stops running after you install/remove the package.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
         Full Development System and the LabVIEW Professional Development System.

Complete the following steps to publish a Web service through an NI package:

   1.  Include the Web service in a package:
           1.  Right-click Build Specifications in the Project Explorer window and select
         New » Package to launch the Package Properties dialog box.
           2.  On the Web Services page, place a checkmark in the checkbox for the Web
              service you want to include.
           3.  (Optional) On the Package Installer page, place a checkmark in the Create a
           Package Installer checkbox to build your distribution into a package
               installer file .exe.
           4.  (Optional) On the Feed page, choose whether to add your package to a local
             feed or publish the package to a feed on a SystemLink server.
   2.  Build the package that contains the Web service:


                                                    © National Instruments Corporation 1543

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1543 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1544 ordinal=1544 -->
## LabVIEW User Manual

LabVIEW User Manual


                        1.  Click Build and the Build Status dialog box appears.
                        2.  When LabVIEW completes building the package, click Explore to open the
                        destination directory where LabVIEW saves the package file(s).
                3.   Install the package on the target computer so that the Web service starts running on
                 the target computer:
                        1.  Double-click the package .nipkg in the destination directory and install the
                     package through NI Package Manager. When the installation is complete, the
                 Web service is published to the NI Web Server on the local computer.

            Note Publishing Web services to the NI Web Server requires administrator privilege.

                        2.  Close the LabVIEW project. Published Web services run on the LabVIEW
                     Runtime and do not depend on the LabVIEW Development System.


        When Do I Create a Package Installer?

         A package installer includes all package dependencies so that the target can install the
          package without network access or any NI software. If you want to publish the Web service
           to a computer that does not have an internet connection or any necessary software for
            installing the package and running the Web service, such as NI Package Manager and the
         LabVIEW Runtime, you need to create a package installer.


        When Do I Add the Web Service to a Feed?

        On the deployment target, you can subscribe to a feed to find and install the package and
           receive update notifications from NI Package Manager or NI SystemLink via network
           access. NI recommends using feeds when distributing multiple packages that have
          dependencies on one another.


          Related Information

            Installing Packages from a Feed

          Deploying Applications to Clients on a Server

       Publishing a Web Service through a Stand-Alone Application
        (Real-Time, Windows)

          Parent Topic : Publishing Web Services


1544  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1544 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1545 ordinal=1545 -->
## LabVIEW User Manual

LabVIEW User Manual


You can publish a Web service to the NI Web Server or Application Web Server through a
stand-alone application. The Web service starts/stops running when the application starts/
stops running.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
         Full Development System and the LabVIEW Professional Development System.

Complete the following steps to publish a Web service through a stand-alone application:

   1.  Include the Web service in an application:
           1.  (Windows) Right-click Build Specifications in the Project Explorer window
           and select New » Application to launch the Application Properties dialog
             box. (Real-Time) Right-click Build Specifications in Project Explorer and
              select New » Real-Time Application to launch the Real-Time Application
             Properties dialog box.
           2.  On the Web Services page, place a checkmark in the checkbox for the Web
              service you want to include.
           3.  Choose a web server for hosting the Web service. Refer to Hosting Web
              Services for more information on each web server.

 Note (Real-Time) You can use only the Application Web Server to host Web services on an
          RT target because the NI Web Server does not support RT targets.

           4.  (Optional) If you choose Application Web Server in step c, configure which
             port you want to use to accept requests for the Web service. You must
             configure each application that runs simultaneously to use a unique port.
             Place a checkmark in the Enable SSL checkbox and configure the other
             items if you want to allow clients to use HTTPS protocol to call the Web
               service.
   2.  Build the application that contains the Web service:
           1.  Click Build and the Build Status dialog box appears.
           2.  When LabVIEW completes building the application, click Explore to open the
             destination directory where LabVIEW saves the application files.
   3.  Run the application on the target device so that the Web service starts running on
      the device:
           1.  (Windows) Double-click the executable in the destination directory to run it.
             (Real-Time) Right-click the application you build under Build Specifications
               in Project Explorer, and click Run as startup. The application publishes the
         Web service to the web server on the target device.

   Note Publishing Web services to the NI Web Server requires administrator privilege.

           2.  Close the LabVIEW project. Published Web services run on the LabVIEW
           Runtime and do not depend on the LabVIEW Development System.


                                                    © National Instruments Corporation 1545

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1545 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1546 ordinal=1546 -->
## LabVIEW User Manual

LabVIEW User Manual


       Publishing a Web Service through an Installer (Windows)

          Parent Topic : Publishing Web Services

         You can publish a Web service to the Application Web Server through a Windows installer.
         The Web service starts/stops running after you finish the installation/removal process.

             NOTE
                  For more information about concepts in this topic, refer to the Web services
                   introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
                     Full Development System and the LabVIEW Professional Development System.

         Complete the following steps to publish a Web service through a Windows installer:

                1.  Include the Web service in an installer:
                        1.  Right-click Build Specifications in the Project Explorer window and select
                New » Installer to launch the Installer Properties dialog box.
                        2.  On the Web Services page, place a checkmark in the checkbox for the Web
                         service you want to include.
                2.  Build the installer that contains the Web service:
                        1.  Click Build and the Build Status dialog box appears.
                        2.  When LabVIEW completes building the installer, click Explore to open the
                        destination directory where LabVIEW saves the installer files.
                3.  Run the installer on the target computer so that the Web service starts running on
                 the target computer:
                        1.  Double-click the installer .exe in the destination directory to install the
                         application, and the installed application publishes the Web service to the
                  web server on the local computer.
                        2.  Close the LabVIEW project. Published Web services run on the LabVIEW
                     Runtime and do not depend on the LabVIEW Development System.

       Publishing and Unpublishing a Stand-Alone Web Service (Real-
       Time, Windows)

          Parent Topic : Publishing Web Services

         You can publish or unpublish a stand-alone Web service to the Application Web Server
            directly from a LabVIEW project.

             NOTE
                  For more information about concepts in this topic, refer to the Web services
                   introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
                     Full Development System and the LabVIEW Professional Development System.


1546  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1546 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1547 ordinal=1547 -->
## LabVIEW User Manual

LabVIEW User Manual


To publish a stand-alone Web service to either the computer where you develop the Web
service or a connected RT target, right-click the Web service project item in the Project
Explorer window and select Application Web Server » Publish. Published Web services
run on the LabVIEW Runtime and do not depend on the LabVIEW Development System.

To unpublish a stand-alone Web service, right-click the Web service project item and select
Application Web Server » Unpublish.

Testing and Debugging a Web Service on the Application Web
Server (Real-Time, Windows)

Before you publish a Web service to a target, you might want to test that clients can invoke
and communicate with HTTP method VIs and static content as expected. If you notice
unexpected behavior or errors, you can correct them and then test the Web service again.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
         Full Development System and the LabVIEW Professional Development System.


Workflow for Debugging a Web Service

Testing and debugging a Web service is typically an iterative process you complete in the
LabVIEW project that contains the Web service files. Complete the following steps to test
and debug a Web service on the Application Web Server:

      Note In this topic, you test and debug a Web service on the Application Web Server.
         You can also test your Web service on the NI Web Server, refer to Testing and
                    Debugging a Web Service on the NI Web Server.


   1.   If the Web service is part of a stand-alone application, open and run any startup VIs
       for the application from the project.

   2.  (Windows) Right-click the Web service project item   under My Computer in the
       project tree and select Application Web Server»Start (Debug Server). (Real-Time)
       Right-click the Web service project item    the RT target in the project tree and
       select Start (Debug Server). LabVIEW places the Web service on a debugging
       server, where it behaves as if published on a target.
   3.  Open HTTP method VIs from the project. Use standard LabVIEW debugging
       techniques, such as probes, breakpoints, and execution highlighting, to observe
       their behavior when the client invokes them.
   4.  Invoke an HTTP method VI from a client, such as a web browser, using the URL
     mapped to the VI. You can find and copy the appropriate URL directly from the
       project.
   5.   If you notice an error or finish testing the Web service, (Windows) right-click the Web
       service project item in the project tree and select Application Web Server»Stop
     (Debug Server). (Real-Time) Right-click the Web service project item and select


                                                    © National Instruments Corporation 1547

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1547 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1548 ordinal=1548 -->
## LabVIEW User Manual

LabVIEW User Manual


               Stop (Debug Server). If startup VIs for a LabVIEW stand-alone application are
                 running, you do not have to stop them.

            Note You cannot edit HTTP method VIs until you stop the debugging session because
                  LabVIEW reserves HTTP method VIs for execution during debugging.

                6.  Edit the VIs to correct any issues you noticed.
                7.  (Optional) Repeat steps 2-6 to validate your changes to the Web service files.


          Accessing HTTP Method VIs in Debugging Mode

         Complete the following steps to determine the URL of an HTTP method VI during a
          debugging session:

                1.  Right-click an HTTP method VI and select Show Method URL to display the HTTP
              Method URL dialog box.
                2.  In the Available Servers pull-down menu, select the item that contains Local
               Debugging, and then click Copy URL. The Web service runs in the debugging
                environment, so you access it on a different server and port than if you had
                published it to a target.

            Note The Web service does not respond to any requests from the client if the HTTP
                              Method URL dialog box is open.
                3.  Paste the URL into a standard web browser and replace the {value} variables
                 with numeric values, such as: http://127.0.0.1:8001/
             TutorialService/Add?b=2&a=3.


          Related Information

          Developing Web Services

         Debugging Server

        Setting Up the Application Web Server for Web Services

         To host your Web services on the Application Web Server, you need to set up the web
           server before you run or publish the Web services.

             NOTE
                  For more information about concepts in this topic, refer to the Web services
                   introduction and tutorial. LabVIEW Web services are available only in the LabVIEW
                     Full Development System and the LabVIEW Professional Development System.

         Complete the following steps to enable and configure the Application Web Server for
           hosting Web services that are not part of a LabVIEW stand-alone application.


1548  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1548 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1549 ordinal=1549 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
      The web server that hosts Web services included with a stand-alone application is
        automatically enabled.

   1.  Open a web browser.
   2.  In the browser, enter a URL for the target on which you want to enable the
       Application Web Server. The URL must conform to the following syntax:
             •   To set up the Application Web Server on the local host system, enter the
             following URL: http://localhost:3582.
             •   To set up the Application Web Server on a remote target system, right-click
             the target in a LabVIEW project, select Properties, and browse to the Web
             Server page. Click the Configure Web Application Server button. If the
            button is disabled, ensure the Application Web Server is installed on the
               target.
                   TIP
                  You also can enter the following URL in a Web browser: http://
                   [remote device IP address] where [remote device IP address] is the IP
                    address of the remote device.

          NOTE
             Because NI Web-based Configuration & Monitoring requires Microsoft
                 Silverlight, you might need to browse to the URL with Microsoft Internet
               Explorer, which provides better compatibility with Microsoft Silverlight.
   3.  Click Login and enter a username and password to gain access to NI Web-based
       Configuration & Monitoring for the system. If you have not established security
       settings for NI Web-based Configuration & Monitoring on the system, enter the
      username Admin and a blank password to gain access using the default credentials.
   4.  Click the Web Server Configuration button to display the Web Server
      Configuration page.
   5.  Click Help for information about enabling and configuring the Application Web
       Server.

The Application Web Server runs as an independent system service. You can enable and
run the Application Web Server without running LabVIEW on the host system.


Related Information

Hosting Web Services

Configuring Web Services Security when Using the Application
Web Server (Real-Time, Windows)

You can use Transport Layer Security (TLS), previously known as Secure Sockets Layer
(SSL), encryption, user and group permissions, and API keys to establish secure
communication between Web clients and LabVIEW Web services.


                                                    © National Instruments Corporation 1549

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1549 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1550 ordinal=1550 -->
## LabVIEW User Manual

LabVIEW User Manual


         Complete the following procedures to establish the different methods of Web services
            security:

                   •   Assigning Permissions to Web Service Files
                   •   Configuring API Key Security

             NOTE
                    In this topic, you configure the security settings for Application Web Server. If you
                 use the NI Web Server to host Web services, refer to Configuring Web Services
                   Security when Using the NI Web Server for detailed instructions.


          Assigning Permissions to Web Service Files

         You can require a specific permission for the following types of files:

                   •  HTTP method VIs —Set permissions that apply to individual VIs.
                   •   Public static files —Set permissions that apply to all public static files in the Web
                   service.

         Complete the following steps to configure a Web service to accept only HTTP requests from
        Web clients with valid permissions:

                1.  Right-click the Web service project item    in the project tree and select Properties
                  to display the Web Service Properties dialog box.
                2.  Browse to the page that applies to the type of file you want to configure:
                             •   For HTTP method VIs, browse to the HTTP Method VI Settings page, select a
                           VI from the Web Service VI table, and click the Application Web Server tab
                           in Web Service VI Properties.
                             •   For public static files, browse to the Service Settings page and the Static
                   Documents section.
                3.  In the Required permissions table, add the name of a permission you previously
                 created in the Security Configuration page of NI Web-based Configuration &
                 Monitoring.


          Accessing Web Service Files with Permissions

         A Web client must provide a valid username and password whenever the client submits an
        HTTP request for a file protected by permissions. The username and password must
          correspond to a user in the NI Web-based Configuration & Monitoring utility that has been
          granted the same permission added for the HTTP method VI or public static file.

         Use the OpenHandle VI to provide a username and password for HTTP requests made by a
        Web client built in LabVIEW.


1550  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1550 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1551 ordinal=1551 -->
## LabVIEW User Manual

LabVIEW User Manual


Configuring API Key Security

You also can use API keys to restrict which clients can send HTTP requests to HTTP method
VIs. An API key is a string of seemingly random characters that consists of two parts, an
access ID and a secret ID. The access ID works similarly to a username, and the secret ID
works similarly to a password intended only for authorized clients.

You can configure a single API key that applies to all Web services running on any web
server, including the Application Web Server, web servers for embedded applications, and
the Web service debugging server. You first must configure an access ID and secret ID for
the Web Server to generate API keys. Then you must enable API key security for each URL
mapping that you want to protect.


Configuring API Key Security on the Web Server

To establish an access ID and secret ID on the Application Web Server, launch the NI Web-
based Configuration & Monitoring utility and navigate to the Web Server Configuration
page. Use the Web Services API Key tab to generate, apply, and reset API keys.


Securing URL Mappings with API Key Security

Complete the following steps to enable API key security for an HTTP method VI in a Web
service:

   1.  Right-click the Web service project item    in the project tree and select Properties
       to display the Web Service Properties dialog box.
   2.  On the HTTP Method VI Settings page, select a VI from the Web Service VI table, and
        click the Application Web Server tab in the Web Service VI Properties.
   3.  Place a checkmark in the Require API key checkbox.


Accessing URL Mappings with API Key Security

When you establish an API key and enable that API key for an HTTP method VI, any HTTP
request from a Web client that corresponds to the VI must contain the correct API key. You
can use the SetAPIKey VI to configure a Web client built in LabVIEW to provide an API key
when making HTTP requests.


Related Information

Hosting Web Services


                                                    © National Instruments Corporation 1551

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1551 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1552 ordinal=1552 -->
## LabVIEW User Manual

LabVIEW User Manual


       Configuring the Root Directory of the Web Server

                 If you use the built-in LabVIEW Web Server, the root directory is the location from which the
        Web Server loads files for document requests. The default root directory for the Web Server
              is labview\www.

         Complete the following steps to configure the root directory of the Web Server.

                1.  Select Tools»Options to display the Options dialog box.
                2.  Select the Web Server page from the Category list of the Options dialog box.
                3.  Place a checkmark in the Enable Remote Panel Server checkbox in the Remote
               Panel Server section.
                4.  Enter the path of the root directory you want the Web Server to use in the Root
                 directory text box. You also can click the browse button to navigate to and select
                 the directory.
                5.  Click the OK button to save the current configuration and close the dialog box.

             NOTE
              When a user enters the URL of the Web Server without specifying a filename, an
                    error page or directory listing might display. You can create an index.htm file in
                  the Web Server root directory that automatically loads instead.

        Tutorials

          Tutorial: Creating and Publishing a LabVIEW Web Service to the NI Web
        Server (Windows)

         Complete the following steps to create, publish, and exchange data between a LabVIEW
        Web service and a web client, in this case, a web browser.

             NOTE
                LabVIEW Web services are available only in the LabVIEW Full Development System
               and the LabVIEW Professional Development System.

           This tutorial contains the following sections:

                1.  Creating a Web Service
                2.  Testing and Debugging the Web Service
                3.  Configuring How Clients Access the Web Service
                4.  Publishing the Web Service to the NI Web Server
                5.  Accessing the Web Service with a Client


1552  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1552 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1553 ordinal=1553 -->
## LabVIEW User Manual

LabVIEW User Manual


Creating a Web Service

Develop a Web service in a LabVIEW project to group together and configure the VIs and
other files that make up the Web service. Complete the following steps to create a Web
service project and two HTTP method VIs.

   1.  Create a LabVIEW project to organize the Web service files. Save the project as
     Tutorial.lvproj.
   2.  Right-click My Computer and select New»Web Service. LabVIEW adds a Web
       service project item and folders under the target.
          NOTE
               In this tutorial, you create a Web service and publish it on the host
             computer. You also can publish a Web service to a Real-Time (RT) target by
               creating a Web service project under the RT target in Project Explorer. If
            you want to publish your Web services to RT targets, you can use only the
              Application Web Server to host your Web services. Refer to Tutorial:
              Creating and Publishing a LabVIEW Web Service to the Application Web
              Server for detailed instructions.

   3.  Right-click the Web service project item      , select Rename, and name the Web
       service TutorialService. The project appears as follows:


   4.  Right-click Web Resources and select New VI to create a new HTTP method VI,
      which is a VI that receives HTTP requests from clients and returns data to clients.
      LabVIEW opens a new VI from a template.
          NOTE
            By default, an HTTP method VI returns data to clients via the connector
             pane. In this tutorial, the HTTP method VIs return the default JSON-
             formatted text responses. When you create an HTTP method VI outside this
                 tutorial, you also can stream data to a client in a custom format, such as a
             customized HTML page or image data. Configure the output format type on
              the HTTP Method VI Settings page of the Web Service Properties dialog
              box.


                                                    © National Instruments Corporation 1553

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1553 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1554 ordinal=1554 -->
## LabVIEW User Manual

LabVIEW User Manual


                5.  In the new VI, build the block diagram, front panel, and connector pane as shown in
                 the following figures.

                                                                                    Co           Block Diagram                                                  Front Panel


             When you publish this VI as part of a Web service, a web client can send an HTTP
                 request to invoke it. When invoked, this VI performs the following actions:
                             •   Receives the values of any controls assigned to the connector pane
                     exceptLabVIEW Web Service Request from the HTTP request the client
                    made. LabVIEW Web Service Request acts like a refnum by identifying the
                        current HTTP request.
                             •   Computes the sum of a and b.
                             •   Returns the sum of those values to the client via the c indicator assigned to
                       the connector pane.
                             •   Executes the Read Request Variable VI and returns the query string the client
                       included in the current HTTP request, which LabVIEW Web Service Request
                            identifies.
                             TIP
                                  In a more complex Web service, you might use other VIs on the Web
                                Services palette to enable features such as setting HTTP headers and
                                authentication.
                6.  Notice that each control and indicator appears on the connector pane. With the
                  default Terminal output type, Web services can receive data from clients or send
                data to clients only through inputs and outputs assigned to the connector pane of
              an HTTP method VI.
                       TIP
                        Assign recognizable names to each object. These names become part of the
                   URL that web clients use to exchange data with the VI.
                7.  Save the VI as Add.vi.
                8.  Select File»Save As and select Copy»Open additional copy in the dialog box that
                prompts. Ensure the Add copy to Tutorial.lvproj checkbox contains a checkmark,
              and then click Continue.
                9.  Save the new copy as Subtract.vi.
              10. Open the block diagram of Subtract.vi and replace the Add function with the
                 Subtract function. Rewire the controls and indicators.


1554  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1554 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1555 ordinal=1555 -->
## LabVIEW User Manual

LabVIEW User Manual


   11. Return to the project, right-click Web Resources, and select New Web Resource.
     Rename the new project item AdditionalOperations.
   12. Drag Subtract.vi under the AdditionalOperations project item. Save the
       project, which should appear as in the following figure.


Notice the following features in the project tree:

    •   LabVIEW appends an HTTP request type to the name of each HTTP method VI,
      which by default is GET. You can change the type of HTTP request that clients send
       to a specific HTTP method VI later in this tutorial.

    •   The Web service project item    also contains a Startup VIs folder. This tutorial
      does not use startup VIs, but you can find more information about them at the end
       of the tutorial.


Related Information

Components of a Web Service

Assigning Terminals to Controls and Indicators

Developing HTTP Method VIs: Choosing the Format of Output Data

Configuring HTTP Headers, Streaming, and Buffering

Managing a Project in LabVIEW


                                                    © National Instruments Corporation 1555

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1555 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1556 ordinal=1556 -->
## LabVIEW User Manual

LabVIEW User Manual


          Testing and Debugging the Web Service

          Before you publish the Web service to a target, you might want to test that the HTTP
         method VIs communicate with clients as expected. You can run the Web service on the NI
        Web Server directly from the LabVIEW project to allow a client to send requests to HTTP
         method VIs.

                1.  Right-click the Web service project item   and select Start.
                2.   If you are using the NI Web Server for the first time on your computer, complete the
                  following steps to enable and configure the NI Web Server:
                        1.  Click Configure NI Web Server in the Start Web Service dialog box to
                      launch NI Web Server Configuration.
                        2.  For this tutorial, choose the Simple local access configuration preset and
                            click Next.
                        3.  On the Authentication tab, select Log in using an admin user for server
                      administration and create your password. Click Next.
                        4.  Click Finish to apply this configuration.
                3.  Switch back to the LabVIEW project and repeat step 1. The Web service is now
                running on the NI Web Server.
                4.  Open Add.vi. Notice that the Run button indicates the VI is reserved for execution
                   because LabVIEW loads the Web service and makes it available on the NI Web
                 Server for communication with clients.
                5.  Close Add.vi.
                6.  Complete the following steps to get the URL that clients use to invoke Add.vi :
                        1.  Right-click Add.vi and select Show Method URL to display the HTTP
                    Method URL dialog box.
                        2.  In the Available Servers pull-down menu, select the item that contains NI
                 Web Server, and then click Copy URL.
                        3.  Close the dialog box.
                       NOTE
                          The Web service does not respond to any requests from the client if
                              the HTTP Method URL dialog box is open.
                7.  Paste the URL from step 6 into a standard web browser and replace the {value}
                  variables with numeric values, such as: http://127.0.0.1:80/
             TutorialService/Add?b=2&a=3.
                  NOTE
                        NI Web Server uses 80/443 as the default port in accordance with HTTP/
                    HTTPS protocol. However, the port number might change if another
                          application occupies the port. You can customize the port number in NI Web
                        Server Configuration. Refer to Configuring NI Web Server for more
                        information on server settings like authentication, port, and remote
                         connections.
                8.  Browse to the URL. Add.vi receives the HTTP request from the browser, computes
                 the sum of the values for a and b, and returns a response with the name and output
                 value of each indicator assigned to the connector pane of Add.vi. In this tutorial,


1556  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1556 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1557 ordinal=1557 -->
## LabVIEW User Manual

LabVIEW User Manual


      the response is a JSON string, which is the default Terminal output format. Recall
       that Add.vi has two indicators assigned to its connector pane: c and value, whose
       values the HTTP method VI returns in the response.
     {"c":5,"value":"b=2&a=3"}

          NOTE
                       If you notice unexpected behavior, you must stop the debugging session
              before you can edit the Web service files because you cannot edit the files
              while LabVIEW reserves them for execution. Right-click the Web service
               project item and select Stop.
   9.  Repeat steps 6 and 7 for Subtract.vi, or update the URL from step 7 to reflect
      the unique URL mapping for Subtract.vi : http://127.0.0.1:80/
     TutorialService/AdditionalOperations/Subtract?b=2&a=3.
   10. Repeat step 8 for Subtract.vi.
   11. Right-click the Web service project item and select Stop.


Related Information

Testing and Debugging a Web Service

Setting up the NI Web Server for Web Services


Configuring How Clients Access the Web Service

Web clients use URLs to exchange data with HTTP method VIs. Later in this tutorial, you
will enter a specific URL in a web browser to send data directly to the controls on the
connector pane of the HTTP method VIs.

Complete the following steps to define the URLs clients can use to access the HTTP method
VIs:

   1.  Right-click the Web service project item   and select Properties to display the
     Web Service Properties dialog box.
   2.  On the HTTP Method VI Settings page, notice that HTTP method VIs from the Web
      Resources folder in the LabVIEW project appear in the table of Web service VIs.
       Further, notice how placing Subtract.vi under the
     AdditionalOperations project item affects the URL mapping compared to
     Add.vi.
   3.  Select Subtract.vi in the table and notice the following features on the URL
     Mapping tab at the bottom of the page:
             •   You can change the HTTP request type in the Method pull-down menu. Use
             the default GET value for Subtract.vi.
             •   You can choose to disable the standard format LabVIEW uses to map a URL to
             the VI and instead customize the part of the URL that appears after the


                                                    © National Instruments Corporation 1557

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1557 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1558 ordinal=1558 -->
## LabVIEW User Manual

LabVIEW User Manual


                         service name. For this tutorial, use the standard URL mapping and include
                       the VI name.
                             •   The URL field displays the base URL LabVIEW creates for the HTTP method
                               VI. For example, for Subtract.vi, LabVIEW creates the default URL
                    mapping /AdditionalOperations/Subtract.


                  NOTE
                           In a more complex Web service, you might use the remaining tabs on this
                      page to configure the format that the VI returns output data to the web
                              client, as well as security settings like privileges.
                4.  Click OK to close the Web Service Properties dialog box.
                5.  Save Tutorial.lvproj.


1558  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1558 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1559 ordinal=1559 -->
## LabVIEW User Manual

LabVIEW User Manual


Related Information

Understanding URL Mappings and Query Strings in Web Services


Publishing the Web Service to the NI Web Server

You can publish the Web service you create to the NI Web Server. The NI Web Server is a
production-grade web server that can host user-authored services, such as LabVIEW Web
services, and SystemLink™ services created by NI. The NI Web Server protects web
applications against common web security threats, provides high scalability to many
enterprise-grade data services, and allows device management. In this tutorial, you
publish the web service by including it in an NI package and installing the package.

      NOTE
       You can also publish your Web service to the Application Web Server. Refer to
         Tutorial: Creating and Publishing a LabVIEW Web Service to the Application Web
        Server for more details.

Complete the following steps to publish the Web service to the NI Web Server running on
the local computer through a package:

   1.  Right-click the Build Specifications in the Project Explorer window and select
     New»Package to launch the Package Properties dialog box.
   2.  On the Information page, specify the location to build the package in the Package
      output directory text box.
   3.  On the Web Services page, place a checkmark in the TutorialService
      checkbox to include the Web service in the package.
   4.  Click Build and the Build Status dialog box appears.
   5.  When LabVIEW completes building the package, click Explore to open the
       destination directory where LabVIEW saves the package file .nipkg.
   6.  Double-click the package to install it through the NI Package Manager. When the
       installation is complete, the Web service is published to the NI Web Server on the
      host computer.
   7.  Close the LabVIEW project. Published Web services run on the LabVIEW Runtime
     and do not depend on the LabVIEW Development System.


Related Information

Publishing Web Services


Accessing the Web Service with a Client

Complete the following steps to send data to the published Web service from a web
browser via a URL:


                                                    © National Instruments Corporation 1559

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1559 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1560 ordinal=1560 -->
## LabVIEW User Manual

LabVIEW User Manual


                1.  Paste the URL from step 7 in the Testing and Debugging the Web Service section into
               a standard web browser and replace the {value} variables with numeric values,
                such as: http://127.0.0.1:80/TutorialService/Add?b=2&a=3.
                  NOTE
                                        If the client is located on a different system than where you publish the Web
                            service, you must replace 127.0.0.1 with the actual IP address of the
                         hosting system or the hostname you customize in NI Web Server
                          Configuration.
                2.  The browser returns a JSON response with the output values from each indicator
                 assigned to the connector pane.


          Related Information

          Sending Data to a Deployed Application Using URLs


        Where to Go Next

                   •   Overview: Web-based Communication with a LabVIEW Application —An overall
                 introduction to LabVIEW Web Service
                   •   Publishing a Web Service through a Package —Include a Web service in an NI
                package, so that the Web service runs when you install the package.
                   •   Publishing a Web Service through a Stand-Alone Application —Include a Web
                  service in a LabVIEW stand-alone application, so that the Web service runs when the
                  application runs.
                   •   Developing HTTP Method VIs or Developing Startup VIs to Initialize and
              Communicate with HTTP Method VIs —Develop more complex HTTP method VIs, as
                  well as startup VIs that run as part of a Web service application but do not exchange
                data with a web client.
                   •   Integrating Static Content into a Web Service —Publish static content such as HTML
                pages or images with a Web service.


         Example Code

           Refer to the following LabVIEW projects for examples of using Web services:

                   •  examples\Connectivity\Web Services\Weather Monitor\Web
            Services — Weather Monitor.lvproj


1560  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1560 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1561 ordinal=1561 -->
## LabVIEW User Manual

LabVIEW User Manual


Tutorial: Creating and Publishing a LabVIEW Web Service to the
Application Web Server (Real-Time, Windows)

Complete the following steps to create, publish, and exchange data between a LabVIEW
Web service and a web client, in this case, a web browser.

      NOTE
       For more information about concepts in this topic, refer to the Web services
        introduction. LabVIEW Web services are available only in the LabVIEW Full
       Development System and the LabVIEW Professional Development System.

This tutorial contains the following sections:

   1.  Creating a Web Service
   2.  Testing and Debugging the Web Service
   3.  Configuring How Clients Access the Web Service
   4.  Publishing the Web Service to the Application Web Server
   5.  Accessing the Web Service with a Client
   6.  Monitoring the Web Service


Creating a Web Service

Develop a Web service in a LabVIEW project to group together and configure the VIs and
other files that make up the Web service. Complete the following steps to create a Web
service project and two HTTP method VIs.

   1.  Create a LabVIEW project to organize the Web service files. Save the project as
     Tutorial.lvproj.
   2.  Right-click My Computer and select New»Web Service. LabVIEW adds a Web
       service project item and folders under the target.
          NOTE
                        •   In this tutorial, you create a Web service and publish it on the host
                   computer. You also can publish a Web service to a Real-Time target
                  by creating a Web service project under the RT target in a LabVIEW
                       project.
                        •   (Windows) NI recommends using the NI Web Server to host your Web
                      service on a Windows computer. Refer to Tutorial: Creating and
                     Publishing a LabVIEW Web Service to the NI Web Server for detailed
                       instructions.

   3.  Right-click the Web service project item      , select Rename, and name the Web
       service TutorialService. The project appears as follows:


                                                    © National Instruments Corporation 1561

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1561 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1562 ordinal=1562 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Right-click Web Resources and select New VI to create a new HTTP method VI,
               which is a VI that receives HTTP requests from clients and returns data to clients.
               LabVIEW opens a new VI from a template.
                  NOTE
                     By default, an HTTP method VI returns data to clients via the connector
                        pane. In this tutorial, the HTTP method VIs return the default JSON-
                        formatted text responses. When you create an HTTP method VI outside this
                              tutorial, you also can stream data to a client in a custom format, such as a
                       customized HTML page or image data. Configure the output format type on
                        the HTTP Method VI Settings page of the Web Service Properties dialog
                         box.
                5.  In the new VI, build the block diagram, front panel, and connector pane as shown in
                 the following figures.

                                                                                    Co           Block Diagram                                                  Front Panel


             When you publish this VI as part of a Web service, a web client can send an HTTP
                 request to invoke it. When invoked, this VI performs the following actions:
                             •   Receives the values of any controls assigned to the connector pane
                     exceptLabVIEW Web Service Request from the HTTP request the client


1562  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1562 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1563 ordinal=1563 -->
## LabVIEW User Manual

LabVIEW User Manual


         made. LabVIEW Web Service Request acts like a refnum by identifying the
           current HTTP request.
          •   Computes the sum of a and b.
          •   Returns the sum of those values to the client via the c indicator assigned to
          the connector pane.
          •   Executes the Read Request Variable VI and returns the query string the client
          included in the current HTTP request, which LabVIEW Web Service Request
            identifies.
                TIP
                    In a more complex Web service, you might use other VIs on the Web
                  Services palette to enable features such as HTTP sessions,
                   authentication, HTTP headers, and cookies.
6.  Notice that each control and indicator appears on the connector pane. With the
    default Terminal output type, Web services can receive data from clients or send
    data to clients only through inputs and outputs assigned to the connector pane of
   an HTTP method VI.
          TIP
           Assign recognizable names to each object. These names become part of the
         URL that web clients use to exchange data with the VI.
7.  Save the VI as Add.vi.
8.  Select File»Save As and select Copy»Open additional copy in the dialog box that
    prompts. Ensure the Add copy to Tutorial.lvproj checkbox contains a checkmark,
   and then click Continue.
9.  Save the new copy as Subtract.vi.
10. Open the block diagram of Subtract.vi and replace the Add function with the
    Subtract function. Rewire the controls and indicators.
11. Return to the project, right-click Web Resources, and select New Web Resource.
   Rename the new project item AdditionalOperations.
12. Drag Subtract.vi under the AdditionalOperations project item. Save the
    project, which should appear as in the following figure.


                                                 © National Instruments Corporation 1563

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1563 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1564 ordinal=1564 -->
## LabVIEW User Manual

LabVIEW User Manual


           Notice the following features in the project tree:

                   •   LabVIEW appends an HTTP request type to the name of each HTTP method VI,
               which by default is GET. You can change the type of HTTP request that clients send
                  to a specific HTTP method VI later in this tutorial.

                   •   The Web service project item    also contains a Startup VIs folder. This tutorial
               does not use startup VIs, but you can find more information about them at the end
                  of the tutorial.


          Related Information

         Components of a Web Service

           Assigning Terminals to Controls and Indicators

          Developing HTTP Method VIs: Choosing the Format of Output Data

           Configuring HTTP Headers, Streaming, and Buffering

         Managing a Project in LabVIEW


          Testing and Debugging the Web Service

          Before you publish the Web service to a target, you might want to test that the HTTP
         method VIs communicate with clients as expected. You can place the Web service on a
          debugging server directly from the LabVIEW project to allow a client to send requests to
        HTTP method VIs. The debugging server provides a sandbox-like environment.


1564  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1564 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1565 ordinal=1565 -->
## LabVIEW User Manual

LabVIEW User Manual


   1.  (Windows) Right-click the Web service project item   under My Computer and
       select Application Web Server»Start (Debug Server). (Real-Time) Right-click the
     Web service project item   under the RT target and select Start (Debug Server).
   2.  Open Add.vi. Notice that the Run button indicates the VI is reserved for execution
         because LabVIEW loads the Web service and makes it available on the
      debugging server for communication with clients.
   3.  Close Add.vi.
   4.  Complete the following steps to get the URL that clients use to invoke Add.vi :
           1.  Right-click Add.vi and select Show Method URL to display the HTTP
           Method URL dialog box.
           2.  In the Available Servers pull-down menu, select the item that contains
            Local Debugging, and then click the Copy URL button. Clients must
           communicate with Web services on the debugging server through a different
             port than if you publish the service to a web server.
           3.  Close the dialog box.
               NOTE
                 The Web service does not respond to any requests from the client if
                    the HTTP Method URL dialog box is open.
   5.  Paste the URL from step 4 into a standard web browser and replace the {value}
       variables with numeric values, such as: http://127.0.0.1:8001/
     TutorialService/Add?b=2&a=3.
   6.  Browse to the URL. Add.vi receives the HTTP request from the browser, computes
      the sum of the values for a and b, and returns a response with the name and output
      value of each indicator assigned to the connector pane of Add.vi. In this tutorial,
      the response is a JSON string, which is the default Terminal output format. Recall
       that Add.vi has two indicators assigned to its connector pane, c and value, whose
       values the HTTP method VI returns in the response.
     {"c":5,"value":"b=2&a=3"}

          NOTE
                       If you notice unexpected behavior, you must stop the debugging session
              before you can edit the Web service files because you cannot edit the files
              while LabVIEW reserves them for execution.
   7.  Repeat steps 4 and 5 for Subtract.vi, or update the URL from step 5 to reflect
      the unique URL mapping for Subtract.vi : http://127.0.0.1:8001/
     TutorialService/AdditionalOperations/Subtract?b=2&a=3.
   8.  Repeat step 6 for Subtract.vi.
   9.  (Windows) Right-click the Web service project item and select Application Web
      Server»Stop (Debug Server). (Real-Time) Right-click the Web service project item
     and select Stop (Debug Server).


Related Information

Testing and Debugging a Web Service on the Application Web Server


                                                    © National Instruments Corporation 1565

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1565 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1566 ordinal=1566 -->
## LabVIEW User Manual

LabVIEW User Manual


          Configuring How Clients Access the Web Service

        Web clients use URLs to exchange data with HTTP method VIs. Later in this tutorial, you
             will enter a specific URL in a web browser to send data directly to the controls on the
          connector pane of the HTTP method VIs.

         Complete the following steps to define the URLs clients can use to access the HTTP method
             VIs:

                1.  Right-click the Web service project item   and select Properties to display the
            Web Service Properties dialog box.
                2.  On the HTTP Method VI Settings page, notice that HTTP method VIs from the Web
               Resources folder in the LabVIEW project appear in the table of Web service VIs.
                   Further, notice how placing Subtract.vi under the
            AdditionalOperations project item affects the URL mapping compared to
              Add.vi.
                3.  Select Subtract.vi in the table and notice the following features on the URL
              Mapping tab at the bottom of the page:
                             •   You can change the HTTP request type in the Method pull-down menu. Use
                       the default GET value for Subtract.vi.
                             •   You can choose to disable the standard format LabVIEW uses to map a URL to
                       the VI and instead customize the part of the URL that appears after the
                         service name. For this tutorial, use the standard URL mapping and include
                       the VI name.
                             •   The URL field displays the base URL LabVIEW creates for the HTTP method
                               VI. For example, for Subtract.vi, LabVIEW creates the default URL
                    mapping /AdditionalOperations/Subtract.


1566  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1566 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1567 ordinal=1567 -->
## LabVIEW User Manual

LabVIEW User Manual


          NOTE
               In a more complex Web service, you might use the remaining tabs on this
            page to configure the format that the VI returns output data to the web
                 client, as well as security settings like permissions.
   4.  Click OK to close the Web Service Properties dialog box.
   5.  Save Tutorial.lvproj.


Related Information

Understanding URL Mappings and Query Strings in Web Services


                                                    © National Instruments Corporation 1567

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1567 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1568 ordinal=1568 -->
## LabVIEW User Manual

LabVIEW User Manual


          Publishing the Web Service to the Application Web Server

         You can publish the Web service you create to the Application Web Server. In this tutorial,
         you publish a stand-alone Web service, but in a more complex application, you might
           publish a Web service through a LabVIEW stand-alone application or an installer. The
           Application Web Server hosts Web services on a network and provides multiple security-
           related features to protect the network data exchange, including Secure Socket Layer (SSL)
           encryption.

             NOTE
                (Windows) You can also publish your Web service to the NI Web Server. Refer to
                     Tutorial: Creating and Publishing a LabVIEW Web Service to the NI Web Server for
                   detailed instructions.

         Complete the following steps to publish the Web service to the Application Web Server
          running on the local computer:

                1.  Right-click the Web service project item and select Application Web
                Server»Publish. The Deployment Progress dialog box appears.
                2.   If LabVIEW publishes the Web service without errors, click the Close button. Web
                   clients can now exchange data with the HTTP method VIs.


          Related Information

           Publishing Web Services

           Setting up the Application Web Server for Web Services


          Accessing the Web Service with a Client

         Complete the following steps to send data to the published Web service from a web
          browser via a URL:

                1.  Right-click Add.vi and select Show Method URL to display the HTTP Method URL
                  dialog box.
                2.  In the Available Servers pull-down menu, select the item that contains
                 Application, and then click the Copy URL button. This URL contains a different port
              number than the URL for the debugging server. LabVIEW uses this port number for
               communication with the Web service files running on the Application Web Server.
                3.  Close the dialog box.
                4.  Paste the URL into a standard web browser and replace the {value} variables
                 with numeric values, such as: http://127.0.0.1:8080/
             TutorialService/Add?b=2&a=3.
                  NOTE
                                        If the client is located on a different system than where you publish the Web
                            service, you must replace 127.0.0.1 with the actual IP address of the
                         hosting system.


1568  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1568 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1569 ordinal=1569 -->
## LabVIEW User Manual

LabVIEW User Manual


   5.  The browser returns a JSON response with the output values from each indicator
      assigned to the connector pane.


Related Information

Sending Data to a Deployed Application Using URLs


Monitoring the Web Service

Complete the following steps to check the status of Web services published to the
Application Web Server:

   1.  Right-click the Web service project item and select Application Web
      Server»Manage Web Server. NI Web-based Configuration & Monitoring opens in a
     web browser.


   2.  Click the Web Services Management button in the left-hand sidebar           .
   3.  Select TutorialService in the Published Web Services list. If the list is empty, click
      the Refresh button.
   4.  Notice that the status of the Web service is Running. To pause, resume, restart, and
      unpublish Web services, use the buttons at the bottom of the page.
   5.  On the right side of the page, notice that the URL mappings for the HTTP method
        VIs, Add and AdditionalOperations/Subtract, appear with the HTTP
     method they perform.


Where to Go Next

    •   Communicating with a LabVIEW Application from Web Clients
    •   Overview: Web-based Communication with a LabVIEW Application —An overall
       introduction to LabVIEW Web Service
    •   Publishing a Web Service through a Stand-Alone Application —Include a Web
       service in a LabVIEW stand-alone application, so that the Web service runs when the
       application runs.
    •   Publishing a Web Service through an Installer —Include a Web service in a Windows
        installer, so that the Web service runs when you finish the installation process.
    •   Developing HTTP Method VIs or Developing Startup VIs to Initialize and
     Communicate with HTTP Method VIs —Develop more complex HTTP method VIs, as
       well as startup VIs that run as part of a Web service application but do not exchange
      data with a web client.
    •   Integrating Static Content into a Web Service —Publish static content such as HTML
      pages or images with a Web service.


                                                    © National Instruments Corporation 1569

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1569 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1570 ordinal=1570 -->
## LabVIEW User Manual

LabVIEW User Manual


         Example Code

           Refer to the following LabVIEW projects for examples of using Web services:

                   •  examples\Connectivity\Web Services\Weather Monitor\Web
            Services — Weather Monitor.lvproj

      Adding New Browser Access List Entries

         Complete the following steps to add a new entry to the Browser Access List.

                1.  Select Tools»Options to display the Options dialog box.
                2.  Select Web Server from the Category list.
                3.  Type a valid browser address in the Browser Address text box. Enter a domain
               name, such as mydomain.com, or an IP address, such as 130.164.123.123.
               You also can use wildcards in the browser address.

             NOTE
                             If the Web Server runs on a computer that does not have access to a DNS server, do
                 not use domain name entries in the Browser Access List. Requests to resolve the
               domain name or IP address fail, slowing down the computer.

                1.  Click the Allow Viewing and Controlling, Allow Viewing, or Deny Access buttons
                  to allow or deny access to the selected item, respectively. Two green checkmarks
                appear to the left of the item when you allow viewing and controlling of the front
                  panel, a single green checkmark appears when you allow only viewing of the front
                  panel, and a red X appears when you deny access.
                2.   If an entry does not have one or two green checkmarks or a red X by its name, the
                 syntax for the entry is incorrect. Edit the entry or click the Remove button to delete
                           it.
                3.  Click the OK button to close the Options dialog box and save the changes.

       Allowing and Denying Web Browser Access

         Use the Browser Access section on the Web Server page of the Options dialog box to
           configure which browser addresses can view your VI front panels. Create a Browser Access
            List that allows and denies access to individual browser addresses. You also can use the
        Web Server:TCP/IP Access List property to allow and deny access to browser addresses
          programmatically.

        When a Web browser attempts to obtain a VI front panel image, the Web Server compares
          the browser address to the entries in the Browser Access List to determine whether it
          should grant access. If an entry in the Browser Access List matches the browser address,
          the Web Server permits or denies access based on how you set up the entry. By default all
          browsers have access to the LabVIEW Web Server. When you add new Browser Access List


1570  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1570 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1571 ordinal=1571 -->
## LabVIEW User Manual

LabVIEW User Manual


entries, edit existing entries, or remove entries, use the correct syntax, order, and wildcards
in the entries.

      RELATED INFORMATION
       Syntax for Browser Address Lists on page 1579
       Adding New Browser Access List Entries on page 1570
        Editing Existing Browser Access List Entries on page 1571
      Removing Browser Access List Entries on page 1461
       Syntax for Browser Address Lists on page 1579

Editing Existing Browser Access List Entries

Complete the following steps to edit a browser address in the Browser Access List.

   1.  Select Tools»Options to display the Options dialog box.
   2.  Select Web Server from the Category list.
   3.  Select the address you want to modify in the Browser Access List in the Browser
      Access section. The address appears in the text box.
   4.  Edit the address in the text box or click the Allow Viewing and Controlling, Allow
      Viewing, or Deny Access buttons. You also can use wildcards in the browser
       address.
   5.  Click the OK button to close the Options dialog box and save the changes.

Front Panels

Controlling an Application or Front Panel Remotely Using a
Browser or LabVIEW

Complete the following steps to control an application or front panel remotely using a Web
browser or LabVIEW.

      NOTE
      The application or VI you want to view must be in memory on the server computer.

   1.  View an application or front panel remotely in a browser or in LabVIEW.
   2.  Click the bottom of the remote front panel window or right-click the front panel
      anywhere and select Request Control of VI from the shortcut menu. If no other
       client is currently in control, you have control of the front panel. If another client is
       currently controlling the VI, the server queues the request until the other client
       relinquishes control or until the control time limit times out. Only the user at the
       server computer can monitor the queue list.


                                                    © National Instruments Corporation 1571

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1571 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1572 ordinal=1572 -->
## LabVIEW User Manual

LabVIEW User Manual


         To completely close the connection to the Web Server running on the server computer,
            click the close glyph on the browser window or LabVIEW window border. However, if you
         want to release control of the front panel but maintain a connection so you can view the
           front panel, right-click the front panel in any open space and select Release Control of VI
         from the shortcut menu or right-click a front panel object, such as a graph, and select
        Remote Panel Client»Release Control of VI from the shortcut menu.

               Note If you want to save the data generated by a VI running on a remote computer,
                            use DataSocket or TCP instead of remote front panels.


         You also can use the Application methods to release and request control of a remote front
          panel programmatically.

       Enabling and Configuring the Web Server for Remote Front
       Panels

         Complete the following steps to enable and configure the LabVIEW Web Server for viewing
         and controlling front panels remotely. The Web server only can run while LabVIEW remains
         open on the host machine.

                1.  Select Tools»Options to display the Options dialog box.
                2.  Select the Web Server page from the Category list of the Options dialog box.
                3.  Place a checkmark in the Enable Remote Panel Server checkbox in the Remote
               Panel Server section. The default Web Server configuration is suitable for most
                  applications.

             NOTE
                    (Linux) By default, LabVIEW uses port 8000 so the Web Server can run in accounts
                   that do not have root access. If you have root access, you can change the port to
                80. If you use any port other than 80, you must specify the port number in URLs
                   that refer to the server, as shown in the following example:
             http://hostname:8000/index.htm

                1.  To control browser access to the front panels or control which VIs are visible on the
               Web, configure the Browser Access and Visible VIs sections of the Web Server
                 page.
                2.  Click the OK button to close the Options dialog box and save the changes. The Web
                 Server is running.

         Use the Web Server properties to enable and configure the Web Server programmatically.
         You also can enable and configure the Web Server in a built application.


1572  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1572 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1573 ordinal=1573 -->
## LabVIEW User Manual

LabVIEW User Manual


Enabling TLS/SSL Security for Remote Front Panels (Windows)

You can enable Transport Layer Security (TLS), previously known as Secure Sockets Layer
(SSL), encryption for network communication involving remote front panels.

      NOTE
       To use TLS/SSL encryption with LabVIEW Web services, you must enable TLS/SSL
      on the Application Web Server.

Complete the following steps to enable TLS/SSL on the LabVIEW Web Server for remote
front panels.

   1.  Navigate to the Remote Panel Server section on the Web Server page of the
      Options dialog box. If necessary, enable the LabVIEW Web Server for use with
      remote front panels.
   2.  Place a checkmark in the SSL checkbox.
   3.  Enter the network port to encrypt with TLS/SSL in the SSL Port field or use the
       default TLS/SSL port 443. You cannot enable TLS/SSL on network communication
       that uses the default port 80.
   4.  Leave the SSL certificate file text box blank to use the default LabVIEW self-signed
        certificate.
   5.  (Optional) Specify the address of the system or target that contains the certificate in
      the Server address text box.
          NOTE
            You also can navigate directly to the certificate file that you created using
              the SSL certificate file text box.
   6.  (Optional) Click the Query button to display available certificates located on the
       server in the Discovered certificates listbox.
   7.  (Optional) Select the certificate from the Discovered certificates listbox.

Errors When Connecting to Remote Front Panels

The following table lists errors that might occur when you connect to remote front panels
in LabVIEW or in a Web browser.

 Error                                          Solution

 Invalid server IP       Contact the server administrator to get the correct IP address or
 address               name of the computer to which you want to connect.

 Remote panel         The server administrator must enable the LabVIEW Web Server.
 connection refused       Verify that the Server IP Address and Port you entered in the
 by specified server           Connect to Remote Panel dialog box are correct.


                                                    © National Instruments Corporation 1573

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1573 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1574 ordinal=1574 -->
## LabVIEW User Manual

LabVIEW User Manual


            Error                                          Solution

                              The server administrator must specify the IP addresses for all             Client does not have                                    potential clients wanting to view or control a remote front panel.            access to remote                                                         If the server administrator does not specify any IP addresses,           panel server                                 LabVIEW allows all clients to access remote front panels.

                               The client and server computers must be running the same
                                  version of LabVIEW. If you are using a browser to view and control
          Remote panel          a remote front panel, you must use a version of the LabVIEW
            protocol version      Run-Time Engine compatible with the version of LabVIEW on the
           incompatible           server computer. Also, contact the server administrator to verify
                                     that the HTML document specifies the correct version of the
                                            LabVIEW Run-Time Engine.

                              You must use a version of LabVIEW compatible with the version of
          LabVIEW client        LabVIEW on the server computer. If you are using a browser to
            version is             view and control a remote front panel, you must use a version of
           incompatible with       the LabVIEW Run-Time Engine compatible with the version of
          LabVIEW server          LabVIEW on the server computer. Also, contact the server
            version                 administrator to verify that the HTML document specifies the
                                            correct version of the LabVIEW Run-Time Engine.

            Server does not                            Make sure you entered the IP address or computer name of the           support Remote                                                          server correctly.           Panels

                            A memory or network problem occurred. This error might occur if
                               you try to connect to a large front panel. Try to connect to the
                                    front panel again, or request that the server administrator modify
                                the front panel so it uses less memory. This error also might occur          Remote panel server                                                          if you deploy a VI to a Real-time target without the Web Server             failed to send                                   enabled, and subsequently enable the Web Server. The error           requested VI                                 occurs because the deployed VI does not have a front panel in this
                                        case, since LabVIEW only preserves the front panel of a VI
                               deployed to a Real-Time target when the Web server is enabled.
                                           This behavior is for performance optimization.

             Client does not have  The server administrator must specify the VIs that clients can view
            access to specified VI                            or control.

           Requested VI is not   A VI is considered to be in memory whenever the VI is open on the
           loaded into memory    server machine. The VI does not have to be running. Also, make
          on the server          sure the VI name you entered matches the host machine exactly,
          computer                                including the.vi extension.

        Functionality Not Supported in Viewing and Controlling
      Remote Front Panels

         The following list includes functionality not supported and recommendations to consider
        when viewing and controlling remote front panels.


1574  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1574 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1575 ordinal=1575 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Because of the constraints of a Web browser, user interface applications that
      attempt to manipulate the dimensions and location of a front panel do not work
       properly when that front panel is displayed as a part of a Web page. Although the
     Web Server and the LabVIEW browser plug-in attempt to preserve the fidelity of
      complex user interface applications—in particular, those that present dialog boxes
     and subVI windows—some applications might not work properly in the context of a
     Web browser. National Instruments recommends that you do not export these types
       of applications for use in a Web browser.
    •   Avoid exporting VIs that have While Loops but no wait function. These VIs prevent
      background tasks from performing in a reasonable amount of time, making front
      panels unresponsive when viewed or controlled remotely.
    •  Some VIs might not work exactly the same way from a remote computer as they do
     when run locally. Embedded.NET and ActiveX controls do not display on a remote
       client because they draw and operate almost completely independently of LabVIEW.
          If a VI presents the standard file dialog box, the controller receives an error because
      you cannot browse a file system remotely. Also, the browse button of a path control
         is disabled in remote panels.
    •   Clients viewing a front panel remotely might see different behavior depending on
      whether the front panel they are connecting to is from a built application.
        Specifically, if the front panel is from a built application, any programmatic changes
       to the front panel made before the client connects to the front panel are not
       reflected on the client computer. For example, if a Property Node changes a caption
     on a control before a client connects to that front panel, the client will see the
       original caption of the control, not the changed caption.
    •   Only a controller can remotely view the front panel of a VI dynamically opened and
      run using the VI Server or the front panel of a subVI configured to display the front
      panel when called. Clients not controlling the VI cannot view the front panel.
    •   Block diagrams that achieve certain user interface effects by polling properties of a
       front panel control might experience decreases in performance when you control
      the VI from a remote computer. You can improve the performance of these VIs by
      using the Wait for Front Panel Activity function.
    •   LabVIEW cannot generate a Panel Close event for a VI being viewed or controlled
       remotely. If you are viewing or controlling a VI remotely, LabVIEW can generate
      events only in the Control class, that is not in the Application or VI class.
    •     If you are remotely viewing or controlling a VI which displays the front panel of a
      subVI when calling the subVI, avoid manually closing the front panel of the subVI.
      Otherwise, you might lose control of the VI on both the client computer and the
       server computer. If you must view the front panel of the subVI when called,
       configure LabVIEW to close the subVI after it runs.

Locking and Unlocking Remote Front Panels

You can lock and unlock a front panel that a client views remotely so the client cannot or
can change the values of the front panel controls.

Right-click anywhere on the front panel of the running VI and select Lock Control to lock a
front panel that a client views remotely. When you lock a front panel that clients view
remotely, LabVIEW queues any requests from clients to control the front panel.


                                                    © National Instruments Corporation 1575

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1575 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1576 ordinal=1576 -->
## LabVIEW User Manual

LabVIEW User Manual


         You also can use the Remote Panel:Lock Control method to lock control of a remote front
          panel programmatically.

            Right-click anywhere on the front panel of the running VI and select Unlock Control to
          allow a client viewing the front panel remotely to change the value of front panel controls.
        When you unlock a front panel that clients view remotely, LabVIEW grants control to the
           next client in the queue. If no clients are in the queue, the method unlocks the front panel.

         You also can use the Remote Panel:Unlock Control method to unlock control of a remote
           front panel programmatically.

      Managing Client Traffic to a Front Panel

                 If you are managing a server that provides front panels for clients to view and control from
         remote computers, you can monitor all client traffic to the server. Select Tools»Remote
          Panel Connection Manager to display the Remote Panel Connection Manager window.

         Use this window to manage the client queue list, disconnect a client, and specify how long
           to retain network client traffic data. To disconnect all clients, select a VI name or Total
         Network Traffic and click the Disconnect Client button.

         You also can use the Remote Panel:Connections To Servers and the Remote
          Panel:Connections To Clients properties to retrieve information about remote front panel
           connections.

       Publishing VIs and Stand-Alone Applications on the Web

         Use the LabVIEW Web Server to publish images of front panels from a VI or a stand-alone
           application to the Web. By default, after you enable the Web Server, all VIs and applications
           are visible to all Web browsers. However, you can control browser access to the published
           front panels and configure which VIs are visible on the Web. To display front panels on the
         Web, the VIs must be in memory on the computer.

         The Web Server can generate images of front panels in the JPEG and PNG image formats.
         The JPEG format compresses graphics well but can lose some graphic detail. This format
         works best for photos. For line art, front panels, and block diagrams, JPEG compression
         can result in fuzzy graphics and uneven colors. The PNG format also compresses graphics
            well, although not always as well as the JPEG format. However, PNG compression does not
           lose any detail.

         Use the Web Publishing Tool to create an HTML document and embed static or animated
         images of the front panel or to embed a front panel in an HTML document so a client
         computer can view and control the front panel remotely. You also can embed static images
           of the front panel in an existing HTML document. To deploy an HTML document with the
           application, enable and configure the Web Server in a stand-alone application.

         Use the Snapshot option in the Web Publishing Tool to return a static image of the front
          panel of a VI currently in memory on the server computer. Use the Monitor option in the
        Web Publishing Tool to return an animated image of the front panel of a VI or application
           currently in memory on the server computer. Use the Embedded option in the Web


1576  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1576 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1577 ordinal=1577 -->
## LabVIEW User Manual

LabVIEW User Manual


Publishing Tool to embed a front panel in an HTML document so a client computer can
view and control the front panel remotely.

      NOTE
      The front panel of the VI or application you want to publish might be large. It takes
       the Web Server longer to create a large image, which can slow the execution of the
          VI. Also, a large image takes a significant amount of time to transmit to the
       browser, especially over a slow modem connection. Therefore, make sure the front
       panels of VIs and applications you want to publish are a reasonable size.

After you publish a VI or an application, you can control the application or front panel
remotely or view either using a browser or using LabVIEW.

You can also share VIs with registered users on ni.com.

      RELATED INFORMATION
       Enabling and Configuring the Web Server for Remote Front Panels on page 1572
       Allowing and Denying Web Browser Access on page 1570
        Specifying Which VIs Are Visible on the Web on page 1579
       Creating HTML Documents and Embedding Front Panel Images on page 1449
       Viewing an Application or Front Panel Remotely Using a Browser on page 1582
      Embedding a Front Panel Image in an Existing HTML Document on page 1450
       Enabling the Web Server in Stand-Alone Applications on page 1509
        Controlling an Application or Front Panel Remotely Using a Browser or LabVIEW on
       page 1571
       Viewing an Application or Front Panel Remotely Using a Browser on page 1582
       Viewing an Application or Front Panel Remotely Using LabVIEW on page 1583

Sending an Email from a VI

You can use the Send Email Express VI to quickly send emails from LabVIEW to a list of
recipients you specify.

Complete the following steps to configure the Send Email Express VI to send an email:

      NOTE
            If you want to configure headers, set Transport Layer Security (TLS) settings, or
        include an attachment, you can use the standard SMTP Email VIs to configure and
       send an email with more advanced settings. Refer to the labview\examples
      \Data Communication\Protocols\SMTP\Send Email using SMTP
      Client.vi for an example of using the standard SMTP Email VIs to send an
        email.


                                                    © National Instruments Corporation 1577

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1577 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1578 ordinal=1578 -->
## LabVIEW User Manual

LabVIEW User Manual


                1.  Add the Send Email Express VI to the block diagram. The Configure Send Email
                  dialog box automatically opens.
                2.  Specify your email address or the email address from which you want to send the
                email in the Sender's Email Address textbox located in the User Information
                   section.
                3.  Specify the host name or IP address of the SMTP server, such as
             my.mailserver.com, you want to use to send the email in the Outgoing Mail
                Server (SMTP) textbox. If you do not know which mail server to use, contact the
               network administrator for the name of a valid server.
                4.  Specify the port number of the SMTP server you want to use to send the email in the
                Port textbox. The default is 25, which is standard for open connections. However, if
               you use a secure connection, you may need to change the port number.
                5.  (Optional) Place a checkmark in the Require Log-in checkbox to transmit log-in
                  credentials to the SMTP server. Most public SMTP servers require log-in credentials.
                        1.  Specify the log-in username, in the Username textbox, for the SMTP server
                    you specify. On most public servers, this is your email address or the email
                      address from which you want to send the email.
                        2.  Specify the log-in password, in the Password textbox, for the SMTP server
                    you specify.
                6.  (Optional) Place a checkmark in the Use Secure Connection (TLS\SSL) checkbox to
                  require a TLS\SSL secured connection when LabVIEW communicates with the SMTP
                   server.
                7.  Specify the email address(es) of the recipient(s) in the Recipients textbox located in
                 the Email section. To send an email to multiple recipients, separate each email
                address with a comma. You must enter at least one email address. You also can wire
               a recipient list to the Recipients input on the block diagram.
                8.  (Optional) Specify the subject of the message in the Subject textbox. You also can
                 wire a subject line to the Subject input on the block diagram.
                9.  (Optional) Specify a message in plain text, in the Message textbox, that you want to
               send to the recipient(s). You also can wire a message to the Message input on the
                 block diagram.
              10. (Optional) Click the Send Test Email button to test the configuration of the VI by
                sending a test email to the email address you specify in Sender's Email Address.
              11. Click the OK button to save the configuration and close the Configure Send Email
                  dialog box.
              12. Wire all error in and error out terminals on the block diagram.
              13. Run the VI. LabVIEW sends an email according to the configuration you set.

       Setting Time Limits on Client Control

          With the Web Server, you can set a time limit on how long a remote client can control a VI
        when multiple clients are waiting to control the VI. You should set a time limit to guarantee
           that every client has a chance to obtain control of the VI. When a particular client reaches


1578  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1578 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1579 ordinal=1579 -->
## LabVIEW User Manual

LabVIEW User Manual


the time limit, the next client in the queue is the controller. However, all clients still can
view the front panel.

      NOTE
       LabVIEW does not begin monitoring the time limit set on a particular VI until a
       second client requests control of the same VI. If a second client never requests
        control of the VI, then the initial client never loses control of the VI.

Complete the following steps to set the time limit on how long each client can control a
particular VI.

   1.  Select Tools»Options to display the Options dialog box.
   2.  Select Web Server from the Category list.
   3.  Click a VI in the Visible VIs list in the Visible VIs section. If no VIs appear in the list,
      you need to add visible VI entries to the list and then select it.
   4.  Place a checkmark in the Allow access checkbox.
   5.   If you want to change the default time limit, remove the checkmark from the Use
      default checkbox. The default is 300 seconds.
   6.  In the Control time limit (sec) field, enter the amount of time in seconds you want
       to allow each client to control the front panel of the VI you selected in the Visible
       VIs list.
   7.  Click the OK button.

Specifying Which VIs Are Visible on the Web

Use the Visible VIs section of the Web Server page to configure which VIs are visible on the
Web. Create a Visible VIs list that allows and denies access to individual VIs, groups of VIs,
or directory paths. You also can use the VI Access List property to allow and deny access to
VIs programmatically.

When a Web browser attempts to obtain a VI front panel image, the Web Server compares
the VI name to the entries in the Visible VIs list to determine whether it should grant
access. If an entry in the Visible VIs list matches the VI name, the Web Server permits or
denies access to that VI image based on how you set up the entry. By default, the front
panel images of all VIs are visible. When you add new Visible VIs list entries, edit existing
entries, or remove entries, use the correct syntax, order, and wildcards in the entries.

Syntax for Browser Address Lists

You can enter an IP address, such as 130.164.140.12, or a domain name, such as
www.ni.com, in the Browser Access List in the Browser Access section on the Web
Server page of the Options dialog box or the Machine access list in the VI Server page of
the Options dialog box.

Use the * wildcard to specify a group of browser addresses. For example, you can specify
all browsers within the domain domain.com with the entry *.domain.com. You can


                                                    © National Instruments Corporation 1579

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1579 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1580 ordinal=1580 -->
## LabVIEW User Manual

LabVIEW User Manual


           specify all browsers in the subnet whose first two octets are 130.164 with the entry
        130.164.*. You can only use the * wildcard at the beginning of a domain name or at the
         end of an IP address.

         The permission for an entry later in the Browser Access List or the Machine access list
           overrides previous permissions. You can click and drag an entry in the list to change the
           order.

          For example, if you deny access to all browser addresses ending in *.test.site.com,
          but after that entry you give a.test.site.com and b.test.site.com access,
          those two browsers still have access, because the entries later in the list override the first
            entry.

            In general, you should use the * wildcard to set up general allowances or denials, and
           follow those entries with more specific entries that reverse part of the previous permission.
          For best performance, place the most frequently matched entries toward the bottom of the
                list.

         The following example illustrates how to use the * wildcard correctly.

           Access                       Permission Status              List Entry

                                   *                  Allows access to all browser addresses.

                                               Allows access to all browser addresses ending                            * .site.com                                                           with .site.com.
                                            Denies access to this browser address even though          X       public.site.com                                                       previous entry allows access.

                                              Denies access to any browser address ending          X           * .test.site.com                                                        with .test.site.com.
                                             Allows access to this browser address even though                 a.test.site.com                                                       previous entry denies access.

                                             Denies access to all browser addresses whose IP          X        130.164.123. *                                                 addresses begin with 130.164.123.
                                             Allows access to this browser address even though                 130.164.123.123                                                       previous entry denies access.

      Syntax for the VIs Lists

         Each entry in the Visible and Exported VIs lists describes a VI name or a VI path and can
           contain wildcard characters. The Web and VI Servers compare entries that contain path
           separators against VI paths and compare entries that do not contain path separators
           against VI names only.


1580  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1580 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1581 ordinal=1581 -->
## LabVIEW User Manual

LabVIEW User Manual


Use the following wildcard characters when specifying entries in the Visible and Exported
VIs lists.

 Wildcard                                  Action
 ?            Matches exactly one arbitrary character except for the path separator.
 *           Matches zero or more arbitrary characters except for the path separator.
 **          Matches zero or more arbitrary characters including the path separator.
 \                       Cancels the interpretation of special characters.


The permission for an entry later in the list overrides previous permissions. You can click
and drag an entry in the list to change the order.

For example, if you deny access to all VI front panels in c:\labview\server, but after
that entry you give access to c:\labview\server\local.vi, that VI is still visible,
because the entry later in the list overrides the first entry.

In general, you should use the * wildcard to set up general allowances or denials, and
follow those entries with more specific entries that reverse part of the previous permission.
For best performance, place the most frequently matched entries toward the bottom of the
list.

The following example illustrates how to use the wildcards correctly.

 VIs List                 Permission Status Entry

                            *                          Allows access to all VIs.

                                                     Allows access to all VIs in
          c:\labview\server\*                                        c:\labview\server.
                                                     Allows access to all VIs in
           c:\labview\test\**         c:\labview\test and its
                                                               subdirectories.

                                            Denies access to this VI even though the X     c:\labview\test\private.vi                                                   previous entry allows access.

                                              Allows access to any VI that begins with
               srvr_*.vi               the string srvr_ and ends with the
                                                                   string .vi.
                                                  Denies access to Are You X        Are You Finished\?.vi                                           Finished?.vi.
                                             Denies access to all VIs named Open?
 X              Open?.vi               where ? represents one arbitrary
                                                character except for the path separator.


                                                    © National Instruments Corporation 1581

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1581 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1582 ordinal=1582 -->
## LabVIEW User Manual

LabVIEW User Manual


      Viewing an Application or Front Panel Remotely Using a
      Browser

         To view an application or front panel remotely using a Web browser, you must first
           configure the server. Complete the following steps to configure the server so a client
         computer can view an application front panel remotely using a browser.

                 TIP
                  For VIs that will be viewed or controlled remotely, create as small front panels as
                    possible. The Web Server uses more system resources to load and display large
                    front panel images than small front panel images, which can slow the execution of
                  the VI itself.

                1.  Enable the Web Server on the server computer where the application or VI you want
                  to view is located.
                2.  Configure the browser access list so the client computer can connect to the server.
                3.  Make sure the application is running or the VIs whose front panels you want clients
                  to view are in memory on the server computer.
                4.  Create an HTML file using the Web Publishing Tool. You also can use an existing
             HTML file.
                5.   If you did not use the Web Publishing Tool, place the HTML file in the labview\www
                   directory. Change the LVFPPVINAME parameter of the <OBJECT> and <EMBED>
                 tags to the name of the top-level VI for the application or the top-level VI you loaded
                  into memory. If you used the Web Publishing Tool, this step is completed
                 automatically for you.

         You also can change the WIDTH and HEIGHT parameters of the <OBJECT> and
        <EMBED> tags to customize the application or front panel appearance in the client
          browser.

         Complete the following steps if you are on a client computer and do not have LabVIEW
            installed but want to view a front panel remotely using a browser.

             NOTE
              When you view a front panel remotely from a browser, the application or VI you
               want to view must be running on the server computer.

                1.   Install the LabVIEW Run-Time Engine.
                2.  Launch the default browser.
                3.  In the URL of the browser, type the IP address or computer name of the server
                 followed by the name of the HTML file. For example, http://ipaddress/
             filename.html. If access is denied, an error message appears in the browser.
               You now can request control of the application or remote front panel.

         To completely close the connection to the Web Server running on the server computer,
            click the close glyph on the browser window border.


1582  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1582 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1583 ordinal=1583 -->
## LabVIEW User Manual

LabVIEW User Manual


You also can use the Application methods to open a connection and request control of a
remote front panel programmatically.

Viewing an Application or Front Panel Remotely Using
LabVIEW

To view an application or front panel remotely using LabVIEW, you must first configure the
server. Complete the following steps to configure the server so a client computer can view
a front panel remotely using LabVIEW.

       TIP
       For VIs that will be viewed or controlled remotely, create as small front panels as
        possible. The Web Server uses more system resources to load and display large
        front panel images than small front panel images, which can slow the execution of
       the VI itself.

   1.  Enable the Web Server on the server computer where the VI or application you want
       to view is located.
   2.  Configure the browser access list so the client computer can connect to the server.
   3.  Configure the visible VIs list so the client computer can access the VI or application
       front panels remotely. If you do not configure the visible VIs list, the client can
      access all VIs that are loaded into memory on the server computer.
   4.  Make sure the application is running or the VIs whose front panels you want clients
       to view are in memory on the server computer.

Complete the following steps if you are on a client computer and want to view a front panel
remotely using LabVIEW.

   1.  Select Operate»Connect to Remote Panel to display the Connect to Remote Panel
       dialog box.
   2.  In the Server address field, enter the IP address or computer name of the server to
      which you want to connect.
   3.  In the VI name field, enter the name of the VI whose front panel you want to view.
      Or enter the name of the top-level VI of the application you want to view.
   4.  Enter the HTTP Port. The default is 80.
   5.   If you want to immediately request control of the front panel, place a checkmark in
      the Request control checkbox. You also can request control at the bottom of the
      remote front panel window when it appears on your computer.
   6.  Click the Connect button. The front panel appears on your computer allowing you
       to view it. If access is denied, an error message appears in the Connection status
       section of the Connect to Remote Panel dialog box.

      NOTE
            If you want to save the data generated by a VI running on a remote computer, use
       DataSocket or TCP instead of remote front panels.


                                                    © National Instruments Corporation 1583

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1583 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1584 ordinal=1584 -->
## LabVIEW User Manual

LabVIEW User Manual


         To completely close your connection to the Web Server running on the server computer,
            click the close glyph on the LabVIEW window border.

               Note The server computer managing remote front panels must have the LabVIEW
                       Full or Professional Development System or must build the front panels into a
                 stand-alone application. Clients can use any LabVIEW development system to view
                               and control those front panels remotely.


         You also can use the Application methods to open a connection and request control of a
         remote front panel programmatically.

     Web Server Syntax Examples

         Use the Web Publishing Tool to embed a static or animated image of a front panel in an
        HTML document or to embed a front panel in an HTML document so a client computer can
          view and control the front panel remotely. To embed the static image of a front panel in an
            existing HTML document, enter the top-level VI name of the application in the following
           scenarios.

         To embed the static image of a VI named Example.vi running on the same computer in
         an HTML document, use the following code in the HTML document:

        <IMG SRC="/.snap?Example.vi">

         To embed the static image of a VI named Example.vi running on the computer foo in
         an HTML document, use the following code in the HTML document:

        <IMG SRC="http://foo/.snap?Example.vi">

         To embed the static image of a VI named Test 1.vi running on the computer foo using
         image type = png and image depth = 24, use the following code in the HTML document:

        <IMG SRC="http://foo/.snap?Test%201.vi&type=png&depth=24">

       Creating a TCP Client

         Complete the following steps to create a TCP client using the TCP functions.

                1.  (Optional) Create a TCP server. When you create a TCP server, you specify the
               remote port or service name to represent the port you want the server to use for
                communication.
                2.  Use the TCP Open Connection function to open a connection to a server. You must
                  specify the remote port or service name for the server. The remote port or service
            name identifies a communication channel on the computer that the server uses to
                    listen for communication requests. If you specify a service name, LabVIEW queries
                 the NI Service Locator for the port number that the server registered. If you want to


1584  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1584 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1585 ordinal=1585 -->
## LabVIEW User Manual

LabVIEW User Manual


       establish a connection to a remote computer, you must specify the Internet address
       of the server. The address identifies a computer on the network. If you do not
       specify an address, LabVIEW establishes a connection to the local computer.
   3.  Use the TCP Read function to read a message from the server. You must specify the
     number of bytes you want to read.
   4.  Use the TCP Write function to send a message to a server.
   5.  Use the TCP Close Connection function to close the connection to the server.

Refer to the following VIs for examples of a TCP client:

    •  labview\examples\Data Communication\Protocols\TCP\TCP
     Named Service\TCP Named Service.lvproj

      RELATED INFORMATION
       Creating a TCP Server on page 1585
       NI Service Locator on page 750

Creating a TCP Server

Complete the following steps to create a TCP server using the TCP functions.

   1.  Use the TCP Listen VI or the TCP Create Listener and TCP Wait On Listener functions
       to wait for a connection. You must specify the port and optionally a service name.
       This port or service name must be the same port or service name that the client
      attempts to access.
             •   TCP Listen VI
             •   TCP Create Listener Function
             •   TCP Wait On Listener Function
   2.   If a connection is established, use the TCP Write function to send a message to the
        client. The data must be in a form that the client can accept.
   3.  Use the TCP Read function to read a message from the client.
   4.  Use the TCP Close Connection function to close the connection.

Refer to the following VIs for examples of a TCP server:

    •  labview\examples\Data Communication\Protocols\TCP\TCP
     Named Service\TCP Named Service.lvproj

      RELATED INFORMATION
       Creating a TCP Client on page 1584


                                                    © National Instruments Corporation 1585

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1585 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1586 ordinal=1586 -->
## LabVIEW User Manual

LabVIEW User Manual


     Domains

       Using the Domain Account Manager (Windows)

           Select Tools»Security»Domain Account Manager to display the Domain Account
         Manager. Use the Domain Account Manager to create and destroy a local domain, export
         and import a local domain, add and remove network domains, import a Lookout account,
         and manage domain users and groups.

         The Domain Account Manager includes the following components:

                   •  My Computer —Displays the local domain.
                   •   Network Domains —Lists network domains the administrator configures.
                   •   User list —Lists users in the selected domain.
                   •   Group list —Lists groups in the selected domain.


                 (Windows) To view related topics, click the Locate button, shown at left, in the
                   toolbar at the top of this window. The LabVIEW Help highlights this topic in the
                            Contents tab so you can navigate the related topics.

       Adding a Network Domain (Windows)

         Use the Domain Account Manager to create and destroy a local domain, export and import
         a local domain, add and remove network domains, import a Lookout account, and manage
         domain users and groups.

         Complete the following steps to use the Domain Account Manager to add a network
         domain to the network domain list.

                1.  Select Tools»Security»Domain Account Manager to display the Domain Account
               Manager.
                2.  Select Domain»Browse for Domains or right-click the network domain list and
                   select Browse for Domains from the shortcut menu to display the Browse for
              Domains dialog box.
                3.  Select the network domain you want to manage.
                4.  Click the OK button to close the dialog box. LabVIEW adds the network domain to
                 the network domain list.

         You also can find a network domain by entering the name or IP address of the host
         machine in the Find Domain dialog box. Select Domain»Find Domain or right-click the
          network domain list and select Find Domain from the shortcut menu to display the Find
        Domain dialog box.


1586  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1586 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1587 ordinal=1587 -->
## LabVIEW User Manual

LabVIEW User Manual


To remove a network domain from view, click the network domain and select
Edit»Remove From View or right-click the domain and select Remove From View from
the shortcut menu. Removing a domain from view does not destroy the domain.

Creating a Local Domain (Windows)

Use the Domain Account Manager to create and destroy a local domain, export and import
a local domain, add and remove network domains, import a Lookout account, and manage
domain users and groups.

Complete the following steps to use the Domain Account Manager to create a local
domain on a computer.

   1.  Select Tools»Security»Domain Account Manager to display the Domain Account
      Manager.
          NOTE
                       If a local domain already exists on the computer, the Domain Account
           Manager loads the local domain automatically. To create a new local
             domain, first destroy the existing local domain.
   2.  Select File»New»Local Domain or right-click the domain list and select New Local
     Domain from the shortcut menu to display the Domain Properties dialog box.
   3.  Click the General tab and enter a name for the domain in the Domain text box.
   4.  Click the Passwords tab and configure the minimum and maximum lengths of
      passwords and the password expiration date.


       Note The password length and expiration date apply as the default setting for all
                               user accounts in the domain.


   1.  Click the Access Control tab and add machines or IP addresses to the Grant List or
     Deny List. Select list to activate specifies which list the domain is currently using.
   2.  Click the OK button to display the Change Password dialog box.
   3.  Enter a password for the Administrator account and click the OK button. By default,
      the user name for the account that you are creating is Administrator.


     Note The Domain Account Manager creates a list of built-in users and groups when
      you create a local domain. The built-in users include Administrator and Guest, and
              the built-in groups include Administrators, Guests, and Operators.

Creating and Configuring Domain Groups (Windows)

Use the Domain Account Manager to create and destroy a local domain, export and import
a local domain, add and remove network domains, import a Lookout account, and manage
domain users and groups.


                                                    © National Instruments Corporation 1587

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1587 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1588 ordinal=1588 -->
## LabVIEW User Manual

LabVIEW User Manual


         Complete the following steps to use the Domain Account Manager to create, configure,
         and delete domain groups. You must be logged in to the domain to create, configure, or
           delete groups.

                1.  Select Tools»Security»Domain Account Manager to display the Domain Account
               Manager.
                2.  Click the group list and select File»New»Group or right-click the group list and
                   select New from the shortcut menu to display the Group Properties dialog box.
                3.  Enter the group name in the Group name text box.
                4.  Enter a description in the Description text box.
                5.  Add a user to the group by selecting the user in the Users not in group list and
                   clicking the right arrow button. To remove a user from the group, select a user in the
                Users in group list and click the left arrow button.
                6.  Click the OK button.

         You also can configure domain group properties with the Group Properties dialog box.
            Click the group and select Edit»Properties or right-click the group and select Properties
         from the shortcut menu to display the Group Properties dialog box.

         To delete a domain group, click the group and select Edit»Delete or right-click the group
         and select Delete from the shortcut menu. You cannot delete a built-in group. Deleting a
          group invalidates all previous groups by that name, and entries in the Access Control List
          might become invalid. Even if you recreate a group with the same name, you must add user
          accounts to the new group manually.

       Creating and Configuring Domain Users (Windows)

         Use the Domain Account Manager to create and destroy a local domain, export and import
         a local domain, add and remove network domains, import a Lookout account, and manage
         domain users and groups.

         Complete the following steps to use the Domain Account Manager to create, configure,
         and delete domain users. You must be logged in to the domain to create, configure, or
           delete users.

                1.  Select Tools»Security»Domain Account Manager to display the Domain Account
               Manager.
                2.  Click the user list and select File»New»User or right-click the user list and select
            New from the shortcut menu to display the User Properties dialog box.
                3.  Click the General tab and enter the user name in the User name text box.
                4.  Enter the user's full name in the Full name text box.
                5.  Enter a description in the Description text box.
                6.  Place a checkmark in the Account is locked checkbox if you want to lock a user
                account without removing the user from the domain.
                7.  Click the Change Password button to display the Change Password dialog box.
                8.  Enter and re-type a password for the user and click the OK button.


1588  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1588 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1589 ordinal=1589 -->
## LabVIEW User Manual

LabVIEW User Manual


   9.  Click the Memberships tab and add the new user to a group by selecting the group
       in the Groups user can join list and clicking the right arrow button. To remove the
      user from a group, select a group in User is member of these groups list and click
      the left arrow button.
   10. Click the OK button.

You also can configure domain user properties. Click the user and select Edit»Properties
or right-click the user and select Properties from the shortcut menu to display the User
Properties dialog box and configure user settings.

To delete a domain user, click the user and select Edit»Delete or right-click the user and
select Delete from the shortcut menu. You cannot delete a built-in user. Deleting a user
invalidates all previous users by that name, and entries in the Access Control List might
become invalid. Even if you recreate a user with the same name, the internal user
identification number is different.

Destroying a Local Domain (Windows)

Use the Domain Account Manager to create and destroy a local domain, export and import
a local domain, add and remove network domains, import a Lookout account, and manage
domain users and groups.

Complete the following steps to use the Domain Account Manager to destroy a local
domain. You must log in to the local domain before you can destroy it.

   1.  Select Tools»Security»Domain Account Manager to display the Domain Account
      Manager.
   2.  Click the local domain and select Domain»Destroy Local Domain or right-click the
       local domain and select Destroy Local Domain from the shortcut menu.
   3.  When a dialog box prompts you to confirm that you want to destroy the domain,
        click the Yes button.
   4.  Enter the password in the Enter Administrator Password dialog box and click the
    OK button.

If you cannot destroy a domain through the Domain Account Manager, such as if you do not
have the password for the domain, you can delete the domain directly from the
National Instruments/Shared/Domain directory. You must log on to the


                                                    © National Instruments Corporation 1589

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1589 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1590 ordinal=1590 -->
## LabVIEW User Manual

LabVIEW User Manual


         computer as an administrator to delete files from the National Instruments
            directory.

              RELATED INFORMATION
                 Using the Domain Account Manager (Windows) on page 1586
                  Creating a Local Domain (Windows) on page 1587
                  Exporting and Importing a Local Domain Using the Domain Account Manager
                 (Windows) on page 1590
                 Adding a Network Domain (Windows) on page 1586
                 Importing a Lookout Account (Windows) on page 1591
                  Creating and Configuring Domain Users (Windows) on page 1588
                  Creating and Configuring Domain Groups (Windows) on page 1587
                 Logging In to a Domain (Windows) on page 1592
                 Using the Domain Account Manager (Windows) on page 1586

       Exporting and Importing a Local Domain Using the Domain
       Account Manager (Windows)

         Use the Domain Account Manager to create and destroy a local domain, export and import
         a local domain, add and remove network domains, import a Lookout account, and manage
         domain users and groups.


          Exporting a Local Domain

         Complete the following steps to use the Domain Account Manager to export a local
          domain. You must log in to the local domain before you can export it.

                1.  Select Tools»Security»Domain Account Manager to display the Domain Account
               Manager.
                2.  Select File»Import and Export»Export Local Domain To File or right-click the local
              domain and select Import and Export»Export Local Domain To File from the
                 shortcut menu. A file dialog box appears.
                3.  Navigate to the location where you want to export the local domain.
                4.  Enter a filename for the domain and click the Save button.
                5.  Enter the password in the Enter Administrator Password dialog box and click the
            OK button.


1590  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1590 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1591 ordinal=1591 -->
## LabVIEW User Manual

LabVIEW User Manual


Importing a Local Domain

Complete the following steps to use the Domain Account Manager to import a local
domain.

      NOTE
       You cannot import a domain that already exists on the network.

   1.  Select Tools»Security»Domain Account Manager to display the Domain Account
      Manager.
   2.  Select File»Import and Export»Import Local Domain From File or right-click the
     domain list and select Import and Export»Import Local Domain From File from
      the shortcut menu. A file dialog box appears.
   3.  Select the domain you want to import and click the Open button.

 Note If a local domain already exists on the computer, a dialog box prompts you to save a
 copy of the existing local domain. Click the Yes button to save a copy of the existing local
  domain before you import the new domain. Click the No button to replace the existing
     local domain with the new domain. Click the Cancel button to cancel the import.

   4.  Enter the password in the Enter Administrator Password dialog box and click the
    OK button.

Importing a Lookout Account (Windows)

Use the Domain Account Manager to create and destroy a local domain, export and import
a local domain, add and remove network domains, import a Lookout account, and manage
domain users and groups.

Complete the following steps to use the Domain Account Manager to import a Lookout
account.

   1.  Select Tools»Security»Domain Account Manager to display the Domain Account
      Manager.
   2.  Select File»New»Import Lookout Security File or right-click the domain list and
       select Import Lookout Security File from the shortcut menu to display the Domain
       Properties dialog box.
          NOTE
                       If a local domain already exists on the computer, a dialog box prompts you
              to save a copy of the existing local domain. Click the Yes button to save a
             copy of the existing local domain before you import the Lookout account.
               Click the No button to replace the existing local domain with the Lookout
              account. Click the Cancel button to cancel the import.
   3.  Click the General tab and enter a name for the domain in the Domain text box.
   4.  Click the Passwords tab and configure the minimum and maximum lengths of
      passwords and the password expiration date.


                                                    © National Instruments Corporation 1591

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1591 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1592 ordinal=1592 -->
## LabVIEW User Manual

LabVIEW User Manual


                Note The password length and expiration date apply as the default setting for all
                                          user accounts in the domain.


                1.  Click the Access Control tab and add machines or IP addresses to the Grant List or
              Deny List. Select list to activate specifies which list the domain is currently using.
                2.  Click the OK button to display the Change Password dialog box.
                3.  Enter a password for the Administrator account and click the OK button.
                4.  Enter the default password for all users and click the OK button.

       Logging In to a Domain (Windows)

         Use the Domain Account Manager to create and destroy a local domain, export and import
         a local domain, add and remove network domains, import a Lookout account, and manage
         domain users and groups.

         Complete the following steps to use the Domain Account Manager to log in to a domain.

                1.  Select Tools»Security»Domain Account Manager to display the Domain Account
               Manager.
                2.  Click the domain you want to log in to and select Domain»Log In or right-click the
              domain and select Log In from the shortcut menu to display the Log In to Domain
                  dialog box.
                3.  Enter the user name and password and click the Log In button.

             NOTE
               The login user must be an Administrator or a member of the Administrators group.

         To log out of a domain, click the domain and select Domain»Log Out or right-click the
         domain and select Log Out from the shortcut menu.

              RELATED INFORMATION
                 Using the Domain Account Manager (Windows) on page 1586
                  Creating a Local Domain (Windows) on page 1587
                  Destroying a Local Domain (Windows) on page 1589
                  Exporting and Importing a Local Domain Using the Domain Account Manager
                 (Windows) on page 1590
                 Adding a Network Domain (Windows) on page 1586
                 Importing a Lookout Account (Windows) on page 1591
                  Creating and Configuring Domain Users (Windows) on page 1588
                  Creating and Configuring Domain Groups (Windows) on page 1587


1592  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1592 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1593 ordinal=1593 -->
## LabVIEW User Manual

LabVIEW User Manual


LabVIEW Measurement Concepts
This section provides instructions for performing measurements and controlling
instruments with LabVIEW.
Overview of Virtual Instruments and Measurements

Virtual instrumentation combines hardware and software with industry-standard
computer technologies to create user-defined instrumentation solutions. National
Instruments specializes in developing plug-in and distributed hardware and driver
software for data acquisition (DAQ), IEEE 488 (GPIB), PXI, serial, and industrial
communications. The driver software is the application programming interface (API) to the
hardware and is consistent across National Instruments application software, such as
LabVIEW, LabWindows™/CVI™, and Measurement Studio. These platforms deliver the
sophisticated display and analysis capabilities that virtual instrumentation requires.

You can use virtual instrumentation to create a complete and customized system for test,
measurement, and industrial automation by combining different hardware and software
components. If the system changes, you often can reuse the virtual instrument
components without purchasing additional hardware or software.


Taking Measurements with Virtual Instruments

Different hardware and software components can make up a virtual instrumentation
system. You can use a variety of hardware components to monitor or control a process or
to test a device. If you can connect the hardware to the computer and understand how the
hardware takes measurements, you can incorporate hardware into a virtual
instrumentation system.
Controlling Instruments

You control instruments by sending commands and data between the instrument and the
computer. You can develop various LabVIEW applications to configure and control many
types of instruments.


Choosing Method of Instrument Control

Due to the wide array of instruments and instrument control interfaces, it is important to
choose the proper method of instrument control. The following flowchart can help you
choose the appropriate method of instrument control.


                                                    © National Instruments Corporation 1593

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1593 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1594 ordinal=1594 -->
## LabVIEW User Manual

LabVIEW User Manual


          Using Instrument Drivers

         Use instrument drivers to control and communicate with instrument hardware in a system.
         LabVIEW instrument drivers are sets of VIs that simplify instrument control and reduce test
         program development time by eliminating the need for you to learn the complex, low-level
         programming commands for each instrument.

        When you need easy-to-use drivers with block diagram source code, use LabVIEW Plug and
          Play instrument drivers. LabVIEW Plug and Play instrument drivers include error handling,
           front panels, block diagrams, icons, and help. (Windows) When you need advanced
            functionality such as instrument interchangeability, simulation, and state-caching, use
          Interchangeable Virtual Instruments (IVI) instrument drivers. Refer to IVI on the National
          Instruments Web site for more information about IVI instrument drivers.
      Instruments and DAQ Devices

      General-Purpose DAQ

         A general-purpose DAQ device is a device that acquires or generates data and can contain
           multiple channels. You also can use general-purpose DAQ devices to generate analog
            signals, such as a sine wave, and digital signals, such as a pulse. Typically, you connect
          these devices directly to the internal bus of a computer through a plug-in slot.

         A general-purpose DAQ measurement system is different from other measurement systems
          because the software installed on the computer performs the actual measurements. The
        DAQ device only converts the incoming signal into a digital signal the computer can use.
           This means that the same DAQ device can perform a multitude of measurements simply by
          changing the software application that reads the data. In addition to acquiring the data,
          the application for a DAQ measurement system also uses the software that processes the
          data and displays the results. Although this flexibility allows you to have one hardware
          device for many types of measurements, you must spend more time developing the
            different applications for the different types of measurements. LabVIEW includes many
           acquisition and analysis functions to help you develop different applications.


1594  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1594 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1595 ordinal=1595 -->
## LabVIEW User Manual

LabVIEW User Manual


How Computers Communicate with DAQ Devices

Before a computer-based measurement system can measure a physical signal, such as
temperature, a sensor or transducer must convert the physical signal into an electrical one,
such as voltage or current. The plug-in DAQ device is only one system component of the
entire measurement system. You cannot always directly connect signals to a plug-in DAQ
device. In these cases, you must use signal conditioning accessories to condition the
signals before the plug-in DAQ device converts them to digital information. The software
controls the DAQ system by acquiring the raw data, analyzing, and presenting the results.

A DAQ system has the following options:

    •   The plug-in DAQ device resides in the computer. You can plug the device into the PCI
        slot of a desktop computer or the PCMCIA slot of a laptop computer for a portable
     DAQ measurement system.
    •   The DAQ device is external and connects to the computer through an existing port,
      such as the serial port or Ethernet port, which means you can quickly and easily
      place measurement nodes near sensors.


Software and DAQ Devices

The computer receives raw data through the DAQ device. The application software you
write presents and manipulates the raw data in a form you can understand. The software
also controls the DAQ system by commanding the DAQ device when to acquire data from
channels, and from which channels to acquire the data.

Typically, DAQ software includes drivers and application software. Drivers are unique to the
device or type of device and include the set of commands the device accepts. Application
software, such as LabVIEW, sends the drivers commands, such as a command to acquire
and return a thermocouple reading. The application software also displays and analyzes
the acquired data.

NI measurement devices include NI-DAQ driver software and NI Measurements VIs and
functions that you can use to configure, acquire data from, and send data to the
measurement devices.


NI-DAQ

NI-DAQ 7. x contains two NI-DAQ drivers—Traditional NI-DAQ (Legacy) and NI-DAQmx—each
with its own application programming interface (API), hardware configuration, and
software configuration. NI-DAQ 8.0 and later come with only NI-DAQmx, the replacement
for Traditional NI-DAQ (Legacy).

    •   Traditional NI-DAQ (Legacy) is an upgrade to NI-DAQ 6.9. x, the earlier version of NI-
      DAQ. Traditional NI-DAQ (Legacy) has the same VIs and functions and works the
     same way as NI-DAQ 6.9. x. You can use Traditional NI-DAQ (Legacy) on the same
      computer as NI-DAQmx, which you cannot do with NI-DAQ 6.9. x. However, you
      cannot use Traditional NI-DAQ (Legacy) on Windows Vista.
    •   NI-DAQmx is the latest NI-DAQ driver with new VIs, functions, and development
       tools for controlling measurement devices. The advantages of NI-DAQmx over


                                                    © National Instruments Corporation 1595

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1595 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1596 ordinal=1596 -->
## LabVIEW User Manual

LabVIEW User Manual


                 previous versions of NI-DAQ include the DAQ Assistant for configuring channels and
              measurement tasks for a device; increased performance, including faster single-
                 point analog I/O and multithreading; and a simpler API for creating DAQ
                  applications using fewer functions and VIs than earlier versions of NI-DAQ.
                  NOTE
                      (Windows) LabVIEW supports NI-DAQmx and the DAQ Assistant. (Mac OS X)
                     LabVIEW supports NI-DAQmx Base but not the DAQ Assistant. (Linux)
                     LabVIEW supports NI-DAQmx but not the DAQ Assistant.

           Traditional NI-DAQ (Legacy) and NI-DAQmx support different sets of devices. Refer to Data
           Acquisition (DAQ) Hardware on the National Instruments Web site for the list of supported
           devices.

      Instrument I/O

        Many instruments are external to the computer and do not rely on a computer to take a
         measurement. By connecting instruments to a computer, you can control and monitor the
          instruments programmatically and collect data that you can process further or store in
              files. You can install some instruments in a computer similar to general-purpose DAQ
           devices. These internal instruments are called modular instruments.

          Regardless of how you connect to an instrument, the computer must use a specific
           protocol to communicate with the instrument. How the computer controls the instrument
         and acquires data from the instrument depends on the type of the instrument. GPIB, serial
            port, and PXI are common types of instruments.

           Like general-purpose DAQ devices, instruments digitize data, but they have a special
          purpose or are designed for a specific type of measurement. For standalone instruments,
         you generally cannot modify the software that processes the data and calculates the result
          because the software usually is built into the instrument.

         Because modular instrumentation uses software running on standard PC technology, you
         can modify the behavior of these instruments more easily. For example, with some digital
          multimeter modular instruments, you can program the instruments to acquire a buffer of
          data at a high rate of speed, much like an oscilloscope.


       How Computers Control Instruments

         Computers control instruments by sending commands to the instruments over a bus, such
          as GPIB, PXI, or RS232. For example, you can send a command to the instrument to
         measure a signal and then send another command to send the resulting data over the bus
         back to the computer.


         Instrument Drivers

          Instrument drivers are not required to use an instrument, but can help save you time as
         you develop an application.


1596  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1596 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1597 ordinal=1597 -->
## LabVIEW User Manual

LabVIEW User Manual


Using instrument drivers provides the following advantages:

    •   You can use instrument drivers to quickly build complete systems. Instrument
       drivers receive, parse, and scale the response strings from instruments into scaled
      data that you can use in test programs.
    •   Instrument drivers can reduce software development costs because developers do
      not need to spend time understanding low-level command syntax needed to
      program instruments.
    •   Instrument drivers can help make test programs easier to maintain because
      instrument drivers contain all the I/O for an instrument within one library, separate
      from other code, which is easy to upgrade when or if the hardware changes.

Waveform Control and Digital Waveform Control

Use the waveform control, the digital waveform control, the waveform graph, and the
digital waveform graph to represent the waveforms and digital waveforms you acquire or
generate. LabVIEW represents an analog waveform, such as a sine wave or a square wave,
with the waveform data type by default. A 1D array of waveform data type represents
multiple waveforms. LabVIEW represents a digital waveform with the digital waveform
data type by default.

The waveform and digital waveform controls consist of components that include a start
time, a delta t, the waveform data, and attributes. Use the Waveform VIs and functions to
access and manipulate individual components.

The start time (t0) is a time stamp associated with the first measurement point in the
waveform. Use the start time to synchronize plots on a multi-plot waveform graph or
digital waveform graph and to determine delays between waveforms. Delta t (dt) is the
time interval in seconds between any two points in the signal. The waveform data and the
digital waveform data are the values that represent the waveform. An array of any numeric
data type other than the fixed-point numeric data type can represent analog waveform
data. Generally, the number of data values in the array corresponds directly to the number
of scans from a DAQ device. The digital data type represents a digital waveform and
displays the digital data in a table. Attributes include information about the signal, such as
the name of the signal and the device acquiring the signal. NI-DAQ automatically sets some
attributes for you. Use the Set Waveform Attribute function to set attributes, and use the
Get Waveform Attribute function to read attributes.

      NOTE
            If you convert the waveform data type to the dynamic data type, you can set and
       read attributes of the dynamic data by using the Set Dynamic Data Attributes
       Express VI and the Get Dynamic Data Attributes Express VI, respectively. These
       Express VIs automatically convert the dynamic data type to the waveform data
       type before you can set and read attributes. The dynamic data type is for use with
       Express VIs.


                                                    © National Instruments Corporation 1597

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1597 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1598 ordinal=1598 -->
## LabVIEW User Manual

LabVIEW User Manual


          Displaying Waveforms

         To represent waveform data in the front panel window, use the waveform control or the
         waveform graph. To represent digital waveform data, use the digital waveform control or
          the digital waveform graph.

         Use the waveform control and the digital waveform control to manipulate the t0, dt, and Y
         components of the waveform or to display those components as an indicator. When you
           wire a waveform to a graph, the t0 component is the initial value on the x-axis. The number
           of scans acquired and the dt component determine the subsequent values on the x-axis.
         The data elements in the Y component comprise the points on the plot of the graph.

                 If you want to let a user control a certain component, such as the dt component, create a
           front panel control and wire it to the appropriate component in the Build Waveform
          (Analog Waveform) function.

                 If you want to organize digital waveform data into a digital waveform array, use the Group
            Digital Signals Express VI.


          Using the Waveform Control

         You can use several VIs to accept, operate on, and/or return waveforms. In addition, you
         can wire the waveform data type directly to many controls, including the graph, chart,
          numeric controls, and numeric array controls.

         The AI Acquire Waveform VI acquires a specified number of samples at a specified sample
           rate at a particular time from a single input channel and returns a waveform. The Digital IIR
             Filter VI accepts an array of waveforms and filters the data of each waveform. The AI
         Sample Channel VI acquires a single sample from a channel and returns a single-point
          waveform. The Sine Waveform VI generates a sine waveform, and the AO Generate
         Waveform VI sends a waveform to a device.

         Use the Get Waveform Components (Analog Waveform) function to extract and manipulate
          the components of a waveform you generate. The Negate function negates waveform data
         and plots the results to a graph.


          Using the Digital Waveform Control

         Use the Digital Waveform VIs and functions to manipulate digital data by extracting and
           editing the components of the digital signal. Use the NI-DAQmx VIs on the Digital I/O
           palette to acquire and send a digital signal. The Digital Waveform palette also includes VIs
           that convert analog data to digital signals, search a digital signal for a pattern, append a
             digital signal(s) to another digital signal, and perform other digital tasks.

           Refer to the Taking an NI-DAQmx Measurement in LabVIEW tutorial for more information
          about creating typical DAQ applications.


1598  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1598 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1599 ordinal=1599 -->
## LabVIEW User Manual

LabVIEW User Manual


Data and String Manipulation Techniques

Communicating with instruments involves sending data to instruments and retrieving data
from instruments. You rarely need to format the data sent to or retrieved from the
instrument when using instrument drivers because the instrument driver handles the
formatting for you. However, you might need to format the data when writing VIs to
communicate with instruments.

When you communicate with a message-based instrument, you must format and build the
correct command strings for the instrument to perform the appropriate operation or return
a response.

No standards exist for register-based instrument communication. Each device operates
differently, and the instrument documentation is the best resource for learning how to
program the device.

Typically, a command string, or query, is a combination of text and numeric values. Some
instruments require text-only command strings, requiring you to convert the numeric
values to text and append them to the command string. Similarly, to use the data an
instrument returns in LabVIEW, you must convert the data to a format a VI, function, or
indicator can accept.

(Windows) You can use the Instrument I/O Assistant to send queries to an instrument and
to format the data an instrument returns. Place the Instrument I/O Assistant Express VI on
the block diagram to access the Instrument I/O Assistant.

You can use the Format Into String function to build command strings to send to an
instrument or to append other strings or numeric data types to an initial string.


Formatting Data Retrieved from an Instrument

Just as the commands strings you send to an instrument contain headers and trailers,
most instruments return data with headers and/or trailers. The header usually contains
information such as the number of data points returned or the instrument settings. Trailer
information often contains units or other instrument settings at the end of the data string.
The instrument documentation should describe what header and trailer information to
expect from each data transfer. You must first remove the header and trailer information
before you can display or analyze the returned data in LabVIEW.

You can use String Subset functions to parse the header and trailer information in a string
and display them in string indicators. You can use the Scan From String function to parse
the data from the string.


Waveform Transfers

Instruments also can return data in other formats, such as ASCII, 1-byte binary, and 2-byte
binary formats. The instrument documentation describes available formats and how to
convert each one to usable data.


                                                    © National Instruments Corporation 1599

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1599 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1600 ordinal=1600 -->
## LabVIEW User Manual

LabVIEW User Manual


          ASCII Waveforms

                 If an instrument returns data in ASCII format, you can view the data as a character string.
          However, if you need to manipulate the data in numeric format or if you need to graph the
           data, you must convert the string data to numeric data. As an example, consider a
         waveform composed of 1,024 points and in which each point has a value between 0 and
           255. Using ASCII encoding, you need a maximum of 4 bytes to represent each data value (a
        maximum of 3 bytes for the value and 1 byte for the separator, such as a comma). You need
         a maximum of 4,096 bytes (4 bytes 1,024) plus any header and trailer bytes to represent the
         waveform as an ASCII string. You can use the Fract/Exp String To Number function to
          convert the ASCII string to a numeric array.


          1-Byte Binary Waveforms

        Some instruments do not have the option of sending data in ASCII format or send all
         waveform data in binary format. Because no standard exists for binary format, refer to the
          instrument documentation to determine exactly how the instrument stores the data
           values. One common binary format is 1-byte binary. With this type of data encoding, the
          instrument converts each piece of data to an 8-bit binary value before sending it.

        When you read 1-byte binary data from the bus, the instrument returns the data as a
           character string. However, the characters do not appear to correspond to the expected
           data. LabVIEW interprets the binary numbers as ASCII character values, and displays the
          corresponding characters. For example, if you send the value of 65 as one data value, you
          read the character A from the bus. For a value of 13, no printable ASCII character exists
          because 13 corresponds to an invisible carriage return character.

         You can display these invisible characters in a string indicator by right-clicking the
           indicator and selecting '\'Codes Display from the shortcut menu. The carriage return
           character is \r in the string indicator.

         To use the numeric data in an ASCII string with the Analysis VI or to display the numeric
          data in a graph or chart, you must convert the binary string to a numeric array. If the
          instrument sends a binary string that contains 1,024 1-byte binary encoded values, the
         waveform requires only 1,024 bytes plus any header information. Using binary encoding,
         you need only 1 byte to represent each data value, assuming each value is an unsigned 8-
            bit integer. You can use String Subset functions and the String To Byte Array function to
          convert the binary string to an array of integers.

             NOTE
              When acquiring binary data, extract the data using the data size rather than
                  searching for the first character of the trailer information because that character
                might be part of the binary values.


          2-Byte Binary Waveforms

        When data is in 2-byte binary format, it is binary encoded and sent as ASCII characters
            similar to the 1-byte binary format. However, 16 bits of data, or two ASCII characters,
           represent each data value. Although this format uses twice as much space as the 1-byte
           binary format, it is more efficiently packed than ASCII-formatted data.


1600  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1600 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1601 ordinal=1601 -->
## LabVIEW User Manual

LabVIEW User Manual


As an example, consider an oscilloscope that transfers waveform data in binary notation.
For this example, assume the waveform consists of 1,024 data points where each value is a
2-byte signed integer. Therefore, the entire waveform requires 2,048 bytes plus a 5-byte
header and a 2-byte trailer. After you remove the 5-byte header, use the Unflatten From
String function to convert the waveform string to an array of 16-bit integers.

It is important to know the order of the bytes you receive when data is transferred in 2-byte
binary format. The 2-byte combination qH has the corresponding integer value of 29,000,
but the opposite byte order of Hq has the corresponding integer value of 18,545.

      NOTE
       You can configure the byte order for some instruments, and some instruments
       have a fixed byte order. Refer to the instrument documentation for specific
       instrument byte information.

If you receive the high byte first, you must reverse the order of the bytes before you convert
them to an integer value. Use the Unflatten From String to reverse the byte order.

Comparing DAQ Devices and Computer-Based
Instruments for Data Acquisition

The fundamental task of all measurement systems is the measurement and/or generation
of real-world physical signals. Measurement devices help you acquire, analyze, and present
the measurements you take.

Through data acquisition, you acquire and convert physical signals, such as voltage,
current, pressure, and temperature, into digital formats and transfer them into the
computer. Popular methods for acquiring data include plug-in DAQ and instrument
devices, GPIB instruments, PXI (PCI eXtensions for Instrumentation) instruments, and
RS232 instruments.

Through data analysis, you transform raw data into meaningful information by using curve
fitting, statistical analysis, frequency response, or other numerical operations.

      NOTE
      Many of these operations are available only in the LabVIEW Full and Professional
       Development Systems.

Through data presentation, you display data in a graph, thermometer, table, or other visual
display.

Configuring DAQ Devices, Instruments, and Other
Devices

You can configure DAQ devices, instruments, and other devices to control the device or
instrument using an I/O control. After you configure the device or instrument, configure the
I/O control to pass Traditional NI-DAQ (Legacy) virtual channels, NI-DAQmx resources (such


                                                    © National Instruments Corporation 1601

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1601 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1602 ordinal=1602 -->
## LabVIEW User Manual

LabVIEW User Manual


          as tasks, channels, and scales), IVI logical names, VISA resource names, FieldPoint I/O
           points, or Motion resource names to I/O VIs to communicate with an instrument or a
         measurement device.

         The NI-DAQ driver software provides LabVIEW with a high-level interface to National
          Instruments DAQ devices. Driver software, such as NI-DMM, NI-SCOPE, NI-FGEN, and NI-
         SWITCH, provides LabVIEW with high-level interfaces to modular instrumentation. Use
            driver software such as NI-488.2, NI-VISA, and Interchangeable Virtual Instruments (IVI) to
         communicate with stand-alone instruments. The LabVIEW VIs call into the driver software,
         which communicates with the measurement devices. Refer to the DAQ Getting Started
          Guide for more information about installing NI-DAQmx.


          Configuring Devices and Instruments Using MAX and the DAQ Assistant
         (Windows)

         You can use MAX to configure the following items:

                   •   Traditional NI-DAQ (Legacy) virtual channels
                   •    IVI logical names
                   •   VISA resource names
                   •   FieldPoint I/O points
                   •   Motion resource names

             NOTE
                You can access MAX on multiple platforms, but LabVIEW supports the DAQ
                   Assistant on Windows only. You cannot use Traditional NI-DAQ (Legacy) on
               Windows Vista.

         To launch MAX, you can select Tools»Measurement & Automation Explorer or double-
            click the NI MAX icon on the desktop. You also can create a new Traditional NI-DAQ
           (Legacy) virtual channel from the front panel by right-clicking the traditional DAQ channel
           control and selecting New Channel from the shortcut menu.

             NOTE
               The Measurement & Automation Explorer option is available only if you install
                Measurement & Automation Explorer.

         You can right-click an IVI logical name, FieldPoint IO point, VISA resource name, or Motion
          resource name control and select Allow Undefined Names from the shortcut menu to
           enter logical names you have not configured in MAX or another configuration utility. You
           also can use the Allow Undefined Names property to programmatically configure the IVI
            logical name control to accept undefined IVI logical names.

         You can right-click the VISA resource name or Motion resource name control and select
          Allow Multiple Names from the shortcut menu to configure the controls to allow the user
           to enter more than one resource name.

         The DAQ Assistant allows you to create and configure the following for NI-DAQmx.


1602  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1602 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1603 ordinal=1603 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Tasks
    •   Global channels
    •   Scales

Refer to the Using NI-DAQmx Name Controls book for more information about configuring
tasks, channels, and scales for NI-DAQmx.


Configuring Devices and Instruments Using Other Utilities (Mac OS X and
Linux)

You can use the configuration utilities for the instrument. Refer to the instrument
documentation for information about the configuration utilities. You also can configure I/O
controls to pass VISA resource names that have not been configured.
Types of Instruments

Types of Instruments

When you use a PC to automate a test system, you are not limited to the type of instrument
you can control. You can mix and match instruments from various categories. The most
common categories of instrument interfaces are GPIB, serial, and modular instruments.
Additional types of instruments include image acquisition, motion control, USB, Ethernet,
parallel port, NI-CAN, and other devices.

When you use PCs to control instruments, you need to understand properties of the
instrument, such as the communication protocols to use. Refer to the instrument
documentation for information about the properties of an instrument.

GPIB Communication

GPIB, or General Purpose Interface Bus, instruments offer test and manufacturing
engineers the widest selection of vendors and instruments for general-purpose to
specialized vertical market test applications. GPIB instruments are often used as stand-
alone benchtop instruments where measurements are taken by hand. You can automate
these measurements by using a PC to control the GPIB instruments.

Use instrument drivers and the VISA VIs to control GPIB instruments. When you use the
VISA VIs, you need to know the instrument address. Use the VISA resource name control or
MAX on Windows to verify communication with the instrument and determine the
instrument address. You also need to know the command set for the instrument. Most
instruments use SCPI, or Standard Commands for Programmable Instruments: a single,
comprehensive command set suitable for all instruments. Refer to the NI Developer Zone
for more information about common instrument commands and protocols.

The GPIB protocol categorizes devices as controllers, talkers, or listeners to determine
which device has active control of the bus. Each device has a unique GPIB primary address
between 0 and 30. The Controller defines the communication links, responds to devices


                                                    © National Instruments Corporation 1603

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1603 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1604 ordinal=1604 -->
## LabVIEW User Manual

LabVIEW User Manual


           that request service, sends GPIB commands, and passes/receives control of the bus.
           Controllers instruct Talkers to talk and to place data on the GPIB. You can address only one
          device at a time to talk. The Controller addresses the Listener to listen and to read data
         from the GPIB. You can address several devices to listen.

         The GPIB is a digital, 24-conductor parallel bus. The GPIB uses an 8-bit parallel, byte-serial,
          asynchronous data transfer scheme, which means that whole bytes are sequentially
         handshaked across the bus at a speed that the slowest participant in the transfer
          determines. Because the unit of data on the GPIB is a byte, the messages transferred are
           frequently encoded as ASCII character strings. Refer to the GPIB documentation for more
          information about the hardware specifications of GPIB devices.

         You can obtain faster data rates with HS488 devices and controllers. HS488 is an extension
           to GPIB that most NI controllers support.

           Refer to the NI Developer Zone for more information on communicating with GPIB
           instruments.

      Modular Instruments

          NI modular instruments are high-speed hardware products that include the functionality of
        many traditional benchtop instruments for test and measurement. NI modular instruments
           include high-speed digitizers, signal generators, high-speed digital I/O devices, high-
          frequency (RF) devices, digital multimeters (DMMs), programmable power supplies and
          source measure units (SMUs), and switches. NI modular instrument platforms include PCI,
          PCI Express, PXI, PXI Express, SCXI, and USB.

         You can use the instrument drivers that ship with NI modular instruments products to
           create custom measurement applications and user interfaces. Each instrument driver
           includes a palette of LabVIEW VIs that you can use to control a modular instrument from
          LabVIEW.

         Because NI modular instruments combine flexible, user-defined software and scalable,
          general-purpose hardware components, you can modify measurements as your needs
          change. For example, you can make modifications to your program or substitute one
          instrument for another. You also can create custom measurements and define the
          algorithms used to make those measurements.

           Refer to Modular Instruments at ni.com for more information about NI modular
           instruments.

       Serial Port Communication

            Serial communication transmits data between a computer and a peripheral device, such as
         a programmable instrument or another computer. Serial communication uses a
           transmitter to send data one bit at a time over a single communication line to a receiver.
         Use this method when data transfer rates are low or you must transfer data over long
           distances. Most computers have one or more serial ports, so you do not need any extra
         hardware other than a cable to connect the instrument to the computer or to connect two
         computers to each other.


1604  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1604 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1605 ordinal=1605 -->
## LabVIEW User Manual

LabVIEW User Manual


You must specify four parameters for serial communication: the baud rate of the
transmission, the number of data bits that encode a character, the sense of the optional
parity bit, and the number of stop bits. A character frame packages each transmitted
character as a single start bit followed by the data bits.

Baud rate is a measure of how fast data moves between instruments that use serial
communication.

Data bits are transmitted upside down and backwards, which means that inverted logic is
used and the order of transmission is from least significant bit (LSB) to most significant bit
(MSB). To interpret the data bits in a character frame, you must read from right to left and
read 1 for negative voltage and 0 for positive voltage.

An optional parity bit follows the data bits in the character frame. The parity bit, if present,
also follows inverted logic. This bit is included as a means of error checking. You specify
ahead of time for the parity of the transmission to be even or odd. If you choose for the
parity to be odd, the parity bit is set in such a way so the number of 1s add up to make an
odd number among the data bits and the parity bit.

The last part of a character frame consists of 1, 1.5, or 2 stop bits that are always
represented by a negative voltage. If no further characters are transmitted, the line stays in
the negative (MARK) condition. The transmission of the next character frame, if any, begins
with a start bit of positive (SPACE) voltage.


Rate of Data Transfer

You can calculate the maximum transmission rate in characters per second for a given
communication setting by dividing the baud rate by the bits per character frame.


Serial Hardware Overview

The following examples are the most common recommended standards of serial port
communication:

    •   RS232 (ANSI/EIA-232 Standard) is used for many purposes, such as connecting a
      mouse, printer, or modem. It also is used with industrial instrumentation. Because
       of improvements in line drivers and cables, applications often increase the
      performance of RS232 beyond the distance and speed in the standards list. RS232 is
       limited to point-to-point connections between PC serial ports and devices.
    •   RS422 (AIA RS422A Standard) uses a differential electrical signal as opposed to the
      unbalanced (single-ended) signals referenced to ground with RS232. Differential
       transmission, which uses two lines each to transmit and receive signals, results in
       greater noise immunity and longer transmission distances as compared to RS232.
    •   RS485 (EIA-485 Standard) is a variation of RS422 that allows you to connect up to 32
      devices to a single port and define the necessary electrical characteristics to ensure
      adequate signal voltages under maximum load. With this enhanced multidrop
       capability, you can create networks of devices connected to a single RS485 serial
       port. The noise immunity and multidrop capability make RS485 an attractive choice
       in industrial applications that require many distributed devices networked to a PC
       or other controller for data collection and other operations.


                                                    © National Instruments Corporation 1605

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1605 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1606 ordinal=1606 -->
## LabVIEW User Manual

LabVIEW User Manual


         Connecting a Serial Device

                 If you have a serial device in a system, you first must obtain the pinout for that device and
        make sure you have the correct cable to connect the serial device to the computer.
          Determine if the device is data communications equipment (DCE) or data terminal
         equipment (DTE) and what settings it uses to communicate—baud rate, data bits, stop bits,
            parity, or handshaking (flow control).


         More Information About Serial Communication

           Refer to the NI Developer Zone for more information on communicating with Serial
           instruments.

       Ethernet Communication

         You can use NI-VISA to communicate with Ethernet devices, such as NI LXI-based
           instruments. Ethernet devices are used within measurement systems for tasks such as
           general networking and remote data storage.

           Refer to the NI Developer Zone for information on communicating with Ethernet
          instruments using NI-VISA.

     USB Communication

         You can use NI-VISA to communicate with a USB device. Universal Serial Bus (USB) is a
         message-based communication bus. Each USB device has its own command set. You can
          use VISA Read and VISA Write functions to send these commands to an instrument and
          read the response from an instrument.

           Refer to the NI Developer Zone for information on communicating with USB instruments
          using NI-VISA.

              RELATED INFORMATION
                 Using VISA in LabVIEW on page 1616

      Other Types of Communication

            In addition to instrument drivers, you can use the Instrument I/O Assistant to communicate
          with message-based instruments and graphically parse the response. For example, you can
          use the Instrument I/O Assistant to send a query to an instrument to verify communication
          with that instrument.

                 If you do not create an instrument driver, use VISA to control GPIB, serial, USB, Ethernet,
             LXI, PXI, or VXI instruments. VISA is a standard API that you can use to control a wide range
           of instruments. VISA makes the appropriate driver calls depending on the type of


1606  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1606 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1607 ordinal=1607 -->
## LabVIEW User Manual

LabVIEW User Manual


instrument you use so you do not have to learn instrument-specific communication
protocols.

Use NI-488.2 to develop and debug an application program. The NI-488.2 driver has high-
level commands that automatically handle all bus management, so you do not have to
learn the programming details of the GPIB hardware board or the IEEE 488.2 protocol. Low-
level commands are also available for maximum flexibility and performance.

Use the instrument and device drivers provided on the National Instruments Device Drivers
DVD to control NI modular instruments and devices for industrial automation, such as NI-
CAN.

      RELATED INFORMATION
       Using VISA in LabVIEW on page 1616
       GPIB Communication on page 1603
        Serial Port Communication on page 1604
      USB Communication on page 1606
       Ethernet Communication on page 1606
       Modular Instruments on page 1604

Instrument Drivers

Using Instrument Drivers

An instrument driver is a set of high-level functions that control and communicate with
instrument hardware in a system. In LabVIEW, an instrument driver is a set of VIs that
communicate with an instrument using LabVIEW built-in VISA I/O functions. Each VI
corresponds to a programmatic operation, such as configuring, reading from, writing to,
and triggering an instrument. LabVIEW instrument drivers simplify instrument control and
reduce test program development time by eliminating the need for you to learn the
complex, low-level programming commands for each instrument. You also can control
instruments directly.

The Instrument Driver Network contains instrument drivers for a variety of programmable
instruments that use the GPIB, Ethernet, serial, and other interfaces. You also can search
for National Instruments drivers at NI Drivers and Updates on the National Instruments
Web site. You can use an instrument driver for a particular instrument as is. However,
LabVIEW Plug and Play instrument drivers are distributed with their block diagram source
code, so you can customize them for a specific application. You can create instrument
control applications and systems by programmatically linking instrument driver VIs on the
block diagram. Use the NI Instrument Driver Finder to search for and install LabVIEW Plug
and Play instrument drivers without leaving the LabVIEW development environment.
Select Tools»Instrumentation»Find Instrument Drivers or Help»Find Instrument
Drivers to launch the Instrument Driver Finder.

LabVIEW instrument drivers usually use VISA functions to communicate with instruments.
You can use VISA for many different instrument types, such as GPIB, serial, USB, LXI, PXI,


                                                    © National Instruments Corporation 1607

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1607 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1608 ordinal=1608 -->
## LabVIEW User Manual

LabVIEW User Manual


         and VXI. Once you learn how to use VISA for one type of instrument, you do not have to
           learn a different way to communicate when you use another type of instrument. You do
         have to learn about the specific command set for the two instruments, but the method by
         which you send and receive the commands does not change.

             NOTE
                You can use the Instrument I/O Assistant to communicate with message-based
                  instruments and graphically parse the response.

          NI provides more than 8,000 instrument drivers from more than 275 vendors. Refer to the
          Instrument Driver Network on the National Instruments Web site for a list of available
          instrument drivers. You also can search for National Instruments drivers at NI Drivers and
         Updates on the National Instruments Web site.

         You can search for and install existing LabVIEW instrument drivers.

                 (Windows) To view related topics, click the Locate button, shown at left, in the
                   toolbar at the top of this window. The LabVIEW Help highlights this topic in the
                            Contents tab so you can navigate the related topics.

      Types of Instrument Drivers

         You can use Plug and Play and Interchangeable Virtual Instrument (IVI) driver types to
           control instruments in LabVIEW. National Instruments considers drivers Certified or
           Noncertified depending on if they meet specific requirements.


          Plug and Play Instrument Drivers

         A LabVIEW Plug and Play instrument driver is a set of VIs that controls and communicates
          with a programmable instrument. Each VI corresponds to a programmatic operation, such
          as configuring, reading from, writing to, or triggering an instrument. LabVIEW Plug and Play
          instrument drivers include error handling, front panels, block diagrams, icons, and help.
         Because LabVIEW Plug and Play drivers maintain a common architecture and interface, you
         can quickly connect to and communicate with an instrument with very little or no code
          development. Project-style drivers take advantage of the LabVIEW project and library. You
         can use project-style drivers in the same way as previous LabVIEW Plug and Play drivers.

         Use the NI Instrument Driver Finder to search for and install LabVIEW Plug and Play
          instrument drivers without leaving the LabVIEW development environment. Select
          Tools»Instrumentation»Find Instrument Drivers or Help»Find Instrument Drivers to
          launch the Instrument Driver Finder. If you want to download IVI and contributed drivers,
          use the Instrument Driver Network. You also can search for National Instruments drivers at
          NI Drivers and Updates on the National Instruments Web site.


            IVI Instrument Drivers

           National Instruments IVI drivers are sophisticated, DLL-based drivers developed in
         LabWindows™/CVI™ that allow for simulation and instrument interchangeability. You do


1608  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1608 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1609 ordinal=1609 -->
## LabVIEW User Manual

LabVIEW User Manual


not have to rewrite an application to use it with a similar instrument type. For example,
you can write a VI that works with several different brands of oscilloscopes, even if those
oscilloscopes use different bus connections. To achieve interchangeability, the IVI
Foundation, which develops IVI standards, defines specifications for the following
instrument classes: DMM, oscilloscope, arbitrary waveform/function generator, DC power
supply, switch, power meter, spectrum analyzer, and RF signal generator. Use IVI drivers for
the following additional benefits: instrument state caching for improved performance,
multithread safety, and instrument attribute access. Refer to IVI on the National
Instruments Web site for more information about IVI instrument drivers.

To convert an instrument driver written in LabWindows/CVI, download the LabVIEW
Instrument Driver Import Wizard from the National Instruments Web site.

Finding and Installing Instrument Drivers

Use the NI Instrument Driver Finder to search for and install LabVIEW Plug and Play
instrument drivers without leaving the LabVIEW development environment. Select
Tools»Instrumentation»Find Instrument Drivers or Help»Find Instrument Drivers to
launch the Instrument Driver Finder.

If you want to download an IVI driver or browse for noncertified drivers, you can download
instrument drivers from the Instrument Driver Network. You also can download National
Instruments drivers from NI Drivers and Updates on the National Instruments Web site.

LabVIEW installs instrument driver files to the labview\instr.lib directory. Access
the instrument driver VIs installed to this directory on the Instrument Drivers palette.

      NOTE
       To install, create, or modify instrument drivers, the labview\instr.lib
        directory must have read and write access.

Accessing Instrument Driver VIs

The Instrument Driver VIs are located on the Instrument Drivers palette.


Organization of Instrument Driver

The following illustration shows the organization of a typical instrument driver.


                                                    © National Instruments Corporation 1609

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1609 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1610 ordinal=1610 -->
## LabVIEW User Manual

LabVIEW User Manual


          Typical Instrument Driver Components

         Most instrument drivers have menu palettes that include the following components.

                   •   The Initialize VI, the first instrument driver VI you call, establishes communication
                 with the instrument. Additionally, it can perform any necessary actions to place the
                instrument in its default power on state or in another specific state. Generally, you
               need to call the Initialize VI only once at the beginning of an application.
                   •   The Configuration, Action, Data, and Utility VIs provide numerous functionalities to
                  control and communicate with the instrument.
                   •   The Close VI terminates the software connection to the instrument and frees system
                  resources. Generally, you need to call the Close VI only once at the end of an
                  application or when you finish communication with an instrument. Make sure that
                    for each successful call to the Initialize VI, you use a matching Close VI to avoid
                 maintaining unnecessary memory resources.

         Use the NI Example Finder to search or browse for project-style instrument driver
          examples. You can find non-project style instrument driver examples in the Instrument
          Drivers palette and subpalettes.

        Many instrument drivers have a VI Tree VI you can use to view the entire instrument driver
           hierarchy. The VI Tree VI is a non-executable VI that illustrates the functional structure of
          the instrument driver.

         You can test instrument driver VIs to interactively determine the appropriate instrument
           configuration settings.

       Getting Started with Instrument Drivers

         To verify communication with an instrument and test a typical programmatic instrument
           operation, open an instrument driver example VI. Look over each of the controls and set
         them appropriately. Generally, with the exception of the resource name control, the
           defaults for most controls will be sufficient for the first run. You will need to set the
          resource name appropriately.

         Use the NI Example Finder to search or browse for project-style instrument driver
          examples. You can find non-project style instrument driver examples in the Instrument
          Drivers palette and subpalettes.

            After running the VI, check to see that the VI returned reasonable data and did not report
         an error in the error cluster. Instrument driver examples most commonly fail for one of the
           following reasons:

                   •   NI-VISA is not installed. You install NI-VISA from the National Instruments Device
                  Drivers DVD.
                   •   The resource name is incorrect. The instrument driver example VI requires you to
                  specify the correct resource for the instrument. Instruments that are powered on at
               LabVIEW launch time appear in the VISA resource name pull-down menu. If the


1610  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1610 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1611 ordinal=1611 -->
## LabVIEW User Manual

LabVIEW User Manual


      instrument does not appear in this list, launch Measurement & Automation Explorer
       to configure the device.
    •   The instrument driver does not support the exact model you are using. You might
      need to double-check that the instrument driver supports the instrument model
      you are using.

After you have verified basic communication with the instrument using the example VI, you
might want to customize instrument control for your application. If the application
requirements are similar to the example VI, the simplest means of creating a customized VI
is to save a copy of the example VI by selecting Save As from the File menu. You can
change the default values in the front panel window by selecting Edit»Make Current
Values Default. Block diagram changes might include changing the constants wired to the
instrument driver subVIs.

Interactively Testing Instrument Driver VIs

You might want to test instrument driver VIs interactively before you include them in an
application. Testing instrument driver VIs helps to select appropriate instrument
configuration settings. To run the driver VIs from their front panels, you must first run the
Initialize VI. For subsequent VIs, you must first select the resource name from the VISA
resource name pull-down menu.

After you have selected a resource, you can interactively run the driver VI from the front
panel multiple times without resetting the resource selection.

In general, you should run the instrument driver VIs in the order you want to call them in
the application. First you run the Initialize VI, followed by one or more configuration VIs. If
you are using a trigger for the measurement, you might need to call an action VI to arm the
trigger. Calls to data VIs then collect the measured value(s). When you are finished testing
the instrument driver component VIs, you should run the Close VI to deallocate resources.

Creating Instrument Control Applications

Instrument drivers include many component VIs for use in building an instrument control
application. Wire the VIs together similar to a typical LabVIEW application.


Establishing Communication

The Initialize VI, the first instrument driver VI you call, establishes communication with the
instrument. Additionally, it can perform any necessary actions to place the instrument in
its default power on state or in another specific state. Generally, you need to call the
Initialize VI only once at the beginning of an application.

      NOTE
      Use the resource name and resource name out terminals to connect the Initialize VI
        to subsequent VIs that interact with or close the instrument.


                                                    © National Instruments Corporation 1611

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1611 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1612 ordinal=1612 -->
## LabVIEW User Manual

LabVIEW User Manual


           Interacting with the Instrument

         The Configuration VIs are a collection of software routines that configure the instrument to
          perform the operation you want. Numerous Configuration VIs can exist, depending on the
            particular instrument. After you call these VIs, the instrument is ready to take
         measurements or to simulate a system.

         The Action VIs initiate or terminate test and measurement operations, such as arming the
            trigger system or generating a stimulus. Action VIs are different from Configuration VIs
          because they do not change the instrument settings but order the instrument to carry out
         an action based on its current configuration. The Status VIs obtain the current status of the
          instrument or the status of pending operations.

         The Data VIs transfer data to or from the instrument. Examples include VIs for reading a
         measured value or waveform and VIs for downloading waveforms or digital patterns to a
          source instrument.

         The Utility VIs perform a variety of operations that are auxiliary to the most often used
          instrument driver VIs. These VIs include the majority of the instrument driver template VIs,
          such as reset, self-test, revision, error query, and error message. The Utility VIs might also
           include other custom instrument driver VIs that perform operations such as calibration or
           storage and recall of setups.


          Closing the connection

         The Close VI terminates the software connection to the instrument and frees system
           resources. Generally, you need to call the Close VI only once at the end of an application or
        when you finish communication with an instrument. Make sure that for each successful call
           to the Initialize VI, you use a matching Close VI to avoid maintaining unnecessary memory
           resources.


          Error Handling

                It is important to perform error handling in instrument control applications because there
           are several potential sources for errors.

      Modifying an Existing Instrument Driver


         You might want to modify an existing driver to optimize the code. In general, you should
          optimize only those VIs that are called repeatedly in a loop. Configuration VIs generally are
           called only once and have little effect on application speed.

          Follow the Instrument Driver Modification Instructions to modify an existing instrument
            driver.

                 If you need to modify only one or two VIs, consider renaming each VI by selecting
          File»Save As and selecting the Rename option in the Save As dialog box. After you modify


1612  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1612 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1613 ordinal=1613 -->
## LabVIEW User Manual

LabVIEW User Manual


the name, you can modify the block diagram and front panel controls. Most changes to the
block diagram should affect the String functions.

If you need to modify several VIs and the existing driver is a project-style driver, consider
creating a new driver using the existing driver as the starting point. Select
Tools»Instrumentation»Create Instrument Driver Project to launch the Create New
Instrument Driver Project wizard and create a new driver using the existing driver as the
source.

If you intend to submit the modified driver to National Instruments for certification, refer to
the NI Developer Zone for more information on Instrument Driver Certification.

Creating Instrument Drivers


Before you build an instrument driver, you can check for existing drivers for the instrument
you are using. You can search for existing drivers using the NI Instrument Driver Finder, the
manufacturer's Web site, and the Instrument Driver Network on the National Instruments
Web site. You also can search for National Instruments drivers at NI Drivers and Updates on
the National Instruments Web site.

Use the Create New Instrument Driver Project wizard to create a new instrument driver
project. Select Tools»Instrumentation»Create Instrument Driver Project to launch the
Create New Instrument Driver Project wizard. After creating the new instrument driver,
follow the Instrument Driver Modification Instructions to complete the driver.

Use the Instrument Driver VI Wizard to create an instrument driver VI for an instrument
driver project. Right-click a LabVIEW instrument driver project library .lvlib in the
Project Explorer window and select New»Instrument Driver VI from the shortcut menu to
launch the Instrument Driver VI Wizard.

      NOTE
       To install, create, or modify instrument drivers, the labview\instr.lib
        directory must have read and write access.

Instrument Control Error Handling

It is important to perform error handling in instrument control applications because there
are several potential sources for errors. Error handling with instrument driver VIs is similar
to error handling with other I/O VIs in LabVIEW. Each instrument driver VI contains an error
in input and an error out output for passing error clusters from one VI to another. The error
cluster contains a Boolean flag that indicates if an error occurred, an error code number,
and a string that contains the location of the VI where the error occurred.

    •   VISA functions can return errors because VISA or the underlying software or
      hardware is not properly installed. For example, when communicating with GPIB
       instruments, NI-488.2 must be installed correctly to use a National Instruments GPIB
       controller card. Similarly, if the board is not installed or is not correctly configured,
      the instrument driver VIs return an error.


                                                    © National Instruments Corporation 1613

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1613 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1614 ordinal=1614 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   VISA functions can return errors if the device you are accessing is not responding to
                 the commands you have sent. The instrument could be incorrectly addressed,
                 malfunctioning, or unable to understand the commands that are being sent.

         Use the Simple Error Handler or General Error Handler VIs to detect and report these errors
            in an application.
     Measurement Applications

       Creating a Typical DAQ Application

         Use the I/O controls on the I/O and Classic I/O palettes to specify the instrument or device
          resource you want to communicate with. Use the VIs on the Measurement I/O palette to
          develop DAQ applications.

         Complete the following basic programmatic steps to create a DAQ application.

                1.  Configure the measurement hardware.
                2.  Create tasks and channels.
                3.  (Optional) Set timing.
                4.  (Optional) Set triggering.
                5.  Read or write data.
                6.  Clear.

           Notice that timing and triggering are optional. Include the timing step if you want to
           specify hardware timing instead of software timing. If you are using NI-DAQmx, you can use
          the DAQ Assistant to set timing parameters for a task.

             NOTE
                (Windows) LabVIEW supports NI-DAQmx and the DAQ Assistant. (Mac OS X)
                LabVIEW supports NI-DAQmx Base but not the DAQ Assistant. (Linux) LabVIEW
                 supports NI-DAQmx but not the DAQ Assistant.

         Use triggering if you want the device to acquire samples only when certain conditions are
          met. For example, you might want to acquire samples if the input signal goes higher than 4
              V. If you are using NI-DAQmx, you can use the DAQ Assistant to configure triggering for a
            task.

        Many NI-DAQmx applications also can include steps to start, stop, and clear the task. For
          example, for applications that use a counter/timer to count edges or to measure period,
          use the Start VI to arm the counter.

            In NI-DAQmx, LabVIEW clears the task automatically when the VI hierarchy that created the
           task finishes executing.


1614  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1614 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1615 ordinal=1615 -->
## LabVIEW User Manual

LabVIEW User Manual


Traditional NI-DAQ (Legacy) and NI-DAQmx include VIs for timing, triggering, reading, and
writing samples. Use the Data Acquisition VIs and Functions to acquire data from DAQ
devices. To use these VIs, you must have the NI-DAQ driver software and DAQ hardware
installed. After you acquire data, you can use the built-in Signal Processing, Report
Generation, and Mathematics VIs and functions to analyze, generate reports, and perform
mathematical operations on that data.

You can use the NI-DAQmx properties to extend the functionality of the NI-DAQmx VIs.

Many of the Traditional NI-DAQ (Legacy) and NI-DAQmx VIs are polymorphic and can accept
or return data of various types, such as scalar values, arrays, or waveforms. You use other
polymorphic NI-DAQmx VIs to configure various triggers and methods of sample timing,
and to create virtual channels. By default, NI-DAQmx VIs appear with the polymorphic VI
selector.


Physical and Virtual Channels

A physical channel is a terminal or pin at which you can measure or generate an analog or
digital signal. Every physical channel on a device that supports NI-DAQmx has a unique
name.

A virtual channel is a collection of property settings that can include a name, a physical
channel, input terminal connections, the type of measurement or generation, and scaling
information. In Traditional NI-DAQ (Legacy) and earlier versions, configuring virtual
channels is an optional way to record which channels are being used for different
measurements, but virtual channels are integral to every NI-DAQmx measurement.


Tasks

A task in NI-DAQmx is a collection of one or more virtual channels with timing, triggering,
and other properties. A task represents a measurement or a generation you want to
perform. You can set up and save all of the configuration information in a task and use the
task in an application.

In NI-DAQmx, you can configure virtual channels as part of a task or separate from a task.

Complete the following steps to perform a measurement or a generation with a task.

   1.  Create a task and channels.
   2.  (Optional) Configure the channel, timing, and triggering properties.
   3.  Read or write samples.
   4.  Clear the task.

Repeat steps 2 and 3, if it is appropriate for the application. For example, after reading or
writing samples, you can reconfigure the channel, timing, or triggering properties and then
read or write additional samples based on this new configuration.


                                                    © National Instruments Corporation 1615

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1615 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1616 ordinal=1616 -->
## LabVIEW User Manual

LabVIEW User Manual


       Creating a Typical FieldPoint Application

         Use the I/O controls on the I/O and Classic I/O palettes to specify the instrument or device
          resource with which you want to communicate. Use the VIs on the FieldPoint palette to
          develop FieldPoint distributed I/O applications. Most FieldPoint applications require only
          the FP Read VI and the FP Write VI. The FP Read VI returns data from the FieldPoint I/O
          channel or group of channels the FieldPoint IO Point function represents. The FP Write VI
          sends data to the FieldPoint I/O channel or group of channels the FieldPoint IO Point
           function represents. You also can use properties to extend the functionality of FieldPoint
            VIs programmatically.


         Channels versus Items

           FieldPoint modules consist of physical I/O points called channels. Items represent the
          channels or groups of channels. You can create items in Measurement & Automation
           Explorer (MAX) and use the FieldPoint I/O Point control to access the items in LabVIEW.


          Using the FieldPoint I/O Point Control

         Use the FieldPoint I/O Point control to communicate with the FieldPoint items you create
            in MAX. Place the FieldPoint I/O Point control in the front panel window. Right-click the
           control and select the items you want to read from or write to from the shortcut menu. If
         you do not see the FieldPoint items you want, configure the items in MAX.

      Using Properties with Measurement Applications

         You can write most measurement applications using only the VIs of the NI-DAQmx, NI-VISA,
         and IVI Instrument Driver APIs. You also can use properties with these APIs to extend the
            functionality to include less commonly used features. For example, you can use the VISA
          Configure Serial Port VI to set several commonly used serial port settings in a VISA Session,
           including the baud rate. However, if you want to change only the baud rate, you can use a
          Property Node.

         Use the Property Node on the DAQmx palette to configure various low-level settings for NI-
         DAQmx. Use the Property Node on the VISA Advanced palette for any VISA property. Use
          the Property Nodes on the Modular Instrument palette and the IVI Instrument Drivers
           palette for these APIs, respectively.
      VISA in LabVIEW

      Using VISA in LabVIEW

          VISA is a standard I/O API for instrumentation programming.


1616  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1616 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1617 ordinal=1617 -->
## LabVIEW User Manual

LabVIEW User Manual


Versatility of VISA

VISA can control GPIB, serial, USB, Ethernet, PXI, or VXI instruments, making the
appropriate driver calls depending on the type of instrument you use so you do not have to
learn instrument-specific communication protocol. It is platform independent, bus
independent, and environment independent. In other words, the same API is used
regardless of device type, platform, or programming language.

Before you begin using VISA, make sure you choose the appropriate method of instrument
control.


Message-Based Communication

GPIB, serial, USB, Ethernet, and some VXI instruments use message-based communication.
You program message-based instruments with high-level ASCII character strings. The
instrument has a local processor that parses the command strings and sets the appropriate
register bits to perform the operations you want. The Standard Commands for
Programmable Instruments (SCPI) standardizes the ASCII command strings used to
program compliant instruments. Similar instruments often use similar commands. Instead
of learning different command messages for each type of instrument from each
manufacturer, you need to learn only one command set. The most common message-
based functions are VISA Read, VISA Write, VISA Assert Trigger, VISA Clear, and VISA Read
STB.


Register-Based Communication

PXI and many VXI instruments use register-based communication. You program register-
based instruments at a low level using binary information that you write directly to the
instrument control registers. Speed is the advantage of this type of communication
because the instrument no longer needs to parse the command strings and convert the
information to register-level programming. Register-based instruments literally
communicate at the level of direct hardware manipulation. The most common register-
based functions are VISA In, VISA Out, VISA Move In, and VISA Move Out.

        (Windows) To view related topics, click the Locate button, shown at left, in the
        toolbar at the top of this window. The LabVIEW Help highlights this topic in the
                  Contents tab so you can navigate the related topics.

Selecting a Resource Name

The front panel of most instrument driver VIs includes a VISA resource name control and a
VISA resource name out indicator. These controls and indicators pass session information
between instrument driver subVIs. The VISA resource name identifies the resource on
which the VI operates. It also differentiates between different sessions of the instrument
driver.

VISA resource name is a unique identifier reference to a device I/O session. It identifies the
device with which the VI communicates and passes all necessary configuration information
required to perform the I/O.


                                                    © National Instruments Corporation 1617

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1617 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1618 ordinal=1618 -->
## LabVIEW User Manual

LabVIEW User Manual


          VISA resource name out contains the same identifier information as VISA resource name.
                It passes the reference out of the VI and into other subsequent VIs that access the same
           instrument. Wiring VISA resource names together establishes data dependencies.

         You select the VISA resource name in the Initialize VI from the VISA resource name pull-
        down menu. Instruments that are powered on and connected to your computer are visible
            in the VISA resource name pull-down menu. If the instrument does not appear in this list,
           enter the instrument descriptor using the following format:

        Interface Type[board index]::Address::INSTR. Examples resource
        names: GPIB: GPIB::22::INSTR, GPIB board 0, primary address 22
        Serial: COM1 TCP/IP Instr: TCPIP::10.0.32.48::INSTR TCP/IP
        Socket: TCPIP::10.0.32.45::3800::SOCKET

          (Windows) Use MAX to determine the available resources and instrument addresses and set
            aliases.

       Verifying VISA Communication

         To verify that VISA and the device driver are installed correctly and VISA detects the
           instrument, first view the resource names that appear in the VISA resource name pull-
        down menu. If no resource names appear in this list, VISA or the device driver might not be
            installed correctly. (Windows) Use Measurement & Automation Explorer to configure and
            test instrument communication. If resource names appear in the VISA resource name pull-
        down menu, but a particular instrument does not appear in the list, you might have a cable
          connection problem.

                 If VISA is installed correctly and VISA detects the instrument, but you receive errors when
         you run the instrument control application, you must identify what sequence of VIs
          produces the error in LabVIEW. If you are using an instrument driver, try to run each VI
            interactively and verify that each control is set appropriately.

          NI I/O Trace is a tool for monitoring instrument I/O communications while your application
           runs. You can use NI I/O Trace to capture instrument I/O calls and their results while
         LabVIEW VIs run. Capturing calls and their results can help you debug problems with
          instrument communications. Select Tools»Instrumentation»NI I/O Trace to launch NI I/O
           Trace. (Windows) You also can select Start»All Programs»National Instruments»NI I/O
          Trace to launch NI I/O Trace. (Mac OS X) You also can select Applications»National
          Instruments»NI I/O Trace and double-click the NI I/O Trace icon to launch NI I/O Trace.
            (Linux) You also can type niiotrace in the command line to launch NI I/O Trace.

       Creating a Typical VISA Application

         Use the I/O controls on the I/O and Classic I/O palettes to specify the instrument or device
          resource with which you want to communicate.


1618  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1618 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1619 ordinal=1619 -->
## LabVIEW User Manual

LabVIEW User Manual


VISA Functions and Properties

Use the VIs and functions on the VISA palette to build VIs that control instruments. Use VISA
properties to extend the functionality of VISA VIs programmatically. Before you begin using
VISA, make sure you choose the appropriate method of instrument control.

For most simple instrument applications, you need only two VISA functions, VISA Write and
VISA Read. Refer to the Simple Serial VI in the labview\examples\Instrument IO
\Serial directory for an example of how to use VISA functions.

   Open example    Find related examples

Use the VIs in the VISA Advanced VIs and functions palette to build advanced VISA VIs. Refer
to the folders in the labview\examples\Instrument IO\VISA directory for
examples of using advanced VISA VIs.

Refer to the labview\examples\Instrument IO\GPIB\GPIB.lvproj for
examples of using VISA VIs with GPIB devices.

   Open example    Find related examples

LabVIEW Shared Libraries
This section provides information on using shared libraries in LabVIEW.
Calling Shared Libraries

A shared library is a file containing executable program modules that any number of
different programs can use to perform some function. You can call these program modules,
or shared library functions, from LabVIEW by using the Call Library Function Node. Call a
shared library function when you want to accomplish any of the following tasks:

    •   Using functions written in another programming language within LabVIEW
    •   Performing tasks that LabVIEW cannot perform with its own functions and VIs, such
      as calling system routines
    •   Completing tasks that are better suited for text-based languages


Shared Libraries on Different Platforms

(Windows) A shared library is called a DLL.

(OS X) A shared library is called a Framework.

(Linux) A shared library is called a Shared Library function.


                                                    © National Instruments Corporation 1619

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1619 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1620 ordinal=1620 -->
## LabVIEW User Manual

LabVIEW User Manual


          General Approach to Calling Shared Libraries

           Calling a shared library function in LabVIEW includes the following actions:

                1.  You obtain or create a shared library.
                2.  You configure a Call Library Function Node to call a function within the shared
                     library.
                3.  LabVIEW calls the function when the Call Library Function Node executes.
                4.  LabVIEW passes input data from the block diagram to the executable code.
                5.  LabVIEW returns data from the executable code to the block diagram.


          Limitations on Calling Shared Libraries in LabVIEW

                   •   Shared libraries must use either the stdcall or C calling convention. You can use
               any language to write shared libraries as long as the shared libraries can be called
                 using one of these two calling conventions.
                   •   Shared libraries execute synchronously. You cannot reset a VI that is running a
                shared library until execution completes. If you want to write a shared library that
                performs a long task, be aware that LabVIEW cannot perform other tasks in the
              same thread while the shared library executes.
                   •   VIs that call shared libraries are platform specific. VIs that call functions within
                shared libraries execute on different platforms only if you have a corresponding
                    library for each platform. If you move a VI that call a shared library with a Call
                  Library Function Node to another platform, you must update the node to specify the
                 version of the shared library that is compiled for the new platform.

         Examples and troubleshooting information help you build and use shared libraries and
           successfully configure the Call Library Function Node in LabVIEW. The general methods
          described here for DLLs also apply to other types of shared libraries. Refer to the labview
        \examples\dll directory for examples of using shared libraries.

       Configuring the Call Library Function Node

         Use the Call Library Function Node to directly call a 32-bit Windows DLL, a OS X
         Framework, or a Linux Shared Library function. With this node, you can create an interface
            in LabVIEW to call existing libraries or new libraries specifically written for use with
          LabVIEW. National Instruments recommends using the Call Library Function Node to create
         an interface to external code.

             NOTE
               Be aware when using the Call Library Function Node or writing code that is called
                by the Call Library Function Node that LabVIEW reserves Windows messages
             WM_USER through WM_USER+99 for internal use only.

            Right-click the Call Library Function Node and select Configure from the shortcut menu to
           display the Call Library Function dialog box. Use the Call Library Function dialog box to


1620  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1620 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1621 ordinal=1621 -->
## LabVIEW User Manual

LabVIEW User Manual


specify the library, function, parameters, return value for the node, calling conventions,
and function callbacks on Windows. When you click the OK button in the Call Library
Function dialog box, LabVIEW updates the Call Library Function Node according to your
settings, displaying the correct number of terminals and setting the terminals to the
correct data types.

      NOTE
            If you want to run applications or shared libraries created with different versions of
       LabVIEW on the same computer, the computer must have a version of the LabVIEW
       Run-Time Engine that is compatible with each version of LabVIEW used to create
       the applications or shared libraries.


Configuring Library Name or Path

You must specify either the name of the shared library or the path to the shared library on
disk. However, these two techniques produce different consequences when you distribute
or relocate your VIs and applications.

      CAUTION
      Do not specify the location of a system shared library, such as kernel32.dll,
       by path. Because LabVIEW automatically includes by-path shared libraries in build
        specifications, you might distribute a by-path system shared library to another
       computer inadvertently. Redistributing some shared libraries, such as
      kernel32.dll, might cause the target computer to crash. Therefore, always
        specify system shared libraries by name.

If you want to run applications or shared libraries created on different platforms, use the *
wildcard to make the reference to the shared library platform independent. Use * for the
file extension and * or ** to the left of the file extension, depending on how you name 32-
bit and 64-bit libraries.

The following example illustrates how to use the * wildcard.

 Example                                     Translation

                 LabVIEW replaces the reference with the appropriate file extension to
 myshared.*    match the platform that is running the Call Library Node, for example,
               myshared.dll, myshared.so, and myshared.framework.
                   LabVIEW replaces the reference with myshared32.* on 32-bit
                    platforms and myshared64.* on 64-bit platforms. You can place
 myshared*.*       the * anywhere to the left of the file extension. For example,
                 my*shared.* can translate to my32shared.*. LabVIEW
                              replaces .* with the appropriate file extension.
                    LabVIEW replaces the reference with myshared.* on 32-bit
                   platforms and myshared_64.* on 64-bit platforms. You can place
 myshared**.*      the ** anywhere to the left of the file extension. For example,
                my**shared.* can translate to my_64shared.*. LabVIEW
                              replaces .* with the appropriate file extension.


                                                    © National Instruments Corporation 1621

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1621 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1622 ordinal=1622 -->
## LabVIEW User Manual

LabVIEW User Manual


             NOTE
               Keep the C++ compiler from introducing platform dependence in exported
                  function names through a process called name mangling by using the C++
                 compiler function export directive, extern "C"{}, in your header file.

          Related Information

           Specifying the Location of Shared Libraries on Disk


          Configuring for Multiple Thread Operation

            In a multithreaded operating system, you can make multiple calls to a DLL or shared library
           simultaneously. You can select the thread to execute the library call from the Thread
           section on the Function tab of the Call Library Function dialog box. The thread options
           are Run in UI thread and Run in any thread. If you select Run in UI thread, the Call
           Library Function Node switches from the thread the VI is currently executing in to the user
            interface thread. If you select Run in any thread, the Call Library Function Node continues
            in the currently executing thread. By default, all Call Library Function Nodes run in the user
            interface thread.

          Before you configure a Call Library Function Node to run in any thread, make sure that
           multiple threads can call the function simultaneously. In a shared library, code can be
          considered thread-safe when:

                   •     It does not store any global data, such as global variables, files on disk, and so on.
                   •     It does not access any hardware. In other words, the code does not contain register-
                   level programming.
                   •     It does not make any calls to any functions, shared libraries, or drivers that are not
                 thread safe.
                   •     It uses semaphores or mutexes to restrict access to global resources.
                   •     It is called by only one non-reentrant VI.

             NOTE
                       All calls to LabVIEW-built shared libraries should specify Run in any thread. If you
                  configure the Call Library Function Node using LabVIEW-built shared libraries and
                   specify Run in UI thread, LabVIEW might hang and require you to restart.

          Related Information

           Multitasking, Multithreading, and Multiprocessing


          Setting the Calling Convention

           Calling conventions define the way to pass information from a piece of code to a function.
         Use the Calling convention control on the Function tab of the Call Library Function
           dialog box to select the calling convention for the function. The default calling convention
              is C. The C calling convention allows variable-length parameter lists.


1622  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1622 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1623 ordinal=1623 -->
## LabVIEW User Manual

LabVIEW User Manual


(Windows) You also can use the standard Windows calling convention, stdcall. The
number of parameters passed to the function is fixed.

Refer to the documentation for the DLL you want to call for the appropriate calling
conventions.

      CAUTION
       Using the incorrect calling convention can cause an irregular shutdown of
       LabVIEW.


Configuring Parameters

This section discusses the return value and how to add parameters to the Call Library
Function Node.

To configure parameters for the Call Library Function Node, navigate to the Parameters
tab of the Call Library Function dialog box. Initially, the Call Library Function Node has no
parameters and has a return type of Void.

As you configure parameters, the Function Prototype text box displays the C prototype for
the function you are building. This text box is a read-only display.

      NOTE
            If a type library is found, the parameters are updated to match the parameters
       found in the type library for the selected function. The order of the parameters
      must match the prototype of the function found in the library.

The return type for the Call Library Function Node returns to the right terminal of the top
terminal. If the return type is Void, the top terminal is unused. Each additional pair of
terminals corresponds to a parameter in the Parameters list of the Call Library Function
Node. To pass a value to the Call Library Function Node, wire to the left terminal of a
terminal pair. To read the value of a parameter after the Call Library Function Node call,
wire from the right terminal of a terminal pair. The following illustration shows a Call
Library Function Node that has a return type of Void, a string parameter, and a numeric
parameter.


Configuring Return Type

For return type, you can set Type to Void, Numeric, or String. Void is only available for
return type and is not available for other parameters. Use Void for the return type if your
function does not return any values.


                                                    © National Instruments Corporation 1623

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1623 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1624 ordinal=1624 -->
## LabVIEW User Manual

LabVIEW User Manual


         Even if the function you call returns a value, you can use Void for the return type. When the
           function returns a value and you select Void as the return type, the value returned by the
           function is ignored.

             NOTE
               The function you are calling can return a C string pointer. If you want to deallocate
                  the pointer, you must do so explicitly as LabVIEW does not automatically
                   deallocate the C string pointer for you.

                 TIP
                             If the function you are calling returns a data type not listed, choose a return data
                 type the same data size as the one returned by the function. For example, if the
                  function returns a char data type, use an 8-bit unsigned integer. A call to a function
                    in a DLL cannot return a pointer because there are no pointer types in LabVIEW.
                 However, you can specify the return type as an integer that is the same size as the
                    pointer. LabVIEW then treats the address as a simple integer, and you can pass it to
                   future DLL calls.

          Related Information

           String Return Type


         Adding and Deleting Parameters

         To add parameters to the Call Library Function Node, navigate to the Parameters tab of
          the Call Library Function dialog box. Click the Add a parameter button. To remove a
          parameter, click the Delete the selected parameter button. To change the order of the
          parameters, use the Move the selected parameter up one and Move the selected
         parameter down one buttons to the right of the parameter list.


          Editing Parameters

           Select the parameter from the Parameters list to edit the data type or parameter name.
         You can edit the parameter name to something more descriptive, which makes it easier to
           distinguish between parameters. The parameter name does not affect the call, but it is
          propagated to output wires. Also, you can edit all fields in the Current parameter section
            for the selected parameter.


          Selecting the Parameter Type

         Use the Type pull-down menu to indicate the data type of each parameter. You can select
         from the following parameter types:

                   •   Numeric
                   •   Array
                   •   String
                   •   Waveform


1624  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1624 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1625 ordinal=1625 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Digital Waveform
    •   Digital Data
    •   ActiveX
    •   Adapt to Type
    •   Instance Data Pointer

      NOTE
            If the library function expects a data type not included in the previous list, you
      must convert the LabVIEW data into the type the function expects. Common data
       types that require conversion include structures, arrays containing pointers to
       other data, and pointers to callback functions.

After you select an item from the Type pull-down menu, you see more items you can use to
indicate details about the parameter and about how to pass the data to the library
function. The Call Library Function Node has a number of different items for parameter
types because of the variety of data types required by different libraries. Refer to the
documentation for the library you call to determine which parameter types to use.

The following sections discuss the different parameter types available from the Type pull-
down menu.

(Windows) Refer to the labview\examples\Connectivity\Libraries and
Executables\Libraries and Executables.lvproj for an example of using
data types in shared libraries.

Related Information

Calling Functions That Expect Other Data Types


Numeric

For numeric data types, you must indicate the exact numeric type by using the Data Type
pull-down menu. You can choose from the following data types:

    •    8-, 16-, 32-, 64-bit, and pointer-sized signed and unsigned integers
    •   4-byte, single-precision numbers
    •   8-byte, double-precision numbers

If you use pointer-sized integers, the Call Library Function Node adapts to the specific
operating system it is being executed on and passes data of the appropriate size to and
from the library function. LabVIEW represents the data in 64 bits and, on 32-bit platforms,
translates the numeric data types to 32-bit integer types.

      NOTE
       You can pass extended-precision numbers and complex numbers by selecting
      Adapt to Type from the Type pull-down menu. However, standard libraries
        generally do not use extended-precision numbers and complex numbers.


                                                    © National Instruments Corporation 1625

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1625 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1626 ordinal=1626 -->
## LabVIEW User Manual

LabVIEW User Manual


         Use the Pass pull-down menu to indicate whether you want to pass the value or a pointer
           to the value.


          Array

         Use the Data Type pull-down menu to indicate the data type of the array. You can choose
         from the same data types available for numeric parameters.

           Specify the dimensions of the array in Dimensions.

         Use the Array Format pull-down menu to make one of the following choices:

                   •   Array Data Pointer —passes a pointer to the array data, allowing the called library
                  to access the array data as the specified data type of the array data.
                   •   Array Handle —passes a pointer to a pointer that points to a four-byte value for
               each dimension, followed by the data.
                   •   Array Handle Pointer —passes a pointer to an array handle.

         Use the Minimum size control to have LabVIEW check at run time that the memory
         LabVIEW allocated for an array data pointer is at least the Minimum size. To indicate the
        Minimum size of a 1D array, you can enter a numeric value, or, if you configure an integer
          parameter in the Parameters list, you can select the parameter from the pull-down menu.
           This option is available only for array data pointers.

             NOTE
                             If you pass in an array that is smaller than the Minimum size, LabVIEW enlarges the
                     size of the array to the minimum. However, if you pass in an array that is bigger
                 than the minimum, the array retains the larger size.

              CAUTION
              Do not attempt to resize an array with system functions, such as realloc. Doing
                 so might crash your system. Instead, use one of the memory manager functions,
                such as NumericArrayResize.

          Related Information

        Memory Manager Functions

          NumericArrayResize Function


           String

         Use the String Format pull-down menu to indicate the string format. You can choose from
          the following string formats:

                   •  C String Pointer —a string followed by a null character.


1626  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1626 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1627 ordinal=1627 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Pascal String Pointer —a string preceded by a length byte.
    •   String Handle —a pointer to a pointer to four bytes for length information, followed
      by string data.
    •   String Handle Pointer —a pointer to an array of string handles.

Select a string format that the library function expects. Most standard libraries expect
either a C string or a Pascal string. If the library function you are calling is written for
LabVIEW, you might want to use the String Handle format. When configuring a Pascal
string pointer, you must wire a value to the string input on the block diagram. That value
must be initialized with enough characters to hold any new string that may be written to
that Pascal string. When configuring a C string pointer, you have two options:

    •   Wire a value to the string input that is initialized with enough characters to hold any
     new string that may be written to that string.
    •   Specify the string size in the Minimum size pull-down menu on the Parameters tab
       of the Call Library Function dialog box.

Use the Minimum size control to have LabVIEW check at run time that the memory
LabVIEW allocated for a C string pointer is at least the Minimum size. To indicate the
Minimum size of a string, you can enter a numeric value, or, if you configure an integer
parameter in the Parameters list, you can select the parameter from the pull-down menu.
This option is available only for C string pointers.

      NOTE
            If you pass in a string that is smaller than the Minimum size, LabVIEW enlarges the
         size of the string to the minimum. However, if you pass in a string that is bigger
       than the minimum, the string retains the larger size.

      CAUTION
      Do not attempt to resize an array with system functions, such as realloc. Doing
       so might crash your system. Instead, use one of the memory manager functions,
       such as NumericArrayResize.


Waveform

When you call a shared library that includes a waveform data type, you do not have to
specify a numeric value from the Data Type pull-down menu; the default is 8-byte Double.
However, you must specify Dimensions. If the parameter is a single waveform, specify
Dimensions as 0. If the parameter is an array of waveforms, specify Dimensions as 1.
LabVIEW does not support an array of waveforms greater than one-dimensional.

      NOTE
        Pointer-sized signed and unsigned integers are not available in the Data Type pull-
      down menu for waveforms.


                                                    © National Instruments Corporation 1627

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1627 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1628 ordinal=1628 -->
## LabVIEW User Manual

LabVIEW User Manual


           Digital Waveform

           Specify Dimensions as 0 if the parameter is a single digital waveform. Specify Dimensions
          as 1 if the parameter is an array of digital waveforms. LabVIEW does not support an array of
             digital waveforms greater than one-dimensional.


           Digital Data

           Specify Dimensions as 1 if the Parameter is an array of digital data. Otherwise, specify
         Dimensions as 0. LabVIEW does not support an array of digital data greater than one-
          dimensional.

             NOTE
                You can pass waveforms, digital waveforms, and digital data through shared
                      libraries, but you cannot access the data inside the shared libraries.


          ActiveX

           Select one of the following items from the Data Type pull-down menu:

                   •   ActiveX Variant Pointer —passes a pointer to ActiveX data.
                   •   IDispatch* Pointer —passes a pointer to the IDispatch interface of an ActiveX
               Automation server.
                   •   IUnknown* Pointer —passes a pointer to the IUnknown interface of an ActiveX
               Automation server.

          Related Information

          Using ActiveX with LabVIEW


         Adapt to Type

         Use Adapt to Type to pass arbitrary LabVIEW data types to DLLs in the following ways:

                   •   Scalars are passed by reference. A pointer to the scalar is passed to the library.
                   •   Arrays and strings are passed according to the Data Format setting. You can choose
               from the following Data Format settings:
                         ◦   Handles by Value passes the handle to the library. The handle is not NULL.
                         ◦   Pointers to Handles passes a pointer to the handle to the library. If the
                      handle is NULL, treat the handle as an empty string or array. To set a value
                  when the handle is NULL, you must allocate a new handle.
                         ◦   Array Data Pointer passes a pointer to the first element of the array,
                        allowing the called library to access the array data as the data type of the
                         array data.


1628  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1628 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1629 ordinal=1629 -->
## LabVIEW User Manual

LabVIEW User Manual


            ◦   Interface to Data allows you to inspect LabVIEW data and data type
             information in C++ code. For more information about this setting, refer to the
         ILVDataInterface.idl and ILVTypeInterface.idl files in the
         labview\cintools directory.
    •   Clusters are passed by reference.
    •   Scalar elements in arrays or clusters are in line. For example, a cluster containing a
      numeric is passed as a pointer to a structure containing a numeric.
    •   Clusters within arrays are in line.
    •   Strings and arrays within clusters are referenced by a handle.

      NOTE
      When one or more of the parameters of the function you want to call in a DLL are of
       types that do not exist in LabVIEW, ensure that each parameter is passed to the
        function in a way that allows the DLL to correctly interpret the data. Create a
        skeleton .c file from the current configuration of the Call Library Function Node.
      By viewing the .c file, you can determine whether LabVIEW will pass the data in a
      manner compatible with the DLL function. You then can make any necessary
       adjustments.

Related Information

Completing the.c File


Instance Data Pointer

Use Instance Data Pointer to access data allocated for each instance of the Call Library
Function Node. The Instance Data Pointer references a pointer sized allocation that you
may use at your own discretion. This allocation is also passed to each of the callback
functions on the Callbacks tab.


Configuring Callbacks

When you configure a Call Library Function Node to call a function, you can use the
Callback tab to specify other functions within the same library to call at the following
times:

    •   Reserve time—When the top-level VI that causes the Call Library Function Node to
      execute begins executing. Specify a Reserve callback when you need to perform
        initialization tasks before the primary function executes.
    •   Unreserve time—When the top-level VI that caused the Call Library Function Node
       to execute stops executing. Specify an Unreserve callback when you save or analyze
      information or carry out clean-up operations.
    •   Abort—The specified function executes if the VI that called the primary function
       aborts.


                                                    © National Instruments Corporation 1629

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1629 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1630 ordinal=1630 -->
## LabVIEW User Manual

LabVIEW User Manual


          Instance Data Pointer Instance Data Pointer
             NOTE
                You cannot use the Callback tab to pass callback functions as parameters to library
                   functions. The Call Library Function Node cannot directly call library functions that
                   require a callback function as a parameter, but you can create a wrapper library to
                implement such calls.


           Calling Functions That Expect Other Data Types

         You might encounter a function that expects data in a form that the Call Library Function
        Node cannot pass. Specifically, the Call Library Function Node does not support structures
           or arrays containing a pointer to other data or structures containing flat arrays that can be
           variably sized. You can call a function that expects an unsupported data type in the
           following ways:

                   •     If the data contains no pointers, you might be able to use the Flatten To String
                 function to create a string containing the binary image of the data required and pass
                    this string as a C string pointer. You will probably want to use the byte order input
                  to Flatten To String to specify that the data be flattened in native byte order.
                   •   Write a library function that accepts the data in the form used by LabVIEW and
                  builds the data structure expected by the other library. This function then can call
                 the other library and retrieve any returned values before returning. Your function
                     will probably accept the data from the block diagram as Adapt to Type, so that any
                 block diagram data type can be passed.
                   •     If the function expects a callback function as a parameter, complete the following
                 steps to call the function from LabVIEW.
                        1.  Write a wrapper library that defines at least two new functions:
                                 ◦  A wrapper function that accepts from LabVIEW any data required by
                             the original function. This wrapper function must call the original
                                function, passing the data from LabVIEW as well as a callback function
                               that you define in the same wrapper library.
                                 ◦   The callback function that you want to pass to the original function.
                        2.  Call the wrapper function with the Call Library Function Node.

          Related Information

           Flatten To String Function


          Configuring Error Checking

         Use error checking to ensure no errors occur if you call a DLL or shared library with the Call
           Library Function Node.

         The Maximum and Default controls on the Error Checking tab of the Call Library Function
           dialog box allow LabVIEW to recover from unhandled exceptions that occur in the
           configuration of the Call Library Function Node or during a call to a shared library or DLL.


1630  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1630 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1631 ordinal=1631 -->
## LabVIEW User Manual

LabVIEW User Manual


The Disabled control on the Error Checking tab disables error checking but improves the
execution speed of the Call Library Function Node.

If you use the Call Library Function Node to call a shared library generated by LabVIEW, the
node automatically calls the LVDLLStatus function embedded in the shared library. For
these LabVIEW-generated shared libraries, this function detects certain errors, including
the following:

    •   A VI inside the shared library uses licensed features that are not installed on the
       target computer.
    •   A VI inside the shared library uses a Call Library Function Node whose associated
      shared library is not installed on the target computer.
    •   The VIs inside the shared library were compiled using the SSE2 optimizations but
      the target computer does not support SSE2 instructions.

In these cases, the Call Library Function Node returns error 1003.

Specifying the Location of Shared Libraries on Disk

To call a shared library with the Call Library Function node, you must specify
either the name of the shared library or the path to the shared library on disk. However,
these two techniques produce different consequences when you distribute or relocate your
VIs and applications. Use the following table to determine which technique addresses your
particular use case.

 Technique                                                    Basis of for                                                                      Effects on                     Relevant use cases           Search Specifying                                                           Distribution                                                Algorithm Location

             The shared library is in the system                                                         LabVIEW does not                search path. Common examples                                              System      include the shared                 include system shared libraries, By name                                          search      library automatically                such as kernel32.dll, and                                                  algorithm           in build                     third party shared libraries                                                                           specifications.              designed for componentized reuse.

                                                            LabVIEW             The shared library is private to your                                                                    automatically                       VI. Common examples include   The path you By path                                                         includes the shared                shared libraries that you wrote       specify                                                                             library in build                    specifically for a particular VI.                                                                           specifications.


To specify the location of a shared library, you can enter the name or path in the Library
name or path text box of the Call Library Function dialog box. You can also wire the name
or path to the path in input of the Call Library Function Node.


                                                    © National Instruments Corporation 1631

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1631 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1632 ordinal=1632 -->
## LabVIEW User Manual

LabVIEW User Manual


              CAUTION
              Do not specify the location of a system shared library, such as kernel32.dll,
                by path. Because LabVIEW automatically includes by-path shared libraries in build
                    specifications, you might distribute a system shared library to another computer
                    inadvertently. Redistributing some shared libraries, such as kernel32.dll,
                might cause the target computer to crash. Therefore, always specify system shared
                     libraries by name.


       Common Problems Loading a Shared Library by Name

                 If LabVIEW cannot locate a shared library by name, consider the following possible causes:

                   •   To locate shared libraries that you specify by name, LabVIEW uses a modified
                 version of the system search algorithm defined by your operating system. Refer to
                 the Related information for more about how LabVIEW shared library directories are
               used by the Call Library Function node.
                   •   Specifying a shared library by name is not the same as specifying a relative path to a
                shared library within the same directory as the calling VI. To specify the latter,
                 enter ./ shared library name as the path to the shared library.


       Common Problems Loading a Shared Library by Path

                 If LabVIEW cannot locate a shared library by path, consider the following possible causes:

                   •     If you use a relative path to specify the location of the shared library, LabVIEW
                   interprets the path relative to the location of the VI on disk.
                   •     If you use an absolute path to specify the location of the shared library, LabVIEW
                 saves the relative location of the shared library rather than the absolute path.
                  Therefore, if you change the location of the shared library relative to the VI, LabVIEW
                cannot locate the shared library and must search for it.


       How LabVIEW Locates Missing Shared Libraries

                 If LabVIEW cannot locate a shared library that you specified either by name or by path,
         LabVIEW searches the VI search path for the missing shared library. If LabVIEW finds the
          shared library, it updates the path to the shared library within the Call Library Function
           dialog box.

          Searching for missing shared libraries requires extra time, displays an unavoidable search
           dialog box, and causes unsaved changes in the calling VI that you must save yourself.


1632  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1632 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1633 ordinal=1633 -->
## LabVIEW User Manual

LabVIEW User Manual


Therefore, configure VIs with the correct name or path information for shared libraries
whenever possible.

      NOTE
       You can configure stand-alone applications to search for shared libraries in specific
        locations on a target computer by using a .ini file. Refer to the Related
        information for more about how to change the VI search path for LabVIEW
        executables.

      RELATED INFORMATION
        Call Library Function Node
        Call Library Function Dialog Box
       Paths Page (Options Dialog Box)
       LabVIEW Shared Library Directories Used by Call Library Function Node
     How Can I Change or Set the VI Search Path for LabVIEW Executables?

Calling External APIs

You might need to access external APIs from within LabVIEW code. Most often, you access
external APIs to obtain functionality that the operating system provides. Normally, you can
use the LabVIEW Call Library Function Node to accomplish this goal. You must provide the
following information to the Call Library Function Node to access external APIs from within
LabVIEW code:

    •   Function name as it appears in the library
    •   Function prototype
    •   Library or module in which the function resides
    •   Calling conventions of the function
    •   Thread-safe status of the function

      CAUTION
      Do not specify the location of a system shared library, such as kernel32.dll, by
        path. Because LabVIEW automatically includes by-path shared libraries in build
        specifications, you might distribute a system shared library to another computer
        inadvertently. Redistributing some shared libraries, such as kernel32.dll,
       might cause the target computer to crash. Therefore, always specify system shared
         libraries by name.


                                                    © National Instruments Corporation 1633

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1633 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1634 ordinal=1634 -->
## LabVIEW User Manual

LabVIEW User Manual


       Common Pitfalls with the Call Library Function Node

         The function reference documentation for any API should provide most of the information
           that the Call Library Function Node requires. However, you should keep in mind the
        common errors listed in this section.

             NOTE
                  Configure the Call Library Function Node to return an error when some of the
                       pitfalls described below occur by selecting the Maximum or Default control on the
                  Error Checking tab of the Call Library Function dialog box.


           Incorrect Function Name

          Your library call can fail when the name of the function as it appears in the library is
            different than is expected. Usually this error occurs due to function name redefinition, or to
           function name decoration, as in the following examples:

                   •   Redefinition —This pitfall appears when an API manufacturer uses a define
               mechanism, such as #define directive in ANSI C, to define an abstracted function
             name to one of many functions present in the library, based on some external
                 condition such as language or debug mode. In such cases, you can look in the
                header .h file for the API to determine whether a #define directive redefined the
             name of a function you want to use.
                   •   Function Name Decoration —This pitfall appears when certain functions have their
              names decorated when they are linked. A typical C compiler tracks name
                  decoration, and when it looks for a function in a shared library, it recognizes the
                decorated name. However, because LabVIEW is not a C compiler, it does not
                 recognize decorated names. If you suspect that function name decoration is causing
                     difficulty, inspect the shared library’s exported functions. If the function name that
                appears in the function prototype section has characters such as @ appended to it,
                 the function was decorated when the DLL was built. This is most common with C++
                 compilers. In LabVIEW, the Function name control in the Call Library Function
                  dialog box is a pull-down menu where you can access a list of all functions within
                 the library you have selected. In addition, most operating systems have a utility you
               can use to view a library’s exports, for example, QuickView on the Windows
                 operating system and the nm command on most Linux systems. If the Function
            name list contains entries but the function you want to call does not appear in the
                         list, the most likely reason is that the function has not been exported. Refer to the
               documentation for your compiler for information about how to mark functions for
                  export.


         Data Types

          Your library call can fail when you do not use the correct data types. LabVIEW only supports
           basic numeric data types and C strings. Also, you can select Adapt to Type from the Type
          pull-down menu of the Call Library Function dialog box and direct LabVIEW to pass its
        own internal data types for a given parameter. You might encounter the following specific
          problems:


1634  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1634 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1635 ordinal=1635 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Non-Standard Data Type Definitions —Frequently, other APIs use non-standard
       definitions for data types. For example, instead of using char, short, and long,
      the Windows API uses BYTE, WORD, and DWORD. If an API that you are using makes
      use of such data types, you need to find the equivalent basic C data type so that you
      can properly configure the Call Library Function Node.
    •   Structure and Class Data Types —Some APIs have structure and, in the case of C++,
       class data types. LabVIEW cannot use these data types. If you need to use a function
       that has a structure or class as an argument, you should write a shared library
      wrapper function that takes as inputs the data types that LabVIEW supports and
       that appropriately packages them before LabVIEW calls the desired function.
    •   ActiveX Objects —If you want to call a shared library that contains ActiveX objects,
      use the Automation Open function with the Property Node and the Invoke Node
       instead of the Call Library Function Node.

(Windows) Refer to the labview\examples\Connectivity\Libraries and
Executables\Libraries and Executables.lvproj for an example of using
data types in shared libraries.


Constants

Your library call can fail when your external code uses identifiers in place of constants.
Many APIs define identifiers for constants to make the code easier to read. LabVIEW must
receive the actual value of the constant rather than the identifier that a particular API uses.
Constants are usually numeric, but they might also be strings or other values. To identify all
constants, inspect the header file for the API to find the definitions. The definition might
either be in #define statements or in enumerations, which use the enum keyword.


Calling Conventions

Your library call can fail when certain operating systems use calling conventions other than
the C calling convention and the Standard __stdcall calling convention. The calling
convention defines how data is passed to a function and how clean up occurs after the
function call is complete. The documentation for the API should say which calling
convention(s) you must use. The Standard __stdcall calling convention is also known
as the WINAPI convention, or the Pascal convention.

Use of calling conventions other than the C or Standard calling conventions frequently
causes the failure of library calls in LabVIEW because those other calling conventions use
an incompatible method for maintaining the stack.


                                                    © National Instruments Corporation 1635

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1635 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1636 ordinal=1636 -->
## LabVIEW User Manual

LabVIEW User Manual


      Example 1: Call a Shared Library That You Built

           This section describes the tasks necessary to complete the Array Average VI you started
           building in Building a Shared Library to Call from LabVIEW so the VI can call the avg_num
           function in myshared.dll.

             NOTE
                    (Linux) The shared library file has a .so extension. You cannot call functions in
                     static libraries .a files) on Linux. You can only call shared libraries .so files)
                  dynamically.

         You must complete the following tasks before the Array Average VI can call the avg_num
           function in myshared.dll.

                   •   Complete configuration of the Call Library Function Node.
                   •   Build the front panel window.
                   •   Complete the block diagram.


         Complete Configuration of the Call Library Function Node

             NOTE
                             If you want to run applications or shared libraries created with different versions of
                LabVIEW on the same computer, the computer must have a version of the LabVIEW
                Run-Time Engine that is compatible with each version of LabVIEW used to create
                  the applications or shared libraries.

         Complete the following steps to complete the configuration of the Call Library Function
         Node.

                1.  Open the Array Average VI block diagram.
                2.  Right-click the Call Library Function Node and select Configure from the shortcut
             menu to open the Call Library Function dialog box.
                3.  Click the Browse button to the right of the Library Name or Path control to display
               a file dialog box.
                4.  Navigate to the location of your myshared.dll file.
                5.  Select myshared.dll and click the Open button. The file path to
            myshared.dll appears in the Library Name or Path control. The Library Name
                or Path control specifies the library name or path for the function you are calling.
                 Enter only the library name if the library is in the search path of the system. Enter
                 the entire path if the library is not in the search path of the system.


1636  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1636 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1637 ordinal=1637 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
       To make the reference platform independent, use the * wildcard. Keep the C++
       compiler from introducing platform dependence in exported function names
       through a process called name mangling by using the C++ compiler function export
         directive, extern "C"{}, in your header file.


Build the Front Panel Window

Complete the following steps to create the front panel of the Array Average VI.

   1.  Place an array control on the front panel window and label it Array.
   2.  Place a numeric control in the array shell and resize the array to contain four
      elements.
   3.  Right-click the Array control and select Representation»Single Precision from the
       shortcut menu.
   4.  Place a numeric indicator on the front panel window and label it Avg Value to
       display the result of your averaging calculation.
   5.  Right-click the Avg Value indicator and select Representation»Single Precision
      from the shortcut menu.
   6.  Place a numeric indicator on the front panel and label it Error to display any
       errors that your VI generates.
   7.  Right-click the Error indicator and select Representation»Long from the shortcut
     menu.

The following front panel belongs to the Array Average VI.


Complete the Block Diagram

Complete the following steps to complete the block diagram of the Array Average VI.

   1.  Wire Array to the a input of the Call Library Function Node.
   2.  Place an Array Size function on the block diagram.
   3.  Wire Array to the input of the Array Size function.
   4.  Wire the Array Size function output to the size input of the Call Library Function
      Node.


                                                    © National Instruments Corporation 1637

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1637 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1638 ordinal=1638 -->
## LabVIEW User Manual

LabVIEW User Manual


                5.  Right-click the avg input of the Call Library Function Node and select
                Create»Constant from the shortcut menu. Set the constant value to zero.
                6.  Wire the avg output of the Call Library Function Node to Avg Value.
                7.  Wire the error output of the Call Library Function Node to Error.

         The following block diagram shows the completed Array Average block diagram.


        Run the VI

        On the front panel, enter values in Array and run the VI to calculate the average of those
           values. Save your work and close the VI.

                 If your shared library returns incorrect results or crashes, verify the data types and wiring
           to see if you wired the wrong type of information.

      Example 2: Call a Hardware Driver API

         You might want to access an API associated with hardware you have purchased. In this
          example, you call a hypothetical interface card for a databus called X-bus.

             NOTE
                You do not need to use the Call Library Function Node to gain access to the APIs of
                  National Instruments hardware. All National Instruments products come with
                LabVIEW interfaces.


          Configure the Call Library Function Node

         The X-bus interface card comes with a software driver for your operating system. The X-bus
          documentation provides the following standard information:

                   •   A listing of all functions you can use to access the hardware
                   •   Description of the shared library file xbus.dll that contains these functions


1638  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1638 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1639 ordinal=1639 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Instructions on including a header file xbus.h
          NOTE
             Although LabVIEW does not permit you to include such header files, you can
            open header files and extract information about function prototypes and
               constants.
    •   (Windows) A statement about the Standard __stdcall calling convention that
      the X-bus library uses

One of the functions you want to use with this hypothetical hardware is XBusRead16,
which reads a 16-bit integer from a certain address. The documentation describes
XBusRead16 as follows:

 long XBusRead16(unsigned    Puts 16 bits from the register at "offset" into the
 long offset,               memory location pointed to by "data." Returns 1 if
 short*data);                                  successful, or 0 if it fails.


Given the preceding information from the X-bus documentation, complete the following
steps to configure the LabVIEW Call Library Function Node.

   1.  Open a new, blank VI and save the VI as Read Data.
   2.  Place a Call Library Function Node on the block diagram.
   3.  Right-click the Call Library Function Node object and select Configure from the
       shortcut menu.
   4.  Make the following settings in the Call Library Function dialog box:
           1.  Enter XbusRead16 in the Function name control.
           2.  Select the stdcall (WINAPI) control from the Calling Convention field.
           3.  Navigate to the Parameters page of the Call Library Function dialog box.
              Select Numeric from the Type pull-down menu for return type.
           4.  Select Signed 32-bit Integer from the Data Type pull-down menu for return
              type.
           5.  Add a parameter and name it offset.
           6.  Select Numeric from the Type pull-down menu.
           7.  Select Unsigned 32-bit Integer from the Data Type pull-down menu.
           8.  Add a parameter and name it data.
           9.  Select Numeric from the Type pull-down menu.
          10. Select Signed 16-bit Integer from the Data Type pull-down menu.
          11. Select Pointer to Value from the Pass pull-down menu.
   5.  Inspect the function prototype that appears in the Function Prototype field. If the
      prototype you see does not match the definition of the function in the API you are
        calling, you must change your settings in the Call Library Function dialog box.


                                                    © National Instruments Corporation 1639

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1639 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1640 ordinal=1640 -->
## LabVIEW User Manual

LabVIEW User Manual


          Place a numeric control, numeric indicator, and round LED indicator on the front panel
         window. Label the control and indicators and complete the block diagram as shown in the
           following block diagram and front panel.


      Example 3: Call the Win32 API

         You might want to access the 32-bit Windows platform API (Win32 API). In Win32
          environments, various DLLs permit your application to interact with the operating system
         and with the graphical user interface. Because the API offers thousands of functions,
         programmers must rely on the documentation for the Microsoft Software Development Kit
           (SDK). Microsoft Visual Studio products give you access to the SDK documentation. You
           also can access this information at the Microsoft Developer Network (MSDN) website.

                 TIP
                  Instead of using the Windows DLL as described in this example, you could easily
                   create this message box in LabVIEW.

            In this example, you call the Windows MessageBox function, a function which illustrates
           several of the typical complexities of the Win32 API. MessageBox is a simple SDK
           function that presents a small dialog box with a message, and has the following prototype:

        int MessageBoxHWND hWnd, // handle to owner window

        LPCTSTR lpText, // text in message box

        LPCTSTR lpCaption, // message box title

        UINT uType // message box style;


1640  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1640 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1641 ordinal=1641 -->
## LabVIEW User Manual

LabVIEW User Manual


Notice the non-standard data types, such as HWND and LPCTSTR. The Win32 API uses
hundreds of data types in the SDK, and very few of them are standard C data types.
However, many of the non-standard data types are merely aliases for standard C data
types. The API uses the aliases to identify the context of a particular data type. The
following table lists the data types in the preceding prototype and the corresponding
standard C data types.

 WIN32 SDK Data Type                           Standard C Data Type
 HWND                                       int **
 LPCTSTR                                 const char *
 UINT                                    unsigned int

To properly call the MessageBox function in LabVIEW, you need to identify the equivalent
LabVIEW data types, which you can usually infer from the C data types. Mapping LPCTSTR
and UINT to LabVIEW is straightforward: LPCTSTR is a C String and UINT is a U32.

Mapping HWND is more complex. The previous table lists HWND as a double pointer to an
integer. However, inspection of the function shows that MessageBox uses HWND merely
as a reference number that identifies the owner of the window. Because of this fact, you do
not need to know the integer value for which the HWND is a handle. Instead, you need to
know the value of the HWND variable itself. Because it is a double pointer, and hence a
pointer, you can be treat it as a 32-bit unsigned integer, or in LabVIEW terms, a U32.
Handles such as HWND are common in the Win32 SDK. In LabVIEW, you are almost always
interested in the handle itself and not the data to which it points. Therefore, you can
usually treat handles as U32. Handle names always begin with the letter H in the Win32
API.

If the SDK documentation does not make clear what C data type corresponds to a Win32
type, search windef.h for the appropriate #define or typedef statement.

The following table lists the Win32 SDK data types from the previous table and their
corresponding LabVIEW data types.

 WIN32 SDK Data Type                       LabVIEW Data Type
 HWND                                    uInt32
 LPCTSTR                        CStr (C string pointer)
 UINT                                    uInt32

(Windows) Refer to the labview\examples\Connectivity\Libraries and
Executables\Libraries and Executables.lvproj for a list of more Win32
API data types.


                                                    © National Instruments Corporation 1641

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1641 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1642 ordinal=1642 -->
## LabVIEW User Manual

LabVIEW User Manual


          Constants

           This section presents methods for finding the numerical values of constants in the Win32
            API, using MessageBox constants as examples. The following table lists selected
           constants for MessageBox.

          Constant                                        Description
        MB_ABORTRETRYIGNORE          An Abort, Retry, Ignore message box.
                                  A Cancel, Try Again, Continue message box on Windows
        MB_CANCELTRYCONTINUE                                           2000. An alternative to MB_ABORTRETRYIGNORE.
                                   A Help button to add to a message box on Windows XP
                                   and later. The system sends a WM_HELP message to the        MB_HELP                                     owner whenever the user clicks the Help button or
                                                             presses<F1>.

                                   A message box with an OK button. This is the default        MB_OK                                                    message box.


            In Visual Studio, programmers do not use the actual values of constants. In LabVIEW,
          however, you need to pass the actual numeric value of the constant to the function. You
            find these values in the header files that come with the SDK. The SDK documentation
          normally lists the relevant header file at the bottom of the help topic for a given function.
          For MessageBox, the SDK documentation specifies the header file as winuser.h.

         The header file named in the preceding statement usually declares the constants.
          Searching through that header file, you should be able to find a #define statement or an
          enumeration that assigns the constant text a value. winuser.h defines values for some
           of the MessageBox constants as follows:

        #define MB_OK 0x00000000L

        #define MB_ABORTRETRYIGNORE 0x00000002L

        #define MB_ICONWARNING MB_ICONEXCLAMATION

          Thus, MB_OK has the decimal value 0. MB_ABORTRETRYIGNORE has the decimal value
           2. MB_ICONWARNING is defined as MB_ICONEXCLAMATION. Elsewhere in winuser.h
         you find the following statement defining MB_ICONEXCLAMATION :

        #define MB_ICONEXCLAMATION 0x00000030L

         A hexadecimal value of 30 translates to a decimal value of 48.

         Keep in mind that constants in the SDK often are used in bitfields. A bitfield is usually a
           single integer in which each bit controls a certain property. The uType parameter in
        MessageBox is an example of a bitfield. Often, you can combine multiple constants in
          order to set multiple properties through one parameter. In order to combine these


1642  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1642 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1643 ordinal=1643 -->
## LabVIEW User Manual

LabVIEW User Manual


constants, you use a bitwise OR operation |. For example, to set the MessageBox to have
a warning icon and the buttons Abort, Retry, and Ignore, you pass the following value of
uType to MessageBox :

MB_ABORTRETRYIGNORE|MB_ICONEXCLAMATION = 0x32

In LabVIEW, you combine multiple constants by wiring integer types to the OR operator, as
shown in the following block diagram.


Determining the Proper Library and Function Name

Before you can configure the call to the Win32 API, you must identify the DLL that contains
MessageBox and the specific name of MessageBox within the DLL. Refer to the
description of MessageBox in the documentation that comes with your SDK or search for
MessageBox Function () on the Microsoft Web site. The Requirements section of
the documentation on the Microsoft Web site contains the following information:

 Minimum supported client                Windows 2000 Professional

 Minimum supported server                  Windows 2000 Server

 Header                                   Winuser.h (include Windows.h)

 Library                                                User32.lib

 DLL                                                   User32.dll

 Unicode and ANSI names        MessageBoxW (Unicode) and MessageBoxA (ANSI)

The DLL line specifies user32.dll as the DLL that contains MessageBox. The Unicode
and ANSI names line specifies the name of the MessageBox function for each type of
character encoding.

Unicode Versions and ANSI Versions of Functions

MessageBox uses two string arguments. The SDK implements two versions of functions
that use string arguments, a Unicode version and an ANSI version. One of the items in the
Requirements section of the MessageBox documentation says, “Unicode: Implemented
as Unicode and ANSI version on Windows.” You can distinguish the two versions in the DLL
because each has a W (Unicode) or an A (ANSI) appended to the end of the function name.
winuser.h contains the following code:

#ifdef UNICODE


                                                    © National Instruments Corporation 1643

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1643 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1644 ordinal=1644 -->
## LabVIEW User Manual

LabVIEW User Manual


        #define MessageBox MessageBoxW

        #else

        #define MessageBox MessageBoxA

        #endif // !UNICODE

         The preceding code defines MessageBox to be either MessageBoxA or
        MessageBoxW, depending on whether the application is a Unicode application. In effect,
         a MessageBox function does not exist in user32.dll. Instead, user32.dll contains
         a function MessageBoxA and a function MessageBoxW. In most cases in LabVIEW, you
          use the ANSI version of the function because the LabVIEW strings are based on ANSI, not
          Unicode. For this example, you use the MessageBoxA function.


          Configuring a Call to the Win32 API

       Now that you are familiar with many aspects of the Win32 API, you can configure a LabVIEW
            Call Library Function Node to call the MessageBox function. Remember that you must
          use the Standard __stdcall calling convention in calls to any function in the Windows
          SDK.

         The following front panel shows a correctly configured instance of the Call Library Function
         Node. Make your Call Library Function dialog box match the settings in the graphic.


1644  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1644 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1645 ordinal=1645 -->
## LabVIEW User Manual

LabVIEW User Manual


The following block diagram shows a VI designed to call the Win32 API. Configure your
block diagram to match the following block diagram.


The VI generates the following message box.


                                                    © National Instruments Corporation 1645

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1645 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1646 ordinal=1646 -->
## LabVIEW User Manual

LabVIEW User Manual


       Additional Windows Examples of LabVIEW Calls to DLLs

          (Windows) The following examples can help you learn more about calling DLLs from
          LabVIEW:

                   •   The Call DLL VI located in labview\examples\Connectivity\Libraries
            and Executables\Libraries and Executables.lvproj allows you
                  to browse examples of C and C++ external code data types and how they interface
                 with LabVIEW.
                   •   The Sound Player VI located in the labview\examples\Graphics and
            Sound\Sound directory lets you play Windows .WAV sound files on your
               computer from LabVIEW, if you have a sound card with Windows sound drivers
                   installed on your system.
                   •     If you do not have a sound, card you can generate a sound in your PC speaker by
                   calling the MessageBeep function in User32.DLL. The function prototype is as
                   follows:
            VOID MessageBeep(UINT uType);

                   •   You can programmatically position your cursor anywhere on your monitor using the
            SetCursorPos function in User32.DLL. The function prototype is as follows:
            BOOL SetCursorPos(INT x, INT y);

            x and y are the coordinates you want, referenced from the upper left corner of the
                  screen. The return value is TRUE if the function was successful and FALSE if it was
                  unsuccessful. Remember that the value returned is type BOOL, which is defined in
                 the Win32 API as a 32-bit signed integer with values 0 = FALSE and 1 = TRUE.

     Debugging Shared Libraries and Calls to Shared
       Libraries

        When you debug your LabVIEW calls to shared libraries, you must be prepared to trace
         problems in the shared library you are calling and in the implementation of the Call Library
          Function Node in LabVIEW.


          Troubleshooting the Call Library Function Node

        When the LabVIEW calls to shared libraries generate errors, check for the following
         problems in your use of the Call Library Function Node:

                   •    Verify the Call Library Function Node has the correct name or path for the shared
                     library. Also ensure that you specify the location on disk appropriately for your use
                  case. Some use cases require you to specify the shared library by path, and other
                use cases require you to specify the shared library by name.


1646  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1646 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1647 ordinal=1647 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   For LabVIEW-built shared libraries, make sure the computer has a version of the
      LabVIEW Run-Time Engine that is compatible with each version of LabVIEW used to
       create the shared libraries.
    •     If you receive the error message Function not found in library, verify
      the Call Library Function Node has the correct spelling, syntax, and case sensitivity
       for the function name that you are calling.
    •   Be sure that the compiler has not decorated the function.
    •     If you receive an error message that a secondary shared library cannot be found, yet
      you properly specified the path to the primary shared library in the Call Library
      Function Node, the primary shared library needs additional functions from one or
     more other shared libraries. You need to find the other shared libraries and place
     them in the same directory as the shared library that needs them or in a directory
       that is in the search path. Refer to the KnowledgeBase at ni.com for more
       information.
    •     If your VI crashes, verify that return types and data types of arguments for functions
       in the Call Library Function Node exactly match the data types your function uses.
       Also, verify the Call Library Function Node uses the proper calling convention (C or
     __stdcall using the Error Checking Level tab in the Call Library Function dialog
       box.
    •    Verify that all the parameters are defined to be passed by the correct method, such
      as value or pointer. Also, verify the Call Library Function Node passes arguments to
      the function in the correct order.
    •   For arrays or strings of data, always pass a buffer or array that is large enough to
      hold any results that the function places in the buffer. However, if you are passing
     them as LabVIEW handles, use LabVIEW Manager functions to resize them under
       Visual C++ or Xcode compilers.
    •     If you receive a message, the cause is almost always an error in the code of the
      shared library, such as writing past the end of the memory allocated for an array.
      Notice that these kinds of crashes might or might not occur at the time the shared
       library call actually executes on the block diagram.
    •   Use the Automation Open function with the Property Node and the Invoke Node
       instead of the Call Library Function Node if you want to call a shared library that
       contains ActiveX objects.
    •    All calls to LabVIEW-built shared libraries should specify Run in any thread. If you
       configure the Call Library Function Node using LabVIEW-built shared libraries and
       specify Run in UI thread, LabVIEW might hang and require you to restart.
    •   Pascal strings do not exceed 255 characters in length.
    •   Resizing of arrays and strings can take place only when the Call Library Function
     Node passes a LabVIEW array handle or LabVIEW string handle. Resize arrays and
       strings using functions exported through labviewv.lib to a Visual C++ project,
     and liblvexports.a to an Xcode project
    •  Remember that C strings are NULL terminated. If your DLL function returns numeric
      data in a binary string format, for example, through GPIB or the serial port, it might
       return NULL values as part of the data string.

Related Information

Calling Shared Libraries in LabVIEW


                                                    © National Instruments Corporation 1647

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1647 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1648 ordinal=1648 -->
## LabVIEW User Manual

LabVIEW User Manual


          Configure the Call Library Function Node

            Call Library Function Node

            Call Library Function Dialog Box

         LabVIEW Manager Functions

           Specifying the Location of Shared Libraries on Disk

          Using the LabVIEW Run-Time Engine

           Building a Function Prototype

          Automation Open Function

          Property Node

          Invoke Node

           ActiveX Container Overview


          Troubleshooting Your Shared Library

         Check for the following problems in your shared library when LabVIEW calls to shared
             libraries generate errors:

                   •    Verify that shared library functions that other applications call appear in the module
                   definition file EXPORTS section, or you include the _declspec (dllexport)
               keyword in the function declaration. Keep the C++ compiler from introducing
                 platform dependence in exported function names through a process called name
               mangling by using the C++ compiler function export directive, extern "C"{}, in your
                header file, as shown in the following example code:
            extern "C" {

            /* your function prototypes here */

            }
                   •  Remember that you need to declare the function with the _declspec
            (dllexport) keyword in the header file and the source code, or define it in the
            EXPORTS section of the module definition file.
                   •  When you use the _declspec (dllexport) keyword and you are also using
                 the __stdcall calling convention, you must declare the shared library function
             name in the EXPORTS section of the module definition .def file. In the absence of
               a .def file, __stdcall might truncate function names in an unpredictable
                  pattern, so the actual function name is unavailable to applications that call the
                shared library.


1648  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1648 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1649 ordinal=1649 -->
## LabVIEW User Manual

LabVIEW User Manual


•  When a function has not been properly exported, you must recompile the shared
     library. Never recompile the shared library while the shared library is loaded into
   memory by another application, for example, by your VI. Before recompiling a
    shared library, make sure that all applications making use of the shared library are
   unloaded from memory. This ensures that the shared library itself is not loaded into
   memory during a recompile. The shared library might fail to rebuild correctly if you
    forget this point and your compiler does not warn you. However, most compilers
   warn you when the shared library is in use by an application.
•   Try to debug the shared library by using the source level debugger provided with
    your compiler. Using the debugger of your compiler, you can set breakpoints, step
    through your code, watch the values of the variables, and so on. Debugging using
    conventional tools can be extremely beneficial. Refer to the appropriate manual for
    your compiler for more information about debugging.
•   Calling the shared library from another C program is also another way to debug the
    shared library. By calling the shared library from another C program, you have a
   means of testing the shared library independent of LabVIEW, thus helping you to
    identify any problems, sooner.
•  When calling a LabVIEW shared library that passes a 2D array, you must first declare
    the handler variable and initialize the variable to NULL, as shown in the following C
    code:
   main

   {

   /*LabVIEW data handler variable for the array */

   TD1Hd1myArray = NULL;

   ...

   /* Call to the LabVIEW shared library function */

   DLLFunctionalCall(&myArray);

   ...

   }

      If you do not initialize the handler variable to NULL, the code produces a General
   Protection Fault when you call the shared library.
•   To allow LabVIEW shared library functions to execute without interruption, LabVIEW
    delays the processing of operating system messages until the end of any calls to
    shared library functions or until you load a modal window from the shared library.
    Delaying the operating system messages, such as keyboard messages from the
    users, is useful in order to avoid calling the same shared library file while a shared
    library function runs. For example, if the shared library function is called in response
    to the user pressing a button, the user should not be able to press the button again
    until the shared library function has completed. When LabVIEW delays the
    processing of operating system messages, all function calls to the same LabVIEW
    shared library are put into a queue. That queue will be executed after the original


                                                 © National Instruments Corporation 1649

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1649 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1650 ordinal=1650 -->
## LabVIEW User Manual

LabVIEW User Manual


                shared library function call completes. A modal window is a type of window that
                remains active or remains on top of all other LabVIEW windows until you close the
              window or open another modal window. If you load a modal window from the
                shared library, LabVIEW overrides the process delay and processes the messages to
                 allow the modal window to become active. You cannot interact with other windows
                 while a modal window is open. Most dialog boxes in LabVIEW are modal windows.
               You cannot open a non-modal window from a LabVIEW callback VI nor a shared
                    library while any other process is running. If you want your callback VI or shared
                    library to call a non-modal window, you must do so programmatically by
                completing the steps outlined in the Callback VIs topic.
                   •   You can choose whether to delay operating system messages in shared libraries that
               you build. Before building the shared library, navigate to the Advanced page of the
               Shared Library Properties dialog box and remove the checkmark from the Delay
                operating system messages in shared library checkbox to process operating
                system messages while shared library functions run.
                   •   The following scenarios might cause the No debuggable applications or
            runtime libraries found error to appear.
                         ◦   The debuggable shared library was not loaded or was unloaded by the
                         application.
                         ◦   The configuration ini file of the shared library, created by the Application
                          Builder, was not distributed with the shared library.

          Related Information

          Callback VIs

          Shared Library Properties Dialog Box

      Module Definition Files

        When you build a shared library, you configure LabVIEW to use the C calling convention in
          the .c source file you built with the Call Library Function Node. In contrast, you use the
        __stdcall calling convention when you call the Win32 API. When you build a shared
            library with __stdcall, you normally use a module definition .def file to export the
           functions in your shared library. In the absence of a .def file, __stdcall might truncate
           function names in an unpredictable pattern, so the actual function name would be
           unavailable to applications that call the shared library.

         You can associate a .def file with a shared library. The .def file contains the statements
            for defining a shared library, such as the name of the shared library and the functions that
                it exports, as shown in the following example code:

        LIBRARY myshared

        EXPORTS

        avg_num


1650  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1650 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1651 ordinal=1651 -->
## LabVIEW User Manual

LabVIEW User Manual


The preceding code example demonstrates the following key requirements for .def files:

    •   The only mandatory entries in the .def files are the LIBRARY statement and the
     EXPORT statement.
    •   The LIBRARY statement must be the first statement in the file.
    •   The name you specify in the LIBRARY statement identifies the library in the import
       library of the shared library.
    •   The names you specify in the EXPORTS statement identify the functions that the
      shared library exports.

      NOTE
        Instead of a .def file, many Windows programmers use the LINK option in Project
        Settings of the Visual C++ compiler to obtain equivalent command-line options for
      most module definition statements.

Using Arrays and Strings in the Call Library Function
Node

This section reviews important concepts regarding array and string data in the Call Library
Function Node.

(Windows) Refer to the labview\examples\Connectivity\Libraries and
Executables\Libraries and Executables.lvproj for an example of using
arrays and strings in shared libraries (DLLs).


Arrays of Numeric Data

Arrays of numeric data can be comprised of any type of integers or floating point numbers
with single (4-byte) or double (8-byte) precision. When you pass an array of data to a
shared library function, you can pass the data as an array data pointer, as a LabVIEW array
handle, or as a LabVIEW array handle pointer.

Array Data Pointers have the following characteristics whether you pass the Array Data
Pointers in the Windows API or in another API:

    •   You can set the number of dimensions in the array, but you must not include
      information about the size of the array dimension(s). Instead, you must pass the size
       of the array dimension(s) information to your shared library in a separate variable.
    •   Never resize an array or perform operations that might change the length of the
       array data passed from LabVIEW. Resizing might cause a crash because the pointer
      sent is not an allocated block but points into the middle of an allocated block.
    •   To return an array of data, you should allocate an array of sufficient size in LabVIEW,
      pass the array to your function, and have this array act as the buffer. If the data
       takes less space, you can return the correct size as a separate parameter and then,
     on the calling diagram, use array subset to extract the valid data.


                                                    © National Instruments Corporation 1651

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1651 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1652 ordinal=1652 -->
## LabVIEW User Manual

LabVIEW User Manual


        Remember that the Windows API does not use LabVIEW array handles, so with functions
           that are part of the Windows API you can use only Array Data Pointers.

                 If you pass the array data as a LabVIEW array handle, you can use LabVIEW Manager
           functions, such as NumericArrayResize, to resize the handle. If you need to resize a
          handle to an array of strings or clusters, consider alignment on different platforms.

          Related Information

         LabVIEW Manager Functions

          NumericArrayResize Function


           String Data

         The types of your string pointers must match the types of string pointers that your function
           uses, or errors occur. The Call Library Function Node offers the following choices:

                   •  C String Pointer is a pointer to the string, followed by a NULL character. Most Win32
                 API functions use this C-style string pointer.
                   •   Pascal String Pointer is a pointer to the string, preceded by a length byte.
                   •   LabVIEW String Handle is a pointer to a pointer to the string, preceded by four
                 bytes of length information.
                   •   LabVIEW String Handle Pointer is a pointer to a handle for a string, preceded by
                  four bytes of length information.

         You can think of a string as an array of characters. Assembling the characters in order forms
         a string. LabVIEW stores a string in a special format in which the first four bytes of the array
           of characters form a 32-bit signed integer that stores how many characters appear in the
             string. Thus, a string with n characters requires n + 4 bytes to store in memory. For
          example, in the following illustration, the string text contains four characters.


        When LabVIEW stores the string, the first four bytes contain the value 4 as a 32-bit signed
         number, and each of the following four bytes contains a character of the string. The
          advantage of this type of string storage is that NULL characters are allowed in the string.
           Strings are virtually unlimited in length, up to 231 characters. This method of string storage
              is shown in the previous illustration. If you pass a LabVIEW string handle from the Call
           Library Function Node to the shared library, then you can use the LabVIEW Manager
           functions, such as DSSetHandleSize, to resize the LabVIEW string handle.

         The Pascal string format is nearly identical to the LabVIEW string format, but instead of
           storing the length of the string as a 32-bit signed integer, the string length is stored as an 8-
            bit unsigned integer. Storing the string length as an 8-bit unsigned integer limits the length
           of a Pascal-style string to 255 characters. A Pascal string that is n characters long will
           require n + 1 bytes of memory to store. The following illustrations shows a Pascal string.


1652  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1652 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1653 ordinal=1653 -->
## LabVIEW User Manual

LabVIEW User Manual


C strings are probably the type of strings you will deal with most commonly. The
similarities between the C-style string and normal numeric arrays in C becomes much more
clear when you see that C strings are declared as char*, where char is typically an 8-bit
unsigned integer. Unlike LabVIEW and Pascal strings, C strings do not contain any
information that directly gives the length of the string. Instead, C strings use a special
character called the NULL character to indicate the end of the string. NULL is defined to
have a value of zero in the ASCII character set. Notice that NULL is the number zero and not
the character “ 0. ” Thus, in C, a string that contains n characters requires n + 1 bytes of
memory to store: n bytes for the characters in the string and one additional byte for the
NULL termination character. The following illustration shows how a C-style string is stored
in memory.


The advantage of C-style strings is that they are limited in size only by available memory.
However, if you are acquiring data from an instrument that returns numeric data as a
binary string, as is common with serial or GPIB instruments, values of zero in the string are
possible. If you treat the string as a C-style string, your program incorrectly assumes that
the end of the string has been reached, when in fact your instrument is returning a numeric
value of zero. For binary data that might contain NULL values, consider using an array of 8-
bit unsigned integers.

Observe the following guidelines when passing string data to a shared library:

    •   Never resize a string, concatenate a string, or perform operations that might
       increase the length of string data passed from LabVIEW if you are using the C or
       Pascal string pointers.
    •     If you must return data as a string, allocate a string of the appropriate length in
      LabVIEW and pass this string into the shared library to act as a buffer. You can
       specify the string size and allocate the correct amount of memory with the
     Minimum size control on the Parameters tab of the Call Library Function dialog
       box. If you pass in a string that is smaller than the Minimum size, LabVIEW enlarges
      the size of the string to the minimum.
    •     If you pass a LabVIEW string handle from the Call Library Function Node to the
      shared library, you can use the LabVIEW Manager functions, such as
     DSSetHandleSize, to resize the LabVIEW string handle. Consider alignment on
       different platforms before resizing the string handle.

Related Information

Call Library Function Dialog Box

LabVIEW Manager Functions


                                                    © National Instruments Corporation 1653

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1653 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1654 ordinal=1654 -->
## LabVIEW User Manual

LabVIEW User Manual


          DSSetHandleSize Function


         Determining When to Resize Array and String Handles in Shared Libraries

        When a shared library function increases the size of a string or array that you passed by
          handle, you need to adjust the size of the handle that references the data. You can adjust
          the handle size using the memory manager routine DSSetHandleSize. Because this
           routine requires you to calculate the size of the new memory space, you must account for
          platform-dependent requirements about how you align and pad memory. A piece of data is
           aligned if it falls on a boundary equal to a multiple of its size. For example, a 2-byte value is
           at a memory address that is a multiple of 2 and a 4-byte value is at a memory address that
              is a multiple of 4. On Intel processors the maximum alignment is 4.

         The following examples highlight alignment differences on various platforms for a three-
          dimensional array of clusters, with each cluster containing a double-precision, floating-
           point number and a 1-byte Boolean:

                   •   (Windows) The first twelve bytes describe the size of each dimension of the array
                   (four bytes per dimension). Cluster elements follow, with each cluster element
                  consisting of an 8-byte double-precision floating-point number followed by a 1-byte
                Boolean. LabVIEW ignores alignment on Windows.
                   •    (64-bit LabVIEW running on Windows) The first twelve bytes describe the size of
               each dimension of the array (four bytes per dimension) followed by four bytes of
                padding. Cluster elements follow, with each cluster element consisting of an 8-byte
                 double-precision floating-point number followed by a 1-byte Boolean and seven
                 bytes of padding.
                   •   (OS X and Linux) The first twelve bytes describe the size of each dimension of the
                  array (four bytes per dimension). Cluster elements follow, with each cluster element
                  consisting of an 8-byte double-precision floating-point number followed by a 1-byte
               Boolean and three bytes of padding.

             NOTE
                 Although you must use DSSetHandleSize to resize a string or an array of
                    arbitrary data type, you can use the NumericArrayResize manager routine to
                    resize arrays of numeric data. NumericArrayResize automatically accounts
                     for platform-dependent alignment requirements.

          Related Information

          DSSetHandleSize Function

          NumericArrayResize Function

        How LabVIEW Stores Data in Memory

        How LabVIEW Stores Clusters in Memory


1654  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1654 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1655 ordinal=1655 -->
## LabVIEW User Manual

LabVIEW User Manual


Array and String Tip

When you are not passing LabVIEW handles and your shared library function must create
an array, resize an array, or resize a string of data, you should break the shared library
function into the following two shared library functions:

    •   Determine the number of elements that the array requires or the length of the string
       to be returned. Have the first shared library function return the desired size to
      LabVIEW.
    •   In LabVIEW, initialize an array or string with default values and pass this array to the
      second shared library function in your shared library, which actually places the data
       into the array. If you are working with string-based instrument control, it might be
       easier to pass an array of 8-bit integers than C strings because of the possibility of
      having NULL values in the string. When you are passing a LabVIEW array handle or
      LabVIEW string handle from the Call Library Function Node to your shared library,
      you can use the LabVIEW Manager functions to resize or create an array or string.

Related Information

Completing the.c File
Importing Shared Libraries

This book describes the Import Shared Library wizard you can use to create or update a
LabVIEW project library of wrapper VIs for functions in a Windows .dll file, an OS
X .framework file, or a Linux .so file.

        (Windows) To view related topics, click the Locate button, shown at left, in the
        toolbar at the top of this window. The LabVIEW Help highlights this topic in the
                  Contents tab so you can navigate the related topics.

Advantages of the Import Shared Library Wizard
Compared to the Call Library Function Node

Although you can use either the Call Library Function Node or the Import Shared Library
wizard to call shared library functions, the Import Shared Library wizard can accelerate
the process of integrating the shared library functions and reduce the potential for errors
when calling these libraries.

If you provide the name of a shared library file and a header .h file, the wizard parses the
header file and generates a wrapper VI for each function in the shared library, which the
wizard saves in a LabVIEW project library .lvlib. The VIs that the wizard generates each
contain a Call Library Function Node that accesses the selected function from the shared
library.

The Import Shared Library wizard has the following advantages compared to using the
Call Library Function Node directly:


                                                    © National Instruments Corporation 1655

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1655 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1656 ordinal=1656 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   The wizard automatically configures the Call Library Function Nodes generated in
                 the wrapper VIs by the wizard. Optionally, you also can customize the configuration
                    for this Call Library Function Node.
                   •   You can use the wizard to configure calls to multiple functions or entire libraries at
                 once. With the Call Library Function Node, you must configure each node to call a
                 function in a shared library individually.
                   •   Because the wizard generates the wrapper VIs in the shared library you specify, you
               can easily locate and update those VIs. For example, if you want to add or remove
             some of the functions you already imported from the shared library, you can run the
               Import Shared Library wizard again to update the previously generated wrapper
                     VIs. You can run the wizard multiple times on the same shared library file.
                   •   The wizard converts the data types in the shared library to LabVIEW data types. For
                example, the wizard automatically generates cluster data types for any structure
                data types in the shared library functions. With the Call Library Function Node, you
              must manually convert the structure data type.

                 If you want to individually configure each call to a shared library or if you want to
          customize configurations for calling shared libraries, use the Call Library Function Node to
             call libraries directly. Otherwise, use the Import Shared Library wizard to automate this
           process.

                 TIP
                             If you want to import a shared library file for an instrument driver, you can
               download the LabVIEW Instrument Driver Import Wizard from ni.com.


          Related Information

          Using the Import Shared Library Wizard

          Importing Functions from a Shared Library File

          Example: Importing Functions from a Shared Library File (Windows)

          Troubleshooting the Import Shared Library Wizard

            Call Library Function Node

      Supported Data Types for the Import Shared Library
      Wizard

         The LabVIEW Import Shared Library wizard converts the following shared library data types
           to the indicated LabVIEW data types.

                   •   numeric and numeric pointer
                   •    string and string pointer
                   •   void and void pointer


1656  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1656 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1657 ordinal=1657 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Boolean and Boolean pointer
    •   cluster and cluster pointer

For return values in the shared library functions, the Input/Output type can only be Output.
The Configure VIs and Controls page of the Import Shared Library wizard displays an
exclamation point   icon to indicate that LabVIEW cannot process the specified data type.
For data types that LabVIEW does not support, create a custom control and link to it. Refer
to the Example: Importing Functions from a Shared Library File topic for more details.


Numeric

                       LabVIEW                              Unsigned C Data             I/O                 Pass      LabVIEW            Icon            Control                               Representation Type           Type              Type    Representation                         Type                                (unsigned int)

 __int8            Input    Numeric    Value            I8             U8

 __int16           Input    Numeric    Value           I16             U16

 __int32           Input    Numeric    Value           I32             U32

 __int64           Input    Numeric    Value           I64             U64

 char              Input    Numeric    Value            I8             U8

 short             Input    Numeric    Value           I16             U16

 int               Input    Numeric    Value           I32             U32

 long              Input    Numeric    Value           I32             U32

 float             Input    Numeric    Value        SGL

 double           Input    Numeric    Value       DBL


Numeric Pointer

                               I/O                              LabVIEW                         Unsigned                         Type            Pass     LabVIEW C Type  Icon    I/O Type           Control                         Representation                             (const          Type  Representation                                Type                          (unsigned int*)                                 int*)

 __int8              Input/Output  Input  Numeric Pointer         I8           U8 *

 __int16              Input/Output  Input  Numeric Pointer        I16          U16 *

 __int32              Input/Output  Input  Numeric Pointer        I32          U32 *


                                                    © National Instruments Corporation 1657

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1657 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1658 ordinal=1658 -->
## LabVIEW User Manual

LabVIEW User Manual


                                          I/O                                       LabVIEW                         Unsigned                                  Type            Pass     LabVIEW         C Type  Icon    I/O Type           Control                         Representation                                       (const          Type  Representation                                         Type                          (unsigned int*)                                              int*)

            __int64                        Input/Output  Input  Numeric Pointer        I64          U64            *

            short *       Input/Output  Input  Numeric Pointer        I16          U16

              int *         Input/Output  Input  Numeric Pointer        I32          U32

           long *        Input/Output  Input  Numeric Pointer        I32          U32

              float *        Input/Output  Input  Numeric Pointer      SGL

           double                        Input/Output  Input  Numeric Pointer     DBL            *


           String and String Pointer

         C Type               Icon         I/O Type           LabVIEW Control Type

           char*                          Input/Output                    String

           Char []                         Input/Output                    String

           const char *                        Input                        String

           const char []                        Input                        String


          Void and Void Pointer

                                               LabVIEW                                                                 Pass      LabVIEW         C Type     Icon          I/O Type            Control                                                            Type    Representation                                                  Type

                             void means no control is
            void            needed and can appear
                             only as the return control

            void*                 Input/Output        Numeric    Value        U32

           const void                                      Input            Numeric    Value        U32            *


1658  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1658 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1659 ordinal=1659 -->
## LabVIEW User Manual

LabVIEW User Manual


Boolean and Boolean Pointer

 C Type          Icon       I/O Type        LabVIEW Control Type      Pass Type

 bool                         Input                Boolean               Value

 bool *                   Input/Output            Boolean               Pointer

 const bool *                  Input                Boolean               Pointer


Cluster and Cluster Pointer

 C Type            Icon      I/O Type       LabVIEW Control Type     Pass Type

 struct                        Input                  Cluster               Value

 Struct *                  Input/Output              Cluster               Pointer

 const struct *                  Input                  Cluster               Pointer

Using the Import Shared Library Wizard

Use the Import Shared Library wizard to create or update a LabVIEW project library of
wrapper VIs for functions in a Windows .dll file, an OS X .framework file, or a
Linux .so file.

The Import Shared Library wizard supports most C and C++ header files. The wrapper VIs
the wizard creates use the Call Library Function Node, which does not support the C++
this pointer or calling methods in C++ classes.

      NOTE
            If you want to import a shared library file for an instrument driver, you can
      download the LabVIEW Instrument Driver Import Wizard from ni.com.

The Import Shared Library wizard parses the header file, lists the functions in the shared
library, converts data types in the shared library to LabVIEW data types, and generates a
wrapper VI for each function. The wizard saves the VIs in a LabVIEW project library that you
can edit and creates an HTML report about the generated library that you can launch when
you complete the wizard.

In the wizard, you can specify include paths and preprocessor definitions, configure the
individual VIs that wrap each function, and configure memory allocation and error
handling. The wizard also creates custom controls for structure elements in the original
functions and adds the controls to the project library. You can use the custom controls to
modify all the VIs in the library that contain the corresponding data type.

You can run the wizard multiple times on the same shared library file. If you select the
Update VIs for a shared library option on the Specify Create or Update Mode page, the


                                                    © National Instruments Corporation 1659

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1659 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1660 ordinal=1660 -->
## LabVIEW User Manual

LabVIEW User Manual


          wizard overwrites the previous version of the project library file and the existing VIs within
           that file. If you choose not to re-import generated VIs within the project library file, the VIs
          remain unchanged in the directory. The wizard retains the most recent settings for each
           individual function in a particular shared library. For example, if you have a shared library
           that contains three functions, you might update only the second function. The next time
         you run the wizard on that shared library file, it retains the original settings for functions
         one and three and the new settings for function two.

           Select Tools»Import»Shared Library to launch the Import Shared Library wizard. Follow
          the prompts to create wrapper VIs for shared library files. You must provide the name of a
          shared library file and a header .h file for the wizard to parse.

           Refer to the Importing Functions from a Shared Library File topic for step-by-step
           instructions for importing a shared library and creating wrapper VIs.
     LabVIEW Manager Functions in Shared Libraries

      Using LabVIEW Manager Functions in Shared Libraries

         LabVIEW has a suite of functions that you can call from shared libraries. This suite of
           functions performs user-specified routines using the appropriate instructions for a given
           platform. These routines, which manage the functions of a specific operating system, are
         grouped into the following categories:

                   •  Memory manager
                   •    File manager
                   •   Support manager


           Portability of LabVIEW Manager Functions

           External code written using the LabVIEW managers is portable, that is, you can compile it
          without modification on any platform that supports LabVIEW. This portability has the
           following advantages:

                   •   The LabVIEW application is built on top of the manager functions. Except for the
              manager functions, the LabVIEW source code is identical across platforms.
                   •   The analysis VIs rely mainly on manager functions. Therefore, their source code is
                 the same for all platforms.

             NOTE
              When you call the LabVIEW manager functions from a shared library, use
             #include extcode.h in any files that use manager functions and link to
              labviewv.lib. Set the structure alignment of the compiler to 1 byte.

         To achieve platform independence, data types should not depend on the peculiarities of
           various compilers. For example, the C language does not define the size of an integer.
          Without an explicit definition of the size of each data type, you have difficulty creating code


1660  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1660 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1661 ordinal=1661 -->
## LabVIEW User Manual

LabVIEW User Manual


that works identically across multiple compilers. LabVIEW managers use data types that
explicitly indicate the size of the data type. For example, if a routine requires a 4-byte
integer as a parameter, you define the parameter as an int32. The managers define data
types in terms of the fundamental data types for each compiler. Thus, on one compiler, the
managers might define an int32 as an int, while on another compiler, the managers
might define an int32 as a long int. When you write external code, use the manager
data types instead of the host computer data types so your code is more portable and has
fewer errors.


Pointers as Parameters

Some manager functions have a parameter that is a pointer. These parameter type
descriptions are identified by a trailing asterisk, such as the ph parameter of the
DSCopyHandle allocating and releasing function, or are type defined as such, such as
the name parameter of the FNamePtr function. In most cases, the manager function
writes a value to pre-allocated memory. In some cases, such as FStrFitsPath or
GetALong, the function reads a value from the memory location, so you do not have to
pre-allocate memory for a return value.

The following functions have parameters that return a value for which you must pre-
allocate memory.

 DSMemStats                               FNamePtr
 DSCopyHandle                            FNewRefNum
 DateToSecs                              FPathToArr
 DSMemStats                           FPathToAZString
 FCreate                              FPathToDSString
 FCreateAlways                          FPathToPath
 FFlattenPath                           FRefNumToFD
 FGetAccessRights                      FStringToPath
 FGetEOF                                FTextToPath
 FGetInfo                              FUnflattenPath
 FGetPathType                             GetAlong
 FMOpen                                   SetALong
 FMRead                                  RandomGen
 FMTell                                  SecsToDate
 FMWrite                             NumericArrayResize


                                                    © National Instruments Corporation 1661

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1661 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1662 ordinal=1662 -->
## LabVIEW User Manual

LabVIEW User Manual


         You must allocate space for this return value. The following examples illustrate incorrect
         and correct ways to call one of these functions from within a generic function foo.

           Incorrect example:

        foo(Path path) {

        PStr p;/* an uninitialized pointer */ File *fd;/* an
        uninitialized pointer */

        MgErr err;

        err = FNamePtr(path, p);

        err = FMOpen(fd, path, openReadOnly denyWriteOnly);

        }

            In the incorrect example, p is a pointer to a Pascal string, but the pointer is not initialized to
           point to any allocated buffer. FNamePtr expects its caller to pass a pointer to an allocated
          space and writes the name of the file referred to by path into that space. Even if the
           pointer does not point to a valid place, FNamePtr writes its results there, with
          unpredictable consequences. Similarly, FMOpen writes its results to the space to which fd
           points, which is not a valid place because fd is uninitialized.

           Correct example:

        foo(Path path) {

        Str255 buf; /* allocated buffer of 256 chars */

        File fd;

        MgErr err;

        err = FNamePtr(path, buf);

        err = FMOpen(&fd, path, openReadOnly, denyWriteOnly);

        }


1662  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1662 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1663 ordinal=1663 -->
## LabVIEW User Manual

LabVIEW User Manual


In the correct example, buf contains space for the maximum-sized Pascal string, whose
address is passed to FNamePtr. fd is a local variable (allocated space) for a file
descriptor.

      RELATED INFORMATION
      Memory Manager on page 1672
         File Manager on page 1676
       Support Manager on page 1680
       LabVIEW Manager Data Types on page 1663

LabVIEW Manager Data Types

LabVIEW Manager data types include the following data types:

    •   Scalar
    •   Char
    •   Dynamic
    •   Memory-related
    •   Constants


Scalar

Scalar data types include Boolean and numeric.


Boolean

External code modules work with two kinds of Boolean scalars—those existing in LabVIEW
block diagrams and those passing to and from manager routines. The manager routines
use a conventional Boolean form where 0 is FALSE and 1 is TRUE. This conventional
Boolean form is called a Bool32 and is stored as a 32-bit value.

LabVIEW block diagrams store Boolean scalars as 8-bit values. The value is 0 if FALSE and 1
if TRUE. This Boolean form is called an LVBoolean.

The following table describes the two forms of Boolean scalars.

 Name                                         Description
 Bool32                                 32-bit integer, 0 if FALSE, 1 if TRUE
 LVBoolean                              8-bit integer, 0 if FALSE, 1 if TRUE


                                                    © National Instruments Corporation 1663

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1663 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1664 ordinal=1664 -->
## LabVIEW User Manual

LabVIEW User Manual


         Numeric

         The manager data types support 8-, 16-, 32-, and 64-bit signed and unsigned integers.

         LabVIEW supports the following single, double, and extended floating-point data types.

          Type                                                Description

            Single                                                         32-bit

          Double                                                        64-bit

           Extended                                  Up to 80-bit


         LabVIEW supports complex numbers containing two floating-point numbers, with different
         complex numeric types for each of the floating-point data types.

         LabVIEW supports the following basic data types for numbers:

                   •   Signed integers
                         ◦  int8 8-bit integer
                         ◦  int16 16-bit integer
                         ◦  int32 32-bit integer
                         ◦  int64 64-bit integer
                   •   Unsigned integers
                         ◦  uInt8 8-bit integer
                         ◦  uInt16 16-bit integer
                         ◦  uInt32 32-bit integer
                         ◦  uInt64 64-bit integer
                         ◦  size_t 32-bit integer
                   •   Floating-point numbers
                         ◦  float32 32-bit floating-point number
                         ◦  float64 64-bit floating-point number
                         ◦  floatExt extended-precision floating-point number

         The following table explains how various platforms store extended-precision numbers.

           Platform                                Storage Format
                                  80-bit structure with two int32 components, mhi and mlo, and an          Windows and Linux                                      int16 component, e


1664  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1664 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1665 ordinal=1665 -->
## LabVIEW User Manual

LabVIEW User Manual


 Mac Intel                       64-bit double-precision floating-point number


Complex Numbers

The complex data types are structures with two floating-point components, re and im. As
with floating-point numbers, complex numbers can have 32-bit, 64-bit, and extended-
precision components. The following table contains the code for the type definitions for
each of these complex data types.

 Complex Number Type                              Code
                                typedef struct {

 32-bit                           float32 re, im;

                                } cmplx64;
                                typedef struct {

 64-bit                           float64 re, im;

                                } cmplx128;
                                typedef struct {

 Extended-precision                  floatExtre, im;

                                } cmplxExt;


char

The char data type is defined by C to be an 8-bit signed integer. LabVIEW defines an
unsigned char data type, with the following type definition:

typedef uInt8 uChar;


Dynamic

LabVIEW defines a number of data types you must allocate and deallocate dynamically.
Arrays, strings, and paths have data types you must allocate using memory manager and
file manager routines.


                                                    © National Instruments Corporation 1665

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1665 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1666 ordinal=1666 -->
## LabVIEW User Manual

LabVIEW User Manual


          Arrays

         LabVIEW supports arrays of any of the basic data types described in this section. You can
           construct more complicated data types using clusters, which can in turn contain scalars,
            arrays, and other clusters.

         The first four bytes of a LabVIEW array indicate the number of elements in the array. The
          elements of the array follow the length field.


           Strings

         LabVIEW supports C- and Pascal-style strings, lists of strings, and LStr, a special string
          data type you use for string parameters to external code modules. The support manager
           contains routines for manipulating strings and converting them among the different types
           of strings.


           C-Style Strings (CStr)

         A C-style string CStr is a series of zero or more unsigned characters, terminated by a zero.
        C strings have no effective length limit. Most manager routines use C strings, unless you
           specify otherwise. The following code is the type definition for a C string:

        typedef uChar *CStr;


           Pascal-Style Strings (PStr)

         A Pascal-style string PStr is a series of unsigned characters. The value of the first character
           indicates the length of the string. A PStr can have a range of 0 to 255 characters. The
           following code is the type definition for a Pascal string:

        typedef uChar            Str255[256], Str31[32],
        *StringPtr,
        **StringHandle;
        typedef uChar            *PStr;


         LabVIEW Strings (LStr)

         The first four bytes of a LabVIEW string LStr indicate the length of the string. The specified
         number of characters follow the length of the string. LStr is the string data type used by
         LabVIEW block diagrams. The following code is the type definition for an LStr string:

        typedef struct {


1666  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1666 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1667 ordinal=1667 -->
## LabVIEW User Manual

LabVIEW User Manual


int32 cnt;

/* number of bytes that follow */

uChar str[1];

/* cnt bytes */

} LStr, *LStrPtr, **LStrHandle;


Concatenated Pascal String (CPStr)

Many algorithms require manipulation of lists of strings. Arrays of strings are usually the
most convenient representation for lists. However, arrays of strings can place a burden on
the memory manager because of the large number of dynamic objects it must manage. To
make working with lists more efficient, LabVIEW supports the concatenated Pascal string
CPStr data type, which is a list of Pascal-style strings concatenated into a single block of
memory. Using the CPStr data structure, you can use support manager routines to create
and manipulate lists.

The following code is the type definition for a CPStr string:

typedef struct {

int32 cnt;

/* number of pascal strings that follow */

uChar str[1];

/* cnt concatenated pascal strings */

} CPStr, *CPStrPtr, **CPStrHandle;


Paths

A path (pathname) indicates the location of a file or directory in a file system. LabVIEW has
a separate data type for a path, represented as Path, which the file manager defines in a
platform-independent manner. The actual data type for a path is private to the file
manager and subject to change. You can create and manipulate Path data types using file.


Memory-Related

LabVIEW uses pointers and handles to reference dynamically allocated memory. The
memory-related data types have the following type definitions:

typedef uChar *UPtr;


                                                    © National Instruments Corporation 1667

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1667 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1668 ordinal=1668 -->
## LabVIEW User Manual

LabVIEW User Manual


        typedef uChar **UHandle;


          Constants

         The manager data types define the following constant for use with external code modules:

        NULL 0(uInt32)

         The following constants define the possible values of the Bool32 data type:

        FALSE 0 (int32)

        TRUE 1 (int32)

         The following constants define the possible values of the LVBoolean data type:

        LVFALSE 0 (uInt8)

        LVTRUE 1 (uInt8)

      LabVIEW Manager Function Errors

                 If you receive errors from LabVIEW Manager functions, most error names correspond to
         LabVIEW error codes. The error names correspond to the following LabVIEW error codes:

            Error Name                                   LabVIEW Error Code Number
        mgArgErr                                                  1
        mFullErr                                                  2
        fEOF                                                      4
        fIsOpen                                                   5
        fIOErr                                                    6
        fNotFound                                                7
        fNoPerm                                                   8
        fDiskFull                                                9
        fDupPath                                                 10
        ftMFOpen                                                 11
        fNotEnabled                                             12


1668  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1668 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1669 ordinal=1669 -->
## LabVIEW User Manual

LabVIEW User Manual


Error Name                                   LabVIEW Error Code Number
rfNotFound                                               13
rAddFailed                                               14
rNotFound                                                15
iNotFound                                                16
iMemoryErr                                               17
dPenNotExist                                            18
cfgBadType                                               19
cfgTokenNotFound                                       20
cfgParseError                                           21
cfgAllocError                                           22
ecLVSBFormatError                                      23
ecLVSBSubrError                                        24
ecLVSBNoCodeError                                      25
wNullWindow                                             26
wDestroyMixup                                           27
menuNullMenu                                            28
pAbortJob                                                29
pBadPrintRecord                                        30
pDriverError                                            31
pWindowsError                                           32
pMemoryError                                            33
pDialogError                                            34
pMiscError                                               35
dvInvalidRefnum                                        36
dvDeviceNotFound                                       37
dvParamErr                                               38
dvUnitErr                                                39
dvOpenErr                                                40


                                                   © National Instruments Corporation 1669

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1669 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1670 ordinal=1670 -->
## LabVIEW User Manual

LabVIEW User Manual


            Error Name                                   LabVIEW Error Code Number
        dvAbortErr                                               41
        bogusError                                               42
        cancelError                                             43
        OMObjLowErr                                             44
        OMObjHiErr                                               45
        OMObjNotInHeapErr                                      46
        OMOHeapNotKnownErr                                     47
        OMBadDPIdErr                                            48
        OMNoDPinTabErr                                          49
        OMMsgOutOfRangeErr                                     50
        OMMethodNullErr                                        51
        OMUnknownMsgErr                                        52
        mgNotSupported                                          53
        ncBadAddressErr                                        54
        ncInProgress                                            55
        ncTimeOutErr                                            56
        ncBusyErr                                                57
        ncNotSupportedErr                                      58
        ncNetErr                                                 59
        ncAddrInUseErr                                          60
        ncSysOutOfMem                                           61
        ncSysConnAbortedErr                                   62
        ncConnRefusedErr                                       63
        ncNotConnectedErr                                      64
        ncAlreadyConnectedErr                                 65
        ncConnClosedErr                                        66
        amInitErr                                                67
        occBadOccurrenceErr                                   68


1670  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1670 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1671 ordinal=1671 -->
## LabVIEW User Manual

LabVIEW User Manual


Error Name                                   LabVIEW Error Code Number
occWaitOnUnBoundHdlrErr                               69
occFunnyQOverFlowErr                                  70
fDataLogTypeConflict                                  71
ecLVSBCannotBeCalledFromThread                      72
amUnrecognizedType                                     73
mCorruptErr                                             74
ecLVSBErrorMakingTempDLL                             75
ecLVSBOldCIN                                            76
fmtTypeMismatch                                        81
fmtUnknownConversion                                  82
fmtTooFew                                                83
fmtTooMany                                               84
fmtScanError                                            85
lvOLEConvertErr                                        87
rtMenuErr                                                88
pwdTampered                                             89
LvVariantAttrNotFound                                 90
LvVariantTypeMismatch                                 91
axEventDataNotAvailable                               92
axEventStoreNotPresent                                93
axOccurrenceNotFound                                  94
axEventQueueNotCreated                                95
axEventInfoNotAvailable                               96
oleNullRefnumPassed                                   97
iviInvalidDowncast                                    102
iviInvalidClassSesn                                   103
ncSockNotMulticast                                    108
ncSockNotSinglecast                                   109


                                                   © National Instruments Corporation 1671

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1671 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1672 ordinal=1672 -->
## LabVIEW User Manual

LabVIEW User Manual


            Error Name                                   LabVIEW Error Code Number
        ncBadMulticastAddr                                    110
        ncMcastSockReadOnly                                   111
        ncMcastSockWriteOnly                                  112
        ncDatagramMsgSzErr                                    113
        dataCorruptErr                                         116
        requireFullPathErr                                    117
        folderNotExistErr                                     118
        ncBtInvalidModeErr                                    119
        ncBtSetModeErr                                         120
        mgBtInvalidGUIDStrErr                                 121
        rVersInFuture                                          122

     Memory Manager

         Most applications need routines for allocating and deallocating memory on request. The
         LabVIEW memory manager is the set of platform-independent memory manager functions
         you can use to dynamically allocate, manipulate, and deallocate memory. The memory
         manager supports dynamic allocation of both nonrelocatable and relocatable blocks,
          using pointers and handles.

                 If you need to perform dynamic memory allocation or manipulation from external code
          modules, use the memory manager. If your external code operates on data types other
          than scalars, you should understand how LabVIEW manages memory and know which
              utilities manipulate data.

         The following code shows how the memory manager defines generic handle and pointer
          data types:

        typedef uChar *UPtr;

        typedef uChar **UHandle;

             All data passed to or from a shared library is allocated using the memory manager. You
          should only use file manager functions, not the memory manager routines, to manipulate
           paths. Thus, your shared library should use the memory routines when working with
          parameters passed from the block diagram.


1672  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1672 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1673 ordinal=1673 -->
## LabVIEW User Manual

LabVIEW User Manual


Memory Allocation

Applications use the following types of memory allocation:

    •    Static
    •   Dynamic

      NOTE
       You can allocate memory for variables in C code using malloc. However, do not
        assign the resulting pointer to any variable you pass back to the LabVIEW block
       diagram. Use the memory manager functions if you want to create or resize
      memory associated with a variable passed from the LabVIEW block diagram.


Static Memory Allocation

With static memory allocation, the compiler determines memory requirements when you
create an application. When you launch the application, LabVIEW creates memory for the
known global memory requirements of the application. The memory LabVIEW creates
remains allocated while the application runs. Static memory allocation is simple to work
with because the compiler handles all the details.

However, static memory allocation cannot address the memory management
requirements of most real-world applications because you cannot determine most
memory requirements until run time. Also, statically declared memory might result in
larger memory requirements because the memory is allocated for the duration of the
application.


Dynamic Memory Allocation

With dynamic memory allocation, you reserve memory when you need it and free memory
when you are no longer using it. Dynamic allocation requires more work than static
memory allocation because you have to determine memory requirements and allocate
and deallocate memory as necessary.

You can use the LabVIEW memory manager to dynamically allocate memory in the
following ways:

    •   Using pointers to allocate memory
    •   Using handles to allocate memory


Using Pointers for Dynamic Memory Allocation

The more conventional method uses pointers to allocate memory. With pointers, you
request a block of memory of a certain size. The routine returns the address of the block of
memory to your shared library. When you no longer need the block of memory, you call a
routine to free the block of memory. You can use the block of memory to store data. You
reference the data stored in the block of memory by using the address the manager routine


                                                    © National Instruments Corporation 1673

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1673 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1674 ordinal=1674 -->
## LabVIEW User Manual

LabVIEW User Manual


          returned when you created the pointer. You can make copies of the pointer and use them
            in multiple places in your application to refer to the same data.

           Pointers in the LabVIEW memory manager are nonrelocatable, which means the manager
          never moves the memory block to which a pointer refers while that memory is allocated
            for a pointer. Because other references to the memory block do not become out of date,
          not moving the memory block allocated to a pointer avoids problems that occur when you
         need to change the amount of memory allocated to a pointer. If you need more memory,
            sufficient memory might not exist to expand the memory space of the pointer without
         moving the memory block to a new location. If an application had multiple references to
          the pointer, moving the memory block to a new location causes problems because each
           pointer refers to the old memory address of the data. Using invalid pointers can cause
          severe problems.


          Using Handles for Dynamic Memory Allocation

         A second form of memory allocation uses handles. As with pointers, when you allocate
        memory using handles, you request a block of memory of a certain size. The memory
         manager allocates the memory and adds the address of the memory block to a list of
          master pointers. The memory manager returns a handle that is a pointer to the master
            pointer. If you reallocate a handle and it moves to another address, the memory manager
          updates the master pointer to refer to the new address. If you look up the correct address
          using the handle, you access the correct data.

         Use handles to perform most memory allocation in LabVIEW. Pointers are available
          because in some cases they are more convenient and simpler to use.


          Using Pointers and Handles

          Create a handle using DSNewHandle, which allows you to specify the size of the memory
           block, or DSNewAlignedHandle, which allows you to specify the size, alignment, and
          alignment offset of the memory block. Create a pointer using DSNewPtr. Create a handle
           or pointer and set it to all zeros using DSNewHClr, DSNewAlignedHClr, and
        DSNewPClr.

        When you are finished with the handle or pointer, release it using DSDisposeHandle or
        DSDisposePtr.

                 If you need to resize an existing handle, use the DSSetHandleSize function, which
          determines the size of an existing handle. If you need to resize and realign an existing
          handle, use the DSSetAlignedHandleSize function, which determines the size,
          alignment, and alignment offset of an existing handle. You also can resize and realign an
            existing handle and set it to all zeros using DSSetAlignedHSzClr. Because pointers are not
           relocatable, you cannot resize them.

         A handle is a pointer to a pointer. In other words, a handle is the address of an address. The
         second pointer, or address, is a master pointer, which means it is maintained by the
        memory manager. Languages that support pointers provide operators for accessing data
         by its address. With a handle, you use this operator twice—once to get to the master
            pointer, and a second time to get to the actual data.


1674  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1674 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1675 ordinal=1675 -->
## LabVIEW User Manual

LabVIEW User Manual


Additional routines make it easy to copy and concatenate handles and pointers to other
handles, check the validity of handles and pointers, and copy or move blocks of memory
from one place to another.


Simple Example of Using Pointers and Handles

This simple example demonstrates how to work with pointers and handles in C.

The following code shows how to work with a pointer to an int32 :

int32 *myInt32P;

myInt32P = (int32 *)DSNewPtr(sizeof(int32));

*myInt32P = 5;

x = *myInt32P + 7;

...

DSDisposePtr(myInt32P);

The first line declares the variable myInt32P as a pointer to, or the address of, a 32-bit
signed integer. The first line does not actually allocate memory for the int32. The first
line creates memory for an address and associates the name myInt32P with that
address. The P at the end of the variable name is a convention used in this example to
indicate the variable is a pointer.

The second line creates a block of memory in the data space large enough to hold a single
32-bit signed integer and sets myInt32P to refer to this memory block.

The third line places the value 5 in the memory location to which myInt32P refers. The *
operator refers to the value in the address location.

The fourth line sets x equal to the value at address myInt32P plus 7.

The last line frees the pointer.

The following code is the same example using handles instead of pointers:

int32 **myInt32H;

myInt32H =(int32**)DSNewHandle(sizeof(int32));

**myInt32H = 5;

x = **myInt32H + 7;


                                                    © National Instruments Corporation 1675

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1675 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1676 ordinal=1676 -->
## LabVIEW User Manual

LabVIEW User Manual


        ...

        DSDisposeHandle(myInt32H);

         The first line declares the variable myInt32H as a handle to a 32-bit signed integer.
             Strictly speaking, the first line declares myInt32H as a pointer to a pointer to an int32.
          As with the previous example, the first line does not allocate memory for the int32. The
               first line creates memory for an address and associates the name myInt32H with that
           address. The H at the end of the variable name is a convention used in this example to
           indicate the variable is a handle.

         The second line creates a block of memory in the data space large enough to hold a single
         int32. DSNewHandle places the address of the memory block as an entry in the master
           pointer list and returns the address of the master pointer entry. Finally, the second line sets
        myInt32H to refer to the master pointer.

         The third line places the value 5 in the memory location to which myInt32H refers.
         Because myInt32H is a handle, you use the * operator twice to get to the data.

         The fourth line sets x equal to the value referenced by myInt32H plus 7.

         The last line frees the handle.

           This example shows only the simplest aspects of how to work with pointers and handles in
            C. Other examples show different aspects of using pointers and handles. Refer to a C
         manual for a list of other operators you can use with pointers and for more information
          about how to work with pointers.

        File Manager

         The file manager supports routines for opening and creating files, reading data from and
           writing data to files, and closing files. In addition, you can manipulate the end-of-file mark
           of a file and position the current read or write mark to an arbitrary position in the file. You
           also can move, copy, and rename files, determine and set file characteristics, and delete
              files.

         The file manager contains a number of routines for directories, with which you can create
         and delete directories. You also can determine and set directory characteristics and obtain
         a list of a directory's contents.

         LabVIEW supports concurrent access to the same file, so you can have a file open for both
          reading and writing simultaneously. When you open a file, you can indicate whether you
         want the file to be read from and written to concurrently. You also can lock a range of the
               file, if you need to make sure a range is nonvolatile at a given time.

         The file manager also provides many routines for manipulating paths, or path names, in a
          platform-independent manner. The file manager supports the creation of path
           descriptions, which are either relative to a specific location or absolute, that is, the full
           path. With file manager routines you can create and compare paths, determine


1676  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1676 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1677 ordinal=1677 -->
## LabVIEW User Manual

LabVIEW User Manual


characteristics of paths, and convert a path between platform-specific descriptions and the
platform-independent form.

Applications that manipulate files can use the functions in the file manager. The file
manager routines support basic file operations such as creating, opening, and closing files,
writing data to files, and reading data from files. In addition, you can use file manager
routines to create directories, determine characteristics of files and directories, and copy
files. File manager routines use a LabVIEW data type for file path names, called Path s,
that indicates a file or directory path independent of the platform. You can translate a
Path to and from the conventional format a host platform uses for describing a file
pathname.


Identifying Files and Directories

When you perform operations on files and directories, you need to identify the target of the
operation. The platforms LabVIEW supports use a hierarchical file system, meaning files are
stored in directories, possibly nested several levels deep. These hierarchical file systems
support the connection of multiple discrete storage media, called volumes. For example,
DOS-based systems support multiple drives connected to the system. For most of these
hierarchical file systems, you must include the volume name to specify the location of a
file. On other systems, such as Linux, you do not need to specify the volume name because
the physical implementation of the file system is hidden from the user.

How you identify a target depends upon whether the target is an open or closed file. If a
target is a closed file or a directory, specify the target using the path of the target. The path
describes the volume containing the target, the directories between the top level and the
target, and the name of the target. If the target is an open file, use a file descriptor to
specify that LabVIEW should perform an operation on the open file. The file descriptor is an
identifier the file manager associates with the file when you open it. When you close the
file, the file manager dissociates the file descriptor from the file.


Path Specifications

LabVIEW uses the following types of file path specifications:

    •   Conventional
    •   Empty
    •   LabVIEW specifications


Conventional

All platforms have a method for describing the paths for files and directories. These path
specifications are similar, but they are usually incompatible from one platform to another.
You usually specify a path as a series of names separated by separator characters.
Typically, the first name is the top level of the hierarchical specification of the path. The
last name is the file or directory the path identifies.

A path can be one of the following types:


                                                    © National Instruments Corporation 1677

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1677 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1678 ordinal=1678 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Relative path
                   •   Absolute path

         A relative path describes the location of a file or directory relative to an arbitrary location
            in the file system. An absolute path describes the location of a file or directory starting from
          the top level of the file system.

         A path does not necessarily go from the top of the hierarchy down to the target. You can
           often use a platform-specific tag in place of a name that indicates the path should go up a
            level from the current location.

         (OS X 64-bit and Linux) You specify the path of a file or directory as a series of names
          separated by the slash (/) character. If the path is an absolute path, you begin the
            specification with a slash. Indicate the path should move up a level using two periods in a
         row (..). Thus, the following path specifies a file readme relative to the top level of the file
          system, where username is the user directory:

        /usr/home/ username /myapps/readme

         The following paths are two relative paths to the same file:

          username /myapps/readme                   relative to /usr/home
        ../myapps/readme           relative to a directory inside of the username directory


          (Windows) You separate names in a path with a backslash (\) character. If the path is an
          absolute path, you begin the specification with a drive designation, followed by a colon (:),
          followed by the backslash. Indicate the path should move up a level using two periods in a
         row (..). Thus, the following path specifies a file readme relative to the top level of the file
          system, on a drive named C :

        c:\home\ username \myapps\readme

         The following paths are two relative paths to the same file:

          username \myapps\readme                relative to the home directory
        ..\myapps\readme           relative to a directory inside of the username directory


         (OS X 32-bit) You separate names in a path with the colon (:) character. If the path is an
          absolute path, you begin the specification with the name of the volume containing the file.
                 If an absolute path consists of only one name, that is, it specifies a volume, the path must
         end with a colon. If the path is a relative path, it begins with a colon. The colon is optional
            for a relative path consisting of only one name. Indicate the path should move up a level
          using two colons in a row (::). Thus, the following path specifies a file readme relative to
          the top level of the file system, on a drive named hard drive :

        hard drive:home: username :myapps:readme


1678  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1678 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1679 ordinal=1679 -->
## LabVIEW User Manual

LabVIEW User Manual


The following paths are two relative paths to the same file:

 : username :myapps:readme               relative to the home directory
 ::myapps:readme             relative to a directory inside of the username directory


Empty

You can define a path with no names, called an empty path. An empty path is either
absolute or relative. An absolute path contains the complete address of a file's location
within the file hierarchy. An empty absolute path refers to the highest point in the file
hierarchy. A relative path contains the address of a file's location relative to the position of
the user within the file hierarchy. An empty relative path refers to the current position of
the user within the file hierarchy.

(OS X 64-bit and Linux) A slash (/) represents the empty absolute path. The slash specifies
the root of the file hierarchy. A period (.) represents the empty relative path.

(Windows) You represent the empty absolute path as an empty string. The empty absolute
path specifies the set of all volumes on the system. A period (.) represents the empty
relative path.

(OS X 32-bit) The empty absolute path is represented as an empty string. The absolute path
specifies the set of all volumes on the system. A colon (:) represents the empty relative
path.


LabVIEW

In LabVIEW, you specify a path using a special LabVIEW data type, represented as Path.
The exact structure of the Path data type is private to the file manager. You create and
manipulate the Path data type using file manager routines.

A Path is a dynamic data structure. Just as you use memory manager routines to allocate
and deallocate handles and pointers, you use file manager routines to create and
deallocate a Path. Just as with handles, declaring a Path variable does not actually
create a Path. Before you can use the Path to manipulate a file, you must dynamically
allocate the Path using file manager routines. When you are finished using the Path
variable, you should release the Path using file manager routines.

In addition to providing routines for the creation and elimination of a Path, the file
manager provides routines for comparing, duplicating, determining Path characteristics,
and converting Path to and from other formats, such as the platform-specific format for
the system on which LabVIEW is running.


                                                    © National Instruments Corporation 1679

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1679 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1680 ordinal=1680 -->
## LabVIEW User Manual

LabVIEW User Manual


            File Descriptors

        When you open a file, LabVIEW returns a file descriptor associated with the file. A file
           descriptor is a data type LabVIEW uses to identify open files. All operations performed on
         an open file use the file descriptor to identify the file.

         A file descriptor is valid only while the file is open. If you close the file, the file descriptor is
         no longer associated with the file. If you open the file again, the new file descriptor is most
             likely different from the previous file descriptor.


            File Refnums

            In the file manager, LabVIEW accesses open files using file descriptors. However, on the
           front panel and block diagram, LabVIEW accesses open files using file refnums. A file
         refnum contains a file descriptor for use by the file manager and additional information
         used by LabVIEW.

         LabVIEW specifies file refnums using the LVRefNum data type, the exact structure of
         which is private to the file manager. To pass references to open files into a shared library,
          convert file refnums to file descriptors with the FRefNumToFD LabVIEW Manager function.
         To pass references to open files out of a shared library, convert file descriptors to file
          refnums with the FNewRefNum LabVIEW Manager function.

      Support Manager

         The support manager contains a collection of constants, macros, basic data types, and
           functions, such for bit or byte manipulation of data, string manipulation, mathematical
           operations, sorting, searching, and determining the current time and date.

         The string functions contain much of the functionality of the string libraries supplied with
          standard C compilers, such as string concatenation and formatting. You can use variations
           of many of these functions with LabVIEW strings, Pascal strings, and C strings. The
           following table describes the different string types.

            String Type                               Description

          LabVIEW           4-byte length field followed by data, generally stored in a handle

            Pascal                           1-byte length field followed by data

         C                              data terminated by a null character


          With the utility functions, you can sort and search on arbitrary data types, using quicksort
         and binary search algorithms. You also can convert numeric error codes to the associated
            text description.

         The support manager also contains transcendental functions for many complex and
          extended floating-point operations.


1680  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1680 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1681 ordinal=1681 -->
## LabVIEW User Manual

LabVIEW User Manual


Certain routines specify time as a data structure. The following example code illustrates
specifying time as a data structure:

typedef struct {

int32sec;/* 0:59 */

int32min;/* 0:59 */

int32hour;/* 0:23 */

int32mday;/* day of the month, 1:31 */

int32mon;/* month of the year, 1:12 */

int32year;/* year, 1600:3000 */

int32wday;/* day of the week, 1:7 for Sun:Sat */

int32yday;/* day of year (julian date), 1:366 */

int32isdst;/* 1 if daylight savings time */

} DateRec;

Signal Processing and Analysis

June 2012, 371365H-01

Use this book to learn about signal processing and analysis concepts.

© 2005–2012 National Instruments. All rights reserved.
Signal Generation in LabVIEW

The Signal Generation VIs create many common signals required for network analysis and
simulation. You also can use the Signal Generation VIs in conjunction with National
Instruments hardware to generate analog output signals.

The names of most of the Signal Generation VIs contain the word wave or pattern. These
names indicate whether a VI can keep track of the phase of the signal it generates each
time the VI is called.

      NOTE
       You can use the Signal Generation VIs only in the LabVIEW Full and Professional
       Development Systems.


                                                    © National Instruments Corporation 1681

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1681 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1682 ordinal=1682 -->
## LabVIEW User Manual

LabVIEW User Manual


        When you use a VI that requires the normalized frequency as an input, you must convert
          the frequency units to the normalized units of cycles per sample. You must use normalized
           units of cycles per sample with the following Signal Generation VIs :

                   •   Sine Wave VI
                   •   Square Wave VI
                   •   Sawtooth Wave VI
                   •   Triangle Wave VI
                   •   Arbitrary Wave VI
                   •   Chirp Pattern VI

        IIR Filter Characteristics in LabVIEW

             IIR filters in LabVIEW have the following characteristics:

                   •   The IIR Filter VI interprets values at negative indexes in the following impulse
                equations as zero the first time you call the VI.
                   x0 = 1

                        xi = 0

                    for all i ≠ 0.
                   •   A transient response, or delay, proportional to the filter order occurs before the
                       filter reaches a steady state.
                   •   The number of elements in the filtered sequence equals the number of elements in
                 the input sequence.
                   •   The filter retains the internal filter state values when the filtering process finishes.

     Curve Fitting in LabVIEW

        Some Fitting VIs return only the coefficients for the curve that best describe the input data
          while other Fitting VIs return the fitted curve. Using the VIs that return only coefficients
           allows you to further manipulate the data. The VIs that return the fitted curve also return
          the coefficients and the mean squared error (MSE). MSE is a relative measure of the
           residuals between the expected curve values and the actual observed values. Because the
           input data represents a discrete system, the VIs use the following equation to calculate
         MSE:


         where f is the sequence representing the fitted values, y is the sequence representing the
          observed values, and n is the number of observed sample points.


1682  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1682 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1683 ordinal=1683 -->
## LabVIEW User Manual

LabVIEW User Manual


The Fitting VIs automatically set up and solve the Jacobian system and return the set of
coefficients that best describes the data set.

Related information Fitting VIs
Spline Interpolation

Spline interpolation avoids the disadvantages of polynomial interpolation because
functions require more data points and the line interpolant is similar to the original
function.

Cubic spline interpolation is a common type of spline interpolation that uses a third-order
polynomial for each interval between two adjacent points. Third-order polynomials must
meet the following conditions:

    •   The first and second derivatives at interior points are continuous.
    •   The polynomials pass through all data points.
    •   For one-dimensional interpolation, the second derivatives for the beginning and
     end points are zero. For spline interpolant, the initial boundary and final boundary
       inputs specify the first derivatives at the beginning and end points. For spline
       interpolation, a line with the first derivatives behaves the same as the spline
       interpolant. For spline interpolation, a line with a natural spline behaves the same
      as one-dimensional interpolation.

For example, the equation


with natural cubic spline interpolation is shown in the following figure.


                                                    © National Instruments Corporation 1683

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1683 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1684 ordinal=1684 -->
## LabVIEW User Manual

LabVIEW User Manual


        When you have more data points of fx, the interpolant of the cubic spline interpolation is
            similar to fx, as shown in the following figure.


          Related information

           Interpolate 1D VI

           Spline Interpolant VI

           Spline Interpolation VI
      Basic Linear Algebra Subroutines

       Introduction to Basic Linear Algebra Subroutines

           Basic Linear Algebra Subroutines (BLAS) are routines that provide standard functions for
           basic vector and matrix operations. You can classify these routines in the following three
             levels:

                   •   BLAS level 1, which calculates vector operations.
                   •   BLAS level 2, which calculates matrix-vector operations.
                   •   BLAS level 3, which calculates matrix-matrix operations.

          For example, dgemm is a BLAS level 3 function that calculates the general real matrix-
          matrix product using the following expression:


         where α and β are scalars, A, B, and C are matrices, and opA is A or AT.


1684  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1684 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1685 ordinal=1685 -->
## LabVIEW User Manual

LabVIEW User Manual


Refer to BLAS (Basic Linear Algebra Subprograms) for more information on the BLAS
functions.

Related information BLAS (Basic Linear Algebra Subprograms)

Choosing Between BLAS VIs and Linear Algebra VIs

While LabVIEW provides basic Linear Algebra VIs, you can use the Basic Linear Algebra
Subroutines VIs for advanced linear algebra algorithms. Use the Basic Linear Algebra
Subroutines VIs to combine multiple linear algebra operations, reduce data copying in
LabVIEW, and optimize execution. Therefore, if you have limited memory, use the Basic
Linear Algebra Subroutines VIs.
      NOTE
       Note You can use the Basic Linear Algebra Subroutines VIs only in the LabVIEW Full
      and Professional Development Systems.

For example, the following expression combines linear algebra functions:


where α is scalar, A is a matrix, and X and Y are vectors.

With linear algebra VIs, you need five different VIs and functions to perform this
calculation, as shown in the following block diagram.


To simplify the code on a block diagram, you can replace multiple VIs and functions with
the Basic Linear Algebra Subroutines VIs. For the current example, the gemv - General
Matrix-Vector Product VI simplifies the code, as shown in the following block diagram.


                                                    © National Instruments Corporation 1685

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1685 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1686 ordinal=1686 -->
## LabVIEW User Manual

LabVIEW User Manual


          Related information Linear Algebra VIs Basic Linear Algebra Subroutines VIs gemv -
          General Matrix-Vector Product VI
      Solving ODEs in LabVIEW

         Use the ODE Solver VI to specify the ODE solver to use to evaluate an ordinary differential
           equation. You can use the ODE Solver VI only in the LabVIEW Full and Professional
         Development Systems.

         LabVIEW includes the following ODE solvers:

                   •   Runge-Kutta 1 (Euler) —A fixed step-size, single-step explicit Runge-Kutta ODE
                  solver of first order.
                   •   Runge-Kutta 2 —A fixed step-size, single-step explicit Runge-Kutta ODE solver of
               second order.
                   •   Runge-Kutta 3 —A fixed step-size, single-step explicit Runge-Kutta ODE solver of
                   third order.
                   •   Runge-Kutta 4 —A fixed step-size, single-step explicit Runge-Kutta ODE solver of
                  fourth order.
                   •   Runge-Kutta 23 —A variable step-size, single-step explicit Runge-Kutta ODE solver
                  of third order.
                   •   Runge-Kutta 45 —A variable step-size, single-step explicit Runge-Kutta ODE solver
                  of fifth order, which uses the Dormand-Prince coefficients.
                   •  BDF —A variable step-size, variable order (orders 1 through 5) implementation of
                 the multi-step backwards difference formula (BDF), also known as Gear's Method.
                 This method is adequate for moderately stiff problems.
                   •   Adams-Moulton —A variable step-size, multi-step variable order (orders 1 through
                  12) implementation of the Adams-Moulton predictor-corrector pair in predict-
                  evaluate-correct-evaluate (PECE) mode.
                   •   Rosenbrock —A variable step-size, single-step explicit solver. This method is
               adequate for some stiff problems.


1686  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1686 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1687 ordinal=1687 -->
## LabVIEW User Manual

LabVIEW User Manual


Solving PDEs in LabVIEW

Use the Partial Differential Equations VIs to solve partial differential equations (PDE),
including the Helmholtz, heat, and wave equations. The following table provides details
about these equations.

      NOTE
      The Partial Differential Equations VIs are available only in the LabVIEW Full and
        Professional Development Systems.


 Type of              Dimension and Domain   Boundary Condition       Method Equation

                                      The polygonal      The finite element
                                    domain supports    method solves the
                                           only the Dirichlet    equation defined on                 The equation is                                               condition. The    the polygonal domain. Helmholtz      two-dimensional and                                            rectangular domain   The finite difference equation      defined in a rectangular or                                            supports the      method solves the                  polygonal domain.                                                    Dirichlet and      equation defined on
                                    Neumann          the rectangular
                                                 conditions.           domain.

                 The equation is         The equation
                 one-dimensional or         supports the      The finite difference Heat                 two-dimensional and          Dirichlet and      method solves this equation               defined on the rectangular      Neumann             equation.
                     domain.                conditions.

                 The equation is         The equation
                 one-dimensional or         supports the      The finite difference Wave                 two-dimensional and          Dirichlet and      method solves this equation               defined on the rectangular      Neumann             equation.
                     domain.                conditions.


The following block diagram examples show a common order for solving PDEs with the VIs.
While you can add the VIs to the block diagram in the order they appear in the two
examples, you do not need to follow that order when you use the PDE VIs. The following list
provides an example of an order you can use when you want to solve PDEs with the VIs.

    •   Define PDE
    •   Define PDE Domain
    •   Define PDE Boundary Condition
    •   Define PDE Initial Condition
    •  PDE Solver
    •  PDE Rendering

The following block diagram illustrates an example of how to solve a 1D wave equation.


                                                    © National Instruments Corporation 1687

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1687 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1688 ordinal=1688 -->
## LabVIEW User Manual

LabVIEW User Manual


             NOTE
               The polymorphic instance you choose must match the type of equation you need
                   to solve. The type of instance also needs to be consistent from step to step.
                  Otherwise, LabVIEW returns a type conflict error.

         The following block diagram illustrates an example of how to solve a Helmholtz equation
            in a loop. The coefficient, the right side of the equation, and the domain of the equation do
          not change during the execution. While you do not need to repeatedly define the equation
         and domain in the loop, the boundary values vary over time. Therefore, you only need to
           place the definition of the boundary condition in the loop. In the following block diagram
          example, a shift register of a While Loop implements the PDE class to transfer data from
         one iteration to the next.


          Related information Partial Differential Equations VIs Define PDE VI Define PDE Domain VI
           Define PDE Boundary Condition VI Define PDE Initial Condition VI PDE Solver VI PDE
          Rendering VI
      Point-By-Point Analysis

       Point-by-Point Analysis and Array-Based Analysis in

         The approach used for most point-by-point analysis operations in LabVIEW remains the
        same as array-based analysis. You can use filters, integration, mean value algorithms, and
          so on, in the same situations and for the same reasons that you can use these operations in
          array-based data analysis. In contrast, the computation of zeros in polynomial functions is
          not relevant to point-by-point analysis, and point-by-point versions of these array-based
            VIs are not necessary.

         The following table compares array-based LabVIEW analysis to point-by-point analysis.


1688  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1688 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1689 ordinal=1689 -->
## LabVIEW User Manual

LabVIEW User Manual


 Data Analysis Technology
 Array-Based Analysis (traditional paradigm)   Point-By-Point Analysis (newer paradigm)
     •   Prepare a buffer unit of data.                •    Receive continuous stream of data.
     •   Analyze data.                                     •    Filter and analyze data continuously.
     •   Produce a buffer of analyzed data.         •      Generate real-time events and
     •   Generate report.                                   reports continuously.


The following table presents other comparisons between array-based and point-by-point
analysis.

                                             Data Acquisition and Analysis with Characteristic           Array-Based Analysis                                                         Point By Point VIs

                                              Compatible with real-time systems;                       Limited compatibility with Compatibility                                    backward compatible with                             real-time systems                                                         array-based systems

 Data typing                  Array-oriented                  Scalar-oriented

 Interruptions              Interruptions critical            Interruptions tolerated

 Operation              You observe, offline            You control, online

                     Compensate for startup     Startup data loss does not occur; Performance and                      data loss (4-5 seconds) with      initialize the data acquisition programming                     complex “state machines”   system once and run continuously

                         Reflection of a process, like Point of view                                             Direct, natural flow of a process                            a mirror

 Programming               Specify a buffer            No explicit buffers

                                             Output a report and an event in real Results                   Output a report                                                             time

 Run-time behavior        Delayed processing                  Real time

 Run-time behavior              Stop                       Continue

 Run-time behavior               Wait                   Now

 Work style                 Asynchronous                 Synchronous


When you perform point-by-point analysis, keep in mind the following concepts:

    •   Initialization —You must initialize the point-by-point analysis application to
      prevent interference from settings you made in previous sessions of data analysis.
    •   Reentrant Execution —You must enable LabVIEW reentrant execution for point-by-
      point analysis. Reentrant execution allocates fixed memory to a single analysis


                                                    © National Instruments Corporation 1689

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1689 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1690 ordinal=1690 -->
## LabVIEW User Manual

LabVIEW User Manual


                  process, guaranteeing that two processes that use the same analysis function never
                   interfere with each other.
                  NOTE
                                        If you create custom VIs to use in a point-by-point application, be sure to
                       enable reentrant execution. Reentrant execution is enabled by default in
                       almost all Point By Point VIs.
                   •   Deterministic Performance —Point-by-point analysis is the natural companion to
             many deterministic systems, because it efficiently integrates with the flow of a real-
                time data signal.

          Related information Reentrant Execution

      Performing Analysis without Buffers of Data


           Analysis functions yield solutions that characterize the behavior of a data set. In array-
         based data acquisition and analysis, you might analyze a large set of data by dividing the
          data into 10 smaller buffers. Analyzing those 10 sets of data yields 10 solutions. You can
           further resolve those 10 solutions into one solution that characterizes the behavior of the
            entire data set.

            In point-by-point analysis, you analyze an entire data set in real-time. A sample unit of a
            specific length replaces a buffer. The point-by-point sample unit can have a length that
         matches the length of a significant event in the data set that you are analyzing. For
          example, the application in a case study acquires a few thousand samples per second to
           detect defective train wheels. The input data for the train wheel application comes from
          the signal generated by a train that is moving at 60 km to 70 km per hour. The sample
           length corresponds to the minimum distance between wheels.

         A typical point-by-point analysis application analyzes a long series of sample units, but you
           are likely to have interest in only a few of those sample units. To identify those crucial
          samples of interest, the point-by-point application focuses on transitions, such as the end
           of the relevant signal.

         The train wheel detection application in the case study uses the end of a signal to identify
            crucial samples of interest. The instant the application identifies the transition point, it
          captures the maximum amplitude reading of the current sample unit. This particular
          amplitude reading corresponds to the complete signal for the wheel on the train whose
           signal has just ended. You can use this real-time amplitude reading to generate an event or
         a report about that wheel and that train.

          Related concepts Case Study of Point-By-Point Analysis


1690  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1690 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1691 ordinal=1691 -->
## LabVIEW User Manual

LabVIEW User Manual


Case Study of Point-by-Point Analysis

Case Study of Point-By-Point Analysis Application Built in
LabVIEW

This case study shows a complete point-by-point analysis application built in LabVIEW with
Point By Point VIs.

      NOTE
       You can use the Point By Point VIs only in the LabVIEW Full and Professional
       Development Systems.

Refer to the Train Wheel PtByPt VI in the labview\examples\ptbypt
\PtByPt_No_HW.llb for an example of using the Point By Point VIs.

The Train Wheel PtByPt VI is a real-time data acquisition application that detects defective
train wheels and demonstrates the simplicity and flexibility of point-by-point data analysis.

When acquiring data with real-time performance, point-by-point analysis helps you
analyze data in real time. Point-by-point analysis occurs continuously and instantaneously.
While you acquire data, you filter and analyze it, point by point, to extract the information
you need and to make an appropriate response. This case study demonstrates the
effectiveness of the point-by-point approach for generation of both events and reports in
real time.

Related information Point By Point VIs

Point-By-Point Analysis of Train Wheels

In this example, the maintenance staff of a train yard must detect defective wheels on a
train. The current method of detection consists of a railroad worker striking a wheel with a
hammer and listening for a different resonance that identifies a flaw. Automated
surveillance must replace manual testing, because manual surveillance is too slow, too
prone to error, and too crude to detect subtle defects. An automated solution also adds the
power of dynamic testing, because the train wheels can be in service during the test,
instead of standing still.

The automated solution to detect potentially defective train wheels needs to have the
following characteristics:

    •   Detect even subtle signs of defects quickly and accurately.
    •   Gather data when a train travels during a normal trip.
    •   Collect and analyze data in real time to simplify programming and to increase speed
     and accuracy of results.


                                                    © National Instruments Corporation 1691

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1691 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1692 ordinal=1692 -->
## LabVIEW User Manual

LabVIEW User Manual


         The Train Wheel PtByPt VI offers a solution for detecting defective train wheels.

             NOTE
                   This example focuses on implementing a point-by-point analysis program in
                 LabVIEW. The issues of ideal sampling periods and approaches to signal
                  conditioning are beyond the scope of this example.

       Overview of the LabVIEW Point-By-Point Solution

          As well as Point By Point VIs, the Train Wheel PtByPt VI requires standard LabVIEW
         programming objects, such as Case structures, While Loops, numeric controls, and
          numeric operators.

         The data the Train Wheel PtByPt VI acquires flows continuously through a While Loop. The
          process carried out by the Train Wheel PtByPt VI inside the While Loop consists of five
           analysis stages that occur sequentially. The following list reflects the order in which the five
           analysis stages occur, briefly describes what occurs in each stage, and corresponds to the
           labeled portions of the previous block diagram.

                1.  In the data acquisition stage (DAQ), waveform data flows into the While Loop.
                2.  In the Filter stage, separation of low- and high-frequency components of the
               waveform occurs.
                3.  In the Analysis stage, detection of the train, wheel, and energy level of the waveform
                    for each wheel occurs.
                4.  In the Events stage, responses to signal transitions of trains and wheels occurs.
                5.  In the Report stage, the logging of trains, wheels, and trains that might have
                  defective wheels occurs.

          Related information While Loop Case Structure

        Characteristics of a Train Wheel Waveform

         The characteristic waveform that train wheels emit determines how you analyze and filter
          the waveform signal point-by-point. A train wheel in motion emits a signal that contains
          low- and high-frequency components. If you mount a strain gauge in a railroad track, you
           detect a noisy signal similar to a bell curve. The following illustration shows the low- and
          high-frequency components of this curve.


         The low-frequency component of train wheel movement represents the normal noise of
           operation. Defective and normal wheels generate the same low-frequency component in
          the signal. The peak of the curve represents the moment when the wheel moves directly


1692  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1692 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1693 ordinal=1693 -->
## LabVIEW User Manual

LabVIEW User Manual


above the strain gauge. The lowest points of the bell curve represent the beginning and
end of the wheel, respectively, as the wheel passes over the strain gauge.

The signal for a train wheel also contains a high-frequency component that reflects the
quality of the wheel. In operation, a defective train wheel generates more energy than a
normal train wheel. In other words, the high-frequency component for a defective wheel
has greater amplitude.

Analysis Stages of the Train Wheel

Five Analysis Stages of the Train Wheel

The waveform of all train wheels, including defective ones, falls within predictable ranges.
This predictable behavior allows you to choose the appropriate analysis parameters. These
parameters apply to five analysis stages.

      NOTE
       You must adjust parameters for any implementation of the Train Wheel PtByPt VI
       because the characteristics of each data acquisition system differ.

DAQ Stage of the Train Wheel PtByPt VI

Data moves into the Point By Point VIs through the input data parameter. The point-by-
point detection application operates on the continuous stream of waveform data that
comes from the wheels of a moving train. For a train moving at 60 km to 70 km per hour, a
few hundred to a few thousand samples per second are likely to give you sufficient
information to detect a defective wheel.

Filter Stage of the Train Wheel PtByPt VI

The Train Wheel PtByPt VI must filter low- and high-frequency components of the train
wheel waveform. Two Butterworth Filter PtByPt VIs perform the following tasks:

    •   Extract the low-frequency components of the waveform.
    •   Extract the high-frequency components of the waveform.

In the Train Wheel PtByPt VI, the Butterworth Filter PtByPt VIs use the following
parameters:

    •   order specifies the amount of the waveform data that the VI filters at a given time
     and is the filter resolution. 2 is acceptable for the Train Wheel PtByPt VI.
    •     fl specifies the low cut-off frequency, which is the minimum signal strength that
       identifies the departure of a train wheel from the strain gauge. 0.01 is acceptable for
      the Train Wheel PtByPt VI.


                                                    © National Instruments Corporation 1693

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1693 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1694 ordinal=1694 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   fh specifies the high cut-off frequency, which is the minimum signal strength that
                    identifies the end of high-frequency waveform information. 0.25 is acceptable for
                 the Train Wheel PtByPt VI.

          Related information Butterworth Filter PtByPt VI

         Analysis Stage of the Train Wheel PtByPt VI

         The point-by-point detection application must analyze the low- and high-frequency
         components separately. The Array Max & Min PtByPt VI extracts waveform data that reveals
          the level of energy in the waveform for each wheel, the end of each train, and the end of
          each wheel.

          Three separate Array Max & Min PtByPt VIs perform the following discrete tasks:

                   •    Identify the maximum high-frequency value for each wheel.
                   •    Identify the end of each train.
                   •    Identify the end of each wheel.

             NOTE
               The name Array Max & Min PtByPt VI contains the word array only to match the
              name of the array-based form of this VI. You do not need to allocate arrays for the
                   Array Max & Min PtByPt VI.

            In the Train Wheel PtByPt VI, the Array Max & Min PtByPt VIs use the following parameters
         and functions:

                   •   sample length specifies the size of the portion of the waveform that the Train Wheel
                PtByPt VI analyzes. To calculate the ideal sample length, consider the speed of the
                     train, the minimum distance between wheels, and the number of samples you
                  receive per second. 100 is acceptable for the Train Wheel PtByPt VI. The Train Wheel
                PtByPt VI uses sample length to calculate values for all three Array Max & Min PtByPt
                     VIs.
                   •   The Multiply function sets a longer portion of the waveform to analyze. When this
                 longer portion fails to display signal activity for train wheels, the Array Max & Min
                PtByPt VIs identify the end of the train. 4 is acceptable for the Train Wheel PtByPt VI.
                   •   threshold provides a comparison point to identify when no train wheel signals exist
                   in the signal that you are acquiring. threshold is wired to the Greater? function. 3 is
              an acceptable setting for threshold in the Train Wheel PtByPt VI.

          Related information Multiply Function Greater? Function Array Max and Min PtByPt VI


1694  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1694 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1695 ordinal=1695 -->
## LabVIEW User Manual

LabVIEW User Manual


Events Stage of the Train Wheel PtByPt VI

After the Analysis stage identifies maximum and minimum values, the Events stage detects
when these values cross a threshold setting.

The Train Wheel PtByPt VI logs every wheel and every train that it detects. Two Boolean
Crossing PtByPt VIs perform the following tasks:

    •   Generate an event each time the Array Max & Min PtByPt VIs detect the transition
      point in the signal that indicates the end of a wheel.
    •   Generate an event every time the Array Max & Min PtByPt VIs detect the transition
      point in the signal that indicates the end of a train.

The Boolean Crossing PtByPt VIs respond to transitions. When the amplitude of a single
wheel waveform falls below the threshold setting, the end of the wheel has arrived at the
strain gauge. For the Train Wheel PtByPt VI, 3 is a good threshold setting to identify the end
of a wheel. When the signal strength falls below the threshold setting, the Boolean
Crossing PtByPt VIs recognize a transition event and pass that event to a report.

Analysis of the high-frequency signal identifies which wheels, if any, might be defective.
When the Train Wheel PtByPt VI encounters a potentially defective wheel, the VI passes the
information directly to the report at the moment the end-of-wheel event is detected.

In the Train Wheel PtByPt VI, the Boolean Crossing PtByPt VIs use the following parameters:

    •    initialize resets the VI for a new session of continuous data acquisition.
    •   direction specifies the kind of Boolean crossing.

Related information Boolean Crossing PtByPt VI

Report Stage of the Train Wheel PtByPt VI

The Train Wheel PtByPt VI reports on all wheels for all trains that pass through the data
acquisition system. The Train Wheel PtByPt VI also reports any potentially defective
wheels.

Every time a wheel passes the strain gauge, the Train Wheel PtByPt VI captures its
waveform, analyzes it, and reports the event. The following table describes the
components of a report on a single train wheel.

 Information Source                        Meaning of Results

 Counter mechanism for         Stage One: Wheel number four has passed the strain
 waveform events                                   gauge.

 Analysis of highpass filter        Stage Two: Wheel number four has passed the strain
 data                             gauge and the wheel might be defective.


                                                    © National Instruments Corporation 1695

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1695 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1696 ordinal=1696 -->
## LabVIEW User Manual

LabVIEW User Manual


           Information Source                        Meaning of Results

           Counter mechanism for       Stage Three: Wheel number four in train number eight has
             end-of-train events          passed the strain gauge, and the wheel might be defective.


         The Train Wheel PtByPt VI uses point-by-point analysis to generate a report, not to control
         an industrial process. However, the Train Wheel PtByPt VI acquires data in real time, and
         you can modify the application to generate real-time control responses, such as stopping
          the train when the Train Wheel PtByPt VI encounters a potentially defective wheel.

      Accessing Scanned I/O Data
           This section provides information on using and accessing I/O variables in LabVIEW.
      Using I/O Variables (Real-Time, Windows)

         An I/O variable is a type of shared variable that transfers I/O data. When accessed locally,
           I/O variables use the NI Scan Engine for single-point access to I/O data. When accessed
           remotely, I/O variables use the NI Publish-Subscribe Protocol (NI-PSP) for single-point or
           buffered access to I/O data. An I/O variable can communicate directly with a physical I/O
          channel or can transfer custom I/O data between an FPGA VI and a real-time (RT) VI running
         on the same target.

              CAUTION
               The NI Scan Engine does not buffer data. To avoid losing data when accessing I/O
                   variables locally, you must read each data point before the next point arrives and
                  avoid writing data faster than the NI Scan Engine period.

         The following table summarizes the use cases for I/O variables:

          Use                                                             I/O Variable Type

            Transferring scaled I/O data between the I/O hardware and a  I/O Variables for Scaled I/O
          LabVIEW VI without using the LabVIEW FPGA Module                  Data

            Transferring custom FPGA-processed I/O data between a                                                                           I/O Variables for Custom          LabVIEW FPGA VI and a LabVIEW Real-Time VI running on the                                                             FPGA I/O Data         same hardware device


             NOTE
                   Refer to the specific hardware device documentation for information about NI
                Scan Engine support.


1696  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1696 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1697 ordinal=1697 -->
## LabVIEW User Manual

LabVIEW User Manual


I/O Variables for Scaled I/O Data

To use I/O variables for scaled I/O data, you first must connect a supported I/O device to a
target with the NI Scan Engine installed and then add the I/O device to the target in
LabVIEW project.

When you add a supported I/O device to a supported target in the Project Explorer window,
LabVIEW automatically adds an I/O variable for each I/O channel. If you physically add an
I/O device to a target included in the current LabVIEW project, you must add the new I/O
device to the project and deploy the corresponding I/O variables before you can use them.

If you physically remove an I/O device from a target that is part of the current LabVIEW
project, you must delete the I/O device from the project and redeploy the target that
contained the I/O device. Redeploying the target ensures that the configuration on the
target reflects the project configuration. You can use the Project & System Comparison
dialog box to ensure that the project and target configurations match.


I/O Variables for Custom FPGA I/O Data (FPGA Module or Real-Time Module)

If the project includes an FPGA target that supports the NI Scan Engine, you can create
user-defined I/O variables to transfer custom I/O data between FPGA VIs and RT VIs running
on the same hardware device.

You can add user-defined I/O variables to the block diagrams of FPGA VIs and RT VIs
running on the chassis that hosts the user-defined I/O variables. However, because all I/O
variables are unidirectional, you must configure the direction of each user-defined I/O
variable as either FPGA to Host or Host to FPGA. For example, you can acquire analog I/O
data and perform an FFT on the data in an FPGA VI, use an FPGA to Host I/O variable to
transfer the processed data to a control loop in an RT VI, then use a Host to FPGA I/O
variable to transfer output data from the RT control loop back to the FPGA for output to the
physical I/O channel.

You must install the LabVIEW FPGA Module to create user-defined I/O variables. However, if
you have only the Real-Time Module, you can access user-defined I/O variables from RT VIs
even if you do not install the LabVIEW FPGA Module. For example, a developer with the
LabVIEW FPGA Module could create user-defined I/O variables and compile an FPGA bitfile
that accesses those variables. Then that developer could distribute the bitfile and the
LabVIEW project containing the user-defined I/O variables to another developer without
the FPGA Module, who could use the project to run the bitfile on a CompactRIO chassis. In
this case, the second developer could not create new user-defined I/O variables but could
use the Real-Time Module to access the user-defined I/O variables created by the first
developer.

(Windows) If network publishing is enabled on a user-defined I/O variable, you can use the
variable in any RT VI or Windows-based VI within the same LabVIEW project. For example,
you can use network-published I/O variables to create a user interface VI that runs on
Windows.

      NOTE
        User-defined I/O variables support scanned access only. You cannot use direct
       access for user-defined I/O variables.


                                                    © National Instruments Corporation 1697

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1697 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1698 ordinal=1698 -->
## LabVIEW User Manual

LabVIEW User Manual


          Configuring I/O Variables

         You can configure I/O variables interactively at edit-time or run-time or programmatically
           at run-time. You also can use a combination of these methods. The following table
         summarizes the advantages and disadvantages of each method:

          Method              Use Case             Advantages        Disadvantages

                                                                                                                 •    Configuration
                                                                                          settings are
                                                                               not visible
                                                                 when you
                                                                           view the block
                                                                                 diagram.                           Configuring settings for I/O
                              variables when you have      Requires less           •      You can             Interactive                             access to the Project       programming.                                                                                     configure
                                Explorer window.                                                                                         settings for an
                                                                                       I/O variable
                                                                                 only on the
                                                                                          target that
                                                                                    hosts the
                                                                                              variable.


1698  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1698 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1699 ordinal=1699 -->
## LabVIEW User Manual

LabVIEW User Manual


 Method              Use Case             Advantages        Disadvantages

                           •    Configuring settings
                            for I/O variables
                   when you do not
                     have access to the
                          Project Explorer
                       window. For
                     example, if you plan
                            to create a
                          stand-alone
                       application that uses
                    an I/O variable and
                    you need to change
                           configuration           •   Configuration
                         settings for the I/O           settings are
                           variable while              visible when
                         running the           you view the
                            application,                block                                                                  Requires more Programmatic                         configure the I/O            diagram.      programming.
                              variable                                                                   •     You can                       programmatically.                                                   configure I/O
                           •    Configuring settings           variables
                           for an I/O variable            remotely.
                      from a computer
                      other than the target
                         that hosts the I/O
                             variable. For
                     example, if you need
                        to configure an I/O
                            variable on a
                    CompactRIO target
                        from a host
                     computer, configure
                        the I/O variable
                       programmatically.


Configuring I/O Variables Interactively

Use the Shared Variable Properties dialog box to configure a single I/O variable or the
Multiple Variable Editor window to configure multiple I/O variables simultaneously.

You can update the description, network, and scaling options of an I/O variable even while
running a VI that uses the I/O variable. However, you cannot update the name or data type
of an I/O variable at run-time.

      NOTE
      When you add a new I/O variable or change the configuration of an I/O variable,
       you must deploy the variable to activate the new configuration.


                                                    © National Instruments Corporation 1699

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1699 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1700 ordinal=1700 -->
## LabVIEW User Manual

LabVIEW User Manual


          Configuring I/O Variables Programmatically

         Complete the following steps to use the Variable properties to configure an I/O variable
          programmatically:

                1.  Add the Variable Property Node to the block diagram.
                2.  Right-click the reference input and select Create»Constant from the shortcut
              menu.
                3.  Click the arrow button on the right side of the shared variable refnum constant and
                   select Browse.
                4.  Use the Browse Variable Object dialog box to select the I/O variable you want to
                  configure.
                5.  Right-click the shared variable refnum constant and use the Select Variable Class
                 shortcut menu to select the class of the property you want to use.
                6.  Click the white area of the Variable Property Node and select the property you want
                  to use.
                7.  (Optional) Use the Positioning tool to resize the Variable Property Node to display
              more than one property simultaneously.

         The following figure shows an example of programmatically configuring an I/O variable on
         a remote target:


            In this example, the Variable Property Node specifies the current limit for a channel on a
         CompactRIO module by configuring the I/O variable that corresponds to that channel.

             NOTE
                             If the Variable Property Node cannot connect to the remote I/O variable after five
                  seconds, the configuration call times out. Complete the following steps to change
                     this timeout period:
                         1.  Open the labview\LabVIEW.ini file as a text file.
                         2.  On a new line, enter RemoteIOVConfigurationTimeout= followed
                      by the new timeout period in number of seconds. For example, if you want
                         to extend the timeout period to 10 seconds, enter
                  RemoteIOVConfigurationTimeout=10.
                         3.  Save and close the file.


1700  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1700 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1701 ordinal=1701 -->
## LabVIEW User Manual

LabVIEW User Manual


Deploying I/O Variables

To deploy I/O variables, right-click the project item that contains the I/O variables in the
Project Explorer window and select Deploy from the shortcut menu.

When you run a VI that contains I/O variable nodes, LabVIEW automatically deploys the I/O
variable containers to which those I/O variables belong. This action deploys all of the I/O
variables in the containers.

      NOTE
            If an I/O driver fails to initialize, LabVIEW aborts loading all I/O variables in the
        project. In this case, the I/O variables might still appear in the project, but if an
        application attempts to access the variables, a run-time error occurs. Refer to the
         specific target I/O driver documentation for information about debugging I/O
        driver errors.


Scaling I/O Variable Values

You can enable linear scaling on an I/O variable or alias on the Scaling page of the Shared
Variable Properties dialog box. However, I/O variables do not support nonlinear scaling.

      NOTE
      Some I/O buses implement hardware scaling. In this case, LabVIEW I/O variable
        scaling provides an additional scaling layer. LabVIEW does not overwrite the
       hardware scaling. LabVIEW uses the hardware-scaled value from the I/O bus as the
       raw value when calculating the software-scaled value.


Creating I/O Aliases

You can create aliases of an I/O variable to name and scale the I/O data differently in
different contexts. For example, if you have an I/O variable connected to a thermocouple
input, you can create a Celsius alias and a Fahrenheit alias. Then you could scale each alias
and use the aliases to display the temperature in both units of measure.

The value of an I/O alias is linked bidirectionally to the value of the parent, so updating the
value of the parent updates the value of the I/O alias, and updating the value of the I/O
alias updates the value of the parent. By extension, updating any link in a chain of I/O
aliases updates all other links in the chain.


Creating a Single I/O Alias

To create an I/O alias, right-click a target that contains I/O variables in the Project Explorer
window and select New»Variable from the shortcut menu to display the Shared Variable
Properties. Enter a name for the I/O alias and select I/O Alias from the Variable Type pull-


                                                    © National Instruments Corporation 1701

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1701 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1702 ordinal=1702 -->
## LabVIEW User Manual

LabVIEW User Manual


        down menu. Then click the Browse button and select the existing I/O variable or I/O alias
           to which you want to bind the new I/O alias.

             NOTE
              When you bind an alias to an I/O variable, ensure that the data type of the alias
                matches the data type of the underlying I/O variable.

         You can use the Project Explorer window to edit the name, description, network-publishing
            settings, and scaling of an I/O alias. You also can use the Multiple Variable Editor window to
            edit multiple I/O aliases simultaneously.

             NOTE
                You cannot deploy a library that contains both I/O aliases and other types of
                 shared variables. You must deploy I/O aliases in a separate library.


          Creating Multiple I/O Aliases Simultaneously

         You can use the Batch Variable Creation dialog box to create multiple I/O aliases
           simultaneously. Complete the following steps to batch create I/O aliases:

                1.  Create a single I/O alias to use as a template for the batch creation process.
                2.  Right-click the variable library that contains the I/O alias and select Create
                 Variables from the shortcut menu to display the Batch Variable Creation dialog box.
                3.  Select Copy properties from, click the Browse button, and select the existing I/O
                    alias that you want to use as a template.
                4.  Enter the number of I/O aliases you want to create in the Number to create field
              and click the OK button to create the new I/O aliases.

            After you complete these steps, LabVIEW automatically opens the Multiple Variable Editor
         window, which you can use to edit the new variables. For example, you might want to edit
          the Alias Path of each I/O alias to bind to a unique I/O variable.


          Forcing I/O Variable Values

         You can force the value of an I/O variable either interactively or programmatically. Forcing
         an I/O variable causes the associated I/O data to assume the value you specify until you
          unforce the variable, reboot the target, or force the variable to assume a different value.
          Unforcing an I/O variable returns control of the I/O value to the NI Scan Engine.

             NOTE
              When an I/O variable is forced, each I/O variable access takes slightly longer than
              when the variable is not forced, which could cause a loop to run late if the loop
                  period is not long enough to accommodate the forcing overhead.


1702  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1702 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1703 ordinal=1703 -->
## LabVIEW User Manual

LabVIEW User Manual


Forcing I/O Variable Values Interactively

Use the NI Distributed System Manager to force or unforce the value of an I/O variable
during debugging or to manually control an I/O channel. From LabVIEW, select
Tools»Distributed System Manager to launch the NI Distributed System Manager. You
also can launch the Distributed System Manager by right-clicking an RT target in the
Project Explorer window and selecting Utilities»View in System Manager.

      NOTE
       You can use the NI Distributed Manager security settings to prevent users from
        forcing I/O variables from within the NI Distributed System Manager.


Forcing I/O Variable Values Programmatically

Use the Forcing VIs to force and unforce I/O variables programmatically.


Forcing I/O Aliases

Forcing applies to aliases as well as standard I/O variables. When you force an I/O variable,
you also force all associated aliases. When you force an alias, you also force the parent I/O
variable and all other associated aliases.

      NOTE
       LabVIEW applies scaling to forced values as if the forced value were the actual
       value of the I/O channel. So, when you force one link in a chain of aliases, all links
        in the chain scale appropriately.


Forcing and Unforcing all I/O Variables on a Target Simultaneously

You can use the global forcing state of a target to force and unforce all I/O variables on the
target simultaneously. You can enable and disable global forcing on a target either
interactively or programmatically.

Use the Enable Forcing and Disable Forcing buttons in the NI Distributed System Manager
to enable and disable global forcing on a target interactively. Use the Enable Variable
Forcing and Disable Variable Forcing VIs to enable and disable global forcing on a target
programmatically.

Complete the following steps to force all the I/O variables on a target simultaneously:

   1.  Disable forcing on the target so that you can set the desired forcing values of the I/O
       variables individually without individually forcing the I/O variables.
   2.  Set the desired forcing values for all the I/O variables on the target.
   3.  Enable forcing on the target to force all I/O variables on the target simultaneously.


                                                    © National Instruments Corporation 1703

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1703 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1704 ordinal=1704 -->
## LabVIEW User Manual

LabVIEW User Manual


          Accessing I/O Variables Remotely

                 If network-publishing is enabled on an I/O variable, you can access the I/O variable from a
         remote computer connected to the same network as the target that hosts the I/O variable.
         You can access remote I/O variables interactively using the I/O Variable Probe view in the NI
           Distributed System Manager. You also can access remote I/O variables programmatically in
         a VI.

         Use the Shared Variable Properties dialog box to enable and disable network publishing on
         an I/O variable. Enable network-publishing if you need to monitor I/O values on a host
         computer or access an I/O variable from a remote target. Use the Scan Engine page to set
          the global network-publishing rate for all I/O variables on a target.

             NOTE
                             If you do not plan to access I/O variables remotely, disable network publishing to
                 minimize CPU overhead. When you disable network publishing on an I/O variable
                  or I/O alias, you cannot access the variable from a VI running on another computer.
                 However, you still can force the variable from the NI Distributed System Manager.
                To prevent users from forcing an I/O variable, use the System Manager security
                     settings.


          Accessing I/O Variables Locally

         LabVIEW adds I/O variables to a global scan engine memory map and updates the values of
              all I/O variables concurrently. However, for I/O variable access on the local target that hosts
          the I/O variable, you can configure each node to use either scanned access or direct access.

         Complete the following steps to select the local access mode of an I/O variable node:

                1.  Right-click an I/O variable node on the block diagram.
                2.  Select Local Access Mode from the shortcut menu
                3.  Select the access mode you want to use for the node.

             NOTE
                LabVIEW adds all I/O variables to the global scan engine memory map regardless
                   of the access mode you use for each variable.


          Selecting a Local Access Mode

            In general, scanned access is appropriate for groups of I/O channels with similar update
            rates, and direct access is appropriate for individual I/O channels that update
          asynchronously to the scan period. The following table summarizes when to use each I/O
          access method:

                                                                                 Access        Common Use                                                                     Method

            Single-point access to I/O channels that share a common update rate       Scanned


1704  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1704 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1705 ordinal=1705 -->
## LabVIEW User Manual

LabVIEW User Manual


                                                                       Access Common Use                                                            Method

 Single-point access to local I/O channels asynchronous to the NI Scan
 Engine period, such as a single write for an emergency stop output (not        Direct
 supported for user-defined I/O variables)


      NOTE
       You can use direct access for I/O channels that update slower than the NI Scan
       Engine period. However, in such cases, scanned access typically provides the same
        I/O behavior more efficiently than direct access.


Scanned Access

By default, LabVIEW configures I/O variable nodes to use scanned access. Use scanned
access for sets of I/O channels that update at a single rate and for expansion I/O channels.
Scanned access uses the scan engine memory map to perform non-blocking I/O reads and
writes, as shown in the following figure:


Each time you read from an I/O variable using scanned access, the NI Scan Engine
immediately returns the most recent value stored in the memory map without blocking, or
waiting for a new value. During each scan, LabVIEW reads the most recent I/O value and
writes that value to the NI Scan Engine memory map.

Each time you write to an I/O variable using scanned access, you overwrite the previous
value stored in the scan engine memory map. During each scan, LabVIEW pushes the value
stored in the memory map to the physical I/O channel. To prevent data loss, you must
synchronize all I/O variable write operations to the scan period.


Direct Access

Use direct access to read or write single-point local I/O channels asynchronously to the
scan period. You can use direct access when the application needs to write a value as soon
as possible. Direct access bypasses the scan engine memory map and communicates
directly with the I/O device driver to perform non-blocking I/O reads and writes, as shown
in the following figure:

      NOTE
        User-defined I/O variables do not support direct access.


                                                    © National Instruments Corporation 1705

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1705 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1706 ordinal=1706 -->
## LabVIEW User Manual

LabVIEW User Manual


             NOTE
                             If you use the NI Scan Engine in conjunction with the RIO Scan Interface, the
                hardware scan signal governs updates to I/O. If you write a value via direct access
                under the idle state of the hardware scan signal, the value propagates to the
                hardware after the idle state of the hardware scan signal ends.

             NOTE
               The speed of direct access varies by controller, I/O module, and communication
                   protocol. Refer to the specific hardware documentation for more information
                about I/O access speed.


           Interpreting I/O Variable Node Icons

         Each I/O variable node on the block diagram includes a glyph to indicate one of the
           following access methods:

           Access Method                              Node Appearance

           NI-PSP

          Scanned

             Direct


            Data Communication Methods Home
      Accessing Scanned I/O Data (Real-Time, Windows)
         Use the NI Scan Engine for single-point access to scanned I/O data.


          Using the NI Scan Engine

         The NI Scan Engine enables efficient single-point access to sets of data channels, such as
           I/O channels, using a scan that stores data in a global memory map and updates all values
           at a single rate, known as the scan period. The NI Scan Engine installs on LabVIEW for


1706  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1706 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1707 ordinal=1707 -->
## LabVIEW User Manual

LabVIEW User Manual


Windows by default. You also can install the NI Scan Engine on supported LabVIEW targets,
such as RT Series PXI and CompactRIO targets. Refer to the specific hardware device
documentation for information about NI Scan Engine support.

(Real-Time Module) By default, the NI Scan Engine runs in a thread above time-critical
priority on RT targets, although LabVIEW includes the scan thread in the time-critical
category when reporting CPU usage statistics. When running the NI Scan Engine at above
time-critical priority, you must synchronize the deterministic sections of the application
with the scan period to ensure that the scan thread does not affect the determinism of the
application. For applications in which I/O is not the highest-priority task, you also can
configure the priority of the scan engine to fall between time-critical and Timed Structure
priority. If you do not plan to use I/O variables on a target, do not install the NI Scan Engine
on the target. If the NI Scan Engine is already installed on the target, you can use
Measurement & Automation Explorer (MAX) to uninstall the NI Scan Engine.

      NOTE
       (Windows) The only NI Scan Engine priority available on Windows is normal
         priority. Because of the non-deterministic nature of the Windows operating
       system, the timing of the NI Scan Engine is not guaranteed when running on
       Windows.


Configuring NI Scan Engine Settings

Use the Scan Engine page to configure scan engine settings including the scan period,
network-publishing rate, and priority level of the NI Scan Engine.

Use the NI Distributed System Manager to monitor and manage scan engine faults and
modes. Select Tools»Distributed System Manager to display the NI Distributed System
Manager. You also can use the NI Scan Engine VIs to view and configure scan engine
settings programmatically.


Deploying and Running the NI Scan Engine

After you configure NI Scan Engine settings in the Project Explorer window, you must
deploy a project item that uses the NI Scan Engine, such as My Computer or an RT target,
for the settings to take effect.

(Windows) The NI Scan Engine starts running the first time you deploy the target and stops
running when you close the project. To automatically deploy the NI Scan Engine and I/O
variables when a built application runs, you must enable the Include target hardware
configuration checkbox on the Advanced page of the Application Properties dialog box
before building the application.

(Real-Time Module) When running on an RT target, the NI Scan Engine starts automatically
when you boot the target and runs continuously until you shut down the target.

A single computer can run only a single instance of the NI Scan Engine at a time. For
example, if you create a Windows built application that uses the NI Scan Engine, you must
close the project from which you built the application before you can run the application
on the same computer. Although you can configure multiple instances of the NI Scan
Engine in multiple LabVIEW projects, deployment of subsequent projects using the NI Scan


                                                    © National Instruments Corporation 1707

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1707 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1708 ordinal=1708 -->
## LabVIEW User Manual

LabVIEW User Manual


          Engine fails if an instance of the NI Scan Engine is running. To run a different instance of the
          NI Scan Engine, you first must stop the current instance.


         Scan Engine Timing

         The NI Scan Engine executes at regular intervals determined by the Scan Period you
           specify on the Scan Engine page. Choose a period long enough to accommodate both the
          scan itself and the application logic, as shown in the following illustration:


             NOTE
               The length of the scan depends on the number and type of I/O items deployed to
                  the target. To maximize scan engine performance, undeploy any I/O items that you
               do not plan to use in the application.

         Use the Get Scan Engine Period VI to read the scan period programmatically. Use the Set
         Scan Engine Period VI to set the scan period programmatically.

             NOTE
                  (Real-Time Module) Real-time loops generally need one or two warm-up iterations
                   to begin executing deterministically. Before checking to ensure that an application
                meets timing requirements, you should allow each time-critical loop to execute
               warm-up iterations.


          Synchronizing to the Scan Engine

           (Real-Time Module) Unless you configure the NI Scan Engine to run below time-critical
             priority, you must synchronize time-critical code to the scan period to avoid collisions that
          could affect the determinism of the application.

         Use the Synchronize to Scan Engine timing source to synchronize timed structure
          execution to the scan engine. If you do not want to use a timed structure, you can use the
          Synchronize to Scan Engine VI to synchronize to the scan engine. Both synchronization
         methods trigger execution at the time labeled End of Scan in the previous illustration. To
          use I/O variables as a coherent data set, ensure that the synchronized code finishes
           executing before the next scan iteration. However, you can skip scan iterations if the code
         does not depend on a coherent data set.

             NOTE
                             If synchronized code does not finish executing before the next scan iteration, the
                  information reported by the error cluster of an I/O variable might lose
                  synchronization with the I/O value.


1708  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1708 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1709 ordinal=1709 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
      When you click the Abort button on a VI that involves synchronization to the NI
       Scan Engine, the VI does not abort until the current scan iteration completes, so
       the VI might appear to hang temporarily if the scan period is sufficiently long.


NI Scan Engine Modes

      NOTE
       Only certain targets and devices use NI Scan Engine modes. CompactRIO targets
       with local I/O modules do not use NI Scan Engine modes. Refer to the I/O hardware
       documentation for information about hardware-specific mode behavior.

LabVIEW defines four NI Scan Engine modes:

 0  Initialization Mode               Occurs only briefly during startup.

                      The required mode when configuring scan engine settings on 1 Configuration Mode                               hardware that uses NI Scan Engine modes.

 2     Active Mode      The mode in which the scan engine runs and updates values.

 3     Fault Mode     The mode triggered when a major or unrecoverable fault occurs.


      NOTE
        Fault mode behavior varies by target. Refer to the specific target hardware
       documentation for information about fault mode behavior.

Use the NI Distributed System Manager to view and configure the scan engine mode. The
NI Distributed System Manager displays the value of the scan engine mode using the
EngineState status item. Use the Get Scan Engine Mode VI to read the scan engine mode
programmatically. Use the Set Scan Engine Mode VI to set the scan engine mode
programmatically.


   Data Communication Methods Home
NI Scan Engine Faults (Real-Time, Windows)

Targets with the NI Scan Engine installed use faults to address asynchronous error
conditions. LabVIEW defines three fault levels: minor, major, and unrecoverable. LabVIEW
logs all faults in memory on the target. Use the Scan Engine Probe view in the NI
Distributed System Manager to view and clear NI Scan Engine faults on a target.

Minor faults are equivalent to warnings and do not trigger fault handling behavior.
Examples of minor faults include startup errors, which can occur when the controller is
unable to apply its saved configuration on startup.


                                                    © National Instruments Corporation 1709

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1709 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1710 ordinal=1710 -->
## LabVIEW User Manual

LabVIEW User Manual


          Major faults are equivalent to errors. For example, if LabVIEW detects that the scan engine
          has run late, LabVIEW triggers major fault −66460. If LabVIEW detects ten consecutive late
          scan iterations, LabVIEW triggers major fault −66461 and the NI Scan Engine stops running.

             NOTE
             Some I/O hardware drivers implement fault handling behavior in response to
                major faults. Refer to the specific hardware documentation for information about
                     fault handling behavior.

          Unrecoverable faults can occur due to a hardware failure or software crash. In the event of
         an unrecoverable fault, reboot the controller and contact National Instruments.


         Viewing and Clearing Faults

         Use the NI Distributed System Manager to view and clear faults. You also can use the Get
           Fault List VI and the Clear Fault VI to view and clear faults programmatically. Clearing a
            fault removes the fault from memory as if the fault had never occurred.


         System Faults

         LabVIEW defines a set of common faults. You can log additional faults based on LabVIEW
           error clusters. LabVIEW groups fault codes by type, as shown in the following table:

             NOTE
                   Refer to the specific hardware documentation for information about fault handling
                   behavior.


            Fault Type                                   Range of Fault Codes

            I/O Scan Driver Errors                            −66000 through −66099

            I/O Variables                                   −66200 through −66299

           NI Scan Engine VIs                              −66300 through −66399

           NI Scan Engine                                 −66400 through −66499

           User Fault                                   Any LabVIEW error code


          Triggering Faults

         You can use the Set Fault VI to trigger minor or major faults based on LabVIEW error codes.
         To trigger a custom fault, you can define a custom error code and then pass that code to
          the Set Fault VI.

         LabVIEW reserves a memory pool large enough to log up to 100 unique fault codes. If you
          exceed 100 unique fault codes, LabVIEW triggers minor fault −66420 and stops logging
           additional faults. However, even if the maximum number of user faults has been reached, a


1710  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1710 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1711 ordinal=1711 -->
## LabVIEW User Manual

LabVIEW User Manual


major or unrecoverable fault still can trigger hardware drivers to initiate fault handling
behavior.


Configuring Faults

You can customize the level and triggering behavior of specific faults with custom fault
configurations. You can apply custom fault configurations either interactively or
programmatically.

Use the Fault Configuration section of the Scan Engine page to apply custom fault
configurations interactively. Use the Fault Configuration VIs to apply custom fault
configurations programmatically.

Some faults cannot be configured. However, the list of configurable faults depends on
which NI Scan Engine I/O software is installed. Use the Configurable Faults list in the Fault
Configuration section of the Scan Engine page to view the list of configurable faults
interactively.
Reading and Writing I/O Variable Containers as
Arrays (Real-Time, Windows)

By accessing the channels of an I/O variable container as a single array, you can optimize
performance and streamline the block diagram. Use the Shared Variable functions to read
and write local I/O variable containers as arrays.


Specifying I/O Variable Containers

An I/O variable container is an item in a LabVIEW project that contains I/O variables. Use
one of the following methods to specify an I/O variable container to read or write on the
block diagram:

    •   Use a variable refnum control or constant to specify the I/O variable container using
     one of the following methods:
            ◦   By finding the I/O variable container programmatically
            ◦   By building the URL string programmatically on the block diagram
            ◦   By typing the URL of the container into the constant
            ◦   By using the Browse Variable Object dialog box to find the container
               interactively
    •   Find the I/O variable container programmatically.


Reading and Writing I/O Variable Containers

You can wire a reference to an I/O variable container to the shared variable refnum in
input of one of the following functions:


                                                    © National Instruments Corporation 1711

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1711 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1712 ordinal=1712 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Read Variable
                   •   Write Variable
                   •   Direct Variable Read
                   •   Direct Variable Write
                   •   Scanned Variable Read
                   •   Scanned Variable Write

        When you use one of the read functions in the previous list to read an I/O variable
           container, the function returns an array that contains the data for each channel in the I/O
           container. The order of the channels in the array corresponds to the order of the channels
           that the All Variables property returns. When you use one of the write functions in the
          previous list to write an I/O variable container, you must wire an array indexed in this same
           order.

          For example, the following block diagram uses the Scanned Variable Read function to read
              all the I/O channels in the analog input module Mod1 as an array of doubles:


         Unsupported Features

         The techniques described in this topic do not support the following features:

          Unsupported Feature                                 Details

           Reading and writing I/O       You can specify only one data type for an I/O variable
            variable containers that        container. Therefore, reading or writing an I/O variable
            include multiple data       container with channels of multiple data types results in an
           types                                                        error.

                                        This technique applies only to local I/O variable containers.
           Reading and writing PSP       You cannot use this technique to access I/O variable
            variable containers          containers remotely or to access network-published shared
                                                              variable libraries.

           Reading timestamps       You cannot enable timestamps when using this technique.


            Data Communication Methods Home


1712  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1712 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1713 ordinal=1713 -->
## LabVIEW User Manual

LabVIEW User Manual


PID and Fuzzy Logic

Use PID and Fuzzy Logic VIs for Proportional-Integral-Derivative (PID) and fuzzy logic
control. These VIs appear under the Control & Simulation palette. You can use the PID VIs
with input/output (I/O) functions such as data acquisition (DAQ) to implement control of
physical processes.


PID Control

The Proportional-Integral-Derivative (PID) algorithm is the most common control
algorithm used in industry. A PID controller is a feedback controller you can use to control
processes such as heating and cooling systems, fluid level monitoring, flow control,
pressure control, and so on. You can use the PID VIs with National Instruments hardware
such as a DAQ device, FieldPoint I/O module, or GPIB board, to connect your PC to a system
and develop LabVIEW control applications. You also can use the PID VIs with LabVIEW math
and logic functions to create block diagrams for real control strategies.


Fuzzy Logic

Fuzzy logic is a method of rule-based decision making for expert systems and process
control. Fuzzy logic differs from traditional Boolean logic in that fuzzy logic allows for
partial membership in a set. You can use fuzzy logic to control processes represented by
subjective, linguistic descriptions. You can wire acquired data to a fuzzy controller to
implement real-time decision making or control of a physical system. You also can use
outputs of the fuzzy controller with DAQ analog output hardware to implement real-time
process control.

Use the Fuzzy System Designer to design a fuzzy system interactively. Use the Fuzzy Logic
VIs to design and control fuzzy systems programmatically.

      RELATED INFORMATION
       PID Control on page 1747
       Fuzzy Logic on page 1739

Tutorial: Using the Fuzzy System Designer

You can use the PID and Fuzzy Logic VIs to design a fuzzy system in one of two ways: using
the Fuzzy System Designer or using the Fuzzy Logic VIs. This tutorial teaches you to design
a fuzzy system interactively using the Fuzzy System Designer.

       TIP
        Refer to the Modifying a Fuzzy System with the Fuzzy Logic VIs tutorial to learn how
        to design and modify fuzzy systems using the Fuzzy Logic VIs.


                                                    © National Instruments Corporation 1713

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1713 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1714 ordinal=1714 -->
## LabVIEW User Manual

LabVIEW User Manual


            In this tutorial, you use the Fuzzy System Designer to design a fuzzy system similar to the
           vehicle maneuvering example described in the topics on fuzzy system design. As a
           reference, you can find the complete fuzzy system you design in this tutorial, Truck -
        backward.fs, in the labview\examples\control\fuzzy\Car Parking
            directory.

          Next 1. Creating Input Linguistic Variables

       Creating Input Linguistic Variables

         The first step in designing a fuzzy system with the Fuzzy System Designer is to create the
           input and output linguistic variables for the system. In the vehicle maneuvering example
          described in the topics on fuzzy system design, the fuzzy system has two linguistic input
            variables, Vehicle Position x and Vehicle Orientation β, and one linguistic output variable,
           Steering Angle φ.

                 TIP
               The graphs in the Creating Membership Functions topic illustrate the range and
               membership functions for each of these linguistic variables.

         Complete the following steps to create an input linguistic variable that corresponds to the
           Vehicle Position x input linguistic variable of the vehicle maneuvering example.

                1.  Select Tools»Control Design and Simulation»Fuzzy System Designer to launch
                 the Fuzzy System Designer and display the Variables page.
                2.  Click the Add Input Variable button to the right of the Input variables list to
                  display the Edit Variable dialog box.
                3.  In the Name text box, enter vehicle-position.
                4.  Specify the Range by entering 0 in the minimum field and 10 in the maximum
                      field. This specifies that the position of the vehicle relative to the destination ranges
               from 0.0 to 10.0 meters.
                5.  Click the Add Membership Function button under the Membership functions
                  control to enable the control and create a new membership function for the vehicle-
                  position linguistic variable.
                6.  In the Name text box, enter left.
                7.  Select Trapezoid from the Shape pull-down menu to specify that a trapezoid
                 function determines the degrees of membership for the linguistic variable.
                8.  Click the Color field to select the color to use for the membership function in the
              Membership functions graph.
                9.  In the Points array, enter the following numbers, one for each element of the array:
                  0, 0, 1, 4. These points specify the values of the linguistic variable corresponding to
                 the base and top points, in order from left to right and base to top, of the
              membership function.
              10. Repeat steps 5 through 9 for each of the following membership functions for Vehicle
                  Position x, using the shape and points shown in the following table:


1714  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1714 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1715 ordinal=1715 -->
## LabVIEW User Manual

LabVIEW User Manual


Membership Function                            Shape             Points

                    Triangle                                  3, 4, 5

                    Triangle                                4.5, 5, 5.5

                    Triangle                                  5, 6, 7

                 Trapezoid                              6, 9, 10, 10


          NOTE
           The Points array requires that each point for a given membership function
           be greater than or equal to all previous points. If the array automatically
            changes your entries to fit this requirement, try entering points from left to
                right.

     You can compare the Membership functions graph to the Vehicle Position graph in
     the Creating Membership Functions topic to confirm your entries.
  11. Click the OK button to save your changes and return to the Variables page. The
      vehicle-position input variable appears in the Input variables list and the
     corresponding membership functions appear in the Input variable membership
     functions graph.
  12. Repeat steps 2 through 11 to create a vehicle-orientation input linguistic variable
      that corresponds to the Vehicle Orientation β variable of the vehicle maneuvering
     example. The following graph shows the range and membership functions for the
      variable.
          NOTE
             For the purposes of this tutorial, you can use approximate values for the
             points of the membership functions.


                                                   © National Instruments Corporation 1715

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1715 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1716 ordinal=1716 -->
## LabVIEW User Manual

LabVIEW User Manual


       Creating Output Linguistic Variables

         You create output linguistic variables similarly to how you create input linguistic variables
            in the Fuzzy System Designer. Complete the following steps to create an output linguistic
           variable that corresponds to the Steering Angle φ output linguistic variable of the vehicle
         maneuvering example.

                1.  Click the Add Output Variable button to the right of the Output variables list to
                  display the Edit Variable dialog box.
                2.  Enter steering-angle in the Name text box.
                3.  Enter a minimum value of -30 and a maximum value of 30. This range specifies
                  that the amount that the steering wheel can turn ranges from -30.0 to 30.0 degrees.
                4.  Click the Add Membership Function button to create a new membership function
                    for the steering-angle output variable.
                5.  Enter neg-large in the Name text box.
                6.  Select Triangle from the Shape pull-down menu to specify that a triangle function
                determines the degrees of membership for the linguistic variable.
                7.  Select the color you want to use for the membership function in the Membership
                functions graph from the Color picker.
                8.  Enter -30, -30, and -15 in the fields of the Points array. These points specify the
                 values of the linguistic variable corresponding to the base and top points, in order
               from left to right and base to top, of the membership function.
                9.  Repeat steps 4 through 8 to create each of the membership functions shown in the
                  following graph.


1716  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1716 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1717 ordinal=1717 -->
## LabVIEW User Manual

LabVIEW User Manual


   10. Click the OK button to save your changes.
   11. Select File»Save As to save the fuzzy system as vehicle_maneuvering.fs in
      an easily accessible location.

Creating a Rule Base with Pre-Generated Rules

Rules describe, in words, the relationships between input and output linguistic variables
based on their linguistic terms. The rule base of a fuzzy system determines the output
values of the fuzzy system based on the input values.

The vehicle-position input linguistic variable you created in step 1 has five
membershipfunctions, and the vehicle-orientation input linguistic variable has seven.
Therefore, you can construct rules to associate 35 possible combinations of the linguistic
terms of these input linguistic variables with the linguistic terms of the steering-angle
output linguistic variable you created in step 2.

      NOTE
      The table in the Complete Rule Bases topic illustrates this rule base.

Complete the following steps to create the complete rule base for the vehicle maneuvering
example. You must have created both input linguistic variables and the output linguistic
variable before creating this rule base.

   1.  Click the Rules tab of the Fuzzy System Designer to display the Rules page.
   2.  Select Operate»Pre-Generate Rules to display the Pre-Generate Rules dialog box.
   3.  Select AND (Minimum) from the Antecedent connective pull-down menu. This
      antecedent connective specifies that the smallest degree of membership of the
      antecedents determines the truth value of the aggregated rule antecedent for each
        rule.


                                                    © National Instruments Corporation 1717

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1717 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1718 ordinal=1718 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Enter a Degree of support of 1 to specify the weight that you want to apply to each
                    rule. The final rule weight for each rule is equal to the Degree of support multiplied
               by the truth value of the aggregated rule antecedent.
                5.  Select Minimum from the Consequent implication pull-down menu to specify that
                 the fuzzy logic controller truncates the output membership functions at the value of
                 the corresponding rule weights before performing defuzzification. Defuzzification is
                 the process of converting the degrees of membership of output linguistic variables
                  into numerical values.
                6.  Click the OK button to return to the Rules page. The Fuzzy System Designer
                populates the Rules list with all 35 combinations of linguistic terms of the input
                   variables. Each rule uses the same antecedent connective, degree of support, and
                  implication method that you specified in the Pre-Generate Rules dialog box.

           Notice that the consequent of each rule in the Rules list is THEN 'steering-angle' IS 'neg-
             large'. However, the linguistic term of the steering-angle output variable depends on the
          combination of linguistic terms of the input variables. Therefore, you must modify the pre-
          generated rules to use the correct consequents.

      Modifying Pre-Generated Rules

         Complete the following steps to modify the pre-generated rules to use the correct
          consequents.

                1.  Select the first rule in the Rules list to display an IF THEN diagram that shows the
               Antecedents and Consequents of the rule.
                2.  In the THEN column, select neg-small as the linguistic term for the steering-angle
                output linguistic variable. Notice the consequent of the rule in the Rules list
               changes to THEN 'steering-angle' IS 'neg-small'.
                3.  Repeat steps 1 and 2 for each rule using the consequents in the following table:


1718  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1718 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1719 ordinal=1719 -->
## LabVIEW User Manual

LabVIEW User Manual


   4.  Select File»Save to save the fuzzy system.

The fuzzy system now has a complete linguistic rule base with which to analyze input data
and produce output data. However, the rule base returns the output data as linguistic
terms. The fuzzy controller must defuzzify the output data before the output can apply to
the control structure that the fuzzy system automates. You therefore must specify a
defuzzification method for the fuzzy controller to use.

Specifying a Defuzzification Method

After you create the rule base for a fuzzy system, you must specify how a fuzzy controller
performs defuzzification for the system.

In the vehicle maneuvering example, you must supply a continuous output signal to
control the steering angle of the vehicle. Therefore, you must use a defuzzification method
that calculates the best compromise between any rules that apply at a given time.
According to the guidelines for selecting a defuzzification method the Center of Maximum
(CoM), Center of Area (CoA), and Center of Sums (CoS) defuzzification methods all fit this
requirement.

Complete the following steps to specify the defuzzification method.


                                                    © National Instruments Corporation 1719

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1719 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1720 ordinal=1720 -->
## LabVIEW User Manual

LabVIEW User Manual


                1.  On the Rules page of the Fuzzy System Designer, select the method you want to use
               from the Defuzzification method pull-down menu.
                2.  Select File»Save to save the fuzzy system.

         The fuzzy system is complete. However, before you integrate the fuzzy system into the
           control structure you want to automate, you must test the functionality of the system.

       Testing the Fuzzy System

         You can test the relationship between the input and output values of a fuzzy system to
           validate the rule base of the fuzzy system.

         Complete the following steps to test the vehicle maneuvering fuzzy system you created
           inthe previous steps.

                1.  Click the Test System tab of the Fuzzy System Designer to display the Test System
                 page.
                2.  Enter an Input value of 5 for the vehicle-position input linguistic variable. Recall
               from creating the input linguistic variables in step 1 that a value of 5 for vehicle-
                  position corresponds to the center linguistic term.
                3.  Enter an Input value of -30 for the vehicle-orientation input linguistic variable,
               which corresponds to the left-down linguistic term.
                4.  In the Invoked Rules table at the bottom of the page, notice that the fuzzy system
                 invokes rule 15: IF 'vehicle-position' IS 'center' AND 'vehicle-orientation' IS 'left-
               down' THEN 'steering-angle' IS 'neg-medium'. Recall from creating the output
                    linguistic variable in step 2 that the neg-medium linguistic term for the steering-
                 angle variable corresponds to the range between -30 and -5. If you configured the
                  fuzzy system correctly, the Output value indicator for the steering-angle displays a
                 value within that range. The fuzzy controller calculates the Output value based on
                 the weight of the rule, the consequent implication method, and the defuzzification
               method.
                5.  (Optional) Use the Input variable 1 and Input variable 2 slide controls to sweep a
                range of values for the input linguistic variables and observe the corresponding
               changes in the Input/Output relationship graph. You can use this graph to verify
                  that the rule base is reasonable and complete. For example, if the Input/Output
                 relationship graph displays 0 at some points, the rule base might be incomplete.
                6.  Fix any errors you find while testing and save the fuzzy system.
                7.  Click the Close button to exit the Fuzzy System Designer.

       Controlling the Fuzzy System

            After you create a fuzzy system in the Fuzzy System Designer, you can use the FL Fuzzy
           Controller VI to implement a controller for the fuzzy system. The FuzzyEx Car Backward
          Parking VI, located in the labview\examples\control\fuzzy\Car Parking
            directory, illustrates how to implement a controller for a fuzzy system.


1720  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1720 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1721 ordinal=1721 -->
## LabVIEW User Manual

LabVIEW User Manual


   Open example    Find related examples

This example uses the FL Load Fuzzy System VI to load both the Truck - forward.fs
and Truck - backward.fs files. These files represent the fuzzy systems for moving
the vehicle forward and backwards, respectively. Each FL Load Fuzzy System VI passes
a .fs file to a FL Fuzzy Controller VI, which implements a fuzzy controller for the fuzzy
system.

The fuzzy system you created in this tutorial is similar to the Truck - backward.fs
file. You can implement a fuzzy controller for the fuzzy system you created in the same
fashion that the FuzzyEx Car Backward Parking VI implements a controller for the Truck
- backward.fs file.
Tutorial: Modifying a Fuzzy System with the Fuzzy
Logic VIs

In the Using the Fuzzy System Designer tutorial, you design a fuzzy system interactively
using the Fuzzy System Designer and then implement a fuzzy controller for that system
using the FL Fuzzy Controller VI. You also can design a fuzzy system programmatically
using the Fuzzy Logic VIs. However, in most cases, it is easier to use the Fuzzy System
Designer to design a fuzzy system first and then use the Fuzzy Logic VIs to make
programmatic modifications to the system. In this tutorial, you modify a fuzzy system
programmatically using the Fuzzy Logic VIs.

This tutorial uses the example of a greenhouse control system to illustrate how to modify a
fuzzy system using the Fuzzy Logic VIs. The greenhouse.fs file, located in the
labview\examples\control\fuzzy\Dynamic greenhouse controller
directory, represents the fuzzy system that you modify in this chapter.

 Next 1. Observing the Fuzzy System

Observing the Fuzzy System

Before you modify a fuzzy system, you must familiarize yourself with the design of the
system. Complete the following steps to open and observe the greenhouse fuzzy system in
the Fuzzy System Designer.

   1.  Select Tools»Control Design and Simulation»Fuzzy System Designer to launch
      the Fuzzy System Designer.
   2.  Select File»Open and navigate to greenhouse.fs in the labview\examples
     \control\fuzzy\Dynamic greenhouse controller directory.
   3.  Click the OK button to open the greenhouse fuzzy system in the file dialog box. The
      Variables page displays details about the input and output variables of the fuzzy
      system.


                                                    © National Instruments Corporation 1721

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1721 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1722 ordinal=1722 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.  Observe the input and output linguistic variables. The greenhouse fuzzy system has
              two input variables, Temperature and Humidity, and two output variables, Electric
                Roof and Water Spills.
                5.  Observe the ranges and membership functions for the linguistic variables. For
                example, the Temperature input variable represents the temperature, in degrees
                   Celsius, inside the greenhouse, with a range of 0 to 50 and three membership
                  functions: Cold, Normal, and Warm. You can see on the Input variable membership
                functions graph that a trapezoid function represents the shape of the Cold
              membership function. The left base, left top, right top, and right base points of this
              membership function are 0, 0, 13, and 21, respectively.
                6.  Click the Rules tab to display the Rules page. The Rules list displays nine rules for
                 the fuzzy system, which correspond to all possible combinations of the membership
                 functions of the two input linguistic variables. Also notice that the Defuzzification
             method for the fuzzy system is Center of Area (CoA).
                7.  Select the first rule in the Rules list: IF 'Temperature' IS 'Cold' AND 'Humidity' IS
                    'Dry' THEN 'Electric Roof' IS 'Closed' ALSO 'Water Spills' IS 'Moderate'. Notice the
                   characteristics of this rule. For example, the Antecedent connective is AND
               (Minimum), the Degree of support is 1, and the Consequent implication is
                Product.
                8.  Continue exploring the fuzzy system in the Fuzzy System Designer. When you are
                   familiar with the system, you can click the Close button to exit the Fuzzy System
                 Designer.

      Loading the Fuzzy System

          Before modifying the greenhouse fuzzy system, you must load the.fs file. Complete the
           following steps to load the greenhouse.fs file.

                1.  Select File»New VI to create a new, blank VI.
                2.  Press the <Ctrl-E> keys to display the block diagram.
                3.  Add the FL Load Fuzzy System VI to the block diagram.
                4.  Right-click the file path input of the FL Load Fuzzy System VI and select
                Create»Constant from the shortcut menu.
                5.  Enter the absolute path to the greenhouse.fs file in the path constant.
                  NOTE
                      You also can use the File I/O VIs and functions to create a relative path to
                        wire to the file path input.
                6.  Select File»Save and save the VI as Modified Greenhouse Fuzzy
            System.vi in an easily accessible location.

      Modifying a Linguistic Variable

         You can use the Variables VIs to modify the linguistic variables in a fuzzy system. Complete
          the following steps to modify the range of the Temperature input linguistic variable of the
          greenhouse fuzzy system to use degrees Fahrenheit instead of degrees Celsius.


1722  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1722 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1723 ordinal=1723 -->
## LabVIEW User Manual

LabVIEW User Manual


   1.  Add the FL Set Variable VI to the block diagram. This VI modifies the name, range, or
     membership functions of a linguistic variable in a fuzzy system.
   2.  Wire the fuzzy system out output of the FL Load Fuzzy System VI to the fuzzy
      system in input of the FL Set Variable VI.
   3.  Right-click the input/output input of the FL Set Variable VI and select
      Create»Constant from the shortcut menu.
   4.  Select Input from the input/output constant to specify that you want to modify an
      input linguistic variable.
   5.  Right-click the variable index input of the FL Set Variable VI and select
      Create»Constant from the shortcut menu.
   6.  Enter 0 in the variable index constant to specify that you want to modify the first
        linguistic variable. The index is zero-based and corresponds to the order in which
      the linguistic variable was created. Recall that the Temperature variable is the first
      input linguistic variable in the fuzzy system.
   7.  Create constants for the minimum and maximum inputs of the FL Set Variable VI
     and set them to 32 and 122, respectively. This new range represents the possible
      temperature, in degrees Fahrenheit, inside the greenhouse. The block diagram now
      resembles the following image:


   8.  Save the VI.

This VI sets the new range of the Temperature variable when it runs. However, you still
must modify the membership functions of the Temperature variable to complete the
Celsius to Fahrenheit conversion.

Modifying Membership Functions

You can use the Membership VIs to modify the membership functions for linguistic
variables in a fuzzy system. Complete the following steps to modify the membership
functions of the Temperature input linguistic variable to use degrees Fahrenheit instead of
degrees Celsius.

   1.  Add the FL Set Membership Function VI to the block diagram.
   2.  Wire the fuzzy system out output of the FL Set Variable VI to the fuzzy system in
      input of the FL Set Membership Function VI.
   3.  Create constants for the membership function index, variable index, and input/
      output inputs of the FL Set Membership Function VI and set them to 0, 0, and


                                                    © National Instruments Corporation 1723

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1723 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1724 ordinal=1724 -->
## LabVIEW User Manual

LabVIEW User Manual


                 Input, respectively. These inputs specify that you want to modify the first
              membership function, Cold, of the Temperature input linguistic variable.
                4.  Create a constant for the shape input of the FL Set Membership Function VI.
                5.  Select Trapezoid from the shape constant to specify the shape of the function that
                determines the degrees of membership for the linguistic variable.
                6.  Create a constant for the points input of the FL Set Membership Function VI. This
                 input specifies the values of the linguistic variable corresponding to the base and
                top points, in order from left to right and base to top, of the membership function.
                7.  In the first four elements of the points array constant, enter the values 32, 32, 55,
              and 70, respectively.
                8.  Repeat steps 1 through 5 for the Normal and Warm membership functions. For each
              membership function, add a new FL Set Membership Function VI to the block
               diagram and wire the fuzzy system out output of the previous VI to the fuzzy
               system in input of the next VI. Use the shapes and points shown in the following
                   table:

          Membership Function                          Shape               Points

                          Gaussian                           59, 68, 77, 86

                          Trapezoid                          75, 90, 122, 122


               The block diagram now resembles the following image:


                9.  Save the VI.

      Modifying a Rule

         You can use the Rules VIs to modify the rules for a fuzzy system. This section demonstrates
        how to recreate the first rule of the greenhouse fuzzy system:


1724  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1724 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1725 ordinal=1725 -->
## LabVIEW User Manual

LabVIEW User Manual


 IF 'Temperature' IS 'Cold' AND 'Humidity' IS 'Dry' THEN 'Electric Roof' IS 'Closed' ALSO
 'Water Spills' IS 'Moderate'


and replace the existing first rule of the fuzzy system with the rule you create.

When you use the Rules VIs to create rules, you must create the rules in parts. First, you
create the antecedents. Then, you create the consequents. Finally, you combine the
antecedents and consequents for a specific rule. The next three steps of this tutorial walk
you through each of these actions.

Creating Antecedents

The first step in creating a rule is to create the antecedents of the rule. Complete the
following steps to create the 'Temperature' IS 'Cold' and 'Humidity' IS 'Dry' antecedents.

   1.  Add the FL Create Antecedent VI to the block diagram. This VI creates an
      antecedent, or IF portion, of a rule for a fuzzy system.
   2.  Create constants for the variable index and membership function index inputs of
      the FL Create Antecedent VI and set them both to 0. These inputs specify that you
      want to associate the Temperature input linguistic variable with the Cold
     membership function.
   3.  Create a constant for the condition input of the FL Create Antecedent VI.
   4.  Select = from the condition constant to calculate the degree of membership of the
        linguistic variable within the membership function. FL Create Antecedent VI now
       creates the 'Temperature' IS 'Cold' antecedent.
   5.  Repeat steps 1 through 4 to create the 'Humidity' IS 'Dry' antecedent. In the
      greenhouse fuzzy system, Dry is the first membership function of the second input
        linguistic variable, so use 1 as the variable index and 0 as the membership
      function index.
   6.  Add a Build Array function to the block diagram.
   7.  Resize the Build Array function to display two input elements.
   8.  Wire the antecedent output of the first FL Create Antecedent VI to the first element
      input of the Build Array function.
   9.  Wire the antecedent output of the second FL Create Antecedent VI to the second
      element input of the Build Array function. The section of block diagram you just
      created resembles the following image:


                                                    © National Instruments Corporation 1725

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1725 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1726 ordinal=1726 -->
## LabVIEW User Manual

LabVIEW User Manual


              10. Save the VI.

       Creating Consequents

         You create rule consequents similarly to how you create rule antecedents. Complete the
           following steps to create the 'Electric Roof' IS 'Closed' and 'Water Spills' IS 'Moderate'
          consequents.

                1.  Add the FL Create Consequent VI to the block diagram. This VI creates a consequent,
                 or THEN portion, of a rule for a fuzzy system.
                2.  Create constants for the variable index and membership function index inputs of
                 the FL Create Consequent VI and set them both to 0. These inputs specify that you
               want to associate the Electric Roof output linguistic variable with the Closed
              membership function.
                  NOTE
                         Unlike the FL Create Antecedent VI, the FL Create Consequent VI does not
                      have a condition input. The FL Create Consequent VI always returns the
                      consequent corresponding to the degree of membership of the output
                          variable within the membership function.
                3.  Repeat steps 1 and 2 to create the 'Water Spills' IS 'Moderate' consequent. In the
               greenhouse fuzzy system, Moderate is the second membership function of the
               second output linguistic variable Water Spills, so set both the variable index and
              membership function index to 1.
                4.  Add a Build Array function to the block diagram.
                5.  Resize the Build Array function to display two input elements.
                6.  Wire the consequent output of the first FL Create Consequent VI to the first
               element input of the Build Array function.
                7.  Wire the consequent output of the second FL Create Consequent VI to the second
               element input of the Build Array function. The section of block diagram you just
                 created resembles the following image:


                8.  Save the VI.

      Combining the Antecedents and Consequents for a Rule

         Complete the following steps to combine the antecedents and consequents you created in
          the previous steps to form a specific rule.


1726  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1726 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1727 ordinal=1727 -->
## LabVIEW User Manual

LabVIEW User Manual


1.  Add an FL Set Rule VI to the block diagram. This VI modifies the antecedents,
    consequents, or relationships of a rule in a fuzzy system.
2.  Wire the fuzzy system out output of the last FL Set Membership Function VI to the
    fuzzy system in input of the FL Set Rule VI.
3.  Create a constant for the rule index input of the FL Set Rule VI and set it to 0 to
    specify that you want to modify the first rule in the fuzzy system.
4.  Wire the appended array output of the first Build Array function to the antecedents
    input of the FL Set Rule VI.
5.  Wire the appended array output of the second Build Array function to the
   consequents input of the FL Set Rule VI.
6.  Create a constant for the antecedent connective input of the FL Set Rule VI to
    specify how the VI calculates the truth value of the aggregated rule antecedent.
7.  Select AND (Minimum) from the antecedent connective constant. The aggregated
    rule antecedent now is IF 'Temperature' IS 'Cold' AND 'Humidity' IS 'Dry', where this
    VI uses the smallest degree of membership of the individual antecedents to
    calculate the truth value of the aggregated rule antecedent.
        NOTE
          You cannot specify how this VI calculates the truth value of an aggregated
            rule consequent. This VI always uses the greatest degree of membership of
           the individual consequents to calculate the truth value of the aggregated
            rule consequent.
8.  Create a constant for the consequent implication input of the FL Set Rule VI. This
    input specifies the implication method this VI uses to scale the membership
    functions of the output linguistic variables based on the rule weight.
9.  Select Product from the consequent implication constant to specify that this VI
    uses the Product implication method.
10. Create a constant for the degree of support input and set it to 1. This input
    specifies the weight that you want to apply to the rule. The final rule weight is equal
    to the degree of support multiplied by the truth value of the aggregated rule
    antecedent. The section of block diagram you just created resembles the following
    image:


                                                 © National Instruments Corporation 1727

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1727 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1728 ordinal=1728 -->
## LabVIEW User Manual

LabVIEW User Manual


              11. Save the VI.

      Saving the Fuzzy System

            In previous sections of this tutorial, you modified the linguistic variables, membership
           functions, and rules of the greenhouse fuzzy system. You now can save the fuzzy system to
         a .fs file. Complete the following steps to save the modified fuzzy system to a .fs file.

                1.  Add the FL Save Fuzzy System VI to the block diagram.
                2.  Wire the fuzzy system out output of the FL Set Rule VI to the fuzzy system in input
                  of the FL Save Fuzzy System VI.
                3.  Right-click the file path input of the FL Save Fuzzy System VI and select
                Create»Constant from the shortcut menu.
                4.  Enter the absolute path to a modified greenhouse.fs file in the path
                  constant. The FL Save Fuzzy System VI creates the .fs file when it runs.
                  NOTE
                      You also can use the File I/O VIs and functions to create a relative path to
                        wire to the file path input of the FL Save Fuzzy System VI.
                5.  Save the Modified Greenhouse Fuzzy System VI.
                6.  Run the VI. The VI loads the original greenhouse.fs file, modifies the linguistic
                  variable and membership functions you specified, creates new antecedents and
                consequents for a rule, and saves all the changes to the modified
            greenhouse.fs file.

         You now can use the Fuzzy System Designer to open the modified greenhouse.fs
               file and observe the modifications you made to the greenhouse fuzzy system.


1728  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1728 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1729 ordinal=1729 -->
## LabVIEW User Manual

LabVIEW User Manual


You also can use the FL Fuzzy Controller VI to implement a fuzzy logic controller for the
modified greenhouse fuzzy system. The FuzzyEx Dynamic Fuzzy Controller for a
greenhouse example VI in the labview\examples\control\fuzzy\Dynamic
greenhouse controller directory implements a controller for the greenhouse fuzzy
system. This example VI uses the FL Load Fuzzy System VI to load the greenhouse.fs
file.

   Open example    Find related examples

You can load the modified greenhouse.fs file instead and then run the example VI
to implement a controller for the modified greenhouse fuzzy system.
Fuzzy System

Multi-Loop Control

Most of the PID VIs are polymorphic VIs for use in multiple control-loop applications. For
example, you can design a multi-loop PID control application using the PID VI and DAQ
functions for input and output. A DAQ analog input function returns an array of data when
you configureit for multiple channels. You can wire this array directly into the process
variable input of the PID VI. The polymorphic type of the PID VI automatically switches
from DBL to DBL Array, which calculates and returns an array of output values
corresponding to the number of values in the process variable array. You also can switch
the type of the polymorphic VI manually by right-clicking the VI icon and selecting Select
Type from the shortcut menu.

When the polymorphic type is DBL Array, other inputs automatically change to array inputs
as well. For example, the PID VI inputs setpoint, PID gains, and output range all become
array inputs. Each of these inputs can have an array length ranging from 1 to the array
length of the process variable input. If the array length of any of these inputs is less than
the array length of the process variable input, the PID VI reuses the last value in the array
for other calculations. For example, if you specify only one set of PID gains in the PID gains
array, the PID VI uses these gains to calculate each output value corresponding to each
process variable input value. Other polymorphic PID and Fuzzy Logic VIs operate in the
same manner.

Non-Overlapping Input Terms

The following image shows the controller I/O characteristic that results when non-
overlapping antecedent terms describe the input variable.


                                                    © National Instruments Corporation 1729

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1729 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1730 ordinal=1730 -->
## LabVIEW User Manual

LabVIEW User Manual


          Only one rule is active for each input situation that leads to the stepped controller
            characteristic.

              RELATED INFORMATION
                   I/O Characteristics of Fuzzy Controllers on page 1744
                   Specifying an Antecedent Connective on page 1756
                  Creating a Rule Base on page 1788


1730  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1730 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1731 ordinal=1731 -->
## LabVIEW User Manual

LabVIEW User Manual


Partially Overlapping Input Terms

To illustrate how the I/O characteristics of a fuzzy controller depend on design parameters
such as the rule base and membership function specifications of the fuzzy system, consider
a single-input fuzzy controller. Many of the characteristics of a single-input fuzzy controller
apply to fuzzy controllers with two or more inputs.

The following image shows the I/O characteristic of a fuzzy controller for a fuzzy system
that has only three linguistic terms for the input variable x and the output variable y. The
rule base consists of three rules, which indicate that the increasing input values cause the
output value to increase.


                                                    © National Instruments Corporation 1731

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1731 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1732 ordinal=1732 -->
## LabVIEW User Manual

LabVIEW User Manual


         The resulting controller characteristic shows nonlinear behavior. You obtain different
            intervals within the controller characteristic because the input linguistic terms partially
           overlap. The rule base has only one valid rule outside of the overlapping regions. The
          output therefore has a constant value determined by the output linguistic term of the
          output linguistic variable, which is independent of the degree of truth for that rule.

         The overlapping sections of the antecedent terms lead to the rising intervals of the
            controller characteristic. Within these parts, two rules are simultaneously active. The
            different consequent terms, weighted by the degrees of truth of the different active rules,
          determine the output value. Notice that the overlapping triangular consequent terms
          cause the rising edges of the controller characteristic to be nonlinear.


1732  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1732 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1733 ordinal=1733 -->
## LabVIEW User Manual

LabVIEW User Manual


Fuzzy Controllers

Dual-Input Fuzzy Controllers

In principle, the conclusions about I/O characteristics for single-input fuzzy controllers also
are valid for controllers with two or more inputs. However, using the AND (Minimum)
antecedent connective to combine the different input conditions raises an additional
nonlinear effect. The fuzzy controller considers the antecedent of the rule with the lowest
degree of truth as shown in the Reproducing a Given I/O Characteristic example.

The following image shows the I/O characteristic field for a dual-input fuzzy controller.


                                                    © National Instruments Corporation 1733

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1733 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1734 ordinal=1734 -->
## LabVIEW User Manual

LabVIEW User Manual


         Because the AND (Minimum) antecedent connective is nonlinear, the characteristic field is
          not exactly linear despite the membership functions that overlap entirely for both input
            variables. Non-overlapping membership functions yield a stepped characteristic field with
          constant planes, as shown in the following image.


       Fault Protection

                 If a PID VI receives an invalid input, such as NaN (Not a Number), the VI outputs NaN until
         you reinitialize the VI. However, you can use the Not A Number/Path/Refnum? function to
          check for invalid inputs and respond in a way that is appropriate to the application. The
           following block diagram uses the Not A Number/Path/Refnum? function with a Select
           function and a Feedback Node to reuse the last valid input when the VI receives an invalid
           input.


1734  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1734 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1735 ordinal=1735 -->
## LabVIEW User Manual

LabVIEW User Manual


Refer to the General PID with Fault Protection VI in the labview\examples\control
\PID directory for an example of a single-channel PID implementation that includes fault
protection.

   Open example    Find related examples

Filtering Control Inputs

You can use the PID Control Input Filter VI to filter unwanted, high-frequency noise from
measured values in a control application. For example, if you are measuring process
variable values using a DAQ device, you can use the this VI to filter noise from input values
in the control loop before passing the values to control functions such as the PID VI.

When filtering noise, set the sampling rate of the control system to at least 10 times the
fastest time constant of the physical system. This ensures that any frequency components
of the measured signal greater than 1/10 of the sampling frequency are a result of noise in
the measured signal. Gains in the PID controller can amplify this noise and produce
unnecessary wear on actuators and other system components.

The PID Control Input Filter VI uses a lowpass fifth-order finite impulse response (FIR) filter.
The cutoff frequency of the lowpass filter is 1/10 of the sampling frequency, regardless of
the actual sampling frequency value.

You can use the Filters PtByPt VIs or the LabVIEW Digital Filter Design Toolkit to perform
additional filtering tasks. Refer to the National Instruments website for more information
about or to purchase the Digital Filter Design Toolkit.

Fully Overlapping Input Terms

The following image shows the resulting controller I/O characteristic for antecedent terms
that overlap entirely. The consequent term distribution and the rule base remain
unchanged for this case.


                                                    © National Instruments Corporation 1735

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1735 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1736 ordinal=1736 -->
## LabVIEW User Manual

LabVIEW User Manual


              RELATED INFORMATION
                   I/O Characteristics of Fuzzy Controllers on page 1744
                   Specifying an Antecedent Connective on page 1756
                  Creating a Rule Base on page 1788


1736  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1736 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1737 ordinal=1737 -->
## LabVIEW User Manual

LabVIEW User Manual


Fuzzy Controllers

You can use fuzzy controllers to control fuzzy systems. Most traditional control algorithms
require a mathematical model of the system you want to control. However, many physical
systems are difficult or impossible to model mathematically. In addition, many processes
are either nonlinear or too complex for you to control with traditional strategies. However,
if you can describe a control strategy qualitatively, you can use fuzzy logic to create a fuzzy
controller that emulates a heuristic rule-of-thumb strategy.

The following image illustrates the process of a fuzzy controller.


Fuzzification

Fuzzification is the process of associating crisp, or numerical, input values with the
linguistic terms of the corresponding input linguistic variables.

For example, a fuzzy controller might associate the temperature reading from a
thermometer with the linguistic terms cold, moderate, and hot for the current temperature
linguistic variable. Depending on the membership functions for the linguistic terms, the
temperature value might correspond to one or more of the linguistic terms.


Implementing a Linguistic Control Strategy

After a fuzzy controller fuzzifies the input values of a fuzzy system, the fuzzy controller uses
the corresponding input linguistic terms and the rule base to determine the resulting
linguistic terms of the output linguistic variables.

For example, suppose the current temperature of a room is 50 degrees, which corresponds
to a linguistic term of cold with a degree of membership of 0.4. Also suppose the desired
temperature is 70, which corresponds to a linguistic term of moderate with a degree of
membership of 0.8. The fuzzy controller invokes the following rule of the fuzzy system: IF
current temperature is cold AND desired temperature is moderate, THEN heater setting is
low.

Notice that this rule consists of two antecedents, " current temperature is cold " and "
desired temperature is moderate ". The truth value of each antecedent is equal to the
degree of membership of the linguistic variable within the corresponding linguistic term.
The fuzzy logic controller uses an antecedent connective to determine how to calculate the


                                                    © National Instruments Corporation 1737

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1737 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1738 ordinal=1738 -->
## LabVIEW User Manual

LabVIEW User Manual


           truth value of the aggregated rule antecedent. Suppose the invoked rule in this example
          uses the AND (Minimum) antecedent connective, which specifies to use the smallest degree
           of membership of the antecedents as the truth value of the aggregated rule antecedent.
           Therefore, the truth value of the aggregated rule antecedent is 0.4.

         You can specify a degree of support for each rule of a fuzzy system. The weight of a rule is
          equal to the degree of support multiplied by the truth value of the aggregated rule
          antecedent. The fuzzy controller uses an implication method to scale the membership
           functions of an output linguistic variable based on the rule weight before performing
            defuzzification.


           Defuzzification

           Defuzzification is the process of converting the degrees of membership of output linguistic
           variables within their linguistic terms into crisp numerical values. A fuzzy controller can use
         one of several mathematical methods to perform defuzzification. The most accurate
            defuzzification method for a fuzzy controller varies based on the control application.


          Related Information

           I/O Characteristics of Fuzzy Controllers

          Fuzzy Controllers in Closed-Loop Control Structures

      Fuzzy Controllers in Closed-Loop Control Structures

         The most common use case for fuzzy controllers is in closed-loop control structures. The
         most basic structure of closed-loop control applications uses sensor signals as input
           signals for the system and the outputs as command values to drive the actuators of the
           process. The following image shows a simple closed-loop control structure with a fuzzy
            controller.


1738  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1738 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1739 ordinal=1739 -->
## LabVIEW User Manual

LabVIEW User Manual


Pure fuzzy control applications are more the exception than the rule. In most cases the
fuzzy controller outputs serve as reference parameters, such as gains, that you provide to a
conventional controller instead of directly to driving actuators.

Because you can regard a fuzzy controller as a nonlinear characteristic field controller, it
has no internal dynamic aspects. Thus, you must implement any dynamic property by an
appropriate preprocessing of the measured input data.

PID and Fuzzy Logic VIs enable you to integrate fuzzy controllers and PID control. For
example, you can use fuzzy controllers with conventional PID controllers or create hybrid
fuzzy-PI controllers. Use either the Fuzzy System Designer or the Fuzzy Logic VIs to design a
fuzzy system. Then use the FL Fuzzy Controller VI to implement a fuzzy controller for the
fuzzy system. Finally, you can integrate the fuzzy controller into a control structure you
create using the PID VIs.

      RELATED INFORMATION
       PID Control on page 1747
       Using Fuzzy Controllers with PID Controllers on page 1760
        Fuzzy-PI Controllers on page 1741
        Fuzzy-PI Controllers on page 1741
       Using Fuzzy Controllers with PID Controllers on page 1760

Fuzzy Logic

Fuzzy logic is a method of rule-based decision making used for expert systems and process
control. Fuzzy logic differs from traditional Boolean logic in that fuzzy logic allows for
partial membership in a set.

Traditional Boolean logic is two-valued in the sense that a member either belongs to a set
or does not. Values of one and zero represent the membership of a member to the set with
one representing absolute membership and zero representing no membership. Fuzzy logic
allows for partial membership, or a degree of membership, which might be any value along
the continuum of zero to one.

You can think of fuzzy logic in terms of fuzzy systems, which are systems of variables
associated with fuzzy logic, and fuzzy controllers, which use defined rules to control a fuzzy
system based on the current values of input variables. You can use the Fuzzy Logic VIs to
design and control fuzzy systems. You also can use the Fuzzy System Designer to design
fuzzy systems interactively.


Related Information

Fuzzy Systems

Fuzzy Controllers

Tutorial: Using the Fuzzy System Designer


                                                    © National Instruments Corporation 1739

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1739 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1740 ordinal=1740 -->
## LabVIEW User Manual

LabVIEW User Manual


            Tutorial: Modifying a Fuzzy System with the Fuzzy Logic VIs

              RELATED INFORMATION
                 Fuzzy Systems on page 1740
                 Fuzzy Controllers on page 1737
                 Fuzzy Systems on page 1740
                 Fuzzy Controllers on page 1737

      Fuzzy System Design Overview

         The topics in this section use an example fuzzy system that automates a vehicle to park
              itself to illustrate the basics of fuzzy system design.

             NOTE
               The topics in this section describe the general process of designing a fuzzy system.
                You also can refer to the tutorials Using the Fuzzy System Designer and Modifying a
                 Fuzzy System with the Fuzzy Logic VIs for examples with step-by-step instructions
                   of how to design a fuzzy system with the PID and Fuzzy Logic VIs.

         A fuzzy system consists of three main parts: linguistic variables, membership functions,
         and rules. Therefore, fuzzy system design is a three-step process:

                1.  Creating Linguistic Variables
                2.  Creating Membership Functions
                3.  Creating a Rule Base

      Fuzzy Systems

         A fuzzy system is a system of variables that are associated using fuzzy logic. A fuzzy
            controller uses defined rules to control a fuzzy system based on the current values of input
            variables. You can use the Fuzzy System Designer and the Fuzzy Logic VIs to design and
           control fuzzy systems.

          Fuzzy systems consist of three main parts: linguistic variables, membership functions, and
            rules.


           Linguistic Variables

            Linguistic variables represent, in words, the input variables and output variables of the
          system you want to control. For a heater, you might have two input linguistic variables,
           current temperature and desired temperature, and one output linguistic variable, heater
            setting. Each linguistic variable has a range of expected values. For example, the range of
           current temperature might be 0 to 100 degrees. The range of desired temperature might be
          50 to 80 degrees.


1740  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1740 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1741 ordinal=1741 -->
## LabVIEW User Manual

LabVIEW User Manual


A fuzzy controller requires at least one input linguistic variable and one output linguistic
variable.


Linguistic Terms and Membership Functions

Linguistic terms represent, in words, categories for the values of a linguistic variable. The
linguistic variables current temperature and desired temperature each might include the
linguistic terms cold, moderate, and hot. The linguistic variable heater setting might
include the linguistic terms off, low, and high.

Membership functions are numerical functions corresponding to linguistic terms. A
membership function represents the degree of membership of linguistic variables within
their linguistic terms. The degree of membership is continuous between 0 and 1, where 0 is
equal to 0% membership and 1 is equal to 100% membership. For example, the linguistic
variable current temperature might have full membership (1) within the linguistic term hot
at 100 degrees, no membership (0) within that term at 70 degrees or less, and partial
membership at all temperatures between 70 and 100 degrees.


Rules

Rules describe, in words, the relationships between input and output linguistic variables
based on their linguistic terms. For example, you might define the following rule:

 IF current temperature is cold AND desired temperature is moderate, THEN heater setting
 is low.


The clauses " current temperature is cold " and " desired temperature is moderate " are the
antecedents of this rule. The AND connective specifies how the fuzzy logic controller
relates the two antecedents to determine the truth value for the aggregated rule
antecedent. The clause " heater setting is low " is the consequent of this rule.

A rule base is the set of rules for a fuzzy system. The rule base is equivalent to the control
strategy of the controller.


Related Information

Fuzzy System Design Overview

Defuzzification Methods

Fuzzy-PI Controllers

A PI controller is a controller that produces proportional plus integral control action. The PI
controller has only one input and one output. The output value increases when the input
value increases.


                                                    © National Instruments Corporation 1741

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1741 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1742 ordinal=1742 -->
## LabVIEW User Manual

LabVIEW User Manual


         A fuzzy-PI controller is a generalization of the conventional PI controller that uses an error
           signal and its derivative as input signals. Fuzzy-PI controllers have two inputs and one
           output. Multiple inputs allow for greater control diversity for a fuzzy-PI controller over a
          conventional PI controller.

         The fuzzy-PI controller shown in the following image uses the error signal e t and its
           derivative de t/ dt from the measured data preprocessing step as inputs. If the output
           signal describes the necessary difference toward the current output value, you need a
          subsequent integrator device to build up the command variable value.


         Advantages of Fuzzy-PI Controllers

         The benefit of the fuzzy-PI controller is that it does not have a special operating point. The
           rules evaluate the difference between the measured value and the set value, which is the
           error signal. The rules also evaluate the tendency of the error signal to determine whether
           to increase or decrease the control variable. The absolute value of the command variable
          has no influence.

          Another advantage of a fuzzy-PI controller over a conventional PI controller is that it can
         implement nonlinear control strategies and that it uses linguistic rules. With fuzzy-PI
            controllers, you can consider the error tendency by itself when the error becomes small.

      Gain Scheduling

          Gain scheduling refers to a system where you change controller parameters based on
         measured operating conditions. For example, the scheduling variable can be the setpoint,
          the process variable, a controller output, or an external signal. For historical reasons, the
         term gain scheduling is used even if other parameters such as derivative time, Td, or
            integral time, Ti change. Gain scheduling effectively controls a system whose dynamics
         change with the operating conditions.

         You can use the PID Gain Schedule VI, to apply different sets of PID parameters for different
           regions of operation of your controller. Because most processes are nonlinear, PID


1742  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1742 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1743 ordinal=1743 -->
## LabVIEW User Manual

LabVIEW User Manual


parameters that produce a desired response at one operating point might not produce a
satisfactory response at another operating point. The PID Gain Schedule VI selects and
outputs one set of PID gains from a gain schedule based on the current value of its gain
scheduling value input. For example, to implement a gain schedule based on the value of
the process variable, wire the process variable value to the gain scheduling value input
and wire the PID gains out output to the PID gains input of the PID VI.

The PID gain schedule input of the PID Gain Schedule VI is an array of clusters of PID gains
and corresponding maximum values. Each set of PID gains corresponds to the range of
input values from the max value of the previous element of the array to the max value of
the same element of the array. The input range of the PID gains of the first element of PID
gain schedule is all values less than or equal to the corresponding max value.

The following front panel shows a VI that uses the setpoint value as the gain scheduling
variable with a default range of 0 to 100.


The following table summarizes parameter ranges specified in the previous image:

 Range                                        Parameters

 0 SP  30                                  Kc = 10 Ti = 0.02 Td = 0.02
 30 SP  70                                 Kc = 12 Ti = 0.02 Td = 0.01


                                                    © National Instruments Corporation 1743

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1743 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1744 ordinal=1744 -->
## LabVIEW User Manual

LabVIEW User Manual


          Range                                        Parameters

          70 SP  100                               Kc = 15 Ti = 0.02 Td = 0.005

       I/O Characteristics of Fuzzy Controllers

         You can consider a fuzzy controller to be a nonlinear characteristic field controller. The rule
          base and membership functions of the fuzzy system determine the behavior of the
            controller. Because the controller has no internal dynamic aspects, the I/O characteristics
         can describe the transient response of the controller completely.

           This section includes examples that show the I/O characteristics of a fuzzy controller under
           various of conditions. Select an item from the list for information about I/O characteristics
           of a fuzzy controller with the described conditions.

                   •    Partially Overlapping Input Terms
                   •    Fully Overlapping Input Terms
                   •   Non-Overlapping Input Terms
                   •   Undefined Input Term Intervals
                   •   Singletons as Output Terms with Fully Overlapping Input Terms
                   •   Different Overlapping Degrees of Membership Functions for Output Terms
                   •   Wide and Small Membership Functions for the Output Terms
                   •   Using the Mean of Maximum (MoM) Defuzzification Method
                   •   Reproducing a Given I/O Characteristic
                   •   Dual-Input Fuzzy Controllers


1744  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1744 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1745 ordinal=1745 -->
## LabVIEW User Manual

LabVIEW User Manual


These examples show that you can use a fuzzy controller to perform arbitrary I/O
operations. The number of input and output linguistic terms depends on the desired
characteristic type and the precision to which you approximate the given I/O characteristic.

      RELATED INFORMATION
       Fuzzy Controllers on page 1737
       Creating a Rule Base on page 1788
       Creating Membership Functions on page 1791
        Partially Overlapping Input Terms on page 1731
        Fully Overlapping Input Terms on page 1735
       Non-Overlapping Input Terms on page 1729
       Undefined Input Term Intervals on page 1758
        Singletons as Output Terms with Fully Overlapping Input Terms on page 1753
        Different Overlapping Degrees of Membership Functions for Output Terms on page
       1802
       Wide and Small Membership Functions for Output Terms on page 1809
       Using the Mean of Maximum (MoM) Defuzzification Method on page 1806
       Reproducing a Given I/O Characteristic on page 1775
       Dual-Input Fuzzy Controllers on page 1733

PID Algorithms

The following equations describe the basic PID algorithm. This section also provides
information about how the PID VIs implement this algorithm, as well as the advanced PID
algorithm.


Basic PID Controller

The following simulation diagram represents the basic PID (Proportional-Integral-
Derivative) controller:


                                                    © National Instruments Corporation 1745

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1745 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1746 ordinal=1746 -->
## LabVIEW User Manual

LabVIEW User Manual


             NOTE
                  Constructing a simulation diagram like the one in the previous image requires the
                LabVIEW Control Design and Simulation Module. However, the PID VIs implement
                 PID controllers for you. You do not need the Control Design and Simulation Module
                   to build PID controllers. Refer to the National Instruments website at ni.com for
               more information about the Control Design and Simulation Module.


          Error Calculation (e)

         A PID controller compares the setpoint SP to the process variable PV to obtain the error e,
          as follows:


          where                                                    e is the error

         SP is the setpoint

          PV is the process variable


          Controller Action (u(t))

         The PID controller calculates the controller action, u(t) as follows:


          where                                                        Kc is controller gain
              Ti is the integral time in minutes, also called the reset time
           Td is the derivative time in minutes, also called the rate time


1746  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1746 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1747 ordinal=1747 -->
## LabVIEW User Manual

LabVIEW User Manual


This equation involves three actions that simultaneously apply to the output of the
controller:


Proportional Action (P)

Proportional action P is proportional to the error e. This term defines how quickly the
controller must respond to changes in the error. The following formula represents the
proportional action:


Integral Action (I)

Integral action I is proportional to the integral of the error e. This term is generally used to
correct steady-state error and to avoid disturbances in the system. The following formula
represents the integral action:


Derivative Action (D)

Derivative action D is proportional to the derivative of the error e. This term works as a
brake to the response, avoiding the system to overshoot. The following formula represents
the derivative action:


Related Information

PID Topologies

Implementing the PID Algorithm with the PID VIs

Advanced PID Algorithm
PID Control

Proportional-Integral-Derivative (PID) controllers are common feedback controllers. In PID
control, you specify a process variable and a setpoint. The process variable is the system
parameter you want to control, such as temperature, pressure, or flow rate, and the
setpoint is the desired value for that system parameter. A PID controller determines a
controller output value, for example the heater power or valve position, and applies the


                                                    © National Instruments Corporation 1747

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1747 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1748 ordinal=1748 -->
## LabVIEW User Manual

LabVIEW User Manual


            controller output value to the system to drive the process variable toward the setpoint
           value.

         Use the PID VIs to develop the following control applications based on PID controllers:

                   •   Proportional (P); proportional-integral (PI); proportional-derivative (PD); and
                  proportional-integral-derivative (PID) algorithms
                   •   Gain-scheduled PID
                   •   PID autotuning
                   •   Error-squared PID
                   •   Lead-Lag compensation
                   •   Setpoint profile generation
                   •   Multi-loop cascade control
                   •   Feedforward control

              RELATED INFORMATION
                Implementing the PID Algorithm with the PID VIs on page 1764
                 Gain Scheduling on page 1742
                 Autotuning PID Controllers (PID and Fuzzy Logic) on page 1774
                Advanced PID Algorithm on page 1770
                 Lead/Lag on page 1768
                  Setpoint Profile Generation on page 1752
                  Multi-Loop Control on page 1729
                 Lead/Lag on page 1768
                 PID Algorithms on page 1745
                 Designing a Control Strategy on page 1799
                Implementing PID Controllers with the PID VIs on page 1763
                 Autotuning PID Controllers (PID and Fuzzy Logic) on page 1774

      PID Relay Autotuning Technique

         The PID Relay autotuning technique, which is used by the Autotuning Wizard and the PID
          Relay instance of the PID Online Autotuning VI, uses the setpoint relay experiment to
          determining the information needed to tune the controller.

         The following image illustrates the autotuning procedure excited by the setpoint relay
          experiment, which connects a relay and an extra feedback signal with the setpoint. The
           setpoint relay steps the setpoint up or down, exciting the autotuning procedure and
           allowing the controller to respond to the change and tune the system for an acceptable
          response. The PID Autotuning VI and the PID Relay instance of the PID Online Autotuning


1748  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1748 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1749 ordinal=1749 -->
## LabVIEW User Manual

LabVIEW User Manual


polymorphic VI directly implement this process. The existing controller remains in the
loop.


For most systems, the nonlinear relay characteristic generates a limiting cycle, from which
the autotuning algorithm identifies the relevant information needed for PID tuning. If the
existing controller is proportional only, the autotuning algorithm identifies the ultimate
gain Ku and ultimate period Tu. If the existing model is PI or PID, the autotuning algorithm
identifies the dead time and time constant TP, which are two parameters in the integral-
plus-deadtime model.


PID Topologies

Standard PID literature provides several ways to define a PID controller. In general, PID
controllers are classified using the following forms.


Academic Form

In the Academic form, the proportional parameter P actuates on the integral I and
derivative D terms, as represented by the following equation:


The algorithms implemented by the PID VIs are based on the Academic form with time
expressed in minutes.


Parallel Form

In the Parallel form, the three parameters P, I, and D are independent of each other and
control each interaction. This form also is referred to as non-interacting PID. The Parallel
form is represented by the following equation:


                                                    © National Instruments Corporation 1749

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1749 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1750 ordinal=1750 -->
## LabVIEW User Manual

LabVIEW User Manual


          Series Form

            In the Series form, the parameters are coupled and in series with each component, as
          represented by the following equation:


          Converting Topologies

         You can use the PID Structure Conversion VI to convert a PID controller from one topology,
           or form, to another.

      Programmatically Autotuning a Previously
     Implemented PID Controller

         You can use the PID Online Autotuning VI to tune a controller you implement or previously
         implemented with the PID Advanced VI.

             NOTE
                You must use the PID Advanced VI to implement the controller. You can implement
                 PID controllers with various PID VIs, but PID Advanced is the only VI that supports
                   putting the controller under manual control, which is necessary for using the PID
                  Online Autotuning VI. You also can use the PID Advanced Autotuning VI to
                implement and autotune a PID controller from a single VI.

         Complete the following steps autotune a previously implemented PID controller.

                1.   If you have not already done so, implement a PID controller using the PID Advanced
                      VI.
                2.  Put the controller in manual mode by setting the auto? input of the PID Advanced VI
                  to FALSE.
                3.  Add the PID Online Autotuning VI to the block diagram within the control loop but to
                 the left of the PID Advanced VI.
                4.  Manually select the polymorphic instance of the PID Online Autotuning VI.
                5.  Without deleting the controls, constants, or shift registers that contain the values,
                 delete the wires to the setpoint, process variable, and PID gains inputs of the PID
               Advanced VI.
                6.  Wire the values to the Setpoint in, Process Variable, and PID gains in inputs of the
                PID Online Autotuning VI.
                7.  Create a Boolean control with latched mechanical action and a default value of
                FALSE, and wire the control to the Autotune? input of the PID Online Autotuning VI.
                8.  Wire the setpoint out, Process Variable Out, and PID gains out outputs of the PID
                 Online Autotuning VI to the setpoint, process variable, and PID gains inputs of the
                PID Advanced VI.


1750  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1750 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1751 ordinal=1751 -->
## LabVIEW User Manual

LabVIEW User Manual


   9.  (Optional) If you are specifying a value for the dt (s) input, wire the same value to
      both VIs.
   10. Run the VI.
   11. Set Autotune? to TRUE to begin autotuning.

Refer to the Autotuning PID Online and Inline VI in the labview\examples\control
\PID for an example of implementing autotuning with the PID Online Autotuning VI and
the PID Advanced VI.

   Open example    Find related examples
Programmatically Implementing and Autotuning a
PID Controller

You can use the PID Advanced Autotuning VI both to implement and autotune a PID
controller.

      NOTE
      The PID Advanced Autotuning VI incorporates the functionality of the PID
       Advanced VI and the PID Online Autotuning VI. You also can use the PID Online
       Autotuning VI to programmatically autotune a previously implemented PID
         controller.

Complete the following steps to implement a tuned PID controller with the PID Advanced
Autotuning VI.

   1.  Add the PID Advanced Autotuning VI to the block diagram within a control loop.
   2.  Wire the inputs you want to use to implement the controller. Minimally, wire the
       setpoint, process variable, and PID gains inputs.
   3.  Create a control for the autotuning parameters input and select the controller
      type and control specification you want to use.
   4.  Set the technique component of the autotuning parameters input to the
      autotuning technique you want to use.
   5.  Create a Boolean control with latched mechanical action and a default value of
      FALSE for the Autotune? input.
   6.  Run the VI.
   7.  Set Autotune? to TRUE to begin autotuning.

Refer to the Autotuning PID Online VI in the labview\examples\control\PID for an
example of implementing autotuning with the PID Advanced Autotuning VI.

   Open example    Find related examples


                                                    © National Instruments Corporation 1751

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1751 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1752 ordinal=1752 -->
## LabVIEW User Manual

LabVIEW User Manual


      Setpoint Profile Generation

         You can use the PID Setpoint Profile VI inside a control loop to generate a profile of setpoint
           values over time for a ramp and soak type PID application. For example, you might want to
         ramp the setpoint temperature of an oven control system over time, and then hold, or
           soak, the setpoint at a certain temperature for another period of time. You can use the PID
           Setpoint Profile VI to implement any arbitrary combination of ramp, hold, and step
           functions.

           Specify the setpoint profile as an array of pairs of time and setpoint values with the time
           values in ascending order.


       Ramp Setpoint Profile

         You can specify a ramp setpoint profile with two setpoint profile array values, as shown in
          the following image.


       Ramp and Hold Setpoint Profile

         A ramp and hold setpoint profile also can have two successive array values with the same
           setpoint value, as shown in the following image.


1752  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1752 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1753 ordinal=1753 -->
## LabVIEW User Manual

LabVIEW User Manual


Step Setpoint Profile

A step setpoint profile can have two successive array values with the same time value but
different setpoint values, as shown in the following image.


The PID Setpoint Profile VI returns a single setpoint value determined from the current
elapsed time. The first call to the VI initializes the current time in the setpoint profile to 0.
On subsequent calls, the VI determines the current time from the previous time and the dt
input value. If you reinitialize the current time to 0 by passing a value of TRUE to the
reinitialize? input, you can repeat the specified setpoint profile.
Singletons as Output Terms with Fully Overlapping
Input Terms

The simplest way to obtain a linear controller characteristic is to use singletons as
consequent terms with entirely overlapping input terms. Singletons are normalized
rectangular membership functions with an infinitely small width. Using singleton
membership functions for consequent terms makes the Center of Area (CoA)


                                                    © National Instruments Corporation 1753

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1753 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1754 ordinal=1754 -->
## LabVIEW User Manual

LabVIEW User Manual


            defuzzification method identical to the Center of Maximum (CoM) method. The following
         image shows the controller for the CoA method using singleton membership functions.


         The controller characteristic remains relatively unchanged when you leave the input terms
            entirely overlapped to vary the overlapping degree of the membership functions for the
          consequent terms, especially if all the consequent terms are equal in width. Then only the
            typical values of the consequent terms are significant.

           Therefore, in most closed-loop control applications, you can use singleton membership
           functions to model the output terms sufficiently rather than using triangular or other
         membership function types.


1754  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1754 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1755 ordinal=1755 -->
## LabVIEW User Manual

LabVIEW User Manual


Specifying a Consequent Implication Method

A fuzzy controller uses a consequent implication method to scale the membership
functions of each output linguistic variable based on the corresponding rule weight before
performing defuzzification.

With PID and Fuzzy Logic VIs, you can use either the Minimum or Product consequent
implication method.


Minimum Consequent Implication Method

In the Minimum implication method, the fuzzy logic controller truncates the output
membership functions at the value of the corresponding rule weights. For example, if an
output linguistic variable has three membership functions with rule weights 0.5, 0.8, and
0.3, respectively, the scaled membership functions might appear similar to the following
image.


Product Consequent Implication Method

In the Product implication method, the fuzzy logic controller scales the output
membership functions at the value of the corresponding rule weights. For example, if an
output linguistic variable has three membership functions with rule weights 0.5, 0.8, and
0.3, respectively, the scaled membership functions might appear similar to the following
image.


                                                    © National Instruments Corporation 1755

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1755 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1756 ordinal=1756 -->
## LabVIEW User Manual

LabVIEW User Manual


      Specifying an Antecedent Connective

        When creating a rule base, if a rule has more than one antecedent, you must specify an
          antecedent connective to determine how to calculate the truth value of the aggregated
            rule antecedent.

         Because linguistic variables can have partial degrees of membership within linguistic
           terms, you cannot use Boolean operators from conventional dual logic as antecedent
           connectives. PID and Fuzzy Logic VIs use the following antecedent connectives instead.


        AND (Minimum)

        μ A * B = min (μ A, μ B


        AND (Product)

        μ A * B = (μ A, μ B


       OR (Maximum)

        μ A + B = max (μ A, μ B


       OR (Probabilistic)

         A + B = (A + B - AB)


1756  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1756 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1757 ordinal=1757 -->
## LabVIEW User Manual

LabVIEW User Manual


Notice that these definitions agree with the logical operators used in Boolean logic. A truth
table uses conventional operators to yield equivalent results.

The AND (Minimum) antecedent connective specifies to use the smallest degree of
membership of the antecedents as the truth value of the aggregated rule antecedent, while
the AND (Product) specifies to use the product of the degrees of membership of the
antecedents. The OR (Maximum) antecedent connective specifies to use the largest degree
of membership of the antecedents. The OR (Probabilistic) antecedent connective specifies
to use the probabilistic sum of the degrees of membership of the antecedents.


Antecedent Connectives for a Vehicle Maneuvering Fuzzy System

Assume the following rules are invoked for the input values of a vehicle maneuvering fuzzy
system.

                         IF Vehicle Position x is                  Vehicle Orientation β is Left                                    AND (1)                   Center (degree of              Up (degree of membership                                        (Minimum)                   membership = 0.8)                        = 1.0) = 0.8

 THEN Steering
 Angle φ is
 Negative Small

                         IF Vehicle Position x is                  Vehicle Orientation β is Left                                    AND (2)                 Right Center (degree of            Up (degree of membership                                        (Minimum)                   membership = 0.1)                        = 1.0) = 0.1

 THEN Steering
 Angle φ is
 Negative Medium


Notice that each rule uses the AND (Minimum) antecedent connective. In Rule 1, Vehicle
Position x has a degree of membership of 0.8 within the linguistic term Center and Vehicle
Orientation β has a degree of membership of 1.0 within the linguistic term Left Up. Because
the antecedent connective is AND (Minimum), the fuzzy controller for this fuzzy system
uses the smallest degree of membership of the antecedents, or 0.8, as the truth value of
the aggregated rule antecedent. Similarly, the smallest degree of membership of the
antecedents in Rule 2 is 0.1. Therefore, the fuzzy controller uses 0.1 as the truth value of the
aggregated rule antecedent. The truth value of the aggregated rule antecedent is
equivalent to the degree of truth of the rule.

If these two rules are the only rules invoked for a given set of input values, the other
linguistic terms for the Steering Angle φ output linguistic variable have a truth value of 0.
The following list describes the final truth values for each of the linguistic terms.

 Negative Large Negative
 Medium Negative Small     to a degree of to a degree of to a degree of to a   0.0 0.1 0.8
 Zero Positive Small          degree of to a degree of to a degree of to a     0.0 0.0 0.0
 Positive Medium Positive                   degree of                         0.0
 Large


                                                    © National Instruments Corporation 1757

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1757 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1758 ordinal=1758 -->
## LabVIEW User Manual

LabVIEW User Manual


                 If a rule has more than one consequent, the fuzzy logic controller must evaluate the
          aggregated rule consequent. When you implement a fuzzy controller with PID and Fuzzy
           Logic VIs, the fuzzy controller always considers only the consequent that has the largest
          degree of membership.
     Undefined Input Term Intervals

                 If the rule base has undefined intervals within input and output linguistic terms, or if the
            rule base is incomplete, you must specify the output of the fuzzy controller. If no rule is
           available for a certain situation, the output value remains undefined. One way to avoid this
         problem is to leave the current output value unchanged until the controller encounters a
           situation that is covered by the rules. The following image shows the resulting effect on the
            controller characteristic.


1758  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1758 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1759 ordinal=1759 -->
## LabVIEW User Manual

LabVIEW User Manual


If you use an old output value as a default value, undefined intervals or incomplete rule
bases can lead to hysteretic effects on the controller characteristic.

You can use non-overlapping, rectangular-shaped consequent terms to obtain an exact
linear controller characteristic for a single-input controller. In this case, both the area and
momentum vary linearly with the degree of truth, and overlapping regions of the output
linguistic terms do not cause any distortion.


                                                    © National Instruments Corporation 1759

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1759 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1760 ordinal=1760 -->
## LabVIEW User Manual

LabVIEW User Manual


      Using Fuzzy Controllers with PID Controllers

         The chemical industries and process technologies often use fuzzy controllers with
          underlying PID control loops. The fuzzy controllers these industries use are PID fuzzy
            controllers that control single-process parameters. Usually, people supervise the operating
           point of the entire process.

         The following image shows the controller structure of the fuzzy controller with underlying
          PID control loops.


          For automatic operation of such multi-variable control problems, you must build a model-
         based controller. However, for most applications, either the process is too complex to
         model adequately, or the mathematical modeling task requires too much time.


          Using a Fuzzy Controller to Tune PID Controller Parameters

         The following image shows how to use a fuzzy controller to tune the parameters of a
          conventional PID controller automatically. This fuzzy controller constantly interprets the
          process reaction and calculates the optimal P, I, and D gains. You can apply this control
           structure to processes that change their characteristics over time.


1760  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1760 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1761 ordinal=1761 -->
## LabVIEW User Manual

LabVIEW User Manual


Using a Fuzzy Controller to Correct PID Controller Output

In the following image, both the fuzzy controller and the PID controller work in parallel.
The process adds the output signals from both controllers, but the output signal from the
fuzzy controller is zero under normal operating conditions. The PID controller output leads
the process. The fuzzy controller intervenes only when it detects abnormal operating
conditions, such as strong disturbances.


                                                    © National Instruments Corporation 1761

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1761 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1762 ordinal=1762 -->
## LabVIEW User Manual

LabVIEW User Manual


     PID Autotuning
     Implementing Autotuning with the Autotuning
      Wizard

         To use the Autotuning Wizard to improve your controller performance, you must first create
          your control application and determine PID parameters that produce stable control of the
          system. You can develop the control application using either the PID VI, the PID Gain
          Schedule VI, or the PID Autotuning VI. Because the PID Autotuning VI has inputs and
          outputs consistent with the other PID VIs, you can replace many PID VIs with it.

             NOTE
               The PID Autotuning VI cannot directly replace the PID Advanced VI or the more
                advanced autotuning VIs, such as PID Advanced Autotuning or PID Online
                  Autotuning. These VIs provide advanced functionality that the PID Autotuning VI
                does not support.


          Autotuning-Specific Inputs

         The PID Autotuning VI has several inputs and outputs specific to the autotuning procedure,
           including the following inputs:

                   •   autotuning parameters —A cluster of parameters that the PID Autotuning VI uses
                    for the autotuning process. The Autotuning Wizard allows you to specify all of these
                parameters manually, so wiring this input is optional.
                   •   autotune? —Specifies whether to invoke the Autotuning Wizard and begin
                 autotuning. Wire a Boolean control, such as a button, tothis input so a user can
                 press the button to open the Autotuning Wizard. The Autotuning Wizard steps the
                 user through the autotuning process.
                  NOTE
                         Set the Boolean control mechanical action to Latch When Released so the
                        Autotuning Wizard does not open repeatedly when the user presses the
                         button.


          Autotuning-Specific Outputs

         The following outputs are specific to the autotuning procedure:

                   •   tuning completed? —Indicates when the autotuning process is complete. You can
                use this output to determine when to update the PID gains values.
                   •   PID gains out —Returns the tuned PID gains. Before autotuning completes, PID
                gains out returns the same values as the PID gains input. PID gains out updates
                 only when autotuning completes and tuning completed? returns TRUE.


1762  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1762 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1763 ordinal=1763 -->
## LabVIEW User Manual

LabVIEW User Manual


Implementing PID Controllers with the PID VIs

The PID VIs are all variations of the basic PID VI, and each variation provides additional
functionality as described in the following table. You can use these VIs interchangeably
because they use consistent inputs and outputs where possible. Refer to the help topic for
the VI you want to use for specific information about the VI.

 Use Case                                                                VI Name

     •   Simple systems, or when an efficient algorithm is
        required.                                                  PID VI
     •   Implements the basic PID algorithm

     •   Complex systems that require options for manual or
       automatic operation, setpoint weighting, filtering of
        derivative action, and so on.
                                                            PID Advanced VI
     •   Implements the advanced PID algorithm and provides
        extra input parameters to expand on the functionality
        of the PID VI.

 Complex systems that require the same advanced options as   PID Advanced Autotuning
 the PID Advanced VI and the ability to autotune parameters.                 VI

                                                            PID Autotuning Systems that contain significant dead time.                                                              (Temperature) VI

 Systems that require lead/lag function.                          PID Lead-Lag VI


      RELATED INFORMATION
       Implementing the PID Algorithm with the PID VIs on page 1764
       Advanced PID Algorithm on page 1770
       Autotuning PID Controllers (PID and Fuzzy Logic) on page 1774
       Lead/Lag on page 1768
        Fault Protection on page 1734
        Multi-Loop Control on page 1729
        Setpoint Profile Generation on page 1752
       Gain Scheduling on page 1742
        Control Output Rate Limiting on page 1788
       Lead/Lag on page 1768
       Converting Between Percentage of Full Scale and Engineering Units on page 1788
         Filtering Control Inputs on page 1735


                                                    © National Instruments Corporation 1763

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1763 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1764 ordinal=1764 -->
## LabVIEW User Manual

LabVIEW User Manual


     Implementing the PID Algorithm with the PID VIs

           This following sections describe how the basic PID VIs (not including PID Advanced, PID
         Advanced Autotuning, and other VIs with advanced options) implement the PID algorithm,
         and the assumptions and transformations necessary to implement the PID controller. To
         implement a PID controller, LabVIEW requires the algorithm to sample the input signals
         and discretize the integral and derivative action.

             NOTE
               The following formulas apply to most VIs on the PID palette. The PID Advanced and
                 PID Advanced Autotuning VIs use extended formulas with more advanced optional
                    features.

         The following simulation diagram represents the PID implementation provided by the
           basic PID VIs:


             NOTE
                  Constructing a simulation diagram like the one in the previous image requires the
                LabVIEW Control Design and Simulation Module. However, the PID VIs implement
                 PID controllers for you. You do not need the Control Design and Simulation Module
                   to build PID controllers. Refer to the National Instruments website at ni.com for
               more information about the Control Design and Simulation Module.


          Error Calculation

         The following formula represents the current error used in calculating proportional,
            integral, and derivative action:


1764  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1764 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1765 ordinal=1765 -->
## LabVIEW User Manual

LabVIEW User Manual


 where                          k is the index of the sampled signal at time k * t

 e(k) is the current error

 SP is the setpoint

 PV is the process variable


Proportional Action

Proportional action is the controller gain times the error, as shown in the following
formula:


 where                                             Kc is the controller gain
 e(k) is the current error


The PID VIs express the proportional component in terms of controller gain. The
relationship between controller gain Kc and proportional band PB is Kc = 100 / PB.


Integral Action (Trapezoidal Integration)

There are several options for discretizing integral action, such as forward difference,
backward difference, and trapezoidal approximation, which is also known as Tustin or
Bilinear transformation. The PID VIs use trapezoidal integration to avoid sharp changes in
integral action when there is a sudden change in PV or SP, as represented by the following
formula:


 where                   ΔT is the sampling time of the controller


Derivative Action

Abrupt changes in SP can generate bumps to the output of the controller as a result of
applying derivative action to the error e. These bumps are referred to as derivative kick. To
avoid derivative kick, you can apply derivative action to the PV only, and not to the error e.
The following formula represents the derivative action implemented by the PID VIs, which
avoids derivative kick:


                                                    © National Instruments Corporation 1765

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1765 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1766 ordinal=1766 -->
## LabVIEW User Manual

LabVIEW User Manual


          Controller Output

           Controller output is the summation of the proportional, integral, and derivative action, as
         shown in the following formula:


         Output Limiting and the Anti-Windup Algorithm

         The actual controller output is limited to the range specified for control output.

                   If                                       then


         and

                   if                                       then


         The PID VIs use an integral sum correction algorithm that facilitates anti-windup. Windup
          occurs at the upper limit of the controller output. When the error e decreases, the
            controller output decreases, moving out of the windup area. The integral sum correction
          algorithm prevents abrupt controller output changes when you switch from manual to
          automatic mode or change any other parameters. The integral sum correction works as
            follows:


                   If                                      then


         The previous statement demonstrates that the integral sum correction does not take into
          account the derivative action on value changes.


          Default PID Values and Gain Changes

         The default ranges for the parameters SP, PV, and output range correspond to percentage
           values. However, you can use actual engineering units. Adjust corresponding ranges
           accordingly. The parameters Ti and Td are specified in minutes.

         You can call the PID VIs from inside a While Loop with a fixed cycle time. All the PID VIs are
           reentrant. Multiple calls from high-level VIs use separate and distinct data. Also, the PID VI
          has a multi-channel mode where you provide an array that represents an input for each
           channel.


1766  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1766 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1767 ordinal=1767 -->
## LabVIEW User Manual

LabVIEW User Manual


PID gains can change at any time. When a change is detected, the PID algorithm tries to
perform a bumpless transition by adjusting the integral action to keep the output constant
with the new parameters. This avoids output changes when you try to modify the PID
parameters, and is useful in gain scheduling.


Gain Scheduling

Gain scheduling refers to a system where you change controller parameters based on
measured operating conditions. For example, the scheduling variable can be the setpoint,
the process variable, a controller output, or an external signal. For historical reasons, the
term gain scheduling is used even if other parameters such as derivative time or integral
time change. Gain scheduling effectively controls a system with dynamics that change with
operating conditions.

With the PID Gain Schedule VI, you can define unlimited sets of PID parameters for gain
scheduling. For each schedule, you can use autotuning to update the PID parameters.

Internal Model Control Autotuning Method

Internal model control (IMC) is a control technique that uses an internal model to try to
estimate the system response. PID and Fuzzy Logic VIs use IMC when it cannot successfully
implement the Ziegler-Nichols method, such as when a model has no delay. You also can
use the PID Autotuning Design VI to directly implement this autotuning method.

This method assumes a first-order model with delay. If your system is not a first-order
model, these techniques try to approximate one during tuning.

The following table shows the tuning formula for the internal model control technique,
where K is the model gain,  is the plant time constant, c is the desired time constant, and
is the plant delay.

 Controller                          Model         Kc            Ti       Td

 PI (delay-free)                                    —


 PI + Plant (with delay)                                —


 PID


This method is based on algorithms and techniques described in reference material by
Seborg, Dale E., Thomas F. Edgar, and Duncan A. Mellichamp. For more information about
this method, refer to the reference material by those authors.


                                                    © National Instruments Corporation 1767

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1767 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1768 ordinal=1768 -->
## LabVIEW User Manual

LabVIEW User Manual


     Lead/Lag

         You can use the PID Lead-Lag VI to implement a PID controller with a lead/lag function. The
            VI uses a positional algorithm that approximates a true exponential lead/lag. Feedforward
           control schemes often use this kind of algorithm as a dynamic compensator.

         The output value on the first call to the VI is the same as the input value.
      Logging Parameter Values After Autotuning

         The PID autotuning VIs, including PID Autotuning, PID Advanced Autotuning, and PID
          Online Autotuning, update the parameters of a PID controller and return updated PID gains
           values for the next iteration of the control application. To ensure that the correct PID gains
           values are available each time you run your control application, you must either save the VI
         you are using to implement the application each time it runs, or use a datalog file to save
          the PID gains.

         The following block diagram shows a VI that uses the File I/O VIs and functions to create a
          datalog file and save the latest value of the PID gains out output of the PID Autotuning VI
           to the file.


          Before the control loop begins, the Open/Create/Replace File function opens a datalog file,
         and the Read from Binary File function reads the file to obtain the PID gains parameters.
        When the autotuning procedure runs, a local variable updates the PID gains control. After
          the control loop is complete, the Write to Binary File function writes the current PID gains


1768  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1768 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1769 ordinal=1769 -->
## LabVIEW User Manual

LabVIEW User Manual


cluster to the datalog file and saves the file. This ensures that each time the control
application runs, the PID Autotuning VI uses updated parameters.

      RELATED INFORMATION
       Autotuning PID Controllers (PID and Fuzzy Logic) on page 1774
       Updating PID Parameters After Autotuning on page 1777

Online Autotuning Techniques

To tune PID parameters of a system, some PID VIs allow you to select the technique to
apply to the system. You can choose from two techniques that implement a step response-
based measurement and two techniques that implement a frequency response-based
measurement.

On the PID Advanced Autotuning VI, the autotuning parameters input allows you to
configure the technique to use. With the PID Online Autotuning polymorphic VI, select the
polymorphic instance that corresponds to a tuning technique you want to use. Other PID
VIs control the tuning technique for you.


Step Response Techniques

The following techniques are based on step response measurement:

    •   Step Open Loop —Performs an open-loop step test. This technique applies a step to
      the input and waits until it reaches steady-state, when the process variable does not
      change. This technique assumes that you can model any process as a first-order lag
     and a pure deadtime system.
    •   Step Closed Loop —Performs a closed-loop step test similar to the Step Open Loop
      technique.

If you do not know the characteristics of the model, such as initial PID gains, you can first
perform Step Open Loop tuning on the model to obtain the parameters. Wait until the
input reaches steady-state. This process is also known as commissioning. Next, perform
Step Closed Loop tuning on the model using the parameters computed by the Step Open
Loop tuning process as initial parameters. Both techniques assume a first-order model
with delay. If your system is not a first-order model, these techniques try to approximate
one during tuning.


Frequency Response Techniques

The following techniques are based on frequency response measurement

    •   PID Relay —Uses the setpoint relay experiment to determine the information
      needed to tune the controller. The Autotuning Wizard uses this technique.
    •   Relay Feedback —Uses an on-off relay in a feedback loop to determine ultimate gain
     and ultimate frequency. This technique is a variation on a closed-loop step test, but


                                                    © National Instruments Corporation 1769

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1769 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1770 ordinal=1770 -->
## LabVIEW User Manual

LabVIEW User Manual


                       is more efficient for systems with a large time constant. This method also
                 incorporates hysteresis to avoid noise in the system.


          Related Information

          Step Open Loop Autotuning Technique

          Step Closed Loop Autotuning Technique

          PID Relay Autotuning Technique

          Relay Feedback Autotuning Technique

              RELATED INFORMATION
                 Autotuning PID Controllers (PID and Fuzzy Logic) on page 1774
                 Step Open Loop Autotuning Technique on page 1777
                 Step Closed Loop Autotuning Technique on page 1777
                 PID Relay Autotuning Technique on page 1748
                Implementing Autotuning with the Autotuning Wizard on page 1762
                 Relay Feedback Autotuning Technique on page 1775
                 Step Open Loop Autotuning Technique on page 1777
                 Step Closed Loop Autotuning Technique on page 1777
                 PID Relay Autotuning Technique on page 1748
                 Relay Feedback Autotuning Technique on page 1775

     Advanced PID Algorithm

         The PID Advanced VI uses the same algorithm and assumptions as the PID VIs algorithm,
          but adds the functionality described in the following sections.

         The following simulation diagram represents the PID implementation provided by the PID
         Advanced VI:


1770  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1770 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1771 ordinal=1771 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
        Constructing a simulation diagram like the one in the previous image requires the
       LabVIEW Control Design and Simulation Module. However, the PID VIs implement
       PID controllers for you. You do not need the Control Design and Simulation Module
        to build PID controllers. Refer to the National Instruments website at ni.com for
      more information about the Control Design and Simulation Module.


Manual/Automatic Operation

In some situations, you might need to switch off the PID controller and operate the system
in open-loop, or manual, mode. The PID Advanced VI uses a method similar to the anti-
windup algorithm to ensure the transition between manual and automatic modes does
not cause any bump to the output of the controller.


Setpoint Weighting for Proportional Action and Derivative Action

Setpoint weighting refers to corrections applied to the error value of the controller. The
beta input (Β), which can range between 0 and 1, is applied to the proportional action as:


 where                                                    e is the error

 SP is the setpoint

 PV is the process variable

 Kc is controller gain


                                                    © National Instruments Corporation 1771

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1771 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1772 ordinal=1772 -->
## LabVIEW User Manual

LabVIEW User Manual


         You can use the beta input to reduce the overshoot of setpoint change and to allow
           increasing the gain of the controller to improve the disturbance rejection of the controller.

         The gamma (γ) input, which also can range between 0 and 1, is applied to the error and to
          the derivative as:


            Filter for Derivative Action

          Error-Squared PID Implemented by the Linearity Factor (L)

         The derivative action implemented by the PID Advanced VI is based on the backward
         method for derivative action. However, depending on the values of the derivative action,
           proportional gain, and sampling time, the controller could generate responses with fast
            oscillation, especially when performing autotuning with PID. To prevent this issue, this VI
          provides an alpha parameter that implements an additional filter for the derivative action
           D. This filter reduces the bandwidth content as defined by:


         where Td is the derivative time in minutes, also called the rate time.

         The linearity input introduces linearity change on the gain, as shown in the following
           equations:


         The error for calculating proportional action with two degree-of-freedom control is shown
            in the following formula:


                                                                                       SPrange is the
          where                                                            range of the
                                                                                     setpoint

         ß is the setpoint factor for the two degree-of-freedom PID algorithm
           described by the proportional action formula

           L is the linearity factor that produces a nonlinear gain term in which
           the controller gain increases with the magnitude of the error


1772  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1772 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1773 ordinal=1773 -->
## LabVIEW User Manual

LabVIEW User Manual


If L is 1, the controller is linear. A value of 0.1 makes the minimum gain of the controller
10% Kc. Use of a nonlinear gain term is referred to as an error-squared PID algorithm.


Error-Squared PID Implemented by the Linearity Factor (L)

The linearity input introduces linearity change on the gain, as shown in the following
equations:


The error for calculating proportional action with two degree-of-freedom control is shown
in the following formula:


                                                                            SPrange is the
 where                                                            range of the
                                                                          setpoint

 ß is the setpoint factor for the two degree-of-freedom PID algorithm
 described by the proportional action formula

 L is the linearity factor that produces a nonlinear gain term in which
 the controller gain increases with the magnitude of the error


If L is 1, the controller is linear. A value of 0.1 makes the minimum gain of the controller
10% Kc. Use of a nonlinear gain term is referred to as an error-squared PID algorithm.

Autotuning Methods for Testing PID Parameters

Autotuning automatically tests different parameter values for a PID controller to determine
the best response. A variety of methods exist for testing these parameters. PID and Fuzzy
Logic VIs support the following methods for PID autotuning:

    •   Ziegler-Nichols
    •   Internal Model Control
    •   Cohen-Coon
    •   Chien-Hrones-Reswick

The Autotuning Wizard and most of the autotuning PID VIs use the Ziegler-Nichols method
or, if Ziegler-Nichols is not possible, the Internal Model Control method. Only the PID


                                                    © National Instruments Corporation 1773

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1773 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1774 ordinal=1774 -->
## LabVIEW User Manual

LabVIEW User Manual


          Autotuning Design VI can implement the Cohen-Coon and Chien-Hrones-Reswick tuning
          methods.

              RELATED INFORMATION
                   Ziegler-Nichols Autotuning Method on page 1779
                   Internal Model Control Autotuning Method on page 1767
                Cohen-Coon Autotuning Method on page 1786
                 Chien-Hrones-Reswick Autotuning Method on page 1784

      Autotuning PID Controllers (PID and Fuzzy Logic)

           Often, many PID controllers are poorly tuned. As a result, some controllers are too
           aggressive and some controllers are too sluggish. Tuning a controller involves adjusting the
          parameters of the system to get the desired, or optimal, response. However, manually
          tuning PID controllers can be difficult when you do not know the process dynamics or
           disturbances. In this case, you can use autotuning to automatically test different parameter
           values and determine the best response.

         Choose from the following VIs that integrate autotuning based on your specific application
         needs and your knowledge of tuning theory.

          Use Case                                                                   VI Name

                     •   Autotuning that runs with minimal user input or knowledge
                   of tuning algorithms.                                                                         PID Advanced
                                                                            Autotuning VI                     •   Single VI implements a controller for a system and allows
                   tuning.

                     •   Autotuning that runs with minimal user input or knowledge
                   of tuning algorithms.
                                                                         PID Autotuning
                     •   Single VI implements a controller for a system with significant                                                                           (Temperature) VI
                deadtime and allows tuning. How-To: Programmatically
                Implementing and Autotuning a PID Controller

                     •   Controlling the autotuning technique used to identify the
                  system. Other PID VIs automatically determine the technique.
                     •   Tuning system parameters, then passing the output              PID Online
                                                                            Autotuning VI                 parameters to the PID Advanced VI to implement that
                     controller. How-To: Programmatically Autotuning a
                   Previously Implemented PID Controller

                     •   Generating PID parameters for a system given an
                  input/output signal. This technique is useful when you have
                     insufficient information about the system and you want to
                                                                         PID Autotuning                 develop initial parameters based on system response.
                                                                             Design VI
                     •   Provides access to multiple methods for determining PID
                  parameters. Other PID VIs automatically determine the
                method.


1774  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1774 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1775 ordinal=1775 -->
## LabVIEW User Manual

LabVIEW User Manual


 Use Case                                                                   VI Name

     •   Performing interactive autotuning in a dialog box that you
       use to configure the process.
                                                              PID Autotuning VI
     •   Not supported on RT or FPGA hardware targets. How-To:
       Implementing Autotuning with the Autotuning Wizard

     •   PID applications with high-speed control and/or high channel
       count on an FPGA target.                                    PID (FPGA) VI
     •   Implements a fixed-point PID algorithm.


      RELATED INFORMATION
       Online Autotuning Techniques on page 1769
       Programmatically Autotuning a Previously Implemented PID Controller on page
       1750
       Implementing Autotuning with the Autotuning Wizard on page 1762
       Updating PID Parameters After Autotuning on page 1777
       Logging Parameter Values After Autotuning on page 1768
       Online Autotuning Techniques on page 1769
       Autotuning Methods for Testing PID Parameters on page 1773

Relay Feedback Autotuning Technique

The Relay Feedback autotuning technique, which is used by the Relay Feedback instance of
the PID Online Autotuning VI, uses an on-off relay in a feedback loop to determine ultimate
gain and ultimate frequency. This technique is a variation on a closed-loop (ultimate gain)
test, but is more efficient for systems with a large time constant. This method also
incorporates hysteresis to avoid noise in the system.

      RELATED INFORMATION
       Online Autotuning Techniques on page 1769

Reproducing a Given I/O Characteristic

Consider the stepped linear characteristic curve shown in the following image. You can
describe the four linear sections with the five circled base points (xi, yi).


                                                    © National Instruments Corporation 1775

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1775 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1776 ordinal=1776 -->
## LabVIEW User Manual

LabVIEW User Manual


         To use a single-input fuzzy controller to reproduce the given characteristic, use five
            linguistic terms each for the input and output quantities, naming them x1, x2,..., x5 and y1,
               y2,..., y5, respectively. To obtain the stepped linear sections between the base points, you
          always must have exactly two available active rules. To implement this situation, entirely
          overlap the triangular membership functions for the input variable, giving each a typical
           value that corresponds to a certain base point component, xi.

         To obtain characteristic sections that are exactly linear, you must model the output
           variable with singleton membership functions, each of which has a typical value that
          corresponds to a certain base point component, yi. The rule base is then a linguistic
          enumeration of the five base points.


1776  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1776 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1777 ordinal=1777 -->
## LabVIEW User Manual

LabVIEW User Manual


Step Closed Loop Autotuning Technique

The Step Closed Loop autotuning technique, which is used by the Step Closed Loop
instance of the PID Online Autotuning VI, performs a closed-loop step test. This technique
is very accurate and reaches steady state faster than the Step Open Loop technique.

In closed-loop tuning, the PID Online Autotuning VI applies the Step Open Loop response
with the controller in a closed loop, and then back-calculates the dynamics of the system
by removing the closed loop gain.

The Step Closed Loop autotuning technique measures the deadtime Td, time constant T,
and process gain K values of a controller and multiplies them according to the formulas for
the heuristic method in place. For example, most PID VIs use the Ziegler-Nichols method.

      RELATED INFORMATION
       Online Autotuning Techniques on page 1769
       Step Open Loop Autotuning Technique on page 1777
       Step Open Loop Autotuning Technique on page 1777
       Autotuning Methods for Testing PID Parameters on page 1773
        Ziegler-Nichols Autotuning Method on page 1779

Step Open Loop Autotuning Technique

The Step Open Loop autotuning technique, which is used by the Step Open Loop instance
of the PID Online Autotuning VI, performs an open-loop step test. This technique assumes
that you can model any process as a first-order lag and a pure deadtime.

The Step Open Loop autotuning technique measures the deadtime Td, time constant T, and
process gain K values of a controller and multiplies them according to the formulas for the
heuristic method in place. For example, most PID VIs use the Ziegler-Nichols method.

      RELATED INFORMATION
       Online Autotuning Techniques on page 1769
       Autotuning Methods for Testing PID Parameters on page 1773
        Ziegler-Nichols Autotuning Method on page 1779

Updating PID Parameters After Autotuning

The PID autotuning VIs, including PID Autotuning, PID Advanced Autotuning, and PID
Online Autotuning, calculate new parameters for a PID controller that result in the best
response. When autotuning, you must write your code to apply the new PID controller
parameters (the PID gains) when the autotuning is complete.


                                                    © National Instruments Corporation 1777

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1777 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1778 ordinal=1778 -->
## LabVIEW User Manual

LabVIEW User Manual


         You can use the following methods to update PID parameters after autotuning.

             NOTE
                    In both of the following methods, you must manually save the PID gains so that
                you can use the PID gains out values the next time you run the control application.
                 Ensure that the PID gains control shows the current updated parameters, select
               Operate»Make Current Values Default, and save the VI. If you do not want to
                 manually save the VI after each run, you can use a datalog file to save PID gains
                   values.


          Using Shift Registers to Update PID Parameters

         The following block diagram shows a simple implementation of using shift registers to
          update PID parameters in the PID Autotuning VI.The shift register on the left stores the
              initial value of the PID gains. PID gains out then passes an updated value to the right-hand
             shift register terminal when each control loop iteration completes. This method is simple,
          but limited in that the user cannot change PID gains manually while the control loop runs.


          Using Local Variables to Update PID Parameters

            In place of shift registers, you can use a local variable to store updated PID gains values. In
          the following block diagram, PID Autotuning VI reads the PID gains control on each
            iteration of the While Loop, and a local variable updates the control only when tuning
         complete? is TRUE. This method allows for manual control of the PID gains while the
           control loop executes.


1778  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1778 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1779 ordinal=1779 -->
## LabVIEW User Manual

LabVIEW User Manual


Ziegler-Nichols Autotuning Method

Ziegler and Nichols developed heuristic methods for determining the parameters of a PID
controller. The Autotuning Wizard and PID VIs that use the PID Relay autotuning technique
use this method.

When using the Ziegler-Nichols autotuning method, select one of the following three types
of desired loop response performance: fast (1/4 damping ratio), normal (some overshoot),
and slow (little overshoot). The following tables show the tuning formulas for each type of
loop performance.

      NOTE
       During tuning, the process remains under closed-loop PID control. You do not need
        to switch off the existing controller and perform the experiment under open-loop
        conditions. In the setpoint relay experiment, the setpoint signal mirrors the
        setpoint for the PID controller.


Ziegler-Nichols Closed Loop/Frequency Response Method

The following tables show the tuning formulas for different types of loop performance
under proportional-only control, where Ku is the controller gain and Tu is the period of
oscillation.

 Fast Performance

 Controller                                  Kc               Ti             Td
 P                                             0.5 Ku      —        —
 PI                                             0.4 Ku         0.8 Tu       —
 PID                                           0.6 Ku         0.5 Tu          0.12 Tu


 Normal Performance

 Controller                                     Kc               Ti           Td
 P                                                0.2 Ku      —       —
 PI                                             0.18 Ku         0.8 Tu      —
 PID                                           0.25 Ku         0.5 Tu        0.12 Tu


 Slow Performance

 Controller                                   Kc                Ti            Td


                                                    © National Instruments Corporation 1779

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1779 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1780 ordinal=1780 -->
## LabVIEW User Manual

LabVIEW User Manual


          Slow Performance

         P                                           0.13 Ku      —       —
             PI                                          0.13 Ku         0.8 Tu      —
           PID                                         0.15 Ku         0.5 Tu         0.12 Tu


           Ziegler-Nichols Open Loop/Step Response Method

         The following tables shows the tuning formulas for different types of loop performance
         under PI or PID control, where TP is the time constant and  is the dead time.

            Fast Performance

            Controller                                     Kc                  Ti          Td
         P                                          TP /        —      —
             PI                                               0.9 TP /            3.33      —
           PID                                             1.1 TP /             2.0          0.5


          Normal Performance

            Controller                                        Kc                  Ti         Td
         P                                               0.44 TP /       —     —
             PI                                                 0.4 TP /           5.33     —
           PID                                             0.53 TP /            4.0         0.8


          Slow Performance

            Controller                                      Kc                   Ti         Td
         P                                             0.26 TP /       —      —
             PI                                            0.24 TP /           5.33     —
           PID                                           0.32 TP /             4.0          0.8


             NOTE
               The previous tables provides proportional gain Kc values. The following equation
                  describes the relationship between proportional gain and proportional band PB:
                  Kc = 100/ PB


1780  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1780 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1781 ordinal=1781 -->
## LabVIEW User Manual

LabVIEW User Manual


Defuzzification
Center of Area (CoA)

In the Center of Area (CoA) defuzzification method, also called the Center of Gravity (CoG)
method, the fuzzy controller first calculates the area under the scaled membership
functions and within the range of the output variable. The fuzzy logic controller then uses
the following equation to calculate the geometric center of this area.


where CoA is the center of area, x is the value of the linguistic variable, and xmin and xmax
represent the range of the linguistic variable. The Center of Area defuzzification method
effectively calculates the best compromise between multiple output linguistic terms.

The following image shows the Center of Area defuzzification method for the Steering
Angle φ output linguistic variable of a vehicle maneuvering fuzzy system, assuming the
Minimum implication method. The shaded portion of the graph represents the area under
the scaled membership functions.


                                                    © National Instruments Corporation 1781

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1781 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1782 ordinal=1782 -->
## LabVIEW User Manual

LabVIEW User Manual


         The following image summarizes the process of a fuzzy controller for the vehicle
         maneuvering example using the Center of Area defuzzification method.


      Center of Maximum (CoM)

            In the Center of Maximum (CoM) defuzzification method, the fuzzy logic controller first
          determines the typical numerical value for each scaled membership function. The typical


1782  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1782 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1783 ordinal=1783 -->
## LabVIEW User Manual

LabVIEW User Manual


numerical value is the mean of the numerical values corresponding to the degree of
membership at which the membership function was scaled.


where xn is the typical numerical value for the scaled membership function n, and μn is the
degree of membership at which the membership function n was scaled.

The following image illustrates how to use the CoM defuzzification method with the vehicle
maneuvering example.


The values -15° and -5° are the typical values of the linguistic terms Negative Medium and
Negative Small. The degrees of truth for these linguistic terms are 0.1 and 0.8, respectively.
Therefore, the defuzzified crisp output value φfinal is calculated by the following equation:


The CoM defuzzification method is identical to the Center of Area (CoA) method with
singleton membership functions.

The CoM and CoA defuzzification methods usually apply to closed-loop control
applications of fuzzy logic. These methods usually result in continuous output signals
because a small change in input values does not change the best compromise value for the
output.


                                                    © National Instruments Corporation 1783

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1783 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1784 ordinal=1784 -->
## LabVIEW User Manual

LabVIEW User Manual


      Center of Sums (CoS)

            In the Center of Sums (CoS) defuzzification method, the fuzzy logic controller first
           calculates the geometric center of area for each membership function, as shown in the
           following image.


         The fuzzy controller then uses the following equation to calculate a weighted average of
          the geometric center of area for all membership functions.


         where CoAn is the geometric center of area of the scaled membership function n, and arean
              is the area of the scaled membership function n.
      Chien-Hrones-Reswick Autotuning Method

         The Chien-Hrones-Reswick autotuning method focuses on setpoint response and
          disturbance response. This method provides formulas for 0% and 20% overshoot.

             NOTE
                You must use the PID Autotuning Design VI to implement this autotuning method.
                   Select the Chien-Hrones-Reswick polymorphic instance and use the Tuning
                   specifications input to configure which formula you want to use.

         The following tables shows the Chien-Hrones-Reswick recommendations for each tuning
           formula:


1784  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1784 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1785 ordinal=1785 -->
## LabVIEW User Manual

LabVIEW User Manual


 Regulator – 0% overshoot

 Controller                              Kc                      Ti            Td
 P                                       0.3 TP /         —       —
 PI                                      0.6 TP /              4        —
 PID                                  0.95 TP /                2.4            0.42

where TP is the time constant and  is the deadtime.

 Regulator – 20% overshoot

 Controller                              Kc                     Ti             Td
 P                                       0.7 TP /         —        —
 PI                                      0.7 TP /               2.3        —
 PID                                     1.2 TP /              2             0.42

where TP is the time constant and  is the deadtime.

 Servo – 0% overshoot

 Controller                               Kc                       Ti           Td
 P                                        0.3 TP /         —       —
 PI                                     0.35 TP /                1.2       —
 PID                                      0.6 TP /                                0.5

where TP is the time constant and  is the deadtime.

 Servo – 20% overshoot

 Controller                              Kc                      Ti            Td
 P                                       0.7 TP /         —       —
 PI                                      0.6 TP /                 —
 PID                                  0.95 TP /                1.4            0.47

where TP is the time constant and  is the deadtime.


                                                    © National Instruments Corporation 1785

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1785 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1786 ordinal=1786 -->
## LabVIEW User Manual

LabVIEW User Manual


     Cohen-Coon Autotuning Method

         The Cohen-Coon autotuning method is an offline method for tuning PID controllers. This
         method uses PID parameters obtained from an open-loop transfer function experiment.
           This method is similar to the Ziegler-Nichols method, but provides better results when the
            controller has a large deadtime Td relative to the time constant T.

             NOTE
                You must use the PID Autotuning Design VI to implement this autotuning method.

         The following table shows the Cohen-Coon recommendations for tuning parameters under
            different tuning specifications:

            Controller                   Kc                            Ti                Td

         P                              —          —


             PI                                         —


           PID


         Where T is the time constant

          Kc is the proportional gain

          Td is the deadtime
     Complete Rule Bases

         A rule base with at least one active rule for each possible combination of input linguistic
           variables and linguistic terms is a complete rule base. If you define an incomplete rule
           base, you must specify a default linguistic term for each output linguistic variable so the
           fuzzy controller can handle situations in which no rules are active.

         The Vehicle Position x input linguistic variable has five linguistic terms, and the Vehicle
           Orientation β linguistic variable has seven linguistic terms. Therefore, the rule base of the
           vehicle maneuvering example consists of N = 5*7 = 35 rules. You can document the


1786  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1786 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1787 ordinal=1787 -->
## LabVIEW User Manual

LabVIEW User Manual


complete rule base in matrix form, as shown in the following image for the vehicle
maneuvering fuzzy system.


In the previous image, each column or row represents an antecedent of a rule. The term at
the intersection of a column and a row is the consequent of the rule corresponding to the
aggregated rule antecedent. For example, the following rule is highlighted:

 IF Vehicle Position x is Left Center AND Vehicle Orientation β is Left, THEN Steering Angle
 φ is Negative Small.


Cascading Fuzzy Systems

Plotting a rule base in matrix form, as in the previous image, is helpful for detecting
inconsistencies, such as contradictory rules. However, plotting a rule basein matrix form is
efficient only for small rule bases. Detecting inconsistencies in large rule bases is difficult.
For fuzzy systems with numerous controller inputs, you can use cascading fuzzy systems to
avoid large rule bases. In cascading fuzzy systems, the outputs of the first fuzzy system
serve as the inputs to the next fuzzy system, and so on.


                                                    © National Instruments Corporation 1787

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1787 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1788 ordinal=1788 -->
## LabVIEW User Manual

LabVIEW User Manual


      Control Output Rate Limiting

         Sudden changes in control output are often undesirable or even dangerous for many
           control applications. For example, a sudden large change in setpoint can cause a very large
         change in controller output. Although in theory this large change in controller output
            results in fast response of the system, it also can cause unnecessary wear on actuators or
         sudden large power demands. In addition, the PID controller can amplify noise in the
          system and result in a constantly changing controller output.

         You can use the PID Output Rate Limiter VI to avoid the problem of sudden changes in
            controller output. Wire the output value of the PID VI to the input (controller output)
           input of the PID Output Rate Limiter VI to limit the slew, or rate of change, of the output to
          the value of the output rate (EGU/min).

          Assign a value to initial output to specify the output value on the first call to the VI. Use the
          dt (s) input to specify the same control-loop cycle time you use for the PID VI.
      Converting Between Percentage of Full Scale and
      Engineering Units

         The default setpoint, process variable, and output ranges for the PID VIs correspond to
          percentage of full scale. In other words, proportional gain Kc relates percentage of full scale
          output to percentage of full scale input. This is the default behavior of many PID controllers
         used for process control applications. To implement PID in this way, you must scale all
           inputs to percentage of full scale and all controller outputs to actual engineering units, for
          example, volts for analog output.

         You can use the PID EGU to Percentage VI to convert any input from real engineering units
           to percentage of full scale, and you can use the PID Percentage to EGU VI to convert the
            controller output from percentage to real engineering units.

             NOTE
               The PID VIs do not use the setpoint range and output range information to convert
                  values to percentages in the PID algorithm. The controller gain relates the output
                    in engineering units to the input in engineering units. For example, a gain value of
                1 produces an output of 10 for a difference between setpoint and process variable
                   of 10, regardless of the output range and setpoint range.

      Creating a Rule Base

            After create linguistic variables, defining linguistic terms, and creating membership
           functions, the last step of fuzzy system design is creating a rule base. Rules describe, in
          words, the relationships between input and output linguistic variables based on their
            linguistic terms. A rule base is the set of rules for a fuzzy system.


1788  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1788 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1789 ordinal=1789 -->
## LabVIEW User Manual

LabVIEW User Manual


To create a rule, you must specify the antecedents, or IF portions, and consequents, or
THEN portions, of the rule. For example, consider the following rule for a vehicle
maneuvering fuzzy system:

 IF Vehicle Position x is Left Center AND Vehicle Orientation β is Left Up, THEN Steering
 Angle φ is Positive Small.


The clauses " Vehicle Position x is Left Center " and " Vehicle Orientation β is Left Up " are
the antecedents of this rule. The clause " Steering Angle φ is Positive Small " is the
consequent of this rule.

Associate an input linguistic variable with a corresponding linguistic term to form an
antecedent. Associate an output linguistic variable with a corresponding linguistic term to
form a consequent. The consequent of a rule represents the action you want the fuzzy
controller to take if the linguistic terms of the input linguistic variables in the rule are met.

When constructing a rule base, avoid contradictory rules, or rules with the same IF portion
but different THEN portions. A consistent rule base is a rule base that has no contradictory
rules.

      NOTE
      The rule base itself is the biggest influence on the I/O characteristics of a fuzzy
         controller. The rule base determines the principal functionality of the controller.
        Refer to the Using the Mean of Maximum (MoM) Defuzzification Method example to
       see how changing the rule base can affect the output characteristic of a fuzzy
         controller.


Total Possible Rules

The total number N of possible rules for a fuzzy system is defined by thefollowing equation:

N = p1 * p2 *...* pn

where pn is the number of linguistic terms for the input linguistic variable n.

If each input linguistic variable has the same number of linguistic terms, the total number
N of possible rules is defined by the following equation:

N = pm

where p is the number of linguistic terms for each input linguistic variable and m is the
number of input linguistic variables. For example, for three input linguistic variables with
five linguistic terms each, the total number of possible rules is N = 53 = 125.


Additional Information About Rule Bases

The following topics contain additional important information about creating rule bases:


                                                    © National Instruments Corporation 1789

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1789 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1790 ordinal=1790 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Complete Rule Bases
                   •   Specifying an Antecedent Connective
                   •   Specifying a Consequent Implication Method

      Creating Linguistic Variables

        When you design a fuzzy system, linguistic variables represent, in words, the input
           variables and output variables of the system you want to control.

        When you create a linguistic variable to represent an input or output variable, decide how
        many linguistic terms, or categories of values of the linguistic variable, you want to create.
            Linguistic variables usually have an odd number of linguistic terms, with a middle linguistic
         term and symmetric linguistic terms at each extreme. In most applications, three to seven
            linguistic terms are sufficient for categorizing the values of a linguistic variable.

          Consider an example in which you want to automate a vehicle to park itself from an
            arbitrary starting position. A driver can control the vehicle by constantly evaluating the
           current status of the vehicle, such as the distance from the target position and the
           orientation of the vehicle, to derive the correct steering angle. The following image
             illustrates this example.


         You can define two input linguistic variables for this example. Vehicle Position x represents
          the vehicle position in relation to the destination. Vehicle Orientation β represents the
           orientation of the vehicle. You also can define an output linguistic variable, Steering Angle
          φ, to represent the steering angle of the vehicle that you want to control.


1790  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1790 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1791 ordinal=1791 -->
## LabVIEW User Manual

LabVIEW User Manual


Defining Linguistic Terms

You can define linguistic terms of Left, Left Center, Center, Right Center, and Right for the
Vehicle Position x input linguistic variable to describe the possible positions of the vehicle
in relation to the destination. You can define linguistic terms of Left Down, Left, Left Up, Up,
Right Up, Right, and Right Down for the Vehicle Orientation β input linguistic variable to
describe the possible orientations of the vehicle. The linguistic terms of the Steering Angle
φ output linguistic variable must represent both the direction and magnitude that the
steering angle changes. Therefore, you can use the linguistic terms Negative Large,
Negative Medium, Negative Small, Zero, Positive Small, Positive Medium, and Positive
Large for this output linguistic variable.

The next step in designing a fuzzy system is creating membership functions that
correspond to the linguistic terms you define.
Creating Membership Functions

When you design a fuzzy system, you first create linguistic variables for which you define
linguistic terms. After you define the linguistic terms, you must apply membership
functions to those terms. Membership functions are simply numerical functions that
correspond to linguistic terms. A membership function represents the degree of
membership of linguistic variables within their linguistic terms.

You can apply the normalized standard membership functions shown in the following
image to most technical processes. These standard functions include Λ-type (triangular
shape), Π-type (trapezoidal shape), singleton-type (vertical line shape), Sigmoid-type
(wave shape), and Gaussian-type (bell shape) membership functions.


Example Triangle Membership Function for the Linguistic Term

Example Trapezoidal Membership Function for the Linguistic Term Center

Membership Functions for a Vehicle Maneuvering Fuzzy System

For example, the linguistic variable Vehicle Position x might have full membership (1)
within the linguistic term Center at 5 meters, no membership (0) within that term at 4
meters or less and 6 meters or greater, and partial membership at all distances between 4
and 6 meters. If you plot the degree of membership against the value of Vehicle Position x,
you can see that the resulting membership function is a triangle function.


                                                    © National Instruments Corporation 1791

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1791 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1792 ordinal=1792 -->
## LabVIEW User Manual

LabVIEW User Manual


         Sometimes a linguistic variable has full membership within a linguistic term at a range of
           values rather than at a point value. If, for example, the linguistic variable Vehicle Position x
          has full membership within the linguistic term Center at values x = 5 ± 0.25 m, a trapezoidal
         membership function applies, as shown in the following image.


         The following image shows the membership functions for Vehicle Position x.


1792  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1792 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1793 ordinal=1793 -->
## LabVIEW User Manual

LabVIEW User Manual


The following image shows the membership functions for Vehicle Orientation β.


The following image shows the membership functions for Steering Angle φ.


                                                    © National Instruments Corporation 1793

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1793 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1794 ordinal=1794 -->
## LabVIEW User Manual

LabVIEW User Manual


         Example Trapezoidal Membership Function for the Linguistic Term

         Membership Functions for a Vehicle Maneuvering Fuzzy System

         Sometimes a linguistic variable has full membership within a linguistic term at a range of
           values rather than at a point value. If, for example, the linguistic variable Vehicle Position x
          has full membership within the linguistic term Center at values x = 5 ± 0.25 m, a trapezoidal
         membership function applies, as shown in the following image.


1794  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1794 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1795 ordinal=1795 -->
## LabVIEW User Manual

LabVIEW User Manual


The following image shows the membership functions for Vehicle Position x.


The following image shows the membership functions for Vehicle Orientation β.


The following image shows the membership functions for Steering Angle φ.


                                                    © National Instruments Corporation 1795

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1795 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1796 ordinal=1796 -->
## LabVIEW User Manual

LabVIEW User Manual


         Membership Functions for a Vehicle Maneuvering Fuzzy System

         The following image shows the membership functions for Vehicle Position x.


         The following image shows the membership functions for Vehicle Orientation β.


1796  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1796 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1797 ordinal=1797 -->
## LabVIEW User Manual

LabVIEW User Manual


The following image shows the membership functions for Steering Angle φ.


Defuzzification Methods

Defuzzification is the process of converting the degrees of membership of output linguistic
variables within their linguistic terms into crisp numerical values. Consider the following
rules:


                                                    © National Instruments Corporation 1797

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1797 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1798 ordinal=1798 -->
## LabVIEW User Manual

LabVIEW User Manual


                                     IF Vehicle Position x is                  Vehicle Orientation β is Left                                            AND              (1)                   Center (degree of              Up (degree of membership                                                 (Minimum)                            membership = 0.8)                        = 1.0) = 0.8

         THEN Steering
           Angle φ is
           Negative Small

                                     IF Vehicle Position x is                  Vehicle Orientation β is Left                                            AND              (2)                 Right Center (degree of            Up (degree of membership                                                 (Minimum)                            membership = 0.1)                        = 1.0) = 0.1

         THEN Steering
           Angle φ is
           Negative Medium


         These two rules specify two non-zero values for the Steering Angle φ output linguistic
            variable:

           Negative Medium Negative Small              to a degree of to a degree of      0.1 0.8


             NOTE
                 Fuzzy controllers use an implication method to scale the membership functions of
                 output linguistic variables before performing defuzzification.

         A fuzzy controller can use one of several mathematical methods to perform defuzzification:
          Center of Area (CoA), modified Center of Area (mCoA), Center of Sums (CoS), Center of
        Maximum (CoM), or Mean of Maximum (MoM). Selecting a defuzzification method depends
         on the context of the design you want to calculate with the fuzzy controller.


          Related Information

          Center of Area (CoA)

          Modified Center of Area (mCoA)

          Center of Maximum (CoM)

        Mean of Maximum (MoM)

          Center of Sums (CoS)


1798  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1798 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1799 ordinal=1799 -->
## LabVIEW User Manual

LabVIEW User Manual


Selecting a Defuzzification Method

      RELATED INFORMATION
       Creating Linguistic Variables on page 1790
       Fuzzy Controllers on page 1737
        Specifying a Consequent Implication Method on page 1755
       Creating Membership Functions on page 1791
       Center of Area (CoA) on page 1781
       Modified Center of Area (mCoA) on page 1804
       Center of Sums (CoS) on page 1784
       Center of Maximum (CoM) on page 1782
      Mean of Maximum (MoM) on page 1803
        Selecting a Defuzzification Method on page 1805
       Center of Area (CoA) on page 1781
       Modified Center of Area (mCoA) on page 1804
       Center of Maximum (CoM) on page 1782
      Mean of Maximum (MoM) on page 1803
       Center of Sums (CoS) on page 1784
        Selecting a Defuzzification Method on page 1805

Designing a Control Strategy

You can design a control strategy by sketching a flowchart that includes the physical
process and control elements such as valves and measurements. Also include feedback
from the process and any required computations. You then can use the PID VIs, combined
with the math and logic VIs and functions in LabVIEW, to translate the flowchart into a
LabVIEW block diagram.

The following image shows a sample control flowchart:


                                                    © National Instruments Corporation 1799

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1799 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1800 ordinal=1800 -->
## LabVIEW User Manual

LabVIEW User Manual


         The following image shows the equivalent LabVIEW block diagram:


            In the previous images, FT is the flow transmitter, LT is the level transmitter, LC is the level
           of control, and SP is the setpoint. The only elements missing from this simplified VI are the
           loop-tuning parameters and the automatic-to-manual switching.

         You can handle the inputs and outputs through DAQ devices, FieldPoint I/O modules, GPIB
           instruments, or serial I/O ports. You can adjust polling rates in real time. Potential polling
           rates are limited only by your hardware and by the number and graphical complexity of
          your VIs.


1800  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1800 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1801 ordinal=1801 -->
## LabVIEW User Manual

LabVIEW User Manual


Setting Timing

The PID VI and the PID Lead-Lag VI are time-dependent. A VI can acquire timing
information either from a value you supply to the cycle time control, dt, or from a time
keeper such as those built into the PID VIs. If dt is less than or equal to zero, the VI
calculates new timing information each time LabVIEW calls it. At each call, the VI measures
the time since the last call and uses that difference in its calculations. If you call a VI from a
While Loop that uses one of the LabVIEW Timing VIs and functions, you can achieve fairly
regular timing, and the internal time keeper compensates for variations. However, the
resolution of the Tick Count (ms) function is limited to 1 ms.

If dt is a positive value in seconds, the VI uses that value in the calculations, regardless of
the elapsed time. National Instruments recommends you use this method for fast loops,
such as when you use acquisition hardware to time the controller input or real-time
applications. Refer to the example VIslocated in the labview\examples\control
\PID directory for examples of using timing with the PID VIs.

   Find related examples

      NOTE
            If you installed NI-DAQmx, you also can view relevant examples in the labview
      \examples\DAQmx\Control\Control.llb directory.

According to control theory, a control system must sample a physical process at a rate
about 10 times faster than the fastest time constant in the physical process. For example, a
time constant of 60 seconds is typical for a temperature control loop in a small system. In
this case, a cycle time of about 6 seconds is sufficient. Faster cycling does not improve
performance. In fact, running all your control VIs too fast can degrade the response time of
your LabVIEW application.

All VIs within a loop execute once per iteration at the same cycle time. To run several
control VIs at different cycle times and still share data between them, as for example in a
cascade, you must separate the VIs into independently timed While Loops. The following
block diagram shows a cascade with two independently timed While Loops:


                                                    © National Instruments Corporation 1801

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1801 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1802 ordinal=1802 -->
## LabVIEW User Manual

LabVIEW User Manual


         A global variable passes the output of the PID VI in Loop A to the process variable input of
          the PID VI in Loop B. You can place both While Loops on the same block diagram or in
          separate VIs. Use additional global or local variables to pass any other necessary data
         between the two While Loops.

                 If the front panel of your VI does not contain graphics that LabVIEW must update
           frequently, the PID VIs can execute at kilohertz (kHz) rates. However, actions such as mouse
            activity and window scrolling interfere with these rates.
       Different Overlapping Degrees of Membership
      Functions for Output Terms

         The following image shows that if all the consequent terms are equal in width, the
          overlapping degree of the membership functions for the consequent terms has no
            significant influence on the controller characteristic.


1802  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1802 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1803 ordinal=1803 -->
## LabVIEW User Manual

LabVIEW User Manual


      RELATED INFORMATION
       Creating Membership Functions on page 1791
        I/O Characteristics of Fuzzy Controllers on page 1744

Mean of Maximum (MoM)

Use the Mean of Maximum (MoM) defuzzification method for pattern recognition
applications. This defuzzification method calculates the most plausible result. Rather than


                                                    © National Instruments Corporation 1803

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1803 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1804 ordinal=1804 -->
## LabVIEW User Manual

LabVIEW User Manual


          averaging the degrees of membership of the output linguistic terms, the MoM
            defuzzification method selects the typical value of the most valid output linguistic term.

         The following image illustrates the MoM defuzzification method.


      Modified Center of Area (mCoA)

         Because the Center of Area (CoA) defuzzification method evaluates the area under the
           scaled membership functions only within the range of the output linguistic variable, the
            resulting crisp output values cannot span the full range. To solve this problem, use the
          modified Center of Area defuzzification method.

         The modified Center of Area defuzzification method is similar to the Center of Area
            defuzzification method. However, the fuzzy logic controller considers the full area under
          the scaled membership functions, even if this area extends beyond the range of the output
            variable. The fuzzy logic controller uses the following equation to calculate the geometric
           center of the full area under the scaled membership functions.


         where mCoA is the modified center of area.

         The interval of integration is between the minimum membership function value and the
        maximum membership function value. Note that this interval might extend beyond the
          range of the output variable.


1804  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1804 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1805 ordinal=1805 -->
## LabVIEW User Manual

LabVIEW User Manual


Comparing CoA and Modified CoA Defuzzification Methods

The following image illustrates the difference between the Center of Area and modified
Center of Area defuzzification methods.


Selecting a Defuzzification Method

In decision support systems, the choice of the defuzzification method depends on the
context of the decision you want to calculate with the fuzzy controller. For quantitative
decisions like project prioritization, apply the Center of Maximum (CoM) method. For
qualitative decisions, such as an evaluation of credit worthiness, Mean of Maximum (MoM)
is the correct method.

An important aspect of a defuzzification method is the continuity of the output signal.
Consider a fuzzy system with a complete rule base and overlapping membership functions.


                                                    © National Instruments Corporation 1805

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1805 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1806 ordinal=1806 -->
## LabVIEW User Manual

LabVIEW User Manual


         A defuzzification method is continuous if an arbitrary small change of an input value never
          causes an abrupt change in the output signal.

            In this respect, the defuzzification methods CoM and Center of Area (CoA) are continuous
          because, assuming overlapping output membership functions, the best compromise does
          not jump to a different value with a small change to the inputs. The defuzzification method
        MoM, however, is discontinuous because an arbitrary small change in the input values of
          the fuzzy system can cause the output value to switch to another, more plausible result.

          Using CoA or CoM as the defuzzification method results in continuous controller
            characteristic functions, especially within those intervals of the input values in which two
           or more rules are active simultaneously. This behavior results from the averaging character
           of the defuzzification methods.

         The following table compares the different defuzzification methods based on various
          assessment criteria.

          Assessment                                                Method             Criteria

            Center of Sums       Center of        Mean of
                 (CoS)      Maximum (CoM)  Maximum (MoM)

             Linguistic                                Best            Best      Most Plausible                             Best Compromise             Characteristic                     Compromise    Compromise       Result

                              Implausible with  Implausible with
                                   varying           varying
                           membership     membership
                               function shapes   function shapes              Fit with Intuition                                  Good        Good                            and strong      and strong
                                overlapping      overlapping
                           membership     membership
                                  functions         functions

            Continuity               Yes               Yes             Yes         No

           Computational                                 Very High        Medium        Low         Very Low             Effort

                                                              Closed-Loop      Pattern                              Closed-Loop      Closed-Loop                                                                        Control,      Recognition,                                Control, Decision  Control, Decision            Application Field                                         Decision       Decision                               Support, Data     Support, Data                                                                Support, Data  Support, Data                                    Analysis           Analysis                                                                        Analysis        Analysis

      Using the Mean of Maximum (MoM) Defuzzification
     Method

        When you use the Mean of Maximum (MoM) defuzzification method, you calculate the most
           plausible result. In other words, the fuzzy controller uses the typical value of the


1806  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1806 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1807 ordinal=1807 -->
## LabVIEW User Manual

LabVIEW User Manual


consequent term of the most valid rule as the crisp output value. This behavior results in
stepped output characteristics, as shown in the following image.


The previous image shows entirely overlapping membership functions for input and output
terms.


Changing the Rule Base

The rule base itself has the biggest influence on the controller characteristic. The rule base
determines the principal functionality of the controller.


                                                    © National Instruments Corporation 1807

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1807 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1808 ordinal=1808 -->
## LabVIEW User Manual

LabVIEW User Manual


         The following image illustrates how the controller characteristic changes if you change the
            rule base of the previous example to include the following rules:

           Rule 1:             IF         x = negative        THEN          y = negative

           Rule 2:             IF           x = zero          THEN           y = positive

           Rule 3:             IF         x = positive        THEN          y = negative


1808  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1808 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1809 ordinal=1809 -->
## LabVIEW User Manual

LabVIEW User Manual


Wide and Small Membership Functions for Output
Terms

If you want to significantly influence the controller characteristic, use output terms that
membership functions model with equally distributed typical values but different scopes
of influence instead. The different terms have different areas and thus different weights
with respect to the defuzzification process. A wide output term has more influence on the
inference result than a small neighboring output term. The following image demonstrates
this effect.


                                                    © National Instruments Corporation 1809

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1809 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1810 ordinal=1810 -->
## LabVIEW User Manual

LabVIEW User Manual


              RELATED INFORMATION
                   I/O Characteristics of Fuzzy Controllers on page 1744
                  Creating Membership Functions on page 1791
                    Defuzzification Methods on page 1797


1810  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1810 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1811 ordinal=1811 -->
## LabVIEW User Manual

LabVIEW User Manual


Distributed System Manager Overview

Use the Distributed System Manager to complete the following tasks:

    •   Create shared or network variables.
    •   Monitor shared or network variables.
    •   Create and monitor processes.
    •   Create and monitor I/O servers.
    •   Manage security.
    •   Manage aliases.
    •   Start and stop the Shared Variable Engine.
    •   Force I/O variable values.
    •   View and clear scan engine faults.
    •   View and set scan engine modes.
    •   Monitor real-time target resources.
    •   Monitor alarms and events.
    •   Acknowledge alarms and events.
    •   Configure alarms for shared variables.
    •   Monitor historical trends.
    •   Log historical trends.
    •   Synchronize time for networked computers.

      NOTE
       You must use an alternate method to start or stop the Shared Variable Engine on
      Windows 7/Vista.


                                                    © National Instruments Corporation 1811

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1811 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1812 ordinal=1812 -->
## LabVIEW User Manual

LabVIEW User Manual


           Select Start»National Instruments»NI Distributed System Manager to launch the
           Distributed System Manager. In LabVIEW, you also can launch the Distributed System
         Manager by selecting Tools»Distributed System Manager.

              RELATED INFORMATION
                   Creating, Modifying, or Deleting Shared or Network Variables on page 1837
                  Monitoring Variables with the Watch List View on page 1834
                  Processes on page 1841
                   I/O Servers on page 1817
                Shared Variable Engine on page 1819
                  Forcing I/O Variable Values (NI Scan Engine) on page 1815
                 Viewing and Clearing Faults (NI Scan Engine) on page 1822
                 Viewing and Setting the Scan Engine Mode (NI Scan Engine) on page 1821
                  Monitoring Alarms and Events on page 1833
                Acknowledging Alarms and Events on page 1822
                  Configuring Alarms for Shared Variables (DSC Module) on page 1832
                  Synchronizing Time for Networked Computers on page 1819
                Systems on page 1820
                  Processes on page 1841
                Shared or Network Variables on page 1818
                  Monitoring Variables with the Watch List View on page 1834
               CPU/Memory Probe View on page 1824
                   I/O Variable Probe View on page 1825
                  Process Probe View on page 1827
                Scan Engine Probe View on page 1827
                   Variable Probe View on page 1829
              Web Server Probe View on page 1830
              Web Service Probe View on page 1831

      Distributed System Manager Components
          Learn about the components of the Distributed System Manager.

                   •   System tree —Displays all available objects on the network. The system tree
                appears as the primary navigation pane in the System Manager workspace.
                   •   System tree object —Refers to all types of objects that might appear in the system
                    tree. System tree object can refer to a system, process, variable, or additional object
                 types installed with modules and toolkits.


1812  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1812 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1813 ordinal=1813 -->
## LabVIEW User Manual

LabVIEW User Manual


    •   Watch list — Monitors a single variable or multiple variables contained within a
      system or process.
    •   Auto View —Displays the Probe view for any system tree object that you select. If
      you select multiple objects, this view displays a Watch List view that contains all of
      the selected objects.
    •   Probe views —Display information and configuration options for the following
      components:
            ◦  CPU/Memory
            ◦   I/O Variable
            ◦   Process
            ◦   Scan Engine
            ◦   Variable
            ◦  Web Server
            ◦  Web Service

File Menu

The File menu contains items for managing System Manager workspaces. Workspaces
display information about all shared or network variables that are currently deployed,
including the URL, current value, data type, timestamp information, and any error or
quality messages. Quality messages list errors and other conditions that apply to the
variable.

    •  New Workspace —Creates a new workspace. When you select this menu item, the
      System Manager removes all variables from the Watch List view and resets the
      workspace layout.
    •  Open Workspace —Opens a saved workspace.
    •   Save Workspace —Saves the current workspace with the .smw extension.
    •   Settings —Displays the Settings dialog box where you can customize workspace
       layout, set the data update rate, and specify the System Manager to save its
      workspace between sessions.

Actions Menu

The Actions menu contains items for starting and stopping the Shared Variable Engine,
refreshing your workspace, and logging into a system.

    •   Start Local Shared Variable Engine —Restarts the Shared Variable Engine.
          NOTE
            You must use an alternate method to start the Shared Variable Engine on
            Windows 7/Vista.


                                                    © National Instruments Corporation 1813

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1813 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1814 ordinal=1814 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Stop Local Shared Variable Engine —Shuts down the Shared Variable Engine.
                  NOTE
                      You must use an alternate method to stop the Shared Variable Engine on
                    Windows 7/Vista.
                   •   Register Computer —Displays the Register Computer dialog box, which you can
                use to register remote computers.
                   •   Alias Manager —Displays the Alias Manager dialog box, which you can use to
                 configure aliases for local computers and IP addresses.
                         ◦   (DSC Module) The Shared Variable Engine uses aliases when running custom
                         I/O servers that refer to other variables in the system.
                   •   Log In —Displays the NI Security Login dialog box.
                   •   Log Out —Logs out of the session configured in the NI Security Login dialog box.
                   •   Configure Security —Displays the NI ACL Configuration dialog box, which you can
                use to update security settings.
                   •  Add System to My Systems —Displays the Add Systems to My Systems dialog box
                  that allows you to add a system to My Systems on the system tree.

      View Menu

         The View menu contains the options to display certain windows in the workspace and
          access a system tree object that does not appear in the system tree.

                   •   Auto View —Displays the Probe view for any system tree object that you select. If
               you select multiple objects, this view displays a Watch List that contains all of the
                 selected objects.
                   •   Alarms and Events —Displays the Alarms and Events view for any systems located
                 within My Systems on the system tree.
                   •   Probe Location —Displays the Probe Location dialog box for a system, process, or
                   variable. You can enter the location of objects that appear in the system tree, as well
                 as those that do not.
                   •   Configure Time Servers — (DSC Module) Displays the Shared Variable Engine Time
                 Server Configuration dialog box. You can use the dialog box to synchronize the time
                  of machines on the network with a central time server.
                   •  New Watch List —Creates a blank Watch List view. Drag a system tree object into
                    this view to add it to the Watch List view.
                   •   Refresh —Updates the contents of the system tree and Watch List views.


1814  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1814 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1815 ordinal=1815 -->
## LabVIEW User Manual

LabVIEW User Manual


    •  New Historical Trend — (DSC Module) Creates a blank Historical Trend view. Drag
      a system tree pane object into this view to monitor the historical trend of this
       object.

      RELATED INFORMATION
        Distributed System Manager Overview on page 1811
        Distributed System Manager Overview on page 1811
        Distributed System Manager Overview on page 1811
       Monitoring Variables with the Watch List View on page 1834
       Alarms and Events View on page 1823
       Systems on page 1820
       Processes on page 1841
       Shared or Network Variables on page 1818

Help Menu

The Help menu contains items to explain and define System Manager features and provide
System Manager documentation.

    •   System Manager Overview —Displays the NI Distributed System Manager Help.
      Use this help file for information about creating and managing shared or network
       variables and other system tree objects.
          NOTE
              Refer to the LabVIEW Help, NI Measurement Studio Help, or
            LabWindows/CVI Help for more information about using variables created
              with the System Manager in your applications.
    •   About System Manager —Displays general information about the current
        installation, such as the version number.

Forcing I/O Variable Values (NI Scan Engine)

You can use an I/O variable probe to force I/O variable values. Forcing an I/O variable
causes the input or output and all associated aliases of the variable to assume the forced
value until you unforce the value. If an input from hardware returns an error, and the
associated I/O variable is forced, System Manager does not display the error. However, if
the error results in a fault, LabVIEW registers the fault. If an output returns an error, System
Manager displays the error.

      NOTE
            If you link several I/O variables in a chain of aliases and force one of the I/O
        variables in the chain, the forced value applies to all I/O variables in the chain.


                                                    © National Instruments Corporation 1815

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1815 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1816 ordinal=1816 -->
## LabVIEW User Manual

LabVIEW User Manual


          Enabling I/O Variable Forcing

         Complete the following steps to enable and disable I/O variable forcing on a target with the
          NI Scan Engine installed.

                1.  Click a scan-enabled target in the system tree to display a target probe in the Auto
                View. You also can right-click a target and select Probe to display a target probe in a
                 separate window.
                2.  The Scan Engine page of a real-time target probe displays the Forcing Enabled LED
                   indicator, which indicates whether I/O variable forcing is enabled on the controller.
                3.  Use the Enable Forcing button to enable forcing. Use the Disable Forcing button to
                  disable forcing and unforce all forced I/O variable values. Use the Clear Forcing
                button to clear forcing on all I/O variables.

             NOTE
                             If you disable forcing and then enable forcing again, all previously-forced I/O
                   variables return to their last forced value, unless you have cleared those values
                  using the Clear Forcing button.


          Forcing I/O Variable Values

         Complete the following steps to force and unforce I/O variable values.

                1.  Click an I/O variable in the system tree to display an I/O variable probe in the Auto
              View or right-click an I/O variable and select Probe to display an I/O variable probe
                   in a separate window.
                2.  In the New Value section of the I/O variable probe, enter or select the new value for
                 the I/O variable.
                3.  Click the Force button to force the I/O variable to the value you specified.
                4.  Click the Unforce button to unforce the I/O variable value.

             NOTE
                   Individual I/O variable forcing applies only if forcing is enabled on the target. Use
                  the Enable Forcing and Disable Forcing buttons to enable and disable forcing on
                  the target.


         Batch Forcing I/O Variable Values

         Complete the following steps to perform batch forcing on a set of I/O variables.

                1.  Disable forcing on the target.
                2.  Force each I/O variable to the desired value.
                3.  Enable forcing on the target.


1816  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1816 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1817 ordinal=1817 -->
## LabVIEW User Manual

LabVIEW User Manual


I/O Servers

An I/O server is an application that communicates with and manages input and output
devices such as programmable logic controllers (PLCs), remote input/output devices,
remote Shared Variable Engines, and data acquisition (DAQ) plug-in devices. These I/O
servers read selected input items and write to the selected output items on demand.


Shortcut Menu

Right-click an I/O server on the system tree to display the following options.

    •   Watch List —Creates a new Watch List view that contains the single variable or
       multiple variables contained within the selected system or process.
    •   Probe —Displays the I/O Server Probe view for the selected system.
    •   Edit I/O Server —Configures the selected I/O server.
    •  Remove I/O Server —Removes the selected I/O server.

Observing Trend View of Variables

Use the Variable Probe view in the System Manager to monitor the value of a variable over
time using the trend view graph.

Complete the following steps to monitor the value of a variable over time using the trend
view graph.

   1.  Right-click a variable in the system tree.
   2.  Select Probe from the shortcut menu to open a new Variable Probe view for the
       selected variable.
   3.  Place a checkmark in the Show Trend checkbox to display the trend view graph.

Programmatically Accessing Published Values

You can access system tree objects such as shared or network variables from outside the
System Manager environment. Use the network path for a system tree object to access that
object from another environment.

The network path to shared or network variables consists of the system name, the name of
the process in which the shared variable resides, and the shared variable name: \
\system\process\variable. For example, the network path \
\system1\myprocess\myvariable identifies a shared variable named
myvariable in the process named myprocess on a system named system1.


                                                    © National Instruments Corporation 1817

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1817 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1818 ordinal=1818 -->
## LabVIEW User Manual

LabVIEW User Manual


         You can determine the network path using the Probe view for any system tree object. The
          Location field displays the network path for the selected object.

             NOTE
                   Refer to the LabVIEW Help, NI Measurement Studio Help, or LabWindows/CVI Help
                     for more information about accessing shared or network variables created or
                 modified with the System Manager from other applications.

      Saving and Restoring a System Manager Workspace

        When you customize the System Manager workspace, you can save the customized
         workspace and restore it in a later System Manager session.

         Complete the following steps to save and restore a customized System Manager
          workspace.

                1.  Customize the System Manager workspace.
                2.  Select File»Save Workspace to save your workspace as a .smw file.
                3.  To restore a workspace in a later session, select File»Open Workspace and navigate
                  to the .smw file you want to restore.

     Shared or Network Variables

         LabVIEW uses the term shared variable and Measurement Studio and LabWindows/CVI use
          the term network variable to describe software items that exist on a network and can
         communicate between programs, applications, remote computers, and hardware through
          the Shared Variable Engine (SVE). Variables can represent a value or an I/O point. The SVE
          uses the NI Publish-Subscribe Protocol (NI-PSP) data transfer protocol to write data and
          allow users to read live data. NI-PSP is a proprietary technology that provides fast and
            reliable data transmission for large and small applications and is installed as a service on
          the computer when you install LabVIEW, Measurement Studio, or LabWindows/CVI.

         Use the System Manager to create, modify, or delete shared or network variables. You also
         can monitor shared or network variables using the Watch List view.


          Shortcut Menu

            Right-click a variable on the system tree to display the following options.

                   •   Watch List —Creates a new Watch List view that contains the selected variable.
                   •   Probe —Displays the Variable Probe view for the selected system.
                   •   Edit Variable —Displays the Shared Variable Properties dialog box, which you can
                use to configure the selected variable.
                   •  Remove Variable —Removes the selected variable from the owning process.


1818  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1818 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1819 ordinal=1819 -->
## LabVIEW User Manual

LabVIEW User Manual


Shared Variable Engine

The Shared Variable Engine (SVE) uses the NI Publish-Subscribe Protocol (NI-PSP) to
enable the data transfer of shared or network variables through a network. The SVE
manages the use and connectivity of shared or network variables on single or multiple
systems.


Stopping Shared Variable Engine

Select Actions»Stop Local Shared Variable Engine to shut down the SVE. You can create,
configure, and remove variables in the System Manager after you shut down the SVE. While
the SVE is shut down, variable values do not update, and the SVE does not log alarms for
variables.

      NOTE
       You must use an alternate method to stop the Shared Variable Engine on Windows
         7/Vista.


Starting Shared Variable Engine

Select Actions»Start Local Shared Variable Engine to restart the SVE. The SVE is always
running after you install LabVIEW, LabWindows/CVI, or Measurement Studio unless you
select Actions»Stop Local Shared Variable Engine to manually shut down the SVE.

      NOTE
       You must use an alternate method to start the Shared Variable Engine on Windows
         7/Vista.

      RELATED INFORMATION
        Actions Menu on page 1813

Synchronizing Time for Networked Computers

Complete the following steps to set time synchronization.

   1.  Select View»Configure Time Servers to display the Shared Variable Engine Time
      Server Configuration dialog box.
   2.  Notice the Time server search order list. Any computer that is running the time
      synchronization service can serve as a time server or a time client. The primary time
       server is the first computer listed in the Time Server Search Order list. If no
      computer is set as a primary time server, the computer synchronizes to itself.
   3.  To add a computer to the Time server search order list, click the Add button to
       display the Select Computer dialog box.


                                                    © National Instruments Corporation 1819

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1819 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1820 ordinal=1820 -->
## LabVIEW User Manual

LabVIEW User Manual


                4.   If you know the name of the computer you want to add, you can type the name into
                 the Host text box. If you do not know the exact name of the computer, you can
               browse for the computer using the network tree in the Machines list. To remove a
               computer from the Time server search order list, select the computer name and
                    click the Remove button.
                5.  To change the order in which computers search for a time synchronization server,
                   select the computer name and click the Up or Down button.
                6.  Use Sleep time (seconds) to set how long each computer waits between each
                  synchronization. Set the primary time synchronization server sleep time to 60
                 seconds. If the primary server is off-line for some reason, a computer scheduled to
                 synchronize automatically seeks out the second computer on the synchronization
                  server list. At the time of the next synchronization, the computer first looks for the
                primary server before seeking a secondary synchronization server.
                7.  Click the OK button.
                8.  Repeat steps 4 through 7 for all computers on the network that you want to
                 synchronize to make sure that the order of search for time servers is the same for all
                 the computers, including the primary time synchronization server.

     Systems

          Systems are local computers or LabVIEW Real-Time targets available through the System
          Manager. Systems available on your local subnetwork appear by default. Select
          Actions»Add System to My Systems to access systems outside your local subnetwork that
         do not appear in the system tree.


          Shortcut Menu

            Right-click a system on the system tree to display the following options.

                   •  Add to My Systems —Moves a selected system listed in Network Items to My
              Systems on the system tree.
                   •  Remove From My Systems —Removes a selected system listed in My Systems.
                   •   Watch List —Creates a new Watch List view that contains the single variable or
                 multiple variables contained within the system or process that you select.
                   •   Probe —Displays the Systems Probe view, which displays the location address for
                 the selected system.
                   •  Add Process —Displays the Add Process dialog box.
                   •   Register Computer — Registers the selected system.
                   •   Unregister Computer — Unregisters the selected system.

       VI States

          Requires: Real-Time Module


1820  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1820 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1821 ordinal=1821 -->
## LabVIEW User Manual

LabVIEW User Manual


Select a real-time target to display a target probe in the Auto View. You also can right-click
the target and select Probe to display the probe in a separate window. Click the VI States
tab of a real-time target probe to display this view. Use this view to start, stop, and monitor
VIs on the real-time target.

This view includes the following components:

    •   Port —Specifies the TCP/IP port at which the VI server listens for requests on the
       real-time target. Right-click the real-time target in the Project Explorer window and
       select Properties from the shortcut menu to display the RT Target Properties
       dialog box. Select VI Server from the Category list to display the VI Server page,
      where you can configure the TCP/IP port for the VI Server.
    •   Update Interval —Sets the minimum time that the server waits between updates.
      The actual update interval might exceed the time you specify if higher priority tasks
      are running on the real-time target.
    •  Show Top Level VIs Only —Filters all subVIs from the list of real-time target VIs.
    •   Start Monitoring —Starts monitoring VIs on the real-time target.
    •   Stop Monitoring —Stops monitoring VIs on the real-time target.
    •   Start VI —Starts an idle VI that you select from the list of real-time target VIs.
    •   Stop VI —Stops a VI that you select from the list of real-time target VIs.

Viewing and Setting the Scan Engine Mode (NI
Scan Engine)

You can use the Scan Engine page of a target probe to view and set the scan engine mode
of a target with the NI Scan Engine installed.

Complete the following steps to view and set the scan engine mode.

   1.  Click a scan-enabled target in the system tree to display a target probe in the Auto
      View. You also can right-click a target and select Probe to display a target probe in a
      separate window.
   2.  The Scan Engine page of a target probe displays scan engine modes under the Scan
      Engine Enabled LED indicator and highlights the current scan engine mode with a
      green LED indicator.
   3.  Use the Change to Config button to set the scan engine mode to Config Mode or
      the Change to Active button to set the scan engine mode to Active Mode. You
      cannot enter Active Mode directly from Fault Mode. You must first clear all major
       faults on the target.

      NOTE
        Entering Config Mode from Fault Mode automatically converts all major faults to
       minor faults. You cannot enter fault mode manually. The target enters fault mode
       only when a major or unrecoverable fault occurs.


                                                    © National Instruments Corporation 1821

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1821 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1822 ordinal=1822 -->
## LabVIEW User Manual

LabVIEW User Manual


      Viewing and Clearing Faults (NI Scan Engine)

         You can view and clear faults on a target with the NI Scan Engine installed. Complete the
           following steps to view and clear faults.

                1.  Click a scan-enabled target in the system tree to display a target probe in the Auto
                View. You also can right-click a target and select Probe to display a target probe in a
                 separate window. The Scan Engine page of the target probe displays the faults
                  active on the target in a table that includes the fault code and description. The Fault
                Present LED indicator appears black when no fault is present, orange when only
               minor faults are present, and red when major or unrecoverable faults are present.
                2.  Click the Clear Faults button to clear all faults on the target.
                3.  To ensure that you successfully cleared all faults on the target, check the Fault
                Present LED indicator.

      Alarms and Events

      Acknowledging Alarms and Events

         You can acknowledge alarms and events that the Alarms and Events view displays by using
          the Acknowledge Selected Alarms and Events or Acknowledge All Alarms and Events dialog
           box.

             NOTE
              When you acknowledge an alarm, the alarm appears in purple as acknowledged in
                  the Alarms and Events view. When the alarm is no longer in the alarm state, the
                 alarm disappears from the Alarms and Events view. When you acknowledge an
                   event, the event disappears from the Alarms and Events view.

         Complete the following steps to acknowledge alarms or events by using the Alarms and
          Events view.

                1.  Select the alarms and events that you want to acknowledge. You can press the
                  <Ctrl> key and select multiple alarms and events.
                2.  Right-click a selected alarm or event and select Acknowledge from the shortcut
             menu to display the Acknowledge Selected Alarms and Events dialog box.
                3.  (Optional) Enter comments in the Comments text box.
                  NOTE
                   Comments apply to alarms only.
                4.  Click the OK button to acknowledge the selected items and close the dialog box.


1822  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1822 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1823 ordinal=1823 -->
## LabVIEW User Manual

LabVIEW User Manual


      NOTE
       To acknowledge all the alarms and events at one time, you can right-click in this
       view and select Acknowledge All from the shortcut menu to display the
      Acknowledge All Alarms and Events dialog box. Then, complete steps 3 and 4 to
       acknowledge all alarms and events in this view.

Alarm Probe View

Requires: DSC Module

In the system tree pane, right-click an alarm and select Probe to display this view. This
view shows the status and properties of the selected alarm.

This view includes the following components:

    •   Location —Displays the location of the alarm.
    •   Status —Displays the status of the alarm.
    •   Priority —Displays the priority of the alarm.
    •   Level —Displays the level of the alarm.
    •   Description —Displays the description of the alarm.

Alarms and Events View

Requires: NI Distributed System Manager (Windows)

Select View»Alarms and Events to display or hide the Alarms and Events view. The NI
Distributed System Manager supports only one Alarms and Events view.

Use the Alarms and Events view to monitor and acknowledge alarms and events. You can
view alarms and events of other processes by using the Select Processes dialog box. By
default, the Alarms and Events view displays alarms and events of systems in My
Systems. You can add a system to My Systems to access systems that do not appear in the
system tree pane.

      NOTE
       You must have the LabVIEW Datalogging and Supervisory Control (DSC) Module
        installed to monitor and acknowledge alarms.

This view includes the following components:

    •   Select Processes —Displays the Select Processes dialog box, which you use to
       select multiple processes from the system tree pane. The Alarms and Events view
      then displays alarms and events that these processes generate.
    •  Show Alarms —Specifies whether to display alarms in the Alarms and Events view.
      By default, this checkbox contains a checkmark.


                                                    © National Instruments Corporation 1823

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1823 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1824 ordinal=1824 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •  Show Events —Specifies whether to display events in the Alarms and Events view.
               By default, this checkbox contains a checkmark.
                   •   Acknowledge —Displays the Acknowledge Selected Alarms and Events dialog box,
               which you use to acknowledge alarms and events you select in the Alarms and
               Events view.
                   •   Acknowledge All —Displays the Acknowledge All Alarms and Events dialog box,
               which you use to acknowledge all alarms and events in the Alarms and Events
                  view.
                   •    Filter —Displays the Filter Options dialog box, which you use to display alarms and
                 events that meet certain criteria.
                   •   Columns —Displays the Show Columns dialog box, which you use to show or hide
               columns in the Alarms and Events view.

       Alerts Probe View

          Requires: Real-Time Module

           Select a real-time target to display a target probe in the Auto View. You also can right-click
          the target and select Probe to display the probe in a separate window. Click the Alerts tab
           of a real-time target probe to display this view. Use this view to configure and monitor
            alerts on the real-time target.

           This view includes the following components:

                   •   Log Alert when memory usage is above —Enables alert logging when memory
                usage on the real-time target exceeds the value you specify.
                   •   Log Alert when CPU usage is above —Enables alert logging when the real-time
                  target CPU usage exceeds the value you specify.
                   •   Log Alert when VI changes state —Enables alert logging when a VI listed in the VI
                 States view changes state.
                   •   Recent Alerts —Lists recently-logged alerts.
                   •   Clear —Removes all entries from the Recent Alerts list.
                   •   Save —Saves the Recent Alerts list as a text file on the local computer.

     CPU/Memory Probe View

          Requires: NI Scan Engine

           Select a real-time target to display a target probe in the Auto View. You also can right-click
          the target and select Probe to display the probe in a separate window. Click the CPU/
        Memory tab of a real-time target probe to display this view. Use this view to monitor CPU
         and memory usage on the target.

           This view includes the following components:


1824  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1824 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1825 ordinal=1825 -->
## LabVIEW User Manual

LabVIEW User Manual


    •  CPU N Usage Chart (%) —Tracks utilization of CPU N over time, as a percentage of
       capacity.
    •  Memory Usage Chart (MB) —Tracks target memory usage over time.
    •  CPU N Statistics —Includes current CPU usage statistics including total CPU usage,
     CPU usage by priority level, and CPU usage dedicated to Timed Structures and
       interrupt service routines (ISRs). Each value represents a percentage of total
       capacity.
    •  Memory Statistics —Displays current memory usage data.
            ◦   Allocated —The amount of memory, in MB, currently allocated on the target.
            ◦   Available —The amount of memory, in MB, currently available on the target.
            ◦   Contiguous —The largest contiguous block of available memory on the
               target, in MB.
            ◦   Total —The total amount of memory available to the operating system, in
           MB.
            ◦   Usage —The percentage of total memory currently allocated on the target.

Date Time Probe View

Requires: NI Distributed System Manager

Select a system from the system tree to display the system in the Auto View. You also can
right-click the system and select Probe to display the Probe view in a separate window.
Click the Date Time tab of a system probe to display this view. Use this view to set the date
and time on the system. Date Time only appears for systems that you have sufficient
privileges to modify the date and time settings.

This view includes the following components:

    •   Local System Time (UTC) —Displays the time on the current system running NI
       Distributed System Manager.
    •   Target System Time (UTC) —Displays the time on the selected target system
      displayed in the Probe view or Auto View.
    •   Set to local —Assigns the value of the Target System Time (UTC) to the value of the
      Local System Time (UTC). Use this button to sync times between the system
      running NI Distributed System Manager and the system displayed in the Probe view
       or Auto View.
    •   Refresh —Refreshes the values that appear in Local System Time (UTC) and Target
     System Time (UTC).

I/O Variable Probe View

Requires: NI Scan Engine

Click an I/O variable in the system tree to display this view in the Auto View. You also can
right-click an I/O variable and select Probe to display this view in a separate window.


                                                    © National Instruments Corporation 1825

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1825 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1826 ordinal=1826 -->
## LabVIEW User Manual

LabVIEW User Manual


           This view displays the location of an I/O variable and allows you to view or customize the
           following components:

                   •   Location —Specifies the location of the item you want to probe. To probe a variable,
                    for example, enter the information in the following format: //SystemName/
             Process/Variable.
                   •   Current Value —Displays the current value of the selected variable.
                   •  New Value —Allows you to enter a new value to assign to the variable.
                   •   Force — Forces the variable to assume New Value until you unforce the variable,
                reboot the target, or force the variable to assume another New Value.
                   •   Unforce —Stops forcing the variable and returns control of the I/O value to the scan
                 engine.
                   •   Set —Sets the value in the New Value field as the current value.
                   •  Show Trend —Displays the trend view graph of the selected variable.
                   •   Data Type —Displays the data type of the selected variable.
                   •   Timestamp —Displays the timestamp of the selected variable.
                   •   Quality —Displays the quality of the selected variable. The quality indicates errors
                 or other conditions that apply to the variable.
                   •   Access Type —Displays the supported access mode(s) of the variable. This includes
                 Read-only, Write-only, or Read/Write. LabVIEW modules and toolkits you have
                   installed might provide additional access types.

     OpenCSRs Probe View

          Requires: NI Distributed System Manager (Windows)

            Right-click OpenCSRs and select Probe from the shortcut menu to display this view. This
          view displays open certificate signing requests available on the Web Server. You can create
        new CSRs, display or delete existing CSRs, and install digitally signed certificates that
          correspond to an open CSR.

           This view includes the following components:

                   •  Open Certificate Signing Requests —Displays open CSRs on the Web Server.
                   •   Create —Launches the Create a Certificate Signing Request dialog box.
                   •   Delete —Deletes the selected CSR.
                   •  Show —Displays the value of the selected CSR.
                   •    Install —Displays the text field to paste the signed certificate returned by the
                    certificate authority (CA).

           Refer to the LabVIEW Help for information about enabling SSL on the LabVIEW Web Server.


1826  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1826 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1827 ordinal=1827 -->
## LabVIEW User Manual

LabVIEW User Manual


Process Probe View

Requires: NI Distributed System Manager (Windows)

Right-click a process and select Probe from the shortcut menu to display this view. This
view shows the status of the selected process and allows you to start or stop that process.

This view includes the following components:

    •   Location —Displays the location of the selected process.
    •   State —Displays whether the process is online or offline, or displays if you do not
      have sufficient access privileges to modify the state.
    •   Start Process —Starts the selected process. You must have sufficient access
       privileges to start a process.
    •   Stop Process —Stops the selected process. You must have sufficient access
       privileges to stop a process.

Scan Engine Probe View

Requires: NI Scan Engine

Select a target with the NI Scan Engine installed to display this view in the Auto View. You
also can right-click the target and select Probe to display this view in a separate window.
Use this view to monitor and manage the scan engine running on the target.

This view includes the following components:

    •   Forcing —Contains information and options related to I/O variable forcing.
          NOTE
              Forcing does not persist after a reboot of the target.

            ◦   Forcing Enabled —Indicates whether forcing is enabled on the target.
             Forcing must be enabled on the target for individual I/O variable or I/O alias
              forces to take effect. This setting serves as a master switch for all I/O variable
           and I/O alias forcing on the target.
            ◦   Enable Forcing —Enables forcing on the target, switching the state of the
            Forcing Enabled setting to TRUE. This option is available only when I/O
              variable forcing is disabled.
            ◦   Disable Forcing —Disables forcing on the target, switching the state of the
            Forcing Enabled setting to FALSE. This option is available only when I/O
              variable forcing is enabled.
               NOTE
                    Unless you clear forcing, the previous forced values of all forced I/O
                      variables and I/O aliases return when you re-enable forcing on the
                       target.


                                                    © National Instruments Corporation 1827

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1827 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1828 ordinal=1828 -->
## LabVIEW User Manual

LabVIEW User Manual


                         ◦   Clear Forcing —Unforces all currently forced I/O variables and I/O aliases on
                       the target and returns control of the I/O values to the NI Scan Engine.
                       NOTE
                                This button does not affect the master Forcing Enabled setting on
                              the target.
                   •   Faults —Contains information and options related to scan engine faults.
                         ◦   Fault Present —Indicates the presence of faults on the target. The LED
                      appears black when no fault is present, orange when only minor faults are
                        present, and red when major or unrecoverable faults are present.
                         ◦   Clear All Faults —Clears all faults on the target. If the target is in Fault mode,
                         clearing all faults returns the target to the previous mode in effect before
                        entering Fault Mode.
                         ◦   Clear Selected Fault —Clears the fault currently selected in the Fault List. If
                   no fault is currently selected, no action occurs.
                         ◦   Fault List —Lists the faults active on the target.
                                 ▪   Error Code —The error code associated with the fault.
                                 ▪   Highest Level —The highest level of the fault since last cleared.
                                 ▪   First Occurrence —The time of the first occurrence of the fault since
                                    last cleared.
                                 ▪  Num of Occurrences —The number of occurrences of the fault since
                                    last cleared.
                                 ▪   Description —The fault description.
                   •   Scan Engine Mode —Contains information and options related to the mode of the
                 NI Scan Engine on the target.
                  NOTE
                         This section is available only with expansion I/O hardware. This section is
                       not available if only local I/O drivers are installed on the target. Refer to the
                          I/O hardware documentation for information about hardware-specific
                  mode behavior.

                         ◦   Configuration —Indicates whether the scan engine is in Configuration mode.
                         ◦   Active —Indicates whether the scan engine is in Active mode.
                         ◦   Fault —Indicates whether the scan engine is in Fault mode.
                         ◦   I/O Drivers —Lists the I/O drivers installed on the target that interface with
                       the NI Scan Engine.
                         ◦  Change to Configuration —Switches the scan engine to Configuration
                    mode. If the target was previously in Fault mode, switching to Configuration
                 mode automatically changes the level of all active major faults to minor.
                         ◦  Change to Active —Switches the scan engine to Active mode. You cannot
                       switch directly to Active mode from Fault mode. You must clear all major
                           faults to leave Fault mode before you can switch to Active mode.
                   •   Refresh Local Modules —Discovers new I/O modules on the target. If a local I/O
              module is detected in a slot that was not previously deployed from a LabVIEW
                   project, this operation creates new I/O variables for the I/O module. These
                 automatically created I/O variables use the default I/O variable settings. This


1828  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1828 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1829 ordinal=1829 -->
## LabVIEW User Manual

LabVIEW User Manual


      operation does not add the new I/O variables to a LabVIEW project, and the new I/O
       variables do not persist when the target restarts. If you physically change an I/O
     module deployed from a LabVIEW project, this operation cannot overwrite the
      deployed configuration until you undeploy the I/O module in the LabVIEW project.
      However, if you physically change an I/O module that was automatically detected
      by this operation or the corresponding Refresh Local Modules VI, this operation
      adds and deletes automatically created I/O variables to match the new physical
       configuration.

ServerCertificates Probe View

Requires: NI Distributed System Manager (Windows)

Right-click ServerCertificates and select Probe from the shortcut menu to display this
view. This view displays self-signed certificates available on the Web Server, including the
default LabVIEW self-signed certificate. You can create a new self-signed certificate and
display or delete existing self-signed certificates.

This view includes the following components:

    •   Server Certificates —Displays self-signed certificates on the Web Server.
    •   Create —Launches the Create a Self-Signed Certificate dialog box.
    •   Delete —Deletes the selected self-signed certificate.
    •  Show —Displays the value of the selected self-signed certificate.

Refer to the LabVIEW Help for information about enabling SSL on the LabVIEW Web Server
and the default LabVIEW self-signed certificate.

Variable Probe View

Requires: NI Distributed System Manager (Windows)

Right-click a variable and select Probe from the shortcut menu to display this view. This
view displays the location of the selected shared or network variable and allows you to
view or customize aspects of that variable.

This view includes the following components:

    •   Location —Displays the location of the selected variable.
    •   Current Value —Displays the current value of the selected variable.
    •  New Value —Allows you to enter a new value to assign to the variable.
    •   Set —Sets the value in the New Value field as the current value.
    •  Show Trend —Displays the trend view graph of the selected variable.
    •   Data Type —Displays the data type of the selected variable.


                                                    © National Instruments Corporation 1829

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1829 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1830 ordinal=1830 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Timestamp —Displays the timestamp of the selected variable.
                   •   Quality —Displays the quality of the selected variable. The quality indicates errors
                 or other conditions that apply to the variable.
                   •   Access Type —Displays the supported access mode(s) of the variable. This includes
                 Read-only, Write-only, or Read/Write. LabVIEW modules and toolkits you have
                   installed might provide additional access types.

     Web Server Probe View

          Requires: NI Distributed System Manager (Windows)

            Right-click a Web Server and select Probe from the shortcut menu to display this view. This
          view displays Web services available on the Web Server. You can pause, resume, restart,
            delete, or reset statistics for one or all of the available Web services. Refer to the LabVIEW
          Help for information about LabVIEW Web services and related terminology.

           This view includes the following components:

                   •   Location —Displays the location of the selected Web Server.
                   •   Deployed Web Services —Displays a listbox of all Web services available on the
            Web Server.
                         ◦   Operations on selected —Displays components that perform operations on
                       the selected Web service.
                                 ▪   Pause —Pauses the selected Web service.
                                 ▪  Resume —Resumes the selected Web service.
                                 ▪   Restart —Restarts the selected Web service.
                                 ▪   Reset Statistics —Resets all statistical variables for the selected Web
                                  service.
                                 ▪   Delete —Removes the selected Web service from the Web Server.
                   •   Operations on all —Displays components that perform operations on all Web
                  services on the Web Server.
                         ◦   Pause All —Pauses all Web services on the Web Server.
                         ◦  Resume All —Resumes all Web services on the Web Server.
                         ◦   Restart All —Restarts all Web services on the Web Server.
                         ◦   Reset All Statistics —Resets statistical variables for all Web services on the
                 Web Server.

     Web Server URL Mapping View

          Requires: NI Distributed System Manager (Windows)

           Select a URL mapping and click the Run Selected button on the Web Server Probe view to
           display this view. This view allows you to assign values to connector pane inputs of the


1830  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1830 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1831 ordinal=1831 -->
## LabVIEW User Manual

LabVIEW User Manual


Web method VI specified by the selected URL mapping. You then can send an HTTP request
with these values to the Web method VI. Refer to the LabVIEW Help for information about
LabVIEW Web services and related terminology.

This view includes the following components:

    •   Parameters —Displays available connector pane inputs for the Web method VI
      associated with the selected URL mapping. You must assign connector pane inputs
      before you send an HTTP request to the Web method VI.
    •   Values —Specifies values for the connector pane inputs of the Web method VI
      associated with the selected URL mapping.
    •   Results —Displays the response from the Web service after you send an HTTP
       request.
    •   Host —Displays the computer name of the Web Server running the selected Web
       service.
    •   Port —Displays the port of the Web Server interface running the selected Web
       service.
    •   Request —Displays the complete URL mapping for the HTTP request.
    •   Send request —Sends an HTTP request to the Web method VI associated with the
       selected URL mapping. You must specify Values for the connector pane inputs of
      the Web method VI before you send an HTTP request.

Web Service Probe View

Requires: NI Distributed System Manager (Windows)

Right-click a Web service and select Probe from the shortcut menu to display this view.
This view displays the state of the selected Web service and allows you to pause, resume,
restart, or reset statistics for the Web service. You also can send HTTP requests to the Web
service using available URL mappings. Refer to the LabVIEW Help for information about
LabVIEW Web services and related terminology.

This view includes the following components:

    •   Location —Displays the location of the selected Web Service.
    •   State —Displays whether the Web service is running or paused.
    •   Pause —Pauses the selected Web service.
    •  Resume —Resumes the selected Web service.
    •   Restart —Restarts the selected Web service.
    •   Reset Statistics —Resets all statistical variables for the selected Web service.
    •  URL Mappings —Displays a listbox of available URL Mappings for the selected Web
       service.
            ◦  Run Selected —Displays the Web Server URL Mapping view for the selected
          URL mapping.


                                                    © National Instruments Corporation 1831

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1831 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1832 ordinal=1832 -->
## LabVIEW User Manual

LabVIEW User Manual


      Configure Web Services Security View

          Requires: NI Distributed System Manager (Windows)

            Right-click a Web Server in the system tree and select Web Services Security from the
           shortcut menu to display this dialog box. Use this dialog box to configure security for
         LabVIEW Web services. Refer to the LabVIEW Help for information about LabVIEW Web
           services security and related terminology.

           This view includes the following components:

                   •  Web Services security key —Configures the API key used for Web services security.
                         ◦   Access ID —Specifies the public ID component of the API key. The Access ID
                     works similarly to a username.
                         ◦   Secret ID —Specifies the private ID component of the API key. The Secret ID
                     works similarly to a password and only authorized clients should possess
                           this string.
                         ◦   Paste from Clipboard —Pastes an API key located on the clipboard into the
                      Access ID and Secret ID fields. If the content of the clipboard does not
                     conform to the correct format of an API key, the content of the clipboard
                     does not import and the current Access ID and Secret ID remain.
                         ◦   Reset —Resets the Access ID and Secret ID.

       Configuring Alarms for Shared Variables (DSC Module)

         Complete the following steps to configure alarms for shared variables.

                1.  In the system tree pane, locate the alarm you want to configure and expand this
                 alarm. The System Manager displays the attributes of the alarm.
                2.  Right-click the attribute you want to configure and select Probe from theshortcut
              menu. A Probe view of the attribute appears.
                3.  Specify a new value of the attribute in the New Value text box or option buttons to
                 configure this attribute.
                  NOTE
                      You cannot configure the alarm statuses, such as Ack, Description, and Set.
                4.  Click the Set button to set the new value of the attribute.

             NOTE
                You also can configure alarms by using the Auto View.


1832  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1832 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1833 ordinal=1833 -->
## LabVIEW User Manual

LabVIEW User Manual


Monitoring Alarms and Events

Use the Alarms and Events view to monitor alarms and events. Complete the following
steps to monitor alarms and events by using the Alarms and Events view.

   1.  Locate the Alarms and Events view. If you do not see this view, select View»Alarms
     and Events to display this view.
   2.  (Optional) Configure the filter options to display alarms, events, or both alarms and
      events in this view.
   3.  Click the Select Processes button to display the Select Processes dialog box. You
       also can display this dialog box by right-clicking in the Alarms and Events view and
       selecting Select Processes from the shortcut menu.
   4.  In the Available Processes list, select the processes you want to monitor. Press and
      hold the <Shift-Ctrl> keys to select multiple processes from the list.
   5.  Click the Add button to add this process to the Selected Processes list.
          NOTE
            You can select a process from the Selected Processes list and click the
           Remove button to remove the process from this list. You also can click the
              Clear button to remove all processes from this list.
   6.  Repeat steps 4 and 5 to add all the processes that you want to monitor to the
      Selected Processes list.
   7.  Click the OK button to close the Select Processes dialog box.

The Alarms and Events view displays alarms and events that the selected processes
generate. You can acknowledge these alarms and events by using the Alarms and Events
view.

Monitoring and Editing Data Item Ranges

Complete the following steps to monitor and edit data items by using the Probe view or
Auto View.

      NOTE
       You cannot monitor or edit extended data items or array data items in the NI
       System Manager.

   1.  In the system tree, right-click a data item range and select Probe from the shortcut
     menu to create a Probe view. The Probe view displays detailed information about
      the data item range.
   2.  In the Change item text box, enter the data item that you want to monitor or edit.
   3.  Click the Apply button to display the value of the data item.
   4.  Enter the new value of the data item in the New Value section.
   5.  Click the Set button to apply the new value to the data item.


                                                    © National Instruments Corporation 1833

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1833 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1834 ordinal=1834 -->
## LabVIEW User Manual

LabVIEW User Manual


             NOTE
                You also can click the Auto View to display the detailed information.

       Monitoring Data Items in Data Item Ranges

         Complete the following steps to create a new Watch List view for data item ranges or add a
          data item range to an existing Watch List view.

                1.  In the system tree, right-click a data item range and select Watch List from the
                 shortcut menu. The System Manager displays the Add Item to Watch List dialog
                 box. You also can drag a data item to an existing Watch List view to display this
                  dialog box.
                2.  In the Items from range text box, enter the data item to monitor.
                3.  Click the OK button to create a watch list for the data item.

             NOTE
                You can create a Watch List view for multiple data item ranges or multiple system
                   tree objects that include data item ranges. You also can add these system tree
                   objects to an existing Watch List view. When you create a Watch List view for these
                 system tree objects or add these system tree objects to an existing Watch List
                   view, the Add Item to Watch List dialog box does not appear. The System Manager
                adds the first data items of the data item ranges by default.

       Monitoring Variables with the Watch List View

         The Watch List view displays information about a single variable or multiple variables
          contained within a system or process. The Watch List view displays the variable location,
           current value, data type, timestamp, access (read/write) status, and quality. The quality
           indicates errors or other conditions that apply to the variable.

             NOTE
                   Variables that use the array and cluster data type do not display the values of
                   individual components.

         Complete the following steps to monitor variables using the Watch List view.

                1.  Right-click a system tree object, which includes all systems, processes, and variables
                  available in the system tree.
                2.  Select Watch List from the shortcut menu to open a new Watch List view.
                3.  To customize the Watch List view, right-click anywhere inside the Watch List view.
                4.  Select Show Columns from the shortcut menu to show and hide any of the
                 information columns available in the Watch List view. You also can reorder the
               columns by dragging the column headings.


1834  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1834 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1835 ordinal=1835 -->
## LabVIEW User Manual

LabVIEW User Manual


Creating Certificates and Processes

Creating a Certificate from a CSR

After you create a certificate signing request (CSR), you must have the CSR digitally signed
by a trusted certificate authority (CA) in order to create a certificate.

Complete the following steps to create a certificate from a CSR.

   1.  Create a CSR.
   2.  In System Manager, expand the tree item for the system, such as localhost.
   3.  Expand the item NI_SSLConfiguration.
   4.  Expand the item OpenCSRs.
   5.  Select a CSR from the tree, such as Request Handle-100.
   6.  Copy the text from the Certificate Signing Request field of the OpenCSRs Probe
      view for the item. If the OpenCSRs Probe view does not appear, right-click the CSR
     and select Probe from the shortcut menu.
   7.  Send the text to a trusted CA that can digitally sign the CSR. If you do not have a
       trusted CA to sign the request, you also can create a self-signed certificate rather
      than using a CSR and a CA.
   8.  When a CA returns a signed certificate, right-click the CSR from the tree and select
       Install from the shortcut menu.
   9.  Paste the character string provided by the CA into the text box.
   10. Click the Install button.

If the installation is successful, a new certificate with the same name as the CSR appears
under the ServerCertificates item in the tree. The System Manager automatically deletes
the CSR from both the tree and the file system.

Creating a Certificate Signing Request

You can create a certificate signing request (CSR) using the System Manager.

Complete the following steps to create a CSR in the System Manager.

   1.  Enable SSL on an instance of the LabVIEW Web Server. Refer to the LabVIEW Help for
      information about enabling SSL on the LabVIEW Web Server.
   2.  Expand the tree item for a system, such as localhost.
   3.  Expand the item NI_SSLConfiguration.
   4.  Right-click OpenCSRs from the tree and select Probe from the shortcut menu to
       display the OpenCSRs Probe view.


                                                    © National Instruments Corporation 1835

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1835 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1836 ordinal=1836 -->
## LabVIEW User Manual

LabVIEW User Manual


                5.  In the OpenCSRs Probe view, click the Create button to display the Create a
                   Certificate Signing Request dialog box.
                6.  In the Create a Certificate Signing Request dialog box, enter the appropriate
                   identifying information into the Values column.
                7.  Click the Submit button. If you experience errors, confirm that the identifying
                 information uses the correct syntax.

         The dialog box displays the name and character string for the new CSR. You must send this
           character string to a trusted CA to create a certificate from the CSR.

              RELATED INFORMATION
                  Create a Certificate Signing Request Dialog Box

       Creating a Self-Signed Certificate

         You can create a custom self-signed certificate using the System Manager. You can use this
           self-signed certificate in place of the default LabVIEW self-signed certificate.

         Complete the following steps to create a custom self-signed certificate in the System
          Manager.

                1.  Enable SSL on an instance of the LabVIEW Web Server. Refer to the LabVIEW Help for
                 information about enabling SSL on the LabVIEW Web Server.
                2.  Expand the tree item for a system, such as localhost.
                3.  Expand the item NI_SSLConfiguration.
                4.  Right-click ServerCertificates from the tree and select Probe from the shortcut
             menu to display the ServerCertificates Probe view.
                5.  In the ServerCertificates Probe view, click the Create button to display the Create
              a Self-Signed Certificate dialog box.
                  NOTE
                     The default LabVIEW self-signed certificate appears as Certificate
                  Handle-0 in the tree. All custom self-signed certificates that you create
                         are assigned a subsequent number starting at 100, such as Certificate
                   Handle-100.
                6.  In the Create a Self-Signed Certificate dialog box, enter the appropriate
                   identifying information into the Values column.
                7.  Select the duration of the certificate in the Valid for how many days? option.
                8.  Click the Submit button. If you experience errors, confirm that the identifying
                 information uses the correct syntax.

         The dialog box displays the name and public key for the new certificate. The certificate also
          appears in the tree under the ServerCertificates item.


1836  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1836 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1837 ordinal=1837 -->
## LabVIEW User Manual

LabVIEW User Manual


Creating Processes

You can create processes on a local or LabVIEW Real-Time target.

Complete the following steps to create a process with the System Manager.

   1.  Right-click a system in the system tree.
   2.  Select Add Process from the shortcut menu to display the Add Process dialog box.
   3.  Configure the process in the Add Process dialog box. You can use this dialog box to
       configure the process name and whether the process will run after you create it.

After you create a process, you can add shared or network variables or add I/O servers to
that process.

      RELATED INFORMATION
       Processes on page 1841
       Systems on page 1820
        Creating, Modifying, or Deleting Shared or Network Variables on page 1837
        I/O Servers on page 1817

Creating, Modifying, or Deleting Shared or Network
Variables

You can create shared or network variables within processes on a local or real-time target.

Complete the following steps to create a variable with the System Manager.

   1.  Select an existing process in the system tree or create a new process.
   2.  Right-click the process and select Add Variable from the shortcut menu to display
      the Shared Variable Properties dialog box.
   3.  Configure the variable in the Shared Variable Properties dialog box. You can use
       this dialog box to configure settings such as the variable name, data type, and
       buffering.

You now can use the variable in an application. When the process is running, the Watch List
view updates to include information about the variable such as current value, timestamp,
and quality messages. Quality messages list errors and other conditions that apply to the
variable.


                                                    © National Instruments Corporation 1837

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1837 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1838 ordinal=1838 -->
## LabVIEW User Manual

LabVIEW User Manual


          Modifying a Shared or Network Variable

            Right-click the variable in the system tree and select Edit Variable from the shortcut menu
           to display the Shared Variable Properties dialog box.


          Deleting a Shared or Network Variable

            Right-click the variable in the system tree and select Remove Variable from the shortcut
         menu.

     Custom VI-based Server - On Input Change Wizard

          Requires: DSC Module

            Click the New button on the Configure Custom VI - On Input Change I/O Server dialog box
           to display this wizard. You also can select Tools»DSC Module»VI Based Server Wizard»On
          Input Change in LabVIEW to display this wizard.

           This wizard includes the following pages:

                   •   Select VI —Use this page to specify a VI you want to convert into an I/O server.
                 Contains the following options:
                         ◦   Path to VI —Specifies the path to the VI that you want to convert to a custom
                         I/O server.
                         ◦  Run VI Analyzer on VI —Displays the LabVIEW VI Analyzer Toolkit, which runs
                           tests that can identify improvements you can make to the VI. You must have
                       the LabVIEW VI Analyzer Toolkit installed to use this option.
                   •   Configure Server Distribution Component —Specifies build options for the I/O
                   server. Contains the following options:
                         ◦   Configuration name —Specifies the name of the configuration for the
                    custom I/O server. You can have multiple configurations for each custom I/O
                          server. The default name is the name of the VI converted to a custom I/O
                          server.
                         ◦   Support files —Lists additional VIs you want to include in the LabVIEW
                         project library to deploy. The wizard automatically includes any subVIs or
                       other files that are in the VI hierarchy. You only need to add dynamically
                         called VIs or files.
                         ◦   Select Support File —Specifies the path to the support files needed to run
                       the VI-based server. Click the Browse button to navigate to and select the
                      support files. You must select a file before you can click the Add button to
                    add the file to the Support files list.
                         ◦  Add —Adds the VI or file to the Support files list.
                         ◦  Remove —Removes the VI or file you select in the Support files list.
                   •   Server Distribution Component —Displays a summary of the server the Custom VI-
               based Server - On Input Change Wizard builds and allows you to build the server.
                 Contains the following options:


1838  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1838 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1839 ordinal=1839 -->
## LabVIEW User Manual

LabVIEW User Manual


            ◦   Server configuration file —Specifies the path to the VI that the wizard
             converts to a custom I/O server.
            ◦   Server support files directory —Specifies the path to the files created when
             the wizard converts the VI to a custom I/O server.

Click the Build button to build the on input change I/O server. When the Custom VI Server -
On Input Change Wizard generates the files, you can open the Configure Custom VI - On
Input Change I/O Server dialog box to configure the I/O server.

      RELATED INFORMATION
       Configure Custom VI - On Input Change I/O Server Dialog Box

Custom VI-based Server - Periodic Wizard

Requires: DSC Module

Click the New button on the Configure Custom VI - Periodic I/O Server dialog box to launch
the Custom VI Server - Periodic Wizard. You also can select Tools»DSC Module»VI Based
Server Wizard»Periodic to launch this dialog box. Use this wizard to create a custom VI-
based periodic I/O server.

This wizard includes the following pages:

    •   Select VI —Use this page to specify a VI you want to convert into an I/O server.
      Contains the following options:
            ◦   Path to VI —Specifies the path to the VI that you want to convert to a custom
              I/O server.
            ◦  Run VI Analyzer on VI —Displays the LabVIEW VI Analyzer Toolkit, which runs
               tests that can identify improvements you can make to the VI. You must have
             the LabVIEW VI Analyzer Toolkit installed to use this option.
    •   Select Controls and Indicators To Publish —Specifies the controls and indicators
       of the VI for which you want to publish values. Contains the following options:
            ◦   Controls —Lists the controls on the VI you can select to convert to a custom
              I/O server.
            ◦   Select All —Selects all of the controls or indicators on the VI.
            ◦   Deselect All —Deselects all of the controls or indicators on the VI.
            ◦   Indicators —Lists the indicators on the VI you can select to convert to a
           custom I/O server.
            ◦   Select All —Selects all of the controls or indicators on the VI.
            ◦   Deselect All —Deselects all of the controls or indicators on the VI.
    •   Select Method To Stop The Server —Specifies a mechanism to stop the periodic
       I/O server. Contains the following options:
            ◦   Abort VI —Configures the custom I/O server to abort the VI.


                                                    © National Instruments Corporation 1839

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1839 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1840 ordinal=1840 -->
## LabVIEW User Manual

LabVIEW User Manual


                         ◦   Stop the following While Loops —Configures the custom I/O server to use
                       the While Loop you select to stop running the VI. Contains the following
                         options:
                                 ▪   While Loops —Lists the While Loops available to stop the VI.
                                 ▪   View on block diagram —Opens the block diagram from which you
                           can select a While Loop to stop the VI.
                                 ▪   Timeout —Specifies the amount of time, in milliseconds, you want
                             the VI to wait before timing out.
                   •   Configure Server Distribution Component —Specifies build options for the I/O
                   server. Contains the following options:
                         ◦   Configuration name —Specifies the name of the configuration for the
                    custom I/O server. You can have multiple configurations for each custom I/O
                          server. The default name is the name of the VI converted to a custom I/O
                          server.
                         ◦   Support files —Lists additional VIs you want to include in the LabVIEW
                         project library to deploy. The wizard automatically includes any subVIs or
                       other files that are in the VI hierarchy. You only need to add dynamically
                         called VIs or files.
                         ◦   Select Support File —Specifies the path to the support files needed to run
                       the VI-based server. Click the Browse button to navigate to and select the
                      support files. You must select a file before you can click the Add button to
                    add the file to the Support files list.
                         ◦  Add —Adds the VI or file to the Support files list.
                         ◦  Remove —Removes the VI or file you select in the Support files list.
                   •   Server Distribution Component —Displays a summary of the files the Custom VI
                 Server - Periodic Assistant builds. Contains the following options:
                         ◦   Server configuration file —Specifies the path to the VI that the wizard
                        converts to a custom I/O server.
                         ◦   Server template file —Specifies the path to the template file created when
                       the wizard converts the VI to a custom I/O server.
                         ◦   Server support files directory —Specifies the path to the files created when
                       the wizard converts the VI to a custom I/O server.

            Click the Build button to build the periodic I/O server. When LabVIEW generates the files,
         you can edit the configuration and set initial values for the I/O server in the Configure
        Custom VI - Periodic I/O Server dialog box.

              RELATED INFORMATION
                  Configure Custom VI - On Input Change I/O Server Dialog Box

      Customizing the System Manager Workspace

         The System Manager allows you to customize the workspace. Most System Manager views
          appear as a window by default. You can dock these views on the workspace to build a
         custom work environment.


1840  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1840 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1841 ordinal=1841 -->
## LabVIEW User Manual

LabVIEW User Manual


Complete the following steps to customize the System Manager workspace.

   1.  Open a new view, such as a Watch List or Event Window view.
   2.  Click and hold the top bar of the desired view window.
   3.  Drag the window to the top, bottom, or sides of the System Manager workspace to
      dock the window.
          NOTE
                       If you dock multiple views in an area of the workspace, the System Manager
              automatically adds tabs to allow navigation between the views.

   4.  To undock a view to a separate window, select the Restore Down button    in the
       top-right of the view.
          NOTE
               Select View»Auto View to display the Variable Details view for the selected
             system tree object. The Variable Details view appears docked by default
           when you select Auto View.
   5.  Select File»Save Workspace to save the workspace as a .smw file.
   6.  Select File»Open Workspace and navigate to a .smw file to restore a previously
      customized workspace.

Processes

Processes are hierarchies of shared or network variables and I/O servers. Processes
provide a logical means of organizing data. For example, if multiple, independent
applications run on one server, you can create a process for each application. Similarly, if
you have a very large application, you might divide the application into discrete
subsystems and create a process for each subsystem. In addition to organizing data, you
can start and stop each process independently, which allows you to take one subsystem
offline while the rest of the application continues to run. When you stop a process, the
values of variables in that process become unavailable and do not update.

Use the System Manager to create processes and start and stop existing processes.


Shortcut Menu

Right-click a process on the system tree to display the following options.

    •   Watch List —Creates a new Watch List view that displays the information for all
       variables contained within the process you select.
    •   Probe —Displays the Process Probe view for the selected process.
    •  Add Variable —Displays the Shared Variable Properties dialog box, which you can
      use to create a new variable within the selected process.
    •  Add I/O Server —Displays the Create New I/O Server dialog box to create an I/O
       server and add it to the Shared Variable Engine.


                                                    © National Instruments Corporation 1841

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1841 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1842 ordinal=1842 -->
## LabVIEW User Manual

LabVIEW User Manual


                   •   Stop Process —Stops the selected process in the system tree. When a process stops,
                 the values of variables in that process become unavailable and do not update. You
              must have sufficient access privileges to stop a process.
                   •   Start Process —Starts the selected process in the system tree. Processes
                 automatically start when you create them. If you select the Stop Process item to
                 stop a process, you can use Start Process to restart the process. You must have
                    sufficient access privileges to start a process.
                   •  Remove Process —Removes the selected process in the system tree. You must have
                    sufficient access privileges to remove a process.


1842  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1842 -->

<!--KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1843 ordinal=1843 -->
## LabVIEW User Manual

LabVIEW User Manual


1843  ni.com

<!--END_KB_RECORD source=NI_LABVIEW_USER_MANUAL locator=page:1843 -->

