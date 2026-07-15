# NI DOCUMENT BUNDLE: labview-nxg-rt-module-designing-application

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-rt-module-designing-application start=1 end=4 -->
<!--NI_TOPIC bundle=labview-nxg-rt-module-designing-application path=addremovesw.html language=enus -->
## TOPIC 00001: Managing Software on a Real-Time Target

- bundle_id: `labview-nxg-rt-module-designing-application`
- source_path: `addremovesw.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-designing-application/raw/resource/enus/addremovesw.html
- document_id: `labview-nxg-rt-module-designing-application`
- page_type: `leaf`
- content_type: `task`
- source_description: Install the LabVIEW Real-Time Module and other driver software on the remote target. In the Live view of SystemDesigner, select the device for which you want to manage software. On the Item tab of the configuration pane, expand the Installed software section and click Manage software... to launch th

Managing Software on a Real-Time
 Target

Install the LabVIEW Real-Time Module and other driver software on the remote
 target.

1. In the Live view of SystemDesigner, select the device for which you want to
 manage software.
2. On the Item tab of the configuration pane, expand the
 Installed software section and click
 Manage software... to launch the dialog.
3. Use the dialog to complete the following tasks:
  1. [Apply a
 base system image to your target.](/csh?topicname=formatrt.html)
  2. [Select
 a programming environment to use on your target.](/csh?topicname=programenv.html)
  3. [Install software packages on your target.](/csh?topicname=installpkg.html)

<!--NI_TOPIC bundle=labview-nxg-rt-module-designing-application path=formatrt.html language=enus -->
## TOPIC 00002: Applying Base System Images to the RT Target

- bundle_id: `labview-nxg-rt-module-designing-application`
- source_path: `formatrt.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-designing-application/raw/resource/enus/formatrt.html
- document_id: `labview-nxg-rt-module-designing-application`
- page_type: `leaf`
- content_type: `task`
- source_description: In the Manage Software dialog, select a base system image to apply to the target. A base system image allows you to manage NI software through feeds located on ni.com.If you are using older software and want to proceed with a legacy installation, the dialog will refer you to NI MAX to continue. Sele

Applying Base System Images to the RT
 Target

In the Manage Software dialog, select a base system image to apply to the target.

Note

1. Select a base system image to apply to the target and click
 OK.
2. If the dialog prompts you to format the target, click
 Format. 
 org.dita.html5/xsl/topic.xsl 455Note Formatting erases all
 installed software and user data from the target but retains the network
 settings.

After you select a base system image, select
 a programming environment to use on the target.

Parent topic:

Managing Software on a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-designing-application path=installpkg.html language=enus -->
## TOPIC 00003: Installing Packages on the Target

- bundle_id: `labview-nxg-rt-module-designing-application`
- source_path: `installpkg.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-designing-application/raw/resource/enus/installpkg.html
- document_id: `labview-nxg-rt-module-designing-application`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Manage Software dialog, install packages on the target based on the programming environment you selected. Available packages are filtered to be compatible with your target and the programming environment. Use the following table to determine how to install packages on the target based on whet

Installing Packages on the Target

In the Manage Software dialog, install packages on the target based on the programming
 environment you selected.

Note

Use the following table to determine how to install packages on the target based on
 whether the target and/or host PC have internet access.

| Scenario | Package Installation Instructions |
| --- | --- |
| The target has internet access. | Select the packages you want to install on the target and click Review. After you review your selections, click Continue to complete the installation process. After the package installation is complete, close the dialog window. |
| The target and host PC both have internet access and the offline repository is installed on the host PC. | Follow the prompts to choose between installing the packages from ni.com or retrieving packages from the local repository on the host PC. Select the packages you want to install on the target and click Review. After you review your selections, click Continue to complete the installation process. After the package installation is complete, close the dialog window. |
| The host PC has internet access but the target does not. The packages are available on the host. | Follow the prompts to choose between allowing the target to securely access ni.com through the host computer, or retrieving the packages from the local repository on the host PC. Select the packages you want to install on the target and click Review. After you review your selections, click Continue to complete the installation process. After the package installation is complete, close the dialog window. |
| The host PC has internet access but the target does not. The required packages are not yet installed on the host. | Follow the prompts to allow the target to securely access ni.com through the host PC. Select the packages you want to install on the target and click Review. After you review your selections, click Continue to complete the installation process. After the package installation is complete, close the dialog window. |
| Neither the host nor the target has internet access. | Follow the troubleshooting steps that appear in the software wizard dialog to install the required packages. Select the packages you want to install on the target and click Review. After you review your selections, click Continue to complete the installation process. After the package installation is complete, close the dialog window. |

Parent topic:

Managing Software on a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-designing-application path=programenv.html language=enus -->
## TOPIC 00004: Selecting a Programming Environment

- bundle_id: `labview-nxg-rt-module-designing-application`
- source_path: `programenv.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-designing-application/raw/resource/enus/programenv.html
- document_id: `labview-nxg-rt-module-designing-application`
- page_type: `leaf`
- content_type: `task`
- source_description: In the Manage Software dialog, select the programming environment you want to use on the target. The programming environment you choose depends on where your application was developed and which run-time version you want to use on the target.The programming environment and run-time version you choose

Selecting a Programming Environment

In the Manage Software dialog, select the programming environment you want to use on the
 target.

Note

1. Select the programming environment you want to use on the target.
2. If you selected LabVIEW, select a run-time version.

Note

Parent topic:

Managing Software on a Real-Time Target
