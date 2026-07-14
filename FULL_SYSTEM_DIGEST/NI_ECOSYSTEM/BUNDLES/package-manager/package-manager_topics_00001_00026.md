# NI DOCUMENT BUNDLE: package-manager

<!--NI_BUNDLE_CHUNK bundle=package-manager start=1 end=26 -->
<!--NI_TOPIC bundle=package-manager path=add-package-to-feed.html language=enus -->
## TOPIC 00001: Adding a Package to a Feed

- bundle_id: `package-manager`
- source_path: `add-package-to-feed.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/add-package-to-feed.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the command line interface to add a package to a feed. Place the package in a directory. You can place the package either in the same source directory as the other packages in the feed or in a different directory. Open a command prompt. Change directories to the location of Package Manager. The

### Adding a Package to a Feed

Use the command line interface to add a package to a feed.

1. Place the package in a directory. 
 You can place the package either in the same source directory as the other packages in the feed or in a different directory.
2. Open a command prompt.
3. Change directories to the location of Package Manager. 
 The default location is C:\Program Files\National Instruments\NI Package
 Manager.
4. Run the following command: nipkg
 feed-add-pkg "<location of
 feed>" "<name and filepath of
 package(s)>". 
 For example, Package Manager can update the feed manifest files
 in the C:\temp\myTestFeed directory using the package files in the
 C:\temp\myTestPackage directory.
 To do so, enter the following command.
 C:\Program Files\National Instruments\NI Package Manager> nipkg
 feed-add-pkg
 "C:\temp\myTestFeed"
 "C:\temp\myTestPackage\my-test-package.nipkg".

Parent topic:

Package Distribution

Related concepts:

- Package Creation

Related tasks:

- Creating a Feed
- Installing Packages from a Feed

<!--NI_TOPIC bundle=package-manager path=assemble-eula-package.html language=enus -->
## TOPIC 00002: Assembling a EULA Package

- bundle_id: `package-manager`
- source_path: `assemble-eula-package.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/assemble-eula-package.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Assemble an End-User License Agreement (EULA) package by creating a root directory that contains subdirectories, source files, and configuration files. For detailed information and examples of configuration files you include in a package, refer to Control File Attributes. Create a root directory for

### Assembling a EULA Package

Assemble an End-User License Agreement (EULA) package by creating a root directory that
 contains subdirectories, source files, and configuration files.

Control File
 Attributes

1. Create a root directory for all components of the EULA package. 
 For example: C:\temp\MyEulaPkg
2. In the root directory, create a Debian binary file. 
 Note A Debian binary file declares conformity to the Debian standard. For more
 information, visit debian.org.
  1. Using a text editor, create a new document.
  2. Enter 2.0 in the file.
  3. Save the file as debian-binary and
 omit the file extension.
3. In the root directory, create a control
 subdirectory. 
 C:\temp\MyEulaPkg\control
4. Inside the control subdirectory, create a
 control file.
  1. Using a text editor, create a new document and enter all control file
 attributes and values required for your package. 
 Architecture: windows_x64
Conflicts: ni-package-manager
Description: This is a custom license agreement for my software.
XB-DisplayName: My Software License Agreement
XB-EulaTitle: My Software
Homepage: https://www.mycompany.com
Maintainer: My company <support@mycompany.com>
Package: eula-mycompany
XB-Plugin: eula
Section: Infrastructure
XB-UserVisible: no
Version: 1.0.0.0 
 Note To display a EULA
 during package installation, add the XB-EULA attribute to the package control file and set
 the attribute value to the name of the EULA package. When building a
 feed, ensure that you include the EULA package along with any
 package that references it.
  2. Save the file as control but omit
 the file extension.
5. In the root directory, create a data
 subdirectory. 
 C:\temp\MyEulaPkg\data
6. In the data subdirectory, create your license file with
 file extension .rtf or .txt. 
 C:\temp\MyEulaPkg\data\my-company-software-license.rtf

[IMAGE alt='image' src='GUID-AD1F582E-C5FC-4E71-A85D-B3CAE23829AB-a5.jpg']

[IMAGE alt='image' src='GUID-55B09E88-9F2F-4818-8EBF-7794F6848929-a5.jpg']

Parent topic:

Package Creation

Related concepts:

- Localized Attributes

<!--NI_TOPIC bundle=package-manager path=assemble-file-package.html language=enus -->
## TOPIC 00003: Assembling a File Package

- bundle_id: `package-manager`
- source_path: `assemble-file-package.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/assemble-file-package.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Assemble a File package by creating a root directory that contains subdirectories, source files, and configuration files. For detailed explanation and examples of the configuration files you include in a package, refer to the following topics: Control File Attributes Installation Target Roots for Fi

### Assembling a File Package

Assemble a File package by creating a root directory that contains subdirectories,
 source files, and configuration files.

For detailed explanation and examples of the configuration files you include in a package, refer to the following topics:

- Control File Attributes
- Installation Target Roots for File Packages
- Instructions XML for File Packages

Before you build a File package, assemble all appropriate source files and subdirectories into a single root directory.

1. Create a root directory to hold all components of the File package. 
 For example: 
 C:\temp\MyFilePkg
2. Inside the root directory, create a 
 control subdirectory. 
 For example: 
 C:\temp\MyFilePkg\control
3. Inside the 
 control subdirectory, create a control file.
  1. Using a text editor, create a new document and name it control.
  2. Enter all control file attributes and values needed for your package. 
 See [Control File Attributes](control-file-attributes.html#GUID-16D97F2A-09D6-4F28-A33C-35D1BBEC07A8) for more information
 about attributes for your control file.
  3. Enter 
 file for the 
 XB-Plugin attribute to indicate that the package is a File package.
  4. Save the file and omit the file extension.
4. Inside the root directory, create a 
 data subdirectory. 
 For example: 
 C:\temp\MyFilePkg\data
5. Inside the 
 data subdirectory, create one or more installation target subdirectories. 
 The subdirectories you create specify where Package Manager installs the files in that subdirectory. 
 For example, if you create C:\temp\MyFilePkg\data\Desktop, Package Manager installs
 any files inside that subdirectory to the Desktop.
6. (Optional) Inside the 
 data subdirectory, create an instructions file.
  1. Using a text editor, create a new document and name it instructions.
  2. Enter all appropriate elements and attributes for your package. 
 See [Instructions XML for File Packages](instructions-xml-file-packages.html#GUID-29BE2213-93C1-4281-8570-7CE1338AEB4A) for more
 information about the elements and attributes for your instructions
 file.
  3. Save the file and omit the file extension.
7. Inside the root directory, create a Debian binary file. This file declares conformity to the Debian standard. For more information, visit debian.org.
  1. Using a text editor, create a new document and name it debian-binary.
  2. Enter 2.0 .
  3. Save the file and omit the file extension.

The following figure shows an example File package where the installation target root is 
 Desktop:

[IMAGE alt='image' src='GUID-5C7DEF18-8680-4173-A3E3-858203278E98-a5.svg']

Parent topic:

Package Creation

Related concepts:

- Instructions XML for File Packages
- Package Components

Related tasks:

- Building a Package using the Command Line Interface

Related reference:

- Control File Attributes
- Installation Target Roots for File Packages

<!--NI_TOPIC bundle=package-manager path=assemble-wininst-package.html language=enus -->
## TOPIC 00004: Assembling a WinInst Package

- bundle_id: `package-manager`
- source_path: `assemble-wininst-package.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/assemble-wininst-package.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Assemble a Windows Installer (WinInst) package by creating a root directory that contains subdirectories, source files, and configuration files. For detailed explanation and examples of the configuration files you include in a package, refer to the following topics: Control File Attributes Instructi

### Assembling a WinInst Package

Assemble a Windows Installer (WinInst) package by creating a root directory that
 contains subdirectories, source files, and configuration files.

For detailed explanation and examples of the configuration files you include in a package, refer to the following topics:

- Control File Attributes
- Instructions XML for WinInst Packages

Before you build a WinInst package, assemble all appropriate source files and subdirectories into a single directory.

1. Create a root directory to hold all components of the WinInst package. 
 For example: 
 C:\temp\MyWinInstPkg
2. Inside the root directory, create a 
 control subdirectory. 
 For example: 
 C:\temp\MyWinInstPkg\control
3. Inside the 
 control subdirectory, create a control file.
  1. Using a text editor, create a new document and name it control.
  2. Enter all control file attributes and values needed for your package. 
 See [Control File Attributes](control-file-attributes.html#GUID-16D97F2A-09D6-4F28-A33C-35D1BBEC07A8) for more information
 about attributes for your control file.
  3. Enter 
 wininst for the 
 XB-Plugin attribute to indicate that the package is a WinInst package.
  4. Save the control file and omit the file extension.
4. Inside the root directory, create a 
 data subdirectory. 
 For example: 
 C:\temp\MyWinInstPkg\data
5. Inside the 
 data subdirectory, include any MSI files or executable files.
6. (Optional) Inside the 
 data subdirectory, create an instructions file.
  1. Using a text editor, create a new document and name it instructions.
  2. Enter all appropriate elements and attributes for your package. 
 See [Instructions XML for WinInst Packages](instructions-xml-wininst-packages.html#GUID-96BD71E8-354A-4892-B764-F2A0D2477666) for more
 information about the elements and attributes for your instructions
 file.
  3. Save the instructions file and omit the file extension.
7. Inside the root directory, create a Debian binary file. This file declares conformity to the Debian standard. For more information, visit debian.org.
  1. Using a text editor, create a new document and name it debian-binary.
  2. Enter 2.0 .
  3. Save the file and omit the file extension.

The following figure shows an example WinInst package:

[IMAGE alt='image' src='GUID-E7492E0D-1ACF-4B8A-AF7B-8FAD9DE9BB90-a5.svg']

Parent topic:

Package Creation

Related concepts:

- Package Components
- Instructions XML for WinInst Packages

Related reference:

- Control File Attributes

<!--NI_TOPIC bundle=package-manager path=assembling-relative-file-package.html language=enus -->
## TOPIC 00005: Assembling a Relative File Package

- bundle_id: `package-manager`
- source_path: `assembling-relative-file-package.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/assembling-relative-file-package.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Assemble a relative file package by creating a root directory that contains subdirectories, source files, and configuration files. For detailed explanation and examples of the control file you include in a package, refer to the Control File Attributes topic: Before you build a relative file package,

### Assembling a Relative File Package

Assemble a relative file package by creating a root directory that contains
 subdirectories, source files, and configuration files.

For detailed explanation and examples of the control file you include in a package, refer
 to the Control File Attributes topic:

Before you build a relative file package, assemble all appropriate source files and
 subdirectories into a single root directory.

1. Create a root directory to hold all components of the relative file package. 
 For example: C:\temp\MyRelativeFilePkg
2. Inside the root directory, create a control
 subdirectory. 
 For example: C:\temp\MyRelativeFilePkg\control
3. Inside the control subdirectory, create a control
 file.
  1. Using a text editor, create a new document and name it control.
  2. Enter all control file attributes and values needed for your package. 
 See Control File Attributes topic for more information about attributes for your
 control file.
  3. Enter relative-file for the XB-Plugin attribute to indicate that the package is a
 relative file package.
  4. Save the file and omit the file extension.
4. Inside the root directory, create a data
 subdirectory. 
 For example: C:\temp\MyRelativeFilePkg\data. 
 Package Manager installs any files inside the data
 subdirectory to the installation path. The default installation path is:
 C:\Program Files\National Instruments\NI Package
 Manager\Installed
 Use the --install-root=<DIRECTORY> option with
 install and uninstall commands to specify a
 non-default installation path.
 Note Package Manager does not display installed and available relative file packages. Use the command
 line interface to access Package Manager with relative file packages. Refer to the
 Accessing the Command Line Interface for Package Manager topic for more information.
5. (Optional) Inside the data subdirectory, create one
 or more subdirectories.
6. Inside the root directory, create a Debian binary file. This file declares conformity
 to the Debian standard. For more information, visit debian.org.
  1. Using a text editor, create a new document and name it debian-binary.
  2. Enter 2.0 .
  3. Save the file and omit the file extension.

[IMAGE alt='image' src='GUID-7325FEBA-7486-4EA4-940C-28B39228B9E5-a5.svg']

Parent topic:

Package Creation

Related concepts:

- Package Components

Related tasks:

- Building a Package Using the Command Line Interface
- Accessing the Command Line Interface for Package Manager

Related reference:

- Control File Attributes

<!--NI_TOPIC bundle=package-manager path=automate-installer.html language=enus -->
## TOPIC 00006: Automating an Installer

- bundle_id: `package-manager`
- source_path: `automate-installer.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/automate-installer.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Automate the unattended or quiet installation of an online installer, offline installer, or Package Manager using the command line interface (CLI). To make the installation process non-interactive, include the --passive option at the command prompt. Unattended mode is not fully quiet. Status dialogs

### Automating an Installer

Automate the unattended or quiet installation of an online installer, offline
 installer, or Package Manager using the command line interface (CLI).

To make the installation process non-interactive, include the --passive option at the command prompt. Unattended mode is not fully quiet.
 Status dialogs appear during the installation process, but you do not need to interact
 with them. You can use this mode when installing from a script or the command line.

--quiet

Note

Automating the Unattended Installation of
 Package Manager

An *online installer* is a lightweight executable containing no packages
 in itself, but installs a product by downloading the necessary packages from the
 internet. An *offline installer* contains the complete set of packages
 needed for the product, which are bundled into a one-time download. Since offline
 installers contain the complete contents of software, it typically takes longer to
 download.

Complete the following steps to automate the unattended installation of an online
 installer, offline installer, or Package Manager.

1. Navigate to ni.com/downloads and search for the product you want to install. If you are
 installing Package Manager, navigate to the Package Manager download page.
2. Select the product version, edition, and driver software you need, if applicable.
3. Determine the installer type you need and complete the corresponding steps to download
 and run the installer.

#### Selecting an Online Installer
 Type

Installers of this type always download as an .exe and are typically under 10 MB. This option is not
 available for all products,

1. Click
 Download if an online installer is
 available.
2. Ensure the installer is an
 executable.
3. Run Command Prompt as an
 administrator and pass one of the following commands and options: The following options are not required when using the --passive or --quiet options:
  - start "" /wait "path of install.exe" --passive --accept-eulas --prevent-reboot
  - For quiet installation, use the --quiet option instead of the --passive 
 option. start "" /wait "path of install.exe" --quiet --accept-eulas --prevent-reboot
  - To make the installation process skip any license activation,
 include the --prevent-activation 
 option in the command
 prompt. start "" /wait "path of install.exe" --prevent-activation Note License
 activation must still be performed to use any product requiring
 activation.
  - To prevent the installation process from displaying a completion
 prompt, include the --hide-completion option at the command
 prompt. start "" /wait "path of install.exe" --hide-completion
  - To install Package Manager passively but require user interaction
 for the rest of the installation, include the --autoinstall-nipkg option in the command
 prompt. start "" /wait "path of install.exe" --autoinstall-nipkg

#### Selecting an Offline Installer
 Type

Installers of this type download as an .iso file. You must either mount the .iso file or extract all of the files to a local directory before
 launching the installer. The NI Package Manager offline installer downloads as an
 .exe file and you can use the same
 command-line when launching that executable.

1. Download an offline installer in
 one of the following ways.
  - Click Individual
 Offline Installers if available.
    1. Select one of the
 offline installer options. Note Product
 versions with a higher value in the third field of a
 version include patch fixes. For example:
 23.0.1.
    2. Click
 Download .
    3. Wait until the
 installer finishes downloading before completing the next
 step.
  - Click the title of the
 latest version of the product you are installing.
    1. Click the download
 link to download your offline installer.
    2. Proceed once the
 installer has finished downloading.
2. Run Command Prompt as an
 administrator and change to the directory in which you downloaded your
 installer using the cd command. For
 example:
 cd "C:\Users\lvadmin\downloads"
3. Pass one of the following commands
 and arguments: The following options are not required when using the --passive or --quiet options:
  - start "" /wait "path of install.exe" --passive --accept-eulas --prevent-reboot
  - For quiet installation, use the --quiet option instead of the --passive 
 option. start "" /wait "path of install.exe" --quiet --accept-eulas --prevent-reboot
  - To make the installation process skip any license activation,
 include the --prevent-activation 
 option in the command
 prompt. start "" /wait "path of install.exe" --prevent-activation Note License
 activation must still be performed to use any product requiring
 activation.
  - To prevent the installation process from displaying a completion
 prompt, include the --hide-completion option at the command
 prompt. start "" /wait "path of install.exe" --hide-completion
  - To install Package Manager passively but require user interaction for the rest of the
 installation, include the --autoinstall-nipkg option in the command
 prompt. start "" /wait "path of install.exe" --autoinstall-nipkg

#### Verifying the Installer

echo
 %errorlevel%

Note

- A return code of 0 indicates that you
 successfully installed the software.
- A return code of -125071 indicates that
 you successfully installed the software but are required to reboot your
 machine.
- A return code of -126300 indicates that
 you only installed Package Manager and must reboot your machine and then
 rerun the installer to complete the software installation.

#### Troubleshooting

```text
start "" "path to install.exe" /?
```

Parent topic:

Package Installation

Related reference:

- Troubleshooting Problems with Installing, Updating, Repairing, or Removing NI Software

Related information:

- Software and Driver Downloads
- Package Manager Download
- Automating the Unattended Installation of NI Package Manager

<!--NI_TOPIC bundle=package-manager path=build-package-using-cli.html language=enus -->
## TOPIC 00007: Building a Package Using the Command Line Interface

- bundle_id: `package-manager`
- source_path: `build-package-using-cli.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/build-package-using-cli.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the command line interface to build a package with your source files. Before you build a package, you must assemble the intended source files and subdirectories into a single directory. Open a command prompt. Change directories to the location of Package Manager. The default location is C:\Progr

### Building a Package Using the Command Line
 Interface

Use the command line interface to build a package with your source files.

Before you build a package, you must assemble the intended source files and subdirectories into a single directory.

1. Open a command prompt.
2. Change directories to the location of Package Manager. 
 The default location is C:\Program Files\National
 Instruments\NI Package Manager.
3. Run the following command: nipkg
 pack "<directory
 containing package source files>" "<destination of .nipkg file>". 
 For example, if you enter nipkg pack
 "C:\temp\MyTestPackage"
 "C:\temp", Package Manager creates the .nipkg file in the temp
 directory.

Parent topic:

Package Creation

Related concepts:

- Package Components

Related tasks:

- Accessing the Command Line Interface for Package Manager
- Assembling a File Package
- Assembling a WinInst Package
- Assembling a EULA Package

<!--NI_TOPIC bundle=package-manager path=cli-package-manager.html language=enus -->
## TOPIC 00008: Accessing the Command Line Interface for Package Manager

- bundle_id: `package-manager`
- source_path: `cli-package-manager.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/cli-package-manager.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Modify the execution of Package Manager processes by using the Package Manager command line interface nipkg.exe or the Package Manager GUI command-line NIPackageManager.exe. You can use the CLI for the following purposes: Silently install, update, repair, or remove NI software Build and manage packa

### Accessing the Command Line Interface for
 Package Manager

Modify the execution of Package Manager processes by using the Package Manager
 command line interface nipkg.exe or the Package Manager GUI
 command-line NIPackageManager.exe.

You can use the CLI for the following purposes:

- Silently install, update, repair, or remove NI software
- Build and manage packages
- View the current state of your system
- Run the GUI in browse or command mode

1. Open a command prompt window.
2. Navigate to C:\Program Files\National Instruments\NI Package
 Manager by typing the following into the command line and pressing
 Enter: 
 cd C:\Program Files\National Instruments\NI Package Manager
3. Access the Package Manager CLI.
  - Package Manager CLI by typing the following and pressing
 Enter: nipkg.exe
    1. To access the built-in CLI help, type nipkg help .
    2. Press Enter. Note For help on a specific command,
 type nipkg help <command>. For example, type the following to access help for
 the install 
 command. nipkg help install
  - Package Manager GUI by typing the following and pressing
 Enter: NIPackageManager.exe
    1. To access built-in browse mode and command mode help, type
 one of the following:
      - NIPackageManager.exe /?
      - NIPackageManager.exe --help
    2. Press Enter.
4. Execute supported commands on the Package Manager CLI or GUI.

#### Package Manager CLI Supported
 Commands

The Package Manager CLI supports a list of commands that you can use to adjust the
 behavior of Package Manager.

```text
NI Package Manager Command-Line Interface manages the installation of software packages.

Usage: nipkg help <command>
       nipkg <command> [OPTIONS] [arguments]
       nipkg (install|remove) [OPTIONS] <package>...
       nipkg update [OPTIONS] [feed-name]

Commands
        help - Print help message
        download - Download a package
        info - Show attributes for available packages
        info-installed - Show attributes for installed packages
        install - Installs a package
        repair - Repairs packages
        remove - Uninstalls previously installed package(s)
        upgrade - Upgrades installed packages
        list - Show a list of (or search) available packages
        list-fields - Show package attributes
        list-installed - Show a list of installed packages
        list-providers - List packages that provide the requested package specification(s)
        list-upgradable - Show a list of available upgrades
        list-source-feeds - Show the list of feeds that contain the specified package names
        lock - Prevents installed package(s) from being upgraded or removed
        unlock - Allows installed package(s) to be upgraded and removed
        pack - Creates or packs a package
        unpack - Unpacks an existing package
        get-from-cache - Get the .nipkg file from the installed packages cache
        get-dependencies - List dependencies of specified packages
        update - Updates the local cache
        feed-download - Download a feed
        feed-add - Adds an existing feed to the current configuration
        feed-remove - Removes a feed from the current configuration
        feed-create - Creates a new feed
        feed-add-absolute-package - Adds an absolute reference to a package to a feed
        feed-add-pkg - Adds one or more packages to a feed
        feed-remove-pkg - Removes one or more packages from a feed
        feed-edit - Edit the configuration for an existing feed
        feed-info - Prints detailed information about a feed
        feed-list - Lists the configured package feeds
        config-get - Get local configuration parameters
        config-set - Set a local configuration parameter
        compare-versions - Compare version strings
        show-version - Print version
```

#### Configuration Options

You can use the CLI for Package Manager (nipkg.exe) to configure
 behavior settings using the config-set command.

config-set

nipkg.ini

%LOCALAPPDATA%\National
 Instruments\NI Package Manager

--system

config-set

nipkg.ini

%PROGRAMDATA%\National Instruments\NI Package
 Manager\Settings

Note

```text
nipkg.exe config-set [ATTRIBUTE] [VALUE]
```

Note

nipkg.exe help
 config-set

| Purpose | nipkg config-set Attribute Name | Additional Info |
| --- | --- | --- |
| (Introduced in Package Manager 2023 Q3)Enables Package Manager features that automatically connect to ni.com | nipkg.enable-NI-connectivity | The default value is true. Set this option to false to disable features that contribute to timeout delays, especially on systems that do not connect to ni.com. When false: The Browse Products tab is hidden NI-managed feeds are disabled, automatic download of missing packages from ni.com is disabled Online installers downloaded from ni.com will error |
| Copies installed packages to cache | nipkg.cachepackages | The default value is true. Disabling this setting does not remove previously cached packages.Note Cached packages are required to repair packages and for building feeds and installers in LabVIEW and similar tools. The location of the package cache directory is: %PROGRAMDATA%\\National Instruments\\NI Package Manager\\Packages |
| Removes package from cache when the package is removed | nipkg.uncacheuninstalledpackages | The default value is true. Enabling this setting does not remove previously cached packages. If enabled, upgrading Package Manager automatically removes any package in cache that is not installed. The location of the package cache directory is: %PROGRAMDATA%\\National Instruments\\NI Package Manager\\Packages |
| Logs network traffic with remote servers | nipkg.curldebugfile-enable | The default value is false. cURL logs are created in %LOCALAPPDATA%\\National Instruments\\NI Package Manager\\Logs\\WinInstMSI.For more information, see the article Generating and Locating NI Package Manager Error Logs. |
| Downloads and installs missing dependencies from ni.com | nipkg.nipkgui.automatically-install-missing-dependencies | The default value is true. This setting is ignored when nipkg.enable-NI-connectivity is set to false. |
| Displays the Browse Products tab in Package Manager | nipkg.nipkgui.enable-browse-products | The default value is true. This setting is ignored when nipkg.enable-NI-connectivity is set to false. |
| Enables MSI logging for WinInst packages | nipkg.plugin.wininst.msilogs-enabled | The default value is false. For more information, see the article Generating and Locating NI Package Manager Error Logs. |
| Directory for MSIs log files | nipkg.plugin.wininst.msilogs-directory | This directory is located at %LOCALAPPDATA%\\National Instruments\\NI Package Manager\\Logs\\WinInstMSI. For more information, see the article Generating and Locating NI Package Manager Error Logs. |
| Disables the Windows Fast Startup power option | nipkg.plugin.wininst.override-windows-fast-startup | The default value is true. Package Manager sets this attribute to false when: The Settings pane is dismissed. The "Ask to disable Windows Fast Startup when installing software" option is unchecked. For more information on Windows Fast Startup, see the article Hardware Not Detected After Upgrading Windows Version. |
| Specifies the proxy server that Package Manager uses to download packages | nipkg.proxyserver | The format of the value is server:port. server specifies a valid server name or IP address and port specifies the port number. If you do not specify this value, Package Manager attempts to query the OS for a proxy configuration. |

Related information:

- Generating and Locating NI Package Manager Error Logs
- Hardware Not Detected After Upgrading Windows Version

<!--NI_TOPIC bundle=package-manager path=control-file-attributes.html language=enus -->
## TOPIC 00009: Control File Attributes

- bundle_id: `package-manager`
- source_path: `control-file-attributes.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/control-file-attributes.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: A control file is a text file without an extension that contains metadata describing properties and relationships of the package, such as its name, version, type, and dependencies. Both File packages and WinInst packages require a control file. Package Manager generates the package according to the

### Control File Attributes

A control file is a text file without an extension that contains metadata describing
 properties and relationships of the package, such as its name, version, type, and
 dependencies. Both File packages and WinInst packages require a control file. Package Manager
 generates the package according to the metadata in the control file.

| Attribute Name | Required | Type | Default | Description | Example |
| --- | --- | --- | --- | --- | --- |
| Architecture | Yes | String | N/A | Indicates the OS architecture supported by the package.Expected values: windows_x64 (Installable only on a 64-bit Windows) windows_all (Deprecated with the removal of 32-bit Windows) | Architecture: windows_allNote You can only specify one architecture per package. |
| Conflicts | No | String relationship array | NULL | Declares a conflict between one binary package and another.Package Manager does not install conflicting packages on a system at the same time.For packages with XB-Plugin set to eula, you can prevent the EULA package from being installed on disk by setting this value to ni-package-manager. | See the String Relationship Array section for an example. |
| Depends | No | String relationship array | NULL | Declares an absolute dependency. windows_x64 packages should only depend on windows_x64 and windows_all packages. windows_all packages should only depend on windows_all packages. Special package system-windows-x64 can be used as a placeholder for 64-bit dependencies. | See the String Relationship Array section for an example. |
| Description | Yes | Multi-line | N/A | Provides a description of the binary package.Consists of two parts: the single-line synopsis and the multi-line long description.NI recommends using two white space characters between the synopsis and the long description to improve readability.You can optionally specify localized text. See Localized Attributes. | See the Multi-line Attributes section for an example. |
| Enhances | No | String relationship array | NULL | Declares that a package enhances the functionality of another package.Only use this attribute in packages that have XB-UserVisible set to yes. | See the String Relationship Array section for an example. |
| Homepage | No | String | NULL | The URL that the package vendor uses to provide more detailed information about the package. | Homepage: http://www.ni.com |
| Installed-Size | No | Long integer | 0 | Provides an estimate of the total amount of disk space required to install the package.Expected value: an integer value of the estimated install size in bytes, divided by 1024 and rounded up. | Installed-Size: 25485141 |
| Maintainer | Yes | String | N/A | The package maintainer's name and email address.Expected values: the name of the maintainer followed by the email address inside angle brackets. | Maintainer: National Instruments <support@ni.com> |
| Package | Yes | String | N/A | Specifies a unique identification for a package.A package name must be a unique, user friendly string that a customer would type on the command line and meet the following requirements: Consist only of lower case letters (a-z), digits (0-9), plus (+) and minus (-) signs, and periods (.) Start with an alphanumeric character Must not contain uppercase letters Have a min length of two characters Have a max length of 58 characters Expected values: Match the regular expression ^[a-z0-9][a-z0-9.+-]{2,}$ NI recommends that you start the name of your package with your company name followed by a dash (ex: ni-testpackage) | Good syntax: Package: ni-labview-2015 Package: ni-daqmx Package: ni-daqmx-labview-2015-support Incorrect syntax: Package: LabVIEW_2015 Package: NationalInstrumentsGPIB Package: labview |
| Provides | No | String relationship array | NULL | Declares that the package satisfies an absolute dependency of another package. | See the String Relationship Array section for an example. |
| Recommends | No | String relationship array | NULL | Declares a strong dependency that is not absolute.Lists packages that would be installed with this one in most situations.Only recommend packages with XB-UserVisible set to yes. | See the String Relationship Array section for an example. |
| Replaces | No | String relationship array | NULL | Declares that the package replaces other packages.Conflicts should be used in conjunction with Replaces. | See the String Relationship Array section for an example. |
| Section | No | String | NULL | Specifies the category in which the package is classified.Expected values: Programming Environments Application Software Add-Ons Drivers Runtime Utilities Documentation Infrastructure For packages that set XB-Plugin to eula, you must set this value to Infrastructure. See Assembling a EULA Package for more information about creating EULA packages. | Section: Application Software |
| Suggests | No | String relationship array | NULL | Declares that one package may be more useful with one or more other packages.Notifies Package Manager and the user that the listed packages are related to this one, but not required.Only suggest packages with XB-UserVisible set to yes. | See the String Relationship Array section for an example. |
| Supplements | No | String relationship array | NULL | Declares that a package supplements the functionality of another package.Only use this attribute in packages that have XB-UserVisible set to yes. | See the String Relationship Array section for an example. |
| Version | Yes | String | N/A | Specifies the version number of the package.Use the debian format. For more information, visit https://www.debian.org. | Version: 17.1.0.1 |
| XB-DisplayName | No | String | NULL | User friendly package name.You can optionally specify localized text. See Localized Attributes. | XB-DisplayName: NI LabVIEW 2017 |
| XB-DisplayVersion | No | String | NULL | User friendly display version. | XB-DisplayVersion: 15.0.0 |
| XB-Eula | No | String relationship array | NULL | Declares which EULA packages the package requires. | XB-Eula: eula-mycompany, eula-ni-standard |
| XB-EulaTitle | No | String | NULL | Specifies the displayed title of the EULA package. Use this attribute only in packages that have XB-Plugin set to eula | XB-EulaTitle: My Software Name |
| XB-MessageCondition-# For example:XB-MessageCondition-1, XB-MessageCondition-2, etc. | No | String | N/A | Specifies a condition for when the corresponding message will show in Package Manager.Only MSI conditions are accepted and should be enclosed in <msi>...</msi> tags. Unless enclosed in a CDATA block, text within the tags needs to have '<' and '>' characters escaped as '<' and '>'. | XB-MessageCondition-1: <msi>VISA32COMPANYNAME ~<> "National Instruments"</msi> XB-MessageCondition-2: <msi><![CDATA[VISA32COMPANYNAME ~<> "National Instruments"]]></msi> |
| XB-MessageText-# For example: XB-MessageText-1, XB-MessageText-2, etc. | No | Multi-line | N/A | Contains an important message that Package Manager displays before installing the package.Consists of two parts, a header and a body.You can specify a condition for displaying this message by using the corresponding MessageCondition attribute below. If you do not specify a condition, this message will always show when you install this package.NI recommends you create preformatted text for each line of the body using two spaces at the beginning of each line.You can optionally specify localized text. See Localized Attributes. | XB-MessageText-1: This is my message headerThis is my message body.There are multiple lines. |
| XB-OsRequires | No | String | N/A | Declares which OS versions the package requires.If you do not specify XB-OsRequires, all OSs Package Manager currently supports are allowed.Define the OS bitness restriction using the Architecture attribute.If the OS of a system cannot satisfy XB-OsRequires for a package, the Package Manager GUI does not display the package.If a package has a dependency with a more restrictive XB-OsRequires, the package inherits the more restrictive OS requirement. | See the OS Requirement section for an example. |
| XB-Plugin | Yes | String | NULL | The Agent used to install the package.Expected values: eula file wininst relative-file | XB-Plugin: file |
| XB-ReleaseNotes | No | Multi-line | NULL | Release notes for the package.You can optionally specify localized text. See Localized Attributes. | See the Multi-line Attributes section for an example. |
| XB-StoreProduct | No | Boolean | no | Specifies whether the package is a product in Package Manager.You must set the value to yes for your package to appear in the Installed and Packages tabs when Products Only is checked.Expected values: no yes | XB-StoreProduct: no |
| XB-UserVisible | No | Boolean | no | Specifies whether Package Manager displays the package.Expected values: no yes You must set the value to no for packages that set XB-Plugin to eula. See Assembling a EULA Package for more information about creating EULA packages. | XB-UserVisible: no |
| XB-VisibleForRuntimeDeployment | No | Boolean | no | Specifies whether NI Package Builder displays the package by default when dependencies are added.Expected values: no yes | XB-VisibleForRuntime: yes |

Parent topic:

Package Components

Related tasks:

- Assembling a EULA Package
- Assembling a Relative File Package

#### String Relationship Array

Package Manager expects a string relationship array, or a list of package names separated by commas, as the value of control file attributes that declare relationships.

Format these attribute values according to the following syntax rules:

- Separate package names using commas.
- Separate alternative package names for any dependency using vertical bars. This indicates that any one of the alternative packages listed satisfies the dependency.
- Include version requirements for a package in parenthesis following the name of the package. You can restrict the applicability of each package to particular versions in all of the string relationship array fields except for 
 Provides .
- Inside the parenthesis, use one of the following
 operators followed by a version number to indicate the relationship between the package and
 version. You can use white space in the version specification.

| Operator | Relationship |
| --- | --- |
| << | strictly earlier |
| <= | earlier or equal |
| = | exactly equal |
| >= | later or equal |
| >> | strictly later |
| != | excluding |

In the following example, the 
 Depends attribute declares a dependency on package01 version 2.2.1 or later, and states that package03 is an alternative package that satisfies the dependency on package02.

Depends: package01 (>= 2.2.1), package02 | package03

#### Multi-line Attributes

The value of a multi-line attribute consists of a single-line synopsis followed by additional lines that provide an extended description.

The first line of a multi-line attribute is reserved for the attribute name followed by a single-line synopsis. Provide a short description or heading for this portion of the attribute. 
 XB-ReleaseNotes attributes do not use a single-line synopsis.

The extended description contains additional details you provide for the attribute. Format the extended description of a multi-line attribute according to the following rules:

- Create a paragraph using a single space at the beginning of a line. When displaying this text, the displaying program removes the leading space and uses word wrapping. A paragraph must contain at least one non-whitespace character.
- Preserve whitespace and line breaks within text using two or more spaces at the beginning of a line. If the display area does not scroll horizontally and a line is too long to fit, the displaying program creates line breaks where necessary.
- Create a blank line using a single space followed by a period.

The following text provides an example of how you can use the formatting rules for multi-line attributes to enter text for the 
 Description element:

```text
      Description: Example of multi-line attribute contents.
 The single space at the beginning of this line creates a paragraph. 
 .
  The double space at the beginning of these lines creates preformatted
  text that preserves whitespace and line breaks.
```

#### OS Requirement

The XB-OsRequires version contains up to three integer
 fields for Windows operating system versions. The first two fields correspond to
 Windows operating system versions as specified by Microsoft on [Operating System Version](https://docs.microsoft.com/en-us/windows/win32/sysinfo/operating-system-version). The third field is only applicable to the
 Windows 10 operating system builds as specified by Microsoft on [Windows
 10 release information](https://docs.microsoft.com/en-us/windows/release-information/).

Format the attribute fields according to the following syntax rules:

- Separate fields using periods.
- Separate multiple requirements using commas.
- Specify alternative requirements using vertical bars.
 Vertical bars take precedence over commas.
- The following operators are supported by this
 attribute: OperatorRelationship<<less than<=less than or equal to=equal to>=greater than or equal to>>greater than!=excluding

XB-OsRequires

| Example | Resulting Requirement |
| --- | --- |
| XB-OsRequires: >=6.3 | Requires Windows 8.1 or newer |
| XB-OsRequires: >=10.0, !=10.0.18363 | Requires Windows 10 or newer, but not Windows 10 version 1909 |
| XB-OsRequires: >=6.3, <10 \| >=10.0.18363 | Requires Windows 8.1 or newer and either the OS is older than Windows 10, or it is Windows 10 version 1909 or newer |

Related tasks:

- Assembling a File Package
- Assembling a WinInst Package

#### Localized Attributes

Description, display name, release notes, and message text appears localized in the
 Package Manager user interface when you include versions of the attributes that are appended
 with a language-specific suffix.

The Package Manager GUI displays localized text for the Description, XB-DisplayName,
 XB-ReleaseNotes, and XB-MessageText attributes when you include localized versions of
 these attributes. Localized versions of these attributes are appended with a hyphen and
 a language-specific suffix to the attribute name. If there is no language-specific
 attribute that matches the language of the Package Manager GUI, the non-localized
 attribute text is used.

```text
DisplayName: LabVIEW (64-bit) English
DisplayName-de: LabVIEW (64 Bit) – Englisch
DisplayName-es: LabVIEW (64 bits) – Español
DisplayName-fr: LabVIEW (64 bits) – Anglais
DisplayName-it: LabVIEW (64 bit) – Italiano
DisplayName-ja: LabVIEW (64ビット) 英語版
DisplayName-ko: LabVIEW (64비트) 영어 버전
DisplayName-zh-CN: LabVIEW（64位）英语版
```

<!--NI_TOPIC bundle=package-manager path=creating-feed.html language=enus -->
## TOPIC 00010: Creating a Feed

- bundle_id: `package-manager`
- source_path: `creating-feed.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/creating-feed.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Create feeds to distribute multiple packages that have dependencies on one another and consolidate package file updates in one location. Place one or more packages (.nipkg) in a single source directory. The packages in the feed can be any mix of package types. If a package depends on packages hosted

### Creating a Feed

Create feeds to distribute multiple packages that have dependencies on one another and consolidate package file updates in one location.

1. Place one or more packages (.nipkg) in a single source directory. 
 The packages in the feed can be any mix of package types. Note If a package depends on
 packages hosted on ni.com, you do not need to include these packages in your
 feed. Package Manager automatically downloads and installs dependencies from
 ni.com.
2. Open a command prompt.
3. Change directories to the location of Package Manager. 
 The default location is 
 C:\Program Files\National Instruments\NI Package Manager.
4. Run the following command: nipkg
 feed-create "<target location of
 feed>" "<location of source
 directory>". 
 For example, if you enter C:\Program Files\National Instruments\NI Package
 Manager> nipkg
 feed-create
 "C:\temp\myTestFeed"
 "C:\temp\myTestPackage", Package Manager creates the
 feed manifest files in the C:\temp\myTestFeed directory using the
 package files in C:\temp\myTestPackage.
5. Place the source directory in a location that is accessible to your intended recipients, such as a network file server.

Parent topic:

Package Distribution

Related concepts:

- Package Creation

Related tasks:

- Installing Packages from a Feed

<!--NI_TOPIC bundle=package-manager path=extended-support-changes.html language=enus -->
## TOPIC 00011: Updates and Changes for Package Manager Extended Support Versions

- bundle_id: `package-manager`
- source_path: `extended-support-changes.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/extended-support-changes.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Browse updates and changes made in Package Manager versions on extended support. If you cannot find changes for your version, it might be a more recent version, documented as a new feature. Or, your version might not have included user-facing updates. You can find more information about non-visible

### Updates and Changes for Package Manager Extended Support Versions

Browse updates and changes made in Package Manager versions
 on extended support.

Note

Release Notes

#### Package Manager 2023 Q2

##### New Features

- .NET Framework 4.8 now installs with NI Software.
- Improved performance by minimizing wait times for package download during online
 installation.

#### Package Manager 2022 Q4

##### New Features

- New command-line option—Use the command-line option
 --exclude-dependencies for repairing only packages
 listed in the command from the Package Manager CLI. Refer to Accessing the Command Line Interface for Package
 Manager for more information about how to access the built-in
 help.
- A status bar now displays the number of selected packages on each tab in
 Package Manager.

##### Behavior Changes

- You can perform installations, repairs, and updates to all software packages you
 select including software hidden by filtering and search.

#### Package Manager 20.7, 21.0, 21.3, 21.8, and
 2022 Q3

##### New Features

New command-line option—Use the command-line option --quiet for
 fully silent installation from Package Manager online installers, offline
 installers, and the main Package Manager GUI. Refer to Accessing the Command Line Interface for Package Manager
 for more information about how to access the built-in help.

##### Behavior Changes

- BROWSE PRODUCTS tab reintroduced—Package Manager
 reintroduces the BROWSE PRODUCTS tab, which was removed
 in Package Manager 20.6, to align with customer workflows and processes.
- Changes to Windows support—Package Manager drops support for Windows 7, Windows
 8.1, Windows Server 2008 R2, Windows Server 2012, and all 32-bit Windows
 operating systems. Package Manager adds support for Windows Server 2019. Due to
 the supported OS changes, upgrading Package Manager or installing most 2021 NI
 software will cause all deployment installers built in LabVIEW, TestStand, NI
 Package Builder, or LabWindows/CVI to now only support Windows 10 64-bit
 (version 1507) or newer. For detailed information about NI operating system
 support, visit ni.com/r/win32bitsupport .
- Requirements for offline installers—Users scripting offline installers must use
 the command-line option --accept-eulas if using the options
 --quiet or --progress-only .

#### Package Manager 20.6

##### New
 Features

Add arguments to shortcuts—Use the optional attribute arguments to
 add arguments to shortcuts that Package Manager creates during installation. Refer
 to Instructions XML for File Packages for more
 information.

New control file attribute—Use the new value relative-file of the
 control file attribute XB-Plugin to install all files in a folder
 relative to the root of the installation target directory. Refer to Assembling a Relative File Package and Control File Attributes for more information.

##### Behavior Changes

BROWSE PRODUCTS

Browse Products

ni.com/downloads

#### Package Manager 20.5

##### New
 Features

Define operating system requirements for packages—Use the
 attribute XB-OSRequires to specify the operating systems the
 package supports. Refer to Control File Attributes for more
 information.

##### Behavior Changes

NI Package Manager 20.5 does not have new behaviors.

#### Package Manager 20.1

##### Behavior Changes

NI Package Manager enables the Automatically download and install missing
 dependencies from ni.com setting by default. This setting allows
 Package Manager to search for, download, and install missing dependencies from
 ni.com for both installation and upgrade operations.

<!--NI_TOPIC bundle=package-manager path=install-packages-from-feed.html language=enus -->
## TOPIC 00012: Installing Packages from a Feed

- bundle_id: `package-manager`
- source_path: `install-packages-from-feed.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/install-packages-from-feed.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: To install packages from a feed, you register the feed and install it from the Packages tab. Open Package Manager and click (Settings). Select the checkbox for Show available packages and feed management tools. Package Manager displays General and Feeds sections in the Settings dialog box. In the Fe

### Installing Packages from a Feed

To install packages from a feed, you register the feed and install it from the 
 Packages tab.

1. Open Package Manager and click 
 [IMAGE alt='image' src='GUID-A72D394C-BE86-4461-8107-B928D011C8A9-a5.png'] (Settings).
2. Select the checkbox for 
 Show available packages and feed management tools. 
 Package Manager displays General and Feeds sections in the 
 Settings dialog box.
3. In the Feeds section, click 
 Add.
4. In the 
 Add feed dialog box, enter a name for the feed and the feed path. Click 
 Add.
5. Open the 
 Packages tab, select the checkbox for each package you want to install and then click 
 Install. 
 Tip Remove the checkmark from
 the Products Only checkbox to view all available packages.
 Note Performing an installation applies to all selected packages including packages
 hidden by filtering and search.
6. Follow instructions in the installation prompt to complete installation. 
 Note 
 The Packages tab lists packages that are not installed but are available from the
 registered feeds in Package Manager. The Packages tab only lists the highest versions
 available for packages. The Updates tab lists all packages available for installed
 packages. The Packages tab may include packages whose dependent packages are not
 located in the registered feeds. Package Manager attempts to connect to ni.com to
 locate missing dependencies during installation.

Parent topic:

Package Installation

Related tasks:

- Creating a Feed

<!--NI_TOPIC bundle=package-manager path=install-remove-upgrade.html language=enus -->
## TOPIC 00013: Installing, Updating, Repairing, and Removing NI Software

- bundle_id: `package-manager`
- source_path: `install-remove-upgrade.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/install-remove-upgrade.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use Package Manager to install, update, repair, and remove NI software. Installing NI Software Use Package Manager to install available NI software. Refer to Can I Change the Installation Folder of My Software in NI Package Manager? for information on changing default install locations. On the BROWS

### Installing, Updating, Repairing, and
 Removing NI Software

Use Package Manager to install, update, repair, and remove NI software.

#### Installing NI Software

Use Package Manager to install available NI software.

Note

Can I Change the
 Installation Folder of My Software in NI Package Manager?

1. On the BROWSE PRODUCTS tab, click a product category to
 display available products in that category.
2. Select the product that you want to install and click
 INSTALL. 
 Package Manager may recommend additional software that adds functionality to
 the product you are installing, though suites may require you to select
 products before you see recommended additional software. Items that are
 checked by default are most strongly recommended. You may lack certain
 support or functionality if you decline to install these additional items.
 For example, if you have LabVIEW installed and you install a driver, Package
 Manager recommends driver support for LabVIEW. If you decline to install
 driver support, you will be unable to develop applications with that driver
 in LabVIEW.
 Note To download instrument
 drivers for most NI software, launch your software, plug in your hardware,
 and follow the instructions provided by your software.
3. Complete the remaining installation steps as prompted.

Related information:

- Can I Change the Installation Folder of My Software in NI Package
 Manager?

#### Updating NI Software

Use Package Manager to update NI software installed on your system, including Package
 Manager itself.

1. On the UPDATES tab, select the software that you want to
 update and click UPDATE. 
 If the software you want to update is not displayed on the
 UPDATES tab, you must update the software using NI Update Service
 or check the BROWSE PRODUCTS tab for a newer version of the
 product.Tip Select the
 checkbox at the top of the table and click UPDATE to update all
 NI software including software hidden by filtering and search.
2. Complete the remaining update steps as prompted. 
 Note 
 The Updates tab does not list packages whose dependent packages are not located in
 the registered feeds in Package Manager.

#### Repairing NI Software

Use Package Manager to repair NI software installed on your system if the
 software does not run correctly. Software may not run correctly due to corrupt or
 missing files.

1. On the INSTALLED tab, select the NI software that you want
 to repair and click REPAIR. 
 Tip Select the checkbox at the
 top of the table and click REPAIR to repair all NI software
 including software hidden by filtering and search. 
 Package Manager may recommend additional software to repair. You can
 de-select the items that you do not want to repair. But you may encounter issues
 using the software if you decline to repair these additional items.
2. Complete the remaining repair steps as prompted. 
 Note 
 Package Manager by default repairs all specified packages and their dependent
 packages. If dependencies do not require repair, streamline the process and use the
 --exclude-dependencies option in the Package Manager CLI. Enter
 nipkg help repair to the CLI for more information.

#### Removing NI Software

You use Package Manager to remove NI software installed on your system.

1. On the INSTALLED tab, select the software that you want to remove
 and click REMOVE. 
 Tip Select the checkbox at the
 top of the table and click REMOVE to remove all NI software
 including software hidden by filtering and search.
2. Complete the remaining removing steps as prompted.

Related reference:

- Troubleshooting Problems with Installing, Updating, Repairing, or Removing NI Software

<!--NI_TOPIC bundle=package-manager path=install-single-package.html language=enus -->
## TOPIC 00014: Installing a Single Package

- bundle_id: `package-manager`
- source_path: `install-single-package.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/install-single-package.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: You can install a single package on any system with Package Manager installed. Double click the package file to open Package Manager. Follow instructions in the installation prompt to complete installation.

### Installing a Single Package

You can install a single package on any system with Package Manager installed.

1. Double click the package file to open Package Manager.
2. Follow instructions in the installation prompt to complete installation.

Parent topic:

Package Installation

Related concepts:

- Package Creation

<!--NI_TOPIC bundle=package-manager path=installation-target-roots.html language=enus -->
## TOPIC 00015: Installation Target Roots for File Packages

- bundle_id: `package-manager`
- source_path: `installation-target-roots.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/installation-target-roots.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: The directories you create inside the data folder inform Package Manager where to install the files when you build packages.If you create a subdirectory inside a target root, Package Manager will create the subdirectory on the target system. Packages with Architecture values windows_all cannot use 6

### Installation Target Roots for File Packages

The directories you create inside the data folder inform Package Manager where to
 install the files when you build packages.If you create a subdirectory inside a
 target root, Package Manager will create the subdirectory on the target system.

Packages with Architecture values windows_all cannot use
 64-bit only target roots like ProgramFiles_64 or LV2017DIR64. Package Manager will error regardless of OS if these
 roots are encountered. Packages with Architecture value windows_x64 can use both 32- and 64-bit roots.

#### Custom
 Paths

A *custom* path is an absolute path or network path that cannot be specified by
 a Windows-standard location or an NIPath target root. Configure a custom path in the
 instructions file and use the custom path name where a target root path can be specified. A
 custom path's name and value are not shared with other packages.

#### Windows-Standard Locations

Note

| Target Root | Name in File Package | Default Folder |
| --- | --- | --- |
| Home | Home | %SystemDrive%\\Users\\Public or %PUBLIC% |
| Desktop | Desktop | %PUBLIC%\\Desktop |
| Documents | Documents | %PUBLIC%\\Documents |
| ProgramData | ProgramData | %SystemDrive%\\ProgramData |
| Startup | Startup | %ProgramData%\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp |
| ProgramMenu | ProgramMenu | %ProgramData%\\Microsoft\\Windows\\Start Menu\\Programs |
| ProgramFiles | ProgramFiles ProgramFiles_32 ProgramFiles_64 | 64-bit OS: _32 = %SystemDrive%\\Program Files (x86) _64 (or no suffix) = %SystemDrive%\\Program Files ProgramFiles is equivalent to ProgramFiles_64. |
| System | System System_32 System_64 | 64-bit OS: _32 = %windir%\\SysWOW64 _64 (or no suffix) = %windir%\\system32 System is equivalent to System_64. |
| BootVolume | BootVolume | %SystemDrive% |
| NIPkgMgrTemp | NIPkgMgrTemp | %TEMP%\\NIPackageManager Note Package Manager deletes files installed in this folder after the package installation completes. Therefore, use this root only for customExecute paths. Do not use this root with a customExecute that runs the uninstall step. When installing multiple packages, this root installs all files in the default folder. Use this root if there are dependencies among the packages. For example, if package 3 relies on files in package 1 and 2, use this root to ensure that the three packages are installed in the same folder so that package 3 can access the dependency files in package 1 and 2. |
| NIPkgMgrTempUnique | NIPkgMgrTempUnique | %TEMP%\\NIPackageManager\\Temporary unique sub-directory per transaction Note Package Manager deletes files installed in this folder after the package installation completes. Therefore, use this root only for customExecute paths. Do not use this root with a customExecute that runs the uninstall step. |

#### Toggling Paths

toggling

ProgramFiles

System

NIPaths

Note

#### NIPaths Target Roots

NIPaths target roots are always prefixed
 by ni-paths.

Note

NIPaths

NIPaths

| Target Root | Name in File Package | Default Folder |
| --- | --- | --- |
| CVI2020DIR | ni-paths-CVI2020DIR | [NIDIR]CVI2020 |
| CVI2020PUBAPPDATADIR | ni-paths-CVI2020PUBAPPDATADIR | [NIPUBAPPDATADIR]CVI2020 |
| CVI2020PUBDOCSDIR | ni-paths-CVI2020PUBDOCSDIR | [NIPUBDOCSDIR]CVI2020 |
| FLEXLOGGERDIR64 | ni-paths-FLEXLOGGERDIR64 | [NIDIR64]FlexLogger\\ |
| IVISTANDARDROOTDIR | ni-paths-IVISTANDARDROOTDIR | [Program Files_32]\\IVI Foundation\\IVI\\ |
| IVISTANDARDROOTDIR64 | ni-paths-IVISTANDARDROOTDIR64 | [ProgramFiles_64]\\IVI Foundation\\IVI\\ |
| LVXXXXDIR64 | ni-paths-LVXXXXDIR64 | [NIDIR64]\\LabVIEW XXXXNote Example: For the target root LV2018DIR64 the name in file package is ni-paths-LV2018DIR64 and the default folder is [NIDIR64]\\LabVIEW 2018. |
| MSTUDIODIR | ni-paths-MSTUDIODIR | [NIDIR]\\Measurement Studio\\ |
| NIADDONSDIR64 | ni-paths-NIADDONSDIR64 | [NIDIR64]\\Addons\\ |
| NIFPGA51DIR64 | ni-paths-NIFPGA51DIR64 | [BootVolume]\\NIFPGA\\ |
| NILEGALROOTDIR | ni-paths-NILEGALROOTDIR | [NIDIR]\\ |
| NILMLICENSESDIR | ni-paths-NILMLICENSESDIR | [NIPUBAPPDATADIR]\\License Manager\\Licenses\\ |
| NILMPRODUCTINFODIR | ni-paths-NILMPRODUCTINFODIR | [NIPUBAPPDATADIR]\\License Manager\\ProductInfo\\ |
| NIPMDIR | ni-paths-NIPMDIR | [NIDIR]\\NI Package Manager\\ |
| NIPMDIR64 | ni-paths-NIPMDIR64 | [NIDIR64]\\NI Package Manager\\ |
| NIPUBAPPDATADIR | ni-paths-NIPUBAPPDATADIR | [ProgramData]\\National Instruments\\ |
| NIPUBDOCSDIR | ni-paths-NIPUBDOCSDIR | [Documents]\\National Instruments\\ |
| NISHAREDDIR | ni-paths-NISHAREDDIR | [NIDIR]\\Shared\\ |
| NISHAREDDIR64 | ni-paths-NISHAREDDIR64 | [NIDIR64]\\Shared\\ |
| RTFEEDSDIR64 | ni-paths-RTFEEDSDIR64 | [NIDIR64]RT Feeds\\ |
| TESTSTANDXXXXDIR | ni-paths-TESTSTANDXXXXDIR | [NIDIR]\\TestStand XXXX\\Note Example: For the target root TESTSTAND2018DIR the name in file package is ni-paths-TESTSTAND2018DIR and the default folder is [NIDIR]\\TestStand 2018\\. |
| TESTSTANDXXXXDIR64 | ni-paths-TESTSTANDXXXXDIR64 | [NIDIR64]\\TestStand XXXX\\ Note Example: For the target root TESTSTAND2018DIR64 the name in file package is ni-paths-TESTSTAND2018DIR64 and the default folder is [NIDIR64]\\TestStand 2018\\. |
| VERISTAND2020DIR | ni-paths-VERISTAND2020DIR | [NIDIR]VeriStand 2020\\ |
| VERISTAND2020DIR64 | ni-paths-VERISTAND2020DIR64 | [NIDIR64]VeriStand 2020\\ |

Parent topic:

Package Components

Related tasks:

- Assembling a File Package

<!--NI_TOPIC bundle=package-manager path=instructions-xml-file-packages.html language=enus -->
## TOPIC 00016: Instructions XML for File Packages

- bundle_id: `package-manager`
- source_path: `instructions-xml-file-packages.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/instructions-xml-file-packages.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The optional Instructions XML file you create provides Package Manager with instructions for customized execution of package installation. The instructions XML file consists of a root <instructions> element with several child elements. Each child element is optional. <targetAttributes> <customDirect

### Instructions XML for File Packages

The optional Instructions XML file you create provides Package Manager with instructions for customized execution of package installation.

<instructions>

- <targetAttributes>
- <customDirectories>
- <shortcuts>
- <returnCodeConventions>
- <customExecutes>
- <osUninstallEntry>

Name the instructions XML file instructions, omit the file extension, and place it in the root of the data directory of a File package.

The following text is an example instructions file for a File package.

```text
<instructions>
    <targetAttributes readOnly="allReadOnly"/>
    <customDirectories>
        <customDirectory name="customDir1" path="D:\subdir"/>
        <customDirectory name="customDir2" path="\\myserver\subdir"/>
    </customDirectories>
    <shortcuts>
        <shortcut>
            <destination root="ProgramMenu" path="Test\Shortcut.lnk">
                <localizedDestination root="ProgramMenu" path="Test\Verknüpfung.lnk" language="de"/>
                <localizedDestination root="ProgramMenu" path="Test\Raccourci.lnk" language="fr"/>
                <localizedDestination root="ProgramMenu" path="Test\ショートカット.lnk" language="ja"/>
                <localizedDestination root="ProgramMenu" path="Test\바로가기.lnk" language="ko"/>
                <localizedDestination root="ProgramMenu" path="Test\快捷方式.lnk" language="zh-CN"/>
            </destination>
            <target root="Program Files" path="Shortcuts\executable.exe"/>
        </shortcut>
    </shortcuts>
    <customExecutes>
        <customExecute root="Documents" exeName="executable.exe"/>
    </customExecutes>
</instructions>
```

Parent topic:

Package Components

#### <targetAttributes> Element

The 
 <targetAttributes> element provides optional instructions regarding locations where Package Manager installs files on the target system.

<targetAttributes> is an empty element, meaning that it has attributes, but does not contain elements or text content. It has the following attributes:

| Attribute Name | Type | Possible Values | Details | Examples |
| --- | --- | --- | --- | --- |
| readOnly | Enum | allWritable —(default) Makes all package files for installation writable regardless of the original source file's read-only attribute value. allReadOnly —Makes all package files for installation read-only regardless of the original source file's read-only attribute value. keepSource —Keeps the original source file's read-only attribute value when installing. | Declares to Package Manager whether to make all files read-only, file-writable, or to keep the read-only attribute value from the original source file. The default is allWritable when you do not declare a readOnly attribute or include an instructions file. | <targetAttributes readOnly="allReadOnly"/> |

#### <customDirectories> Element

The <customDirectories> element provides a list of
 absolute path locations to which Package Manager installs files on
 the target system.

<customDirectories> contains the <customDirectory> child
 element.

#### <customDirectory> Element

The <customDirectory> element defines one absolute
 or network path to which Package Manager installs files on the target system.

You can have multiple instances of <customDirectory> in the
 Instructions file.

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| name | String | Characters that are valid for a Windows directory name: Consist only of lower case letters (a-z), digits (0-9), plus (+) and minus (-) signs, and periods (.) Start with an alphanumeric character Have a min length of two characters Have a max length of 58 characters An error results if the name attribute: Is an existing target root Begins with ni_ Contains invalid characters | <customDirectory name="examplename1" path="D:\\bin"/> |
| path | String | An absolute or network path on the target system | <customDirectory name="examplename2" path="\\\\servername\\sharename\\subdir"/> |

#### <shortcuts> Element

The 
 <shortcuts> element provides a list of shortcuts that Package Manager creates during installation.

<shortcuts> contains the 
 <shortcut> child element.

#### <shortcut> Element

The 
 <shortcut> element defines one shortcut that Package Manager creates during installation.

<shortcut>

<shortcut>

- <destination>
- <target>

#### <destination> Element

The 
 <destination> element specifies the location where Package Manger creates a shortcut file.

<destination> is required and can have one or more
 optional <localizedDestination> child
 elements. It has the following attributes:

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| root | String | A supported target root. Packages with a windows_all architecture cannot use 64-bit specific target roots, such as ProgramFiles_64 or LV2017DIR64. | <destination root="Startup" path="testShortcut.lnk"/> |
| path | String | The path and file name appended to the root target. Refer to XML Syntax Rules for Quotation Marks for syntax requirements. | <destination root="ProgramFiles" path="Shortcuts\\test.exe"/> |

Related reference:

- Installation Target Roots for File Packages

#### <localizedDestination> Element

The <localizedDestination> element specifies an
 alternate localized path to use for the shortcut file when installing the file package
 in a given language.

<localizedDestination> is an empty element, meaning
 that it has attributes, but does not contain elements or text content. It has the following
 attributes:

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| root | String | A supported target root. Packages with a windows_all architecture cannot use 64-bit specific target roots, such as ProgramFiles_64 or LV2017DIR64. | <localizedDestination root="ProgramMenu"/> |
| path | String | The path and file name appended to the root target. | <localizedDestination root="ProgramMenu" path="Test\\Verknüpfung.lnk" /> |
| language | String | Language code of the localized path. Possible values: de fr ja ko zh-CN | <localizedDestination root="ProgramMenu" path="Test\\Verknüpfung.lnk" language="de"/> |

Related reference:

- Installation Target Roots for File Packages

#### <target> Element

The 
 <target> element specifies the location of the file for which Package Manager creates a shortcut.

<target> is an empty element, meaning that it has attributes, but does not contain elements or text content. It has the following attributes:

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| root | String | A supported target root. Packages with a windows_all architecture cannot use 64-bit specific target roots, such as ProgramFiles_64 or LV2017DIR64. | <target root="Startup" path="testShortcut.lnk"/> |
| path | String | The path and file name appended to the root target after it is resolved. Refer to XML Syntax Rules for Quotation Marks for syntax requirements. | <target root="ProgramFiles" path="Shortcuts\\test.exe"/> |
| arguments | String | Optional arguments passed to the target file. Refer to XML Syntax Rules for Quotation Marks for syntax requirements. | <target root="ProgramFiles" path="Shortcuts\\test.exe" arguments="--argument1"/> |

Related reference:

- Installation Target Roots for File Packages

#### <returnCodeConventions> Element

The <returnCodeConventions> element provides a
 list of custom return code conventions. Package Manager uses these
 conventions when performing custom actions for this package.

The <returnCodeConventions> element is optional in
 the instructions file, but can contain one or more <returnCodeConvention> child elements.

#### <returnCodeConvention> Element

The <returnCodeConvention> element defines how to
 interpret a return code for one or more custom executes in this package.

The <returnCodeConvention> element can have one or
 more optional <returnCode> child elements. <returnCode> rules evaluate in definition order.

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| name | String | A unique name for this return code convention. A custom execute in this package can use this name in its returnCodeConvention field to associate itself with this return code convention. | <returnCodeConvention name="alwaysReboot" defaultResult="rebootRequired"/> |
| defaultResult | Enum | Indicates the semantic result of a return code that does not match any existing return code mapping rules. success failure rebootRequired | <returnCodeConvention name="ignore" defaultResult="success"/> |

#### <returnCode> Element

The <returnCode> element defines a return code
 mapping rule for its parent <returnCodeConvention>.

The <returnCode> element is empty. This element has
 attributes, but does not contain elements or text content. <returnCode> has the following attributes.

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| min | Integer | Indicates the lower bound of a range of return codes this rule matches. May not be combined with the value attribute. | <returnCode min="0" max="1024" result="success"/> |
| max | Integer | Indicates the upper bound of a range of return codes this rule matches. May not be combined with the value attribute. | <returnCode min="-50" max="-1" result="success"/> |
| value | Integer | Indicates a single return code this rule matches. May not be combined with the min or max attributes. | <returnCode value="1641" result="rebootRequired"/> |
| result | Enum | Indicates the semantic result of a return code matching this rule. | <returnCode value="3010" result="rebootRequired"/> |

#### <customExecutes> Element

The 
 <customExecutes> element provides a list of custom actions for Package Manager to perform on the package.

<customExecutes> contains the 
 <customExecute> child element.

#### <customExecute> Element

The 
 <customExecute> element defines one custom action Package Manager performs on the package.

The 
 <customExecute> element is optional in the Instructions file, but you can include as many as needed for your package. <customExecute> is an empty element, meaning that it has attributes, but does not contain elements or text content. It has the following attributes:

| Attribute Name | Type | Required | Value | Description | Examples |
| --- | --- | --- | --- | --- | --- |
| root | String | Yes | The root path to the executable. Packages with a windows_all architecture cannot use 64-bit specific target roots, such as ProgramFiles_64 or LV2017DIR64. | Specifies the root path to the executable. A supported target root. Refer to Installation Target Roots to see supported target roots.Note To run an executable, you must first install the package that includes the executable. You can configure a package to temporarily install the executable by setting the target root path to NIPkgMgrTempUnique and setting the schedule attribute to post. Package Manager then installs the package to the NIPkgMgrTempUnique directory and runs the executable from there before deleting files in the directory. | <customExecute root="Documents" exeName="executable.exe"/> |
| exeName | String | Yes | The file name of the executable. | Specifies the file name of the executable.Can include a path relative to the root. Refer to XML Syntax Rules for Quotation Marks for syntax requirements. | <customExecute root="ProgramData" exeName="actions\\executable.exe"/> |
| arguments | String | No | Command line arguments to pass to the executable. | Specifies command line arguments for Package Manager to pass to the executable.The value is formatted. You can include a supported target root and/or the following arguments:Note The arguments are case insensitive. Refer to XML Syntax Rules for Quotation Marks for syntax requirements. %REBOOTPENDING%—Passes pending reboot information. If a reboot is required at the end of the transaction, Package Manager replaces %REBOOTPENDING% with 1. Otherwise, Package Manager replaces %REBOOTPENDING% with 0. You can use this argument only if the value of the schedule attribute is postall. %NIPMLANGUAGECODE%—Specifies the language in which Package Manager runs using the ISO language code. Possible values: en, de, fr, ko, ja, or zh-CN. | <customExecute root="ProgramData" exeName="executable1.exe" arguments="-open %desktop%\\file.txt"/> <customExecute root="ProgramData" exeName="executable2.exe" arguments="-reboot %rebootpending%" schedule=postall/> <customExecute root="ProgramData" exeName="executable3.exe" arguments="-language %nipmlanguagecode%"/> |
| step | Enum | No | install —(default) Package Manager runs the executable when installing the package. uninstall —Package Manager runs the executable when removing the package. reinstall—Package Manager runs the executable when repairing the package. | Specifies the transaction step during which Package Manager runs the executable. To run the same executable in multiple steps, such as install, uninstall, and repair, list a <customExecute> element for each step. If you omit this attribute, Package Manager uses its default value. Note During the development of a package, if you set the value of step to uninstall, set the value of ignoreErrors to y in order to avoid a situation where Package Manager cannot remove a package from the target system. | <customExecute step="uninstall" root="ProgramData" ignoreErros="y" exeName="actions\\executable.exe"/> |
| schedule | Enum | No | post (default) pre postall | Specifies the relative point within the transaction steps when Package Manager runs the executable.If you omit this attribute, Package Manager uses its default value. | <customExecute step="install" schedule="post" root="ProgramData" exeName="executable.exe"/> |
| wait | Boolean | No | n (default) y | Specifies whether the custom action is synchronous, where Package Manager should wait for it to finish before continuing, or asynchronous, where Package Manager should not wait.If you omit this attribute, Package Manager uses its default value. | <customExecute root="ProgramData" exeName="executable.exe" wait="n"/> |
| ignoreErrors | Boolean | No | n (default) y | Specifies whether Package Manager reports an error if it cannot run the executable or the executable returns a value other than 0. Requires you to set the value of wait to y so Package Manager will wait to receive the return code. If you omit this attribute, Package Manager uses its default value. This attribute may not be used in combination with either ignoreLaunchErrors or returnCodeConvention. | <customExecute root="ProgramData" exeName="executable.exe" wait="y" ignoreErrors="y"/> |
| hideConsoleWindow | Boolean | No | n (default) y | Specifies whether to hide the console window for console applications. Does not display console messages when you run GUI applications. Console applications still run, but without a console window for user input or message output. If you omit this attribute, Package Manager uses its default value. Does not prevent the application from creating additional console windows. | <customExecute root="ProgramData" exeName="executable.exe" hideConsoleWindow="y"/> |
| ignoreLaunchErrors | Boolean | No | n (default) y | Specifies whether Package Manager reports an error if it cannot run or cannot find the executable. This attribute may not be used in combination with ignoreErrors. | <customExecute root="ProgramData" exeName="executable.exe" ignoreLaunchErrors="y"/> |
| returnCodeConvention | String | No | Must match the name of a predefined convention or a <returnCodeConvention> element defined in this package. The following predefined conventions are available: console (default) installer ignore | Indicates how to interpret the return codes the executable returns. wait must be set to y, so the agent waits to receive the return code For console, 0 = success and any other value is an error. For installer, 0 = success, 1641 = reboot required, 3010 = reboot required, and any other value is an error. For ignore, Package Manager ignores the return code. This attribute may note be used in combination with ignoreErrors. | <customExecute root="ProgramData" exeName="executable.exe" returnCodeConvention="installer"/> |

Related reference:

- Installation Target Roots for File Packages

##### Behavior of Executables Scheduled as Postall

For Instructions files in which you include a <customExecute> element where schedule="postall", Package Manager demonstrates specific behaviors that may affect
 package installation.

The postall value instructs Package Manager to run the
 executable after completing the installation, reinstallation, and/or removal steps for all
 packages.

- Package Manager runs 
 postall executables in the specified order of package installation. Dependencies install first.
- If only a 
 postall executable in a package fails, Package Manager considers the package installed.
- When there are multiple packages with 
 postall executables, Package Manager does not run the remaining executables if one of the 
 postall executables fails. Packages are considered installed assuming no other errors occurred during installation.
- If installation of a package fails, either through MSI failure or failure of an executable scheduled as pre or post , Package Manager displays an error message stating that the package failed to install. Next, it runs all the executables from packages installed up to the point where installation failed. Package Manager does not consider the broken package installed and does not run the postall executables of the broken package. All packages installed before the failure occurred remain installed and Package Manager runs the postall executables of these packages.

##### XML Syntax Rules for Quotation
 Marks

Review the XML syntax rules for quotation marks to adhere to Microsoft's conditional
 statement syntax and to enclose paths with spaces within quotation marks.

You must enclose literal text within quotation marks to adhere to Microsoft's conditional
 statement syntax. The Instructions XML syntax provides two ways of adhering to this
 requirement:

- Use single quotation marks to delimit the XML string. This allows the use of double
 quotation marks inside the string. For
 example: <customExecute condition='IEDETECTED~="Yes" AND VersionNT64 = 601 AND NIRUNNINGINSILENTMODE'/>
- Use the XML escape character for double quotation marks, " , to delimit the literal text in the XML string. With the XML escape
 character, you can use double quotation marks or single quotation marks to delimit the XML
 string. For
 example: <customExecute condition="IEDETECTED~="Yes" AND VersionNT64 = 601 AND NIRUNNINGINSILENTMODE"/>

You must enclose paths with spaces within quotation marks. Single quotation marks are not
 allowed in the path:

- Use the XML escape character for double quotation marks, " , to enclose path in the XML string. For
 example: <customExecute exeName=""VC RunTime Installer.exe"" arguments="/q /norestart" inPackage="y"/>

##### Custom Execute Examples

The following invokes a PowerShell script that the package could have installed and
 passes two arguments after installation.

```text
<customExecute root="BootVolume" exeName="Windows\System32\WindowsPowerShell\v1.0\powershell.exe" arguments="-File &quot;%ProgramData%\My App Name\MyInstallScript.ps1&quot; &quot;argument 1&quot; &quot;argument 2&quot;" step="install" schedule="post" wait="y" ignoreErrors="n" hideConsoleWindow="y" />
```

#### <osUninstallEntry> Element

The <osUninstallEntry> element provides
 optional instructions for the package to appear in the Add/Remove
 Programs interface.

<osUninstallEntry> is an empty element. That is, it
 has attributes but does not contain elements or text content. <osUninstallEntry> has the following attributes:

| Attribute Name | Type | Possible Values | Details | Examples |
| --- | --- | --- | --- | --- |
| ux | Enum | ni—(default) Shows normal Package Manager interface elements during a modify or uninstall operation. oem—Hides all dialog text and links referring to NI during a modify or uninstall operation. | For third-party packages, the oem value allows the package to appear as a first-class item in the list of installed applications. When performing modify and uninstall operations, the Add/Remove Programs interface only refers to the named package. | <osUninstallEntry ux="oem"/> |

<!--NI_TOPIC bundle=package-manager path=instructions-xml-wininst-packages.html language=enus -->
## TOPIC 00017: Instructions XML for WinInst Packages

- bundle_id: `package-manager`
- source_path: `instructions-xml-wininst-packages.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/instructions-xml-wininst-packages.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The optional Instructions XML file you create provides Package Manager with instructions for customized execution of MSIs and executables. WinInst packages without an instructions file run all MSIs in ascending ASCII order by file name. The instructions XML file consists of a root <instructions> ele

### Instructions XML for WinInst Packages

The optional Instructions XML file you create provides Package Manager with instructions for customized execution of MSIs and
 executables.

Note

<instructions>

- <upgrade>
- <msis>
- <returnCodeConventions>
- <customExecutes>

1. Name the instructions XML file instructions .
2. Remove the XML file extension.
3. Place the XML file in the data directory root of a
 WinInst package.

The following text is an example instructions file for a WinInst package.

```text
<instructions>
    <msis>
        <msi name="Setup.msi">
            <property name="ADDLOCAL" value="ALL"/>
            <langFile language="de">transform1.mst</langFile>
            <langFile language="fr">transform2.mst;transform3.mst</langFile>
            <langFile language="ja">transform4.mst</langFile>
            <langFile language="ko">transform5.mst</langFile>
            <langFile language="zh-CN">transform6.mst</langFile>
        </msi>
        <msi name="Setup64.msi">
            <property name="ADDLOCAL" value="ALL"/>
        </msi>
    </msis>
</instructions>
```

Parent topic:

Package Components

#### <upgrade> Element

The <upgrade> element specifies how a package
 upgrades a previous version of itself.

The following enum values are valid inside the <upgrade> tags.

| Value | Description | Example |
| --- | --- | --- |
| clean | Package Manager removes the old version of the package before installing the new version of the package. This value is the default behavior when the element value is blank. | <upgrade>clean</upgrade> |
| native | Package Manager installs the new version of the package before removing the old version of the package. The MSI performs the native upgrade behavior. | <upgrade>native</upgrade> |

#### <msis> Element

The <msis> element provides a list of MSI files
 in the package.

<msis> contains the 
 <msi> child element.

Package Manager runs the MSIs from the list in the order of
 inclusion. If you do not list any MSIs, Package Manager runs all MSIs
 in the package data directory. Package Manager runs the MSIs in no
 particular order and without conditions, properties, or transforms.

Note

<msis>

Package Manager

Package Manager

#### <msi> Element

The <msi> element represents one MSI in the
 package. The element also includes any conditions for running the MSI, properties to set to the
 MSI, and transforms to apply to the MSI.

The 
 <msi> element is optional in the Instructions file, but you can include as many as needed for your package. List MSIs using one 
 <msi> element for each MSI. 
 <msi> contains the 
 <property> element.

It has the following attributes:

| Attribute Name | Type | Required | Description | Examples |
| --- | --- | --- | --- | --- |
| name | String | Yes | Specifies the path to the MSI, relative from the root of the data directory, including its file name. The path value is case sensitive. | <msi name="temp\\example.msi"/> |
| condition | WinInst Condition | No | Specifies an MSI condition for Package Manager to evaluate before installing the MSI. The value must be a valid MSI condition string. To include quotes in a condition, use single quotes. If you specify a condition, you must include a Depends relationship in your control file that declares a dependency on the ni-msiproperties package of the minimum version you require. Package Manager will install the MSI only on a system where the statement evaluates to TRUE. Packages install only once. If conditions are TRUE, the MSI must install all its features. If conditions are FALSE, the MSI does not install anything. At least one MSI in the instructions file must have a TRUE condition, or else Package Manager does not record that the package is installed. Note If you specify any condition, property, or command-line in your instructions file, you must declare a dependency on the ni-msiproperties package of the minimum version that you require. | <msi name="example.msi" condition="(VersionNT64 = 601) AND (NIRUNNINGINSILENTMODE)"/> |
| skipUninstall | Boolean | No | Specifies whether the MSI should not uninstall when its package is uninstalled. The attribute can be one of the following values: n (default) y Consider using this attribute for a package that installs a third-party MSI to prevent the package from removing the MSI when the MSI can be installed separately without the package. | <msi name="temp\\example.msi" skipUninstall="y"/> |

#### <property> Element

The <property> element specifies a property
 (name-value pair) that Package Manager passes to the MSI engine for this
 MSI.

For a list of supported properties, rules, and guidelines, refer to *Properties and
 Conditions in WinInst Packages*.

| Attribute Name | Type | Required | Possible Values | Description | Examples |
| --- | --- | --- | --- | --- | --- |
| name | string | Yes | All uppercase string that follows the MSI naming rules for properties. | Specifies the name of the property that Package Manager passes when running the MSI. Note You can specify any condition, property, or command-line in the instructions file. To do so, you must declare a dependency on the ni-msiproperties package. This declaration must occur on the minimum version that you require. | <property name="INSTALLLEVEL" value="1000"/> |
| value | WinInst condition | Yes | The value of the property. | Specifies the value of the property that Package Manager passes to the MSI when running it. The value can be a property in brackets. Using brackets indicates that Package Manager should evaluate and replace the property at run-time with the actual value. | <property name="MYLANGCODE" value="[NIPMLANGUAGECODE]"/> |
| step | Enum | No | install —(default) Package Manager applies the property when installing the package. reinstall —Package Manager applies the property when repairing the package. uninstall —Package Manager applies the property when removing the package. | Specifies the type of transaction during which Package Manager applies the property. If Package Manager should apply the property during multiple steps, list multiple <property> elements. If you omit this attribute, Package Manager uses the default value. | <property name="INSTALLLEVEL" value="1000" step="install"/> |

#### <langFile> Element

The <langFile> element specifies the transforms
 to pass to the MSI.

You can include multiple transform files for each language by delimiting the transform
 files with semicolons. The transform files must be in the same directory as the MSI files.
 The transform file must also have a path that is a relative path of the package data
 directory.

For example, if the MSI file path is foo\bar.msi, the
 transform file path must be foo\transform
 filename.mst.

| Attribute Name | Type | Required | Possible Values | Description | Examples |
| --- | --- | --- | --- | --- | --- |
| language | Enum | Yes | de fr ja ko zh-CN | Specifies the ISO language code of the language in which Package Manager runs. | <langFile language="de">transform1.mst</langFile> <langFile language="zh-CN">transform2.mst;transform3.mst</langFile> |

#### <returnCodeConventions> Element

The <returnCodeConventions> element provides a
 list of custom return code conventions. Package Manager uses these
 conventions when performing custom actions for this package.

The <returnCodeConventions> element is optional in
 the instructions file, but can contain one or more <returnCodeConvention> child elements.

#### <returnCodeConvention> Element

The <returnCodeConvention> element defines how to
 interpret a return code for one or more custom executes in this package.

The <returnCodeConvention> element can have one or
 more optional <returnCode> child elements. <returnCode> rules evaluate in definition order.

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| name | String | A unique name for this return code convention. A custom execute in this package can use this name in its returnCodeConvention field to associate itself with this return code convention. | <returnCodeConvention name="alwaysReboot" defaultResult="rebootRequired"/> |
| defaultResult | Enum | Indicates the semantic result of a return code that does not match any existing return code mapping rules. success failure rebootRequired | <returnCodeConvention name="ignore" defaultResult="success"/> |

#### <returnCode> Element

The <returnCode> element defines a return code
 mapping rule for its parent <returnCodeConvention>.

The <returnCode> element is empty. This element has
 attributes, but does not contain elements or text content. <returnCode> has the following attributes.

| Attribute Name | Type | Value | Examples |
| --- | --- | --- | --- |
| min | Integer | Indicates the lower bound of a range of return codes this rule matches. May not be combined with the value attribute. | <returnCode min="0" max="1024" result="success"/> |
| max | Integer | Indicates the upper bound of a range of return codes this rule matches. May not be combined with the value attribute. | <returnCode min="-50" max="-1" result="success"/> |
| value | Integer | Indicates a single return code this rule matches. May not be combined with the min or max attributes. | <returnCode value="1641" result="rebootRequired"/> |
| result | Enum | Indicates the semantic result of a return code matching this rule. | <returnCode value="3010" result="rebootRequired"/> |

#### <customExecutes> Element

The <customExecutes> element provides a list of
 package executables.

The <customExecutes> element contains the <customExecute> child element.

#### <customExecute> Element

The <customExecute> element provides Package Manager with conditions for the executable.

These conditions include the following instructions.

- How to run the executable.
- When to run the executable.
- What arguments to pass to the executable.
- How to handle the executable errors and the user interface.

The <customExecute> element is optional in the
 Instructions file, but you can include as many <customExecute> elements as needed for your package. <customExecute> is an empty element, meaning that it has
 attributes, but does not contain elements or text content. <customExecute> has the following attributes that tell Package Manager
 conditions for running the executable:

When

Why

What

How

| Attribute Name | Type | Possible Values | Description | Example |
| --- | --- | --- | --- | --- |
| step | Enum | install—(default) Package Manager runs the executable when installing the package. uninstall —Package Manager runs the executable when removing the package. reinstall —Package Manager runs the executable when repairing the package. | Specifies the transaction step during which Package Manager runs the executable. To run the same executable in multiple steps, such as install, uninstall, and repair, list a <customExecute> element for each step. If you omit this attribute, Package Manager uses its default value. Note If you set the value of inPackage to y, you must set the value of step to install or omit the attribute. (See the inPackage attribute below.) | <customExecute step="uninstall" exeName="[NIDIR]\\actions\\executable.exe"/> |
| schedule | Enum | post —(default) Package Manager runs the executable immediately after completing the transaction step for the current package. pre —Package Manager runs the executable immediately before completing the transaction step for the current package. postall —Package Manager runs the executable after completing the transaction steps for all packages. preall—Package Manager runs the executable before completing the transaction steps for all packages. Valid only when you set the value of step to uninstall. | Specifies the relative point within the transaction steps when Package Manager runs the executable. If the value of <upgrade> is clean, Package Manager runs a <customExecute> with attribute values step="install" and schedule="pre" after removing the old package and before installing the new package. If you omit this attribute, Package Manager uses its default value. Note If you set the value of the inPackage attribute to y, you must set the value of schedule to pre or post, or omit the attribute. (See the inPackage attribute below.) | <customExecute step="install" schedule="post" exeName="[NIDIR]\\executable.exe"/> |

| Attribute Name | Type | Possible Value | Description | Example |
| --- | --- | --- | --- | --- |
| condition | WinInst condition | The condition for the MSI. | Specifies an MSI condition for Package Manager to evaluate before running the executable. Package Manager runs this executable only on a system where the statement evaluates to TRUE. Refer to Properties and Conditions in WinInst Packages for a list of syntax requirements and supported NIPaths. If you omit this attribute, the executable always runs. Note If you specify any condition, property, or command-line in your instructions file, you must declare a dependency on the ni-msiproperties package of the minimum version that you require. | <customExecute exeName="[NIDIR]\\executable.exe" condition="VersionNT >=600"/> |

| Attribute Name | Type | Possible Values | Description | Example |
| --- | --- | --- | --- | --- |
| arguments | String | Command line arguments to pass to the executable. | Specifies command line arguments for Package Manager to pass to the executable. This is a formatted value, so you can include a ni-msiproperties directory property in brackets. Refer to Properties and Conditions in WinInst Packages for a list of syntax requirements and supported properties. If you include the full path to the executable, omit the exeName attribute. Note If you specify any condition, property, or command-line in your instructions file, you must declare a dependency on the ni-msiproperties package of the minimum version that you require. | <customExecute exeName="[ProgramFilesFolder]\\executable.exe" arguments="-listall"/> |
| formatArguments | Boolean | n (default) y | Specifies whether the arguments attribute contains strings that the MSI engine needs to resolve.If you set the value of this attribute to y, you must include a Depends relationship in your control file that declares a dependency on the ni-msiproperties package of the minimum version you require.Note If you specify any condition, property, or command-line in your instructions file, you must declare a dependency on the ni-msiproperties package of the minimum version that you require. | <customExecute exeName="[ProgramFilesFolder]\\executable.exe" arguments="[NIDIR]" formatArguments="y"/> |
| exeName | String | The path and file name of the executable. | Specifies the path and the file name of the executable. This value is case-sensitive. If the value of inPackage is n or undefined, exeName must contain an ni-msiproperties property and not a hard-coded path. If you specify an ni-msiproperties property, you must include a depends relationship in your control file that declares a dependency on the ni-msiproperties package of the minimum version that you require. Refer to Properties and Conditions in WinInst Packages for a list of syntax requirements and supported properties. If you omit this attribute, you must specify the full path to the executable in arguments. | <customExecute exeName="[ProgramFilesFolder]\\executable.exe"/> |
| inPackage | Boolean | n (default) y | Specifies whether the executable resides in the package data folder. If you set the value of this attribute to y, observe the following rules: The value of exeName must be a relative path to the executable within the package data folder. You must set the value of wait to y. Otherwise, Package Manager may delete the executable before it runs. You must set the value of step to install or reinstall. You must set the value of schedule to pre or post. You must use a File Package to install the executable to the target system. Package Manager does not evaluate exeName for NIPaths properties. If you omit this attribute, Package Manager uses its default value. | The following example specifies a relative path to the executable, where executable.exe resides in a subfolder named actions within the package data directory.<customExecute exeName="actions\\executable.exe" inPackage="y"/> |

| Attribute Name | Type | Possible Values | Description | Example |
| --- | --- | --- | --- | --- |
| wait | Boolean | n (default) y | Specifies whether the executable is synchronous, meaning Package Manager should wait for it to finish before continuing, or asynchronous, meaning Package Manager should not wait. If the value is n, Package Manager ignores the executable's return code, as if returnCodeConvention="ignore". If the value is n, you must not include the executable within the package because Package Manager may delete the entire package from temp before running the executable. If you omit this attribute, Package Manager uses its default value. | <customExecute exeName="executable.exe" wait="n"/> |
| ignoreLaunchErrors | Boolean | n (default) y | Specifies whether Package Manager reports an error if it cannot run or cannot find the executable.If you omit this attribute, Package Manager uses its default value. | <customExecute exeName="executable.exe" ignoreLaunchErrors="y"/> |
| hideConsoleWindow | Boolean | n (default) y | Specifies whether to hide the console window for console applications. Does not display console messages when you run GUI applications. Does not cause any errors for a window application if present. Console applications still run, but without a console window for user input or message output. | <customExecute exeName="executable.exe" hideConsoleWindow="y"/> |
| returnCodeConvention | String | Must match the name of a predefined convention or a <returnCodeConvention> defined in this package. The following predefined conventions are available: console (default) installer ignore | Indicates how to interpret the return codes the executable returns. wait must be set to y, so the agent waits to receive the return code. For console, 0 = success and any value is an error. For installer, 0 = success, 3010 = reboot required or 1641 = reboot required, and anything else is an error. For ignore, Package Manager ignores the return code. If you omit this attribute, Package Manager uses its default value. | <customExecute step="uninstall" exeName="[ProgramFilesFolder]executable1.exe" returnCodeConvention="installer"/> |

#### Behavior of Executables Scheduled as Postall

For Instructions files in which you include a <customExecute> element where schedule="postall", Package Manager demonstrates specific behaviors that may affect
 package installation.

The postall value instructs Package Manager to run the
 executable after completing the installation, reinstallation, and/or removal steps for all
 packages.

- Package Manager runs 
 postall executables in the specified order of package installation. Dependencies install first.
- If only a 
 postall executable in a package fails, Package Manager considers the package installed.
- When there are multiple packages with 
 postall executables, Package Manager does not run the remaining executables if one of the 
 postall executables fails. Packages are considered installed assuming no other errors occurred during installation.
- If installation of a package fails, either through MSI failure or failure of an executable scheduled as pre or post , Package Manager displays an error message stating that the package failed to install. Next, it runs all the executables from packages installed up to the point where installation failed. Package Manager does not consider the broken package installed and does not run the postall executables of the broken package. All packages installed before the failure occurred remain installed and Package Manager runs the postall executables of these packages.

#### Properties and Conditions in WinInst Packages

You can use WinInst conditions in <msi> and
 <customExecute> elements to conditionally execute
 WinInst MSIs and executable files.

If you specify any condition, property, or command in your instructions file, you must declare a dependency in your package's control file on the 
 ni-msiproperties package. The 
 ni-msiproperties package has dependencies on additional packages:

- ni-euladepot
- ni-mdfsupport
- ni-metauninstaller
- ni-security-update-kb67l8lcqw-killbits

You must include the 
 ni-msiproperties package and its dependencies in the same feed as the package you build. If you have NI software installed on your system, these packages should exist in their default location on your system: 
 %ProgramData%\National Instruments\NI Package Manager\packages. Copy the 
 ni-msiproperties package and its dependencies from this location to the same directory as your package when you build the feed.

Note

ni-security-update-kb67l8lcqw-killbits

ni-msiproperties

##### Syntax Requirements for WinInst Conditions

WinInst conditions included in <msi> and
 <customExecute> elements must follow Microsoft's
 MSI conditional statement syntax.

You must enclose literal text within quotation marks to adhere to
 Microsoft's conditional statement syntax. The Instructions XML syntax provides two ways
 of adhering to this requirement:

- Use single quotation marks to delimit the XML string.
 This allows the use of double quotation marks inside the string. For example:
 <customExecute condition='IEDETECTED~="Yes" AND
 VersionNT64 = 601 AND NIRUNNINGINSILENTMODE'/>
- Use the XML escape character for double quotation
 marks, " , to delimit the literal text in the XML string.
 With the XML escape character, you can use double quotation marks or single
 quotation marks to delimit the XML string. For example: <customExecute condition="IEDETECTED~="Yes" AND
 VersionNT64 = 601 AND NIRUNNINGINSILENTMODE"/>

You must enclose paths with spaces within quotation marks. Single quotation
 marks are not allowed in the path:

- Use the XML escape character for double quotation marks, " , to
 enclose path in the XML string. For example: <customExecute
 exeName=""VC RunTime Installer.exe"" arguments="/q /norestart"
 inPackage="y"/>

##### Properties You Can Use in Conditions

When including conditions in a WinInst package, you can use any Windows property or
 property defined in the ni-msiproperties package.

If you use a property in the 
 arguments attribute of a 
 <customExecute>, you must include a 
 formatArgument attribute and set the value to 
 y. For a comprehensive list of Windows Installer properties, such as 
 ProgramFiles64Folder and 
 DesktopFolder, search for Property Reference at https://msdn.microsoft.com.

You can use the following list of additional Package Manager-specific properties:

- NIINTERNETCONNECTEDTOMICROSOFT = YES (Package Manager uses this value if a connection to http://go.microsoft.com is successful. Otherwise, the value is 
 NO .)
- NIRUNNINGINSILENTMODE = 1 (Package Manager uses this value only when running in silent mode. Otherwise, it leaves the value undefined.)
- NIPKGPROCESSID (The process ID of the current Package Manager process.)
- NIPMLANGUAGECODE (The ISO language code of the language in
 which Package Manager runs. Possible values: en ,
 de , fr , ko , ja , or zh-CN .)

You can use the 
 <property> element to pass additional Windows properties to each MSI, for example:

- ADDLOCAL = ALL
- INSTALLLEVEL = 100 (You can also enter a value of 
 1000 , which turns on more or all of your features.)

##### Properties You Cannot Use in Conditions

Do not use properties that exist only inside of your specific MSI.

- Do not use any property that is defined in your MSI's Property table, by AppSearch, or by the Upgrade table.
- Do not use any Feature state, Component state, or File key.

##### Properties Passed to Every MSI

Package Manager defines and automatically passes some properties to MSIs run from WinInst packages.

Package Manager always passes the following properties to every MSI at install, uninstall, and repair. You do not need to specify these in the instructions file.

- REBOOT = ReallySuppress
- PROMPTROLLBACKCOST = D
- NIRUNNINGINSILENTMODE = 1 
 Note Package Manager uses this value only when running in silent
 mode. Otherwise, it leaves the value undefined.
- NIPKGPROCESSID = 
 The process ID of the current Package Manager
 process.

<!--NI_TOPIC bundle=package-manager path=manual-overview.html language=enus -->
## TOPIC 00018: Package Manager Overview

- bundle_id: `package-manager`
- source_path: `manual-overview.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/manual-overview.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: Package Manager is software that installs, updates, repairs, and removes NI software. Key Features Installing, Updating, Repairing, and Removing NI Software Troubleshooting Problems with Installing, Updating, Repairing, or Removing NI Software Package Creation Installing a Single Package

### Package Manager
 Overview

Package Manager is software that installs, updates, repairs,
 and removes NI software.

#### Key Features

- Installing,
 Updating, Repairing, and Removing NI Software
- Troubleshooting Problems with Installing, Updating, Repairing, or Removing
 NI Software
- Package
 Creation
- Installing a
 Single Package

<!--NI_TOPIC bundle=package-manager path=new-features-and-changes.html language=enus -->
## TOPIC 00019: Package Manager New Features and Changes

- bundle_id: `package-manager`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/new-features-and-changes.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of Package Manager. Discover what is new in the latest releases of Package Manager.If you cannot find new features and changes for your version, it might not include user-facing updates. However, your versio

### Package Manager
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of Package Manager.

Package Manager

Note

Release Notes

#### Package Manager
 2025 Q4

Learn about new features, behavior changes, and other updates in Package Manager
 2025 Q4.

##### New
 Features

This version of Package Manager provides
 support for the following features:

- Adds support for user-controlled connectivity to ni.com through the graphical user
 interface:
  - Adds the ability to enable or disable Package Manager 
 features that automatically connect to ni.com.
  - Enables partial connectivity to ni.com by allowing users to manually select features
 like the Browse Products tab, automatically register ni.com feeds
 for installed packages, and automatically download and install missing
 dependencies.

#### Package Manager
 2025 Q3

Learn about new features, behavior changes, and other updates in Package Manager
 2025 Q3.

##### New
 Features

This version of the Package Manager provides
 support for the following features:

- Package Manager adds SHA256 package checksums to feeds it
 creates.
- Package Manager verifies package integrity using SHA256
 checksums when downloading packages from feeds that specify SHA256 package checksums.

#### Package Manager 2024 Q3

##### New Features

- You can now use <returnCodeConventions> ,
 <returnCodeConvention> , and <returnCode> elements when defining XML
 instructions for file packages and WinInst packages.

Related reference:

- <returnCodeConventions> Element
- <returnCodeConvention> Element
- <returnCode> Element

#### Package Manager 2024 Q1

##### New Features

Create an Add/Remove Programs entry to uninstall or repair a product package

Related concepts:

- <osUninstallEntry> Element

#### Package Manager 2023 Q3

##### New Features

- Create custom directories for select package file installation
- Incorporate support for URL redirection, commonly referred to as URL forwarding,
 in Package URLs
- Additional options available for automating an installer
- Configuration options to control the behavior of Package Manager available,
 including a new option nipkg.enable-NI-connectivity

Related concepts:

- <customDirectory> Element

Related tasks:

- Automating an Installer

Related reference:

- Installation Target Roots for File Packages
- Configuration Options

<!--NI_TOPIC bundle=package-manager path=package-components.html language=enus -->
## TOPIC 00020: Package Components

- bundle_id: `package-manager`
- source_path: `package-components.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/package-components.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: A package is comprised of a root directory containing subdirectories, payload files, and configuration files that define the result of the package's installation on the target system. Component Details control subdirectory Contains the control file. The control file contains metadata describing prop

### Package Components

A package is comprised of a root directory containing subdirectories, payload files,
 and configuration files that define the result of the package's installation on the target
 system.

| Component | Details |
| --- | --- |
| control subdirectory | Contains the control file. The control file contains metadata describing properties and relationships of the package, such as its name, version, type, and dependencies. Package Manager generates the package according to the metadata in the control file. The control file is a text file without an extension. You declare whether a package is a File package or WinInst package in the control file by assigning the appropriate value to the XB-Plugin attribute. |
| data subdirectory | Contains the payload you intend to distribute with your package. Depending on whether you build a File package, Relative File package, or WinInst package, some of the data subdirectory contents will differ. Note Package Manager will compress this directory while creating the .nipkg file. There is a 10 GB size limit on the resulting compressed file. File packages contain the following items: Root directories—the structure you create for these directories determines where Package Manager installs payload items. (Optional) Instructions file—provides instructions for running any included executables and creates shortcuts to files on the target system. Relative File packages contain the following items: Root directories—the structure you create for these directories determines where Package Manager installs payload items. WinInst packages contain the following items: One or more .msi files—each MSI is automatically found and executed in ascending ASCII order according to its file name unless you provide an instructions file to customize the execution. (Optional) Instructions file—customizes the execution of the MSIs and specifies conditions for running executables. |
| debian-binary file | Declares conformity to the Debian standard. |

- [Control File Attributes](control-file-attributes.html#GUID-16D97F2A-09D6-4F28-A33C-35D1BBEC07A8) A control file is a text file without an extension that contains metadata describing properties and relationships of the package, such as its name, version, type, and dependencies. Both File packages and WinInst packages require a control file. Package Manager generates the package according to the metadata in the control file.
- [Installation Target Roots for File Packages](installation-target-roots.html) The directories you create inside the data folder inform Package Manager where to install the files when you build packages.
- [Instructions XML for File Packages](instructions-xml-file-packages.html#GUID-29BE2213-93C1-4281-8570-7CE1338AEB4A) The optional Instructions XML file you create provides Package Manager with instructions for customized execution of package installation.
- [Instructions XML for WinInst Packages](instructions-xml-wininst-packages.html#GUID-96BD71E8-354A-4892-B764-F2A0D2477666) The optional Instructions XML file you create provides Package Manager with instructions for customized execution of MSIs and executables.

Parent topic:

Package Creation

<!--NI_TOPIC bundle=package-manager path=package-creation.html language=enus -->
## TOPIC 00021: Package Creation

- bundle_id: `package-manager`
- source_path: `package-creation.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/package-creation.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To create a package using Package Manager, you gather the relevant components into a single directory and build the package using the command line interface. A package is a single compressed file that contains payload files intended for installation on a target system. Packages created by Package Ma

### Package Creation

To create a package using Package Manager, you gather the relevant components into a single directory and build the package using the command line interface.

A *package* is a single compressed file that contains payload files intended for
 installation on a target system. Packages created by Package Manager have a
 .nipkg file extension. You can create three types of packages with
 Package Manager: File packages, Windows Installer (WinInst) packages, and end-user license
 agreement (EULA) packages.

Build a File package when you simply want to install files in directories you specify on a
 target system. File packages cannot include file-level conditions, so Package Manager always
 installs all files you include in the File package payload. In contrast, the payload for
 WinInst packages is one or more MSI files. Building a WinInst package allows you to install
 MSIs and include registry keys, conditions, or .NET assemblies. However, you can include and
 run executables using both package types. Build a EULA package when you want to allow a
 package to display a license agreement when installing the package.

Note

- [Assembling a EULA Package](assemble-eula-package.html) Assemble an End-User License Agreement (EULA) package by creating a root directory that contains subdirectories, source files, and configuration files.
- [Assembling a File Package](assemble-file-package.html) Assemble a File package by creating a root directory that contains subdirectories, source files, and configuration files.
- [Assembling a Relative File Package](assembling-relative-file-package.html) Assemble a relative file package by creating a root directory that contains subdirectories, source files, and configuration files.
- [Assembling a WinInst Package](assemble-wininst-package.html) Assemble a Windows Installer (WinInst) package by creating a root directory that contains subdirectories, source files, and configuration files.
- [Building a Package Using the Command Line Interface](build-package-using-cli.html) Use the command line interface to build a package with your source files.
- [Package Components](package-components.html) A package is comprised of a root directory containing subdirectories, payload files, and configuration files that define the result of the package's installation on the target system.

<!--NI_TOPIC bundle=package-manager path=package-distribution.html language=enus -->
## TOPIC 00022: Package Distribution

- bundle_id: `package-manager`
- source_path: `package-distribution.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/package-distribution.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: To distribute packages, you can deliver individual package files to recipients, or you can create a feed to which recipients subscribe. A feed is a collection of package files that includes a manifest containing information on the included packages. The packages in a feed satisfy all dependencies re

### Package Distribution

To distribute packages, you can deliver individual package files to recipients, or you can create a feed to which recipients subscribe.

A 
 *feed* is a collection of package files that includes a manifest containing information on the included packages. The packages in a feed satisfy all dependencies required for the installation of an application. NI recommends using feeds when distributing multiple packages that have dependencies on one another. With feeds, you can create a single location where you host and maintain all packages intended for end user access.

You can use Package Manager to create and manage a feed for small-scale distributions, such as hosting a feed on a network file server. For large-scale distributions where you need to provide granular user permissions and roles for managing feeds, you can use SystemLink.

- [Creating a Feed](creating-feed.html) Create feeds to distribute multiple packages that have dependencies on one another and consolidate package file updates in one location.
- [Adding a Package to a Feed](add-package-to-feed.html) Use the command line interface to add a package to a feed.
- [Removing a Package from a Feed](remove-package-from-feed.html) Use the command line interface to remove a package from a feed.

<!--NI_TOPIC bundle=package-manager path=package-installation.html language=enus -->
## TOPIC 00023: Package Installation

- bundle_id: `package-manager`
- source_path: `package-installation.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/package-installation.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use Package Manager to install a single package, install multiple packages through a feed, or automate package installation.

### Package Installation

Use Package Manager to install a single package, install
 multiple packages through a feed, or automate package installation.

- [Installing a Single Package](install-single-package.html) You can install a single package on any system with Package Manager installed.
- [Installing Packages from a Feed](install-packages-from-feed.html) To install packages from a feed, you register the feed and install it from the Packages tab.
- [Automating an Installer](automate-installer.html) Automate the unattended or quiet installation of an online installer, offline installer, or Package Manager using the command line interface (CLI).

<!--NI_TOPIC bundle=package-manager path=remove-package-from-feed.html language=enus -->
## TOPIC 00024: Removing a Package from a Feed

- bundle_id: `package-manager`
- source_path: `remove-package-from-feed.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/remove-package-from-feed.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `task`
- source_description: Use the command line interface to remove a package from a feed. Open a command prompt. Change directories to the location of Package Manager. The default location is C:\Program Files\National Instruments\NI Package Manager. Run the following command: nipkg feed-remove-pkg "<location of feed>" "<name

### Removing a Package from a Feed

Use the command line interface to remove a package from a feed.

1. Open a command prompt.
2. Change directories to the location of Package Manager. 
 The default location is 
 C:\Program Files\National Instruments\NI Package Manager.
3. Run the following command: nipkg
 feed-remove-pkg "<location of
 feed>" "<name and filepath of
 package(s)>". 
 For example, if you enter C:\Program Files\National Instruments\NI Package
 Manager> nipkg
 feed-remove-pkg
 "C:\temp\myTestFeed"
 "C:\temp\myTestPackage\my-test-package.nipkg", Package
 Manager removes my-test-package.nipkg from the feed manifest files
 in the C:\temp\myTestFeed directory.

Parent topic:

Package Distribution

Related concepts:

- Package Creation

Related tasks:

- Creating a Feed
- Installing Packages from a Feed

<!--NI_TOPIC bundle=package-manager path=troubleshoot-install-remove-upgrade.html language=enus -->
## TOPIC 00025: Troubleshooting Problems with Installing, Updating, Repairing, or Removing NI Software

- bundle_id: `package-manager`
- source_path: `troubleshoot-install-remove-upgrade.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/troubleshoot-install-remove-upgrade.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table explains potential causes for problems you may encounter while installing, updating, repairing, or removing NI software using Package Manager. Problem Potential Causes Solutions Package Manager asks you to allow removal of packages you did not select. A product installed on your

### Troubleshooting Problems with Installing,
 Updating, Repairing, or Removing NI Software

The following table explains potential causes for problems you may encounter while
 installing, updating, repairing, or removing NI software using Package Manager.

| Problem | Potential Causes | Solutions |
| --- | --- | --- |
| Package Manager asks you to allow removal of packages you did not select. | A product installed on your system depends on the item you are trying to remove. | Click Allow Removal to remove the product along with all of its dependencies, or click Cancel to cancel the removal. |
| The item you are trying to install or update conflicts with a product installed on your system. | Click Allow Removal to remove the conflicting product and install/update the requested items, or click Cancel to cancel the installation/update. |  |
| Package Manager found some problems with your request. | Your request contains conflicts or dependencies that Package Manager cannot resolve. | Review your request for problems, modify your request, and try again. |
| Your request contains a locked package. |  |  |
| Your request contains a package that is not available. |  |  |
| Your request contains one or more packages that are incompatible with your operating system. |  |  |
| The BROWSE PRODUCTS tab is not visible. | Package Manager is not configured to show available products. | Click » GENERAL and select the Show the BROWSE PRODUCTS tab and auto-register product feeds checkbox. |
| You are unable to install, update, or repair software. | You may not be connected to the Internet. You must have an Internet connection if the software you are installing, updating, or repairing is sourced online or on a network server. | Check your Internet and network server connections. If the problem persists, check the log files located at <localappdata>\\National Instruments\\NI Package Manager\\Logs or contact NI for further assistance. |
| The specified source location is inaccessible. | Ensure the source location is accessible or try again. |  |
| You are encountering an MSI failure. | Reboot the machine and try again. |  |
| You are using an outdated version of Package Manager. | Download the latest version of Package Manager from ni.com/downloads. |  |
| You are having trouble detecting or using your hardware within your newly installed product. | You may have deselected Disable Windows fast startup during the installation process. | See the article Hardware Not Detected After Upgrading Windows Version for more information. |
| You are missing support or functionality that you expected to be installed with your product. | You may have declined to install additional software that Package Manager recommended during the installation of your product. | To install the items you declined, open the INSTALLED tab, hover over your product, click (Install or remove related packages), and follow the instructions to select items and install. |
| Some files may be corrupt or missing. | Refer to Installing, Updating, Repairing, and Removing NI Software. |  |

Related tasks:

- Installing, Updating, Repairing, and Removing NI Software

Related information:

- Hardware Not Detected After Upgrading Windows Version
- Software and Driver Downloads

<!--NI_TOPIC bundle=package-manager path=user-manual-welcome.html language=enus -->
## TOPIC 00026: Package Manager User Manual

- bundle_id: `package-manager`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/package-manager/raw/resource/enus/user-manual-welcome.html
- document_id: `package-manager`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Package Manager User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### Package Manager
 User Manual

The Package Manager User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Download Package Manager
- License Setup and Activation
- Package Manager Release Notes
