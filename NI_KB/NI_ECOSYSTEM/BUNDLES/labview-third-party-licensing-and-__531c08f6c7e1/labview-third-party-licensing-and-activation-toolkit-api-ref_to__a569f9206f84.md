# NI DOCUMENT BUNDLE: labview-third-party-licensing-and-activation-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-third-party-licensing-and-activation-toolkit-api-ref start=1 end=22 -->
<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/3rdpartylic_pal.html language=enus -->
## TOPIC 00001: Third Party Licensing & Activation VIs

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/3rdpartylic_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/3rdpartylic_pal.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Third Party Licensing & Activation VIs

**Requires:** Third Party Licensing & Activation Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Third Party Licensing & Activation VIs to [enforce licensing in deployment add-ons](addonlicensing.html), such as executables, that you build in LabVIEW.

Refer to the labview\examples\addonlicensing directory for examples of using the Third Party Licensing & Activation VIs in the source code for an add-on. Refer to the LabVIEW Add-on Dev Center on the NI Community for additional resources related to licensing a deployment add-on.

| Palette Object | Description |
| --- | --- |
| Activate License | Activates a license file for an add-on. You can choose to allow automated online activation, manual activation, or both, but you must manually select the polymorphic instance you want to use. |
| Activate License for Custom Hardware | Activates a license file and binds it to a specific hardware target. You can choose to allow automated online activation, manual activation, or both, but you must manually select the polymorphic instance you want to use. |
| Add Licensing to Library | Associates the license you specify in licensing information with the add-on you specify in product information. |
| Get Development License File Path | Returns the path to the development license file that LabVIEW uses to activate an add-on. The location of the license file depends on the company name because LabVIEW installs license files in the National Instruments\\Partners\\<company name>\\Licenses directory. |
| Get License Status | Returns the status of a license file. Use this VI to check if a license file associated with an add-on is activated, in evaluation mode, expired, or invalid. |
| Product Activation | Configures and displays a dialog box in which users can activate an add-on license, and then activates the license. Use this VI to allow users to activate an executable add-on when the executable runs. |
| Remove Licensing from Library | Removes the password and licensing information from the specified library so that the library is no longer password protected, which means the add-on is no longer licensed. |

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/activatecustomhw.html language=enus -->
## TOPIC 00002: Activate License for Custom Hardware VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/activatecustomhw.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/activatecustomhw.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Activate License for Custom Hardware VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Activates a license file and binds it to a specific hardware target. You can choose to allow automated online activation, manual activation, or both, but you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

When you bind a license to a specific **custom hardware ID**, this VI adds the ID to the license, and if a user tries to use the license on a different target, the status of the license is invalid. If you do not need to bind a license to a specific hardware target, use the [Activate License](../addonlicensing/activatelicense.html) VI.

[Details](#details)  [Examples](#examples)

#### Activate Automatically

[IMAGE alt='image' src='activatecustomhwauto.gif']

|  | activation server URL specifies the path to the getcode.asp script file that creates the activation code(s) needed to activate the license. LabVIEW concatenates the activation server URL and the activation server name into a single string to locate the correct script file. Typically, the URL is /<path_to_activation_server>/unlock/getcode.asp. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
| --- | --- |
|  | Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | activation server name specifies the name of the server on which you want LabVIEW to look for the getcode.asp script file that creates the activation code(s) needed to activate the license. If you use an Instant SOLO Server account, specify the value swk to identify the correct server. |
|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | license ID is the license ID that the user receives when he or she purchases the add-on. The user enters the license ID only when performing the automated activation process through an Internet connection. |
|  | license password is the password that the user receives when he or she purchases the add-on. The user enters the license password only when performing the automated activation process through an Internet connection. |
|  | custom hardware ID specifies the serial number of the hardware target to which you want to bind the license. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. |
|  | encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. |
|  | license file info out returns information about the run-time license from the license file info input. handle returns the reference that is used internally only. full path returns the full, or absolute, path to the license file that the user wants to activate. password returns the password to the license file that the user wants to activate. |
|  | handle returns the reference that is used internally only. |
|  | full path returns the full, or absolute, path to the license file that the user wants to activate. |
|  | password returns the password to the license file that the user wants to activate. |
|  | activation successful? indicates whether the add-on was successfully activated. All inputs must be valid for successful activation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Activate Manually

[IMAGE alt='image' src='activatecustomhwman.gif']

|  | custom hardware ID specifies the serial number of the hardware target to which you want to bind the license. |
| --- | --- |
|  | user code 1 (activation session number) is a code that you can generate randomly from the PP_COMPNO function in keylib32.dll or keylib64.dll. Use this code to create the activation code(s) that the user enters in activation code 1 or activation code 2. |
|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | activation code 1 is the first activation code that you create based on user code 1 and user code 2. The user enters this code after he or she receives the activation code(s) via the Web or telephone. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | activation code 2 (Optional) is the second activation code that you create based on user code 1 and user code 2. The user enters this code if he or she receives two activation codes via the Web or telephone. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. |
|  | encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. |
|  | license file info out returns information about the run-time license from the license file info input. handle returns the reference that is used internally only. full path returns the full, or absolute, path to the license file that the user wants to activate. password returns the password to the license file that the user wants to activate. |
|  | handle returns the reference that is used internally only. |
|  | full path returns the full, or absolute, path to the license file that the user wants to activate. |
|  | password returns the password to the license file that the user wants to activate. |
|  | activation successful? indicates whether the add-on was successfully activated. All inputs must be valid for successful activation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Activate License for Custom Hardware Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Examples

Refer to the following VIs for examples of using the Activate License for Custom Hardware VI:

- Activate License - Activate Automatically with Custom Hardware VI: labview\examples\addonlicensing\03 Activate License
- Activate License - Activate Manually with Custom Hardware VI: labview\examples\addonlicensing\03 Activate License

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/activatelicense.html language=enus -->
## TOPIC 00003: Activate License VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/activatelicense.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/activatelicense.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Activate License VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Activates a license file for an add-on. You can choose to allow automated online activation, manual activation, or both, but you must [manually select the polymorphic instance](/csh?topicname=lvhowto/selectingdefaultinstpolyvi.html) you want to use.

If you want to bind a license to a specific hardware target, use the [Activate License for Custom Hardware](../addonlicensing/activatecustomhw.html) VI.

[Details](#details)  [Examples](#examples)

#### Activate Automatically

[IMAGE alt='image' src='activatelicensevi.gif']

|  | activation server URL specifies the path to the getcode.asp script file that creates the activation code(s) needed to activate the license. LabVIEW concatenates the activation server URL and the activation server name into a single string to locate the correct script file. Typically, the URL is /<path_to_activation_server>/unlock/getcode.asp. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
| --- | --- |
|  | Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | activation server name specifies the name of the server on which you want LabVIEW to look for the getcode.asp script file that creates the activation code(s) needed to activate the license. If you use an Instant SOLO Server account, specify the value swk to identify the correct server. |
|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | license ID is the license ID that the user receives when he or she purchases the add-on. The user enters the license ID only when performing the automated activation process through an Internet connection. |
|  | license password is the password that the user receives when he or she purchases the add-on. The user enters the license password only when performing the automated activation process through an Internet connection. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. |
|  | encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. |
|  | license file info out returns information about the run-time license from the license file info input. handle returns the reference that is used internally only. full path returns the full, or absolute, path to the license file that the user wants to activate. password returns the password to the license file that the user wants to activate. |
|  | handle returns the reference that is used internally only. |
|  | full path returns the full, or absolute, path to the license file that the user wants to activate. |
|  | password returns the password to the license file that the user wants to activate. |
|  | activation successful? indicates whether the add-on was successfully activated. All inputs must be valid for successful activation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Activate Manually

[IMAGE alt='image' src='activatelicmanuallyvi.gif']

|  | user code 2 (hardware ID) is the ID number of the computer to which you want to bind the add-on. You can get the ID from the PP_COMPNO function in keylib32.dll or keylib64.dll. If you do not want to bind the add-on to a computer, you can enter any integer for user code 2. However, you must use the same integer to create the activation code(s). |
| --- | --- |
|  | user code 1 (activation session number) is a code that you can generate randomly from the PP_COMPNO function in keylib32.dll or keylib64.dll. Use this code to create the activation code(s) that the user enters in activation code 1 or activation code 2. |
|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | activation code 1 is the first activation code that you create based on user code 1 and user code 2. The user enters this code after he or she receives the activation code(s) via the Web or telephone. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | activation code 2 (Optional) is the second activation code that you create based on user code 1 and user code 2. The user enters this code if he or she receives two activation codes via the Web or telephone. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. |
|  | encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. |
|  | license file info out returns information about the run-time license from the license file info input. handle returns the reference that is used internally only. full path returns the full, or absolute, path to the license file that the user wants to activate. password returns the password to the license file that the user wants to activate. |
|  | handle returns the reference that is used internally only. |
|  | full path returns the full, or absolute, path to the license file that the user wants to activate. |
|  | password returns the password to the license file that the user wants to activate. |
|  | activation successful? indicates whether the add-on was successfully activated. All inputs must be valid for successful activation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Activate License Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Examples

Refer to the following VIs for examples of using the Activate License VI:

- Activate License - Activate Automatically VI: labview\examples\addonlicensing\03 Activate License
- Activate License - Activate Manually VI: labview\examples\addonlicensing\03 Activate License

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/addlictolibrary.html language=enus -->
## TOPIC 00004: Add Licensing to Library VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/addlictolibrary.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/addlictolibrary.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Add Licensing to Library VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Associates the license you specify in **licensing information** with the add-on you specify in **product information**.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='addlictolibraryvi.gif']

|  | product information contains the information that LabVIEW uses to associate the license with the correct add-on. path to lvlib specifies the path, on the developer machine, to the LabVIEW library (.lvlib) that makes up the add-on. company name specifies the company name LabVIEW will display when prompting users to activate the add-on. LabVIEW also uses company name to locate the directory that contains the add-on license on the user computer because add-on licenses are installed into a directory named after the company. product name specifies the name of the add-on. This name also is the add-on name that appears to the user in the Activation dialog box. product version specifies the version of the add-on. This version also is the add-on version that appears to the user in the Activation dialog box. purchase page URL specifies the URL of the Web page through which users can purchase the add-on. This URL also is the page that the Purchase button in the activation dialog box displays in a Web browser. |
| --- | --- |
|  | path to lvlib specifies the path, on the developer machine, to the LabVIEW library (.lvlib) that makes up the add-on. |
|  | company name specifies the company name LabVIEW will display when prompting users to activate the add-on. LabVIEW also uses company name to locate the directory that contains the add-on license on the user computer because add-on licenses are installed into a directory named after the company. |
|  | product name specifies the name of the add-on. This name also is the add-on name that appears to the user in the Activation dialog box. |
|  | product version specifies the version of the add-on. This version also is the add-on version that appears to the user in the Activation dialog box. |
|  | purchase page URL specifies the URL of the Web page through which users can purchase the add-on. This URL also is the page that the Purchase button in the activation dialog box displays in a Web browser. |
|  | licensing information contains the information that LabVIEW uses to associate the correct license with the add-on. license file path specifies the path to the license file on the developer computer. This path must go to the license file that you created with the same product name and definition as the add-on. license file password specifies the password to the license file that the user wants to activate. auto activation URL specifies the URL that LabVIEW uses to activate an add-on automatically. This URL must be in the format http(s)://soloserver/unlock. web activation URL specifies the URL to the Web page that users must visit to obtain the activation code(s) they need to manually activate an add-on. phone activation number specifies the phone number that users must call to obtain the activation code(s) they need to manually activate an add-on. activation methods lists the activation methods that you can choose to allow for the add-on. You can allow one type of activation, or you can allow users to choose between two or three types of activation. 0None1Auto2Web3Auto \| Web4Phone5Auto \| Phone6Web \| Phone7Auto \| Web \| Phone |
|  | license file path specifies the path to the license file on the developer computer. This path must go to the license file that you created with the same product name and definition as the add-on. |
|  | license file password specifies the password to the license file that the user wants to activate. |
|  | auto activation URL specifies the URL that LabVIEW uses to activate an add-on automatically. This URL must be in the format http(s)://soloserver/unlock. |
|  | web activation URL specifies the URL to the Web page that users must visit to obtain the activation code(s) they need to manually activate an add-on. |
|  | phone activation number specifies the phone number that users must call to obtain the activation code(s) they need to manually activate an add-on. |
|  | activation methods lists the activation methods that you can choose to allow for the add-on. You can allow one type of activation, or you can allow users to choose between two or three types of activation. 0None1Auto2Web3Auto \| Web4Phone5Auto \| Phone6Web \| Phone7Auto \| Web \| Phone |
| 0 | None |
| 1 | Auto |
| 2 | Web |
| 3 | Auto \| Web |
| 4 | Phone |
| 5 | Auto \| Phone |
| 6 | Web \| Phone |
| 7 | Auto \| Web \| Phone |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | current lvlib password specifies the current password to the LabVIEW library (.lvlib) that makes up the add-on. You do not need to supply this value the first time you add licensing to a library. Instead, just supply the new lvlib password. |
|  | new lvlib password specifies the password you want to assign to the library that makes up the add-on. If you are making changes to a library that is already licensed, you can wire the same value to both current lvlib password and new lvlib password to keep the same password. |
|  | licensing successful? indicates whether the library that makes up the add-on was activated successfully. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Add Licensing to Library Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Example

Refer to the Add Licensing To Library VI in the labview\examples\addonlicensing\04 Adding Licensing to Library directory for an example of using the Add Licensing to Library VI.

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/addonlicensing.html language=enus -->
## TOPIC 00005: Third Party Licensing & Activation Toolkit

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/addonlicensing.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/addonlicensing.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Third Party Licensing & Activation Toolkit

June 2012, 373159C-01

The Third Party Licensing & Activation Toolkit enables you to license add-ons that you create with LabVIEW. Users of a licensed add-on must evaluate or activate the add-on according to the activation methods you allow. The Third Party Licensing & Activation Toolkit provides methods for licensing two types of add-ons:

- A development add-on consists of a library of files, such as VIs or custom controls, that others can use when developing in LabVIEW. Apply licensing to a development add-on so that LabVIEW automatically checks the license status of the files at edit time.
- A deployment add-on is a stand-alone application that you build in LabVIEW, such as an executable, and then distribute to users. Apply licensing to a deployment add-on so the add-on checks the license status when users run the add-on.

The following topics provide resources and procedures you can use to create, license, and distribute an add-on.

| Licensing at a Glance | Resources |
| --- | --- |
| Licensing a Development Add-on Licensing a Deployment Add-on | Requirements for Licensing Add-ons Support and Resources |

© 2010–2012 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/bldinstall_3rdpartylic.html language=enus -->
## TOPIC 00006: Final Step: Package the Add-on for Distribution (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/bldinstall_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/bldinstall_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Final Step: Package the Add-on for Distribution (Third Party Licensing & Activation Toolkit)

*This task is the final step in the [procedure for applying licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

After you create and license an add-on, prepare the add-on for distribution to users. Consider one of the following methods for distributing an add-on:

- Use the JKI VI Package Manager (VIPM) Professional or Enterprise edition software to bundle add-on files in a JKI VI Package file, a single file users can access to install the add-on with LabVIEW.
 [IMAGE alt='Note' src='note.gif']
**Note** Refer to the JKI website for more information about the VIPM software. Refer to the VIPM software documentation for information about using the VIPM software to bundle and share add-ons.
- In LabVIEW, use the Application Builder to create an Installer build specification and build an installer. The rest of this topic contains instructions for building an installer for a development add-on .

Whichever process you use to build an installer, make sure to install the correct files in the correct locations, as described in the steps below. LabVIEW uses these locations to find the files necessary to activate an add-on when a user wants to use the add-on.

#### Building an Installer in LabVIEW

Complete the steps in the following sections to build an installer using the Application Builder Installer build specification.

##### Prepare the Files Required to Build an Installer

1. Create a LabVIEW project ( .lvproj ) and add the following files to the project:
  - The library ( .lvlib ) file from step 1 that contains the add-on files.
  - The license ( .lf ) file you created and applied to the library file.
2. Create a VI that uses the System Exec VI to call RegisterAddon.exe , located in the LabVIEWInstallDir\resource\Partners directory, with the following command line: 
 
 RegisterAddon.exe -- -s -l *path_to_lvlib* 
 
where l is a lowercase L, and *path_to_lvlib* is the path to the LabVIEW library relative to the LabVIEW installation directory.
3. Save the new VI in the project.
4. In the Project Explorer window, build an executable from the VI you create to call RegisterAddon.exe .

In the next section, you configure the installer to automatically run this executable and call RegisterAddon.exe. RegisterAddon.exe adds information about the add-on to the system registry of the computer on which you install the add-on. This ensures that LabVIEW prompts users to activate the add-on after they install the add-on.

Refer to the 07 Sample Toolkit Project example in the labview\examples\addonlicensing directory to see an example before you build an installer.

##### Configure the Installer Build Specification

1. Open the LabVIEW project that contains the add-on ( .lvlib ) that you want to distribute.
2. In the Project Explorer window, right-click Build Specifications and select New»Installer from the shortcut menu to display the Installer Properties dialog box.
 [IMAGE alt='Note' src='note.gif']
**Note** You also can open the 07 Sample Toolkit Project example in the labview\examples\addonlicensing directory and adapt the files and installer build specification in the .lvproj file.
3. Select the Destinations category at the left of the dialog box, and if necessary, add the following new destinations:
  - [LabVIEW *X*]»resource»Partners , where X is the LabVIEW version number.
  - [Public App Data]»National Instruments»Partners»*company name*»Licenses , where company name is the same value you specified when you licensed the add-on.
  - The directory in which you want to install the add-on files. If an existing destination is sufficient, proceed to the next step.
4. Add the executable you created in the previous section to the [LabVIEW *X*]\resource\Partners destination.
5. Select the Source Files category and add the license file ( .lf ) to the [Public App Data]»National Instruments»Partners»*company name*»Licenses destination.
6. Select the Source File Settings category and, one at a time, select each of the license files you want to install and place a checkmark in the Unlock checkbox for each of the files, if necessary. This setting ensures that the license files work as expected when installed on a computer running Windows 7 or Windows Vista.
7. Select the Additional Installers category and place a checkmark in the NI Third Party Add-on Activation Libraries checkbox in the National Instruments Installers to Include listbox.
8. Select the Advanced category and place a checkmark in the Run executable at end of installation checkbox. The Select Target File dialog box appears.
9. Select the executable that you created to call RegisterAddon.exe .
10. Place a checkmark in the Require the LabVIEW *x* [32-bit or 64-bit] development system or later checkbox.
11. (Optional) Configure other options in the installer to meet the needs of the add-on.
12. Click the Build button to exit the dialog box and build the installer for the add-on.

You can distribute this installer to users. When the installer runs, it installs the add-on, and then runs the executable you create in the previous section to register the add-on.

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/createtoolkit_3rdpartylic.html language=enus -->
## TOPIC 00007: Step 1: Develop the Add-on Files (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/createtoolkit_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/createtoolkit_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 1: Develop the Add-on Files (Third Party Licensing & Activation Toolkit)

*This task is step 1 in the [procedure for applying licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

The VIs that make up an add-on must be in a LabVIEW project library before you can license the add-on. Complete the following steps to package an add-on for licensing.

1. Create the VIs or other files that make up the add-on. Refer to the Related Links section to find more information about developing VIs in LabVIEW.
2. Create a LabVIEW project library ( .lvlib ), which becomes the packaged add-on.
3. Add the add-on files to the library.
4. Save the library.

Next Step: If you want to apply [standard licensing](overview_3rdpartylic.html), [license the add-on](proddef_standard.html). If you want to apply [advanced, custom licensing](overview_3rdpartylic.html), [create a product definition for the add-on](proddeflfedit_3rdpartylic.html).

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

**Related Links**

[Application Development and Design Guidelines](/csh?topicname=lvdevconcepts/lvdevconcepts_main.html)

[Best Practices for Large Application Development](/csh?topicname=lvdevconcepts/best_practices_large_apps.html)

[Creating VIs and SubVIs](/csh?topicname=lvconcepts/creating_vis_and_subvis.html)

[LabVIEW Style Checklist](/csh?topicname=lvdevconcepts/checklist.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/getdevlicfilepath.html language=enus -->
## TOPIC 00008: Get Development License File Path VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/getdevlicfilepath.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/getdevlicfilepath.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Development License File Path VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Returns the path to the development license file that LabVIEW uses to activate an add-on. The location of the license file depends on the company name because LabVIEW installs license files in the National Instruments\Partners\<company name>\Licenses directory.

[Details](#details)

[IMAGE alt='image' src='getdevlicfilepathvi.gif']

|  | license file name specifies the name of the license file you want the path to. |
| --- | --- |
|  | company name is the name you supplied when you associated the license file with the add-on library. LabVIEW uses company name to locate the directory that contains the add-on license on the user computer because add-on licenses are installed into a directory named after the company. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | license file path returns the path to the development license file that LabVIEW uses to activate an add-on. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get Development License File Path Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/getlicensestatus.html language=enus -->
## TOPIC 00009: Get License Status VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/getlicensestatus.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/getlicensestatus.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get License Status VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Returns the status of a license file. Use this VI to check if a license file associated with an add-on is activated, in evaluation mode, expired, or invalid.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='getlicensestatusvi.gif']

|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
| --- | --- |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | dev license is valid specifies whether a user with a development license can use that license instead of using the run-time license the license file info input identifies. The default is FALSE. If TRUE, this VI checks the status of both the run-time license and the development license, which you identify with the dev license file info input. Distributing both development and run-time licenses is useful for allowing you to protect certain functionality with the run-time license, but still allowing users to test parts of the product in a development environment. |
|  | Distributing both development and run-time licenses is useful for allowing you to protect certain functionality with the run-time license, but still allowing users to test parts of the product in a development environment. |
|  | dev license file info contains information that identifies a development license file that can optionally protect the add-on. If the dev license is valid input is FALSE, LabVIEW ignores this input and checks only the run-time license, which you identify with the license file info input. If dev license is valid is TRUE, LabVIEW uses this development license only if the status of the development license is "better" than the status of the run-time license. For example, if the run-time license is expired, but the development license is activated or in evaluation status, then the development license can allow users to access the add-on. Note This development license file must be present in the following directory: [Public App Data]\\National Instruments\\Partners\\company name\\Licenses, where [Public App Data] corresponds to the CommonAppDataFolder property and company name is the same value you specified when you licensed the add-on. name specifies the name of the development license file. password specifies the password for the license file. company name is the name you supplied when you associated the license file with the add-on library. LabVIEW uses company name to locate the directory that contains the add-on license on the user computer because add-on licenses are installed into a directory named after the company. |
|  | Note This development license file must be present in the following directory: [Public App Data]\\National Instruments\\Partners\\company name\\Licenses, where [Public App Data] corresponds to the CommonAppDataFolder property and company name is the same value you specified when you licensed the add-on. |
|  | name specifies the name of the development license file. |
|  | password specifies the password for the license file. |
|  | company name is the name you supplied when you associated the license file with the add-on library. LabVIEW uses company name to locate the directory that contains the add-on license on the user computer because add-on licenses are installed into a directory named after the company. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | custom hardware ID specifies the serial number of the hardware target with which you want to use the license. If the license file is bound to the serial number for a specific target, the custom hardware ID must match the number in the license. Otherwise, this VI returns a license status of Invalid, even if the license has a status of activated or evaluation. If you do not wire a value to this input, this VI does not check the license for a serial number. |
|  | license file info out returns information about the run-time license from the license file info input. handle returns the reference that is used internally only. full path returns the full, or absolute, path to the license file that the user wants to activate. password returns the password to the license file that the user wants to activate. |
|  | handle returns the reference that is used internally only. |
|  | full path returns the full, or absolute, path to the license file that the user wants to activate. |
|  | password returns the password to the license file that the user wants to activate. |
|  | license status returns the status of the license that LabVIEW uses to activate the add-on. You define the meaning of each status when you create the license file. This VI returns the status of the license the license file info input identifies unless dev license is valid is TRUE. In this case, LabVIEW returns the status of either license file info or dev license file info, depending on which license has the "best" status. For example, if the run-time license is expired, but the development license is activated or in evaluation status, then this VI returns the status of the development license. 0Invalid1Expired2Evaluation3Activated |
| 0 | Invalid |
| 1 | Expired |
| 2 | Evaluation |
| 3 | Activated |
|  | error code returns an error if this VI fails to retrieve the license status. This error code is from SoftwareKey. Visit the support section of the SoftwareKey website for more information about this error code. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Get License Status Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Example

Refer to the Get License Status VI in the labview\examples\addonlicensing\01 Get License Status directory for an example of using the Get License Status VI.

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/lictoolkit_3rdpartylic.html language=enus -->
## TOPIC 00010: Step 5: Add the License to the Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/lictoolkit_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/lictoolkit_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 5: Add the License to the Add-on (Third Party Licensing & Activation Toolkit)

*This task is step 5 in the [procedure for applying advanced licensing](overview_3rdpartylic.html) to an add-on.*

After you develop an add-on, create a product definition for the add-on, and create a license file for the add-on, you have everything necessary to apply the license to the add-on. Complete the following steps to finish the licensing process.

1. Select Tools»Add-on Licensing Tool to display the Add-on Licensing Tool dialog box.
2. Click the Advanced Mode button at the bottom-left of the dialog box to open the correct interface for applying the license file to the add-on.
3. Complete all required fields in the Add-on Licensing Tool dialog box to complete the licensing process.

The **Add-on Licensing Tool** dialog box applies the license to all files in the LabVIEW project library that makes up the add-on.

[Next Step: Package the Add-on for Distribution](bldinstall_3rdpartylic.html)

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/morehelp_3rdpartylic.html language=enus -->
## TOPIC 00011: Support and Resources (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/morehelp_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/morehelp_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Support and Resources (Third Party Licensing & Activation Toolkit)

The following resources contain tutorials and other support information that you might find helpful as you use the Third Party Licensing & Activation Toolkit:

- LabVIEW Add-on Dev Center —Visit this add-on development forum on the NI Community for more information about developing and licensing add-ons in LabVIEW.
- Concept Software Support Center—Refer to the support section of the SoftwareKey website for more information about using Protection PLUS, LFEdit, and Instant SOLO Server.

If the previous items do not answer your question, contact the LabVIEW Partner Team at labviewpartnerprogram@ni.com for support requests related to licensing add-ons.

[[IMAGE alt='image' src='back_arrow.gif']](addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](addonlicensing.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/overview_3rdpartylic.html language=enus -->
## TOPIC 00012: Licensing a Development Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/overview_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/overview_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Licensing a Development Add-on (Third Party Licensing & Activation Toolkit)

This topic contains instructions for licensing a [development add-on](addonlicensing.html) that consists of files others can use when developing in LabVIEW. The Third Party Licensing & Activation Toolkit provides two options for licensing add-ons: standard licensing or advanced licensing.

The flow charts show the procedure for developing, licensing, and distributing an add-on using each option. Click an item to view instructions for completing that task.

| Standard licensing | Advanced licensing |
| --- | --- |
| Use a single, streamlined tool in LabVIEW to create and apply a license with standard, predefined settings.You must have an Internet connection and an Instant SOLO Server account to use standard mode. Note This functionality is available only in LabVIEW 2010 and later. | Use multiple tools that allow you to customize advanced licensing options, such as the length of the evaluation period.You must use a fully licensed version of Concept Software Protection PLUS to perform the advanced licensing procedure. (Optional) You need an Instant SOLO Server account to enable automated activation for licenses. |
|  | Note This functionality is available only in LabVIEW 2010 and later. |
| Complete the following procedure to apply standard licensing: | Complete the following procedure to apply advanced licensing: |

[[IMAGE alt='image' src='back_arrow.gif']](addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](addonlicensing.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/overview_deploylic.html language=enus -->
## TOPIC 00013: Licensing a Deployment Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/overview_deploylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/overview_deploylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Licensing a Deployment Add-on (Third Party Licensing & Activation Toolkit)

The procedure for adding licensing to [deployment add-ons](addonlicensing.html), such as executables, is similar to the procedure for [adding licensing to a development add-on](overview_3rdpartylic.html). The following flow chart show the process for developing, licensing, and distributing a stand-alone application.

|  | Note You can click some of the items to view a procedure for completing that task. For items without an additional procedure, refer to the LabVIEW Add-on Dev Center on the NI Community for step–by–step instructions for completing those tasks. |
| --- | --- |

|  |
| --- |
|  |
|  |
|  |
|  |

Licensing a deployment-add-on requires you to use [certain tools](requirements_3rdpartylic.html) in conjunction with LabVIEW.

[[IMAGE alt='image' src='back_arrow.gif']](addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](addonlicensing.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/proddef_standard.html language=enus -->
## TOPIC 00014: Step 2: License the Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/proddef_standard.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/proddef_standard.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 2: License the Add-on (Third Party Licensing & Activation Toolkit)

*This task is step 2 in the [procedure for applying standard licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

After you [develop an add-on](createtoolkit_3rdpartylic.html), use the [Add-on Licensing Tool](../addonlicensing/std_addonlictooldb.html) dialog box to create a license and apply it to the add-on.

|  | Note The functionality this topic describes is available only in LabVIEW 2010 and later. |
| --- | --- |

Complete the following steps to create a license and apply it to the add-on. You must have an Internet connection and a free [Instant SOLO Server](requirements_3rdpartylic.html)™ account to use standard mode. You can sign up for an account at the same time that you complete the procedure.

1. In LabVIEW, select Tools»Add-on Licensing Tool to display the Add-on Licensing Tool dialog box.
2. Log in to your Instant SOLO Server account.
3. Select Define a new add-on to license .
4. Complete all required fields and pages in the Add-on Licensing Tool dialog box to create a license and apply the license to the files in the LabVIEW project library file ( .lvlib ) you created in step 1 .

|  | Note Refer to the Developer Zone at ni.com/zone or click the Help button in the Add-on Licensing Tool dialog box for more information about completing the fields in the dialog box. |
| --- | --- |

After you finish using the **Add-On Licensing Tool** dialog box to license the add-on, notice that the output directory contains only the files the library file contains, as well as the newly created license file. You must manually copy any additional, unlicensed files you want to distribute with the add-on to that folder.

[Next Step: Package the Add-on for Distribution](bldinstall_3rdpartylic.html)

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/proddeflfedit_3rdpartylic.html language=enus -->
## TOPIC 00015: Step 2: Create a Product Definition for the Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/proddeflfedit_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/proddeflfedit_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 2: Create a Product Definition for the Add-on (Third Party Licensing & Activation Toolkit)

*This task is step 2 in the [procedure for applying advanced licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

After you [develop an add-on](createtoolkit_3rdpartylic.html) in LabVIEW, complete the following steps to name and define the add-on in LFEdit, a component of the [Protection PLUS](requirements_3rdpartylic.html) software. This procedure creates a product definition. In the next step, you create a license file that corresponds to this product definition.

|  | Note You must use a fully licensed version of Protection PLUS to use LFEdit to create a product definition and license file. |
| --- | --- |

1. Launch LFEdit by selecting Start»SoftwareKey Licensing System»PLUS»LFEdit .
2. Select Product Definition»Setup to display the Product Definitions Setup dialog box.
3. Click the Add button to create a new product definition.
4. On the General page, enter a name and description for the add-on.
5. Click the License File tab and browse to a convenient location at which to save the license file. National Instruments recommends that you name the file with the .lf extension rather than the default .ini extension.
6. On the License File page, enter a value in the Password text box. 
 [IMAGE alt='Tip' src='tip.gif']
**Tip** Record the password. You must specify the password when you add a license file to the add-on in a future step.
7. (Optional) If you want to enable automated activation for the add-on , record the values from the Seed and Reg Key 2 Seed text boxes on the Trigger Codes page for use in a future step.
8. Click the EZTrial tab. To implement hardware binding (in which the license file is bound to the computer ID number), select the Enhanced Algorithms option.
9. (Optional) Place a checkmark in the Unlimited checkbox in the Times to Run section.

[Next Step: Create a License File for the Add-on](prodliclfedit_3rdpartylic.html)

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/proddefsolo_3rdpartylic.html language=enus -->
## TOPIC 00016: Step 4 (Optional): Enable Automated Activation for the Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/proddefsolo_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/proddefsolo_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 4 (Optional): Enable Automated Activation for the Add-on (Third Party Licensing & Activation Toolkit)

*This task is step 4 in the [procedure for applying advanced licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

You can allow users to activate an add-on through an automated online process. Automated activation allows users to enter a license ID and password and have the toolkit automatically activated.

Complete the followings steps to enable the automated activation mechanism for an add-on.

|  | Note You must have an Instant SOLO Server account to enable automated activation for an add-on. |
| --- | --- |

**Creating a Profile for Automated Activations**

1. Open the SoftwareKey website in a Web browser.
2. Log in to your Instant SOLO Server account using the account information you received by e-mail after you signed up for an account. Sign up for an account if you do not have one.
3. Select Authors»Products»Add Product Wizard from the top menubar in the Web page.
4. On the Add Product Wizard page, enter the name of the add-on in the Product Name text box.
5. Enter a description of the add-on in the Description text box.
6. (Optional) Complete the rest of this page as needed for your add-on.
7. Click the Next button at the bottom of the page to create the product definition.
8. The Purchasing URLs page opens and displays URLs you can use to direct users to a website where they can order the add-on. Use these URLs later in the licensing process to direct users to web pages where they can purchase the add-on.

**Linking the Add-on with the Automated Activation Mechanism**

1. Select Authors»Products»List from the top menubar in the Web page.
2. Click the name of the add-on to open its profile in SOLO Server.
3. In the Other Information section, click the Add link.
4. In the Add Product Option page, enter the name and description of the licensing option.
5. Select PLUS Single Option from the Product Option Type list.
6. In the Product Activation & Licensing Details section, enter a trigger code in the Trigger Code # text box. Refer to the EZ Trigger documentation on the SoftwareKey website for a list of trigger codes.
 [IMAGE alt='Note' src='note.gif']
**Note** If you enabled hardware binding when you created the product definition in LFEdit, you must select one of the hardware binding trigger codes.
7. In the Product Activation & Licensing Details section, enter the values for the seeds that you created in LFEdit in the Trigger Code Seed and RegKey 2 Seed text boxes.
8. (Optional) Complete the rest of this page as needed for the add-on.
9. Click the Submit button to add the product option.

Now that automated activation mechanism is enabled, in the next step, you can specify that you want LabVIEW to allow users to perform automated online activations of the add-on.

[Next Step: Add the License to the Add-on](lictoolkit_3rdpartylic.html)

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/prodliclfedit_3rdpartylic.html language=enus -->
## TOPIC 00017: Step 3: Create a License File for the Add-on (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/prodliclfedit_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/prodliclfedit_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Step 3: Create a License File for the Add-on (Third Party Licensing & Activation Toolkit)

*This task is step 3 in the [procedure for applying advanced licensing](overview_3rdpartylic.html) to a [development add-on](addonlicensing.html).*

After you [create a product definition](proddeflfedit_3rdpartylic.html) for the add-on, you must create the license file that you will later apply to the add-on. Complete the following steps to create a license file for an add-on.

|  | Note You must use a fully licensed version of Protection PLUS to use LFEdit to create a product definition and license file. |
| --- | --- |

1. In LFEdit , select File»New License File .
2. Select the product definition for the add-on you want to license from the pull-down menu and click the OK button.
3. (Optional) Enter information on each page of the dialog box to customize the license. However, you also can leave all fields at their default settings. Refer to the Protection PLUS Online Manual in the support section of the SoftwareKey website for more information about customizing a license file.
4. Select File»Save License File to save the license file at the location you specified when you created the product definition. To save the license file to a different location, select File»Save License File As to browse to the location where you want to save the license file.

[Next Step (Optional): Enable Automated Activation for the Add-on](proddefsolo_3rdpartylic.html)

[[IMAGE alt='image' src='back_arrow.gif']](overview_3rdpartylic.html) [*Licensing a Development Add-on* Workflow](overview_3rdpartylic.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/productactivation.html language=enus -->
## TOPIC 00018: Product Activation VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/productactivation.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/productactivation.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Product Activation VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Configures and displays a dialog box in which users can activate an add-on license, and then activates the license. Use this VI to allow users to activate an executable add-on when the executable runs.

You can use the **custom hardware ID** input to bind the license to a specific hardware target.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='productactivationvi.gif']

|  | license file info contains information that identifies the run-time license that protects the add-on when users run the add-on. handle is a reference to the license file and is used internally only. You do not need to change this input. full path specifies the full, or absolute, path to the license file on the user machine. password specifies the password for the license file. |
| --- | --- |
|  | handle is a reference to the license file and is used internally only. You do not need to change this input. |
|  | full path specifies the full, or absolute, path to the license file on the user machine. |
|  | password specifies the password for the license file. |
|  | activation info contains the information you want to appear to the user in the activation dialog box. trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. activation server name specifies the name of the server on which you want LabVIEW to look for the getcode.asp script file that creates the activation code(s) needed to activate the license. If you use an Instant SOLO Server account, specify the value swk to identify the correct server. activation server URL specifies the path to the getcode.asp script file that creates the activation code(s) needed to activate the license. LabVIEW concatenates the activation server URL and the activation server name into a single string to locate the correct script file. Typically, the URL is /<path_to_activation_server>/unlock/getcode.asp. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. supports automatic activation specifies whether the option to activate the add-on through an automated online process is available in the activation dialog box this VI displays when it runs. supports web activation specifies whether to enable the option to acquire activation codes through a Web page you specify in the web activation URL input. supports phone activation specifies whether to enable the option to acquire activation code(s) through a phone number that you list in the phone activation number input. web activation URL specifies the URL to the Web page that users must visit to obtain the activation code(s) they need to manually activate an add-on. phone activation number specifies the phone number that users must call to obtain the activation code(s) they need to manually activate an add-on. purchase page URL specifies the URL of the Web page through which users can purchase the add-on. This URL also is the page that the Purchase button in the activation dialog box displays in a Web browser. |
|  | trigger code seed is the trigger code stored in the product definition you create in LFEdit. Refer to the EZ Trigger documentation on the SoftwareKey website to learn more about trigger codes. |
|  | encryption seed is the Reg Key 2 seed stored in the product definition you create in LFEdit. |
|  | activation server name specifies the name of the server on which you want LabVIEW to look for the getcode.asp script file that creates the activation code(s) needed to activate the license. If you use an Instant SOLO Server account, specify the value swk to identify the correct server. |
|  | activation server URL specifies the path to the getcode.asp script file that creates the activation code(s) needed to activate the license. LabVIEW concatenates the activation server URL and the activation server name into a single string to locate the correct script file. Typically, the URL is /<path_to_activation_server>/unlock/getcode.asp. Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | Note Activation code 1 is the RegKey1 code that you generate in LFEdit, and activation code 2 is the RegKey2 code that you generate in LFEdit. |
|  | supports automatic activation specifies whether the option to activate the add-on through an automated online process is available in the activation dialog box this VI displays when it runs. |
|  | supports web activation specifies whether to enable the option to acquire activation codes through a Web page you specify in the web activation URL input. |
|  | supports phone activation specifies whether to enable the option to acquire activation code(s) through a phone number that you list in the phone activation number input. |
|  | web activation URL specifies the URL to the Web page that users must visit to obtain the activation code(s) they need to manually activate an add-on. |
|  | phone activation number specifies the phone number that users must call to obtain the activation code(s) they need to manually activate an add-on. |
|  | purchase page URL specifies the URL of the Web page through which users can purchase the add-on. This URL also is the page that the Purchase button in the activation dialog box displays in a Web browser. |
|  | custom hardware ID specifies the serial number of the hardware target to which you want to bind the license. When you bind a license to a specific custom hardware ID, this VI adds the ID to the license and if a user tries to use the license on a different target, the status of the license is invalid. By default, this VI does not bind the license to a specific serial number. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | activation successful? indicates whether the add-on was successfully activated. All inputs must be valid for successful activation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Product Activation Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Example

Refer to the Launch Activation Dialog VI in the labview\examples\addonlicensing\02 Launch Activation Dialog directory for an example of using the Product Activation VI.

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/removelicfromlibrary.html language=enus -->
## TOPIC 00019: Remove Licensing from Library VI

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/removelicfromlibrary.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/removelicfromlibrary.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Remove Licensing from Library VI

**Owning Palette:** [Third Party Licensing & Activation VIs](../addonlicensing/3rdpartylic_pal.html)

**Requires:** Third Party Licensing & Activation Toolkit

Removes the password and licensing information from the specified library so that the library is no longer password protected, which means the add-on is no longer licensed.

|  | Note The license file associated with the library must be present in the following directory: [Public App Data]\\National Instruments\\Partners\\company name\\Licenses, where [Public App Data] corresponds to the CommonAppDataFolder property and company name is the same value you specified when you licensed the add-on. Otherwise, LabVIEW returns error code –314519. |
| --- | --- |

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='removelicfromlibraryvi.gif']

|  | path to lvlib specifies the path, on the developer machine, to the LabVIEW library (.lvlib) that makes up the add-on. |
| --- | --- |
|  | current lvlib password specifies the current password to the LabVIEW library (.lvlib) that makes up the add-on. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | current lvlib password specifies the current password to the LabVIEW library (.lvlib) that makes up the add-on. |

#### Remove Licensing from Library Details

[[IMAGE alt='image' src='back_arrow.gif']](../addonlicensing/addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](../addonlicensing/addonlicensing.html)

#### Example

Refer to the Remove Licensing From Library VI in the labview\examples\addonlicensing\05 Removing Licensing from Library directory for an example of using the Remove Licensing from Library VI.

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/requirements_3rdpartylic.html language=enus -->
## TOPIC 00020: Requirements for Licensing Add-ons (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/requirements_3rdpartylic.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/requirements_3rdpartylic.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Requirements for Licensing Add-ons (Third Party Licensing & Activation Toolkit)

The procedure for licensing an add-on requires that you use LabVIEW in conjunction with certain other tools, depending on the type of add-on you want to license. Refer to the SoftwareKey website for more information about the products this topic mentions.

#### Requirements for Development Add-ons

When you license a [development add-on](addonlicensing.html) that consists of files others can use when developing in LabVIEW, the tools you must use also depend on the type of licensing you apply: standard licensing or advanced licensing.

##### Standard Licensing

The [procedure for applying standard licensing](overview_3rdpartylic.html) to a development add-on requires you to log in to an Instant SOLO Server™ account. You can sign up for an account after you begin the procedure.

|  | Note The National Instruments-managed Instant SOLO Server account that you use to apply standard licensing is unique to the standard-licensing tool. Thus, you must use a separate account to log in to any other tools that require an Instant SOLO Server account. |
| --- | --- |

You also must have an Internet connection to apply standard licensing.

##### Advanced Licensing

The [procedure for applying advanced licensing](overview_3rdpartylic.html) to a development add-on requires you to use the Concept Software Protection PLUS™ software in conjunction with LabVIEW. You must use the LFEdit™ (License File Editing) program, which is part of the Protection PLUS software, to create a product definition and a license file for the add-on.

(Optional) If you want to [enable automated online activation](../addonlicensing/proddefsolo_3rdpartylic.html) for the add-on, you must have an Instant SOLO Server account.

|  | Note If you have an NI-managed Instant SOLO Server account for use with the standard-licensing LabVIEW tool, you must use a different Instant SOLO Server account to enable automated online activation for an add-on. |
| --- | --- |

#### Requirements for Deployment Add-ons

The [procedure for licensing deployment add-ons](overview_deploylic.html) that you build in LabVIEW, such as executables, allows you to use the [Third Party Licensing & Activation](../addonlicensing/3rdpartylic_pal.html) VIs or the Concept Software Protection PLUS software. If you choose to use the Protection PLUS software, use the Instant PLUS™ program, which is part of the Protection PLUS software, to apply licensing to the add-on. If you use the Instant PLUS program, you also must have an Instant SOLO Server account.

Refer to the LabVIEW Add-on Dev Center on the NI Community for additional resources related to licensing deployment add-ons.

[[IMAGE alt='image' src='back_arrow.gif']](addonlicensing.html) [*Third Party Licensing & Activation Toolkit* Home](addonlicensing.html)

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/reusing_license.html language=enus -->
## TOPIC 00021: Editing Existing License Files (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/reusing_license.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/reusing_license.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Editing Existing License Files (Third Party Licensing & Activation Toolkit)

You can edit the details of licenses you [create with the Add-on Licensing Tool dialog box](proddef_standard.html), and then apply the updated license to an add-on.

|  | Note The functionality this topic describes is available only in LabVIEW 2010 and later. |
| --- | --- |

Complete the following steps to access an existing license file stored in your [Instant SOLO Server](requirements_3rdpartylic.html) account.

1. Select Tools»Add-on Licensing Tool to display the Add-on Licensing Tool dialog box.
2. Log in to your Instant SOLO Server account.
3. Select Select an add-on to license .
4. Click the Edit button beside the name of the add-on whose license details you want to edit.
5. Update the fields whose values you want to change.

|  | Note Refer to the Developer Zone at ni.com/zone or click the Help button in the Add-on Licensing Tool dialog box for more information about completing the fields in the dialog box. |
| --- | --- |

<!--NI_TOPIC bundle=labview-third-party-licensing-and-activation-toolkit-api-ref path=addonlicensing/tplatoolkit_error_codes.html language=enus -->
## TOPIC 00022: Error Codes (Third Party Licensing & Activation Toolkit)

- bundle_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- source_path: `addonlicensing/tplatoolkit_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-third-party-licensing-and-activation-toolkit-api-ref/raw/resource/enus/addonlicensing/tplatoolkit_error_codes.html
- document_id: `labview-third-party-licensing-and-activation-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Third Party Licensing & Activation Toolkit)

The [Third Party Licensing & Activation Toolkit](../addonlicensing/3rdpartylic_pal.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −314528 | The library you are trying to remove licensing from is currently not activated. To remove licensing from this library, please activate it first. |
| −314527 | The library you are trying to remove licensing from does not have licensing enabled. |
| −314526 | Activation URL must be of the form "/path_to_solo/unlock/getcode.asp". Check for a leading "/" in the URL. The activation URL is the URL on the activation server where the getcode.asp script file resides. |
| −314525 | Activation server address must be a SOLO server address of the form "server_path". Do not include the "http://" or "https://" prefix. |
| −314524 | The KEYLIB32.DLL on your machine could not be verified. The KEYLIB32.DLL on your machine could not be verified. This DLL is used for licensing purposes. You will need to acquire a valid version of the DLL from your application vendor or from SoftwareKey before you can use the software. |
| −314523 | Missing the input for the LabVIEW library's new password. |
| −314522 | Product information URL must be of the form "http(s)://path_to_webpage". |
| −314521 | Product purchase page URL must be of the form "http(s)://path_to_webpage". |
| −314520 | License file specified could not be opened. Check the password. The license file specified could not be opened. The main reason this may occur is because the password is incorrect. You should also check that the path you have chosen is a license file. |
| −314519 | Path to license file is invalid. |
| −314518 | No activation methods have been specified. You must specify at least one method for activation. |
| −314517 | Phone activation number is invalid. |
| −314516 | Web activation URL must be of the form "http(s)://path_to_webpage". |
| −314515 | URL for automated online activation must be a SOLO Server URL in the form "http(s)://path_to_solo/unlock". |
| −314514 | Path to library is invalid. |
| −314513 | Missing product version input. |
| −314512 | Missing product name input. |
| −314511 | Missing company name input. |
| −314502 | Command line arguments do not specify the add-on(s) to be registered. |
| −314501 | Could not find the LabVIEW installation directory from the registry. |
| −314500 | The Third Party Licensing & Activation Toolkit is supported only on the Windows platform. This toolkit is supported only on the Windows platforms because the implementation uses Windows-specific operating systems calls and libraries. To use this toolkit, you must use LabVIEW for Windows. |
