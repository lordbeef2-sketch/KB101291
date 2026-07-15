# AUTHORITATIVE PDF EXTRACTION: README.pdf

- source_repository: https://github.com/Systems-Modeling/SysML-v2-Release
- source_commit: `288d129c0d532065d45434bbb48a920898b719af`
- source_path: `install/eclipse/README.pdf`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Release/blob/288d129c0d532065d45434bbb48a920898b719af/install/eclipse/README.pdf
- source_bytes: 94589
- source_sha256: `861375e448cb7db16b3d583c458825d7c968ac3c654bb15bd82870531786c0ab`
- pdf_pages: 3
- extracted_utc: `2026-07-14T16:48:16.202611+00:00`
- pdf_metadata: `{'/Title': 'SysML v2 Release Eclipse Installation', '/Creator': '', '/Producer': 'Asciidoctor PDF 2.3.19, based on Prawn 2.4.0', '/ModDate': "D:20260219220149+01'00'", '/CreationDate': "D:20260703003204+02'00'"}`

## SEMANTIC PAGE-BY-PAGE EXTRACTION

### PDF PAGE 1

Open an Eclipse workspace.



                  Select



                  Select



                  Navigate to the


                  wish.) Click



                  In the Install window, select the



                  Continue with the installation (select


                  Eclipse.




                 SysML v2 Release Eclipse
                                     Installation
                                            dot -c
Requirements: Eclipse 2025-12 (4.38), with Java Development Kit
                  Make sure that your Eclipse has PlantUML with SysMLv2 extensions. You can install it from the
(Note: The release may work on later versions of Eclipse, but it has only been tested on 2025-12.)
                  update site of
Installing the pluginsInstall New Software

1.
2.        Help > Install New SoftwarePlantUML visualization requires that .

3.        Add… and then, in the add dialog, select download/Archive… .

4.                    org.omg.sysml.site.zip archive and select it. (You can give it a name if you
                 Add.     The recommended GraphViz version is 2.44.1. Make sure you have initialized GraphViz with

5.                                     KerML and SysML Editors category and click Next.

6.                                           Install Anyway if asked), and, when it is complete, restart



                  If Eclipse cannot automatically find the path to the GraphViz executable, you can set it by going
Installing PlantUML graphical visualization
                  to
Graphical visualization is available in Eclipse using the open source PlantUML tooling to render
diagrams.

1.
                    https://github.com/himi/p2-update-puml-sysmlv2/raw/main/updates with Help >


2.                                             GraphViz be installed. Visit https://www.graphviz.org/
                and download the appropriate package for your environment.

     ◦
               command. See https://plantuml.com/ja/graphviz-dot for details.

3.
      Preferences > PlantUML. For details, visit https://plantuml.com/en/eclipse.

Installing the model library and modeling
projects

If you are updating an existing installation of an earlier SysML v2 release, then, before proceeding
with the procedure below, delete the kerml, sysml and sysml.library projects from your workspace,
selecting Delete project contents from disk.





                                                                                                            1

### PDF PAGE 2

sysml.library










































                    Select



                    Under



                    Browse to the



                    Under


                    click



                    Turn off






                    Repeat the above steps for the
































                    Double click on a file with a


                    (KerML) or Systems Modeling Language (SysML).



                    Create new KerML files in the



                    Create new SysML files in the



 1.        File > ImportYou can view the model library files in the .

 2.         General, choose Existing Projects into Workspace.

 3.                 To show SysML diagrams, in sysml.library directory and select it.

 4.         Projects, select sysml.library, under Options select Copy projects into workspace, then
          Finish. (If Eclipse asks whether to "overwrite settings", select diagram rendered in the view is relative to the text selected in the active SysML editor view.No.)

 5.             Project > Build AutomaticallyTree (BDD-like), interconnection (IBD-like) and state machine views are currently supported., then select Project > Clean… and build only
                    .

 6.                                     kerml and sysml projects.

Important Note: Import the kerml and sysml projects only after importing and building the
sysml.library project.

After installation is complete, if you wish to turn Build Automatically back on, first go to
Preferences > General > Workspace > Build and make sure that sysml.library is before kerml and
sysml in the build order.

Working with model files

 1.                                   .kerml or .sysml extension to view it in a Kernel Modeling Language


 2.                                     kerml/src directory with the extension .kerml.

 3.                                    sysml/src directory with the extension .sysml.

 4.                                                    sysml.library project, but do not change them.

 5.                 Select               Window > Show View > Other… select the PlantUML view. The




Release Note: While performance has improved further in this release, there are still cases inSelect

which the processing of a file with several name resolution errors can take a long time, particularly
if the Quantities and UnitsEnter the project name (and location if necessary), then press Next. library is being used.

Initializing new model projectsOn the Project References page, check the

You can also create a separate project for your KerML or SysML files.other projects should be visible for resolving cross-references.

 1.        File > New > Project... to open the New Project wizard.

 2.        General/ProjectRight-click the new project and select .

 3.
 4.                 the indexing infrastructure necessary for resolving references between different files.sysml.library project. This step tells Eclipse which



 5.                                               Configure > Convert to an Xtext project. This step sets up






2

### PDF PAGE 3

Create any text files with










































































6.                                .kerml or .sysml extensions to start working with a new file.

                Adding the project references to an existing project can be done in the project
               Properties dialog available from the popup menu on the project in the Project
                References page.


                If the Xtext setup (step 5) is missed, opening the KerML or SysML editor shows a
               dialog asking to convert the project to an Xtext project. Accepting this has the same
                results as manually selecting the menu item on the project.







































































                                                                                                                      3

## LAYOUT-PRESERVING POPPLER EXTRACTION

### LAYOUT PDF PAGE 1

```text
        SysML v2 Release Eclipse
                   Installation

Requirements: Eclipse 2025-12 (4.38), with Java Development Kit

(Note: The release may work on later versions of Eclipse, but it has only been tested on 2025-12.)

Installing the plugins

 1. Open an Eclipse workspace.
 2. Select Help > Install New Software.
 3. Select Add… and then, in the add dialog, select Archive… .
 4. Navigate to the org.omg.sysml.site.zip archive and select it. (You can give it a name if you

     wish.) Click Add.
 5. In the Install window, select the KerML and SysML Editors category and click Next.
 6. Continue with the installation (select Install Anyway if asked), and, when it is complete, restart

     Eclipse.

Installing PlantUML graphical visualization

Graphical visualization is available in Eclipse using the open source PlantUML tooling to render
diagrams.

 1. Make sure that your Eclipse has PlantUML with SysMLv2 extensions. You can install it from the
     update site of https://github.com/himi/p2-update-puml-sysmlv2/raw/main/updates with Help >
     Install New Software

 2. PlantUML visualization requires that GraphViz be installed. Visit https://www.graphviz.org/
     download/ and download the appropriate package for your environment.
       ◦ The recommended GraphViz version is 2.44.1. Make sure you have initialized GraphViz with
          dot -c command. See https://plantuml.com/ja/graphviz-dot for details.

 3. If Eclipse cannot automatically find the path to the GraphViz executable, you can set it by going
     to Preferences > PlantUML. For details, visit https://plantuml.com/en/eclipse.

Installing the model library and modeling
projects

If you are updating an existing installation of an earlier SysML v2 release, then, before proceeding
with the procedure below, delete the kerml, sysml and sysml.library projects from your workspace,
selecting Delete project contents from disk.

                                                                                                                                                                     1
```

### LAYOUT PDF PAGE 2

```text
 1. Select File > Import.
 2. Under General, choose Existing Projects into Workspace.
 3. Browse to the sysml.library directory and select it.
 4. Under Projects, select sysml.library, under Options select Copy projects into workspace, then

     click Finish. (If Eclipse asks whether to "overwrite settings", select No.)
 5. Turn off Project > Build Automatically, then select Project > Clean… and build only

     sysml.library.
 6. Repeat the above steps for the kerml and sysml projects.

Important Note: Import the kerml and sysml projects only after importing and building the
sysml.library project.

After installation is complete, if you wish to turn Build Automatically back on, first go to
Preferences > General > Workspace > Build and make sure that sysml.library is before kerml and
sysml in the build order.

Working with model files

 1. Double click on a file with a .kerml or .sysml extension to view it in a Kernel Modeling Language
     (KerML) or Systems Modeling Language (SysML).

 2. Create new KerML files in the kerml/src directory with the extension .kerml.
 3. Create new SysML files in the sysml/src directory with the extension .sysml.
 4. You can view the model library files in the sysml.library project, but do not change them.
 5. To show SysML diagrams, in Window > Show View > Other… select the PlantUML view. The

     diagram rendered in the view is relative to the text selected in the active SysML editor view.
     Tree (BDD-like), interconnection (IBD-like) and state machine views are currently supported.

Release Note: While performance has improved further in this release, there are still cases in
which the processing of a file with several name resolution errors can take a long time, particularly
if the Quantities and Units library is being used.

Initializing new model projects

You can also create a separate project for your KerML or SysML files.

 1. Select File > New > Project... to open the New Project wizard.
 2. Select General/Project.
 3. Enter the project name (and location if necessary), then press Next.
 4. On the Project References page, check the sysml.library project. This step tells Eclipse which

     other projects should be visible for resolving cross-references.
 5. Right-click the new project and select Configure > Convert to an Xtext project. This step sets up

     the indexing infrastructure necessary for resolving references between different files.

2
```

### LAYOUT PDF PAGE 3

```text
6. Create any text files with .kerml or .sysml extensions to start working with a new file.

  Adding the project references to an existing project can be done in the project
   Properties dialog available from the popup menu on the project in the Project
   References page.

  If the Xtext setup (step 5) is missed, opening the KerML or SysML editor shows a
   dialog asking to convert the project to an Xtext project. Accepting this has the same
   results as manually selecting the menu item on the project.

                                                                                             3
```
