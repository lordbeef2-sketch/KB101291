# NI DOCUMENT BUNDLE: labview-nxg-application-builder

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-application-builder start=1 end=28 -->
<!--NI_TOPIC bundle=labview-nxg-application-builder path=applications.html language=enus -->
## TOPIC 00001: Applications

- bundle_id: `labview-nxg-application-builder`
- source_path: `applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/applications.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: An application is a program designed to perform a group of coordinated functions or tasks. A web application is an application that is capable of running in web browsers. Use an Application document (.gcomp) to create an application from scratch or from existing code. The Application document contai

Applications

An *application* is a program designed to
 perform a group of coordinated functions or tasks. A web application is an application that is
 capable of running in web browsers.

Use an *Application* document (.gcomp) to
 create an application from scratch or from existing code. The Application document
 contains your source files, such as VIs, text files, and other types of files.

You can build your application into HTML, JavaScript, and CSS that you share on web servers
 and run in web browsers outside the development environment.

Parent topic:

Building and Distributing Applications and Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=build-and-dist.html language=enus -->
## TOPIC 00002: Building and Distributing Applications and Libraries

- bundle_id: `labview-nxg-application-builder`
- source_path: `build-and-dist.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/build-and-dist.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Build your code into a package that you share and run outside or within the development environment. An application is a program designed to perform a group of coordinated functions or tasks. A web application is an application that is capable of running in web browsers. A library is a collection of

Building and Distributing Applications and
 Libraries

Build your code into a package that you share and run outside or within the development
 environment.

application

A *library* is a collection of source files, such
 as VIs, type definitions, classes, and other support files.

Use an Application or Library document (.gcomp) to create an
 application, library, or custom palette. Each document contains your source files, such as
 VIs, menus, and text files.

Use the following steps to build and customize your
 application or library.

1. Create your application or library. 
 OptionDescription[Create an
 application](creating-executable.html)
 To create an executable, create an Application
 document (.gcomp), add source files to the document, and build the
 application into an executable.
 org.dita.html5/xsl/topic.xsl 455Note You can also [build your
 application from the CLI](build-application.html).[Create a
 library](creating-library.html)
 Use a Library document (.gcomp) to add source files and to
 create a library or an [add-on library](creating-custom-palette.html).org.dita.html5/xsl/topic.xsl 455Note You can also [build your library
 from the CLI](build-library.html).
2. Optional: 
 [Localize
 strings](create-localized-string-dictionaries.html)—To localize strings for objects that display at run
 time, such as dialog boxes, add custom entries to a string dictionary file and use the
 Get Localized String node to retrieve the strings
 programmatically.
3. Optional: 
 [Optimize your
 library](run-operation-using-cli.html)—Use the command line interface (CLI) to run a predefined command that
 optimizes library file performance.
4. Optional: 
 [Create an
 executable](creating-executable.html)—Build your application into an executable. 
 org.dita.html5/xsl/topic.xsl 455Note The target that the executable runs on must have the LabVIEW Run-Time Engine
 installed.
5. [Package your
 file](distribute-apps-libs.html)—Package your application or library into a package or package
 installer.
6. Optional: 
 Add a project to LabVIEW NXG—Add a LabVIEW NXG project that demonstrates the use
 of an add-on library to LabVIEW NXG as an example or template.

<!--NI_TOPIC bundle=labview-nxg-application-builder path=build-application.html language=enus -->
## TOPIC 00003: build-application

- bundle_id: `labview-nxg-application-builder`
- source_path: `build-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/build-application.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `reference`
- source_description: Builds the specified application into a binary. To build an application from the CLI, use the following syntax: gwebcli.exe build-application -p <relative or absolute location of the project> -n <name of the application> -t <Web Server target containing the application> -s For example: gwebcli.exe b

build-application

Builds the specified application into a binary.

To build an application from the CLI, use the following syntax:

```text
        
          gwebcli.exe build-application -p <relative or absolute location of the project> -n <name of the application> -t <Web Server target containing the application> -s
      
```

For example:

```text
        
          gwebcli.exe build-application -p "C:\G Web Projects\Project.gwebproject" -n "Application.gcomp" -t "Default Web Server" -s
      
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project containing the application to build. | -p "C:\\G Web Projects\\Project.gwebproject" --path="C:\\G Web Projects\\Project.gwebproject" |
| -n --name=VALUE | Yes | Specifies the name of the application to build. | -n "Application.gcomp" --name="Application.gcomp" |
| -t --target=VALUE | This argument is required if the project contains SystemDesigner targets. | The target that contains the application to build. This option is only required if the project contains SystemDesigner targets. | -t "Default Web Server" --target="Default Web Server" |
| -s --save | No | Saves the application and project file after building. Use this argument when you select Auto-increment version on build in the application. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=labview-nxg-application-builder path=build-library.html language=enus -->
## TOPIC 00004: build-library

- bundle_id: `labview-nxg-application-builder`
- source_path: `build-library.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/build-library.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `reference`
- source_description: Builds the specified library into a binary. To build a library from the CLI, use the following syntax: gwebcli.exe build-library -p <relative or absolute location of the project> -n <name of the library> -t For example: gwebcli.exe build-library -p "C:\G Web Projects\Project.gwebproject" -n "Library

build-library

Builds the specified library into a binary.

To build a library from the CLI, use the following syntax:

```text
        
          gwebcli.exe build-library -p <relative or absolute location of the project> -n <name of the library> -t
      
```

For example:

```text
        
          gwebcli.exe build-library -p "C:\G Web Projects\Project.gwebproject" -n "Library.gcomp" -t
      
```

Note

build-library

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project containing the library to build. | -p "C:\\G Web Projects\\Project.gwebproject" --path="C:\\G Web Projects\\Project.gwebproject" |
| -n --name=VALUE | Yes | Specifies the name of the library to build. | -n "Library.gcomp" --name="Library.gcomp" |
| -t --target=VALUE | This argument is required if the project contains SystemDesigner Web Server targets. | Specifies the SystemDesigner Web Server target that contains the library to build. You can view Web Server targets you added to SystemDesigner by opening the library in the editor and clicking the Select target drop down. | -t "Default Web Server" --target="Default Web Server" |
| -s --save | No | Saves the library and project file after building. Use this argument when you select Auto-increment version on build in the library. | — |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=labview-nxg-application-builder path=building-code-into-exe.html language=enus -->
## TOPIC 00005: Building Code into an Executable

- bundle_id: `labview-nxg-application-builder`
- source_path: `building-code-into-exe.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/building-code-into-exe.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use an Application document (.gcomp) to build code into an executable. Before you begin, create a project that contains the files you want to include in your executable. Create a new Application document. On the Project Files tab, right-click one or more VIs you want to include in your executable an

Building Code into an Executable

Use an Application document (.gcomp) to build code into an executable.

Before you begin, create a project that contains the files you want to include in your executable.

1. Create a new Application document.
  1. On the Project Files tab, right-click one or more
 VIs you want to include in your executable and select Create
 Application/Library from item.
  2. In the Create Application or
 Library dialog box, set Type to
 Application.
  3. Enter values in 
 Application name and 
 Namespace.
  4. Determine whether to enable the Include
 dependencies not in an Application or Library checkbox. If you
 enable the Include dependencies not in an Application or
 Library checkbox, the Application or Library document you create
 includes any dependencies one or more of your VIs require that are not already
 in an Application or Library document.
  5. Click OK.
2. In the Application document, select a VI and enable the 
 Top-level VI checkbox. 
 The panel of the top-level VI launches when you run the executable. 
 You must choose at least one VI to be the top-level VI. If you enable the 
 Top-level VI checkbox for multiple VIs, the VIs launch in separate windows when you run the executable.
3. On the Document tab, enter information
 about your application in the Details section.
4. Optional: 
 In the Icon section, click the
 ... button to import a .ico file
 to use as the icon of the executable.
5. Optional: 
 If your application requires additional binary files
 located outside the application directory, add the binary file
 locations.
  1. In the
 Document tab, under the Run time
 section, click + to add an additional binary file
 location.
  2. Enter the file path or
 browse to the location of the additional binary file.
6. Click Build. 
 The Build Queue tab shows the status of the
 build process.

Locate item in Windows
 Explorer

Parent topic:

Creating an Executable

<!--NI_TOPIC bundle=labview-nxg-application-builder path=cli-global-arguments.html language=enus -->
## TOPIC 00006: Global Arguments

- bundle_id: `labview-nxg-application-builder`
- source_path: `cli-global-arguments.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/cli-global-arguments.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `reference`
- source_description: Refer to the table below for a list of arguments you can use when executing an operation with the command line interface. All arguments are case-sensitive. Argument Description Example -v --verbose Increases the detail of the output log. gwebcli.exe build-application -p "C:\G Web Projects\Project.gw

Global Arguments

Refer to the table below for a list of arguments you can use when executing an operation with the command line interface.

Note

| Argument | Description | Example |
| --- | --- | --- |
| -v --verbose | Increases the detail of the output log. | gwebcli.exe build-application -p "C:\\G Web Projects\\Project.gwebproject" -n "Application.gcomp" -v |

Parent topic:

Running Operations Using the Command Line Interface

<!--NI_TOPIC bundle=labview-nxg-application-builder path=code-dependency-guidelines.html language=enus -->
## TOPIC 00007: Code Dependency Guidelines

- bundle_id: `labview-nxg-application-builder`
- source_path: `code-dependency-guidelines.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/code-dependency-guidelines.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: Understand the code dependency guidelines to fix missing dependency errors or perform code refactoring. A VI in an Application or Library document can call only VIs within the same component or in a dependency library.

Code Dependency Guidelines

Understand the code dependency guidelines to fix missing dependency errors or perform code refactoring.

A VI in an Application or Library document can call only VIs within the same component or in
 a dependency library.

[IMAGE alt='1378' src='GUID-F0955503-5949-42F0-8132-B5EDBE39185B-a5.svg']

Parent topic:

Componentizing Applications

<!--NI_TOPIC bundle=labview-nxg-application-builder path=componentize-application.html language=enus -->
## TOPIC 00008: Componentizing Applications

- bundle_id: `labview-nxg-application-builder`
- source_path: `componentize-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/componentize-application.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: Componentizing an application helps you organize code into logical groups, save time from creating duplicate code, and enhance software stability. Use Application and Library documents to create component-based applications, in which you compose loosely coupled code into modular and cohesive project

Componentizing Applications

Componentizing an application helps you organize code into logical groups, save time from
 creating duplicate code, and enhance software stability. Use Application and
 Library documents to create component-based applications, in which you compose loosely
 coupled code into modular and cohesive projects.

The following figure demonstrates how to convert a project with loosely coupled code into a component-based project.

[IMAGE alt='1378' src='GUID-073E4D0F-B796-4939-848D-E1BFF3CF58E5-a5.svg']

When you build the application, each top-level VI is built into a separate HTML page with
 required support files. The following figure shows an example of the build result.

[IMAGE alt='1378' src='GUID-67CA1E2F-F40A-4931-BB3B-6C577581275E-a5.png']

#### Best Practices for Componentizing
 Applications

Consider the following guidelines when componentizing an
 application:

- Keep application components small and
 self-contained.
- Store code that you might reuse in a separate
 Library document.
- Create namespaces to
 organize files into logical groups.
- Avoid creating circular dependencies between
 libraries, which cause problems such as build failures.
- Analyze your application composition frequently for
 opportunities to refactor code. Refer to Code Dependency Guidelines when
 refactoring code.

#### Code Dependency Guidelines

A VI in an
 Application or Library document can call only VIs within the same component or in a
 dependency library.

[IMAGE alt='1378' src='GUID-F0955503-5949-42F0-8132-B5EDBE39185B-a5.svg']

Parent topic:

Applications

<!--NI_TOPIC bundle=labview-nxg-application-builder path=create-localized-string-dictionaries.html language=enus -->
## TOPIC 00009: Creating Localized String Dictionaries

- bundle_id: `labview-nxg-application-builder`
- source_path: `create-localized-string-dictionaries.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/create-localized-string-dictionaries.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: To localize strings for objects that display at run time, such as dialog boxes, add custom entries to a string dictionary file and use the Get Localized String node to retrieve the strings programmatically. Before you can localize objects that display at run time, generate a string dictionary file u

Creating Localized String Dictionaries

To localize strings for objects that display at run
 time, such as dialog boxes, add custom entries to a string dictionary file and use the
 Get Localized String node to retrieve the strings
 programmatically.

Before you can localize objects that display at run time, generate a string dictionary file using 
 Export strings, create a copy of the string dictionary file, and save it in a new folder that indicates the language of the string dictionary file. You must save the new folder within the project folder in the same location as the original dictionary folder and name the new folder using standard Microsoft locale names, such as en-US or zh-CN. 
 Export strings overwrites any existing dictionary in the folder for the default language of the editor. If you want to preserve an existing dictionary, save a copy of the existing dictionary file in a separate location. You can also create your own string dictionary file which contains entries for each string you want to localize, but this file must follow the same syntax and file extension as the dictionaries that 
 Export strings generates.

Note

Exporting Strings for Localization

1. Open the string dictionary file you want to edit with a text editor.
2. Add a key to the string dictionary file. You can specify any name for the key, but any new entries you add to the dictionary file must use the same syntax as the entries automatically generated by 
 Export strings.
3. Add the localized text you want the object to display within the 
 <loc> element. If you want to localize the text "Good Morning!" to German, for example, make your new entry look similar to the following example: 
 <entry key="New_Key_Name">
 <loc>[de-DE] Guten Morgen!</loc>
 </entry> 
 Repeat this process for each string you want to localize.
4. Save the dictionary file.
5. Add the Get Localized String node to the diagram.
6. Right-click the key input and select 
 Create constant. Enter the key name you added to the dictionary file. For the above example, enter 
 New_Key_Name.
7. Right-click the fallback input and select 
 Create constant. Enter text in this constant that you want to display if the Get Localized String node cannot locate the key you specify in key.
8. Right-click the base path input and enter the file path to the application you want to localize.
9. Wire the localized string output to the object you want to localize. For example, if you want to localize the string in a dialog box, wire this output to the message input of a dialog box node.
10. Run the application. 
 The application now displays the localized string(s). 
 org.dita.html5/xsl/topic.xsl 455Note The application determines which dictionary to retrieve keys from based on the language you define in the editor preferences. You must have the editor set to the desired language, or the application does not display the localized strings.

You have now created a localized string dictionary for your
 code.

optimizing its
 performance

packaging your library

Parent topic:

Building and Distributing Applications and Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=creating-a-command-vi-plugin.html language=enus -->
## TOPIC 00010: Creating a Command VI Plugin

- bundle_id: `labview-nxg-application-builder`
- source_path: `creating-a-command-vi-plugin.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/creating-a-command-vi-plugin.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Command VIs to insert custom menu items in the LabVIEW NXG editor. Before you begin, ensure that the LabVIEW NXG Editor Plugin Authoring Tools package is installed. Create or open a project. Click FileNewApplication and select Editor Plugin as the application sub-type. This application type is r

Creating a Command VI Plugin

Use Command VIs to insert custom menu items in the LabVIEW NXG editor.

Before you begin, ensure that the LabVIEW NXG
 Editor Plugin Authoring Tools package is installed.

1. Create or open a project.
2. Click File»New»Application and select Editor Plugin as the application
 sub-type. 
 This application type is required for all VI Editor Plugins. Command VIs created
 outside of an application with the Editor Plugin sub-type will not function
 correctly.
3. In the Application document, click New»Command VI.
4. Open the Menu view of the Command VI and fill out the following fields: 
[IMAGE alt='1378' src='GUID-199757AD-382F-439D-AB1A-1DC68C1F2C63-a5.png'] 
 Location — Specifies where in the editor you want your menu items to
 appear.
 Label — Specifies the name of the menu item.
 Submenus — Specifies the submenu you want your menu item to be grouped
 under.org.dita.html5/xsl/topic.xsl 455Note Use backslashes to add
 additional levels of submenus. For example:
 Submenu1/Submenu2/Test.
 Weight — Specifies the relative position of the menu item compared to other items in
 the Add-ons menu or submenu. The weight value must be a number between 0 and 1, where
 lower numbers indicate a higher position in the menu. It may be helpful to think of it
 as menu items with a lower weight floating to the top.
5. Configure the panel and diagram of the Command VI to add the functionality you want to
 execute when a user selects the menu item. 
 org.dita.html5/xsl/topic.xsl 455Note Command VIs cannot be inline or
 recursive but they can include subVIs that are. Additionally, by default, Command VI
 panels do not appear when a user selects them as a menu item. To show a panel when the
 menu item is selected, include the following code in your Command VIs. 
[IMAGE alt='1378' src='GUID-CA2158C9-E92B-43EE-AC1E-8433EC3808D2-a5.png']
6. Click New»Package/Installer to create a new Package (.lvdist) document.
7. Configure the package document.
  1. In the Files section, add your application.
  2. Set the Destination to Public Add-ons.
  3. Fill out the rest of the document to suit your application.
8. Click Build.
9. Locate and install your package.
10. Restart LabVIEW NXG when prompted. 
 Your Command VI plugin appears in the location you specified. 
[IMAGE alt='1378' src='GUID-C7901957-6F57-44FD-B809-A9823F94DD7D-a5.png'] 
org.dita.html5/xsl/topic.xsl 455Note The lifetime of your plugin is linked to
 the project from which it is launched. If you close the project that was active when you
 launched the plugin, the plugin terminates at the same time. To uncouple the lifetime of
 your plugin from the lifetime of the project, build your program into an executable that
 you can call from a Command VI with the System Exec
 VI.
11. Distribute the package or installer to end users for them to install using NI Package
 Manager.

Parent topic:

VI Editor Plugins

<!--NI_TOPIC bundle=labview-nxg-application-builder path=creating-custom-palette.html language=enus -->
## TOPIC 00011: Creating a Custom Palette

- bundle_id: `labview-nxg-application-builder`
- source_path: `creating-custom-palette.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/creating-custom-palette.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: The palette provides an organized hierarchy of all the objects you can add to the diagram or panel. Create a palette file (.gpal), or an add-on library, to customize a palette category with the objects in your library. By default, custom categories are added to the Add-ons palette category. On the D

Creating a Custom Palette

The palette provides an organized hierarchy of all the objects you can add to the
 diagram or panel. Create a palette file
 (.gpal), or an add-on library, to customize a palette category
 with the objects in your library. By default, custom categories are added to the
 Add-ons palette category.

1. On the 
 Document tab of a Library document, click 
 Create palette file.
2. In the 
 Palette Options dialog box, select the type of palette you want to create.
  - G diagram palette —Create a palette containing objects you can drop on the diagram.
  - G panel palette —Create a palette containing objects you can drop on the panel.
3. Click OK.
4. In the palette file, use the options on the 
 Item tab to customize each palette item.

creating a web
 application

Parent topic:

Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=creating-executable.html language=enus -->
## TOPIC 00012: Creating an Executable

- bundle_id: `labview-nxg-application-builder`
- source_path: `creating-executable.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/creating-executable.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: To create an executable, create an Application document (.gcomp), add source files to the document, and build the application into an executable. Create a new Application document. Click FileNewApplication. In the Create Application dialog box, enter values in Application name and Namespace. Click O

Creating an Executable

To create an executable, create an Application
 document (.gcomp), add source files to the document, and build the
 application into an executable.

1. Create a new Application document.
  1. Click 
 File»New»Application.
  2. In the 
 Create Application dialog box, enter values in 
 Application name and 
 Namespace.
  3. Click OK.
2. Add source files to the Application document in one of the following ways:
  - Create files under the project and drag the files from the 
 Project Files tab to the Application document.
  - In the Application document, click 
 New on the document toolbar and select the type of file to create.
  - In the Application document, click
 Import files on the document toolbar and select
 files on disk to copy to the Application document.
3. In the Application document, select a VI and enable the 
 Top-level VI checkbox. 
 The panel of the top-level VI launches when you run the executable. 
 You must choose at least one VI to be the top-level VI. If you enable the 
 Top-level VI checkbox for multiple VIs, the VIs launch in separate windows when you run the executable.
4. On the Document tab, enter information
 about your application in the Details section.
5. Optional: 
 In the Icon section, click the
 ... button to import a .ico file
 to use as the icon of the executable.
6. Optional: 
 If your application requires additional binary files
 located outside the application directory, add the binary file
 locations.
  1. In the
 Document tab, under the Run time
 section, click + to add an additional binary file
 location.
  2. Enter the file path or
 browse to the location of the additional binary file.
7. Click Build. 
 The Build Queue tab shows the status of the
 build process.

Locate item in Windows
 Explorer

package your
 application

Parent topic:

Applications

<!--NI_TOPIC bundle=labview-nxg-application-builder path=creating-library-from-existing-files.html language=enus -->
## TOPIC 00013: Creating a Library from Existing Files

- bundle_id: `labview-nxg-application-builder`
- source_path: `creating-library-from-existing-files.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/creating-library-from-existing-files.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Library document (.gcomp) to create a library from existing files. Before you begin, create a project that contains the files you want to include in your library. On the Project Files tab, right-click the VI(s) you want to include in your library and select Create Application/Library from item

Creating a Library from Existing Files

Use a Library document (.gcomp) to create a library from existing files.

Before you begin, create a project that contains the files you want to include in your library.

1. On the 
 Project Files tab, right-click the VI(s) you want to include in your library and select 
 Create Application/Library from item.
2. In the Create Application or Library
 dialog box, set Type to
 Library.
3. Enter values in 
 Library name and 
 Namespace.
4. Determine whether to enable the Include
 dependencies not in an Application or Library checkbox. If you
 enable the Include dependencies not in an Application or
 Library checkbox, the Application or Library document you create
 includes any dependencies one or more of your VIs require that are not already
 in an Application or Library document.
5. Click OK.

The Library document appears in the project and contains the files you selected to include in the library.

Parent topic:

Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=creating-library.html language=enus -->
## TOPIC 00014: Creating a Library

- bundle_id: `labview-nxg-application-builder`
- source_path: `creating-library.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/creating-library.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: To create a library, create a Library document (.gcomp) and add source files to the document. Create a new Library document. Click FileNewLibrary. In the Create Library dialog box, enter values in Library name and Namespace. Click OK. Save the Library document. Add source files to the Library docume

Creating a Library

To create a library, create a Library document (.gcomp) and add source files to the document.

1. Create a new Library document.
  1. Click 
 File»New»Library.
  2. In the 
 Create Library dialog box, enter values in 
 Library name and 
 Namespace.
  3. Click OK.
  4. Save the Library document.
2. Add source files to the Library document in one of the following ways:
  - Create files under the project and drag the files from the 
 Project Files tab to the Library document.
  - In the Library document, click 
 New on the document toolbar and select the type of file to create.
  - In the Library document, click 
 New»Import files on the document toolbar and select files on disk to copy to the Library document.
3. For each item in the Library document, configure the build options as needed.
  - Enable Export if you
 want to allow a source file to be called from other applications or
 libraries. Disable Export for internal source
 files.
  - Enable Always
 include if you want to include a support file, such as a
 text, image, or audio file or source files, such as .gvis or .gtypes, when
 you share the library.
4. On the Document tab, enter information about your library
 in the Details section.
5. Click File»Save all.

optimizing your
 library

package it

Parent topic:

Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=debugging-an-executable.html language=enus -->
## TOPIC 00015: Debugging an Executable

- bundle_id: `labview-nxg-application-builder`
- source_path: `debugging-an-executable.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/debugging-an-executable.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: After building code into an executable, you can debug the executable. On the Document tab of the Application document, click Debug to launch the executable in debugging mode. If you click Debug without building the executable, LabVIEW automatically builds the executable and launches the executable i

Debugging an Executable

After building code into an executable, you can debug the executable.

1. On the 
 Document tab of the Application document, click 
 Debug to launch the executable in debugging mode. 
 org.dita.html5/xsl/topic.xsl 455Note If you click 
 Debug without building the executable, LabVIEW automatically builds the executable and launches the executable in debugging mode. 
 The top-level VI and the executable start running in debugging mode. LabVIEW locks the entire hierarchy of VIs in the Application document to avoid VI changes during the debugging process.
2. On the diagram of the top-level VI, debug the executable using the same techniques for debugging a VI.
3. After you finish debugging, click 
 Stop debugging. 
 LabVIEW stops running the executable and unlocks the entire hierarchy of VIs in the Application document.

Parent topic:

Creating an Executable

<!--NI_TOPIC bundle=labview-nxg-application-builder path=distribute-apps-libs.html language=enus -->
## TOPIC 00016: Packaging an Application or Library

- bundle_id: `labview-nxg-application-builder`
- source_path: `distribute-apps-libs.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/distribute-apps-libs.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Package your application or library for distribution. Before you begin, create an application or a library before completing the following tasks: Package an Application—Use a Package document (.lvdist) to build an application into a package. Package a Library—Use a Package document (.lvdist) to buil

Packaging an Application or Library

Package your application or library for distribution.

Before you begin, create an application or a library before completing the following tasks:

- [Package an
 Application](distributing-app-lib.html)—Use a Package document (.lvdist) to
 build an application into a package.
- [Package a
 Library](package-libraries.html)—Use a Package document (.lvdist) to
 build a library into a package or package installer.

Parent topic:

Building and Distributing Applications and Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=distributing-app-lib.html language=enus -->
## TOPIC 00017: Packaging an Application

- bundle_id: `labview-nxg-application-builder`
- source_path: `distributing-app-lib.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/distributing-app-lib.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Package document (.lvdist) to build an application into a package. The Package document contains the build configuration and metadata for your package, such as version, maintainer, and display name. Click FileNewPackage/Installer. The Package document opens in the project. Drag the files you w

Packaging an Application

Use a Package document (.lvdist) to
 build an application into a package.
 The Package document contains the build configuration and metadata for your
 package, such as version, maintainer, and display name.

1. Click 
 File»New»Package/Installer. 
 The Package document opens in the project.
2. Drag the files you want to distribute from the 
 Project Files tab to the 
 Files section. 
 You can include applications and other support files. 
 The Package document automatically calculates the package dependencies that your application requires.
3. Review the contents of the 
 Package Dependencies section, which displays package dependencies your application requires. 
 You can include additional dependencies by clicking 
 Dependencies and selecting packages under 
 Add Dependencies.
4. In the 
 Information section, confirm that the Package document filled the text boxes with information you want. 
 The Package document automatically gathers information from the project and your NI User Account to complete the 
 Information section. The values in the text boxes become metadata in the package. NI Package Manager reads the metadata of packages to sort them and display information about them to users.
5. On the 
 Document tab, choose the target on which to build the package contents in 
 Build target.
6. Select the package output type from 
 Output type.
7. In 
 Output directory, specify the location to save the package output.
8. Click File»Save all.
9. Click 
 Build. 
 The Build Queue tab shows the status of the
 build process.

Right-click the package and click Locate directory in Windows Explorer
 to locate the package in the output directory. You can distribute your software
 content using NI Package Manager or other distribution channels.

Parent topic:

Packaging an Application or Library

<!--NI_TOPIC bundle=labview-nxg-application-builder path=export-import-strings-for-localization.html language=enus -->
## TOPIC 00018: Exporting Strings for Localization

- bundle_id: `labview-nxg-application-builder`
- source_path: `export-import-strings-for-localization.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/export-import-strings-for-localization.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Localize applications into additional languages by exporting the strings into a string dictionary file, translating the file, and saving your changes. The string dictionary file contains information to localize the following strings: Application title and description Window titles and descriptions O

Exporting Strings for Localization

Localize applications into additional languages by exporting the strings into a string dictionary file, translating the file, and saving your changes.

- Application title and description
- Window titles and descriptions
- Object labels and descriptions
- Private data (listbox item names, 
 graph plot names, graph cursor names, and graph annotation names)
- Free labels (panel and diagram) 
 org.dita.html5/xsl/topic.xsl 455 Note The string dictionary file does not contain information to localize string data in diagram constants, arrays, or clusters.

Creating Custom String Dictionaries for Localization

Note

1. Open the application you want to localize.
2. Save the application.
3. On the 
 Document tab, click 
 Export strings in the Localization section.
4. Navigate to the string dictionary file using the path in the file dialog box and click 
 OK to close the dialog box.
5. Create a copy of the string dictionary file and save it in a new folder that indicates the language of the string dictionary file. You must save the new folder within the project folder in the same location as the original dictionary folder and name the new folder using standard Microsoft locale names, such as en-US or zh-CN. 
 If you do not follow these guidelines, your application may not be able to locate the localized string dictionary file.
6. Translate the new string dictionary file and save the changes.
7. Save and close the project.
8. Reload the project and reopen the application.
9. On the 
 Document tab of the panel, select the language from the 
 Preview drop-down menu. 
 The localized strings now display in the application.
 org.dita.html5/xsl/topic.xsl 455Note If you modify an application after you export and translate the string dictionary, the string dictionary may contain incorrect or missing keys, and the application may no longer display the correct localized content. If you need to export strings again and want to preserve an existing dictionary, make sure to save a copy of the existing dictionary in a separate location. 
 Export strings overwrites any existing dictionary in the folder for the default language of the editor.

To localize an application in multiple languages, create copies of the dictionary file and repeat this process to create dictionaries for all desired languages.

Parent topic:

Creating Localized String Dictionaries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=libraries.html language=enus -->
## TOPIC 00019: Libraries

- bundle_id: `labview-nxg-application-builder`
- source_path: `libraries.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/libraries.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: A library is a collection of source files, such as VIs, type definitions, classes, and other support files. You can use a library to organize source​ files into a single hierarchy of items. A library allows you to reuse code across multiple applications without having to implement the same functiona

Libraries

A *library* is a collection of source files, such
 as VIs, type definitions, classes, and other support files. You can use a library
 to organize source​ files into a single hierarchy of items.

A library allows you to reuse code across multiple applications without having to implement the same functionality in each application.​ Your code must be part of a library before you can reuse it across ​applications.

Use a *Library* document (.gcomp) to create a library. The
 Library​ document allows you to perform the following actions: ​

- Organize files
 using namespaces to avoid name collisions.​
- Customize the organization of files on the
 palette.
- Enable source files to be called from other
 applications and libraries​.

Parent topic:

Building and Distributing Applications and Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=optimize-project.html language=enus -->
## TOPIC 00020: optimize-project

- bundle_id: `labview-nxg-application-builder`
- source_path: `optimize-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/optimize-project.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `reference`
- source_description: Improves the load time and performance of your projects by loading, compiling, and saving project files during the build process. Similar to mass compiling in LabVIEW, the optimize-project command:Verifies the existence of subVIs and links them to the main VI.Updates files to the current G Web Devel

optimize-project

Improves the load time and performance of your projects by loading,
 compiling, and saving project files during the build process.

mass compiling in LabVIEW

optimize-project

- Verifies the existence of subVIs and links them to the main VI.
- Updates files to the current G Web Development Software version.
- Reports corrupt files which can prevent your project from loading
 correctly.

```text
gwebcli.exe optimize-project -p <relative or absolute location of the project> -t <time in seconds> -s <name of target to exclude>
```

```text
gwebcli.exe optimize-project -p "C:\G Web Projects\Project.gwebproject" -t 60 -s "Default Web Server"
```

| Argument | Required | Description | Example |
| --- | --- | --- | --- |
| -p --path=VALUE | Yes | Specifies the relative or absolute path of the project to optimize.Note You can reference multiple paths in a comma-separated list. | -p "C:\\G Web Projects\\Project.gwebproject" --path=".\\Add\\Add.gwebproject, .\\Subtract\\Subtract.gwebproject" |
| -s --skipTargets=VALUE | No | Specifies which targets to exclude in the optimization process. | -s "Default Web Server" --skipTarget="Default Web Server" |
| -t --timeout=VALUE | No | Specifies the amount of time in seconds before the operation exits. | -t 10 --timeout=10 |

Parent topic:

Predefined Command Line Operations

<!--NI_TOPIC bundle=labview-nxg-application-builder path=organizing-code-to-avoid-name-collisions.html language=enus -->
## TOPIC 00021: Organizing Code to Avoid Name Collisions

- bundle_id: `labview-nxg-application-builder`
- source_path: `organizing-code-to-avoid-name-collisions.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/organizing-code-to-avoid-name-collisions.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: A namespace is a container used to organize files into logical groups. Items in the same namespace must have a unique name. Namespaces help to prevent name collisions. Open an Application or Library document. On the document toolbar, click NewAdd namespace. Rename the namespace. Give your namespace

Organizing Code to Avoid Name Collisions

A 
 *namespace* is a container used to organize files into logical groups. Items in the same namespace must have a unique name. Namespaces help to prevent name collisions.

1. Open an Application or Library document.
2. On the document toolbar, click 
 New»Add namespace.
3. Rename the namespace. 
 org.dita.html5/xsl/topic.xsl 455Tip Give your namespace a meaningful name to indicate that the namespace contains files of the same logical group.
4. Drag files from the project to the namespace.
5. Optional: 
 Rename the files as necessary. 
 Different namespaces can contain files that have the same name. For example, the 
 Main VI namespace and the 
 SubVI namespace in the same Application or Library document can each contain a file named 
 Function.gvi.
6. Click File»Save all.

After you build an application, each namespace corresponds to a folder in the output directory.

Parent topic:

Componentizing Applications

<!--NI_TOPIC bundle=labview-nxg-application-builder path=package-libraries.html language=enus -->
## TOPIC 00022: Packaging a Library

- bundle_id: `labview-nxg-application-builder`
- source_path: `package-libraries.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/package-libraries.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use a Package document (.lvdist) to build a library into a package or package installer. The Package document contains the build configuration and metadata, such as version, maintainer, and display name, for your package. Before you begin, create a library of source files using a Library document (.

Packaging a Library

Use a Package document (.lvdist) to
 build a library into a package or package installer.

The Package document contains the build configuration and metadata, such as version,
 maintainer, and display name, for your package.

create a library

.gcomp

1. Click 
 File»New»Package/Installer. 
 The Package document opens in the project.
2. Drag the library or libraries you want to distribute from the Project
 Files tab to the Files section. 
 You can include applications and other support files.org.dita.html5/xsl/topic.xsl 455Note Make sure that the Destination is set to
 Public Add-ons and that the company information is filled in.
 Your libraries will be installed in G Web Development
 Software[version]/addons/[company name]/[product name]. 
 The Package document automatically calculates the package dependencies that your
 library requires.
3. In the right rail, click Create palette
 file.
4. Use the pull-down to choose whether you will create a
 G diagram palette or a G panel palette
 library.
5. Review the contents of the Package Dependencies section, which
 displays package dependencies your library requires. 
 You can include additional dependencies by clicking Add
 dependencies and selecting packages.
6. In the Information section, confirm that the values in the
 Package document are correct. 
 The Package document automatically gathers information from the project and your NI
 User Account to complete the Information section. The values in the
 text boxes become metadata in the package. NI Package Manager reads the metadata of
 packages to sort them and display information about them to users.
7. In Output type on the Document tab,
 select Package for the output type. Select Package
 Installer if you want to create an installer that includes all of your
 packages.
8. In 
 Output directory, specify the location to save the package output.
9. Click File»Save all.
10. Click 
 Build. 
 The Build Queue tab shows the status of the
 build process.

Locate directory in File Explorer

Parent topic:

Packaging an Application or Library

<!--NI_TOPIC bundle=labview-nxg-application-builder path=place-diagram-contents.html language=enus -->
## TOPIC 00023: Adding Code Snippets to a Custom Palette

- bundle_id: `labview-nxg-application-builder`
- source_path: `place-diagram-contents.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/place-diagram-contents.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Add items to a palette file (.gpal) that include chunks of code from your diagram. Before you begin, complete the following prerequisite tasks: Enable .gpal option to place diagram contents when dropped.Enable preview features.Relaunch G Web Development Software. Create a VI within your project. Cre

Adding Code Snippets to a Custom
 Palette

Add items to a palette file (.gpal) that include chunks of code from
 your diagram.

- Enable .gpal option to place diagram contents when
 dropped.
- Enable preview features .
- Relaunch G Web Development Software.

1. [Create a VI within your project.](/csh?topicname=create-vi.html)
2. [Create a library.](/csh?topicname=creating-library.html)
3. Add the VI to the library.
4. On the 
 Document tab of a Library document, click 
 Create palette file.
5. Select G diagram palette from the palette type drop-down
 menu.
6. Open your palette file (.gpal). Select your VI.
7. In the Item tab, under Behavior,
 select Place diagram contents. 
 The block of diagram code from the VI will appear on the diagram in
 projects that include your custom .gpal. org.dita.html5/xsl/topic.xsl 455Note You
 cannot include a VI in an application if any of the exported VIs in the
 library are broken. If a VI in your library containing a snippet is broken,
 disable the VI's Export box before building the
 package.

Parent topic:

Creating a Custom Palette

<!--NI_TOPIC bundle=labview-nxg-application-builder path=predefined-cli-operations.html language=enus -->
## TOPIC 00024: Predefined Command Line Operations

- bundle_id: `labview-nxg-application-builder`
- source_path: `predefined-cli-operations.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/predefined-cli-operations.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: The command line interface supports the following operations: build-application—Builds the specified application into a binary. build-library—Builds the specified library into a binary. optimize-project—Improves the load time and performance of your projects by loading, compiling, and saving project

Predefined Command Line Operations

The command line interface supports the following operations:

- build-application — Builds the specified application into a binary.
- build-library — Builds the specified library into a binary.
- optimize-project — Improves the load time and performance of your projects by loading,
 compiling, and saving project files during the build process.

Parent topic:

Running Operations Using the Command Line Interface

<!--NI_TOPIC bundle=labview-nxg-application-builder path=run-operation-using-cli.html language=enus -->
## TOPIC 00025: Running Operations Using the Command Line Interface

- bundle_id: `labview-nxg-application-builder`
- source_path: `run-operation-using-cli.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/run-operation-using-cli.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Run a predefined set of operations in G Web Development Software using the command line interface (CLI). For example, use the CLI to automate the build process of applications you develop. Open a command prompt. Change directories to the location of the CLI. The default location is C:\Program Files\

Running Operations Using the Command Line Interface

Run a predefined set of operations in G Web
 Development Software using the command line interface (CLI).
 For example, use the CLI to automate the build process of applications you
 develop.

1. Open a command prompt.
2. Change directories to the location of the CLI. 
 org.dita.html5/xsl/topic.xsl 455Note The default location is
 C:\Program Files\National Instruments\G Web Development
 Software <version>.
3. Execute a command using the following syntax: 
 gwebcli.exe <operation name>
 -<arguments>.org.dita.html5/xsl/topic.xsl 455Tip To access the
 built-in help for the CLI, execute the gwebcli.exehelp command. To learn more
 about a specific operation, execute the gwebcli.exe <operation name> --help command.

Parent topic:

Building and Distributing Applications and Libraries

<!--NI_TOPIC bundle=labview-nxg-application-builder path=testing-and-debugging-a-vi-editor-plugin.html language=enus -->
## TOPIC 00026: Testing and Debugging a VI Editor Plugin

- bundle_id: `labview-nxg-application-builder`
- source_path: `testing-and-debugging-a-vi-editor-plugin.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/testing-and-debugging-a-vi-editor-plugin.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `task`
- source_description: Use VI Editor Plugin debugging tools to verify and troubleshoot how your plugin appears to users. Open the Editor Plugin application you want to debug. To test how your plugin appears to users, click Run in the Document tab to the right. A new instance of the G Web Development Software editor appear

Testing and Debugging a VI Editor
 Plugin

Use VI Editor Plugin debugging tools to verify and troubleshoot how your plugin appears
 to users.

1. Open the Editor Plugin application you want to debug.
2. To test how your plugin appears to users, click Run in the
 Document tab to the right. 
 A new instance of the G Web Development Software editor appears. This instance
 includes any plugins that the application contains as though they were already installed
 as a package. For example, any Command VIs in the application appear as menu items in this
 instance.
3. To debug any issues you observe in testing your application, return to the Application
 document and click Debug in the Document
 tab. 
 A new instance of the editor appears with all plugins included just as before.
 However, in debug mode, you can also use breakpoints and probes in the original instance
 of the editor to debug your plugin as it runs.

Parent topic:

VI Editor Plugins

<!--NI_TOPIC bundle=labview-nxg-application-builder path=types-of-distributions.html language=enus -->
## TOPIC 00027: Types of Package Outputs

- bundle_id: `labview-nxg-application-builder`
- source_path: `types-of-distributions.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/types-of-distributions.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: With a Package document (.lvdist), you can create a package or package installer to distribute applications and/or add-ons to clients. The following table helps you determine when to use a package or package installer. Output Type Definition File Type Installation Method Configuration Options Packag

Types of Package Outputs

With a Package document (.lvdist), you can create a package or
 package installer to distribute applications and/or add-ons to clients.

The following table helps you determine when to use a package or package installer.

| Output Type | Definition | File Type | Installation Method | Configuration Options |
| --- | --- | --- | --- | --- |
| Package | A single compressed file containing software intended for installation on a target machine. | .nipkg | NI Package Manager or SystemLink Note In most cases, you must add the package to a feed that also includes the dependencies of the package before installing. | Add the package to a feed—clients of the software can subscribe to the feed and install the package from Package Manager via network access. |
| Package Installer | A folder containing the main software package, package dependencies, and an executable file that extracts the package and installs it on a target machine. Note By default, a package installer includes all of the package dependencies in the output so clients of the software can install the package without network access. | .exe | Run the package installer file. Note Web applications can be hosted and used directly via SystemLink. | Reference package dependencies using feeds instead of including the dependencies in the output—when a package installer that references feeds runs, it retrieves dependencies from the feed locations. Require installation of the exact hierarchy and versions of all the dependencies—when clients of the software install the package, the installer installs the exact versions of the dependencies found on the machine that built the package installer when it was built. Note This is recommended only for installing on a clean machine because it might upgrade or downgrade installed packages on the target machine. |

Parent topic:

Packaging an Application or Library

<!--NI_TOPIC bundle=labview-nxg-application-builder path=vi-editor-plugins.html language=enus -->
## TOPIC 00028: VI Editor Plugins

- bundle_id: `labview-nxg-application-builder`
- source_path: `vi-editor-plugins.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-application-builder/raw/resource/enus/vi-editor-plugins.html
- document_id: `labview-nxg-application-builder`
- page_type: `leaf`
- content_type: `concept`
- source_description: The G Web Development Software editor is extensible. You can add new functionality, such as new document types, menu items, properties, and settings. You can use VI Editor Plugins to create basic G plugins to extend G Web Development Software. Command VIs (.gcmd) are a type of VI that allow you to i

VI Editor Plugins

The G Web Development Software editor is extensible. You can add new functionality, such
 as new document types, menu items, properties, and settings.

You can use VI Editor Plugins to create basic G plugins to
 extend G Web Development Software.

.gcmd

- File»Add-ons
- Help»Add-ons
- Tools Launcher tab

End users can run VI Editor Plugins in G Web Development Software without installing any
 additional packages. To create a VI Editor Plugin, you must select the optional G Web
 Development Software Editor Plugin Authoring Tools package when you install G Web
 Development Software through NI Package Manager.

Parent topic:

Building and Distributing Applications and Libraries
