# NOMAGIC DOCUMENTATION SPACE: FAQ

<!--NOMAGIC_SPACE key=FAQ chunk=2 -->

<!--NOMAGIC_PAGE id=64973922 space=FAQ version=5 -->
## PAGE 00059: FAQ archive

- page_id: `64973922`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/64973922/FAQ+archive
- version_number: 5
- version_date: `2022-02-24T14:40:40.997+01:00`
- ancestors: Frequently Asked Questions
- labels: []

### NORMALIZED CONTENT

#### EXPAND: Performance

Performance

##### [Major Issues](https://docs.nomagic.com/support/faq/major-issues)

After updating to the latest Java version (1.6.0_39 and higher or 1.7.0_13 and higher), MagicDraw can neither open projects nor accept license files. An Exception is generated. What is the fix for this issue?

Java versions 1.6.0_39 and higher or 1.7.0_13 and higher are incompatible with MagicDraw v17.0.2 (prior SP3) and v17.0.3 (prior SP1) and older versions.

**What is the Reason That Has Caused Java 6 Update 39 and higher or Java 7 Update 13 and higher Incompatibility With Our Products?**

It was Oracle’s mistake in introducing the undocumented behavior changes that have caused the incompatibility between Java and our product. As a result, MagicDraw 17.0.2 &17.0.3 and older versions are not compatible with Java 6 update u39 and higher or Java 7 update u13 and higher. 
 Oracle Java 6 update u39 and higher or Java 7 update u13 and higher have undocumented changes in the way the threading works. 
 
 
 **Solution**

Please **[manually](https://docs.nomagic.com/support/installation-and-use.html#applying_patch)*** update to:

- Service pack 3 for MagicDraw 17.0.2 which solves this incompatibility issue was released on 25th February 2013.
- Service pack 1 for MagicDraw 17.0.3 which solves this incompatibility issue was released on 4th March 2013.

For older MagicDraw versions we highly recommend using the officially recommended Java version:

- 1.6.0_31 for MagicDraw v17.0.2 (prior SP3).
- 1.7.0_07 (1.6.0_35 for Mac OS X Lion and Mountain Lion) for MagicDraw v17.0.3 (prior SP1).

In order to change Java version which MagicDraw uses, please follow the**[instructions in this file](https://docs.nomagic.com/files/Java%20downgrade%20tutorial.pdf)**.

* - autoupdate feature fails to install these service packs because of Java incompatibility. You should follow the instructions for [manual update](https://docs.nomagic.com/support/installation-and-use.html#applying_patch).

Permalink

A stereotype applied on attribute, operation, parameter, or other kind of property disappears from the model after the project update from Teamwork Server 17.0.4, if a property has been edited. How can this be handled?

To handle the problem, please use the following workaround:

1. Open the mduml.properties * file that can be found in <MagicDraw installation folder>\bin.
2. Next to JAVA_ARGS, add the following line: -Ddisable.element.version.service=true. Example: JAVA_ARGS=-Xmx2396M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -DLOCALCONFIG\=true -splash\:data/splash.gif -Xss1024K -Ddisable.element.version.service=true
3. Restart MagicDraw.

The issue will be fixed in v17.0.4 SP1.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

The file list dialog on Mac OS X doesn't respond appropriately when selecting folders

Fix for this problem is described at [https://bugs.openjdk.java.net/browse/JDK-8006420](https://bugs.openjdk.java.net/browse/JDK-8006420)

To solve the problem:

1. Open the magicdraw.properties file, which is located in < MagicDraw* installation directory>/bin .
2. From the JAVA_ARGS = line, remove the - splash\:data/splash.gif parameter

After this fix, on MagicDraw* startup, the spash screen will not be displayed for a few second, but the open file list dialog refresh problem will be solved.

The fix is sheduled into the nearest release.

* - This is valid for all MagicDraw-based Cameo Suite products.

Permalink

MagicDraw 17.0.5 stops responding on Mac OS X Mavericks, and I keep seeing the spinning wait pointer (aka Spinning Beach Ball of Death). How can I fix the issue?

MagicDraw stops responding due to an issue detected in Java SE 7 Update 40, which is bundled with MagicDraw 17.0.5 (for the issue details, go to [https://bugs.openjdk.java.net/browse/JDK-8025588](https://bugs.openjdk.java.net/browse/JDK-8025588)[).](https://bugs.openjdk.java.net/browse/JDK-8025588)

This issue will be fixed in **MagicDraw 17.0.5 SP1**, coming out in the middle of February.

To solve the issue manually (without the SP), switch the version of the bundled Java to SE 7 Update 25*, which does not cause the issue. For this, do the following:

1. Open the magicdraw.properties file, stored in <MagicDraw installation directory>/bin.
2. Find the JAVA_HOME property and add the path to the location of Java SE 7 Update 25 on your PC. For example, “JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home”.

Please contact our customer support, if this does not help.

-- 
 * If you do not have Java SE 7 Update 25 installed on your PC, download the installer from the [Java SE 7 Downloads](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html#jdk-7u25-oth-JPR) page. You need the*jdk-7u25-macosx-x64.dmg*file.

Permalink

On Windows, MagicDraw doesn't support HiDPI screen resolutions. How to solve this problem?

To get the best effect of MagicDraw, lower your screen resolution to HD 1920 x 1080. 
 The simplest way to change resolution settings is to right-click anywhere on your desktop and select **Screen resolution**. Then use the slider to select the required setting. 
 We are working to find ways to support HiDPI.

Permalink

How do I adjust the scaling factor when using MagicDraw 18.2 on a HiDPI screen?

You can turn off scaling by including a certain parameter to the *magicdraw.properties* file.

1. Open <MagicDraw installation directory>\bin.
2. Find and open magicdraw.properties.
3. Find line JAVA_ARGS= and add *-Dmagicdraw.resolution.scale=1* to it.

Permalink

Why the Model Browser of my project doesn’t show newly created elements, and corrupted elements appear in it with no reason?

This happens because of the Model Browser refresh problem with MagicDraw 18.0. 
 To solve this problem, do one of the following:

- Refresh the project (press F5 ).
- Save the project (press Ctrl+S ).
- Change the Model Browser settings. For example, turn on the Show Auxiliary Resources option.

Permalink

MagicDraw is unstable and slow when running on Java SE 8 Update 60. How do I solve this?

This is a [known](http://bugs.java.com/view_bug.do?bug_id=8061636) Java bug. This issue will be fixed in MagicDraw 18.3, but in the meantime you can upgrade to the [recommended Java version](https://docs.nomagic.com/support/jvm-list.html). 
 
 After installation, open *<MagicDraw installation directory>\\bin*, and modify the *magicdraw.properties** file. 
 
 Change line *JAVA_HOME=* to correspond with the Java version you\'ve installed. 
 
 * If you are using MagicDraw 17.0.4 or earlier, the properties file is called *mduml.properties*.

Permalink

MagicDraw is unstable and slow when running on Java SE 8 Update 101/102. How do I solve this?

This is a known Java bug. This issue is fixed in MagicDraw 18.4. If you are using MagicDraw 18.3 and earlier versions, you can use [the recommended Java version](https://docs.nomagic.com/component/content/article/jvm-list?Itemid=153)that comes with installation.

Once you have installed the recommended Java version, do the following:

1. Open the bin folder <MD install directory>\bin .
2. Open the file magicdraw.properties .
3. Look for the line "JAVA_HOME=" and change the Java version with the one you have installed.

Permalink

MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?

Solution is to run *magicdraw.sh* file from the */bin* directory.

This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.

Please update your modeling tool to the **version 18.4 SP1** to avoid the installation incompatibility.

Permalink

##### [Performance](https://docs.nomagic.com/support/faq/performance)

MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?

This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select **Options** > **Look and Feel** > **Metal**.

Permalink

Sometimes when running the program the StackOverflowError occurs.

If you are running the Sun's JVM, set the following java properties in your mduml.properties* file: to the line JAVA_ARGS=-Xmx600M, append the string -Xss[stack size]

For example:

JAVA_ARGS=-Xmx600M -Xss2M

This sets java stack size to 2 megabytes.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Sometimes when running the program the OutOfMemory error occurs.

If you are running the Sun's JVM, set the following java properties in your mduml.properties* file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.

For example:

JAVA_ARGS=-Xmx800M

This sets java heap size to 800 megabytes.

If you get exception "java.lang.OutOfMemoryError: PermGen space" please, check if PermSize is specified in mduml.properties* file.

The JAVA_ARGS line should look like:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M

If PermSize is specified in mduml.properties* file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.

For example:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.

We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.

Permalink

Using a nvidia 8240 agp adapter in dual monitor mode any part of the display past the first 1/3 of the second monitor does not display correctly. Using ASUS nvidia 8240 delux latest driver. Also tried the nvidia latest driver with the same result.

Try to start MagicDraw without direct draw, and edit JAVA_ARGS the line in the MagicDrawUML/bin/mduml.properties* file by adding -Dsun.java2d.noddraw=true.

The line should look like: JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M -Dsun.java2d.noddraw=true.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

MagicDraw is unstable and slow when running on Java SE 8 Update 60. How do I solve this?

This is a [known](http://bugs.java.com/view_bug.do?bug_id=8061636) Java bug. This issue will be fixed in MagicDraw 18.3, but in the meantime you can upgrade to the [recommended Java version](https://docs.nomagic.com/support/jvm-list.html). 
 
 After installation, open *<MagicDraw installation directory>\\bin*, and modify the *magicdraw.properties** file. 
 
 Change line *JAVA_HOME=* to correspond with the Java version you\'ve installed. 
 
 * If you are using MagicDraw 17.0.4 or earlier, the properties file is called *mduml.properties*.

Permalink

MagicDraw is unstable and slow when running on Java SE 8 Update 101/102. How do I solve this?

This is a known Java bug. This issue is fixed in MagicDraw 18.4. If you are using MagicDraw 18.3 and earlier versions, you can use [the recommended Java version](https://docs.nomagic.com/component/content/article/jvm-list?Itemid=153)that comes with installation.

Once you have installed the recommended Java version, do the following:

1. Open the bin folder <MD install directory>\bin .
2. Open the file magicdraw.properties .
3. Look for the line "JAVA_HOME=" and change the Java version with the one you have installed.

Permalink

MagicDraw freezes. Do you know how to fix that?

In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, "MD log file" tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).

Permalink

From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?

While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.

In order to analyze and fix the issue, more information is required. Please provide us with the following information:

1. Can you reproduce the problem? If yes, what are the steps to reproduce it?
2. If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.
3. Send us the memory dump file. It may help to detect the problem.

To create a memory dump file, please do the following:

1. In the properties * file, append JAVA_ARGS parameters as follows: -XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots
2. Start your modeling tool.

The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.

*

- For MagicDraw, the properties file is magcdraw.properties ( mduml.properties for MagicDraw version 17.0.4 or earlier).
- For Cameo Enterprise Architecture, the properties files is cameoea.properties .
- For Cameo Systems Modeleer, the properties files is csm.properties .
- For Cameo Business Modeler, the properties file is csm.properties .

Permalink

What are the common recommendations to increase performance?

When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase an efficiency of modeling, we suggest the following solutions:

- Increase a java heap size.
- Do not keep unused diagrams open. Open project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.
- Increase an active validation period. MagicDraw takes less memory with increased active validations period.
- Split the project to read only modules. Keep read only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.
- Use Garbage Collector to free unused memory.
- Turn of antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.

For more information see "MagicDraw User Manual" > "Performance Improvement" section. Manual is available in < MagicDraw installation directory > \manual\

Permalink

I suspect a performance problem. How do I solve it?

To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:

**Generating a log file when the modeling tool freezes or performs slowly:**

1. When a modeling tool runs slowly or freezes, open*<modeling tool installation directory>\bin,* and run *submit_issue.exe* several times. It dumps threads into the log file.

2. Click **Help** > **About** on the main menu of your modeling tool. In the open dialog, select the **Environment** tab and click the **Log File** link. The log file opens.[*](#path)

3. Save the file and register an issue. Click **Help** >**Report an Issue** on the main menu of your modeling tool or go to [http://www.nomagic.com/support.html](http://www.nomagic.com/support.html)[.](https://docs.nomagic.com/support.html)

*If a modeling tool is inactive, as of version 17.0.4, log file is stored in the following location:

- Windows Vista/7/8 C:\Users\<USERNAME>\AppData\Local\.magicdraw\<md.version.number>
- Windows 2000/XP C:\Documents and Settings\<USERNAME>\Local Settings\Application Data\.magicdraw\<md.version.number>
- Windows NT4 C:\WINNT\Profiles\<USERNAME>\Local Settings\Application Data\.magicdraw\<md.version.number>
- Other OS: <user.home>/.magicdraw/<md.version.number>

**By using Java VisualVM:**

The modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.

The following steps outline how to obtain the data from VisualVM:

**Note.**Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.

**On Windows OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Task Manager .
3. Start Java VisualVM . If you selected the default location on the JDK installation process, VisualVM is located in C:\Program Files\Java\jdk<version number>\bin\ jvisualvm.exe . Otherwise, start the exe from your customized location.
4. Start the modeling tool.
5. In Task Manager , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Task Manager ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details, including the email address where the ticket link will be sent, and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team. For more information about reporting an issue, please visit http://www.nomagic.com/support.html .

**On Mac OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Activity Monitor .
3. Start Java VisualVM . If you selected the default location on the JDk installation process, VisualVM is located in /Library/Java/JavaVirtualMachines/jdk<version number>.jdk /Contents/Home/bin/jvisualvm . Otherwise, start **jvisualvm** from your customized location.
4. Start the modeling tool.
5. In Activity Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Activity Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished and click the Stop button.
10. In the CPU samples tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the *.nps file.
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details including the email address where the ticket link will be sent and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team. For more information about reporting an issue, please visit http://www.nomagic.com/support.html .

**On Linux OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start System Monitor .
3. To start Java VisualVM , execute the jvisualvm tool from the bin directory of the JDK. When the tool runs, the Java VisualVM window opens.
4. Start the modeling tool.
5. In System Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in System Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details including the email address where the ticket link will be sent and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team. For more information about reporting an issue, please visit http://www.nomagic.com/support.html .

Permalink

After loading a project, there wasn’t a big memory usage but after some actions it increased dramatically. How could I manage it?

In order to troubleshoot this issue, we will need the program’s log files (located in the install directory of your tool). Additional information might be required about the Java environment on which our modeling tools are based. The information we need is called the “heapdump” and can be obtained using the Java VisualVM program.

Please read and follow this procedure to install Java VisualVM and send this data to us (while the tool is running):

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ , if you do not have it.
2. Start Task Manager or other appropriate tool depending on your OS.
3. Start Java VisualVM. If you have selected the default location on the JDK installation process, VisualVm is located in C:\Program Files\Java\jdk<version number>\bin\ jvisualvm.exe. Otherwise start the jvisualvm.exe from your custom location.
4. In the Task Manager or other program according to you OS, find the PID (Process Identifier) of your modeling tool.
5. In the Java VisualVM, find Java process by the modeling tool PID and double click to open it.
6. Right click the Java process and, from the shortcut menu, select Heap Dump . The heapdump file creates under your process.
7. Save the heapdump file. Right click the heapdump and, on the shortcut menu, click Save As .
8. Register an issue and sent the saved *.hprof file for the investigation. For this, on the main menu of your modeling tool, click Help > Report an Issue or go to http://www.nomagic.com/support.html .

Permalink

Where can I find log files of a modeling tool, Cameo Collaborator and Teamwork Cloud?

When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.

**Accessing log files**

- For a modeling tool

Open your modeling tool and in the main menu go to **Help** > **About <modeling tool name>**. In the **Environment** tab, click the link provided in the **Log File** line to open a log file.

- For Cameo Collaborator

Go to Alfresco Community installation directory, and obtain the *alfresco.log*, *share.log* and *solr.log* files.

Go to *<Alfresco Community installation directory>\tomcat\logs*, and obtain the *alfrescotomcat-stderr.log*, *alfrescotomcat-stdout.log* and *catalina.log* files.

- For Teamwork Cloud

Go to *<user home directory>\.twcloud\<server version>*, and obtain the *server.log* and *client.log* files.

Go to *<Cassandra installation directory>\logs* on Windows OS or */var/lib/Cassandra* on Linux, and obtain the Cassandra log file.

**Generating a log file**

If the performance of your modeling tool declines or it freezes, go to *<modeling tool installation directory>\bin*, and run the *submit_issue.exe* file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file, as described above.

**Java crash log files**

If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the *<modeling tool installation directory>/bin* or *<modeling tool installation directory>* directory. The names of these log files start with "hs_err", e.g., *hs_err_pid15693.log*. If you find the Java crash log file, the reason your modeling tool crashed was that Java crashed.

Permalink

##### [Installation and Running](https://docs.nomagic.com/support/faq/installation-and-running)

How to install MagicDraw in a silent mode, i.e., without the installer GUI?

Please start the installer with the following parameters: 
 -i silent -DUSER_INSTALL_DIR=

The example:

MD_UML_169_win.exe -i silent "-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9" 
 MagicDraw will be installed silently, with a default configuration.

Permalink

What is the best way to reinstall MagicDraw on new computer or the same one after formatting.

Reinstall product on new computer:

1. Deactivate the current license .
2. Download and install the fresh installation on new machine.
3. Start it after the installation is finished.
4. The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.
5. Uninstall the product from old machine.
6. You will be requested to activate the license and receive the commercial license dedicated for the particular machine.

Permalink

MagicDraw does not start on Mac OS after QuickTime 7.2 update

This is a known issue in Intel based Mac OS with QuickTime 7.2 update that causes most of the Power PC applications to refuse to start. This problem hounts some Java apps too, and sometimes MagicDraw refuses to start from the icon created by the installer. Although it is possible to start MagicDraw from command line (look for classpath and JVM flags from Indo.plit file).

There is available one solution that fixes the Power PC apps and also the MagicDraw from here: [http://mactip.blogspot.com/2007/07/dependent-dylib-is-not-prebound.html](http://mactip.blogspot.com/2007/07/dependent-dylib-is-not-prebound.html)

The fix involves some command-line and text editor usage, but it's relatively simple and it works.

Permalink

I installed MagicDraw and it ran. Worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?

This problem is Install Anywhere related and appears when you uninstall previous version of MagicDraw and then, without restarting your computer, install another MagicDraw in the same directory. We would suggest to uninstall MagicDraw, restart your computer, and then install MagicDraw again.

Permalink

On the Macintosh, MagicDraw points out error at startup: java.lang.NullPointerException

On the Macintosh, MagicDraw points out error at startup:

**java.lang.NullPointerException** 
 **at sun.java2d.SunGraphicsEnvironment.getAvailableFontFamilyNames(SunGraphic sEnvironment.java:327)** 
 **at sun.java2d.SunGraphicsEnvironment.getAvailableFontFamilyNames(SunGraphic sEnvironment.java:359)** 
 **at com.nomagic.actions.SetFontFaceAction.(SetFontFaceAction.java)** 
 **at com.nomagic.actions.SetFontAction.(SetFontAction.java)**

...

Based on messages from the Apple java-dev mailing archive, a lot of people who use Java 1.4.1 on Mac have experienced similar problems. Someone suggested this had to do with bitmap fonts in a Classic install in "/System Folder/Fonts". And it seems that renaming "/System Folder/Fonts/" to "/System Folder/Fonts.not/" or something else and rebooting your machine can solve the problem.

Permalink

In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?

You can save configuration files in the modeling tool installation directory or on your chosen directory.

To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties* (this file is in*\bin*): 
 JAVA_ARGS=-Dlocalconfig=false

**NOTE**: For Windows users. If you are using MagicDraw 17.0.4 or later, you must also add argument 
 -DWINCONFIG\=false.

To store configuration files to your chosen location

1. In the /. <modeling tool name> / folder, create file named <modeling tool properties file name> redirect , that is magicdrawredirect , cameoearedirect , csmredirect , or cbmredirect .
2. In the created file, type absolute (for example, C:\users\john\Documents ) or relative (relative to modeling tool installation directory, for example, ..\configurations ) path where configuration and auxiliary files will be saved.

Or:

1. Open the *.properties * file, which is located in \bin .
2. Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location= <absolute path to a custom location>

For example, *-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData*

**NOTE:** If there is defined to store files in installation directory (see the section "To store MagicDraw configuration files in MagicDraw installation directory" above), files will not be stored to your chosen location. 
 
 
 * For more information about configuration files please, see [Configuration files](https://docs.nomagic.com/display/MD185/Configuration+files)

Permalink

After the download the installer cannot be launched or it just appears on the screen and vanishes

Please check if the file is not truncated. You can see the exact file size at the download page.

Permalink

I ran into a trouble when installing MagicDraw: Launching installer... Exception in thread "main" java.lang.NoClassDefFoundError: com/zerog/lax/LAX

In most cases such error appears when installer file is truncated or corrupted.

Please try to download an installer again.

Another option is that /usr/bin/java is an old version java. To check which java is used by installer, set environment variable LAX_DEBUG and launch installation again.

By default installer first uses java found in /usr/bin. But there is possibility to use specific VM when launching the installer. Please add parameter LAX_VM to launcher and second parameter path to java executable, here is an example (assuming that java is in /opt/j2sdk1.5.0_03):

./MD_UML_105_unix.sh LAX_VM /opt/j2sdk1.5.0_03/bin/java

Permalink

How to run MagicDraw under Unix after installation?

Run mduml* file, which is located in MagicDraw installation directory, bin folder.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Update of JAVA 1.6.0.13 for Mac OS causes the disappearing menu.

We have found that update of JAVA 1.6.0.13 for Mac OS triggers the problem with disappearing MagicDraw menu. This issue is fixed in 16.5 SP3. Also we suggest two workarounds:

1. You need to define older JAVA version in mduml.properties * ( /bin/ ) file and work with that JAVA version (for example version 1.5.0 or previous 1.6.0).
2. You need to change Look & Feel style by editing global.opt file. Note: This problem does not exist on Metal Look & Feel.

Steps how to do that:

- Shutdown MagicDraw application;
- Go to ./magicdraw/ /data/;
- Open global.opt file with text editor;
- Find LOOK_AND_FEEL_CLASS propertyID.
- Replace tag apple.laf.AquaLookAndFeel with new one: javax.swing.plaf.metal.MetalLookAndFeel
- Save file;
- Start MagicDraw application.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

When I saving project after I have upgraded Magicdraw to v16.6 I get a save error.

Save error appears saving project with modules when MagicDraw v16.6 is installed on top of MagicDraw v15.0 or earlier (using autoupdate functionality). This problem occurs because one or more old resource descriptors from MagicDraw v15.0 or earlier are corrupted.

To prevent MagicDraw project save error you need to install MagicDraw v16.6 to a new location – to a new and empty folder, for example, "MagicDraw 16.6". Note that on the first MagicDraw startut you can import MagicDraw environment options from previous MagicDraw installations.

You may download MagicDraw 16.6 from your personal or company profile on www.nomagic.com, also to obtain unlock keys.

Permalink

Is it possible to create a MagicDraw installation package with a set of some default options?

First of all you need to pre-configure MagicDraw. Do the following:

1. Check if you have the permission to write to the MagicDraw installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.
2. In magicdraw.properties , which is in \bin , set the parameter value: JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false
3. Run MagicDraw and set desired options, then close the program.
4. Reopen magicdraw.properties and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.
5. Copy the MagicDraw installation folder and paste it on a new machine.

Let us explain the difference between changed parameter values:

a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in*\.magicdraw\* . Options are loaded in the following order:

1. From <Common Application Data location>\.magicdraw\
2. From the MagicDraw installation folder

b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the MagicDraw installation folder and are loaded from there.

Permalink

I have installed and activated MagicDraw v16.9 as the administrator. When I had logged into my regular account, MagicDraw asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?

The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.

The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.

You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).

For the instructions on how to change the configuration files directory, please find the issue "In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?"

Note: It is important to know that the MagicDraw seat license can be used by a single user only.

Permalink

After installing MagicDraw on the Mac OS with Java (1.6.0_17), default Look & Feel does not function and the Mac menu bar is gone.

In order to fix the problem with the menu bar after java update on the Mac OS, you need to open /.magicdraw/16.6/data/global.opt and change the string "com.apple.laf.AquaLookAndFeel" to "apple.laf.AquaLookAndFeel".

Permalink

After updating MagicDraw to version 17.0.1 exceptions can be shown on different actions.

After updating MagicDraw to version 17.0.1 exceptions can be shown on different actions. The exception stack trace may look like :

**java.lang.RuntimeException: java.lang.reflect.InvocationTargetException** 
 **at com.nomagic.utils.Utilities.invokeAndWaitOnDispatcher(Utilities.java:1578)** 
 **at com.nomagic.magicdraw.core.project.ProjectsManager.setActiveProject(ProjectsMana ger.java:315)** 
 **...**

OR

**java.lang.AbstractMethodError** 
 **at com.nomagic.magicdraw.core.project.ProjectsManager.fireProjectPreActivated(Proje ctsManager.java:1352)** 
 **at com.nomagic.magicdraw.core.project.ProjectsManager$2.run(ProjectsManager.java:26 9)** 
 **at com.nomagic.utils.Utilities.invokeAndWaitOnDispatcher(Utilities.java:1562)** 
 **...**

You are using incompatible plugin e.g. Cameo Simulation Toolkit 1.1, Cameo Data Modeler 16.8, EstimIX, ExtendIX, or other. Those plugin versions are not compatible with MagicDraw 17.0.1.

Please update or remove incompatible plugins from Help > Resource/Plugin Manager > Click the button "Check For Updates" > and download compatible version OR remove incompatible plugin from the MagicDraw.

[Plugins compatibility can be checked here](https://docs.nomagic.com/support/compatibility).

Permalink

There is no Implementation toolbar on the Implementation diagram pallet in MagicDraw 17.0 SP1

To see the pallet, you need to upgrade your MagicDraw to a new version of 17.0 SP1.

To upgrade MagicDraw to the new version of 17.0 SP1:

1. On the main menu, click Help > Check For Updates .
2. Click Apply Patch .
3. Restart MagicDraw.

Permalink

When Resource/Plugin Manager is started error is shown.

When Resource/Plugin Manager is started error is shown:

**java.lang.NullPointerException** 
 **at com.nomagic.magicdraw.resourcemanager.sb.b(sb.java:247)** 
 **at com.nomagic.magicdraw.resourcemanager.sb.j(sb.java:223)** 
 **at com.nomagic.magicdraw.resourcemanager.sb.e(sb.java:84)**

**MagicDraw up to version 17.0.1 SP1 with Java version 1.7 is used.**

This issue is 1.7 Java specific.

We highly recommend to use the bundled Java, which comes with MagicDraw installation (select to use the bundle Java in third MagicDraw installer step).

Java can be changed in mduml.properties* file in "JAVA_HOME=" line. mduml.properties* can be found in "MagicDraw install dir" / bin folder.

This issue is already fixed in v17.0.1 SP1 
 
 
 * If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

After upgrading Java to 1.6.0_26, MagicDraw becomes unpredictable.

The following issues appear:

- MagicDraw hangs on a splash screen.
- Any model or diagram cannot be opened.
- Any diagram or element cannot be created.
- In the md.log file, the exception "net.sf.ehcache.CacheException" appears.

**What should I do?**

To start MagicDraw normally, perform the following steps:

- Update MagicDraw into 17.0 SP3 or
- Delete all cache folders from user home directory > /.magicdraw/ version > / and restart MagicDraw.

Note: Upgrading the Mac OS X to 10.6.5, upgrades Java to version 1.6.0_26 automatically.

Permalink

How to update MagicDraw to new version?

You may find all the information about updating to new version at [Updating modeling tools and plugins](https://docs.nomagic.com/display/NMDOC/Updating+modeling+tools+and+plugins).

Permalink

When I run the exe file I get a warning: Please select another location to extract the installer to:

This error occurs when you have a corrupted installer file. Please download the file and install again.

Permalink

When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to MagicDraw installation directory or "failed to copy resource directory". How can this be handled?

We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.

To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following: 
 1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**. 
 2. From the **System Configuration** dialog, click the **Tools** tab. 
 3. Select the **Change UAC Settings** tool and click **Launch** button. 
 4. Move the slider to the highest value to set **Always notify** and click **OK**. 
 5. Restart the computer to apply changes.

To enable UAC on Windows Vista OS, do the following: 
 1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**. 
 2. From the**System Configuration**dialog, click the **Tools** tab. 
 3. Select the **Enable UAC** tool and click **Launch** button. The **CMD** window opens. 
 4. When the command is completed, you can close **CMD** window. 
 5. Restart the computer to apply changes.

To run MagicDraw as administrator, right-click the MagicDraw icon and choose **Run as Administrator**.

To run MagicDraw as an administrator all the time, do the following: 
 1. Right-click the MagicDraw icon and choose **Properties**. 
 2. Click the **Compatibility** tab. 
 3. In the **Privilege Level** area, select **Run this program as an administrator**. 
 4. Click **OK**.

Permalink

When trying to launch MagicDraw on OS X Mountain Lion, the error appears: "MagicDraw.app" is damaged and can't be opened. You should move it to the Trash."

Please note that downloaded installs are not corrupted or damaged and this problem is not related to the MagicDraw application. This issue is related to the new OS X Mountain Lion functionality, "Gatekeeper."

The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.

In order to launch MagicDraw, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: [http://support.apple.com/kb/HT5290](http://support.apple.com/kb/HT5290)

Note: We are communicating with Apple to solve this issue so that our customers may execute MagicDraw without any problems.

Permalink

I cannot start MagicDraw 17.0.4 on MAC OS X after it has been upgraded from version 17.0.3 SP1 by using the no-install package.

We offer you to solve the problem in one of the following ways.

**Solution #1:**

1. Remove MagicDraw.app from <MagicDraw 17.0.3 SP1 installation directory>.
2. Extract MagicDraw_1704_no_install_mac.zip to <MagicDraw 17.0.3 SP1 installation directory>. Select to overwrite all files, when you will be asked. A new MagicDraw.app file will appear in <MagicDraw 17.0.3 SP1 installation directory>.
3. Use the MagicDraw.app file to start the upgraded version of MagicDraw.

**Solution #2:**

1. Extract MagicDraw_1704_no_install_mac.zip to <MagicDraw 17.0.3 SP1 installation directory>. Select to overwrite all files, when you will be asked.
2. Copy the MagicDraw.app file and paste it in the same directory. The MagicDraw Copy.app file will appear in <MagicDraw 17.0.3 SP1 installation directory>.
3. Use the MagicDraw Copy.app file to start the upgraded version of MagicDraw.

Permalink

MagicDraw 17.0.4 can be started neither on Mac OS X Lion nor on Mac OS X Mountain Lion. JRELoadError appears when trying to start the application. How can this be handled?

The error appears because the MagicDraw.app file cannot find the installed Java 6.

To handle the problem, please use one of the following workarounds:

- Start MagicDraw using the mduml * file that can be found in <MagicDraw installation folder>/bin.
- Install Java 6 in your computer and use the MagicDraw.app file to start MagicDraw 17.0.4.

This issue will be fixed in MagicDraw 17.0.5.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

MagicDraw does not start after upgrading to OS X Yosemite. How can I fix this issue?

The problem is that MagicDraw earlier than 17.0.2 SP3 or 17.0.3 SP1 cannot be started on OS X Yosemite. 
 To start MagicDraw on OS X Yosemite, you must upgrade the modeling tool at least to 17.0.2 SP3 or 17.0.3 SP1. 
 
 If MagicDraw still does not start, you must upgrade Java on your computer. For recommended Java versions and links to downloads, please visit [http://www.nomagic.com/support/jvm-list.html](http://www.nomagic.com/support/jvm-list.html)[.](https://docs.nomagic.com/support/jvm-list.html)

Permalink

How do I turn on debug log mode?

To initialize **log4j**, open *<MagicDraw installation directory>/data*, and modify the *debug.properties* file.

Change the debug level for appropriate categories by specifying *log4j.category.<category>=DEBUG* or turn on debug for all categories *log4j.rootCategory=DEBUG,SO*.

Permalink

Cache error occurred. How to handle it?

Close your modeling tool, delete all cache folders and start the program again. 
 Cache folders can be found in *<user home directory>\.<modeling tool>\<version number>*, for example *<userhome>\.magicdraw\<18.2>*.

If the problem still exists, please add the **-Dcom.sun.media.imageio.disableCodecLib=true** option into the **JAVA_ARGS** line in the modeling tool properties file, for example *magicdraw.properties*. A properties file is in *<modeling tool installation directory>\bin*.

See the example:

JAVA_ARGS=-Xmx4000M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -DLOCALCONFIG\=true -splash\:data/splash.png -Dmd.class.path\=$java.class.path -Dcom.nomagic.osgi.config.dir\=configuration -Desi.system.config\=data/application.conf -Dlogback.configurationFile\=data/logback.xml -Xss1024K -Dcom.sun.media.imageio.disableCodecLib=true

Permalink

MagicDraw does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?

Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in *.zip/iso* files are not secure because of the dylib-hijacking problem. 
 (Please find more about it at [https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/](https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/)[). 
 All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.](https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/)

The solutions are:

1. To run magicdraw.sh file from the /bin directory.
2. To download the original signed MagicDraw.dmg file and to install the application again.
3. To remove the program from quarantine.

To remove the application from quarantine, please do:

1. Open a terminal.
2. Using the terminal, open the MagicDraw installation directory.
3. Write the command: xattr -d com.apple.quarantine MagicDraw.app/
4. Close the terminal and start MagicDraw using the .app file.

**NOTE:** This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.

Permalink

I have installed several versions of the modeling tool on Mac OS and the application can’t be opened using the .app file. How should I start a program?

Please restart your computer. After multiple updates or after installing different versions of a modeling tool on the same machine with Mac OS, sometimes it happens for unknown reason.

Permalink

When I run MagicDraw 18.5 on Mac OS X 10.11 El Capitan in the native full screen mode, why do most dialogs appear behind previously open dialogs?

This is a known issue with Mac OS X 10.11 El Capitan operating system. Most dialogs in the application will be displayed behind previously open dialogs, affecting usability of the user interface. There is no solution to this problem. Please try to downgrade the Mac OS to some earlier version.

Permalink

How do I start the License Server Manager on UNIX Platforms automatically?

Edit the appropriate boot script, which could be one of the following: */etc/rc.boot, /etc/rc.local, /etc/rc2.d/Sxxx,*or*/sbin/ rc2.d/Sxxxx.*

Then, include commands similar to the following:

/bin/su daniel -c 'echo starting lmgrd > \ 
 /home/flexlm/v11/hp700_u9/boot.log' 
 /bin/nohup /bin/su daniel -c 'umask 022; \ 
 /home/flexlm/v11/hp700_u9/lmgrd -c \ 
 /home/flexlm/v11/hp700_u9/license.dat >> \ 
 /home/flexlm/v11/hp700_u9/boot.log' 
 /bin/su daniel -c 'echo sleep 5 >> \ 
 /home/flexlm/v11/hp700_u9/boot.log' 
 /bin/sleep 5 
 /bin/su daniel -c 'echo lmdiag >>\ 
 /home/flexlm/v11/hp700_u9/boot.log' 
 /bin/su daniel -c '/home/flexlm/v11/hp700_u9/lmdiag -n -c\ 
 /home/flexlm/v11/hp700_u9/license.dat >> \ 
 /home/flexlm/v11/hp700_u9/boot.log' 
 /bin/su daniel -c 'echo exiting >>\ 
 /home/flexlm/v11/hp700_u9/boot.log'

Please note that this does not start the vendor daemon until you reboot the system.

Permalink

##### [Java Virtual Machine (JVM)](https://docs.nomagic.com/support/faq/java-virtual-machine-jvm)

MagicDraw 17.0.5 stops responding on Mac OS X Mavericks, and I keep seeing the spinning wait pointer (aka Spinning Beach Ball of Death). How can I fix the issue?

MagicDraw stops responding due to an issue detected in Java SE 7 Update 40, which is bundled with MagicDraw 17.0.5 (for the issue details, go to [https://bugs.openjdk.java.net/browse/JDK-8025588](https://bugs.openjdk.java.net/browse/JDK-8025588)[).](https://bugs.openjdk.java.net/browse/JDK-8025588)

This issue will be fixed in **MagicDraw 17.0.5 SP1**, coming out in the middle of February.

To solve the issue manually (without the SP), switch the version of the bundled Java to SE 7 Update 25*, which does not cause the issue. For this, do the following:

1. Open the magicdraw.properties file, stored in <MagicDraw installation directory>/bin.
2. Find the JAVA_HOME property and add the path to the location of Java SE 7 Update 25 on your PC. For example, “JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home”.

Please contact our customer support, if this does not help.

-- 
 * If you do not have Java SE 7 Update 25 installed on your PC, download the installer from the [Java SE 7 Downloads](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html#jdk-7u25-oth-JPR) page. You need the*jdk-7u25-macosx-x64.dmg*file.

Permalink

How can I start MagicDraw v16.9 and later on Mac PowerPC?

MagicDraw needs Java to be supported. Java 1.6 is available on the 64-bit Intel-based Macs only. Non-Intel-based PowerPC does not support Java 1.6 and later.

The latest MagicDraw version which can support Java 1.5 is MagicDraw v16.6.

Permalink

I want to check which JVM is used for installation under Linux.

You can watch installation process by setting environment variable LAX_DEBUG to value 1 before starting installation.

Permalink

There are problems when using JVM 1.6 with MagicDraw v14.0 and previous.

The problems are usually related with opening/creating projects. The recommendation is to use JVM 1.5 for MagicDraw v14.0 and previous.

Permalink

How do I know what version of JVM I am running?

You may find this information in the About window (Help menu -> About)

or

If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.

Permalink

How to change JVM version?

1. Go to <modeling tool installation directory>\bin and open the <modeling tool>.properties file (eg., magicdraw.properties , csm.properties , cameoea.properties ) for editing. If you are using MagicDraw 17.0.4 or earlier, the name of the property file is mduml.properties .
2. In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144

NOTE: Integrated MagicDraw runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that MagicDraw integrates with. If you are running MagicDraw integrated with IDE, read the appropriate readme.html for specific integration, found in the *integrations* folder.

Permalink

How to install Java 1.5 on Mac OS X 10.6 Snow Leopard?

In order to install Java 1.5 on Mac OS X 10.6 Snow Leopard, please follow these steps.

Execute the following commands in the terminal:

1. Get the java 5 that was included in 10.5 "leopard" and unpack:

cd /tmp/

curl -o java.1.5.0-leopard.tar.gz

[http://www.cs.washington.edu/homes/isdal/snow_leopard_workarou](http://www.cs.washington.edu/homes/isdal/snow_leopard_workarou)[nd/java.1.5.0-leopard.tar.gz.](http://www.cs.washington.edu/homes/isdal/snow_leopard_workaround/java.1.5.0-leopard.tar.gz)

tar -xvzf java.1.5.0-leopard.tar.gz

2. Move it to your System java folder (password needed):

sudo mv 1.5.0 /System/Library/Frameworks/JavaVM.framework/Versions/1.5.0-leopard

3. Tell OS X that java 5 actually is java 5:

cd /System/Library/Frameworks/JavaVM.framework/Versions/

sudo rm 1.5.0

sudo ln -s 1.5.0-leopard 1.5.0

sudo rm 1.5

sudo ln -s 1.5.0 1.5

After these commands, Java 1.5 will be installed. You can check Java 1.5 on Java Preferences dialog (open "/Applications/Utilities/Java Preferences.app")

Change the properties to use Java 1.5 32-bit on MagicDraw. Open file "mduml.properties"*, which is located in /bin and change path in line JAVA_HOME=.

The line should look like:

JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/1.5/Home

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.

You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties* file, in the line:

JAVA_ARGS=-Xmx800M

The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.

On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.

More information about OutOfMemory problems you can find in readme.html by "OutOfMemory problem" paragraph. This file is located in <MagicDraw installation directory>.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?

Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.

The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.

If you are using an **earlier version than 18.4 SP1**and cannot start the modeling tool*, please do the following:

1. Download the original signed <modeling tool*>.dmg file and install the application again.
2. In bin\ magicdraw.properties** , set JAVA_HOME to the Java version installed in the <modeling_tool*_installation_directory >\java folder.

Example: *JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre*

1. Run magicdraw.sh*** file from the /bin folder.

*MagicDraw, Cameo EA, Cameo Systems Modeler

** cameoea.properties, csm.properties

***camocea.sh, csm.sh

Permalink

##### [Save, Load, Import, Export](https://docs.nomagic.com/support/faq/save-load-import-export)

How to migrate existing projects to the new MagicDraw version?

You should copy all contents from old version projects folder to new version projects folder. If projects do not show up, copy the complete projects directory into the same location by creating all new projects and then importing the latest .xml.zip file.

Permalink

How can I copy a diagram from one MagicDraw project into another one?

Use project import feature. After importing a project you will have to remove unnecessary elements by hand. If the imported project is very large, it will not be very convenient. Thus, large project should be divided into logical modules and only specific modules with needed diagrams should be imported.

Permalink

When I save a diagram to .emf image and try to insert this image file to my OpenOffice document I only get empty image.

Such problem really exists and will be fixed in future releases.

As a workaround we suggest to save your diagrams as SVG and then use free Inkscape editor ([http://www.inkscape.org/](http://www.inkscape.org/)) to export diagrams as hi-res png.

Permalink

We are seeing the following error loading our model: Failed to load Windows configuration. Reseting to default.

This is known problem. Your model and diagrams are ok, the only thing, which could not be restored, is layout of MagicDraw windows inside application. Such things can happen when project is saved and then loaded on computers which has different resolution or different windows management system.

Usually this error does not appear any more after save and load. If it still exists after save/load, please send us md.log file from the user home/.magicdraw directory (the info about where the MagicDraw configuration files are located, you may find in the About screen).

Permalink

When exporting image to EMF and pasting to Mac Word, error message "Image is corrupted" appears .

This is a know problem of Mac Word. Still we don't know when it will be fixed.

Permalink

Are there any recommendations for saving diagram as image?

It is not recommended to use the following fonts for diagram saving as .eps, .emf, and .wmf:

Default, Dialog, DialogInput, Monospaced, SansSerif, and Serif.

Permalink

I am trying to import an XMI 1.1 file with MagicDraw. I got a load error "Wrong XMI version : MagicDraw supports only Unisys XMI 1.0"

Up to MagicDraw 10.0 version, XMI v1.0, v.1.1 and v1.2 load, save and import is supported.

Beginning with MagicDraw 10.0 XMI 2.1 is supported. And only model load from XMI 1.0 - 1.2.

But if you are trying to open an Unisys XMI 1.1 (XMI v1.1 with Unisys extensions), it is not supported by MagicDraw, only Unisys XMI 1.0 can be loaded.

Permalink

I have saved the project file with MagicDraw version 17.0.1 and now I can't open it with MagicDraw version 17.0. Are project files backward compatible?

Project files saved with MagicDraw version 17.0.1 or later cannot be opened with MagicDraw version 17.0 or earlier. Moreover, as of version 17.0.1, the project file inner structure has been changed.

Usually, projects of all MagicDraw versions are not backward compatible.

Please note that once a project file is saved with v17.0.1 for the first time, the backup file of a project created with an earlier program version is created automatically. The backup file is stored in the same location as the project file. While saving the project created with program version earlier than 17.0.1, a warning about the file format incompatibility appears.

Warnings about the file format incompatibility also appear when MagicDraw is downloading or updates automatically.

Permalink

##### [Projects migration to UML 2](https://docs.nomagic.com/support/faq/projects-migration-to-uml-2)

What will happen with my old projects on MagicDraw Teamwork Server?

After opening teamwork projects with MagicDraw 10.0 version or later, they will be converted to UML2 data following the same instructions as for regular MagicDraw projects.

Permalink

What XMI version supports MagicDraw?

Since MagicDraw 10.0 version, XMI 2.1 standard for UML2 is supported.

Permalink

Can I open older MagicDraw files?

With MagicDraw 10.0 or later version you can open all projects, created with previous MagicDraw versions. After opening projects, created before MagicDraw 10.0 version, they will be converted to UML2.

Permalink

##### [UML/Diagramming](https://docs.nomagic.com/support/faq/uml-diagramming)

How can (inv:, def:, init:, derive:, pre:, post:, body: ) type constraints be modeled?

All of the variants, defined in OCL 2.0 spec can be modeled (inv:, def:, init:, derive:, pre:, post:, body: ), but each is modeled in a slightly different way. Correspondingly, the header line in the OCL expression editor is generated according to model situation.*

**inv:*** is easiest - any simple constraint having an OCL2.0 expression language is treated as invariant. They should have a field constrainedElement filled in, pointing to some class (constrainedElement=SomeClass). To be extra thorough in following the OCL spec, you should also apply the <<invariant>> stereotype on the constraint, but this is not necessary - it is implied.

Note that any other OCL constraints/expressions, that the handling code can not classify into the more specific categories (as defined below) are treated as inv: constraints.*

**def:*** - definition constraints are modeled in the same way as invariant constraints, but the constraint must have <<definition>> stereotype applied. The concrete element to be defined (additional field or additional operation) is placed inside of the body.*

**init:*** - this has to be an expression (not a constraint!) placed in some property's defaultValue field. So, you need to create some property in your class, then open specification of that property, then rightclick the Default Value field, go to >Value Specification>Opaque Expression. After this you can enter the OCL into the field in the same manner as you enter OCL into the specification field of the constraint*.

**derive:*** - is modeled the same way as init, but the property has to be derived ( isDerived=true ).*

**pre:**, *post: - these are constraints on some operation of the class. However these must be placed NOT as a simple constraints(rightclick>New Element>Constraint) BUT in a special designated fields(metaproperties) of the operation. Open operation specification window, switch into Expert mode, see the Precondition, Postcondition fields. Click the necesary field, click [+], then choose Constraint. Fill in the OCL constraint as necessary.*

**body:*** - body condition is filled in the same way as pre and post conditions, but there is an additional hoop to jump through - for some reason, I do not know why, Body Condition field is marked as not shown in Expert mode (neither in Standart). So in specification window of Operation, click Customize button, find Body Condition field, and flip the radio button to Expert, and OK the dialog. After this, Body Condition field will appear in Expert mode specification window of operation in the same way Precondition and Postcondition fields do.

Small nuance: operation can have multiple pre and post conditions but only one body condition.

All these things are described/mandated in the OCL spec (06-05-01.pdf for OCL2.0), chapter 12: The Use of OCL Expressions in UML Models.

Modeling of these expression types is also briefly mentioned in MagicDraw UserManual.pdf. See chapter 8 Model Analysis>Validation>Advanced Topics>Modeling other types OCL2.0 constraints/expressions

Permalink

Search for the elements, which are not used in diagrams, finds attributes, operations, or slots that are represented on transitions. How to find out whether a particular element is needed in the model or not?

It is considered that an element is used in a diagram, when there is a dedicated symbol representing it on the diagram. States and transitions have dedicated symbols for them. When a signal is assigned to the transition via trigger, it does not have a dedicated symbol on the diagram. It is only a part of textual representation of transition signature.

Let's do the following: assign a type X to an attribute on a diagram. Though we see X on the diagram as an attribute type, it is not considered as used in the diagram, because it is displayed only as a part of the attribute notation.

If you want to find out whether a particular element is needed in the model or not, use the Usages/ Dependencies functionality. Select an element in the Model Browser and from its shortcut menu select Used By. This way you may follow the chain of elements in the model and decide whether a given element is rubbish, or it makes sense.

Permalink

I have no possibility to display the names of transitions in the State Machine diagram. The option "show name" in the context menu of the transition doesn't work.

The name of the transition (the value of the name property) is never shown in diagram - this has no semantic meaning. Instead, you can specify e.g. a signal, that triggers the transition. In this case the name of the trigger is displayed. If trigger name is not specified, signal name is displayed. If start typing on a transition, the signal with the name is typed will be created Automatically and the trigger will reference that signal.

A trigger defines types of events that can initiate a transition between states. An event is anything that can happen in a system: signal sent by some behavior, a call to a specific operation, reaching a point in time, a change in values within the system, etc. In other words, the formally defined list of possible events is enough for modeling state machine transitions using UML. A transition has to know of some event (indirectly), it cannot be fired by a trigger alone.

Transition signature defined in section 15.3.14 of UML 2.2 is as follows:

::= [ [',' ]* ['[' ']'] ['/' ]]

However, trigger is a non-terminal and its production rule is described in section "13.3.31 Trigger" (UML 2.2):

::= | | | |

Production rules for call-event, signal-event, any-receive-event, time-event and change-event are described in sections 13.3.6, 13.3.25, 13.3.1, 13.3.27, 13.3.7 respectively:

::= ['(' [ ] ')']

::= ['(' [ ] ')']

::= 'all'

::= |

::= 'after'

::= 'at'

::= 'when'

As can be seen, trigger names are never used in transition labeling. Instead, names of the referenced elements are used.

Permalink

I have two diagrams on which the same pair of classes appears. On one of the diagrams an association is displayed between this pair, but not on the other. How can I get this association to appear on the other diagram?

Please use Related Elements > Display Paths shortcut menu command.

Permalink

I have a class which has a realization relationship to an interface. When I use this class in a sequence diagram (as the receiver of a message), I cannot select the operation, which is part of the interface.

Class must implement all operations from interface first. From the class shortcut menu, choose Tools->Implement/Override Operations or implement all operations manually.

Permalink

How do I connect interface to port with Interface Realization relation?

Port must have type specified. Only after that provided interfaces can be specified. This is because port can't provide interfaces itself, port type does (Interface Realization relation is created between type of the port and Interface, it can't be connected to Port, because port is not Classifier). Port type can be also class like port_impl.

Permalink

How do I associate a state diagram with a certain class?

There are two ways:

1. Drag and drop a state diagram on the selected class in the browser.

2. Choose the "State Diagram" command from the class shortcut menu in the browser tree.

Permalink

Is there any way to get a sequence diagram from a communication diagram?

Currently there is no way to generate a sequence diagram from a communication diagram, or vice versa.

Communication diagram is kind of Interaction Diagram and reuses some UML elements from Sequence Diagram, but is very limited. Most of advanced Sequence Diagram elements can't be reflected in Communication Diagram. It includes all kinds of CombinedFragments, Gates, Nested activations, Sequence of messages and more, so even theoretically Communication Diagram can't be equal to Sequence Diagram.

Currently we try to gather information what would be the benefits of this feature. We would be very grateful if you could share your opinion with us.

For non automatic elements reuse - Communication Diagram can be generated inside the same Interaction (as Sequence Diagram). In this case Lifelines can be reused by simply drag'n'drop them from Interaction directly to communication diagram.

Permalink

If I add a class to a class diagram and begin typing its name with the prefix of the already existing class, the name will be automatically completed. How to tell MagicDraw that it has made the correct assumption and that I would like to accept its choic

Go with the arrows to the desired class name and press Enter.

Permalink

Does your tool support bidirectional associations (arrow at each end or no arrows)?

MagicDraw allows you to show navigability arrow only on one end of an association path. When both ends are "navigable," MagicDraw simply suppresses that information and arrows are not visible.

Permalink

How to do a loop with a conditional in sequence diagram?

You may model loops and conditions using fragments.

Use Combined fragment with operator "loop" for iteration notation and add another one Combined Fragment with operator "alt" for conditional messages grouping inside loop.

Permalink

I would like to specify that a string has maximum length 8 or that an account number has only 14 numbers. How do I specify this?

"Type Modifier" property should be used. Open property specification window, switch to the "Expert" property displaying mode, and define value (for example - 14) there.

Permalink

Is there a way to automatically display links when element with relations is dragged onto the diagram?

To automatically discover relations on elements drag'n'drop - go to Options -> Environment -> Diagram -> Editing -> and change Display paths on element drop to true.

Permalink

Is there a way I can find all items in the containment tree that are not used in any diagram? This would be useful to tidy up models.

You can easily find elements that are not used in any diagram using MagicDraw Find functionality.

Select command Find... from the main Edit menu to invoke Find dialog. Then specify search scope (we do not recommend to search in the whole Data package, as elements from modules will be found), and select checkboxes "Search data unused in diagrams" and "Load diagrams and unloadable modules".

Elements that are not used in any diagram will be displayed in the Search tab in model browser.

Permalink

How to visualize particular parts of the model in a diagram?

To visualize relationships between elements do the following:

1. Select one or more elements in the diagram.

2. Right-click selected elements and, from the shortcut menu, select **Related Elements** > **Display Paths**. To see related elements of the selected element do the following:

1. Drag an element into a diagram.
2. Right-click this element and, from the shortcut menu, select Related Elements > Display Related Elements . The Display Related Elements dialog will open.
3. In the dialog, choose settings you need and click OK. We suggest using the Layout feature to arrange elements automatically for a better view in a diagram. You can find this feature in the main menu, in the diagram toolbar, or in the diagram shortcut menu. For more information about related elements please refer to Section Displaying Related Elements in MagicDraw UserManual.pdf. To open the manual, in the main menu, select Help > MagicDraw UserManual . Also you can find the manual in the < MagicDraw install root > \manual folder.

If you are using MagicDraw 16.8 or the later version, you can use a Relation Map for the relationship visualizing. To create the Relation Map do the following:

1. Select one or more elements in the diagram.
2. Right-click selected elements and, from the shortcut menu, select Related Elements > Create Relation Map . A new Relation Map will be created. For more information about the Relation Map creation please refer to Section Relation Map in MagicDraw UserManual.pdf. To open the manual, in the main menu, select Help > MagicDraw UserManual . Also you can find the manual in the < MagicDraw install root > \manual folder.

Permalink

How could I change the symbol style?

There are several ways to change the symbol style. For this purpose you can use:

- Buttons on the Diagram toolbar 
 - **Project Options** dialog 
 - **Symbol Properties** dialog 
 
 Using buttons on Diagram toolbar 
 
 There are buttons in the diagram toolbar designed to modify a symbol style.

[IMAGE alt='' src='https://docs.nomagic.com/images/diagram_toolbar_1st.png']

**Set Selected Symbol Style as Default**. If you select a symbol, for example, class A and click this button, a current class symbol style will be set as default for all new classes in the project.

[IMAGE alt='' src='https://docs.nomagic.com/images/diagram_toolbar_2nd.png']

**Apply Default Symbol Style**. If you select a symbol and click this button, a default style will be applied to the symbol.

[IMAGE alt='' src='https://docs.nomagic.com/images/diagram_toolbar_3rd.png']

**Select All of the Same type**. If you want to select on a diagram all symbols of the same type, click only one symbol as an example of the type and then click this button. All symbols of this type will be selected. Once all symbols of the same type are selected, you could apply changes, for example, a new default style to all of them at one go. 
 
 **NOTE:** If you can not see these buttons, please, switch your perspective to the Expert mode (on the main menu, click **Options > Perspectives > Perspectives**and select the **Expert** check box in the **Select Perspective** dialog). 
 
 Using Project Options dialog 
 
 1. On the main menu, click **Options > Project**. The **Project Options** dialog will open. 
 2. In the Project Options tab tree, select **Symbols properties styles > Default**, expand **Default** if needed, and then click the appropriate node: **Shapes, Paths, Diagram**, or **Stereotypes**. If you want to change style of a particular shape or path, expand the **Shapes** or **Paths** node, and select the desired symbol, for example, the actor or link. 
 3. Edit property values in the pane on the right. 
 4. When you have finished, do any of the following: 
 - If you need to apply changes to the project, click the **Apply** button. The list of diagrams wherein the symbol style changes can be applied will open. Select diagrams (use CTRL or SHIFT keys for multiple selection) you need and click **OK**. Then click **OK** to close the **Project Options** dialog. 
 - If you do not need to apply changes right now, click **OK** to close the **Project Options** dialog. The new style properties will be saved and set as default. 
 
 Using Symbol Properties dialog 
 
 1. Select a symbol and open the **Symbol Properties** dialog (right-click on the symbol and select **Symbol(s) Properties** or press ENTER+ALT). 2. Edit symbol property values (see figure bellow). 3. Select the **Make Default**check box before closing the dialog (see figure bellow), and all symbols of this type in the same diagram will be in the new style.

[IMAGE alt='' src='https://docs.nomagic.com/images/MakeDefault_selected.png']

Permalink

##### [Printing](https://docs.nomagic.com/support/faq/printing)

MagicDraw crashes or some text is messed up when printing a diagram.

Try to add "-Dsun.java2d.print.shapetext=true" property at JAVA_ARGS in mduml.properties* file, located in MagicDraw install root, "bin" directory.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Page margins are returned incorrectly from the Page Setup dialog

Add "-Dmagicdraw.pageSetupDialog=true" property at JAVA_ARGS in mduml.properties* file, located in MagicDraw install root, "bin" directory. It will enable magicdraw page setup dialog in which paper margins could be customized.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Page setup dialog doesn't list large media size on Linux

Add "-Dmagicdraw.pageSetupDialog=true" property at JAVA_ARGS in mduml.properties* file, located in MagicDraw install root, "bin" directory. It will enable magicdraw page setup dialog in which media size could be customized manually by typing size in inches.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

When I try to print, I get a warning dialog that says "No print service found." I am able to print with other applications as well as from the command line of a terminal window.

Problem is that the default server address in CUPS 1.2 is a domain socket, which Java does not support. They will be implementing a fix for that. At current time you can force your Java applications to use IP instead of domain sockets. Create/update an /etc/cups/client.conf file containing:

ServerName localhost

Permalink

##### [Code Engineering](https://docs.nomagic.com/support/faq/code-engineering)

How to reverse Java 7?

Our code engineering supports Java 6. Java 7 isn't supported yet. This capability is scheduled for our 17.0.2 release.

Permalink

While Reversing Oracle database I got the following error. Any idea?

Data reading error: ORA-06502: PL/SQL: numeric or value error

LPX-00210: expected '<' instead of 'n'

ORA-06512: at "SYS.UTL_XML", line 0

ORA-06512: at "SYS.DBMS_METADATA_INT", line 3296

...

There is a bug in Oracle 9 METADATA package.

Solution can be to reverse with user having all privileges or applying latest patch to Oracle 9.x.

As a workaround is to export database to DDL file and reverse with MagicDraw.

Permalink

Is it possible to reverse QT library?

Since MagicDraw 12.1 SP2, you may reverse QT library.

To reverse QT library using MagicDraw 12.1 SP2, you should add the following macro into MagicDraw > Options->Project... C++ Language Options ... Use explicit macros (these macros are included into MagicDraw starting from v12.5 )

// QT

#define Q_AUTOTEST_EXPORT

#define Q_CLASSINFO(name, value)

#define Q_COMPAT_EXPORT

#define Q_CORE_EXPORT

#define Q_CORE_EXPORT_INLINE inline

#define Q_D(Class)

#define Q_DECL_IMPORT

#define Q_DECLARE_ASSOCIATIVE_ITERATOR(map)

#define Q_DECLARE_BUILTIN_METATYPE(TYPE, NAME)

#define Q_DECLARE_EXTENSION_INTERFACE(IFace, IId)

#define Q_DECLARE_FLAGS(Flags, enum)

#define Q_DECLARE_INTERFACE(IFace, IId)

#define Q_DECLARE_METATYPE(txt)

#define Q_DECLARE_MUTABLE_SEQUENTIAL_ITERATOR(c)

#define Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR(c)

#define Q_DECLARE_OPERATORS_FOR_FLAGS(Flags)

#define Q_DECLARE_PRIVATE(Class)

#define Q_DECLARE_PUBLIC(Class)

#define Q_DECLARE_SEQUENTIAL_ITERATOR(name)

#define Q_DECLARE_SHARED(name)

#define Q_DECLARE_TYPEINFO(TYPE, FLAGS)

#define Q_DECL_DEPRECATED

#define Q_DISABLE_COPY(Class)

#define Q_DUMMY_COMPARISON_OPERATOR(c)

#define Q_ENUMS(x) #define Q_FLAGS(x)

#define Q_GADGET #define Q_GUI_EXPORT

#define Q_GUI_EXPORT_INLINE inline

#define Q_INLINE_TEMPLATE

#define Q_INTERFACES(x)

#define Q_NETWORK_EXPORT

#define Q_NOREPLY

#define Q_OBJECT

#define Q_OPENGL_EXPORT

#define Q_OUTOFLINE_TEMPLATE inline

#define Q_OVERRIDE(text)

#define Q_PRIVATE_SLOT(d, signature)

#define Q_PROPERTY(text)

#define Q_Q(Class)

#define Q_REQUIRED_RESULT

#define Q_SCRIPTABLE

#define Q_SIGNALS protected

#define Q_SLOTS

#define Q_SQL_EXPORT

#define Q_SVG_EXPORT

#define Q_TESTLIB_EXPORT

#define Q_TYPENAME typename

#define Q_XML_EXPORT

#define QDBUS_EXPORT

#define QDESIGNER_COMPONENTS_EXPORT

#define QDESIGNER_EXTENSION_EXPORT

#define QDESIGNER_SDK_EXPORT

#define QDESIGNER_SHARED_EXPORT

#define QDESIGNER_UILIB_EXPORT

#define QDESIGNER_WIDGET_EXPORT

#define QDOC_PROPERTY(text)

#define QT_ASCII_CAST_WARN

#define QT_ASCII_CAST_WARN_CONSTRUCTOR

#define QT_ASSISTANT_CLIENT_EXPORT

#define QT_BEGIN_HEADER

#define QT_DEPRECATED

#define QT_DEPRECATED_VARIABLE

#define QT_DEPRECATED_CONSTRUCTOR

#define QT_END_HEADER

#define QT_FASTCALL

#define QT_FT_BEGIN_HEADER

#define QT_FT_END_HEADER

#define QT_MOC_COMPAT

#define QT_MODULE(name)

#define QT_STATIC_CONST static const

#define QT_STATIC_CONST_IMPL const

#define QT_TR_NOOP(x)

#define QT_TRANSLATE_NOOP(scope, x)

#define slots

#define signals protected

// Microsoft extension

#define __forceinline inline

#define CALLBACK

#define LRESULT void

#define _ENTRY(p1, p2, p3, p4) p1

Permalink

When I reverse engineer my project, there are a number of classes that are referenced in my code that cannot be found and are placed in the "Default" package. All of the classes are found in .jar files that my code depends on. I have checked the box that

When I reverse engineer my project, there are a number of classes that are referenced in my code that cannot be found and are placed in the "Default" package. All of the classes are found in .jar files that my code depends on. I have checked the box that tells the reverse engineer to look in the classpath for classes. Is there somewhere in magicdraw where I should set the classpath?

Permalink

Is there any way I can import an existing jar-file so that the classes from this file will be usable in the project ?

You can use bytecode engineering set for reversing class files placed in your jar. Right click on "Code Engineering sets" node in browser, "New -> Java bytecode" and then edit created code engineering set by adding class files from jar file. Execute "Reverse" action on created code engineering set and classes will be created in model.

Permalink

How to import certain Java types?

Choose the 'New From Template' command from the 'File' menu. You may also reverse the needed Java classes and import them to the project.

Permalink

What is the difference between the Quick Reverse and the general one?

Performing the Quick Reverse you may instantly add new model elements or merge with the created ones in your model; you don't need to create a new Round Trip Set. Use it if you don't want to use code generation on the reverse code constantly.

Permalink

Does MagicDraw allow to import current Java source code, alter the OO model and create modified source code?

Yes, it does. We call this "round-trip engineering". You can reverse your source code, make changes in the model and regenerate it back without losing already coded parts (e.g. method bodies). You must use the code engineering set (the MagicDraw name for a collection of classes for code engineering). If you only do framework generation (Ctrl+G), you will receive only the generated framework (all other information will be lost), so be accurate at this point.

Permalink

Do you have an edition of MagicDraw that can parse a set of Java files and create the corresponding class diagram?

MagicDraw Professional Java Edition possesses reverse engineering capability for Java. You may also reverse descriptors and will get a model describing your Enterprise Java Beans.

More information about MagicDraw editions you may find at www.nomagic.com/editions.php

Permalink

##### [Features](https://docs.nomagic.com/support/faq/features)

How can I share files (images, other projects, text documents, etc.) together with a project?

There are a couple of solutions:

1. You can copy and paste or drag and drop images to a diagram. The image shape will be available for the copied image. MagicDraw supports .gif, .jpg, .svg, and .png image file types.

Note: The project size increases accordingly to the quantity and size in bytes of the inserted images, and this might have a great impact on the performance.

2. You can link external files to the project by specifying the relative paths to them. The relative path is always suggested, when creating a hyperlink to the external file, which is stored in the same folder with the project.

A relative path for a hyperlink can also be specified manually, e.g., "file:// /My Pictures/sample.jpg" for the picture, which is stored in the My Pictures directory that is located in the same folder with the project.

Permalink

Is it possible to add a hyperlink with a relative path* to an image or a project file?

*A relative path begins at a current folder of the hierarchy (i.e., a project or the MagicDraw installation) and specifies the file's location from there.

You can add a hyperlink with a path, which is relative to the MagicDraw installation folder. For example, the path "[file://sample.jpg](file://sample.jpg)" refers to the image, which is stored in the MagicDraw installation folder.

A path, which is relative to the project storage location, is always suggested, when creating a hyperlink to the file, which is stored in the same folder with the project. A relative path can also be specified manually. For example, the path "[file://My Pictures/sample.jpg](file://My Pictures/sample.jpg)" refers to the picture, which is stored in the My Pictures directory that is located in the same folder with the project.

Permalink

Is there any plugin to make automatically the UML2 transformation without having to make File->Export->To UML2 from the user interface?

Just go to "Options->Environment->EMF UML2 (vx.x) XMI Options", and change the option "Export Model to EMF UML2 XMI on project save" The project will be exported on project saving.

Permalink

We are editing different diagrams in the same model, which is held in the CVS repository.Although working in different areas of the model, we keep getting unmergible files from the repository whenever we update our working versions from CVS after the othe

In MagicDraw, the following options are available for sharing model for simultaneous work:

1. Model decomposition functionality is available in MagicDraw. Now it is possible to reuse project module in another project.

2. MagicDraw Teamwork Server. This product is fully optimized for working with UML model.

3. Since MagicDraw version 12.5, Teamwork Server integration with ClearCase and SVN is presented.

CVS is an options just for storing, not sharing

Permalink

How to copy a diagram into the Windows clipboard and paste into a Word doc?

Choose the 'Copy as EMF' or 'Copy as JPG' command from the 'Edit' menu.

Permalink

Does MagicDraw support model consistency between all diagrams?

MagicDraw supports metamodel relation (consistency) between class and interaction (sequence and communication) diagrams: it reflects all the operations of the class in the message call action list. Classifier can be assigned to any lifeline. Class operations can be selected in the triggers in the state/activity diagrams.

Permalink

How to open console together with the MagicDraw application?

Edit file mduml.properties* in bin directory. Change line CONSOLE=false to line CONSOLE=true

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Is there any way that I can access elements from other projects?

Since MagicDraw Version 7.0, partitioning functionality is presented in MagicDraw. Now it is possible to reuse project module by reference in another project.

Also MagicDraw Teamwork Server is available, which enables team collaboration.

Permalink

##### [Integrations](https://docs.nomagic.com/support/faq/integrations)

MD v15.5, oAW 4.3 and Eclipse 3.4 integration. Try to run oAW sample as oAW workflow. The exceptions appears in console and sample fails to run. 5 INFO WorkflowRunner - Exception in thread "main" java.lang.ExceptionInInitializerError at org.openarchitectu

The problem is outdated Xerces library, used by MagicDraw. Please remove this library (it is not necessary, because java 1.5/1.6 already has XML parsing in the standard install).

There is also a workaround. Please specify the-Djavax.xml.parsers.SAXParserFactory=com.sun.org.apache.xerces.internal.jaxp. SAXParserFactoryImpl parameter for the Java when running the workflow. This will force the script to use Java's default implementation instead of one brought in by MagicDraw.

Permalink

I get an error when trying to perfom CVS operations in MagicDraw. I use a local cvs repository at home. Does MagicDraw support a CVSROOT of the form "/my/cvsroot"?

MagicDraw CVS integration supports only pserver connection type.

Permalink

Automatic search in combo boxes is not working. I'm using MagicDraw integrated with IntelliJ.

You should modify the idea.properties file in the IntelliJ: idea.popup.weight property set to medium. After editing it should look like that: idea.popup.weight=medium

Permalink

Does MagicDraw support Eclipse integration within OSX?

Since MagicDraw version 12.5, Eclipse and MagicDraw works together on Mac OS X with JVM 1.6.0.

Permalink

Do MagicDraw integrations with IDEs support Java 5.0 code engineering?

Since MagicDraw 10.5 version, integration with Eclipse supports Java 5.0 code engineering.

Since MagicDraw 15.0 version, integration with NetBeans and JBuilder (works only up to MaigcDraw v17.0.1) supports Java 5.0 code engineering also.

Permalink

Does MagicDraw Standard edition integrate with Eclipse?

Yes, MagicDraw Standard edition, as well as Professional integrates with Eclipse, WSAD, JBuilder (works only up to MaigcDraw v17.0.1), Sun One Studio, and NetBeans without any problems. The difference is that the Standard edition itself has no code engineering functionality but this does not have any impact to the integration.

Permalink

Do you plan to link with any of the popular IDEs/source code tools?

Yes. We currently have integrations with Eclipse 3.1 or later (JDT or Java IDE), JBuilder 8.0, 9.0, X, 2005, 2006, 2007 (works only to MagicDraw v17.0.1), 2008, IBM RAD 7.0, IBM RAD 7.5, BEA WebLogic Workshop v9.2, v10.1, v10.2, Netbeans 6.0 or later, Sun Java Studio 8, Sun ONE Studio 5 (works only up to MagicDraw 10.5 version), IntelliJ IDEA 4.5 or later.

Permalink

With what version of IntelliJ IDEA integrates MagicDraw?

MagicDraw integrates with IntelliJ IDEA 4.X or later

Permalink

Diagrams or Browser tabs are frozen because of modal dialog appearance.

The solution is to close and reopen Diagram View or Browser tabs in all Eclipse perspectives.

Permalink

I am trying to install MagicDraw and use Eclipse integration in Japanese, but menu fonts are corrupted.

Please, try to add such line -DdefaultFont=true in eclipse.ini file after vmargs.

The lines should look like:

-vmargs

-DdefaultFont=true

Permalink

After unintegration, Eclipse cannot be started with new integrated MagicDraw

After unintegration, old directory is still remembered by Eclipse. The solution is to unintegrate Eclipse from MagicDraw, then start Eclipse, close it, and only then integrate with new MagicDraw version and launch again.

Permalink

Out of memory errors with MagicDraw and Eclipse

Some JVMs put restrictions on the total amount of memory available on the heap. If you are getting OutOfMemoryErrors while running Eclipse, the VM can be told to let the heap grow to a larger amount by passing the -vmargs command to the Eclipse launcher. For example, the following command would run Eclipse with a heap size of 512MB:

eclipse [normal arguments] -vmargs -Xmx512M [more VM args]

Some JVMs have restrictions on permanent generation memory, which can be exceeded in integration. In order to increase permanent generation memory size, you need to specify additionally -XX:MaxPermSize (use it for Sun JVM). For example, the following command would run Eclipse with a permanent generation memory size of 128MB:

eclipse [normal arguments] -vmargs -XX:MaxPermSize=128M [more VM args]

Permalink

MagicDraw integrated with Eclipse cannot be started

Sometimes when starting MagicDraw from Eclipse, MagicDraw is not started. This problem can appear after MagicDraw version update. The solution is to launch Eclipse with the -clean parameter first time when this problem appears:

eclipse -clean

Permalink

MagicDraw windows are not redrawed properly running within Eclipse

If you have specified property "-Dsun.java2d.d3d=false" in "eclipse.ini", try to remove it or set the "true" value.

Permalink

I have followed integration steps for MagicDraw 17.0 and Eclipse 3.7, but I see no integration inside of Eclipse. What should I do?

MagicDraw 17.0 SP2 and earlier is not compatible with Eclipse 3.7.

We suggest you to integrate MagicDraw 17.0 SP2 with Eclipse 3.6.

uml2ecore transformation of openArchitectureWare framework does not work on Linux, Mac OS

Symptom: you get the following error when doing uml2ecore transformation:

797 INFO CompositeComponent - Generator.contraintsEtc: generating 'org::openarchitectureware::util::uml2ecore::templates::files::root FOR ecoreModel' => directory 'meta/' 7823 ERROR WorkflowRunner - org/openarchitectureware/util/uml2ecore/templates/files.xpt: unexpected char: 0xFFFD (Note, that char may be different, e.g. on Mac, unexpected char: 0xB4 is encountered)

Cause: uml2ecore transformation contains a bug, which precludes it from working on systems, where default file encoding is non standard. For example on Ubuntu v7.04 (Feisty Fawn) default encoding is UTF-8; Mac OS X, MacRoman encoding is used bu default. This causes transformation to fail, because files.xpt template file in the transformation plugin is encoded in ISO-8859-1.

This bug is not a bug in MagicDraw, but a bug in openArchitectureWare. This bug is acknowledged and tracked in oAW bug list: [https://bugs.eclipse.org/bugs/show_bug.cgi?id=177956](https://bugs.eclipse.org/bugs/show_bug.cgi?id=177956) This bug is present in oAW v4.1.2. Currently we do not know, when this issue will be fixed.

Workaround:

1) locate the uml2ecore plugin jar file. This file is usualy /plugins/org.openarchitectureware.util.uml2ecore_4.1.2.v20070314.jar (note that version numbers/dates may be slightly different in your install). Backup this file somewhere, we will be editing it.

2) inside this jar archive, locate uml2ecoreWorkflow.oaw file, open it in editor and scroll to the bottom.

3) locate the oaw.xpand2.Generator invocation component (id="Generator.contraintsEtc"), and add additional tag inside. Here is the final result you should get:

..... 
 
 4) update jar archive with this new version of uml2ecoreWorkflow.oaw file

5) restart Eclipse.

uml2 ecore transformation should now run cleanly.

Permalink

##### [Teamwork Server](https://docs.nomagic.com/support/faq/teamwork-server)

Can Teamwork Server up to v17.0 be integrated with SVN v1.6?

Teamwork Server starting from v17.0 supports SVN 1.6 server and client. Teamwork Server up to v17.0 does support SVN server v1.6. However SVN client version 1.4 or 1.5 should be used. Lower version clients are compatible with SVN server v1.6. You can include older SVN clients in system paths or define it for Teamwork Server by setting java properties. To do this open "teamwork_server.properties" file and add "-DSVN= " to JAVA_ARGS line.

Please restart the Teamwork Server to apply changes.

Permalink

I cannot login to the Teamwork Server, although installation has been successful.

Please try to add such line to the Teamwork Server/data/muserver.properties file:

java.rmi.server.hostname=teamwork.server.com, where teamwork.server.com is the ip of the computer of the Teamwork Server.

Permalink

How to connect to the Teamwork Server via ssh?

1. Stop the Teamwork Server.

2. Edit run_server_nogui.properties file by adding -Djava.rmi.server.hostname=localhost to the line JAVA_ARGS. This prevents from direct connecting from client to server (skipping ssh tunnel).

3. Start the Teamwork Server using run_server_nogui.exe.

4. On the client side, run command line: ssh -L 1099:host:1099 [user@host.](mailto:user@host.) Host here is a hostname of the Teamwork Server.

5. Run a client. For a server address, use localhost:1099.

Limitation of such configuration is that all clients should use ssh tunneling.

Permalink

How to start the Teamwork Server on startup of Redhat Linux as service?

Please update TEAMWORK_HOME variable in attached script file (TEAMWORK_HOME="/teamwork/MagicDraw_Teamwork_Server/bin") according to your installation path bin dir.

Copy the "teamwork" service script to /etc/init.d.

Then as a root enable the "teamwork" service for runlevel 3 using following commands:

cd /etc/rc3.d

ln -s ../init.d/teamwork S99teamwork

RedHat based Linux distrubutions the service run levels may be configured using "chkconfig" command.

You may test the "teamwork" service using "service" command.

Use "service teamwork start" command to start MagicDraw Teamwork Server

Use "service teamwork stop" command to stop MagicDraw Teamwork Server

Use "service teamwork status" command to check if MagicDraw Teamwork

Server is running.

Permalink

Scheduling of synchronization between two distant Teamwork Servers does not work. How to turn it on?

The scheduling of synchronization between two distant Teamwork Servers **is by default turned off**. 
 
 To turn on the scheduling:

1. Open the muserver.properties file that can be found in <MagicDraw Teamwork Server installation directory>\data.
2. Edit the file as the follows: server.synchronize.scheduler.enable=true
3. Restart the Teamwork Server.

Permalink

On logging back to the Teamwork Server after the MagicDraw has been crashed, the server complaints that the user is already logged in.

After the MagicDraw application has been crashed, please, wait about 6 min. and only then try to connect.

The other solution is to restart the Teamwork Server.

Note: After restarting the server, all users will be disconnected.

Permalink

I cannot find the Teamwork Server menu, although I see it in the docs.

You should have an evaluation MagicDraw version or a commercial/academic license (not demo) in order to access Teamwork Server menu.

Permalink

How to upgrade the Teamwork Server?

Instructions how to upgrade teamwork server:

1. Stop the Teamwork Server.

2. Remove NT service from the teamwork server (if it was added).

3. Install a new version of the Teamwork Server and run it.

4. When the Import configuration dialog box appears, provide earlier version installation directory, to import configurations from it. 5. Select checkbox Import all projects in order to import teamwork projects from earlier Teamwork Server version.

6. Start new Teamwork Server (add NT service if needed).

7. Install new client version.

8. Uninstall old Teamwork Server.

Newer version install will not detect nor uninstall older one service. Projects should be imported manually. Project server and client version should be the same and cannot be mixed up. Also we recommend to use the same JVM version for server an client.

Importing projects from previous Teamwork Server version.

If you had previous Teamwork Server version with projects stored, it is possible to import them automatically using MagicDraw GUI or perform manual migration.

To import projects using GUI

1. After installation is complete and Teamwork Server is launched first time, the Import Configuration dialog box opens.

2. Path to the previous Teamwork Server installation, which was found in your computer, is specified in the Location text box. You can change this path by clicking "..." button.

3. Select the Import all projects check box for projects transfer to the newest Teamwork Server version.

4. Click Import.

To import projects manually

Copy Projects directory with all its files from previous Teamwork Server installation directory, to the new /Projects directory.

NOTE Follow the instructions in dialog boxes to update profiles during project import.

If server is started on SVN/ClearCase repository.

2. Open Administrator's Console, trigger project export. Choose the directory to dump the data to. Chose the permanent directory (not some temporary directory) - this will be the directory in which server will subsequently operate.

3. In Administrator's Console, reconfigure server for work with Built-In repository; specify the directory where you dumped projects as a directory to work with.

4. Restart server, to use new repository.

5. Projects are now in a new, Built-In repository.

Permalink

We have a project in Teamwork Server with many versions. Old versions use large amount of space on the disk. How to clean up old versions in Teamwork Server?

Clean up of old versions is not recommended but if you really need it you should do the following thing:

1. Stop teamwork server.

2. Backup your project directory.

3. Go to teamwork server projects directory, find there file projects.xml and using this file find directory for project you want to clean up.

4. In this directory you can remove files modelXXX.xml.zip XXX is the version number. Each version is saved in its own file.

For example if you want to remove all versions from 1 to 10 you need to remove model1.xml.zip model2.xml.zip and so on until model10.xml.zip. Please note that:

a. You will not be able to open the versions you removed.

b. Do not remove latest version, in this case you will not be able to open project at all.

c. If your project is module and used in another project (project B) you can get trouble opening project's B old versions.

5. After clean up, start the server.

Permalink

Where can I find the server.log file?

The server.log file is located in /projects.

Permalink

After the December 1st Teamwork Server v16.8 and v16.9 does not start, out of memory error is shown and lots of log files are created in the projects folder. How to start Teamwork Server?

Add parameter value "-Dbackup.interval=YEAR" to JAVA_ARGS in both teamwork_server.properties and teamwork_server_nogui.properties those are located in "MagicDraw Teamwork Server installation directory"\bin.

Permalink

Teamwork Server (prior to v17.0.2 SP3 and v17.0.3 SP1) running as service stops when the user logs out from the OS.

Here are the instructions on how to fix it:

1. Open the file ....\MagicDraw Teamwork Server\bin\teamwork_server_nogui.properties 
 2. Add -Xrs to JAVA_ARGS. It should look something like this: 
 JAVA_ARGS=-Xmx400M -Xrs -Djava.rmi.server.useCodebaseOnly\=true 
 -Dsun.rmi.server.exceptionTrace\=true -Djava.awt.headless\=true 
 -Duser.language\=en -DLOCALCONFIG\=false 
 3. Restart the Teamwork service. 
 4. Log out. 
 5. Test if you can connect to the Teamwork server with MagicDraw.

Note: This issue is resolved in v17.0.2 SP3 and v17.0.3 SP1

Permalink

In Teamwork server up to v17.0.2 SP3 and v17.0.3 SP1, there are issues with adding/starting the service using Java versions 1.7.0_21 and 1.6.0_45.

This issue is caused by Java update

[http://www.oracle.com/technetwork/java/javase/6u45-relnotes-1932876.html](http://www.oracle.com/technetwork/java/javase/6u45-relnotes-1932876.html)

The solution is to use an earlier Java version. The list of recommended Java versions can be found at [http://www.nomagic.com/support/jvm-list.html](http://www.nomagic.com/support/jvm-list.html)

Problem will be fixed in the next teamwork server version and service pack.

Permalink

A stereotype applied on attribute, operation, parameter, or other kind of property disappears from the model after the project update from Teamwork Server 17.0.4, if a property has been edited. How can this be handled?

To handle the problem, please use the following workaround:

1. Open the mduml.properties * file that can be found in <MagicDraw installation folder>\bin.
2. Next to JAVA_ARGS, add the following line: -Ddisable.element.version.service=true. Example: JAVA_ARGS=-Xmx2396M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -DLOCALCONFIG\=true -splash\:data/splash.gif -Xss1024K -Ddisable.element.version.service=true
3. Restart MagicDraw.

The issue will be fixed in v17.0.4 SP1.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

Teamwork Server stops when I log off from my OS. Is there a solution to this?

If Teamwork Server is running as application, it does stop upon logoff from the OS. The solution is to run the server as a service. 
 
 Please check Teamwork Server User Guide, section "Starting the server without using GUI" for detailed instructions for your particular OS. The User Guide is available at [http://www.nomagic.com/support/documentation.html](http://www.nomagic.com/support/documentation.html)[.](https://docs.nomagic.com/support/documentation.html)

Permalink

##### [Modules](https://docs.nomagic.com/support/faq/modules)

Do you support editing a referred module inside a project?

Yes, MagicDraw supports both read-only and read-write modes for module usage. Usage of read-write modules is a bit tricky, especially if we have modules nested in one another and with circular dependencies between one another. When partitioning always refer to Modules dialog (Options>Modules) as your friend and guide.

Permalink

Do you support dynamic loading of modules?

Yes, module can be loaded/unloaded by the user at (almost) any time during the work process. Also module usage has a parameter which governs if module should be loaded at project load time: "always load" means module is loaded with project "auto-load" and "auto-load with prompt" module is not loaded, but MagicDraw tries to guess when user would need module contents (e.g. when user runs search in the entire model) and loads module then.

"manual load" means module is not loaded - user can load it later.

Permalink

##### [Floating licenses (v16.8 and later)](https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later)

Cameo daemon thinks my hostid is 000000000000

I got the following messages in my cameo daemon log file: 
 16:36:22 (cameo) Server started on cm1 for: MagicDrawEnterprise 
 16:36:22 (cameo) Wrong hostid on SERVER line for license file: 
 16:36:22 (cameo) licenses/cameo/license.txt 
 16:36:22 (cameo) SERVER line says 90b11c596715, hostid is 000000000000 
 16:36:22 (cameo) Invalid hostid on SERVER line 
 16:36:22 (cameo) Disabling 5 licenses from feature MagicDrawEnterprise(0393 0246 4250 573D ) 
 16:36:22 (cameo) EXTERNAL FILTERS are OFF 
 16:36:22 (cameo) No valid hostids, exiting 
 16:36:22 (cameo) EXITING DUE TO SIGNAL 34 Exit reason 2

**Answer**

Currently, FlexLM does not support interface names other than eth0, eth1, ..., ethN. Alternate interface names, such as em1, are not recognized and will return the invalid hostid 000000000000.

As a workaround we offer you to change your interface names to ethN, such as eth0. Consult the documentation of both your system and distribution to learn how to reset an interface name. Look for more information:

- Solution for "Hostid 00000000000" on Red Hat 6 and Fedora15
- Consistent Network device naming-Name network interfaces to match chassis labels

Please contact our customer support, if this does not help.

Permalink

How to return the floating license if two licenses are used by the same user on the same PC?

When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.

By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.

For more details, please see [How to release a hanging license to the pool?](https://docs.nomagic.com/support/faq/53-floating-licenses-v16-8-and-later/122-how-to-release-a-hanging-license-to-the-pool)

Permalink

How to release a hanging license to the pool?

There are several methods how to release license:

1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at [http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf](http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf)

2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. Follow the link http://:8080 to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.

3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at [http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf](http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf)

Permalink

I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?

You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.

In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.

Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at [http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf](http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf)[.](https://docs.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf)

Permalink

What command-line options are available with lmadmin?

You can find list of the options by issuing the following command at the command prompt:

>lmadmin -help

Permalink

I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.

Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.

Permalink

When we try to start the cameo vendor daemon, we get the error:(lmgrd) cameo using TCP-port 0 (cameo) tcp_s is bad!!! EXITING (cameo) DUE TOSIGNAL 28 Exit reason 5

Such an error appears when demo daemon, included in the license server installation, has expired

Please remove the demo daemon from the server and try again. There are couple few ways to do so:

- You can remove it from server graphical interface side, or
- Directly from server.xml file side. Do as following:

1. In order to start the server without demo daemon, first remove daemon from the server.xml file. This file you can found in the platform directory "conf" folder.
2. Remove the line: <daemon dateBasedVersion="false" dlog="false" executable="demo/demo" license="demo/demo.lic" logFile="logs/demo.log" logOverwrite="false" name="demo" port="0" restartRetries="3"/>
3. Start license server again.

Permalink

When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?

Such an error appears when:

The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.

Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.

You may check and change the port number in the FLEXnet license administrator console.

Permalink

The FLEXnet license server doesn’t respond, so the end user cannot connect to the license server. The following information is provided in the Cameo.log file: (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 ... (cameo) Lost communications with lmgrd. Comm

It can occur because of Microsoft® Windows DEP (Data Execution Prevention) on the server. DEP simply kills the lmgrd application when it starts.

The suggested solution is:

1. Stop the license service using LMTOOLS.EXE or the Windows Services dialog box.

2. Open Task Manager and stop all processes named like lmgrd.exe and cameo.exe

3. Select Control Panel > System > Advanced > Performance Settings > Data Execution Prevention

4. Select the Turn on DEP for all programs and services except those I select check box and add to the list LMGRD.EXE, LMUTIL.EXE, LMTOOLS.EXE, and the vendor daemon, where the license manager is installed

5. Restart the service

DEP also may impact LMTOOLS.EXE crashes or stops the license service (you cannot checkout any licenses then). It is known that such a situation occurs not only on the Microsoft® Windows 2008 server but also on the Microsoft® Windows 2003 server.

Permalink

I got error "File not found, cameo.exe" what to do?

As the log says, "File not found, cameo.exe". So the lmadmin cannot find the daemon. There are two reasons / solutions:

- Maybe you have put the daemon cameo.exe in another folder.

Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.

- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from [https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download](https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download)

Permalink

I have firewall blocking the connection to the FLEXnet license server. What ports are used?

By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.

Permalink

License Server Manager Not Starting

The license server manager will not start if either of the following ports are in use:

* Default license server port (no ports in range 27000 to 27009 available)

* Default HTTP port for the license server manager user interface (port 8080)

Permalink

On new key application into FLEXnet licenses server lmadmin error appears – "Inconsistent server host name in: licenses\cameo\…

This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.

Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.

Permalink

Where can I find lmgrid or lmadmin log file?

The location of the log file depends on what license server manager you use.

- If it is lmgrid , the cameo.log and lmgrid.log files can both be found directly in the root package of the lmgrid installation.
- If it is lmadmin , the cameo.log file can be found in <lmadmin installation directory>\logs , for example, C:\Program Files\FlexNet Publisher License Server Manager\logs .

**Note:** The default location of the log file can be changed during the product configuration.

Permalink

How to reset the lmadmin password, if a user cannot connect to a server using a web interface

1. From *<flexnet license server installation directory>\conf*, open the *server.xml* file for editing.

2. In the line

<user firstName="System" id="admin" lastName="Administrator" password="(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ" passwordExpired="false" privileges="admin" type="local-admin"/>

change the password key value to "aa" as shown in the following example:

<user firstName="System" id="admin" lastName="Administrator" password="aa" passwordExpired="false" privileges="admin" type="local-admin"/>

3. Restart *lmadmin* (end the *lmadmin* process and start it again manually).

4. Connect to the FlexNet server (the default address is http://<server_name>:8090) with the following credentials:

User Name: *admin* 
 Password: *aa*

5. In the **User Configuration** tab, click **Edit**, enter a new password and save it.

Permalink

##### [Floating License (v16.6 and earlier)](https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier)

Where can I download the floating license server, which I've purchaced?

Login with the purchaser's username and password, click on license list, and download from there (or get keys from there).

Permalink

How to connect to the Floating License Server via SSH?

1. Stop the Floating License Server.

2. Edit run_server_nogui.properties file by adding -Djava.rmi.server.hostname=localhost to the line JAVA_ARGS. This prevents from direct connecting from client to server (skipping ssh tunnel).

3. Start the FLoating License Server using run_server_nogui.exe.

4. On the client side, run command line: ssh -L 1099:host:1099 [user@host.](mailto:user@host.) Host here is a hostname of the Floating License Server.

5. Run a client. For a server address, use localhost:1099.

Limitation of such configuration is that all clients should use ssh tunneling.

Permalink

Do we need to install a new version of the floating license server, or can we use an old one with new version clients?

Since MagicDraw v12.0, Floating License server supports 12.0 and higher MagicDraw clients versions.

For example FL v14.0 can work with v. 12.0, v12.5, and v14.0 clients.

Permalink

I am unable to add NT service.

You must have administrator rights to add an NT service.

Permalink

I've got MagicDraw running on two PC's but when I tried to install it on another I get a "Not connecting to license server" error message.

Use the text name of the license server instead the actual IP address.

Permalink

MagicDraw Floating license Server and Teamwork Server v15.0 running on Windows 2003 Server as service has to be started after every reboot to make it work. How to avoid this?

Please copy the msvcr71.dll to the /lib. This DLL is installed under \jre\bin.

Permalink

Where can I find more problems and solutions regarding license server - Lmadmin?

Flexera software lmadmin FAQ is available at [http://www.globes.com/support/fnp_utilities_download.htm](http://www.globes.com/support/fnp_utilities_download.htm) > Documentation section > lmadmin Migration FAQ.

Permalink

##### [SysML Plugin](https://docs.nomagic.com/support/faq/sysml-plugin)

How to avoid cyclic dependencies appearing between modules when SysML «allocate», «satisfy», and «refine» relationships connect elements residing in different modules?

The problem is specific for SysML which creates values on both ends for relationships thus creating cyclic dependencies between modules. This issue is fixed in MagicDraw 17.0 SP5 which will be released on April, 2012. Currently as a workaround we suggest to perform the following steps:

1. Export model elements to modules and make them read-only.
2. Then draw «allocate», «satisfy», and «refine» relationships.

Permalink

##### [ParaMagic Plugin](https://docs.nomagic.com/support/faq/paramagic-plugin)

ParaMagic v17.0.1 is incompatible with SysML v17.0.2 SP1

ParaMagic 17.0.1 does not support SysML 17.0.2 SP1 since all SysML Primitive Value Types were moved to the separate "PrimitiveValueTypes" package in order to comply with the SysML 1.3 specification. ParaMagic is dependent on the previous specification and is not finding the primitive value types where it expects to find them. 
 Do not use SysML v17.0.2 with SP1 with ParaMagic v17.0.1.

Permalink

I have the ParaMagic plugin for MagicDraw. How do I access Mathematica to solve parametric equations?

There are three ways for ParaMagic to access Mathematica:

1. Mathematica is installed locally (on the same computer or a networked drive).

2. Mathematica is installed on an internal network as a web services provider. We can provide a web services interface for installation.

3. Evaluation configuration. ParaMagic (as initially installed) is set to access a NoMagic server copy of Mathematica for a 30 day evaluation period. After this, switch to method 1 or 2.

Permalink

ParaMagic needs Java 1.6 to run correctly. Can it run with Java 1.5?

ParaMagic plugin uses specific Java 1.6 features and is not compatible with Java 1.5.

For MacOS, you may download java 1.6 update from Apple page (direct link is [http://www.apple.com/downloads/macosx/apple/application_updates/ja](http://www.apple.com/downloads/macosx/apple/application_updates/ja) vaformacosx105 update1.html). Please note that this java is only for 64-bit Mac OS (as Mac Book Pro can have both 32 and 64 bit operating systems). For 32-bit Mac OS X, users can install SoyLatte JDK to run ParaMagic. For details on SoyLatte, go to: [http://landonf.bikemonkey.](http://landonf.bikemonkey.) org/static/soylatte/

Permalink

How can I learn more about ParaMagic?

Download evaluation copies of MagicDraw, the SysML, and ParaMagic plugins. Go through the demonstration models with help of ParaMagic tutorials. Free access to Mathematica as a web service is available over the Internet during the evaluation period.

Permalink

How does ParaMagic differ from SysML simulations approaches?

Multiple approaches have been proposed, including code generation from state machine and activity diagrams and generation of Simulink models from SysML. Each approach has its applications, but ParaMagic provides a simple, flexible process with links to multiple solvers and data sources. Rather than being the best tool for creating a complex simulation of a small piece of a SysML model, it helps ties together system capabilities at the global level.

Permalink

How does ParaMagic do requirements checking?

Quantitative requirements can be formulated as constraint statements, e.g. If(actual_weight required_weight, Then Result = True, Else Result = False) and incorporated in parametric dagrams. Every time the parametric simulation is executed, the constraint statement provides a clear answer for whether the requirement is being met. Integrating a requirements management tool like Cameo Req+ with MagicDraw and ParaMagic provides a powerful approach to creating, tracing and verifying requirements.

Permalink

Can I use ParaMagic with UML, UPDM (DoDAF/MoDAF), or business process modeling languages?

The official specifications for these other profiles do not explicitly include Parametrics, but, in MagicDraw, SysML features can be linked to these kinds of models and ParaMagic simulations can be incorporated easily.

Permalink

How does the ParaMagic-Excel link work?

ParaMagic allows data to be transferred between a SysML model instance and one or more Excel spreadsheets by creating a mapping between instance values and worksheet cells. The user can import initial data from spreadsheets into a model instance and, after running the simulation, export results to Excel for reports, graphing and further processing. Excel is not used by ParaMagic as a mathematical solver, however, so Mathematica and/or MATLAB is still required.

Permalink

What mathematical solvers does ParaMagic link to?

ParaMagic uses Mathematica from Wolfram Research or MATLAB from The MathWorks or a combination of the two. Solving standard mathematical equations embedded as constraints in SysML parametric diagrams requires Mathematica. Using MATLAB, constraints are written as external calls on MATLAB functions or scripts. Existing simulation models, functions and templates in MATLAB, Simulink or Mathematica can be incorporated directly into SysML models.

Permalink

How does ParaMagic work?

ParaMagic creates a constraint network from the parametric model using constraint graph and "Composable Object" algorithms developed at the Georgia Institute of Technology. "Acausal" networks often make it possible to solve the model in multiple directions, swapping inputs and outputs in the different model instances or at runtime. For example, calculate the weight of a system from its individual components, or calculate the weight allowance for a specific component from the overall system weight budget.

Permalink

What is ParaMagic?

ParaMagic is a plugin for MagicDraw that extracts the parametric relationships in a SysML model, exports them to a mathematical solver program, and uploads the calculation results back into the SysML model. It handles simulation execution, solver management, and some display functions.

Permalink

What are Parametrics used for?

Parametrics insures data consistency within the SysML model and provides the potential for simulating model performance and comparing against system requirements. Possible usage areas:

Engineering projects: calculate cost, weight or power budgets, vehicle speed, component strength, and others.

Computer systems, calculate message traffic levels, database capacity needs, system availability, and others.

Business systems, calculate manpower needs or time to delivery.

Anything from "ballpark" estimates and "sanity" checks to detailed optimization, trade studies and sensitivity analysis can be organized throughout the development process.

Permalink

What is Parametrics?

Parametrics functionality allows SysML model-builders to include mathematical formulas as part of the model. Parametrics is part of the OMG SysML 1.0 specification.

Permalink

##### [Cameo DataHub](https://docs.nomagic.com/support/faq/cameo-datahub)

DataHub 3.0 does not support detection and synchronization of changes to entity stereotypes

When a synchronized entity is given a new stereotype, it will be treated as a new entity in DataHub and the eventual associations previously tied to it are lost. We are working on a Service Pack for DataHub 3.0 that will address and solve this limitation. Per current plans, the Service Pack will be released in mid-May 2009. Until the Service Pack is available, users can avoid the occurrence of this issue by not changing the stereotypes of entities after these have been imported in DataHub and associations created. Please note that the auto-numbering feature of SysML 16.5 plugin for MagicDraw adds new stereotypes to the SysML entities. Therefore these entities, if already imported in DataHub, will be treated as new ones after re-numbering.

Permalink

DataHub Console closed unexpectedly. This issue occurred on Windows 7 update (September 2014)

Solution: 
 To prevent DataHub Console from closing unexpectedly, add the following code into <DataHub folder>\datahubconsole\datahubconsole.ini

-vmargs 
 -Dorg.eclipse.swt.browser.DefaultType=mozilla

Permalink

##### [MagicDraw RSXConverter](https://docs.nomagic.com/support/faq/magicdraw-rsxconverter)

Why the label/text on the relationship is not in a correct position?

You can correct the label/text position for every relationship on the diagram by:

1. Select all elements in the diagram (press Ctrl + A).

2. Right Click on the diagram.

3. Select Paths.

4. Select Reset Labels Position.

Permalink

Why does the conversion stop with the message "Cannot convert string "" to a double"?

This could occur when the model file of RSA/RSM might not supply complete data for the conversion process. Most cases are caused by the element on the diagram.

To solve this problem, elements need to be relocated to get new coordinates.

Currently known elements are:

Separator line inside Alt Combined Fragment needs to be adjusted.

Permalink

The installation process seems to be complete, but I do not see any changes in my RSA/RSM.

Run Eclipse with the -clean option to solve this problem.

eclipse -clean

or modify eclipse.ini by adding the following line

-clean

to always start Eclipse with the -clean option.

Permalink

What is MagicDraw RSXConverter?

MagicDraw RConverter is a tool to convert IBM® Rational® Software Architect (RSA) or IBM® Rational® Software Modeler (RSM) file format (*.emx, .epx, .efx) to MagicDraw-supported file format (*.mdxml).

Permalink

##### [MagicDraw RConverter](https://docs.nomagic.com/support/faq/magicdraw-rconverter)

How long does it take to convert the large model?

It depends on the project size. For jdk1.4 APIs which contain about 3,000 classes, MagicDraw RConverter spent about 4 hours to convert (tested on Pentium4 2.8 MHz, RAM 512 Mbytes).

Permalink

Is that possible for RConverter to convert IBM Rational Software Modeller without any constraints?

No, it is not possible. RConverter can be used only for Rational Rose 2003 model converting.

Permalink

What is the data format after conversion?

MagicDraw 9.0 XMI. Such file can be opened with latest MagicDraw version.

Permalink

Is it possible for RConverter to convert IBM Rational Software Modeler without any constraints?

No, it is not possible. RConverter can only be used for Rational Rose 2003 model conversion. To convert RSA/RSM models, you will need to use RSXConverter.

Permalink

Is that possible to use MagicDraw RConverter on Mac or Linux?

No, MagicDraw RConverter is designed to run on Windows platform (tested on Window XP service pack 2).

Permalink

What is the limitation for the evaluation of RConverter?

The evaluation version of MagicDraw RConverter is 30 days with the ability to convert up to 50 elements.

Permalink

What is MagicDraw RConverter?

MagicDraw RConverter is the tool to convert Rational Rose project (.mdl) to MagicDraw's readable file (.xml).

Permalink

##### [Cameo Inter-Op](https://docs.nomagic.com/support/faq/cameo-inter-op)

How can I import a model from IBM® Rational® System Architect to MagicDraw?

Please use Cameo Inter-Op to convert your model from the IBM® Rational® System Architect format to the MagicDraw format. For more information about Cameo Inter-Op features, see the "[Cameo Inter-Op description](https://docs.nomagic.com/products/cameo-inter-op)" page.

Permalink

How can I import a model from IBM® Rational® Rhapsody to MagicDraw?

Please use Cameo Inter-Op to convert your model from the IBM® Rational® Rhapsody format to the MagicDraw format. For more information about Cameo Inter-Op features, see the "[Cameo Inter-Op description](https://docs.nomagic.com/products/cameo-inter-op)" page.

Permalink

How can I check if the Cameo Inter-Op installation process is complete?

You can test Cameo Inter-Op by transforming a sample that is provided in a program from which you need to transform a model. For example, if it is a transformation from IBM® Rational® System Architect to MagicDraw, select DoDAF_Samples for the transformation.

Permalink

I suspect that a performance issue can be solved by changing memory settings. How can I change it for Cameo Inter-Op?

To change memory settings, please perform the following steps:

1. Open the < Cameo Inter-Op installation directory > \cameo\cameoiop.ini file for editing.
2. Change the values of the arguments shown in the following example :

--launcher.XXMaxPermSize

512m

-vmargs

-Xms60m-Xmx512m

Permalink

How can I provide the IBM® Rational® System Architect model to the customer support team in case that the model is required to be used for the problem investigation?

Please use the Sodius XML exporter to export your IBM® Rational® System Architect model to a format supported by MagicDraw and send the exported model to the customer support team "[Download the Sodius XML exporter](http://download.sodius.com/files/cameo/sa/mdw-sa-xml-export-1.9.3.exe)" .

Permalink

##### [Interchange with Other Tools](https://docs.nomagic.com/support/faq/interchange-with-other-tools)

How can I import IBM Rational Rose files?

MagicDraw RConverter is the tool to convert Rational Rose project (.mdl) to MagicDraw's readable file (.xml). You can download MagicDraw RConverter Evaluation version at [http://www.nomagic.com](http://www.nomagic.com) in the download section.

Permalink

How can I import Borland Together files with MagicDraw 10.0 or later version?

To import Borland Together files you need to open XMI file with MagicDraw 9.5 version, save and then open with MagicDraw 10.0 or later version.

Permalink

Where I can find Export for Unisys XMI operations?

The MagicDraw 10.0 version or later does not have Export As Unisys XMI commands.

Unisys XMI is for UML 1.3, MagicDraw 10.0 or later uses UML2 metamodel.

Permalink

I would like to find out whether it is possible to view a .vsd document in MagicDraw or even convert the .vsd file to MagicDraw format?

There is a Visio plug-in that allows you to export to XMI 1.0. This format is supported by MagicDraw.

Permalink

How can I import IBM Rational Software Architect/Modeler files?

MagicDraw RSXConverter is an eclipse plugin deployed in an RSA/RSM environment for exporting an RSA/RSM file format (*.emx, .efx, .epx) to a MagicDraw readable file format (.mdxml). You can download an evaluation version of MagicDraw RSXConverter at [http://www.nomagic.com](http://www.nomagic.com) in download section.

Permalink

##### [Plugins](https://docs.nomagic.com/support/faq/plugins)

Is DoDAF Plugin 2.0 compatible with DoDAF Plugin 1.0?

DoDAF Plugin 2.0 is not compatible with DoDAF Plugin 1.0. Projects, created with DoDAF Plugin 1.0, cannot be opened with DoDAF Plugin 2.0 and vice versa.

Permalink

How to set up Eclipse for plug-in development?

1. Create Java Project.
2. Include all *.jar files from "MagicDraw\lib" folder into Project Build Path. Exclude "md_commontw_api.jar" and "md_commontw.jar".
3. Write plug-in. Start from main Plug-in class by extending "com.nomagic.magicdraw.plugins.Plugin".
4. Create Plug-in descriptor file "plugin.xml".
5. Make clean plug-in directory in MagicDraw plug-ins directory (./plugins/ ), copy "plugin.xml" to it. Do not copy any binaries to MagicDraw plug-ins directory or they will have conflicts with your binaries in Eclipse.
6. Create new Debug configuration to run Application.
7. select "Project" your plug-in project.
8. search for Main class, select "com.nomagic.magicdraw.Main".
9. add "-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M" to Arguments.
10. Apply changes.

More details can be found in "[MagicDraw Open API User Guide](https://docs.nomagic.com/files/FreeFormDiagram_1_0.zip)"

Hints:

- don't forget to include all sub folders from "MagicDraw\lib" into your Build Path;

- create jar file from Eclipse: use "Export / JAR file";

- you wouldn't have to copy files each time if you will select destination jar file already in "MagicDraw\plugins" folder;

-save jar file description to build jar file later;

Permalink

I have created my own MagicDraw plugin with customer diagram, profile, templates and samples. How do I pack them to share for multiple users through MagicDraw Resources Manager.

Resource Manager needs more information which is stored in resource descriptor. It must know what files were installed because it must be able to perform uninstall operation.

I have attached our free form custom diagram. It would be best if you will look through this sample and I'll describe main rules for descriptor writing. You will find descriptor file in "data/resourcemanager/MDR_Custom_Diagram_Free_Form_1513_descriptor.xml".

- xml tag

- "id" is most important. It must be unique. To prevent duplicates in future use "22**", for example "2201".

- "name" must be unique between all MagicDraw resources.

- "type" must be one of: "Custom Diagram", "Plugin", "Profile", "Sample", "Template".

- is your resource version

- will be needed only if your resource depends on other resources.

- defines files which will be installed. Do not use "*.*" (all files in directory) in common directories like " /samples" because uninstalling your resource will remove all files from this directory!

- each tag defines one file which must be copied to "MagicDraw root" directory.

Descriptor file must be placed in your resource zip file in directory "data/resourcemanager" whith specific naming. Name of descriptor file is formed from values from tag: "MDR_ _ _ _descriptor.xml", all spaces in names is replaced by underscore symbol "_".

[Resource sample you may find here](https://docs.nomagic.com/files/FreeFormDiagram_1_0.zip).

Permalink

SysML 16.5 SP2 has a modification of MD_customization_for_SysML.mdzip how to update MD_customization_for_SysML.mdzip in our Teamwork Server and successfully work with it?:

1. Login with appropriate right, preferable 'Administrator'.

2. Remove MD_customization_for_SysML.mdzip from your Teamwork Server.

3. Create a new SysML project.

4. Add the newly-created SysML project to Teamwork.

5. In the Add Project to Teamwork Settings dialog, select the Local Modules tab.

6. Ensure that the Action for MD_customization_for_SysML.mdzip is Add to Teamwork.

7. Click the Add button in the Add Project to Teamwork Settings dialog.

MD_customization_for_SysML.mdzip will be automatically updated in your Teamwork.

Permalink

##### [Documentation/Help](https://docs.nomagic.com/support/faq/documentation-help)

Where can I find MagicDraw configuration files (md.log and several other files)?

By default MagicDraw configuration and auxiliary files are stored in the user home directory

User home directory/.magicdraw/version.

Information about this location you may find in the MagicDraw About screen, Info tab (Help->About->Environment)

Permalink

When invoking Help>Contents the program hangs.

The "Help" may not be started because another application is using "Help" port. You may see this in the helpserver.log file, which is located in MagicDraw installation directory. If the server port is already in use, the java.rmi.server.ExportException appears in this file. To change Help port, you need to invoke the "Environment Options" dialog from the "Options" main menu. On the appeared dialog, "General" tab change the "Help Server Port", submit changes and try to invoke Help again.

Permalink

MagicDraw Help cannot be invoked. What should I do?

Reasons why you cannot invoke the Help can be the following:

1. There is no reference to the topic, or a particular topic does not exist in MagicDraw Help. If a reference to the topic is broken, you can start the MagicDraw Help manually:

1.1. On the Help menu, click Help Content. The MagicDraw Help opens.

1.2. Browse in the help content or use a keyword to search for a particular topic.

Please let us know about broken links by contacting our customer support.

2. The communication with a server through Remote Method Invocation (RMI) is broken. Please do the following:

2.1. Open the mduml.properties* file. You can find the file in \bin.

2.2. To the JAVA_ARGS line, add a value -Dnostubfixing\=true, as it shown in the following example:

JAVA_ARGS=-Xmx1200M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -Dnostubfixing\=true

If the problem still persists, please contact our support team and attach the following files:

helpserver.log

md.log

You can find these files in one of the following ways:

Go to \.magicdraw\.

On the Help menu, click About MagicDraw. In the About dialog, select the Environment tab and then click the link next to Configuration Files.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

Permalink

The Java documentation, delivered with MagicDraw contains only some package.html files.

You may find full MagicDraw OpenAPI javadoc in *<modeling tool installation directory>\openapi\docs* or download from [http://jdocs.nomagic.com/](http://jdocs.nomagic.com/)[.](http://jdocs.nomagic.com/)

Permalink

Where can I find documentation about working with MagicDraw, MagicDraw integrations, floating license server, and teamwork server?

All MagicDraw documentation is located in MagicDraw installation directory, manual folder. Also you may download it from the www.nomagic.com.

Permalink

##### [Older Versions](https://docs.nomagic.com/support/faq/older-versions)

I'm trying to run MagicDraw 3.5.1, but when I launch the application I get the error message "Can't read/write to main.ini"

When launching MagicDraw Version 3.5.1 or 3.6, you get the error message "Can't read/write to main.ini", contact [support@magicdraw.com](mailto:support@magicdraw.com). We will send you a new main.ini file.

Permalink

When installing MagicDraw on Fedora Core 5, Suse 10.1, and later :error while loading shared libraries error appears

There are two ways to solve it:

1. Use no install version.

2. Modify install script file. Example with MD_UML_115_unix.sh:

cat MD_UML_115_unix.sh | sed 's/export LD_ASSUME_KERNEL/#xport LD_ASSUME_KERNEL/g' > MD_UML_115_unix.sh2; mv MD_UML_115_unix.sh2 MD_UML_115_unix.sh

Permalink

##### [Licensing](https://docs.nomagic.com/support/faq/licensing)

I connect to a network through the LAN or Wireless adapter. When I change the connection from LAN to wireless or vice versa, I get the message about the invalid license file, and MagicDraw closes. What should I do?

MagicDraw licenses are locked to a particular computer using the network adapter’s MAC address. MagicDraw locks itself to the first MAC address in the list. On a Windows computer, the wireless is first by default. If you switch off the wireless, its MAC address is removed from the list and MagicDraw can no longer find it. In order to solve the invalid license problem, you need to change the network adapter order so that the LAN adapter is at the top of the adapters list. That way, the MAC address of the LAN adapter will always be the first in the list, even if you switch to the wireless connection.

To avoid this problem, you should configure your network settings to change the network adapters (connections) order on Windows XP, Windows Vista, and Windows 7 operating systems.

The following procedures explain how to configure your network settings on these operating systems:

Windows XP

1. From the Control Panel , open the Network Connections dialog.
2. On the Advanced menu, click Advanced Settings . The Advanced Settings dialog opens.
3. Select the Adapters and Bindings tab, and, in the Connections list, select the LAN adapter and move it to the top of the list.

Windows Vista*

1. From the Control Panel , open the Network and Internet dialog.
2. Go to the Network and Sharing Center and, on the left side of the dialog, select Manage Network Connections .
3. On the menu, select Advanced > Advanced Settings. The Advanced Settings dialog opens. Note: If you cannot see the menu bar,select Organize > Layout > Menu bar .
4. Select the Adapters and Bindings tab, and, in the Connections list, select the LAN adapter and move it to the top of the list.

Windows 7*

1. From the Control Panel , open the Network and Internet dialog.
2. Go to the Network and Sharing Center and, on the left side of the dialog, select Change adapter settings .
3. On the menu, select Advanced > Advanced Settings. The Advanced Settings dialog opens. Note: If you cannot see the menu bar,select Organize > Layout > Menu bar .
4. Select the Adapters and Bindings tab, and, in the Connections list, select the LAN adapter and move it to the top of the list.

* Depending on your Windows configurations, the command sequence may be slightly different.

Permalink

I'm requested to activate may MagicDraw licenses. What should I do?

Starting from MagicDraw v16.9 commercial licenses are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.

The commercial license activation is needed after the purchase transaction has been completed.

License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.

Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to www.nomagic.com and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.

For MagicDraw, plugins and other products activation instructions refer to: [https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing](https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing)[.](https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing)

Permalink

I'm unable to unlock MagicDraw. "Key or user name is invalid!" message appears.

Make sure that MagicDraw software and unlock key are the same version. If you install the latest software, you must get the latest version unlock keys.

Permalink

How to unlock MagicDraw vesion 12.0 and later?

After downloading MagicDraw, you will get an unlock key file to your mailbox.

1. Save this unlock key file, into the local file system before starting MagicDraw.

2. When starting MagicDraw for the first time you will be asked to browse for the unlock key file. Click the "..." button and select the file from the directory you saved the file.

3. System will automatically activate MagicDraw and you will be able to use it.

Permalink

I have downloaded MagicDraw demo. Where do I get the unlock key?

Unlock key is sent to you automatically by email (to the e-mail address which you provided registering to www.nomagic.com).

Permalink

I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?

Installation on multiple machines is supported by the Mobile or Floating license.

More about Mobile User License could be found at 
 [http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html](http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html)

More about Floating License could be found at 
 [http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html](http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html)

Note: The Seat license can be used by a single user on a single installation.

If you have any questions about the licensing or purchasing, please feel free to contact your account executive or [sales@nomagic.com](mailto:sales@nomagic.com).

Permalink

An additional floating license is reserved after switching from wired to wireless connection and back when MagicDraw is open. That license is released only after some time, but not instantly as I expect to. How can I fix this?

This is a known issue and we are investigating on it. So far we recommend modifying the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.

To set the time-out:

1. Open the FlexNet installation directory, find the *cameo.opt* file and open it for edit. If you cannot find the file, create a new file and save it as *cameo.opt*.

2. Add to this file the following line:

TIMEOUTALL 900

3. Place the *cameo.opt* file in the same directory with the *cameo.exe* file. For example, *C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo*.

4. In the VENDOR line of the license file specify the relative path to the *cameo.opt* file so that the FlexNet server could find it.

For example, 
VENDOR cameo licenses/cameo/cameo **licenses/cameo/cameo.opt** PORT=1101

5. Restart the FlexNet server.

6. Open the *cameo.log* file to check that the *cameo.opt* file is added in the proper directory.

If the path to the file is like in the example of the 3rd step, you should see the corresponding text: 
**14:44:35 (cameo) Using options file: "licenses/cameo/cameo.opt"** 
 14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise 
 14:44:35 (cameo) EXTERNAL FILTERS are OFF 
 **14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds**

Permalink

##### [Users Profiles](https://docs.nomagic.com/support/faq/users-profiles)

Is my personal information secure at www.nomagic.com?

Yes, it is. Even having the username/password, the intruder won't be able to access the credit card information since we don't keep any credit card data in the database. Shopping cart works via HTTPS, therefore, it is impossible to sniff any data.

Permalink

Where can I change my profile data (user name, company name, etc.)?

[Login to our website](https://www.magicdraw.com/main.php?ts=login&cmd_show_login=1&show_confirm=1&menu=login) with your username and password, click on Edit Personal Information right-side menu selection and edit your details.

Permalink

What if I forgot my profile password?

Use our reminder service - enter your email and click the Send password button. New password will be generated and sent by email.

Permalink

##### [Purchase](https://docs.nomagic.com/support/faq/purchase)

Where is my MagicDraw purchase information stored?

Purchased MagicDraw software installation files and unlock keys are stored under your personal profile. In order to download it, [login to our website](https://www.magicdraw.com/main.php?ts=login&cmd_show_login=1&show_confirm=1&menu=login) with your username and password, click on License List right-side menu selection.

Permalink

I would like to receive notifications about the releases of new MagicDraw versions or service packs.

If you want to subscribe to any of existing MagicDraw mailing list, [please login](https://www.magicdraw.com/main.php?ts=login&cmd_show_login=1&show_confirm=1&menu=login) to our web site [http://www.nomagic.com](http://www.nomagic.com) with your username and password. Click on "Mailing List' right side menu selection, check appropriate checkbox and click the Update button.

Permalink

Bought one MagicDraw Floating license a month ago; and bought one more Floating license yesterday. I would like to know how can I add additional Floating license to the Floating license server.

First of all open "key.txt" file located in floating license server installation directory. Then remove key from this file and restart server. After that enter new license key for floating license server. All keys you can re-obtain from your personal download area, by clicking button "Send Unlock Keys": [http://www.nomagic.com](http://www.nomagic.com)

Permalink

How do I get the product updates? Where do I download the newest software?

Notifications about updates will be sent by email. The newest software will be automatically added to your [personal download area](https://www.magicdraw.com/main.php?ts=login&cmd_show_login=1&show_confirm=1&menu=login).

Permalink

Why do I need customer profile, why cannot I go to the shopping cart and order the software directly?

The registration operation and customer profile help us to make sure that you get customer support and discounts when purchasing our products later. Customers purchased software (unlock keys and installation files) also is stored under his/her personal profile.

Permalink

Will I receive my software on CD?

Sorry, we don't have our software on CD. We deliver products electronically.

Permalink

##### [Other Issues](https://docs.nomagic.com/support/faq/other-issues)

After MagicDraw installation, menu items are bold

The problem occurs, when during the installation, the default language is changed. This problem is related to Java 1.7.

The solution is to install MagicDraw* again without changing the default language. Then, you can change the languange after the installation. To do this, on the **Options** menu, click **Environment**, and then in the **General** options group, change the **Language** property.

* This is valid for all MagicDraw-based Cameo Suite products.

Permalink

We have a document management application (built into .Net and IIS 6). When we open a MagicDraw document from the DM application, we get an error "Page not found", even though the page is there.

You have to add a mime type to the IIS configuration. For .mdxml, etc., assign a mime type of application/x-uml.

Permalink

The UML metamodel in UML_Standard_Profile.xml includes only metaclasses and no attributes. However, we need them for defining OCL constraints.

MagicDraw uses the simplified metamodel profile that has no attributes visualized. But the attributes still exist in the code.

As a solution we suggest you to use the sample of the full metamodel profile, because it has no striped attributes. We use this profile mainly as a reference when writing OCL constraints.

Download the sample of the full metamodel profile, using the MagicDraw capabilities:

1. From the Help menu, select Resource/Plugin Manager.

2. Click the Check for Updates button.

3. Wait while the checking for updates is finished.

4. In the Filter box, choose All Resources.

5. In the product list, scroll down to the UML Standard Profile with attributes for OCL and select it.

6. Click the Download / Install button.

The full metamodel profile will be stored in the " /samples" directory.

Permalink

How do I merge completely different projects that have no common history into one project (possibly by choosing only certain parts that should be merged)?

Merge functionality can be employed for this. Choose the Tools -> Project Merge menu item, specify the source project (the project from which you want to port changes), the target project (the project to which you want to port changes), and an empty ancestor project. Then press the Merge button and you will be provided with the standard Merge dialog, which allows you choosing which changes should be merged-in.

Permalink

How to change the font size in various MagicDraw UI places?

Font and other UI style options can be changed by changing look&feel theme (Metal theme should be used). It can be changed from the Options > Look&Feel > Metal. Theme can be customized in theme customization dialog which can be opened from Options > Look&Feel > Customize.

Permalink

Installation file is identified as suspicious or infected by virus. What to do?

Please be sure that you got the installation file from [www.nomagic.com](http://www.nomagic.com).

In this case we can confirm our software is not infected by a virus and it is safe to use it.

One known reason why antivirus software in rare cases identifies *.exe files as suspicious is because of Norton antivirus software issues where a legitimate file is misidentified and subsequently quarantined. More can be found at [http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&tabid=2](http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&tabid=2)[. As they say in above document suspicious level is very low.](http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&tabid=2)

Workarounds for this issue are available. We suggest to:

- ignore suspicions from Norton antivirus.
- use the "no install" installation (*_no_install.zip).
- Symantec suggests disabling the auto protection option and checking if the issue is resolved.

Let us know at [support@nomagic.com](mailto:support@nomagic.com) if more help is required.

We are working with Norton antivirus to eliminate this issue.

Permalink

Is it possible to add a hyperlink with a relative path to an image or a project file?

A relative path begins at a current folder of the hierarchy (i.e., a project or MagicDraw installation) and specifies the file's location from there.

You add a hyperlink with a path relative to the MagicDraw installation folder. For example, the path *[file://sample.jpg](file://sample.jpg)* refers to the image that is stored in the MagicDraw installation folder.

When creating a hyperlink to the file stored in the same folder with the project, a path relative to that location is always suggested. A relative path can also be specified manually. For example, the path *[file://MyPictures/sample.jpg](file://MyPictures/sample.jpg)* refers to the picture stored in the My Pictures directory located in the same folder as the project.

Permalink

##### [CameoMDA](https://docs.nomagic.com/support/faq/cameomda)

I have out of memory problem.

To avoid out of memory problem, you need to select the output folder, which contains only the related source code, otherwise, the oAW engine will scan recursively all the files and sub folders in the selected output folder, and then parse the content of each file. This process will take a lot of memory and can cause of out of memory problem.

Permalink

##### [Specific Domains](https://docs.nomagic.com/support/faq/specific-domains)

What your tool can offer from realtime and embedded systems modeling perspective?

We have integrations and partners with third-party tools to support specific needs. [http://www.sinelabore.com](http://www.sinelabore.com) is the tool which allows you to generates C, C++, C#, Ada or Objective-C code for embedded systems from our State machines.

CoFluent Studio plugin allows to integrate MagicDraw with CoFluent Studio. By exporting UML models to CoFluent Studio, designers can use C/C++ as action language and generate transaction-level modeling (TLM) SystemC code to run simulations. Co-Simulation with MATLAB/Simulink is also available. The instrumented SystemC code coupled with CoFluent Studio?s analysis tools allows designers to observe the real-time execution of their models and extract performance figures like latencies, data throughputs, buffer levels, resource loads, power consumption, memory footprint and cost.

CoFluent Studio targets complex multiprocessor systems with rich application content, whether they are:

- Multi-board (large equipments, distributed/networked systems)
- On-board (embedded systems)
- On-chip (SoC, FPGA, ASIC, ASSP)

Additionally, we are working on our own Simulation Toolkit which allows to run discrete event simulation and supports executable UML standards like W3C SCXML for State Machines and OMG fUML for Activities. Feel free to request demo or additional information at [support@nomagic.com](mailto:support@nomagic.com).

Permalink

What capabilities does your tool offer for model execution and result analysis?

Model execution and simulation capabilities are provided in Cameo Simulation Toolkit for MagicDraw. This tool supports STANDARD BASED Statemachines, Activities, SysML parametrics execution, and quick UI prototyping based on MagicDraw User Interface Modeling diagram.

For more information about Cameo Simulation Toolkit [please visit here](https://docs.nomagic.com/product-addons/magicdraw-addons/cameo-simulation-toolkit).

Permalink

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><div class="subTopic_section"><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="c5d9268e-58ed-4295-8f56-974345fe75ce"><ac:parameter ac:name="title">Performance</ac:parameter><ac:rich-text-body><p><br /></p></ac:rich-text-body></ac:structured-macro><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/major-issues">Major Issues</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">After updating to the latest Java version (1.6.0_39 and higher or 1.7.0_13 and higher), MagicDraw can neither open projects nor accept license files. An Exception is generated. What is the fix for this issue?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Java versions 1.6.0_39 and higher or 1.7.0_13 and higher are incompatible with MagicDraw v17.0.2 (prior SP3) and v17.0.3 (prior SP1) and older versions.</p><p><strong>What is the Reason That Has Caused Java 6 Update 39 and higher or Java 7 Update 13 and higher Incompatibility With Our Products?</strong></p><p>It was Oracle’s mistake in introducing the undocumented behavior changes that have caused the incompatibility between Java and our product. As a result, MagicDraw 17.0.2 &amp;17.0.3 and older versions are not compatible with Java 6 update u39 and higher or Java 7 update u13 and higher.<br /> Oracle Java 6 update u39 and higher or Java 7 update u13 and higher have undocumented changes in the way the threading works. <br /> <br /> <br /> <strong>Solution</strong></p><p>Please <strong><a href="https://docs.nomagic.com/support/installation-and-use.html#applying_patch">manually</a>*</strong> update to:</p><ul><li>Service pack 3 for MagicDraw 17.0.2 which solves this incompatibility issue was released on 25th February 2013.</li><li>Service pack 1 for MagicDraw 17.0.3 which solves this incompatibility issue was released on 4th March 2013.</li></ul><p><br /> For older MagicDraw versions we highly recommend using the officially recommended Java version:</p><ul><li>1.6.0_31 for MagicDraw v17.0.2 (prior SP3).</li><li>1.7.0_07 (1.6.0_35 for Mac OS X Lion and Mountain Lion) for MagicDraw v17.0.3 (prior SP1).</li></ul><p>In order to change Java version which MagicDraw uses, please follow the<strong> <a href="https://docs.nomagic.com/files/Java%20downgrade%20tutorial.pdf">instructions in this file</a></strong>.</p><p>* - autoupdate feature fails to install these service packs because of Java incompatibility. You should follow the instructions for <a href="https://docs.nomagic.com/support/installation-and-use.html#applying_patch">manual update</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/after-updating-to-the-latest-java-version-1-6-0-39-and-higher-or-1-7-0-13-and-higher-magicdraw-can-neither-open-projects-nor-accept-license-files-an-exception-is-generated-what-is-the-fix-for-this-issue"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">A stereotype applied on attribute, operation, parameter, or other kind of property disappears from the model after the project update from Teamwork Server 17.0.4, if a property has been edited. How can this be handled?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To handle the problem, please use the following workaround:</p><ol><li>Open the mduml.properties<sup>*</sup> file that can be found in &lt;MagicDraw installation folder&gt;\bin.</li><li>Next to JAVA_ARGS, add the following line:<br /> -Ddisable.element.version.service=true.<br /> Example:<br /> JAVA_ARGS=-Xmx2396M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M<br /> -DLOCALCONFIG\=true -splash\:data/splash.gif -Xss1024K<br /> -Ddisable.element.version.service=true</li><li>Restart MagicDraw.</li></ol><p>The issue will be fixed in v17.0.4 SP1.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/a-stereotype-applied-on-attribute-operation-parameter-or-other-kind-of-property-disappears-from-the-model-after-the-project-update-from-teamwork-server-17-0-4-if-a-property-has-been-edited-how-can-this-be-handled"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">The file list dialog on Mac OS X doesn't respond appropriately when selecting folders</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p><br /> Fix for this problem is described at <a href="https://bugs.openjdk.java.net/browse/JDK-8006420">https://bugs.openjdk.java.net/browse/JDK-8006420</a></p><p>To solve the problem:</p><ol><li>Open the <em>magicdraw.properties</em> file, which is located in &lt;<em>MagicDraw* installation directory&gt;/bin</em>.</li><li>From the <strong>JAVA_ARGS</strong>= line, remove the -<strong>splash\:data/splash.gif</strong> parameter</li></ol><p>After this fix, on MagicDraw* startup, the spash screen will not be displayed for a few second, but the open file list dialog refresh problem will be solved.</p><p>The fix is sheduled into the nearest release.</p><hr /><p>* - This is valid for all MagicDraw-based Cameo Suite products.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/the-file-list-dialog-on-mac-os-x-doesn-t-respond-appropriately-when-selecting-folders"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw 17.0.5 stops responding on Mac OS X Mavericks, and I keep seeing the spinning wait pointer (aka Spinning Beach Ball of Death). How can I fix the issue?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw stops responding due to an issue detected in Java SE 7 Update 40, which is bundled with MagicDraw 17.0.5 (for the issue details, go to <a href="https://bugs.openjdk.java.net/browse/JDK-8025588">https://bugs.openjdk.java.net/browse/JDK-8025588</a><a href="https://bugs.openjdk.java.net/browse/JDK-8025588">).</a></p><p>This issue will be fixed in <strong>MagicDraw 17.0.5 SP1</strong>, coming out in the middle of February.</p><p>To solve the issue manually (without the SP), switch the version of the bundled Java to SE 7 Update 25*, which does not cause the issue. For this, do the following:</p><ol><li>Open the <em>magicdraw.properties</em> file, stored in &lt;MagicDraw installation directory&gt;/bin.</li><li>Find the JAVA_HOME property and add the path to the location of Java SE 7 Update 25 on your PC. For example, “JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home”.</li></ol><p>Please contact our customer support, if this does not help.</p><p>--<br /> * If you do not have Java SE 7 Update 25 installed on your PC, download the installer from the <a href="http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html#jdk-7u25-oth-JPR">Java SE 7 Downloads</a> page. You need the<em> jdk-7u25-macosx-x64.dmg</em>file.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/magicdraw-17-0-5-stops-responding-on-mac-os-x-mavericks-and-i-keep-seeing-the-spinning-wait-pointer-aka-spinning-beach-ball-of-death"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">On Windows, MagicDraw doesn't support HiDPI screen resolutions. How to solve this problem?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To get the best effect of MagicDraw, lower your screen resolution to HD 1920 x 1080.<br /> The simplest way to change resolution settings is to right-click anywhere on your desktop and select <strong>Screen resolution</strong>. Then use the slider to select the required setting.<br /> We are working to find ways to support HiDPI.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/on-windows,-magicdraw-doesn-t-support-hidpi-screen-resolutions-how-to-solve-this-problem"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How do I adjust the scaling factor when using MagicDraw 18.2 on a HiDPI screen?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can turn off scaling by including a certain parameter to the <em>magicdraw.properties</em> file.</p><ol><li>Open <em>&lt;MagicDraw installation directory&gt;\bin.</em></li><li>Find and open <em>magicdraw.properties.</em></li><li>Find line <em>JAVA_ARGS=</em> and add <strong><em>-Dmagicdraw.resolution.scale=1 </em></strong>to it.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/how-do-i-adjust-the-scaling-factor-when-using-magicdraw-18-2-on-a-hidpi-screen"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Why the Model Browser of my project doesn’t show newly created elements, and corrupted elements appear in it with no reason?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This happens because of the Model Browser refresh problem with MagicDraw 18.0.<br /> To solve this problem, do one of the following:</p><ul><li>Refresh the project (press <strong>F5</strong>).</li><li>Save the project (press <strong>Ctrl+S</strong>).</li><li>Change the Model Browser settings. For example, turn on the <strong>Show Auxiliary Resources</strong> option.</li></ul></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/why-the-model-browser-of-my-project-doesn-t-show-newly-created-elements-and-corrupted-elements-appear-in-it-with-no-reason"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw is unstable and slow when running on Java SE 8 Update 60. How do I solve this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a <a href="http://bugs.java.com/view_bug.do?bug_id=8061636">known</a> Java bug. This issue will be fixed in MagicDraw 18.3, but in the meantime you can upgrade to the <a href="https://docs.nomagic.com/support/jvm-list.html">recommended Java version</a>.<br /> <br /> After installation, open <em>&lt;MagicDraw installation directory&gt;\\bin</em>, and modify the <em>magicdraw.properties</em>* file.<br /> <br /> Change line <em>JAVA_HOME=</em> to correspond with the Java version you\'ve installed.<br /> <br /> * If you are using MagicDraw 17.0.4 or earlier, the properties file is called <em>mduml.properties</em>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/magicdraw-is-unstable-and-slow-when-running-on-java-se-8-update-how-do-i-solve-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw is unstable and slow when running on Java SE 8 Update 101/102. How do I solve this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a known Java bug. This issue is fixed in MagicDraw 18.4. If you are using MagicDraw 18.3 and earlier versions, you can use <a href="https://docs.nomagic.com/component/content/article/jvm-list?Itemid=153">the recommended Java version</a>that comes with installation.</p><p>Once you have installed the recommended Java version, do the following:</p><ol><li>Open the bin folder <em>&lt;MD install directory&gt;\bin</em>.</li><li>Open the file <em>magicdraw.properties</em>.</li><li>Look for the line <em>&quot;JAVA_HOME=&quot;</em> and change the Java version with the one you have installed.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/magicdraw-is-unstable-and-slow-when-running-on-java-se-8-update-101-102-how-do-i-solve-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Solution is to run <em>magicdraw.sh</em> file from the <em>/bin</em> directory.</p><p>This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.</p><p>Please update your modeling tool to the <strong>version 18.4 SP1</strong> to avoid the installation incompatibility.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/major-issues/magicdraw-18-4-does-not-start-after-upgrading-to-mac-os-x-sierra-how-can-i-fix-this-issue"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/performance">Performance</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select <strong>Options</strong> &gt; <strong>Look and Feel</strong> &gt; <strong>Metal</strong>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/the-menu-fonts-are-corrupted-when-magicdraw-is-in-japanese-mode"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Sometimes when running the program the StackOverflowError occurs.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>If you are running the Sun's JVM, set the following java properties in your mduml.properties<sup>*</sup> file: to the line JAVA_ARGS=-Xmx600M, append the string -Xss[stack size]</p><p>For example:</p><p>JAVA_ARGS=-Xmx600M -Xss2M</p><p>This sets java stack size to 2 megabytes.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/sometimes-when-running-the-program-the-stackoverflowerror-occurs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Sometimes when running the program the OutOfMemory error occurs.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>If you are running the Sun's JVM, set the following java properties in your mduml.properties<sup>*</sup> file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.</p><p>For example:</p><p>JAVA_ARGS=-Xmx800M</p><p>This sets java heap size to 800 megabytes.</p><p>If you get exception &quot;java.lang.OutOfMemoryError: PermGen space&quot; please, check if PermSize is specified in mduml.properties<sup>*</sup> file.</p><p>The JAVA_ARGS line should look like:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M</p><p>If PermSize is specified in mduml.properties<sup>*</sup> file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.</p><p>For example:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/sometimes-when-running-the-program-the-outofmemory-error-occurs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/when-i-attempt-to-open-certain-file-dialog-boxes-it-takes-several-minutes-for-the-file-dialog-to-open"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Using a nvidia 8240 agp adapter in dual monitor mode any part of the display past the first 1/3 of the second monitor does not display correctly. Using ASUS nvidia 8240 delux latest driver. Also tried the nvidia latest driver with the same result.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Try to start MagicDraw without direct draw, and edit JAVA_ARGS the line in the MagicDrawUML/bin/mduml.properties<sup>*</sup> file by adding -Dsun.java2d.noddraw=true.</p><p>The line should look like: JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M -Dsun.java2d.noddraw=true.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/using-a-nvidia-8240-agp-adapter-in-dual-monitor-mode-any-part-of-the-display-past-the-first-1-3-of-the-second-monitor-does-not-display-correctly-using-asus-nvidia-8240-delux-latest-driver-also-tried-the-nvidia-latest-driver-with-the-same-result"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw is unstable and slow when running on Java SE 8 Update 60. How do I solve this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a <a href="http://bugs.java.com/view_bug.do?bug_id=8061636">known</a> Java bug. This issue will be fixed in MagicDraw 18.3, but in the meantime you can upgrade to the <a href="https://docs.nomagic.com/support/jvm-list.html">recommended Java version</a>.<br /> <br /> After installation, open <em>&lt;MagicDraw installation directory&gt;\\bin</em>, and modify the <em>magicdraw.properties</em>* file.<br /> <br /> Change line <em>JAVA_HOME=</em> to correspond with the Java version you\'ve installed.<br /> <br /> * If you are using MagicDraw 17.0.4 or earlier, the properties file is called <em>mduml.properties</em>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/magicdraw-is-unstable-and-slow-when-running-on-java-se-8-update-how-to-solve"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw is unstable and slow when running on Java SE 8 Update 101/102. How do I solve this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a known Java bug. This issue is fixed in MagicDraw 18.4. If you are using MagicDraw 18.3 and earlier versions, you can use <a href="https://docs.nomagic.com/component/content/article/jvm-list?Itemid=153">the recommended Java version</a>that comes with installation.</p><p>Once you have installed the recommended Java version, do the following:</p><ol><li>Open the bin folder <em>&lt;MD install directory&gt;\bin</em>.</li><li>Open the file <em>magicdraw.properties</em>.</li><li>Look for the line <em>&quot;JAVA_HOME=&quot;</em> and change the Java version with the one you have installed.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/magicdraw-unstable-and-slow-when-running-on-java-se-8-update-101-102-how-do-i-solve-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw freezes. Do you know how to fix that? </a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, &quot;MD log file&quot; tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/magicdraw-freezes-do-you-know-how-to-fix-that"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.</p><p>In order to analyze and fix the issue, more information is required. Please provide us with the following information:</p><ol><li>Can you reproduce the problem? If yes, what are the steps to reproduce it?</li><li>If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.</li><li>Send us the memory dump file. It may help to detect the problem.</li></ol><p>To create a memory dump file, please do the following:</p><ol><li>In the properties<sup>*</sup> file, append JAVA_ARGS parameters as follows:<br /> -XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots</li><li>Start your modeling tool.</li></ol><p>The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.</p><hr /><p>*</p><ul><li>For MagicDraw, the properties file is<em> magcdraw.properties</em> (<em>mduml.properties</em> for MagicDraw version 17.0.4 or earlier).</li><li>For Cameo Enterprise Architecture, the properties files is <em>cameoea.properties</em>.</li><li>For Cameo Systems Modeleer, the properties files is <em>csm.properties</em>.</li><li>For Cameo Business Modeler, the properties file is <em>csm.properties</em>.</li></ul></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/from-time-to-time-we-receive-out-of-memory-exceptions-i-suspect-that-these-exceptions-are-caused-by-magicdraw-memory-leaks-how-would-you-suggest-solving-this-problem"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What are the common recommendations to increase performance?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase an efficiency of modeling, we suggest the following solutions:</p><ul><li>Increase a java heap size.</li><li>Do not keep unused diagrams open. Open project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.</li><li>Increase an active validation period. MagicDraw takes less memory with increased active validations period.</li><li>Split the project to read only modules. Keep read only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.</li><li>Use Garbage Collector to free unused memory.</li><li>Turn of antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.</li></ul><p>For more information see &quot;MagicDraw User Manual&quot; &gt; &quot;Performance Improvement&quot; section. Manual is available in &lt; MagicDraw installation directory &gt; \manual\</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/what-are-the-common-recommendations-to-increase-performance"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I suspect a performance problem. How do I solve it?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:</p><p><strong>Generating a log file when the modeling tool freezes or performs slowly:</strong></p><p>1. When a modeling tool runs slowly or freezes, open<em> &lt;modeling tool installation directory&gt;\bin,</em> and run <em>submit_issue.exe</em> several times. It dumps threads into the log file.</p><p>2. Click <strong>Help</strong> &gt; <strong>About</strong> on the main menu of your modeling tool. In the open dialog, select the <strong>Environment</strong> tab and click the <strong>Log File</strong> link. The log file opens.<a href="#path">*</a></p><p>3. Save the file and register an issue. Click <strong>Help</strong> &gt;<strong> Report an Issue</strong> on the main menu of your modeling tool or go to <a href="http://www.nomagic.com/support.html">http://www.nomagic.com/support.html</a><a href="https://docs.nomagic.com/support.html">.</a></p><p>*If a modeling tool is inactive, as of version 17.0.4, log file is stored in the following location:</p><ul><li>Windows Vista/7/8 <em>C:\Users\&lt;USERNAME&gt;\AppData\Local\.magicdraw\&lt;md.version.number&gt;</em></li><li>Windows 2000/XP <em>C:\Documents and Settings\&lt;USERNAME&gt;\Local Settings\Application Data\.magicdraw\&lt;md.version.number&gt;</em></li><li>Windows NT4 <em>C:\WINNT\Profiles\&lt;USERNAME&gt;\Local Settings\Application Data\.magicdraw\&lt;md.version.number&gt;</em></li><li>Other OS: <em>&lt;user.home&gt;/.magicdraw/&lt;md.version.number&gt;</em></li></ul><p><strong>By using Java VisualVM:</strong></p><p>The modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.</p><p>The following steps outline how to obtain the data from VisualVM:</p><p><strong>Note. </strong>Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.</p><p><strong>On Windows OS:</strong></p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/">https://visualvm.github.io/</a><a href="https://visualvm.github.io/" title="Follow link" class="external-link">.</a></li><li>Start <strong>Task Manager</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDK installation process, VisualVM is located in <em>C:\Program Files\Java\jdk&lt;version number&gt;\bin\ jvisualvm.exe</em>. Otherwise, start the <em>exe</em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Task Manager</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Task Manager</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details, including the email address where the ticket link will be sent, and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team. For more information about reporting an issue, please visit <a href="http://www.nomagic.com/support.html">http://www.nomagic.com/support.html</a><a href="http://www.nomagic.com/support.html">.</a></li></ol><p><strong>On Mac OS:</strong></p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/">https://visualvm.github.io/</a><a href="https://visualvm.github.io/" class="external-link" title="Follow link">.</a></li><li>Start <strong>Activity Monitor</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDk installation process, VisualVM is located in <em>/Library/Java/JavaVirtualMachines/jdk&lt;version number&gt;.jdk /Contents/Home/bin/jvisualvm</em>. Otherwise, start <em><strong>jvisualvm</strong></em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Activity Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Activity Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished and click the Stop button.</li><li>In the CPU <strong>samples</strong> tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.</li><li>To save the snapshot, right-click it and select Save As to save the <em>*.nps</em> file.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details including the email address where the ticket link will be sent and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team. For more information about reporting an issue, please visit <a href="http://www.nomagic.com/support.html">http://www.nomagic.com/support.html</a><a href="http://www.nomagic.com/support.html">.</a></li></ol><p><strong>On Linux OS:</strong></p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/">https://visualvm.github.io/</a><a title="Follow link" href="https://visualvm.github.io/" class="external-link">.</a></li><li>Start <strong>System Monitor</strong>.</li><li>To start <strong>Java VisualVM</strong>, execute the <strong>jvisualvm</strong> tool from the <strong>bin</strong> directory of the JDK. When the tool runs, the <strong>Java VisualVM</strong> window opens.</li><li>Start the modeling tool.</li><li>In <strong>System Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>System Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details including the email address where the ticket link will be sent and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team. For more information about reporting an issue, please visit <a href="http://www.nomagic.com/support.html">http://www.nomagic.com/support.html</a><a href="http://www.nomagic.com/support.html">.</a></li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/i-suspect-a-performance-problem-how-could-i-solve-it"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">After loading a project, there wasn’t a big memory usage but after some actions it increased dramatically. How could I manage it?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In order to troubleshoot this issue, we will need the program’s log files (located in the install directory of your tool). Additional information might be required about the Java environment on which our modeling tools are based. The information we need is called the “heapdump” and can be obtained using the Java VisualVM program.</p><p>Please read and follow this procedure to install Java VisualVM and send this data to us (while the tool is running):</p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/">https://visualvm.github.io/</a><a class="external-link" href="https://visualvm.github.io/" title="Follow link">, if you do not have it.</a></li><li>Start Task Manager or other appropriate tool depending on your OS.</li><li>Start Java VisualVM. If you have selected the default location on the JDK installation process, VisualVm is located in C:\Program Files\Java\jdk&lt;version number&gt;\bin\ jvisualvm.exe. Otherwise start the jvisualvm.exe from your custom location.</li><li>In the Task Manager or other program according to you OS, find the PID (Process Identifier) of your modeling tool.</li><li>In the Java VisualVM, find Java process by the modeling tool PID and double click to open it.</li><li>Right click the Java process and, from the shortcut menu, select <strong>Heap Dump</strong>. The heapdump file creates under your process.</li><li>Save the heapdump file. Right click the heapdump and, on the shortcut menu, click <strong>Save As</strong>.</li><li>Register an issue and sent the saved *.hprof file for the investigation. For this, on the main menu of your modeling tool, click <strong>Help</strong> &gt; <strong>Report an Issue</strong> or go to <a href="http://www.nomagic.com/support.html">http://www.nomagic.com/support.html</a><a href="https://docs.nomagic.com/support.html">.</a></li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/after-loading-a-project,-there-wasn’t-a-big-memory-usage-but-after-some-actions-it-increased-dramatically-how-could-i-manage-it"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I find log files of a modeling tool, Cameo Collaborator and Teamwork Cloud?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.</p><p><strong>Accessing log files</strong></p><ul><li><strong>For a modeling tool</strong></li></ul><p>Open your modeling tool and in the main menu go to <strong>Help</strong> &gt; <strong>About &lt;modeling tool name&gt;</strong>. In the <strong>Environment</strong> tab, click the link provided in the <strong>Log File</strong> line to open a log file.</p><ul><li><strong>For Cameo Collaborator</strong></li></ul><p>Go to Alfresco Community installation directory, and obtain the <em>alfresco.log</em>, <em>share.log</em> and <em>solr.log</em> files.</p><p>Go to <em>&lt;Alfresco Community installation directory&gt;\tomcat\logs</em>, and obtain the <em>alfrescotomcat-stderr.log</em>, <em>alfrescotomcat-stdout.log</em> and <em>catalina.log</em> files.</p><ul><li><strong>For Teamwork Cloud</strong></li></ul><p>Go to <em>&lt;user home directory&gt;\.twcloud\&lt;server version&gt;</em>, and obtain the <em>server.log</em> and <em>client.log</em> files.</p><p>Go to <em>&lt;Cassandra installation directory&gt;\logs</em> on Windows OS or <em>/var/lib/Cassandra</em> on Linux, and obtain the Cassandra log file.</p><p><strong>Generating a log file</strong></p><p>If the performance of your modeling tool declines or it freezes, go to <em>&lt;modeling tool installation directory&gt;\bin</em>, and run the <em>submit_issue.exe</em> file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file, as described above.</p><p><strong>Java crash log files</strong></p><p>If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the <em>&lt;modeling tool installation directory&gt;/bin</em> or <em>&lt;modeling tool installation directory&gt;</em> directory. The names of these log files start with &quot;hs_err&quot;, e.g., <em>hs_err_pid15693.log</em>. If you find the Java crash log file, the reason your modeling tool crashed was that Java crashed.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/performance/where-can-i-find-log-files-of-a-modeling-tool,-cameo-collaborator-and-teamwork-cloud"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/installation-and-running">Installation and Running</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to install MagicDraw in a silent mode, i.e., without the installer GUI?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please start the installer with the following parameters:<br /> -i silent -DUSER_INSTALL_DIR=</p><p>The example:</p><p>MD_UML_169_win.exe -i silent &quot;-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9&quot;<br /> MagicDraw will be installed silently, with a default configuration.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/how-to-install-magicdraw-in-a-silent-mode-i-e-without-the-installer-gui"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What is the best way to reinstall MagicDraw on new computer or the same one after formatting.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Reinstall product on new computer:</p><ol><li><a href="https://docs.nomagic.com/support/activation.html#deactivation_in_aplication">Deactivate the current license</a>.</li><li>Download and install the fresh installation on new machine.</li><li>Start it after the installation is finished.</li><li>The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.</li><li>Uninstall the product from old machine.</li><li>You will be requested to activate the license and receive the commercial license dedicated for the particular machine.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/what-is-the-best-way-to-reinstall-magicdraw-on-new-computer-or-the-same-one-after-formatting"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw does not start on Mac OS after QuickTime 7.2 update</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a known issue in Intel based Mac OS with QuickTime 7.2 update that causes most of the Power PC applications to refuse to start. This problem hounts some Java apps too, and sometimes MagicDraw refuses to start from the icon created by the installer. Although it is possible to start MagicDraw from command line (look for classpath and JVM flags from Indo.plit file).</p><p>There is available one solution that fixes the Power PC apps and also the MagicDraw from here: <a href="http://mactip.blogspot.com/2007/07/dependent-dylib-is-not-prebound.html">http://mactip.blogspot.com/2007/07/dependent-dylib-is-not-prebound.html</a></p><p>The fix involves some command-line and text editor usage, but it's relatively simple and it works.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/magicdraw-does-not-start-on-mac-os-after-quicktime-7-2-update"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I installed MagicDraw and it ran. Worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This problem is Install Anywhere related and appears when you uninstall previous version of MagicDraw and then, without restarting your computer, install another MagicDraw in the same directory. We would suggest to uninstall MagicDraw, restart your computer, and then install MagicDraw again.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/i-installed-magicdraw-and-it-ran-worked-fine-i-shut-down-my-machine-started-today-and-magicdraw-won-t-start"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">On the Macintosh, MagicDraw points out error at startup: java.lang.NullPointerException</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>On the Macintosh, MagicDraw points out error at startup:</p><p><strong>java.lang.NullPointerException</strong><br /> <strong>at sun.java2d.SunGraphicsEnvironment.getAvailableFontFamilyNames(SunGraphic sEnvironment.java:327)</strong><br /> <strong>at sun.java2d.SunGraphicsEnvironment.getAvailableFontFamilyNames(SunGraphic sEnvironment.java:359)</strong><br /> <strong>at com.nomagic.actions.SetFontFaceAction.(SetFontFaceAction.java)</strong><br /> <strong>at com.nomagic.actions.SetFontAction.(SetFontAction.java)</strong></p><p>...</p><p>Based on messages from the Apple java-dev mailing archive, a lot of people who use Java 1.4.1 on Mac have experienced similar problems. Someone suggested this had to do with bitmap fonts in a Classic install in &quot;/System Folder/Fonts&quot;. And it seems that renaming &quot;/System Folder/Fonts/&quot; to &quot;/System Folder/Fonts.not/&quot; or something else and rebooting your machine can solve the problem.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/on-the-macintosh-magicdraw-points-out-error-at-startup-java-lang-nullpointerexception"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can save configuration files in the modeling tool installation directory or on your chosen directory.</p><p>To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties<sup>*</sup> (this file is in<em> \bin</em>):<br /> JAVA_ARGS=-Dlocalconfig=false</p><p><strong>NOTE</strong>: For Windows users. If you are using MagicDraw 17.0.4 or later, you must also add argument <br /> -DWINCONFIG\=false.</p><p>To store configuration files to your chosen location</p><ol><li>In the /.<em>&lt;modeling tool name&gt;</em>/ folder, create file named <em> &lt;modeling tool properties file name&gt; redirect</em>, that is <em>magicdrawredirect</em>, <em>cameoearedirect</em>, <em>csmredirect</em>, or <em>cbmredirect</em>.</li><li>In the created file, type absolute (for example, <em>C:\users\john\Documents</em>) or relative (relative to modeling tool installation directory, for example, <em>..\configurations</em>) path where configuration and auxiliary files will be saved.</li></ol><p>Or:</p><ol><li>Open the *.properties<sup>*</sup> file, which is located in <em>\bin</em>.</li><li>Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location=<em>&lt;absolute path to a custom location&gt;</em></li></ol><p>For example, <em>-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData</em></p><p><strong>NOTE:</strong> If there is defined to store files in installation directory (see the section &quot;To store MagicDraw configuration files in MagicDraw installation directory&quot; above), files will not be stored to your chosen location.<br /> <br /> <br /> * For more information about configuration files please, see <a href="https://docs.nomagic.com/display/MD185/Configuration+files">Configuration files</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/in-our-company-the-storage-of-user-home-directory-is-limited-how-to-force-to-keep-configuration-files-in-other-directory"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">After the download the installer cannot be launched or it just appears on the screen and vanishes</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please check if the file is not truncated. You can see the exact file size at the download page.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/after-the-download-the-installer-cannot-be-launched-or-it-just-appears-on-the-screen-and-vanishes"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I ran into a trouble when installing MagicDraw: Launching installer... Exception in thread &quot;main&quot; java.lang.NoClassDefFoundError: com/zerog/lax/LAX</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In most cases such error appears when installer file is truncated or corrupted.</p><p>Please try to download an installer again.</p><p>Another option is that /usr/bin/java is an old version java. To check which java is used by installer, set environment variable LAX_DEBUG and launch installation again.</p><p>By default installer first uses java found in /usr/bin. But there is possibility to use specific VM when launching the installer. Please add parameter LAX_VM to launcher and second parameter path to java executable, here is an example (assuming that java is in /opt/j2sdk1.5.0_03):</p><p>./MD_UML_105_unix.sh LAX_VM /opt/j2sdk1.5.0_03/bin/java</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/i-ran-into-a-trouble-when-installing-magicdraw-launching-installer-exception-in-thread-main-java-lang-noclassdeffounderror-com-zerog-lax-lax"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to run MagicDraw under Unix after installation?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Run mduml<sup>*</sup> file, which is located in MagicDraw installation directory, bin folder.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/how-to-run-magicdraw-under-unix-after-installation"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Update of JAVA 1.6.0.13 for Mac OS causes the disappearing menu.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>We have found that update of JAVA 1.6.0.13 for Mac OS triggers the problem with disappearing MagicDraw menu. This issue is fixed in 16.5 SP3. Also we suggest two workarounds:</p><ol><li>You need to define older JAVA version in mduml.properties<sup>*</sup> ( /bin/ ) file and work with that JAVA version (for example version 1.5.0 or previous 1.6.0).</li><li>You need to change Look &amp; Feel style by editing global.opt file. Note: This problem does not exist on Metal Look &amp; Feel.</li></ol><p>Steps how to do that:</p><ul><li>Shutdown MagicDraw application;</li><li>Go to ./magicdraw/ /data/;</li><li>Open global.opt file with text editor;</li><li>Find LOOK_AND_FEEL_CLASS propertyID.</li><li>Replace tag apple.laf.AquaLookAndFeel with new one:<br /> javax.swing.plaf.metal.MetalLookAndFeel</li><li>Save file;</li><li>Start MagicDraw application.</li></ul><p><br /> <sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/update-of-java-1-6-0-13-for-mac-os-causes-the-disappearing-menu"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When I saving project after I have upgraded Magicdraw to v16.6 I get a save error.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Save error appears saving project with modules when MagicDraw v16.6 is installed on top of MagicDraw v15.0 or earlier (using autoupdate functionality). This problem occurs because one or more old resource descriptors from MagicDraw v15.0 or earlier are corrupted.</p><p>To prevent MagicDraw project save error you need to install MagicDraw v16.6 to a new location – to a new and empty folder, for example, &quot;MagicDraw 16.6&quot;. Note that on the first MagicDraw startut you can import MagicDraw environment options from previous MagicDraw installations.</p><p>You may download MagicDraw 16.6 from your personal or company profile on www.nomagic.com, also to obtain unlock keys.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-i-saving-project-after-i-have-upgraded-magicdraw-to-v16-6-i-get-a-save-error"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is it possible to create a MagicDraw installation package with a set of some default options?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>First of all you need to pre-configure MagicDraw. Do the following:</p><ol><li>Check if you have the permission to write to the MagicDraw installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.</li><li>In <em>magicdraw.properties</em>, which is in <em>\bin</em>, set the parameter value:<br /> JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false</li><li>Run MagicDraw and set desired options, then close the program.</li><li>Reopen magicdraw.properties and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.</li><li>Copy the MagicDraw installation folder and paste it on a new machine.</li></ol><p>Let us explain the difference between changed parameter values:</p><p>a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in<em> \.magicdraw\</em> . Options are loaded in the following order:</p><ol><li>From <em>&lt;Common Application Data location&gt;\.magicdraw\</em></li><li>From the MagicDraw installation folder</li></ol><p>b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the MagicDraw installation folder and are loaded from there.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/is-it-possible-to-create-a-magicdraw-installation-package-with-a-set-of-some-default-options"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have installed and activated MagicDraw v16.9 as the administrator. When I had logged into my regular account, MagicDraw asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.</p><p>The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.</p><p>You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).</p><p>For the instructions on how to change the configuration files directory, please find the issue &quot;In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?&quot;</p><p>Note: It is important to know that the MagicDraw seat license can be used by a single user only.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/i-have-installed-and-activated-magicdraw-v16-9-as-the-administrator-when-i-had-logged-into-my-regular-account-magicdraw-asked-for-a-license-key-file-and-for-the-license-activation-again-how-can-i-escape-the-license-activation-on-the-same-machine-twice"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">After installing MagicDraw on the Mac OS with Java (1.6.0_17), default Look &amp; Feel does not function and the Mac menu bar is gone.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In order to fix the problem with the menu bar after java update on the Mac OS, you need to open /.magicdraw/16.6/data/global.opt and change the string &quot;com.apple.laf.AquaLookAndFeel&quot; to &quot;apple.laf.AquaLookAndFeel&quot;.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/after-installing-magicdraw-on-the-mac-os-with-java-1-6-0-17-default-look-feel-does-not-function-and-the-mac-menu-bar-is-gone"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">After updating MagicDraw to version 17.0.1 exceptions can be shown on different actions.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>After updating MagicDraw to version 17.0.1 exceptions can be shown on different actions. The exception stack trace may look like :</p><p><strong>java.lang.RuntimeException: java.lang.reflect.InvocationTargetException</strong><br /> <strong>at com.nomagic.utils.Utilities.invokeAndWaitOnDispatcher(Utilities.java:1578)</strong><br /> <strong>at com.nomagic.magicdraw.core.project.ProjectsManager.setActiveProject(ProjectsMana ger.java:315)</strong><br /> <strong>...</strong></p><p>OR</p><p><strong>java.lang.AbstractMethodError</strong><br /> <strong>at com.nomagic.magicdraw.core.project.ProjectsManager.fireProjectPreActivated(Proje ctsManager.java:1352)</strong><br /> <strong>at com.nomagic.magicdraw.core.project.ProjectsManager$2.run(ProjectsManager.java:26 9)</strong><br /> <strong>at com.nomagic.utils.Utilities.invokeAndWaitOnDispatcher(Utilities.java:1562)</strong><br /> <strong>...</strong></p><p>You are using incompatible plugin e.g. Cameo Simulation Toolkit 1.1, Cameo Data Modeler 16.8, EstimIX, ExtendIX, or other. Those plugin versions are not compatible with MagicDraw 17.0.1.</p><p>Please update or remove incompatible plugins from Help &gt; Resource/Plugin Manager &gt; Click the button &quot;Check For Updates&quot; &gt; and download compatible version OR remove incompatible plugin from the MagicDraw.</p><p><a href="https://docs.nomagic.com/support/compatibility">Plugins compatibility can be checked here</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/after-updating-magicdraw-to-version-17-0-1-exceptions-can-be-shown-on-different-actions"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">There is no Implementation toolbar on the Implementation diagram pallet in MagicDraw 17.0 SP1</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To see the pallet, you need to upgrade your MagicDraw to a new version of 17.0 SP1.</p><p>To upgrade MagicDraw to the new version of 17.0 SP1:</p><ol><li>On the main menu, click <strong>Help &gt; Check For Updates</strong>.</li><li>Click <strong>Apply Patch</strong>.</li><li>Restart MagicDraw.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/there-is-no-implementation-toolbar-on-the-implementation-diagram-pallet-in-magicdraw-17-0-sp1"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When Resource/Plugin Manager is started error is shown.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When Resource/Plugin Manager is started error is shown:</p><p><strong>java.lang.NullPointerException</strong><br /> <strong>at com.nomagic.magicdraw.resourcemanager.sb.b(sb.java:247)</strong><br /> <strong>at com.nomagic.magicdraw.resourcemanager.sb.j(sb.java:223)</strong><br /> <strong>at com.nomagic.magicdraw.resourcemanager.sb.e(sb.java:84)</strong></p><p><strong>MagicDraw up to version 17.0.1 SP1 with Java version 1.7 is used.</strong></p><p>This issue is 1.7 Java specific.</p><p>We highly recommend to use the bundled Java, which comes with MagicDraw installation (select to use the bundle Java in third MagicDraw installer step).</p><p>Java can be changed in mduml.properties<sup>*</sup> file in &quot;JAVA_HOME=&quot; line. mduml.properties<sup>*</sup> can be found in &quot;MagicDraw install dir&quot; / bin folder.</p><p>This issue is already fixed in v17.0.1 SP1<br /> <br /> <br /> <sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-resource-plugin-manager-is-started-error-is-shown"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">After upgrading Java to 1.6.0_26, MagicDraw becomes unpredictable.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The following issues appear:</p><ul><li>MagicDraw hangs on a splash screen.</li><li>Any model or diagram cannot be opened.</li><li>Any diagram or element cannot be created.</li><li>In the md.log file, the exception &quot;net.sf.ehcache.CacheException&quot; appears.</li></ul><p><strong>What should I do?</strong></p><p>To start MagicDraw normally, perform the following steps:</p><ul><li>Update MagicDraw into 17.0 SP3 or</li><li>Delete all cache folders from user home directory &gt; /.magicdraw/ version &gt; / and restart MagicDraw.</li></ul><p>Note: Upgrading the Mac OS X to 10.6.5, upgrades Java to version 1.6.0_26 automatically.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/after-upgrading-java-to-1-6-0-26-magicdraw-becomes-unpredictable"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to update MagicDraw to new version?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You may find all the information about updating to new version at <a href="https://docs.nomagic.com/display/NMDOC/Updating+modeling+tools+and+plugins">Updating modeling tools and plugins</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/how-to-update-magicdraw-to-new-version"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When I run the exe file I get a warning: Please select another location to extract the installer to:</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This error occurs when you have a corrupted installer file. Please download the file and install again.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-i-run-the-exe-file-i-get-a-warning-please-select-another-location-to-extract-the-installer-to"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to MagicDraw installation directory or &quot;failed to copy resource directory&quot;. How can this be handled?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.</p><p>To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following:<br /> 1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.<br /> 2. From the <strong>System Configuration</strong> dialog, click the <strong>Tools</strong> tab.<br /> 3. Select the <strong>Change UAC Settings</strong> tool and click <strong>Launch</strong> button.<br /> 4. Move the slider to the highest value to set <strong>Always notify</strong> and click <strong>OK</strong>.<br /> 5. Restart the computer to apply changes.</p><p>To enable UAC on Windows Vista OS, do the following:<br /> 1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.<br /> 2. From the<strong> System Configuration </strong>dialog, click the <strong>Tools</strong> tab.<br /> 3. Select the <strong>Enable UAC</strong> tool and click <strong>Launch</strong> button. The <strong>CMD</strong> window opens.<br /> 4. When the command is completed, you can close <strong>CMD</strong> window.<br /> 5. Restart the computer to apply changes.</p><p>To run MagicDraw as administrator, right-click the MagicDraw icon and choose <strong>Run as Administrator</strong>.</p><p>To run MagicDraw as an administrator all the time, do the following:<br /> 1. Right-click the MagicDraw icon and choose <strong>Properties</strong>.<br /> 2. Click the <strong>Compatibility</strong> tab.<br /> 3. In the <strong>Privilege Level</strong> area, select <strong>Run this program as an administrator</strong>.<br /> 4. Click <strong>OK</strong>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-trying-to-install-or-import-a-plugin-to-magicdraw-the-error-appears-saying-that-you-do-not-have-rights-to-write-to-magicdraw-installation-directory"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When trying to launch MagicDraw on OS X Mountain Lion, the error appears: &quot;MagicDraw.app&quot; is damaged and can't be opened. You should move it to the Trash.&quot;</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please note that downloaded installs are not corrupted or damaged and this problem is not related to the MagicDraw application. This issue is related to the new OS X Mountain Lion functionality, &quot;Gatekeeper.&quot;</p><p>The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.</p><p>In order to launch MagicDraw, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: <a href="http://support.apple.com/kb/HT5290">http://support.apple.com/kb/HT5290</a></p><p>Note: We are communicating with Apple to solve this issue so that our customers may execute MagicDraw without any problems.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-trying-to-launch-magicdraw-on-os-x-mountain-lion-the-error-appears-magicdraw-app-is-damaged-and-can-t-be-opened-you-should-move-it-to-the-trash"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I cannot start MagicDraw 17.0.4 on MAC OS X after it has been upgraded from version 17.0.3 SP1 by using the no-install package.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>We offer you to solve the problem in one of the following ways.</p><p><strong>Solution #1:</strong></p><ol><li>Remove MagicDraw.app from &lt;MagicDraw 17.0.3 SP1 installation directory&gt;.</li><li>Extract MagicDraw_1704_no_install_mac.zip to &lt;MagicDraw 17.0.3 SP1 installation directory&gt;. Select to overwrite all files, when you will be asked. A new MagicDraw.app file will appear in &lt;MagicDraw 17.0.3 SP1 installation directory&gt;.</li><li>Use the MagicDraw.app file to start the upgraded version of MagicDraw.</li></ol><p><strong>Solution #2:</strong></p><ol><li>Extract MagicDraw_1704_no_install_mac.zip to &lt;MagicDraw 17.0.3 SP1 installation directory&gt;. Select to overwrite all files, when you will be asked.</li><li>Copy the MagicDraw.app file and paste it in the same directory. The MagicDraw Copy.app file will appear in &lt;MagicDraw 17.0.3 SP1 installation directory&gt;.</li><li>Use the MagicDraw Copy.app file to start the upgraded version of MagicDraw.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/i-cannot-start-magicdraw-17-0-4-on-mac-os-x-after-it-has-been-upgraded-from-version-17-0-3-sp1-by-using-the-no-install-package"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw 17.0.4 can be started neither on Mac OS X Lion nor on Mac OS X Mountain Lion. JRELoadError appears when trying to start the application. How can this be handled?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The error appears because the MagicDraw.app file cannot find the installed Java 6.</p><p>To handle the problem, please use one of the following workarounds:</p><ul><li>Start MagicDraw using the mduml<sup>*</sup> file that can be found in &lt;MagicDraw installation folder&gt;/bin.</li><li>Install Java 6 in your computer and use the MagicDraw.app file to start MagicDraw 17.0.4.</li></ul><p>This issue will be fixed in MagicDraw 17.0.5.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/magicdraw-17-0-4-can-be-started-neither-on-mac-os-x-lion-nor-on-mac-os-x-mountain-lion-jreloaderror-appears-when-trying-to-start-the-application-how-can-this-be-handled"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw does not start after upgrading to OS X Yosemite. How can I fix this issue?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The problem is that MagicDraw earlier than 17.0.2 SP3 or 17.0.3 SP1 cannot be started on OS X Yosemite.<br /> To start MagicDraw on OS X Yosemite, you must upgrade the modeling tool at least to 17.0.2 SP3 or 17.0.3 SP1.<br /> <br /> If MagicDraw still does not start, you must upgrade Java on your computer. For recommended Java versions and links to downloads, please visit <a href="http://www.nomagic.com/support/jvm-list.html">http://www.nomagic.com/support/jvm-list.html</a><a href="https://docs.nomagic.com/support/jvm-list.html">.</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/magicdraw-does-not-start-after-upgrading-to-os-x-yosemite-how-can-i-fix-this-issue"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How do I turn on debug log mode?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To initialize <strong>log4j</strong>, open <em>&lt;MagicDraw installation directory&gt;/data</em>, and modify the <em>debug.properties</em> file.</p><p>Change the debug level for appropriate categories by specifying <em>log4j.category.&lt;category&gt;=DEBUG</em> or turn on debug for all categories <em>log4j.rootCategory=DEBUG,SO</em>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/how-do-i-turn-on-debug-log-mode"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Cache error occurred. How to handle it?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Close your modeling tool, delete all cache folders and start the program again.<br /> Cache folders can be found in <em>&lt;user home directory&gt;\.&lt;modeling tool&gt;\&lt;version number&gt;</em>, for example <em>&lt;userhome&gt;\.magicdraw\&lt;18.2&gt;</em>.</p><p>If the problem still exists, please add the <strong>-Dcom.sun.media.imageio.disableCodecLib=true</strong> option into the <strong>JAVA_ARGS</strong> line in the modeling tool properties file, for example <em>magicdraw.properties</em>. A properties file is in <em>&lt;modeling tool installation directory&gt;\bin</em>.</p><p>See the example:</p><p>JAVA_ARGS=-Xmx4000M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -DLOCALCONFIG\=true -splash\:data/splash.png -Dmd.class.path\=$java.class.path -Dcom.nomagic.osgi.config.dir\=configuration -Desi.system.config\=data/application.conf -Dlogback.configurationFile\=data/logback.xml -Xss1024K -Dcom.sun.media.imageio.disableCodecLib=true</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/cache-error-occurred-how-to-handle-it"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in <em>.zip/iso</em> files are not secure because of the dylib-hijacking problem.<br /> (Please find more about it at <a href="https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/">https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/</a><a href="https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/">).<br /> All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.</a></p><p>The solutions are:</p><ol><li>To run <em>magicdraw.sh</em> file from the <em>/bin</em> directory.</li><li>To download the original signed <em>MagicDraw.dmg</em> file and to install the application again.</li><li>To remove the program from quarantine.</li></ol><p>To remove the application from quarantine, please do:</p><ol><li>Open a terminal.</li><li>Using the terminal, open the MagicDraw installation directory.</li><li>Write the command: <em>xattr -d com.apple.quarantine MagicDraw.app/</em></li><li>Close the terminal and start MagicDraw using the <em>.app</em> file.</li></ol><p><strong>NOTE:</strong> This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/magicdraw-does-not-start-on-mac-os-x-sierra-from-a-no-install-file-using-the-app-file-what-is-a-solution-for-it"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have installed several versions of the modeling tool on Mac OS and the application can’t be opened using the .app file. How should I start a program?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please restart your computer. After multiple updates or after installing different versions of a modeling tool on the same machine with Mac OS, sometimes it happens for unknown reason.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/i-have-installed-several-versions-of-the-modeling-tool-on-mac-os-and-the-application-can’t-be-opened-using-the-app-file-how-should-i-start-a-program"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When I run MagicDraw 18.5 on Mac OS X 10.11 El Capitan in the native full screen mode, why do most dialogs appear behind previously open dialogs?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a known issue with Mac OS X 10.11 El Capitan operating system. Most dialogs in the application will be displayed behind previously open dialogs, affecting usability of the user interface. There is no solution to this problem. Please try to downgrade the Mac OS to some earlier version.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/when-i-run-magicdraw-18-5-on-mac-os-x-10-11-el-capitan-in-the-native-full-screen-mode,-why-do-most-dialogs-appear-behind-previously-open-dialogs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How do I start the License Server Manager on UNIX Platforms automatically?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Edit the appropriate boot script, which could be one of the following: <em>/etc/rc.boot, /etc/rc.local, /etc/rc2.d/Sxxx, </em>or<em> /sbin/ rc2.d/Sxxxx.</em></p><p>Then, include commands similar to the following:</p><p>/bin/su daniel -c 'echo starting lmgrd &gt; \<br /> /home/flexlm/v11/hp700_u9/boot.log'<br /> /bin/nohup /bin/su daniel -c 'umask 022; \<br /> /home/flexlm/v11/hp700_u9/lmgrd -c \<br /> /home/flexlm/v11/hp700_u9/license.dat &gt;&gt; \<br /> /home/flexlm/v11/hp700_u9/boot.log'<br /> /bin/su daniel -c 'echo sleep 5 &gt;&gt; \<br /> /home/flexlm/v11/hp700_u9/boot.log'<br /> /bin/sleep 5<br /> /bin/su daniel -c 'echo lmdiag &gt;&gt;\<br /> /home/flexlm/v11/hp700_u9/boot.log'<br /> /bin/su daniel -c '/home/flexlm/v11/hp700_u9/lmdiag -n -c\<br /> /home/flexlm/v11/hp700_u9/license.dat &gt;&gt; \<br /> /home/flexlm/v11/hp700_u9/boot.log'<br /> /bin/su daniel -c 'echo exiting &gt;&gt;\<br /> /home/flexlm/v11/hp700_u9/boot.log'</p><p>Please note that this does not start the vendor daemon until you reboot the system.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/installation-and-running/how-do-i-start-the-license-server-manager-on-unix-platforms-automatically"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm">Java Virtual Machine (JVM)</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw 17.0.5 stops responding on Mac OS X Mavericks, and I keep seeing the spinning wait pointer (aka Spinning Beach Ball of Death). How can I fix the issue?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw stops responding due to an issue detected in Java SE 7 Update 40, which is bundled with MagicDraw 17.0.5 (for the issue details, go to <a href="https://bugs.openjdk.java.net/browse/JDK-8025588">https://bugs.openjdk.java.net/browse/JDK-8025588</a><a href="https://bugs.openjdk.java.net/browse/JDK-8025588">).</a></p><p>This issue will be fixed in <strong>MagicDraw 17.0.5 SP1</strong>, coming out in the middle of February.</p><p>To solve the issue manually (without the SP), switch the version of the bundled Java to SE 7 Update 25*, which does not cause the issue. For this, do the following:</p><ol><li>Open the <em>magicdraw.properties</em> file, stored in &lt;MagicDraw installation directory&gt;/bin.</li><li>Find the JAVA_HOME property and add the path to the location of Java SE 7 Update 25 on your PC. For example, “JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home”.</li></ol><p>Please contact our customer support, if this does not help.</p><p>--<br /> * If you do not have Java SE 7 Update 25 installed on your PC, download the installer from the <a href="http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html#jdk-7u25-oth-JPR">Java SE 7 Downloads</a> page. You need the<em> jdk-7u25-macosx-x64.dmg</em>file.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/magicdraw-17-0-5-stops-responding-on-mac-os-x-mavericks-and-i-keep-seeing-the-spinning-wait-pointer-aka-spinning-beach-ball-of-death-how-can-i-fix-the-issue"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I start MagicDraw v16.9 and later on Mac PowerPC?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw needs Java to be supported. Java 1.6 is available on the 64-bit Intel-based Macs only. Non-Intel-based PowerPC does not support Java 1.6 and later.</p><p>The latest MagicDraw version which can support Java 1.5 is MagicDraw v16.6.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/how-can-i-start-magicdraw-v16-9-and-later-on-mac-powerpc"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I want to check which JVM is used for installation under Linux.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can watch installation process by setting environment variable LAX_DEBUG to value 1 before starting installation.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/i-want-to-check-which-jvm-is-used-for-installation-under-linux"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">There are problems when using JVM 1.6 with MagicDraw v14.0 and previous.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The problems are usually related with opening/creating projects. The recommendation is to use JVM 1.5 for MagicDraw v14.0 and previous.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/there-are-problems-when-using-jvm-1-6-with-magicdraw-v14-0-and-previous"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How do I know what version of JVM I am running?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You may find this information in the About window (Help menu -&gt; About)</p><p>or</p><p>If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/how-do-i-know-what-version-of-jvm-i-am-running"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to change JVM version?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><ol><li>Go to <em>&lt;modeling tool installation directory&gt;\bin</em> and open the <em>&lt;modeling tool&gt;.properties</em> file (eg., <em>magicdraw.properties</em>, <em>csm.properties</em>, <em>cameoea.properties</em>) for editing. If you are using MagicDraw 17.0.4 or earlier, the name of the property file is <em>mduml.properties</em>.</li><li>In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144</li></ol><p>NOTE: Integrated MagicDraw runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that MagicDraw integrates with. If you are running MagicDraw integrated with IDE, read the appropriate readme.html for specific integration, found in the <em>integrations</em> folder.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/how-to-change-jvm-version"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to install Java 1.5 on Mac OS X 10.6 Snow Leopard?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In order to install Java 1.5 on Mac OS X 10.6 Snow Leopard, please follow these steps.</p><p>Execute the following commands in the terminal:</p><p>1. Get the java 5 that was included in 10.5 &quot;leopard&quot; and unpack:</p><p>cd /tmp/</p><p>curl -o java.1.5.0-leopard.tar.gz</p><p><a href="http://www.cs.washington.edu/homes/isdal/snow_leopard_workarou">http://www.cs.washington.edu/homes/isdal/snow_leopard_workarou</a><a href="http://www.cs.washington.edu/homes/isdal/snow_leopard_workaround/java.1.5.0-leopard.tar.gz"> nd/java.1.5.0-leopard.tar.gz.</a></p><p>tar -xvzf java.1.5.0-leopard.tar.gz</p><p>2. Move it to your System java folder (password needed):</p><p>sudo mv 1.5.0 /System/Library/Frameworks/JavaVM.framework/Versions/1.5.0-leopard</p><p>3. Tell OS X that java 5 actually is java 5:</p><p>cd /System/Library/Frameworks/JavaVM.framework/Versions/</p><p>sudo rm 1.5.0</p><p>sudo ln -s 1.5.0-leopard 1.5.0</p><p>sudo rm 1.5</p><p>sudo ln -s 1.5.0 1.5</p><p>After these commands, Java 1.5 will be installed. You can check Java 1.5 on Java Preferences dialog (open &quot;/Applications/Utilities/Java Preferences.app&quot;)</p><p>Change the properties to use Java 1.5 32-bit on MagicDraw. Open file &quot;mduml.properties&quot;<sup>*</sup>, which is located in /bin and change path in line JAVA_HOME=.</p><p>The line should look like:</p><p>JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/1.5/Home</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/how-to-install-java-1-5-on-mac-os-x-10-6-snow-leopard"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties<sup>*</sup> file, in the line:</p><p>JAVA_ARGS=-Xmx800M</p><p>The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.</p><p>On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.</p><p>More information about OutOfMemory problems you can find in readme.html by &quot;OutOfMemory problem&quot; paragraph. This file is located in &lt;MagicDraw installation directory&gt;.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/i-would-like-to-increase-java-heap-size-that-magicdraw-would-run-faster-with-larger-models-i-have-12-gb-of-ram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.</p><p>The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.</p><p>If you are using an <strong>earlier version than 18.4 SP1 </strong>and cannot start the modeling tool*, please do the following:</p><ol><li>Download the original signed <em>&lt;modeling tool*&gt;.dmg</em> file and install the application again.</li><li>In <em>bin\</em><em>magicdraw.properties<sup>**</sup></em>, set <em>JAVA_HOME</em> to the Java version installed in the <em>&lt;modeling_tool*_installation_directory &gt;\java</em> folder.</li></ol><p>Example: <em>JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre</em></p><ol><li>Run magicdraw.sh*** file from the /bin folder.</li></ol><hr /><p>*MagicDraw, Cameo EA, Cameo Systems Modeler</p><p>** cameoea.properties, csm.properties</p><p>***camocea.sh, csm.sh</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/java-virtual-machine-jvm/magicdraw-does-not-start-on-mac-os-x-after-a-java-version-upgrade-to-jdk-jre-9-java-9-when-using-a-no-install-file-or-running-an-application-from-a-bin-directory-how-do-i-solve-this"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/save-load-import-export">Save, Load, Import, Export</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to migrate existing projects to the new MagicDraw version?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You should copy all contents from old version projects folder to new version projects folder. If projects do not show up, copy the complete projects directory into the same location by creating all new projects and then importing the latest .xml.zip file.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/how-to-migrate-existing-projects-to-the-new-magicdraw-version"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I copy a diagram from one MagicDraw project into another one?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Use project import feature. After importing a project you will have to remove unnecessary elements by hand. If the imported project is very large, it will not be very convenient. Thus, large project should be divided into logical modules and only specific modules with needed diagrams should be imported.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/how-can-i-copy-a-diagram-from-one-magicdraw-project-into-another-one"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When I save a diagram to .emf image and try to insert this image file to my OpenOffice document I only get empty image.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Such problem really exists and will be fixed in future releases.</p><p>As a workaround we suggest to save your diagrams as SVG and then use free Inkscape editor (<a href="http://www.inkscape.org/">http://www.inkscape.org/</a>) to export diagrams as hi-res png.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/when-i-save-a-diagram-to-emf-image-and-try-to-insert-this-image-file-to-my-openoffice-document-i-only-get-empty-image"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">We are seeing the following error loading our model: Failed to load Windows configuration. Reseting to default.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is known problem. Your model and diagrams are ok, the only thing, which could not be restored, is layout of MagicDraw windows inside application. Such things can happen when project is saved and then loaded on computers which has different resolution or different windows management system.</p><p>Usually this error does not appear any more after save and load. If it still exists after save/load, please send us md.log file from the user home/.magicdraw directory (the info about where the MagicDraw configuration files are located, you may find in the About screen).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/we-are-seeing-the-following-error-loading-our-model-failed-to-load-windows-configuration-reseting-to-default"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When exporting image to EMF and pasting to Mac Word, error message &quot;Image is corrupted&quot; appears .</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a know problem of Mac Word. Still we don't know when it will be fixed.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/when-exporting-image-to-emf-and-pasting-to-mac-word-error-message-image-is-corrupted-appears"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Are there any recommendations for saving diagram as image?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>It is not recommended to use the following fonts for diagram saving as .eps, .emf, and .wmf:</p><p>Default, Dialog, DialogInput, Monospaced, SansSerif, and Serif.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/are-there-any-recommendations-for-saving-diagram-as-image"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I am trying to import an XMI 1.1 file with MagicDraw. I got a load error &quot;Wrong XMI version : MagicDraw supports only Unisys XMI 1.0&quot;</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Up to MagicDraw 10.0 version, XMI v1.0, v.1.1 and v1.2 load, save and import is supported.</p><p>Beginning with MagicDraw 10.0 XMI 2.1 is supported. And only model load from XMI 1.0 - 1.2.</p><p>But if you are trying to open an Unisys XMI 1.1 (XMI v1.1 with Unisys extensions), it is not supported by MagicDraw, only Unisys XMI 1.0 can be loaded.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/i-am-trying-to-import-an-xmi-1-1-file-with-magicdraw-i-got-a-load-error-wrong-xmi-version-magicdraw-supports-only-unisys-xmi-1-0"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I have saved the project file with MagicDraw version 17.0.1 and now I can't open it with MagicDraw version 17.0. Are project files backward compatible?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Project files saved with MagicDraw version 17.0.1 or later cannot be opened with MagicDraw version 17.0 or earlier. Moreover, as of version 17.0.1, the project file inner structure has been changed.</p><p>Usually, projects of all MagicDraw versions are not backward compatible.</p><p>Please note that once a project file is saved with v17.0.1 for the first time, the backup file of a project created with an earlier program version is created automatically. The backup file is stored in the same location as the project file. While saving the project created with program version earlier than 17.0.1, a warning about the file format incompatibility appears.</p><p>Warnings about the file format incompatibility also appear when MagicDraw is downloading or updates automatically.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/save-load-import-export/i-have-saved-the-project-file-with-magicdraw-version-17-0-1-and-now-i-can-t-open-it-with-magicdraw-version-17-0-are-project-files-backward-compatible"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/projects-migration-to-uml-2">Projects migration to UML 2</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What will happen with my old projects on MagicDraw Teamwork Server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>After opening teamwork projects with MagicDraw 10.0 version or later, they will be converted to UML2 data following the same instructions as for regular MagicDraw projects.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/projects-migration-to-uml-2/what-will-happen-with-my-old-projects-on-magicdraw-teamwork-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What XMI version supports MagicDraw?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw 10.0 version, XMI 2.1 standard for UML2 is supported.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/projects-migration-to-uml-2/what-xmi-version-supports-magicdraw"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Can I open older MagicDraw files?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>With MagicDraw 10.0 or later version you can open all projects, created with previous MagicDraw versions. After opening projects, created before MagicDraw 10.0 version, they will be converted to UML2.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/projects-migration-to-uml-2/can-i-open-older-magicdraw-files"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/uml-diagramming">UML/Diagramming</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can (inv:, def:, init:, derive:, pre:, post:, body: ) type constraints be modeled?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>All of the variants, defined in OCL 2.0 spec can be modeled (inv:, def:, init:, derive:, pre:, post:, body: ), but each is modeled in a slightly different way. Correspondingly, the header line in the OCL expression editor is generated according to model situation.*</p><p><strong>inv:</strong>* is easiest - any simple constraint having an OCL2.0 expression language is treated as invariant. They should have a field constrainedElement filled in, pointing to some class (constrainedElement=SomeClass). To be extra thorough in following the OCL spec, you should also apply the &lt;&lt;invariant&gt;&gt; stereotype on the constraint, but this is not necessary - it is implied.</p><p>Note that any other OCL constraints/expressions, that the handling code can not classify into the more specific categories (as defined below) are treated as inv: constraints.*</p><p><strong>def:</strong>* - definition constraints are modeled in the same way as invariant constraints, but the constraint must have &lt;&lt;definition&gt;&gt; stereotype applied. The concrete element to be defined (additional field or additional operation) is placed inside of the body.*</p><p><strong>init:</strong>* - this has to be an expression (not a constraint!) placed in some property's defaultValue field. So, you need to create some property in your class, then open specification of that property, then rightclick the Default Value field, go to &gt;Value Specification&gt;Opaque Expression. After this you can enter the OCL into the field in the same manner as you enter OCL into the specification field of the constraint*.</p><p><strong>derive:</strong>* - is modeled the same way as init, but the property has to be derived ( isDerived=true ).*</p><p><strong>pre:</strong>, *post: - these are constraints on some operation of the class. However these must be placed NOT as a simple constraints(rightclick&gt;New Element&gt;Constraint) BUT in a special designated fields(metaproperties) of the operation. Open operation specification window, switch into Expert mode, see the Precondition, Postcondition fields. Click the necesary field, click [+], then choose Constraint. Fill in the OCL constraint as necessary.*</p><p><strong>body:</strong>* - body condition is filled in the same way as pre and post conditions, but there is an additional hoop to jump through - for some reason, I do not know why, Body Condition field is marked as not shown in Expert mode (neither in Standart). So in specification window of Operation, click Customize button, find Body Condition field, and flip the radio button to Expert, and OK the dialog. After this, Body Condition field will appear in Expert mode specification window of operation in the same way Precondition and Postcondition fields do.</p><p>Small nuance: operation can have multiple pre and post conditions but only one body condition.</p><p>All these things are described/mandated in the OCL spec (06-05-01.pdf for OCL2.0), chapter 12: The Use of OCL Expressions in UML Models.</p><p>Modeling of these expression types is also briefly mentioned in MagicDraw UserManual.pdf. See chapter 8 Model Analysis&gt;Validation&gt;Advanced Topics&gt;Modeling other types OCL2.0 constraints/expressions</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-can-inv-def-init-derive-pre-post-body-type-constraints-be-modeled"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Search for the elements, which are not used in diagrams, finds attributes, operations, or slots that are represented on transitions. How to find out whether a particular element is needed in the model or not?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>It is considered that an element is used in a diagram, when there is a dedicated symbol representing it on the diagram. States and transitions have dedicated symbols for them. When a signal is assigned to the transition via trigger, it does not have a dedicated symbol on the diagram. It is only a part of textual representation of transition signature.</p><p>Let's do the following: assign a type X to an attribute on a diagram. Though we see X on the diagram as an attribute type, it is not considered as used in the diagram, because it is displayed only as a part of the attribute notation.</p><p>If you want to find out whether a particular element is needed in the model or not, use the Usages/ Dependencies functionality. Select an element in the Model Browser and from its shortcut menu select Used By. This way you may follow the chain of elements in the model and decide whether a given element is rubbish, or it makes sense.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/search-for-the-elements-which-are-not-used-in-diagrams-finds-attributes-operations-or-slots-that-are-represented-on-transitions-how-to-find-out-whether-a-particular-element-is-needed-in-the-model-or-not"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have no possibility to display the names of transitions in the State Machine diagram. The option &quot;show name&quot; in the context menu of the transition doesn't work.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The name of the transition (the value of the name property) is never shown in diagram - this has no semantic meaning. Instead, you can specify e.g. a signal, that triggers the transition. In this case the name of the trigger is displayed. If trigger name is not specified, signal name is displayed. If start typing on a transition, the signal with the name is typed will be created Automatically and the trigger will reference that signal.</p><p>A trigger defines types of events that can initiate a transition between states. An event is anything that can happen in a system: signal sent by some behavior, a call to a specific operation, reaching a point in time, a change in values within the system, etc. In other words, the formally defined list of possible events is enough for modeling state machine transitions using UML. A transition has to know of some event (indirectly), it cannot be fired by a trigger alone.</p><p>Transition signature defined in section 15.3.14 of UML 2.2 is as follows:</p><p>::= [ [',' ]* ['[' ']'] ['/' ]]</p><p>However, trigger is a non-terminal and its production rule is described in section &quot;13.3.31 Trigger&quot; (UML 2.2):</p><p>::= | | | |</p><p>Production rules for call-event, signal-event, any-receive-event, time-event and change-event are described in sections 13.3.6, 13.3.25, 13.3.1, 13.3.27, 13.3.7 respectively:</p><p>::= ['(' [ ] ')']</p><p>::= ['(' [ ] ')']</p><p>::= 'all'</p><p>::= |</p><p>::= 'after'</p><p>::= 'at'</p><p>::= 'when'</p><p>As can be seen, trigger names are never used in transition labeling. Instead, names of the referenced elements are used.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/i-have-no-possibility-to-display-the-names-of-transitions-in-the-state-machine-diagram-the-option-show-name-in-the-context-menu-of-the-transition-doesn-t-work"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have two diagrams on which the same pair of classes appears. On one of the diagrams an association is displayed between this pair, but not on the other. How can I get this association to appear on the other diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please use Related Elements &gt; Display Paths shortcut menu command.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/i-have-two-diagrams-on-which-the-same-pair-of-classes-appears-on-one-of-the-diagrams-an-association-is-displayed-between-this-pair-but-not-on-the-other-how-can-i-get-this-association-to-appear-on-the-other-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I have a class which has a realization relationship to an interface. When I use this class in a sequence diagram (as the receiver of a message), I cannot select the operation, which is part of the interface.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Class must implement all operations from interface first. From the class shortcut menu, choose Tools-&gt;Implement/Override Operations or implement all operations manually.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/i-have-a-class-which-has-a-realization-relationship-to-an-interface-when-i-use-this-class-in-a-sequence-diagram-as-the-receiver-of-a-message-i-cannot-select-the-operation-which-is-part-of-the-interface"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How do I connect interface to port with Interface Realization relation?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Port must have type specified. Only after that provided interfaces can be specified. This is because port can't provide interfaces itself, port type does (Interface Realization relation is created between type of the port and Interface, it can't be connected to Port, because port is not Classifier). Port type can be also class like port_impl.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-do-i-connect-interface-to-port-with-interface-realization-relation"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How do I associate a state diagram with a certain class?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There are two ways:</p><p>1. Drag and drop a state diagram on the selected class in the browser.</p><p>2. Choose the &quot;State Diagram&quot; command from the class shortcut menu in the browser tree.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-do-i-associate-a-state-diagram-with-a-certain-class"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is there any way to get a sequence diagram from a communication diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Currently there is no way to generate a sequence diagram from a communication diagram, or vice versa.</p><p>Communication diagram is kind of Interaction Diagram and reuses some UML elements from Sequence Diagram, but is very limited. Most of advanced Sequence Diagram elements can't be reflected in Communication Diagram. It includes all kinds of CombinedFragments, Gates, Nested activations, Sequence of messages and more, so even theoretically Communication Diagram can't be equal to Sequence Diagram.</p><p>Currently we try to gather information what would be the benefits of this feature. We would be very grateful if you could share your opinion with us.</p><p>For non automatic elements reuse - Communication Diagram can be generated inside the same Interaction (as Sequence Diagram). In this case Lifelines can be reused by simply drag'n'drop them from Interaction directly to communication diagram.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/is-there-any-way-to-get-a-sequence-diagram-from-a-communication-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">If I add a class to a class diagram and begin typing its name with the prefix of the already existing class, the name will be automatically completed. How to tell MagicDraw that it has made the correct assumption and that I would like to accept its choic</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Go with the arrows to the desired class name and press Enter.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/if-i-add-a-class-to-a-class-diagram-and-begin-typing-its-name-with-the-prefix-of-the-already-existing-class-the-name-will-be-automatically-completed-how-to-tell-magicdraw-that-it-has-made-the-correct-assumption-and-that-i-would-like-to-accept-its-choic"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Does your tool support bidirectional associations (arrow at each end or no arrows)?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw allows you to show navigability arrow only on one end of an association path. When both ends are &quot;navigable,&quot; MagicDraw simply suppresses that information and arrows are not visible.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/does-your-tool-support-bidirectional-associations-arrow-at-each-end-or-no-arrows"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to do a loop with a conditional in sequence diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You may model loops and conditions using fragments.</p><p>Use Combined fragment with operator &quot;loop&quot; for iteration notation and add another one Combined Fragment with operator &quot;alt&quot; for conditional messages grouping inside loop.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-to-do-a-loop-with-a-conditional-in-sequence-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I would like to specify that a string has maximum length 8 or that an account number has only 14 numbers. How do I specify this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>&quot;Type Modifier&quot; property should be used. Open property specification window, switch to the &quot;Expert&quot; property displaying mode, and define value (for example - 14) there.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/i-would-like-to-specify-that-a-string-has-maximum-length-8-or-that-an-account-number-has-only-14-numbers-how-do-i-specify-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is there a way to automatically display links when element with relations is dragged onto the diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To automatically discover relations on elements drag'n'drop - go to Options -&gt; Environment -&gt; Diagram -&gt; Editing -&gt; and change Display paths on element drop to true.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/is-there-a-way-to-automatically-display-links-when-element-with-relations-is-dragged-onto-the-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is there a way I can find all items in the containment tree that are not used in any diagram? This would be useful to tidy up models.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can easily find elements that are not used in any diagram using MagicDraw Find functionality.</p><p>Select command Find... from the main Edit menu to invoke Find dialog. Then specify search scope (we do not recommend to search in the whole Data package, as elements from modules will be found), and select checkboxes &quot;Search data unused in diagrams&quot; and &quot;Load diagrams and unloadable modules&quot;.</p><p>Elements that are not used in any diagram will be displayed in the Search tab in model browser.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/is-there-a-way-i-can-find-all-items-in-the-containment-tree-that-are-not-used-in-any-diagram-this-would-be-useful-to-tidy-up-models"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to visualize particular parts of the model in a diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p class="answer">To visualize relationships between elements do the following:</p><p class="answer">1. Select one or more elements in the diagram.</p><p class="answer">2. Right-click selected elements and, from the shortcut menu, select <strong>Related Elements</strong> &gt; <strong>Display Paths</strong>. To see related elements of the selected element do the following:</p><ol><li class="answer">Drag an element into a diagram.</li><li class="answer">Right-click this element and, from the shortcut menu, select <strong>Related Elements</strong> &gt; <strong>Display Related Elements</strong>. The <strong>Display Related Elements</strong> dialog will open.</li><li class="answer">In the dialog, choose settings you need and click OK. We suggest using the Layout feature to arrange elements automatically for a better view in a diagram. You can find this feature in the main menu, in the diagram toolbar, or in the diagram shortcut menu. For more information about related elements please refer to Section <strong>Displaying Related Elements</strong> in MagicDraw UserManual.pdf. To open the manual, in the main menu, select <strong>Help</strong> &gt; <strong>MagicDraw UserManual</strong>. Also you can find the manual in the &lt; MagicDraw install root &gt; \manual folder.</li></ol><p class="answer">If you are using MagicDraw 16.8 or the later version, you can use a Relation Map for the relationship visualizing. To create the Relation Map do the following:</p><ol><li class="answer">Select one or more elements in the diagram.</li><li class="answer">Right-click selected elements and, from the shortcut menu, select <strong>Related Elements</strong> &gt; <strong>Create Relation Map</strong>. A new Relation Map will be created. For more information about the Relation Map creation please refer to Section <strong>Relation Map</strong> in MagicDraw UserManual.pdf. To open the manual, in the main menu, select <strong>Help</strong> &gt; <strong>MagicDraw UserManual</strong>. Also you can find the manual in the &lt; MagicDraw install root &gt; \manual folder.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-to-visualize-particular-parts-of-the-model-in-a-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How could I change the symbol style?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p class="question">There are several ways to change the symbol style. For this purpose you can use:</p><p class="answer">- Buttons on the Diagram toolbar<br /> - <strong>Project Options</strong> dialog<br /> - <strong>Symbol Properties</strong> dialog <br /> <br /> Using buttons on Diagram toolbar <br /> <br /> There are buttons in the diagram toolbar designed to modify a symbol style.</p><p><img src="https://docs.nomagic.com/images/diagram_toolbar_1st.png" alt="" /></p><p class="answer"><strong>Set Selected Symbol Style as Default</strong>. If you select a symbol, for example, class A and click this button, a current class symbol style will be set as default for all new classes in the project.</p><p><img src="https://docs.nomagic.com/images/diagram_toolbar_2nd.png" alt="" /></p><p class="answer"><strong>Apply Default Symbol Style</strong>. If you select a symbol and click this button, a default style will be applied to the symbol.</p><p><img src="https://docs.nomagic.com/images/diagram_toolbar_3rd.png" alt="" /></p><p class="answer"><strong>Select All of the Same type</strong>. If you want to select on a diagram all symbols of the same type, click only one symbol as an example of the type and then click this button. All symbols of this type will be selected. Once all symbols of the same type are selected, you could apply changes, for example, a new default style to all of them at one go. <br /> <br /> <strong>NOTE:</strong> If you can not see these buttons, please, switch your perspective to the Expert mode (on the main menu, click <strong>Options &gt; Perspectives &gt; Perspectives</strong>and select the <strong>Expert</strong> check box in the <strong>Select Perspective</strong> dialog). <br /> <br /> Using Project Options dialog <br /> <br /> 1. On the main menu, click <strong>Options &gt; Project</strong>. The <strong>Project Options</strong> dialog will open. <br /> 2. In the Project Options tab tree, select <strong>Symbols properties styles &gt; Default</strong>, expand <strong>Default</strong> if needed, and then click the appropriate node: <strong>Shapes, Paths, Diagram</strong>, or <strong>Stereotypes</strong>. If you want to change style of a particular shape or path, expand the <strong>Shapes</strong> or <strong>Paths</strong> node, and select the desired symbol, for example, the actor or link.<br /> 3. Edit property values in the pane on the right.<br /> 4. When you have finished, do any of the following:<br /> - If you need to apply changes to the project, click the <strong>Apply</strong> button. The list of diagrams wherein the symbol style changes can be applied will open. Select diagrams (use CTRL or SHIFT keys for multiple selection) you need and click <strong>OK</strong>. Then click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.<br /> - If you do not need to apply changes right now, click <strong>OK</strong> to close the <strong>Project Options</strong> dialog. The new style properties will be saved and set as default. <br /> <br /> Using Symbol Properties dialog <br /> <br /> 1. Select a symbol and open the <strong>Symbol Properties</strong> dialog (right-click on the symbol and select <strong>Symbol(s) Properties</strong> or press ENTER+ALT). 2. Edit symbol property values (see figure bellow). 3. Select the <strong>Make Default</strong>check box before closing the dialog (see figure bellow), and all symbols of this type in the same diagram will be in the new style.</p><p><img src="https://docs.nomagic.com/images/MakeDefault_selected.png" alt="" /></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/uml-diagramming/how-could-i-change-the-symbol-style"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/printing">Printing</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw crashes or some text is messed up when printing a diagram.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Try to add &quot;-Dsun.java2d.print.shapetext=true&quot; property at JAVA_ARGS in mduml.properties<sup>*</sup> file, located in MagicDraw install root, &quot;bin&quot; directory.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/printing/magicdraw-crashes-or-some-text-is-messed-up-when-printing-a-diagram"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Page margins are returned incorrectly from the Page Setup dialog</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Add &quot;-Dmagicdraw.pageSetupDialog=true&quot; property at JAVA_ARGS in mduml.properties<sup>*</sup> file, located in MagicDraw install root, &quot;bin&quot; directory. It will enable magicdraw page setup dialog in which paper margins could be customized.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/printing/page-margins-are-returned-incorrectly-from-the-page-setup-dialog"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Page setup dialog doesn't list large media size on Linux</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Add &quot;-Dmagicdraw.pageSetupDialog=true&quot; property at JAVA_ARGS in mduml.properties<sup>*</sup> file, located in MagicDraw install root, &quot;bin&quot; directory. It will enable magicdraw page setup dialog in which media size could be customized manually by typing size in inches.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/printing/page-setup-dialog-doesn-t-list-large-media-size-on-linux"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When I try to print, I get a warning dialog that says &quot;No print service found.&quot; I am able to print with other applications as well as from the command line of a terminal window.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Problem is that the default server address in CUPS 1.2 is a domain socket, which Java does not support. They will be implementing a fix for that. At current time you can force your Java applications to use IP instead of domain sockets. Create/update an /etc/cups/client.conf file containing:</p><p>ServerName localhost</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/printing/when-i-try-to-print-i-get-a-warning-dialog-that-says-no-print-service-found-i-am-able-to-print-with-other-applications-as-well-as-from-the-command-line-of-a-terminal-window"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/code-engineering">Code Engineering</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to reverse Java 7?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Our code engineering supports Java 6. Java 7 isn't supported yet. This capability is scheduled for our 17.0.2 release.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/how-to-reverse-java-7"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">While Reversing Oracle database I got the following error. Any idea? </a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Data reading error: ORA-06502: PL/SQL: numeric or value error</p><p>LPX-00210: expected '&lt;' instead of 'n'</p><p>ORA-06512: at &quot;SYS.UTL_XML&quot;, line 0</p><p>ORA-06512: at &quot;SYS.DBMS_METADATA_INT&quot;, line 3296</p><p>...</p><p>There is a bug in Oracle 9 METADATA package.</p><p>Solution can be to reverse with user having all privileges or applying latest patch to Oracle 9.x.</p><p>As a workaround is to export database to DDL file and reverse with MagicDraw.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/while-reversing-oracle-database-i-got-the-following-error-any-idea"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is it possible to reverse QT library?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw 12.1 SP2, you may reverse QT library.</p><p>To reverse QT library using MagicDraw 12.1 SP2, you should add the following macro into MagicDraw &gt; Options-&gt;Project... C++ Language Options ... Use explicit macros (these macros are included into MagicDraw starting from v12.5 )</p><p>// QT</p><p>#define Q_AUTOTEST_EXPORT</p><p>#define Q_CLASSINFO(name, value)</p><p>#define Q_COMPAT_EXPORT</p><p>#define Q_CORE_EXPORT</p><p>#define Q_CORE_EXPORT_INLINE inline</p><p>#define Q_D(Class)</p><p>#define Q_DECL_IMPORT</p><p>#define Q_DECLARE_ASSOCIATIVE_ITERATOR(map)</p><p>#define Q_DECLARE_BUILTIN_METATYPE(TYPE, NAME)</p><p>#define Q_DECLARE_EXTENSION_INTERFACE(IFace, IId)</p><p>#define Q_DECLARE_FLAGS(Flags, enum)</p><p>#define Q_DECLARE_INTERFACE(IFace, IId)</p><p>#define Q_DECLARE_METATYPE(txt)</p><p>#define Q_DECLARE_MUTABLE_SEQUENTIAL_ITERATOR(c)</p><p>#define Q_DECLARE_MUTABLE_ASSOCIATIVE_ITERATOR(c)</p><p>#define Q_DECLARE_OPERATORS_FOR_FLAGS(Flags)</p><p>#define Q_DECLARE_PRIVATE(Class)</p><p>#define Q_DECLARE_PUBLIC(Class)</p><p>#define Q_DECLARE_SEQUENTIAL_ITERATOR(name)</p><p>#define Q_DECLARE_SHARED(name)</p><p>#define Q_DECLARE_TYPEINFO(TYPE, FLAGS)</p><p>#define Q_DECL_DEPRECATED</p><p>#define Q_DISABLE_COPY(Class)</p><p>#define Q_DUMMY_COMPARISON_OPERATOR(c)</p><p>#define Q_ENUMS(x) #define Q_FLAGS(x)</p><p>#define Q_GADGET #define Q_GUI_EXPORT</p><p>#define Q_GUI_EXPORT_INLINE inline</p><p>#define Q_INLINE_TEMPLATE</p><p>#define Q_INTERFACES(x)</p><p>#define Q_NETWORK_EXPORT</p><p>#define Q_NOREPLY</p><p>#define Q_OBJECT</p><p>#define Q_OPENGL_EXPORT</p><p>#define Q_OUTOFLINE_TEMPLATE inline</p><p>#define Q_OVERRIDE(text)</p><p>#define Q_PRIVATE_SLOT(d, signature)</p><p>#define Q_PROPERTY(text)</p><p>#define Q_Q(Class)</p><p>#define Q_REQUIRED_RESULT</p><p>#define Q_SCRIPTABLE</p><p>#define Q_SIGNALS protected</p><p>#define Q_SLOTS</p><p>#define Q_SQL_EXPORT</p><p>#define Q_SVG_EXPORT</p><p>#define Q_TESTLIB_EXPORT</p><p>#define Q_TYPENAME typename</p><p>#define Q_XML_EXPORT</p><p>#define QDBUS_EXPORT</p><p>#define QDESIGNER_COMPONENTS_EXPORT</p><p>#define QDESIGNER_EXTENSION_EXPORT</p><p>#define QDESIGNER_SDK_EXPORT</p><p>#define QDESIGNER_SHARED_EXPORT</p><p>#define QDESIGNER_UILIB_EXPORT</p><p>#define QDESIGNER_WIDGET_EXPORT</p><p>#define QDOC_PROPERTY(text)</p><p>#define QT_ASCII_CAST_WARN</p><p>#define QT_ASCII_CAST_WARN_CONSTRUCTOR</p><p>#define QT_ASSISTANT_CLIENT_EXPORT</p><p>#define QT_BEGIN_HEADER</p><p>#define QT_DEPRECATED</p><p>#define QT_DEPRECATED_VARIABLE</p><p>#define QT_DEPRECATED_CONSTRUCTOR</p><p>#define QT_END_HEADER</p><p>#define QT_FASTCALL</p><p>#define QT_FT_BEGIN_HEADER</p><p>#define QT_FT_END_HEADER</p><p>#define QT_MOC_COMPAT</p><p>#define QT_MODULE(name)</p><p>#define QT_STATIC_CONST static const</p><p>#define QT_STATIC_CONST_IMPL const</p><p>#define QT_TR_NOOP(x)</p><p>#define QT_TRANSLATE_NOOP(scope, x)</p><p>#define slots</p><p>#define signals protected</p><p>// Microsoft extension</p><p>#define __forceinline inline</p><p>#define CALLBACK</p><p>#define LRESULT void</p><p>#define _ENTRY(p1, p2, p3, p4) p1</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/is-it-possible-to-reverse-qt-library"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When I reverse engineer my project, there are a number of classes that are referenced in my code that cannot be found and are placed in the &quot;Default&quot; package. All of the classes are found in .jar files that my code depends on. I have checked the box that </a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When I reverse engineer my project, there are a number of classes that are referenced in my code that cannot be found and are placed in the &quot;Default&quot; package. All of the classes are found in .jar files that my code depends on. I have checked the box that tells the reverse engineer to look in the classpath for classes. Is there somewhere in magicdraw where I should set the classpath?</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/when-i-reverse-engineer-my-project-there-are-a-number-of-classes-that-are-referenced-in-my-code-that-cannot-be-found-and-are-placed-in-the-default-package-all-of-the-classes-are-found-in-jar-files-that-my-code-depends-on-i-have-checked-the-box-that"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Is there any way I can import an existing jar-file so that the classes from this file will be usable in the project ?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can use bytecode engineering set for reversing class files placed in your jar. Right click on &quot;Code Engineering sets&quot; node in browser, &quot;New -&gt; Java bytecode&quot; and then edit created code engineering set by adding class files from jar file. Execute &quot;Reverse&quot; action on created code engineering set and classes will be created in model.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/is-there-any-way-i-can-import-an-existing-jar-file-so-that-the-classes-from-this-file-will-be-usable-in-the-project"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to import certain Java types?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Choose the 'New From Template' command from the 'File' menu. You may also reverse the needed Java classes and import them to the project.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/how-to-import-certain-java-types"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What is the difference between the Quick Reverse and the general one?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Performing the Quick Reverse you may instantly add new model elements or merge with the created ones in your model; you don't need to create a new Round Trip Set. Use it if you don't want to use code generation on the reverse code constantly.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/what-is-the-difference-between-the-quick-reverse-and-the-general-one"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Does MagicDraw allow to import current Java source code, alter the OO model and create modified source code?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes, it does. We call this &quot;round-trip engineering&quot;. You can reverse your source code, make changes in the model and regenerate it back without losing already coded parts (e.g. method bodies). You must use the code engineering set (the MagicDraw name for a collection of classes for code engineering). If you only do framework generation (Ctrl+G), you will receive only the generated framework (all other information will be lost), so be accurate at this point.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/does-magicdraw-allow-to-import-current-java-source-code-alter-the-oo-model-and-create-modified-source-code"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Do you have an edition of MagicDraw that can parse a set of Java files and create the corresponding class diagram?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw Professional Java Edition possesses reverse engineering capability for Java. You may also reverse descriptors and will get a model describing your Enterprise Java Beans.</p><p>More information about MagicDraw editions you may find at www.nomagic.com/editions.php</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/code-engineering/do-you-have-an-edition-of-magicdraw-that-can-parse-a-set-of-java-files-and-create-the-corresponding-class-diagram"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/features">Features</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I share files (images, other projects, text documents, etc.) together with a project?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There are a couple of solutions:</p><p>1. You can copy and paste or drag and drop images to a diagram. The image shape will be available for the copied image. MagicDraw supports .gif, .jpg, .svg, and .png image file types.</p><p>Note: The project size increases accordingly to the quantity and size in bytes of the inserted images, and this might have a great impact on the performance.</p><p>2. You can link external files to the project by specifying the relative paths to them. The relative path is always suggested, when creating a hyperlink to the external file, which is stored in the same folder with the project.</p><p>A relative path for a hyperlink can also be specified manually, e.g., &quot;file:// /My Pictures/sample.jpg&quot; for the picture, which is stored in the My Pictures directory that is located in the same folder with the project.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/how-can-i-share-files-images-other-projects-text-documents-etc-together-with-a-project"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is it possible to add a hyperlink with a relative path* to an image or a project file?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>*A relative path begins at a current folder of the hierarchy (i.e., a project or the MagicDraw installation) and specifies the file's location from there.</p><p>You can add a hyperlink with a path, which is relative to the MagicDraw installation folder. For example, the path &quot;<a href="file://sample.jpg">file://sample.jpg</a>&quot; refers to the image, which is stored in the MagicDraw installation folder.</p><p>A path, which is relative to the project storage location, is always suggested, when creating a hyperlink to the file, which is stored in the same folder with the project. A relative path can also be specified manually. For example, the path &quot;<a href="file://My Pictures/sample.jpg">file://My Pictures/sample.jpg</a>&quot; refers to the picture, which is stored in the My Pictures directory that is located in the same folder with the project.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/is-it-possible-to-add-a-hyperlink-with-a-relative-path-to-an-image-or-a-project-file"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is there any plugin to make automatically the UML2 transformation without having to make File-&gt;Export-&gt;To UML2 from the user interface?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Just go to &quot;Options-&gt;Environment-&gt;EMF UML2 (vx.x) XMI Options&quot;, and change the option &quot;Export Model to EMF UML2 XMI on project save&quot; The project will be exported on project saving.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/is-there-any-plugin-to-make-automatically-the-uml2-transformation-without-having-to-make-file-export-to-uml2-from-the-user-interface"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">We are editing different diagrams in the same model, which is held in the CVS repository.Although working in different areas of the model, we keep getting unmergible files from the repository whenever we update our working versions from CVS after the othe</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>In MagicDraw, the following options are available for sharing model for simultaneous work:</p><p>1. Model decomposition functionality is available in MagicDraw. Now it is possible to reuse project module in another project.</p><p>2. MagicDraw Teamwork Server. This product is fully optimized for working with UML model.</p><p>3. Since MagicDraw version 12.5, Teamwork Server integration with ClearCase and SVN is presented.</p><p>CVS is an options just for storing, not sharing</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/we-are-editing-different-diagrams-in-the-same-model-which-is-held-in-the-cvs-repository-although-working-in-different-areas-of-the-model-we-keep-getting-unmergible-files-from-the-repository-whenever-we-update-our-working-versions-from-cvs-after-the-othe"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to copy a diagram into the Windows clipboard and paste into a Word doc?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Choose the 'Copy as EMF' or 'Copy as JPG' command from the 'Edit' menu.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/how-to-copy-a-diagram-into-the-windows-clipboard-and-paste-into-a-word-doc"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Does MagicDraw support model consistency between all diagrams?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw supports metamodel relation (consistency) between class and interaction (sequence and communication) diagrams: it reflects all the operations of the class in the message call action list. Classifier can be assigned to any lifeline. Class operations can be selected in the triggers in the state/activity diagrams.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/does-magicdraw-support-model-consistency-between-all-diagrams"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to open console together with the MagicDraw application?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Edit file mduml.properties<sup>*</sup> in bin directory. Change line CONSOLE=false to line CONSOLE=true</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/how-to-open-console-together-with-the-magicdraw-application"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is there any way that I can access elements from other projects?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw Version 7.0, partitioning functionality is presented in MagicDraw. Now it is possible to reuse project module by reference in another project.</p><p>Also MagicDraw Teamwork Server is available, which enables team collaboration.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/features/is-there-any-way-that-i-can-access-elements-from-other-projects"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/integrations">Integrations</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MD v15.5, oAW 4.3 and Eclipse 3.4 integration. Try to run oAW sample as oAW workflow. The exceptions appears in console and sample fails to run. 5 INFO WorkflowRunner - Exception in thread &quot;main&quot; java.lang.ExceptionInInitializerError at org.openarchitectu</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The problem is outdated Xerces library, used by MagicDraw. Please remove this library (it is not necessary, because java 1.5/1.6 already has XML parsing in the standard install).</p><p>There is also a workaround. Please specify the-Djavax.xml.parsers.SAXParserFactory=com.sun.org.apache.xerces.internal.jaxp. SAXParserFactoryImpl parameter for the Java when running the workflow. This will force the script to use Java's default implementation instead of one brought in by MagicDraw.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/md-v15-5-oaw-4-3-and-eclipse-3-4-integration-try-to-run-oaw-sample-as-oaw-workflow-the-exceptions-appears-in-console-and-sample-fails-to-run-5-info-workflowrunner-exception-in-thread-main-java-lang-exceptionininitializererror-at-org-openarchitectu"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I get an error when trying to perfom CVS operations in MagicDraw. I use a local cvs repository at home. Does MagicDraw support a CVSROOT of the form &quot;/my/cvsroot&quot;?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw CVS integration supports only pserver connection type.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/i-get-an-error-when-trying-to-perfom-cvs-operations-in-magicdraw-i-use-a-local-cvs-repository-at-home-does-magicdraw-support-a-cvsroot-of-the-form-my-cvsroot"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Automatic search in combo boxes is not working. I'm using MagicDraw integrated with IntelliJ.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You should modify the idea.properties file in the IntelliJ: idea.popup.weight property set to medium. After editing it should look like that: idea.popup.weight=medium</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/automatic-search-in-combo-boxes-is-not-working-i-m-using-magicdraw-integrated-with-intellij"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Does MagicDraw support Eclipse integration within OSX?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw version 12.5, Eclipse and MagicDraw works together on Mac OS X with JVM 1.6.0.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/does-magicdraw-support-eclipse-integration-within-osx"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Do MagicDraw integrations with IDEs support Java 5.0 code engineering?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw 10.5 version, integration with Eclipse supports Java 5.0 code engineering.</p><p>Since MagicDraw 15.0 version, integration with NetBeans and JBuilder (works only up to MaigcDraw v17.0.1) supports Java 5.0 code engineering also.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/do-magicdraw-integrations-with-ides-support-java-5-0-code-engineering"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Does MagicDraw Standard edition integrate with Eclipse?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes, MagicDraw Standard edition, as well as Professional integrates with Eclipse, WSAD, JBuilder (works only up to MaigcDraw v17.0.1), Sun One Studio, and NetBeans without any problems. The difference is that the Standard edition itself has no code engineering functionality but this does not have any impact to the integration.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/does-magicdraw-standard-edition-integrate-with-eclipse"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Do you plan to link with any of the popular IDEs/source code tools?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes. We currently have integrations with Eclipse 3.1 or later (JDT or Java IDE), JBuilder 8.0, 9.0, X, 2005, 2006, 2007 (works only to MagicDraw v17.0.1), 2008, IBM RAD 7.0, IBM RAD 7.5, BEA WebLogic Workshop v9.2, v10.1, v10.2, Netbeans 6.0 or later, Sun Java Studio 8, Sun ONE Studio 5 (works only up to MagicDraw 10.5 version), IntelliJ IDEA 4.5 or later.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/do-you-plan-to-link-with-any-of-the-popular-ides-source-code-tools"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">With what version of IntelliJ IDEA integrates MagicDraw?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw integrates with IntelliJ IDEA 4.X or later</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/with-what-version-of-intellij-idea-integrates-magicdraw"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Diagrams or Browser tabs are frozen because of modal dialog appearance.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The solution is to close and reopen Diagram View or Browser tabs in all Eclipse perspectives.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/diagrams-or-browser-tabs-are-frozen-because-of-modal-dialog-appearance"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I am trying to install MagicDraw and use Eclipse integration in Japanese, but menu fonts are corrupted.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please, try to add such line -DdefaultFont=true in eclipse.ini file after vmargs.</p><p>The lines should look like:</p><p>-vmargs</p><p>-DdefaultFont=true</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/i-am-trying-to-install-magicdraw-and-use-eclipse-integration-in-japanese-but-menu-fonts-are-corrupted"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">After unintegration, Eclipse cannot be started with new integrated MagicDraw</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>After unintegration, old directory is still remembered by Eclipse. The solution is to unintegrate Eclipse from MagicDraw, then start Eclipse, close it, and only then integrate with new MagicDraw version and launch again.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/after-unintegration-eclipse-cannot-be-started-with-new-integrated-magicdraw"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Out of memory errors with MagicDraw and Eclipse</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Some JVMs put restrictions on the total amount of memory available on the heap. If you are getting OutOfMemoryErrors while running Eclipse, the VM can be told to let the heap grow to a larger amount by passing the -vmargs command to the Eclipse launcher. For example, the following command would run Eclipse with a heap size of 512MB:</p><p>eclipse [normal arguments] -vmargs -Xmx512M [more VM args]</p><p>Some JVMs have restrictions on permanent generation memory, which can be exceeded in integration. In order to increase permanent generation memory size, you need to specify additionally -XX:MaxPermSize (use it for Sun JVM). For example, the following command would run Eclipse with a permanent generation memory size of 128MB:</p><p>eclipse [normal arguments] -vmargs -XX:MaxPermSize=128M [more VM args]</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/out-of-memory-errors-with-magicdraw-and-eclipse"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">MagicDraw integrated with Eclipse cannot be started</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Sometimes when starting MagicDraw from Eclipse, MagicDraw is not started. This problem can appear after MagicDraw version update. The solution is to launch Eclipse with the -clean parameter first time when this problem appears:</p><p>eclipse -clean</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/magicdraw-integrated-with-eclipse-cannot-be-started"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw windows are not redrawed properly running within Eclipse</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>If you have specified property &quot;-Dsun.java2d.d3d=false&quot; in &quot;eclipse.ini&quot;, try to remove it or set the &quot;true&quot; value.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/magicdraw-windows-are-not-redrawed-properly-running-within-eclipse"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I have followed integration steps for MagicDraw 17.0 and Eclipse 3.7, but I see no integration inside of Eclipse. What should I do?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw 17.0 SP2 and earlier is not compatible with Eclipse 3.7.</p><p>We suggest you to integrate MagicDraw 17.0 SP2 with Eclipse 3.6.</p><p>uml2ecore transformation of openArchitectureWare framework does not work on Linux, Mac OS</p><p>Symptom: you get the following error when doing uml2ecore transformation:</p><p>797 INFO CompositeComponent - Generator.contraintsEtc: generating 'org::openarchitectureware::util::uml2ecore::templates::files::root FOR ecoreModel' =&gt; directory 'meta/' 7823 ERROR WorkflowRunner - org/openarchitectureware/util/uml2ecore/templates/files.xpt: unexpected char: 0xFFFD (Note, that char may be different, e.g. on Mac, unexpected char: 0xB4 is encountered)</p><p>Cause: uml2ecore transformation contains a bug, which precludes it from working on systems, where default file encoding is non standard. For example on Ubuntu v7.04 (Feisty Fawn) default encoding is UTF-8; Mac OS X, MacRoman encoding is used bu default. This causes transformation to fail, because files.xpt template file in the transformation plugin is encoded in ISO-8859-1.</p><p>This bug is not a bug in MagicDraw, but a bug in openArchitectureWare. This bug is acknowledged and tracked in oAW bug list: <a href="https://bugs.eclipse.org/bugs/show_bug.cgi?id=177956">https://bugs.eclipse.org/bugs/show_bug.cgi?id=177956</a> This bug is present in oAW v4.1.2. Currently we do not know, when this issue will be fixed.</p><p>Workaround:</p><p>1) locate the uml2ecore plugin jar file. This file is usualy /plugins/org.openarchitectureware.util.uml2ecore_4.1.2.v20070314.jar (note that version numbers/dates may be slightly different in your install). Backup this file somewhere, we will be editing it.</p><p>2) inside this jar archive, locate uml2ecoreWorkflow.oaw file, open it in editor and scroll to the bottom.</p><p>3) locate the oaw.xpand2.Generator invocation component (id=&quot;Generator.contraintsEtc&quot;), and add additional tag inside. Here is the final result you should get:</p><p>.....<br /> <br /> 4) update jar archive with this new version of uml2ecoreWorkflow.oaw file</p><p>5) restart Eclipse.</p><p>uml2 ecore transformation should now run cleanly.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/integrations/i-have-followed-integration-steps-for-magicdraw-17-0-and-eclipse-3-7-but-i-see-no-integration-inside-of-eclipse-what-should-i-do"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/teamwork-server">Teamwork Server</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Can Teamwork Server up to v17.0 be integrated with SVN v1.6?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Teamwork Server starting from v17.0 supports SVN 1.6 server and client. Teamwork Server up to v17.0 does support SVN server v1.6. However SVN client version 1.4 or 1.5 should be used. Lower version clients are compatible with SVN server v1.6. You can include older SVN clients in system paths or define it for Teamwork Server by setting java properties. To do this open &quot;teamwork_server.properties&quot; file and add &quot;-DSVN= &quot; to JAVA_ARGS line.</p><p>Please restart the Teamwork Server to apply changes.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/can-teamwork-server-up-to-v17-0-be-integrated-with-svn-v1-6"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I cannot login to the Teamwork Server, although installation has been successful.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please try to add such line to the Teamwork Server/data/muserver.properties file:</p><p>java.rmi.server.hostname=teamwork.server.com, where teamwork.server.com is the ip of the computer of the Teamwork Server.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/i-cannot-login-to-the-teamwork-server-although-installation-has-been-successful"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to connect to the Teamwork Server via ssh?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>1. Stop the Teamwork Server.</p><p>2. Edit run_server_nogui.properties file by adding -Djava.rmi.server.hostname=localhost to the line JAVA_ARGS. This prevents from direct connecting from client to server (skipping ssh tunnel).</p><p>3. Start the Teamwork Server using run_server_nogui.exe.</p><p>4. On the client side, run command line: ssh -L 1099:host:1099 <a href="mailto:user@host.">user@host.</a> Host here is a hostname of the Teamwork Server.</p><p>5. Run a client. For a server address, use localhost:1099.</p><p>Limitation of such configuration is that all clients should use ssh tunneling.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/how-to-connect-to-the-teamwork-server-via-ssh"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to start the Teamwork Server on startup of Redhat Linux as service?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please update TEAMWORK_HOME variable in attached script file (TEAMWORK_HOME=&quot;/teamwork/MagicDraw_Teamwork_Server/bin&quot;) according to your installation path bin dir.</p><p>Copy the &quot;teamwork&quot; service script to /etc/init.d.</p><p>Then as a root enable the &quot;teamwork&quot; service for runlevel 3 using following commands:</p><p>cd /etc/rc3.d</p><p>ln -s ../init.d/teamwork S99teamwork</p><p>RedHat based Linux distrubutions the service run levels may be configured using &quot;chkconfig&quot; command.</p><p>You may test the &quot;teamwork&quot; service using &quot;service&quot; command.</p><p>Use &quot;service teamwork start&quot; command to start MagicDraw Teamwork Server</p><p>Use &quot;service teamwork stop&quot; command to stop MagicDraw Teamwork Server</p><p>Use &quot;service teamwork status&quot; command to check if MagicDraw Teamwork</p><p>Server is running.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/how-to-start-the-teamwork-server-on-startup-of-redhat-linux-as-service"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Scheduling of synchronization between two distant Teamwork Servers does not work. How to turn it on?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The scheduling of synchronization between two distant Teamwork Servers <strong>is by default turned off</strong>.<br /> <br /> To turn on the scheduling:</p><ol><li>Open the muserver.properties file that can be found in &lt;MagicDraw Teamwork Server installation directory&gt;\data.</li><li>Edit the file as the follows:<br /> server.synchronize.scheduler.enable=true</li><li>Restart the Teamwork Server.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/scheduling-of-synchronization-between-two-distant-teamwork-servers-does-not-work-how-to-turn-it-on"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">On logging back to the Teamwork Server after the MagicDraw has been crashed, the server complaints that the user is already logged in.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>After the MagicDraw application has been crashed, please, wait about 6 min. and only then try to connect.</p><p>The other solution is to restart the Teamwork Server.</p><p>Note: After restarting the server, all users will be disconnected.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/on-logging-back-to-the-teamwork-server-after-the-magicdraw-has-been-crashed-the-server-complaints-that-the-user-is-already-logged-in"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I cannot find the Teamwork Server menu, although I see it in the docs.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You should have an evaluation MagicDraw version or a commercial/academic license (not demo) in order to access Teamwork Server menu.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/i-cannot-find-the-teamwork-server-menu-although-i-see-it-in-the-docs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to upgrade the Teamwork Server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Instructions how to upgrade teamwork server:</p><p>1. Stop the Teamwork Server.</p><p>2. Remove NT service from the teamwork server (if it was added).</p><p>3. Install a new version of the Teamwork Server and run it.</p><p>4. When the Import configuration dialog box appears, provide earlier version installation directory, to import configurations from it. 5. Select checkbox Import all projects in order to import teamwork projects from earlier Teamwork Server version.</p><p>6. Start new Teamwork Server (add NT service if needed).</p><p>7. Install new client version.</p><p>8. Uninstall old Teamwork Server.</p><p>Newer version install will not detect nor uninstall older one service. Projects should be imported manually. Project server and client version should be the same and cannot be mixed up. Also we recommend to use the same JVM version for server an client.</p><p>Importing projects from previous Teamwork Server version.</p><p>If you had previous Teamwork Server version with projects stored, it is possible to import them automatically using MagicDraw GUI or perform manual migration.</p><p>To import projects using GUI</p><p>1. After installation is complete and Teamwork Server is launched first time, the Import Configuration dialog box opens.</p><p>2. Path to the previous Teamwork Server installation, which was found in your computer, is specified in the Location text box. You can change this path by clicking &quot;...&quot; button.</p><p>3. Select the Import all projects check box for projects transfer to the newest Teamwork Server version.</p><p>4. Click Import.</p><p>To import projects manually</p><p>Copy Projects directory with all its files from previous Teamwork Server installation directory, to the new /Projects directory.</p><p>NOTE Follow the instructions in dialog boxes to update profiles during project import.</p><p>If server is started on SVN/ClearCase repository.</p><p>2. Open Administrator's Console, trigger project export. Choose the directory to dump the data to. Chose the permanent directory (not some temporary directory) - this will be the directory in which server will subsequently operate.</p><p>3. In Administrator's Console, reconfigure server for work with Built-In repository; specify the directory where you dumped projects as a directory to work with.</p><p>4. Restart server, to use new repository.</p><p>5. Projects are now in a new, Built-In repository.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/how-to-upgrade-the-teamwork-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">We have a project in Teamwork Server with many versions. Old versions use large amount of space on the disk. How to clean up old versions in Teamwork Server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Clean up of old versions is not recommended but if you really need it you should do the following thing:</p><p>1. Stop teamwork server.</p><p>2. Backup your project directory.</p><p>3. Go to teamwork server projects directory, find there file projects.xml and using this file find directory for project you want to clean up.</p><p>4. In this directory you can remove files modelXXX.xml.zip XXX is the version number. Each version is saved in its own file.</p><p>For example if you want to remove all versions from 1 to 10 you need to remove model1.xml.zip model2.xml.zip and so on until model10.xml.zip. Please note that:</p><p>a. You will not be able to open the versions you removed.</p><p>b. Do not remove latest version, in this case you will not be able to open project at all.</p><p>c. If your project is module and used in another project (project B) you can get trouble opening project's B old versions.</p><p>5. After clean up, start the server.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/we-have-a-project-in-teamwork-server-with-many-versions-old-versions-use-large-amount-of-space-on-the-disk-how-to-clean-up-old-versions-in-teamwork-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Where can I find the server.log file?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The server.log file is located in /projects.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/where-can-i-find-the-server-log-file"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">After the December 1st Teamwork Server v16.8 and v16.9 does not start, out of memory error is shown and lots of log files are created in the projects folder. How to start Teamwork Server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Add parameter value &quot;-Dbackup.interval=YEAR&quot; to JAVA_ARGS in both teamwork_server.properties and teamwork_server_nogui.properties those are located in &quot;MagicDraw Teamwork Server installation directory&quot;\bin.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/after-the-december-1st-teamwork-server-v16-8-and-v16-9-does-not-start-out-of-memory-error-is-shown-and-lots-of-log-files-are-created-in-the-projects-folder-how-to-start-teamwork-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Teamwork Server (prior to v17.0.2 SP3 and v17.0.3 SP1) running as service stops when the user logs out from the OS.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Here are the instructions on how to fix it:</p><p>1. Open the file ....\MagicDraw Teamwork Server\bin\teamwork_server_nogui.properties<br /> 2. Add -Xrs to JAVA_ARGS. It should look something like this:<br /> JAVA_ARGS=-Xmx400M -Xrs -Djava.rmi.server.useCodebaseOnly\=true<br /> -Dsun.rmi.server.exceptionTrace\=true -Djava.awt.headless\=true<br /> -Duser.language\=en -DLOCALCONFIG\=false<br /> 3. Restart the Teamwork service.<br /> 4. Log out.<br /> 5. Test if you can connect to the Teamwork server with MagicDraw.</p><p>Note: This issue is resolved in v17.0.2 SP3 and v17.0.3 SP1</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/teamwork-server-prior-to-v17-0-2-sp3-and-v17-0-3-sp1-running-as-service-stops-when-the-user-logs-out-from-the-os"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">In Teamwork server up to v17.0.2 SP3 and v17.0.3 SP1, there are issues with adding/starting the service using Java versions 1.7.0_21 and 1.6.0_45.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This issue is caused by Java update</p><p><a href="http://www.oracle.com/technetwork/java/javase/6u45-relnotes-1932876.html">http://www.oracle.com/technetwork/java/javase/6u45-relnotes-1932876.html</a></p><p>The solution is to use an earlier Java version. The list of recommended Java versions can be found at <a href="http://www.nomagic.com/support/jvm-list.html">http://www.nomagic.com/support/jvm-list.html</a></p><p>Problem will be fixed in the next teamwork server version and service pack.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/in-teamwork-server-up-to-v17-0-2-sp3-and-v17-0-3-sp1-there-are-issues-with-adding-starting-the-service-using-java-versions-1-7-0-21-and-1-6-0-45"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">A stereotype applied on attribute, operation, parameter, or other kind of property disappears from the model after the project update from Teamwork Server 17.0.4, if a property has been edited. How can this be handled?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To handle the problem, please use the following workaround:</p><ol><li>Open the mduml.properties<sup>*</sup> file that can be found in &lt;MagicDraw installation folder&gt;\bin.</li><li>Next to JAVA_ARGS, add the following line:<br /> -Ddisable.element.version.service=true.<br /> Example:<br /> JAVA_ARGS=-Xmx2396M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M<br /> -DLOCALCONFIG\=true -splash\:data/splash.gif -Xss1024K<br /> -Ddisable.element.version.service=true</li><li>Restart MagicDraw.</li></ol><p>The issue will be fixed in v17.0.4 SP1.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/a-stereotype-applied-on-attribute-operation-parameter-or-other-kind-of-property-disappears-from-the-model-after-the-project-update-from-teamwork-server-17-0-4-if-a-property-has-been-edited-how-can-this-be-handled"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Teamwork Server stops when I log off from my OS. Is there a solution to this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>If Teamwork Server is running as application, it does stop upon logoff from the OS. The solution is to run the server as a service.<br /> <br /> Please check Teamwork Server User Guide, section &quot;Starting the server without using GUI&quot; for detailed instructions for your particular OS. The User Guide is available at <a href="http://www.nomagic.com/support/documentation.html">http://www.nomagic.com/support/documentation.html</a><a href="https://docs.nomagic.com/support/documentation.html">.</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/teamwork-server/teamwork-server-stops-when-i-log-off-from-my-os-is-there-a-solution-to-this"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/modules">Modules</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Do you support editing a referred module inside a project?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes, MagicDraw supports both read-only and read-write modes for module usage. Usage of read-write modules is a bit tricky, especially if we have modules nested in one another and with circular dependencies between one another. When partitioning always refer to Modules dialog (Options&gt;Modules) as your friend and guide.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/modules/do-you-support-editing-a-referred-module-inside-a-project"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Do you support dynamic loading of modules?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes, module can be loaded/unloaded by the user at (almost) any time during the work process. Also module usage has a parameter which governs if module should be loaded at project load time: &quot;always load&quot; means module is loaded with project &quot;auto-load&quot; and &quot;auto-load with prompt&quot; module is not loaded, but MagicDraw tries to guess when user would need module contents (e.g. when user runs search in the entire model) and loads module then.</p><p>&quot;manual load&quot; means module is not loaded - user can load it later.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/modules/do-you-support-dynamic-loading-of-modules"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later">Floating licenses (v16.8 and later)</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Cameo daemon thinks my hostid is 000000000000</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>I got the following messages in my cameo daemon log file:<br /> 16:36:22 (cameo) Server started on cm1 for: MagicDrawEnterprise<br /> 16:36:22 (cameo) Wrong hostid on SERVER line for license file:<br /> 16:36:22 (cameo) licenses/cameo/license.txt<br /> 16:36:22 (cameo) SERVER line says 90b11c596715, hostid is 000000000000<br /> 16:36:22 (cameo) Invalid hostid on SERVER line<br /> 16:36:22 (cameo) Disabling 5 licenses from feature MagicDrawEnterprise(0393 0246 4250 573D )<br /> 16:36:22 (cameo) EXTERNAL FILTERS are OFF<br /> 16:36:22 (cameo) No valid hostids, exiting<br /> 16:36:22 (cameo) EXITING DUE TO SIGNAL 34 Exit reason 2</p><p><br /> <strong>Answer</strong></p><p>Currently, FlexLM does not support interface names other than eth0, eth1, ..., ethN. Alternate interface names, such as em1, are not recognized and will return the invalid hostid 000000000000.</p><p>As a workaround we offer you to change your interface names to ethN, such as eth0. Consult the documentation of both your system and distribution to learn how to reset an interface name. Look for more information:</p><ul><li><a href="http://www.exelisvis.com/Support/HelpArticlesDetail/TabId/219/ArtMID/900/ArticleID/5199/5199.aspx">Solution for &quot;Hostid 00000000000&quot; on Red Hat 6 and Fedora15</a></li><li><a href="https://features.opensuse.org/310896">Consistent Network device naming-Name network interfaces to match chassis labels</a></li></ul><p>Please contact our customer support, if this does not help.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/cameo-daemon-thinks-my-hostid-is-000000000000"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to return the floating license if two licenses are used by the same user on the same PC?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.</p><p>By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.</p><p>For more details, please see <a href="https://docs.nomagic.com/support/faq/53-floating-licenses-v16-8-and-later/122-how-to-release-a-hanging-license-to-the-pool">How to release a hanging license to the pool?</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/how-to-return-the-floating-license-if-two-licenses-are-used-by-the-same-user-on-the-same-pc"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to release a hanging license to the pool?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There are several methods how to release license:</p><p>1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at <a href="http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf">http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf</a></p><p>2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. Follow the link http://:8080 to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.</p><p>3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at <a href="http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf">http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/how-to-release-a-hanging-license-to-the-pool"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.</p><p>In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.</p><p>Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at <a href="http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf">http://www.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf</a><a href="https://docs.nomagic.com/files/manuals/fnp_LicAdmin_11_12_1.pdf">.</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/i-m-trying-to-run-the-two-license-servers-and-vendor-daemons-on-same-machine-to-restrict-who-gets-access-to-which-licenses-how-can-i-do-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What command-line options are available with lmadmin?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can find list of the options by issuing the following command at the command prompt:</p><p>&gt;lmadmin -help</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/what-command-line-options-are-available-with-lmadmin"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/i-cannot-start-the-lmadmin-application-as-a-root-the-flexnet-license-server-does-not-start-on-linux"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When we try to start the cameo vendor daemon, we get the error:(lmgrd) cameo using TCP-port 0 (cameo) tcp_s is bad!!! EXITING (cameo) DUE TOSIGNAL 28 Exit reason 5</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Such an error appears when demo daemon, included in the license server installation, has expired</p><p>Please remove the demo daemon from the server and try again. There are couple few ways to do so:</p><ul><li>You can remove it from server graphical interface side, or</li><li>Directly from server.xml file side. Do as following:</li></ul><ol><li>In order to start the server without demo daemon, first remove daemon from the server.xml file. This file you can found in the platform directory &quot;conf&quot; folder.</li><li>Remove the line: &lt;daemon dateBasedVersion=&quot;false&quot; dlog=&quot;false&quot; executable=&quot;demo/demo&quot; license=&quot;demo/demo.lic&quot; logFile=&quot;logs/demo.log&quot; logOverwrite=&quot;false&quot; name=&quot;demo&quot; port=&quot;0&quot; restartRetries=&quot;3&quot;/&gt;</li><li>Start license server again.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/when-we-try-to-start-the-cameo-vendor-daemon-we-get-the-error-lmgrd-cameo-using-tcp-port-0-cameo-tcp-s-is-bad-exiting-cameo-due-tosignal-28-exit-reason-5"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Such an error appears when:</p><p>The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.</p><p>Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.</p><p>You may check and change the port number in the FLEXnet license administrator console.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/when-we-try-to-start-the-vendor-daemon-we-get-the-error-cameo-tcp-s-is-bad-exiting-cameo-exiting-due-to-signal-28-exit-reason-5-how-to-start-the-license-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">The FLEXnet license server doesn’t respond, so the end user cannot connect to the license server. The following information is provided in the Cameo.log file: (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 ... (cameo) Lost communications with lmgrd. Comm</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>It can occur because of Microsoft® Windows DEP (Data Execution Prevention) on the server. DEP simply kills the lmgrd application when it starts.</p><p>The suggested solution is:</p><p>1. Stop the license service using LMTOOLS.EXE or the Windows Services dialog box.</p><p>2. Open Task Manager and stop all processes named like lmgrd.exe and cameo.exe</p><p>3. Select Control Panel &gt; System &gt; Advanced &gt; Performance Settings &gt; Data Execution Prevention</p><p>4. Select the Turn on DEP for all programs and services except those I select check box and add to the list LMGRD.EXE, LMUTIL.EXE, LMTOOLS.EXE, and the vendor daemon, where the license manager is installed</p><p>5. Restart the service</p><p>DEP also may impact LMTOOLS.EXE crashes or stops the license service (you cannot checkout any licenses then). It is known that such a situation occurs not only on the Microsoft® Windows 2008 server but also on the Microsoft® Windows 2003 server.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/the-flexnet-license-server-doesn-t-respond-so-the-end-user-cannot-connect-to-the-license-server-the-following-information-is-provided-in-the-cameo-log-file-cameo-exiting-due-to-signal-28-exit-reason-5-cameo-lost-communications-with-lmgrd-comm"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I got error &quot;File not found, cameo.exe&quot; what to do?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>As the log says, &quot;File not found, cameo.exe&quot;. So the lmadmin cannot find the daemon. There are two reasons / solutions:</p><p>- Maybe you have put the daemon cameo.exe in another folder.</p><p>Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.</p><p>- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from <a href="https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download">https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/i-got-error-file-not-found-cameo-exe-what-to-do"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have firewall blocking the connection to the FLEXnet license server. What ports are used?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/i-have-firewall-blocking-the-connection-to-the-flexnet-license-server-what-ports-are-used"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">License Server Manager Not Starting</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The license server manager will not start if either of the following ports are in use:</p><p>* Default license server port (no ports in range 27000 to 27009 available)</p><p>* Default HTTP port for the license server manager user interface (port 8080)</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/license-server-manager-not-starting"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">On new key application into FLEXnet licenses server lmadmin error appears – &quot;Inconsistent server host name in: licenses\cameo\…</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.</p><p>Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/on-new-key-application-into-flexnet-licenses-server-lmadmin-error-appears-inconsistent-server-host-name-in-licenses-cameo"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I find lmgrid or lmadmin log file?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The location of the log file depends on what license server manager you use.</p><ul><li>If it is <em>lmgrid</em>, the <em>cameo.log</em> and<em> lmgrid.log</em> files can both be found directly in the root package of the lmgrid installation.</li><li>If it is <em>lmadmin</em>, the <em>cameo.log</em> file can be found in <em>&lt;lmadmin installation directory&gt;\logs</em>, for example, <em>C:\Program Files\FlexNet Publisher License Server Manager\logs</em>.</li></ul><p><strong>Note:</strong> The default location of the log file can be changed during the product configuration.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/where-can-i-find-lmgrid-or-lmadmin-log-file"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to reset the lmadmin password, if a user cannot connect to a server using a web interface</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>1. From <em>&lt;flexnet license server installation directory&gt;\conf</em>, open the <em>server.xml</em> file for editing.</p><p>2. In the line</p><p>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</p><p>change the password key value to &quot;aa&quot; as shown in the following example:</p><p>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;aa&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</p><p>3. Restart <em>lmadmin</em> (end the <em>lmadmin</em> process and start it again manually).</p><p>4. Connect to the FlexNet server (the default address is <a>http://&lt;server_name&gt;:8090</a>) with the following credentials:</p><p>User Name: <em>admin</em><br /> Password: <em>aa</em></p><p>5. In the <strong>User Configuration</strong> tab, click <strong>Edit</strong>, enter a new password and save it.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-licenses-v16-8-and-later/how-to-reset-the-lmadmin-password,-if-a-user-cannot-connect-to-a-server-using-a-web-interface"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier">Floating License (v16.6 and earlier)</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I download the floating license server, which I've purchaced?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Login with the purchaser's username and password, click on license list, and download from there (or get keys from there).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/where-can-i-download-the-floating-license-server-which-i-ve-purchaced"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to connect to the Floating License Server via SSH?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>1. Stop the Floating License Server.</p><p>2. Edit run_server_nogui.properties file by adding -Djava.rmi.server.hostname=localhost to the line JAVA_ARGS. This prevents from direct connecting from client to server (skipping ssh tunnel).</p><p>3. Start the FLoating License Server using run_server_nogui.exe.</p><p>4. On the client side, run command line: ssh -L 1099:host:1099 <a href="mailto:user@host.">user@host.</a> Host here is a hostname of the Floating License Server.</p><p>5. Run a client. For a server address, use localhost:1099.</p><p>Limitation of such configuration is that all clients should use ssh tunneling.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/how-to-connect-to-the-floating-license-server-via-ssh"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Do we need to install a new version of the floating license server, or can we use an old one with new version clients?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Since MagicDraw v12.0, Floating License server supports 12.0 and higher MagicDraw clients versions.</p><p>For example FL v14.0 can work with v. 12.0, v12.5, and v14.0 clients.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/do-we-need-to-install-a-new-version-of-the-floating-license-server-or-can-we-use-an-old-one-with-new-version-clients"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I am unable to add NT service.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You must have administrator rights to add an NT service.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/i-am-unable-to-add-nt-service"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I've got MagicDraw running on two PC's but when I tried to install it on another I get a &quot;Not connecting to license server&quot; error message.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Use the text name of the license server instead the actual IP address.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/i-ve-got-magicdraw-running-on-two-pc-s-but-when-i-tried-to-install-it-on-another-i-get-a-not-connecting-to-license-server-error-message"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw Floating license Server and Teamwork Server v15.0 running on Windows 2003 Server as service has to be started after every reboot to make it work. How to avoid this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please copy the msvcr71.dll to the /lib. This DLL is installed under \jre\bin.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/magicdraw-floating-license-server-and-teamwork-server-v15-0-running-on-windows-2003-server-as-service-has-to-be-started-after-every-reboot-to-make-it-work-how-to-avoid-this"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I find more problems and solutions regarding license server - Lmadmin?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Flexera software lmadmin FAQ is available at <a href="http://www.globes.com/support/fnp_utilities_download.htm">http://www.globes.com/support/fnp_utilities_download.htm</a> &gt; Documentation section &gt; lmadmin Migration FAQ.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/floating-license-v16-6-and-earlier/where-can-i-find-more-problems-and-solutions-regarding-license-server-lmadmin"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/sysml-plugin">SysML Plugin</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How to avoid cyclic dependencies appearing between modules when SysML «allocate», «satisfy», and «refine» relationships connect elements residing in different modules?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The problem is specific for SysML which creates values on both ends for relationships thus creating cyclic dependencies between modules. This issue is fixed in MagicDraw 17.0 SP5 which will be released on April, 2012. Currently as a workaround we suggest to perform the following steps:</p><ol><li>Export model elements to modules and make them read-only.</li><li>Then draw «allocate», «satisfy», and «refine» relationships.</li></ol></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/sysml-plugin/how-to-avoid-cyclic-dependencies-appearing-between-modules-when-sysml-allocate-satisfy-and-refine-relationships-connect-elements-residing-in-different-modules"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin">ParaMagic Plugin</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">ParaMagic v17.0.1 is incompatible with SysML v17.0.2 SP1</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic 17.0.1 does not support SysML 17.0.2 SP1 since all SysML Primitive Value Types were moved to the separate &quot;PrimitiveValueTypes&quot; package in order to comply with the SysML 1.3 specification. ParaMagic is dependent on the previous specification and is not finding the primitive value types where it expects to find them.<br /> Do not use SysML v17.0.2 with SP1 with ParaMagic v17.0.1.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/paramagic-v17-0-1-is-incompatible-with-sysml-v17-0-2-sp1"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have the ParaMagic plugin for MagicDraw. How do I access Mathematica to solve parametric equations?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There are three ways for ParaMagic to access Mathematica:</p><p>1. Mathematica is installed locally (on the same computer or a networked drive).</p><p>2. Mathematica is installed on an internal network as a web services provider. We can provide a web services interface for installation.</p><p>3. Evaluation configuration. ParaMagic (as initially installed) is set to access a NoMagic server copy of Mathematica for a 30 day evaluation period. After this, switch to method 1 or 2.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/i-have-the-paramagic-plugin-for-magicdraw-how-do-i-access-mathematica-to-solve-parametric-equations"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">ParaMagic needs Java 1.6 to run correctly. Can it run with Java 1.5?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic plugin uses specific Java 1.6 features and is not compatible with Java 1.5.</p><p>For MacOS, you may download java 1.6 update from Apple page (direct link is <a href="http://www.apple.com/downloads/macosx/apple/application_updates/ja">http://www.apple.com/downloads/macosx/apple/application_updates/ja</a> vaformacosx105 update1.html). Please note that this java is only for 64-bit Mac OS (as Mac Book Pro can have both 32 and 64 bit operating systems). For 32-bit Mac OS X, users can install SoyLatte JDK to run ParaMagic. For details on SoyLatte, go to: <a href="http://landonf.bikemonkey.">http://landonf.bikemonkey.</a> org/static/soylatte/</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/paramagic-needs-java-1-6-to-run-correctly-can-it-run-with-java-1-5"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can I learn more about ParaMagic?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Download evaluation copies of MagicDraw, the SysML, and ParaMagic plugins. Go through the demonstration models with help of ParaMagic tutorials. Free access to Mathematica as a web service is available over the Internet during the evaluation period.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/how-can-i-learn-more-about-paramagic"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How does ParaMagic differ from SysML simulations approaches?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Multiple approaches have been proposed, including code generation from state machine and activity diagrams and generation of Simulink models from SysML. Each approach has its applications, but ParaMagic provides a simple, flexible process with links to multiple solvers and data sources. Rather than being the best tool for creating a complex simulation of a small piece of a SysML model, it helps ties together system capabilities at the global level.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/how-does-paramagic-differ-from-sysml-simulations-approaches"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How does ParaMagic do requirements checking?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Quantitative requirements can be formulated as constraint statements, e.g. If(actual_weight required_weight, Then Result = True, Else Result = False) and incorporated in parametric dagrams. Every time the parametric simulation is executed, the constraint statement provides a clear answer for whether the requirement is being met. Integrating a requirements management tool like Cameo Req+ with MagicDraw and ParaMagic provides a powerful approach to creating, tracing and verifying requirements.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/how-does-paramagic-do-requirements-checking"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Can I use ParaMagic with UML, UPDM (DoDAF/MoDAF), or business process modeling languages?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The official specifications for these other profiles do not explicitly include Parametrics, but, in MagicDraw, SysML features can be linked to these kinds of models and ParaMagic simulations can be incorporated easily.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/can-i-use-paramagic-with-uml-updm-dodaf-modaf-or-business-process-modeling-languages"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How does the ParaMagic-Excel link work?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic allows data to be transferred between a SysML model instance and one or more Excel spreadsheets by creating a mapping between instance values and worksheet cells. The user can import initial data from spreadsheets into a model instance and, after running the simulation, export results to Excel for reports, graphing and further processing. Excel is not used by ParaMagic as a mathematical solver, however, so Mathematica and/or MATLAB is still required.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/how-does-the-paramagic-excel-link-work"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What mathematical solvers does ParaMagic link to?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic uses Mathematica from Wolfram Research or MATLAB from The MathWorks or a combination of the two. Solving standard mathematical equations embedded as constraints in SysML parametric diagrams requires Mathematica. Using MATLAB, constraints are written as external calls on MATLAB functions or scripts. Existing simulation models, functions and templates in MATLAB, Simulink or Mathematica can be incorporated directly into SysML models.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/what-mathematical-solvers-does-paramagic-link-to"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How does ParaMagic work?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic creates a constraint network from the parametric model using constraint graph and &quot;Composable Object&quot; algorithms developed at the Georgia Institute of Technology. &quot;Acausal&quot; networks often make it possible to solve the model in multiple directions, swapping inputs and outputs in the different model instances or at runtime. For example, calculate the weight of a system from its individual components, or calculate the weight allowance for a specific component from the overall system weight budget.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/how-does-paramagic-work"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What is ParaMagic?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>ParaMagic is a plugin for MagicDraw that extracts the parametric relationships in a SysML model, exports them to a mathematical solver program, and uploads the calculation results back into the SysML model. It handles simulation execution, solver management, and some display functions.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/what-is-paramagic"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What are Parametrics used for?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Parametrics insures data consistency within the SysML model and provides the potential for simulating model performance and comparing against system requirements. Possible usage areas:</p><p>Engineering projects: calculate cost, weight or power budgets, vehicle speed, component strength, and others.</p><p>Computer systems, calculate message traffic levels, database capacity needs, system availability, and others.</p><p>Business systems, calculate manpower needs or time to delivery.</p><p>Anything from &quot;ballpark&quot; estimates and &quot;sanity&quot; checks to detailed optimization, trade studies and sensitivity analysis can be organized throughout the development process.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/what-are-parametrics-used-for"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What is Parametrics?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Parametrics functionality allows SysML model-builders to include mathematical formulas as part of the model. Parametrics is part of the OMG SysML 1.0 specification.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/paramagic-plugin/what-is-parametrics"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/cameo-datahub">Cameo DataHub</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">DataHub 3.0 does not support detection and synchronization of changes to entity stereotypes</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When a synchronized entity is given a new stereotype, it will be treated as a new entity in DataHub and the eventual associations previously tied to it are lost. We are working on a Service Pack for DataHub 3.0 that will address and solve this limitation. Per current plans, the Service Pack will be released in mid-May 2009. Until the Service Pack is available, users can avoid the occurrence of this issue by not changing the stereotypes of entities after these have been imported in DataHub and associations created. Please note that the auto-numbering feature of SysML 16.5 plugin for MagicDraw adds new stereotypes to the SysML entities. Therefore these entities, if already imported in DataHub, will be treated as new ones after re-numbering.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-datahub/datahub-3-0-does-not-support-detection-and-synchronization-of-changes-to-entity-stereotypes"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">DataHub Console closed unexpectedly. This issue occurred on Windows 7 update (September 2014)</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Solution:<br /> To prevent DataHub Console from closing unexpectedly, add the following code into &lt;DataHub folder&gt;\datahubconsole\datahubconsole.ini</p><p>-vmargs<br /> -Dorg.eclipse.swt.browser.DefaultType=mozilla</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-datahub/datahub-console-closed-unexpectedly-this-issue-occurred-on-windows-7-update-september-2014"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/magicdraw-rsxconverter">MagicDraw RSXConverter</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Why the label/text on the relationship is not in a correct position?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can correct the label/text position for every relationship on the diagram by:</p><p>1. Select all elements in the diagram (press Ctrl + A).</p><p>2. Right Click on the diagram.</p><p>3. Select Paths.</p><p>4. Select Reset Labels Position.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rsxconverter/why-the-label-text-on-the-relationship-is-not-in-a-correct-position"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Why does the conversion stop with the message &quot;Cannot convert string &quot;&quot; to a double&quot;?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This could occur when the model file of RSA/RSM might not supply complete data for the conversion process. Most cases are caused by the element on the diagram.</p><p>To solve this problem, elements need to be relocated to get new coordinates.</p><p>Currently known elements are:</p><p>Separator line inside Alt Combined Fragment needs to be adjusted.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rsxconverter/why-does-the-conversion-stop-with-the-message-cannot-convert-string-to-a-double"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">The installation process seems to be complete, but I do not see any changes in my RSA/RSM.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Run Eclipse with the -clean option to solve this problem.</p><p>eclipse -clean</p><p>or modify eclipse.ini by adding the following line</p><p>-clean</p><p>to always start Eclipse with the -clean option.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rsxconverter/the-installation-process-seems-to-be-complete-but-i-do-not-see-any-changes-in-my-rsa-rsm"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What is MagicDraw RSXConverter?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw RConverter is a tool to convert IBM® Rational® Software Architect (RSA) or IBM® Rational® Software Modeler (RSM) file format (*.emx, .epx, .efx) to MagicDraw-supported file format (*.mdxml).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rsxconverter/what-is-magicdraw-rsxconverter"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter">MagicDraw RConverter</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How long does it take to convert the large model?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>It depends on the project size. For jdk1.4 APIs which contain about 3,000 classes, MagicDraw RConverter spent about 4 hours to convert (tested on Pentium4 2.8 MHz, RAM 512 Mbytes).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/how-long-does-it-take-to-convert-the-large-model"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is that possible for RConverter to convert IBM Rational Software Modeller without any constraints?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>No, it is not possible. RConverter can be used only for Rational Rose 2003 model converting.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/is-that-possible-for-rconverter-to-convert-ibm-rational-software-modeller-without-any-constraints"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What is the data format after conversion?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw 9.0 XMI. Such file can be opened with latest MagicDraw version.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/what-is-the-data-format-after-conversion"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Is it possible for RConverter to convert IBM Rational Software Modeler without any constraints?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>No, it is not possible. RConverter can only be used for Rational Rose 2003 model conversion. To convert RSA/RSM models, you will need to use RSXConverter.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/is-it-possible-for-rconverter-to-convert-ibm-rational-software-modeler-without-any-constraints"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Is that possible to use MagicDraw RConverter on Mac or Linux?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>No, MagicDraw RConverter is designed to run on Windows platform (tested on Window XP service pack 2).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/is-that-possible-to-use-magicdraw-rconverter-on-mac-or-linux"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What is the limitation for the evaluation of RConverter?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The evaluation version of MagicDraw RConverter is 30 days with the ability to convert up to 50 elements.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/what-is-the-limitation-for-the-evaluation-of-rconverter"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What is MagicDraw RConverter?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw RConverter is the tool to convert Rational Rose project (.mdl) to MagicDraw's readable file (.xml).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/magicdraw-rconverter/what-is-magicdraw-rconverter"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op">Cameo Inter-Op</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can I import a model from IBM® Rational® System Architect to MagicDraw?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please use Cameo Inter-Op to convert your model from the IBM® Rational® System Architect format to the MagicDraw format. For more information about Cameo Inter-Op features, see the &quot;<a href="https://docs.nomagic.com/products/cameo-inter-op">Cameo Inter-Op description</a>&quot; page.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op/how-can-i-import-a-model-from-ibm-rational-system-architect-to-magicdraw"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can I import a model from IBM® Rational® Rhapsody to MagicDraw?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please use Cameo Inter-Op to convert your model from the IBM® Rational® Rhapsody format to the MagicDraw format. For more information about Cameo Inter-Op features, see the &quot;<a href="https://docs.nomagic.com/products/cameo-inter-op">Cameo Inter-Op description</a>&quot; page.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op/how-can-i-import-a-model-from-ibm-rational-rhapsody-to-magicdraw"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can I check if the Cameo Inter-Op installation process is complete?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You can test Cameo Inter-Op by transforming a sample that is provided in a program from which you need to transform a model. For example, if it is a transformation from IBM® Rational® System Architect to MagicDraw, select DoDAF_Samples for the transformation.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op/how-can-i-check-if-the-cameo-inter-op-installation-process-is-complete"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I suspect that a performance issue can be solved by changing memory settings. How can I change it for Cameo Inter-Op?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To change memory settings, please perform the following steps:</p><ol><li>Open the &lt; Cameo Inter-Op installation directory &gt; \cameo\cameoiop.ini file for editing.</li><li>Change the values of the arguments shown in the following example :</li></ol><p>--launcher.XXMaxPermSize</p><p>512m</p><p>-vmargs</p><p>-Xms60m-Xmx512m</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op/i-suspect-that-a-performance-issue-can-be-solved-by-changing-memory-settings-how-can-i-change-it-for-cameo-inter-op"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I provide the IBM® Rational® System Architect model to the customer support team in case that the model is required to be used for the problem investigation?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please use the Sodius XML exporter to export your IBM® Rational® System Architect model to a format supported by MagicDraw and send the exported model to the customer support team &quot;<a href="http://download.sodius.com/files/cameo/sa/mdw-sa-xml-export-1.9.3.exe">Download the Sodius XML exporter</a>&quot; .</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameo-inter-op/how-can-i-provide-the-ibm-rational-system-architect-model-to-the-no-magic-customer-support-team-in-case-that-the-model-is-required-to-be-used-for-the-problem-investigation"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools">Interchange with Other Tools</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I import IBM Rational Rose files?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw RConverter is the tool to convert Rational Rose project (.mdl) to MagicDraw's readable file (.xml). You can download MagicDraw RConverter Evaluation version at <a href="http://www.nomagic.com">http://www.nomagic.com</a> in the download section.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools/how-can-i-import-ibm-rational-rose-files"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How can I import Borland Together files with MagicDraw 10.0 or later version?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To import Borland Together files you need to open XMI file with MagicDraw 9.5 version, save and then open with MagicDraw 10.0 or later version.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools/how-can-i-import-borland-together-files-with-magicdraw-10-0-or-later-version"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where I can find Export for Unisys XMI operations?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The MagicDraw 10.0 version or later does not have Export As Unisys XMI commands.</p><p>Unisys XMI is for UML 1.3, MagicDraw 10.0 or later uses UML2 metamodel.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools/where-i-can-find-export-for-unisys-xmi-operations"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I would like to find out whether it is possible to view a .vsd document in MagicDraw or even convert the .vsd file to MagicDraw format?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There is a Visio plug-in that allows you to export to XMI 1.0. This format is supported by MagicDraw.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools/i-would-like-to-find-out-whether-it-is-possible-to-view-a-vsd-document-in-magicdraw-or-even-convert-the-vsd-file-to-magicdraw-format"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How can I import IBM Rational Software Architect/Modeler files?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw RSXConverter is an eclipse plugin deployed in an RSA/RSM environment for exporting an RSA/RSM file format (*.emx, .efx, .epx) to a MagicDraw readable file format (.mdxml). You can download an evaluation version of MagicDraw RSXConverter at <a href="http://www.nomagic.com">http://www.nomagic.com</a> in download section.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/interchange-with-other-tools/how-can-i-import-ibm-rational-software-architect-modeler-files"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/plugins">Plugins</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Is DoDAF Plugin 2.0 compatible with DoDAF Plugin 1.0?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>DoDAF Plugin 2.0 is not compatible with DoDAF Plugin 1.0. Projects, created with DoDAF Plugin 1.0, cannot be opened with DoDAF Plugin 2.0 and vice versa.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/plugins/is-dodaf-plugin-2-0-compatible-with-dodaf-plugin-1-0"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to set up Eclipse for plug-in development?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><ol><li>Create Java Project.</li><li>Include all *.jar files from &quot;MagicDraw\lib&quot; folder into Project Build Path. Exclude &quot;md_commontw_api.jar&quot; and &quot;md_commontw.jar&quot;.</li><li>Write plug-in. Start from main Plug-in class by extending &quot;com.nomagic.magicdraw.plugins.Plugin&quot;.</li><li>Create Plug-in descriptor file &quot;plugin.xml&quot;.</li><li>Make clean plug-in directory in MagicDraw plug-ins directory (./plugins/ ), copy &quot;plugin.xml&quot; to it. Do not copy any binaries to MagicDraw plug-ins directory or they will have conflicts with your binaries in Eclipse.</li><li>Create new Debug configuration to run Application.</li><li>select &quot;Project&quot; your plug-in project.</li><li>search for Main class, select &quot;com.nomagic.magicdraw.Main&quot;.</li><li>add &quot;-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M&quot; to Arguments.</li><li>Apply changes.</li></ol><p>More details can be found in &quot;<a href="https://docs.nomagic.com/files/FreeFormDiagram_1_0.zip">MagicDraw Open API User Guide</a>&quot;</p><p>Hints:</p><p>- don't forget to include all sub folders from &quot;MagicDraw\lib&quot; into your Build Path;</p><p>- create jar file from Eclipse: use &quot;Export / JAR file&quot;;</p><p>- you wouldn't have to copy files each time if you will select destination jar file already in &quot;MagicDraw\plugins&quot; folder;</p><p>-save jar file description to build jar file later;</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/plugins/how-to-set-up-eclipse-for-plug-in-development"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I have created my own MagicDraw plugin with customer diagram, profile, templates and samples. How do I pack them to share for multiple users through MagicDraw Resources Manager.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Resource Manager needs more information which is stored in resource descriptor. It must know what files were installed because it must be able to perform uninstall operation.</p><p>I have attached our free form custom diagram. It would be best if you will look through this sample and I'll describe main rules for descriptor writing. You will find descriptor file in &quot;data/resourcemanager/MDR_Custom_Diagram_Free_Form_1513_descriptor.xml&quot;.</p><p>- xml tag</p><p>- &quot;id&quot; is most important. It must be unique. To prevent duplicates in future use &quot;22**&quot;, for example &quot;2201&quot;.</p><p>- &quot;name&quot; must be unique between all MagicDraw resources.</p><p>- &quot;type&quot; must be one of: &quot;Custom Diagram&quot;, &quot;Plugin&quot;, &quot;Profile&quot;, &quot;Sample&quot;, &quot;Template&quot;.</p><p>- is your resource version</p><p>- will be needed only if your resource depends on other resources.</p><p>- defines files which will be installed. Do not use &quot;*.*&quot; (all files in directory) in common directories like &quot; /samples&quot; because uninstalling your resource will remove all files from this directory!</p><p>- each tag defines one file which must be copied to &quot;MagicDraw root&quot; directory.</p><p>Descriptor file must be placed in your resource zip file in directory &quot;data/resourcemanager&quot; whith specific naming. Name of descriptor file is formed from values from tag: &quot;MDR_ _ _ _descriptor.xml&quot;, all spaces in names is replaced by underscore symbol &quot;_&quot;.</p><p><a href="https://docs.nomagic.com/files/FreeFormDiagram_1_0.zip">Resource sample you may find here</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/plugins/i-have-created-my-own-magicdraw-plugin-with-customer-diagram-profile-templates-and-samples-how-do-i-pack-them-to-share-for-multiple-users-through-magicdraw-resources-manager"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">SysML 16.5 SP2 has a modification of MD_customization_for_SysML.mdzip how to update MD_customization_for_SysML.mdzip in our Teamwork Server and successfully work with it?:</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>1. Login with appropriate right, preferable 'Administrator'.</p><p>2. Remove MD_customization_for_SysML.mdzip from your Teamwork Server.</p><p>3. Create a new SysML project.</p><p>4. Add the newly-created SysML project to Teamwork.</p><p>5. In the Add Project to Teamwork Settings dialog, select the Local Modules tab.</p><p>6. Ensure that the Action for MD_customization_for_SysML.mdzip is Add to Teamwork.</p><p>7. Click the Add button in the Add Project to Teamwork Settings dialog.</p><p>MD_customization_for_SysML.mdzip will be automatically updated in your Teamwork.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/plugins/sysml-16-5-sp2-has-a-modification-of-md-customization-for-sysml-mdzip-how-to-update-md-customization-for-sysml-mdzip-in-our-teamwork-server-and-successfully-work-with-it"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/documentation-help">Documentation/Help</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I find MagicDraw configuration files (md.log and several other files)?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>By default MagicDraw configuration and auxiliary files are stored in the user home directory</p><p>User home directory/.magicdraw/version.</p><p>Information about this location you may find in the MagicDraw About screen, Info tab (Help-&gt;About-&gt;Environment)</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/documentation-help/where-can-i-find-magicdraw-configuration-files-md-log-and-several-other-files"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">When invoking Help&gt;Contents the program hangs.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The &quot;Help&quot; may not be started because another application is using &quot;Help&quot; port. You may see this in the helpserver.log file, which is located in MagicDraw installation directory. If the server port is already in use, the java.rmi.server.ExportException appears in this file. To change Help port, you need to invoke the &quot;Environment Options&quot; dialog from the &quot;Options&quot; main menu. On the appeared dialog, &quot;General&quot; tab change the &quot;Help Server Port&quot;, submit changes and try to invoke Help again.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/documentation-help/when-invoking-help-contents-the-program-hangs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">MagicDraw Help cannot be invoked. What should I do?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Reasons why you cannot invoke the Help can be the following:</p><p>1. There is no reference to the topic, or a particular topic does not exist in MagicDraw Help. If a reference to the topic is broken, you can start the MagicDraw Help manually:</p><p>1.1. On the Help menu, click Help Content. The MagicDraw Help opens.</p><p>1.2. Browse in the help content or use a keyword to search for a particular topic.</p><p>Please let us know about broken links by contacting our customer support.</p><p>2. The communication with a server through Remote Method Invocation (RMI) is broken. Please do the following:</p><p>2.1. Open the mduml.properties<sup>*</sup> file. You can find the file in \bin.</p><p>2.2. To the JAVA_ARGS line, add a value -Dnostubfixing\=true, as it shown in the following example:</p><p>JAVA_ARGS=-Xmx1200M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -Dnostubfixing\=true</p><p>If the problem still persists, please contact our support team and attach the following files:</p><p>helpserver.log</p><p>md.log</p><p>You can find these files in one of the following ways:</p><p>Go to \.magicdraw\.</p><p>On the Help menu, click About MagicDraw. In the About dialog, select the Environment tab and then click the link next to Configuration Files.</p><p><sup>*</sup> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/documentation-help/magicdraw-help-cannot-be-invoked-what-should-i-do"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">The Java documentation, delivered with MagicDraw contains only some package.html files.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You may find full MagicDraw OpenAPI javadoc in <em>&lt;modeling tool installation directory&gt;\openapi\docs</em> or download from <a href="http://jdocs.nomagic.com/">http://jdocs.nomagic.com/</a><a href="http://jdocs.nomagic.com/">.</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/documentation-help/the-java-documentation-delivered-with-magicdraw-contains-only-some-package-html-files"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where can I find documentation about working with MagicDraw, MagicDraw integrations, floating license server, and teamwork server?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>All MagicDraw documentation is located in MagicDraw installation directory, manual folder. Also you may download it from the www.nomagic.com.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/documentation-help/where-can-i-find-documentation-about-working-with-magicdraw-magicdraw-integrations-floating-license-server-and-teamwork-server"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/older-versions">Older Versions</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I'm trying to run MagicDraw 3.5.1, but when I launch the application I get the error message &quot;Can't read/write to main.ini&quot;</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>When launching MagicDraw Version 3.5.1 or 3.6, you get the error message &quot;Can't read/write to main.ini&quot;, contact <a href="mailto:support@magicdraw.com">support@magicdraw.com</a>. We will send you a new main.ini file.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/older-versions/i-m-trying-to-run-magicdraw-3-5-1-but-when-i-launch-the-application-i-get-the-error-message-can-t-read-write-to-main-ini"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">When installing MagicDraw on Fedora Core 5, Suse 10.1, and later :error while loading shared libraries error appears</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>There are two ways to solve it:</p><p>1. Use no install version.</p><p>2. Modify install script file. Example with MD_UML_115_unix.sh:</p><p>cat MD_UML_115_unix.sh | sed 's/export LD_ASSUME_KERNEL/#xport LD_ASSUME_KERNEL/g' &gt; MD_UML_115_unix.sh2; mv MD_UML_115_unix.sh2 MD_UML_115_unix.sh</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/older-versions/when-installing-magicdraw-on-fedora-core-5-suse-10-1-and-later-error-while-loading-shared-libraries-error-appears"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/licensing">Licensing</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I connect to a network through the LAN or Wireless adapter. When I change the connection from LAN to wireless or vice versa, I get the message about the invalid license file, and MagicDraw closes. What should I do? </a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw licenses are locked to a particular computer using the network adapter’s MAC address. MagicDraw locks itself to the first MAC address in the list. On a Windows computer, the wireless is first by default. If you switch off the wireless, its MAC address is removed from the list and MagicDraw can no longer find it. In order to solve the invalid license problem, you need to change the network adapter order so that the LAN adapter is at the top of the adapters list. That way, the MAC address of the LAN adapter will always be the first in the list, even if you switch to the wireless connection.</p><p>To avoid this problem, you should configure your network settings to change the network adapters (connections) order on Windows XP, Windows Vista, and Windows 7 operating systems.</p><p>The following procedures explain how to configure your network settings on these operating systems:</p><p>Windows XP</p><ol><li>From the <strong>Control Panel</strong>, open the <strong>Network Connections</strong> dialog.</li><li>On the <strong>Advanced </strong>menu, click <strong>Advanced Settings</strong>. The <strong>Advanced Settings</strong> dialog opens.</li><li>Select the <strong>Adapters and Bindings</strong> tab, and, in the <strong>Connections</strong> list, select the LAN adapter and move it to the top of the list.</li></ol><p>Windows Vista*</p><ol><li>From the <strong>Control Panel</strong>, open the <strong>Network and Internet</strong> dialog.</li><li>Go to the <strong>Network and Sharing Center</strong> and, on the left side of the dialog, select <strong>Manage Network Connections</strong>.</li><li>On the menu, select <strong>Advanced</strong> &gt; <strong>Advanced Settings.</strong> The <strong>Advanced Settings</strong> dialog opens.<strong> Note: </strong>If you cannot see the menu bar,select<strong>Organize &gt; Layout &gt; Menu bar</strong>.</li><li>Select the <strong>Adapters and Bindings</strong> tab, and, in the <strong>Connections</strong> list, select the LAN adapter and move it to the top of the list.</li></ol><p>Windows 7*</p><ol><li>From the <strong>Control Panel</strong>, open the <strong>Network and Internet</strong> dialog.</li><li>Go to the <strong>Network and Sharing Center</strong> and, on the left side of the dialog, select <strong>Change adapter settings</strong>.</li><li>On the menu, select <strong>Advanced</strong> &gt; <strong>Advanced Settings. </strong>The <strong>Advanced Settings</strong> dialog opens.<strong> Note: </strong>If you cannot see the menu bar,select<strong>Organize &gt; Layout &gt; Menu bar</strong>.</li><li>Select the <strong>Adapters and Bindings</strong> tab, and, in the <strong>Connections</strong> list, select the LAN adapter and move it to the top of the list.</li></ol><p>* Depending on your Windows configurations, the command sequence may be slightly different.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/i-connect-to-a-network-through-the-lan-or-wireless-adapter-when-i-change-the-connection-from-lan-to-wireless-or-vice-versa-i-get-the-message-about-the-invalid-license-file-and-magicdraw-closes-what-should-i-do"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I'm requested to activate may MagicDraw licenses. What should I do?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Starting from MagicDraw v16.9 commercial licenses are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.</p><p>The commercial license activation is needed after the purchase transaction has been completed.</p><p>License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.</p><p>Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to www.nomagic.com and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.</p><p>For MagicDraw, plugins and other products activation instructions refer to: <a href="https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing">https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing</a><a href="https://docs.nomagic.com/display/MD190SP1/Modeling+tools+and+plugins+licensing">.</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/i-m-requested-to-activate-may-magicdraw-licenses-what-should-i-do"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I'm unable to unlock MagicDraw. &quot;Key or user name is invalid!&quot; message appears.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Make sure that MagicDraw software and unlock key are the same version. If you install the latest software, you must get the latest version unlock keys.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/i-m-unable-to-unlock-magicdraw-key-or-user-name-is-invalid-message-appears"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to unlock MagicDraw vesion 12.0 and later?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>After downloading MagicDraw, you will get an unlock key file to your mailbox.</p><p>1. Save this unlock key file, into the local file system before starting MagicDraw.</p><p>2. When starting MagicDraw for the first time you will be asked to browse for the unlock key file. Click the &quot;...&quot; button and select the file from the directory you saved the file.</p><p>3. System will automatically activate MagicDraw and you will be able to use it.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/how-to-unlock-magicdraw-vesion-12-0-and-later"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I have downloaded MagicDraw demo. Where do I get the unlock key?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Unlock key is sent to you automatically by email (to the e-mail address which you provided registering to www.nomagic.com).</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/i-have-downloaded-magicdraw-demo-where-do-i-get-the-unlock-key"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Installation on multiple machines is supported by the Mobile or Floating license.</p><p>More about Mobile User License could be found at<br /> <a href="http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html">http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html</a></p><p>More about Floating License could be found at<br /> <a href="http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html">http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html</a></p><p>Note: The Seat license can be used by a single user on a single installation.</p><p>If you have any questions about the licensing or purchasing, please feel free to contact your account executive or <a href="mailto:sales@nomagic.com">sales@nomagic.com</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/i-would-like-to-install-the-application-on-two-machines-but-the-only-one-instance-at-a-time-will-be-used-what-license-do-i-need"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">An additional floating license is reserved after switching from wired to wireless connection and back when MagicDraw is open. That license is released only after some time, but not instantly as I expect to. How can I fix this?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>This is a known issue and we are investigating on it. So far we recommend modifying the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.</p><p>To set the time-out:</p><p>1. Open the FlexNet installation directory, find the <em>cameo.opt</em> file and open it for edit. If you cannot find the file, create a new file and save it as <em>cameo.opt</em>.</p><p>2. Add to this file the following line:</p><p><samp>TIMEOUTALL 900</samp></p><p>3. Place the <em>cameo.opt</em> file in the same directory with the <em>cameo.exe</em> file. For example, <em>C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo</em>.</p><p>4. In the VENDOR line of the license file specify the relative path to the <em>cameo.opt</em> file so that the FlexNet server could find it.</p><p>For example,<br /><samp>VENDOR cameo licenses/cameo/cameo <strong>licenses/cameo/cameo.opt</strong> PORT=1101</samp></p><p>5. Restart the FlexNet server.</p><p>6. Open the <em>cameo.log</em> file to check that the <em>cameo.opt</em> file is added in the proper directory.</p><p>If the path to the file is like in the example of the 3rd step, you should see the corresponding text:<br /><samp><strong>14:44:35 (cameo) Using options file: &quot;licenses/cameo/cameo.opt&quot;</strong><br /> 14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise<br /> 14:44:35 (cameo) EXTERNAL FILTERS are OFF<br /> <strong>14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds</strong></samp></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/licensing/an-additional-floating-license-is-reserved-after-switching-from-wired-to-wireless-connection-and-back-when-magicdraw-is-open"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/users-profiles">Users Profiles</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Is my personal information secure at www.nomagic.com?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Yes, it is. Even having the username/password, the intruder won't be able to access the credit card information since we don't keep any credit card data in the database. Shopping cart works via HTTPS, therefore, it is impossible to sniff any data.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/users-profiles/is-my-personal-information-secure-at-www-nomagic-com"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Where can I change my profile data (user name, company name, etc.)?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p><a href="https://www.magicdraw.com/main.php?ts=login&amp;cmd_show_login=1&amp;show_confirm=1&amp;menu=login">Login to our website</a> with your username and password, click on Edit Personal Information right-side menu selection and edit your details.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/users-profiles/where-can-i-change-my-profile-data-user-name-company-name-etc"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What if I forgot my profile password?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Use our reminder service - enter your email and click the Send password button. New password will be generated and sent by email.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/users-profiles/what-if-i-forgot-my-profile-password"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/purchase">Purchase</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Where is my MagicDraw purchase information stored?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Purchased MagicDraw software installation files and unlock keys are stored under your personal profile. In order to download it, <a href="https://www.magicdraw.com/main.php?ts=login&amp;cmd_show_login=1&amp;show_confirm=1&amp;menu=login">login to our website</a> with your username and password, click on License List right-side menu selection.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/where-is-my-magicdraw-purchase-information-stored"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">I would like to receive notifications about the releases of new MagicDraw versions or service packs.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>If you want to subscribe to any of existing MagicDraw mailing list, <a href="https://www.magicdraw.com/main.php?ts=login&amp;cmd_show_login=1&amp;show_confirm=1&amp;menu=login">please login</a> to our web site <a href="http://www.nomagic.com">http://www.nomagic.com</a> with your username and password. Click on &quot;Mailing List' right side menu selection, check appropriate checkbox and click the Update button.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/i-would-like-to-receive-notifications-about-the-releases-of-new-magicdraw-versions-or-service-packs"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Bought one MagicDraw Floating license a month ago; and bought one more Floating license yesterday. I would like to know how can I add additional Floating license to the Floating license server.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>First of all open &quot;key.txt&quot; file located in floating license server installation directory. Then remove key from this file and restart server. After that enter new license key for floating license server. All keys you can re-obtain from your personal download area, by clicking button &quot;Send Unlock Keys&quot;: <a href="http://www.nomagic.com">http://www.nomagic.com</a></p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/bought-one-magicdraw-floating-license-a-month-ago-and-bought-one-more-floating-license-yesterday-i-would-like-to-know-how-can-i-add-additional-floating-license-to-the-floating-license-server"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">How do I get the product updates? Where do I download the newest software?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Notifications about updates will be sent by email. The newest software will be automatically added to your <a href="https://www.magicdraw.com/main.php?ts=login&amp;cmd_show_login=1&amp;show_confirm=1&amp;menu=login">personal download area</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/how-do-i-get-the-product-updates-where-do-i-download-the-newest-software"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Why do I need customer profile, why cannot I go to the shopping cart and order the software directly?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The registration operation and customer profile help us to make sure that you get customer support and discounts when purchasing our products later. Customers purchased software (unlock keys and installation files) also is stored under his/her personal profile.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/why-do-i-need-customer-profile-why-cannot-i-go-to-the-shopping-cart-and-order-the-software-directly"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Will I receive my software on CD?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Sorry, we don't have our software on CD. We deliver products electronically.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/purchase/will-i-receive-my-software-on-cd"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/other-issues">Other Issues</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">After MagicDraw installation, menu items are bold</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>The problem occurs, when during the installation, the default language is changed. This problem is related to Java 1.7.</p><p>The solution is to install MagicDraw* again without changing the default language. Then, you can change the languange after the installation. To do this, on the <strong>Options</strong> menu, click <strong>Environment</strong>, and then in the <strong>General</strong> options group, change the <strong>Language</strong> property.</p><p>* This is valid for all MagicDraw-based Cameo Suite products.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/after-magicdraw-installation-menu-items-are-bold"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">We have a document management application (built into .Net and IIS 6). When we open a MagicDraw document from the DM application, we get an error &quot;Page not found&quot;, even though the page is there.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>You have to add a mime type to the IIS configuration. For .mdxml, etc., assign a mime type of application/x-uml.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/we-have-a-document-management-application-built-into-net-and-iis-6-when-we-open-a-magicdraw-document-from-the-dm-application-we-get-an-error-page-not-found-even-though-the-page-is-there"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">The UML metamodel in UML_Standard_Profile.xml includes only metaclasses and no attributes. However, we need them for defining OCL constraints.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>MagicDraw uses the simplified metamodel profile that has no attributes visualized. But the attributes still exist in the code.</p><p>As a solution we suggest you to use the sample of the full metamodel profile, because it has no striped attributes. We use this profile mainly as a reference when writing OCL constraints.</p><p>Download the sample of the full metamodel profile, using the MagicDraw capabilities:</p><p>1. From the Help menu, select Resource/Plugin Manager.</p><p>2. Click the Check for Updates button.</p><p>3. Wait while the checking for updates is finished.</p><p>4. In the Filter box, choose All Resources.</p><p>5. In the product list, scroll down to the UML Standard Profile with attributes for OCL and select it.</p><p>6. Click the Download / Install button.</p><p>The full metamodel profile will be stored in the &quot; /samples&quot; directory.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/the-uml-metamodel-in-uml-standard-profile-xml-includes-only-metaclasses-and-no-attributes-however-we-need-them-for-defining-ocl-constraints"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How do I merge completely different projects that have no common history into one project (possibly by choosing only certain parts that should be merged)?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Merge functionality can be employed for this. Choose the Tools -&gt; Project Merge menu item, specify the source project (the project from which you want to port changes), the target project (the project to which you want to port changes), and an empty ancestor project. Then press the Merge button and you will be provided with the standard Merge dialog, which allows you choosing which changes should be merged-in.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/how-do-i-merge-completely-different-projects-that-have-no-common-history-into-one-project-possibly-by-choosing-only-certain-parts-that-should-be-merged"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">How to change the font size in various MagicDraw UI places?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Font and other UI style options can be changed by changing look&amp;feel theme (Metal theme should be used). It can be changed from the Options &gt; Look&amp;Feel &gt; Metal. Theme can be customized in theme customization dialog which can be opened from Options &gt; Look&amp;Feel &gt; Customize.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/how-to-change-the-font-size-in-various-magicdraw-ui-places"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">Installation file is identified as suspicious or infected by virus. What to do?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Please be sure that you got the installation file from <a href="http://www.nomagic.com">www.nomagic.com</a>.</p><p>In this case we can confirm our software is not infected by a virus and it is safe to use it.</p><p>One known reason why antivirus software in rare cases identifies *.exe files as suspicious is because of Norton antivirus software issues where a legitimate file is misidentified and subsequently quarantined. More can be found at <a href="http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&amp;tabid=2">http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&amp;tabid=2</a><a href="http://securityresponse.symantec.com/security_response/writeup.jsp?docid=2010-090201-1030-99&amp;tabid=2">. As they say in above document suspicious level is very low.</a></p><p>Workarounds for this issue are available. We suggest to:</p><ul><li>ignore suspicions from Norton antivirus.</li><li>use the &quot;no install&quot; installation (*_no_install.zip).</li><li>Symantec suggests disabling the auto protection option and checking if the issue is resolved.</li></ul><p>Let us know at <a href="mailto:support@nomagic.com">support@nomagic.com</a> if more help is required.</p><p>We are working with Norton antivirus to eliminate this issue.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/installation-file-is-identified-as-suspicious-or-infected-by-virus-what-to-do"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">Is it possible to add a hyperlink with a relative path to an image or a project file?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>A relative path begins at a current folder of the hierarchy (i.e., a project or MagicDraw installation) and specifies the file's location from there.</p><p>You add a hyperlink with a path relative to the MagicDraw installation folder. For example, the path <em><a href="file://sample.jpg">file://sample.jpg</a></em> refers to the image that is stored in the MagicDraw installation folder.</p><p>When creating a hyperlink to the file stored in the same folder with the project, a path relative to that location is always suggested. A relative path can also be specified manually. For example, the path <em><a href="file://MyPictures/sample.jpg">file://MyPictures/sample.jpg</a></em> refers to the picture stored in the My Pictures directory located in the same folder as the project.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/other-issues/is-it-possible-to-add-a-hyperlink-with-a-relative-path-to-an-image-or-a-project-file"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/cameomda">CameoMDA</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">I have out of memory problem.</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>To avoid out of memory problem, you need to select the output folder, which contains only the related source code, otherwise, the oAW engine will scan recursively all the files and sub folders in the selected output folder, and then parse the content of each file. This process will take a lot of memory and can cause of out of memory problem.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/cameomda/i-have-out-of-memory-problem"> Permalink</a></div></div></div></div></div></div><div class="subTopic_section"><h3 class="subTopic_sectionTitle"><a href="https://docs.nomagic.com/support/faq/specific-domains">Specific Domains</a></h3><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a class="topic_faqToggleLink" href="#">What your tool can offer from realtime and embedded systems modeling perspective?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>We have integrations and partners with third-party tools to support specific needs. <a href="http://www.sinelabore.com">http://www.sinelabore.com</a> is the tool which allows you to generates C, C++, C#, Ada or Objective-C code for embedded systems from our State machines.</p><p>CoFluent Studio plugin allows to integrate MagicDraw with CoFluent Studio. By exporting UML models to CoFluent Studio, designers can use C/C++ as action language and generate transaction-level modeling (TLM) SystemC code to run simulations. Co-Simulation with MATLAB/Simulink is also available. The instrumented SystemC code coupled with CoFluent Studio?s analysis tools allows designers to observe the real-time execution of their models and extract performance figures like latencies, data throughputs, buffer levels, resource loads, power consumption, memory footprint and cost.</p><p>CoFluent Studio targets complex multiprocessor systems with rich application content, whether they are:</p><ul><li>Multi-board (large equipments, distributed/networked systems)</li><li>On-board (embedded systems)</li><li>On-chip (SoC, FPGA, ASIC, ASSP)</li></ul><p>Additionally, we are working on our own Simulation Toolkit which allows to run discrete event simulation and supports executable UML standards like W3C SCXML for State Machines and OMG fUML for Activities. Feel free to request demo or additional information at <a href="mailto:support@nomagic.com">support@nomagic.com</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/specific-domains/what-your-tool-can-offer-from-realtime-and-embedded-systems-modeling-perspective"> Permalink</a></div></div></div></div></div><div class="topic_faqBlock faq_open"><div class="topic_faqPresentation"><a href="#" class="topic_faqToggleLink">What capabilities does your tool offer for model execution and result analysis?</a></div><div class="topic_faqAnswerWrapper"><div class="topic_faqAnswerWrapper_inner"><div class="faq_text clearfix"><p>Model execution and simulation capabilities are provided in Cameo Simulation Toolkit for MagicDraw. This tool supports STANDARD BASED Statemachines, Activities, SysML parametrics execution, and quick UI prototyping based on MagicDraw User Interface Modeling diagram.</p><p>For more information about Cameo Simulation Toolkit <a href="https://docs.nomagic.com/product-addons/magicdraw-addons/cameo-simulation-toolkit">please visit here</a>.</p></div><div class="faq_tools clearfix"><div class="faq_links"><a href="https://docs.nomagic.com/support/faq/specific-domains/what-capabilities-does-your-tool-offer-for-model-execution-and-result-analysis"> Permalink</a></div></div></div></div></div></div>
````

<!--NOMAGIC_PAGE id=68526717 space=FAQ version=6 -->
## PAGE 00060: FlexNet License Server and Floating License

- page_id: `68526717`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/68526717/FlexNet+License+Server+and+Floating+License
- version_number: 6
- version_date: `2021-03-05T15:52:49.674+01:00`
- ancestors: Frequently Asked Questions
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="81449daf-da2c-4b6e-aab0-4810c492c6e8" /></p>
````

<!--NOMAGIC_PAGE id=70389760 space=FAQ version=2 -->
## PAGE 00061: Floating License (Copy)

- page_id: `70389760`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70389760/Floating+License+Copy
- version_number: 2
- version_date: `2021-01-29T14:15:11.426+01:00`
- ancestors: Current FAQ for Review
- labels: []

### NORMALIZED CONTENT

#### EXPAND: How to return the floating license if two licenses are used by the same user on the same PC?

How to return the floating license if two licenses are used by the same user on the same PC?

When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.

By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.

To force the server to return lingering licenses earlier, it is necessary to modify the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.

To set the time-out:

1. Open the FlexNet installation directory, find the *cameo.opt* file and open it for edit. If you cannot find the file, create a new file and save it as *cameo.opt*.

2. Add to this file the following line:

TIMEOUTALL 900

3. Place the *cameo.opt* file in the same directory with the *cameo.exe* file. For example, *C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo*.

4. In the VENDOR line of the license file specify the relative path to the *cameo.opt* file so that the FlexNet server could find it.

For example, 
VENDOR cameo licenses/cameo/cameo **licenses/cameo/cameo.opt** PORT=1101

5. Restart the FlexNet server.

6. Open the *cameo.log* file to check that the *cameo.opt* file is added in the proper directory.

If the path to the file is like in the example of the 3rd step, you should see the corresponding text: 
**14:44:35 (cameo) Using options file: "licenses/cameo/cameo.opt"** 
14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise 
14:44:35 (cameo) EXTERNAL FILTERS are OFF 
**14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds**

#### EXPAND: How to release a hanging license to the pool?

How to release a hanging license to the pool?

There are several methods how to release license:

1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf)

2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. Follow the link http://:8080 to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.

3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf)

#### EXPAND: [To Be Reviewed]How to reset the lmadmin password, if a user cannot connect to a server using a web interface

[To Be Reviewed]How to reset the lmadmin password, if a user cannot connect to a server using a web interface

1. From *<flexnet license server installation directory>\conf*, open the *server.xml* file for editing.

2. In the line

<user firstName="System" id="admin" lastName="Administrator" password="(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ" passwordExpired="false" privileges="admin" type="local-admin"/>

change the password key value to "aa" as shown in the following example:

<user firstName="System" id="admin" lastName="Administrator" password="aa" passwordExpired="false" privileges="admin" type="local-admin"/>

3. Restart *lmadmin* (end the *lmadmin* process and start it again manually).

4. Connect to the FlexNet server (the default address is http://<server_name>:8090) with the following credentials:

User Name: *admin* 
Password: *aa*

5. In the **User Configuration** tab, click **Edit**, enter a new password and save it.

#### EXPAND: Where can I find lmgrid or lmadmin log file?

Where can I find lmgrid or lmadmin log file?

The location of the log file depends on what license server manager you use.

- If it is lmgrid , the cameo.log and lmgrid.log files can both be found directly in the root package of the lmgrid installation.
- If it is lmadmin , the cameo.log file can be found in <lmadmin installation directory>\logs , for example, C:\Program Files\FlexNet Publisher License Server Manager\logs .

**Note:** The default location of the log file can be changed during the product configuration.

#### EXPAND: I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?

I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?

You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.

In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.

Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf)

#### EXPAND: [To Be Reviewed]On new key application into FLEXnet licenses server lmadmin error appears – "Inconsistent server host name in: licenses\cameo\…

[To Be Reviewed]On new key application into FLEXnet licenses server lmadmin error appears – "Inconsistent server host name in: licenses\cameo\…

This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.

Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.

#### EXPAND: License Server Manager Not Starting

License Server Manager Not Starting

The license server manager will not start if either of the following ports are in use:

* Default license server port (no ports in range 27000 to 27009 available)

* Default HTTP port for the license server manager user interface (port 8080)

#### EXPAND: I have firewall blocking the connection to the FLEXnet license server. What ports are used?

I have firewall blocking the connection to the FLEXnet license server. What ports are used?

By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.

#### EXPAND: [To Be Reviewed]I got error "File not found, cameo.exe" what to do?

[To Be Reviewed]I got error "File not found, cameo.exe" what to do?

As the log says, "File not found, cameo.exe". So the lmadmin cannot find the daemon. There are two reasons / solutions:

- Maybe you have put the daemon cameo.exe in another folder.

Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.

- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from [https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download](https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download)

#### EXPAND: When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?

When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?

Such an error appears when:

The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.

Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.

You may check and change the port number in the FLEXnet license administrator console.

#### EXPAND: I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.

I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.

Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.

#### EXPAND: What command-line options are available with lmadmin?

What command-line options are available with lmadmin?

You can find list of the options by issuing the following command at the command prompt:

>lmadmin -help

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="70d54ade-daf7-4327-9645-861fe7b13814"><ac:parameter ac:name="title">How to return the floating license if two licenses are used by the same user on the same PC?</ac:parameter><ac:rich-text-body><p>When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.</p><p>By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.</p><p>To force the server to return lingering licenses earlier, it is necessary to modify the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.</p><p>To set the time-out:</p><p>1. Open the FlexNet installation directory, find the <em>cameo.opt</em> file and open it for edit. If you cannot find the file, create a new file and save it as <em>cameo.opt</em>.</p><p>2. Add to this file the following line:</p><p><samp style="margin-left: 30.0px;">TIMEOUTALL 900</samp></p><p>3. Place the <em>cameo.opt</em> file in the same directory with the <em>cameo.exe</em> file. For example, <em>C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo</em>.</p><p>4. In the VENDOR line of the license file specify the relative path to the <em>cameo.opt</em> file so that the FlexNet server could find it.</p><p style="margin-left: 30.0px;">For example,<br /><samp>VENDOR cameo licenses/cameo/cameo <strong>licenses/cameo/cameo.opt</strong> PORT=1101</samp></p><p>5. Restart the FlexNet server.</p><p>6. Open the <em>cameo.log</em> file to check that the <em>cameo.opt</em> file is added in the proper directory.</p><p style="margin-left: 30.0px;">If the path to the file is like in the example of the 3rd step, you should see the corresponding text:<br /><samp><strong>14:44:35 (cameo) Using options file: &quot;licenses/cameo/cameo.opt&quot;</strong><br />14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise<br />14:44:35 (cameo) EXTERNAL FILTERS are OFF<br /><strong>14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds</strong></samp></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="3f00f17b-b497-4c00-aec7-68197a2087c2"><ac:parameter ac:name="title">How to release a hanging license to the pool?</ac:parameter><ac:rich-text-body><p>There are several methods how to release license:</p><p>1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf</a></p><p>2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. Follow the link http://:8080 to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.</p><p>3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf</a></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="7edbcc4f-2aa1-4c3a-9384-5aab00784f30"><ac:parameter ac:name="title">[To Be Reviewed]How to reset the lmadmin password, if a user cannot connect to a server using a web interface</ac:parameter><ac:rich-text-body><p>1. From <em>&lt;flexnet license server installation directory&gt;\conf</em>, open the <em>server.xml</em> file for editing.</p><p>2. In the line</p><p><span>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</span></p><p>change the password key value to <span>&quot;aa&quot;</span> as shown in the following example:</p><p><span>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;aa&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</span></p><p>3. Restart <em>lmadmin</em> (end the <em>lmadmin</em> process and start it again manually).</p><p>4. Connect to the FlexNet server (the default address is http://&lt;server_name&gt;:8090) with the following credentials:</p><p>User Name: <em>admin</em><br />Password: <em>aa</em></p><p>5. In the <strong>User Configuration</strong> tab, click <strong>Edit</strong>, enter a new password and save it.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="eecefb9b-3c0e-4c40-9e30-4b17c6b785be"><ac:parameter ac:name="title">Where can I find lmgrid or lmadmin log file?</ac:parameter><ac:rich-text-body><p>The location of the log file depends on what license server manager you use.</p><ul><li>If it is <em>lmgrid</em>, the <em>cameo.log</em> and<em> lmgrid.log</em> files can both be found directly in the root package of the lmgrid installation.</li><li>If it is <em>lmadmin</em>, the <em>cameo.log</em> file can be found in <em>&lt;lmadmin installation directory&gt;\logs</em>, for example, <em>C:\Program Files\FlexNet Publisher License Server Manager\logs</em>.</li></ul><p><strong>Note:</strong> The default location of the log file can be changed during the product configuration.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="594aa135-da4f-4e03-93f6-a41a25e17d35"><ac:parameter ac:name="title">I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?</ac:parameter><ac:rich-text-body><p>You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.</p><p>In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.</p><p>Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf</a></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="2c9218da-8b07-4c94-9ee2-c01b3e7de203"><ac:parameter ac:name="title">[To Be Reviewed]On new key application into FLEXnet licenses server lmadmin error appears – &quot;Inconsistent server host name in: licenses\cameo\…</ac:parameter><ac:rich-text-body><p>This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.</p><p>Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="de18ba2a-db45-433e-8c97-b4aae2c6780c"><ac:parameter ac:name="title">License Server Manager Not Starting</ac:parameter><ac:rich-text-body><p>The license server manager will not start if either of the following ports are in use:</p><p>* Default license server port (no ports in range 27000 to 27009 available)</p><p>* Default HTTP port for the license server manager user interface (port 8080)</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="b0ce3cb2-7c47-4713-afe0-d0078931751e"><ac:parameter ac:name="title">I have firewall blocking the connection to the FLEXnet license server. What ports are used?</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="683b9095-780b-43b3-bdac-80b22279a2ed"><ac:parameter ac:name="title">[To Be Reviewed]I got error &quot;File not found, cameo.exe&quot; what to do?</ac:parameter><ac:rich-text-body><p>As the log says, &quot;File not found, cameo.exe&quot;. So the lmadmin cannot find the daemon. There are two reasons / solutions:</p><p>- Maybe you have put the daemon cameo.exe in another folder.</p><p>Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.</p><p>- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from <a href="https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download">https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download</a></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="57fac7a7-784b-4230-9e27-a45eb8c6af47"><ac:parameter ac:name="title">When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?</ac:parameter><ac:rich-text-body><p>Such an error appears when:</p><p>The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.</p><p>Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.</p><p>You may check and change the port number in the FLEXnet license administrator console.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="b67e1489-1dcc-4cff-ab0e-a5f08148d53d"><ac:parameter ac:name="title">I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="daaf7857-c97c-49b4-9bed-e48638b7d24b"><ac:parameter ac:name="title">What command-line options are available with lmadmin?</ac:parameter><ac:rich-text-body><p>You can find list of the options by issuing the following command at the command prompt:</p><p>&gt;lmadmin -help</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=47094960 space=FAQ version=18 -->
## PAGE 00062: Frequently Asked Questions

- page_id: `47094960`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/47094960/Frequently+Asked+Questions
- version_number: 18
- version_date: `2025-10-10T11:49:30.849+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

#### TIP: Welcome to the Frequently Asked Questions site!

Welcome to the Frequently Asked Questions site!

Got a question? Use a search field to find answers or solutions.

50%

##### Troubleshooting

- [CONFLUENCE_PAGE title='FlexNet License Server and Floating License' space='']
- Magic Collaboration Studio / Teamwork Cloud and Services

##### Need more help?

- [CONFLUENCE_PAGE title='Support' space='SUP']

##### Other resources

- Webinars
- Demo

50%

##### Recently updated articles

page,blogpost10true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e2caa0ec-1ae6-4fb7-b5f7-302fb655d9c1"><ac:parameter ac:name="title">Welcome to the Frequently Asked Questions site!</ac:parameter><ac:rich-text-body><p><span>Got a question? Use a search field to find answers or solutions.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="section" ac:schema-version="1" ac:macro-id="d343bb0f-074a-4f6a-8531-5526de34d5fc"><ac:rich-text-body><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="de61d45c-eb3a-4ada-95f9-e7a6dc769885"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><h3>Troubleshooting</h3><ul><li data-uuid="f8966809-c3db-46c2-bf09-dd02bbc3d5c2"><ac:link><ri:page ri:content-title="FlexNet License Server and Floating License" /><ac:plain-text-link-body><![CDATA[Flexnet License Server]]></ac:plain-text-link-body></ac:link></li><li data-uuid="cefd403d-ef2c-4991-a29d-0423bb05dced"><a href="https://docs.nomagic.com/MCS/?contextKey=faq-and-troubleshooting&amp;version=latest&amp;variant=default">Magic Collaboration Studio / Teamwork Cloud and Services</a></li></ul><h3>Need more help?</h3><ul><li data-uuid="20caea11-6905-4ab1-adf8-78ffa5eb8ef6"><ac:link><ri:page ri:space-key="SUP" ri:content-title="Support" /><ac:plain-text-link-body><![CDATA[Contact Support]]></ac:plain-text-link-body></ac:link></li></ul><h3>Other resources</h3><ul><li data-uuid="5080e561-fc6e-4166-804d-3112989de091"><a href="https://www.nomagic.com/events/webinars">Webinars</a></li><li data-uuid="d9c7a7af-ac77-4525-93af-7258fdf0fa04"><a href="https://www.youtube.com/channel/UC_vJmsXpI4uY9yfpFpb0NwA">Demo</a></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="column" ac:schema-version="1" ac:macro-id="077153aa-ba2c-4186-9277-13b335849309"><ac:parameter ac:name="width">50%</ac:parameter><ac:rich-text-body><p><br /></p><h3>Recently updated articles</h3><p><ac:structured-macro ac:name="recently-updated" ac:schema-version="1" ac:macro-id="58a00b80-f56e-4a54-89e8-c9ae90c19e4d"><ac:parameter ac:name="types">page,blogpost</ac:parameter><ac:parameter ac:name="max">10</ac:parameter><ac:parameter ac:name="spaces"><ri:space ri:space-key="FAQ" /></ac:parameter><ac:parameter ac:name="hideHeading">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=70395814 space=FAQ version=1 -->
## PAGE 00063: From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?

- page_id: `70395814`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395814/From+time+to+time+we+receive+Out+Of+Memory+exceptions.+I+suspect+that+these+exceptions+are+caused+by+MagicDraw+memory+leaks.+How+would+you+suggest+solving+this+problem
- version_number: 1
- version_date: `2021-03-03T14:08:47.800+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.

In order to analyze and fix the issue, more information is required. Please provide us with the following information:

1. Can you reproduce the problem? If yes, what are the steps to reproduce it?
2. If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.
3. Send us the memory dump file. It may help to detect the problem.

To create a memory dump file, please do the following:

1. In the properties* file, append JAVA_ARGS parameters as follows: -XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots
2. Start your modeling tool.

The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.

*

- For MagicDraw, the properties file is magcdraw.properties ( mduml.properties for MagicDraw version 17.0.4 or earlier).
- For Cameo Enterprise Architecture, the properties files is cameoea.properties .
- For Cameo Systems Modeleer, the properties files is csm.properties .
- For Cameo Business Modeler, the properties file is csm.properties .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.</p><p>In order to analyze and fix the issue, more information is required. Please provide us with the following information:</p><ol><li>Can you reproduce the problem? If yes, what are the steps to reproduce it?</li><li>If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.</li><li>Send us the memory dump file. It may help to detect the problem.</li></ol><p>To create a memory dump file, please do the following:</p><ol><li>In the properties* file, append JAVA_ARGS parameters as follows:<br />-XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots</li><li>Start your modeling tool.</li></ol><p>The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.</p><p> </p><hr /><p>*</p><ul><li> For MagicDraw, the properties file is<em> magcdraw.properties</em> (<em>mduml.properties</em> for MagicDraw version 17.0.4 or earlier).</li><li>For Cameo Enterprise Architecture, the properties files is <em>cameoea.properties</em>.</li><li>For Cameo Systems Modeleer, the properties files is <em>csm.properties</em>. </li><li>For Cameo Business Modeler, the properties file is <em>csm.properties</em>.</li></ul>
````

<!--NOMAGIC_PAGE id=111218775 space=FAQ version=23 -->
## PAGE 00064: How do I convert unreadable characters to readable in any text field in Cameo DataHub

- page_id: `111218775`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/111218775/How+do+I+convert+unreadable+characters+to+readable+in+any+text+field+in+Cameo+DataHub
- version_number: 23
- version_date: `2024-09-23T07:30:10.226+02:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: []

### NORMALIZED CONTENT

**Question**:

How do I convert unreadable characters to readable in any text field in Cameo DataHub? 
 
[IMAGE alt='' src='']

**Answer:**Unreadable characters are displayed in Cameo DataHub when you import information containing non-English language characters. These unreadable characters can appear anywhere in the modeling tool. You can convert the unreadable content into readable by modifying the <installation directory/bin/modelingtoolname.properties> file (e.g:magicdraw.properties) and adding the**Dfile.encoding=UTF-8** value to the **JAVA_ARGS**parameter, as shown below. Restart the application after modifications. This modification will not affect any other aspect of the modeling tool. 
 
[IMAGE alt='' src='']

By default, the**Dfile.encoding=UTF-8**encoding isadded to the **JAVA_ARGS**parameter from version 2022xR1.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Question</strong>:</p><p>How do I convert unreadable characters to readable in any text field in Cameo DataHub?<br /><br /><ac:image><ri:attachment ri:filename="CDH_Panel.PNG" /></ac:image></p><p><strong>Answer:<br /><br /></strong>Unreadable characters are displayed in Cameo DataHub when you <span style="color: rgb(23,43,77);">import information containing non-English language characters.</span> These unreadable characters can appear anywhere in the modeling tool. You can convert the unreadable content into readable by modifying the &lt;installation directory/bin/modelingtoolname.properties&gt; file (e.g:magicdraw.properties) and adding the<strong> Dfile.encoding=UTF-8</strong> value to the <strong>JAVA_ARGS </strong>parameter, as shown below. Restart the application after modifications. This modification will not affect any other aspect of the modeling tool.<br /><br /><ac:image ac:width="1200"><ri:attachment ri:filename="Code.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c87a088a-f1f4-48db-94bf-e533a68a3af3"><ac:rich-text-body><p><span style="letter-spacing: 0.0px;">By default, the </span><strong style="letter-spacing: 0.0px;">Dfile.encoding=UTF-8 </strong><span style="letter-spacing: 0.0px;">encoding is </span>added to the <strong>JAVA_ARGS </strong>parameter from version 2022xR1.</p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=70395802 space=FAQ version=2 -->
## PAGE 00065: How do I know what version of JVM I am running?

- page_id: `70395802`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395802/How+do+I+know+what+version+of+JVM+I+am+running
- version_number: 2
- version_date: `2022-07-14T13:37:03.868+02:00`
- ancestors: Frequently Asked Questions > Java Virtual Machine (JVM)
- labels: []

### NORMALIZED CONTENT

You may find this information in the About window (Help menu -> About)

or

If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You may find this information in the About window (Help menu -&gt; About)</p><p>or</p><p>If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=198379031 space=FAQ version=1 -->
## PAGE 00066: How to add a data source for JAMA Connect using the OAuth 2.0 authentication type?

- page_id: `198379031`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379031/How+to+add+a+data+source+for+JAMA+Connect+using+the+OAuth+2.0+authentication+type
- version_number: 1
- version_date: `2024-11-25T07:44:11.482+01:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to add a data source for JAMA Connect using the OAuth 2.0 authentication type?

**Answer**:

To learn more about how toadd a data source for JAMA Connect using the OAuth 2.0 authentication type, refer to[CONFLUENCE_PAGE title='Adding Data Sources for JAMA Connect' space='CDH2024xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Question: </strong></p><p style="">How t<span style="color: rgb(23,43,77);">o a</span><span style="color: rgb(23,43,77);">dd a data source for JAMA Connect using the OAuth 2.0 authentication type?</span></p><p style=""><strong>Answer</strong>:</p><p style="">To learn more about how to<span> </span><span style="color: rgb(23,43,77);">a</span><span style="color: rgb(23,43,77);">dd a data source for JAMA Connect using the OAuth 2.0 authentication type, refer to<span> </span></span><ac:link><ri:page ri:space-key="CDH2024xR2" ri:content-title="Adding Data Sources for JAMA Connect" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=198379026 space=FAQ version=1 -->
## PAGE 00067: How to add a self-signed certificate to DNG?

- page_id: `198379026`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379026/How+to+add+a+self-signed+certificate+to+DNG
- version_number: 1
- version_date: `2024-11-25T07:42:03.558+01:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to add a self-signed certificate to DNG?

**Answer:**

To learn more about how to add a self-signed certificate to DNG, refer to[CONFLUENCE_PAGE title='Server Certificates' space='MD2024xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Question:<span> </span></strong></p><p style="">How to add a self-signed certificate to DNG?</p><p style=""><strong>Answer:</strong><span> </span></p><p style="">To learn more about how to add a self-signed certificate to DNG, refer to<span> </span><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Server Certificates" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=70395793 space=FAQ version=1 -->
## PAGE 00068: How to change JVM version?

- page_id: `70395793`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395793/How+to+change+JVM+version
- version_number: 1
- version_date: `2021-03-03T14:03:58.516+01:00`
- ancestors: Frequently Asked Questions > Java Virtual Machine (JVM)
- labels: []

### NORMALIZED CONTENT

1. Go to <modeling tool installation directory>\bin and open the <modeling tool>.properties file (eg., magicdraw.properties , csm.properties , cameoea.properties ) for editing. If you are using modeling tools of version 17.0.4 or earlier, the name of the property file is mduml.properties .
2. In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144

NOTE: Integrated modelling tools runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that the modeling tool integrates with. If you are running the software integrated with IDE, read the appropriate readme.html for specific integration, found in the *integrations* folder.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ol><li>Go to <em>&lt;modeling tool installation directory&gt;\bin</em> and open the <em>&lt;modeling tool&gt;.properties</em> file (eg., <em>magicdraw.properties</em>, <em>csm.properties</em>, <em>cameoea.properties</em>) for editing. If you are using modeling tools of version 17.0.4 or earlier, the name of the property file is <em>mduml.properties</em>.</li><li>In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144</li></ol><p> </p><p>NOTE: Integrated modelling tools runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that the modeling tool integrates with. If you are running the software integrated with IDE, read the appropriate readme.html for specific integration, found in the <em>integrations</em> folder.</p>
````

<!--NOMAGIC_PAGE id=70402531 space=FAQ version=2 -->
## PAGE 00069: How to check for the wrong file permissions after Teamwork Cloud installation and fix the installation by changing file permissions to the correct ones

- page_id: `70402531`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70402531/How+to+check+for+the+wrong+file+permissions+after+Teamwork+Cloud+installation+and+fix+the+installation+by+changing+file+permissions+to+the+correct+ones
- version_number: 2
- version_date: `2021-03-29T13:24:18.972+02:00`
- ancestors: Frequently Asked Questions > Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

In the Teamwork Cloud installation instructions provided for 18.5 SP1, SP2, SP3, SP4, 19.0 GA, SP1, SP2, SP3, SP4 versions, we recommended using a too wide-ranged permission 777, resulting in a vulnerability in computers. Therefore, we have updated the installation instructions and scripts.

The updated installation instructions are available at:

**19.0 SP4:**

- Installation on Linux using scripts

**19.0 SP3:**

- Installation on Linux using scripts

**19.0 SP2:**

- Installation on Linux using scripts

**19.0 SP1:**

- Installation on Linux using scripts

**19.0 GA:**

- Installation on Linux using scripts

**18.5 SP4:**

- Installation on Linux RedHat and CentOS 7.x

**18.5 SP3:**

- Installation on Linux RedHat and CentOS 7.x

**18.5 SP2:**

- Installation on Linux RedHat and CentOS 7.x

**18.5 SP1:**

- Installation on Linux RedHat and CentOS 7.x
- Installation on Centos 7.x

Check your Teamwork Cloud installation for the incorrect permission and fix it using the following instructions.

There are two places where the incorrect permissions can be found if the old installation scripts were used.

1. The file /etc/environment.

**a. How to check for the problem?**

Execute the command

*stat /etc/environment*

If the problem exists, the result access permission will be shown like the following.

Access: (0777/-rwxrwxrwx)

**b. How to fix the problem?**

Execute the following command to change the permission to 644.

*chmod 644 /etc/environment*

2. The folder /home/twcloud

This is a home folder of the user, twcloud, created from installation helper script.

**a. How to check for the problem**

Execute the command

*stat /home/twcloud*

If the problem exists, the result access permission will be shown like the following.

Access: (0777/drwxrwxrwx)

**b. How to fix the problem?**

We recommend revoking the write and execute permission from group (g) and any other user (o).

Execute the following command to do so.

*chmod -R g-wx,o-wx /home/twcloud*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>In the Teamwork Cloud installation instructions provided for 18.5 SP1, SP2, SP3, SP4, 19.0 GA, SP1, SP2, SP3, SP4 versions, we recommended using a too wide-ranged permission 777, resulting in a vulnerability in computers. Therefore, we have updated the installation instructions and scripts. </p><p>The updated installation instructions are available at:</p><p><strong style="letter-spacing: 0.0px;">19.0 SP4:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud190SP4/Installation+on+Linux+using+scripts">Installation on Linux using scripts</a></li></ul><p><strong>19.0 SP3:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud190SP3/Installation+on+Linux+using+scripts">Installation on Linux using scripts</a></li></ul><p><strong style="letter-spacing: 0.0px;">19.0 SP2:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud190SP2/Installation+on+Linux+using+scripts">Installation on Linux using scripts</a></li></ul><p><strong style="letter-spacing: 0.0px;">19.0 SP1:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud190SP1/Installation+on+Linux+using+scripts">Installation on Linux using scripts</a></li></ul><p><strong style="letter-spacing: 0.0px;">19.0 GA:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud190/Installation+on+Linux+using+scripts">Installation on Linux using scripts</a></li></ul><p><strong style="letter-spacing: 0.0px;">18.5 SP4:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud185SP4/Installation+on+Linux+RedHat+and+CentOS+7.x">Installation on Linux RedHat and CentOS 7.x</a></li></ul><p><strong style="letter-spacing: 0.0px;">18.5 SP3:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud185SP3/Installation+on+Linux+RedHat+and+CentOS+7.x">Installation on Linux RedHat and CentOS 7.x</a></li></ul><p><strong style="letter-spacing: 0.0px;">18.5 SP2:</strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud185SP2/Installation+on+Linux+RedHat+and+CentOS+7.x">Installation on Linux RedHat and CentOS 7.x</a></li></ul><p><strong>18.5 SP1: </strong></p><ul><li><a href="https://docs.nomagic.com/display/TWCloud185SP1/Installation+on+Linux+RedHat+and+CentOS+7.x">Installation on Linux RedHat and CentOS 7.x</a></li><li><a href="https://docs.nomagic.com/display/TWCloud185SP1/Installation+on+Centos+7.x">Installation on Centos 7.x</a></li></ul><p>Check your Teamwork Cloud installation for the incorrect permission and fix it using the following instructions.</p><p>There are two places where the incorrect permissions can be found if the old installation scripts were used.</p><p>1. The file /etc/environment.</p><p style="margin-left: 30.0px;"><strong>a. How to check for the problem?</strong></p><p style="margin-left: 30.0px;">Execute the command</p><p style="margin-left: 60.0px;"><em>stat /etc/environment</em></p><p style="margin-left: 30.0px;">If the problem exists, the result access permission will be shown like the following.</p><p style="margin-left: 60.0px;">Access: (0777/-rwxrwxrwx)</p><p style="margin-left: 30.0px;"><strong>b. How to fix the problem?</strong></p><p style="margin-left: 30.0px;">Execute the following command to change the permission to 644.</p><p style="margin-left: 60.0px;"><em>chmod 644 /etc/environment</em></p><p> </p><p>2. The folder /home/twcloud</p><p>This is a home folder of the user, twcloud, created from installation helper script. </p><p style="margin-left: 30.0px;"><strong>a. How to check for the problem</strong></p><p style="margin-left: 30.0px;">Execute the command</p><p style="margin-left: 60.0px;"><em>stat /home/twcloud</em></p><p style="margin-left: 30.0px;">If the problem exists, the result access permission will be shown like the following.</p><p style="margin-left: 30.0px;">Access: (0777/drwxrwxrwx)</p><p style="margin-left: 30.0px;"><strong>b. How to fix the problem?</strong></p><p style="margin-left: 30.0px;">We recommend revoking the write and execute permission from group (g) and any other user (o).</p><p style="margin-left: 30.0px;">Execute the following command to do so.</p><p style="margin-left: 60.0px;"><em>chmod -R g-wx,o-wx /home/twcloud</em></p>
````

<!--NOMAGIC_PAGE id=198379019 space=FAQ version=2 -->
## PAGE 00070: How to enable image import from DNG?

- page_id: `198379019`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379019/How+to+enable+image+import+from+DNG
- version_number: 2
- version_date: `2024-11-25T07:40:03.255+01:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to enable image import from DNG?

**Answer:**

To learn more about how to enable image import from DNG, refer to[CONFLUENCE_PAGE title='HTML images, RTF, and OLE support' space='CDH2024xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Question:<span> </span></strong></p><p>How to enable image import from DNG? </p><p><strong>Answer:</strong></p><p>To learn more about how to enable image import from DNG, refer to<span> </span><ac:link><ri:page ri:space-key="CDH2024xR2" ri:content-title="HTML images, RTF, and OLE support" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=198379024 space=FAQ version=1 -->
## PAGE 00071: How to enable OLE object support for IBM Doors?

- page_id: `198379024`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379024/How+to+enable+OLE+object+support+for+IBM+Doors
- version_number: 1
- version_date: `2024-11-25T07:41:23.208+01:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to enable OLE object support for IBM Doors?

**Answer:**

To learn more about how to enable image import from DNG, refer to[CONFLUENCE_PAGE title='HTML images, RTF, and OLE support' space='CDH2024xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Question:<span> </span></strong></p><p style="">How to enable OLE object support for IBM Doors?</p><p style=""><strong>Answer:</strong><span> </span></p><p style="">To learn more about how to enable image import from DNG, refer to<span> </span><ac:link><ri:page ri:space-key="CDH2024xR2" ri:content-title="HTML images, RTF, and OLE support" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=70395748 space=FAQ version=1 -->
## PAGE 00072: How to install my modeling tool in a silent mode, i.e., without the installer GUI?

- page_id: `70395748`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395748/How+to+install+my+modeling+tool+in+a+silent+mode+i.e.+without+the+installer+GUI
- version_number: 1
- version_date: `2021-03-03T13:18:16.912+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

Please start the installer with the following parameters: 
-i silent -DUSER_INSTALL_DIR=

The example:

MD_UML_169_win.exe -i silent "-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9" 
MagicDraw will be installed silently, with a default configuration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>Please start the installer with the following parameters:<br />-i silent -DUSER_INSTALL_DIR=</p><p>The example:</p><p>MD_UML_169_win.exe -i silent &quot;-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9&quot;<br />MagicDraw will be installed silently, with a default configuration.</p>
````

<!--NOMAGIC_PAGE id=185729238 space=FAQ version=8 -->
## PAGE 00073: How to maintain the order of requirements  when synchronizing from the DOORS to the modeling tool

- page_id: `185729238`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/185729238/How+to+maintain+the+order+of+requirements+when+synchronizing+from+the+DOORS+to+the+modeling+tool
- version_number: 8
- version_date: `2024-09-03T11:06:26.009+02:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to maintain the order of requirements when synchronizing from the DOORS to the modeling tool

**Answer:**

In the Schema Map Manager dialog, map the requirement **Id**on the modeling side to the **Object Number(Readonly)** on the DOORS side.**[IMAGE alt='' src='']**

As the Object Number is a read-only property, following the same process when synchronizing the requirements from the modeling tool to the DOORS will not give you the same results.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Question: </strong></p><p>How to maintain the order of requirements when synchronizing from the DOORS to the modeling tool</p><p><strong>Answer:</strong></p><p>In the Schema Map Manager dialog, map the requirement <strong>Id </strong>on the modeling side to the <strong>Object Number(Readonly)</strong> on the DOORS side.<strong><br /><br /><ac:image><ri:attachment ri:filename="Schema Map Manager.png" /></ac:image><br /></strong></p><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5f446ba4-6026-405b-ab59-8f1c8d325f2e"><ac:rich-text-body><p>As the Object Number is a read-only property, following the same process when synchronizing the requirements from the modeling tool to the DOORS will not give you the same results.</p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=70395762 space=FAQ version=3 -->
## PAGE 00074: How to release a hanging license to the pool?

- page_id: `70395762`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395762/How+to+release+a+hanging+license+to+the+pool
- version_number: 3
- version_date: `2022-07-14T11:15:27.709+02:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

There are several methods how to release license:

1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing)

2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. Use the default address (http://localhost:8090/) or your server name (http://<server name>:8090) to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.

3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>There are several methods how to release license:</p><p>1. There is a way to configure the license manager to automatically reclaim inactive licenses by creating the options file with specified TIMEOUT feature. Default TIMEOUT feature has a minimum license release time of 900 seconds, which means your license will not be checked back into the pool before 15 minutes of inactivity has elapsed. License Administration Guide with the instructions how to create an options file is available at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing</a></p><p>2. Restart the license server itself. First stop the server from the Administration section of the license server management interface. <span style="color: rgb(62,63,64);">Use the default address (</span><span class="nolink">http://localhost:8090/</span><span style="color: rgb(62,63,64);">) or your server name (http://&lt;server name&gt;:8090)</span> to connect to licenses server interface. Please note that stopping server shut downs and all vendor daemons. Active users will be notified and reconnect to license server would be needed. Start license server manually. On Windows platforms, open the installation directory in Windows Explorer and then double-click the lmadmin.exe file. Or run the lmadmin command with your desired command-line arguments on Unix platforms.</p><p>3. In order to release a hung license to the pool of free licenses please use lmremove command-line argument. Note that lmadmin's default setting disables the operation of lmremove, to enable it start lmadmin with the - allowLicenseReclaim argument. License Administration Guide with the instructions how to combine command line arguments is available at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing</a></p>
````

<!--NOMAGIC_PAGE id=70395765 space=FAQ version=1 -->
## PAGE 00075: How to reset the lmadmin password, if a user cannot connect to a server using a web interface

- page_id: `70395765`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395765/How+to+reset+the+lmadmin+password+if+a+user+cannot+connect+to+a+server+using+a+web+interface
- version_number: 1
- version_date: `2021-03-03T13:56:59.039+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

1. From *<flexnet license server installation directory>\conf*, open the *server.xml* file for editing.

2. In the line

<user firstName="System" id="admin" lastName="Administrator" password="(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ" passwordExpired="false" privileges="admin" type="local-admin"/>

change the password key value to "aa" as shown in the following example:

<user firstName="System" id="admin" lastName="Administrator" password="aa" passwordExpired="false" privileges="admin" type="local-admin"/>

3. Restart *lmadmin* (end the *lmadmin* process and start it again manually).

4. Connect to the FlexNet server (the default address is http://<server_name>:8090) with the following credentials:

User Name: *admin* 
Password: *aa*

5. In the **User Configuration** tab, click **Edit**, enter a new password and save it.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>1. From <em>&lt;flexnet license server installation directory&gt;\conf</em>, open the <em>server.xml</em> file for editing.</p><p>2. In the line</p><p>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;(ENC-01)K86frDi5qtLwVo2R+jXtOV1WakoJaaqqgFqNvGLy91OVdbhJ&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</p><p>change the password key value to &quot;aa&quot; as shown in the following example:</p><p>&lt;user firstName=&quot;System&quot; id=&quot;admin&quot; lastName=&quot;Administrator&quot; password=&quot;aa&quot; passwordExpired=&quot;false&quot; privileges=&quot;admin&quot; type=&quot;local-admin&quot;/&gt;</p><p>3. Restart <em>lmadmin</em> (end the <em>lmadmin</em> process and start it again manually).</p><p>4. Connect to the FlexNet server (the default address is http://&lt;server_name&gt;:8090) with the following credentials:</p><p>User Name: <em>admin</em><br />Password: <em>aa</em></p><p>5. In the <strong>User Configuration</strong> tab, click <strong>Edit</strong>, enter a new password and save it.</p>
````

<!--NOMAGIC_PAGE id=70395759 space=FAQ version=2 -->
## PAGE 00076: How to return the floating license if two licenses are used by the same user on the same PC?

- page_id: `70395759`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395759/How+to+return+the+floating+license+if+two+licenses+are+used+by+the+same+user+on+the+same+PC
- version_number: 2
- version_date: `2021-03-03T13:57:17.257+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.

By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.

To force the server to return lingering licenses earlier, it is necessary to modify the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.

To set the time-out:

1. Open the FlexNet installation directory, find the *cameo.opt* file and open it for edit. If you cannot find the file, create a new file and save it as *cameo.opt*.

2. Add to this file the following line:

TIMEOUTALL 900

3. Place the *cameo.opt* file in the same directory with the *cameo.exe* file. For example, *C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo*.

4. In the VENDOR line of the license file specify the relative path to the *cameo.opt* file so that the FlexNet server could find it.

For example, 
VENDOR cameo licenses/cameo/cameo **licenses/cameo/cameo.opt** PORT=1101

5. Restart the FlexNet server.

6. Open the *cameo.log* file to check that the *cameo.opt* file is added in the proper directory.

If the path to the file is like in the example of the 3rd step, you should see the corresponding text: 
**14:44:35 (cameo) Using options file: "licenses/cameo/cameo.opt"** 
14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise 
14:44:35 (cameo) EXTERNAL FILTERS are OFF 
**14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When a user moves between two subnets (for example, between two WiFi networks) and the user's PC gets different IP addresses, the Floating License connection is lost. Then, when users re-connect to the Floating License Server they get a second Floating License. This results in two licenses being checked out, but only one is actually in use and the other license is inactive.</p><p>By default, the inactive license stays checked out for approximately 2 hours. You can return the inactive license manually, or you can configure the server to return the license after 15 min.</p><p>To force the server to return lingering licenses earlier, it is necessary to modify the server heart-beat option to release license in 15 minutes. You need to free inactive licenses by setting the time-out.</p><p>To set the time-out:</p><p>1. Open the FlexNet installation directory, find the <em>cameo.opt</em> file and open it for edit. If you cannot find the file, create a new file and save it as <em>cameo.opt</em>.</p><p>2. Add to this file the following line:</p><p><samp style="margin-left: 30.0px;">TIMEOUTALL 900</samp></p><p>3. Place the <em>cameo.opt</em> file in the same directory with the <em>cameo.exe</em> file. For example, <em>C:\Program Files (x86)\FlexNet Publisher License Server Manager\licenses\cameo</em>.</p><p>4. In the VENDOR line of the license file specify the relative path to the <em>cameo.opt</em> file so that the FlexNet server could find it.</p><p style="margin-left: 30.0px;">For example,<br /><samp>VENDOR cameo licenses/cameo/cameo <strong>licenses/cameo/cameo.opt</strong> PORT=1101</samp></p><p>5. Restart the FlexNet server.</p><p>6. Open the <em>cameo.log</em> file to check that the <em>cameo.opt</em> file is added in the proper directory.</p><p style="margin-left: 30.0px;">If the path to the file is like in the example of the 3rd step, you should see the corresponding text:<br /><samp><strong>14:44:35 (cameo) Using options file: &quot;licenses/cameo/cameo.opt&quot;</strong><br />14:44:35 (cameo) Server started on panda for: MagicDrawEnterprise<br />14:44:35 (cameo) EXTERNAL FILTERS are OFF<br /><strong>14:44:35 (cameo) ALL FEATURES: INACTIVITY TIMEOUT set to 900 seconds</strong></samp></p>
````

<!--NOMAGIC_PAGE id=70395737 space=FAQ version=1 -->
## PAGE 00077: How to run MagicDraw under Unix after installation?

- page_id: `70395737`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395737/How+to+run+MagicDraw+under+Unix+after+installation
- version_number: 1
- version_date: `2021-03-03T13:07:16.994+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

Run mduml* file, which is located in MagicDraw installation directory, bin folder.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>Run mduml* file, which is located in MagicDraw installation directory, bin folder.</p><p> </p><p>* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p>
````

<!--NOMAGIC_PAGE id=198379028 space=FAQ version=1 -->
## PAGE 00078: How to work with Global Configs for DNG?

- page_id: `198379028`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379028/How+to+work+with+Global+Configs+for+DNG
- version_number: 1
- version_date: `2024-11-25T07:42:44.876+01:00`
- ancestors: Frequently Asked Questions > Cameo DataHub
- labels: ['kb-how-to-article']

### NORMALIZED CONTENT

**Question:**

How to work with Global Configs for DNG?

**Answer:**

To learn more about how to work with Global Configs for DNG, refer to[CONFLUENCE_PAGE title='Configuration Management' space='CDH2024xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Question:<span> </span></strong></p><p style="">How to work with Global Configs for DNG?</p><p style=""><strong>Answer:</strong><span> </span></p><p style="">To learn more about how to work with Global Configs for DNG, refer to<span> </span><ac:link><ri:page ri:space-key="CDH2024xR2" ri:content-title="Configuration Management" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=198379020 space=FAQ version=2 -->
## PAGE 00079: How-to articles

- page_id: `198379020`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/198379020/How-to+articles
- version_number: 2
- version_date: `2024-11-25T07:39:54.584+01:00`
- ancestors: Frequently Asked Questions
- labels: []

### NORMALIZED CONTENT

800c5af0-1ed9-42ff-9b5f-8b86b2f21f87com.atlassian.confluence.plugins.confluence-knowledge-base:kb-how-to-article-blueprintAdd how-to article

800c5af0-1ed9-42ff-9b5f-8b86b2f21f87com.atlassian.confluence.plugins.confluence-knowledge-base:kb-how-to-article-blueprintkb-how-to-articleProvide step-by-step guidance for completing a task.How-to articleAdd how-to articlekb-how-to-article

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: right;"><ac:structured-macro ac:name="create-from-template" ac:schema-version="1" ac:macro-id="c9c68b68-3b57-49f5-910c-1b030b2d3a9b"><ac:parameter ac:name="contentBlueprintId">800c5af0-1ed9-42ff-9b5f-8b86b2f21f87</ac:parameter><ac:parameter ac:name="blueprintModuleCompleteKey">com.atlassian.confluence.plugins.confluence-knowledge-base:kb-how-to-article-blueprint</ac:parameter><ac:parameter ac:name="createButtonLabel">Add how-to article</ac:parameter></ac:structured-macro></p><hr /><p><ac:structured-macro ac:name="content-report-table" ac:schema-version="1" ac:macro-id="fb7bac01-29f5-4359-a322-f84a9117f8b4"><ac:parameter ac:name="contentBlueprintId">800c5af0-1ed9-42ff-9b5f-8b86b2f21f87</ac:parameter><ac:parameter ac:name="blueprintModuleCompleteKey">com.atlassian.confluence.plugins.confluence-knowledge-base:kb-how-to-article-blueprint</ac:parameter><ac:parameter ac:name="analyticsKey">kb-how-to-article</ac:parameter><ac:parameter ac:name="blankDescription">Provide step-by-step guidance for completing a task.</ac:parameter><ac:parameter ac:name="blankTitle">How-to article</ac:parameter><ac:parameter ac:name="spaces"><ri:space ri:space-key="FAQ" /></ac:parameter><ac:parameter ac:name="createButtonLabel">Add how-to article</ac:parameter><ac:parameter ac:name="labels">kb-how-to-article</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=70395788 space=FAQ version=1 -->
## PAGE 00080: I cannot start the lmadmin application as a root. The FlexNet license server does not start on Linux.

- page_id: `70395788`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395788/I+cannot+start+the+lmadmin+application+as+a+root.+The+FlexNet+license+server+does+not+start+on+Linux.
- version_number: 1
- version_date: `2021-03-03T14:01:42.045+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">Please run the lmadmin application as a non-privileged user. Lmadmin has a restriction does not allowing it to start by the root user.</span></p>
````

<!--NOMAGIC_PAGE id=70395782 space=FAQ version=1 -->
## PAGE 00081: I got error "File not found, cameo.exe" what to do?

- page_id: `70395782`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395782/I+got+error+File+not+found+cameo.exe+what+to+do
- version_number: 1
- version_date: `2021-03-03T14:00:39.236+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

As the log says, "File not found, cameo.exe". So the lmadmin cannot find the daemon. There are two reasons / solutions:

- Maybe you have put the daemon cameo.exe in another folder.

Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.

- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from [https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download](https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>As the log says, &quot;File not found, cameo.exe&quot;. So the lmadmin cannot find the daemon. There are two reasons / solutions:</p><p>- Maybe you have put the daemon cameo.exe in another folder.</p><p>Add the Vendor daemon into the installed server. If you are using lmadmin, create licenses/cameo directories under and place the Vendor daemon file cameo.exe under ..../ /licenses/cameo.</p><p>- Maybe you do not have this file, then you can download the Vendor daemon - cameo.exe for your OS from <a class="external-link" href="https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download" rel="nofollow">https://secure.nomagic.com/show_content/download/?content=vendor_daemon_download</a></p>
````

<!--NOMAGIC_PAGE id=70395780 space=FAQ version=1 -->
## PAGE 00082: I have firewall blocking the connection to the FLEXnet license server. What ports are used?

- page_id: `70395780`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395780/I+have+firewall+blocking+the+connection+to+the+FLEXnet+license+server.+What+ports+are+used
- version_number: 1
- version_date: `2021-03-03T14:00:10.395+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">By default 1101 and 27000-27009 ports are used. Range of ports 27000-27009 can be changed to any single port. One port is enough but it must be specified explicitly in lmadmin configuration.</span></p>
````

<!--NOMAGIC_PAGE id=70394578 space=FAQ version=1 -->
## PAGE 00083: I have installed and activated one of your modelling tools as the administrator, logged into my regular account, and tool asked for a license key again. How can I escape the license activation on the same machine twice?

- page_id: `70394578`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70394578/I+have+installed+and+activated+one+of+your+modelling+tools+as+the+administrator+logged+into+my+regular+account+and+tool+asked+for+a+license+key+again.+How+can+I+escape+the+license+activation+on+the+same+machine+twice
- version_number: 1
- version_date: `2021-02-22T16:30:52.952+01:00`
- ancestors: Frequently Asked Questions > FAQ archive > Archived Licensing
- labels: []

### NORMALIZED CONTENT

**I have installed and activated one of your modelling tools as the administrator. When I had logged into my regular account, my modeling tool asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?**

The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.

The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.

You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).

For the instructions on how to change the configuration files directory, please find the issue "In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?"

Note: It is important to know that the MagicDraw seat license can be used by a single user only.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>I have installed and activated one of your modelling tools as the administrator. When I had logged into my regular account, my modeling tool asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?</strong></p><p>The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.</p><p>The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.</p><p>You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).</p><p>For the instructions on how to change the configuration files directory, please find the issue &quot;In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?&quot;</p><p>Note: It is important to know that the MagicDraw seat license can be used by a single user only.</p>
````

<!--NOMAGIC_PAGE id=70395811 space=FAQ version=3 -->
## PAGE 00084: I suspect a performance problem. How do I solve it

- page_id: `70395811`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395811/I+suspect+a+performance+problem.+How+do+I+solve+it
- version_number: 3
- version_date: `2022-12-28T07:53:34.362+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: ['performance']

### NORMALIZED CONTENT

To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:

**Generating a log file when the modeling tool freezes or performs slowly:**

1. When a modeling tool runs slowly or freezes, open*<modeling tool installation directory>\bin,* and run *submit_issue.exe* several times. It dumps threads into the log file.

2. Click **Help** > **About** on the main menu of your modeling tool. In the open dialog, select the **Environment** tab and click the **Log File** link. The log file opens.[*](https://www.nomagic.com/support/faq#path)

3. Save the file and register an issue. Click **Help** >**Report an Issue** on the main menu of your modeling tool

*If a modeling tool is inactive, as of version 17.0.4, log file is stored in the following location:

- Windows Vista/7/8 C:\Users\<USERNAME>\AppData\Local\.magicdraw\<md.version.number>
- Windows 2000/XP C:\Documents and Settings\<USERNAME>\Local Settings\Application Data\.magicdraw\<md.version.number>
- Windows NT4 C:\WINNT\Profiles\<USERNAME>\Local Settings\Application Data\.magicdraw\<md.version.number>
- Other OS: <user.home>/.magicdraw/<md.version.number>

**By using Java VisualVM:**

Modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.

The following steps outline how to obtain the data from VisualVM:

**Note.**Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.

**On Windows OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Task Manager .
3. Start Java VisualVM . If you selected the default location on the JDK installation process, VisualVM is located in C:\Program Files\Java\jdk<version number>\bin\ jvisualvm.exe . Otherwise, start the exe from your customized location.
4. Start the modeling tool.
5. In Task Manager , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Task Manager ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details, including the email address where the ticket link will be sent, and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team.

**On Mac OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Activity Monitor .
3. Start Java VisualVM . If you selected the default location on the JDk installation process, VisualVM is located in /Library/Java/JavaVirtualMachines/jdk<version number>.jdk /Contents/Home/bin/jvisualvm . Otherwise, start **jvisualvm** from your customized location.
4. Start the modeling tool.
5. In Activity Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Activity Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished and click the Stop button.
10. In the CPU samples tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the *.nps file.
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details including the email address where the ticket link will be sent and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team.

**On Linux OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start System Monitor .
3. To start Java VisualVM , execute the jvisualvm tool from the bin directory of the JDK. When the tool runs, the Java VisualVM window opens.
4. Start the modeling tool.
5. In System Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in System Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. To register an issue, open the modeling tool. On the main menu, click Help > Report an Issue. The Report an Issue dialog opens.
13. Fill out all necessary details including the email address where the ticket link will be sent and click Send . You will receive an email containing the ticket link in your inbox.
14. Open the email and click the ticket link. Attach the *.nps file to send the issue to the support team.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:</p><p><strong>Generating a log file when the modeling tool freezes or performs slowly:</strong></p><p>1. When a modeling tool runs slowly or freezes, open<em> &lt;modeling tool installation directory&gt;\bin,</em> and run <em>submit_issue.exe</em> several times. It dumps threads into the log file.</p><p>2. Click <strong>Help</strong> &gt; <strong>About</strong> on the main menu of your modeling tool. In the open dialog, select the <strong>Environment</strong> tab and click the <strong>Log File</strong> link. The log file opens.<a href="https://www.nomagic.com/support/faq#path" class="external-link" rel="nofollow">*</a></p><p>3. Save the file and register an issue. Click <strong>Help</strong> &gt;<strong> Report an Issue</strong> on the main menu of your modeling tool</p><p>*If a modeling tool is inactive, as of version 17.0.4, log file is stored in the following location:</p><ul><li>Windows Vista/7/8 <em>C:\Users\&lt;USERNAME&gt;\AppData\Local\.magicdraw\&lt;md.version.number&gt;</em></li><li>Windows 2000/XP <em>C:\Documents and Settings\&lt;USERNAME&gt;\Local Settings\Application Data\.magicdraw\&lt;md.version.number&gt;</em></li><li>Windows NT4 <em>C:\WINNT\Profiles\&lt;USERNAME&gt;\Local Settings\Application Data\.magicdraw\&lt;md.version.number&gt;</em></li><li>Other OS: <em>&lt;user.home&gt;/.magicdraw/&lt;md.version.number&gt;</em> </li></ul><p><strong>By using Java VisualVM:</strong></p><p style="text-align: justify;">Modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.</p><p style="text-align: justify;">The following steps outline how to obtain the data from VisualVM:</p><p><strong>Note. </strong>Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.</p><p><strong>On Windows OS:</strong></p><ol><li><a class="external-link" href="http://www.oracle.com/technetwork/java/javase/downloads/index.html" rel="nofollow">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a title="Follow link" class="external-link" href="https://visualvm.github.io/" rel="nofollow">https://visualvm.github.io/</a>.</li><li>Start <strong>Task Manager</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDK installation process, VisualVM is located in <em>C:\Program Files\Java\jdk&lt;version number&gt;\bin\ jvisualvm.exe</em>. Otherwise, start the <em>exe</em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Task Manager</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Task Manager</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details, including the email address where the ticket link will be sent, and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team.</li></ol><p><strong>On Mac OS:</strong></p><ol><li><a class="external-link" href="http://www.oracle.com/technetwork/java/javase/downloads/index.html" rel="nofollow">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a title="Follow link" class="external-link" href="https://visualvm.github.io/" rel="nofollow">https://visualvm.github.io/</a>.</li><li>Start <strong>Activity Monitor</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDk installation process, VisualVM is located in <em>/Library/Java/JavaVirtualMachines/jdk&lt;version number&gt;.jdk /Contents/Home/bin/jvisualvm</em>. Otherwise, start <em><strong>jvisualvm</strong></em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Activity Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Activity Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished and click the Stop button.</li><li>In the CPU <strong>samples</strong> tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.</li><li>To save the snapshot, right-click it and select Save As to save the <em>*.nps</em> file.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details including the email address where the ticket link will be sent and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team.</li></ol><p><strong>On Linux OS:</strong></p><ol><li><a class="external-link" href="http://www.oracle.com/technetwork/java/javase/downloads/index.html" rel="nofollow">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/" class="external-link" title="Follow link" rel="nofollow">https://visualvm.github.io/</a>.</li><li>Start <strong>System Monitor</strong>.</li><li>To start <strong>Java VisualVM</strong>, execute the <strong>jvisualvm</strong> tool from the <strong>bin</strong> directory of the JDK. When the tool runs, the <strong>Java VisualVM</strong> window opens.</li><li>Start the modeling tool.</li><li>In <strong>System Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>System Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>To register an issue, open the modeling tool. On the main menu, click <strong>Help</strong> &gt; <strong>Report an Issue. The Report an Issue dialog opens.</strong></li><li>Fill out all necessary details including the email address where the ticket link will be sent and click <strong>Send</strong>. You will receive an email containing the ticket link in your inbox.</li><li>Open the email and click the ticket link. Attach the <em>*.nps</em> file to send the issue to the support team.</li></ol>
````

<!--NOMAGIC_PAGE id=70395799 space=FAQ version=4 -->
## PAGE 00085: I would like to increase java heap size that MagicDraw would run faster with larger models

- page_id: `70395799`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395799/I+would+like+to+increase+java+heap+size+that+MagicDraw+would+run+faster+with+larger+models
- version_number: 4
- version_date: `2021-05-03T11:10:23.437+02:00`
- ancestors: Frequently Asked Questions > Java Virtual Machine (JVM)
- labels: []

### NORMALIZED CONTENT

###### I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.

You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties* file, in the line:

JAVA_ARGS=-Xmx800M

The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.

On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.

For more information, see [CONFLUENCE_PAGE title='Memory allocation' space='MD2021x'].

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h4>I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.</h4><p>You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties* file, in the line:</p><p>JAVA_ARGS=-Xmx800M</p><p>The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.</p><p>On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.</p><p>For more information, see <ac:link><ri:page ri:space-key="MD2021x" ri:content-title="Memory allocation" /></ac:link>.</p><p> </p><p>* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p>
````

<!--NOMAGIC_PAGE id=70395755 space=FAQ version=1 -->
## PAGE 00086: I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?

- page_id: `70395755`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395755/I+would+like+to+install+the+application+on+two+machines+but+the+only+one+instance+at+a+time+will+be+used.+What+license+do+I+need
- version_number: 1
- version_date: `2021-03-03T13:46:53.599+01:00`
- ancestors: Frequently Asked Questions > FAQ archive > Archived Licensing
- labels: []

### NORMALIZED CONTENT

Installation on multiple machines is supported by the Mobile or Floating license.

More about Mobile User License could be found at 
[http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html](https://www.nomagic.com/resources/sales-and-licenses/mobile-licensing)

More about Floating License could be found at 
[http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html](https://www.nomagic.com/resources/sales-and-licenses/floating-licensing)

Note: The Seat license can be used by a single user on a single installation.

If you have any questions about the licensing or purchasing, please feel free to contact your account executive or [sales@nomagic.com](mailto:sales@nomagic.com).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>Installation on multiple machines is supported by the Mobile or Floating license.</p><p>More about Mobile User License could be found at<br /><a class="external-link" href="https://www.nomagic.com/resources/sales-and-licenses/mobile-licensing" rel="nofollow">http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html</a></p><p>More about Floating License could be found at<br /><a class="external-link" href="https://www.nomagic.com/resources/sales-and-licenses/floating-licensing" rel="nofollow">http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html</a></p><p>Note: The Seat license can be used by a single user on a single installation.</p><p>If you have any questions about the licensing or purchasing, please feel free to contact your account executive or <a href="mailto:sales@nomagic.com" class="external-link" rel="nofollow">sales@nomagic.com</a>.</p>
````

<!--NOMAGIC_PAGE id=70395752 space=FAQ version=1 -->
## PAGE 00087: I'm requested to activate my modeling tool license. What should I do?

- page_id: `70395752`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395752/I+m+requested+to+activate+my+modeling+tool+license.+What+should+I+do
- version_number: 1
- version_date: `2021-03-03T13:19:34.115+01:00`
- ancestors: Frequently Asked Questions > FAQ archive > Archived Licensing
- labels: []

### NORMALIZED CONTENT

Commercial licenses of our products are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.

The commercial license activation is needed after the purchase transaction has been completed.

License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.

Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to [www.nomagic.com](http://www.nomagic.com/) and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.

For MagicDraw, plugins and other products activation instructions refer to: [https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later](https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Commercial licenses of our products are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.</p><p>The commercial license activation is needed after the purchase transaction has been completed.</p><p>License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.</p><p>Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to <a class="external-link" href="http://www.nomagic.com/" rel="nofollow">www.nomagic.com</a> and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.</p><p>For MagicDraw, plugins and other products activation instructions refer to: <a href="https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later" rel="nofollow">https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later</a></p>
````

<!--NOMAGIC_PAGE id=70395772 space=FAQ version=1 -->
## PAGE 00088: I'm trying to run the two license servers and vendor daemons on same machine to restrict who gets access to which licenses. How can I do this?

- page_id: `70395772`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395772/I+m+trying+to+run+the+two+license+servers+and+vendor+daemons+on+same+machine+to+restrict+who+gets+access+to+which+licenses.+How+can+I+do+this
- version_number: 1
- version_date: `2021-03-03T13:58:32.028+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.

In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.

Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at [https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf](https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can not run two same vendor daemon instances and license servers on the same machine. Being able to do so, would enable users to double the number of licenses.</p><p>In order to set restrictions without starting two license servers, please configure the options file. Options file - a configuration file available on the license server, which license administrators can use to allow / deny / reserve products to be used by specific users, hosts, and groups.</p><p>Instructions how to create and manage the options file for license server is described in the Flexnet License Administration Guide at <a href="https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf" rel="nofollow">https://docs.nomagic.com/display/NMDOC/FlexNet+license+server+installation+and+licensing?preview=/62891142/62891197/fnp_LicAdmin_11_17_0.pdf</a></p>
````

<!--NOMAGIC_PAGE id=70394576 space=FAQ version=2 -->
## PAGE 00089: In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?

- page_id: `70394576`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70394576/In+our+company+the+storage+of+user+home+directory+is+limited.+How+to+force+to+keep+configuration+files+in+other+directory
- version_number: 2
- version_date: `2021-07-16T05:32:37.600+02:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

You can save configuration files in the modeling tool installation directory or on your chosen directory.

To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties* (this file is in*\bin*): 
JAVA_ARGS=-DLOCALCONFIG=false

**NOTE**: For Windows users. If you are using modeling tool of version 17.0.4 or later, you must also add argument 
-DWINCONFIG\=false.

To store configuration files to your chosen location

1. In the /. <modeling tool name> / folder, create file named <modeling tool properties file name> redirect , that is magicdrawredirect , cameoearedirect , csmredirect , or cbmredirect .
2. In the created file, type absolute (for example, C:\users\john\Documents ) or relative (relative to modeling tool installation directory, for example, ..\configurations ) path where configuration and auxiliary files will be saved.

Or:

1. Open the *.properties* file, which is located in \bin .
2. Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location= <absolute path to a custom location>

For example, *-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData*

**NOTE:** If there is defined to store files in installation directory (see the section "To store MagicDraw configuration files in MagicDraw installation directory" above), files will not be stored to your chosen location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can save configuration files in the modeling tool installation directory or on your chosen directory.</p><p>To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties* (this file is in<em> \bin</em>):<br />JAVA_ARGS=-DLOCALCONFIG=false</p><p><strong>NOTE</strong>: For Windows users. If you are using modeling tool of version 17.0.4 or later, you must also add argument<br />-DWINCONFIG\=false.</p><p>To store configuration files to your chosen location</p><ol><li>In the /.<em>&lt;modeling tool name&gt;</em>/ folder, create file named <em> &lt;modeling tool properties file name&gt; redirect</em>, that is <em>magicdrawredirect</em>, <em>cameoearedirect</em>, <em>csmredirect</em>, or <em>cbmredirect</em>.</li><li>In the created file, type absolute (for example, <em>C:\users\john\Documents</em>) or relative (relative to modeling tool installation directory, for example, <em>..\configurations</em>) path where configuration and auxiliary files will be saved.</li></ol><p>Or:</p><ol><li>Open the *.properties* file, which is located in <em>\bin</em>.</li><li>Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location=<em>&lt;absolute path to a custom location&gt;</em></li></ol><p>For example, <em>-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData</em></p><p><strong>NOTE:</strong> If there is defined to store files in installation directory (see the section &quot;To store MagicDraw configuration files in MagicDraw installation directory&quot; above), files will not be stored to your chosen location.<br /><br /><br /><br /></p>
````

<!--NOMAGIC_PAGE id=68526626 space=FAQ version=17 -->
## PAGE 00090: Installation and Running

- page_id: `68526626`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/68526626/Installation+and+Running
- version_number: 17
- version_date: `2021-03-04T07:17:00.631+01:00`
- ancestors: Frequently Asked Questions
- labels: ['installation']

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d185a31b-1d5e-4e24-ac04-81bedd421bf5" /></p>
````

<!--NOMAGIC_PAGE id=70389758 space=FAQ version=2 -->
## PAGE 00091: Installation and Running (Copy)

- page_id: `70389758`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70389758/Installation+and+Running+Copy
- version_number: 2
- version_date: `2021-01-29T14:15:11.452+01:00`
- ancestors: Current FAQ for Review
- labels: []

### NORMALIZED CONTENT

#### EXPAND: Updating your modelling tool to a new version

Updating your modelling tool to a new version

You may find all the information about updating to new version at[Updating modeling tools and plugins](https://docs.nomagic.com/display/NMDOC/Updating+modeling+tools+and+plugins).

#### EXPAND: [To Be Reviewed]In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?

[To Be Reviewed]In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?

You can save configuration files in the modeling tool installation directory or on your chosen directory.

To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties* (this file is in*\bin*): 
JAVA_ARGS=-Dlocalconfig=false

**NOTE**: For Windows users. If you are using modeling tool of version 17.0.4 or later, you must also add argument 
-DWINCONFIG\=false.

To store configuration files to your chosen location

1. In the /. <modeling tool name> / folder, create file named <modeling tool properties file name> redirect , that is magicdrawredirect , cameoearedirect , csmredirect , or cbmredirect .
2. In the created file, type absolute (for example, C:\users\john\Documents ) or relative (relative to modeling tool installation directory, for example, ..\configurations ) path where configuration and auxiliary files will be saved.

Or:

1. Open the *.properties * file, which is located in \bin .
2. Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location= <absolute path to a custom location>

For example, *-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData*

**NOTE:** If there is defined to store files in installation directory (see the section "To store MagicDraw configuration files in MagicDraw installation directory" above), files will not be stored to your chosen location. 
 
 
Article To Combine

[I have installed and activated one of your modelling tools as the administrator. When I had logged into my regular account, my modeling tool asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?](https://www.nomagic.com/support/faq)

The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.

The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.

You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).

For the instructions on how to change the configuration files directory, please find the issue "In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?"

Note: It is important to know that the MagicDraw seat license can be used by a single user only.

#### EXPAND: [To Be Reviewed]My modeling tool does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?

[To Be Reviewed]My modeling tool does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?

Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in *.zip/iso* files are not secure because of the dylib-hijacking problem. 
(Please find more about it at [https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/](https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/)). 
All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.

The solutions are:

1. To run magicdraw.sh file from the /bin directory.
2. To download the original signed MagicDraw.dmg file and to install the application again.
3. To remove the program from quarantine.

To remove the application from quarantine, please do:

1. Open a terminal.
2. Using the terminal, open the MagicDraw installation directory.
3. Write the command: xattr -d com.apple.quarantine MagicDraw.app/
4. Close the terminal and start MagicDraw using the .app file.

**NOTE:** This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.

Article to combine

[MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?](https://www.nomagic.com/support/faq)

Solution is to run *magicdraw.sh* file from the */bin* directory.

This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.

Please update your modeling tool to the **version 18.4 SP1** to avoid the installation incompatibility.

#### EXPAND: [To Be Reviewed]Is it possible to create a modeling tool installation package with a set of some default options?

[To Be Reviewed]Is it possible to create a modeling tool installation package with a set of some default options?

First of all you need to pre-configure your modeling tool. Do the following:

1. Check if you have the permission to write to the software installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.
2. In magicdraw.properties or cea.properties or csm.properties , which is in \bin , set the parameter value: JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false
3. Run the modeling tool and set desired options, then close the program.
4. Reopen magicdraw.properties or cea.properties or csm.properties and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.
5. Copy the installation folder and paste it on a new machine.

Let us explain the difference between changed parameter values:

a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in*\.magicdraw\* . Options are loaded in the following order:

1. From <Common Application Data location>\.magicdraw or .cameo.enterprise.architecture or cameo.systems.modeler\
2. From the modeling tool installation folder

b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the modeling tool installation folder and are loaded from there.

#### EXPAND: [To Be Reviewed]When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to my modeling tool installation directory or "failed to copy resource directory". How can this be handled?

[To Be Reviewed]When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to my modeling tool installation directory or "failed to copy resource directory". How can this be handled?

We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.

To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following: 
1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**. 
2. From the **System Configuration** dialog, click the **Tools** tab. 
3. Select the **Change UAC Settings** tool and click **Launch** button. 
4. Move the slider to the highest value to set **Always notify** and click **OK**. 
5. Restart the computer to apply changes.

To enable UAC on Windows Vista OS, do the following: 
1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**.

2. From the**System Configuration**dialog, click the **Tools** tab. 
3. Select the **Enable UAC** tool and click **Launch** button. The **CMD** window opens. 
4. When the command is completed, you can close **CMD** window. 
5. Restart the computer to apply changes.

To run MagicDraw as administrator, right-click the MagicDraw icon and choose **Run as Administrator**.

To run MagicDraw as an administrator all the time, do the following: 
1. Right-click the MagicDraw icon and choose **Properties**. 
2. Click the **Compatibility** tab. 
3. In the **Privilege Level** area, select **Run this program as an administrator**. 
4. Click **OK**.

#### EXPAND: [To Be Reviewed]How to run MagicDraw under Unix after installation?

[To Be Reviewed]How to run MagicDraw under Unix after installation?

Run mduml* file, which is located in MagicDraw installation directory, bin folder.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

#### EXPAND: [To Be Reviewed]When I run the exe file I get a warning: Please select another location to extract the installer to:

[To Be Reviewed]When I run the exe file I get a warning: Please select another location to extract the installer to:

This error occurs when you have a corrupted installer file. Please download the file and install again.

#### EXPAND: [To Be Reviewed]My modeling tool worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?

[To Be Reviewed]My modeling tool worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?

This problem is Install Anywhere related and appears when you uninstall previous version of our modelling tools and then, without restarting your computer, install another modelling tool in the same directory. We would suggest to uninstall your modelling tool, restart your computer, and then install it again.

#### EXPAND: [To Be Reviewed]What is the best way to reinstall my modeling tool on new computer or the same one after formatting.

[To Be Reviewed]What is the best way to reinstall my modeling tool on new computer or the same one after formatting.

Reinstall product on new computer:

1. Deactivate the current license .
2. Download and install the fresh installation on new machine.
3. Start it after the installation is finished.
4. The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.
5. Uninstall the product from old machine.
6. You will be requested to activate the license and receive the commercial license dedicated for the particular machine.

#### EXPAND: [To Be Reviewed]How to install my modeling tool in a silent mode, i.e., without the installer GUI?

[To Be Reviewed]How to install my modeling tool in a silent mode, i.e., without the installer GUI?

Please start the installer with the following parameters: 
-i silent -DUSER_INSTALL_DIR=

The example:

MD_UML_169_win.exe -i silent "-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9" 
MagicDraw will be installed silently, with a default configuration.

#### EXPAND: [To Be Reviewed]When trying to launch my modeling tool on OS X Mountain Lion, the error appears: "MagicDraw.app" is damaged and can't be opened. You should move it to the Trash."

[To Be Reviewed]When trying to launch my modeling tool on OS X Mountain Lion, the error appears: "MagicDraw.app" is damaged and can't be opened. You should move it to the Trash."

Please note that downloaded installs are not corrupted or damaged and this problem is not related to the modeling tool application. This issue is related to the new OS X Mountain Lion functionality, "Gatekeeper."

The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.

In order to launch their modelling tools, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: [http://support.apple.com/kb/HT5290](http://support.apple.com/kb/HT5290)

Note: We are communicating with Apple to solve this issue so that our customers may execute their modelling tools without any problems.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="2d15b1fb-11e5-4bc4-9602-33171dbbe410"><ac:parameter ac:name="title">Updating your modelling tool to a new version</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">You may find all the information about updating to new version at </span><a href="https://docs.nomagic.com/display/NMDOC/Updating+modeling+tools+and+plugins">Updating modeling tools and plugins</a><span style="color: rgb(85,85,85);">.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="e94457e8-d1bd-4826-81c0-79cbf1ada817"><ac:parameter ac:name="title">[To Be Reviewed]In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?</ac:parameter><ac:rich-text-body><p>You can save configuration files in the modeling tool installation directory or on your chosen directory.</p><p>To store configuration files in the modeling tool installation directory add argument into JAVA_ARGS line in file *.properties<span>*</span> (this file is in<em> \bin</em>):<br />JAVA_ARGS=-Dlocalconfig=false</p><p><strong>NOTE</strong>: For Windows users. If you are using modeling tool of version 17.0.4 or later, you must also add argument<br />-DWINCONFIG\=false.</p><p>To store configuration files to your chosen location</p><ol><li>In the /.<em>&lt;modeling tool name&gt;</em>/ folder, create file named <em> &lt;modeling tool properties file name&gt; redirect</em>, that is <em>magicdrawredirect</em>, <em>cameoearedirect</em>, <em>csmredirect</em>, or <em>cbmredirect</em>.</li><li>In the created file, type absolute (for example, <em>C:\users\john\Documents</em>) or relative (relative to modeling tool installation directory, for example, <em>..\configurations</em>) path where configuration and auxiliary files will be saved.</li></ol><p>Or:</p><ol><li>Open the *.properties<span>*</span> file, which is located in <em>\bin</em>.</li><li>Add the parameter value to the end of the line started with JAVA_ARGS= -Dlocalconfig.location=<em>&lt;absolute path to a custom location&gt;</em></li></ol><p>For example, <em>-Dlocalconfig.location\=C\:\\MagicDraw\\configurationData</em></p><p><strong>NOTE:</strong> If there is defined to store files in installation directory (see the section &quot;To store MagicDraw configuration files in MagicDraw installation directory&quot; above), files will not be stored to your chosen location.<br /><br /><br />Article To Combine</p><p><br /></p><p><a class="topic_faqToggleLink" href="https://www.nomagic.com/support/faq"><span class="topic_faqToggleQuestion">I have installed and activated one of your modelling tools as the administrator. When I had logged into my regular account, my modeling tool asked for a license key file and for the license activation again. How can I escape the license activation on the same machine twice?</span></a></p><p>The proper way to activate the license is to install the application as the administrator, then to login as a regular user, which will use the tool, and proceed with the license activation process.</p><p>The particular user licensing information is stored in the user home directory. So if you want that the application which has already been activated from the administrator account would not require the license activation from the user account on the same machine, you should change the licensing information storage place.</p><p>You can store the licensing information in the MagicDraw installation directory (the read-write rights are required).</p><p>For the instructions on how to change the configuration files directory, please find the issue &quot;In our company the storage of user home directory is limited. How to force to keep configuration files in other directory?&quot;</p><p>Note: It is important to know that the MagicDraw seat license can be used by a single user only.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="1b4b755c-08d4-4a75-948a-c1aea9443812"><ac:parameter ac:name="title">[To Be Reviewed]My modeling tool does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?</ac:parameter><ac:rich-text-body><p>Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in <em>.zip/iso</em> files are not secure because of the dylib-hijacking problem.<br />(Please find more about it at <a href="https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/">https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/</a>).<br />All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.</p><p>The solutions are:</p><ol><li>To run <em>magicdraw.sh</em> file from the  <em>/bin</em> directory.</li><li>To download the original signed <em>MagicDraw.dmg</em> file and to install the application again.</li><li>To remove the program from quarantine.</li></ol><p>To remove the application from quarantine, please do:</p><ol><li>Open a terminal.</li><li>Using the terminal, open the MagicDraw installation directory.</li><li>Write the command: <em>xattr -d com.apple.quarantine MagicDraw.app/</em></li><li>Close the terminal and start MagicDraw using the <em>.app</em> file.</li></ol><p><strong>NOTE:</strong> This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.</p><p><br /></p><p>Article to combine</p><p><br /></p><p><a href="https://www.nomagic.com/support/faq" class="topic_faqToggleLink"><span class="topic_faqToggleQuestion">MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?</span></a></p><p>Solution is to run <em>magicdraw.sh</em> file from the <em>/bin</em> directory.</p><p>This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.</p><p>Please update your modeling tool to the <strong>version 18.4 SP1</strong> to avoid the installation incompatibility.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="58c25b13-5d71-425a-ba7d-e0d2a6d29216"><ac:parameter ac:name="title">[To Be Reviewed]Is it possible to create a modeling tool installation package with a set of some default options?</ac:parameter><ac:rich-text-body><p>First of all you need to pre-configure your modeling tool. Do the following:</p><ol><li>Check if you have the permission to write to the software installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.</li><li>In <em>magicdraw.properties or cea.properties or csm.properties</em>, which is in <em>\bin</em>, set the parameter value:<br />JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false</li><li>Run the modeling tool and set desired options, then close the program.</li><li>Reopen <em>magicdraw.properties or cea.properties or csm.properties</em> and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.</li><li>Copy the installation folder and paste it on a new machine.</li></ol><p>Let us explain the difference between changed parameter values:</p><p>a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in<em> \.magicdraw\</em> . Options are loaded in the following order:</p><ol><li>From <em>&lt;Common Application Data location&gt;\.magicdraw or .cameo.enterprise.architecture or cameo.systems.modeler\</em></li><li>From the modeling tool installation folder</li></ol><p>b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the modeling tool installation folder and are loaded from there.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="0a08dafc-6e6c-4d4a-94d0-dd28e075367d"><ac:parameter ac:name="title">[To Be Reviewed]When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to my modeling tool installation directory or &quot;failed to copy resource directory&quot;. How can this be handled?</ac:parameter><ac:rich-text-body><p>We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.</p><p>To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following:<br />1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.<br />2. From the <strong>System Configuration</strong> dialog, click the <strong>Tools</strong> tab.<br />3. Select the <strong>Change UAC Settings</strong> tool and click <strong>Launch</strong> button.<br />4. Move the slider to the highest value to set <strong>Always notify</strong> and click <strong>OK</strong>.<br />5. Restart the computer to apply changes.</p><p>To enable UAC on Windows Vista OS, do the following:<br />1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.</p><p><br />2. From the<strong> System Configuration </strong>dialog, click the <strong>Tools</strong> tab.<br />3. Select the <strong>Enable UAC</strong> tool and click <strong>Launch</strong> button. The <strong>CMD</strong> window opens.<br />4. When the command is completed, you can close <strong>CMD</strong> window.<br />5. Restart the computer to apply changes.</p><p>To run MagicDraw as administrator, right-click the MagicDraw icon and choose <strong>Run as Administrator</strong>.</p><p>To run MagicDraw as an administrator all the time, do the following:<br />1. Right-click the MagicDraw icon and choose <strong>Properties</strong>.<br />2. Click the <strong>Compatibility</strong> tab.<br />3. In the <strong>Privilege Level</strong> area, select <strong>Run this program as an administrator</strong>.<br />4. Click <strong>OK</strong>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="65adf3fa-7c0b-459f-93bb-ccc62ab04206"><ac:parameter ac:name="title">[To Be Reviewed]How to run MagicDraw under Unix after installation?</ac:parameter><ac:rich-text-body><p>Run mduml<span>*</span> file, which is located in MagicDraw installation directory, bin folder.</p><p> </p><p><span>*</span> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="a1ac3883-3b98-41cd-8194-a3c3292c3734"><ac:parameter ac:name="title">[To Be Reviewed]When I run the exe file I get a warning: Please select another location to extract the installer to:</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">This error occurs when you have a corrupted installer file. Please download the file and install again.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="4c455e7e-235c-4e17-bf51-b3e2b0c8a0c3"><ac:parameter ac:name="title">[To Be Reviewed]My modeling tool worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">This problem is Install Anywhere related and appears when you uninstall previous version of our modelling tools and then, without restarting your computer, install another modelling tool in the same directory. We would suggest to uninstall your modelling tool, restart your computer, and then install it again.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="b96e186b-5dc0-4128-af3e-7b94b5848c7e"><ac:parameter ac:name="title">[To Be Reviewed]What is the best way to reinstall my modeling tool on new computer or the same one after formatting.</ac:parameter><ac:rich-text-body><p>Reinstall product on new computer:</p><ol><li><a href="https://www.nomagic.com/support/activation.html#deactivation_in_aplication">Deactivate the current license</a>.</li><li>Download and install the fresh installation on new machine.</li><li>Start it after the installation is finished.</li><li>The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.</li><li>Uninstall the product from old machine.</li><li>You will be requested to activate the license and receive the commercial license dedicated for the particular machine.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="09a4b7f2-a530-4be8-beb6-030bd129518f"><ac:parameter ac:name="title">[To Be Reviewed]How to install my modeling tool in a silent mode, i.e., without the installer GUI?</ac:parameter><ac:rich-text-body><p>Please start the installer with the following parameters:<br />-i silent -DUSER_INSTALL_DIR=</p><p>The example:</p><p>MD_UML_169_win.exe -i silent &quot;-DUSER_INSTALL_DIR=C:\Program Files\MagicDraw 16.9&quot;<br />MagicDraw will be installed silently, with a default configuration.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="7548ad39-0cef-4c7b-b0ff-c384298ce659"><ac:parameter ac:name="title">[To Be Reviewed]When trying to launch my modeling tool on OS X Mountain Lion, the error appears: &quot;MagicDraw.app&quot; is damaged and can't be opened. You should move it to the Trash.&quot;</ac:parameter><ac:rich-text-body><p>Please note that downloaded installs are not corrupted or damaged and this problem is not related to the modeling tool application. This issue is related to the new OS X Mountain Lion functionality, &quot;Gatekeeper.&quot;</p><p>The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.</p><p>In order to launch their modelling tools, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: <a href="http://support.apple.com/kb/HT5290">http://support.apple.com/kb/HT5290</a></p><p>Note: We are communicating with Apple to solve this issue so that our customers may execute their modelling tools without any problems.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=70395727 space=FAQ version=1 -->
## PAGE 00092: Is it possible to create a modeling tool installation package with a set of some default options?

- page_id: `70395727`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395727/Is+it+possible+to+create+a+modeling+tool+installation+package+with+a+set+of+some+default+options
- version_number: 1
- version_date: `2021-03-03T12:53:51.600+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

First of all you need to pre-configure your modeling tool. Do the following:

1. Check if you have the permission to write to the software installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.
2. In magicdraw.properties or cea.properties or csm.properties , which is in \bin , set the parameter value: JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false
3. Run the modeling tool and set desired options, then close the program.
4. Reopen magicdraw.properties or cea.properties or csm.properties and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.
5. Copy the installation folder and paste it on a new machine.

Let us explain the difference between changed parameter values:

a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in*\.magicdraw\* . Options are loaded in the following order:

1. From <Common Application Data location>\.magicdraw or .cameo.enterprise.architecture or cameo.systems.modeler\
2. From the modeling tool installation folder

b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the modeling tool installation folder and are loaded from there.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>First of all you need to pre-configure your modeling tool. Do the following:</p><ol><li>Check if you have the permission to write to the software installation folder because all information that you change will be stored in this folder. If you do not have the permission to write, contact your system administrator.</li><li>In <em>magicdraw.properties or cea.properties or csm.properties</em>, which is in <em>\bin</em>, set the parameter value:<br />JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false</li><li>Run the modeling tool and set desired options, then close the program.</li><li>Reopen <em>magicdraw.properties or cea.properties or csm.properties</em> and restore the parameter value JAVA_ARGS=-DLOCALCONFIG\=true and remove the parameter -DWINCONFIG\=false.</li><li>Copy the installation folder and paste it on a new machine.</li></ol><p>Let us explain the difference between changed parameter values:</p><p>a) If JAVA_ARGS=-DLOCALCONFIG\=true, then option settings are stored in<em> \.magicdraw\</em> . Options are loaded in the following order:</p><ol><li>From <em>&lt;Common Application Data location&gt;\.magicdraw or .cameo.enterprise.architecture or cameo.systems.modeler\</em></li><li>From the modeling tool installation folder</li></ol><p>b) If JAVA_ARGS=-DLOCALCONFIG\=false -DWINCONFIG\=false, then option settings are stored only in the modeling tool installation folder and are loaded from there.</p>
````

<!--NOMAGIC_PAGE id=68526630 space=FAQ version=5 -->
## PAGE 00093: Java Virtual Machine (JVM)

- page_id: `68526630`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/68526630/Java+Virtual+Machine+JVM
- version_number: 5
- version_date: `2021-03-04T07:17:46.288+01:00`
- ancestors: Frequently Asked Questions
- labels: ['java']

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0338a376-1747-420b-abfc-424d73abbbb6" /></p>
````

<!--NOMAGIC_PAGE id=70389761 space=FAQ version=2 -->
## PAGE 00094: Java Virtual Machine (JVM) (Copy)

- page_id: `70389761`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70389761/Java+Virtual+Machine+JVM+Copy
- version_number: 2
- version_date: `2021-01-29T14:15:11.496+01:00`
- ancestors: Current FAQ for Review
- labels: []

### NORMALIZED CONTENT

#### EXPAND: [To Be Reviewed]How to change JVM version?

[To Be Reviewed]How to change JVM version?

1. Go to <modeling tool installation directory>\bin and open the <modeling tool>.properties file (eg., magicdraw.properties , csm.properties , cameoea.properties ) for editing. If you are using modeling tools of version 17.0.4 or earlier, the name of the property file is mduml.properties .
2. In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144

NOTE: Integrated modelling tools runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that the modeling tool integrates with. If you are running the software integrated with IDE, read the appropriate readme.html for specific integration, found in the *integrations* folder.

#### EXPAND: MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?

MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?

Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.

The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.

If you are using an **earlier version than 18.4 SP1**and cannot start the modeling tool*, please do the following:

1. Download the original signed <modeling tool*>.dmg file and install the application again.
2. In bin\ magicdraw.properties** , set JAVA_HOME to the Java version installed in the <modeling_tool*_installation_directory >\java folder.

Example: *JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre*

1. Run magicdraw.sh*** file from the /bin folder.

*MagicDraw, Cameo EA, Cameo Systems Modeler

** cameoea.properties, csm.properties

***camocea.sh, csm.sh

#### EXPAND: [To Be Reviewed]I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.

[To Be Reviewed]I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.

You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties* file, in the line:

JAVA_ARGS=-Xmx800M

The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.

On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.

More information about OutOfMemory problems you can find in readme.html by "OutOfMemory problem" paragraph. This file is located in <MagicDraw installation directory>.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

#### EXPAND: [To Be Reviewed]How do I know what version of JVM I am running?

[To Be Reviewed]How do I know what version of JVM I am running?

You may find this information in the About window (Help menu -> About)

or

If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.

Article to combine with

[I want to check which JVM is used for installation under Linux.](https://www.nomagic.com/support/faq)

You can watch installation process by setting environment variable LAX_DEBUG to value 1 before starting installation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="6cf6f978-4981-44d9-b368-9b0e3576748c"><ac:parameter ac:name="title">[To Be Reviewed]How to change JVM version?</ac:parameter><ac:rich-text-body><ol><li>Go to <em>&lt;modeling tool installation directory&gt;\bin</em> and open the <em>&lt;modeling tool&gt;.properties</em> file (eg., <em>magicdraw.properties</em>, <em>csm.properties</em>, <em>cameoea.properties</em>) for editing. If you are using modeling tools of version 17.0.4 or earlier, the name of the property file is <em>mduml.properties</em>.</li><li>In the JAVA_HOME line, add the path to the Java software. For example: JAVA_HOME=C\:Program Files\\Java\\jre1.8.0_144</li></ol><p> </p><p>NOTE: Integrated modelling tools runs on the JVM specified by the IDE. In order to change the JVM, you must modify the startup properties for the IDE that the modeling tool integrates with. If you are running the software integrated with IDE, read the appropriate readme.html for specific integration, found in the <em>integrations</em> folder.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="f38e95a9-1832-4de1-911b-deb9bbf60044"><ac:parameter ac:name="title">MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?</ac:parameter><ac:rich-text-body><p>Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.</p><p>The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.</p><p>If you are using an <strong>earlier version than 18.4 SP1 </strong>and cannot start the modeling tool*, please do the following:</p><ol><li>Download the original signed <em>&lt;modeling tool*&gt;.dmg</em> file and install the application again.</li><li>In <em>bin\</em><em>magicdraw.properties<span>**</span></em>, set <em>JAVA_HOME</em> to the Java version installed in the <em>&lt;modeling_tool*_installation_directory &gt;\java</em> folder.</li></ol><p>Example: <em>JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre</em></p><ol><li>Run magicdraw.sh*** file from the /bin folder.</li></ol><hr /><p>*MagicDraw, Cameo EA, Cameo Systems Modeler</p><p>** cameoea.properties, csm.properties</p><p>***camocea.sh, csm.sh</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="9c213c23-ae69-44e0-8caf-4624684ff15a"><ac:parameter ac:name="title">[To Be Reviewed]I would like to increase java heap size that MagicDraw would run faster with larger models. I have 12 GB of RAM.</ac:parameter><ac:rich-text-body><p>You can change the java maximum heap size (-Xmx) in your /bin/mduml.properties<span>*</span> file, in the line:</p><p>JAVA_ARGS=-Xmx800M</p><p>The maximum theoretical heap limit for the 32-bit JVM is 4G. Due to various additional constraints such as available swap, kernel address space usage, memory fragmentation, and VM overhead, in practice the limit can be much lower. On most modern 32-bit Windows systems the maximum heap size will range from 1.4G to 1.6G. On 32-bit Solaris kernels the address space is limited to 2G. On 64-bit operating systems running the 32-bit VM, the max heap size can be higher, approaching 4G on many Solaris systems.</p><p>On 64-bit VMs, you have 64 bits of addressability to work with resulting in a maximum Java heap size limited only by the amount of physical memory and swap space your system provides.</p><p>More information about OutOfMemory problems you can find in readme.html by &quot;OutOfMemory problem&quot; paragraph. This file is located in &lt;MagicDraw installation directory&gt;.</p><p> </p><p><span>*</span> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="59f77d67-45d0-4491-a67c-85f33d752f04"><ac:parameter ac:name="title">[To Be Reviewed]How do I know what version of JVM I am running?</ac:parameter><ac:rich-text-body><p>You may find this information in the About window (Help menu -&gt; About)</p><p>or</p><p>If you have Sun's or IBM's JVM, enter the following in the command prompt: java -version.</p><p><br /></p><p>Article to combine with</p><p><br /></p><p><a class="topic_faqToggleLink" href="https://www.nomagic.com/support/faq"><span class="topic_faqToggleQuestion">I want to check which JVM is used for installation under Linux.</span></a></p><p><br /></p><p><span style="color: rgb(85,85,85);">You can watch installation process by setting environment variable LAX_DEBUG to value 1 before starting installation.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=70395778 space=FAQ version=1 -->
## PAGE 00095: License Server Manager Not Starting

- page_id: `70395778`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395778/License+Server+Manager+Not+Starting
- version_number: 1
- version_date: `2021-03-03T13:59:30.046+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

The license server manager will not start if either of the following ports are in use:

* Default license server port (no ports in range 27000 to 27009 available)

* Default HTTP port for the license server manager user interface (port 8080)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The license server manager will not start if either of the following ports are in use:</p><p>* Default license server port (no ports in range 27000 to 27009 available)</p><p>* Default HTTP port for the license server manager user interface (port 8080)</p>
````

<!--NOMAGIC_PAGE id=70389759 space=FAQ version=3 -->
## PAGE 00096: Licensing (Copy)

- page_id: `70389759`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70389759/Licensing+Copy
- version_number: 3
- version_date: `2022-03-31T06:39:20.098+02:00`
- ancestors: Current FAQ for Review
- labels: []

### NORMALIZED CONTENT

#### EXPAND: [To Be Reviewed]I'm requested to activate my modeling tool license. What should I do?

[To Be Reviewed]I'm requested to activate my modeling tool license. What should I do?

Commercial licenses of our products are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.

The commercial license activation is needed after the purchase transaction has been completed.

License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.

Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to [www.nomagic.com](http://www.nomagic.com) and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.

For MagicDraw, plugins and other products activation instructions refer to: [https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later](https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later)

#### EXPAND: [To Be Reviewed]I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?

[To Be Reviewed]I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?

Installation on multiple machines is supported by the Mobile or Floating license.

More about Mobile User License could be found at 
[http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html](https://www.nomagic.com/resources/sales-and-licenses/mobile-licensing)

More about Floating License could be found at 
[http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html](https://www.nomagic.com/resources/sales-and-licenses/floating-licensing)

Note: The Seat license can be used by a single user on a single installation.

If you have any questions about the licensing or purchasing, please feel free to contact your account executive or [sales@nomagic.com](mailto:sales@nomagic.com).

#### EXPAND: I want to demo one of your modelling tools, how can I do that?

I want to demo one of your modelling tools, how can I do that?

**Beginning with 2022x, Demo install is no longer available.**

Firstly - you have to have an account registered with us - as our download section is only available to our registered customers.

Once you have an account - please log into it and select the product you want to demo from the "Download Trials" list found on the left side of the screen.

Select the version/edition you want to demo and click on next.

Select and download one of the installers that is suitable for your OS and has a word demo in the installer file name. Please note the exact file name of the installer you are downloading - as both demo and full featured installers are provided. Demo installers should not need any license key file to use.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="ebe3322d-59e8-4f1d-b4e2-98b7de9df5e2"><ac:parameter ac:name="title">[To Be Reviewed]I'm requested to activate my modeling tool license. What should I do?</ac:parameter><ac:rich-text-body><p>Commercial licenses of our products are locked to the particular machine. The activation process allows receiving the commercial license dedicated for the particular machine.</p><p>The commercial license activation is needed after the purchase transaction has been completed.</p><p>License activation can be completed from the Licence Manager dialog in the application. You may choose online activation and enable commercial licenses activated automatically.</p><p>Alternatively, you may select offline activation and then you will be required to enter a Host ID in the license owner account (login to <a href="http://www.nomagic.com">www.nomagic.com</a> and select License Activation Management menu item at the right side of page). You can then download the commercial activated license.</p><p>For MagicDraw, plugins and other products activation instructions refer to: <a href="https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later">https://docs.nomagic.com/display/NMDOC/18.0+SP7%2C+18.5+SP4%2C+19.0+SP4%2C+and+later</a></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="640d7874-9e5e-4c68-ab44-0b93fa6fb884"><ac:parameter ac:name="title">[To Be Reviewed]I would like to install the application on two machines, but the only one instance at a time will be used. What license do I need?</ac:parameter><ac:rich-text-body><p>Installation on multiple machines is supported by the Mobile or Floating license.</p><p>More about Mobile User License could be found at<br /><a href="https://www.nomagic.com/resources/sales-and-licenses/mobile-licensing">http://www.nomagic.com/support/sales-and-licensing/mobile-licensing.html</a></p><p>More about Floating License could be found at<br /><a href="https://www.nomagic.com/resources/sales-and-licenses/floating-licensing">http://www.nomagic.com/support/sales-and-licensing/floating-licensing.html</a></p><p>Note: The Seat license can be used by a single user on a single installation.</p><p>If you have any questions about the licensing or purchasing, please feel free to contact your account executive or <span><a href="mailto:sales@nomagic.com">sales@nomagic.com</a></span>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="fa6427fb-ac1d-4c00-9ed4-76bafab05bcb"><ac:parameter ac:name="title">I want to demo one of your modelling tools, how can I do that?</ac:parameter><ac:rich-text-body><p><span style="color: rgb(255,0,0);"><strong>Beginning with 2022x, Demo install is no longer available.</strong></span></p><p>Firstly - you have to have an account registered with us - as our download section is only available to our registered customers.</p><p>Once you have an account - please log into it and select the product you want to demo from the &quot;Download Trials&quot; list found on the left side of the screen.</p><p>Select the version/edition you want to demo and click on next.</p><p>Select and download one of the installers that is suitable for your OS and has a word demo in the installer file name. Please note the exact file name of the installer you are downloading - as both demo and full featured installers are provided. Demo installers should not need any license key file to use.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=70395817 space=FAQ version=1 -->
## PAGE 00097: MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?

- page_id: `70395817`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395817/MagicDraw+does+not+display+Chinese+Hindi+Japanese+Korean+Thai+or+some+special+symbols+such+as+superscript+and+subscript.+Can+this+be+fixed
- version_number: 1
- version_date: `2021-03-03T14:09:34.894+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select**Options**>**Look and Feel**>**Metal**.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select </span><strong>Options</strong><span style="color: rgb(85,85,85);"> &gt; </span><strong>Look and Feel</strong><span style="color: rgb(85,85,85);"> &gt; </span><strong>Metal</strong><span style="color: rgb(85,85,85);">.</span></p>
````

<!--NOMAGIC_PAGE id=106642238 space=FAQ version=15 -->
## PAGE 00098: MagicDraw does not start after upgrading to MAC OS Ventura

- page_id: `106642238`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/106642238/MagicDraw+does+not+start+after+upgrading+to+MAC+OS+Ventura
- version_number: 15
- version_date: `2023-01-17T15:04:04.698+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

**After upgrading to MAC OS Ventura, MagicDraw and other modeling tools do not start or crash.**

This is a known issue. MagicDraw and other modeling tools do not start via APP on MacOS Ventura. You can update the APP with the new file for the 2021x Refresh2 HotFix4 version and later. Contact [Customer Support](https://www.3ds.com/support/) to get the new APP file.

This issue has been solved with 2022x Refresh1 Hot Fix 1, released on December 23, 2022. [CONFLUENCE_PAGE title='Downloading installation files' space='NMDOC']>]]>

To update APP

1. Download < modeling_tool_name >.app.zip file as instructed by Customer Support.
2. Extract the downloaded file.
3. Go to <modeling_tool installation directory>/bin/<...> and open the .properties file.
4. In the open properties file, remove the " JAVA_HOME= " argument value if it is not empty.
5. In the <modeling_tool installation directory>/<..> , replace the APP file with the downloaded one.
6. Start the application.
7. In the open message dialog, click Open . [ATTACHMENT filename='Screenshot 2022-11-28 at 16.58.37.png']

After the APP is updated, the version displayed in the menu does not match the version in the **About**window. This is an expected behavior that has no impact on your modeling tool's functionality.

The new APP contains Java 11.0.16. We highly recommend not changing the Java version.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong><span style="color: rgb(23,43,77);">After upgrading to MAC OS Ventura, MagicDraw and other modeling tools do not start or crash. </span></strong></p><p><span style="color: rgb(23,43,77);">This is a known issue. MagicDraw and other modeling tools do not start via APP on MacOS Ventura. You can update the APP with the new file for the 2021x Refresh2 HotFix4 version and later. Contact <a href="https://www.3ds.com/support/">Customer Support</a> to get the new APP file.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="88683959-038e-42c6-9850-eb6f97f27c45"><ac:rich-text-body><p>This issue has been solved with 2022x Refresh1 Hot Fix 1, released on December 23, 2022. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Downloading installation files" /><ac:plain-text-link-body><![CDATA[Learn how to download installation files >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">To update APP </p><hr /><ol style="text-align: left;"><li>Download &lt;<em>modeling_tool_name</em>&gt;.app.zip file as instructed by Customer Support.</li><li>Extract the downloaded file.</li><li>Go to <em>&lt;modeling_tool installation directory&gt;/bin/&lt;...&gt;</em> and open the .properties file.</li><li>In the open properties file, remove the &quot;<em>JAVA_HOME=</em>&quot; argument value if it is not empty.</li><li>In the <em>&lt;modeling_tool installation directory&gt;/&lt;..&gt;</em>, replace the APP file with the downloaded one.</li><li>Start the application.</li><li>In the open message dialog, click <strong>Open</strong>.<br /><ac:image ac:thumbnail="true" ac:height="250"><ri:attachment ri:filename="Screenshot 2022-11-28 at 16.58.37.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a09ee009-29c9-410a-b2f3-0c05409fcbea"><ac:rich-text-body><p>After the APP is updated, the version displayed in the menu does not match the version in the <strong>About </strong>window. This is an expected behavior that has no impact on your modeling tool's functionality.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="3827e745-7a8a-43bf-bec5-96f10c0389e6"><ac:rich-text-body><p style="text-align: left;">The new APP contains Java 11.0.16. We highly recommend not changing the Java version.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=70395796 space=FAQ version=1 -->
## PAGE 00099: MagicDraw does not start on Mac OS X after a Java version upgrade to JDK/JRE 9 (Java 9) when using a no install file or running an application from a /bin directory. How do I solve this?

- page_id: `70395796`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395796/MagicDraw+does+not+start+on+Mac+OS+X+after+a+Java+version+upgrade+to+JDK+JRE+9+Java+9+when+using+a+no+install+file+or+running+an+application+from+a+bin+directory.+How+do+I+solve+this
- version_number: 1
- version_date: `2021-03-03T14:04:29.553+01:00`
- ancestors: Frequently Asked Questions > Java Virtual Machine (JVM)
- labels: []

### NORMALIZED CONTENT

Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.

The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.

If you are using an **earlier version than 18.4 SP1**and cannot start the modeling tool*, please do the following:

1. Download the original signed <modeling tool*>.dmg file and install the application again.
2. In bin\ magicdraw.properties** , set JAVA_HOME to the Java version installed in the <modeling_tool*_installation_directory >\java folder.

Example: *JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre*

1. Run magicdraw.sh*** file from the /bin folder.

*MagicDraw, Cameo EA, Cameo Systems Modeler

** cameoea.properties, csm.properties

***camocea.sh, csm.sh

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Java version 9 is set as the default system Java after updating Java. This Java version is not supported by our modeling tools*.</p><p>The solution is to download and install version 18.4 SP1 or a later original signed .dmg file, as it has the required Java version bundled in.</p><p>If you are using an <strong>earlier version than 18.4 SP1 </strong>and cannot start the modeling tool*, please do the following:</p><ol><li>Download the original signed <em>&lt;modeling tool*&gt;.dmg</em> file and install the application again.</li><li>In <em>bin\</em><em>magicdraw.properties**</em>, set <em>JAVA_HOME</em> to the Java version installed in the <em>&lt;modeling_tool*_installation_directory &gt;\java</em> folder.</li></ol><p>Example: <em>JAVA_HOME=/Applications/MagicDraw/jre1.8.0_102/mac/Contents/Home/jre</em></p><ol><li>Run magicdraw.sh*** file from the /bin folder.</li></ol><hr /><p>*MagicDraw, Cameo EA, Cameo Systems Modeler</p><p>** cameoea.properties, csm.properties</p><p>***camocea.sh, csm.sh</p>
````

<!--NOMAGIC_PAGE id=70395823 space=FAQ version=1 -->
## PAGE 00100: MagicDraw freezes. Do you know how to fix that?

- page_id: `70395823`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395823/MagicDraw+freezes.+Do+you+know+how+to+fix+that
- version_number: 1
- version_date: `2021-03-03T14:10:26.284+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, "MD log file" tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, &quot;MD log file&quot; tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).</span></p>
````

<!--NOMAGIC_PAGE id=70395833 space=FAQ version=1 -->
## PAGE 00101: MagicDraw Help cannot be invoked. What should I do?

- page_id: `70395833`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395833/MagicDraw+Help+cannot+be+invoked.+What+should+I+do
- version_number: 1
- version_date: `2021-03-03T14:12:33.487+01:00`
- ancestors: Frequently Asked Questions > Documentation / Help
- labels: []

### NORMALIZED CONTENT

Reasons why you cannot invoke the Help can be the following:

1. There is no reference to the topic, or a particular topic does not exist in MagicDraw Help. If a reference to the topic is broken, you can start the MagicDraw Help manually:

1.1. On the Help menu, click Help Content. The MagicDraw Help opens.

1.2. Browse in the help content or use a keyword to search for a particular topic.

Please let us know about broken links by contacting our customer support.

2. The communication with a server through Remote Method Invocation (RMI) is broken. Please do the following:

2.1. Open the mduml.properties* file. You can find the file in \bin.

2.2. To the JAVA_ARGS line, add a value -Dnostubfixing\=true, as it shown in the following example:

JAVA_ARGS=-Xmx1200M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -Dnostubfixing\=true

If the problem still persists, please contact our support team and attach the following files:

helpserver.log

md.log

You can find these files in one of the following ways:

Go to \.magicdraw\.

On the Help menu, click About MagicDraw. In the About dialog, select the Environment tab and then click the link next to Configuration Files.

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Reasons why you cannot invoke the Help can be the following:</p><p>1. There is no reference to the topic, or a particular topic does not exist in MagicDraw Help. If a reference to the topic is broken, you can start the MagicDraw Help manually:</p><p>1.1. On the Help menu, click Help Content. The MagicDraw Help opens.</p><p>1.2. Browse in the help content or use a keyword to search for a particular topic.</p><p>Please let us know about broken links by contacting our customer support.</p><p>2. The communication with a server through Remote Method Invocation (RMI) is broken. Please do the following:</p><p>2.1. Open the mduml.properties* file. You can find the file in \bin.</p><p>2.2. To the JAVA_ARGS line, add a value -Dnostubfixing\=true, as it shown in the following example:</p><p>JAVA_ARGS=-Xmx1200M -XX\:PermSize\=60M -XX\:MaxPermSize\=200M -Dnostubfixing\=true</p><p>If the problem still persists, please contact our support team and attach the following files:</p><p>helpserver.log</p><p>md.log</p><p>You can find these files in one of the following ways:</p><p>Go to \.magicdraw\.</p><p>On the Help menu, click About MagicDraw. In the About dialog, select the Environment tab and then click the link next to Configuration Files.</p><p> </p><p>* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p>
````

<!--NOMAGIC_PAGE id=85768944 space=FAQ version=2 -->
## PAGE 00102: Modeling

- page_id: `85768944`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/85768944/Modeling
- version_number: 2
- version_date: `2024-01-31T15:53:25.881+01:00`
- ancestors: Frequently Asked Questions
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4755ff53-b883-40b9-8c76-b8de2549bf2d" /></p>
````

<!--NOMAGIC_PAGE id=75348730 space=FAQ version=6 -->
## PAGE 00103: Modeling tool version 19.0 SP3 does not start after upgrading to Mac OS X Big Sur

- page_id: `75348730`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/75348730/Modeling+tool+version+19.0+SP3+does+not+start+after+upgrading+to+Mac+OS+X+Big+Sur
- version_number: 6
- version_date: `2021-05-25T13:47:48.003+02:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

###### The modeling tool* version 19.0 SP3 does not start after upgrading to Mac OS X Big Sur. How can I fix this issue?

This happens because the application is moved into quarantine.

To remove the application from quarantine

1. Open a terminal.
2. Write the command: xattr -r -d com.apple.quarantine /< modeling tool installation folder > ( e.g. "xattr -r -d com.apple.quarantine /Applications/MagicDraw")
3. Press Enter to execute the command.
4. Close the terminal and start the modeling tool* using the .app file.

*Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect, MagicDraw, Cameo Systems Modeler, and Cameo Enterprise Architecture

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h4>The modeling tool* version 19.0 SP3 does not start after upgrading to Mac OS X Big Sur. How can I fix this issue?</h4><p>This happens because the application is moved into quarantine.</p><p><br /></p><p>To remove the application from quarantine</p><hr /><ol><li>Open a terminal.</li><li>Write the command: <em>xattr -r -d com.apple.quarantine</em> /&lt;<em>modeling tool installation folder</em>&gt; (<em>e.g. &quot;xattr -r -d com.apple.quarantine /Applications/MagicDraw&quot;)</em></li><li>Press Enter to execute the command.</li><li>Close the terminal and start the modeling tool* using the .app file.</li></ol><p><br /></p><p>*<span style="color: rgb(62,63,64);">Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect, MagicDraw, Cameo Systems Modeler, and Cameo Enterprise Architecture </span></p>
````

<!--NOMAGIC_PAGE id=70395718 space=FAQ version=2 -->
## PAGE 00104: My modeling tool does not start on Mac OS X Sierra from a no install file using the .app file. What is a solution for it?

- page_id: `70395718`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395718/My+modeling+tool+does+not+start+on+Mac+OS+X+Sierra+from+a+no+install+file+using+the+.app+file.+What+is+a+solution+for+it
- version_number: 2
- version_date: `2021-03-03T12:51:44.237+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in *.zip/iso* files are not secure because of the dylib-hijacking problem. 
(Please find more about it at [https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/](https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/)). 
All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.

The solutions are:

1. To run magicdraw.sh file from the /bin directory.
2. To download the original signed MagicDraw.dmg file and to install the application again.
3. To remove the program from quarantine.

To remove the application from quarantine, please do:

1. Open a terminal.
2. Using the terminal, open the MagicDraw installation directory.
3. Write the command: xattr -d com.apple.quarantine MagicDraw.app/
4. Close the terminal and start MagicDraw using the .app file.

**NOTE:** This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.

Article to combine

[MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?](https://www.nomagic.com/support/faq)

Solution is to run *magicdraw.sh* file from the */bin* directory.

This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.

Please update your modeling tool to the **version 18.4 SP1** to avoid the installation incompatibility.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Mac OS X Sierra has an updated gatekeeper policy. It says that all applications which are downloaded in <em>.zip/iso</em> files are not secure because of the dylib-hijacking problem.<br />(Please find more about it at <a href="https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/" class="external-link" rel="nofollow">https://www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x/</a>).<br />All not secure programs, including the .app part of the application are moved to a temporary directory (quarantine), in other words, the application is improperly located and can not be started.</p><p>The solutions are:</p><ol><li>To run <em>magicdraw.sh</em> file from the  <em>/bin</em> directory.</li><li>To download the original signed <em>MagicDraw.dmg</em> file and to install the application again.</li><li>To remove the program from quarantine.</li></ol><p>To remove the application from quarantine, please do:</p><ol><li>Open a terminal.</li><li>Using the terminal, open the MagicDraw installation directory.</li><li>Write the command: <em>xattr -d com.apple.quarantine MagicDraw.app/</em></li><li>Close the terminal and start MagicDraw using the <em>.app</em> file.</li></ol><p><strong>NOTE:</strong> This issue is fixed for the 18.4 SP1 and 18.0 SP6 versions.</p><p><br /></p><p>Article to combine</p><p><br /></p><p><a class="external-link" href="https://www.nomagic.com/support/faq" rel="nofollow">MagicDraw 18.4 does not start after upgrading to Mac OS X Sierra. How can I fix this issue?</a></p><p>Solution is to run <em>magicdraw.sh</em> file from the <em>/bin</em> directory.</p><p>This issue affects the version 18.4 of MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture and Cameo Business Modeler.</p><p>Please update your modeling tool to the <strong>version 18.4 SP1</strong> to avoid the installation incompatibility.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=70401915 space=FAQ version=1 -->
## PAGE 00105: My modeling tool freezes when I open the Specification window while in full-screen mode on Mac OS X

- page_id: `70401915`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70401915/My+modeling+tool+freezes+when+I+open+the+Specification+window+while+in+full-screen+mode+on+Mac+OS+X
- version_number: 1
- version_date: `2021-03-22T14:50:12.958+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

This happens when your system preferences option “Prefer tabs” is set to “always” or “in full screen” (when using the modeling tool in Full-Screen mode).

To work around this issue, go to your Mac OS X System Preferences > General (for Mac OS BigSur) or Dock (for Mac OS Mojave or Catalina) > Prefer tabs and set it to “never".

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This happens when your system preferences option “Prefer tabs” is set to “always” or “in full screen” (when using the modeling tool in Full-Screen mode).</p><p>To work around this issue, go to your Mac OS X System Preferences &gt; General (for Mac OS BigSur) or Dock (for Mac OS Mojave or Catalina) &gt; Prefer tabs and set it to “never&quot;.</p>
````

<!--NOMAGIC_PAGE id=70395742 space=FAQ version=1 -->
## PAGE 00106: My modeling tool worked fine. I shut down my machine, started today, and MagicDraw won't start ?!?

- page_id: `70395742`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395742/My+modeling+tool+worked+fine.+I+shut+down+my+machine+started+today+and+MagicDraw+won+t+start
- version_number: 1
- version_date: `2021-03-03T13:08:40.696+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

This problem is Install Anywhere related and appears when you uninstall previous version of our modelling tools and then, without restarting your computer, install another modelling tool in the same directory. We would suggest to uninstall your modelling tool, restart your computer, and then install it again.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><span style="color: rgb(85,85,85);">This problem is Install Anywhere related and appears when you uninstall previous version of our modelling tools and then, without restarting your computer, install another modelling tool in the same directory. We would suggest to uninstall your modelling tool, restart your computer, and then install it again.</span></p>
````

<!--NOMAGIC_PAGE id=70395775 space=FAQ version=1 -->
## PAGE 00107: On new key application into FLEXnet licenses server lmadmin error appears – "Inconsistent server host name in: licenses\cameo\…

- page_id: `70395775`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395775/On+new+key+application+into+FLEXnet+licenses+server+lmadmin+error+appears+%E2%80%93+Inconsistent+server+host+name+in+licenses+cameo+%E2%80%A6
- version_number: 1
- version_date: `2021-03-03T13:59:00.657+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.

Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This error appears if key with different hostid is added into server. Server memorizes host added with first key and does not accept another one, if different host is used in second key. This is known issue which fix is planed with new version of lmadmin.</p><p>Please reinstall Lmadmin before applying key with different hostid. This will allow voiding this issue.</p>
````

<!--NOMAGIC_PAGE id=68526633 space=FAQ version=6 -->
## PAGE 00108: Performance

- page_id: `68526633`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/68526633/Performance
- version_number: 6
- version_date: `2021-03-04T07:18:14.418+01:00`
- ancestors: Frequently Asked Questions
- labels: ['performance']

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="49a6cd6e-6249-46f3-a760-f666e11b639f" /></p>
````

<!--NOMAGIC_PAGE id=70389762 space=FAQ version=4 -->
## PAGE 00109: Performance (Copy)

- page_id: `70389762`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70389762/Performance+Copy
- version_number: 4
- version_date: `2024-01-23T08:45:49.585+01:00`
- ancestors: Current FAQ for Review
- labels: []

### NORMALIZED CONTENT

#### EXPAND: Where can I find log files of a modeling tool, Cameo Collaborator and Teamwork Cloud?

Where can I find log files of a modeling tool, Cameo Collaborator and Teamwork Cloud?

When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.

**Accessing log files**

- For a modeling tool:

Open your modeling tool and in the main menu go to **Help** > **About <modeling tool name>**. In the **Environment** tab, click the link provided in the **Log File** line to open a log file.

Or

Go to *<user.home>\<.modeling tool name>\<modeling tool version>* directory**and obtain *<modeling tool name>.log* file.

Default path for Windows*: C:\Users\<USERNAME>\AppData\Local\.<modeling tool name>\<modeling tool version number>* 
Default path for other operating systems: *<user.home>/.<modeling tool name>/< modeling tool version number>*

- For WebApp/Cameo Collaborator for Teamwork Cloud:

Go to *<WebAppPlatform installation directory>/logs/webappplatform* directory, and obtain the *web-app.log* and/or *collaborator.log* files.

Default path for Linux: */opt/local/TeamworkCloud/WebAppPlatform/logs/webappplatform*

Default path for Windows: *C:\Program Files\TeamworkCloud\WebAppPlatform\logs\webappplatform*

- For Teamwork Cloud:

Go to the *<user.home>\.twcloud\<version number>* directory and obtain the *server.log* file.

Default path for Linux: */home/twcloud/.twcloud/<version>*Default path for Windows: *C:\Users\<USER>\.twcloud\<version>*

Go to the *<user.home>\.authserver\<version number>* directory and obtain the *authserver.log*file.

Default path for Linux: */home/twcloud/.authserver/<version>*Default path for Windows: *C:\Users\<USER>\.authserver\<version>*

- For Cassandra:

Go to *<Cassandra installation directory>\logs* directory and obtain the *cassandra.log* file.

Default path for Linux: */var/log/cassandra*Default path for Windows: *C:\apache-cassandra-<version>\logs*

- Properties files for Teamwork Cloud:

Default for Linux: 
*/opt/local/TeamworkCloud/configuration/application.conf**/opt/local/TeamworkCloud/Authserver/config/authserver.properties**/opt/local/TeamworkCloud/WebAppPlatform/shared/conf/webappplatform.properties*

Default for Windows: 
*C:\Program Files\TeamworkCloud\configuration\application.conf**C:\Program Files\TeamworkCloud\Authserver\config\authserver.properties**C:\Program Files\TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties*

- For Cameo Collaborator for Alfresco:

Go to Alfresco Community installation directory, and obtain the *alfresco.log*, *share.log* and *solr.log*files.

Go to *<Alfresco Community installation directory>\tomcat\logs*, and obtain the *alfrescotomcat-stderr.log, alfrescotomcat-stdout.log* and *catalina.log* files.

**Generating a log file**

If the performance of your modeling tool declines or it freezes, go to *<modeling tool installation directory>\bin,*and run the *submit_issue.exe* or *submit_issue.sh* file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file as described above.

**Java crash log files**

If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the *<modeling tool installation directory>/bin* or *<modeling tool installation directory>*directory. The names of these log files start with "hs_err", e.g., *hs_err_pid15693.log*. If you find the Java crash log file, it indicates that Java was the reason of your modeling tool crash.

#### EXPAND: After loading a project, there wasn’t a big memory usage but after some actions it increased dramatically. How could I manage it?

After loading a project, there wasn’t a big memory usage but after some actions it increased dramatically. How could I manage it?

In order to troubleshoot this issue, we will need the program’s log files (located in the install directory of your tool). Additional information might be required about the Java environment on which our modeling tools are based. The information we need is called the “heapdump” and can be obtained using the Java VisualVM program.

Please read and follow this procedure to install Java VisualVM and send this data to us (while the tool is running):

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ , if you do not have it.
2. Start Task Manager or other appropriate tool depending on your OS.
3. Start Java VisualVM. If you have selected the default location on the JDK installation process, VisualVm is located in C:\Program Files\Java\jdk<version number>\bin\ jvisualvm.exe. Otherwise start the jvisualvm.exe from your custom location.
4. In the Task Manager or other program according to you OS, find the PID (Process Identifier) of your modeling tool.
5. In the Java VisualVM, find Java process by the modeling tool PID and double click to open it.
6. Right click the Java process and, from the shortcut menu, select Heap Dump . The heapdump file creates under your process.
7. Save the heapdump file. Right click the heapdump and, on the shortcut menu, click Save As .
8. Register an issue and sent the saved *.hprof file for the investigation. For this, on the main menu of your modeling tool, click Help > Report an Issue

#### EXPAND: I suspect a performance problem. How do I solve it?

I suspect a performance problem. How do I solve it?

To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:

**Generating a log file when the modeling tool freezes or performs slowly:**

1. When a modeling tool runs slowly or freezes, open*<modeling tool installation directory>\bin,* and run *submit_issue.exe* several times. It dumps threads into the log file.

2. Click **Help** > **About** on the main menu of your modeling tool. In the open dialog, select the **Environment** tab and click the **Log File** link. The log file opens.[*](https://www.nomagic.com/support/faq#path)

3. Save the file and register an issue. Click **Help** >**Report an Issue** on the main menu of your modeling tool

*If a modeling tool is inactive, you can find the log file under:

- For Windows OS: C:\Users\<USERNAME>\AppData\Local\.<modeling tool name>\<modeling tool version number>
- For Other OS: <user.home>/.<modeling tool name>/< modeling tool version number>

**By using Java VisualVM:**

Our modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.

The following steps outline how to obtain the data from VisualVM:

**Note.**Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.

**On Windows OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Task Manager .
3. Start Java VisualVM . If you selected the default location on the JDK installation process, VisualVM is located in C:\Program Files\Java\jdk<version number>\bin\ jvisualvm.exe . Otherwise, start the exe from your customized location.
4. Start the modeling tool.
5. In Task Manager , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Task Manager ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. Raise a support ticket via 3DSupport application and attach the .nps file to the ticket.

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start Activity Monitor .
3. Start Java VisualVM . If you selected the default location on the JDk installation process, VisualVM is located in /Library/Java/JavaVirtualMachines/jdk<version number>.jdk /Contents/Home/bin/jvisualvm . Otherwise, start **jvisualvm** from your customized location.
4. Start the modeling tool.
5. In Activity Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in Activity Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished and click the Stop button.
10. In the CPU samples tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the *.nps file.
12. Raise a support ticket via 3DSupport application and attach the .nps file to the ticket.

**On Linux OS:**

1. Download and install the Java VisualVM with Java SE Development Kit (JDK , valid till version 1.8 ) or separately from https://visualvm.github.io/ .
2. Start System Monitor .
3. To start Java VisualVM , execute the jvisualvm tool from the bin directory of the JDK. When the tool runs, the Java VisualVM window opens.
4. Start the modeling tool.
5. In System Monitor , find the PID (Process Identifier) of your modeling tool.
6. In Java VisualVM , find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in System Monitor ) and double-click to open it.
7. Click the Sampler tab and click the CPU .
8. Initiate the action causing the low performance of your modeling tool.
9. Wait until that action in your modeling tool is finished, then click the Stop button .
10. In the CPU samples tab, click the Snapshot button . The snapshot is created in the Applications tree on the left.
11. To save the snapshot, right-click it and select Save As to save the **.nps* file .
12. Raise a support ticket via 3DSupport application and attach the .nps file to the ticket.

#### EXPAND: [To Be Reviewed]From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?

[To Be Reviewed]From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?

While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.

In order to analyze and fix the issue, more information is required. Please provide us with the following information:

1. Can you reproduce the problem? If yes, what are the steps to reproduce it?
2. If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.
3. Send us the memory dump file. It may help to detect the problem.

To create a memory dump file, please do the following:

1. In the properties * file, append JAVA_ARGS parameters as follows: -XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots
2. Start your modeling tool.

The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.

*

- For MagicDraw, the properties file is*magcdraw.properties* (*mduml.properties* for MagicDraw version 17.0.4 or earlier).
- For Cameo Enterprise Architecture, the properties files is *cameoea.properties*.
- For Cameo Systems Modeleer, the properties files is *csm.properties*.
- For Cameo Business Modeler, the properties file is *csm.properties*.

#### EXPAND: MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?

MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?

This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select**Options**>**Look and Feel**>**Metal**.

#### EXPAND: [To Be Reviewed]Sometimes when running the program the OutOfMemory error occurs.

[To Be Reviewed]Sometimes when running the program the OutOfMemory error occurs.

If you are running the Sun's JVM, set the following java properties in your mduml.properties* file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.

For example:

JAVA_ARGS=-Xmx800M

This sets java heap size to 800 megabytes.

If you get exception "java.lang.OutOfMemoryError: PermGen space" please, check if PermSize is specified in mduml.properties* file.

The JAVA_ARGS line should look like:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M

If PermSize is specified in mduml.properties* file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.

For example:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

#### EXPAND: [To Be Reviewed]MagicDraw freezes. Do you know how to fix that?

[To Be Reviewed]MagicDraw freezes. Do you know how to fix that?

In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, "MD log file" tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).

#### EXPAND: [To Be Reviewed]When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.

[To Be Reviewed]When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.

We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.

#### EXPAND: [To Be Reviewed]What are the common recommendations to increase performance?

[To Be Reviewed]What are the common recommendations to increase performance?

When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase an efficiency of modeling, we suggest the following solutions:

- Increase a java heap size.
- Do not keep unused diagrams open. Open project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.
- Increase an active validation period. MagicDraw takes less memory with increased active validations period.
- Split the project to read only modules. Keep read only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.
- Use Garbage Collector to free unused memory.
- Turn of antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.

For more information see "MagicDraw User Manual" > "Performance Improvement" section. Manual is available in < MagicDraw installation directory > \manual\

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="5def86c2-1ad1-4944-958d-76c1cb5b4529"><ac:parameter ac:name="title">Where can I find log files of a modeling tool, Cameo Collaborator and Teamwork Cloud?</ac:parameter><ac:rich-text-body><p>When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.</p><p><strong>Accessing log files</strong></p><ul><li><strong>For a modeling tool:</strong></li></ul><p>Open your modeling tool and in the main menu go to <strong>Help</strong> &gt; <strong>About &lt;modeling tool name&gt;</strong>. In the <strong>Environment</strong> tab, click the link provided in the <strong>Log File</strong> line to open a log file.</p><p>Or </p><p>Go to <em>&lt;user.home&gt;\&lt;.modeling tool name&gt;\&lt;modeling tool version&gt;</em> directory<em> </em>and obtain <em>&lt;modeling tool name&gt;.log</em> file.</p><p>Default path for Windows<em>: C:\Users\&lt;USERNAME&gt;\AppData\Local\.&lt;modeling tool name&gt;\&lt;modeling tool version number&gt;</em><br />Default path for other operating systems: <em>&lt;user.home&gt;/.&lt;modeling tool name&gt;/&lt; modeling tool version number&gt;</em></p><ul><li><strong>For WebApp/Cameo Collaborator for Teamwork Cloud:</strong></li></ul><p>Go to <em>&lt;WebAppPlatform installation directory&gt;/logs/webappplatform</em> directory, and obtain the <em>web-app.log</em> and/or <em>collaborator.log</em> files.</p><p>Default path for Linux: <em>/opt/local/TeamworkCloud/WebAppPlatform/logs/webappplatform</em></p><p>Default path for Windows: <em>C:\Program Files\TeamworkCloud\WebAppPlatform\logs\webappplatform</em></p><ul><li><strong>For Teamwork Cloud:</strong></li></ul><p>Go to the <em>&lt;user.home&gt;\.twcloud\&lt;version number&gt;</em> directory and obtain the <em>server.log</em> file.</p><p>Default path for Linux: <em>/home/twcloud/.twcloud/&lt;version&gt;<br /></em>Default path for Windows: <em>C:\Users\&lt;USER&gt;\.twcloud\&lt;version&gt;</em></p><p>Go to the <em>&lt;user.home&gt;\.authserver\&lt;version number&gt;</em> directory and obtain the <em>authserver.log </em>file.</p><p>Default path for Linux: <em>/home/twcloud/.authserver/&lt;version&gt;<br /></em>Default path for Windows: <em>C:\Users\&lt;USER&gt;\.authserver\&lt;version&gt;</em></p><ul><li><strong>For Cassandra:</strong></li></ul><p>Go to <em>&lt;Cassandra installation directory&gt;\logs</em> directory and obtain the <em>cassandra.log</em> file.</p><p>Default path for Linux: <em>/var/log/cassandra<br /></em>Default path for Windows: <em>C:\apache-cassandra-&lt;version&gt;\logs</em></p><ul><li><strong>Properties files for Teamwork Cloud:</strong></li></ul><p>Default for Linux:<br /><em>/opt/local/TeamworkCloud/configuration/application.conf<br /></em><em>/opt/local/TeamworkCloud/Authserver/config/authserver.properties<br /></em><em>/opt/local/TeamworkCloud/WebAppPlatform/shared/conf/webappplatform.properties</em></p><p>Default for Windows:<br /><em>C:\Program Files\TeamworkCloud\configuration\application.conf<br /></em><em>C:\Program Files\TeamworkCloud\Authserver\config\authserver.properties<br /></em><em>C:\Program Files\TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties</em></p><ul><li><strong>For Cameo Collaborator for Alfresco:</strong></li></ul><p>Go to Alfresco Community installation directory, and obtain the <em>alfresco.log</em>, <em>share.log</em> and <em>solr.log </em>files.</p><p>Go to <em>&lt;Alfresco Community installation directory&gt;\tomcat\logs</em>, and obtain the <em>alfrescotomcat-stderr.log, alfrescotomcat-stdout.log</em> and <em>catalina.log</em> files.</p><p><strong>Generating a log file</strong></p><p>If the performance of your modeling tool declines or it freezes, go to <em>&lt;modeling tool installation directory&gt;\bin, </em>and run the <em>submit_issue.exe</em> or <em>submit_issue.sh</em> file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file as described above.</p><p><strong>Java crash log files</strong></p><p>If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the <em>&lt;modeling tool installation directory&gt;/bin</em> or <em>&lt;modeling tool installation directory&gt; </em>directory. The names of these log files start with &quot;hs_err&quot;, e.g., <em>hs_err_pid15693.log</em>. If you find the Java crash log file, it indicates that Java was the reason of your modeling tool crash.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="84db34bc-4ccb-42c1-86b9-bb2fd917daea"><ac:parameter ac:name="title">After loading a project, there wasn’t a big memory usage but after some actions it increased dramatically. How could I manage it?</ac:parameter><ac:rich-text-body><p>In order to troubleshoot this issue, we will need the program’s log files (located in the install directory of your tool). Additional information might be required about the Java environment on which our modeling tools are based. The information we need is called the “heapdump” and can be obtained using the Java VisualVM program.</p><p>Please read and follow this procedure to install Java VisualVM and send this data to us (while the tool is running):</p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/" class="external-link" title="Follow link">https://visualvm.github.io/</a>, if you do not have it.</li><li>Start Task Manager or other appropriate tool depending on your OS.</li><li>Start Java VisualVM. If you have selected the default location on the JDK installation process, VisualVm is located in C:\Program Files\Java\jdk&lt;version number&gt;\bin\ jvisualvm.exe. Otherwise start the jvisualvm.exe from your custom location.</li><li>In the Task Manager or other program according to you OS, find the PID (Process Identifier) of your modeling tool.</li><li>In the Java VisualVM, find Java process by the modeling tool PID and double click to open it.</li><li>Right click the Java process and, from the shortcut menu, select <strong>Heap Dump</strong>. The heapdump file creates under your process.</li><li>Save the heapdump file. Right click the heapdump and, on the shortcut menu, click <strong>Save As</strong>.</li><li>Register an issue and sent the saved *.hprof file for the investigation. For this, on the main menu of your modeling tool, click <strong>Help</strong> &gt; <strong>Report an Issue</strong></li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="dfc0f036-c3bc-4b5c-89db-712ea73cb911"><ac:parameter ac:name="title">I suspect a performance problem. How do I solve it?</ac:parameter><ac:rich-text-body><p>To solve the problem, we need a little input from you. We need to examine the log files to troubleshoot the problem. The following list outlines how to submit log files:</p><p><strong>Generating a log file when the modeling tool freezes or performs slowly:</strong></p><p>1. When a modeling tool runs slowly or freezes, open<em> &lt;modeling tool installation directory&gt;\bin,</em> and run <em>submit_issue.exe</em> several times. It dumps threads into the log file.</p><p>2. Click <strong>Help</strong> &gt; <strong>About</strong> on the main menu of your modeling tool. In the open dialog, select the <strong>Environment</strong> tab and click the <strong>Log File</strong> link. The log file opens.<a href="https://www.nomagic.com/support/faq#path">*</a></p><p>3. Save the file and register an issue. Click <strong>Help</strong> &gt;<strong> Report an Issue</strong> on the main menu of your modeling tool</p><p style="">*If a modeling tool is inactive, you can find the log file under:</p><ul style=""><li>For Windows OS: C:\Users\&lt;USERNAME&gt;\AppData\Local\.&lt;modeling tool name&gt;\&lt;modeling tool version number&gt;</li><li>For Other OS: &lt;user.home&gt;/.&lt;modeling tool name&gt;/&lt; modeling tool version number&gt;<br /><br /></li></ul><p><strong>By using Java VisualVM:</strong></p><p style="text-align: justify;">Our modeling tools are Java-based; thus, you can use the Java VisualVM program for performance issue examination. Data provided by VisualVM may help to explore issues accurately.</p><p style="text-align: justify;">The following steps outline how to obtain the data from VisualVM:</p><p><strong>Note. </strong>Please read the steps first to familiarize yourself with the whole procedure to gather more precise information. Step #8 should be started as soon as possible.</p><p><strong>On Windows OS:</strong></p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/" class="external-link" title="Follow link">https://visualvm.github.io/</a>.</li><li>Start <strong>Task Manager</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDK installation process, VisualVM is located in <em>C:\Program Files\Java\jdk&lt;version number&gt;\bin\ jvisualvm.exe</em>. Otherwise, start the <em>exe</em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Task Manager</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Task Manager</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>Raise a support ticket via 3DSupport application and attach the .nps file to the ticket. </li></ol><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a title="Follow link" class="external-link" href="https://visualvm.github.io/">https://visualvm.github.io/</a>.</li><li>Start <strong>Activity Monitor</strong>.</li><li>Start <strong>Java VisualVM</strong>. If you selected the default location on the JDk installation process, VisualVM is located in <em>/Library/Java/JavaVirtualMachines/jdk&lt;version number&gt;.jdk /Contents/Home/bin/jvisualvm</em>. Otherwise, start <em><strong>jvisualvm</strong></em> from your customized location.</li><li>Start the modeling tool.</li><li>In <strong>Activity Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>Activity Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished and click the Stop button.</li><li>In the CPU <strong>samples</strong> tab, click the Snapshot button. The snapshot is created in the Applications tree on the left.</li><li>To save the snapshot, right-click it and select Save As to save the <em>*.nps</em> file.</li><li>Raise a support ticket via 3DSupport application and attach the .nps file to the ticket. </li></ol><p><strong>On Linux OS:</strong></p><ol><li><a href="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Download </a>and install the <strong>Java VisualVM </strong>with <strong>Java SE Development Kit (JDK</strong>, valid<strong> </strong>till version 1.8<strong>) </strong>or separately from <a href="https://visualvm.github.io/" class="external-link" title="Follow link">https://visualvm.github.io/</a>.</li><li>Start <strong>System Monitor</strong>.</li><li>To start <strong>Java VisualVM</strong>, execute the <strong>jvisualvm</strong> tool from the <strong>bin</strong> directory of the JDK. When the tool runs, the <strong>Java VisualVM</strong> window opens.</li><li>Start the modeling tool.</li><li>In <strong>System Monitor</strong>, find the PID (Process Identifier) of your modeling tool.</li><li>In <strong>Java VisualVM</strong>, find the Java process by the modeling tool PID in the Applications tree on the left (the same PID as in <strong>System Monitor</strong>) and double-click to open it.</li><li>Click the <strong>Sampler</strong> tab and click the <strong>CPU</strong>.</li><li>Initiate the action causing the low performance of your modeling tool.</li><li>Wait until that action in your modeling tool is finished, then click the <strong>Stop button</strong>.</li><li>In the <strong>CPU</strong> <strong>samples</strong> tab, click the <strong>Snapshot button</strong>. The snapshot is created in the <strong>Applications</strong> tree on the left.</li><li>To save the snapshot, right-click it and select <strong>Save As to save the <em>*.nps</em> file</strong>.</li><li>Raise a support ticket via 3DSupport application and attach the .nps file to the ticket. </li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="254bfdd8-c4b5-4f1d-8e9c-e5a941f51503"><ac:parameter ac:name="title">[To Be Reviewed]From time to time, we receive Out Of Memory exceptions. I suspect that these exceptions are caused by MagicDraw memory leaks. How would you suggest solving this problem?</ac:parameter><ac:rich-text-body><p>While performing small ordinary tasks (not individual large operations, such as opening a large project or merging several large projects), modeling tool memory leaks may cause OutOfMemory exception errors. This is due to the cumulative effect of performing many small operations that normally do not cause any problems.</p><p>In order to analyze and fix the issue, more information is required. Please provide us with the following information:</p><ol><li>Can you reproduce the problem? If yes, what are the steps to reproduce it?</li><li>If it is possible to reproduce it, send us the project file. We guarantee confidentiality, and shall sign a Non-disclosure Agreement at your request.</li><li>Send us the memory dump file. It may help to detect the problem.</li></ol><p>To create a memory dump file, please do the following:</p><ol><li>In the properties<span>*</span> file, append JAVA_ARGS parameters as follows:<br />-XX\:+HeapDumpOnOutOfMemoryError -XX\:HeapDumpPath\=d\:\\snapshots</li><li>Start your modeling tool.</li></ol><p>The dump file will be created in the provided location – d:\\snapshots (please make sure that this location is available), if an OutOfMemory exception occurs. As the file may be large, please zip the created file, and upload it to the provided ftp server.</p><p><br /></p><hr /><p><span>*</span></p><ul><li><span><span> </span>For MagicDraw, the properties file is<em> magcdraw.properties</em> (<em>mduml.properties</em> for MagicDraw version 17.0.4 or earlier).</span></li><li><span>For Cameo Enterprise Architecture, the properties files is <em>cameoea.properties</em>.</span></li><li><span>For Cameo Systems Modeleer, the properties files is <em>csm.properties</em>. </span></li><li><span>For Cameo Business Modeler, the properties file is <em>csm.properties</em>.</span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="01785e9e-d1e9-4d9d-9396-5bdf6db146f1"><ac:parameter ac:name="title">MagicDraw does not display Chinese, Hindi, Japanese, Korean, Thai, or some special symbols, such as superscript and subscript. Can this be fixed?</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">This issue appears when MagicDraw Look and Feel is Windows. Please change the Look and Feel to Metal. For this, select </span><strong>Options</strong><span style="color: rgb(85,85,85);"> &gt; </span><strong>Look and Feel</strong><span style="color: rgb(85,85,85);"> &gt; </span><strong>Metal</strong><span style="color: rgb(85,85,85);">.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="5956860e-4f68-4756-a147-7ae635027f6d"><ac:parameter ac:name="title">[To Be Reviewed]Sometimes when running the program the OutOfMemory error occurs.</ac:parameter><ac:rich-text-body><p>If you are running the Sun's JVM, set the following java properties in your mduml.properties<span>*</span> file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.</p><p>For example:</p><p>JAVA_ARGS=-Xmx800M</p><p>This sets java heap size to 800 megabytes.</p><p>If you get exception &quot;java.lang.OutOfMemoryError: PermGen space&quot; please, check if PermSize is specified in mduml.properties<span>*</span> file.</p><p>The JAVA_ARGS line should look like:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M</p><p>If PermSize is specified in mduml.properties<span>*</span> file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.</p><p>For example:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M</p><p><br /></p><p><span>*</span> If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="c8466ac4-b134-4741-8997-ee1182ca1740"><ac:parameter ac:name="title">[To Be Reviewed]MagicDraw freezes. Do you know how to fix that?</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">In cases when MagicDraw is not responding, please, run submit_issue.exe. You may find it in /bin/ folder. In case there are processes, submit issue produces thread dump for it and writes it to md.log file. You can grab thread dump directly from Report an Issue frame, &quot;MD log file&quot; tab. Please attach thread dump to this issue report or send us md.log file. This log can be found in the user home directory ( /.magicdraw/ ).</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="4c447e95-e47e-47d9-86fe-e64963658493"><ac:parameter ac:name="title">[To Be Reviewed]When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.</ac:parameter><ac:rich-text-body><p><span style="color: rgb(85,85,85);">We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="241000a8-fc39-4333-b1f1-dfd221154906"><ac:parameter ac:name="title">[To Be Reviewed]What are the common recommendations to increase performance?</ac:parameter><ac:rich-text-body><p>When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase an efficiency of modeling, we suggest the following solutions:</p><ul><li>Increase a java heap size.</li><li>Do not keep unused diagrams open. Open project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.</li><li>Increase an active validation period. MagicDraw takes less memory with increased active validations period.</li><li>Split the project to read only modules. Keep read only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.</li><li>Use Garbage Collector to free unused memory.</li><li>Turn of antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.</li></ul><p>For more information see &quot;MagicDraw User Manual&quot; &gt; &quot;Performance Improvement&quot; section. Manual is available in &lt; MagicDraw installation directory &gt; \manual\</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=111224032 space=FAQ version=2 -->
## PAGE 00110: Publishing is taking a long time

- page_id: `111224032`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/111224032/Publishing+is+taking+a+long+time
- version_number: 2
- version_date: `2023-01-25T18:07:12.212+01:00`
- ancestors: Frequently Asked Questions > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

If publishing takes a very long time, it may be because your project has large diagrams, matrices, or tables.

**Solution:**

When publishing, set a smaller project scope excluding unnecessary diagrams and tables instead of publishing the whole project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If publishing takes a very long time, it may be because your project has large diagrams, matrices, or tables.</p><p><br /></p><p><strong>Solution:</strong></p><p>When publishing, set a smaller project scope excluding unnecessary diagrams and tables instead of publishing the whole project.</p>
````

<!--NOMAGIC_PAGE id=75342927 space=FAQ version=8 -->
## PAGE 00111: Receiving error message that the invalid installation when launching my modeling tool

- page_id: `75342927`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/75342927/Receiving+error+message+that+the+invalid+installation+when+launching+my+modeling+tool
- version_number: 8
- version_date: `2021-05-10T13:43:35.301+02:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

##### Question

I receive an "Invalid installation of <modeling tool name> has been detected:" error message when launching my modeling tool. How do I solve this issue?

##### Symptoms:

When you try launching your modeling tool, it does not start and you receive an error message similar to the one below:

[IMAGE alt='' src='']

##### Resolution:

To resolve this issue, perform the following steps:

1. Uninstall the modeling tool experiencing the issue.
2. Delete the configuration files folder. You can find information for accessing this folder here: https://docs.nomagic.com/display/MD2021x/Configuration+files
3. Restart your computer
4. Install the modeling tool again
5. Try starting the application to see if your issue is resolved.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Question</h3><p>I receive an &quot;Invalid installation of &lt;modeling tool name&gt; has been detected:&quot; error message when launching my modeling tool. How do I solve this issue?</p><h3>Symptoms:</h3><p>When you try launching your modeling tool, it does not start and you receive an error message similar to the one below: </p><p><ac:image><ri:attachment ri:filename="106645_error.png" /></ac:image></p><h3>Resolution:</h3><p>To resolve this issue, perform the following steps:</p><ol><li>Uninstall the modeling tool experiencing the issue. </li><li>Delete the configuration files folder. You can find information for accessing this folder here: <a href="https://docs.nomagic.com/display/MD2021x/Configuration+files">https://docs.nomagic.com/display/MD2021x/Configuration+files</a></li><li>Restart your computer</li><li>Install the modeling tool again </li><li>Try starting the application to see if your issue is resolved. </li></ol>
````

<!--NOMAGIC_PAGE id=70395820 space=FAQ version=1 -->
## PAGE 00112: Sometimes when running the program the OutOfMemory error occurs.

- page_id: `70395820`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395820/Sometimes+when+running+the+program+the+OutOfMemory+error+occurs.
- version_number: 1
- version_date: `2021-03-03T14:10:02.565+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

If you are running the Sun's JVM, set the following java properties in your mduml.properties* file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.

For example:

JAVA_ARGS=-Xmx800M

This sets java heap size to 800 megabytes.

If you get exception "java.lang.OutOfMemoryError: PermGen space" please, check if PermSize is specified in mduml.properties* file.

The JAVA_ARGS line should look like:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M

If PermSize is specified in mduml.properties* file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.

For example:

JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M

* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you are running the Sun's JVM, set the following java properties in your mduml.properties* file: in the line JAVA_ARGS=-Xmx600M, change the number of heap size '600' to maximal heap size in megabytes.</p><p>For example:</p><p>JAVA_ARGS=-Xmx800M</p><p>This sets java heap size to 800 megabytes.</p><p>If you get exception &quot;java.lang.OutOfMemoryError: PermGen space&quot; please, check if PermSize is specified in mduml.properties* file.</p><p>The JAVA_ARGS line should look like:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=150M</p><p>If PermSize is specified in mduml.properties* file and the same problem still appears, the MaxPermSize should be increased. PermSize is part of heap size, so MaxPermSize should always be smaller than heap size specified with Xmx parameter.</p><p>For example:</p><p>JAVA_ARGS=-Xmx600M -XX\:PermSize\=40M -XX\:MaxPermSize\=200M</p><p> </p><p>* If you are using MagicDraw 17.0.5 or later, the name of the property file is magicdraw.properties.</p>
````

<!--NOMAGIC_PAGE id=70402529 space=FAQ version=3 -->
## PAGE 00113: Teamwork Cloud

- page_id: `70402529`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70402529/Teamwork+Cloud
- version_number: 3
- version_date: `2024-01-31T11:25:06.815+01:00`
- ancestors: Frequently Asked Questions
- labels: ['teamwork-cloud']

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1f1616e0-b959-4ebb-aae0-a3546f3504fc" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=85767348 space=FAQ version=9 -->
## PAGE 00114: The labels are not displayed for Item Flows in IBD diagrams

- page_id: `85767348`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/85767348/The+labels+are+not+displayed+for+Item+Flows+in+IBD+diagrams
- version_number: 9
- version_date: `2022-01-11T15:15:23.292+01:00`
- ancestors: Frequently Asked Questions > Modeling
- labels: []

### NORMALIZED CONTENT

###### Q.: Why aren't the labels displayed for Item Flows in Internal Block Diagram(IBD) diagrams?

A.: In some cases, in Internal Block Diagrams (IBD) and other diagrams, labels are intentionally not displayed to avoid a negative impact on diagram layouts. When conveyed items are created in new or existing diagrams, they are displayed automatically throughout the diagrams and can be displaced.

For the information about how to display the conveyed items, see [CONFLUENCE_PAGE title='Information Flow' space='MD2021xR2'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h4>Q.: Why aren't the labels displayed for Item Flows in <span style="color: rgb(62,63,64);">Internal Block Diagram </span>(IBD) diagrams?</h4><p>A.: In some cases, in <span style="color: rgb(62,63,64);">Internal Block Diagrams (</span>IBD) and other diagrams, labels are intentionally not displayed to avoid a negative impact on diagram layouts. When conveyed items are created in new or existing diagrams, they are displayed automatically throughout the diagrams and can be displaced.</p><p>For the information about how to display the conveyed items, see <ac:link ac:anchor="SettinganInformationFlow"><ri:page ri:space-key="MD2021xR2" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Setting an Information Flow]]></ac:plain-text-link-body></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=70405630 space=FAQ version=7 -->
## PAGE 00115: Unable to save TWCloud project locally

- page_id: `70405630`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70405630/Unable+to+save+TWCloud+project+locally
- version_number: 7
- version_date: `2021-04-26T05:09:52.866+02:00`
- ancestors: Frequently Asked Questions > Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

##### Issue/Symptoms:

Users are unable to save a Teamwork Cloud project locally, and see error messages similar to:

[IMAGE alt='' src='']

Users also see similar entries observed in the modeling tool log file:

```text
com.nomagic.esi.api.messages.exceptions.NotAuthorizedException: Not authorized to process com.nomagic.esi.core.msg.GetCommitInfosMsgat com.nomagic.esi.client.core.a.c.d.a(d.java:82)
```

```text
at com.nomagic.esi.client.core.a.c.d.a(d.java:122)
	at com.nomagic.esi.client.core.a.c.i.getCommitInfo(i.java:269)
	at com.nomagic.magicdraw.esi.session.impl.w.b(w.java:72)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.callOnline(OnlineExecutor.java:83)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.callOnline(OnlineExecutor.java:54)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.getOnline(OnlineExecutor.java:113)
	at com.nomagic.magicdraw.esi.session.impl.w.a(w.java:102)
	at com.nomagic.magicdraw.esi.session.impl.w.a(w.java:72)
	at com.nomagic.magicdraw.esi.session.f$c.a(f$c.java:1108)
	at com.nomagic.magicdraw.esi.persistence.c.c.a(c.java:115)
	at com.nomagic.magicdraw.esi.persistence.c.c.a(c.java:98)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:743)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:2470)
	at com.nomagic.magicdraw.esi.rellocate.b.f.b(f.java:518)
	at com.nomagic.magicdraw.esi.rellocate.b.f.c(f.java:424)
	at com.nomagic.magicdraw.persistence.ProjectLoadService.callWithoutAddToRecentFiles(ProjectLoadService.java:1333)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:424)
	at com.nomagic.magicdraw.esi.rellocate.b.f.access$100(f.java:195)
	at com.nomagic.magicdraw.esi.rellocate.b.f$i.execute(f$i.java:378)
	at com.nomagic.task.Task.construct(Task.java:192)
	at com.nomagic.task.SwingWorker$2.call(SwingWorker.java:209)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at com.nomagic.task.SwingWorker$SwingWorkerFuture.run(SwingWorker.java:596)
	at com.nomagic.task.BackportedThreadPoolExecutor$Worker.runTask(BackportedThreadPoolExecutor.java:1593)
	at com.nomagic.task.BackportedThreadPoolExecutor$Worker.run(BackportedThreadPoolExecutor.java:1624)
	at com.nomagic.task.PooledThread.run(PooledThread.java:64)
```

##### Solution:

If a user does not have "Read Resources" permission for all used projects (directly and indirectly used), the user cannot save the project. This is a known issue, and is fixed in version 2021x.

To work around the issue (without upgrading your version), please check which permissions the user has. The user needs at least the "Read Resources" permission or "Resource Reviewer" role for all used projects (directly and indirectly used). Permissions and roles can be assigned to the user through the "TWCloud Admin" web application.

See the procedures on how to sign into that application at [https://docs.nomagic.com/display/TWCloud190SP3/Sign+into+TWCloud+Admin](https://docs.nomagic.com/display/TWCloud190SP3/Sign+into+TWCloud+Admin). 
This link outlines how to assign permission/role to a user: [https://docs.nomagic.com/display/TWCloud190SP3/Permissions](https://docs.nomagic.com/display/TWCloud190SP3/Permissions)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Issue/Symptoms:</h3><p><br />Users are unable to save a Teamwork Cloud project locally, and see error messages similar to:</p><p><ac:image ac:height="162"><ri:attachment ri:filename="129793_autorization+error.png" /></ac:image> </p><p>Users also see similar entries observed in the modeling tool log file:</p><pre>com.nomagic.esi.api.messages.exceptions.NotAuthorizedException: Not authorized to process com.nomagic.esi.core.msg.GetCommitInfosMsg<br />at com.nomagic.esi.client.core.a.c.d.a(d.java:82)</pre><pre>	at com.nomagic.esi.client.core.a.c.d.a(d.java:122)
	at com.nomagic.esi.client.core.a.c.i.getCommitInfo(i.java:269)
	at com.nomagic.magicdraw.esi.session.impl.w.b(w.java:72)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.callOnline(OnlineExecutor.java:83)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.callOnline(OnlineExecutor.java:54)
	at com.nomagic.magicdraw.esi.session.OnlineExecutor.getOnline(OnlineExecutor.java:113)
	at com.nomagic.magicdraw.esi.session.impl.w.a(w.java:102)
	at com.nomagic.magicdraw.esi.session.impl.w.a(w.java:72)
	at com.nomagic.magicdraw.esi.session.f$c.a(f$c.java:1108)
	at com.nomagic.magicdraw.esi.persistence.c.c.a(c.java:115)
	at com.nomagic.magicdraw.esi.persistence.c.c.a(c.java:98)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:743)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:2470)
	at com.nomagic.magicdraw.esi.rellocate.b.f.b(f.java:518)
	at com.nomagic.magicdraw.esi.rellocate.b.f.c(f.java:424)
	at com.nomagic.magicdraw.persistence.ProjectLoadService.callWithoutAddToRecentFiles(ProjectLoadService.java:1333)
	at com.nomagic.magicdraw.esi.rellocate.b.f.a(f.java:424)
	at com.nomagic.magicdraw.esi.rellocate.b.f.access$100(f.java:195)
	at com.nomagic.magicdraw.esi.rellocate.b.f$i.execute(f$i.java:378)
	at com.nomagic.task.Task.construct(Task.java:192)
	at com.nomagic.task.SwingWorker$2.call(SwingWorker.java:209)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at com.nomagic.task.SwingWorker$SwingWorkerFuture.run(SwingWorker.java:596)
	at com.nomagic.task.BackportedThreadPoolExecutor$Worker.runTask(BackportedThreadPoolExecutor.java:1593)
	at com.nomagic.task.BackportedThreadPoolExecutor$Worker.run(BackportedThreadPoolExecutor.java:1624)
	at com.nomagic.task.PooledThread.run(PooledThread.java:64)</pre><h3>Solution:</h3><p>If a user does not have &quot;Read Resources&quot; permission for all used projects (directly and indirectly used), the user cannot save the project. This is a known issue, and is fixed in version 2021x.</p><p>To work around the issue (without upgrading your version), please check which permissions the user has. The user needs at least the &quot;Read Resources&quot; permission or &quot;Resource Reviewer&quot; role for all used projects (directly and indirectly used). Permissions and roles can be assigned to the user through the &quot;TWCloud Admin&quot; web application.</p><p>See the procedures on how to sign into that application at <a class="external-link" href="https://docs.nomagic.com/display/TWCloud190SP3/Sign+into+TWCloud+Admin" title="Follow link">https://docs.nomagic.com/display/TWCloud190SP3/Sign+into+TWCloud+Admin</a>.<br />This link outlines how to assign permission/role to a user: <a class="external-link" href="https://docs.nomagic.com/display/TWCloud190SP3/Permissions" title="Follow link">https://docs.nomagic.com/display/TWCloud190SP3/Permissions</a> </p>
````

<!--NOMAGIC_PAGE id=85764864 space=FAQ version=2 -->
## PAGE 00116: Vulnerabilities

- page_id: `85764864`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/85764864/Vulnerabilities
- version_number: 2
- version_date: `2021-12-14T12:38:21.996+01:00`
- ancestors: Frequently Asked Questions
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8d1dff3e-d020-48ed-ad3c-63aa737c1191" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=70405737 space=FAQ version=1 -->
## PAGE 00117: We have multiple floating license key files, can we combine them into a single key file ourselves?

- page_id: `70405737`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70405737/We+have+multiple+floating+license+key+files+can+we+combine+them+into+a+single+key+file+ourselves
- version_number: 1
- version_date: `2021-04-09T11:28:28.352+02:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

Unfortunately, this is not possible and should not be attempted. If you need to combine floating licenses into a single floating license key file - you should be engaging your account/sales executive.

They will be able to generate and provide you with a floating license key file containing all of your licenses in a single key file.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Unfortunately, this is not possible and should not be attempted. If you need to combine floating licenses into a single floating license key file - you should be engaging your account/sales executive. </p><p>They will be able to generate and provide you with a floating license key file containing all of your licenses in a single key file. </p>
````

<!--NOMAGIC_PAGE id=70395829 space=FAQ version=2 -->
## PAGE 00118: What are the common recommendations to increase performance

- page_id: `70395829`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395829/What+are+the+common+recommendations+to+increase+performance
- version_number: 2
- version_date: `2022-12-13T07:08:59.481+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: ['performance']

### NORMALIZED CONTENT

When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase the efficiency of modeling, we suggest the following solutions:

- Increase a java heap size.
- Do not keep unused diagrams open. Open the project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.
- Increase an active validation period. MagicDraw takes less memory with an increased active validations period.
- Split the project to read-only modules. Keep read-only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.
- Use Garbage Collector to free unused memory.
- Turn off the antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.

For more information, see "MagicDraw User Manual" > "Performance Improvement" section. Manual is available in < MagicDraw installation directory > \manual\

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When you work with very large models or use a lot of diagrams at a time, the performance of MagicDraw may become slow. To increase the efficiency of modeling, we suggest the following solutions:</p><ul><li>Increase a java heap size.</li><li>Do not keep unused diagrams open. Open the project without loading diagrams. Your projects will be opened over a shorter period of time without opening a diagram as well as use less memory.</li><li>Increase an active validation period. MagicDraw takes less memory with an increased active validations period.</li><li>Split the project to read-only modules. Keep read-only modules not loaded. This may help only if your project contains several parts with minimal dependencies between them.</li><li>Use Garbage Collector to free unused memory.</li><li>Turn off the antivirus. Some antivirus software can cause significant performance decrease on project open and other actions.</li></ul><p>For more information, see &quot;MagicDraw User Manual&quot; &gt; &quot;Performance Improvement&quot; section. Manual is available in &lt; MagicDraw installation directory &gt; \manual\</p>
````

<!--NOMAGIC_PAGE id=70395791 space=FAQ version=1 -->
## PAGE 00119: What command-line options are available with lmadmin?

- page_id: `70395791`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395791/What+command-line+options+are+available+with+lmadmin
- version_number: 1
- version_date: `2021-03-03T14:02:08.210+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

You can find list of the options by issuing the following command at the command prompt:

>lmadmin -help

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can find list of the options by issuing the following command at the command prompt:</p><p>&gt;lmadmin -help</p>
````

<!--NOMAGIC_PAGE id=70395745 space=FAQ version=1 -->
## PAGE 00120: What is the best way to reinstall my modeling tool on new computer or the same one after formatting.

- page_id: `70395745`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395745/What+is+the+best+way+to+reinstall+my+modeling+tool+on+new+computer+or+the+same+one+after+formatting.
- version_number: 1
- version_date: `2021-03-03T13:09:21.437+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

Reinstall product on new computer:

1. Deactivate the current license .
2. Download and install the fresh installation on new machine.
3. Start it after the installation is finished.
4. The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.
5. Uninstall the product from old machine.
6. You will be requested to activate the license and receive the commercial license dedicated for the particular machine.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>Reinstall product on new computer:</p><ol><li><a class="external-link" href="https://www.nomagic.com/support/activation.html#deactivation_in_aplication" rel="nofollow">Deactivate the current license</a>.</li><li>Download and install the fresh installation on new machine.</li><li>Start it after the installation is finished.</li><li>The Import Configuration dialog will appear upon opening installation for the first time. In the dialog, type the path to the installation folder of an older installation to import program configurations from it.</li><li>Uninstall the product from old machine.</li><li>You will be requested to activate the license and receive the commercial license dedicated for the particular machine.</li></ol>
````

<!--NOMAGIC_PAGE id=70395826 space=FAQ version=1 -->
## PAGE 00121: When I attempt to open certain file dialog boxes, it takes several minutes for the file dialog to open.

- page_id: `70395826`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395826/When+I+attempt+to+open+certain+file+dialog+boxes+it+takes+several+minutes+for+the+file+dialog+to+open.
- version_number: 1
- version_date: `2021-03-03T14:10:56.122+01:00`
- ancestors: Frequently Asked Questions > Performance
- labels: []

### NORMALIZED CONTENT

We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">We noticed such behavior under Windows NT when mapped network drives are present, but a portion of them are offline. Try disconnecting all offline drives.</span></p>
````

<!--NOMAGIC_PAGE id=70395739 space=FAQ version=1 -->
## PAGE 00122: When I run the exe file I get a warning: Please select another location to extract the installer to:

- page_id: `70395739`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395739/When+I+run+the+exe+file+I+get+a+warning+Please+select+another+location+to+extract+the+installer+to
- version_number: 1
- version_date: `2021-03-03T13:08:02.085+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

This error occurs when you have a corrupted installer file. Please download the file and install again.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><span style="color: rgb(85,85,85);">This error occurs when you have a corrupted installer file. Please download the file and install again.</span></p>
````

<!--NOMAGIC_PAGE id=70395732 space=FAQ version=2 -->
## PAGE 00123: When trying to install or import a plugin to MagicDraw, the error appears saying that you do not have rights to write to my modeling tool installation directory or "failed to copy resource directory". How can this be handled?

- page_id: `70395732`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395732/When+trying+to+install+or+import+a+plugin+to+MagicDraw+the+error+appears+saying+that+you+do+not+have+rights+to+write+to+my+modeling+tool+installation+directory+or+failed+to+copy+resource+directory+.+How+can+this+be+handled
- version_number: 2
- version_date: `2021-03-03T12:55:16.271+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.

To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following: 
1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**. 
2. From the **System Configuration** dialog, click the **Tools** tab. 
3. Select the **Change UAC Settings** tool and click **Launch** button. 
4. Move the slider to the highest value to set **Always notify** and click **OK**. 
5. Restart the computer to apply changes.

To enable UAC on Windows Vista OS, do the following: 
1. Click the **Start** button, type “msconfig” in the **Search** box and press **Enter**.

2. From the**System Configuration**dialog, click the **Tools** tab. 
3. Select the **Enable UAC** tool and click **Launch** button. The **CMD** window opens. 
4. When the command is completed, you can close **CMD** window. 
5. Restart the computer to apply changes.

To run MagicDraw as administrator, right-click the MagicDraw icon and choose **Run as Administrator**.

To run MagicDraw as an administrator all the time, do the following: 
1. Right-click the MagicDraw icon and choose **Properties**. 
2. Click the **Compatibility** tab. 
3. In the **Privilege Level** area, select **Run this program as an administrator**. 
4. Click **OK**.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>We recommend running MagicDraw as an administrator and with enabled UAC (User Account Control) on Windows Vista, Windows 7 and Windows 8 OS in order to avoid some problems that are related with permissions to modify files on the MagicDraw installation root directory.</p><p>To enable UAC on Windows 7, Windows 8, or Windows 10 OS, do the following:<br />1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.<br />2. From the <strong>System Configuration</strong> dialog, click the <strong>Tools</strong> tab.<br />3. Select the <strong>Change UAC Settings</strong> tool and click <strong>Launch</strong> button.<br />4. Move the slider to the highest value to set <strong>Always notify</strong> and click <strong>OK</strong>.<br />5. Restart the computer to apply changes.</p><p>To enable UAC on Windows Vista OS, do the following:<br />1. Click the <strong>Start</strong> button, type “msconfig” in the <strong>Search</strong> box and press <strong>Enter</strong>.</p><p><br />2. From the<strong> System Configuration </strong>dialog, click the <strong>Tools</strong> tab.<br />3. Select the <strong>Enable UAC</strong> tool and click <strong>Launch</strong> button. The <strong>CMD</strong> window opens.<br />4. When the command is completed, you can close <strong>CMD</strong> window.<br />5. Restart the computer to apply changes.</p><p>To run MagicDraw as administrator, right-click the MagicDraw icon and choose <strong>Run as Administrator</strong>.</p><p>To run MagicDraw as an administrator all the time, do the following:<br />1. Right-click the MagicDraw icon and choose <strong>Properties</strong>.<br />2. Click the <strong>Compatibility</strong> tab.<br />3. In the <strong>Privilege Level</strong> area, select <strong>Run this program as an administrator</strong>.<br />4. Click <strong>OK</strong>.</p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=70395750 space=FAQ version=1 -->
## PAGE 00124: When trying to launch my modeling tool on OS X Mountain Lion, the error appears: "MagicDraw.app" is damaged and can't be opened. You should move it to the Trash."

- page_id: `70395750`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395750/When+trying+to+launch+my+modeling+tool+on+OS+X+Mountain+Lion+the+error+appears+MagicDraw.app+is+damaged+and+can+t+be+opened.+You+should+move+it+to+the+Trash.
- version_number: 1
- version_date: `2021-03-03T13:18:45.343+01:00`
- ancestors: Frequently Asked Questions > Installation and Running
- labels: []

### NORMALIZED CONTENT

Please note that downloaded installs are not corrupted or damaged and this problem is not related to the modeling tool application. This issue is related to the new OS X Mountain Lion functionality, "Gatekeeper."

The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.

In order to launch their modelling tools, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: [http://support.apple.com/kb/HT5290](http://support.apple.com/kb/HT5290)

Note: We are communicating with Apple to solve this issue so that our customers may execute their modelling tools without any problems.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p>Please note that downloaded installs are not corrupted or damaged and this problem is not related to the modeling tool application. This issue is related to the new OS X Mountain Lion functionality, &quot;Gatekeeper.&quot;</p><p>The Gatekeeper functionality, by default, does not allow executing applications that are not from the Apple Store or from Identified Developers.</p><p>In order to launch their modelling tools, users can modify the option, which allows executing all the applications from all the providers. For more information on how to do this, go to: <a href="http://support.apple.com/kb/HT5290" class="external-link" rel="nofollow">http://support.apple.com/kb/HT5290</a></p><p>Note: We are communicating with Apple to solve this issue so that our customers may execute their modelling tools without any problems.</p>
````

<!--NOMAGIC_PAGE id=70395785 space=FAQ version=1 -->
## PAGE 00125: When we try to start the vendor daemon, we get the error: (cameo) tcp_s is bad!!! Exiting (cameo) EXITING DUE TO SIGNAL 28 Exit reason 5 How to start the license server?

- page_id: `70395785`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395785/When+we+try+to+start+the+vendor+daemon+we+get+the+error+cameo+tcp_s+is+bad+Exiting+cameo+EXITING+DUE+TO+SIGNAL+28+Exit+reason+5+How+to+start+the+license+server
- version_number: 1
- version_date: `2021-03-03T14:01:08.149+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: []

### NORMALIZED CONTENT

Such an error appears when:

The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.

Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.

You may check and change the port number in the FLEXnet license administrator console.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Such an error appears when:</p><p>The vendor daemon is specified to run on the particular port number that is already used by the other process. The default port numbers for the cameo vendor daemon is 1101.</p><p>Both the FLEXnet license server and the cameo vendor are specified to run on the same port number. Default port numbers for the FLEXnet license server are 27000-27009.</p><p>You may check and change the port number in the FLEXnet license administrator console.</p>
````

<!--NOMAGIC_PAGE id=70395836 space=FAQ version=3 -->
## PAGE 00126: Where can I find an offline documentation about working with your modeling tools, modeling tool integrations and floating license server?

- page_id: `70395836`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395836/Where+can+I+find+an+offline+documentation+about+working+with+your+modeling+tools+modeling+tool+integrations+and+floating+license+server
- version_number: 3
- version_date: `2021-04-09T07:03:21.701+02:00`
- ancestors: Frequently Asked Questions > Documentation / Help
- labels: []

### NORMALIZED CONTENT

All modeling tool documentation is located in the <modeling tool installation directory>/manual folder.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(85,85,85);">All modeling tool documentation is located in the &lt;modeling tool installation directory&gt;/manual folder.</span></p>
````

<!--NOMAGIC_PAGE id=70395769 space=FAQ version=1 -->
## PAGE 00127: Where can I find lmgrid or lmadmin log file?

- page_id: `70395769`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395769/Where+can+I+find+lmgrid+or+lmadmin+log+file
- version_number: 1
- version_date: `2021-03-03T13:57:58.890+01:00`
- ancestors: Frequently Asked Questions > FlexNet License Server and Floating License
- labels: ['lmadmin_log']

### NORMALIZED CONTENT

The location of the log file depends on what license server manager you use.

- If it is lmgrid , the cameo.log and lmgrid.log files can both be found directly in the root package of the lmgrid installation.
- If it is lmadmin , the cameo.log file can be found in <lmadmin installation directory>\logs , for example, C:\Program Files\FlexNet Publisher License Server Manager\logs .

**Note:** The default location of the log file can be changed during the product configuration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The location of the log file depends on what license server manager you use.</p><ul><li>If it is <em>lmgrid</em>, the <em>cameo.log</em> and<em> lmgrid.log</em> files can both be found directly in the root package of the lmgrid installation.</li><li>If it is <em>lmadmin</em>, the <em>cameo.log</em> file can be found in <em>&lt;lmadmin installation directory&gt;\logs</em>, for example, <em>C:\Program Files\FlexNet Publisher License Server Manager\logs</em>.</li></ul><p><strong>Note:</strong> The default location of the log file can be changed during the product configuration.</p>
````

<!--NOMAGIC_PAGE id=70395805 space=FAQ version=29 -->
## PAGE 00128: Where can I find log files of a modeling tool, Cameo Collaborator, and Teamwork Cloud

- page_id: `70395805`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/70395805/Where+can+I+find+log+files+of+a+modeling+tool+Cameo+Collaborator+and+Teamwork+Cloud
- version_number: 29
- version_date: `2024-09-03T08:45:44.414+02:00`
- ancestors: Frequently Asked Questions > Performance
- labels: ['log-files']

### NORMALIZED CONTENT

741469365

INLINE

741469376

INLINE

741469364

INLINE

**On this page**

**Scripts**

The following is the script package used in this page:

- [ATTACHMENT filename='TWC-Log-Script-Pkg.zip']

741469375

INLINE

When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.

##### Using the log file script package

The [ATTACHMENT filename='TWC-Log-Script-Pkg.zip'] contains utilities for gathering and managing log files on your Teamwork Cloud server. These scripts are designed to run from a Linux or Windows Cygwin command line.

- Create log file package Use the getlogfiles.sh script to create a package of all log files associated with Teamwork Cloud operations. This script will create a TAR archive file containing all the latest logs, as well as some system information. The TAR package can be sent along with your support request to help analyze Teamwork Cloud-related issues.
- Reset log files Sometimes you may need to create a fresh set of log files. Use the clearlogfiles.sh script to reset the log files associated with Teamwork Cloud operations. Please make sure all Teamwork Cloud services are stopped before running the script. This script will then rename all the current log files so that new log files can be generated when the Teamwork Cloud services are restarted. Resetting the log files will ensure that the logs will only contain the latest startup information.

##### **Accessing log files**

###### Installation paths

| PACKAGE | OS | VERSION | INSTALL_ROOT |
| --- | --- | --- | --- |
| Teamwork Cloud | Linux | 22xR2, 24x | <install_root> /CATIANoMagicServices |
| 22xR1 and older | <install_root> /TeamworkCloudSuite |  |  |
| Windows | 22xR2, 24x | <install_root>\CATIANoMagicServices |  |
| 22xR1 and older | <install_root>\ TeamworkCloudSuite |  |  |
| Magic Collaboration Studio | Linux | All | <install_root>/MagicCollaborationStudio |
| Windows | All | <install_root>\MagicCollaborationStudio |  |

- For a modeling tool:

Open your modeling tool and in the main menu go to **Help** > **About <modeling tool name>**. In the **Environment** tab, click the link provided in the **Log File** line to open a log file.

Or

Go to the *<user.home>\<.modeling tool name>\<modeling tool version>* directory**and obtain *<modeling tool name>.log* file.

Default path for Windows*: C:\Users\<USERNAME>\AppData\Local\.<modeling tool name>\<modeling tool version number>* 
Default path for other operating systems: *<user.home>/.<modeling tool name>/< modeling tool version number>*

- For Web Application Platform/Cameo Collaborator for Teamwork Cloud:

Log files (e.g., *webapp.log*, *collaborator.log*, etc.) 
Linux: *<install_root>* */WebAppPlatform/logs/webappplatform* Windows: *<install_root>* *\WebAppPlatform\logs\webappplatform*

Configuration 
Linux: *<install_root>/WebAppPlatform/shared/conf/webappplatform.properties* 
Windows: *<install_root>\WebAppPlatform\shared\conf\webappplatform.properties*

###### Teamwork Cloud/Magic Collaboration Studio

Log file for 2024x and later 
Linux *: <install_root>/TeamworkCloud/logs/server.log* **Windows: *<install_root>\TeamworkCloud\logs\* *server.log*

Configuration 
Linux: *<install_root>/TeamworkCloud/configuration/application.conf* 
Windows: *<install_root>\TeamworkCloud\configuration\application.conf*

Log file for earlier versions 
Linux:*/home/twcloud/.twcloud/<version>/server.log* 
Windows: *C:\Users\<user>\.twcloud\<version>\server.log*

- For Authentication server:

Log file for 2022x and later 
Linux: *<install_root>* */WebAppPlatform/logs/webappplatform/authentication.log* 
Windows: *<install_root>\* *WebAppPlatform\logs\webappplatform\authentication.log*

Configuration for 2022x and newer 
Linux: *<install_root>/WebAppPlatform\shared\conf\authserver.properties* 
Windows: *<install_root>\WebAppPlatform\shared\conf\authserver.properties*

Log file for earlier versions 
Linux: */home/twcloud/.authserver/<version>/authserver.log* 
Windows: *C:\Users\<user>\.authserver\<version>\authserver.log*

Configuration for earlier versions 
Linux: *<install_root>* */AuthServer/config/authserver.properties* 
Windows: *<install_root>\* *AuthServer\config\authserver.properties*

- For Cassandra:

Log file 
Linux: */var/log/cassandra/system.log*

Configuration filesLinux:*/etc/cassandra/conf*

- Properties files for Teamwork Cloud:

Default for Linux: 
*/opt/local/TeamworkCloud/configuration/application.conf* */opt/local/TeamworkCloud/Authserver/config/authserver.properties* */opt/local/TeamworkCloud/WebAppPlatform/shared/conf/webappplatform.properties*

Default for Windows: 
*C:\Program Files\TeamworkCloud\configuration\application.conf* *C:\Program Files\TeamworkCloud\Authserver\config\authserver.properties* *C:\Program Files\TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties*

##### **Generating a log file**

If the performance of your modeling tool declines or it freezes, go to *<modeling tool installation directory>\bin,*and run the *submit_issue.exe* or *submit_issue.sh* file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file as described above.

##### **Java crash log files**

If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the *<modeling tool installation directory>/bin* or *<modeling tool installation directory>*directory. The names of these log files start with "hs_err", e.g., *hs_err_pid15693.log*. If you find the Java crash log file, it indicates that Java was the reason of your modeling tool crash.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="381c4090-5045-4e7c-928f-e107f7242b83"><ac:parameter ac:name="id">741469365</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4d1a4155-191a-4b68-bc24-7c0bd07a9101"><ac:parameter ac:name="id">741469376</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a29609b0-0033-4fc9-bd2e-21d4310bfc3f"><ac:parameter ac:name="id">741469364</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ea98aac3-c549-4f9d-a358-e0e474e6bdf9" /></p></ac:layout-cell><ac:layout-cell><p><strong>Scripts</strong></p><p><span style="color: rgb(62,63,64);">The following is the script package used in this page:</span></p><ul><li><ac:link><ri:attachment ri:filename="TWC-Log-Script-Pkg.zip" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="33bf14da-3816-4451-9576-56b4ff0907f2"><ac:parameter ac:name="id">741469375</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>When you report an issue with your modeling tool, Cameo Collaborator or Teamwork Cloud, always include related log files. Log files provide useful information that we need to investigate and troubleshoot your problem.</p><h3>Using the log file script package</h3><p>The <ac:link><ri:attachment ri:filename="TWC-Log-Script-Pkg.zip" /><ac:plain-text-link-body><![CDATA[script package]]></ac:plain-text-link-body></ac:link> contains utilities for gathering and managing log files on your Teamwork Cloud server. These scripts are designed to run from a Linux or Windows Cygwin command line.</p><ul><li><strong>Create log file package</strong> <br />Use the <em>getlogfiles.sh</em> script to create a package of all log files associated with Teamwork Cloud operations. This script will create a TAR archive file containing all the latest logs, as well as some system information. The TAR package can be sent along with your support request to help analyze Teamwork Cloud-related issues.</li><li><strong>Reset log files</strong> <br />Sometimes you may need to create a fresh set of log files. Use the <em>clearlogfiles.sh</em> script to reset the log files associated with Teamwork Cloud operations. Please make sure all Teamwork Cloud services are stopped before running the script. This script will then rename all the current log files so that new log files can be generated when the Teamwork Cloud services are restarted. Resetting the log files will ensure that the logs will only contain the latest startup information.</li></ul><h3><strong>Accessing log files</strong></h3><h4 class="auto-cursor-target">Installation paths</h4><table class="wrapped"><tbody><tr><th>PACKAGE</th><th>OS</th><th>VERSION</th><th>INSTALL_ROOT</th></tr><tr><td rowspan="4">Teamwork <br />Cloud</td><td rowspan="2">Linux</td><td>22xR2, 24x</td><td><em>&lt;install_root&gt;</em> <em>/CATIANoMagicServices</em></td></tr><tr><td>22xR1 and older</td><td><em>&lt;install_root&gt;</em> <em>/<ac:inline-comment-marker ac:ref="a857094d-e861-44c4-b6cf-7b08f23fe673">TeamworkCloudSuite</ac:inline-comment-marker> </em></td></tr><tr><td rowspan="2">Windows</td><td>22xR2, 24x</td><td><em>&lt;install_root&gt;\CATIANoMagicServices</em></td></tr><tr><td>22xR1 and older</td><td><em>&lt;install_root&gt;\</em> <em>TeamworkCloudSuite</em></td></tr><tr><td rowspan="2">Magic <br />Collaboration <br />Studio</td><td>Linux</td><td>All</td><td><em>&lt;install_root&gt;/MagicCollaborationStudio</em></td></tr><tr><td>Windows</td><td>All</td><td><em>&lt;install_root&gt;\MagicCollaborationStudio</em></td></tr></tbody></table><ul><li><strong>For a modeling tool:</strong></li></ul><p>Open your modeling tool and in the main menu go to <strong>Help</strong> &gt; <strong>About &lt;modeling tool name&gt;</strong>. In the <strong>Environment</strong> tab, click the link provided in the <strong>Log File</strong> line to open a log file.</p><p>Or </p><p>Go to the <em>&lt;user.home&gt;\&lt;.modeling tool name&gt;\&lt;modeling tool version&gt;</em> directory<em> </em>and obtain <em>&lt;modeling tool name&gt;.log</em> file.</p><p>Default path for Windows<em>: C:\Users\&lt;USERNAME&gt;\AppData\Local\.&lt;modeling tool name&gt;\&lt;modeling tool version number&gt;</em> <br />Default path for other operating systems: <em>&lt;user.home&gt;/.&lt;modeling tool name&gt;/&lt; modeling tool version number&gt;</em></p><ul><li><strong>For Web Application Platform/Cameo Collaborator for Teamwork Cloud:</strong></li></ul><p>Log files (e.g., <em>webapp.log</em>, <em>collaborator.log</em>, etc.)<br /><span>Linux: </span> <em>&lt;<ac:inline-comment-marker ac:ref="a526b538-fcc3-4e05-96a3-fe5d2c1a1f7f">install_root</ac:inline-comment-marker>&gt;</em> <em>/WebAppPlatform/logs/webappplatform<br /></em> <span>Windows: </span> <em>&lt;install_root&gt;</em> <em>\WebAppPlatform\logs\webappplatform</em></p><p>Configuration<br />Linux: <em>&lt;install_root&gt;/WebAppPlatform/shared/conf/webappplatform.properties</em> <br />Windows: <em>&lt;install_root&gt;\WebAppPlatform\shared\conf\webappplatform.properties</em></p><h4>Teamwork Cloud/Magic Collaboration Studio</h4><p>Log file for 2024x and later<br /><span>Linux</span> <em> <span>: &lt;install_root&gt;/TeamworkCloud/logs/server.log</span> </em> <em> <br /></em>Windows: <em> <span>&lt;install_root&gt;\TeamworkCloud\logs\</span> </em> <em>server.log</em></p><p>Configuration<br />Linux: <em>&lt;install_root&gt;/TeamworkCloud/configuration/application.conf</em> <br />Windows: <em>&lt;install_root&gt;\TeamworkCloud\configuration\application.conf</em></p><p>Log file for earlier versions<br />Linux:<em> /home/twcloud/.twcloud/&lt;version&gt;/server.log</em> <br />Windows: <em>C:\Users\&lt;user&gt;\.twcloud\&lt;version&gt;\server.log</em></p><ul><li><strong>For Authentication server:</strong></li></ul><p>Log file for 2022x and later<br />Linux: <em>&lt;install_root&gt;</em> <em> <span style="color: rgb(23,43,77);">/WebAppPlatform/logs/webappplatform/authentication.log</span> </em> <br />Windows: <em>&lt;install_root&gt;\</em> <em> <span style="color: rgb(23,43,77);">WebAppPlatform\logs\webappplatform\authentication.log</span> </em></p><p>Configuration for 2022x and newer<br />Linux: <em>&lt;install_root&gt;/WebAppPlatform\shared\conf\authserver.properties</em> <br />Windows: <em>&lt;install_root&gt;\WebAppPlatform\shared\conf\authserver.properties</em></p><p>Log file for earlier versions<br />Linux: <em>/home/twcloud/.authserver/&lt;version&gt;/authserver.log</em> <br />Windows: <em>C:\Users\&lt;user&gt;\.authserver\&lt;version&gt;\authserver.log</em></p><p>Configuration for earlier versions<br />Linux: <em>&lt;install_root&gt;</em> <em> <span style="color: rgb(23,43,77);">/AuthServer/config/authserver.properties</span> </em> <br />Windows: <em>&lt;install_root&gt;\</em> <em> <span style="color: rgb(23,43,77);">AuthServer\config\authserver.properties</span> </em></p><ul><li><strong>For Cassandra:</strong></li></ul><p>Log file<br />Linux: <em>/var/log/cassandra/system.log</em></p><p><span>Configuration files <br /></span>Linux:<em> /etc/cassandra/conf</em></p><ul><li><strong>Properties files for Teamwork Cloud:</strong></li></ul><p>Default for Linux:<br /><em>/opt/local/TeamworkCloud/configuration/application.conf<br /></em> <em>/opt/local/TeamworkCloud/Authserver/config/authserver.properties<br /></em> <em>/opt/local/TeamworkCloud/WebAppPlatform/shared/conf/webappplatform.properties</em></p><p>Default for Windows:<br /><em>C:\Program Files\TeamworkCloud\configuration\application.conf<br /></em> <em>C:\Program Files\TeamworkCloud\Authserver\config\authserver.properties<br /></em> <em>C:\Program Files\TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties</em></p><h3><strong>Generating a log file</strong></h3><p>If the performance of your modeling tool declines or it freezes, go to <em>&lt;modeling tool installation directory&gt;\bin, </em>and run the <em>submit_issue.exe</em> or <em>submit_issue.sh</em> file several times. It dumps threads into the log file of your modeling tool. Then you can access the log file as described above.</p><h3><strong>Java crash log files</strong></h3><p>If your modeling tool crashes (disappears), try searching for Java crash log files. They are stored in the running location of the modeling tool, e.g., the <em>&lt;modeling tool installation directory&gt;/bin</em> or <em>&lt;modeling tool installation directory&gt; </em>directory. The names of these log files start with &quot;hs_err&quot;, e.g., <em>hs_err_pid15693.log</em>. If you find the Java crash log file, it indicates that Java was the reason of your modeling tool crash.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=111223996 space=FAQ version=3 -->
## PAGE 00129: Where to find Cameo Collaborator log files

- page_id: `111223996`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/111223996/Where+to+find+Cameo+Collaborator+log+files
- version_number: 3
- version_date: `2023-01-25T12:30:26.386+01:00`
- ancestors: Frequently Asked Questions > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Go to the *<WebAppPlatform_installation_directory>/logs/webappplatform* directory and obtain the *web-app.log* and/or *collaborator.log* files.

#### TIP: Default path to log files

Default path to log files

The default paths to Cameo Collaborator log files are:

- For Linux: /opt/local/TeamworkCloud/WebAppPlatform/logs/webappplatform
- For Windows: C:\Program Files\TeamworkCloud\WebAppPlatform\logs\webappplatform

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Go to the <em>&lt;WebAppPlatform_installation_directory&gt;/logs/webappplatform</em> directory and obtain the <em>web-app.log</em> and/or <em>collaborator.log</em> files.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="786bb646-5e76-4db4-abc5-e39e66b0216b"><ac:parameter ac:name="title">Default path to log files</ac:parameter><ac:rich-text-body><p>The default paths to Cameo Collaborator log files are:</p><ul><li><span style="letter-spacing: 0.0px;">For Linux: /opt/local/TeamworkCloud/WebAppPlatform/logs/webappplatform</span></li><li><span style="letter-spacing: 0.0px;">For Windows: C:\Program Files\TeamworkCloud\WebAppPlatform\logs\webappplatform</span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136708432 space=FAQ version=4 -->
## PAGE 00130: Zip exceptions thrown after Java version upgrade to 11.0.20+ or 17.0.8+

- page_id: `136708432`
- space_key: `FAQ`
- source_url: https://docs.nomagic.com/spaces/FAQ/pages/136708432/Zip+exceptions+thrown+after+Java+version+upgrade+to+11.0.20+or+17.0.8
- version_number: 4
- version_date: `2023-09-18T08:33:59.423+02:00`
- ancestors: Frequently Asked Questions > Java Virtual Machine (JVM)
- labels: []

### NORMALIZED CONTENT

Java 11.0.20+ or 17.0.8+ (or newer) has Improved ZIP64 Extra Field Validation, involving additional checks for *.zip* files. Any necessary adjustments to avoid any issues have been implemented; however, you may encounter exceptions when working with custom plugins or command launchers dealing with *.zip* files.

- If you encounter the following exception (or similar):

*java.util.zip.ZipException: Invalid CEN header*

- Add the following property to your Java arguments:

*-Djdk.util.zip.disableZip64ExtraFieldValidation=true*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Java 11.0.20+ or 17.0.8+ (or newer) has Improved ZIP64 Extra Field Validation, involving additional checks for <em>.zip</em> files. Any necessary adjustments to avoid any issues have been implemented; however, you may encounter exceptions when working with custom plugins or command launchers dealing with <em>.zip</em> files.</p><ul><li>If you encounter the following exception (or similar):</li></ul><p><em>java.util.zip.ZipException: Invalid CEN header</em></p><ul><li>Add the following property to your Java arguments:</li></ul><p><em>-Djdk.util.zip.disableZip64ExtraFieldValidation=true</em></p><p><br /></p>
````
