# NI DOCUMENT BUNDLE: lvrt-api-ref

<!--NI_BUNDLE_CHUNK bundle=lvrt-api-ref start=1 end=145 -->
<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/additional-exclusions-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00001: Additional Exclusions Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/additional-exclusions-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/additional-exclusions-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to configure settings to reduce the size of the stand-alone application, improve load time, and reduce memory usage when you load the resulting build. This page includes the following components: Option Description Typedefs Specifies w

### Additional Exclusions Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to configure settings to reduce the size of the stand-alone application, improve load time, and reduce memory usage when you load the resulting build.

This page includes the following components:

| Option | Description |
| --- | --- |
| Typedefs | Specifies whether to omit type definitions from controls during the output of the build process. Selecting this option for an application with a large number of VIs can potentially reduce the memory usage of the build output. |
| Poly VIs | Specifies to remove unused polymorphic VI instances during the build process. When you add an instance of a polymorphic VI to the block diagram of a VI you include in the build, LabVIEW adds all other instances of the polymorphic VI to the build. If you enable this checkbox, the Application Builder removes any polymorphic VI instances you do not call directly from the block diagram. You may want to disable this option if you dynamically load an instance of a polymorphic VI so the Application Builder does not exclude the polymorphic VI instance you dynamically load from the build. Disabling this checkbox may increase the size of your application. |
| Library members | Specifies to remove unused project library members during the build process. If you enable this checkbox, LabVIEW only includes the VIs from the library you call directly from the block diagram. Enabling this option reduces the application size because LabVIEW does not include the other VIs referenced by the same project library unless the VIs are referenced by other VIs that are part of the build. Library file—If you select to remove unused members of the project library, enable this checkbox to direct LabVIEW to modify the library so that the library file does not refer to the removed members. If you do not modify the project library, the application may take longer to build. |
| Disconnect unused inline subVIs | If you enable this checkbox, LabVIEW does not load any unused inline subVIs into memory when you load the resulting build, which improves load time and reduces memory usage. LabVIEW considers an inline subVI to be unused if VIs within the build only call the subVI statically via the subVI node. LabVIEW does not disconnect unused inline subVIs unless you disable debugging in the build specification on the Advanced page of the dialog box. You also must remove the block diagrams from unused inline subVIs; otherwise, LabVIEW does not disconnect them. Note If an unused inline subVI is a member of a class, LabVIEW loads that subVI into memory when you load the build output even if you enable the Disconnect unused inline subVIs checkbox. |
| Exclude dependent packed libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, LabVIEW excludes copies of dependent packed project libraries to which you link from other build outputs. To exclude dependent packed project library files, LabVIEW retains the links relative to the original dependent packed project libraries instead of copying those files during the build. For example, if you create one build output and then a subsequent build output, you can relatively link the subsequent build output to a file in the first build output. If you leave this checkbox disabled, LabVIEW copies the dependent packed library file to which you linked instead of retaining the relative link to that file. |
| Exclude dependent shared libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, you limit the number of shared libraries LabVIEW copies. When you create one build output and then link to a file in that build output from another build output, LabVIEW traditionally copies the linked file. To limit the number of copied files, LabVIEW retains the links relative to the original files instead of copying the files during the build. Note If you move the original files to which multiple build outputs are linked, those outputs may not load correctly depending on the location to which you move the original files. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/additional-exclusions-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00002: Additional Exclusions Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/additional-exclusions-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/additional-exclusions-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to configure settings to reduce the size of the packed project library. The options on this page do not apply to the .lvlib file you select as the Top-level Library on the Source Files page because LabVIEW includes all files of the

### Additional Exclusions Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to configure settings to reduce the size of the packed project library.

Note

.lvlib

Top-level Library

Source Files

.lvlib

This page includes the following components:

| Option | Description |
| --- | --- |
| Typedefs | Specifies whether to omit type definitions from controls during the output of the build process. Selecting this option for an application with a large number of VIs can potentially reduce the memory usage of the built application. |
| Poly VIs | Specifies to remove unused polymorphic VI instances during the build process. When you add an instance of a polymorphic VI to the block diagram of a VI you include in the build, LabVIEW adds all other instances of the polymorphic VI to the build. If you place a checkmark in this checkbox, LabVIEW removes any polymorphic VI instances you do not call directly from the block diagram. Disable this option if you dynamically load an instance of a polymorphic VI so LabVIEW does not exclude the polymorphic VI instance you dynamically load from the build. Removing the checkmark from this checkbox might increase the size of the packed library. |
| Library members | Specifies to remove unused project library members during the build process. If you place a checkmark in this checkbox, LabVIEW includes only the VIs from the library you call directly from the block diagram. Enabling this option reduces the size of the packed library because LabVIEW does not include the other VIs referenced by the same project library unless the VIs are referenced by other VIs that are part of the build. Library file—If you select to remove unused members of the project library, place a checkmark in this checkbox to direct LabVIEW to modify the library so that the library file does not refer to the removed members. If you do not modify the project library, the packed library might take longer to build. |
| Exclude dependent packed libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, LabVIEW excludes copies of dependent packed project libraries to which you link from other build outputs. To exclude dependent packed project library files, LabVIEW retains the links relative to the original dependent packed project libraries instead of copying those files during the build. For example, if you create one build output and then a subsequent build output, you can relatively link the subsequent build output to a file in the first build output. If you leave this checkbox disabled, LabVIEW copies the dependent packed library file to which you linked instead of retaining the relative link to that file. |
| Exclude dependent shared libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, you limit the number of shared libraries LabVIEW copies. When you create one build output and then link to a file in that build output from another build output, LabVIEW traditionally copies the linked file. To limit the number of copied files, LabVIEW retains the links relative to the original files instead of copying the files during the build. Note If you move the original files to which multiple build outputs are linked, those outputs may not load correctly depending on the location to which you move the original files. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/additional-exclusions-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00003: Additional Exclusions Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/additional-exclusions-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/additional-exclusions-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to configure settings to reduce the size of the shared library, improve load time, and reduce memory usage when you load the resulting build. This page includes the following components: Option Description Typedefs Specifies whether

### Additional Exclusions Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to configure settings to reduce the size of the shared library, improve load time, and reduce memory usage when you load the resulting build.

This page includes the following components:

| Option | Description |
| --- | --- |
| Typedefs | Specifies whether to omit type definitions from controls during the output of the build process. Selecting this option for an application with a large number of VIs can potentially reduce the memory usage of the build output. |
| Poly VIs | Specifies to remove unused polymorphic VI instances during the build process. When you add an instance of a polymorphic VI to the block diagram of a VI you include in the build, LabVIEW adds all other instances of the polymorphic VI to the build. If you enable this checkbox, the Application Builder removes any polymorphic VI instances you do not call directly from the block diagram. You may want to disable this option if you dynamically load an instance of a polymorphic VI so the Application Builder does not exclude the polymorphic VI instance you dynamically load from the build. Disabling this checkbox may increase the size of your application. |
| Library members | Specifies to remove unused project library members during the build process. If you enable this checkbox, LabVIEW only includes the VIs from the library you call directly from the block diagram. Enabling this option reduces the application size because LabVIEW does not include the other VIs referenced by the same project library unless the VIs are referenced by other VIs that are part of the build. Library file—If you select to remove unused members of the project library, enable this checkbox to direct LabVIEW to modify the library so that the library file does not refer to the removed members. If you do not modify the project library, the application may take longer to build. |
| Disconnect unused inline subVIs | If you enable this checkbox, LabVIEW does not load any unused inline subVIs into memory when you load the resulting build, which improves load time and reduces memory usage. LabVIEW considers an inline subVI to be unused if VIs within the build only call the subVI statically via the subVI node. LabVIEW does not disconnect unused inline subVIs unless you disable debugging in the build specification on the Advanced page of the dialog box. You also must remove the block diagrams from unused inline subVIs; otherwise, LabVIEW does not disconnect them. Note If an unused inline subVI is a member of a class, LabVIEW loads that subVI into memory when you load the build output even if you enable the Disconnect unused inline subVIs checkbox. |
| Exclude dependent packed libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, LabVIEW excludes copies of dependent packed project libraries to which you link from other build outputs. To exclude dependent packed project library files, LabVIEW retains the links relative to the original dependent packed project libraries instead of copying those files during the build. For example, if you create one build output and then a subsequent build output, you can relatively link the subsequent build output to a file in the first build output. If you leave this checkbox disabled, LabVIEW copies the dependent packed library file to which you linked instead of retaining the relative link to that file. |
| Exclude dependent shared libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, you limit the number of shared libraries LabVIEW copies. When you create one build output and then link to a file in that build output from another build output, LabVIEW traditionally copies the linked file. To limit the number of copied files, LabVIEW retains the links relative to the original files instead of copying the files during the build. Note If you move the original files to which multiple build outputs are linked, those outputs may not load correctly depending on the location to which you move the original files. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/additional-exclusions-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00004: Additional Exclusions Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/additional-exclusions-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/additional-exclusions-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to configure settings to reduce the size of the source distribution, improve load time, and reduce memory usage when you load the resulting build. This page includes the following components: Option Description Typedefs Specifi

### Additional Exclusions Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to configure settings to reduce the size of the source distribution, improve load time, and reduce memory usage when you load the resulting build.

This page includes the following components:

| Option | Description |
| --- | --- |
| Typedefs | Specifies whether to omit type definitions from controls during the output of the build process. Selecting this option for an application with a large number of VIs can potentially reduce the memory usage of the build output. |
| Poly VIs | Specifies to remove unused polymorphic VI instances during the build process. When you add an instance of a polymorphic VI to the block diagram of a VI you include in the build, LabVIEW adds all other instances of the polymorphic VI to the build. If you enable this checkbox, the Application Builder removes any polymorphic VI instances you do not call directly from the block diagram. You may want to disable this option if you dynamically load an instance of a polymorphic VI so the Application Builder does not exclude the polymorphic VI instance you dynamically load from the build. Disabling this checkbox may increase the size of your application. |
| Library members | Specifies to remove unused project library members during the build process. If you enable this checkbox, LabVIEW only includes the VIs from the library you call directly from the block diagram. Enabling this option reduces the application size because LabVIEW does not include the other VIs referenced by the same project library unless the VIs are referenced by other VIs that are part of the build. Library file—If you select to remove unused members of the project library, enable this checkbox to direct LabVIEW to modify the library so that the library file does not refer to the removed members. If you do not modify the project library, the application may take longer to build. |
| Disconnect unused inline subVIs | If you enable this checkbox, LabVIEW does not load any unused inline subVIs into memory when you load the resulting build, which improves load time and reduces memory usage. LabVIEW considers an inline subVI to be unused if VIs within the build only call the subVI statically via the subVI node. LabVIEW does not disconnect unused inline subVIs unless you disable debugging in the build specification on the Advanced page of the dialog box. You also must remove the block diagrams from unused inline subVIs; otherwise, LabVIEW does not disconnect them. Note If an unused inline subVI is a member of a class, LabVIEW loads that subVI into memory when you load the build output even if you enable the Disconnect unused inline subVIs checkbox. |
| Exclude dependent packed libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, LabVIEW excludes copies of dependent packed project libraries to which you link from other build outputs. To exclude dependent packed project library files, LabVIEW retains the links relative to the original dependent packed project libraries instead of copying those files during the build. For example, if you create one build output and then a subsequent build output, you can relatively link the subsequent build output to a file in the first build output. If you leave this checkbox disabled, LabVIEW copies the dependent packed library file to which you linked instead of retaining the relative link to that file. |
| Exclude dependent shared libraries | Specifies to reduce the overall number of files in a build output. When you enable this checkbox, you limit the number of shared libraries LabVIEW copies. When you create one build output and then link to a file in that build output from another build output, LabVIEW traditionally copies the linked file. To limit the number of copied files, LabVIEW retains the links relative to the original files instead of copying the files during the build. Note If you move the original files to which multiple build outputs are linked, those outputs may not load correctly depending on the location to which you move the original files. |
| Exclude files from vi.lib | Excludes all files in the vi.lib directory from the source distribution. |
| Exclude instr.lib | Excludes all files in the instr.lib directory from the source distribution. |
| Exclude user.lib | Excludes all files in the user.lib directory from the source distribution. Note LabVIEW only excludes files in vi.lib, instr.lib, and user.lib if you do not select them as Always Included in the Source Files page of the Source Distribution Properties dialog box. |
| Options for compiled code | Options for compiled code Preserve compiled code—By default, LabVIEW creates one file to contain the source code and object code for all the files you include in the source distribution. Remove compiled code—Separates compiled code from all the files you include in the source distribution. Note Do not separate compiled code if you intend to load the VIs produced by the source distribution in the LabVIEW Run-Time Engine. Preserve file settings of each VI or library—Maintains the settings for each file in the source distribution. For example, if you include both source-only VIs and VIs that maintain compiled code in a source distribution, use this option to preserve the original settings of each VI. |

#### Building Editable and Run-Time Source Distributions

- Editable source distributions —Build this type of source distribution to package and send code for use in another LabVIEW development environment. The default options in LabVIEW primarily support this use case. Because these source distributions are editable, LabVIEW leaves most of the components that provide optimization unchecked. If necessary, you can change the default components to provide more optimization.
- Run-time source distributions —Build this type of source distribution to be a plugin which is loaded into a stand-alone application. Because you typically include a run-time source distribution in a stand-alone application, avoid editing the code for a source distribution with this use case. Configure run-time source distributions for optimization in order to reduce the output size on disk.

| Component | Editable Source Distributions | Run-Time Source Distributions |
| --- | --- | --- |
| Disconnect type definitions | Remove the checkmark from this box. Preserve type definitions because you can edit the code for source distributions with this use case. | Place a checkmark in this box to avoid including unnecessary files for optimization. |
| Remove unused polymorphic VI instances | Remove the checkmark from this box. Preserve unused polymorphic VI instances because you can edit the code for a source distribution with this use case. | Place a checkmark in this box to remove unused polymorphic VI instances for optimization. |
| Remove unused members of project libraries | Remove the checkmark from this box. Preserve the original library because the code for the source distribution is loaded in the LabVIEW development environment. | Place a checkmark in this box to avoid including unnecessary files for optimization. |
| Modify project library file after removing unused members |  | Remove the checkmark from this box if the source distribution and the stand-alone application that loads the source distribution contain VIs from the same library. If you do not remove the checkmark from this checkbox, the application loads and modifies the library that it shares with the source distribution. Furthermore, the library no longer contains references to the VIs in the source distribution and causes the VIs in the source distribution to break when loaded into the application. For example, if you want to include a source distribution that contains Mean VI within a stand-alone application that contains Median VI, and Mean VI and Median VI belong to the same project library, remove the checkmark from this checkbox when building the stand-alone application. Otherwise, the project library in the stand-alone application only contains a reference to Median VI after removing unused members and modifying the library file. When the stand-alone application loads the source distribution, Mean VI breaks upon load because the library within the stand-alone application no longer contains a reference to Mean VI. Place a checkmark in this box to reduce file size if the source distribution and loading stand-alone application do not contain VIs that are part of the same library. |
| Exclude files from vi.lib | Place a checkmark in this box. Exclude the files from vi.lib because LabVIEW loads the code for the source distribution in the LabVIEW development environment. | Remove the checkmark from this box. A source distribution must include all file dependencies because the stand-alone application that calls the source distribution does not include a vi.lib directory. |
| Exclude files from instr.lib | Place a checkmark in this box. Exclude the files from instr.lib because LabVIEW loads the code for the source distribution in the LabVIEW development environment. | Remove the checkmark from this box. A source distribution must include all file dependencies because the stand-alone application that calls the source distribution does not include an instr.lib directory. |
| Exclude files from user.lib | Place a checkmark in this box. Exclude the files from user.lib because LabVIEW loads the code for the source distribution in the LabVIEW development environment. | Remove the checkmark from this box. A source distribution must include all file dependencies because the stand-alone application that calls the source distribution does not include a user.lib directory. |
| Remove compiled code | Place a checkmark in this box if you want to reduce file size and ensure that LabVIEW addresses automatic or mutation changes without requiring you to save. Remove the checkmark from this box if you want to ensure that each file contains its source code and object code within one file and guarantee that the LabVIEW Run-Time Engine can load all files. | Remove the checkmark from this box. VIs with separate compiled code will fail to load because the LabVIEW Run-Time Engine cannot load files from the compiled object cache that stores the separate compiled code. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/advanced-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00005: Advanced Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/advanced-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/advanced-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to configure advanced settings for a stand-alone real-time application. This page includes the following components: Option Description Enable debugging Enables debugging for the real-time stand-alone application from a host computer.

### Advanced Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to configure advanced settings for a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Enable debugging | Enables debugging for the real-time stand-alone application from a host computer. Wait for debugging—Sets the application, shared library, or .NET interop assembly to load but not run until the user enables it to run through the LabVIEW debugging controls. Place a checkmark in the Enable debugging checkbox to enable this option. |
| Copy error code files | Adds copies of XML-based LabVIEW error code text files from the project\\errors and user.lib\\errors directories to the run-time engine. Note You must manually create an errors folder in the labview\\user.lib directory to organize your error code files. |
| Use custom alias | Copies the project aliases file with the application, shared library, or .NET interop assembly. If you place a checkmark in the checkbox, the Select Project File dialog box appears and you can select an aliases file in the project. Aliases file in project—Specifies the aliases file to use with the application, shared library, or .NET interop assembly if you select Use custom aliases file. BrowseAlias—Displays the Select Project File dialog box, which you can use to select an aliases file. |
| Enhanced DSC support | This option only appears if you have the LabVIEW Datalogging and Supervisory Control (DSC) Module installed. Builds the application with the enhanced DSC Module Run-Time Engine. The DSC Module Run-Time Engine adds additional support for programmatic project library and shared variable management in applications that you build with the DSC Module.You must place a checkmark in this checkbox in the following situations: The application you want to build uses VI Server references to modify a library file programmatically. The application you want to build uses the Save to Library VI. If you do not enable the enhanced DSC Module Run-Time Engine in these two situations, LabVIEW returns error code 1055 when you run the built application, shared library, or .NET interop assembly. Note Enabling this option increases the file size and reduces the start-up performance of the built application, shared library, or .NET interop assembly. |
| Generate user log file | Specifies whether to create a log file for the build. The build log file lists all files contained in the build, including subVIs you do not specify as Startup VIs or Always Included. The log file also contains general build information such as build start and end time, the build specification and project name, and any errors that occurred during the build. Log file path—Specifies the path to save the build log file. |
| Use LabVIEW 8.x file layout | Specifies to use a flat file layout to store source files inside a stand-alone application, shared library, or Web service. LabVIEW enables this option by default for build specifications you load from LabVIEW 8.6 or earlier. National Instruments recommends you disable this option for applications you develop in LabVIEW 2009 or later. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/advanced-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00006: Advanced Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/advanced-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/advanced-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to configure advanced settings for a packed project library. This page includes the following components: Option Description Enable debugging Enables debugging for the packed library. Place a checkmark in the Enable Debugging checkb

### Advanced Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to configure advanced settings for a packed project library.

This page includes the following components:

| Option | Description |
| --- | --- |
| Enable debugging | Enables debugging for the packed library. Place a checkmark in the Enable Debugging checkbox to include block diagrams or front panels with VIs. Use the block diagram of VIs to debug issues with a packed library. Note Disabling this checkbox does not ensure full optimization. |
| Generate user log file | Specifies whether to create a log file for the build. The build log file lists all files contained in the build, including subVIs you do not specify as Always Included. The log file also contains general build information, such as build start and end time, the build specification and project name, and any errors that occur during the build. Log file path—Specifies the path to save the build log file. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/advanced-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00007: Advanced Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/advanced-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/advanced-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to change advanced settings for a shared library. This page includes the following components: Option Description Enable debugging Enables debugging for the application, shared library, .NET interop assembly, or Web service. Disabli

### Advanced Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to change advanced settings for a [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Enable debugging | Enables debugging for the application, shared library, .NET interop assembly, or Web service. Note Disabling this checkbox does not ensure full optimization. Wait for debugging—Sets the application, shared library, or .NET interop assembly to load but not run until the user enables it to run through the LabVIEW debugging controls. Place a checkmark in the Enable debugging checkbox to enable this option. |
| Copy error code files | Adds copies of XML-based LabVIEW error code text files from the project\\errors and user.lib\\errors directories to the run-time engine.Note You must manually create an errors folder in the labview\\user.lib directory to organize your error code files. |
| Use custom alias | Copies the project aliases file with the application, shared library, or .NET interop assembly. If you place a checkmark in the checkbox, the Select Project File dialog box appears and you can select an aliases file in the project. Aliases file in project—Specifies the aliases file to use with the application, shared library, or .NET interop assembly if you select Use custom aliases file. BrowseAlias—Displays the Select Project File dialog box, which you can use to select an aliases file. |
| DelayOSMsg | Delays operating system messages until calls to shared library functions end or until you load a modal window from the shared library.You might choose to delay operating system messages, such as mouse or keyboard messages from the user, in order to avoid calling the same shared library file while a shared library function runs. For example, if the shared library function is called in response to the user pressing a button, the user should not be able to press the button again until the shared library function has completed. If you load a modal window from the shared library, LabVIEW overrides this option and processes the messages to allow the modal window to become active. You cannot interact with other windows while a modal window is open. Most LabVIEW dialog boxes are modal windows. Remove the checkmark from this checkbox if you want to process operating system messages while shared library functions run. |
| IncludeHeaders | Copies into the built shared library any additional LabVIEW header files that are referenced by the header file that is generated during the build process. Including additional header files allows you to use a LabVIEW-built shared library in C or another language that requires those header files. |
| Enhanced DSC support | This option only appears if you have the LabVIEW Datalogging and Supervisory Control (DSC) Module installed. Builds the application with the enhanced DSC Module Run-Time Engine. The DSC Module Run-Time Engine adds additional support for programmatic project library and shared variable management in applications that you build with the DSC Module. You must place a checkmark in this checkbox in the following situations: The application you want to build uses VI Server references to modify a library file programmatically. The application you want to build uses the Save to Library VI. If you do not enable the enhanced DSC Module Run-Time Engine in these two situations, LabVIEW returns error code 1055 when you run the built application, shared library, or .NET interop assembly. Note Enabling this option increases the file size and reduces the start-up performance of the built application, shared library, or .NET interop assembly. |
| Generate user log file | Specifies whether to create a log file for the build. The build log file lists all files contained in the build, including subVIs you do not specify as Startup VIs or Always Included. The log file also contains general build information such as build start and end time, the build specification and project name, and any errors that occurred during the build. Log file path—Specifies the path to save the build log file. |
| Use LabVIEW 8.x file layout | Specifies to use a flat file layout to store source files inside a stand-alone application, shared library, or Web service. LabVIEW enables this option by default for build specifications you load from LabVIEW 8.6 or earlier. National Instruments recommends you disable this option for applications you develop in LabVIEW 2009 or later. |
| labVIEW 2011 compatibility mode | Specifies whether to generate the shared library using the same style as shared libraries built in LabVIEW 2011 and earlier. Disable this checkbox to generate the shared library using the style of LabVIEW 2012 and later. If you migrate a build specification created in LabVIEW 2011 or earlier, this checkbox contains a checkmark by default. Disabling this checkbox might cause unintended errors if pre-existing code relies on the migrated build specification.The following table lists how each style changes the generated shared library. LabVIEW 2011 compatibility mode LabVIEW 2012 and later LabVIEW generates a C function name from the name of the VI and does not include the owning library hierarchy in the function name. LabVIEW generates qualified C function names for the VIs of a project. A qualified name is a name based on the owning library hierarchy of a VI in addition to the VI name. For example, if Foo.vi belongs to FooLib.lvlib, LabVIEW generates the C function name as FooLib_Foo. For projects created prior to LabVIEW 2012 that already have exported VIs, the generated function prototype names are not qualified. To generate these functions with qualified names, remove the corresponding VIs from the Exported VIs list on the Source Files page and then add these VIs back to the Exported VIs list. LabVIEW generates generic type names, such as TD1 and TD2, for LabVIEW enum, cluster, and array type definitions. LabVIEW generates qualified type names for LabVIEW enum, cluster, and array type definitions by preserving the type name you assigned in the VI. For LabVIEW enums, clusters, and arrays that are not type definitions, LabVIEW generates more meaningful names such as int32Array,Cluster1, and Enum1. LabVIEW does not expose enum values in the generated header file. LabVIEW exposes enum values in the generated header file. Functions generated from VIs containing error in and error out clusters include error in and error out parameters. When LabVIEW generates a C function for a VI, LabVIEW does not export the error in and error out clusters as parameters of the new function. Instead, the return value of the function contains the error code of the error out cluster. To get or clear the error message, use the LVGetLastErrorMsg and LVClearLastErrorMsg functions, which are exposed in the extcode.h header file in the labview\\cintools directory. For VIs containing multiple error out parameters, you can use the Define VI Prototype dialog box to choose which error out parameter the generated function uses to return error code information. |
| LabVIEW 2011 compatibility mode | LabVIEW 2012 and later |
| LabVIEW generates a C function name from the name of the VI and does not include the owning library hierarchy in the function name. | LabVIEW generates qualified C function names for the VIs of a project. A qualified name is a name based on the owning library hierarchy of a VI in addition to the VI name. For example, if Foo.vi belongs to FooLib.lvlib, LabVIEW generates the C function name as FooLib_Foo. For projects created prior to LabVIEW 2012 that already have exported VIs, the generated function prototype names are not qualified. To generate these functions with qualified names, remove the corresponding VIs from the Exported VIs list on the Source Files page and then add these VIs back to the Exported VIs list. |
| LabVIEW generates generic type names, such as TD1 and TD2, for LabVIEW enum, cluster, and array type definitions. | LabVIEW generates qualified type names for LabVIEW enum, cluster, and array type definitions by preserving the type name you assigned in the VI. For LabVIEW enums, clusters, and arrays that are not type definitions, LabVIEW generates more meaningful names such as int32Array,Cluster1, and Enum1. |
| LabVIEW does not expose enum values in the generated header file. | LabVIEW exposes enum values in the generated header file. |
| Functions generated from VIs containing error in and error out clusters include error in and error out parameters. | When LabVIEW generates a C function for a VI, LabVIEW does not export the error in and error out clusters as parameters of the new function. Instead, the return value of the function contains the error code of the error out cluster. To get or clear the error message, use the LVGetLastErrorMsg and LVClearLastErrorMsg functions, which are exposed in the extcode.h header file in the labview\\cintools directory. For VIs containing multiple error out parameters, you can use the Define VI Prototype dialog box to choose which error out parameter the generated function uses to return error code information. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/advanced-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00008: Advanced Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/advanced-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/advanced-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to change advanced settings for a source distribution. This page includes the following components: Option Description Generate user log file Specifies whether to create a log file for the build. The build log file lists all fi

### Advanced Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to change advanced settings for a [source distribution](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Generate user log file | Specifies whether to create a log file for the build. The build log file lists all files contained in the build, including subVIs you do not specify as Startup VIs or Always Included. The log file also contains general build information such as build start and end time, the build specification and project name, and any errors that occurred during the build. Log file path—Specifies the path to save the build log file. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/alerts-probe-view.html language=enus -->
## TOPIC 00009: Alerts Probe View

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/alerts-probe-view.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/alerts-probe-view.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select a real-time target to display a target probe in the Auto View. You also can right-click the target and select Probe to display the probe in a separate window. Click the Alerts tab of a real-time target probe to display this view. Use this view to configure and monitor alerts on the real-time

### Alerts Probe View

Select a real-time target to display a target probe in the **Auto View**. You also can right-click the target and select **Probe** to display the probe in a separate window. Click the **Alerts** tab of a real-time target probe to display this view. Use this view to configure and monitor alerts on the real-time target.

This view includes the following components:

| Option | Description |
| --- | --- |
| Log Alert when memory usage is above | Enables alert logging when memory usage on the real-time target exceeds the value you specify. |
| Log Alert when CPU usage is above | Enables alert logging when the real-time target CPU usage exceeds the value you specify. |
| Log Alert when VI changes state | Enables alert logging when a VI listed in the VI States view changes state. |
| Recent Alerts | Lists recently-logged alerts. |
| Clear | Removes all entries from the Recent Alerts list. |
| Save | Saves the Recent Alerts list as a text file on the local computer. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/connector-pane-state-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00010: Connector Pane State Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/connector-pane-state-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/connector-pane-state-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to specify whether caller VIs adapt to the memory allocation changes of exported VIs in a packed project library. This page includes the following component: Option Description Callers adapt Specifies whether a caller VI adapts to c

### Connector Pane State Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to specify whether [caller VIs adapt to the memory allocation changes](/csh?productcategories=147794&context=lvcore_lvconcepts_packed_libraries) of exported VIs in a packed project library.

This page includes the following component:

| Option | Description |
| --- | --- |
| Callers adapt | Specifies whether a caller VI adapts to connector pane changes of the exported VIs without recompiling.If you do not remove the checkmark from the checkbox, the caller VI adapts to connector pane changes of a VI in a packed library. If you remove the checkmark from this checkbox, the caller VI does not adapt and might need to recompile when you make connector pane changes to a VI. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/destinations-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00011: Destinations Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/destinations-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/destinations-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to configure and add destination directories for a stand-alone real-time application. This page includes the following components: Option Description Destinations Specifies the destination directories in which you want to include sourc

### Destinations Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to configure and add destination directories for a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Destinations | Specifies the destination directories in which you want to include source distribution files. Click the New Destination and Remove Destination buttons to add and delete directories from the list. |
| AddDestination | Adds a custom destination directory to the Destinations listbox. |
| RemoveDestination | Removes the destination directory you select from the Destinations listbox. You cannot remove the default destination directory or the support directory. |
| Destination label | Specifies the name that the dialog box uses for the directory you select in the Destinations listbox. Edit the label if you want to change the name. You cannot change the name of the default destination directory or support directory.Editing the destination label has no effect on the directory name on disk. |
| Destination path | Specifies the path to the directory you select in the Destinations listbox.Click the Browse button to navigate to and select a path. If you change the path of the default destination directory, any destinations that are subdirectories automatically update to reflect the new path. Append the [VersionNumber] tag to the path so LabVIEW includes the version of the build when constructing the build directory. For example, the path C:\\temp\\builds\\[VersionNumber] creates the C:\\temp\\builds\\1.0.0.0 directory on disk. The next time you build, the directory on disk increments to C:\\temp\\builds\\1.0.0.1 and so on. Use the [VersionNumbe] tag for the Application (EXE), .NET Interop Assembly, Packed Library, Shared Library (DLL), and Source Distribution build specifications. |
| Destination type | Specifies the destination type of the item you select in the Destinations listbox.You cannot change this setting for applications or support directories. Directory—Specifies that the destination is a directory. Preserve disk hierarchy—Preserves the disk hierarchy of the files targeted to this destination directory. LLB—Specifies that the destination is an LLB. |
| Add to library | Specifies that you want to add files you move to the selected destination to a new project library. Library name—Name of the new project library to which LabVIEW adds the files. |
| Custom Destinations | The following components appear when you select the Custom packaging option. Destinations—Specifies the destination directories in which you want to include source distribution files. Click the Add and Remove Destination buttons to add and delete directories from the list. NewDestination—Adds a destination directory to the Destinations listbox. RemoveDestination—Removes the selected destination directory from the Destinations listbox. You cannot remove any default destination directory that is already present in the Destinations list. Destination label—Specifies the name that the dialog box uses for the directory you select in the Destinations listbox. Edit the label if you want to change the name. You cannot change the name of the default destination directory or support directory.Editing the destination label has no effect on the directory name on disk. Destination path—Specifies the path to the directory you select in the Destinations listbox.Click the Browse button to navigate to and select a path. If you change the path of the default destination directory, any destinations that are subdirectories automatically update to reflect the new path. Append the [VersionNumbe] tag to the path so LabVIEW includes the version of the build when constructing the build directory. For example, the path C:\\temp\\builds\\[VersionNumber] creates the C:\\temp\\builds\\1.0.0.0 directory on disk. The next time you build, the directory on disk increments to C:\\temp\\builds\\1.0.0.1 and so on. Use the [VersionNumbe] tag for the Application (EXE), .NET Interop Assembly, Packed Library, Shared Library (DLL), and Source Distribution build specifications. Destination is LLB—Place a checkmark in this checkbox if you want the specified destination directory to be an LLB file. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/destinations-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00012: Destinations Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/destinations-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/destinations-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to configure the destination settings and add destination directories to a packed project library. This page includes the following components: Option Description Destinations Specifies the destination directories in which you want

### Destinations Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to configure the destination settings and add destination directories to a packed project library.

This page includes the following components:

| Option | Description |
| --- | --- |
| Destinations | Specifies the destination directories in which you want to include the files that the build generates. Click the Add Destination and Remove Destination buttons to add and delete directories.The first destination in the list corresponds with the Target filename on the Information page. |
| AddDestination | Adds a custom destination directory to the Destinations listbox. |
| RemoveDestination | Removes the selected destination directory from the Destinations listbox. You cannot remove any default destination directory that is already present in the Destinations list. |
| Destination label | Specifies the name for the directory selected in the Destinations listbox. You can select these names as destinations on the Source File Settings page in the Destination pull-down menu. You cannot change the Destination label setting for the target filename or support directories.If you do not change the text in the Destination path text box, editing the destination label updates the text in the Destination path text box. |
| Destination path | Specifies the path to the directory or LLB you select in the Destinations listbox. If you change the path of the target filename, any destinations that are subdirectories automatically update to reflect the new path. Note To avoid receiving an error during the build process, ensure that file paths for the destination directory, including the filename, are less than 255 characters. When you select Support Directory from the Destinations list, Destination path specifies where non-LabVIEW files save when you build the packed library. The default location for Support Directory is the same location as the destination directory of the packed library. Append the [VersionNumber] tag to the path so LabVIEW includes the version of the build when constructing the build directory. For example, the path C:\\temp\\builds\\[VersionNumber] creates the C:\\temp\\builds\\1.0.0.0 directory on disk. The next time you build, the directory on disk increments to C:\\temp\\builds\\1.0.0.1 and so on. Use the [VersionNumber] tag for the Application (EXE), .NET Interop Assembly, Packed Library, Shared Library (DLL), and Source Distribution build specifications. |
| Destination type | Specifies the destination type of the item you select in the Destinations listbox.You cannot change this setting for applications or support directories. Directory—Specifies that the destination is a directory. Preserve disk hierarchy—Preserves the disk hierarchy of the files targeted to this destination directory. LLB—Specifies that the destination is an LLB. |
| Add to library | Specifies that you want to add files you move to the selected destination to a new project library. Library name—Name of the new project library to which LabVIEW adds the files. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/destinations-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00013: Destinations Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/destinations-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/destinations-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to configure the destination settings and add destination directories to a shared library. This page includes the following components: Option Description Destinations Specifies the destination directories in which you want to inclu

### Destinations Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to configure the destination settings and add destination directories to a [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Destinations | Specifies the destination directories in which you want to include the files that the build generates. Click the Add Destination and Remove Destination buttons to add and delete directories.The first destination in the list corresponds with the Target filename on the Information page. |
| AddDestination | Adds a custom destination directory to the Destinations listbox. |
| RemoveDestination | Removes the destination directory you select from the Destinations listbox. You cannot remove the default destination directory or the support directory. |
| Destination label | Specifies the name for the directory selected in the Destinations listbox. You can select these names as destinations on the Source File Settings page in the Destination pull-down menu. You cannot change the Destination label setting for the target filename or support directories.If you do not change the text in the Destination path text box, editing the destination label updates the text in the Destination path text box. |
| Destination path | Specifies the path to the directory or LLB you select in the Destinations listbox.If you change the path of the target filename, any destinations that are subdirectories automatically update to reflect the new path. Note To avoid receiving an error during the build process, ensure that file paths for the destination directory, including the filename, are less than 255 characters. Append the [VersionNumber] tag to the path so LabVIEW includes the version of the build when constructing the build directory. For example, the path C:\\temp\\builds\\[VersionNumber] creates the C:\\temp\\builds\\1.0.0.0 directory on disk. The next time you build, the directory on disk increments to C:\\temp\\builds\\1.0.0.1 and so on. Use the [VersionNumber] tag for the Application (EXE), .NET Interop Assembly, Packed Library, Shared Library (DLL), and Source Distribution build specifications. |
| Destination type | Specifies the destination type of the item you select in the Destinations listbox.You cannot change this setting for applications or support directories. Directory—Specifies that the destination is a directory. Preserve disk hierarchy—Preserves the disk hierarchy of the files targeted to this destination directory. LLB—Specifies that the destination is an LLB. |
| Add to library | Specifies that you want to add files you move to the selected destination to a new project library. Library name—Name of the new project library to which LabVIEW adds the files. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/destinations-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00014: Destinations Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/destinations-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/destinations-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to configure the destination settings and add destination directories to a source distribution. This page includes the following components: Option Description Destinations Specifies the destination directories in which you wan

### Destinations Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to configure the destination settings and add destination directories to a source distribution.

This page includes the following components:

| Option | Description |
| --- | --- |
| Destinations | Specifies the destination directories in which you want to include the files that the build generates. Note To avoid receiving an error during the build process, ensure that file paths for the destination directory, including the filename, are less than 255 characters.Click the Add Destination and Remove Destination buttons to add and delete directories from the list. |
| AddDestination | Adds a custom destination directory to the Destinations listbox. |
| RemoveDestination | Removes the selected destination directory from the Destinations listbox. You cannot remove any default destination directory that is already present in the Destinations list. |
| Destination label | Specifies the name that the Application Builder uses for the directory selected in the Destinations listbox. You can select these names as destinations on the Source File Settings page in the pull-down menu. You cannot change the Destination label setting for the destination or support directories.If you do not change the text in the Destination path text box, editing the destination label updates the text in the Destination path text box. |
| Destination path | Specifies the path to the directory or LLB you select in the Destinations listbox.Click the Browse button to navigate to and select a path. If you change the path of the destination directory, any destinations that are subdirectories automatically update to reflect the new path. Append the [VersionNumber] tag to the path so LabVIEW includes the version of the build when constructing the build directory. For example, the path C:\\temp\\builds\\[VersionNumber] creates the C:\\temp\\builds\\1.0.0.0 directory on disk. The next time you build, the directory on disk increments to C:\\temp\\builds\\1.0.0.1 and so on. Use the [VersionNumber] tag for the Application (EXE), .NET Interop Assembly, Packed Library, Shared Library (DLL), and Source Distribution build specifications. |
| Destination type | Specifies the destination type of the item you select in the Destinations listbox.You cannot change this setting for applications or support directories. Directory—Specifies that the destination is a directory. Preserve disk hierarchy—Preserves the disk hierarchy of the files targeted to this destination directory. LLB—Specifies that the destination is an LLB. |
| Add to library | Specifies that you want to add files you move to the selected destination to a new project library. Library name—Name of the new project library to which LabVIEW adds the files. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/information-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00015: Information Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/information-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/information-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to specify a name, executable filename, local destination, and target destination for a stand-alone real-time application. This page includes the following components: Option Description Build specification name Specifies the name of t

### Information Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to specify a name, executable filename, local destination, and target destination for a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies the name of the build specification for the stand-alone real-time application. The name appears under Build Specifications of the RT target on the Project Explorer window. |
| Target filename | Specifies the filename for the stand-alone real-time application.By default, the Application Builder creates the stand-alone application using startup.rtexe as the Target filename. You must change the Target filename if you want to create more than one stand-alone real-time application on the RT target. |
| Local destination directory | Specifies the location on the host computer to save the build. You can enter a path or use the Browse button to navigate to and select the location. |
| Target destination directory | Specifies the location on the RT target to save the build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/information-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00016: Information Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/information-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/information-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to name the packed project library and select locations for the library on both the host computer and the RT target. This page includes the following components: Option Description Build specification name Specifies a unique name fo

### Information Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to name the packed project library and select locations for the library on both the host computer and the RT target.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Target filename | Specifies the filename for the library. (Packed Libraries)Packed libraries must have a .lvlibp extension.When you select a .lvlib file as a Top-level Library on the Source Files page, Target filename changes to the same name as the project library. |
| Local destination directory | Specifies the location on the host computer to save the build. You can enter a path or use the Browse button to navigate to and select the location. |
| Target destination directory | Specifies the location on the RT target to save the build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/information-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00017: Information Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/information-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/information-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to name the shared project library and select locations for the library on both the host computer and the RT target. This page includes the following components: Option Description Build specification name Specifies a unique name fo

### Information Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to name the shared project library and select locations for the library on both the host computer and the RT target.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Target filename | Specifies the filename for the library. |
| Local destination directory | Specifies the location on the host computer to save the build. You can enter a path or use the Browse button to navigate to and select the location. |
| Target destination directory | Specifies the location on the RT target to save the build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/information-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00018: Information Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/information-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/information-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to name the source distribution and select the locations to build the source distribution both on the host computer and on the RT target. This page includes the following components: Option Description Build specification name

### Information Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to name the source distribution and select the locations to build the source distribution both on the host computer and on the RT target.

This page includes the following components:

| Option | Description |
| --- | --- |
| Build specification name | Specifies a unique name for the build specification. The name appears under Build Specifications in the Project Explorer window. |
| Local destination directory | Specifies the location on the host computer to save the build. You can enter a path or use the Browse button to navigate to and select the location. |
| Target destination directory | Specifies the location on the RT target to save the build. |
| Build specification description | Displays information about the build specification. You can view and edit the description on this page only. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/lvrt-dialog-box-help.html language=enus -->
## TOPIC 00019: LabVIEW Real-Time Module Dialog Box Reference

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/lvrt-dialog-box-help.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/lvrt-dialog-box-help.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find detailed information about LabVIEW Real-time Module dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box. These pages are available by clicking the Help buttons in the dialog boxes.

### LabVIEW Real-Time Module Dialog Box Reference

Find detailed information about LabVIEW Real-time Module dialog boxes, including the purpose of the dialog box, how to access the dialog box, and detailed information about the controls and indicators in the dialog box.

These pages are available by clicking the **Help** buttons in the dialog boxes.

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/pre-post-build-actions-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00020: Pre/Post Build Actions Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/pre-post-build-actions-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/pre-post-build-actions-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to specify VIs for LabVIEW to execute before or after the build. Option Description executePreVI Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the LabVIE

### Pre/Post Build Actions Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to [specify VIs for LabVIEW to execute](/csh?productcategories=147794&context=lvcore_lvconcepts_running_vis_before_after) before or after the build.

| Option | Description |
| --- | --- |
| executePreVI | Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the LabVIEW project. When you place a checkmark in this checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the pre-build template VI. If you do not have a VI previously generated from the pre-build template, use the Generate VI button to execute a VI before the build. If the pre-build VI returns an error before a build, the build does not continue, and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePreVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate pre-build | Creates a VI with the pre-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes before the build must match the connector pane of the pre-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |
| executePostVI | Includes a VI that executes after the build. Make sure the VI you want to include is under the target, such as My Computer, in the project. When you place a checkmark in the checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the post-build template VI. If you do not have a VI previously generated from the post-build template, use the Generate VI button to execute a VI after the build. If LabVIEW returns an error during the build, the post-build VI still runs. If the post-build VI returns an error during the build, the build fails and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePostVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate post-build | Creates a VI with the post-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes after the build must match the connector pane of the post-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/pre-post-build-actions-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00021: Pre/Post Build Actions Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/pre-post-build-actions-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/pre-post-build-actions-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to specify VIs for LabVIEW to execute before or after the build for the packed project library. Option Description executePreVI Includes a VI that executes before the build. Make sure the VI you want to include is under the target,

### Pre/Post Build Actions Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to [specify VIs for LabVIEW to execute](/csh?productcategories=147794&context=lvcore_lvconcepts_running_vis_before_after) before or after the build for the packed project library.

| Option | Description |
| --- | --- |
| executePreVI | Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the LabVIEW project.When you place a checkmark in this checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the pre-build template VI. If you do not have a VI previously generated from the pre-build template, use the Generate VI button to execute a VI before the build. If the pre-build VI returns an error before a build, the build does not continue, and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePreVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate pre-build | Creates a VI with the pre-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes before the build must match the connector pane of the pre-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |
| executePostVI | Includes a VI that executes after the build. Make sure the VI you want to include is under the target, such as My Computer, in the project. When you place a checkmark in the checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the post-build template VI. If you do not have a VI previously generated from the post-build template, use the Generate VI button to execute a VI after the build. If LabVIEW returns an error during the build, the post-build VI still runs. If the post-build VI returns an error during the build, the build fails and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePostVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate post-build | Creates a VI with the post-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes after the build must match the connector pane of the post-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/pre-post-build-actions-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00022: Pre/Post Build Actions Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/pre-post-build-actions-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/pre-post-build-actions-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to specify VIs for LabVIEW to execute before or after the build. Option Description executePreVI Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the Lab

### Pre/Post Build Actions Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to [specify VIs for LabVIEW to execute](/csh?productcategories=147794&context=lvcore_lvconcepts_running_vis_before_after) before or after the build.

| Option | Description |
| --- | --- |
| executePreVI | Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the LabVIEW project.When you place a checkmark in this checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the pre-build template VI. If you do not have a VI previously generated from the pre-build template, use the Generate VI button to execute a VI before the build. If the pre-build VI returns an error before a build, the build does not continue, and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePreVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate pre-build | Creates a VI with the pre-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes before the build must match the connector pane of the pre-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |
| executePostVI | Includes a VI that executes after the build. Make sure the VI you want to include is under the target, such as My Computer, in the project. When you place a checkmark in the checkbox, the Select Project File dialog box appears.Select a VI from this dialog box with a connector pane that matches the post-build template VI. If you do not have a VI previously generated from the post-build template, use the Generate VI button to execute a VI after the build. If LabVIEW returns an error during the build, the post-build VI still runs. If the post-build VI returns an error during the build, the build fails and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePostVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate post-build | Creates a VI with the post-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes after the build must match the connector pane of the post-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/pre-post-build-actions-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00023: Pre/Post Build Actions Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/pre-post-build-actions-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/pre-post-build-actions-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to specify VIs for LabVIEW to execute before or after the build. Option Description executePreVI Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in th

### Pre/Post Build Actions Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to [specify VIs for LabVIEW to execute](/csh?productcategories=147794&context=lvcore_lvconcepts_running_vis_before_after) before or after the build.

| Option | Description |
| --- | --- |
| executePreVI | Includes a VI that executes before the build. Make sure the VI you want to include is under the target, such as My Computer, in the LabVIEW project.When you place a checkmark in this checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the pre-build template VI. If you do not have a VI previously generated from the pre-build template, use the Generate VI button to execute a VI before the build. If the pre-build VI returns an error before a build, the build does not continue, and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePreVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate pre-build | Creates a VI with the pre-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes before the build must match the connector pane of the pre-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |
| executePostVI | Includes a VI that executes after the build. Make sure the VI you want to include is under the target, such as My Computer, in the project. When you place a checkmark in the checkbox, the Select Project File dialog box appears. Select a VI from this dialog box with a connector pane that matches the post-build template VI. If you do not have a VI previously generated from the post-build template, use the Generate VI button to execute a VI after the build. If LabVIEW returns an error during the build, the post-build VI still runs. If the post-build VI returns an error during the build, the build fails and the Build Status dialog box appears. VI in project—Displays the name of the build VI after you select it from the Select Project File dialog box or generate a VI with the Generate VI button. BrowsePostVI—Displays the Select Project File dialog box, in which you can select a VI in the project. |
| Generate post-build | Creates a VI with the post-build template VI and adds the VI to the VI in project text box. The connector pane of the VI that executes after the build must match the connector pane of the post-build template VI. If you do not have a VI with a connector pane that matches, click the Generate VI button.If you click the Generate VI button to generate a VI, LabVIEW adds the VI to the project. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/preview-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00024: Preview Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/preview-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/preview-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to see a preview of the files generated for a stand-alone real-time application. Save changes to VIs currently in memory to ensure that the preview is accurate. This page includes the following components: Option Description GeneratePr

### Preview Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to see a preview of the files generated for a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

Note

This page includes the following components:

| Option | Description |
| --- | --- |
| GeneratePreview | Creates a preview of the build that displays in Generated Files. |
| Generated Files | Displays a preview of the directory structure and filenames in the build.Use this preview to determine if you need to change file destinations or other settings. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/preview-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00025: Preview Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/preview-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/preview-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to see a preview of the packed project library build. This page includes the following components: Option Description GeneratePreview Creates a preview of the build that displays in Generated Files. Generated files Displays a previe

### Preview Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to see a preview of the packed project library build.

This page includes the following components:

| Option | Description |
| --- | --- |
| GeneratePreview | Creates a preview of the build that displays in Generated Files. |
| Generated files | Displays a preview of the directory structure and filenames in the build.Use this preview to determine if you need to change file destinations or other settings. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/preview-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00026: Preview Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/preview-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/preview-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to see a preview of the shared library build. This page includes the following components: Option Description GeneratePreview Creates a preview of the build that displays in Generated Files. Generated files Displays a preview of the

### Preview Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to see a preview of the [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications) build.

This page includes the following components:

| Option | Description |
| --- | --- |
| GeneratePreview | Creates a preview of the build that displays in Generated Files. |
| Generated files | Displays a preview of the directory structure and filenames in the build.Use this preview to determine if you need to change file destinations or other settings. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/preview-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00027: Preview Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/preview-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/preview-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to see a preview of the source distribution build. This page includes the following options: Option Description GeneratePreview Creates a preview of the build that displays in Generated Files. Generated files Displays a preview

### Preview Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to see a preview of the [source distribution](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications) build.

This page includes the following options:

| Option | Description |
| --- | --- |
| GeneratePreview | Creates a preview of the build that displays in Generated Files. |
| Generated files | Displays a preview of the directory structure and filenames in the build.Use this preview to determine if you need to change file destinations or other settings. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00028: Real-Time Application Properties Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click Build Specifications under an RT target and select New»Real-Time Application from the shortcut menu to display this dialog box. You also can right-click a build specification under Build Specifications and select Properties from the shortcut menu. Use this

### Real-Time Application Properties Dialog Box

In the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** under an RT target and select **New»Real-Time Application** from the shortcut menu to display this dialog box. You also can right-click a build specification under **Build Specifications** and select **Properties** from the shortcut menu.

Use this dialog box to create and configure settings for a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

The **Real-Time Application Properties** dialog box contains the following pages, which you use to configure the settings for a stand-alone real-time application:

- Information
- Source Files
- Destinations
- Source File Settings
- Advanced
- Additional Exclusions
- Version Information
- Web Services page
- Pre/Post Build Actions
- Component Definition
- Preview

The bottom of the **Real-Time Application Properties** dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the current build specification settings, closes the dialog box, and builds with the current settings. If you rebuild a given specification, LabVIEW overwrites the existing files from the previous build that are part of the current build. However, if you enable the Auto increment checkbox, or Auto increment product version checkbox for installers, on the Version Information page, and you use the [VersionNumber] or [ProductVersion] tags in the appropriate build destination fields, LabVIEW creates a new directory that includes the version number instead of overwriting the previous build on disk.Clicking Build does not save the settings to disk. You must save the project in order to save the build specification settings. |
| OK | Updates the project with the current build specification settings and closes the dialog box without performing a build.Clicking OK does not save the settings to disk. You must save the project in order to save the build specification settings. |
| Cancel | Cancels the build specification settings you changed and closes the dialog box. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00029: Real-Time Packed Library Properties Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Packed Library from the shortcut menu to display this dialog box. You also can right-click a packed project library specification name under Build Specifications and select Properties from the shortcut menu, or double-

### Real-Time Packed Library Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Packed Library** from the shortcut menu to display this dialog box. You also can right-click a packed project library specification name under **Build Specifications** and select **Properties** from the shortcut menu, or double-click the packed library specification name to display this dialog box.

Note

Build Specifications

Project Explorer

display the item

Use this dialog box to access and configure settings for a packed library.

The **Packed Library Properties** dialog box includes the following pages, which you use to configure the settings for the build:

- Information
- Source Files
- Destinations
- Source File Settings
- Advanced
- Additional Exclusions
- Connector Pane State
- Version Information
- Pre/Post Build Actions
- Preview

The bottom of the **Packed Library Properties** dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the current build specification settings, closes the dialog box, and builds with the current settings. If you rebuild a given specification, LabVIEW overwrites the existing files from the previous build that are part of the current build. However, if you enable the Auto increment checkbox, or Auto increment product version checkbox for installers, on the Version Information page, and you use the [VersionNumber] or [ProductVersion] tags in the appropriate build destination fields, LabVIEW creates a new directory that includes the version number instead of overwriting the previous build on disk.Clicking Build does not save the settings to disk. You must save the project in order to save the build specification settings. |
| OK | Updates the project with the current build specification settings and closes the dialog box without performing a build.Clicking OK does not save the settings to disk. You must save the project in order to save the build specification settings. |
| Cancel | Cancels the build specification settings you changed and closes the dialog box. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00030: Real-Time Shared Library Properties Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Shared Library from the shortcut menu to display this dialog box. You also can right-click a shared library specification name under Build Specifications and select Properties from the shortcut menu, or you can double-

### Real-Time Shared Library Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Shared Library** from the shortcut menu to display this dialog box. You also can right-click a shared library specification name under **Build Specifications** and select **Properties** from the shortcut menu, or you can double-click the shared library specification name.

Note

Build Specifications

Project Explorer

display the item

Use this dialog box to access and configure settings for a [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications).

The **Shared Library Properties** dialog box includes the following pages, which you use to configure the settings for the build:

- Information
- Source Files
- Destinations
- Source File Settings
- Advanced
- Additional Exclusions
- Version Information
- Run-Time Languages
- Pre/Post Build Actions
- Preview

The bottom of the **Shared Library Properties** dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the current build specification settings, closes the dialog box, and builds with the current settings. If you rebuild a given specification, LabVIEW overwrites the existing files from the previous build that are part of the current build. However, if you enable the Auto increment checkbox, or Auto increment product version checkbox for installers, on the Version Information page, and you use the [VersionNumber] or [ProductVersion] tags in the appropriate build destination fields, LabVIEW creates a new directory that includes the version number instead of overwriting the previous build on disk.Clicking Build does not save the settings to disk. You must save the project in order to save the build specification settings. |
| OK | Updates the project with the current build specification settings and closes the dialog box without performing a build.Clicking OK does not save the settings to disk. You must save the project in order to save the build specification settings. |
| Cancel | Cancels the build specification settings you changed and closes the dialog box. |

[*Building and Distributing Applications* Hom](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00031: Real-Time Source Distribution Properties Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: From the Project Explorer window, right-click Build Specifications and select New»Source Distribution from the shortcut menu to display this dialog box. You also can right-click a source distribution specification name under Build Specifications and select Properties from the shortcut menu, or you c

### Real-Time Source Distribution Properties Dialog Box

From the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window, right-click **Build Specifications** and select **New»Source Distribution** from the shortcut menu to display this dialog box. You also can right-click a source distribution specification name under **Build Specifications** and select **Properties** from the shortcut menu, or you can double-click the source distribution specification name.

Note

Build Specifications

Project Explorer

display the item

Use this dialog box to access and configure settings for a [source distribution](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications).

The **Source Distribution Properties** dialog box includes the following pages, which you use to configure the setting for the build:

- Information
- Source Files
- Destinations
- Source File Settings
- Advanced
- Additional Exclusions
- Version Information
- Pre/Post Build Actions
- Preview

The bottom of the **Source Distribution Properties** dialog box includes the following buttons:

| Option | Description |
| --- | --- |
| Build | Updates the LabVIEW project with the current build specification settings, closes the dialog box, and builds with the current settings. If you rebuild a given specification, LabVIEW overwrites the existing files from the previous build that are part of the current build. However, if you enable the Auto increment checkbox, or Auto increment product version checkbox for installers, on the Version Information page, and you use the [VersionNumber] or [ProductVersion] tags in the appropriate build destination fields, LabVIEW creates a new directory that includes the version number instead of overwriting the previous build on disk.Clicking Build does not save the settings to disk. You must save the project in order to save the build specification settings. |
| OK | Updates the project with the current build specification settings and closes the dialog box without performing a build.Clicking OK does not save the settings to disk. You must save the project in order to save the build specification settings. |
| Cancel | Cancels the build specification settings you changed and closes the dialog box. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/rt-target-errors-dialog-box.html language=enus -->
## TOPIC 00032: RT Target Errors Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/rt-target-errors-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/rt-target-errors-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Right-click an RT target in the Project Explorer window and select Utilities»View Error Log from the shortcut menu to display this dialog box. Use the RT Target Errors dialog box to view error logs and generate error reports for sessions of an RT target. The RT Target Errors dialog box displays LabV

### RT Target Errors Dialog Box

Right-click an RT target in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) window and select **Utilities»View Error Log** from the shortcut menu to display this dialog box.

Use the **RT Target Errors** dialog box to view error logs and generate error reports for sessions of an RT target. The **RT Target Errors** dialog box displays LabVIEW errors, real-time operating system errors, and kernel logs for an RT target.

This dialog box includes the following components:

| Option | Description |
| --- | --- |
| LabVIEW RT sessions | Displays a list of sessions for the RT target. A session begins when you power on the RT target and ends when you reboot the target. |
| LabVIEW error log | Displays the LabVIEW error codes for errors that occurred on the RT target during the selected session. |
| RT System error log | Displays the system and Real-Time Module driver errors reported by the RT target during the selected session. |
| Kernel log | Displays information saved from an RT target prior to a system crash. Kernel log returns information such as stack crawls, a list of the DLLs in memory, register values, and the code number of the crash for the selected session.National Instruments can use this information to troubleshoot an RT target. |
| Delete Session | Deletes the error logs for the selected sessions and removes the sessions from the LabVIEW RT sessions listbox. |
| Create Report | Saves error logs and RT target information for the selected sessions to a text file. |
| Done | Closes this dialog box. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/rt-target-properties-dialog-box.html language=enus -->
## TOPIC 00033: RT Target Properties Dialog Box

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/rt-target-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/rt-target-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Project Explorer window, right-click an RT target and select Properties from the shortcut menu to display this dialog box. Use the Category list at the left side of the dialog box to access the following pages: General—Sets the IP address for the RT target. OS and CPU Configuration—Applies on

### RT Target Properties Dialog Box

In the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvconcepts_using_labview_projects) window, right-click an RT target and select **Properties** from the shortcut menu to display this dialog box.

Use the **Category** list at the left side of the dialog box to access the following pages:

- General —Sets the IP address for the RT target.
- OS and CPU Configuration —Applies only to the generic RT target. If you plan to build an executable file based on a shipping example without connecting to an RT target, use this page to specify the OS and CPU of the RT target that will run the executable file.
- Conditional Disable Symbols —Defines symbols to use with the Conditional Disable structure in any VI under the RT target.
- VI Server —Configures the VI Server for the RT target.
- Web Server —Configures the Web Server for the RT target.
- User Access —Controls access to VIs and properties for the RT target.
- Host Environment —Enables and controls the polling of the connection with an RT target to check for status.
- Miscellaneous —Sets miscellaneous options for the RT target.
- Scan Engine —Configures settings for the NI Scan Engine running on the RT target.

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/run-time-languages-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00034: Run-Time Languages Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/run-time-languages-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/run-time-languages-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to set the language preferences for a shared library. You can select from all languages that LabVIEW supports. The language preferences apply to aspects of the shared library that the LabVIEW Run-Time Engine affects, such as dialog

### Run-Time Languages Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to set the language preferences for a [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications). You can select from all languages that LabVIEW supports.

The language preferences apply to aspects of the shared library that the [LabVIEW Run-Time Engine](/csh?productcategories=147794&context=lvcore_lvconcepts_using_the_lv_run_time_eng) affects, such as dialog boxes and menus. These items appear in the default language you select. Users can [configure language settings](/csh?productcategories=147794&context=lvcore_lvhowto_setting_rt_lang_prefs) to change the default language to any of the supported languages you select.

Note

This page includes the following components:

| Option | Description |
| --- | --- |
| Support all languages | Enables support for all languages that LabVIEW supports in the build. Remove the checkmark from the checkbox if you want to specify the supported languages. |
| Supported languages | Specifies the languages that the build supports if you remove the checkmark from the Support all languages checkbox. |
| Default language | Specifies the default language that the build supports if you remove the checkmark from the Support all languages checkbox. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-file-settings-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00035: Source File Settings Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-file-settings-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-file-settings-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to edit settings and destination directories for the files and folders included in a stand-alone real-time application. This page includes the following components: Option Description Project Files Displays the tree view of items under

### Source File Settings Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to edit settings and destination directories for the files and folders included in a [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Project Files | Displays the tree view of items under the RT target of the Project Explorer window. |
| Inclusion Type | Appears if you select a VI in the Project Files tree. Specifies whether you want to include the VI as a startup VI, a dynamic VI you can call through the VI Server, or a file included in the real-time stand-alone application only if referenced. |
| Set destination for all contained items | Appears if you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to include all the items in the folder in the real-time stand-alone application or to set the destination directory on the RT target for all the items in the folder.The destination directory options in the Destination pull-down menu correspond to the directories in the Destinations listbox on the Destinations page of the Real-Time Application Properties dialog box. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. |
| Destination | Appears if you select a VI in the Project Files tree. Specifies if you want to include the VI in the stand-alone real-time application or if you want to set a destination directory for the VI on the RT target.The destination directory options in the Destination pull-down menu correspond to the directories in the Destinations listbox on the Destinations page of the Real-Time Application Properties dialog box. |
| Set VI Properties | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the VI properties for the items in the selected folder.When you place a checkmark in the checkbox,LabVIEW enables the Customize VI Properties button. |
| Customize VI Properties | Displays the VI Properties dialog box. Use the dialog box to specify the properties for the selected VI. By default, LabVIEW uses the property settings configured in the VI. Any settings you configure in the VI Properties dialog box override any settings you configured in the Customize Window Appearance dialog box.LabVIEW dims this option for items other than VIs. |
| Set save settings | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the save settings for the items in the selected folder. |
| Use default save settings | Saves the VIs using default save settings. The default save setting for the VIs you add to the Startup VIs and Always Included listboxes on the Source Files page is to remove the block diagram. The default for all other VIs is to remove the block diagram and the front panel. Remove the checkmark from this checkbox to change the default settings for each item you select in the Project Files tree. Remove panel—Removes the front panel from a VI in the build. Removing the front panel reduces the size of the application or shared library. If you select yes, LabVIEW removes the front panel, but Property Nodes or Invoke Nodes that refer to the front panel might return errors that affect the behavior of the source distribution. LabVIEW enables this option if you remove the checkmark from the Use default save settings checkbox. Note NoteIf you execute the Run VI method after placing a checkmark in the Remove front panel checkbox, the Run VI method will return error 1013. Remove diagram—Removes the block diagram from a VI in the build. LabVIEW enables this option if you remove the checkmark from the Remove front panel checkbox. If you remove the front panel, you also remove the block diagram. As a result, if you place a checkmark in the Remove front panel checkbox, a checkmark automatically appears in the Remove block diagram checkbox. |
| Set password | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to configure the password for the items in the selected folder. |
| No password change | Specifies for LabVIEW to not prompt for a password if you use the VI in a build. LabVIEW also does not modify or apply a password you previously applied to the VI.This option is available only if you select the Changed VIs,Development Distribution, or Custom Save options. |
| Remove password | Removes the password you previously applied to a VI or library. Prior to removing the password, LabVIEW prompts you to enter the current password during the build.Note If you programmatically build a source distribution which includes a password protected VI, LabVIEW builds the source distribution without prompting for the VI password. |
| Apply new password | Applies the password you supply in the text box to a VI or library. Prior to applying the new password, LabVIEW prompts you to enter the current password during the build. Enter the password in the text box below the Apply new password option.You also can apply a password to a VI without saving it. This option is not available if you select the Save for Previous or Template option. |
| Rename in build | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox to enter a prefix in the text box and rename all items in the folder by applying the prefix to the existing names. |
| Rename in build | Renames a file that you select in the Project Files list. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-file-settings-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00036: Source File Settings Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-file-settings-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-file-settings-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to edit destinations and properties for the files and folders included in a packed project library. LabVIEW enables the options on this page only if the item you select in the Project Files tree supports the option. You can apply se

### Source File Settings Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to edit destinations and properties for the files and folders included in a packed project library. LabVIEW enables the options on this page only if the item you select in the **Project Files** tree supports the option. You can apply settings to all the files under **Dependencies** but not to individual files under **Dependencies**. If you want to apply settings to individual files, add them to the LabVIEW project.

This page includes the following components:

Note

Project Files

- Set destination for all contained items
- Set VI properties for all contained items
- Set save settings for all contained items
- Set password for all contained items
- Apply prefix to all contained items

| Option | Description |
| --- | --- |
| SourceTree | Displays the tree view of items under the target, such as My Computer, in the Project Explorer window. |
| Inclusion Type | Displays how LabVIEW includes the item in the build. This option corresponds to the inclusion type you selected on the Source Files page. For example, a VI in the Always Included listbox on the Source Files page appears as Always Included. To change the value, return to the Source Files page and remove the item from the Always Included listbox. Note LabVIEW includes dependencies of the top-level library in the packed library, but they do not export with the build and are not visible in the packed library. Always Included—Includes the item in the build. If the VI you select in the Project Files list is a private or community VI, the VI is Always Included. The .lvlib file you select as the Top-level Library on the Source Files page is Always Included. Exported VI—Includes the item in the build. If the VI you select in the Project Files list is a public VI, the VI is an Exported VI. Include if referenced—Includes the item in the build if another item references it. |
| Set Destination | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the destination directory for the items in the selected folder. Note LabVIEW places an item set to Same as caller in the directory of the caller. If you set an item to Same as caller and two different callers are in different directories, LabVIEW places the item in the same directory as the build. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. |
| Destination | Sets the destination for the selected item.The names in the Destination pull-down menu correspond to the options in the Destination label text box on the Destinations page. The default destination is Same as caller and LabVIEW places the item in the same destination as the caller. You cannot set the destination for the exported VIs or the .lvlib file you select as the Top-level Library on the Source Files page. |
| Set VI Properties | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the VI properties for the items in the selected folder.When you place a checkmark in the checkbox,LabVIEW enables the Customize VI Properties button. |
| Customize VI Properties | Displays the VI Properties dialog box. Use the dialog box to specify the properties for the selected VI. By default, LabVIEW uses the property settings configured in the VI. Any settings you configure in the VI Properties dialog box override any settings you configured in the Customize Window Appearance dialog box.LabVIEW dims this option for items other than VIs. |
| Set save settings | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the save settings for the items in the selected folder. |
| Use default save settings | Saves the VIs using default save settings. The default save setting for the VIs you add to project in the Top-level Library and VIs you add to the Always Included listbox on the Source Files page is to remove the block diagram. The default for all other VIs is to remove the block diagram and the front panel. Remove the checkmark from this checkbox to change the default settings for each item you select in the Project Files tree. Remove panel—Removes the front panel from a VI in the build. Removing the front panel reduces the size of the application or shared library. If you select yes, LabVIEW removes the front panel, but Property Nodes or Invoke Nodes that refer to the front panel might return errors that affect the behavior of the source distribution. LabVIEW enables this option if you remove the checkmark from the Use default save settings checkbox. Note NoteIf you execute the Run VI method after placing a checkmark in the Remove front panel checkbox, the Run VI method will return error 1013. Remove diagram—Removes the block diagram from a VI in the build. LabVIEW enables this option if you remove the checkmark from the Remove front panel checkbox. If you remove the front panel, you also remove the block diagram. As a result, if you place a checkmark in the Remove front panel checkbox, a checkmark automatically appears in the Remove block diagram checkbox. |
| Set password | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to configure the password for the items in the selected folder. |
| No password change | Specifies for LabVIEW to not prompt for a password if you use the VI in a build.LabVIEW also does not modify or apply a password you previously applied to the VI. |
| Remove password | Removes the password you previously applied to a VI or library. Prior to removing the password, LabVIEW prompts you to enter the current password during the build.Note If you programmatically build a source distribution which includes a password protected VI, LabVIEW builds the source distribution without prompting for the VI password. |
| Apply new password | Applies the password you supply in the text box to a VI or library.Prior to applying the new password, LabVIEW prompts you to enter the current password during the build. Enter the password in the text box below the Apply new password option. |
| Rename in build | Appears when you select a file in the Project Files list. Renames the selected file. Enter the new name of the file in the text box.Note You cannot rename the .lvlib file you select as the Top-level Library on the Source Files page. |
| Rename in build | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox to enter a prefix in the text box and rename all items in the folder by applying the prefix to the existing names. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-file-settings-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00037: Source File Settings Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-file-settings-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-file-settings-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to edit destinations and properties for the files included in a shared library. LabVIEW enables the options in this page only if the item you select in the Project Explorer tree supports the option. You can apply settings to all the

### Source File Settings Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to edit destinations and properties for the files included in a [shared library](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications). LabVIEW enables the options in this page only if the item you select in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) tree supports the option. You can apply settings to all the items under **Dependencies**, but not to individual items.

Note

.lvlib

Destination

.lvlib

This page includes the following components, depending on whether you select **Dependencies** or a folder:

#### Components that Display When You Select a Folder or Dependencies

- Set destination for all contained items
  - Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies.
- Set VI properties for all contained items
- Set save settings for all contained items
- Set password for all contained items
- Apply prefix to all contained items

#### Components that Always Display

| Option | Description |
| --- | --- |
| SourceTree | Displays the tree view of items under the target, such as My Computer, in the Project Explorer window. |
| Inclusion Type | Displays how LabVIEW includes the item in the build. This option corresponds to the inclusion type you selected in the Source Files page. For example, a VI in the Always Included list appear as Always Included. If you select a folder, the inclusion type corresponds to the inclusion type of the items inside the folder. Service VI—Includes the item in the build as a service VI. Always Included—Includes the item in the build. Include if referenced—Includes the item in the build if another item references it. |
| Destination | Sets the destination for the selected item. LabVIEW enables this option if you have not designated the item as a startup VI.The names in the Destination pull-down menu correspond to the options in the Destination label text box on the Destinations page. The default destination is Same as caller and LabVIEW places the item in the same destination as the caller. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. Make top level in LLB—Appears when you select a destination that is an LLB. Place a checkmark in the Make top level in LLB checkbox if you want the selected VI to be the top level item in the LLB. |
| Customize VI Properties | Displays the VI Properties dialog box. Use the dialog box to specify the properties for the selected VI. By default, LabVIEW uses the property settings configured in the VI. Any settings you configure in the VI Properties dialog box override any settings you configured in the Customize Window Appearance dialog box.LabVIEW dims this option for items other than VIs. |
| Use default save settings | Saves the VIs using default save settings. The default save setting for the VIs you add to the Exported VIs and Always Included listboxes on the Source Files page is to remove the block diagram. The default for all other VIs is to remove the block diagram and the front panel. Remove the checkmark from this checkbox to change the default settings for each item you select in the Project Files tree. Remove panel—Removes the front panel from a VI in the build. Removing the front panel reduces the size of the application or shared library. If you select yes, LabVIEW removes the front panel, but Property Nodes or Invoke Nodes that refer to the front panel might return errors that affect the behavior of the source distribution. LabVIEW enables this option if you remove the checkmark from the Use default save settings checkbox. Note If you execute the Run VI method after placing a checkmark in the Remove front panel checkbox, the Run VI method will return error 1013. Remove diagram—Removes the block diagram from a VI in the build. LabVIEW enables this option if you remove the checkmark from the Remove front panel checkbox. If you remove the front panel, you also remove the block diagram. As a result, if you place a checkmark in the Remove front panel checkbox, a checkmark automatically appears in the Remove block diagram checkbox. |
| No password change | Specifies for LabVIEW to not prompt for a password if you use the VI in a build.LabVIEW also does not modify or apply a password you previously applied to the VI. |
| Remove password | Removes the password you previously applied to a VI or library. Prior to removing the password, LabVIEW prompts you to enter the current password during the build.Note If you programmatically build a source distribution which includes a password protected VI, LabVIEW builds the source distribution without prompting for the VI password. |
| Apply new password | Applies the password you supply in the text box to a VI or library.Prior to applying the new password, LabVIEW prompts you to enter the current password during the build. Enter the password in the text box below the Apply new password option. |
| Rename in build | Renames a file that you select in the Project Files list. |
| Set Destination | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the destination directory for the items in the selected folder. Note LabVIEW places an item set to Same as caller in the directory of the caller. If you set an item to Same as caller and two different callers are in different directories, LabVIEW places the item in the same directory as the build. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. |
| Set VI Properties | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the VI properties for the items in the selected folder.When you place a checkmark in the checkbox,LabVIEW enables the Customize VI Properties button. |
| Set save settings | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the save settings for the items in the selected folder. |
| Set password | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to configure the password for the items in the selected folder. |
| Rename in build | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox to enter a prefix in the text box and rename all items in the folder by applying the prefix to the existing names. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-file-settings-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00038: Source File Settings Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-file-settings-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-file-settings-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to edit destinations and properties for the files included in a source distribution. LabVIEW enables the options on this page only if the item you select in the Project Explorer tree supports the option. You can apply settings

### Source File Settings Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to edit destinations and properties for the files included in a [source distribution](/csh?productcategories=147794&context=lvcore_lvhowto_develop_distribute_applications). LabVIEW enables the options on this page only if the item you select in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvdialog_project_explorer_window) tree supports the option. You can apply settings to all the items under **Dependencies**, but not to individual items under **Dependencies**.

Note

.lvlib

Destination

.lvlib

This page includes the following components:

Note

Project Files

Inclusion Type

- Set destination for all contained items
- Set VI properties for all contained items
- Set save settings for all contained items
- Set password for all contained items
- Apply prefix to all contained items

Inclusion Type

| Option | Description |
| --- | --- |
| SourceTree | Displays the tree view of items in the Project Explorer window. |
| Inclusion Type | Displays how LabVIEW includes the item in the build. This option corresponds to the inclusion type you selected in the Source Files page. For example, a VI in the Always Included list appear as Always Included. If you select a folder, the inclusion type corresponds to the inclusion type of the items inside the folder. Always Included—Includes the item in the build. Always Excluded—Excludes the item from the build. Include if referenced—Includes the item in the build if the another item references it. |
| Destination | Sets the destination for the selected item. LabVIEW enables this option if you have not designated the item as a startup VI.The names in the Destination pull-down menu correspond to the options in the Destination label text box on the Destinations page. The default destination is Same as caller and LabVIEW places the item in the same destination as the caller. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. Make top level in LLB—Appears when you select a destination that is an LLB. Place a checkmark in the Make top level in LLB checkbox if you want the selected VI to be the top level item in the LLB. |
| Customize VI Properties | Displays the VI Properties dialog box. Use the dialog box to specify the properties for the selected VI. By default, LabVIEW uses the property settings configured in the VI. Any settings you configure in the VI Properties dialog box override any settings you configured in the Customize Window Appearance dialog box.LabVIEW dims this option for items other than VIs. |
| Use default save settings | Saves the VIs using default save settings. The default save setting for VIs in a source distribution is to retain the front panel and the block diagram. Remove the checkmark from the Use default save settings checkbox to change the default settings. Note LabVIEW dims this option for items other than VIs. LabVIEW also dims this option if you place a checkmark in the Remove compiled code checkbox on the Additional Exclusions page because you cannot remove the front panel or block diagram from a VI with separate compiled code. Remove panel—Removes the front panel of the selected VI from the target. Removing the front panel reduces the size of the application or shared library. If you select yes, LabVIEW removes the front panel, but Property Nodes or Invoke Nodes that refer to the front panel might return errors that affect the behavior of the source distribution. Note If you execute the Run VI method after placing a checkmark in the Remove front panel checkbox, the Run VI method will return error 1013. Remove diagram—Removes the block diagram from a VI in the build. LabVIEW enables this option if you remove the checkmark from the Remove front panel checkbox. If you remove the front panel, you also remove the block diagram. As a result, if you place a checkmark in the Remove front panel checkbox, a checkmark automatically appears in the Remove block diagram checkbox. |
| No password change | Specifies for LabVIEW to not prompt for a password if you use the VI in a build.LabVIEW also does not modify or apply a password you previously applied to the VI. |
| Remove password | Removes the password you previously applied to a VI or library. Prior to removing the password, LabVIEW prompts you to enter the current password during the build.Note If you programmatically build a source distribution which includes a password protected VI, LabVIEW builds the source distribution without prompting for the VI password. |
| Apply new password | Applies the password you supply in the text box to a VI or library.Prior to applying the new password, LabVIEW prompts you to enter the current password during the build. Enter the password in the text box below the Apply new password option. |
| Rename in build | Renames a file that you select in the Project Files list. |
| Set Destination | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the destination directory for the items in the selected folder. Note LabVIEW places an item set to Same as caller in the directory of the caller. If you set an item to Same as caller and two different callers are in different directories, LabVIEW places the item in the same directory as the build. Set destination for packed project libraries and shared libraries—Appears only when you select Dependencies. |
| Set VI Properties | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the VI properties for the items in the selected folder.When you place a checkmark in the checkbox,LabVIEW enables the Customize VI Properties button. |
| Set save settings | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to set the save settings for the items in the selected folder. |
| Set password | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox if you want to configure the password for the items in the selected folder. |
| Rename in build | Appears when you select a folder in the Project Files tree. Place a checkmark in the checkbox to enter a prefix in the text box and rename all items in the folder by applying the prefix to the existing names. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-files-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00039: Source Files Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-files-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-files-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to specify the startup VIs, dynamic VIs, and support files that you want to include in the stand-alone real-time application. This page includes the following components: Option Description Project Files Displays a list of items added

### Source Files Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to specify the startup VIs, dynamic VIs, and support files that you want to include in the [stand-alone real-time application](/csh?context=lvrt_lvrtconcepts_building_rtapplications).

This page includes the following components:

| Option | Description |
| --- | --- |
| Project Files | Displays a list of items added under the RT target of the Project Explorer window. |
| Startup VIs | Specifies the startup VIs, which are top-level VIs, to use in the stand-alone real-time application.You must define at least one VI as a startup VI. Click the arrow buttons next to the Startup VIs listbox to add or remove the VIs you select, including their dependencies. |
| Always Included | Specifies the dynamic VIs and support files always to include in the application, even if the startup VIs do not contain references to the files.Click the arrow buttons next to the Always Included listbox to add selected files from the Project Files listbox or to remove selected files from the Always Included listbox. When you add a folder to the listbox, you add all items in the folder and cannot remove individual items. Dynamic VIs are VIs that LabVIEW dynamically calls through the VI Server. Support files are non-VI files, such as drivers, text files, and help files that the application uses. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-files-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00040: Source Files Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-files-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-files-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to add and remove files and folders from the packed project library and to specify files to include in the build. This page includes the following components: Option Description SourceTree Displays a list of items under My Computer

### Source Files Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to add and remove files and folders from the packed project library and to specify files to include in the build.

This page includes the following components:

| Option | Description |
| --- | --- |
| SourceTree | Displays a list of items under My Computer in the Project Explorer window.Select files from Project Files and click the arrow buttons next to the Top-level Library and Always Included listboxes to add or remove files from the listboxes. |
| TopTree | Specifies the top-level project library of the packed library. You must define one project library as a top-level library.Click the arrow button next to the Top-level Library listbox to add a selected project library from the Project Files listbox. The packed library also includes the dependencies of the project library. |
| BottomTree | Specifies the dynamic VIs and support files to always include in the packed library.Click the arrow buttons next to the Always Included listbox to add or remove selected files from the Always Included listbox. When you add a folder to the listbox, you add all items in the folder and cannot remove individual items. You cannot move private data controls to the Always Included listbox. Note Dynamic VIs are VIs that LabVIEW dynamically calls through the VI Server. Support files are non-VI files, such as drivers, text files, help files, and .NET assemblies that the packed library uses. LabVIEW includes non-LabVIEW support files in a folder outside the library when you build the packed library. If you add a packed library to the Always Included listbox, LabVIEW also includes the packed library in the folder outside the library when you build. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-files-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00041: Source Files Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-files-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-files-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to add and remove files to build into the shared library. This page includes the following components: Option Description SourceTree Displays the tree view of items under My Computer in the Project Explorer window.Click the arrow bu

### Source Files Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to add and remove files to build into the shared library.

This page includes the following components:

| Option | Description |
| --- | --- |
| SourceTree | Displays the tree view of items under My Computer in the Project Explorer window.Click the arrow buttons next to the Exported VIs and Always Included listboxes to add selected files from Project Files to those lists or to remove selected files from the listboxes. |
| TopTree | Specifies the exported VIs, which users can access as functions of the shared library. You must include at least one exported VI.Click the arrow buttons next to the Exported VIs listbox to add selected VIs from the Project Files listbox or to remove selected VIs from the Exported VIs listbox. If you add one file, the Define VI Prototype dialog box appears. If you add more than one file at a time, the Define VI Prototype dialog box does not appear and LabVIEW uses the default prototype. |
| Configure VIs | Displays when you select an exported VI. Click the button to display the Define VI Prototype dialog box, which you can use to define the parameters of an exported VI. |
| BottomTree | Specifies the dynamic VIs and support files always to include in the shared library.Click the arrow buttons next to the Always Included listbox to add selected files from the Project Files listbox or to remove selected files from the Always Included listbox. When you add a folder to the listbox, you add all items in the folder and cannot remove individual items. Dynamic VIs are VIs that LabVIEW dynamically calls through the VI Server. Support files are non-VI files, such as drivers, text files, help files, and .NET assemblies that the shared library uses. |

You cannot move the following files to the **Exported VIs** or **Always Included** listbox:

**Exported VIs**

- Polymorphic VIs
- Controls
- Private data controls
- Files that are not VIs, such as text, image, or .mnu files
- Library files, such as LabVIEW classes, or XControls
- Global variables

**Always Included**

- Private data controls

If you move a library or LabVIEW class to the **Always Included** listbox, LabVIEW labels all items in the library or class referenced. You can still designate any of the individual items as exported VIs. However, if you move any part of an XControl to the **Always Included** listbox, LabVIEW dims the related XControl files and includes the related files in the build. You cannot designate any of the related items as startup VIs.

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/source-files-page-real-time-source-distribution-properties-dialog-box.html language=enus -->
## TOPIC 00042: Source Files Page (Real-Time Source Distribution Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/source-files-page-real-time-source-distribution-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/source-files-page-real-time-source-distribution-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to add and remove files to build into the source distribution. This page includes the following components: Option Description SourceTree Displays the tree view of items under My Computer in the Project Explorer window.Click th

### Source Files Page (Real-Time Source Distribution Properties Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to add and remove files to build into the source distribution.

This page includes the following components:

| Option | Description |
| --- | --- |
| SourceTree | Displays the tree view of items under My Computer in the Project Explorer window.Click the arrow buttons next to the Exported VIs and Always Included listboxes to add selected files from Project Files to those lists or to remove selected files from the listboxes. |
| TopTree | Specifies the items always to include in source distribution.Click the arrow buttons next to the Always Included listbox to add selected files from the Project Files listbox or to remove selected files from the Always Included listbox. When you add a folder to the listbox, you add all items in the folder and cannot remove individual items. |
| BottomTree | Specifies the VIs and files always to exclude from the source distribution. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/version-information-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00043: Version Information Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/version-information-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/version-information-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to enter the version information for the stand-alone application. This page includes the following components: Option Description Version Specifies the version number to associate with the build. Major—Specifies the component of the ve

### Version Information Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to enter the version information for the stand-alone application.

This page includes the following components:

| Option | Description |
| --- | --- |
| Version | Specifies the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Patch—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. Auto-increment version on build—Specifies whether LabVIEW automatically increments the Build after each build. Note NoteSave the project after you build to ensure that LabVIEW automatically increments correctly the next time you open the project. |
| Product name | Specifies the name that you want to display to users. |
| Legal copyright | (Windows) Specifies the copyright statement to include with the build. |
| Company name | (Windows) Specifies the name of the company you want to associate with the build. |
| Internal name | (Windows) Specifies a name to associate with the build for internal use. |
| Description | (Windows) Specifies information that you want to provide to users about the build. |

The information you add on this page appears in the following manner on different operating systems:

- (Windows) The Version tab when you right-click an application and select Properties from the shortcut menu
- (Mac OS X) The information window when you select an application and then select File»Get Info

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/version-information-page-real-time-packed-library-properties-dialog-box.html language=enus -->
## TOPIC 00044: Version Information Page (Real-Time Packed Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/version-information-page-real-time-packed-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/version-information-page-real-time-packed-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Packed Library Properties dialog box to enter the version information for the packed project library. This page includes the following components: Option Description Version Specifies the version number to associate with the build. Major—Specifies the component of the

### Version Information Page (Real-Time Packed Library Properties Dialog Box)

Use this page of the [Real-Time Packed Library Properties](real-time-packed-library-properties-dialog-box.html) dialog box to enter the version information for the packed project library.

This page includes the following components:

| Option | Description |
| --- | --- |
| Version | Specifies the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Patch—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. Auto-increment version on build—Specifies whether LabVIEW automatically increments the Build after each build. Note NoteSave the project after you build to ensure that LabVIEW automatically increments correctly the next time you open the project. |
| Product name | (Windows) Specifies the name that you want to display to users. |
| Legal copyright | (Windows) Specifies the copyright statement to include with the build. |
| Company name | (Windows) Specifies the name of the company you want to associate with the build. |
| Internal name | (Windows) Specifies a name to associate with the build for internal use. |
| Description | (Windows) Specifies information that you want to provide to users about the build. |

(Windows) After you build a packed library, the information you include on this page appears when you right-click the packed library, select **Properties** from the shortcut menu, and select the **Version** page of the **Properties** dialog box.

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/version-information-page-real-time-shared-library-properties-dialog-box.html language=enus -->
## TOPIC 00045: Version Information Page (Real-Time Shared Library Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/version-information-page-real-time-shared-library-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/version-information-page-real-time-shared-library-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Shared Library Properties dialog box to enter the version information for the shared library. This page includes the following components: Option Description Version Specifies the version number to associate with the build. Major—Specifies the component of the version

### Version Information Page (Real-Time Shared Library Properties Dialog Box)

Use this page of the [Real-Time Shared Library Properties](real-time-shared-library-properties-dialog-box.html) dialog box to enter the version information for the shared library.

This page includes the following components:

| Option | Description |
| --- | --- |
| Version | Specifies the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Patch—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. Auto-increment version on build—Specifies whether LabVIEW automatically increments the Build after each build. Note Save the project after you build to ensure that LabVIEW automatically increments correctly the next time you open the project. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/version-information-page-real-time-source-distribution-dialog-box.html language=enus -->
## TOPIC 00046: Version Information Page (Real-Time Source Distribution Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/version-information-page-real-time-source-distribution-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/version-information-page-real-time-source-distribution-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Source Distribution Properties dialog box to enter the version information for the stand-alone application. This page includes the following components: Option Description Version Specifies the version number to associate with the build. Major—Specifies the component o

### Version Information Page (Real-Time Source Distribution Dialog Box)

Use this page of the [Real-Time Source Distribution Properties](real-time-source-distribution-properties-dialog-box.html) dialog box to enter the version information for the stand-alone application.

This page includes the following components:

| Option | Description |
| --- | --- |
| Version | Specifies the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Patch—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. Auto-increment version on build—Specifies whether LabVIEW automatically increments the Build after each build. Note Save the project after you build to ensure that LabVIEW automatically increments correctly the next time you open the project. |

[*Building and Distributing Applications* Home](/csh?productcategories=147794&context=lvcore_lvconcepts_building_and_distributing_applications)

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/vi-states.html language=enus -->
## TOPIC 00047: VI States

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/vi-states.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/vi-states.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select a real-time target to display a target probe in the Auto View. You also can right-click the target and select Probe to display the probe in a separate window. Click the VI States tab of a real-time target probe to display this view. Use this view to start, stop, and monitor VIs on the real-ti

### VI States

Select a real-time target to display a target probe in the **Auto View**. You also can right-click the target and select **Probe** to display the probe in a separate window. Click the **VI States** tab of a real-time target probe to display this view. Use this view to start, stop, and monitor VIs on the real-time target.

This view includes the following components:

| Option | Description |
| --- | --- |
| Port | Specifies the TCP/IP port at which the VI server listens for requests on the real-time target.Right-click the real-time target in the Project Explorer window and select Properties from the shortcut menu to display the RT Target Properties dialog box. Select VI Server from the Category list to display the VI Server page, where you can configure the TCP/IP port for the VI Server. |
| Update Interval (seconds) | Sets the minimum time that the server waits between updates. The actual update interval might exceed the time you specify if higher priority tasks are running on the real-time target. |
| Show Top Level VIs Only | Filters all subVIs from the list of real-time target VIs. |
| Start Monitoring | Starts monitoring VIs on the real-time target. |
| Stop Monitoring | Stops monitoring VIs on the real-time target. |
| Start VI | Starts an idle VI that you select from the list of real-time target VIs. |
| Stop VI | Stops a VI that you select from the list of real-time target VIs. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=dialog-boxes/web-services-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00048: Web Services Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `dialog-boxes/web-services-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/dialog-boxes/web-services-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to configure web services that you want to include with a stand-alone application. Use Web services on the target computer to which you deploy the stand-alone application. Option Description Web services Lists the available Web service

### Web Services Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](real-time-application-properties-dialog-box.html) dialog box to configure web services that you want to include with a stand-alone application. Use Web services on the target computer to which you deploy the stand-alone application.

| Option | Description |
| --- | --- |
| Web services | Lists the available Web services for the target to which this build specification belongs. |
| Enable HTTP | Allows a client to use HTTP to call any web service that you include with this build specification.You must select this component to interact with the HTTP port control. |
| HTTP port | Specifies the port to use for unencrypted communication.You must configure each application that will run simultaneously to use a unique port. |
| Enable SSL | Select this component to allow a client to use HTTPS to call any included web service.You must select this component to interact with the following components on this page. SSL port—Indicates the TCP/IP port the Web Server uses for TLS/SSL-encrypted communication. You cannot enable TLS/SSL on the port specified by HTTP port. You must use a unique port for SSL port to allow encrypted communication. SSL certificate file—Allows you to browse for paths to certificate files (.cer) on the destination target. If you select a certificate from Discovered certificates, LabVIEW automatically populates this component. Query host for certificates—Contains the following components that allow you to view and select the certificates for a specific target: Discovered certificates—Lists the certificates for the target specified by the Server Address component after you perform a query.SSL certificate file displays the path to certificates you select from this list. Server Address—Specifies a target to query for SSL certificates.You can set the server address as the IP address of the target to which this build specification belongs. However, if you want to use an installer to deploy the application that includes these web services to another computer, change the default IP address to match that computer in order to make sure that LabVIEW can find the correct SSL certificates. Query—Runs a query of the address in Server address to discover SSL certificates.Refer to Discovered certificates to view the names of the certificates and SSL certificate file to view the paths. You must enable SSL on the system web server for the target to use this component. |
| SSL port | Indicates the TCP/IP port the Web Server uses for TLS/SSL-encrypted communication. You cannot enable TLS/SSL on the port specified by HTTP port. You must use a unique port for SSL port to allow encrypted communication. |
| Query host for certificates | Contains the following components that allow you to view and select the certificates for a specific target: Discovered certificates—Lists the certificates for the target specified by the Server Address component after you perform a query.SSL certificate file displays the path to certificates you select from this list. Server Address—Specifies a target to query for SSL certificates.You can set the server address as the IP address of the target to which this build specification belongs. However, if you want to use an installer to deploy the application that includes these web services to another computer, change the default IP address to match that computer in order to make sure that LabVIEW can find the correct SSL certificates. Query—Runs a query of the address in Server address to discover SSL certificates.Refer to Discovered certificates to view the names of the certificates and SSL certificate file to view the paths. You must enable SSL on the system web server for the target to use this component. |
| Query | Runs a query of the address in Server address to discover SSL certificates.Refer to Discovered certificates to view the names of the certificates and SSL certificate file to view the paths. You must enable SSL on the system web server for the target to use this component. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/deterministic-communication-error-codes.html language=enus -->
## TOPIC 00049: Deterministic Communication Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/deterministic-communication-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/deterministic-communication-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deterministic communication protocols can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −40635 The network speed you configured does not match the actual network speed. This can happen if your network adapter is

### Deterministic Communication Error Codes

Deterministic communication protocols can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −40635 | The network speed you configured does not match the actual network speed. This can happen if your network adapter is slower than the network speed you specified or if another adapter, hub, or switch has downgraded the actual network speed. |
| −40634 | The node that owns the associated variable cannot use the "Data Received" timing source, or the node that owns the associated variable can use only the "Data Sent" timing source. |
| -40633 | The requested error cannot be ignored because a full or partial shutdown of the node and/or network has been initiated. |
| -40632 | LabVIEW has detected a valid packet that does not follow NI's deterministic protocol on the network. LabVIEW will shut down the node/network. |
| -40631 | An already deployed configuration for one or more network nodes does not match the configuration of this node. |
| -40630 | The network transmission violated the requested timing. Refer to the "Avoid Jitter" topic and other timing topics in the LabVIEW Help for information on what may have caused the error and how you can avoid it. |
| -40629 | Resource allocation/creation/configuration failed because the existing resource is configured with different parameters. LabVIEW generates this error when you attempt to recreate a particular resource, such as a channel, with, for example, a different buffer size. |
| -40627 | Read failed after three retries because new data was placed into the buffer. |
| -40626 | The clock synchronization algorithm failed because a certain amount of cycle start packets have been missed.The deterministic communication engine must be restarted before additional write network transactions can occur. |
| -40618 | The reference is invalid. |
| -40616 | The deterministic communication engine is unable to locate a device with a specified MAC address. |
| -40615 | LabVIEW cannot instantiate the requested device in a specified mode because there is already a device initialized in deterministic mode. |
| -40613 | The specified subchannel is out of range. Refer to the LabVIEW Help for more information about supported ranges for channel subchannels. |
| -40612 | You have attempted one of the following illegal operations: allocation of a write terminal on a channel that another node owns; allocation of a shared memory variable on a non-shared memory channel; creation of a read or write terminal on a shared memory channel. |
| -40611 | An item with the specified index has already been configured. |
| -40609 | The item offset is outside of the range you specified during channel initialization time. |
| -40608 | One of the following occurred: 1) Message being written to the deterministic-communication engine exceeds the maximum size configured when the channel or terminal was created. 2) Buffer allocated for reading is smaller than the message size. |
| -40606 | A timing source with the same name already exists for the deterministic-communication engine. |
| -40603 | Files for the deterministic-communication engine are not installed properly. |
| -40602 | Deterministic-communication engine ran out of allocated resources. |
| -40601 | The deterministic-communication engine failed to initialize hardware. |
| -40600 | The deterministic communication engine failed to allocate enough memory while performing the requested operation. |
| 40620 | One of the following conditions occurred: 1) This slot-based variable has already been read within this network cycle. 2) This shared-memory-based variable has never been instantiated by the owner. |
| 40621 | The source node is still online, but no new data has been received for more than one network cycle because no new data has been written to the channel on the source node. |
| 40622 | No new data has been received for more than one network cycle because the source node is offline. |
| 40623 | One of the values received from the source node was not read and was overwritten. |
| 40624 | One of the values was overwritten before it was sent. LabVIEW returns this warning for non-shared memory variables that have been written more than once in a single network cycle. |
| 40625 | No data was sent from this channel in the previous network cycle because a write operation was delayed beyond a preconfigured threshold. An interrupt probably caused the delay. |
| 40626 | Clock synchronization algorithm failed because a sufficient number of cycle-start packets were missed. No additional write network transactions are allowed until the deterministic-communication engine is restarted. |
| 40628 | Attempted read operation at least twice before it succeeded due to new data being placed into the buffer. |
| 40630 | Network transmission violated requested timing. Refer to the "Avoid Jitter" topic and other timing topics in the LabVIEW Help for more information about what might have caused this error and how to avoid it. |
| 40631 | A deployed configuration for one or more network nodes does not match the configuration for this node. |
| 40632 | Detected a valid packet on the network that does not conform to the National Instruments deterministic protocol. The node or network will be shut down. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/general-real-time-error-codes.html language=enus -->
## TOPIC 00050: General Real-Time Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/general-real-time-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/general-real-time-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Real-Time Module can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −2232 The number of specified CPUs exceeds the number of CPUs available on the target. The number of specified CPUs exceeds the number of CP

### General Real-Time Error Codes

The Real-Time Module can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −2232 | The number of specified CPUs exceeds the number of CPUs available on the target. The number of specified CPUs exceeds the number of CPUs available on the target. |
| >−2231 | >The CPU pool settings are invalid. Each pool must contain at least 1 CPU. The CPU pool settings are invalid. Each pool must contain at least 1 CPU. |
| >−2230 | >This VI is not supported on the current platform. This VI is not supported on the current platform. |
| >1078 | >Failed to load shared library %s. Ensure that the library is present on the RT target. Use either MAX to install NI software or FTP to transfer custom libraries to the RT target. |
| >1079 | >When the RT target booted, the startup application configured to launch was missing. |
| >1080 | >The startup application configured to launch was corrupt and failed to load when the RT target booted. |
| >1081 | >Exception caused by loading of library %s on RT target device. |
| >1116 | >RTTarget.DiskCache.SizeInKB config token must be greater than zero. |
| >1117 | >RTTarget.DiskCache.Thread.Priority config token must be between -2 and 2. |
| >1118 | >RTTarget.DiskCache.Thread.IntervalInSecs config token must be greater than zero. |
| >1119 | >RTTarget.DiskCache.Thread.LinePerWakeup config token must be greater than or equal to zero. |
| >1120 | >Not enough memory to create disk cache. |
| >1121 | >Cannot create disk cache flush thread. |
| >1575 | >The function name for the %s node cannot be found in the library. To correct this error, right-click the Call Library Function Node and select Configure from the shortcut menu. Then choose the correct function name. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/input-or-ouput-variable-error-codes.html language=enus -->
## TOPIC 00051: I/O Variable Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/input-or-ouput-variable-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/input-or-ouput-variable-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: I/O variables can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −66231 An error occurred while trying to revert a change due to a deployment error. Some variables may have an incorrect configuration. −66230 You

### I/O Variable Error Codes

I/O variables can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −66231 | An error occurred while trying to revert a change due to a deployment error. Some variables may have an incorrect configuration. |
| −66230 | You must use NI-PSP to read or write the value of this I/O Variable. To access the value of this I/O Variable, use a URL with a prefix of ni.var.psp instead of ni.var.io. |
| −66229 | The number of elements written to the I/O variable container does not match the number of I/O variables in the container. The number of elements written to the I/O variable container must match the number of I/O variables in the container. You may also receive this error if you attempt to write to a read-only I/O variable container. |
| −66228 | Invalid session. Close the current refnum(s) and use the Shared Variable node to reopen the variable(s). |
| −66227 | Invalid entry in configuration file. If you edited the configuration file manually, restore a previous version. Otherwise, ensure the version of LabVIEW you used to deploy the variable matches the version of LabVIEW on the target. |
| −66226 | Incorrect use of internal API for I/O variable. If this error persists, contact National Instruments technical support. |
| −66225 | You cannot write to this I/O alias because it is configured as read only. |
| −66224 | You cannot read from this I/O alias because it is configured as write-only. |
| −66223 | The target ran out of memory while trying to configure network publishing of an I/O variable. This variable is no longer published correctly. You can either free some memory and deploy the variable again or restart your system. |
| −66221 | You cannot scale values of this data type. |
| −66219 | Network publishing of I/O variables was late. |
| −66218 | An unexpected error occurred while updating a network-published value. |
| −66217 | The I/O variable configuration is corrupt and cannot be read. Restore this configuration from a previous date or reinstall LabVIEW. If this error persists, contact National Instruments technical support. |
| −66216 | LabVIEW detected a feedback cycle while resolving aliases. |
| −66215 | The NI Scan Engine has not been initialized or has been shut down. |
| −66214 | The alias variable was unable to resolve the parent variable. |
| −66213 | Could not deploy variable because a variable of the same name already exists. If this error persists, contact National Instruments technical support. |
| −66212 | The data type of the reference does not match the data type of the variable. Ensure the data types match and re-open the reference. |
| −66211 | Insufficient memory on target. The value change request was discarded. Reduce memory usage on the target and try again. |
| −66210 | Failed to deploy Shared Variable library containing I/O aliases. A Shared Variable library with the same name without I/O aliases is already deployed to the target. To deploy the Shared Variable library with I/O aliases you must first undeploy the existing library with the same name. |
| −66209 | Failed to initialize a deployed variable at system startup. |
| −66208 | Invalid variable refnum. Either the variable was deleted after the reference was opened or a valid reference was never opened. |
| −66207 | You cannot write to an input channel. |
| −66206 | A required attribute could not be found during deployment of an I/O variable. |
| −66205 | The variable object was not found. |
| −66204 | The data type of the I/O variable alias does not match the data type of the I/O variable itself. Ensure the data types match and try creating the alias again. |
| −66203 | This I/O variable requires a hardware driver that is not installed on the deployment target. Install the missing driver, wait for the target to boot and for the NI Scan Engine to initialize, and deploy the variable again. |
| −66202 | Unable to force the requested channels. If this error persists, contact National Instruments technical support. |
| −66201 | The installed version of nilwpce.dll or nilwpce.out is out of date. Reinstall LabVIEW. If this does not fix the problem, contact National Instruments tech support. |
| −66200 | An unknown error occurred while using a variable. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/ni-scan-engine-error-codes.html language=enus -->
## TOPIC 00052: NI Scan Engine Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/ni-scan-engine-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/ni-scan-engine-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI Scan Engine can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −66504 The LabVIEW callback VI could not be registered or removed. −66503 The Variable run-time engine is not initialized. Ensure that the NI

### NI Scan Engine Error Codes

The NI Scan Engine can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −66504 | The LabVIEW callback VI could not be registered or removed. |
| −66503 | The Variable run-time engine is not initialized. Ensure that the NI Scan Engine is installed and then restart the target. |
| −66502 | Did not find the specified I/O module. Ensure that the specified module name matches the name of the I/O module currently deployed from the project. |
| −66501 | I/O module type mismatch. You attempted to read from an output module or write to an input I/O module. |
| −66500 | The size of the data array does not match the number of channels in the I/O module. |
| −66491 | The wait for an I/O scan completion failed due to either a timeout or because the controller shut down. |
| −66490 | An internal error occurred. The controller was unable to notify user code that the I/O scan completed. |
| −66480 | A user fault has occurred. |
| −66462 | The I/O data is not available because the scan engine is not currently running. Either the scan engine failed to start or stopped because the scan rate was too fast for your installed I/O. |
| −66461 | The I/O scan was repeatedly late and the NI Scan Engine terminated to ensure controller stability. Correct the source of lateness and clear all major faults to restart the scan engine. |
| −66460 | The I/O scan time exceeded the NI Scan Engine period you specified on the Scan Engine page of the target properties dialog box. |
| −66459 | The configuration for the I/O channel you accessed is not internally consistent due to a pending configuration change. Try to access the channel again after the configuration operation is complete. |
| −66457 | The I/O Reference has changed. The I/O Reference has changed, either due to a physical I/O configuration change or a deployed configuration change. To use the new configuration, you must use the Open Module Reference VI to create a new I/O Reference. |
| −66456 | The NI Scan Engine encountered an error while attempting to synchronize with the LabVIEW timing engine. |
| −66455 | The I/O device must be added to the project and deployed before the NI Scan Engine can use it. |
| −66454 | The NI Scan Engine received a request for an I/O driver that is not currently installed on the controller. |
| −66453 | The controller experienced an unrecoverable fault that cannot be cleared. Reboot your controller and contact National Instruments technical support. Refer to the fault list for details about the fault. |
| −66452 | Internal error: A component calling the NI Scan Engine failed to comply with the specified interface. |
| −66451 | The specified period for the NI Scan Engine is too short for this platform. |
| −66450 | The NI Scan Engine cannot perform the requested operation while in Fault mode. Clear all major faults and try again. |
| −66442 | The controller encountered an error and was unable to complete the operation. |
| −66432 | The NI Scan Engine failed to initialize on time, but may function normally given sufficient time. If the scanned I/O in your application is not updating properly, contact National Instruments technical support. |
| −66431 | An internal error terminated the NI Scan Engine. This is an unrecoverable fault. |
| −66430 | An internal error prevented a scan engine mode transition. This is an unrecoverable fault. |
| −66420 | A fault could not be added because it would exceed the maximum number of faults for the controller. |
| −66411 | The variable references I/O that has been taken offline by the user. The value returned is invalid. |
| −66402 | The controller did not have enough memory to complete the operation. |
| −66400 | A scan engine operation failed because the NI Scan Engine was not yet started. Ensure that the VI is running on a controller with the NI Scan Engine installed. |
| −66040 | An internal error occurred. An I/O driver attempted an operation that is not supported by this version of the NI Scan Engine. |
| −66030 | The operation cannot be completed because one of the scanned I/O buses is not in the required I/O mode. |
| −66023 | The I/O scan rate cannot be changed at this time due to the state of one of the scanned I/O buses. Try again later. |
| −66022 | The specified I/O scan rate is within range, but too precise for one of the scanned I/O buses. Round the rate up or down to the supported resolution. |
| −66021 | The specified I/O scan rate is too slow for one of the scanned I/O buses. |
| −66020 | The specified I/O scan rate is too fast for one of the scanned I/O buses. |
| −66013 | An internal error occurred: an I/O plug-in operation requested an invalid I/O collection. |
| −66012 | An internal error occurred: the specified I/O channel is not present in the specified I/O collection. |
| −66011 | An internal error occurred: the variable's data size is not consistent with the size of the I/O channel. |
| −66010 | An internal error occurred: the device identity data is not valid for this I/O plug-in. |
| −66009 | An internal error occurred: this I/O collection was already added to the I/O scan. |
| −66008 | The variable belongs to a module or I/O collection that is currently disconnected or offline. |
| −66004 | An internal error occurred: an invalid argument was passed to an I/O plug-in. |
| −66001 | An I/O plug-in ran out of memory. |
| −66000 | A miscellaneous system error has occurred in an I/O plug-in. |
| 66014 | The I/O variable accessor requested a timestamp, but this I/O device or channel is not configured for timestamps. |
| 66030 | This I/O variable is referencing an I/O device or channel that is not active in the current I/O mode. Data read may be stale or invalid and data written may not be sent to the output. |
| 66410 | The variable's value is being forced. Data read from this variable reflects the forced value, not the value from the underlying input channel. Data written to this variable is ignored, and not written to the underlying output channel. |
| 66411 | The I/O variable is referencing I/O that has been taken offline by the user. The value used may not be current. |
| 66430 | The fault was cleared and the controller is no longer in Fault mode, but the controller was unable to re-enter Active mode and is now in Configuration mode. |
| 66463 | The NI Scan Engine is running but there are no I/O drivers that use the scan engine. The scan engine uses system resources even if no plug-ins are installed. You can uninstall the scan engine from the controller, or install an I/O driver that uses the scan engine. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/real-time-fifo-error-codes.html language=enus -->
## TOPIC 00053: Real-Time FIFO Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/real-time-fifo-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/real-time-fifo-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Real-Time FIFO functions can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −2211 There was an attempt to create a Refnum to an existing RT FIFO using inconsistent Read/Write modes. There was an attempt to cr

### Real-Time FIFO Error Codes

The Real-Time FIFO functions can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −2211 | There was an attempt to create a Refnum to an existing RT FIFO using inconsistent Read/Write modes. There was an attempt to create a Refnum to an existing RT FIFO using inconsistent Read/Write modes. All calls to RT FIFO Create using the same name require the same Read/Write modes. |
| −2209 | The required RT FIFO DLL function is not bound. The required RT FIFO DLL function is not bound. The DLL cannot be found or is missing the function. |
| −2208 | This version of LabVIEW does not support waveforms in an RT FIFO. This version of LabVIEW does not support waveforms in an RT FIFO. Use LabVIEW 7.1 or later instead. |
| −2207 | Invalid waveform passed to the RT FIFO. |
| −2206 | RT FIFO does not exist. |
| −2205 | RT FIFO must contain at least two elements. |
| −2204 | Type mismatch. The named RT FIFO type does not match the type of the existing RT FIFO with the same name. |
| −2203 | Cannot match an empty name. |
| −2202 | The specified name does not exist. |
| −2201 | The specified name already exists and is of a different size or type. |
| −2200 | Unknown internal error. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/real-time-module-error-codes.html language=enus -->
## TOPIC 00054: Real-Time Module Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/real-time-module-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/real-time-module-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page describes error codes specific to the LabVIEW Real-Time Module. The error code tables are arranged in ascending order, from negative to positive values. You also can define custom error codes. Wire an error handler VI to another VI to return a description of any errors that occur. Error ha

### Real-Time Module Error Codes

This page describes [error codes](/csh?productcategories=147794&context=lvcore_lverror_error_code_ranges) specific to the LabVIEW Real-Time Module. The error code tables are arranged in ascending order, from negative to positive values. You also can [define custom error codes](/csh?productcategories=147794&context=lvcore_lvhowto_creating_user_defined_erro).

Wire an [error handler](/csh?productcategories=147794&context=lvcore_glang_dialog_ui_vis) VI to another VI to return a description of any errors that occur. Error handler VIs also can display a dialog box with an error code description and buttons that can stop or continue execution. You also can select **Help»Explain Error** to display an error code description in the **Explain Error** dialog box. Enter the error code number in one of the **Code** fields and click the **Status** button to change the button to a red X. A description of the error code appears in the **Explanation** field. This description is the same description that appears in this help file.

- [Deterministic Communication Error Codes](../errors/deterministic-communication-error-codes.html)
- [General Real-Time Error Codes](../errors/general-real-time-error-codes.html)
- [I/O Variable Error Codes](../errors/input-or-ouput-variable-error-codes.html)
- [NI Scan Engine Error Codes](../errors/ni-scan-engine-error-codes.html)
- [Real-Time FIFO Error Codes](../errors/real-time-fifo-error-codes.html)
- [Real-Time Shared Variable Error Codes](../errors/real-time-shared-variable-error-codes.html)
- [Real-Time Watchdog Error Codes](../errors/real-time-watchdog-error-codes.html)

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/real-time-shared-variable-error-codes.html language=enus -->
## TOPIC 00055: Real-Time Shared Variable Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/real-time-shared-variable-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/real-time-shared-variable-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Shared variables can return the following error codes when the Real-Time FIFO is enabled. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −1950678972 LabVIEW failed to load Logos. There may be a problem with the installation. Ensure that either th

### Real-Time Shared Variable Error Codes

Shared variables can return the following error codes when the Real-Time FIFO is enabled. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −1950678972 | LabVIEW failed to load Logos. There may be a problem with the installation. Ensure that either the Network Variable Engine or Variable Client Support is installed. |
| −1950678970 | Failed to load rtvarsup, which is required for Shared Variables with the Real-Time FIFO enabled. |
| −1950678969 | Failed to load rtvarnet, which is required for Network-Published Shared Variables with the Real-Time FIFO enabled. |
| −1950678966 | Cannot access I/O variables in Direct mode remotely. Either access the I/O variable locally, or change the access mode to Scanned. |
| −1950678964 | Failed to load NI Scan Engine software required for I/O Variable access. If you are hosting I/O variables on an RT target, ensure that the NI Scan Engine is installed on the RT target. If you are hosting I/O variables on Windows, you must install a Windows I/O driver, such as DeviceNet, that includes NI Scan Engine support. If you are hosting I/O variables in a Windows VI, the VI must be part of an open LabVIEW project. If you are hosting I/O variables in a Windows-built application, the application must be configured to include hardware configuration. |
| −1950678958 | This property can be called only on an I/O alias. |
| −1950678957 | This property can be called only on an I/O variable. |
| −2223 | The Variable Client Support software required by the shared variable is missing or of the wrong version. Ensure that you have installed the correct version of the Variable Client Support software on the RT target using MAX. |
| −2221 | The variable RT FIFO write buffer is full. The oldest data point in the buffer will be overwritten. |
| −2220 | The variable RT FIFO read buffer is empty. There is no available data to read. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=errors/real-time-watchdog-error-codes.html language=enus -->
## TOPIC 00056: Real-Time Watchdog Error Codes

- bundle_id: `lvrt-api-ref`
- source_path: `errors/real-time-watchdog-error-codes.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/errors/real-time-watchdog-error-codes.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Real-Time Watchdog VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW. Code Description −22015 Unable to return a value because the value exceeds the width of the return data type. You may be trying to get a timeout value

### Real-Time Watchdog Error Codes

The Real-Time Watchdog VIs can return the following error codes. Refer to the [KnowledgeBase](https://www.ni.com/r/rdbp01) for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −22015 | Unable to return a value because the value exceeds the width of the return data type. You may be trying to get a timeout value using a very small time step, such as nanoseconds. |
| −22014 | This watchdog has had kNIWatchdogHardwareLock enabled. You cannot update the watchdog configuration until you restart the target. |
| −22013 | The kernel portion of the watchdog driver is not present or failed to load correctly. As a result of this error, the watchdog hardware cannot be used. |
| −22012 | This watchdog cannot drive the specified trigger line in the requested manner. |
| −22011 | The watchdog hardware you requested is already in use or has been permanently locked. |
| −22010 | This watchdog cannot drive the specified trigger line. |
| −22009 | A memory allocation attempted by the watchdog driver has failed. Check available memory and disk space. |
| −22008 | The session handle or object pointer for this watchdog is either invalid or illegal. The session pointer is acquired by a call to the reserve method. |
| −22007 | The specified action cannot be added to the watchdog. Some actions can only be added once, and other actions have a maximum number that can be added. You should check for unwanted, repetitive calls to the API in your code. |
| −22006 | The watchdog driver has experienced an unexpected, low-level error. As a result of this error, this watchdog hardware cannot be used. |
| −22005 | The watchdog hardware you requested is either not in the system or has not been registered with the driver. The operating system may not have correctly detected the hardware. |
| −22004 | This watchdog hardware cannot handle the action you tried to register. You might be using a newer version of the API with an older hardware implementation, or you might be working with limited hardware. |
| −22003 | The attribute you tried to set is read only and cannot be changed. For example, you cannot set IDs and instance numbers. |
| −22002 | The attribute you tried to get or set is not recognized as a known attribute by this watchdog hardware. You might be using a newer version of the API with an older hardware implementation. |
| −22001 | This method or attribute is not supported by the watchdog hardware on this system. Not all parameters and methods apply to all types of watchdogs. |
| −22000 | An unexpected error occurred with the watchdog hardware on this system. |

Parent topic:

Real-Time Module Error Codes

<!--NI_TOPIC bundle=lvrt-api-ref path=functions/rt-fifo-create.html language=enus -->
## TOPIC 00057: RT FIFO Create Function

- bundle_id: `lvrt-api-ref`
- source_path: `functions/rt-fifo-create.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/functions/rt-fifo-create.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RT FIFO or obtains a reference to an existing RT FIFO. The RT FIFO Create function returns a reference to an RT FIFO, rt fifo, that you can use with other Real-Time FIFO functions. icon Inputs/Outputs cu32.png elements in array (1) elements in array is the number of elements in the array

### RT FIFO Create Function

Creates an RT FIFO or obtains a reference to an existing RT FIFO. The RT FIFO Create function returns a reference to an RT FIFO, **rt fifo**, that you can use with other Real-Time FIFO functions.

[IMAGE alt='icon' src='rt-fifo-create.png']

#### Inputs/Outputs

| elements in array (1) — elements in array is the number of elements in the array for each RT FIFO element. The default is 1. This input applies only if the RT FIFO elements are arrays. RT FIFOs do not support multi-dimensional arrays. size (10) — size is the number of elements in the RT FIFO. The default is 10. name (unnamed) — name contains the name of the RT FIFO that you want to obtain or create. The default is an empty string name. type — type is the type of data that you want the RT FIFO to contain. RT FIFOs do not support data types of variable size, such as clusters, strings, and variants. RT FIFOs also do not support multi-dimensional arrays. create if not found? (T) — create if not found? specifies whether to create a new RT FIFO if the FIFO specified by the name input does not currently exist. If the RT FIFO does not exist and create if not found? is TRUE, the VI creates a new RT FIFO. If the RT FIFO does not exist and create if not found? is FALSE, the VI does not create a new RT FIFO and returns an error. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. datapoints in waveform (1) — datapoints in waveform is the number of datapoints for every element of the array of waveforms. This input applies only if the RT FIFO elements are waveforms. r/w modes (polling,polling) — r/w modes specifies the read and write modes for a new RT FIFO. The read and write modes define the way you read a value from an empty FIFO or write a value to a FIFO that does not have an empty slot. An RT FIFO can wait until an empty slot becomes available for a write operation or wait until a value is available for a read operation. You can specify one of the following modes for reads and writes: polling—Use this mode to optimize the throughput performance of read and write operations. The polling mode continually polls the FIFO for new data or an open slot. The polling mode responds quicker than the blocking mode to new data or new empty slots, but requires more CPU overhead. Use the timeout in ms input of the RT FIFO Read or RT FIFO Write function to specify the amount of time that a write operation should poll for an empty slot or the amount of time a read operation should poll for new data. You also can use the overwrite on timeout input of the RT FIFO Write VI to specify whether to overwrite the oldest value in the RT FIFO when the value of the timeout in ms input expires. blocking—Use this mode to optimize the utilization of the CPU during read and write operations. The blocking mode allows the thread of the VI to sleep while it waits, allowing other tasks in the system to execute. Use the timeout in ms input of the RT FIFO Read or RT FIFO Write function to specify an amount of time a read operation can wait for a new value or an amount of time a write operation can wait for an empty slot. You also can use the overwrite on timeout input of the RT FIFO Write VI to specify whether to overwrite the oldest value in the RT FIFO when the value of the timeout in ms input expires. If you use the RT FIFO Create function to return a reference to an existing RT FIFO, the reference uses the read and write mode of the existing FIFO and ignores the modes specified with r/w modes. read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. rt fifo — rt fifo is a reference to an existing or newly created RT FIFO. created new? — created new? is TRUE if the function created a new RT FIFO. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. |

For RT FIFOs of array data types, set the **elements in array** input to the number of elements in each array. For RT FIFOs of waveform data types, set the **datapoints in waveform** input to the number of datapoints in the waveform. The number of elements in the array or the number of datapoints in the waveform is the same for every element of the RT FIFO.

You can create a new reference to an existing RT FIFO. To do so, you must specify the same values for **name**, **elements in array**, and **size** as that of the existing RT FIFO. Deleting the reference you create to an existing RT FIFO with the [RT FIFO Delete](rt-fifo-delete.html) function does not delete the original RT FIFO by default. You can wire TRUE to the **force destroy?** input of the RT FIFO Delete function to destroy all references to the RT FIFO.

Note

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- examples\Real-Time Module\RT Communication\RT FIFO\RT FIFO Communication.lvproj

Parent topic:

RT FIFO

<!--NI_TOPIC bundle=lvrt-api-ref path=functions/rt-fifo-delete.html language=enus -->
## TOPIC 00058: RT FIFO Delete Function

- bundle_id: `lvrt-api-ref`
- source_path: `functions/rt-fifo-delete.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/functions/rt-fifo-delete.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a reference or all references to a specified RT FIFO. You must delete an RT FIFO reference to free memory resources allocated for the FIFO when you created the reference. Deleting a reference to an RT FIFO does not delete the original RT FIFO by default. Use the force destroy? input to speci

### RT FIFO Delete Function

Deletes a reference or all references to a specified RT FIFO.

You must delete an RT FIFO reference to free memory resources allocated for the FIFO when you created the reference. Deleting a reference to an RT FIFO does not delete the original RT FIFO by default. Use the **force destroy?** input to specify to delete all reference to the RT FIFO.

[IMAGE alt='icon' src='rt-fifo-delete.png']

#### Inputs/Outputs

| rt fifo — rt fifo is a reference to an existing RT FIFO. force destroy? (F) — force destroy? specifies to delete all references to the RT FIFO if TRUE. If set to FALSE, only deletes the individual reference wired to rt fifo. The default is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- examples\Real-Time Module\RT Communication\RT FIFO\RT FIFO Communication.lvproj

Parent topic:

RT FIFO

<!--NI_TOPIC bundle=lvrt-api-ref path=functions/rt-fifo-read.html language=enus -->
## TOPIC 00059: RT FIFO Read Function

- bundle_id: `lvrt-api-ref`
- source_path: `functions/rt-fifo-read.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/functions/rt-fifo-read.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the oldest element in an RT FIFO. If no new data exists in the RT FIFO or if the RT FIFO is empty, this function waits for the amount of time specified in timeout in ms for new data. If the value of timeout in ms expires, the function returns the value of element in the element out output and

### RT FIFO Read Function

Reads the oldest element in an RT FIFO.

If no new data exists in the RT FIFO or if the RT FIFO is empty, this function waits for the amount of time specified in **timeout in ms** for new data. If the value of **timeout in ms** expires, the function returns the value of **element** in the **element out** output and returns TRUE in the **empty?** output.

[IMAGE alt='icon' src='rt-fifo-read.png']

#### Inputs/Outputs

| rt fifo — rt fifo is a reference to an existing RT FIFO. element — element sets the default return value of an empty RT FIFO. This data type changes to match the type of the default return value you wire. timeout in ms (0) — timeout in ms specifies the time, in milliseconds, that the function waits to receive a new value if the RT FIFO is empty. Wire a -1 to the timeout in ms input to wait indefinitely. The default is 0, which indicates to return immediately. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. rt fifo out — rt fifo out is a reference to an existing RT FIFO. element out — element out is the data read from the RT FIFO. If the VI does not read new data, the VI returns the default element. empty? — empty? is set to TRUE if the RT FIFO is empty when you read it and the value of timeout in ms has expired. error out — error out contains error information. This output provides standard error out functionality. # elements — # elements returns the number of elements remaining in the RT FIFO after the read or write operation. |
| --- |

Caution

element

element

element

Note

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- examples\Real-Time Module\RT Communication\RT FIFO\RT FIFO Communication.lvproj

Parent topic:

RT FIFO

<!--NI_TOPIC bundle=lvrt-api-ref path=functions/rt-fifo-write.html language=enus -->
## TOPIC 00060: RT FIFO Write Function

- bundle_id: `lvrt-api-ref`
- source_path: `functions/rt-fifo-write.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/functions/rt-fifo-write.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element to an RT FIFO. icon Inputs/Outputs cfiforn.png rt fifo rt fifo is a reference to an existing RT FIFO. cstr.png element element is the data to write to the RT FIFO. This data type changes to match the type of the value you want to write. ci32.png timeout in ms (0) timeout in ms (0)

### RT FIFO Write Function

Writes an element to an RT FIFO.

[IMAGE alt='icon' src='rt-fifo-write.png']

#### Inputs/Outputs

| rt fifo — rt fifo is a reference to an existing RT FIFO. element — element is the data to write to the RT FIFO. This data type changes to match the type of the value you want to write. timeout in ms (0) — timeout in ms (0) specifies the time, in milliseconds, that the function waits for an empty slot to write the data in the RT FIFO. The default is 0, which returns immediately. A value of -1 waits indefinitely. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. overwrite on timeout (T) — overwrite on timeout specifies whether to overwrite the oldest value in the RT FIFO if the FIFO does not have an available open slot and the value of the timeout in ms input expires. Use the timeout in ms input to specify an amount of time to wait for an open slot before overwriting the oldest value. If the value of the timeout in ms input expires and the overwrite on timeout input equals TRUE, the RT FIFO overwrites the oldest value and returns TRUE in the timed out? output. rt fifo out — rt fifo out is a reference to an existing RT FIFO. timed out? — timed out? returns TRUE if the timeout value has expired before an empty slot becomes available in the RT FIFO for the write operation. error out — error out contains error information. This output provides standard error out functionality. # elements — # elements returns the number of elements remaining in the RT FIFO after the read or write operation. |
| --- |

If the RT FIFO does not have empty elements, this function waits for an amount of time equal to the value of **timeout in ms** for an element to become available. If an empty element does not become available before the value of **timeout is ms** expires and the **overwrite on timeout** input is TRUE, this function overwrites the oldest element in the RT FIFO and returns TRUE in the **timed out?** output.

Note

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- examples\Real-Time Module\RT Communication\RT FIFO\RT FIFO Communication.lvproj

Parent topic:

RT FIFO

<!--NI_TOPIC bundle=lvrt-api-ref path=lvrt_intro.html language=enus -->
## TOPIC 00061: LabVIEW Real-Time Module Programming Reference Manual

- bundle_id: `lvrt-api-ref`
- source_path: `lvrt_intro.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/lvrt_intro.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Real-Time Module combines LabVIEW graphical programming with the power of a real-time operating system, enabling you to build real-time applications. Use this help to access information about Real-Time Module VIs and functions. Other Resources LabVIEW Real-Time Module Release Notes Visit this si

### LabVIEW Real-Time Module Programming Reference Manual

The Real-Time Module combines LabVIEW graphical programming with the power of a real-time operating system, enabling you to build real-time applications. Use this help to access information about Real-Time Module VIs and functions.

#### Other Resources

[LabVIEW Real-Time Module Release Notes](https://www.ni.com/en-us/support/documentation/release-notes/product.labview-real-time-module.html) 
Visit this site for links to known issues, bugs fixed since the last release, and other notes for any LabVIEW Real-Time Module release.

[NI License Manager Documentation](https://www.ni.com/docs/en-us/bundle/license-manager/page/manual-overview.html) 
Find documentation about activating, deactivating, and transferring software products using license activation codes or license files. For license administrators, this manual includes information for automating product activation and adding volume license servers.

Note

switch to English content

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/accm-mnu.html language=enus -->
## TOPIC 00062: Accumulate & Collect

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/accm-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/accm-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Accumulate & Collect function blocks to collect, summate, or integrate single-point data. icon

### Accumulate & Collect

Use the Accumulate & Collect [function blocks](/csh?context=lvrt_lvfbhelp_function_blocks) to collect, summate, or integrate single-point data.

[IMAGE alt='icon' src='accm-mnu.png']

- [Accumulate](../../../../vi-lib/functionblocks/accumulate/accumulate/merge-accumulate-vi.html) Accumulates a point-by-point sum. When enable is TRUE, this function block adds the value of input to the value of accumulation .
- [Collect Boolean Array](../../../../vi-lib/functionblocks/accumulate/collect-boolean-array/merge-collect-boolean-array-vi.html) Accumulates Boolean input elements when enable is TRUE. The collected data array contains the collection of input elements. If collected data reaches the capacity you specify using the array size input, the function block discards additional input values until you clear the function block by setting the reset input to TRUE.
- [Collect Numeric Array](../../../../vi-lib/functionblocks/accumulate/collect-numeric-array/merge-collect-numeric-array-vi.html) Accumulates numeric input elements when enable is TRUE. The collected data array contains the collection of input elements. If collected data reaches the capacity you specify using the array size input, the function block discards additional input values until you clear the function block by setting the reset input to TRUE.
- [Totalize](../../../../vi-lib/functionblocks/accumulate/totalize/merge-totalize-vi.html) Calculates a trapezoidal Riemann sum to approximate the integral of input .

Parent topic:

Function Blocks

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/bistable-mnu.html language=enus -->
## TOPIC 00063: Bistable/Flip-Flop

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/bistable-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/bistable-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Bistable/Flip-Flop function blocks to store Boolean values. icon

### Bistable/Flip-Flop

Use the Bistable/Flip-Flop [function blocks](/csh?context=lvrt_lvfbhelp_function_blocks) to store Boolean values.

[IMAGE alt='icon' src='bistable-mnu.png']

- [RS Bistable](../../../../vi-lib/functionblocks/bistables/rs-bistable/merge-rs-bistable-vi.html) Creates a reset-dominant latch, also known as a flip-flop.
- [SR Bistable](../../../../vi-lib/functionblocks/bistables/sr-bistable/merge-sr-bistable-vi.html) Creates a set-dominant latch, also known as a flip-flop.

Parent topic:

Function Blocks

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/control-mnu.html language=enus -->
## TOPIC 00064: Control

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/control-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Control function block to implement control algorithms. icon

### Control

Use the Control [function block](/csh?context=lvrt_lvfbhelp_function_blocks) to implement control algorithms.

[IMAGE alt='icon' src='control-mnu.png']

- [PID](../../../../vi-lib/functionblocks/control/pid/merge-pid-vi.html) PID algorithm for PID applications or high speed control applications that require an efficient algorithm. The PID algorithm features control output range limiting with integrator anti-windup and bumpless controller output for PID gain changes. This function block also features manual mode control with bumpless manual to automatic transitions, nonlinear integral action, two degree of freedom control, and error-squared control. You can use this function block to operate on one input value at a time.

Parent topic:

Function Blocks

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/counter-mnu.html language=enus -->
## TOPIC 00065: Timer

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/counter-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/counter-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Timer function blocks to implement counter and timing functionality in real-time applications. icon

### Timer

Use the Timer [function blocks](/csh?context=lvrt_lvfbhelp_function_blocks) to implement counter and timing functionality in real-time applications.

[IMAGE alt='icon' src='counter-mnu.png']

- [Count Down](../../../../vi-lib/functionblocks/counter/count-down/merge-count-down-vi.html) Counts down from the number you specify using the preset value input. The counter value output decrements on each rising edge of the count down input. When counter value reaches zero, done returns TRUE.
- [Count Up](../../../../vi-lib/functionblocks/counter/count-up/merge-count-up-vi.html) Counts up from zero. The counter value output increments on each rising edge of the count up input. The done output returns TRUE when counter value is greater than or equal to preset value .
- [Count Up Down](../../../../vi-lib/functionblocks/counter/count-up-down/merge-count-up-down-vi.html) Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block.
- [Pulse Timer](../../../../vi-lib/functionblocks/counter/pulse-timer/merge-pulse-timer-vi.html) Generates output pulses triggered by rising edges on the input signal.
- [Elapsed Timer](../../../../vi-lib/functionblocks/counter/elapsed-timer/merge-elapsed-timer-vi.html) Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block.
- [Retentive Timer On](../../../../vi-lib/functionblocks/counter/retentive-timer-on/merge-retentive-timer-on-vi.html) A timer that counts up to preset time (ms) while enable is TRUE. When enable is FALSE, this function block retains the accumulated time (ms) value. When accumulated time (ms) reaches preset time (ms) , done returns TRUE until reset, but accumulated time (ms) continues to increment while enable is TRUE until reset.
- [Timer On Delay](../../../../vi-lib/functionblocks/counter/timer-on-delay/merge-timer-on-delay-vi.html) Generates an output signal with falling edges that align with those of the input signal, but with rising edges delayed by preset time (ms) .
- [Timer Off Delay](../../../../vi-lib/functionblocks/counter/timer-off-delay/merge-timer-off-delay-vi.html) Generates an output signal with rising edges that align with the input signal, but with falling edges delayed by preset time (ms) .

Parent topic:

Function Blocks

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/edge-mnu.html language=enus -->
## TOPIC 00066: Edge Detect

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/edge-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/edge-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Edge Detect function blocks to detect transitions on digital signals. icon

### Edge Detect

Use the Edge Detect [function blocks](/csh?context=lvrt_lvfbhelp_function_blocks) to detect transitions on digital signals.

[IMAGE alt='icon' src='edge-mnu.png']

- [Edge Detect](../../../../vi-lib/functionblocks/edge-detection/edge-detect/merge-edge-detect-vi.html) Detects rising edges on input 1 and falling edges on input 2 . The output indicator pulses TRUE for one iteration when input 1 transitions to TRUE, when input 2 transitions to FALSE, or when both conditions occur simultaneously.
- [One Shot Rising with Input](../../../../vi-lib/functionblocks/edge-detection/one-shot-rising-with-input/merge-one-shot-rising-with-input-vi.html) Detects a rising edge, a transition from FALSE to TRUE, on the input signal. When a rising edge occurs, output is TRUE for one function block execution. The value of output remains FALSE until a new rising edge occurs.
- [One Shot Falling With Input](../../../../vi-lib/functionblocks/edge-detection/one-shot-falling-with-input/merge-one-shot-falling-with-input-vi.html) Detects a falling edge, a transition from TRUE to FALSE, on the input signal. When a falling edge occurs, output is TRUE for one function block execution. The value of output remains FALSE until a new falling edge occurs.

Parent topic:

Function Blocks

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/functionblocks/functionblocks-mnu.html language=enus -->
## TOPIC 00067: Function Blocks

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/functionblocks/functionblocks-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/functionblocks/functionblocks-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the LabVIEW function blocks to program using the function block programming paradigm defined in the IEC 61131-3 specification. icon The LabVIEW function blocks conform to the function block programming paradigm defined in the IEC 1131-3 specification. The functionality of the LabVIEW function bl

### Function Blocks

Use the LabVIEW [function blocks](/csh?context=lvrt_lvfbhelp_function_blocks) to program using the function block programming paradigm defined in the IEC 61131-3 specification.

[IMAGE alt='icon' src='functionblocks-mnu.png']

The LabVIEW function blocks conform to the function block programming paradigm defined in the IEC 1131-3 specification. The functionality of the LabVIEW function blocks partially overlaps with functionality provided by LabVIEW VIs and functions. Use function blocks if you want to publish parameter values with shared variables or if you want to use the IEC 1131-3 function block programming paradigm.

By default, each function block you place on the block diagram includes a set of variables corresponding to the function block input and output terminals. Therefore, you must place function blocks in a VI that is part of a LabVIEW project. You can right-click a function block on the block diagram and select **Show Function Block in Project** to highlight the function block item in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvconcepts_using_labview_projects) window. You also can right-click a function block item in the **Project Explorer** window and select **Find on Diagram** to highlight the function block on the block diagram.

#### Function Block Instance Configuration

You can configure the appearance and terminals of each function block instance in the application.

#### Appearance

Each function block instance on the block diagram displays two names: an instance name and a type name. The instance name appears at the top of the function block. You can click and change the instance name to distinguish between multiple instances of the same function block.

To minimize the size of a function block instance on the block diagram, use the **Compact View.** The **Compact View** of a function block instance displays abbreviated input and output terminal names. To switch to **Compact View,** right-click the function block instance on the block diagram and select Icon Style»Compact View. To switch back to the full-sized view, right-click the function block instance on the block diagram and select **Icon Style»Full View.**

#### Terminals

To configure input and output options for a function block instance, right-click the function block instance on the block diagram and select **Properties** from the shortcut menu to display the configuration page for the function block instance. You also can display the configuration page of a function block instance by double-clicking the function block instance on the block diagram.

You can use the **Visible** checkboxes for each terminal on the configuration page of a function block instance to show and hide function block terminals. If you hide a function block input terminal, LabVIEW automatically sets the **Data Source** of the terminal to the **Default value** of the data type. If you subsequently re-enable the **Visible** checkbox, the **Data Source** does not return to its previous value but remains the **Default value** until you specify a new value.

You can configure the data source of a function block terminal to use the block diagram terminal, the terminal variable, or the default value. If you select a data source other than **Terminal,** LabVIEW disables the block diagram terminal.

You can invert the value of a Boolean input or output terminal. Right-click a Boolean terminal on the function block instance and select **Invert** to toggle terminal inversion.

You can reorder function block input terminals and output terminals. However, to conform to dataflow standards, input terminals always appear on the left side of the function block and output terminals always appear on the right side of the function block. To switch the order of two terminals, right-click one of the terminals and select **Select Input** from the shortcut menu, then select the name of the other terminal.

#### Function Block Terminal Variables

By default, LabVIEW creates a single-process shared variable for each input and output terminal of each function block instance you use in the application. The function block terminal variables appear under the function block in the [Project Explorer](/csh?productcategories=147794&context=lvcore_lvconcepts_using_labview_projects) window. You can use function block terminal variables to access the inputs and outputs of a function block without block diagram wires. LabVIEW uses the **Default value** you specify on the function block instance configuration page as the initial value for the terminal variable.

Note

Project Explorer

Note

#### Avoiding Variable Overhead

Variables add overhead to the application, so you should include a function block terminal variable only if you plan to use it. To remove a function block terminal variable, select **No Variable** under **Variable Scope** on the configuration page for the function block instance. To display the configuration page for a function block instance, right-click the function block instance on the block diagram and select **Properties** from the shortcut menu.

#### Input Variables

You can use a function block input terminal variable to read the value of an input terminal from a location elsewhere in the application. LabVIEW writes the value of a function block input terminal to the corresponding variable, unless you have removed the variable by selecting **No Variable** under **Variable scope** on the function block instance configuration page.

If you select **Variable** as the **Data source** for a function block input, the function block uses the value of the variable as the input value. By default, the data source of all function block inputs is **Terminal,** in which case you can still use the variable to read the input value, but you cannot use the variable to write the input value of the function block.

Note

#### Output Variables

You can use a function block output terminal variable to read the value of an output terminal from a location elsewhere in the application. LabVIEW writes the value of a function block output terminal to the corresponding variable, unless you have removed the variable by selecting **No Variable** under **Variable scope** on the function block instance configuration page.

- [Accumulate & Collect](../../../../menus/categories/real-time/functionblocks/accm-mnu.html) Use the Accumulate & Collect function blocks to collect, summate, or integrate single-point data.
- [Bistable/Flip-Flop](../../../../menus/categories/real-time/functionblocks/bistable-mnu.html) Use the Bistable/Flip-Flop function blocks to store Boolean values.
- [Timer](../../../../menus/categories/real-time/functionblocks/counter-mnu.html) Use the Timer function blocks to implement counter and timing functionality in real-time applications.
- [Edge Detect](../../../../menus/categories/real-time/functionblocks/edge-mnu.html) Use the Edge Detect function blocks to detect transitions on digital signals.
- [Control](../../../../menus/categories/real-time/functionblocks/control-mnu.html) Use the Control function block to implement control algorithms.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/rtfifo-mnu.html language=enus -->
## TOPIC 00068: RT FIFO

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/rtfifo-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/rtfifo-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RT FIFO functions to send and receive data deterministically between VIs. RT FIFO functions provide a deterministic data transfer method that does not add jitter to a time-critical VI. An RT FIFO is a lossy form of communication that overwrites the oldest data element when the FIFO is full.

### RT FIFO

Use the RT FIFO functions to send and receive data deterministically between VIs. RT FIFO functions provide a deterministic data transfer method that does not add jitter to a time-critical VI. An RT FIFO is a lossy form of communication that overwrites the oldest data element when the FIFO is full.

The functions on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes) or [specific RT FIFO error codes](../../../errors/real-time-fifo-error-codes.html).

Note

[IMAGE alt='icon' src='rtfifo-mnu.png']

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\RT Communication\RT FIFO\RT FIFO Communication.lvproj

- [RT FIFO Create Function](../../../functions/rt-fifo-create.html) Creates an RT FIFO or obtains a reference to an existing RT FIFO. The RT FIFO Create function returns a reference to an RT FIFO, rt fifo , that you can use with other Real-Time FIFO functions.
- [RT FIFO Read Function](../../../functions/rt-fifo-read.html) Reads the oldest element in an RT FIFO.
- [RT FIFO Write Function](../../../functions/rt-fifo-write.html) Writes an element to an RT FIFO.
- [RT FIFO Delete Function](../../../functions/rt-fifo-delete.html) Deletes a reference or all references to a specified RT FIFO.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=menus/categories/real-time/rttiming-mnu.html language=enus -->
## TOPIC 00069: RT Timing

- bundle_id: `lvrt-api-ref`
- source_path: `menus/categories/real-time/rttiming-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/menus/categories/real-time/rttiming-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RT Timing VIs to control the timing of loops in VIs running on an RT target. icon

### RT Timing

Use the RT Timing VIs to control the timing of loops in VIs running on an RT target.

[IMAGE alt='icon' src='rttiming-mnu.png']

- [Wait Until Next Multiple](../../../vi-lib/express/rvi/timing/nirviwaituntilnextmultiple-vi.html) Waits until the value of the timer becomes a multiple of Count . Use this function to synchronize activities. You can call this function in a loop to control the loop execution rate.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/channels/channel-wire-endpoints.html language=enus -->
## TOPIC 00070: Channel Wire Endpoints

- bundle_id: `lvrt-api-ref`
- source_path: `resource/channels/channel-wire-endpoints.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/channels/channel-wire-endpoints.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Real-Time Module Channel wire endpoints are nodes where a channel wire terminates. By connecting a channel writer endpoint to a reader endpoint using a channel wire, you build a channel. The channel wire endpoints operate on the channel in the following way: the writer endpoints write data

### Channel Wire Endpoints

Requires: Real-Time Module

[Channel wire](/csh?productcategories=147794&context=lvcore_lvconcepts_channel_wires_intro) endpoints are nodes where a channel wire terminates. By connecting a channel writer endpoint to a reader endpoint using a channel wire, you build a channel. The channel wire endpoints operate on the channel in the following way: the writer endpoints write data to the channel, and reader endpoints read data from the channel. You can use the channel wire endpoints to write or read data between parallel sections of code. LabVIEW provides several channel templates. Each template expresses a different communications protocol to use between the writers and readers. Choose which channel template to use based on your communications needs.

Create a channel endpoint by right-clicking a terminal or a wire and selecting Create»Channel Writer or Create»Channel Reader. When you create an endpoint from a terminal, you instantiate the channel template with that data type as its transmission type.

| Template | Description |
| --- | --- |
| Real-Time Stream | Use the Real Time Stream channel to transfer data in time-critical loops. The Real Time Stream is based on the RT FIFO API and can be used within timed loops without causing jitter. |

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/channels/real-time-stream.html language=enus -->
## TOPIC 00071: Real Time Stream

- bundle_id: `lvrt-api-ref`
- source_path: `resource/channels/real-time-stream.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/channels/real-time-stream.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Real-Time Module Use the Real Time Stream channel to transfer data in time-critical loops. The Real Time Stream is based on the RT FIFO API and can be used within timed loops without causing jitter. Endpoint Description Read Reads an element from a Real Time Stream channel. Replicate Split

### Real Time Stream

Requires: Real-Time Module

Use the Real Time Stream channel to transfer data in time-critical loops. The Real Time Stream is based on the RT FIFO API and can be used within timed loops without causing jitter.

| Endpoint | Description |
| --- | --- |
| Read | Reads an element from a Real Time Stream channel. |
| Replicate | Splits a Real Time Stream channel into two Real Time Stream channels so that each of the readers of the channels receives a separate copy of the data written into the original channel. |
| Write | Writes an element to a Real Time Stream channel. If the channel is full, this endpoint defaults to jitter-free operation but can be configured to wait until space is available or a timeout occurs. |

Parent topic:

Channel Wire Endpoints

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/channels/real-time-stream/read-vi.html language=enus -->
## TOPIC 00072: Read

- bundle_id: `lvrt-api-ref`
- source_path: `resource/channels/real-time-stream/read-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/channels/real-time-stream/read-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads an element from a Real Time Stream channel. You can drop this endpoint on the block diagram by right-clicking a Real Time Stream channel terminal or wire and selecting Create»Channel Reader»Real Time Stream»Read. icon Inputs/Outputs cqueuern.png channel channel is the channel wire that connect

### Read

Reads an element from a Real Time Stream [channel](/csh?context=lvcore_lvconcepts_channel_wires_intro).

You can drop this endpoint on the block diagram by right-clicking a Real Time Stream channel terminal or wire and selecting **Create»Channel Reader»Real Time Stream»Read**.

[IMAGE alt='icon' src='read-vi.png']

#### Inputs/Outputs

| channel — channel is the channel wire that connects this endpoint to a writer endpoint. abort before read? (F) — abort before read? specifies whether to abort before reading the element from the channel. The default is FALSE. timeout in ms (-1) — timeout in ms is the time, in milliseconds, that this endpoint has to read the elements from the channel. The default value is -1, which means there is no time limit. abort signal — abort signal is an object for aborting a Real Time channel after the read operation. You can use this object's Abort method to stop the channel. Right click the abort signal terminal and select Create Abort Node to generate the Abort function. element — element returns the data that this endpoint reads from the channel. This output returns the default value of the transmission data type if a timeout occurs, if the channel closes without a valid last element, or if the channel aborts. element valid? — element valid? returns TRUE if the element was read successfully. This output returns FALSE if a timeout occurs or if the channel aborts. done? — done? returns TRUE if the endpoint has read the last element or if the channel aborts on either endpoint. This output returns FALSE if a timeout occurs. timed out? — timed out? returns TRUE if the amount of time specified by timeout in ms elapses. If timed out? is TRUE, element valid? will be FALSE. |
| --- |

#### Related Information

[Write](write-vi.html)

Parent topic:

Real Time Stream

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/channels/real-time-stream/replicate-vi.html language=enus -->
## TOPIC 00073: Replicate

- bundle_id: `lvrt-api-ref`
- source_path: `resource/channels/real-time-stream/replicate-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/channels/real-time-stream/replicate-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Splits a Real Time Stream channel into two Real Time Stream channels so that each of the readers of the channels receives a separate copy of the data written into the original channel. You can drop this endpoint on the block diagram by right-clicking a Real Time Stream channel and selecting Insert»R

### Replicate

Splits a Real Time Stream [channel](/csh?context=lvcore_lvconcepts_channel_wires_intro) into two Real Time Stream channels so that each of the readers of the channels receives a separate copy of the data written into the original channel.

You can drop this endpoint on the block diagram by right-clicking a Real Time Stream channel and selecting **Insert»Replicate**.

[IMAGE alt='icon' src='replicate-vi.png']

#### Inputs/Outputs

| r/w modes (polling, polling) — r/w modes specifies the read and write modes for a new RT FIFO. The read and write modes define the way you read a value from an empty FIFO or write a value to a FIFO that does not have an empty slot. An RT FIFO can wait until an empty slot becomes available for a write operation or wait until a value is available for a read operation. You can specify one of the following modes for reads and writes: polling—Use this mode to optimize the throughput performance of read and write operations. The polling mode continually polls the FIFO for new data or an open slot. The polling mode responds quicker than the blocking mode to new data or new empty slots, but requires more CPU overhead. Use the timeout in ms input of the Read or Write endpoint of the Real Time Stream channel to specify the amount of time that a write operation should poll for an empty slot or the amount of time a read operation should poll for new data. blocking—Use this mode to optimize the utilization of the CPU during read and write operations. The blocking mode allows the thread of the VI to sleep while it waits, allowing other tasks in the system to execute. Use the timeout in ms input of the Read or Write endpoint of the Real Time Stream channel to specify an amount of time a read operation can wait for a new value or an amount of time a write operation can wait for an empty slot. read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. datapoints in waveform (1) — datapoints in waveform is the number of datapoints for every element of the array of waveforms. This input applies only if the RT FIFO elements are waveforms. elements in array (1) — elements in array is the number of elements in the array for each RT FIFO element. The default is 1. This input applies only if the RT FIFO elements are arrays. RT FIFOs do not support multi-dimensional arrays. real time stream — real time stream is the channel wire that connects this endpoint to a writer endpoint and splits into two outgoing channels. independent aborts? (F) — independent aborts? specifies whether signaling one of the outgoing channels to abort only causes that one outgoing channel to abort. The default is FALSE, which means if one of the outgoing channels aborts, the other will also abort. size (10) — size specifies the maximum number of elements that can be buffered in the channel. The default is 10. Space for all the elements is allocated on the first call to this endpoint and will stay the same during subsequent calls until the channel is reset. Reset occurs when the common caller VI of both the writer endpoint and the reader endpoint begins another iteration. real time stream copy 1 — real time stream copy 1 is the first outgoing channel wire that connects this endpoint to a reader endpoint. real time stream copy 2 — real time stream copy 2 is the second outgoing channel wire that connects this endpoint to a reader endpoint. |
| --- |
| read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. |

#### Related Information

[Write](write-vi.html)

[Read](read-vi.html)

Parent topic:

Real Time Stream

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/channels/real-time-stream/write-vi.html language=enus -->
## TOPIC 00074: Write

- bundle_id: `lvrt-api-ref`
- source_path: `resource/channels/real-time-stream/write-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/channels/real-time-stream/write-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element to a Real Time Stream channel. If the channel is full, this endpoint defaults to jitter-free operation but can be configured to wait until space is available or a timeout occurs. You can drop this endpoint on the block diagram by right-clicking a terminal or a wire and selecting Cr

### Write

Writes an element to a Real Time Stream [channel](/csh?context=lvcore_lvconcepts_channel_wires_intro). If the channel is full, this endpoint defaults to jitter-free operation but can be configured to wait until space is available or a timeout occurs.

You can drop this endpoint on the block diagram by right-clicking a terminal or a wire and selecting **Create»Channel Writer»Real Time Stream»Write**.

[IMAGE alt='icon' src='write-vi.png']

#### Inputs/Outputs

| timeout in ms (-1) — timeout in ms is the time, in milliseconds, that this endpoint has to write the specified data to the channel. The default value is -1, which means there is no time limit. size (10) — size specifies the maximum number of elements that can be buffered in the channel. The default is 10. Space for all the elements is allocated on the first call to this endpoint and will stay the same during subsequent calls until the channel is reset. Reset occurs when the common caller VI of both the writer endpoint and the reader endpoint begins another iteration. element — element specifies the data to write to the channel. element valid? (T) — element valid? specifies whether the element is valid. The default is TRUE. If element valid? is FALSE, the endpoint writes the default value of the transmission data type to the channel instead of the value of element, and signals the reader that the element is not a valid data. last element? (F) — last element? specifies whether this is the last element that the endpoint writes to the channel. The default is FALSE. If TRUE, the endpoint marks the channel as closed and ignores further calls to write. The reader endpoint can continue reading data until the last element? output of the reader endpoint returns TRUE. elements in array (1) — elements in array is the number of elements in the array for each RT FIFO element. The default is 1. This input applies only if the RT FIFO elements are arrays. RT FIFOs do not support multi-dimensional arrays. datapoints in waveform (1) — datapoints in waveform is the number of datapoints for every element of the array of waveforms. This input applies only if the RT FIFO elements are waveforms. abort status (no abort) — abort status specifies the abort status of this endpoint. The default is no abort. 0No abort 1Abort now 2Abort if timeout r/w modes (polling, polling) — r/w modes specifies the read and write modes for a new RT FIFO. The read and write modes define the way you read a value from an empty FIFO or write a value to a FIFO that does not have an empty slot. An RT FIFO can wait until an empty slot becomes available for a write operation or wait until a value is available for a read operation. You can specify one of the following modes for reads and writes: polling—Use this mode to optimize the throughput performance of read and write operations. The polling mode continually polls the FIFO for new data or an open slot. The polling mode responds quicker than the blocking mode to new data or new empty slots, but requires more CPU overhead. Use the timeout in ms input of the Read or Write endpoint of the Real Time Stream channel to specify the amount of time that a write operation should poll for an empty slot or the amount of time a read operation should poll for new data. blocking—Use this mode to optimize the utilization of the CPU during read and write operations. The blocking mode allows the thread of the VI to sleep while it waits, allowing other tasks in the system to execute. Use the timeout in ms input of the Read or Write endpoint of the Real Time Stream channel to specify an amount of time a read operation can wait for a new value or an amount of time a write operation can wait for an empty slot. read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. channel — channel is the channel wire that connects this endpoint to a reader endpoint. timed out? — timed out? returns TRUE if the amount of time specified by timeout in ms elapses. done? — done? returns TRUE if the endpoint has written the last element or if the channel aborts on either endpoint. This output returns FALSE if a timeout occurs. |  |
| --- | --- |
| 0 | No abort |
| 1 | Abort now |
| 2 | Abort if timeout |
| read mode — read mode specifies the read mode for the RT FIFO. write mode — write mode specifies the write mode for the RT FIFO. |  |

#### Related Information

[Read](read-vi.html)

Parent topic:

Real Time Stream

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/dialog/variable/featurepacks/rt/real-time-fifo-page-shared-variable-properties-dialog-box.html language=enus -->
## TOPIC 00075: Real-Time FIFO Page (Shared Variable Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `resource/dialog/variable/featurepacks/rt/real-time-fifo-page-shared-variable-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/dialog/variable/featurepacks/rt/real-time-fifo-page-shared-variable-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Real-Time FIFO from the Category list of the Shared Variable Properties dialog box to display this page. Use this page to enable and configure the real-time features of a shared variable. This page includes the following components: Option Description Enable RT FIFO Enables the real-time FIFO

### Real-Time FIFO Page (Shared Variable Properties Dialog Box)

Select **Real-Time FIFO** from the **Category** list of the [Shared Variable Properties](/csh?productcategories=147794&context=lvcore_lvdialog_edit_variable_db) dialog box to display this page.

Use this page to enable and configure the real-time features of a shared variable.

This page includes the following components:

| Option | Description |
| --- | --- |
| Enable RT FIFO | Enables the real-time FIFO for a shared variable of type single-process or network-published.If you configure a network-published shared variable with network buffering and you enable the Real-Time FIFO, the network buffer must be as large as one FIFO element to ensure that data can be written. If the network buffer is smaller than a FIFO element, the network buffer overflows and no data transmits over the network. If you enable the Real-Time FIFO on a shared variable of waveform data type, the variant element of the waveform does not transfer because variants are variable-sized and therefore incompatible with the Real-Time FIFO. FIFO Type—Specifies the type of FIFO configuration to use.If the shared variable contains an array data type, you must specify the number of array elements. If the shared variable contains waveform data type, you must specify the number of points per waveform. If you select an array of waveform data type, you must specify both the number of waveform elements per array and the number of points per waveform. You must specify the required number of elements and/or waveform points exactly to avoid memory allocations that can cause jitter. Single Element—Specifies a FIFO buffer with a single element. Multi-element—Specifies a FIFO buffer with multiple elements. If you choose this option, you also must specify the number of FIFO elements to use. Use network buffer configuration—Uses the configuration you specify in the Use Buffering section of the Network page to configure the size and elements of the FIFO. This option is available only if you enable network buffering. |

To prevent data loss due to buffer overflow, consider using both the network buffer and the Real-Time FIFO buffer. Refer to the [National Instruments Web site](http://digital.ni.com/express.nsf/bycode/sharvar) for additional information about how buffer configuration affects shared variable performance.

Note

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/framework/providers/builds/appbuilder/cdf/component-definition-page-real-time-application-properties-dialog-box.html language=enus -->
## TOPIC 00076: Component Definition Page (Real-Time Application Properties Dialog Box)

- bundle_id: `lvrt-api-ref`
- source_path: `resource/framework/providers/builds/appbuilder/cdf/component-definition-page-real-time-application-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/framework/providers/builds/appbuilder/cdf/component-definition-page-real-time-application-properties-dialog-box.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this page of the Real-Time Application Properties dialog box to create a component definition file (CDF), which defines a stand-alone real-time application and any dependencies. Use the CDF to deploy the stand-alone real-time application from outside of the LabVIEW development environment with N

### Component Definition Page (Real-Time Application Properties Dialog Box)

Use this page of the [Real-Time Application Properties](../../../../../../dialog-boxes/real-time-application-properties-dialog-box.html) dialog box to create a component definition file (CDF), which defines a stand-alone real-time application and any dependencies. Use the CDF to [deploy the stand-alone real-time application from outside of the LabVIEW development environment](/csh?context=lvrt_lvrthowto_rt_building_rt_app) with NI Measurement & Automation Explorer (MAX) or the Install Startup instance of the install VI.

This page includes the following components:

| Option | Description |
| --- | --- |
| Create a component definition file (.cdf) and specify dependencies | Generates a CDF at build time and stores it in the National Instruments\\RT Images\\User Components directory. Place a checkmark in this checkbox only if you need to deploy a startup real-time application from outside of the LabVIEW development environment. |
| Version | Specifies the version number to associate with the build. Major—Specifies the component of the version number that indicates a major revision. Minor—Specifies the component of the version number that indicates a minor revision. Patch—Specifies the component of the version number that indicates a revision to fix problems. Build—Specifies the component of the version number that indicates a specific build. Auto-increment version on build—Specifies whether LabVIEW automatically increments the Build after each build. Note Save the project after you build to ensure that LabVIEW automatically increments correctly the next time you open the project. |
| Required software components | (PXI) Lists the software components that you can specify as dependencies of the startup real-time application. Place a checkmark in the checkbox next to each software component that your startup real-time application depends on. |
| Software component description | (PXI) Displays a description for the software component you select in the Required software components list. |
| Software version | (PXI) Lists the available versions of the software component you select in the Required software components list. Use this pull-down menu to specify a particular version of a software component as a dependency of the startup real-time application. |
| Required software set | (CompactRIO) Lists the software sets that you specify as dependencies of the startup real-time application. Click the software set that the startup real-time application depends on. |
| Addons | (CompactRIO) Lists the addons that correspond to the software set you select in the Required software set list. Place a checkmark in the checkbox next to each addon that the startup real-time application depends on. |
| Show software by set | (CompactRIO) Remove the checkmark from this checkbox to display the Required software components list instead of the Required software set and Addons lists. |
| Software set description | (CompactRIO) Displays a description for the software set you select in the Required software set list. |
| Software addon description | (CompactRIO) Displays a description for the addon you select in the Addons list. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/framework/providers/lvrealtime/pref-pages/os-and-cpu-configuration-page.html language=enus -->
## TOPIC 00077: OS and CPU Configuration Page

- bundle_id: `lvrt-api-ref`
- source_path: `resource/framework/providers/lvrealtime/pref-pages/os-and-cpu-configuration-page.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/framework/providers/lvrealtime/pref-pages/os-and-cpu-configuration-page.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This page is only available when you open a shipping example with a .lvproj file extension and you are not connected to an RT target. In this case, LabVIEW creates a generic target with an IP address of (0.0.0.0). Right click the generic RT target and select Properties to display the Real-Time Targe

### OS and CPU Configuration Page

This page is only available when you open a shipping example with a .lvproj file extension and you are not connected to an RT target. In this case, LabVIEW creates a generic target with an IP address of (0.0.0.0). Right click the generic RT target and select **Properties** to display the [Real-Time Target Properties](../../../../../dialog-boxes/rt-target-properties-dialog-box.html) dialog box. Select **OS and CPU Configuration** from the **Category** list to display this page.

If you plan to build an executable file based on the shipping example without connecting to an RT target, use this page to specify the OS and CPU of the RT target that will run the executable file.

Note

This page includes the following components:

| Option | Description |
| --- | --- |
| Target OS | Specifies the OS installed on the RT target that will run the executable file. |
| Target CPU | Specifies the CPU type for the RT target that will run the executable file. Note Refer to the RT target documentation for information about the target's OS and CPU type. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=resource/plugins/newdialogfiles/projectwizards/rtnpa/rtnpa-llb/real-time-project-wizard.html language=enus -->
## TOPIC 00078: Real-Time Project Wizard

- bundle_id: `lvrt-api-ref`
- source_path: `resource/plugins/newdialogfiles/projectwizards/rtnpa/rtnpa-llb/real-time-project-wizard.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/resource/plugins/newdialogfiles/projectwizards/rtnpa/rtnpa-llb/real-time-project-wizard.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select File»New to open the New dialog box. Expand the Project»Project from Wizard node and select Real-Time Project. Click the OK button to launch the Real-Time Project Wizard. You also can select Tools»Real-Time Module»Project Wizard to launch the Real-Time Project Wizard. Use the Real-Time Projec

### Real-Time Project Wizard

Select **File»New** to open the [New](/csh?productcategories=147794&context=lvcore_lvdialog_new_dialog_box) dialog box. Expand the **Project»Project from Wizard** node and select **Real-Time Project**. Click the **OK** button to launch the Real-Time Project Wizard. You also can select **Tools»Real-Time Module»Project Wizard** to launch the Real-Time Project Wizard.

Use the Real-Time Project Wizard to create a new LabVIEW project that includes an RT target and VIs ready to deploy to the target and host computer.

The Real-Time Project Wizard contains the following pages:

| Option | Description |
| --- | --- |
| Select project type, name, and folder | Includes the following components: Project type—Specifies the type of project to create. You can create projects with the Real-Time Project Wizard using one of three architectures continuous communication, state machine, or custom. Application includes deterministic components—Specifies that the application you want to create includes time-critical tasks that require deterministic performance on the RT target. Project name—Specifies a name for the new project. Project folder—Specifies the location to save the project files and VIs on the host computer. |
| Customize architecture options | Includes the following components: Target Configuration—Specifies the configuration of the VI that runs on the RT target. One loop—Uses a Timed Loop to control the timing and execution of the application tasks. You cannot include file I/O if you want to create an application with deterministic components using the one Timed Loop configuration. Two loops—Uses two Timed Loops running at different priorities to control the timing and execution of the application tasks. The higher priority Timed Loop controls the time-critical tasks. The lower priority Timed Loop controls user interface communication and file I/O tasks. Include file I/O—Specifies to include file I/O in the RT target VI. Host Configuration—Specifies the configuration of the user interface on the host computer. Include user interface—Specifies to include a user interface for the application on the host computer. Host VI—Uses a VI on the host computer to provide a user interface for the application. The VI running on the RT target shares data with the host VI using shared variables. Remote Panel—Uses a web browser to provide a user interface for the application. The Real-Time Project Wizard generates an HTML file that you must transfer to the RT target to publish the front panel of the RT target VI. |
| Add top-level VIs | Appears when you select Custom project from the Project type pull-down menu on the Select project type, name, and folder page. Includes the following components: Add blank VI to target—Adds a blank VI under the RT target in the project. Import existing VIs to host and target—Specifies you want to add existing VIs to the project under the host computer or RT target. VIs imported to run on host—Lists existing VIs that you want to add to the project under the host computer. VIs imported to run on target—Lists existing VIs that you want to add to the project under the RT target. Add VIs—Select VIs to add to the project under the host computer or the RT target. Remove—Removes the selected VIs from the project. |
| Browse targets | Includes the following components: Browse—Opens the Add Targets and Devices dialog box where you can add to the project an RT target of the type you selected. Selected target—Displays the RT target that you select. |
| Preview | Includes the following components: Open VIs when finished—Specifies whether to open the project VIs after the Real-Time Project Wizard creates the VIs. |

Parent topic:

LabVIEW Real-Time Module Dialog Box Reference

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/mathematics/ananlysutility-mnu.html language=enus -->
## TOPIC 00079: Real-Time Analysis Utilities

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/mathematics/ananlysutility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/mathematics/ananlysutility-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Real-Time Analysis Utilities VIs to handle the resources used by analysis functions in an RT application. The VIs on this palette can return general LabVIEW error codes. icon

### Real-Time Analysis Utilities

Use the Real-Time Analysis Utilities VIs to handle the resources used by analysis functions in an RT application.

The VIs on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='ananlysutility-mnu.png']

- [Initialize Analysis Workspace](../../../../../../vi-lib/analysis/aalutilities-llb/initialize-analysis-workspace-vi.html) Initializes the analysis workspace on the RT target and sets the workspace size to reserved memory size (KB) . To prevent race conditions, priority inversions, and other undefined behavior, you must use the Initialize Analysis Workspace VI according to a strict set of guidelines .
- [Enable Analysis Workspace](../../../../../../vi-lib/analysis/aalutilities-llb/enable-analysis-workspace-vi.html) Enables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Enable Analysis Workspace VI according to a strict set of guidelines .
- [Disable Analysis Workspace](../../../../../../vi-lib/analysis/aalutilities-llb/disable-analysis-workspace-vi.html) Disables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Disable Analysis Workspace VI according to a strict set of guidelines .
- [Uninitialize Analysis Workspace](../../../../../../vi-lib/analysis/aalutilities-llb/uninitialize-analysis-workspace-vi.html) Releases all resources used by the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Uninitialize Analysis Workspace VI according to a strict set of guidelines .

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/realtime-mnu.html language=enus -->
## TOPIC 00080: Real-Time

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/realtime-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/realtime-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Real-Time VIs to build deterministic applications using LabVIEW. The VIs on this palette can return general LabVIEW error codes. icon

### Real-Time

Use the Real-Time VIs to build deterministic applications using LabVIEW.

The VIs on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='realtime-mnu.png']

- [RT FIFO](../../../../../../menus/categories/real-time/rtfifo-mnu.html) Use the RT FIFO functions to send and receive data deterministically between VIs. RT FIFO functions provide a deterministic data transfer method that does not add jitter to a time-critical VI. An RT FIFO is a lossy form of communication that overwrites the oldest data element when the FIFO is full.
- [RT Timing](../../../../../../menus/categories/real-time/rttiming-mnu.html) Use the RT Timing VIs to control the timing of loops in VIs running on an RT target.
- [RT Utilities](../../../../../../targets/ni/rt/menus/categories/real-time/rtutility-mnu.html) Use the RT Utilities VIs to perform common tasks related to RT targets.
- [RT Watchdog](../../../../../../targets/ni/rt/menus/categories/real-time/rtwatchdog-mnu.html) Use the RT Watchdog VIs to detect and respond to failure conditions on networked RT Series devices.
- [RT SMP CPU Utilities](../../../../../../targets/ni/rt/menus/categories/real-time/smpcpuutility-mnu.html) Use the VIs on the RT SMP CPU Utilities palette to configure the set of CPUs available for automatic load balancing .
- [Function Blocks](../../../../../../menus/categories/real-time/functionblocks/functionblocks-mnu.html) Use the LabVIEW function blocks to program using the function block programming paradigm defined in the IEC 61131-3 specification.
- [RT Tracing](../../../../../../targets/ni/rt/menus/categories/real-time/rt-tracing-mnu.html) Use the Real-Time Tracing VIs to log events from a Real-Time target and save them to a file for analysis.

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/rt-tracing-mnu.html language=enus -->
## TOPIC 00081: RT Tracing

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/rt-tracing-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/rt-tracing-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Real-Time Tracing VIs to log events from a Real-Time target and save them to a file for analysis. icon

### RT Tracing

Use the Real-Time Tracing VIs to log events from a Real-Time target and save them to a file for analysis.

[IMAGE alt='icon' src='rt-tracing-mnu.png']

- [Start Trace](../../../../../../targets/ni/rt/vi-lib/rt-tracing/start-trace-vi.html) Starts a trace and logs events that occur after the Start Trace VI executes. You must ensure that you call the Start Trace VI before whatever behavior you are interested in occurs.
- [Stop Trace and Save](../../../../../../targets/ni/rt/vi-lib/rt-tracing/stop-trace-and-save-vi.html) Stops logging event data and saves the trace to a file on the Real-Time target.
- [Log User String](../../../../../../targets/ni/rt/vi-lib/rt-tracing/log-user-string-vi.html) Logs an event in the trace containing the specified string. The resulting event will be of type ftrace/print.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/rtett-mnu.html language=enus -->
## TOPIC 00082: RT Execution Trace Tool

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/rtett-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/rtett-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Real-Time Trace Viewer VIs to log a trace session from an application running on an RT target and transfer the trace session to the Real-Time Trace Viewer running on a host computer. The VIs on this palette are deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing palette instead. The

### RT Execution Trace Tool

Use the Real-Time Trace Viewer VIs to log a trace session from an application running on an RT target and transfer the trace session to the Real-Time Trace Viewer running on a host computer.

Caution

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='rtett-mnu.png']

- [TraceTool Start Trace](../../../../../../targets/ni/rt/vi-lib/tracetool-llb/tracetool-start-trace-vi.html) This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace VI executes. You must ensure that you wire the TraceTool Start Trace VI in sequence with all of the VIs that you want to log.
- [TraceTool Stop Trace And Send](../../../../../../targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-send-vi.html) This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer.
- [TraceTool Log User Event](../../../../../../targets/ni/rt/vi-lib/tracetool-llb/tracetool-log-user-event-vi.html) This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Logs a user-defined event in the trace session.
- [TraceTool Stop Trace and Save](../../../../../../targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-save-vi.html) This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Stops logging event data from the application and saves the trace session to file on the RT target.
- [TraceTool Load Trace and Send](../../../../../../targets/ni/rt/vi-lib/tracetool-llb/tracetool-load-trace-and-send-vi.html) This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer.

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/rtutility-mnu.html language=enus -->
## TOPIC 00083: RT Utilities

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/rtutility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/rtutility-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RT Utilities VIs to perform common tasks related to RT targets. The VIs on this palette can return general LabVIEW error codes. The VIs on this palette appear only in the RT context, and will not appear if an RT target is not added to the project. icon SubpaletteDescription NI System Configu

### RT Utilities

Use the RT Utilities VIs to perform common tasks related to RT targets.

The VIs on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes).

The VIs on this palette appear only in the RT context, and will not appear if an RT target is not added to the project.

[IMAGE alt='icon' src='rtutility-mnu.png']

| Subpalette | Description |
| --- | --- |
| NI System Configuration VIs | Use the System Configuration VIs to gather information and perform tasks programmatically on both local and remote systems. |

- [RT Read Switch](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-read-switch-vi.html) Reads the switch state of DIP switches on a networked RT Series device.
- [RT LEDs](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-leds-vi.html) Controls the LEDs on all RT Series devices.
- [RT Debug String](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-debug-string-vi.html) Sends a string to an output port for display, or writes a string to the system log.
- [RT Get CPU Loads](../../../../../../targets/ni/rt/vi-lib/utility/rt-get-cpu-loads-vi.html) Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this VI returns the total load as a percentage of capacity. This VI also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time devoted to Timed Structures and interrupt service routines (ISRs).
- [RT Get Timestamp](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-get-timestamp-vi.html) Inserts a 64-bit timestamp value from a high-precision timing source into a preallocated array at an index value specified by iteration . The timestamp value indicates the time when the RT Get Timestamp VI executes on the RT target.
- [RT Timestamp Analysis](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-timestamp-analysis-vi.html) Analyzes the array of timestamps returned by the RT Get Timestamp VI.
- [RT Calibrate Touchscreen](../../../../../../targets/ni/rt/vi-lib/rtutility-llb/rt-calibrate-touchscreen-vi.html) Opens an interactive wizard that allows end users to calibrate touch panel monitors. This VI runs only on RT targets that support the embedded UI. Refer to the specific RT target hardware documentation to learn if the target supports an embedded UI.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/rtwatchdog-mnu.html language=enus -->
## TOPIC 00084: RT Watchdog

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/rtwatchdog-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/rtwatchdog-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RT Watchdog VIs to detect and respond to failure conditions on networked RT Series devices. The VIs on this palette can return general LabVIEW error codes or specific Watchdog error codes. icon Examples Refer to the following example files included with LabVIEW Real-Time Module. labview\exam

### RT Watchdog

Use the RT Watchdog VIs to detect and respond to failure conditions on networked RT Series devices.

The VIs on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes) or [specific Watchdog error codes](/csh?context=lvrt_lvrthelp_rt_watchdog_error_codes).

[IMAGE alt='icon' src='rtwatchdog-mnu.png']

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\NI Watchdog\Watchdog - RT Engine.lvproj

- [Watchdog Configure](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-configure-vi.html) Configures a new watchdog object with a timeout and expiration actions .
- [Watchdog Whack](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-whack-vi.html) Resets the watchdog counter to the value you specify using either the Watchdog Configure VI or the Watchdog Set Attribute VI.
- [Watchdog Clear](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-vi.html) Resets the watchdog hardware and associated attributes and actions to the default power-on state and closes the watchdog object.
- [Advanced Watchdog](../../../../../../targets/ni/rt/menus/categories/real-time/rtwatchdogadv-mnu.html) Use the Advanced Watchdog VIs to implement advanced low-level watchdog tasks.

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/rtwatchdogadv-mnu.html language=enus -->
## TOPIC 00085: Advanced Watchdog

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/rtwatchdogadv-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/rtwatchdogadv-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced Watchdog VIs to implement advanced low-level watchdog tasks. The VIs and functions on this palette can return general LabVIEW error codes or specific Watchdog error codes. icon

### Advanced Watchdog

Use the Advanced Watchdog VIs to implement advanced low-level watchdog tasks.

The VIs and functions on this palette can return [general LabVIEW error codes](/csh?context=lvcore_lverror_misc_lv_error_codes) or [specific Watchdog error codes](/csh?context=lvrt_lvrthelp_rt_watchdog_error_codes).

[IMAGE alt='icon' src='rtwatchdogadv-mnu.png']

- [Watchdog Open](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-open-vi.html) Opens a watchdog session using the first available watchdog object .
- [Watchdog Start](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-start-vi.html) Restarts the countdown of the watchdog timer if the watchdog object is running or expired.
- [Watchdog Acknowledge](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-acknowledge-vi.html) Resets the watchdog counter to the specified count, but does not start the countdown if the counter has not yet started or has expired.
- [Watchdog Reset](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-reset-vi.html) Resets the watchdog hardware and associated attributes and actions to the default power-on state.
- [Watchdog Close](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-close-vi.html) Closes the watchdog session associated with the watchdog object you specify.
- [Watchdog Add Reset Action](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-reset-action-vi.html) Configures the watchdog object to reset the controller when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.
- [Watchdog Add Interrupt Action](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-interrupt-action-vi.html) Configures the watchdog object to trigger an occurrence when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.
- [Watchdog Add Trigger Action](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-trigger-action-vi.html) Configures the watchdog object to assert a PXI trigger line when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.
- [Watchdog Add Restart RTE Action](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-restart-rte-action-vi.html) Configures the watchdog object to restart only the LabVIEW Run-Time Engine when the watchdog timer expires, without resetting the FPGA application or losing network connection. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.
- [Watchdog Clear Outputs](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-outputs-vi.html) Clears any triggers asserted by the watchdog object .
- [Watchdog Enable](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-enable-vi.html) Enables the watchdog object and starts the countdown of the watchdog timer if the current status of the watchdog object is disabled .
- [Watchdog Disable](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-disable-vi.html) Disables the watchdog object you specify and clears any triggers asserted by the watchdog object.
- [Watchdog Get Attribute](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-get-attribute-vi.html) Returns the current value of the watchdog attribute you specify.
- [Watchdog Set Attribute](../../../../../../targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-set-attribute-vi.html) Sets the watchdog object attribute you specify to the value you specify.

Parent topic:

RT Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/menus/categories/real-time/smpcpuutility-mnu.html language=enus -->
## TOPIC 00086: RT SMP CPU Utilities

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/menus/categories/real-time/smpcpuutility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/menus/categories/real-time/smpcpuutility-mnu.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on the RT SMP CPU Utilities palette to configure the set of CPUs available for automatic load balancing. The VIs on this palette can return general LabVIEW error codes. icon

### RT SMP CPU Utilities

Use the VIs on the RT SMP CPU Utilities palette to [configure the set of CPUs available for automatic load balancing](/csh?context=lvrt_lvrtconcepts_smp_api).

The VIs on this palette can return [general LabVIEW error codes](/csh?productcategories=147794&context=lvcore_lverror_misc_lv_error_codes).

[IMAGE alt='icon' src='smpcpuutility-mnu.png']

- [RT Set CPU Pool Sizes](../../../../../../targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-sizes-vi.html) Sets the number of CPUs in the CPU pools available for automatic load balancing. You can use this VI to define the System pool and the Timed Structures pool by specifying the number of CPUs you want each pool to contain.
- [RT Set CPU Pool Assignments](../../../../../../targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-assignments-vi.html) Assigns CPUs to pools for automatic load balancing . This VI assigns CPUs to one of four possible states: System pool only, Timed Structures pool only, both pools, or no pool (reserved). This VI outputs the bit masks that specify the CPUs assigned to each pool.
- [RT Set CPU Pool](../../../../../../targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-vi.html) Specifies the set of CPUs included in the System pool or the Timed Structures pool for automatic load balancing .
- [RT Get Number of CPUs](../../../../../../targets/ni/rt/vi-lib/utility/rt-get-number-of-cpus-vi.html) Reads the number of CPUs in the system.
- [RT Get CPU Loads](../../../../../../targets/ni/rt/vi-lib/utility/rt-get-cpu-loads-vi.html) Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this VI returns the total load as a percentage of capacity. This VI also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time devoted to Timed Structures and interrupt service routines (ISRs).

Parent topic:

Real-Time

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rt-tracing/log-user-string-vi.html language=enus -->
## TOPIC 00087: Log User String

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rt-tracing/log-user-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rt-tracing/log-user-string-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logs an event in the trace containing the specified string. The resulting event will be of type ftrace/print. icon Inputs/Outputs cstr.png user string user string specifies the string to log to the trace. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this

### Log User String

Logs an event in the trace containing the specified string. The resulting event will be of type ftrace/print.

[IMAGE alt='icon' src='log-user-string-vi.png']

#### Inputs/Outputs

| user string — user string specifies the string to log to the trace. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RT Tracing

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rt-tracing/start-trace-vi.html language=enus -->
## TOPIC 00088: Start Trace

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rt-tracing/start-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rt-tracing/start-trace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts a trace and logs events that occur after the Start Trace VI executes. You must ensure that you call the Start Trace VI before whatever behavior you are interested in occurs. icon Inputs/Outputs cu32.png buffer size (KB) buffer size is the requested size of the memory buffer that logs all even

### Start Trace

Starts a trace and logs events that occur after the Start Trace VI executes. You must ensure that you call the Start Trace VI before whatever behavior you are interested in occurs.

[IMAGE alt='icon' src='start-trace-vi.png']

#### Inputs/Outputs

| buffer size (KB) — buffer size is the requested size of the memory buffer that logs all events in memory on the Real-Time target. If the logged event data exceed the memory buffer size, any subsequent event data that you log overwrites the oldest data in the buffer. The requested buffer size might be modified slightly to meet the system requirements for trace buffers (minimum size, multiple of page size, etc). If you specify 0 as the buffer size, a default buffer size will be used. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RT Tracing

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rt-tracing/stop-trace-and-save-vi.html language=enus -->
## TOPIC 00089: Stop Trace and Save

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rt-tracing/stop-trace-and-save-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rt-tracing/stop-trace-and-save-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops logging event data and saves the trace to a file on the Real-Time target. NI recommends that you call the Stop Trace and Save VI as soon as possible after the behavior you are interested in occurs. This improves the likelihood that the saved trace will contain relevant event data leading up to

### Stop Trace and Save

Stops logging event data and saves the trace to a file on the Real-Time target.

NI recommends that you call the Stop Trace and Save VI as soon as possible after the behavior you are interested in occurs. This improves the likelihood that the saved trace will contain relevant event data leading up to the behavior of interest. If the Stop Trace and Save VI is called too long after the behavior occurs, the relevant event data leading up to the behavior of interest might be lost. This happens because the buffer used to hold event data during tracing has a fixed size. When the buffer fills, additional event data overwrites the oldest information in the buffer. To avoid this situation, you can also modify the buffer size when calling the [Start Trace](start-trace-vi.html) VI.

[IMAGE alt='icon' src='stop-trace-and-save-vi.png']

#### Inputs/Outputs

| trace file path — trace file path specifies the file path on the Real-Time target where the trace will be saved. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Trace files can contain sensitive information about your application and other software running on the Real-Time target. As a result, the trace file is created with admin-only permissions. You will need to use admin credentials to modify the trace file or to copy it from the target. NI recommends you consider encrypting the contents of the trace file if appropriate.

Refer to the [Tracing on NI Linux Real-Time document](https://nilrt-docs.ni.com/troubleshooting/tracing.html) to learn more about viewing and analyzing traces from NI Linux Real-Time targets.

Parent topic:

RT Tracing

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-calibrate-touchscreen-vi.html language=enus -->
## TOPIC 00090: RT Calibrate Touchscreen

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-calibrate-touchscreen-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-calibrate-touchscreen-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens an interactive wizard that allows end users to calibrate touch panel monitors. This VI runs only on RT targets that support the embedded UI. Refer to the specific RT target hardware documentation to learn if the target supports an embedded UI. icon Inputs/Outputs cerrcodeclst.png error in (no

### RT Calibrate Touchscreen

Opens an interactive wizard that allows end users to calibrate touch panel monitors. This VI runs only on RT targets that support the embedded UI. Refer to the specific RT target hardware documentation to learn if the target supports an embedded UI.

[IMAGE alt='icon' src='rt-calibrate-touchscreen-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-debug-string-vi.html language=enus -->
## TOPIC 00091: RT Debug String

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-debug-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-debug-string-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a string to an output port for display, or writes a string to the system log. icon Inputs/Outputs cstr.png String to write String to write is the data string to write to the output port or system log. cu16.png Interface Interface specifies to send the string to an output port or to write the s

### RT Debug String

Sends a string to an output port for display, or writes a string to the system log.

[IMAGE alt='icon' src='rt-debug-string-vi.png']

#### Inputs/Outputs

| String to write — String to write is the data string to write to the output port or system log. Interface — Interface specifies to send the string to an output port or to write the string to the system log. By default, this VI sends the debug string to the video port. 0Write to serial—Sends the debug string to the serial port. This option requires a device capable of serial redirection. 1Write to monitor—Sends the debug string to the video port. 2Write to system log—Sends the debug string to the nierrlog system log. (NI Linux Real-Time) View the debug string in the System Log Viewer page of NI Web-based Configuration & Monitoring. (Phar Lap ETS, VxWorks) View the debug string in the console. The debug string displays alongside other console output. VISA resource name — VISA resource name specifies the VISA resource to open. This control also specifies the session and class. Refer to Configuring I/O Controls for information about configuring a VISA resource name. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Write to serial—Sends the debug string to the serial port. This option requires a device capable of serial redirection. |
| 1 | Write to monitor—Sends the debug string to the video port. |
| 2 | Write to system log—Sends the debug string to the nierrlog system log. (NI Linux Real-Time) View the debug string in the System Log Viewer page of NI Web-based Configuration & Monitoring. (Phar Lap ETS, VxWorks) View the debug string in the console. The debug string displays alongside other console output. |

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-get-timestamp-vi.html language=enus -->
## TOPIC 00092: RT Get Timestamp

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-get-timestamp-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-get-timestamp-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a 64-bit timestamp value from a high-precision timing source into a preallocated array at an index value specified by iteration. The timestamp value indicates the time when the RT Get Timestamp VI executes on the RT target. Use the RT Timestamp Analysis VI to analyze the timestamp array retu

### RT Get Timestamp

Inserts a 64-bit timestamp value from a high-precision timing source into a preallocated array at an index value specified by **iteration**. The timestamp value indicates the time when the RT Get Timestamp VI executes on the RT target.

Use the [RT Timestamp Analysis](rt-timestamp-analysis-vi.html) VI to analyze the timestamp array returned by the RT Get Timestamp VI.

[IMAGE alt='icon' src='rt-get-timestamp-vi.png']

#### Inputs/Outputs

| timestamp array in — timestamp array in specifies the preallocated array used to store timestamps for each iteration of the RT Get Timestamp VI. You must preallocate an array with enough elements to store all of the timestamps you want to collect. iteration — iteration specifies the index value where the RT Get Timestamp VI inserts the current timestamp in the timestamp array. Wire a loop iteration terminal to index the timestamps relative to their execution order. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. timestamp array out — timestamp array out returns an array that contains a timestamp for each iteration of the RT Get Timestamp VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

You can use the RT Get Timestamp VI in a For or While Loop to benchmark code. However, you must ensure that the RT Get Timestamp VI executes in the benchmarking application at the same point relative to the code for each iteration. You also must preallocate the timestamp array that you wire to **timestamp array in** to avoid memory allocations that can affect the timestamp value.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\RT Benchmarking\Benchmark Project.lvproj

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-leds-vi.html language=enus -->
## TOPIC 00093: RT LEDs

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-leds-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-leds-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the LEDs on all RT Series devices. icon Inputs/Outputs ci32.png LED Num LED Num is the number of the LED that the VI modifies. The LED number depends on the type of hardware. LED Num is zero-indexed. You can specify LED Num as 0 for most CompactRIO targets. ci32.png State State is the state

### RT LEDs

Controls the LEDs on all RT Series devices.

[IMAGE alt='icon' src='rt-leds-vi.png']

#### Inputs/Outputs

| LED Num — LED Num is the number of the LED that the VI modifies. The LED number depends on the type of hardware. LED Num is zero-indexed. You can specify LED Num as 0 for most CompactRIO targets. State — State is the state to assign to the LED. 0Turns off the LED 1Sets the LED to the device default color1 2Sets the LED to the device default color2 (if available) 3Toggle between off and default color1 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Led State — Led State indicates if the LED is on or off. TRUE indicates that the LED is on. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Turns off the LED |
| 1 | Sets the LED to the device default color1 |
| 2 | Sets the LED to the device default color2 (if available) |
| 3 | Toggle between off and default color1 |

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-read-switch-vi.html language=enus -->
## TOPIC 00094: RT Read Switch

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-read-switch-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-read-switch-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the switch state of DIP switches on a networked RT Series device. The following table describes the DIP switches you can read with this VI: switch type switch ID Purpose of Switch system 0 Safe mode system 1 IP reset system 2 No app system 3 Console out user 0 User1 icon Inputs/Outputs cenum.p

### RT Read Switch

Reads the switch state of DIP switches on a networked RT Series device.

| switch type | switch ID | Purpose of Switch |
| --- | --- | --- |
| system | 0 | Safe mode |
| system | 1 | IP reset |
| system | 2 | No app |
| system | 3 | Console out |
| user | 0 | User1 |

[IMAGE alt='icon' src='rt-read-switch-vi.png']

#### Inputs/Outputs

| switch type (system switch) — switch type is the type of DIP switch you want to configure. A system switch changes the boot behavior of a controller. A user switch allows users to manually interact with VIs on the device. 0system switch—Specifies that the switch is a system switch. 1user switch—Specifies that the switch is a user switch. switch ID — switch ID is the index number that corresponds to the device DIP switch. Index numbers always start at 0 for each switch type and the total number is based on the number of device DIP switches. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. switch state (on/off) — switch state indicates the state of the switch. TRUE indicates the switch is on. FALSE indicates the switch is off. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | system switch—Specifies that the switch is a system switch. |
| 1 | user switch—Specifies that the switch is a user switch. |

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtutility-llb/rt-timestamp-analysis-vi.html language=enus -->
## TOPIC 00095: RT Timestamp Analysis

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtutility-llb/rt-timestamp-analysis-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtutility-llb/rt-timestamp-analysis-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analyzes the array of timestamps returned by the RT Get Timestamp VI. icon Inputs/Outputs c1du64.png timestamp array timestamp array specifies the array of 64-bit timestamps returned from the RT Get Timestamp VI that you want to analyze. c1du64.png calibration array calibration array is an array use

### RT Timestamp Analysis

Analyzes the array of timestamps returned by the [RT Get Timestamp](/csh?context=lvrt_lvrtvihelp_rt_get_timestamp) VI.

[IMAGE alt='icon' src='rt-timestamp-analysis-vi.png']

#### Inputs/Outputs

| timestamp array — timestamp array specifies the array of 64-bit timestamps returned from the RT Get Timestamp VI that you want to analyze. calibration array — calibration array is an array used to remove the overhead associated with the RT Get Timestamp VI. The RT Timestamp Analysis VI subtracts the mean value of all elements in calibration array from each element in timestamp array to remove the overhead incurred when the RT Get Timestamp VI adds the element to the timestamp array in memory on the RT target. warmup iterations — Warmup iterations specifies the number of timestamps to ignore from the beginning of timestamp array. Use Warmup iterations to remove initial timestamps from the beginning of timestamp array that might have been affected during the initial execution of the application on an RT target. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. mean time (uS) — mean time returns the average execution time for the values in the execution times array. standard deviation (uS) — standard deviation returns the standard deviation for the values in the execution times array. execution times (uS) — execution times returns the execution time, in microseconds, between each element of timestamp array. execution histogram — execution histogram returns histogram values for the elements of execution times. max jitter (uS) — max jitter returns the maximum deviation between elements of execution time and the value of mean time. The value can represent a positive or negative deviation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

The [RT Get Timestamp](rt-get-timestamp-vi.html) VI returns a timestamp array that you can use to benchmark code. The timestamps returned in the array contain additional overhead incurred when the RT Get Timestamp VI adds timestamp values to the array in memory on an RT target. You can run the RT Get Timestamp VI alone for several iterations and add the timestamps to a calibration array. You then can use the **calibration array** input of the RT Timestamp Analysis VI to remove the overhead from the timestamp values. The RT Timestamp Analysis VI subtracts the mean value of the **calibration array** from all timestamps provided in **timestamp array** to calculate the actual execution times for the code that you benchmark.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\RT Benchmarking\Benchmark Project.lvproj

Parent topic:

RT Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-acknowledge-vi.html language=enus -->
## TOPIC 00096: Watchdog Acknowledge

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-acknowledge-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-acknowledge-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the watchdog counter to the specified count, but does not start the countdown if the counter has not yet started or has expired. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that

### Watchdog Acknowledge

Resets the [watchdog counter](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to the specified count, but does not start the countdown if the counter has not yet started or has expired.

[IMAGE alt='icon' src='watchdog-acknowledge-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. watchdog status — watchdog status is the current status of the watchdog timer. The watchdog status output can return the following values: 0Indicates that the watchdog object has expired. 0Indicates that the watchdog object is disabled. 0Indicates that the watchdog object is running normally. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Indicates that the watchdog object has expired. |
| 0 | Indicates that the watchdog object is disabled. |
| 0 | Indicates that the watchdog object is running normally. |

If the watchdog object is running, this VI restarts the countdown. If the watchdog object is expired, you must either use the Watchdog Configure VI to create a new watchdog object or use the Watchdog Start VI to restart the countdown of the watchdog timer. If the watchdog object is disabled, you must use either the Watchdog Whack VI or the Watchdog Enable VI to enable the watchdog object and start the countdown of the watchdog timer.

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-interrupt-action-vi.html language=enus -->
## TOPIC 00097: Watchdog Add Interrupt Action

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-interrupt-action-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-interrupt-action-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the watchdog object to trigger an occurrence when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cocrn.png Occurrence RefNum Occur

### Watchdog Add Interrupt Action

Configures the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to trigger an occurrence when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.

[IMAGE alt='icon' src='watchdog-add-interrupt-action-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. Occurrence RefNum — Occurrence RefNum specifies the occurrence to trigger when the watchdog timer expires. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-reset-action-vi.html language=enus -->
## TOPIC 00098: Watchdog Add Reset Action

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-reset-action-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-reset-action-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the watchdog object to reset the controller when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no erro

### Watchdog Add Reset Action

Configures the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to reset the controller when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.

[IMAGE alt='icon' src='watchdog-add-reset-action-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-restart-rte-action-vi.html language=enus -->
## TOPIC 00099: Watchdog Add Restart RTE Action

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-restart-rte-action-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-restart-rte-action-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the watchdog object to restart only the LabVIEW Run-Time Engine when the watchdog timer expires, without resetting the FPGA application or losing network connection. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI. icon Inputs/Outputs cu64.png wa

### Watchdog Add Restart RTE Action

Configures the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to restart only the LabVIEW Run-Time Engine when the watchdog timer expires, without resetting the FPGA application or losing network connection. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.

[IMAGE alt='icon' src='watchdog-add-restart-rte-action-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-trigger-action-vi.html language=enus -->
## TOPIC 00100: Watchdog Add Trigger Action

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-trigger-action-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-add-trigger-action-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the watchdog object to assert a PXI trigger line when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cu32.png trigger ID trigger I

### Watchdog Add Trigger Action

Configures the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to assert a PXI trigger line when the watchdog timer expires. Use this VI in the configuration stage of the application, prior to the Watchdog Enable VI.

[IMAGE alt='icon' src='watchdog-add-trigger-action-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. trigger ID — trigger ID specifies the trigger line on the PXI bus to assert when the watchdog timer expires. Refer to the specific RT target hardware documentation for information about supported PXI trigger lines. trigger protocol — trigger protocol is the protocol used for trigger action on the PXI bus when the watchdog timer expires. 0Sets the trigger action to be active when the line is high. 0Sets the trigger action to be active when the line is low. 0Sets the trigger action to operate as an open collector output. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Sets the trigger action to be active when the line is high. |
| 0 | Sets the trigger action to be active when the line is low. |
| 0 | Sets the trigger action to operate as an open collector output. |

This VI does not reserve trigger lines nor discriminate between reserved and unreserved trigger lines. If you specify a **trigger ID** corresponding to a trigger line that has been reserved elsewhere, the watchdog object overwrites the existing value on the trigger line when the watchdog timer expires.

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-outputs-vi.html language=enus -->
## TOPIC 00101: Watchdog Clear Outputs

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-outputs-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-outputs-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears any triggers asserted by the watchdog object. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. i

### Watchdog Clear Outputs

Clears any triggers asserted by the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog).

[IMAGE alt='icon' src='watchdog-clear-outputs-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

This VI does not discriminate between reserved and unreserved trigger lines. If you configure the watchdog object with a trigger line that has been reserved elsewhere, this VI clears the existing value on the trigger line.

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-vi.html language=enus -->
## TOPIC 00102: Watchdog Clear

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-clear-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the watchdog hardware and associated attributes and actions to the default power-on state and closes the watchdog object. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur b

### Watchdog Clear

Resets the [watchdog hardware](/csh?context=lvrt_lvrtconcepts_rt_watchdog) and associated attributes and actions to the default power-on state and closes the watchdog object.

[IMAGE alt='icon' src='watchdog-clear-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\NI Watchdog\Watchdog - RT Engine.lvproj

Parent topic:

RT Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-close-vi.html language=enus -->
## TOPIC 00103: Watchdog Close

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-close-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-close-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes the watchdog session associated with the watchdog object you specify. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard e

### Watchdog Close

Closes the watchdog session associated with the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) you specify.

[IMAGE alt='icon' src='watchdog-close-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-configure-vi.html language=enus -->
## TOPIC 00104: Watchdog Configure

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-configure-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-configure-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a new watchdog object with a timeout and expiration actions. Configuring a watchdog object does not start the watchdog counter. Use the Watchdog Start VI or the Watchdog Whack VI to start the watchdog counter. icon Inputs/Outputs cdbl.png timeout (1 sec) timeout specifies the time, in sec

### Watchdog Configure

Configures a new [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) with a **timeout** and **expiration actions**.

Note

Watchdog Start

Watchdog Whack

[IMAGE alt='icon' src='watchdog-configure-vi.png']

#### Inputs/Outputs

| timeout (1 sec) — timeout specifies the time, in seconds, that the function waits before the watchdog timer expires. The timeout period is coerced to a value determined from the available timebase and initial count values. The default is 1 second. expiration actions — expiration actions specifies which actions to take when the watchdog timer expires. You can use any combination of actions. However, not all targets support all actions. Refer to the specific RT target hardware documentation for information about supported actions. reset system — reset system reboots the PXI controller. restart LabVIEW Runtime — restart LabVIEW Runtime restarts only the LabVIEW Real-Time Runtime. When restart LabVIEW Runtime is TRUE, NI recommends that you avoid running timed structures or time-critical VIs on CPU 0. Otherwise, if a LabVIEW application hangs, the watchdog timer may not restart the LabVIEW Run-Time Engine in a timely manner. Refer to Configuring Settings of a Timed Structure for more information about assigning a processor to a timed structure. occurrence — occurrence sets the occurrence when the watchdog timer expires. trigger protocol — trigger protocol is the protocol used for trigger action on the PXI bus when the watchdog timer expires. 0Sets the trigger action to be active when the line is high. 0Sets the trigger action to be active when the line is low. 0Sets the trigger action to operate as an open collector output. trigger line — trigger line is the trigger line on the PXI bus to be asserted when the watchdog timer expires. Refer to the specific RT target hardware documentation for information about supported trigger lines. disable watchdog on VI exit — disable watchdog on VI exit specifies whether this VI disables the watchdog object when the VI stops running. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID — watchdogID identifies the watchdog object. timeout value returned (sec) — timeout value returned specifies the time, in seconds, for the watchdog timer. The timeout period specifies the amount of time that must elapse before the watchdog timer expires. The timeout period is coerced to a value determined from the available timebase and initial count values. The default is 1. occurrence — occurrence is the occurrence associated with the interrupt action that asserts when the watchdog timer expires. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| reset system — reset system reboots the PXI controller. restart LabVIEW Runtime — restart LabVIEW Runtime restarts only the LabVIEW Real-Time Runtime. When restart LabVIEW Runtime is TRUE, NI recommends that you avoid running timed structures or time-critical VIs on CPU 0. Otherwise, if a LabVIEW application hangs, the watchdog timer may not restart the LabVIEW Run-Time Engine in a timely manner. Refer to Configuring Settings of a Timed Structure for more information about assigning a processor to a timed structure. occurrence — occurrence sets the occurrence when the watchdog timer expires. trigger protocol — trigger protocol is the protocol used for trigger action on the PXI bus when the watchdog timer expires. 0Sets the trigger action to be active when the line is high. 0Sets the trigger action to be active when the line is low. 0Sets the trigger action to operate as an open collector output. trigger line — trigger line is the trigger line on the PXI bus to be asserted when the watchdog timer expires. Refer to the specific RT target hardware documentation for information about supported trigger lines. disable watchdog on VI exit — disable watchdog on VI exit specifies whether this VI disables the watchdog object when the VI stops running. |  |
| 0 | Sets the trigger action to be active when the line is high. |
| 0 | Sets the trigger action to be active when the line is low. |
| 0 | Sets the trigger action to operate as an open collector output. |

Supported **timeout** values vary by target. This VI coerces **timeout** up to the next supported value and returns the actual value as **timeout value returned (sec)**. The value of **timeout value returned (sec)** is always greater than or equal to the **timeout** value you specify. The **occurrence** output of this VI returns a reference to the **occurrence** action you specify using the **expiration actions** input.

This VI does not reserve trigger lines, nor does it discriminate between reserved and unreserved trigger lines. If you specify a trigger line that has been reserved elsewhere, the watchdog object overwrites the existing value on the trigger line when the timer expires.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\NI Watchdog\Watchdog - RT Engine.lvproj

Parent topic:

RT Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-disable-vi.html language=enus -->
## TOPIC 00105: Watchdog Disable

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-disable-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-disable-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the watchdog object you specify and clears any triggers asserted by the watchdog object. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This inpu

### Watchdog Disable

Disables the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) you specify and clears any triggers asserted by the watchdog object.

[IMAGE alt='icon' src='watchdog-disable-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

This VI does not discriminate between reserved and unreserved trigger lines. If you configure the watchdog object with a trigger line that has been reserved elsewhere, this VI clears the existing value on the trigger line.

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-enable-vi.html language=enus -->
## TOPIC 00106: Watchdog Enable

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-enable-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-enable-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the watchdog object and starts the countdown of the watchdog timer if the current status of the watchdog object is disabled. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occ

### Watchdog Enable

Enables the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) and starts the countdown of the watchdog timer if the current status of the watchdog object is **disabled**.

[IMAGE alt='icon' src='watchdog-enable-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-get-attribute-vi.html language=enus -->
## TOPIC 00107: Watchdog Get Attribute

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-get-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-get-attribute-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current value of the watchdog attribute you specify. icon Inputs/Outputs cenum.png attribute attribute specifies the watchdog timer attribute to read. The following are valid attributes: 0Currently not supported on any targets. 0Currently not supported on any targets. 0Returns a Boolean

### Watchdog Get Attribute

Returns the current value of the watchdog attribute you specify.

[IMAGE alt='icon' src='watchdog-get-attribute-vi.png']

#### Inputs/Outputs

| attribute — attribute specifies the watchdog timer attribute to read. The following are valid attributes: 0Currently not supported on any targets. 0Currently not supported on any targets. 0Returns a Boolean value specifying whether the watchdog hardware configuration has been completed and locked. 0Returns the Hardware ID number of the watchdog hardware. 0Returns the current value of the watchdog timer. This attribute is not supported on PXI targets. 0Returns the instance number of the watchdog object you specify using the watchdogID in parameter. 0Returns the rate at which the counter decrements. 0Returns the starting value of the counter before the countdown begins. 0Returns the total timeout value (TotalTimeout = InitialCount value * TimeStep value) 0Returns the trigger line configured as the input for the watchdog hardware. watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. attribute value returned — attribute value returned is the value of the specified attribute. This value is undefined if the RT target does not support the attribute you specify. This parameter specifies time values in microseconds. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Currently not supported on any targets. |
| 0 | Currently not supported on any targets. |
| 0 | Returns a Boolean value specifying whether the watchdog hardware configuration has been completed and locked. |
| 0 | Returns the Hardware ID number of the watchdog hardware. |
| 0 | Returns the current value of the watchdog timer. This attribute is not supported on PXI targets. |
| 0 | Returns the instance number of the watchdog object you specify using the watchdogID in parameter. |
| 0 | Returns the rate at which the counter decrements. |
| 0 | Returns the starting value of the counter before the countdown begins. |
| 0 | Returns the total timeout value (TotalTimeout = InitialCount value * TimeStep value) |
| 0 | Returns the trigger line configured as the input for the watchdog hardware. |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-open-vi.html language=enus -->
## TOPIC 00108: Watchdog Open

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-open-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-open-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a watchdog session using the first available watchdog object. icon Inputs/Outputs cbool.png disable watchdog on VI exit (T) disable watchdog on VI exit specifies whether this VI disables the watchdog object when the VI stops running. cerrcodeclst.png error in (no error) error in describes erro

### Watchdog Open

Opens a watchdog session using the first available [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog).

[IMAGE alt='icon' src='watchdog-open-vi.png']

#### Inputs/Outputs

| disable watchdog on VI exit (T) — disable watchdog on VI exit specifies whether this VI disables the watchdog object when the VI stops running. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID — watchdogID identifies the watchdog object. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-reset-vi.html language=enus -->
## TOPIC 00109: Watchdog Reset

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-reset-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the watchdog hardware and associated attributes and actions to the default power-on state. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This inpu

### Watchdog Reset

Resets the [watchdog hardware](/csh?context=lvrt_lvrtconcepts_rt_watchdog) and associated attributes and actions to the default power-on state.

[IMAGE alt='icon' src='watchdog-reset-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-set-attribute-vi.html language=enus -->
## TOPIC 00110: Watchdog Set Attribute

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-set-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-set-attribute-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the watchdog object attribute you specify to the value you specify. This VI coerces the attribute value you specify to the nearest value supported by the watchdog hardware. You can use the attribute value returned indicator to determine the actual attribute value that the VI sets. Refer to the

### Watchdog Set Attribute

Sets the [watchdog object](/csh?context=lvrt_lvrtconcepts_rt_watchdog) attribute you specify to the value you specify.

This VI coerces the **attribute** value you specify to the nearest value supported by the watchdog hardware. You can use the **attribute value returned** indicator to determine the actual **attribute** value that the VI sets. Refer to the specific RT target hardware documentation for information about supported **attribute** values.

[IMAGE alt='icon' src='watchdog-set-attribute-vi.png']

#### Inputs/Outputs

| attribute — attribute is the watchdog timer attribute to write. The following are valid attributes: 0(Read-only) Returns the current value of the watchdog timer. This attribute is not supported on PXI targets. 0(Read-only) Returns the hardware ID number of the watchdog hardware. 0(Read-only) Returns the instance number of the watchdog object you specify using the watchdogID in parameter. 0Currently not supported on any targets. 0Currently not supported on any targets. 0Sets a Boolean value specifying whether the watchdog hardware configuration has been completed and locked. 0Sets the rate at which the counter decrements. 0Sets the starting value of the counter before the countdown begins. 0Sets the total timeout value (TotalTimeout = InitialCount value * TimeStep value) 0Sets the trigger line configured as the input for the watchdog hardware. watchdogID in — watchdogID in specifies a watchdog object. attribute value — attribute value is the value to which the specified attribute is set. Time values are specified in microseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. attribute value returned — attribute value returned is the value of the specified attribute. This value is undefined if the RT target does not support the attribute you specify. This parameter specifies time values in microseconds. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | (Read-only) Returns the current value of the watchdog timer. This attribute is not supported on PXI targets. |
| 0 | (Read-only) Returns the hardware ID number of the watchdog hardware. |
| 0 | (Read-only) Returns the instance number of the watchdog object you specify using the watchdogID in parameter. |
| 0 | Currently not supported on any targets. |
| 0 | Currently not supported on any targets. |
| 0 | Sets a Boolean value specifying whether the watchdog hardware configuration has been completed and locked. |
| 0 | Sets the rate at which the counter decrements. |
| 0 | Sets the starting value of the counter before the countdown begins. |
| 0 | Sets the total timeout value (TotalTimeout = InitialCount value * TimeStep value) |
| 0 | Sets the trigger line configured as the input for the watchdog hardware. |

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-start-vi.html language=enus -->
## TOPIC 00111: Watchdog Start

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-start-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-start-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restarts the countdown of the watchdog timer if the watchdog object is running or expired. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provi

### Watchdog Start

Restarts the countdown of the [watchdog timer](/csh?context=lvrt_lvrtconcepts_rt_watchdog) if the watchdog object is running or expired.

[IMAGE alt='icon' src='watchdog-start-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

If the watchdog object is disabled, you must use either the Watchdog Whack VI or the Watchdog Enable VI to enable the watchdog object and start the countdown of the watchdog timer.

Parent topic:

Advanced Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-whack-vi.html language=enus -->
## TOPIC 00112: Watchdog Whack

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-whack-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/rtwatchdog-llb/watchdog-whack-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the watchdog counter to the value you specify using either the Watchdog Configure VI or the Watchdog Set Attribute VI. icon Inputs/Outputs cu64.png watchdogID in watchdogID in specifies a watchdog object. cbool.png reset watchdog after expire? (F) reset watchdog after expire? determines wheth

### Watchdog Whack

Resets the [watchdog counter](/csh?context=lvrt_lvrtconcepts_rt_watchdog) to the value you specify using either the Watchdog Configure VI or the Watchdog Set Attribute VI.

[IMAGE alt='icon' src='watchdog-whack-vi.png']

#### Inputs/Outputs

| watchdogID in — watchdogID in specifies a watchdog object. reset watchdog after expire? (F) — reset watchdog after expire? determines whether a whack after the watchdog timer has expired resets the watchdog timer. The default value is FALSE, which specifies that the watchdog timer remains expired after the first expiration. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. watchdogID out — watchdogID out has the same value as watchdogID in. watchdog status — watchdog status is the current status of the watchdog timer. The watchdog status output can return the following values: 0Indicates that the watchdog object has expired. 0Indicates that the watchdog object is disabled. 0Indicates that the watchdog object is running normally. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Indicates that the watchdog object has expired. |
| 0 | Indicates that the watchdog object is disabled. |
| 0 | Indicates that the watchdog object is running normally. |

If the countdown of the watchdog timer has not yet started, this VI starts the countdown. If the watchdog object is running or disabled, this VI restarts the countdown of the watchdog timer. If the watchdog object is expired, this VI restarts the countdown of the watchdog timer only if you set **reset watchdog after expire?** to TRUE.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Real-Time Module\NI Watchdog\Watchdog - RT Engine.lvproj

Parent topic:

RT Watchdog

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/tracetool-llb/tracetool-load-trace-and-send-vi.html language=enus -->
## TOPIC 00113: TraceTool Load Trace and Send

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/tracetool-llb/tracetool-load-trace-and-send-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/tracetool-llb/tracetool-load-trace-and-send-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer. This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing palette instead. Use th

### TraceTool Load Trace and Send

**This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead.**

Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer.

Caution

Use the [TraceTool Stop Trace and Save](/csh?context=lvrt_lvtrace_tt_stop_traceandsavec) VI to save a trace session to file on the RT target.

[IMAGE alt='icon' src='tracetool-load-trace-and-send-vi.png']

#### Inputs/Outputs

| Path to Trace Log — Path to Trace Log specifies the path to the trace session file on the RT target. Trace Host Network Address — Trace Host Network Address is the IP address of the host computer where you want to send the trace session. The Real-Time Trace Viewer must be running on the host computer to receive the trace session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\tracetool\Parallel Execution.lvproj

Parent topic:

RT Execution Trace Tool

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/tracetool-llb/tracetool-log-user-event-vi.html language=enus -->
## TOPIC 00114: TraceTool Log User Event

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/tracetool-llb/tracetool-log-user-event-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/tracetool-llb/tracetool-log-user-event-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Logs a user-defined event in the trace session. This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing palette instead. Use the Flag Configuration dialog box in the Real-Time Trace Viewer to co

### TraceTool Log User Event

**This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead.**

Logs a [user-defined event](/csh?context=lvrt_lvtracehelp_log_view_custom_events) in the trace session.

Caution

Use the [Flag Configuration](/csh?context=lvrt_lvtracehelp_flag_config_dialog) dialog box in the Real-Time Trace Viewer to [configure](/csh?context=lvrt_lvtracehelp_creating_custom_events) user event flags.

[IMAGE alt='icon' src='tracetool-log-user-event-vi.png']

#### Inputs/Outputs

| Event ID (0-255) — Event ID is the event code (0–255) you assign to the custom event flag. Use the Flag Configuration dialog box of the Real-Time Trace Viewer to configure user event flags. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\tracetool\User Events.lvproj

Parent topic:

RT Execution Trace Tool

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/tracetool-llb/tracetool-start-trace-vi.html language=enus -->
## TOPIC 00115: TraceTool Start Trace

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/tracetool-llb/tracetool-start-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/tracetool-llb/tracetool-start-trace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace VI executes. You must ensure that you wire the TraceTool Start Trace VI in sequence with a

### TraceTool Start Trace

**This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead.**

Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace VI executes. You must ensure that you wire the TraceTool Start Trace VI in sequence with all of the VIs that you want to log.

Caution

[IMAGE alt='icon' src='tracetool-start-trace-vi.png']

#### Inputs/Outputs

| Detailed Tracing? (F) — Detailed Tracing? enables logging of analysis and custom events in the trace session. You must set the Detailed Tracing? input to TRUE to log analysis and custom events. The default is FALSE. Buffer Size (250000 bytes) — Buffer Size is the size of the memory buffer that logs all events from VIs in memory on the RT target. You must create an appropriately-sized memory buffer to capture all event data. If you exceed the memory buffer size, any subsequent data that you log overwrites the oldest data in the buffer. You cannot change the size of the memory buffer on the RT target after you run the TraceTool Start Trace VI. You must reboot the RT target to resize the memory buffer. Thread Tracing? (T) — Thread Tracing? enables the logging of thread event data from the application running on the RT target. The default is TRUE. VI Tracing? (T) — VI Tracing? enables the logging of VI event data from the application running on the RT target. The default is TRUE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Actual Buffer Size — Actual Buffer Size returns the actual size of the memory buffer allocated for event logging if the real-time operating system cannot allocate the requested Buffer Size. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\tracetool\Parallel Execution.lvproj

Parent topic:

RT Execution Trace Tool

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-save-vi.html language=enus -->
## TOPIC 00116: TraceTool Stop Trace and Save

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-save-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-save-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Stops logging event data from the application and saves the trace session to file on the RT target. This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing palette instead. Use the TraceTool Loa

### TraceTool Stop Trace and Save

**This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead.**

Stops logging event data from the application and saves the trace session to file on the RT target.

Caution

Use the [TraceTool Load Trace and Send](/csh?context=lvrt_lvtrace_tt_load_traceandsendc) VI to transfer the trace session file to the host computer.

[IMAGE alt='icon' src='tracetool-stop-trace-and-save-vi.png']

#### Inputs/Outputs

| Path to Trace Log — Path to Trace Log specifies the path to the trace session file on the RT target. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\tracetool\Parallel Execution.lvproj

Parent topic:

RT Execution Trace Tool

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-send-vi.html language=enus -->
## TOPIC 00117: TraceTool Stop Trace And Send

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-send-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/tracetool-llb/tracetool-stop-trace-and-send-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead. Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer. This VI is deprecated in LabVIEW 2026Q1. See the VIs in

### TraceTool Stop Trace And Send

**This VI is deprecated in LabVIEW 2026Q1. See the VIs in the RT Tracing subpalette instead.**

Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer.

Caution

[IMAGE alt='icon' src='tracetool-stop-trace-and-send-vi.png']

#### Inputs/Outputs

| Trace Host Network Address — Trace Host Network Address is the IP address of the host computer where you want to send the trace session. The Real-Time Trace Viewer must be running on the host computer to receive the trace session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

This function has a timeout of 60 seconds.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\tracetool\Parallel Execution.lvproj

Parent topic:

RT Execution Trace Tool

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/utility/rt-get-cpu-loads-vi.html language=enus -->
## TOPIC 00118: RT Get CPU Loads

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/utility/rt-get-cpu-loads-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/utility/rt-get-cpu-loads-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this VI returns the total load as a percentage of capacity. This VI also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time devoted

### RT Get CPU Loads

Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this VI returns the total load as a percentage of capacity. This VI also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time devoted to Timed Structures and interrupt service routines (ISRs).

[IMAGE alt='icon' src='rt-get-cpu-loads-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. CPU loads — CPU loads returns data corresponding to the distribution of load for each CPU in the system. The Nth element of this array corresponds to the Nth CPU in the system. CPU numbering begins at zero. LabVIEW 2026Q1 and later: On Linux RT targets, the per-CPU load of Timed Structures may be averaged between all CPUs present in the Timed Structures pool. Total Load (%) — Total (%)—Returns the total CPU usage as a percentage of capacity. ISR Load (%) — Time Critical (%)—Returns the CPU usage devoted to time-critical threads as a percentage of total CPU capacity. Timed Structure Load (%) — Timed Structures (%)—Returns the CPU usage devoted to timed structures as a percentage of total CPU capacity. Other Thread Load (%) — High (%)—Returns the CPU usage devoted to high priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Above Normal (%)—Returns the CPU usage devoted to above normal priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Normal (%)—Returns the CPU usage devoted to normal priority threads as a percentage of total CPU capacity. Total Load (%) — Background (%)—Returns the CPU usage devoted to background priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Idle (%)—Returns the amount of idle CPU time as a percentage of total CPU capacity. Total Load (%) — ISR (%)—Returns the CPU usage devoted to interrupt service routines (ISRs) as a percentage of total CPU capacity. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Total Load (%) — Total (%)—Returns the total CPU usage as a percentage of capacity. ISR Load (%) — Time Critical (%)—Returns the CPU usage devoted to time-critical threads as a percentage of total CPU capacity. Timed Structure Load (%) — Timed Structures (%)—Returns the CPU usage devoted to timed structures as a percentage of total CPU capacity. Other Thread Load (%) — High (%)—Returns the CPU usage devoted to high priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Above Normal (%)—Returns the CPU usage devoted to above normal priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Normal (%)—Returns the CPU usage devoted to normal priority threads as a percentage of total CPU capacity. Total Load (%) — Background (%)—Returns the CPU usage devoted to background priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0. Total Load (%) — Idle (%)—Returns the amount of idle CPU time as a percentage of total CPU capacity. Total Load (%) — ISR (%)—Returns the CPU usage devoted to interrupt service routines (ISRs) as a percentage of total CPU capacity. |

Parent topic:

RT Utilities

Parent topic:

RT SMP CPU Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/utility/rt-get-number-of-cpus-vi.html language=enus -->
## TOPIC 00119: RT Get Number of CPUs

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/utility/rt-get-number-of-cpus-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/utility/rt-get-number-of-cpus-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the number of CPUs in the system. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. iu32.png # of CPUs # of CPUs returns the number of CPUs in the system. ierrcodec

### RT Get Number of CPUs

Reads the number of CPUs in the system.

[IMAGE alt='icon' src='rt-get-number-of-cpus-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. # of CPUs — # of CPUs returns the number of CPUs in the system. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RT SMP CPU Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-assignments-vi.html language=enus -->
## TOPIC 00120: RT Set CPU Pool Assignments

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-assignments-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-assignments-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Assigns CPUs to pools for automatic load balancing. This VI assigns CPUs to one of four possible states: System pool only, Timed Structures pool only, both pools, or no pool (reserved). This VI outputs the bit masks that specify the CPUs assigned to each pool. icon Inputs/Outputs c1denum.png CPU poo

### RT Set CPU Pool Assignments

Assigns CPUs to pools for [automatic load balancing](/csh?context=lvrt_lvrtconcepts_smp_api). This VI assigns CPUs to one of four possible states: System pool only, Timed Structures pool only, both pools, or no pool (reserved). This VI outputs the bit masks that specify the CPUs assigned to each pool.

[IMAGE alt='icon' src='rt-set-cpu-pool-assignments-vi.png']

#### Inputs/Outputs

| CPU pools — CPU pools specifies the pool assignments of each CPU in the system. This input is an array of enums. The enum contains the four possible states of a CPU and each element of the array represents a CPU. The array indices 0 - N correspond directly to the CPU indices 0 - N. 0Reserved—Assigns the CPU to neither pool. The CPU is reserved for Timed Structures configured for manual processor assignment. 1System & Timed Structures—Assigns the CPU to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. 2System—Assigns the CPU to the System pool for automatic load balancing of non-timed-structure threads. 3Timed Structures—Assigns the CPU to the Timed Structures pool for automatic load balancing of timed structure threads. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. assigned CPU pools — assigned CPU pools returns the CPU pool assignments. 0Reserved—The CPU is not assigned to a pool. The CPU is reserved for Timed Structures configured for manual processor assignment. 1System & Timed Structures—The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. 2System—The CPU is assigned to the System pool for automatic load balancing of non-timed-structure threads. 3Timed Structures—The CPU is assigned to the Timed Structures pool for automatic load balancing of timed structure threads. system mask — system mask returns a bit mask corresponding to System pool assignments. timed structures mask — timed structures mask returns a bit mask corresponding to the Timed Structures pool assignments. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Reserved—Assigns the CPU to neither pool. The CPU is reserved for Timed Structures configured for manual processor assignment. |
| 1 | System & Timed Structures—Assigns the CPU to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| 2 | System—Assigns the CPU to the System pool for automatic load balancing of non-timed-structure threads. |
| 3 | Timed Structures—Assigns the CPU to the Timed Structures pool for automatic load balancing of timed structure threads. |
| 0 | Reserved—The CPU is not assigned to a pool. The CPU is reserved for Timed Structures configured for manual processor assignment. |
| 1 | System & Timed Structures—The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| 2 | System—The CPU is assigned to the System pool for automatic load balancing of non-timed-structure threads. |
| 3 | Timed Structures—The CPU is assigned to the Timed Structures pool for automatic load balancing of timed structure threads. |

On an N-CPU system, the bits of the bit mask correspond to CPUs 0 through N-1. The right-most bit of each bit mask corresponds to CPU 0 and the left-most bit corresponds to CPU 31, if such a CPU exists in the system.

Refer to the [Specifying the Set of CPUs Available for Automatic Load Balancing](/csh?context=lvrt_lvrtconcepts_smp_api) topic for more information about CPU pools.

Parent topic:

RT SMP CPU Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-sizes-vi.html language=enus -->
## TOPIC 00121: RT Set CPU Pool Sizes

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-sizes-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-sizes-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of CPUs in the CPU pools available for automatic load balancing. You can use this VI to define the System pool and the Timed Structures pool by specifying the number of CPUs you want each pool to contain. You cannot use this VI to create empty pools or partially overlapping pools. Th

### RT Set CPU Pool Sizes

Sets the number of CPUs in the [CPU pools](/csh?context=lvrt_lvrtconcepts_smp_api) available for automatic load balancing. You can use this VI to define the System pool and the Timed Structures pool by specifying the number of CPUs you want each pool to contain.

Note

0

[IMAGE alt='icon' src='rt-set-cpu-pool-sizes-vi.png']

#### Inputs/Outputs

| system pool (-1) — system pool specifies the number of CPUs to assign to the System pool. timed structures pool (-1) — timed structures pool specifies the number of CPUs to assign to the Timed Structures pool. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. assigned CPU pools — assigned CPU pools returns the CPU pool assignments. 0Reserved—The CPU is not assigned to a pool. The CPU is reserved for Timed Structures configured for manual processor assignment. 1System & Timed Structures—The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. 2System—The CPU is assigned to the System pool for automatic load balancing of non-timed-structure threads. 3Timed Structures—The CPU is assigned to the Timed Structures pool for automatic load balancing of timed structure threads. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Reserved—The CPU is not assigned to a pool. The CPU is reserved for Timed Structures configured for manual processor assignment. |
| 1 | System & Timed Structures—The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| 2 | System—The CPU is assigned to the System pool for automatic load balancing of non-timed-structure threads. |
| 3 | Timed Structures—The CPU is assigned to the Timed Structures pool for automatic load balancing of timed structure threads. |

This VI creates the System and Timed Structures pools as adjacent pools of contiguous CPUs. The System pool begins at CPU 0 and the Timed Structures pool begins where the System pool ends. For example, on an eight-CPU system, if you wire a value of 3 to both the **system pool** and **timed structures pool** controls, this VI assigns CPUs 0-2 to the System pool, CPUs 3-5 to the Timed Structures Pool, and leaves CPUs 6-7 reserved for use by Timed Structures configured for manual CPU assignment.

The default pool size of -1 sets the size of the pool automatically. If you specify a value of -1 for both pools, this VI creates the default pool configuration in which both pools contain every CPU in the system. If you specify a size of -1 for only one pool, this VI assigns all remaining CPUs to that pool.

Refer to the [Specifying the Set of CPUs Available for Automatic Load Balancing](/csh?context=lvrt_lvrtconcepts_smp_api) topic for more information about CPU pools.

Parent topic:

RT SMP CPU Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-vi.html language=enus -->
## TOPIC 00122: RT Set CPU Pool

- bundle_id: `lvrt-api-ref`
- source_path: `targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/targets/ni/rt/vi-lib/utility/rt-set-cpu-pool-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of CPUs included in the System pool or the Timed Structures pool for automatic load balancing. This VI is used as a building block for the higher-level SMP CPU Utilities VIs. icon Inputs/Outputs cenum.png pool pool specifies whether to set the System pool or the Timed Structures po

### RT Set CPU Pool

Specifies the set of CPUs included in the System pool or the Timed Structures pool for [automatic load balancing](/csh?context=lvrt_lvrtconcepts_smp_api).

This VI is used as a building block for the higher-level SMP CPU Utilities VIs.

[IMAGE alt='icon' src='rt-set-cpu-pool-vi.png']

#### Inputs/Outputs

| pool — pool specifies whether to set the System pool or the Timed Structures pool. 0System—Specifies the System pool. 1Timed Structures—Specifies the Timed Structures pool. CPU mask — CPU mask specifies which CPUs to assign to the pool. This input is a bit mask in which the right-most bit corresponds to CPU 0 and the left-most bit corresponds to CPU 31, if such a CPU exists in the system. To include a CPU in the pool, set the value of the corresponding bit to one. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | System—Specifies the System pool. |
| 1 | Timed Structures—Specifies the Timed Structures pool. |

Refer to the [Specifying the Set of CPUs Available for Automatic Load Balancing](/csh?context=lvrt_lvrtconcepts_smp_api) topic for more information about CPU pools.

Parent topic:

RT SMP CPU Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/analysis/aalutilities-llb/disable-analysis-workspace-vi.html language=enus -->
## TOPIC 00123: Disable Analysis Workspace

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/analysis/aalutilities-llb/disable-analysis-workspace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/analysis/aalutilities-llb/disable-analysis-workspace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Full or Professional EditionDisables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Disable Analysis Workspace VI according to a strict set of guidelines. icon Inputs/Outputs cerrcodeclst.png error in (no e

### Disable Analysis Workspace

Requires: Full or Professional Edition

Disables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Disable Analysis Workspace VI according to a strict set of [guidelines](/csh?context=lvrt_lvrtconcepts_createmultithreadapps_lv).

[IMAGE alt='icon' src='disable-analysis-workspace-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Place the Disable Analysis Workspace VI in the highest-priority [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop) or [time-critical VI](/csh?context=lvrt_lvrtconcepts_deterministic_apps_vi_priorities) of the RT application.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Mathematics\RT Utilities\RT Analysis Workspace.lvproj

Parent topic:

Real-Time Analysis Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/analysis/aalutilities-llb/enable-analysis-workspace-vi.html language=enus -->
## TOPIC 00124: Enable Analysis Workspace

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/analysis/aalutilities-llb/enable-analysis-workspace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/analysis/aalutilities-llb/enable-analysis-workspace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Full or Professional EditionEnables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Enable Analysis Workspace VI according to a strict set of guidelines. Enabling the analysis workspace allows Mathematics an

### Enable Analysis Workspace

Requires: Full or Professional Edition

Enables the use of the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Enable Analysis Workspace VI according to a strict set of [guidelines](/csh?context=lvrt_lvrtconcepts_createmultithreadapps_lv).

Enabling the analysis workspace allows Mathematics and Signal Processing VIs to allocate internal buffers from the workspace.

[IMAGE alt='icon' src='enable-analysis-workspace-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Place the Enable Analysis Workspace VI in the highest-priority [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop) or [time-critical VI](/csh?context=lvrt_lvrtconcepts_deterministic_apps_vi_priorities) of the RT application.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Mathematics\RT Utilities\RT Analysis Workspace.lvproj

Parent topic:

Real-Time Analysis Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/analysis/aalutilities-llb/initialize-analysis-workspace-vi.html language=enus -->
## TOPIC 00125: Initialize Analysis Workspace

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/analysis/aalutilities-llb/initialize-analysis-workspace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/analysis/aalutilities-llb/initialize-analysis-workspace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Full or Professional EditionInitializes the analysis workspace on the RT target and sets the workspace size to reserved memory size (KB). To prevent race conditions, priority inversions, and other undefined behavior, you must use the Initialize Analysis Workspace VI according to a strict s

### Initialize Analysis Workspace

Requires: Full or Professional Edition

Initializes the analysis workspace on the RT target and sets the workspace size to **reserved memory size (KB)**. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Initialize Analysis Workspace VI according to a strict set of [guidelines](/csh?context=lvrt_lvrtconcepts_createmultithreadapps_lv).

Initializing the analysis workspace preallocates resources for use by the Mathematics and Signal Processing VIs.

[IMAGE alt='icon' src='initialize-analysis-workspace-vi.png']

#### Inputs/Outputs

| reserved memory size (KB) — reserved memory size (KB) specifies the size of the analysis workspace on the RT target. The value of this parameter must be greater than zero and less than 2097152 (2 GB). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Because Initialize Analysis Workspace makes resource requests to the OS, do not place Initialize Analysis Workspace in a [time-critical VI](/csh?context=lvrt_lvrtconcepts_deterministic_apps_vi_priorities) or in a high-priority [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop). Use the Initialize Analysis Workspace VI prior to the [Enable Analysis Workspace](enable-analysis-workspace-vi.html) VI.

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Mathematics\RT Utilities\RT Analysis Workspace.lvproj

Parent topic:

Real-Time Analysis Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/analysis/aalutilities-llb/uninitialize-analysis-workspace-vi.html language=enus -->
## TOPIC 00126: Uninitialize Analysis Workspace

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/analysis/aalutilities-llb/uninitialize-analysis-workspace-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/analysis/aalutilities-llb/uninitialize-analysis-workspace-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: Full or Professional EditionReleases all resources used by the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Uninitialize Analysis Workspace VI according to a strict set of guidelines. icon Inputs/Outputs cerrcodeclst.pn

### Uninitialize Analysis Workspace

Requires: Full or Professional Edition

Releases all resources used by the analysis workspace. To prevent race conditions, priority inversions, and other undefined behavior, you must use the Uninitialize Analysis Workspace VI according to a strict set of [guidelines](/csh?context=lvrt_lvrtconcepts_createmultithreadapps_lv).

[IMAGE alt='icon' src='uninitialize-analysis-workspace-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Because the Uninitialize Analysis Workspace VI makes resource allocation requests to the OS, do not place the Uninitialize Analysis Workspace VI in a [time-critical VI](/csh?context=lvrt_lvrtconcepts_deterministic_apps_vi_priorities) or in a high-priority [Timed Loop](/csh?productcategories=147794&context=lvcore_glang_timed_loop).

#### Examples

Refer to the following example files included with LabVIEW Real-Time Module.

- labview\examples\Mathematics\RT Utilities\RT Analysis Workspace.lvproj

Parent topic:

Real-Time Analysis Utilities

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/express/rvi/timing/nirviwaituntilnextmultiple-vi.html language=enus -->
## TOPIC 00127: Wait Until Next Multiple

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/express/rvi/timing/nirviwaituntilnextmultiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/express/rvi/timing/nirviwaituntilnextmultiple-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the value of the timer becomes a multiple of Count. Use this function to synchronize activities. You can call this function in a loop to control the loop execution rate. When the Wait Until Next Multiple VI executes, it sleeps and blocks the execution of the thread of the calling VI. Any

### Wait Until Next Multiple

Waits until the value of the timer becomes a multiple of **Count**. Use this function to synchronize activities. You can call this function in a loop to control the loop execution rate.

Note

[IMAGE alt='icon' src='nirviwaituntilnextmultiple-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Counter Units | Unit of time the VI uses for the counter. Ticks—(FPGA and RT Module) Sets the counter units to a single clock cycle, the length of which is determined by the clock rate for which the VI is compiled. µSec—(FPGA and RT Module) Sets the counter units to microseconds. mSec—Sets the counter units to milliseconds. Note (Windows) The Windows operating system supports only millisecond resolution. If you select a µSec or Tick resolution under Windows, the VI does not provide exact timing and instead provides an approximation that averages to the requested time over the course of the timing interval. Windows does not support resolutions under one millisecond and rounds them up to one millisecond. Ticks—Sets the counter units to a single clock cycle, the length of which is determined by the clock rate for which the VI is compiled. µSec—Sets the counter units to microseconds. mSec—Sets the counter units to milliseconds. |
| Size of Internal Counter | The maximum time the timer can track. |

#### Inputs/Outputs

| Count(Ticks) — Specifies the time between loop iterations. Tick Count(Ticks) — Returns the value of the free running counter at the time the VI wakes up. The free running counter rolls over when the counter reaches the maximum of Size of Internal Counter specified in the Configure Wait Until Next Multiple dialog box. |
| --- |

Parent topic:

RT Timing

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/accumulate/accumulate/merge-accumulate-vi.html language=enus -->
## TOPIC 00128: Accumulate

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/accumulate/accumulate/merge-accumulate-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/accumulate/accumulate/merge-accumulate-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accumulates a point-by-point sum. When enable is TRUE, this function block adds the value of input to the value of accumulation. icon Dialog Box Options Option Description Inputs Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure.

### Accumulate

Accumulates a point-by-point sum. When **enable** is TRUE, this function block adds the value of **input** to the value of **accumulation**.

[IMAGE alt='icon' src='merge-accumulate-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the input signal for the function block to process. reset — Clears all outputs and internal states of the function block. enable — Specifies whether to process input. If enable is TRUE (default), the function block updates output terminals based on the current input. If enable is FALSE, the function block does not process input. error out — error out contains error information. This output provides standard error out functionality. accumulation — Returns the sum of the accumulated input values. |
| --- |

Parent topic:

Accumulate & Collect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/accumulate/collect-boolean-array/merge-collect-boolean-array-vi.html language=enus -->
## TOPIC 00129: Collect Boolean Array

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/accumulate/collect-boolean-array/merge-collect-boolean-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/accumulate/collect-boolean-array/merge-collect-boolean-array-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accumulates Boolean input elements when enable is TRUE. The collected data array contains the collection of input elements. If collected data reaches the capacity you specify using the array size input, the function block discards additional input values until you clear the function block by setting

### Collect Boolean Array

Accumulates Boolean input elements when **enable** is TRUE. The **collected data** array contains the collection of input elements. If **collected data** reaches the capacity you specify using the **array size** input, the function block discards additional **input** values until you clear the function block by setting the **reset** input to TRUE.

[IMAGE alt='icon' src='merge-collect-boolean-array-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. array size — Specifies the size of the collected data array. enable — Specifies whether to process input. If enable is TRUE (default), the function block updates output terminals based on the current input. If enable is FALSE, the function block does not process input. reset — Clears all outputs and internal states of the function block. input — Specifies the data point to add to the collected data array. full — Indicates whether collected data has reached capacity by returning TRUE when points collected is greater than or equal to array size. Returns FALSE otherwise. collected data — collected data is the array that collects the input points. error out — error out contains error information. This output provides standard error out functionality. points collected — Returns the number of data values contained in collected data. |
| --- |

Parent topic:

Accumulate & Collect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/accumulate/collect-numeric-array/merge-collect-numeric-array-vi.html language=enus -->
## TOPIC 00130: Collect Numeric Array

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/accumulate/collect-numeric-array/merge-collect-numeric-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/accumulate/collect-numeric-array/merge-collect-numeric-array-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accumulates numeric input elements when enable is TRUE. The collected data array contains the collection of input elements. If collected data reaches the capacity you specify using the array size input, the function block discards additional input values until you clear the function block by setting

### Collect Numeric Array

Accumulates numeric input elements when **enable** is TRUE. The **collected data** array contains the collection of input elements. If **collected data** reaches the capacity you specify using the **array size** input, the function block discards additional **input** values until you clear the function block by setting the **reset** input to TRUE.

[IMAGE alt='icon' src='merge-collect-numeric-array-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. array size — Specifies the size of the collected data array. enable — Specifies whether to process input. If enable is TRUE (default), the function block updates output terminals based on the current input. If enable is FALSE, the function block does not process input. reset — Clears all outputs and internal states of the function block. input — Specifies the input signal for the function block to process. full — Indicates whether collected data has reached capacity by returning TRUE when points collected is greater than or equal to array size. Returns FALSE otherwise. collected data — Returns the array that collects the input data values. error out — error out contains error information. This output provides standard error out functionality. points collected — Returns the number of data values contained in collected data. |
| --- |

Parent topic:

Accumulate & Collect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/accumulate/totalize/merge-totalize-vi.html language=enus -->
## TOPIC 00131: Totalize

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/accumulate/totalize/merge-totalize-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/accumulate/totalize/merge-totalize-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates a trapezoidal Riemann sum to approximate the integral of input. If you apply new values to timebase or gain while the function block runs, the new values do not take effect until you reset the function block. icon Dialog Box Options Option Description Inputs Contains the following configu

### Totalize

Calculates a trapezoidal Riemann sum to approximate the integral of **input**.

If you apply new values to **timebase** or **gain** while the function block runs, the new values do not take effect until you reset the function block.

[IMAGE alt='icon' src='merge-totalize-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. timebase — Specifies the units of the time interval between successive input points. DaysSets the unit of time to days. HoursSets the unit of time to hours. MinutesSets the unit of time to minutes. SecondsSets the unit of time to seconds. input — Specifies the input signal for the function block to process. reset — Clears all outputs and internal states of the function block. enable — Specifies whether to process input. If enable is TRUE (default), the function block updates output terminals based on the current input. If enable is FALSE, the function block does not process input. gain — Specifies the amount of gain to apply. The function block multiplies input by gain when calculating total. error out — error out contains error information. This output provides standard error out functionality. total — Returns the approximate integral of input. |  |
| --- | --- |
| Days | Sets the unit of time to days. |
| Hours | Sets the unit of time to hours. |
| Minutes | Sets the unit of time to minutes. |
| Seconds | Sets the unit of time to seconds. |

Parent topic:

Accumulate & Collect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/bistables/rs-bistable/merge-rs-bistable-vi.html language=enus -->
## TOPIC 00132: RS Bistable

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/bistables/rs-bistable/merge-rs-bistable-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/bistables/rs-bistable/merge-rs-bistable-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a reset-dominant latch, also known as a flip-flop. If output is TRUE, output remains TRUE until the function block receives a reset pulse. If output is FALSE, output remains FALSE until the function block receives a set pulse. If set and reset are both TRUE, output is FALSE. icon Dialog Box

### RS Bistable

Creates a reset-dominant latch, also known as a flip-flop.

If **output** is TRUE, **output** remains TRUE until the function block receives a **reset** pulse. If **output** is FALSE, **output** remains FALSE until the function block receives a **set** pulse. If **set** and **reset** are both TRUE, **output** is FALSE.

[IMAGE alt='icon' src='merge-rs-bistable-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. set — Asserts the set signal. reset — Asserts the reset signal. output — Returns the Boolean value stored in the bistable function block. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Bistable/Flip-Flop

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/bistables/sr-bistable/merge-sr-bistable-vi.html language=enus -->
## TOPIC 00133: SR Bistable

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/bistables/sr-bistable/merge-sr-bistable-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/bistables/sr-bistable/merge-sr-bistable-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a set-dominant latch, also known as a flip-flop. If output is TRUE, output remains TRUE until the function block receives a reset pulse. If output is FALSE, output remains FALSE until the function block receives a set pulse. If set and reset are both TRUE, output is TRUE. icon Dialog Box Opt

### SR Bistable

Creates a set-dominant latch, also known as a flip-flop.

If **output** is TRUE, **output** remains TRUE until the function block receives a **reset** pulse. If **output** is FALSE, **output** remains FALSE until the function block receives a **set** pulse. If **set** and **reset** are both TRUE, **output** is TRUE.

[IMAGE alt='icon' src='merge-sr-bistable-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. set — Asserts the set signal. reset — Asserts the reset signal. output — Returns the Boolean value stored in the bistable function block. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Bistable/Flip-Flop

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/control/pid/merge-pid-vi.html language=enus -->
## TOPIC 00134: PID

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/control/pid/merge-pid-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/control/pid/merge-pid-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: PID algorithm for PID applications or high speed control applications that require an efficient algorithm. The PID algorithm features control output range limiting with integrator anti-windup and bumpless controller output for PID gain changes. This function block also features manual mode control w

### PID

PID algorithm for PID applications or high speed control applications that require an efficient algorithm. The PID algorithm features control output range limiting with integrator anti-windup and bumpless controller output for PID gain changes. This function block also features manual mode control with bumpless manual to automatic transitions, nonlinear integral action, two degree of freedom control, and error-squared control.

You can use this function block to operate on one input value at a time.

[IMAGE alt='icon' src='merge-pid-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. process variable — Specifies the current value of the variable that you are controlling. integral time (Ti, min) — Specifies the PID parameter (Ti) that adjusts the effect of the error integral term on the output. auto? (T) — TRUE selects automatic control (default), FALSE selects manual mode. The function block uses bumpless transfer to transition from manual mode to automatic control. derivative time (Td, min) — Specifies the PID parameter (Td) that adjusts the effect of the error derivative term on the output. setpoint — Specifies the setpoint value of the process variable that you are controlling. This is the desired value for the process variable. proportional gain (Kc) — Specifies the proportional gain (Kc) of the PID algorithm. The default value is 1. output — Returns the control output of the PID algorithm that is applied to the controlled process. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Control

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/count-down/merge-count-down-vi.html language=enus -->
## TOPIC 00135: Count Down

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/count-down/merge-count-down-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/count-down/merge-count-down-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Counts down from the number you specify using the preset value input. The counter value output decrements on each rising edge of the count down input. When counter value reaches zero, done returns TRUE. icon Dialog Box Options Option Description Inputs Contains the following configuration options: T

### Count Down

Counts down from the number you specify using the **preset value** input. The **counter value** output decrements on each rising edge of the **count down** input. When **counter value** reaches zero, **done** returns TRUE.

[IMAGE alt='icon' src='merge-count-down-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. load — Sets counter value to preset value. preset value — Specifies the number to count down from. count down — Specifies whether to decrement counter value. Each rising edge of this input triggers counter value to decrease by one. error out — error out contains error information. This output provides standard error out functionality. done — Indicates when the function block finishes counting down. counter value — Returns the current value of the counter. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_CountDown.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/count-up-down/merge-count-up-down-vi.html language=enus -->
## TOPIC 00136: Count Up Down

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/count-up-down/merge-count-up-down-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/count-up-down/merge-count-up-down-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block. icon Dialog Box Options Option Description Inputs Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whet

### Count Up Down

Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block.

[IMAGE alt='icon' src='merge-count-up-down-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset — Sets counter value to zero. count down — Specifies whether to decrement counter value. Each rising edge of this input triggers counter value to decrease by one. load — Sets counter value to preset value. count up — Specifies whether to increment counter value. Each rising edge of this input triggers counter value to increase by one. preset value — Specifies the number to count up to or down from. error out — error out contains error information. This output provides standard error out functionality. count up done — Indicates when the function block finishes counting up. count down done — Indicates when the function block finishes counting down. counter value — Returns the current value of the counter. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_CountUpDown.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/count-up/merge-count-up-vi.html language=enus -->
## TOPIC 00137: Count Up

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/count-up/merge-count-up-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/count-up/merge-count-up-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Counts up from zero. The counter value output increments on each rising edge of the count up input. The done output returns TRUE when counter value is greater than or equal to preset value. icon Dialog Box Options Option Description Inputs Contains the following configuration options: Terminal name—

### Count Up

Counts up from zero. The **counter value** output increments on each rising edge of the **count up** input. The **done** output returns TRUE when **counter value** is greater than or equal to **preset value**.

[IMAGE alt='icon' src='merge-count-up-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset — Sets counter value to zero. preset value — Specifies the number to count up to. count up — Specifies whether to increment counter value. Each rising edge of this input triggers counter value to increase by one. error out — error out contains error information. This output provides standard error out functionality. done — Indicates when the function block finishes counting up. counter value — Returns the current value of the counter. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_CountUp.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/elapsed-timer/merge-elapsed-timer-vi.html language=enus -->
## TOPIC 00138: Elapsed Timer

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/elapsed-timer/merge-elapsed-timer-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/elapsed-timer/merge-elapsed-timer-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block. If reset mode is TRUE on a reset iteration, elapsed time (ms) returns the time elapsed prior to the reset. Otherwise, elapsed time (ms) returns zero on a reset iteration. icon Dialog Box Options

### Elapsed Timer

Reports the elapsed time, in milliseconds, since the first call or previous reset of the function block.

If **reset mode** is TRUE on a reset iteration, **elapsed time (ms)** returns the time elapsed prior to the reset. Otherwise, **elapsed time (ms)** returns zero on a reset iteration.

[IMAGE alt='icon' src='merge-elapsed-timer-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset — Sets elapsed time to zero. reset mode — Specifies whether to report elapsed time (ms) on reset iterations. When reset mode is TRUE on a reset iteration, elapsed time (ms) returns the time that elapsed prior to the reset. When reset mode is FALSE on a reset iteration, elapsed time (ms) returns zero. elapsed time (ms) — Returns the amount of time, in milliseconds, that has elapsed since the initial call or previous reset of the function block. If you leave the function block running without resetting the timer, the timer restarts at zero after approximately 25 days. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_ElapsedTimer.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/pulse-timer/merge-pulse-timer-vi.html language=enus -->
## TOPIC 00139: Pulse Timer

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/pulse-timer/merge-pulse-timer-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/pulse-timer/merge-pulse-timer-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates output pulses triggered by rising edges on the input signal. When a rising edge occurs on input, output pulses TRUE for preset time (ms). icon Dialog Box Options Option Description Inputs Contains the following configuration options: Terminal name—Contains the name of the block diagram ter

### Pulse Timer

Generates output pulses triggered by rising edges on the **input** signal.

When a rising edge occurs on **input**, **output** pulses TRUE for **preset time (ms)**.

[IMAGE alt='icon' src='merge-pulse-timer-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the digital input signal. preset time (ms) — Specifies the amount of time for the function block to use in calculations. elapsed time (ms) — Returns the amount of time, in milliseconds, elapsed since the start of the current or last pulse. If no pulse has started, this output returns the amount of time elapsed since the first call of the function block. error out — error out contains error information. This output provides standard error out functionality. output — Returns the digital output signal. |
| --- |

This function block does not respond to rising edges on **input** received while **output** is TRUE.

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_PulseTimer.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/retentive-timer-on/merge-retentive-timer-on-vi.html language=enus -->
## TOPIC 00140: Retentive Timer On

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/retentive-timer-on/merge-retentive-timer-on-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/retentive-timer-on/merge-retentive-timer-on-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A timer that counts up to preset time (ms) while enable is TRUE. When enable is FALSE, this function block retains the accumulated time (ms) value. When accumulated time (ms) reaches preset time (ms), done returns TRUE until reset, but accumulated time (ms) continues to increment while enable is TRU

### Retentive Timer On

A timer that counts up to **preset time (ms)** while **enable** is TRUE. When enable is FALSE, this function block retains the **accumulated time (ms)** value. When **accumulated time (ms)** reaches **preset time (ms)**, **done** returns TRUE until reset, but **accumulated time (ms)** continues to increment while **enable** is TRUE until reset.

[IMAGE alt='icon' src='merge-retentive-timer-on-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. preset time — Specifies the amount of time for the function block to use in calculations. reset — Sets the value of accumulated time (ms) to zero. enable — Determines whether to measure the cumulative time elapsed time between iterations. error out — error out contains error information. This output provides standard error out functionality. accumulated time — Returns the accumulated time elapsed while enabled since the first call or last reset. done — Indicates whether the latest count has finished. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_RetentiveTimerOn.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/timer-off-delay/merge-timer-off-delay-vi.html language=enus -->
## TOPIC 00141: Timer Off Delay

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/timer-off-delay/merge-timer-off-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/timer-off-delay/merge-timer-off-delay-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an output signal with rising edges that align with the input signal, but with falling edges delayed by preset time (ms). This function block generates an output signal that remains TRUE longer than the input signal by preset time (ms). icon Dialog Box Options Option Description Inputs Cont

### Timer Off Delay

Generates an **output** signal with rising edges that align with the **input** signal, but with falling edges delayed by **preset time (ms)**.

This function block generates an output signal that remains TRUE longer than the input signal by **preset time (ms)**.

[IMAGE alt='icon' src='merge-timer-off-delay-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the digital input signal. preset time (ms) — Specifies the amount of time for the function block to use in calculations. elapsed time (ms) — Returns the amount of time, in milliseconds, elapsed since the start of the delay. If no delay has started, this output returns the amount of time elapsed since the first call of the function block. error out — error out contains error information. This output provides standard error out functionality. output — Returns the digital output signal. |
| --- |

If a new rising edge occurs on **input** during the delay period, **output** remains TRUE and the delay period restarts at the next falling edge of **input**.

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_TimerOffDelay.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/counter/timer-on-delay/merge-timer-on-delay-vi.html language=enus -->
## TOPIC 00142: Timer On Delay

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/counter/timer-on-delay/merge-timer-on-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/counter/timer-on-delay/merge-timer-on-delay-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates an output signal with falling edges that align with those of the input signal, but with rising edges delayed by preset time (ms). This function block generates an output signal that remains FALSE longer than the input signal by preset time (ms). icon Dialog Box Options Option Description I

### Timer On Delay

Generates an **output** signal with falling edges that align with those of the **input** signal, but with rising edges delayed by **preset time (ms)**.

This function block generates an output signal that remains FALSE longer than the input signal by **preset time (ms)**.

[IMAGE alt='icon' src='merge-timer-on-delay-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the digital input signal. preset time (ms) — Specifies the amount of time for the function block to use in calculations. elapsed time (ms) — Returns the amount of time, in milliseconds, elapsed since the start of the delay. If no delay has started, this output returns the amount of time elapsed since the first call of the function block. error out — error out contains error information. This output provides standard error out functionality. output — Returns the digital output signal. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_TimerOnDelay.gif']

Parent topic:

Timer

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/edge-detection/edge-detect/merge-edge-detect-vi.html language=enus -->
## TOPIC 00143: Edge Detect

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/edge-detection/edge-detect/merge-edge-detect-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/edge-detection/edge-detect/merge-edge-detect-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects rising edges on input 1 and falling edges on input 2. The output indicator pulses TRUE for one iteration when input 1 transitions to TRUE, when input 2 transitions to FALSE, or when both conditions occur simultaneously. icon Dialog Box Options Option Description Inputs Contains the following

### Edge Detect

Detects rising edges on **input 1** and falling edges on **input 2**. The **output** indicator pulses TRUE for one iteration when **input 1** transitions to TRUE, when **input 2** transitions to FALSE, or when both conditions occur simultaneously.

[IMAGE alt='icon' src='merge-edge-detect-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input 1 — Specifies the first input. The function block detects rising edges on this input. input 2 — Specifies the second input. The function block detects falling edges on this input. output — Returns the digital output signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_EdgeDetect.gif']

Parent topic:

Edge Detect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/edge-detection/one-shot-falling-with-input/merge-one-shot-falling-with-input-vi.html language=enus -->
## TOPIC 00144: One Shot Falling With Input

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/edge-detection/one-shot-falling-with-input/merge-one-shot-falling-with-input-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/edge-detection/one-shot-falling-with-input/merge-one-shot-falling-with-input-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects a falling edge, a transition from TRUE to FALSE, on the input signal. When a falling edge occurs, output is TRUE for one function block execution. The value of output remains FALSE until a new falling edge occurs. icon Dialog Box Options Option Description Inputs Contains the following confi

### One Shot Falling With Input

Detects a falling edge, a transition from TRUE to FALSE, on the input signal. When a falling edge occurs, **output** is TRUE for one function block execution. The value of **output** remains FALSE until a new falling edge occurs.

[IMAGE alt='icon' src='merge-one-shot-falling-with-input-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the digital input signal. error out — error out contains error information. This output provides standard error out functionality. output — Returns the digital output signal. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_OneShotFallingWithInput.gif']

Parent topic:

Edge Detect

<!--NI_TOPIC bundle=lvrt-api-ref path=vi-lib/functionblocks/edge-detection/one-shot-rising-with-input/merge-one-shot-rising-with-input-vi.html language=enus -->
## TOPIC 00145: One Shot Rising with Input

- bundle_id: `lvrt-api-ref`
- source_path: `vi-lib/functionblocks/edge-detection/one-shot-rising-with-input/merge-one-shot-rising-with-input-vi.html`
- source_url: https://docs-be.ni.com/bundle/lvrt-api-ref/raw/resource/enus/vi-lib/functionblocks/edge-detection/one-shot-rising-with-input/merge-one-shot-rising-with-input-vi.html
- document_id: `lvrt-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Detects a rising edge, a transition from FALSE to TRUE, on the input signal. When a rising edge occurs, output is TRUE for one function block execution. The value of output remains FALSE until a new rising edge occurs. icon Dialog Box Options Option Description Inputs Contains the following configur

### One Shot Rising with Input

Detects a rising edge, a transition from FALSE to TRUE, on the input signal. When a rising edge occurs, **output** is TRUE for one function block execution. The value of **output** remains FALSE until a new rising edge occurs.

[IMAGE alt='icon' src='merge-one-shot-rising-with-input-vi.png']

#### Dialog Box Options

| Option | Description |
| --- | --- |
| Inputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. Data source—Specifies the data source of the input. Select Terminal to wire the input value to the terminal on the block diagram. Select Variable to supply the input value to the function block through the associated terminal variable, if available. Select Default value to use the Default value. The Variable data source option is not available if you select No Variable under Variable Scope. If you select Terminal as the data source and leave the block diagram terminal unwired, LabVIEW uses the Default value. Default value—Specifies the default value of the input. If you select Variable as the data source, LabVIEW uses this value as the initial value of the variable. If you select Default value as the data source, LabVIEW uses this value for every iteration of the function block. |
| Outputs | Contains the following configuration options: Terminal name—Contains the name of the block diagram terminal to configure. Visible?—Specifies whether to display the terminal on the block diagram. Variable scope—Specifies the availability and scope of the variable associated with the terminal. Select Single-process to use a single-process shared variable. Select Network-published to use a network-published shared variable. Select No Variable if you do not want to use a terminal variable. To minimize overhead, include function block terminal variables only when necessary. If you change the Variable scope to No Variable after creating the function block instance, LabVIEW deletes the terminal variable. |

#### Inputs/Outputs

| error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. input — Specifies the digital input signal. error out — error out contains error information. This output provides standard error out functionality. output — Returns the digital output signal. |
| --- |

The timing of this function block depends on the rate of the Timed Loop or While Loop in which you place the function block. For example, if you need the function block to update with millisecond resolution, you can place the function block in a Timed Loop configured to execute every millisecond.

The following timing diagram illustrates the behavior of this function block.

[IMAGE alt='image' src='loc_eps_TD_OneShotRisingWithInput.gif']

Parent topic:

Edge Detect
