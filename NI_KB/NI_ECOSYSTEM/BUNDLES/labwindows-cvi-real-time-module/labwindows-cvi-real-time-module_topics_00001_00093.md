# NI DOCUMENT BUNDLE: labwindows-cvi-real-time-module

<!--NI_BUNDLE_CHUNK bundle=labwindows-cvi-real-time-module start=1 end=93 -->
<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/avoiding_shared_resources.html language=enus -->
## TOPIC 00001: Avoiding Shared Resources

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/avoiding_shared_resources.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/avoiding_shared_resources.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Avoiding Shared Resources

In LabWindows/CVI, there are resources that two or more threads might need to share. Shared resources can cause jitter and prevent applications from taking advantage of multiple CPUs. Common examples of shared resources include the following:

- Thread safe variables (Utility Library)
- Thread locks (Utility Library)
- The memory manager
- Single-threaded DLLs

If a thread uses a shared resource, the thread acquires an operating system mutex around the resource to protect the resource from access by other threads. A *mutex* can be held only by one thread at a time so that other threads may not access the associated resource. If a higher priority thread preempts a lower priority thread and attempts to use a locked resource, the higher priority thread must wait because the shared resource is not available. The lower priority thread becomes more important than the higher priority thread because it must finish its work and release the shared resource before the higher priority thread can proceed. This scenario is a *priority inversion* and can affect determinism.

#### Memory Allocations and Preallocating Arrays

When a thread allocates memory, the thread accesses the memory manager. The memory manager allocates memory for data storage. The memory manager is a shared resource and might be locked by a mutex for up to several milliseconds. Allocating memory within deterministic code can affect the determinism of the code.

If you are using arrays in deterministic loops, you can reduce jitter by preallocating the arrays before entering the loops.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/backingrestoringreplicating.html language=enus -->
## TOPIC 00002: Backing Up, Restoring, and Replicating RT Targets

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/backingrestoringreplicating.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/backingrestoringreplicating.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Backing Up, Restoring, and Replicating RT Targets

You can use RT target disk images to backup, restore, and replicate RT targets. An RT target disk image is a copy of the file contents of the primary RT target hard drive.

There are two different methods you can use to create and apply RT target disk images. For networked RT targets, you can use the programmatic method, which involves using the functions in the System Replication class of the [Real-Time Utility Library](../rtutillib/rtutillibtree.htm) on the host computer. For USB-enabled RT targets, you can use the USB method, which involves booting from an RT Desktop PC Utility USB drive and using the **National Instruments Real-Time Desktop PC Utility Collection** menu.

|  | Note You cannot use the programmatic method to apply an image created with the USB method. You also cannot use the USB method to apply an image created with the programmatic method. |
| --- | --- |

For more information about creating and applying RT target disk images programmatically, refer to the [CreateRTSystemImage](../rtutillib/cvicreatertsystemimage.htm) and [ApplyRTSystemImage](../rtutillib/cviapplyrtsystemimage.htm) functions.

#### Backing Up RT Targets with a USB Drive

After you install the necessary software components and drivers on an RT target and deploy an RT application on the target, you can create a disk image of the target. You can use this image to restore or replicate the original RT target.

##### Creating RT Target Disk Images

Complete the following steps to create and store an RT target disk image on an RT Desktop PC Utility USB Drive.

1. Boot the RT target from the utility drive .
2. Select Backup, Restore, or Replicate the Real-Time System from the National Instruments Real-Time Desktop PC Utility Collection menu.
3. Select Backup system to default folder to clear the default disk image folder on the USB drive and create the new disk image in the default disk image directory. You also can select Backup system to unique folder to create the disk image in a unique folder on the USB drive.
4. When you finish using the USB utility drive, remove the USB drive and update any BIOS settings you changed when you configured the RT target to boot from the utility drive . If you want to boot back into a LabVIEW RT installation on the hard drive, you must ensure that you restore the Boot Configuration from Windows/Other OS to its original value.

#### Restoring and Replicating RT Targets with a USB Drive

You can apply RT target disk images to restore and replicate RT targets.

To restore a previously backed-up RT target in the event of a hard drive failure, apply the backup disk image to the target. To replicate an RT target, apply an RT target disk image created from the original target to other RT targets of the same model code. You can use the [GetRTSystemInfo](../rtutillib/cvigetrtsysteminfo.htm) function to find the model code of an RT target.

If you need a target to run an application on restart after applying a disk image, you must ensure the application was deployed to the original target before the disk image was created. To ensure that a target runs as expected after applying the disk image, you must test the original target before creating the disk image.

|  | Note Before attempting to apply an RT target disk image, ensure that the RT target can boot the real-time operating system. Before attempting to apply an RT target disk image to an unconfigured RT Desktop PC target, follow the instructions in the Using Desktop PCs as RT Targets with the Real-Time Module manual. |
| --- | --- |

##### Applying an RT Target Disk Image

Complete the following steps to apply an RT target disk image from an RT Desktop PC Utility USB drive.

1. Boot the RT target from the utility drive .
2. Select Backup, Restore, or Replicate the Real-Time System from the National Instruments Real-Time Desktop PC Utility Collection menu.
3. Select Restore or Replicate a Real-Time System from the National Instruments Real-Time Desktop PC Utility Collection menu.
4. Select Restore system from default folder to apply the disk image stored in the default disk image folder on the USB drive. You also can select Select an image to restore to apply an image from a unique directory on the USB drive.
5. When you finish using the USB utility drive, remove the USB drive and update any BIOS settings you changed when you configured the RT target to boot from the utility drive . If you want to boot back into a LabVIEW RT installation on the hard drive, you must ensure that you restore the Boot Configuration from Windows/Other OS to its original value.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/bootingintolvrt.html language=enus -->
## TOPIC 00003: Booting the RT Target into LabVIEW RT

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/bootingintolvrt.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/bootingintolvrt.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Booting the RT Target into LabVIEW RT

Before you begin configuration, make sure your remote system is booted into LabVIEW Real-Time. If your RT target came with only LabVIEW Real-Time preinstalled on its hard drive, the system is already set up to boot into LabVIEW Real-Time. Many NI RT targets have DIP switches or BIOS settings for booting into LabVIEW Real-Time. For more information, refer to the *Booting Into the LabVIEW Real-Time Module* topic in the *Measurement & Automation Explorer Help*. You can permanently format the hard drive and configure it to boot directly into RT using the **Tools»Desktop PC Utility USB Drive** command in MAX.

If you are converting a desktop computer to an RT target, refer to the Using Desktop PCs as RT Targets with the LabWindows/CVI Real-Time Module document for information about booting into LabVIEW RT.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/bootingtargetfromusb.html language=enus -->
## TOPIC 00004: Booting an RT Target from an RT Desktop PC Utility USB Drive

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/bootingtargetfromusb.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/bootingtargetfromusb.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Booting an RT Target from an RT Desktop PC Utility USB Drive

The steps for configuring an RT target to boot from an RT Desktop PC Utility USB Drive differ depending on the type of RT target.

|  | Note Refer to the Measurement & Automation Explorer Help for information about creating an RT Desktop PC Utility Drive. |
| --- | --- |

#### NI PXI, Industrial Controller, and Stand-Alone CompactDAQ RT Targets

Complete the following steps to boot these NI RT targets from an RT Desktop PC Utility USB Drive.

1. Connect a keyboard and monitor to the RT target.
2. Restart the target. As it boots up, hold the <Del> key to boot into the BIOS.
3. Set Legacy USB Support to Enabled . Depending on the RT target, you might need to save changes and restart the RT target after setting this option.
4. Locate the Boot Configuration setting and write it down. After you finish using the utility drive, you will return the Boot Configuration to this setting so the controller boots into the proper OS.
5. Set Boot Configuration to Windows/Other OS . Depending on the RT target, you might need to save changes and restart the RT target after setting this option.
6. Set the controller to boot from the USB drive before the hard drive. Depending on the RT target, you might need to save changes and restart the RT target after setting this option.
7. If the BIOS contains an option for configuring the USB drive as a hard disk, set this option. If the BIOS does not contain this option, no action is necessary.
8. Ensure the RT Desktop PC Utility USB Drive is inserted into the controller.
9. Exit the BIOS while saving these changes. Select Yes if you are prompted to confirm. The RT target restarts and boots from the utility USB drive.

|  | Note Legacy USB support causes severe jitter in RT applications. When you are ready to deploy an application to the RT target, re-enter the BIOS and disable this setting. Other BIOS settings also reduce the performance of RT applications. |
| --- | --- |

#### Desktop RT Targets

Complete the following steps to boot a desktop RT target from an RT Desktop PC Utility USB Drive.

|  | Note Instructions for entering and configuring the BIOS differ by PC manufacturer. Refer to the PC user manual for information about completing the following steps. |
| --- | --- |

1. Restart the desktop PC and enter the BIOS.
2. Configure the BIOS to boot from the USB drive before the hard drive.
3. Insert the RT Desktop PC Utility USB Drive and exit the BIOS while saving changes.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/bp_nilm.html language=enus -->
## TOPIC 00005: Activating Your Software

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/bp_nilm.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/bp_nilm.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Activating Your Software

##### How do I activate my software?

Use the NI Activation Wizard to obtain an activation code for your software. You can launch the NI Activation Wizard two ways:

- Launch the product and choose to activate your software from the list of options presented.
- Launch NI License Manager by selecting Start»All Programs»National Instruments»NI License Manager or from NI Launcher in Windows 8. Click the Activate button in the toolbar.

|  | Notes If your software is a part of a Volume License Agreement (VLA), contact your VLA administrator for installation and activation instructions. NI software for OS X and Linux operating systems does not require activation. |
| --- | --- |

##### What is activation?

Activation is the process of obtaining an activation code to enable your software to run on your computer. An *activation code* is an alphanumeric string that verifies the software, version, and computer ID to enable features on your computer. Activation codes are unique and are valid on only one computer.

##### What is the NI Activation Wizard?

The NI Activation Wizard is a part of NI License Manager that steps you through the process of enabling software to run on your machine.

##### What information do I need to activate?

You need your product serial number, user name, and organization. The NI Activation Wizard determines the rest of the information. Certain activation methods may require additional information for delivery. This information is used only to activate your product. Complete disclosure of the National Instruments software licensing information privacy policy is available at ni.com/activate/privacy. If you optionally choose to register your software, your information is protected under the National Instruments privacy policy, available at ni.com/privacy.

##### How do I find my product serial number?

Your serial number uniquely identifies your purchase of NI software. You can find your serial number on the Certificate of Ownership included in your software kit. If your software kit does not include a Certificate of Ownership, you can find your serial number on the product packing slip or on the shipping label.

If you have installed a previous version using your serial number, you can find the serial number by selecting the **Help»About** menu item within the application or by selecting your product within NI License Manager (**Start»All Programs»National Instruments»NI License Manager** or from NI Launcher in Windows 8). You can also contact your local National Instruments branch at ni.com/contact.

##### What is a Computer ID?

The computer ID contains unique information about your computer. National Instruments requires this information to enable your software. You can find your computer ID through the NI Activation Wizard or by using NI License Manager, as follows:

1. Launch NI License Manager by selecting Start»All Programs»National Instruments»NI License Manager or from NI Launcher in Windows 8.
2. Click the Display Computer Information button in the toolbar.

For more information about product activation and licensing refer to ni.com/activate.

##### How can I evaluate NI software?

You can install and run most NI application software in evaluation mode. This mode lets you use a product with certain limitations, such as reduced functionality or limited execution time. Refer to your product documentation for specific information on the product's evaluation mode.

##### Moving Software After Activation

To transfer your software to another computer, install and activate it on the second computer. You are not prohibited from transferring your software from one computer to another and you do not need to contact or inform NI of the transfer. Because activation codes are unique to each computer, you will need a new activation code. Refer to the [How do I activate my software?](#activate) section of this topic to learn how to acquire a new activation code and reactivate your software.

##### Deactivating a Product

To deactivate a product and return the product to the state it was in before you activated it, right-click the product in the NI License Manager tree and select **Deactivate**. If the product was in evaluation mode before you activated it, the properties of the evaluation mode may not be restored.

##### Using Windows Guest Accounts

NI License Manager does not support Microsoft Windows Guest accounts. You must log in to a non-Guest account to run licensed NI application software.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/builddeterapps_rt.html language=enus -->
## TOPIC 00006: Creating Deterministic Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/builddeterapps_rt.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/builddeterapps_rt.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Creating Deterministic Applications

Determinism is the characteristic of a system that describes how consistently it responds to external events or performs operations within a given time limit. Jitter is a measure of the extent to which execution timing fails to meet deterministic expectations. If you intend to build deterministic applications to execute deterministic tasks, use the programming techniques in this section to reduce jitter in applications running on RT targets.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/commapps_rttarget.html language=enus -->
## TOPIC 00007: Sharing Data Remotely across a Network

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/commapps_rttarget.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/commapps_rttarget.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Sharing Data Remotely across a Network

After creating applications that run on an RT target, you might need to share data with applications running on other targets, such as the host computer.

Using remote communication methods, an application running on an RT target can share data with applications running on other targets across a network. You might use remote communication for the following reasons:

- You want to exchange data between a host computer and the RT target to provide a user interface.
- You want to perform additional data processing or logging on a different target.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringanrtapp.html language=enus -->
## TOPIC 00008: Configuring an RT Application

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringanrtapp.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringanrtapp.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring an RT Application

After you [configure the RT target](configuringrttarget.html), you can create an RT application on the host computer and then run the application on an RT target. The applications that you create with the LabWindows/CVI Real-Time Module are DLLs.

Complete the following steps to create a DLL and specify an RT target directly from LabWindows/CVI:

1. Create a project in LabWindows/CVI using RTmain instead of main as the entry-point function for the program. Select Edit»Insert Construct»RTmain to insert the RTmain code into the program source.
2. Select an active configuration for the project from the Build»Configuration submenu.
3. Select Build»Target Type»Dynamic Link Library to configure the project to generate a DLL.
4. Select Build»Target Settings to open the Target Settings dialog box. Select Real-time only in the Run-time support option. If you specify this option, LabWindows/CVI does not link to the entire set of LabWindows/CVI libraries but instead links to only those libraries supported on an RT system . 
Configure the other options in the Target Settings dialog box and then click OK to exit the dialog box.
5. Select Build»Build to create the DLL.

You also can use a project template to create an RT DLL. The project template includes basic settings for RT projects described in the preceding section. To select a project template, select **File»New»Project from Template**. In the New Project from Template dialog box, select **Real-Time Target Application**.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringio.html language=enus -->
## TOPIC 00009: Configuring I/O

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringio.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringio.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring I/O

You must configure any National Instruments I/O devices before you can target them from a LabWindows/CVI RT application. For information about how to correctly configure I/O devices, refer to the documentation for that hardware.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringnetworksettings.html language=enus -->
## TOPIC 00010: Configuring Network Settings

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringnetworksettings.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringnetworksettings.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring Network Settings

|  | Note For the initial configuration, you must connect networked RT targets to the same network subnet as the host computer from which you launch MAX. |
| --- | --- |

Complete the following steps to configure network settings:

1. Connect the RT target to the network and power on the target.
2. Launch MAX and expand the Remote Systems item in the MAX configuration tree.
3. Select the RT target from the Remote Systems list. Some RT targets will be listed with an automatically configured name or IP address while other targets will be listed as 0.0.0.0. .
4. Specify a name for the RT target in the System Settings tab.
5. Configure the IP address settings in the Network Settings tab using one of the following options:
  - Select the DHCP or Link Local item from the Configure IPv4 Address option to obtain an IP address automatically.
  - Select the Static item from the Configure IPv4 Address option and specify an IP address.
6. Click Save to commit the changes.
7. Click Yes to reboot the RT target when prompted.

If your previously configured RT target is on another subnet and does not appear under the **Remote Systems** item, you must add the target manually. Complete the following steps to add the RT target:

1. Right-click the Remote Systems item and select Create New .
2. Select the target type and click Next .
3. Enter the host name or IP address of the device. You can obtain the host name or IP address of the RT target by running MAX from a computer on the same subnet as the target or by connecting a monitor to the target and viewing the information displayed when the target boots.
4. Click Finish . MAX adds the device to the Remote Systems list.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringrttarget.html language=enus -->
## TOPIC 00011: Configuring an RT Target

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringrttarget.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringrttarget.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring an RT Target

After you install LabWindows/CVI and the RT module, you must use NI Measurement & Automation Explorer (MAX) to configure the RT target and to install software and drivers on the RT target. MAX provides access to NI devices and systems and can communicate with networked RT targets, or remote systems, located on the same subnet as the computer running MAX. You also can use the NI System Configuration API for LabWindows/CVI to programmatically configure your RT target. Refer to the *NI System Configuration LabWindows/CVI Function Reference Help*, located in the National Instruments\Shared\CVI\nisyscfg directory, for more information about using this API to interact with your RT target.

Complete the following steps to configure the RT target.

1. Boot the RT target into LabVIEW RT .
2. Configure network settings .
3. Install software on the RT target .
4. Configure I/O .
5. Configure system settings .
6. Configure time settings .

Refer to the *Measurement & Automation Explorer Help* for a complete tutorial about configuring the RT target. Select **Help»MAX Help** to access this help file, and then refer to the *MAX Remote Systems Help* section.

|  | Note The Measurement & Automation Explorer Help refers to the LabVIEW Real-Time Module. However, you can apply the same concepts when you use the LabWindows/CVI Real-Time Module. |
| --- | --- |

After you complete these steps, you can target the remote system from LabWindows/CVI.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringsystemsettings.html language=enus -->
## TOPIC 00012: Configuring System Settings

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringsystemsettings.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringsystemsettings.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring System Settings

Complete the following steps to configure system settings:

1. Select the System Settings tab to configure system-level settings for the RT target.
2. Configure the Locale option to match the language you use for strings in your RT application. This option is available only when you install the Language Support for LabVIEW RT component on the RT target. This option determines the code page that LabWindows/CVI uses when processing strings containing ASCII characters above 127 or multibyte characters.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/configuringtimesettings.html language=enus -->
## TOPIC 00013: Configuring Time Settings

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/configuringtimesettings.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/configuringtimesettings.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Configuring Time Settings

Complete the following steps to configure time settings:

1. Select the Time Settings tab to configure date and time settings for the RT target.
2. Use the Time Zone option to configure the time zone for the RT target. You can use this setting with time and date functions to provide accurate time information relative to the time zone setting.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/createmultithreadapps.html language=enus -->
## TOPIC 00014: Creating Deterministic Applications with the Real-Time Module

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/createmultithreadapps.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/createmultithreadapps.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Creating Deterministic Applications with the Real-Time Module

Single-CPU computers achieve multitasking by running one application for a short amount of time and then running other applications for short amounts of time. As long as the amount of processor time allocated for each application is small enough, computers appear to have multiple applications running simultaneously. Systems with multiple CPUs, on the other hand, can achieve true parallelism.

Multithreading applies the concept of multitasking to a single application by breaking it into smaller tasks that execute for short amounts of time in different threads. A *thread* is a completely independent flow of execution within an application. Multithreaded applications maximize the efficiency of the processor because the processor does not sit idle if there are other threads ready to run. An application that reads and writes from a file, performs I/O, or polls the user interface for activity can benefit from multithreading because it can use the processor to run other tasks during breaks in these activities.

The real-time operating system (RTOS) on NI RT targets uses a combination of round robin and preemptive scheduling to execute threads. Round robin scheduling applies only to threads of equal priority. Equal shares of processor time are allocated among equal priority threads. For example, a thread is allotted 10 ms to run. The processor executes all the tasks it can in 10 ms and whatever is incomplete at the end of that period must wait to complete during the next allocation of time for that thread. Preemptive scheduling means that any higher priority thread that needs to execute immediately pauses execution of all lower priority threads and begins to execute. A thread with the highest possible priority preempts all lower priority threads. If you have multiple threads with the same priority, and that priority level is less than 9, the threads use round robin scheduling. If you have multiple threads with the same priority, and the priority level is 9 or higher, the threads do not use round robin scheduling. A thread with the highest possible priority level continues running indefinitely until it cooperatively yields the processor for another thread.

#### Dividing Tasks to Create Deterministic Multithreaded Applications

Deterministic applications depend on deterministic tasks to complete on time, every time. Therefore, deterministic tasks need dedicated processor resources to ensure timely completion. Dividing tasks helps to ensure that each task receives the processor resources it needs to execute on time.

Separate deterministic tasks from all other tasks to ensure deterministic tasks receive enough processor resources. For example, if a control application acquires data at regular intervals and stores the data on disk, you must handle the timing and control of the data acquisition deterministically. However, storing the data on disk is inherently a non-deterministic task because file I/O operations have unpredictable response times that depend on the hardware and the availability of the hardware resource. You can use [asynchronous timers](creatingdeterappsusingasynctimers.html) and [threads](deterministic_apps_func_priorities.html) with different priorities to control the execution and timing of deterministic tasks.

|  | Note Within deterministic tasks, ensure that each operation receives dedicated processor resources by avoiding unnecessary parallelism. You can accomplish this by not dividing the deterministic task into multiple threads unnecessarily. In a multiple-CPU system, avoid creating more parallel operations than the number of available CPUs. Because it is impossible to determine the execution order of parallel operations, unnecessary parallelism can impede determinism. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/creatingdeterappsusingasynctimers.html language=enus -->
## TOPIC 00015: Creating Deterministic Applications Using Asynchronous Timers

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/creatingdeterappsusingasynctimers.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/creatingdeterappsusingasynctimers.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Creating Deterministic Applications Using Asynchronous Timers

Separate deterministic tasks from non-deterministic tasks and place deterministic tasks in different threads to ensure they receive enough processor resources. You can prioritize the threads to control the amount of processor resources each thread receives.

You can place a task in a thread by writing a callback function that accomplishes a particular task and creating an [asynchronous timer](/csh?topicname=toolslib/toolslibasychronous_timers_control.htm) to call that function. The asynchronous timer calls the function repeatedly at the period and priority you specify. You can create an asynchronous timer using the functions in the Asynchronous Timer instrument driver. Call [NewAsyncTimerWithPriority](/csh?topicname=toolslib/functionreference/cvinewasynctimerwithpriority.htm) to create an asynchronous timer with a particular period and priority.

The priority of the asynchronous timer determines the priority of the thread that calls the timer callback. The priority can be any value from -15 to 15. The default priority of a thread in the system is 0. The operating system scheduler runs at priority level 9. Any threads running at a priority level equal to or higher than 9 are not subject to timeslicing by the scheduler and will run until they yield the CPU or are preempted by a higher priority thread.

#### Cooperatively Yielding Asynchronous Timer Execution

Because of the preemptive scheduling used by the real-time operating system (RTOS), higher priority threads can monopolize processor resources. A high priority asynchronous timer might use all of the processor resources, not allowing lower priority threads to execute.

You must create asynchronous timers with a period large enough to run the callback function and still have idle time before the next iteration to allow lower priority threads to execute. You must do this while maintaining the determinism required by your application. By configuring asynchronous timers in this manner, you can ensure that the timer cooperatively yields processor resources.

|  | Note If your application is running on a multiple-CPU system and has a high priority asynchronous timer handling a deterministic task, consider manually assigning the timer to a dedicated CPU. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/creatingrtapps.html language=enus -->
## TOPIC 00016: Creating Real-Time Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/creatingrtapps.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/creatingrtapps.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Creating Real-Time Applications

This section includes information about the steps involved in creating real-time applications with the LabWindows/CVI Real-Time Module.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/cvilibsinrtapps.html language=enus -->
## TOPIC 00017: Using LabWindows/CVI Libraries in RT Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/cvilibsinrtapps.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/cvilibsinrtapps.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Using LabWindows/CVI Libraries in RT Applications

To build a DLL that you can run on a real-time (RT) target, you must select **Real-time only** in the **Run-time support** option of the [Target Settings](/csh?topicname=cvi/usermanual/prjdlltargetsettings.htm) dialog box.

If you select **Real-time only**, the project does not link to the entire set of LabWindows/CVI libraries but instead links to a smaller set of LabWindows/CVI built-in library [functions](cvilvrtfunctions.html) that are supported in RT applications.

#### LabWindows/CVI Libraries

The following libraries and functions are supported in RT applications:

- Analysis Library or Advanced Analysis Library
- ANSI C Library, with the following exceptions:
 [IMAGE alt='Note' src='note.gif']
**Note** Only the "C" locale is recognized, and all case-sensitive functions, such as stricmp and tolower, perform conversions only from characters a-z to characters A-Z, and vice-versa, and perform comparisons using only this set of characters. Locale-specific case sensitivity is not honored.
  - Any functions that interact with the keyboard or that require user input are not available.
  - The multibyte to wide-character conversion functions mbtowc and mbstowcs are not available. The wide-character to multibyte conversion functions wctomb and wcstombs are not available.
- Formatting and I/O Library, with the following exceptions:
  - ArrayToFile
  - FileToArray
- Internet Library, with the following exceptions:

 [IMAGE alt='Note' src='note.gif']
**Note** The Internet Library is available only in the LabWindows/CVI Full Development System.
  - InetLaunchDefaultWebBrowser
  - InetPing
- Network Streams Library
- Network Variable Library, with the following exception:
  - CNVVariableEngineIsRunning
- Real-Time Utility Library, with the following exceptions:
  - GetRTSystemInfo
  - FindAllRTSystemsOnSubnet
  - RTSystemSelectPopup
  - System Configuration class
  - System Replication class
- TCP Support Library
- TDM Streaming Library, with the following exceptions:
  - TDMS_AdvancedAsyncRead
  - TDMS_AdvancedAsyncWrite
  - TDMS_ConfigureAsyncReads
  - TDMS_ConfigureAsyncWrites
  - TDMS_GetAsyncReadStatus
  - TDMS_GetAsyncWriteStatus
  - TDMS_ReserveFileSize
- UDP Support Library
- The following functions in the User Interface Library:
  - PostDeferredCall
  - PostDeferredCallToThread
  - ProcessSystemEvents
- The following functions in the Utility Library:
  - All functions in the Multithreading class
  - All functions in the Debugging and Run-time Error Reporting class, with the following exception:
    - CVIDynamicMemoryInfo
  - All functions in the Date/Time class
  - Beep
  - Cls
  - CVIRTEHasBeenDetached
  - GetDir
  - InStandaloneExecutable
  - RoundRealToNearestInteger
  - SetDir
  - TruncateRealNumber

|  | Note All the functions that are supported in RT applications are multithread safe. |
| --- | --- |

#### LabWindows/CVI Tools Library (Toolslib) Instrument Drivers

The following Toolslib instrument drivers are supported in RT applications:

- Asynchronous Timers
- Reading/Writing .ini–Style Files, with the following exceptions:
  - Ini_ReadFromRegistry
  - Ini_WriteToRegistry
- Regular Expressions
- The following functions in the Programmer's Toolbox:
  - All functions in the Miscellaneous class, with the following exceptions:
    - GetFileCLibTime
    - GetGeneralErrorString
    - InternationalFileTime
    - InternationalFileDate
    - NetworkVariablePopup
    - OpenDocumentInDefaultViewer
    - ShowHtmlHelp
    - StartPCSound
    - StopPCSound
  - All functions in the Time Conversions class
  - All functions in the String Handling class
  - All functions in the File class, with the following exceptions:
    - SaveBitmapToFile
    - SaveCtrlDisplayToFile
    - SavePanelDisplayToFile
  - All functions in the Searching and Sorting class
  - All functions in the Lists class
  - All functions in the Hash Tables class
  - All functions in the Memory Block Handles class
  - All functions in the Constants and Conversions class
  - All functions in the Special Double Precision Numbers and Functions class
  - All functions in the Callback Posting class, with the following exception:
    - PostDelayedCall
  - All functions in the Endianess class

#### Additional Libraries

You also can link a **Real-time only** project to the following libraries, which may require you to install additional components on the RT target.

- RS-232 Library —You must install NI-Serial on the RT target using the Remote Systems item in NI Measurement & Automation Explorer (MAX).
- Hardware Libraries —You must install the appropriate driver for any hardware library that you use in an RT application. The following hardware libraries are supported in RT applications:
  - VISA Library
  - NI-DAQmx Library
  - Traditional NI-DAQ Library ( with limitations )
  - NI-DMM
  - NI-Scope
  - NI-FGEN
  - NI-Switch
  - NI-HSDIO
  - NI-CAN

|  | Notes Additional driver support might have been added since this product was released. Contact National Instruments for an up-to-date list of supported drivers. If NI-DAQmx 8.0 or earlier is installed on the local computer and you link the project to the LabWindows/CVI NI-DAQmx Library, you must manually download the NI-DAQmx run-time DLL for RT (\\bin\\nicaip.dll) to the \\ni-rt\\system\\ folder on the RT target using FTP. You do not need to download this DLL if NI-DAQmx 8.1 or later is installed. |
| --- | --- |

If you [use an external compiler](/csh?topicname=cvi/programmerref/buildingprjinextcompiler.htm) and want to use functions that are supported in RT applications, include CVI*version*\extlib\msvc\cvi_lvrt.lib in the external compiler project instead of cvirt.lib and cvisupp.lib. Remember that when you use an external compiler, you link to that compiler's ANSI C library.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/cvilvrtfunctions.html language=enus -->
## TOPIC 00018: LabWindows/CVI Functions Supported in Real-Time Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/cvilvrtfunctions.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/cvilvrtfunctions.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI Functions Supported in Real-Time Applications

You must use the subset of LabWindows/CVI functions that are [supported in real-time (RT) applications](cvilibsinrtapps.html) when you create DLLs to run on RT targets. If you include a function in your real-time application that is not supported on RT, LabWindows/CVI generates a link error.

LabWindows/CVI supports a subset of ANSI C, Formatting and I/O, Internet, Network Variable, Real-Time Utility, TCP Support, TDM Streaming, UDP Support, and Utility Library functions in RT applications. LabWindows/CVI also supports functions in the following Tools Library (Toolslib) instrument drivers: Asynchronous Timers, 
Reading/Writing .ini–Style Files, Regular Expressions, and Programmer's Toolbox.

#### Supported Functions

LabWindows/CVI supports the following list of built-in library functions in RT applications.

|  | Note This list does not include functions in the Analysis Library, Advanced Analysis Library, or any of the hardware libraries supported on RT. |
| --- | --- |

**A**

AddCVITimeIntervals 

AddStringPrefix 

AddStringQuotes 

AddToCVIAbsoluteTime 

assert 

abort 

abs 

acos 

AppendString 

asctime 

asin 

atan 

atan2 

atexit 

atof 

atoi 

atoi64 

atol 

AvogadroConstant

**B**

BeingDebuggedByCVI 

Breakpoint 

BinSearch 

BinStrToUInt 

BinStrToULongLong 

bsearch

**C**

calloc 

ceil 

CelsiusToFahrenheit 

CelsiusToKelvin 

clearerr 

ClientTCPRead 

ClientTCPWrite 

clock 

close 

CloseCom 

CloseFile 

CloseWinsock 

Cls 

CmtDiscardLock 

CmtDiscardTSQ 

CmtDiscardTSV 

CmtDiscardThreadLocalVar 

CmtDiscardThreadPool 

CmtExitThreadPoolThread 

CmtFlushTSQ 

CmtGetCurrentThreadID 

CmtGetErrorMessage 

CmtGetLock 

CmtGetLockEx 

CmtGetMainThreadID 

CmtGetNumProcessors 

CmtGetTSQAttribute 

CmtGetTSQReadPtr 

CmtGetTSQWritePtr 

CmtGetTSVPtr 

CmtGetThreadLocalVar 

CmtGetThreadPoolAttribute 

CmtGetThreadPoolFunctionAttribute 

CmtInstallTSQCallback 

CmtInstallThreadPoolCallback 

CmtNewLock 

CmtNewTSQ 

CmtNewTSV 

CmtNewThreadLocalVar 

CmtNewThreadPool 

CmtPreAllocThreadPoolThreads 

CmtReadTSQData 

CmtReleaseLock 

CmtReleaseTSQReadPtr 

CmtReleaseTSQWritePtr 

CmtReleaseTSVPtr 

CmtReleaseThreadPoolFunctionID 

CmtScheduleThreadPoolFunction 

CmtScheduleThreadPoolFunctionAdv 

CmtSetTSQAttribute 

CmtSetTSV 

CmtSetThreadPoolAttribute 

CmtTerminateThreadPoolThread 

CmtUninstallTSQCallback 

CmtUninstallThreadPoolCallback 

CmtWaitForThreadPoolFunctionCompletion 

CmtWaitForThreadPoolFunctionCompletionEx 

CmtWriteTSQData 

CNSDataCreateArray 

CNSDataCreateScalar 

CNSDataCreateStruct 

CNSDataDiscard 

CNSDataGetArrayDimensions 

CNSDataGetArrayElementType 

CNSDataGetArrayValue 

CNSDataGetNumArrayDimensions 

CNSDataGetNumStructFields 

CNSDataGetScalarValue 

CNSDataGetStructFields 

CNSDataGetType 

CNSDiscardEndpoint 

CNSFinish 

CNSFlush 

CNSFreeMemory 

CNSGetEndpointAttribute 

CNSGetErrorDescription 

CNSNewArrayEndpoint 

CNSNewEndpoint 

CNSNewScalarEndpoint 

CNSReadArray 

CNSReadData 

CNSReadMultipleData 

CNSReadMultipleScalar 

CNSReadScalar 

CNSWriteArray 

CNSWriteData 

CNSWriteMultipleData 

CNSWriteMultipleScalar 

CNSWriteScalar 

CNVBrowse 
 
CNVBrowseNextItem 
 
CNVCheckDataQuality 
 
CNVCreateArrayDataValue 
 
CNVCreateAsyncReader 
 
CNVCreateBrowser 
 
CNVCreateBufferedSubscriber 
 
CNVCreateBufferedWriter 
 
CNVCreateReader 
 
CNVCreateScalarDataValue 
 
CNVCreateStructDataValue 
 
CNVCreateSubscriber 
 
CNVCreateWriter 
 
CNVDeleteProcess 
 
CNVDeleteVariable 
 
CNVDispose 
 
CNVDisposeBrowser 
 
CNVDisposeData 
 
CNVFinish 
 
CNVFreeMemory 
 
CNVGetArrayDataDimensions 
 
CNVGetArrayDataValue 
 
CNVGetConnectionAttribute 
 
CNVGetDataFromBuffer 
 
CNVGetDataQuality 
 
CNVGetDataQualityDescription 
 
CNVGetDataServerError 
 
CNVGetDataType 
 
CNVGetDataUTCTimestamp 
 
CNVGetErrorDescription 
 
CNVGetNumberOfStructFields 
 
CNVGetProcesses 
 
CNVGetVariables 
 
CNVGetRegisteredMachines 
 
CNVGetScalarDataValue 
 
CNVGetStructFields 
 
CNVGetTimestampInfo 
 
CNVGetVariableAttribute 
 
CNVNewProcess 
 
CNVNewVariable 
 
CNVNewVariableCollection 
 
CNVProcessExists 
 
CNVProcessIsRunning 
 
CNVPutDataInBuffer 
 
CNVRead 
 
CNVReadAsync 
 
CNVRegisterMachine 
 
CNVSetArrayDataValue 
 
CNVSetConnectionAttribute 
 
CNVSetScalarDataValue 
 
CNVSetVariableAttribute 

CNVStartProcess 
 
CNVStopProcess 
 
CNVUnregisterMachine 
 
CNVVariableExists 
 
CNVWrite 
 
CVNSetStructDataValue 
 
ComBreak 

ComFromFile 

CompareBytes 

CompareStrings 

CompareCVIAbsoluteTimes 

CompareCVIAbsoluteTimesWithTolerance 

CompareCVITimeIntervals 

CompareCVITimeIntervalsWithTolerance 

ComRd 

ComRdByte 

ComRdTerm 

ComSetEscape 

ComToFile 

ComWrt 

ComWrtByte 

ConfigureProcessorPool 

ConnectToTCPServer 

ConnectToTCPServerEx 

ConvertArrayType 

CopyBytes 

CopyString 

cos 

cosh 

CreateAndOpenTemporaryFile 

CreateUDPChannel 

CreateUDPChannelConfig 

CStringCompare 

CStringNoCaseCompare 

ctime 

CVIAbsoluteTimeFromCNVTime 

CVIAbsoluteTimeFromCVIANSITime 

CVIAbsoluteTimeFromCVIUILTime 

CVIAbsoluteTimeFromFILETIME 

CVIAbsoluteTimeFromLocalCalendar 

CVIAbsoluteTimeToCNVTime 

CVIAbsoluteTimeToCVIANSITime 

CVIAbsoluteTimeToCVIUILTime 

CVIAbsoluteTimeToFILETIME 

CVIAbsoluteTimeToLocalCalendar 

CVIRTEHasBeenDetached 

CVITimeIntervalFromSeconds 

CVITimeIntervalFromTimeUnit 

CVITimeIntervalToFractionalUnitTime 

CVITimeIntervalToSeconds 

CVITimeIntervalToTimeUnit

**D**

DateStr 

DebugPrintf 

DecrementCVIAbsoluteTime 

DecrementCVITimeInterval 

DegToRad 

Delay 

DelayWithEventProcessing 

DeleteAndRename 

difftime 

DisableBreakOnLibraryErrors 

DiscardAsyncTimer 

DisconnectFromTCPServer 

DisconnectTCPClient 

DisposeHandle 

DisposeRTSystemInfo 

DisposeUDPChannel 

div 

DivideCVITimeInterval 

DoAssert 

DoubleCompare

**E**

ElementaryCharge 

EnableBreakOnLibraryErrors 

eof 

ErrorPrintf 

Euler 

exit 

exp

**F**

fabs 

FahrenheitToCelsius 

fclose 

fdopen 

feof 

ferror 

FeetToMeters 

fflush 

fgetc 

fgetpos 

fgets 

FileExists 

FillBytes 

FindClosestColorInTable 

FindPattern 

FloatCompare 

floor 

FlushInQ 

FlushOutQ 

fmod 

Fmt 

FmtFile 

FmtOut 

fopen 

FP_Compare 

fprintf 

fputc 

fputs 

fread 

free 

freopen 

FreeRTUtilMemory 

frexp 

fscanf 

fseek 

fsetpos 

ftell 

fwrite

**G**

_getmbcp 

GallonsToLiters 

GetAllTCPHostAddresses 

GetAsyncTimerAttribute 

GetAsyncTimerResolution 

GetBreakOnFirstChanceExceptions 

GetBreakOnLibraryErrors 

GetBreakOnProtectionErrors 

getc 

getchar 

GetComConnectionState 

GetComLineStatus 

GetComStat 

GetCurrentCVIAbsoluteTime 

GetDir 

GetEnableResourceTracking 

getenv 

GetFileInfo 

GetFileWritability 

GetFmtErrNdx 

GetFmtIOError 

GetFmtIOErrorString 

GetHandleSize 

GetHostTCPSocketHandle 

GetInQLen 

GetOutQLen 

GetRS232ErrorString 

GetRTSystemInfo 

GetRTUtilErrorString 

gets 

GetSystemComHandle 

GetSystemDate 

GetSystemTime 

GetTCPErrorString 

GetTCPHostAddr 

GetTCPHostConnectionAddr 

GetTCPHostName 

GetTCPPeerAddr 

GetTCPPeerName 

GetTCPSystemErrorString 

GetTimeUS 

GetUDPAttribute 

GetUDPErrorString 

GetUDPSocketHandle 

gmtime 

GravitationalConstant

**H**

HalfPi 

HashTableClear 

HashTableCreate 

HashTableDispose 

HashTableFindItem 

HashTableGetAttribute 

HashTableGetItem 

HashTableInsertItem 

HashTableIteratorAdvance 

HashTableIteratorCreate 

HashTableIteratorDispose 

HashTableIteratorGetItem 

HashTableRemoveItem 

HashTableSetAttribute 

HasNonWhiteSpace 

HeapSort 

HostIsBigEndian 

HostIsLittleEndian

**I**

_ismbblead 
IncrementCVIAbsoluteTime 

IncrementCVITimeInterval 

InetFreeMemory 
 
InetFTPAutoRetrieve 

InetFTPAutoSend 
 
InetFTPChangeDir 
 
InetFTPClose 
 
InetFTPCommand 
 
InetFTPDelete 
 
InetFTPGetDir 
 
InetFTPGetDirList 
 
InetFTPLogin 
 
InetFTPLoginEx 
 
InetFTPMakeDir 
 
InetFTPReceiveData 
 
InetFTPRemoveDir 
 
InetFTPRename 
 
InetFTPRetrieveFile 
 
InetFTPSendData 
 
InetFTPSendFile 
 
InetFTPSetPassiveMode 
 
InetGetErrorMessage 
 
InetPop3Close 
 
InetPop3DeleteMessage 
 
InetPop3GetMessage 

InetPop3GetMessageInfo 
 
InetPop3GetMessageSize 
 
InetPop3GetNumMessages 
 
InetPop3Open 
 
InetPop3ParseMessageHeader 
 
InetResolveHostname 
 
InetSendMail 
 
InetTelnetClose 
 
InetTelnetOpen 
 
InetTelnetRead 
 
InetTelnetReadUntil 
 
InetTelnetRunScript 
 
InetTelnetWrite 
 
Ini_CopySection 

Ini_CopySectionEx 

Ini_DisableInternalSorting 

Ini_DisableSorting 

Ini_Dispose 

Ini_GetBoolean 

Ini_GetData 

Ini_GetDouble 

Ini_GetInt 

Ini_GetInt64 

Ini_GetPointerToRawString 

Ini_GetPointerToString 

Ini_GetRawStringCopy 

Ini_GetRawStringIntoBuffer 

Ini_GetStringCopy 

Ini_GetStringIntoBuffer 

Ini_GetUInt 

Ini_GetUInt64 

Ini_ItemExists 

Ini_LineOfLastAccess 

Ini_New 

Ini_NthItemName 

Ini_NthSectionName 

Ini_NumberOfItems 

Ini_NumberOfSections 

Ini_PutBoolean 

Ini_PutData 

Ini_PutDouble 

Ini_PutInt 

Ini_PutRawString 

Ini_PutString 

Ini_PutUInt 

Ini_ReadFromFile 

Ini_ReadGeneric 

Ini_RemoveItem 

Ini_RemoveSection 

Ini_SectionExists 

Ini_SetDuplicateChecking 

Ini_SetSectionFilter 

Ini_SetTokens 

Ini_Sort 

Ini_SortInternally 

Ini_WriteGeneric 

Ini_WriteToFile 

InsertionSort 

InstallComCallback 

InStandaloneExecutable 

IntCompare 

InternationalDate 

InternationalTime 

isalnum 

isalpha 

iscntrl 

isdigit 

IsFinite 

isgraph 

IsInfinity 

islower 

IsNotANumber 

isprint 

ispunct 

isspace 

isupper 

isxdigit

**K**

KelvinToCelsius 

KilogramsToPounds 

KilometersToMiles

**L**

labs 

ldexp 

ldiv 

ListAppend 

ListApplyToEach 

ListApplyToEachEx 

ListBinSearch 

ListClear 

ListCompact 

ListCopy 

ListCreate 

ListDispose 

ListDisposePtrList 

ListEqual 

ListFindItem 

ListFindItemInRange 

ListGetDataPtr 

ListGetItem 

ListGetItems 

ListGetItemSize 

ListGetPtrToItem 

ListHeapSort 

ListInsertInOrder 

ListInsertionSort 

ListInsertItem 

ListInsertItems 

ListIsSorted 

ListNumItems 

ListPreAllocate 

ListQuickSort 

ListRemoveDuplicates 

ListRemoveItem 

ListRemoveItems 

ListReplaceItem 

ListReplaceItems 

ListSetAllocationPolicy 

LitersToGallons 

Ln10 

Ln2 

LnOfPi 

localeconv 

localtime 

log 

log10 

Log10OfEuler 

Log10OfPi 

longjmp 

lseek

**M**

_mbsbtype 

_mbscat 

_mbschr 

_mbscmp 

_mbscpy 

_mbscspn 

_mbsdec 

_mbsicmp 

_mbsinc 

_mbslen 

_mbsnbcat 

_mbsnbcmp 

_mbsnbcpy 

_mbsnbicmp 

_mbspbrk 

_mbsrchr 

_mbsspn 

_mbsstr 

_mbstok 

malloc 

mblen 

memchr 

memcmp 

memcpy 

memmove 

memset 

MetersToFeet 

mktime 

MilesToKilometers 

modf 

MolarGasConstant 

MultiplyCVITimeInterval

**N**

NegativeInfinity 

NewAsyncTimer 

NewAsyncTimerWithPriority 

NewHandle 

NIWatchdog_Clear 

NIWatchdog_ClearOutputs 

NIWatchdog_Configure 

NIWatchdog_Disable 

NIWatchdog_GetAttribute 

NIWatchdog_SetAttribute 

NIWatchdog_Whack 

NotANumber 

NumFmtdBytes

**O**

open 

OpenCom 

OpenComConfig 

OpenFile 

OutputDoubleItem 

OutputIntegerItem 

OutputList 

OutputShortItem 

OutputStringItem

**P**

_putenv 

perror 

Pi 

Pin 

PlanckConstant 

PositiveInfinity 

PostDeferredCall 

PostDeferredCallToThread 

PostDeferredCallToThreadAndWait 

PoundsToKilograms 

pow 

printf 

ProcessSystemEvents 

ProcessTCPEvents 

putc 

putchar 

puts

**Q**

qsort

**R**

RadToDeg 

raise 

rand 

Random 

read 

ReadFile 

ReadLine 

realloc 

ReciprocalOfEuler 

ReciprocalOfPi 

RegExpr_Destroy 

RegExpr_FindPatternInText 

RegExpr_GetErrorElaboration 

RegExpr_GetErrorString 

RegExpr_MatchText 

RegExpr_Parse 

RegisterTCPServer 

RegisterTCPServerEx 

remove 

RemoveFileIfExists 

RemoveSurroundingWhiteSpace 

rename 

ResumeAsyncTimerCallbacks 

ReturnRS232Err 

rewind 

RoundRealToNearestInteger 

RTIsShuttingDown 

RydbergConstant

**S**

Scan 

scanf 

ScanFile 

ScanIn 

ServerTCPRead 

ServerTCPWrite 

SetAsyncTimerAttribute 

SetBOLE 

SetBreakOnFirstChanceExceptions 

SetBreakOnLibraryErrors 

SetBreakOnProtectionErrors 

setbuf 

SetCommitMode 

SetComTime 

SetCTSMode 

SetDir 

SetEnableResourceTracking 

SetFilePtr 

SetHandleSize 

setjmp 

setlocale 

SetProcessorAffinityForThread 

SetRandomSeed 

SetSystemDate 

SetSystemTime 

SetTCPDisconnectMode 

SetUDPAttribute 

setvbuf 

SetXMode 

ShortCompare 

signal 

sin 

sinh 

SkipNonWhiteSpace 

SkipWhiteSpace 

sopen 

SpeedOfLight 

sprintf 

sqrt 

srand 

sscanf 

strcat 

strchr 

strcmp 

strcoll 

strcpy 

strcspn 

StrDup 

StrDupWithoutSurrWhiteSpace 

strerror 

strftime 

stricmp 

StrICmp 

StrICmpWithoutSurrWhiteSpace 

StringCopyMax 

StringLength 

StringLowerCase 

StringUpperCase 

strlen 

strncat 

strncmp 

strncpy 

strnicmp 

StrNICmp 

strpbrk 

strrchr 

strspn 

strstr 

strtod 

StrToInt 

strtok 

strtol 

strtol64 

StrToLongLong 

StrToUInt 

strtoul 

StrToULongLong 

strxfrm 

SubtractCVIAbsoluteTimes 

SubtractCVITimeIntervals 

SubtractFromCVIAbsoluteTime 

SuspendAsyncTimerCallbacks 

SwapBlock 

SyncWait

**T**

tan 

tanh 

TCPFreeMemory 

TDMS_AddChannel 

TDMS_AddChannelGroup 

TDMS_AdvancedCloseFile 

TDMS_AdvancedCreateFile 

TDMS_AdvancedOpenFile 

TDMS_AdvancedSyncRead 

TDMS_AdvancedSyncWrite 

TDMS_AllocateAlignedMemory 

TDMS_AppendDataValues 

TDMS_ChannelGroupPropertyExists 

TDMS_ChannelPropertyExists 

TDMS_CloseChannel 

TDMS_CloseChannelGroup 

TDMS_CloseFile 

TDMS_CreateFile 

TDMS_CreateLinearScalingInfo 

TDMS_CreatePolynomialScalingInfo 

TDMS_CreateReciprocalScalingInfo 

TDMS_CreateRTDScalingInfo 

TDMS_CreateStrainGageScalingInfo 

TDMS_CreateTableScalingInfo 

TDMS_CreateThermistorScalingInfo 

TDMS_CreateThermocoupleScalingInfo 

TDMS_DefragmentFile 

TDMS_FilePropertyExists 

TDMS_FreeAlignedMemory 

TDMS_FreeMemory 

TDMS_GetChannelGroupProperty 

TDMS_GetChannelGroupPropertyNames 

TDMS_GetChannelGroupPropertyType 

TDMS_GetChannelGroups 

TDMS_GetChannelGroupStringPropertyLength 

TDMS_GetChannelProperty 

TDMS_GetChannelPropertyNames 

TDMS_GetChannelPropertyType 

TDMS_GetChannels 

TDMS_GetChannelStringPropertyLength 

TDMS_GetDataType 

TDMS_GetDataTypeSize 

TDMS_GetDataValues 

TDMS_GetFileProperty 

TDMS_GetFilePropertyNames 

TDMS_GetFilePropertyType 

TDMS_GetFileStringPropertyLength 

TDMS_GetLibraryErrorDescription 

TDMS_GetNumChannelGroupProperties 

TDMS_GetNumChannelGroups 

TDMS_GetNumChannelProperties 

TDMS_GetNumChannels 

TDMS_GetNumDataValues 

TDMS_GetNumFileProperties 

TDMS_OpenFile 

TDMS_SaveFile 

TDMS_SetChannelGroupProperty 

TDMS_SetChannelInfo 

TDMS_SetChannelProperty 

TDMS_SetFileProperty 

TDMS_SetNextReadPosition 

TDMS_SetNextWritePosition 

ThreeHalvesPi 

time 

Timer 

TimeStr 

tmpfile 

tmpnam 

ToBigEndian16 

ToBigEndian32 

ToBigEndian64 

ToLittleEndian16 

ToLittleEndian32 

ToLittleEndian64 

tolower 

ToOtherEndian16 

ToOtherEndian32 

ToOtherEndian64 

toupper 

TraceConfigure 

TraceLoadAndSend 

TraceStart 

TraceStopAndSave 

TraceStopAndSend 

TraceUserEvent 

TransposeData 

TruncateRealNumber 

TwoPi

**U**

UIntToBinStr 

UDPMulticastSubscribe 

UDPMulticastUnsubscribe 

UDPRead 

UDPWrite 

ungetc 

ULongLongToBinStr 

UnregisterTCPServer 

UnregisterTCPServerEx

**V**

vfprintf 

vfscanf 

vprintf 

vscanf 

vsprintf 

vsscanf

**W**

WaitUS 

WaitUntilNextMultipleUS 

WaitUntilUS 

wcslen 

write 

WriteFile 

WriteLine 

WriteStringToFile

**X**

XModemConfig 

XModemReceive 

XModemSend

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/cvirtmodulehelp.htm language=enus -->
## TOPIC 00019: LabWindows/CVI Real-Time Module Help

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/cvirtmodulehelp.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/cvirtmodulehelp.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='nieagle.gif']

### LabWindows™/CVI™ Real-Time Module Help

August 2013, 372398F-01

This help file includes an introduction to the LabWindows/CVI Real-Time Module, programming considerations for real-time (RT) applications, and function reference information for the LabWindows/CVI Real-Time Utility Library. For more information about programming in LabWindows/CVI, refer to the *LabWindows/CVI Help*.

For more information about this help file, refer to the following topics:

[Related Documentation](rt_related_docs.html)

[Glossary](/csh?topicname=cvi/bp_glossary.htm)

[Important Information](/csh?topicname=cvi/bp_important_information.htm)

[Technical Support and Professional Services](/csh?topicname=cvi/bp_technical_support_resources.htm)

To comment on National Instruments documentation, refer to the National Instruments website.

© 2007–2013 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/cvirtmoduleplats.html language=enus -->
## TOPIC 00020: LabWindows/CVI Real-Time Module Platforms

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/cvirtmoduleplats.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/cvirtmoduleplats.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### LabWindows/CVI Real-Time Module Platforms

The Real-Time Module can execute applications on hardware targets running the NI ETS real-time operating system. The NI ETS real-time operating system runs on NI RT Series hardware to enable deterministic behavior and extended reliability.

For installation instructions for the Real-Time Module, refer to the Getting Started with the LabWindows/CVI Real-Time Module manual.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/debuggingrtapp.html language=enus -->
## TOPIC 00021: Debugging an RT Application

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/debuggingrtapp.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/debuggingrtapp.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Debugging an RT Application

If you select a [debug configuration](/csh?topicname=cvi/usermanual/settingprojconfigs.htm), you can debug the DLL from the LabWindows/CVI environment as you would [debug any other application](/csh?topicname=cvi/usermanual/sierundebugrunintstate.htm). For example, you can set breakpoints and watch expressions, step through code, view and edit variable values, and so on.

|  | Note Do not use the LabWindows/CVI debugging features to debug execution timing problems because the debugging features affect the timing of an application. |
| --- | --- |

#### Using the Real-Time Trace Viewer

Use the [Real-Time Trace Viewer](/csh?topicname=cvitracehelp/cvi_tracetoolkit_help.html) to analyze the timing and execution of an RT application. Use the [Real-Time Trace Viewer functions](../rtutillib/rtutillibtree.htm) in the Real-Time Utility Library to capture the timing and execution data of functions and threads in applications running on an RT target. The Real-Time Trace Viewer displays the timing and event data, or trace session, on the host computer.

In LabWindows/CVI, select **Tools»Real-Time Trace Viewer** to launch the Real-Time Trace Viewer.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/deployinganrtapp.html language=enus -->
## TOPIC 00022: Deploying an RT Application

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/deployinganrtapp.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/deployinganrtapp.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Deploying an RT Application

When you finish developing your RT application, you can deploy it to an RT target. After you deploy the RT application, the RT application runs automatically every time the RT target reboots.

Select **Run»Install Program to Real-Time Execution Target** to deploy your RT application. This option performs the following actions:

- Checks that the release configuration of the DLL has been built; if not, LabWindows/CVI prompts you to build the DLL or cancel.
- Deploys the release DLL and any statically linked DLLs to the NI-RT\CVI folder on the RT target.
- Sets the release DLL as the startup DLL. The startup DLL runs automatically every time the RT target reboots.
- Displays a dialog box indicating that the DLL was copied and prompting you to reboot the RT target.

If you have additional support files that you need to deploy, complete the following steps:

1. Select Run»Manage Files on Real-Time Execution Target to launch the LabWindows/CVI Real-Time File Copy Utility .
2. Click Add Files and browse to any support files that your application requires. The utility immediately copies the files to the NI-RT\CVI folder on the RT target.
3. Click Done when you finish adding support files.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/deterministic_apps_func_priorities.html language=enus -->
## TOPIC 00023: Creating Deterministic Applications Using Threads Set to Different Priorities

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/deterministic_apps_func_priorities.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/deterministic_apps_func_priorities.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Creating Deterministic Applications Using Threads Set to Different Priorities

Separate deterministic tasks from non-deterministic tasks and place deterministic tasks in different threads to ensure they receive enough processor resources. You can prioritize the threads to control the amount of processor resources each thread receives.

You can place a task in a thread by writing a function that accomplishes a particular task and scheduling that function in a thread using the [Thread Pool](/csh?topicname=cvi/libref/thread_pool_class_utility.html) functions in the [Utility Library](/csh?topicname=cvi/libref/cviutility_library.htm). Call [CmtNewThreadPool](/csh?topicname=cvi/libref/cvicmtnewthreadpool.htm) to create a thread pool. Then call [CmtScheduleThreadPoolFunctionAdv](/csh?topicname=cvi/libref/cvicmtschedulethreadpoolfunctionadv.htm) to schedule your function to run in the thread pool at a particular priority.

|  | Note Do not use the default thread pool option of CmtScheduleThreadPoolFunctionAdv in RT applications. Default thread pool threads continue running after your RT application exits. This behavior can cause the real-time target to become unstable. Instead, create a new thread pool and discard the thread pool before your RT application exits. |
| --- | --- |

The thread priority can be any value from -15 to 15. The default priority of a thread in the system is 0. The operating system scheduler runs at priority level 9. Any threads running at a priority level equal to or higher than 9 are not subject to timeslicing by the scheduler and will run until they yield the CPU or are preempted by a higher priority thread.

#### Cooperatively Yielding Thread Execution

Because of the preemptive scheduling used by the real-time operating system (RTOS), higher priority threads can monopolize processor resources. A high priority thread might use all of the processor resources, not allowing lower priority threads to execute, such as the FTP server thread of an RT target.

You must create threads that periodically yield to allow lower priority threads to execute while maintaining the determinism required by your application. By [timing a thread](timing_deterapps.html), you can ensure that the thread cooperatively yields processor resources.

|  | Note In applications running on a multiple CPU system, you can manually assign high priority threads handling deterministic tasks to dedicated processors. If you assign a high priority thread to a dedicated CPU, the thread can safely monopolize processor resources without adversely affecting other tasks. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/exploring_communication_methods.html language=enus -->
## TOPIC 00024: Exploring Remote Communication Methods

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/exploring_communication_methods.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/exploring_communication_methods.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Exploring Remote Communication Methods

You can use high-level software protocols to communicate between applications running on the RT target and applications running on other targets, such as the host computer. Each protocol has its advantages and disadvantages. The following list classifies the different communication methods:

- Network Communication—Used for communication over Ethernet networks.
  - Network Variables
  - Network Streams
  - TCP
  - UDP
- Bus Communication—Used for communication over different bus communication ports.
  - Serial
  - CAN

#### Network Communication

This section describes the most common network communication protocols used with the LabWindows/CVI Real-Time Module. Use this information to help you [select the right networking protocol(s) for your application](networkuserinterface.html#rt_networking_options).

##### Network Variables

You can use [network variables](/csh?topicname=cvi/libref/cvinetvarandrt.htm) to share data between applications running on different targets across a network. However, the transfer of the data across the network is not deterministic. Due to network latency, the most recently written data may not be available to an application running on a machine across the network. In this case, the application attempting to read from the network variable returns the previous value. For data logging applications, you can use timestamps to programmatically ensure that each value is logged once and only once.

##### Network Streams

You can use [network streams](/csh?topicname=cvi/libref/networkstreamslibrary.htm) to [stream data or send commands](/csh?topicname=cvi/libref/networkstreaming.htm) between an RT target and a host computer. A network stream is a lossless, unidirectional, one-to-one communication channel that consists of a writer and a reader endpoint.

##### TCP

TCP is an industry-standard protocol for communicating over networks. Applications running on the host computer can communicate with RT target DLLs using the [TCP Support Library](/csh?topicname=cvi/libref/cvitcp_library.htm) functions. However, TCP is non-deterministic, and using TCP communication in deterministic code can affect the determinism of the code.

The Real-Time Module extends the capabilities of the existing TCP functions to enable communication with networked RT Series devices.

##### UDP

UDP is a network transmission protocol for transferring data between two locations on a network. UDP is not a connection-based protocol, so the transmitting and receiving computers do not establish a network connection. Because there is no network connection, there is little overhead when transmitting data. However, UDP is non-deterministic, and using UDP communication in deterministic code can affect the determinism of the code.

When using UDP functions to send data, the receiving computer must have a read port open before the transmitting computer sends the data. Use the CreateUDPChannel or CreateUDPChannelConfig functions to open a write port and specify the IP address and port of the receiving computer. The data transfer occurs in byte streams of varying lengths called datagrams. Datagrams arrive at the listening port, and the receiving computer buffers and then reads the data.

You can transfer data bidirectionally with UDP. With bidirectional data transfers, both computers specify a read and write port and transmit data back and forth using the specified ports. You can use bidirectional UDP data transfers to send and receive data from a LabWindows/CVI application on the RT target.

UDP has the ability to perform fast data transmissions. However, UDP cannot guarantee that all datagrams arrive at the receiving computer. Because UDP is not connection-based, you cannot verify the arrival of datagrams. You must ensure that network congestion does not affect the transmission of datagrams. Also, you must read data stored in the data buffer of the receiving computer fast enough to prevent overflow and loss of data.

#### Bus Communication

##### Serial

Serial communication is the transmission of data between two locations through the serial ports. The [RS-232 Library](/csh?topicname=cvi/libref/cvirs232_library.htm) functions provide serial communication support for communication between RT targets with serial devices and serial instruments or computers that have a serial connection. Serial communication is ideal when transfer data rates are low or for transmitting data over long distances. You must add the NI-Serial RT software on the RT target from NI Measurement & Automation Explorer (MAX). Refer to the *Measurement & Automation Explorer Help* for information about adding software on an RT target.

Serial communication is non-deterministic and using serial communication in deterministic code can affect the determinism of the code.

##### CAN

Controller Area Network (CAN) is a deterministic, multi-drop communication bus standardized as ISO 11898. Using CAN, you can transfer up to 8 data bytes per frame at a rate of up to 1 Mbit per second. You can network multiple RT systems using NI-CAN interface cards and NI-CAN driver software. You must add the NI-CAN RT software on the RT target from MAX. Refer to the *Measurement & Automation Explorer Help* for information about adding software on an RT target.

Visit ni.com/info and enter the Info Code CANManual to view the NI-CAN Hardware and Software Manual for information about using NI-CAN hardware and software.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/installingrtswonhost.html language=enus -->
## TOPIC 00025: Installing the Real-Time Module Software on a Host Computer

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/installingrtswonhost.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/installingrtswonhost.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Installing the Real-Time Module Software on a Host Computer

You must first install the Real-Time Module software on a host computer before you can configure and install software on the RT target. To install and use the Real-Time Module software, you must have the following:

- Free Disk Space —In addition to the minimum system requirements for LabWindows/CVI, you must have at least 250 MB of free disk space for the Real-Time Module software. Refer to the LabWindows/CVI Release Notes for minimum system requirements.
- RT Target —The LabWindows/CVI Real-Time Module supports NI RT Series PXI controllers, NI Real-Time Industrial Controllers, stand-alone NI CompactDAQ systems, and desktop PCs converted to RT targets. Refer to the Using Desktop PCs as RT Targets with the Real-Time Module document for more information about converting a desktop computer to an RT target.

Complete the following steps to install the LabWindows/CVI Real-Time Module on a host computer.

1. Install LabWindows/CVI. Refer to the LabWindows/CVI Release Notes for information about installing LabWindows/CVI. 

 [IMAGE alt='Note' src='note.gif']
**Note** Do not install the device driver software when you are prompted to do so during the LabWindows/CVI installation. Instead, install the device driver software when you are prompted during the LabWindows/CVI Real-Time Module installation.
2. Insert the LabWindows/CVI media into the disk drive. If the media does not run automatically, open Windows Explorer, right-click the disk drive icon, and select AutoPlay .
3. Select Install LabWindows/CVI, Modules, and Toolkits on the National Instruments LabWindows/CVI screen.
4. Follow the instructions on the screen.
5. During the installation, use the National Instruments Device Drivers media to install the device drivers that you need.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/installingswonrttarget.html language=enus -->
## TOPIC 00026: Installing Software on the RT Target

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/installingswonrttarget.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/installingswonrttarget.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Installing Software on the RT Target

Use the LabVIEW Real-Time Software Wizard in MAX to install the software and drivers from the host computer on the RT target. With the LabVIEW Real-Time Software Wizard, you can view and change the software that is installed on the target. Click **Help** in the wizard for more information about installing and uninstalling software on the RT target.

Complete the following steps to launch the LabVIEW Real-Time Software Wizard:

1. Find and expand your RT target under the Remote Systems item in the MAX configuration tree, right-click Software , and select Add/Remove Software . 
When you select Add/Remove Software , MAX launches the LabVIEW Real-Time Software Wizard. This displays all the National Instruments software and drivers installed on the host computer that you can install on a selected RT target.
2. Select the software you want to install on the RT target, click the icon next to the software, and select Install the feature . 
Some components are automatically included as dependencies of other components. For more information about the features listed in the wizard, select the feature to view a description. 
The following list describes components you might commonly install. 

 [IMAGE alt='Note' src='note.gif']
**Note** If you have multiple versions of a component installed on the host computer, the most recent version is selected by default. You can choose to install another version.
  - Ethernet Drivers —MAX automatically selects the appropriate Ethernet driver(s) for the RT target when you install the LabWindows/CVI Run-Time Engine for RT component.
  - LabVIEW Real Time —MAX selects this item automatically when you install the LabWindows/CVI Run-Time Engine for RT component.
    - NI RT Extensions for SMP (MultiCore Support) —Install this item to take advantage of parallel processing on a multiple-CPU system. 

 [IMAGE alt='Note' src='note.gif']
**Note** Single-CPU systems perform best without the **NI RT Extensions for SMP** component. Also, some applications, such as those that consist mainly of single-point I/O, can achieve lower latency on a multicore system by using a single CPU without the **NI RT Extensions for SMP** component.
    - Microsoft Visual Studio 2008 Runtime Support —Install this item if your application requires additional DLLs built with Visual Studio 2008.
  - LabWindows/CVI Network Streams for RT —Install this item if your application uses functions from the Network Streams Library.
  - LabWindows/CVI Network Variable for RT —Install this item if your application uses functions from the Network Variable Library.
  - LabWindows/CVI Run-Time Engine for RT —Install this item to add support for LabWindows/CVI RT applications on the RT target. This component is required for all LabWindows/CVI RT applications.
  - Language Support for LabVIEW RT —Install this item if you are using strings in your RT application containing ASCII characters above 127 or multibyte characters. After installing this item on the RT target, you can configure the locale in MAX by selecting the target in the Remote Systems item in the MAX configuration tree, selecting the System Settings tab, and modifying the Locale option.
  - NI Hardware Drivers —Install the appropriate drivers for any other hardware libraries that you use in your application. For example, install the NI-DAQmx component if your application uses functions from the NI-DAQmx Library.
  - Network Variable Engine —MAX automatically selects this item when you install the LabWindows/CVI Network Variable for RT component.
  - NI Web-Based Configuration and Monitoring —Install this item to use a Web browser to monitor and configure an RT target.
  - State System Publisher —Install this item to monitor CPU and memory usage for an RT target from the NI Distributed System Manager.
  - USB Support —Install this item to enable support for accessing USB thumbdrives.
  - Variable Client Support for LabVIEW RT —MAX automatically selects this item when you install the LabWindows/CVI Network Variable for RT component.
3. When you finish selecting the software you want to install, click Next and continue following the instructions on the screen.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/intro_cvirt_module.html language=enus -->
## TOPIC 00027: Introduction to the LabWindows/CVI Real-Time Module

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/intro_cvirt_module.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/intro_cvirt_module.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Introduction to the LabWindows/CVI Real-Time Module

Most LabWindows/CVI applications run on a general-purpose OS such as Windows or Linux®. Some applications require real-time performance that general-purpose operating systems cannot guarantee. The LabWindows/CVI Real-Time Module extends the capabilities of LabWindows/CVI to address the need for real-time performance.

Use the Real-Time Module to build [deterministic applications](createmultithreadapps.html) to execute on a real-time operating system. First develop your application in LabWindows/CVI, and then execute the application on an RT target. The RT target can run applications in a stable platform optimized for real-time performance.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/monitoringconfiguringremotedevice.html language=enus -->
## TOPIC 00028: Monitoring and Configuring a Remote Device from a Web Browser

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/monitoringconfiguringremotedevice.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/monitoringconfiguringremotedevice.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Monitoring and Configuring a Remote Device from a Web Browser

After you install NI Web-Based Monitoring and Configuration on a remote device, such as an RT target, you can use a Web browser to monitor and configure the device.

Use the **LabVIEW Real-Time Software Wizard** in NI Measurement & Automation Explorer (MAX) to determine whether NI Web-Based Monitoring and Configuration is installed on an RT target and to install the software if necessary.

#### Accessing the Configuration Page

To access Web-based monitoring and configuration for a remote device, enter in a Web browser the URL http://*[remote device IP address]* where *[remote device IP address]* is the actual IP address of the remote device.

#### Logging into the Configuration Page

Web-based monitoring and configuration uses a permission-based security model. By default, each remote device includes a single user with the following name and password:

- User name — Admin
- Password — <blank>

After you access the Web-based monitoring and configuration page for a remote device, complete the following steps to log in for the first time.

|  | Note The User name and Password fields are case-sensitive. |
| --- | --- |

1. Click the Login button in the top-right corner of the page.
2. Enter Admin in the User name field.
3. Leave the Password field blank.
4. Click the OK button.

#### Monitoring and Configuring the Device

After you log in, click **Help** on each page of the NI Web-Based Monitoring and Configuration for information about monitoring and configuring the device.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/networkuserinterface.html language=enus -->
## TOPIC 00029: Network the User Interface

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/networkuserinterface.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/networkuserinterface.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Network the User Interface

RT targets supported by the LabWindows/CVI Real-Time Module are designed to run headless, with only a basic output display. Creating a GUI for a LabWindows/CVI Real-Time Module application requires a distributed computing approach: display the GUI on a general-purpose operating system and use a remote communication protocol to transfer data between the RT target and the GUI device.

Because supported network protocols are non-deterministic, you must separate the remote communication code from the deterministic code in your application. If data you are transferring originates in deterministic code, you must [pass the data](passing_data_between_funcs.html) from your deterministic code to the code that implements the remote communication.

#### Use the Right Networking Equipment

It can be tempting to use the networking equipment you already have or select the cheapest equipment available. However, the quality of commercial off-the-shelf networking equipment varies widely, so take the time to decide what type of networking equipment is most appropriate for your application. For some applications, lower-quality networking equipment is adequate. However, for applications that depend on network throughput, latency, or reliability, high-quality networking equipment can be crucial.

#### Use the Right Networking Protocol

The following table summarizes the advantages, disadvantages, and common use cases of the most common remote communication protocols for transferring data between RT targets and GUI devices:

| Use Case | Protocol | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Monitoring latest values | Network Variables | Easy to program, publishes to many computers at once, integrates with industrial protocols | High CPU overhead, proprietary, requires the Network Variable Engine |
| Streaming data between an RT target and a host computer, sending commands to an RT target | Network Streams | High throughput, lossless, automatic connection management | Single writer — single reader, unidirectional data transfer, proprietary |
| Starting point for custom protocols | TCP or UDP | Efficient CPU and memory usage, flexible, standard protocol for interoperability | Programming difficulty, string data only, no built-in method to identify data |

The following table presents networking protocol recommendations for the most common RT GUI use cases:

| Use Case | Example | Recommended Protocols |
| --- | --- | --- |
| Command (one to one) | Sending user interface value changes from a host PC to an RT target | Network Streams functions |
| Command (one to many) | Sending user interface value changes from a host PC to multiple RT targets | Network variables |
| Command (many to one) | Sending user interface value changes from multiple clients to an RT target | Network variables |
| Monitor (one to one) | Using a host PC to monitor latest values published by an RT target | Network variables |
| Monitor (one to many) | Using multiple clients to monitor latest values published by an RT target | Network variables |
| Monitor (many to one) | Using a host PC to monitor latest values published by multiple RT targets | Network variables |
| Stream (one to one) | Sending a continuous stream of data from an RT target to be logged on a host PC | Network Streams functions |
| Stream (one to many) | Web video server | TCP or UDP |
| Stream (many to one) | Web video client | TCP or UDP |

##### Creating a Dedicated Interface

For applications that require a single, dedicated user interface terminal, use the [Network Streams](/csh?topicname=cvi/libref/networkstreaming.htm) Library functions to stream data continuously and to send commands. Use network variables to monitor the latest value of each variable.

##### Creating a SCADA Interface

For supervisory control and data acquisition (SCADA) user interfaces typically involve one or more user interface terminals interacting with numerous embedded controllers. For SCADA applications, use [network variables](/csh?topicname=cvi/libref/cvinetworkvariables.htm) to send commands and monitor latest values.

Refer to the NetworkVariableRT.prj in the \samples\realtime\NetworkVariableRT directory for an example of using network variables to publish user interface data.

#### Use the Right Payload Sizes

Payload size is the amount of data you send over the network at once. Throughput and CPU efficiency increase as payload size increases. However, waiting to accumulate a large amount of data before sending the data increases the latency of your network transfers. When streaming data, the goal usually is to maximize throughput. By contrast, when sending commands, the goal usually is to minimize latency.

##### Streaming Data Continuously

To maximize throughput, follow these guidelines:

- Use an efficient networking protocol, such as UDP, TCP, or network streams.
- Accumulate data before sending the data over the network. By sending data in payloads of 1 KB (1024 bytes) or a multiple thereof, you can achieve high throughput and low CPU overhead while maintaining reasonable latency for most applications. However, if you need to minimize latency while streaming data, use a smaller payload size.
- Consider switching to polling mode for Ethernet packet detection. The Packet Detection setting of an RT target is on the Network Settings tab, under the More Settings pull-down menu in NI Measurement & Automation Explorer.
 [IMAGE alt='image' src='note.gif']
**Note** Polling mode provides lower jitter than interrupt mode. However, the CPU overhead required by polling mode decreases the maximum throughput you can achieve.

##### Sending Commands

To minimize latency, follow these guidelines:

- Use an efficient networking protocol, such as UDP, TCP, or network streams.
- Send each command as soon as possible. For example, if you are using network streams, you can call the CNSFlush function to send data immediately.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/optimizing_applications.html language=enus -->
## TOPIC 00030: Optimizing Deterministic Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/optimizing_applications.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/optimizing_applications.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Optimizing Deterministic Applications

The programming techniques in this section can reduce execution jitter in applications that run on an RT target.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/passing_data_between_funcs.html language=enus -->
## TOPIC 00031: Sharing Data Locally on an RT Target (RT Module)

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/passing_data_between_funcs.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/passing_data_between_funcs.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Sharing Data Locally on an RT Target

After dividing tasks in an application into threads of different priorities, you might need to communicate between different threads on the RT target. Use global variables, thread safe variables, and thread safe queues to share data between threads running on an RT target.

You can use global variables to access and pass small amounts of data between threads, such as from a time-critical thread to a lower priority thread. Global variables can share data smaller than 32-bits, such as scalar data, between threads deterministically. However, global variables of larger data types require locking to prevent simultaneous access and therefore become [shared resources](avoiding_shared_resources.html) that you must use carefully from deterministic code.

[Thread safe variables](/csh?topicname=cvi/programmerref/threadsafevariable.htm) combine the reading or writing of a variable with the necessary acquiring and releasing of a lock. The lock provides safe access from multiple threads. Due to the locking aspect, thread safe variables are [shared resources](avoiding_shared_resources.html) that you must use carefully from deterministic code. The Utility Library provides [functions and macros](/csh?topicname=cvi/libref/thread_safe_variable_class_utility.html) to use thread safe variables in your application.

Global variables and thread safe variables are lossy forms of communication, meaning that one thread can overwrite the data before the other thread reads the data. Tasks in a lower priority thread might not have enough processor time to read the data before other tasks in a different thread overwrite the data.

[Thread safe queues](/csh?topicname=cvi/programmerref/threadsafequeue.htm) provide an efficient mechanism for passing multiple data values between threads. The thread safe queue is optimized such that one thread can write to the queue while another thread reads from the queue. The Utility Library provides [functions](/csh?topicname=cvi/libref/thread_safe_queue_class_utility.html) to use thread safe queues in your application.

|  | Note Do not use the OPT_TSQ_DYNAMIC_SIZE option for a thread safe queue that is accessed from deterministic code. This option can cause the queue to allocate memory during use, which can affect determinism. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/real-time_system_components.html language=enus -->
## TOPIC 00032: Real-Time System Components

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/real-time_system_components.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/real-time_system_components.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Real-Time System Components

A real-time system consists of software and hardware components. The software components include LabWindows/CVI, the LabWindows/CVI Run-Time Engine (RTE) for RT, and the LabWindows/CVI applications you create. The hardware components of a real-time system include a host computer and an RT target. The following sections describe the different components of a real-time system.

#### Host Computer

The host computer is a computer with LabWindows/CVI and the LabWindows/CVI Real-Time Module installed. Use the host computer to develop applications for the real-time system. You can use LabWindows/CVI running on the host computer to interactively debug your application as it runs on the RT target. The host computer also can run Windows applications that communicate with applications running on RT targets to provide user interaction, monitoring, and so on.

#### LabWindows/CVI

Use LabWindows/CVI on the host computer to develop and debug real-time applications. The Real-Time Module extends the capabilities of LabWindows/CVI with additional tools for creating, debugging, and deploying deterministic applications.

#### LabWindows/CVI Run-Time Engine for RT

The LabWindows/CVI RTE for RT is a version of the LabWindows/CVI Run-Time Engine that runs on RT targets. The LabWindows/CVI RTE requires the LabVIEW Real-Time Engine, also called the RT Engine. The LabWindows/CVI Real-Time Module includes the necessary LabVIEW RT components for the RT target. The LabWindows/CVI RTE provides deterministic real-time performance for the following reasons:

- The LabWindows/CVI RTE runs on an RTOS, which ensures that the operating system services adhere to real-time operation.
- The LabWindows/CVI RTE runs on RT Series hardware. RT targets are designed to run only the applications and device drivers necessary for RT applications, which prevents other applications from impeding the execution of RT applications.
- RT targets do not use virtual memory, because virtual memory can cause unpredictable performance.

#### RT Target

An RT target is a networked computer running a real-time operating system. The RT target runs the LabWindows/CVI Run-Time Engine for RT and applications you create using LabWindows/CVI. You can use a separate host computer to communicate with and control applications on an RT target through an Ethernet connection. The LabWindows/CVI RT Module supports the following RT targets:

- NI RT Series PXI Controller —An embedded computer in a rugged PC-based platform for measurement and automation systems.
- NI Real-Time Industrial Controller —An embedded computer in a rugged, high-performance, fanless form factor.
- Stand-alone NI CompactDAQ Systems —An embedded computer in a compact, portable, rugged data-logging platform.
- Desktop PCs as RT Targets —A desktop PC configured with LabWindows/CVI RTE software. Refer to the Using Desktop PCs as RT Targets with the LabWindows/CVI Real-Time Module document for information about desktop PC targets.

|  | Note The LabWindows/CVI Help does not contain information about specific RT Targets. Refer to the appropriate device documentation for information about the device. |
| --- | --- |

##### USB Storage Devices

The Real-Time Module includes support for USB storage devices, such as thumb drives and external USB hard drives, for RT targets that have onboard USB hardware. Connect an external USB storage device to a USB port of an RT target and then access the device from applications running on the RT target.

When you plug a USB thumb drive into the RT system, the thumb drive is automatically assigned a drive letter of U:. Each additional drive you add is automatically assigned the next available drive letter. For example, V:, W::, X:, and so on.

|  | Caution Disconnecting a USB drive during operation can cause data corruption. To maintain data integrity, close all files on the USB drive before disconnecting the drive. |
| --- | --- |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rt_projectvariable.html language=enus -->
## TOPIC 00033: Sharing Data Using Network Variables

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rt_projectvariable.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rt_projectvariable.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Sharing Data Using Network Variables

You can use [network variables](/csh?topicname=cvi/libref/cvinetworkvariables.htm) to share data between applications across a network.

#### Network Variable Engine

When you create a network variable on a target, the Network Variable Engine on the target hosts the network variable. The Network Variable Engine sends the data you share to other targets across the network.

When an RT target hosts a network variable, that target controls the data and other targets do not affect the availability of the network variable. If availability is not a concern, consider hosting the network variable on the host computer. This frees up processor time on the target and allows you to use the security features.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rt_related_docs.html language=enus -->
## TOPIC 00034: Related Documentation (Real-Time Module)

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rt_related_docs.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rt_related_docs.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Real-Time Module)

Most LabWindows/CVI Real-Time Module manuals also are available as PDFs. You must have Adobe Reader installed to view the PDFs. Refer to the Adobe Systems Incorporated website at www.adobe.com to download the latest version of Adobe Reader. Refer to the National Instruments Product Manuals Library at ni.com/manuals for updated documentation resources.

The following documents contain information that you may find helpful as you use this help file:

- Getting Started with the LabWindows/CVI Real-Time Module—Use this manual as a tutorial to familiarize yourself with the LabWindows/CVI Real-Time Module and the basic Real-Time Module features you use to build real-time applications.
- LabWindows/CVI Release Notes—Use these release notes to learn about the new features included in this version of the LabWindows/CVI Real-Time Module.
- Using Desktop PCs as RT Targets with the LabWindows/CVI Real-Time Module—Use this document to access information about configuring a desktop PC as an RT target and information about installing software on the desktop PC.
- LabWindows/CVI Real-Time Module Readme —Use this document to learn about system requirements, installation instructions, and known issues for this version of the LabWindows/CVI Real-Time Module.
- PID Control Toolkit User Manual —Use this manual to access information about using the PID Control Toolkit functions.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rt_smp.html language=enus -->
## TOPIC 00035: Optimizing RT Applications for Multiple-CPU Systems

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rt_smp.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rt_smp.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Optimizing RT Applications for Multiple-CPU Systems

You can use the NI RT Extensions for SMP to take advantage of parallel processing on multiple-CPU systems, also known as multicore, multi-processor, or SMP systems. Use the LabVIEW Real-Time Software Wizard in MAX to install the NI RT Extensions for SMP. Refer to the *Measurement & Automation Explorer Help* for information about using the LabVIEW Real-Time Software Wizard.

The NI RT Extensions for SMP includes a CPU scheduler that allocates threads among available CPUs. You can take advantage of the CPU scheduler to achieve parallel execution on multiple-CPU systems. Many RT applications can [benefit](rt_smp_when.html) from additional CPUs without rewriting the application. However, by writing the RT application with multiple CPUs in mind, you might be able to achieve significant performance gains. To realize the full benefits of an RT system with multiple CPUs, you must implement a parallel or pipelined architecture in the RT target DLL.

|  | Note Single-CPU systems perform best without the NI RT Extensions for SMP. Also, some applications, such as those that consist mainly of single-point I/O, can achieve lower latency on a multicore system by using a single CPU without the NI RT Extensions for SMP. |
| --- | --- |

When writing a DLL to run on a system with multiple CPUs, [avoid shared resource](avoiding_shared_resources.html) conflicts whenever possible. The advantage of a system with multiple CPUs is that separate threads can execute simultaneously on separate CPUs. Simultaneous requests for a shared resource impede parallel execution and diminish the performance benefit of a multiple-CPU system.

When you install the NI RT Extensions for SMP, the Real-Time Module automatically balances threads across all available CPUs. However, you might be able to optimize the performance of some applications using [manual CPU assignment](settingprocessoraffinitymulticpu.html).

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rt_smp_when.html language=enus -->
## TOPIC 00036: Determining When to Use Multiple CPUs

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rt_smp_when.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rt_smp_when.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Determining When to Use Multiple CPUs

When you install the NI RT Extensions for SMP, the Real-Time Module balances threads across available CPUs in a process called automatic load balancing. Automatic load balancing enables RT target applications that incorporate parallelism to take advantage of multiple-CPU systems, also known as multicore, multi-processor, or SMP systems. However, transferring data between CPUs takes longer than transferring data from one operation to the next on a single CPU. Also, the overhead of the CPU scheduler slightly increases latency on the RT system, which can slow down single-point I/O applications that do not benefit from parallelism. In general, an application will benefit from multiple CPUs only if the time saved through parallel processing exceeds the time spent allocating system resources and transferring data between CPUs.

|  | Note If you are unsure whether to run an application with or without NI RT Extensions for SMP, you can test use the application using both configurations. Use the LabVIEW Real-Time Software Wizard in MAX to install and uninstall the NI RT Extensions for SMP. Refer to the Measurement & Automation Explorer Help for information about using the LabVIEW Real-Time Software Wizard. |
| --- | --- |

#### Applications that Benefit from Multiple CPUs

Real-time applications often include datalogging or host communication tasks that run in parallel to time-critical tasks. For example, running an application with parallel loops on a multiple-CPU RT system can improve performance without any need to rewrite the VI.

Applications that require multiple time-critical processes might also benefit from multiple CPUs. Because of the preemptive nature of time-critical tasks, it is generally best to include only one time-critical loop on a single-CPU system. However, on a multiple-CPU system you can include a time-critical loop on each CPU.

#### Applications that Do Not Benefit from Multiple CPUs

Although most real-time applications realize an immediate performance boost by switching to a multiple-CPU system, some applications must be rewritten to benefit from additional CPUs and other applications cannot benefit from additional CPUs. Real-time applications that consist of a single sequential loop do not benefit immediately from additional CPUs. If the loop consists of intensive processing, you might be able to increase performance by implementing a pipelined architecture. However, applications that consist primarily of single-point I/O processing usually do not benefit from multiple CPUs because the CPU scheduler contributes a slight amount of additional latency.

Applications that contain [shared resources](avoiding_shared_resources.html) might not benefit from additional CPUs until you rewrite the application to avoid shared resource conflicts. Simultaneous requests for a shared resource impede parallel execution and diminish the performance benefit of a multiple-CPU system.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rtmoduleconcepts.html language=enus -->
## TOPIC 00037: Real-Time Module Concepts

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rtmoduleconcepts.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rtmoduleconcepts.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Real-Time Module Concepts

This section includes information about the LabWindows/CVI Real-Time Module and real-time programming techniques to help you build deterministic applications.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/rtsharedatadeterm.html language=enus -->
## TOPIC 00038: Sharing Data in Deterministic Applications (RT Module)

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/rtsharedatadeterm.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/rtsharedatadeterm.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Sharing Data in Deterministic Applications

After separating deterministic tasks from non-deterministic tasks in an application, you must use deterministic communication methods to share data. You can use deterministic communication methods to share data between threads running on an RT target and between applications across a network running on different targets.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/runninganrtapp.html language=enus -->
## TOPIC 00039: Running an RT Application

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/runninganrtapp.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/runninganrtapp.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Running an RT Application

Select **Run»Debug Project** to run your RT application.

|  | Note If you select a release configuration, LabWindows/CVI displays a warning message. Click Continue to download and run the release DLL on the RT target. |
| --- | --- |

LabWindows/CVI automatically builds the DLL and downloads the DLL and any DLLs that are statically linked to it onto the specified RT target. LabWindows/CVI places the files that it automatically downloads in the NI-RT\CVI\temp folder. LabWindows/CVI empties the folder when you reset the RT device.

While you run your RT application, LabWindows/CVI displays a **<<Running on *target*>>** menu in the upper left corner of the LabWindows/CVI environment. The menu contains the following options, which you can use for debugging and for shutting down the RT application:

- Toggle Breakpoint —Turn on or turn off a breakpoint on the selected line.
- Break Execution —Suspend execution of the program.
- Simulate RT Shutting Down —End program execution. This option causes the RTIsShuttingDown function to return 1 , giving the RT application an opportunity to run any necessary cleanup code and exit. The RT target does not reboot.
- Abort Execution and Reboot Target —End program execution and reboot the RT target. The application cleanup code is not guaranteed to finish running before the RT target reboots.
- Disconnect from RT target —Disconnect LabWindows/CVI from the RT target while the RT application continues running on the target. Once you disconnect from the RT target, you cannot reconnect LabWindows/CVI to the RT application that is running.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/settingprocessoraffinitymulticpu.html language=enus -->
## TOPIC 00040: Setting Processor Affinity in Multiple-CPU Systems

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/settingprocessoraffinitymulticpu.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/settingprocessoraffinitymulticpu.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Setting Processor Affinity in Multiple-CPU Systems

Use the Symmetric Multiprocessing Functions in the [Real-Time Utility Library](../rtutillib/rtutillibtree.htm) to assign threads to CPUs. Call [SetProcessorAffinityForThread](../rtutillib/cvisetprocessoraffinityforthread.htm) to assign a thread to a specific CPU. Note that setting the processor affinity for a thread does not give the thread exclusive use of that CPU. You must call [ConfigureProcessorPool](../rtutillib/cviconfigureprocessorpool.htm) to remove the CPU from the system processor pool. Once you remove a CPU from the system pool, the CPU run only threads that you assign to it.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/specifyinganrttarget.html language=enus -->
## TOPIC 00041: Specifying an RT Target

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/specifyinganrttarget.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/specifyinganrttarget.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Specifying an RT Target

Complete the following steps to select the RT target on which to run your RT application.

|  | Note Before you can select or configure an RT target, you must set the Run-time support for your project to Real-time only. You can specify this option in the Target Settings dialog box. |
| --- | --- |

1. Select Run»Select Execution Target for Debugging to view a list of previously configured RT targets. Select the RT target you want to use from the list, if it is available.
2. To configure a new RT target, select Run»Select Execution Target for Debugging»New Execution Target . In the New Real-Time Execution Target dialog box, enter the computer name or IP address of the RT target in the Hostname/IP Address option and then click OK to exit the dialog box.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/timing_deterapps.html language=enus -->
## TOPIC 00042: Timing Deterministic Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/timing_deterapps.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/timing_deterapps.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Timing Deterministic Applications

Because of the preemptive scheduling used by the real-time operating system (RTOS), higher priority threads can monopolize processor resources. A high priority thread might use all of the processor resources, not allowing lower priority threads to execute. After [separating the deterministic tasks from non-deterministic tasks](createmultithreadapps.html#dividing_tasks_to_create_deterministic_multithreaded_applications), you can use timing methods to ensure deterministic performance for deterministic tasks while allowing non-deterministic tasks to execute as needed.

You can use the Microsecond Sleep Functions in the [Real-Time Utility Library](../rtutillib/rtutillibtree.htm) and external timing sources to control loop execution rates.

[Asynchronous timers](/csh?topicname=toolslib/toolslibasychronous_timers_control.htm) inherently control loop execution rate based on the specified timer period. The period must be longer than the time required to execute the callback function so that time remains for lower priority threads to run before the next timer iteration.

#### Timing Loops Using the Microsecond Sleep Functions

Use the Microsecond Sleep Functions to time loops on RT targets. With these functions, you can use the microsecond timer of the RTOS to control the timing of loops. By configuring a sleep period for a portion of each loop, you allow time for lower priority threads to execute before the next loop iteration.

##### SleepUS

The [SleepUS](../rtutillib/cvisleepus.htm) function causes a thread to sleep for the specified amount of time. For example, if the microsecond timer value is 112 μs when SleepUS executes and the **duration** parameter is 10, then the thread sleeps and does not return until the microsecond timer value equals 122 μs.

##### SleepUntilNextMultipleUS

The [SleepUntilNextMultipleUS](../rtutillib/cvisleepuntilnextmultipleus.htm) function causes a thread to sleep until the value of the microsecond timer equals equals a multiple of the **multiple** parameter. For example, if SleepUntilNextMultipleUS executes with a **multiple** input of 10 μs and the microsecond timer value is 112 μs, the function that calls SleepUntilNextMultipleUS sleeps until the microsecond timer value equals 120 μs because 120 μs is the first multiple of 10 μs after the execution of SleepUntilNextMultipleUS.

##### SleepUntilUS

The [SleepUntilUS](../rtutillib/cvisleepuntilus.htm) function causes a thread to sleep until the value of the microsecond timer equals the value of the **targetTime** parameter.

#### Timing Deterministic Applications Using External Timing Sources

The National Instruments drivers that run on RT targets support functions that can cause the current thread to sleep and then return when the driver detects a specific event. For example, you can use NI-DAQmx and NI data acquisition hardware to time real-time applications. Refer to the specific NI driver documentation for information about functions that you can use to sleep and wait for driver events.

##### Timing Real-Time Applications with NI-DAQmx

You can use NI data acquisition hardware with NI-DAQmx to match loop rates to match the rate of the hardware clock. With NI-DAQmx, you can use the following methods to time real-time applications:

- Hardware-Timed Single-Point —NI-DAQmx supports hardware-timed, single-point sample mode in which samples are acquired or generated continuously using hardware timing and no buffering. You can use hardware-timed, single-point mode for control applications that require input and/or output within a deterministic period of time. Refer to the NI-DAQmx Single-Point Real-Time Applications topic of the NI-DAQmx Help for information about using hardware-timed, single-point operations to time your deterministic application.
- Counter Timers —NI-DAQmx supports using hardware-timed counter input operations to drive a control loop. Use the DAQmxCfgSampClkTiming function to synchronize the counter operations with the counter sample clock. Refer to the Hardware-Timed Counter Tasks topic of the NI-DAQmx Help for information about using counter input operations to time deterministic applications.

Refer to the *NI-DAQmx Help* for more information about timing control loops using NI data acquisition hardware and NI-DAQmx software. Select **Start»All Programs»National Instruments»NI-DAQ»NI-DAQmx Help** to display the *NI-DAQmx Help*.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=cvirtmodulehelp/windowssdkfuncsinrt.html language=enus -->
## TOPIC 00043: Windows SDK Functions Supported in Real-Time Applications

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `cvirtmodulehelp/windowssdkfuncsinrt.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/cvirtmodulehelp/windowssdkfuncsinrt.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Windows SDK Functions Supported in Real-Time Applications

You can include a subset of Microsoft Windows SDK functions when you create DLLs to run on real-time (RT) targets. If you include a function in your real-time application that is not supported on RT, LabWindows/CVI generates a link error.

LabWindows/CVI automatically includes the following import libraries when LabWindows/CVI links projects with the **Run-time support** option set to **Real-time only**:

- kernel32_lvrt.lib
- user32_lvrt.lib

If you are using the [LabWindows/CVI Full Development System](/csh?topicname=cvi/basefdsdiffs.htm), you can optionally use functions in wsock32_lvrt.lib. To do so, you must manually add wsock32_lvrt.lib to your project from the CVI<*version*>\bin\msvc or CVI<*version*>\bin\msvc64 directory.

|  | Note The behavior of Windows SDK functions in real-time applications might not completely match the behavior on Windows due to partial implementations and differences in the NI real-time operating system. Make sure to test that the functionality of your application works as expected. |
| --- | --- |

#### Supported Functions

LabWindows/CVI supports the following list of Windows SDK functions in real-time applications.

##### kernel32_lvrt.lib

|  | Note To use the Windows SDK implementation of the ReadFile and WriteFile functions, instead of the LabWindows/CVI implementation, define the SDK_CONFLICT_PRIORITY macro in the Compiler Defines section of the Build Options dialog box. |
| --- | --- |

CancelWaitableTimer 

 CloseHandle 

 CompareFileTime 

 CompareStringA 

 CompareStringW 

 CopyFileA 

 CopyFileW 

 CreateDirectoryA 

 CreateDirectoryW 

 CreateEventA 

 CreateEventW 

 CreateFileA 

 CreateFileW 

 CreateMutexA 

 CreatePipe 

 CreateProcessW 

 CreateSemaphoreA 

 CreateSemaphoreW 

 CreateThread 

 CreateWaitableTimerA 

 DebugBreak 

 DeleteCriticalSection 

 DeleteFileA 

 DeleteFileW 

 DeviceIoControl 

 DisableThreadLibraryCalls 

 DuplicateHandle 

 EnterCriticalSection 

 ExitProcess 

 ExitThread 

 FatalAppExitA 

 FileTimeToLocalFileTime 

 FileTimeToSystemTime 

 FindClose 

 FindFirstFileA 

 FindFirstFileExA 

 FindFirstFileExW 

 FindFirstFileW 

 FindNextFileA 

 FindNextFileW 

 FindResourceA 

 FlushFileBuffers 

 FreeEnvironmentStringsW 

 FreeLibrary 

 GetCommandLineA 

 GetConsoleCP 

 GetConsoleMode 

 GetConsoleOutputCP 

 GetConsoleScreenBufferInfo 

 GetCurrentDirectoryA 

 GetCurrentDirectoryW 

 GetCurrentProcessId 

 GetCurrentThread 

 GetCurrentThreadId 

 GetDateFormatW 

 GetDiskFreeSpaceA 

 GetDiskFreeSpaceExA 

 GetDriveTypeA 

 GetDriveTypeW 

 GetEnvironmentStrings 

 GetEnvironmentStringsW 

 GetEnvironmentVariableA 

 GetExitCodeThread 

 GetFileAttributesA 

 GetFileAttributesW 

 GetFileInformationByHandle 

 GetFileSize 

 GetFileTime 

 GetFileType 

 GetFullPathNameA 

 GetFullPathNameW 

 GetLargestConsoleWindowSize 

 GetLastError 

 GetLocalTime 

 GetLocaleInfoW 

 GetLogicalDriveStringsA 

 GetLogicalDrives 

 GetLongPathNameW 

 GetModuleFileNameA 

 GetModuleFileNameW 

 GetModuleHandleA 

 GetModuleHandleW 

 GetNumberOfConsoleInputEvents 

 GetOverlappedResult 

 GetPrivateProfileIntA 

 GetPrivateProfileStringA 

 GetProcAddress 

 GetProcessAffinityMask 

 GetProcessHeap 

 GetStartupInfoA 

 GetStartupInfoW 

 GetStdHandle 

 GetStringTypeA 

 GetStringTypeW 

 GetSystemDirectoryA 

 GetSystemDirectoryW 

 GetSystemInfo 

 GetSystemTime 

 GetSystemTimeAsFileTime 

 GetSystemWindowsDirectoryW 

 GetTempPathA 

 GetThreadContext 

 GetThreadLocale 

 GetThreadPriority 

 GetThreadTimes 

 GetTickCount 

 GetTimeFormatW 

 GetTimeZoneInformation 

 GetVersion 

 GetVersionExW 

 GetWindowsDirectoryA 

 GlobalAlloc 

 GlobalFree 

 HeapAlloc 

 HeapCompact 

 HeapCreate 

 HeapDestroy 

 HeapFree 

 HeapReAlloc 

 HeapSize 

 HeapValidate 

 HeapWalk 

 InitializeCriticalSection 

 InterlockedCompareExchange 

 InterlockedDecrement 

 InterlockedExchange 

 InterlockedExchangeAdd 

 InterlockedIncrement 

 IsBadCodePtr 

 IsBadReadPtr 

 IsBadWritePtr 

 IsDBCSLeadByteEx 

 IsDebuggerPresent 

 LCMapStringA 

 LCMapStringW 

 LeaveCriticalSection 

 LoadLibraryA 

 LoadLibraryExA 

 LoadLibraryW 

 LoadResource 

 LocalAlloc 

 LocalFileTimeToFileTime 

 LocalFree 

 LocalReAlloc 

 LockFile 

 LockResource 

 MoveFileA 

 MoveFileW 

 MultiByteToWideChar 

 OpenEventA 

 OpenMutexA 

 OpenSemaphoreA 

 OpenWaitableTimerA 

 OutputDebugStringA 

 OutputDebugStringW 

 PeekConsoleInputA 

 PeekNamedPipe 

 PulseEvent 

 QueryPerformanceCounter 

 QueryPerformanceFrequency 

 RaiseException 

 ReadConsoleA 

 ReadConsoleInputA 

 ReadConsoleOutputA 

 ReadFile 

 ReleaseMutex 

 ReleaseSemaphore 

 RemoveDirectoryA 

 RemoveDirectoryW 

 ResetEvent 

 ResumeThread 

 RtlUnwind 

 SetConsoleCtrlHandler 

 SetConsoleCursorPosition 

 SetConsoleMode 

 SetConsoleTextAttribute 

 SetCurrentDirectoryA 

 SetCurrentDirectoryW 

 SetEndOfFile 

 SetEnvironmentVariableA 

 SetEnvironmentVariableW 

 SetEvent 

 SetFileAttributesA 

 SetFileAttributesW 

 SetFilePointer 

 SetFileTime 

 SetLastError 

 SetLocalTime 

 SetStdHandle 

 SetSystemTime 

 SetThreadAffinityMask 

 SetThreadContext 

 SetThreadIdealProcessor 

 SetThreadPriority 

 SetWaitableTimer 

 SizeofResource 

 Sleep 

 SleepEx 

 SuspendThread 

 SystemTimeToFileTime 

 TerminateProcess 

 TerminateThread 

 TlsAlloc 

 TlsFree 

 TlsGetValue 

 TlsSetValue 

 TryEnterCriticalSection 

 UnhandledExceptionFilter 

 UnlockFile 

 VirtualAlloc 

 VirtualFree 

 VirtualQuery 

 WaitForMultipleObjects 

 WaitForSingleObject 

 WideCharToMultiByte 

 WriteConsoleA 

 WriteConsoleOutputA 

 WriteFile 

 WritePrivateProfileStringA 

 lstrcatA 

 lstrcmpA 

 lstrcmpiA 

 lstrcpyA 

 lstrlenA

##### user32_lvrt.lib

CharNextA 

 CharPrevA 

 wsprintfA

##### wsock32_lvrt.lib

WSAAsyncGetHostByAddr 

 WSAAsyncGetHostByName 

 WSAAsyncGetProtoByName 

 WSAAsyncGetProtoByNumber 

 WSAAsyncGetServByName 

 WSAAsyncGetServByPort 

 WSAAsyncSelect 

 WSACancelAsyncRequest 

 WSACancelBlockingCall 

 WSACleanup 

 WSAGetLastError 

 WSAIsBlocking 

 WSASetBlockingHook 

 WSASetLastError 

 WSAStartup 

 WSAUnhookBlockingHook 

 __WSAFDIsSet 

 accept 

 bind 

 closesocket 

 connect 

 gethostbyaddr 

 gethostbyname 

 gethostname 

 getpeername 

 getprotobyname 

 getprotobynumber 

 getservbyname 

 getservbyport 

 getsockname 

 getsockopt 

 htonl 

 htons 

 inet_addr 

 inet_ntoa 

 ioctlsocket 

 listen 

 ntohl 

 ntohs 

 recv 

 recvfrom 

 select 

 send 

 sendto 

 setsockopt 

 shutdown 

 socket

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviapplyrtsystemimage.htm language=enus -->
## TOPIC 00044: ApplyRTSystemImage

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviapplyrtsystemimage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviapplyrtsystemimage.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### ApplyRTSystemImage

int ApplyRTSystemImage (char IPAddress[], char imagePath[], int options, ProgressCallbackType callback, void *callbackData);

#### Purpose

Applies an image to a target system, replacing its current configuration with that of the image. Call [CreateRTSystemImage](../rtutillib/cvicreatertsystemimage.htm) to create an image.

The target system must have an IP address in order to be imaged. You can configure a target IP stack by calling [SetRTIPConfiguration](../rtutillib/cvisetrtipconfiguration.htm). The imaging process preserves a target IP stack configuration and hostname.

Before copying the image to the target system, ApplyRTSystemImage deletes every file and directory on the C:\ drive. If the target system has a Windows installation, ApplyRTSystemImage deletes only the \NI-RT directory.

|  | Note Images created from Windows dual boot RT systems contain some Windows system files from the root directory. Because of this, National Instruments recommends that you not apply such an image to a different Windows dual boot system because the system files on the target are overwritten by the ones from the image, potentially corrupting the Windows installation. |
| --- | --- |

To prevent other applications from interfering with the imaging process, ApplyRTSystemImage locks the target system with the password kilgoretrout for the duration of the operation. If you locked the system with a different password, LabWindows/CVI restores the password after imaging completes.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IPAddress | char [] | IP address or DNS-resolvable hostname of the system to image. You cannot apply an image to a system that is freshly formatted or otherwise unconfigured. You must first call SetRTIPConfiguration to configure its IP address and reboot it with RebootRTSystem. |
| imagePath | char [] | The path to the image directory. This is the directory that contains the RTCtrlr.ini file. Images are not compatible across different controller models because the drivers in an image are model-specific. You must specify an image that was created from a model that matches the target system. |
| options | int | A bitfield consisting of 0 or more RTUtilOptions bitwise OR-ed together: RTUtilOption_RunInNewThreadThe function should return immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. RTUtilOption_RequireSystemMatchEnsure that the specified image only be applied to the system from which it was created. By default, an image must only match the target system's device code (i.e. hardware model). This option imposes an additional restriction that source and target machines not only be the same model of system, but actually be the same system. |
| RTUtilOption_RunInNewThread | The function should return immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. |  |
| RTUtilOption_RequireSystemMatch | Ensure that the specified image only be applied to the system from which it was created. By default, an image must only match the target system's device code (i.e. hardware model). This option imposes an additional restriction that source and target machines not only be the same model of system, but actually be the same system. |  |
| callback | ProgressCallbackType | A callback function that receives notification of events that occur on the system. You can pass NULL if you do not want to register a callback. The callback function, type ProgressCallback, takes the following form: int CVICALLBACK CallbackFunc (const char *systemIP, const char *systemMAC, int event, void *eventData1, void *eventData2, void *callbackData); The callback is executed in a separate thread every time a RTUtilEvent occurs on the system. If you are interested only in certain events, your callback must examine the event parameter passed in. The systemIP parameter contains the IP address of the system for which the event occurred. The systemMAC parameter contains the system MAC address. The callback return value is ignored. You do not need to explicitly unregister your callback. The callback stop receiving notifications once the operation for which it was registered has completed. Just before the callback is unregistered, it receives the RTUtilEvent_CallbackUnregistered event to indicate that it is safe to clean up callbackData, if necessary. The following lists RTUtilEvent events and relevant details for each event: Event Description RTUtilEvent_NewSystemStatus The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown RTUtilEvent_BeginCreateImage Beginning image creation operation. RTUtilEvent_EndCreateImage Finished image creation operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginApplyImage Beginning image application operation. RTUtilEvent_EndApplyImage Finished image application operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginFormatSystem Beginning system HD format operation. RTUtilEvent_EndFormatSystem Finished system HD format operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_EnumRemoteFiles Enumerating files on the remote system. RTUtilEvent_CreateLocalDirs Creating local image directory hierarchy. RTUtilEvent_BeginTransferFiles Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. RTUtilEvent_EndTransferFiles Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. RTUtilEvent_DeleteExistingFiles Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. RTUtilEvent_CheckingForSafeMode Checking that the remote system is booted into safe mode. RTUtilEvent_RebootIntoSafeMode Rebooting the remote system into safe mode. RTUtilEvent_RebootIntoInstallMode Rebooting the remote system into install mode. RTUtilEvent_BeginReboot Rebooting the remote system. RTUtilEvent_BeginFormattingHD Beginning hard drive format. RTUtilEvent_EndFormattingHD Hard drive finished reformatting. RTUtilEvent_GetFile Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_PutFile Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteFile Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteDir Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateLocalDir Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateRemoteDir Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CallbackUnregistered The callback is about to be unregistered. You can deallocate callbackData if necessary. |
| Event | Description |  |
| RTUtilEvent_NewSystemStatus | The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown |  |
| RTUtilEvent_BeginCreateImage | Beginning image creation operation. |  |
| RTUtilEvent_EndCreateImage | Finished image creation operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginApplyImage | Beginning image application operation. |  |
| RTUtilEvent_EndApplyImage | Finished image application operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginFormatSystem | Beginning system HD format operation. |  |
| RTUtilEvent_EndFormatSystem | Finished system HD format operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_EnumRemoteFiles | Enumerating files on the remote system. |  |
| RTUtilEvent_CreateLocalDirs | Creating local image directory hierarchy. |  |
| RTUtilEvent_BeginTransferFiles | Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. |  |
| RTUtilEvent_EndTransferFiles | Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. |  |
| RTUtilEvent_DeleteExistingFiles | Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. |  |
| RTUtilEvent_CheckingForSafeMode | Checking that the remote system is booted into safe mode. |  |
| RTUtilEvent_RebootIntoSafeMode | Rebooting the remote system into safe mode. |  |
| RTUtilEvent_RebootIntoInstallMode | Rebooting the remote system into install mode. |  |
| RTUtilEvent_BeginReboot | Rebooting the remote system. |  |
| RTUtilEvent_BeginFormattingHD | Beginning hard drive format. |  |
| RTUtilEvent_EndFormattingHD | Hard drive finished reformatting. |  |
| RTUtilEvent_GetFile | Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_PutFile | Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteFile | Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteDir | Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateLocalDir | Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateRemoteDir | Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CallbackUnregistered | The callback is about to be unregistered. You can deallocate callbackData if necessary. |  |
| callbackData | void * | A pointer-width value the library passes to the callback function through the callbackData parameter. You can use the callbackData as an integer value or as a pointer to a data object you want to access in the callback function. This way, you do not have to declare the data object as a global variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTSystemImaging\RTSystemImaging.cws for an example of using the ApplyRTSystemImage function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviconfigureprocessorpool.htm language=enus -->
## TOPIC 00045: ConfigureProcessorPool

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviconfigureprocessorpool.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviconfigureprocessorpool.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### ConfigureProcessorPool

int ConfigureProcessorPool (int processorPoolID, unsigned int processorMask, unsigned int *previousProcessorMask);

#### Purpose

Configures the set of processors included in the specified processor pool.

Processor pool changes take effect the next time the operating system schedules a thread assigned to the pool to run. You can force a thread to give up the remainder of its current timeslice by calling the Windows SDK function Sleep. The next time the thread executes, it reflects the new processor pool settings.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| processorPoolID | int | Specifies the processor pool to configure. You must pass kProcessorPool_System. By default, all threads in the system are assigned to the system pool. Operating system threads are always assigned to this pool. The operating system schedules all threads assigned to this pool to the group of processors included in the pool. The operating system automatically moves threads between processors to balance the load between the processors. Note that changes you make to the system processor pool while you debug one RT application persist while you debug subsequent RT applications. National Instruments recommends that you reset the system processor pool to include all processors before you exit any RT application. Rebooting the RT target resets the system processor pool to include all processors. |
| processorMask | unsigned int | Specifies the set of processors to be included in the processor pool. You must specify one or more valid processors. The first processor in the system is indicated by the lowest order bit in the mask. You can determine the total number of processors on the system by calling CmtGetNumProcessors. You cannot specify processors that do not exist on the system. However, you can pass a mask of 0xFFFFFFFF to indicate that the pool should include all available processors regardless of the number of processors on the system. The processor mask for the system pool must always include the first processor. The first processor in the system is unique because it processes all interrupts in the system. |
| Output |  |  |
| Name | Type | Description |
| previousProcessorMask | unsigned int | Returns the processor mask of the specified pool before making this call. You can pass NULL for this paramter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\SymmetricMultiprocessingRT\SymmetricMultiprocessingRT.cws for an example of using the ConfigureProcessorPool function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvicreatertsystemimage.htm language=enus -->
## TOPIC 00046: CreateRTSystemImage

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvicreatertsystemimage.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvicreatertsystemimage.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### CreateRTSystemImage

int CreateRTSystemImage (char IPAddress[], char outputDirPath[], int options, ProgressCallbackType callback, void *callbackData);

#### Purpose

Creates an image of the target RT system that you can use for system restoration or cloning. Call [ApplyRTSystemImage](../rtutillib/cviapplyrtsystemimage.htm) to apply an image to a target system.

An image is a snapshot of an RT system configuration. By default, an image encompasses the entire C:\ volume. If the system also has a Windows installation, the image is limited to the files directly in C:\ and everything under the C:\NI-RT directory. LabWindows/CVI implements images as a local copy of the relevant files and directories of the target system. This implementation makes it possible to hand-edit an image to add, remove, rename, or replace files or directories in any way you want.

Images are useful for restoring a known, working configuration to a system that has become cluttered or unstable over time. Also, because an image is a complete archive of the files on a system at a given time, saving periodic images can be useful for tracking system state over time for quality assurance. Saving an image also makes it possible to install or restore drivers and software from a host Windows machine that does not have any drivers or NI Measurement & Automation Explorer (MAX) installed.

Using images for cloning can simplify the process of deploying a particular system configuration to multiple production targets. Once you configure and test your development system, you can create an image of that system and apply it to any number of unconfigured, identical systems.

You can specify RTUtilOption_GetSoftwareOnly in the **options** parameter to create an image that contains only core system files and software/drivers installed by MAX. A software-only image is useful as a clean, baseline configuration that you can use as a common starting point for multiple systems or for purging a system of all extraneous programs, data files, and so on that you have added or created over time.

To prevent other applications from interfering with the image creation process, this function locks the target system with the password kilgoretrout for the duration of the operation. If you locked the system with a different password, LabWindows/CVI restores the password after the operation completes.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IPAddress | char [] | The IP address or DNS-resolvable hostname of the system to image. |
| outputDirPath | char [] | The directory in which to store the system image. If the path does not exist, the function creates the path. An image is comprised of many files, so National Instruments recommends that you specify a new directory for every distinct image you create. Note Existing files in the directory may be overwritten by files in the new image. National Instruments highly recommends that you empty your image directory before you create the image; CreateRTSystemImage considers any files in the image directory to be part of the image and copies the files to target systems when you apply the image. |
|  | Note Existing files in the directory may be overwritten by files in the new image. National Instruments highly recommends that you empty your image directory before you create the image; CreateRTSystemImage considers any files in the image directory to be part of the image and copies the files to target systems when you apply the image. |  |
| options | int | A bit field consisting of 0 or more RTUtilOption flags bitwise OR-ed together. You can specify the following flags: Flag Description RTUtilOption_RunInNewThread The function returns immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. RTUtilOption_GetSoftwareOnly The created image should only contain system files and software packages installed from NI Measurement & Automation Explorer (MAX). This option is useful for capturing the NI driver/software configuration of a system without including user programs or other data or output files. |
| Flag | Description |  |
| RTUtilOption_RunInNewThread | The function returns immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. |  |
| RTUtilOption_GetSoftwareOnly | The created image should only contain system files and software packages installed from NI Measurement & Automation Explorer (MAX). This option is useful for capturing the NI driver/software configuration of a system without including user programs or other data or output files. |  |
| callback | ProgressCallbackType | A callback function that receives notification of events that occur on the system. You can pass NULL if you do not want to register a callback. The callback function, type ProgressCallback, takes the following form: int CVICALLBACK CallbackFunc (const char *systemIP, const char *systemMAC, int event, void *eventData1, void *eventData2, void *callbackData); The callback is executed in a separate thread every time a RTUtilEvent occurs on the system. If you are interested only in certain events, your callback must examine the event parameter passed in. The systemIP parameter contains the IP address of the system for which the event occurred. The systemMAC parameter contains the system MAC address. The callback return value is ignored. You do not need to explicitly unregister your callback. The callback stop receiving notifications once the operation for which it was registered has completed. Just before the callback is unregistered, it receives the RTUtilEvent_CallbackUnregistered event to indicate that it is safe to clean up callbackData, if necessary. The following lists RTUtilEvent events and relevant details for each event: Event Description RTUtilEvent_NewSystemStatus The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown RTUtilEvent_BeginCreateImage Beginning image creation operation. RTUtilEvent_EndCreateImage Finished image creation operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginApplyImage Beginning image application operation. RTUtilEvent_EndApplyImage Finished image application operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginFormatSystem Beginning system HD format operation. RTUtilEvent_EndFormatSystem Finished system HD format operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_EnumRemoteFiles Enumerating files on the remote system. RTUtilEvent_CreateLocalDirs Creating local image directory hierarchy. RTUtilEvent_BeginTransferFiles Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. RTUtilEvent_EndTransferFiles Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. RTUtilEvent_DeleteExistingFiles Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. RTUtilEvent_CheckingForSafeMode Checking that the remote system is booted into safe mode. RTUtilEvent_RebootIntoSafeMode Rebooting the remote system into safe mode. RTUtilEvent_RebootIntoInstallMode Rebooting the remote system into install mode. RTUtilEvent_BeginReboot Rebooting the remote system. RTUtilEvent_BeginFormattingHD Beginning hard drive format. RTUtilEvent_EndFormattingHD Hard drive finished reformatting. RTUtilEvent_GetFile Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_PutFile Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteFile Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteDir Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateLocalDir Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateRemoteDir Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CallbackUnregistered The callback is about to be unregistered. You can deallocate callbackData if necessary. |
| Event | Description |  |
| RTUtilEvent_NewSystemStatus | The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown |  |
| RTUtilEvent_BeginCreateImage | Beginning image creation operation. |  |
| RTUtilEvent_EndCreateImage | Finished image creation operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginApplyImage | Beginning image application operation. |  |
| RTUtilEvent_EndApplyImage | Finished image application operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginFormatSystem | Beginning system HD format operation. |  |
| RTUtilEvent_EndFormatSystem | Finished system HD format operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_EnumRemoteFiles | Enumerating files on the remote system. |  |
| RTUtilEvent_CreateLocalDirs | Creating local image directory hierarchy. |  |
| RTUtilEvent_BeginTransferFiles | Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. |  |
| RTUtilEvent_EndTransferFiles | Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. |  |
| RTUtilEvent_DeleteExistingFiles | Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. |  |
| RTUtilEvent_CheckingForSafeMode | Checking that the remote system is booted into safe mode. |  |
| RTUtilEvent_RebootIntoSafeMode | Rebooting the remote system into safe mode. |  |
| RTUtilEvent_RebootIntoInstallMode | Rebooting the remote system into install mode. |  |
| RTUtilEvent_BeginReboot | Rebooting the remote system. |  |
| RTUtilEvent_BeginFormattingHD | Beginning hard drive format. |  |
| RTUtilEvent_EndFormattingHD | Hard drive finished reformatting. |  |
| RTUtilEvent_GetFile | Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_PutFile | Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteFile | Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteDir | Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateLocalDir | Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateRemoteDir | Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CallbackUnregistered | The callback is about to be unregistered. You can deallocate callbackData if necessary. |  |
| callbackData | void * | A pointer-width value the library passes to the callback function through the callbackData parameter. You can use the callbackData as an integer value or as a pointer to a data object you want to access in the callback function. This way, you do not have to declare the data object as a global variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTSystemImaging\RTSystemImaging.cws for an example of using the CreateRTSystemImage function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvidisposertsysteminfo.htm language=enus -->
## TOPIC 00047: DisposeRTSystemInfo

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvidisposertsysteminfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvidisposertsysteminfo.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### DisposeRTSystemInfo

int DisposeRTSystemInfo (RTSystemInfoPtr systemInfo);

#### Purpose

Frees the memory associated with a system information pointer (RTSystemInfoPtr) allocated by the Real-Time Utility Library.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| systemInfo | RTSystemInfoPtr | The RTSystemInfoPtr to dispose. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTSystemImaging\RTSystemImaging.cws for an example of using the DisposeRTSystemInfo function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvifindallrtsystemsonsubnet.htm language=enus -->
## TOPIC 00048: FindAllRTSystemsOnSubnet

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvifindallrtsystemsonsubnet.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvifindallrtsystemsonsubnet.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### FindAllRTSystemsOnSubnet

int FindAllRTSystemsOnSubnet (RTSystemInfoPtr **systems, int *numSystems);

#### Purpose

Discovers all RT systems present on the local subnet and returns an array of system information pointers (RTSystemInfoPtr) containing information about each target. FindAllRTSystemsOnSubnet finds only systems that are booted and running, though the systems do not need to have IP settings configured or have any software installed.

Windows This function is supported only on Windows.

#### Parameters

| Output |  |  |
| --- | --- | --- |
| Name | Type | Description |
| systems | RTSystemInfoPtr * | Output parameter that receives a null-terminated array of system information pointers (RTSystemInfoPtr). FindAllRTSystemsOnSubnet dynamically allocates a RTSystemInfoPtr for each system that is found and the array in which to store the structure pointers. The returned array is numSystems + 1 long, with the last item being a null pointer. This function allocates new memory each time you call it. If you call this function multiple times, you must explicitly free the previously returned array and structures between each call. Do not attempt to reuse previously allocated arrays or structures by passing them back in. You must call DisposeRTSystemInfo on each RTSystemInfoPtr in the returned array. You must also free the array itself by calling FreeRTUtilMemory. |
| numSystems | int | A pointer to a variable that receives the number of systems found. This value is the number of system information pointers (RTSystemInfoPtr) returned in the systems parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the FindAllRTSystemsOnSubnet function:

- realtime\RTConfig\RTConfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RTSystemImaging\RTSystemImaging.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviformatrtsystem.htm language=enus -->
## TOPIC 00049: FormatRTSystem

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviformatrtsystem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviformatrtsystem.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### FormatRTSystem

int FormatRTSystem (char address[], int addressType, int options, ProgressCallbackType callback, void *callbackData);

#### Purpose

Reformats the hard drive of a system, completely erasing all data.

|  | Note RT desktop PCs and PXI controllers with floppy disk drives are not supported. These types of systems lack the internal ROM used to boot to safe mode. |
| --- | --- |

After you reformat, the target is in an unconfigured state without an IP address and continues to boot into safe mode until you configure the target with software.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| options | int | A bit field consisting of 0 or more RTUtilOption flags bitwise OR-ed together. You can specify the following flag: RTUtilOption_RunInNewThread The function returns immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. |
| RTUtilOption_RunInNewThread | The function returns immediately without waiting for the operation to complete. The operation is carried out asynchronously in a new thread. You must register a callback to get progress updates or a return code for the asynchronous operation. |  |
| callback | ProgressCallbackType | A callback function that receives notification of events that occur on the system. You can pass NULL if you do not want to register a callback. The callback function, type ProgressCallback, takes the following form: int CVICALLBACK CallbackFunc (const char *systemIP, const char *systemMAC, int event, void *eventData1, void *eventData2, void *callbackData); The callback is executed in a separate thread every time a RTUtilEvent occurs on the system. If you are interested only in certain events, your callback must examine the event parameter passed in. The systemIP parameter contains the IP address of the system for which the event occurred. The systemMAC parameter contains the system MAC address. The callback return value is ignored. You do not need to explicitly unregister your callback. The callback stop receiving notifications once the operation for which it was registered has completed. Just before the callback is unregistered, it receives the RTUtilEvent_CallbackUnregistered event to indicate that it is safe to clean up callbackData, if necessary. The following lists RTUtilEvent events and relevant details for each event: Event Description RTUtilEvent_NewSystemStatus The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown RTUtilEvent_BeginCreateImage Beginning image creation operation. RTUtilEvent_EndCreateImage Finished image creation operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginApplyImage Beginning image application operation. RTUtilEvent_EndApplyImage Finished image application operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginFormatSystem Beginning system HD format operation. RTUtilEvent_EndFormatSystem Finished system HD format operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_EnumRemoteFiles Enumerating files on the remote system. RTUtilEvent_CreateLocalDirs Creating local image directory hierarchy. RTUtilEvent_BeginTransferFiles Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. RTUtilEvent_EndTransferFiles Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. RTUtilEvent_DeleteExistingFiles Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. RTUtilEvent_CheckingForSafeMode Checking that the remote system is booted into safe mode. RTUtilEvent_RebootIntoSafeMode Rebooting the remote system into safe mode. RTUtilEvent_RebootIntoInstallMode Rebooting the remote system into install mode. RTUtilEvent_BeginReboot Rebooting the remote system. RTUtilEvent_BeginFormattingHD Beginning hard drive format. RTUtilEvent_EndFormattingHD Hard drive finished reformatting. RTUtilEvent_GetFile Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_PutFile Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteFile Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteDir Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateLocalDir Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateRemoteDir Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CallbackUnregistered The callback is about to be unregistered. You can deallocate callbackData if necessary. |
| Event | Description |  |
| RTUtilEvent_NewSystemStatus | The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown |  |
| RTUtilEvent_BeginCreateImage | Beginning image creation operation. |  |
| RTUtilEvent_EndCreateImage | Finished image creation operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginApplyImage | Beginning image application operation. |  |
| RTUtilEvent_EndApplyImage | Finished image application operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginFormatSystem | Beginning system HD format operation. |  |
| RTUtilEvent_EndFormatSystem | Finished system HD format operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_EnumRemoteFiles | Enumerating files on the remote system. |  |
| RTUtilEvent_CreateLocalDirs | Creating local image directory hierarchy. |  |
| RTUtilEvent_BeginTransferFiles | Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. |  |
| RTUtilEvent_EndTransferFiles | Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. |  |
| RTUtilEvent_DeleteExistingFiles | Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. |  |
| RTUtilEvent_CheckingForSafeMode | Checking that the remote system is booted into safe mode. |  |
| RTUtilEvent_RebootIntoSafeMode | Rebooting the remote system into safe mode. |  |
| RTUtilEvent_RebootIntoInstallMode | Rebooting the remote system into install mode. |  |
| RTUtilEvent_BeginReboot | Rebooting the remote system. |  |
| RTUtilEvent_BeginFormattingHD | Beginning hard drive format. |  |
| RTUtilEvent_EndFormattingHD | Hard drive finished reformatting. |  |
| RTUtilEvent_GetFile | Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_PutFile | Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteFile | Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteDir | Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateLocalDir | Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateRemoteDir | Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CallbackUnregistered | The callback is about to be unregistered. You can deallocate callbackData if necessary. |  |
| callbackData | void * | A pointer-width value the library passes to the callback function through the callbackData parameter. You can use the callbackData as an integer value or as a pointer to a data object you want to access in the callback function. This way, you do not have to declare the data object as a global variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTConfig\RTConfig.cws for an example of using the FormatRTSystem function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvifreertutilmemory.htm language=enus -->
## TOPIC 00050: FreeRTUtilMemory

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvifreertutilmemory.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvifreertutilmemory.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### FreeRTUtilMemory

int FreeRTUtilMemory (void *pointer);

#### Purpose

Frees memory allocated by the Real-Time Utility Library.

|  | Note Do not call this function on system information pointers (RTSystemInfoPtr) returned by the library; you must call DisposeRTSystemInfo instead. |
| --- | --- |

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointer | void * | A pointer originally allocated by the Real-Time Utility Library. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the FreeRTUtilMemory function:

- realtime\RTConfig\RTConfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RTSystemImaging\RTSystemImaging.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigetledstate.htm language=enus -->
## TOPIC 00051: GetLedState

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigetledstate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigetledstate.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetLedState

int GetLedState (LedId LEDIdentifier, LedState *LEDState);

#### Purpose

Gets the state of an LED on the real-time target.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LEDIdentifier | LedId | The identifier of the LED for which this function will get the state. The LED identifier can be one of the following: kUser1Led kUser2Led kUser3Led kUser4Led Not all real-time targets have LEDs that can be accessed with this function. Even real-time targets with accessible LEDs might not have LEDs corresponding to each LED identifier. In rare cases, the labeling of the LEDs on the real-time target might not match the names of the LED identifiers. |
| Output |  |  |
| Name | Type | Description |
| LEDState | LedState | The current state of the specified LED. The LED state can be one of the following: kLedOff - The LED is off. kLedColor1 - The LED is on. kLedColor2 - The LED is on with an alternate color. Not all LEDs support this state. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigetrtmoduleaddr.htm language=enus -->
## TOPIC 00052: GetRTModuleAddr

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigetrtmoduleaddr.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigetrtmoduleaddr.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetRTModuleAddr

int GetRTModuleAddr (int moduleID, const char name[], void *address);

#### Purpose

Loads the address of the specified exported symbol from a DLL module.

The following code illustrates how to load the address of a function and call that function.

##### Example

void (__stdcall *funcPtr) (double dval, int *ival); 
 


int moduleId; 

int ival; 

int status; 
 


LoadRTModule ("my_dll.dll", &moduleId); 

if (moduleId != 0) 

{

GetRTModuleAddr (moduleId, "my_function", &funcPtr); 

 if (funcPtr != 0)

(*funcPtr) (1.0, &ival);

}

You must ensure that the calling convention used when calling through the function pointer matches the calling convention of the function as defined in the module. You can specify the calling convention in the function pointer declaration. In the preceding example, the function pointer is declared as __stdcall. If you do not specify a calling convention in the function pointer declaration, then the default calling convention will be used. To determine the default calling convention, select **Options»Build Options** in the Workspace window.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| moduleID | int | A module ID obtained from LoadRTModule. |
| name | const char [] | The name of the exported symbol whose address is to be obtained from the specified module. |
| Output |  |  |
| Name | Type | Description |
| address | void * | The address of the symbol with the specified name. If this function returns an error the address will be set to zero. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigetrtsysteminfo.htm language=enus -->
## TOPIC 00053: GetRTSystemInfo

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigetrtsysteminfo.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigetrtsysteminfo.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetRTSystemInfo

int GetRTSystemInfo (char address[], int addressType, RTSystemInfoPtr *systemInfo);

#### Purpose

Queries a specific RT system on the network for information about its identity and configuration.

GetRTSystemInfo returns the information in a system information pointer (RTSystemInfoPtr) that includes the system IP settings, MAC address, hostname, serial number, model description, system status, firmware revision, and so on.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| Output |  |  |
| Name | Type | Description |
| systemInfo | RTSystemInfoPtr | Output parameter that receives the RTSystemInfoPtr allocated by this function call. The library dynamically allocates the RTSystemInfoPtr and fills it with data retrieved from the RT system. You must remember to call DisposeRTSystemInfo when you finish using the returned pointer. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTSystemImaging\RTSystemImaging.cws for an example of using the GetRTSystemInfo function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigetrtutilerrorstring.htm language=enus -->
## TOPIC 00054: GetRTUtilErrorString

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigetrtutilerrorstring.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigetrtutilerrorstring.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetRTUtilErrorString

char *GetRTUtilErrorString (int error);

#### Purpose

Converts an error code returned by the Real-Time Utility Library into a meaningful error message.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| error | int | An error code returned by the Real-Time Utility Library. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| errorString | char * | The error message associated with the error number. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigetswitchstate.htm language=enus -->
## TOPIC 00055: GetSwitchState

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigetswitchstate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigetswitchstate.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetSwitchState

int GetSwitchState (SwitchId switchIdentifier, int *switchState);

#### Purpose

Gets the state of a switch on the real-time target.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| switchIdentifier | SwitchId | The identifier of the switch for which this function will get the state. The switch identifier can be one of the following: kBootSafeModeSwitch kResetIPAddressSwitch kDisableStartupAppSwitch kEnableSerialRedirectionSwitch kUser1Switch Not all real-time targets have switches that can be accessed with this function. Even real-time targets with accessible switches might not have switches corresponding to each switch identifier. In some cases, the labeling of the switches on the real-time target might not exactly match the names of the switch identifiers. |
| Output |  |  |
| Name | Type | Description |
| switchState | int | The state of the specified switch. The switch state is either zero (off) or non-zero (on). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvigettimeus.htm language=enus -->
## TOPIC 00056: GetTimeUS

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvigettimeus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvigettimeus.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### GetTimeUS

unsigned long long GetTimeUS (void);

#### Purpose

Returns the current time in microseconds since power was turned on to the real-time target.

RT This function is supported only on RT systems.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentTime | unsigned long long | Return value indicating the current time in microseconds since power was turned on to the real-time target. This value will never rollover to zero. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviloadrtmodule.htm language=enus -->
## TOPIC 00057: LoadRTModule

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviloadrtmodule.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviloadrtmodule.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### LoadRTModule

int LoadRTModule (const char pathname[], int *moduleID);

#### Purpose

Loads a DLL module. 
 


This function will also try to load any statically linked dependencies of the specified module. If any of the dependencies cannot be found or loaded, then the specified DLL will fail to load. 
 


After you load a module you can access symbols in that module by calling [GetRTModuleAddr](../rtutillib/cvigetrtmoduleaddr.htm). 
 


Each module loaded by this function is reference counted. The reference count increases each time you call LoadRTModule and decreases each time you call [UnloadRTModule](../rtutillib/cviunloadrtmodule.htm). When the reference count reaches zero the module is unloaded.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pathname | const char [] | The relative or absolute pathname of the DLL module to load. If pathname is a simple filename or relative path, then LoadRTModule will search the system path to locate the file. |
| Output |  |  |
| Name | Type | Description |
| moduleID | int | The ID of the loaded module. If this function returns an error the module ID will be set to zero. Zero is not a valid module ID. You can pass this value to GetRTModuleAddr and UnloadRTModule. When you are done using the module, call UnloadRTModule. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvilockrtsystem.htm language=enus -->
## TOPIC 00058: LockRTSystem

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvilockrtsystem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvilockrtsystem.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### LockRTSystem

int LockRTSystem (char address[], int addressType, char password[]);

#### Purpose

Secures the system with a **password** so that no one can remotely configure or alter the target without first providing the correct password.

A locked system cannot have software installed or removed or be otherwise configured from NI Measurement & Automation Explorer (MAX) or from the Real-Time Utility Library functions. FTP clients cannot connect to a locked system without logging in with the correct password. Additionally, if the system has the password-protect reboots property set (RTSystemInfoFlag_ProtectReboots), the system cannot reboot without the password or without being explicitly unlocked.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| password | char [] | The password with which to lock the system. There are no restrictions on the type of string that you can use as a password. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_clear.htm language=enus -->
## TOPIC 00059: NIWatchdog_Clear

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_clear.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_clear.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_Clear

int NIWatchdog_Clear (NIWatchdogHandle watchdog);

#### Purpose

Releases the watchdog timer hardware and frees memory associated with the watchdog timer object.

Call this function when you are finished using the watchdog timer.

If you configured the watchdog timer with a trigger line, then clearing the watchdog timer restores the trigger line to its default power-on state.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

#### Example

Refer to realtime\WatchdogRT\WatchdogRT.cws for an example of using the NIWatchdog_Clear function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_clearoutputs.htm language=enus -->
## TOPIC 00060: NIWatchdog_ClearOutputs

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_clearoutputs.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_clearoutputs.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_ClearOutputs

int NIWatchdog_ClearOutputs (NIWatchdogHandle watchdog);

#### Purpose

If the watchdog timer was configured with a trigger line then this function restores the trigger line to its default power-on state.

This function modifies the trigger line only if [NIWatchdog_Whack](../rtutillib/cviniwatchdog_whack.htm) reports the previous state of the watchdog timer as expired.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_configure.htm language=enus -->
## TOPIC 00061: NIWatchdog_Configure

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_configure.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_configure.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_Configure

int NIWatchdog_Configure (double timeoutRequested, int resetComputerOnExpiration, NIWatchdogTriggerLine triggerLine, NIWatchdogTriggerProtocol triggerProtocol, NIWatchdogHandle *watchdog, double *actualTimeout);

#### Purpose

Creates and configures a new [watchdog](../rtutillib/cviwatchdogfunctionsoverview.htm) timer.

Each watchdog timer object reserves a watchdog hardware counter on the system. As a result the number of watchdog timer objects you can have at one time is limited by the number of watchdog hardware counters on your computer. National Instruments RT Series PXI controllers usually have one watchdog hardware counter. You can clear a watchdog timer object by calling [NIWatchdog_Clear](../rtutillib/cviniwatchdog_clear.htm), which releases the hardware counter and allows a new watchdog timer object to use the hardware counter. If you do not clear a watchdog timer object, then the watchdog hardware counter will remain reserved and unavailable for use until you reboot the computer.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| timeoutRequested | double | The requested timeout in seconds for the watchdog timer. The timeout is the amount of time that must elapse before the watchdog timer counts down to zero and expires. The watchdog timer uses the requested timeout to choose initial count and time step values for a hardware counter. The hardware counter starts at the initial count and decrements by one each time the period indicated by the time step elapses. The initial count and timestep values are limited to those that can be exactly represented by the hardware counter. As a result, the actual timeout used by the watchdog timer might differ from the requested timeout. The actual timeout value is returned in the actualTimeout parameter. |
| resetComputerOnExpiration | int | Specifies whether to reboot the computer when the watchdog timer expires. |
| triggerLine | NIWatchdogTriggerLine | The trigger line to set when the watchdog timer expires. When the watchdog timer is in the running or expired state, the trigger line is set to the appropriate level depending on the value of the triggerProtocol parameter. When the watchdog timer is in the disabled state, the trigger line is in the default power-on state. Not all trigger lines exist on all systems or are supported on all systems. |
| triggerProtocol | NIWatchdogTriggerProtocol | Specifies whether to set the configured trigger line high (NIWatchdogTriggerProtocol_HighOnExpiration) or low (NIWatchdogTriggerProtocol_LowOnExpiration) when the watchdog timer is in the expired state. The trigger line is set to the opposite level while the watchdog timer is in the running state. |
| Output |  |  |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | The handle for the new watchdog timer object. When you finish using the watchdog timer object, call NIWatchdog_Clear to release the watchdog timer hardware and to free memory associated with the watchdog timer object. Zero is not a valid handle. |
| actualTimeout | double | The actual timeout in seconds used by the watchdog timer. The timeout is the amount of time that must elapse before the watchdog timer counts down to zero and expires. The actual timeout is determined by the initial count and time step values used to configure the watchdog hardware counter. The hardware counter starts at the initial count and decrements by one each time the period indicated by the time step elapses. The initial count and timestep values are limited to those that can be exactly represented by the hardware counter. As a result, the actual timeout used by the watchdog timer might differ from the requested timeout. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

#### Example

Refer to realtime\WatchdogRT\WatchdogRT.cws for an example of using the NIWatchdog_Configure function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_disable.htm language=enus -->
## TOPIC 00062: NIWatchdog_Disable

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_disable.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_disable.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_Disable

int NIWatchdog_Disable (NIWatchdogHandle watchdog);

#### Purpose

Puts the watchdog timer in the disabled state.

If you configured the watchdog timer with a trigger line, then disabling the watchdog timer restores the trigger line to its default power-on state.

Call the [NIWatchdog_Whack](../rtutillib/cviniwatchdog_whack.htm) function to restart a disabled watchdog timer.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_getattribute.htm language=enus -->
## TOPIC 00063: NIWatchdog_GetAttribute

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_getattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_getattribute.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_GetAttribute

int NIWatchdog_GetAttribute (NIWatchdogHandle watchdog, NIWatchdogAttribute attribute, void *value);

#### Purpose

Gets the value of a watchdog timer attribute.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |
| attribute | NIWatchdogAttribute | The watchdog timer attribute to obtain. |
| Output |  |  |
| Name | Type | Description |
| value | void * | The value of the specified watchdog timer attribute. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_setattribute.htm language=enus -->
## TOPIC 00064: NIWatchdog_SetAttribute

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_setattribute.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_setattribute.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_SetAttribute

int NIWatchdog_SetAttribute (NIWatchdogHandle watchdog, NIWatchdogAttribute attribute, ...);

#### Purpose

Sets the value of a watchdog timer attribute.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |
| attribute | NIWatchdogAttribute | The watchdog timer attribute to set. |
| value | ... | The value to which the specified watchdog timer attribute is set. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviniwatchdog_whack.htm language=enus -->
## TOPIC 00065: NIWatchdog_Whack

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviniwatchdog_whack.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviniwatchdog_whack.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdog_Whack

int NIWatchdog_Whack (NIWatchdogHandle watchdog, int restartExpiredWatchdog, NIWatchdogState *previousState);

#### Purpose

Whacks the [watchdog](../rtutillib/cviwatchdogfunctionsoverview.htm) timer. The state of the watchdog timer determines the exact behavior. [NIWatchdog_Configure](../rtutillib/cviniwatchdog_configure.htm) creates new watchdog timers in the disabled state.

If the watchdog timer is in the disabled state, this function resets the hardware counter to the initial count, starts the countdown, and changes the state to running.

If the watchdog timer is in the running state, this function resets the hardware counter to the initial count and the countdown continues. The watchdog timer remains in the running state.

If the watchdog timer is in the expired state, the behavior of this function depends on the **restartExpiredWatchdog** parameter. If the **restartExpiredWatchdog** parameter is true, this function resets the hardware counter to the initial count, starts the countdown, and changes the state to running. If the **restartExpiredWatchdog** parameter is false this function does not modify the watchdog timer.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| watchdog | NIWatchdogHandle | A watchdog timer handle obtained from NIWatchdog_Configure. |
| restartExpiredWatchdog | int | Specifies whether to restart the watchdog timer when it is in the expired state. If this parameter is true, this function resets the hardware counter to the initial count, starts the countdown, and changes the state to running. If you configured the watchdog timer with a trigger line, restarting the watchdog timer also resets the trigger line. If this parameter is false, this function does not modify the watchdog timer. If you configured the watchdog timer with a trigger line, the trigger line will remain set. |
| Output |  |  |
| Name | Type | Description |
| previousState | NIWatchdogState | The state of the watchdog timer when this function is called, but before any changes are made. Watchdog timers have the following states: NIWatchdogState_Disabled—The watchdog timer has just been created by a call to NIWatchdog_Configure or has just been disabled by a call to NIWatchdog_Disable. The watchdog timer is not counting down while in this state. NIWatchdogState_Running—The watchdog timer is counting down but has not reached zero. NIWatchdogState_Expired—The watchdog timer has finished counting down to zero. When the watchdog timer enters the expired state it might reset the computer or set a trigger line, depending on how it was configured. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

#### Example

Refer to realtime\WatchdogRT\WatchdogRT.cws for an example of using the NIWatchdog_Whack function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvirebootrtsystem.htm language=enus -->
## TOPIC 00066: RebootRTSystem

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvirebootrtsystem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvirebootrtsystem.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### RebootRTSystem

int RebootRTSystem (char address[], int addressType, int timeout, ProgressCallbackType callback, void *callbackData);

#### Purpose

Reboots a remote real-time system.

If you specify a **timeout**, this function waits for the reboot to complete before returning. Otherwise, the function returns immediately.

You can provide a **callback** to asynchronously receive updates on the progress of the reboot.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| timeout | int | The maximum number of seconds to wait for the system to finish rebooting before returning the error kRTTimeout. To have the function return immediately without waiting for the reboot to complete, pass -1. |
| callback | ProgressCallbackType | A callback function that receives notification of events that occur on the system. You can pass NULL if you do not want to register a callback. The callback function, type ProgressCallback, takes the following form: int CVICALLBACK CallbackFunc (const char *systemIP, const char *systemMAC, int event, void *eventData1, void *eventData2, void *callbackData); The callback is executed in a separate thread every time a RTUtilEvent occurs on the system. If you are interested only in certain events, your callback must examine the event parameter passed in. The systemIP parameter contains the IP address of the system for which the event occurred. The systemMAC parameter contains the system MAC address. The callback return value is ignored. You do not need to explicitly unregister your callback. The callback stop receiving notifications once the operation for which it was registered has completed. Just before the callback is unregistered, it receives the RTUtilEvent_CallbackUnregistered event to indicate that it is safe to clean up callbackData, if necessary. The following lists RTUtilEvent events and relevant details for each event: Event Description RTUtilEvent_NewSystemStatus The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown RTUtilEvent_BeginCreateImage Beginning image creation operation. RTUtilEvent_EndCreateImage Finished image creation operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginApplyImage Beginning image application operation. RTUtilEvent_EndApplyImage Finished image application operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_BeginFormatSystem Beginning system HD format operation. RTUtilEvent_EndFormatSystem Finished system HD format operation. eventData1 (int *)—Pointer to the return code. RTUtilEvent_EnumRemoteFiles Enumerating files on the remote system. RTUtilEvent_CreateLocalDirs Creating local image directory hierarchy. RTUtilEvent_BeginTransferFiles Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. RTUtilEvent_EndTransferFiles Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. RTUtilEvent_DeleteExistingFiles Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. RTUtilEvent_CheckingForSafeMode Checking that the remote system is booted into safe mode. RTUtilEvent_RebootIntoSafeMode Rebooting the remote system into safe mode. RTUtilEvent_RebootIntoInstallMode Rebooting the remote system into install mode. RTUtilEvent_BeginReboot Rebooting the remote system. RTUtilEvent_BeginFormattingHD Beginning hard drive format. RTUtilEvent_EndFormattingHD Hard drive finished reformatting. RTUtilEvent_GetFile Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_PutFile Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteFile Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_DeleteDir Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateLocalDir Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CreateRemoteDir Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). RTUtilEvent_CallbackUnregistered The callback is about to be unregistered. You can deallocate callbackData if necessary. |
| Event | Description |  |
| RTUtilEvent_NewSystemStatus | The status of the system changed. eventData1 (int *)—Pointer to the new status. One of RTSystemStatus_Rebooting, RTSystemStatus_Initializing, RTSystemStatus_Connected, RTSystemStatus_Disconnected, RTSystemStatus_Unconfigured, RTSystemStatus_Unknown |  |
| RTUtilEvent_BeginCreateImage | Beginning image creation operation. |  |
| RTUtilEvent_EndCreateImage | Finished image creation operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginApplyImage | Beginning image application operation. |  |
| RTUtilEvent_EndApplyImage | Finished image application operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_BeginFormatSystem | Beginning system HD format operation. |  |
| RTUtilEvent_EndFormatSystem | Finished system HD format operation. eventData1 (int *)—Pointer to the return code. |  |
| RTUtilEvent_EnumRemoteFiles | Enumerating files on the remote system. |  |
| RTUtilEvent_CreateLocalDirs | Creating local image directory hierarchy. |  |
| RTUtilEvent_BeginTransferFiles | Beginning transfer of a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of files. |  |
| RTUtilEvent_EndTransferFiles | Finished transferring a batch of files to/from the remote system. eventData1 (int *)—Pointer to the number of failures. eventData2 (const char *)—Semicolon-separated list of failed file paths. |  |
| RTUtilEvent_DeleteExistingFiles | Deleting files and/or directories from the remote system. eventData1 (int *)—Pointer to the number of files to delete. eventData2 (int *)—Pointer to the number of directories to remove. |  |
| RTUtilEvent_CheckingForSafeMode | Checking that the remote system is booted into safe mode. |  |
| RTUtilEvent_RebootIntoSafeMode | Rebooting the remote system into safe mode. |  |
| RTUtilEvent_RebootIntoInstallMode | Rebooting the remote system into install mode. |  |
| RTUtilEvent_BeginReboot | Rebooting the remote system. |  |
| RTUtilEvent_BeginFormattingHD | Beginning hard drive format. |  |
| RTUtilEvent_EndFormattingHD | Hard drive finished reformatting. |  |
| RTUtilEvent_GetFile | Getting a file from the remote system. eventData1 (const char *)—File path (local). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_PutFile | Sending a file to the remote system. eventData1 (const char *)—File path (remote). eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteFile | Deleting a file from the remote system. eventData1 (const char *)—File path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_DeleteDir | Deleting a directory from the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateLocalDir | Creating a local directory. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CreateRemoteDir | Creating a directory on the remote system. eventData1 (const char *)—Directory path. eventData2 (int *)—Pointer to the 0-based index (in the batch). |  |
| RTUtilEvent_CallbackUnregistered | The callback is about to be unregistered. You can deallocate callbackData if necessary. |  |
| callbackData | void * | A pointer-width value the library passes to the callback function through the callbackData parameter. You can use the callbackData as an integer value or as a pointer to a data object you want to access in the callback function. This way, you do not have to declare the data object as a global variable. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the RebootRTSystem function:

- realtime\RTConfig\RTConfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RTSystemImaging\RTSystemImaging.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvirtisshuttingdown.htm language=enus -->
## TOPIC 00067: RTIsShuttingDown

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvirtisshuttingdown.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvirtisshuttingdown.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### RTIsShuttingDown

int RTIsShuttingDown (void);

#### Purpose

Indicates whether the real-time target is shutting down.

You can use RTIsShuttingDown to programmatically determine when to run the cleanup code in a real-time application, as follows:

void CVIFUNC_C RTmain (void) 

{

if (InitCVIRTE (0, 0, 0) == 0)

return; /* out of memory */

/* your initialization code */

while (!RTIsShuttingDown ())

{ 
 

 /* your code */ 
 

 
 }

/* your cleanup code */

CloseCVIRTE ();

}

RT This function is supported only on RT systems.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| shuttingDown | int | Indicates whether the real-time target is shutting down. RTIsShuttingDown initially returns false. The following table describes when RTIsShuttingDown returns true and the behavior of the cleanup code and the real-time target. Shutdown Method During Development and Debugging After the DLL is Deployed on an RT Target Select Run»Simulate RT Shutting Down The cleanup code runs to completion. The real-time target does not reboot. Not applicable. Select Run»Abort Execution and Reboot Target The cleanup code is not guaranteed to run to completion. The real-time target reboots. Not applicable. Reboot through MAX The cleanup code is not guaranteed to run to completion. The real-time target reboots. The cleanup code runs to completion. The real-time target reboots. National Instruments recommends that you use the Simulate RT Shutting Down item to terminate execution while you are debugging. Code Description 1 The real-time target is shutting down. 0 The real-time target is not shutting down. |
| Shutdown Method | During Development and Debugging | After the DLL is Deployed on an RT Target |
| Select Run»Simulate RT Shutting Down | The cleanup code runs to completion. The real-time target does not reboot. | Not applicable. |
| Select Run»Abort Execution and Reboot Target | The cleanup code is not guaranteed to run to completion. The real-time target reboots. | Not applicable. |
| Reboot through MAX | The cleanup code is not guaranteed to run to completion. The real-time target reboots. | The cleanup code runs to completion. The real-time target reboots. |
| Code | Description |  |
| 1 | The real-time target is shutting down. |  |
| 0 | The real-time target is not shutting down. |  |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.1 and later

#### Examples

Refer to the following examples that use the RTIsShuttingDown function:

- realtime\FileIORT\FileIORT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\LoopTimingRT\LoopTimingRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\NetworkVariableRT\NetworkVariableRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RS-232RT\DebugViaCom.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RS-232RT\Messages.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\SymmetricMultiprocessingRT\SymmetricMultiprocessingRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\ThreadPriorityRT\ThreadPriorityRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\WatchdogRT\WatchdogRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvirtsystemselectpopup.htm language=enus -->
## TOPIC 00068: RTSystemSelectPopup

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvirtsystemselectpopup.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvirtsystemselectpopup.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### RTSystemSelectPopup

int RTSystemSelectPopup (int options, RTSystemInfoPtr **systems);

#### Purpose

Presents a selection dialog box displaying a list of all running RT systems detected on the local subnet. The user can select one or more systems from this list; the selected systems are returned as an array of RTSystemInfoPtr objects.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| options | int | A bit field consisting of 0 or more RTUtilOption flags bitwise OR-ed together. You can specify the following flags: Flag Description RTUtilOption_ShowUnconfigured Allow unconfigured systems (IP of "0.0.0.0") to appear in the selection list. RTUtilOption_AllowMultipleSelect Show checkboxes in the selection list so that the user may select multiple systems. By default, no checkboxes are shown, and the user may select only one system. RTUtilOption_DefaultSelectAll Initially select all systems (applies only to multiple selection). RTUtilOption_ShowIPAddressColumn Add a column to the selection list that shows each system's IP address. RTUtilOption_ShowMACAddressColumn Add a column to the selection list that shows each system's MAC address. RTUtilOption_ShowModelColumn Add a column to the selection list that shows each system's model type (e.g. "Generic Desktop PC", "PXI-0000"). RTUtilOption_ShowSerialNumberColumn Add a column to the selection list that shows each system's serial number. |
| Flag | Description |  |
| RTUtilOption_ShowUnconfigured | Allow unconfigured systems (IP of "0.0.0.0") to appear in the selection list. |  |
| RTUtilOption_AllowMultipleSelect | Show checkboxes in the selection list so that the user may select multiple systems. By default, no checkboxes are shown, and the user may select only one system. |  |
| RTUtilOption_DefaultSelectAll | Initially select all systems (applies only to multiple selection). |  |
| RTUtilOption_ShowIPAddressColumn | Add a column to the selection list that shows each system's IP address. |  |
| RTUtilOption_ShowMACAddressColumn | Add a column to the selection list that shows each system's MAC address. |  |
| RTUtilOption_ShowModelColumn | Add a column to the selection list that shows each system's model type (e.g. "Generic Desktop PC", "PXI-0000"). |  |
| RTUtilOption_ShowSerialNumberColumn | Add a column to the selection list that shows each system's serial number. |  |
| Output |  |  |
| Name | Type | Description |
| systems | RTSystemInfoPtr * | If the user selects one or more systems from the list, this parameter returns a null-terminated array containing a RTSystemInfoPtr for each selected system. If the user cancels the popup, a null pointer will be returned instead of an array. If data is returned, this function allocates memory for the RTSystemInfoPtr items and the array that contains them. You must call DisposeRTSystemInfo on each RTSystemInfoPtr in the returned array. You must also free the array itself by calling FreeRTUtilMemory. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| OK | int | 0 if the user cancelled the dialog, 1 otherwise. No errors are returned by the function. Any errors that occur as a result of calling this function are reported directly by error popups. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisetledstate.htm language=enus -->
## TOPIC 00069: SetLedState

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisetledstate.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisetledstate.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SetLedState

int SetLedState (LedId LEDIdentifier, LedState LEDState);

#### Purpose

Sets the state of an LED on the real-time target.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LEDIdentifier | LedId | The identifier of the LED for which this function will set the state. The LED identifier can be one of the following: kUser1Led kUser2Led kUser3Led kUser4Led Not all real-time targets have LEDs that can be accessed with this function. Even real-time targets with accessible LEDs might not have LEDs corresponding to each LED identifier. In rare cases, the labeling of the LEDs on the real-time target might not match the names of the LED identifiers. |
| LEDState | LedState | The state of the specified LED. The LED state can be one of the following: kLedOff - The LED is off. kLedColor1 - The LED is on. kLedColor2 - The LED is on with an alternate color. Not all LEDs support this state. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisetprocessoraffinityforthread.htm language=enus -->
## TOPIC 00070: SetProcessorAffinityForThread

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisetprocessoraffinityforthread.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisetprocessoraffinityforthread.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SetProcessorAffinityForThread

int SetProcessorAffinityForThread (int processorPoolID, int processorIndex, int *previousProcessorPoolID, int *previousProcessorIndex);

#### Purpose

Configures the current thread to run on a pool of processors or on one individual processor.

Processor affinity changes take effect the next time the operating system schedules the current thread to run. You can force a thread to give up the remainder of its current timeslice by calling the Windows SDK function Sleep with a sleep duration of 0. The next time the thread executes, it reflects the new processor affinity settings.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| processorPoolID | int | The pool of processors on which to run the thread. You must pass one of the following values: Value Description kProcessorPool_System By default, all threads in the system are assigned to the system pool. Operating system threads are always assigned to this pool. The operating system schedules all threads assigned to this pool to the group of processors included in the pool. The operating system automatically moves threads between processors to balance the load between the processors. By default, the system processor pool includes all processors on the system. You can change the set of processors included in the system pool by calling ConfigureProcessorPool. The system pool always includes the first processor in the system. The first processor in the system is unique because it processes all interrupts in the system. kProcessorPool_None Use this pool ID to indicate that the thread should not be assigned to a pool and that you will assign this thread to a specific processor. You specify the particular processor for this thread with the processorIndex parameter. |
| Value | Description |  |
| kProcessorPool_System | By default, all threads in the system are assigned to the system pool. Operating system threads are always assigned to this pool. The operating system schedules all threads assigned to this pool to the group of processors included in the pool. The operating system automatically moves threads between processors to balance the load between the processors. By default, the system processor pool includes all processors on the system. You can change the set of processors included in the system pool by calling ConfigureProcessorPool. The system pool always includes the first processor in the system. The first processor in the system is unique because it processes all interrupts in the system. |  |
| kProcessorPool_None | Use this pool ID to indicate that the thread should not be assigned to a pool and that you will assign this thread to a specific processor. You specify the particular processor for this thread with the processorIndex parameter. |  |
| processorIndex | int | If you pass kProcessorPool_None for the processorPoolID parameter, this value specifies the zero-based index of the single processor on which the thread can run. The index must represent a valid processor on the system. You can determine the total number of processors on the system by calling CmtGetNumProcessors. If you pass any other value for the processorPoolID parameter, LabWindows/CVI ignores this value. |
| Output |  |  |
| Name | Type | Description |
| previousProcessorPoolID | int | Returns the processor pool ID of the thread before you called this function. You can pass NULL for this parameter. |
| previousProcessorIndex | int | If the previousProcessorPoolID parameter returns kProcessorPool_None, then this parameter returns the processor index of the thread before you called this function. Otherwise this parameter returns -1. You can pass NULL for this parameter. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\SymmetricMultiprocessingRT\SymmetricMultiprocessingRT.cws for an example of using the SetProcessorAffinityForThread function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisetrtipconfiguration.htm language=enus -->
## TOPIC 00071: SetRTIPConfiguration

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisetrtipconfiguration.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisetrtipconfiguration.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SetRTIPConfiguration

int SetRTIPConfiguration (char address[], int addressType, SystemIPSettings *IPSettings);

#### Purpose

Changes the IP configuration settings of an RT system.

|  | Note LabWindows/CVI does not apply changes to the IP settings until the next time you reboot. If you query the system IP settings after calling this function but before rebooting, GetRTSystemInfo returns the original settings. To initiate a reboot, call RebootRTSystem. |
| --- | --- |

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| IPSettings | SystemIPSettings * | A pointer to a SystemIPSettings structure that contains the new IP settings. You must fill out all fields of the structure appropriately, even if you want to change only one setting. You can reuse the SystemIPSettings ip field of the RTSystemInfoPtr returned by GetRTSystemInfo or FindAllRTSystemsOnSubnet. Edit the values you want to change, and pass the updated SystemIPSettings pointer into this function. If you set usingDHCP to true, this function ignores any addresses you specify, and the system instead uses DHCP to set its IP stack. Note LabWindows/CVI does not apply changes to the IP settings until the next time you reboot. If you query the system IP settings after calling this function but before rebooting, SetRTIPConfiguration returns the original settings. To initiate a reboot, call RebootRTSystem. |
|  | Note LabWindows/CVI does not apply changes to the IP settings until the next time you reboot. If you query the system IP settings after calling this function but before rebooting, SetRTIPConfiguration returns the original settings. To initiate a reboot, call RebootRTSystem. |  |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the SetRTIPConfiguration function:

- realtime\RTConfig\RTConfig.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RTSystemImaging\RTSystemImaging.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisetrtsystemsetting.htm language=enus -->
## TOPIC 00072: SetRTSystemSetting

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisetrtsystemsetting.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisetrtsystemsetting.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SetRTSystemSetting

int SetRTSystemSetting (char address[], int addressType, int setting, ...);

#### Purpose

Changes settings of an RT system.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| setting | int | The system setting to change. You can specify one of the following values: Value Data Type Description RTSystemSetting_Hostname char * The hostname assigned to the system. RTSystemSetting_Comment char * (up to 64 bytes) A message attached to the system. The usage and interpretation of this message is user-defined. RTSystemSetting_ProtectReboots int A boolean indicating whether the system requires a password to reboot when it is locked. RTSystemSetting_HaltIfTCPFails int A boolean indicating whether to abort system startup if a TCP/IP (including DHCP) failure occurs at boot time. |
| Value | Data Type | Description |
| RTSystemSetting_Hostname | char * | The hostname assigned to the system. |
| RTSystemSetting_Comment | char * (up to 64 bytes) | A message attached to the system. The usage and interpretation of this message is user-defined. |
| RTSystemSetting_ProtectReboots | int | A boolean indicating whether the system requires a password to reboot when it is locked. |
| RTSystemSetting_HaltIfTCPFails | int | A boolean indicating whether to abort system startup if a TCP/IP (including DHCP) failure occurs at boot time. |
| value | ... | The new value to assign to setting. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTConfig\RTConfig.cws for an example of using the SetRTSystemSetting function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisleepuntilnextmultipleus.htm language=enus -->
## TOPIC 00073: SleepUntilNextMultipleUS

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisleepuntilnextmultipleus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisleepuntilnextmultipleus.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SleepUntilNextMultipleUS

unsigned int SleepUntilNextMultipleUS (unsigned int multiple);

#### Purpose

Suspends the current thread until the next multiple of the specified number of microseconds.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| multiple | unsigned int | Specifies the multiple in microseconds. In effect, this is the maximum amount of time the thread will sleep. The thread will resume execution when the low-order 32 bits of the value returned by GetTimeUS is a multiple of the specified number of microseconds. The maximum sleep duration you can specify with this function is approximately 71 minutes. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentTime | unsigned int | Return value indicating the current time in microseconds since power was turned on to the real-time target. This value corresponds to the low-order 32 bits of the value returned by GetTimeUS. This value will rollover to zero approximately every 71 minutes. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisleepuntilus.htm language=enus -->
## TOPIC 00074: SleepUntilUS

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisleepuntilus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisleepuntilus.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SleepUntilUS

unsigned int SleepUntilUS (unsigned int targetTime);

#### Purpose

Suspends the current thread until the specified target time.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetTime | unsigned int | Specifies the target time when you want the thread to resume execution after it suspends. You may add the desired number of microseconds to the return value of GetTimeUS or any of the other Microsecond Sleep functions to obtain the desired target time. The thread will resume execution when the low-order 32 bits of the value returned by GetTimeUS matches the specified target time. The maximum sleep duration you can specify with this function is approximately 71 minutes. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentTime | unsigned int | Return value indicating the current time in microseconds since power was turned on to the real-time target. This value corresponds to the low-order 32 bits of the value returned by GetTimeUS. This value will rollover to zero approximately every 71 minutes. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvisleepus.htm language=enus -->
## TOPIC 00075: SleepUS

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvisleepus.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvisleepus.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### SleepUS

unsigned int SleepUS (unsigned int duration);

#### Purpose

Suspends the current thread for the specified number of microseconds.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| duration | unsigned int | Specifies the sleep duration in microseconds. The maximum sleep duration is approximately 71 minutes. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| currentTime | unsigned int | Return value indicating the current time in microseconds since power was turned on to the real-time target. This value corresponds to the low-order 32 bits of the value returned by GetTimeUS. This value will rollover to zero approximately every 71 minutes. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Examples

Refer to the following examples that use the SleepUS function:

- realtime\FileIORT\FileIORT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\LoopTimingRT\LoopTimingRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\NetworkVariableRT\NetworkVariableRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\RS-232RT\DebugViaCom.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\SymmetricMultiprocessingRT\SymmetricMultiprocessingRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\ThreadPriorityRT\ThreadPriorityRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example
- realtime\WatchdogRT\WatchdogRT.cws 
 [IMAGE alt='image' src='open.gif'] Open example

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitraceconfigure.htm language=enus -->
## TOPIC 00076: TraceConfigure

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitraceconfigure.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitraceconfigure.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceConfigure

int TraceConfigure (int functionCalls, int threads, int details, int requestedBufferSize, int *actualBufferSize);

#### Purpose

Configures execution tracing on the real-time target.

|  | Note You must set the Real-time function tracing option in the Target Settings dialog box to User-defined functions only or User-defined functions and library functions to log function activity. |
| --- | --- |

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| functionCalls | int | Specifies whether to include function activity in the trace session. |
| threads | int | Specifies whether to include thread activity in the trace session. |
| details | int | Specifies whether to include more detailed information in the trace session. This information includes sleep spans, wait for object spans, wait for memory spans, and priority inheritance spans. |
| requestedBufferSize | int | The number of bytes you want to reserve for trace sessions on the RT target. The TraceStart function uses a memory buffer to store function and thread events. The memory buffer might not be able to store all the trace information, depending on the length of the trace session and the amount of detail that you record. In this case, the TraceStart function removes the oldest entries in the buffer to accommodate newer entries, and your trace will not begin with a call to TraceStart. You must reboot the RT target before you can change the size of the buffer. The first call to TraceConfigure or TraceStart after a reboot of the real-time target allocates the internal buffer; subsequent calls do not change the buffer size. Pass 0 or a negative value if you want to use the default buffer size of 250 KB. |
| Output |  |  |
| Name | Type | Description |
| actualBufferSize | int | The actual size of the memory buffer in bytes. Pass NULL if you do not need this information. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitraceloadandsend.htm language=enus -->
## TOPIC 00077: TraceLoadAndSend

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitraceloadandsend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitraceloadandsend.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceLoadAndSend

int TraceLoadAndSend (char filename[], char hostAddress[]);

#### Purpose

Loads a trace session and sends it to the Real-Time Trace Viewer running on the host computer that you specify with **hostAddress**.

|  | Note Ensure that the Real-Time Trace Viewer is running on the host computer when you call this function. Otherwise, the function returns an error. |
| --- | --- |

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | char [] | The name of the file containing the trace session. You can specify simple filenames, relative paths, and absolute paths. |
| hostAddress | char [] | The machine name or IP address of the host computer on which you are running the Real-Time Trace Viewer. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitracesetthreadname.htm language=enus -->
## TOPIC 00078: TraceSetThreadName

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitracesetthreadname.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitracesetthreadname.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceSetThreadName

int TraceSetThreadName (char threadName[]);

#### Purpose

Sets the display name that will be used for the current thread when viewing the trace session in the Real-Time Trace Viewer.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| threadName | char [] | The display name for the current thread. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 2012 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitracestart.htm language=enus -->
## TOPIC 00079: TraceStart

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitracestart.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitracestart.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceStart

int TraceStart (void);

#### Purpose

Starts the trace session.

By default, TraceStart logs function and thread events and logs detailed events, which include system events. TraceStart uses a default buffer size of 250 KB to log trace sessions. If you reach the memory buffer limit when logging event data, TraceStart overwrites the oldest data in the buffer.

If you want to specify the size of the buffer and whether to enable or disable the logging of function, thread, and detailed events, call [TraceConfigure](../rtutillib/cvitraceconfigure.htm).

TraceStart logs data until you call [TraceStopAndSend](../rtutillib/cvitracestopandsend.htm) or [TraceStopAndSave](../rtutillib/cvitracestopandsave.htm).

|  | Note You must set the Real-time function tracing option in the Target Settings dialog box to User-defined functions only or User-defined functions and library functions to log function activity. |
| --- | --- |

RT This function is supported only on RT systems.

#### Parameters

None.

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitracestopandsave.htm language=enus -->
## TOPIC 00080: TraceStopAndSave

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitracestopandsave.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitracestopandsave.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceStopAndSave

int TraceStopAndSave (char filename[]);

#### Purpose

Stops logging event data and saves the trace session to the file and location you specify with **filename**.

Ensure that all threads you want to trace are still running at the time you stop tracing. If any threads exit while tracing is in progress, those threads display as Terminated (Name Unknown) when you view the trace session in the Real-Time Trace Viewer.

You can manually transfer the saved trace session to a computer running the Real-Time Trace Viewer. Select **File»Open** to load the trace session in the Real-Time Trace Viewer.

You also can programmatically transfer and load the saved trace session in the Real-Time Trace Viewer using [TraceLoadAndSend](../rtutillib/cvitraceloadandsend.htm).

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| filename | char [] | The name of the file to which to save the trace session. You can specify simple filenames, relative paths, and absolute paths. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitracestopandsend.htm language=enus -->
## TOPIC 00081: TraceStopAndSend

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitracestopandsend.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitracestopandsend.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceStopAndSend

int TraceStopAndSend (char hostAddress[]);

#### Purpose

Stops logging event data and sends the trace session to the Real-Time Trace Viewer running on the host computer that you specify with **hostAddress**.

Ensure that all threads you want to trace are still running at the time you stop tracing. If any threads exit while tracing is in progress, those threads display as Terminated (Name Unknown) when you view the trace session in the Real-Time Trace Viewer.

|  | Note Ensure that the Real-Time Trace Viewer is running on the host computer when you call this function. Otherwise, the function returns an error. |
| --- | --- |

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| hostAddress | char [] | The machine name or IP address of the host computer on which you are running the Real-Time Trace Viewer. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cvitraceuserevent.htm language=enus -->
## TOPIC 00082: TraceUserEvent

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cvitraceuserevent.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cvitraceuserevent.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### TraceUserEvent

int TraceUserEvent (int userEvent);

#### Purpose

Records a [user event](/csh?topicname=cvitracehelp/log_view_custom_events.html) in the trace session. The Real-Time Trace Viewer displays user events in the Thread view.

User events are helpful if you want to track specific activity in your application in the Real-Time Trace Viewer. For example, if you want to track each time that your application acquires a global lock, you can decide that event 0 will track those occurrences. Each time you acquire a global lock in your application, add the following call:

TraceUserEvent(0);

The Real-Time Trace Viewer displays a flag to indicate each occurrence of the user event.

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| userEvent | int | The number of the event (0-255). |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviunloadrtmodule.htm language=enus -->
## TOPIC 00083: UnloadRTModule

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviunloadrtmodule.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviunloadrtmodule.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### UnloadRTModule

int UnloadRTModule (int moduleID);

#### Purpose

Unloads a DLL module. 
 


Each module loaded by [LoadRTModule](../rtutillib/cviloadrtmodule.htm) is reference counted. The reference count increases each time you call LoadRTModule and decreases each time you call UnloadRTModule. When the reference count reaches zero the module is unloaded. 
 


When the module is unloaded you can no longer use the module ID or addresses obtained from [GetRTModuleAddr](../rtutillib/cvigetrtmoduleaddr.htm).

RT This function is supported only on RT systems.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| moduleID | int | A module ID obtained from LoadRTModule. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 9.0 and later

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviunlockrtsystem.htm language=enus -->
## TOPIC 00084: UnlockRTSystem

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviunlockrtsystem.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviunlockrtsystem.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### UnlockRTSystem

int UnlockRTSystem (char address[], int addressType, char password[]);

#### Purpose

Unlocks a previously locked system.

Windows This function is supported only on Windows.

#### Parameters

| Input |  |  |
| --- | --- | --- |
| Name | Type | Description |
| address | char [] | Specifies RT system on which to operate. You can pass the IP address, DNS-resolvable hostname, or MAC address. You must specify IP addresses in dot-decimal format, as a sequence of 4 decimal octets separated by dots. An example of an IP address is 127.0.0.1. You must specify MAC addresses as a sequence of 6 hexadecimal octets separated by colons. An example of a MAC address is 00:AB:11:CD:2e:3f. Letters can be uppercase, lowercase, or mixed case. Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |
|  | Note Newly formatted or otherwise unconfigured systems, which appear in MAX 0.0.0.0, do not have assigned IP addresses. To call this function on an unconfigured system, you must specify its MAC address. |  |
| addressType | int | Specifies the type of address string you pass to the address parameter. You can pass one of the following values: Value Description Example AddressType_IP An IP address or DNS-resolvable hostname. 127.0.0.1 SomeHost AddressType_MAC A MAC address. 01:23:45:AB:CD:EF |
| Value | Description | Example |
| AddressType_IP | An IP address or DNS-resolvable hostname. | 127.0.0.1 SomeHost |
| AddressType_MAC | A MAC address. | 01:23:45:AB:CD:EF |
| password | char [] | The password to use to unlock the system. |

#### Return Value

| Name | Type | Description |
| --- | --- | --- |
| status | int | Return value indicating whether the function was successful. Unless otherwise stated, zero indicates successful execution and a negative number indicates that an error occurred. You can call the GetRTUtilErrorString function to obtain a message that describes the error. |

#### Additional Information

**Library:** [Real-Time Utility Library](../rtutillib/rtutillibtree.htm)

**Include file:** rtutil.h

**LabWindows/CVI compatibility:** LabWindows/CVI 8.5 and later

#### Example

Refer to realtime\RTConfig\RTConfig.cws for an example of using the UnlockRTSystem function.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/cviwatchdogfunctionsoverview.htm language=enus -->
## TOPIC 00085: NI Watchdog Functions

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/cviwatchdogfunctionsoverview.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/cviwatchdogfunctionsoverview.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NI Watchdog Functions

The NI Watchdog functions require NI Watchdog 3.0 or later to be installed on the real-time target. You can install NI Watchdog to the host computer from the National Instruments Device Drivers media. Use the Remote Systems item in the configuration tree in NI Measurement & Automation Explorer (MAX) to install this item from the host computer to the target.

You can use the NI Watchdog functions only on supported National Instruments RT Series PXI controllers.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/listofwatchdogattrs.htm language=enus -->
## TOPIC 00086: List of Watchdog Attributes

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/listofwatchdogattrs.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/listofwatchdogattrs.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### List of Watchdog Attributes

The following list contains the watchdog attributes. You can get and set the watchdog attributes using NIWatchdog_GetAttribute and NIWatchdog_SetAttribute.

[Initial Count](niwatchdogattribute_initialcount.html)

[Time Step](niwatchdogattribute_timestep.html)

[Total Timeout](niwatchdogattribute_totaltimeout.html)

[Whack Input Sequence](niwatchdogattribute_whackinputsource.html)

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/niwatchdogattribute_initialcount.html language=enus -->
## TOPIC 00087: NIWatchdogAttribute_InitialCount

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/niwatchdogattribute_initialcount.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/niwatchdogattribute_initialcount.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdogAttribute_InitialCount

| Data Type: | unsigned int |
| --- | --- |
| Description: | The initial count of the watchdog hardware counter. The hardware counter decrements by one each time the period indicated by the Time Step attribute elapses. When the current count reaches zero, the watchdog timer expires. You can reset the current count back to the initial count by calling the NIWatchdog_Whack function. Note that modifying this attribute causes a corresponding change in the Total Timeout attribute.The value you specify for this attribute is coerced to the closest value that can be represented by the hardware counter. You can obtain the coerced value by getting this attribute immediately after setting it. |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/niwatchdogattribute_timestep.html language=enus -->
## TOPIC 00088: NIWatchdogAttribute_TimeStep

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/niwatchdogattribute_timestep.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/niwatchdogattribute_timestep.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdogAttribute_TimeStep

| Data Type: | unsigned int |
| --- | --- |
| Description: | The time step of the watchdog hardware counter specified in microseconds. The time step specifies the period of time that elapses between decrements of the current count. Note that modifying this attribute causes a corresponding change in the Total Timeout attribute.The value you specify for this attribute is coerced to the closest value that can be represented by the hardware counter. You can obtain the coerced value by getting this attribute immediately after setting it. |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/niwatchdogattribute_totaltimeout.html language=enus -->
## TOPIC 00089: NIWatchdogAttribute_TotalTimeout

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/niwatchdogattribute_totaltimeout.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/niwatchdogattribute_totaltimeout.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdogAttribute_TotalTimeout

| Data Type: | unsigned int |
| --- | --- |
| Description: | The total timeout in microseconds that must elapse before the watchdog timer expires. The total timeout is the product of the Initial Count attribute and the Time Step attribute. Note that modifying the Total Timeout attribute automatically modifies the Initial Count and Time Step attributes to obtain the closest total timeout value.The value you specify for this attribute is coerced to the closest value that can be represented by the watchdog hardware counter. You can obtain the coerced value by getting this attribute immediately after setting it. |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/niwatchdogattribute_whackinputsource.html language=enus -->
## TOPIC 00090: NIWatchdogAttribute_WhackInputSource

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/niwatchdogattribute_whackinputsource.html`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/niwatchdogattribute_whackinputsource.html
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### NIWatchdogAttribute_WhackInputSource

| Data Type: | integer |
| --- | --- |
| Description: | The input source used to whack the watchdog timer. You can only specify one source. If you specify the software source, you can whack the watchdog timer in software by calling the NIWatchdog_Whack function. If you specify a PXI trigger line as the source, you can whack the watchdog timer by momentarily applying a high signal (usually +5 volts) to that trigger line. Refer to your hardware documentation for more information. Whacking the watchdog timer with a PXI trigger line resets the count of a watchdog timer that is in a Running state and restarts a watchdog timer that is in an expired state. As long as the configured PXI trigger line receives a high signal, it continues to reset the count of the watchdog timer. If you are whacking a watchdog timer with a PXI trigger line, then the only way to start the watchdog timer from a disabled state, such as when it is first created, is to call the NIWatchdog_Whack function. Call the NIWatchdog_Whack function only when the watchdog timer is in a disabled state. If you call NIWatchdog_Whack when the watchdog timer is in the running or expired state, then NIWatchdog_Whack might report incorrect watchdog states and might not modify the watchdog timer as expected. When you have set the input source to a PXI trigger line, you cannot set the input source back to software without clearing the watchdog timer and creating it again. You can change the input source from one PXI trigger line to another PXI trigger line, but you must restart the watchdog timer from a disabled or expired state by calling the NIWatchdog_Whack function before the change will take effect. |
| Values: | NIWatchdogWhackInputSource_Software (0x00000001L)Software NIWatchdogWhackInputSource_PXITrig0 (0x00000008L)PXI Trigger Line 0 NIWatchdogWhackInputSource_PXITrig1 (0x00000010L)PXI Trigger Line 1 NIWatchdogWhackInputSource_PXITrig2 (0x00000020L)PXI Trigger Line 2 NIWatchdogWhackInputSource_PXITrig3 (0x00000040L)PXI Trigger Line 3 NIWatchdogWhackInputSource_PXITrig4 (0x00000002L)PXI Trigger Line 4 NIWatchdogWhackInputSource_PXITrig5 (0x00000004L)PXI Trigger Line 5 NIWatchdogWhackInputSource_PXITrig6 (0x00000080L)PXI Trigger Line 6 NIWatchdogWhackInputSource_PXITrig7 (0x00000100L)PXI Trigger Line 7 |
| NIWatchdogWhackInputSource_Software (0x00000001L) | Software |
| NIWatchdogWhackInputSource_PXITrig0 (0x00000008L) | PXI Trigger Line 0 |
| NIWatchdogWhackInputSource_PXITrig1 (0x00000010L) | PXI Trigger Line 1 |
| NIWatchdogWhackInputSource_PXITrig2 (0x00000020L) | PXI Trigger Line 2 |
| NIWatchdogWhackInputSource_PXITrig3 (0x00000040L) | PXI Trigger Line 3 |
| NIWatchdogWhackInputSource_PXITrig4 (0x00000002L) | PXI Trigger Line 4 |
| NIWatchdogWhackInputSource_PXITrig5 (0x00000004L) | PXI Trigger Line 5 |
| NIWatchdogWhackInputSource_PXITrig6 (0x00000080L) | PXI Trigger Line 6 |
| NIWatchdogWhackInputSource_PXITrig7 (0x00000100L) | PXI Trigger Line 7 |
| LabWindows/CVICompatibility: | LabWindows/CVI 9.0 and later |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/rtutillib.htm language=enus -->
## TOPIC 00091: Real-Time Utility Library

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/rtutillib.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/rtutillib.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Real-Time Utility Library

The Real-Time Utility Library contains functions that are useful for writing RT applications.

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/rtutilliberrors.htm language=enus -->
## TOPIC 00092: Real-Time Utility Library Error Codes

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/rtutilliberrors.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/rtutilliberrors.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Real-Time Utility Library Error Codes

If an error condition occurs during a call to any of the functions in the LabWindows/CVI Real-Time Utility Library, the **status** return value contains the error code. This code is a nonzero value that specifies the type of error that occurred. Error codes are negative numbers. The following table lists the currently defined error codes and their associated meanings.

Error codes are defined in cvi\include\rtutil.h.

| Code | Defined Constant | Error Message |
| --- | --- | --- |
| 0 | kRTNoError | No error. |
| -15200 | kRTShouldNotBeCalledOnHost | This function is supported only on real-time systems. |
| -15201 | kRTShouldNotBeCalledOnTarget | This function is not supported on real-time systems. |
| -15202 | kRTBadlyFormedIP | Badly formed IP address. |
| -15203 | kRTBadlyFormedMAC | Badly formed MAC address |
| -15204 | kRTTargetNotFound | Target not found. |
| -15205 | kRTInvalidAddressType | Invalid address type specified. |
| -15206 | kRTInvalidIPSetting | One or more IP settings were invalid. |
| -15207 | kRTInvalidSettingType | Unknown setting type. |
| -15208 | kRTInvalidSettingValue | Invalid value passed. |
| -15209 | kRTSystemNotOnLocalSubnet | The target system must be on the local subnet. |
| -15210 | kRTOperationNotSupported | Operation not supported by the remote system. |
| -15211 | kRTTimeout | Operation timed out. |
| -15212 | kRTRemoteSystemResponseError | The remote system did not respond or gave an unexpected response. |
| -15213 | kRTRemoteOperationFailure | An operation on the remote system failed. |
| -15214 | kRTSystemNotConfigured | The remote system's IP settings are not configured. |
| -15215 | kRTNotInSafeMode | The remote system must first be booted into safe mode. This may require using a safe-mode boot disk, changing a BIOS setting, or setting a DIP switch on the controller. |
| -15216 | kRTSafeModeBootFailure | The remote system failed to boot into safe mode. |
| -15217 | kRTRebootError | The remote system failed to reboot. |
| -15218 | kRTSystemLocked | System is locked. |
| -15219 | kRTIncorrectPassword | Incorrect password. |
| -15220 | kRTUnsupportedOption | A specified option is unrecognized or not supported by the function. |
| -15221 | kRTGetFilesFailure | One or more files could not be copied from the target. The image is incomplete. |
| -15222 | kRTPutFilesFailure | One or more files could not be copied to the target. The target may not boot properly or may be otherwise corrupted. |
| -15223 | kRTInvalidImage | The specified path does not contain a valid image. |
| -15224 | kRTIncompatibleImage | The specified image is incompatible with the target. |
| -15225 | kRTSystemImageMismatch | This image was not originally created from the specified target. |
| -15226 | kRTNullPointer | Null pointer was passed. |
| -15227 | kRTFailedToLoadDLL | A required DLL failed to load. |
| -15228 | kRTIncompatibleDLLVersion | A required DLL is of an incompatible version. |
| -15229 | kTraceNotSupported | Execution tracing is not supported on this platform. |
| -15230 | kTraceNotInProgress | You can call this function only during execution tracing. |
| -15231 | kTraceInProgress | An execution trace is in progress. |
| -15232 | kTraceFileWriteError | The execution trace could not be written to the file. |
| -15233 | kTraceFileReadError | The execution trace could not be read from the file. |
| -15234 | kTraceFileSendError | The execution trace could not be sent to the Real-Time Trace Viewer. Ensure that the Real-Time Trace Viewer is running on the host computer and that the host computer is connected to the network. |
| -15235 | kTraceInvalidEventID | The event ID is invalid. |
| -15236 | kRTOutOfMemory | Out of memory. |
| -15237 | kRTNetworkError | General network error. |
| -15238 | kRTInternalError | Internal error. |
| -15239 | kRTGeneralError | Unclassified error. |
| -15240 | kRTUnknownError | Unknown error. |
| -15241 | kInvalidProcessorPoolId | Invalid processor pool ID. |
| -15242 | kSystemPoolMustIncludeFirstProcessor | The system pool must include the first processor. |
| -15243 | kMaskContainsNoValidProcessors | The processor mask contains no valid processors. |
| -15244 | kMaskContainsInvalidProcessors | The processor mask contains invalid processors. |
| -15245 | kProcessorIndexSpecifiesInvalidProcessor | The processor index specifies an invalid processor. |
| -15246 | kOperationNotSupportedOnSingleProcessorSystems | Operation not supported on single processor systems. |
| -15247 | kWDFailedToLoadNIWatchdogLibrary | The watchdog library could not be loaded. Ensure that NI Watchdog support is installed on the target computer. |
| -15248 | kWDInvalidParameter | Invalid parameter. |
| -15249 | kWDInvalidAttribute | Invalid attribute. |
| -15250 | kWDInvalidWatchdogHandle | Invalid watchdog handle. |
| -15251 | kWDMultipleWhackInputSourcesNotSupported | Multiple whack input sources are not supported. |
| -15252 | kWDUnexpectedError | Unexpected watchdog error. |
| -15253 | kWDNumberTooBig | Unable to return a value because it would exceed the width of the return data type. |
| -15254 | kWDWatchdogIsLocked | This watchdog timer has been locked. No further changes can be made to the watchdog hardware until the system restarts. |
| -15255 | kWDCannotConnectToKernel | The kernel portion of the watchdog driver is not present or failed to load correctly. Watchdog hardware cannot be used. |
| -15256 | kWDUnsupportedProtocol | This watchdog timer cannot drive the specified trigger line in the requested manner. Not all watchdog hardware can drive trigger lines in all possible ways. |
| -15257 | kWDHardwareInUse | The watchdog hardware you requested is already in use or has been locked. |
| -15258 | kWDUnsupportedTriggerLine | This watchdog timer cannot drive the specified trigger line. Not all watchdog hardware can drive all trigger lines. |
| -15259 | kWDOutOfMemory | A memory allocation by the watchdog driver failed. Check available memory and disk space. |
| -15260 | kWDTooManyActions | The specified action cannot be added to the watchdog timer. Some actions can only be added once and others can only be added a maximum number of times. |
| -15261 | kWDPALFailure | The watchdog driver has experienced an unexpected low-level error. The watchdog hardware cannot be used. |
| -15262 | kWDHardwareNotPresent | The watchdog hardware you requested is either not in the system or has not been registered with the driver. |
| -15263 | kWDUnsupportedParamAction | The specified action cannot be handled by this watchdog hardware. |
| -15264 | kWDUnsupportedAttribute | The specified attribute is not supported by this watchdog hardware. |
| -15265 | kWDFeatureNotSupported | The specified method or attribute is not supported by this watchdog hardware. |
| -15266 | kRTFileNotFound | File not found. |
| -15267 | kRTInvalidModuleId | Invalid module ID. |
| -15268 | kRTSymbolNotFound | Symbol not found. |
| -15269 | kRTFailedToLoadModule | Failed to load module. Verify that all dependencies of this module are present on the system. |
| -15270 | kRTSystemError | System error. |
| -15271 | kRTInvalidParameter | Invalid parameter. |
| -15272 | kRTUnsupportedLedId | The specified LED ID is not supported on this system. |
| -15273 | kRTUnsupportedLedIdOrState | The specified LED ID or LED state is not supported on this system. |
| -15274 | kRTUnsupportedSwitchId | The specified switch ID is not supported on this system. |

<!--NI_TOPIC bundle=labwindows-cvi-real-time-module path=rtutillib/rtutillibtree.htm language=enus -->
## TOPIC 00093: Real-Time Utility Library Function Tree

- bundle_id: `labwindows-cvi-real-time-module`
- source_path: `rtutillib/rtutillibtree.htm`
- source_url: https://docs-be.ni.com/bundle/labwindows-cvi-real-time-module/raw/resource/enus/rtutillib/rtutillibtree.htm
- document_id: `labwindows-cvi-real-time-module`
- page_type: `leaf`
- content_type: ``

### Real-Time Utility Library Function Tree

| Class/Panel Name | Function Name |
| --- | --- |
| System Query |  |
| Get System Information | GetRTSystemInfo |
| Find All Systems On Subnet | FindAllRTSystemsOnSubnet |
| System Select Popup | RTSystemSelectPopup |
| Is the System Shutting Down? | RTIsShuttingDown |
| System Configuration |  |
| Set IP Configuration | SetRTIPConfiguration |
| Set System Setting | SetRTSystemSetting |
| Reboot System | RebootRTSystem |
| Lock System | LockRTSystem |
| Unlock System | UnlockRTSystem |
| Format System | FormatRTSystem |
| System Replication |  |
| Create System Image | CreateRTSystemImage |
| Apply System Image | ApplyRTSystemImage |
| Microsecond Wait Functions |  |
| Sleep | SleepUS |
| Sleep Until | SleepUntilUS |
| Sleep Until Next Multiple | SleepUntilNextMultipleUS |
| Get Current Time | GetTimeUS |
| Real-Time Trace Viewer |  |
| Configure Trace | TraceConfigure |
| Start Trace | TraceStart |
| Stop And Send Trace | TraceStopAndSend |
| Stop And Save Trace | TraceStopAndSave |
| Load And Send Trace | TraceLoadAndSend |
| Record A User Event | TraceUserEvent |
| Set Thread Name | TraceSetThreadName |
| Symmetric Multi-Processing |  |
| Set Processor Affinity For Thread | SetProcessorAffinityForThread |
| Configure Processor Pool | ConfigureProcessorPool |
| Watchdog Timer |  |
| Configure | NIWatchdog_Configure |
| Whack | NIWatchdog_Whack |
| Clear | NIWatchdog_Clear |
| Get Attribute | NIWatchdog_GetAttribute |
| Set Attribute | NIWatchdog_SetAttribute |
| Clear Outputs | NIWatchdog_ClearOutputs |
| Disable | NIWatchdog_Disable |
| LEDs and Switches |  |
| Get LED State | GetLedState |
| Set LED State | SetLedState |
| Get Switch State | GetSwitchState |
| External Modules |  |
| Load RT Module | LoadRTModule |
| Unload RT Module | UnloadRTModule |
| Get RT Module Address | GetRTModuleAddr |
| Free RTUtil Memory | FreeRTUtilMemory |
| Dispose RT System Info | DisposeRTSystemInfo |
| Get RTUtil Error String | GetRTUtilErrorString |
