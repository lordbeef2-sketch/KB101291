# NOMAGIC DOCUMENTATION SPACE: Developer Guides 2024x Refresh3

<!--NOMAGIC_SPACE key=DEVG2024xR3 chunk=2 -->

<!--NOMAGIC_PAGE id=225347232 space=DEVG2024xR3 version=1 -->
## PAGE 00223: Used project management

- page_id: `225347232`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347232/Used+project+management
- version_number: 1
- version_date: `2024-02-13T09:43:13.025+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with project > Projects management
- labels: []

### NORMALIZED CONTENT

*com.nomagic.magicdraw.core.project.ProjectsManager* provides the used project management (project usage, export, import, reload, and package sharing) methods.

Example #1. Exporting a used local project

The collection of project packages can be exported as a used project.

```java

```

###### Example #2. Exporting a used server project

The *com.nomagic.magicdraw.teamwork.application.TeamworkUtils*class is used to export a used server project.

```java

```

###### Example #3. Using a project

The local and server project usage is similar - an appropriate project descriptor must be used, but module directories project option should be updated before using local project:

```java
directories = projectOptions.getModulesDirectories(true);
    if (!directories.contains(moduleDir))
    {
        projectOptions.addModuleDirectory(moduleDir);
    }
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.createProjectDescriptor(file.toURI());
    // Use a project
    projectsManager.useModule(project, projectDescriptor);]]>
```

###### Example #4. Importing a used project

The local and server project import does not differ. Just an appropriate project descriptor must be used:

```java

```

###### Example #5. Reloading a used project

The local and server project reload does not differ. Just an appropriate project descriptor must be used:

```java

```

###### Example #6. The package sharing

```java

```

###### Example #7. Editing a used project within the project

```java
moduleUsages = Collections.singleton(moduleUsage);
 
        final boolean readOnly = attachedProject.isReadOnly();
        if (readOnly)
        {
            // Make the used project editable (the read-write accessibility mode) 
            ModulesService.setReadOnlyOnTask(moduleUsages, false);
        }
        // Get the first shared package of the used project 
        final Collection sharedPackages = ProjectUtilities.getSharedPackages(attachedProject);
        final Package aPackage = sharedPackages.iterator().next();
        // Create a class in the used project
        SessionManager.getInstance().createSession("Create use case in used project");
        final Class aCase = project.getElementsFactory().createClassInstance();
        aCase.setOwner(aPackage);
        aCase.setName("myClass");
        SessionManager.getInstance().closeSession();
        // save the used project
        Application.getInstance().getProjectsManager().saveModule(project, attachedProject, true, false);
        if (readOnly)
        {
             // Make a used project not editable (the read-only accessibility mode) 
             ModulesService.setReadOnlyOnTask(moduleUsages, true);
        }
    }]]>
```

**Advanced management**

Use the *com.nomagic.magicdraw.core.ProjectUtilities* utility class for retrieving more project decomposition related information.

Use the *com.nomagic.magicdraw.core.modules.ModulesService* or***ProjectsManager* classes for managing attached projects.

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Project descriptor' space='DEVG2024xR3']
- [CONFLUENCE_PAGE title='Project structure decomposition' space='DEVG2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="WordSection1"><p><em>com.nomagic.magicdraw.core.project.ProjectsManager</em> provides the used project management (project usage, export, import, reload, and package sharing) methods. </p><p><span style="color: rgb(0,0,0);font-weight: bold;line-height: 1.4285715;">Example #1. Exporting a used local project</span></p><p>The collection of project packages can be exported as a used project.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="913962ec-aad1-48bb-8902-a81e7ae50e3a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    ProjectsManager projectsManager = Application.getInstance().getProjectsManager(); 
    File file = new File(moduleFilePath);
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.createProjectDescriptor(file.toURI());
    // Export a collection of packages as a used project 
    projectsManager.exportModule(project, packages, "My used local project", projectDescriptor);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div><div class="WordSection2"><h4>Example #2. Exporting a used server project</h4><p>The <em>com.nomagic.magicdraw.teamwork.application.TeamworkUtils </em>class is used to export a used server project.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8337accb-146f-422a-b9e7-a276c3514fde"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    TeamworkUtils.exportTeamworkModule(project, packages, "My used remote project", remoteProjectQualifiedName);]]></ac:plain-text-body></ac:structured-macro><br /><h4>Example #3. Using a project</h4><p>The local and server project usage is similar - an appropriate project descriptor must be used, but module directories project option should be updated before using local project:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8f167a1d-1b61-492d-af07-7fecf7ab221a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[	ProjectsManager projectsManager = Application.getInstance().getProjectsManager(); 
    File file = new File(moduleFilePath);
    // update project options only when using local project
    String moduleDir = file.getParent();
    ProjectOptions projectOptions = project.getOptions();
    List<String> directories = projectOptions.getModulesDirectories(true);
    if (!directories.contains(moduleDir))
    {
        projectOptions.addModuleDirectory(moduleDir);
    }
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.createProjectDescriptor(file.toURI());
    // Use a project
    projectsManager.useModule(project, projectDescriptor);]]></ac:plain-text-body></ac:structured-macro><br /><h4>Example #4. Importing a used project</h4><p>The local and server project import does not differ. Just an appropriate project descriptor must be used:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dfc417a8-1948-41b1-a941-072fa2cf2855"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[	ProjectsManager projectsManager = Application.getInstance().getProjectsManager(); 
    File file = new File(moduleFilePath);
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.createProjectDescriptor(file.toURI()); 
    projectsManager.importModule(project, projectDescriptor);]]></ac:plain-text-body></ac:structured-macro><br /><h4>Example #5. Reloading a used project</h4><p>The local and server project reload does not differ. Just an appropriate project descriptor must be used:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="34b7bdea-cb62-4982-b563-3d4aa8eabbc8"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    ProjectsManager projectsManager = Application.getInstance().getProjectsManager();
    File file = new File(moduleFilePath); 
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.createProjectDescriptor(file.toURI());
    projectsManager.reloadModule(project, projectDescriptor);]]></ac:plain-text-body></ac:structured-macro><br /><h4>Example #6. The package sharing</h4><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="63bfe953-0a0a-49b8-ae86-0b8b4fa64a44"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    ProjectsManager projectsManager = Application.getInstance().getProjectsManager();
    SessionManager.getInstance().createSession("Create shared package");
    // Create a package to share
    Package aPackage = project.getElementsFactory().createPackageInstance();
    aPackage.setOwner(project.getModel());
    aPackage.setName("myShare");
    SessionManager.getInstance().closeSession();
 
    // Share a package
    projectsManager.sharePackage(project, Arrays.asList(aPackage), "my used project");


    // Save a project
    ProjectDescriptor projectDescriptor = ProjectDescriptorsFactory.getDescriptorForProject(project);
    projectsManager.saveProject(projectDescriptor, true);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div><h4>Example #7. Editing a used project within the project</h4><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c1d6e8ec-af93-4da5-931d-36ba95abccf9"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    final String moduleFileName = new File(moduleFilePath).getName();
    // Find a used project directly used by the project (the primary project)
    final IAttachedProject attachedProject = ProjectUtilities.findAttachedProjectByName(project, moduleFileName, false);
    if (attachedProject != null)
    {
        final ModuleUsage moduleUsage = new ModuleUsage(project.getPrimaryProject(), attachedProject);
        final Set<ModuleUsage> moduleUsages = Collections.singleton(moduleUsage);
 
        final boolean readOnly = attachedProject.isReadOnly();
        if (readOnly)
        {
            // Make the used project editable (the read-write accessibility mode) 
            ModulesService.setReadOnlyOnTask(moduleUsages, false);
        }
        // Get the first shared package of the used project 
        final Collection<Package> sharedPackages = ProjectUtilities.getSharedPackages(attachedProject);
        final Package aPackage = sharedPackages.iterator().next();
        // Create a class in the used project
        SessionManager.getInstance().createSession("Create use case in used project");
        final Class aCase = project.getElementsFactory().createClassInstance();
        aCase.setOwner(aPackage);
        aCase.setName("myClass");
        SessionManager.getInstance().closeSession();
        // save the used project
        Application.getInstance().getProjectsManager().saveModule(project, attachedProject, true, false);
        if (readOnly)
        {
             // Make a used project not editable (the read-only accessibility mode) 
             ModulesService.setReadOnlyOnTask(moduleUsages, true);
        }
    }]]></ac:plain-text-body></ac:structured-macro><p><strong>Advanced management</strong></p><p>Use the <em>com.nomagic.magicdraw.core.ProjectUtilities</em> utility class for retrieving more project decomposition related information.</p><p>Use the <em>com.nomagic.magicdraw.core.modules.ModulesService</em> or<em> </em><em>ProjectsManager</em> classes for managing attached projects.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4a08eab3-2fc2-4bad-9ef7-29af33cb5d38"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Project descriptor" ri:space-key="DEVG2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Project structure decomposition" ri:space-key="DEVG2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347383 space=DEVG2024xR3 version=1 -->
## PAGE 00224: Using and extending other UI components

- page_id: `225347383`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347383/Using+and+extending+other+UI+components
- version_number: 1
- version_date: `2024-01-31T16:08:58.002+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide
- labels: []

### NORMALIZED CONTENT

Open API exposes some reusable and customizable UI components. They can be used for example from custom actions.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Open API exposes some reusable and customizable UI components. They can be used for example from custom actions.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0121fd4b-0734-4531-8ebb-22017f830cb2" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347282 space=DEVG2024xR3 version=1 -->
## PAGE 00225: Using StereotypesHelper

- page_id: `225347282`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347282/Using+StereotypesHelper
- version_number: 1
- version_date: `2024-02-13T10:27:51.475+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML model > Working with stereotypes and tagged values
- labels: []

### NORMALIZED CONTENT

Use utility class *com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper* to work with profiles, stereotypes, tagged values.

*StereotypesHelper* extends *com.nomagic.uml2.ext.jmi.helpers.TagsHelper*. Keep in mind that *Tagged Values*in these helpers are also called stereotype properties.

*StereotypeHelper* still provides deprecated API to check for stereotypes by a stereotype name. Try to avoid this API and pass Stereotype as object if possible. In many models several profiles with stereotypes with same names can be used and this "name based" API can cause unpredictable results.

So general rules are:

- Put URI for your profiles and find Profile in model by URI, not by profile name
- Find Stereotype element inside a specific Profile, not in a whole model
- Pass Stereotype element to StereotypesHelper methods instead of passing a stereotype name

****

**Find a stereotype by name**

Find profile by URI (or by name) first using

*StereotypesHelper.getProfileByURI(Project, java.lang.String)*

*StereotypesHelper.getProfile(Project, java.lang.String)*

Find stereotype by name inside a profile using

*StereotypesHelper.getStereotype(Project, java.lang.String, Profile[)](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#getStereotype-com.nomagic.magicdraw.core.Project-java.lang.String-com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile-)*

****

**Check if stereotype is applied**

Check if any stereotype is applied

*StereotypesHelper.hasStereotype(Element[)](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-)*

*or*

*check if**Element.getAppliedStereotype()* collection is empty

**

Check if concrete stereotype is assigned

,

)

or

Element.getAppliedStereotype()

Check if concrete stereotype or derived stereotype is applied

*StereotypesHelper.hasStereotypeOrDerived(Element[,](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotypeOrDerived-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)Stereotype[)](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotypeOrDerived-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)*

****

**Get value of tagged value**

Values of tagged values are returned as *java.util.List* even if upper multiplicity of tag 1. In this case List will have zero or one object.

*TagsHelper.getStereotypePropertyValue(Element, Property)*

*TagsHelper.getStereotypePropertyValue(Element, Stereotype, java.lang.String)*

*TagsHelper.getStereotypePropertyFirst(Element, Property)*

*TagsHelper.getStereotypePropertyFirst(Element, Stereotype, java.lang.String)*

*TagsHelper.getTaggedValue(Element, Property)*

*TagsHelper.getTaggedValue(Element, Stereotype, java.lang.String)*

**

**Set value of tagged value**

*TagsHelper.setStereotypePropertyValue(Element, Stereotype, Property, java.lang.Object)*

*TagsHelper.setStereotypePropertyValue(Element, Stereotype, java.lang.String, java.lang.Object)*

**

*TagsHelper.clearStereotypeProperty(Element, Property)*

*TagsHelper.clearStereotypeProperty(Element, Property**)*

**Collect all elements with applied stereotype**

For a concrete stereotype use

*StereotypesHelper.getStereotypedElements(Stereotype)*

For a concrete stereotype and derived stereotypes from it use

*StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)*

Check if stereotype can be applied to Element

,

)

###### Remove stereotype from element

*StereotypesHelper.removeStereotype(Element[,](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#removeStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)Stereotype[)](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#removeStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)*

*or*

*remove from collection Element.getAppliedStereotype().*TaggedValues of removed stereotype will not be removed immediately using this approach, but will be removed on transaction commit.

###### Apply stereotype to element

*StereotypesHelper.addStereotype(Element[,](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#addStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)Stereotype[)](http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#addStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-)*

*or*

*add into collection *Element.getAppliedStereotype()**

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Use utility class <em style="line-height: 1.4285715;">com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper</em> to work with profiles, stereotypes, tagged values.</p><p><em>StereotypesHelper</em> extends <em>com.nomagic.uml2.ext.jmi.helpers.TagsHelper</em>. Keep in mind that <em style="letter-spacing: 0.0px;">Tagged Values </em>in these helpers are also called stereotype properties.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5dce80e5-9c6e-41b1-b514-60eaa771f2dc"><ac:rich-text-body><p><em>StereotypeHelper</em> still provides deprecated API to check for stereotypes by a stereotype name. Try to avoid this API and pass Stereotype as object if possible. In many models several profiles with stereotypes with same names can be used and this &quot;name based&quot; API can cause unpredictable results.</p><p>So general rules are:</p><ul><li>Put URI for your profiles and find Profile in model by URI, not by profile name</li><li>Find Stereotype element inside a specific Profile, not in a whole model</li><li>Pass Stereotype element to <em>StereotypesHelper</em> methods instead of passing a stereotype name</li></ul></ac:rich-text-body></ac:structured-macro><p><strong><br /></strong></p><p><strong>Find a stereotype by name</strong></p><p>Find profile by URI (or by name) first using </p><p><em>StereotypesHelper.getProfileByURI(Project, java.lang.String)</em></p><p><em>StereotypesHelper.getProfile(Project, java.lang.String)</em></p><p><br /></p><p>Find stereotype by name inside a profile using </p><p><em>StereotypesHelper.getStereotype(Project, java.lang.String, Profile<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#getStereotype-com.nomagic.magicdraw.core.Project-java.lang.String-com.nomagic.uml2.ext.magicdraw.mdprofiles.Profile-">)</a></em></p><p><strong><br /></strong></p><p><strong>Check if stereotype is applied</strong></p><p>Check if any stereotype is applied</p><p><em>StereotypesHelper.hasStereotype(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-">)</a></em></p><p><em>or </em></p><p><em>check if </em><em style="letter-spacing: 0.0px;">Element.getAppliedStereotype()</em> collection is empty</p><p><em><br /></em></p><div>Check if concrete stereotype is assigned</div><div><em>StereotypesHelper.hasStereotype(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">, </a>Stereotype<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">)</a></em></div><div><em>or</em></div><div><em>check if <em>Element.getAppliedStereotype()</em> collection contains stereotype</em></div><p><span style="line-height: 1.4285715;"><br /></span></p><p><span style="line-height: 1.4285715;">Check if concrete stereotype or derived stereotype is applied</span></p><p><em>StereotypesHelper.hasStereotypeOrDerived(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotypeOrDerived-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">, </a>Stereotype<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#hasStereotypeOrDerived-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">)</a></em></p><p><strong><br /></strong></p><p><strong>Get value of tagged value</strong></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c641583f-7087-4073-9f5c-5be5b57c6145"><ac:rich-text-body><p>Values of tagged values are returned as <em>java.util.List</em> even if upper multiplicity of tag 1. In this case List will have zero or one object.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><em>TagsHelper.getStereotypePropertyValue(Element, Property)</em></p><p><em>TagsHelper.getStereotypePropertyValue(Element, Stereotype, java.lang.String)</em></p><p><br /></p><p><em>TagsHelper.getStereotypePropertyFirst(Element, Property)</em></p><p><em>TagsHelper.getStereotypePropertyFirst(Element, Stereotype, java.lang.String)</em></p><p><br /></p><p><em style="letter-spacing: 0.0px;">TagsHelper.getTaggedValue(Element, Property)</em></p><p><em>TagsHelper.getTaggedValue(Element, Stereotype, java.lang.String)</em></p><p><em><br /></em></p><p><strong style="line-height: 1.4285715;">Set value of tagged value</strong></p><p><em>TagsHelper.setStereotypePropertyValue(Element, Stereotype, Property, java.lang.Object)</em></p><p><em>TagsHelper.setStereotypePropertyValue(Element, Stereotype, java.lang.String, java.lang.Object)</em></p><p><em><br /></em></p><p><em>TagsHelper.clearStereotypeProperty(Element, Property)<br /></em></p><p><em>TagsHelper.clearStereotypeProperty(Element, Property</em><em>)</em></p><p><br /></p><p><strong>Collect all elements with applied stereotype</strong></p><p>For a concrete stereotype use</p><p><em>StereotypesHelper.getStereotypedElements(Stereotype)</em></p><p>For a concrete stereotype and derived stereotypes from it use</p><p><em>StereotypesHelper.getStereotypedElementsIncludingDerived(Stereotype)</em></p><p><br /></p><div><strong style="line-height: 1.4285715;">Check if stereotype can be applied to Element</strong></div><div><strong style="line-height: 1.4285715;"><br /></strong><em>StereotypesHelper.canApplyStereotype(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#canApplyStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">, </a>Stereotype<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#canApplyStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">)</a></em></div><div><em><br /></em></div><div><h4>Remove stereotype from element</h4><p><em>StereotypesHelper.removeStereotype(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#removeStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">, </a>Stereotype<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#removeStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">)</a></em></p><p><em>or </em></p><p><em>remove from collection Element.getAppliedStereotype(). </em>TaggedValues of removed stereotype will not be removed immediately using this approach, but will be removed on transaction commit.</p><h4>Apply stereotype to element</h4><p><em>StereotypesHelper.addStereotype(Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#addStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">, </a>Stereotype<a href="http://jdocs.nomagic.com/2024x/com/nomagic/uml2/ext/jmi/helpers/StereotypesHelper.html#addStereotype-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype-">)</a></em></p><p><em>or</em></p><p><em>add into collection <em>Element.getAppliedStereotype()</em> </em></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2bb9601d-36fa-4719-9f75-2df28ff82fc1"><ac:parameter ac:name="language">java</ac:parameter><ac:parameter ac:name="title">Sample</ac:parameter><ac:plain-text-body><![CDATA[Element element = ....; //Element for which we add stereotype, set tag value and then remove the stereotype.
Project project = ...; //Project
String tagValue = "test value";
Profile profile = StereotypesHelper.getProfile(project, "ProfileNameExample");
Stereotype stereotype = StereotypesHelper.getStereotype(project, "StereotypeNameExample", profile);
StereotypesHelper.addStereotype(element, stereotype); //We add stereptype to element
StereotypesHelper.setStereotypePropertyValue(element, stereotype, "TagName", tagValue); //we set stereotype tag named "TagName"
StereotypesHelper.removeStereotype(element, stereotype); //we remove stereotype from element]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div><p><br /></p>
````

<!--NOMAGIC_PAGE id=225347428 space=DEVG2024xR3 version=1 -->
## PAGE 00226: Utility class

- page_id: `225347428`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347428/Utility+class
- version_number: 1
- version_date: `2023-12-08T15:24:12.074+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Oracle DDL generation and customization
- labels: []

### NORMALIZED CONTENT

The utility class helps to retrieve information from model elements. Use these commands to get particular information:

```text

```

Returns *true* if a given element has an applied given stereotype.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to check. |
| $stereotypeName | java.lang.String | A stereotype name to be checked. |  |
| Return | - | boolean | true if elements have an applied stereotype with a given name. |

```text

```

From the given element, stereotype name, and tag name returns a tag value as *Boolean* from the Oracle profile.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to check. |
| $stereotypeName | java.lang.String | A stereotype name (from the default profile) that should be applied. |  |
| $propertyName | java.lang.String | A property name which value will be retrieved. |  |
| Return | - | boolean | A boolean value of property (tag). |

```text

```

Returns a list of given property values, that exist on the given element with the applied stereotype from the Oracle profile.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| $stereotypeName | java.lang.String | A stereotype name which should be applied. |  |
| $propertyName | java.lang.String | A property (tag) name to get values from. |  |
| Return | - | java.util.List | A list of property values. |

```text

```

Returns teh first given tag property value from the given element, which has the applied given stereotype.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| $stereotypeName | java.lang.String | A stereotype name that should be applied to the element. |  |
| $propertyName | java.lang.String | A property name where to check for values. |  |
| Return | - | java.lang.String | The first property value in a string representation. |

```text

```

From the given property returns the default value as boolean.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $property | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property | A boolean property to be check for the default value. |
| Return | - | boolean | The default boolean value of a property (tag). |

```text

```

Returns first given tag property value from given element, which has applied given stereotype from profile.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| $profileName | java.lang.String | A profile name where the stereotype exists. |  |
| $stereotypeName | java.lang.String | A stereotype name. |  |
| $propertyName | java.lang.String | A property (tag) name, which value will be checked. |  |
| Return | - | java.lang.String | The first value in a property list in String. |

```text

```

Returns a list of given property values, that exist on a given element with an applied stereotype from the given profile.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| $profileName | java.lang.String | A profile name where the stereotype exists. |  |
| $stereotypeName | java.lang.String | A stereotype name. |  |
| $propertyName | java.lang.String | A property (tag) name, which value will be checked. |  |
| Return | - | java.lang.List | A list of property values. |

```text

```

From the given tag value returns the *String* representation.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $object | java.lang.Object | An objectto be tested. |
| Return | - | java.lang.String | A string representation of the object. |

```text

```

Returns *true* if element is data type.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | boolean | true if the element is the datatype. |

```text

```

From the given type and modifier returns it's description.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $type | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type | A type of an element. |
| $modifier | java.lang.String | A modifier of the type. |  |
| Return | - | java.lang.String | A type definition for Oracle DDL. |

```text

```

Returns the Type modifier for the given element.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | java.lang.String | The Type modifier description. |

```text

```

Returns the list of operation parameters.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Operation | An operation to be tested. |
| Return | - | java.util.List | A list of operation parameters. |

```text

```

Returns the given property constraint.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $column | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property | A column to check for the constraint. |
| Return | - | java.util.List | A constraint definition. |

```text

```

Returns the CREATE statement for the given element.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | Java.lang.String | A description - CREATE or CREATE OR REPLACE. |

```text

```

Returns the Return type parameter of a given Operation.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameters | $operation | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature | An operation to check. |
| $createIfNeeded | boolean | A flag to create a return parameter if it does not exist. |  |
| Return | - | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Parameter | Return the parameter of a given Operation. |

```text

```

Returns a name of a given index.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $index | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.BehavioralFeature | BehavioralFeature as an Oracle index to be checked for a name. |
| Return | - | java.lang.String | A name of an index. |

```text

```

From the given dependency, returns a table constraint definition.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $dependency | com.nomagic.uml2.ext.magicdraw.classes.ddependencies.Dependency | A dependency to be tested. |
| Return | - | java.lang.String | A definition of the table constraint. |

```text

```

Checks if a given element is a package.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | boolean | true if the element is a package. |

```text

```

Returns *true,* if a given package is a database.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $package | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package | A package to be tested. |
| Return | - | boolean | true if a package is a database. |

```text

```

Returns *true,* if a given element has the public visibility.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | boolean | true if an element has the public visibility. |

```text

```

Reverses a given list.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $list | Java.util.List | A list to be reversed. |
| Return | - | Java.util.List | A reversed list. |

```text

```

Returns a reference name description for the element with the "Ref:Element" tag.

|  | Name | Type | Description |
| --- | --- | --- | --- |
| Parameter | $element | com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element | An element to be tested. |
| Return | - | java.lang.String | A reference element name. |

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The utility class helps to retrieve information from model elements. Use these commands to get particular information:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dd2bf68c-70a4-4df2-928b-a4eb8e20d2e6"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[    $oracleHelper.hasStereotype($element, $stereotypeName)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns <em>true</em> if a given element has an applied given stereotype.</p><table><tbody><tr><th> </th><th><p>Name </p></th><th> Type</th><th>Description </th></tr><tr><td rowspan="2"><strong> Parameters </strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2<span style="line-height: 1.4285715;">.ext.magicdraw.<br />c</span><span style="line-height: 1.4285715;">lasses.mdkernel.</span><span style="line-height: 1.4285715;">Element</span></pre></td><td><span>An element to check.</span></td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td>A s<span>tereotype name to be checked.</span></td></tr><tr><td><strong> Return</strong></td><td><pre>-</pre></td><td><pre> boolean</pre></td><td><span><em>true</em> if elements have an applied stereotype with a given name.</span></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ef33f155-c59e-4bbd-b77a-0cebbef4bdaa"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getBooleanValueFromDefaultProfile($element, $stereotypeName, $propertyName)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">From the given element, stereotype name, and tag name returns a tag value as <em>Boolean</em> from the Oracle profile.</p><table><tbody><tr><th> </th><th>Name </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="3"><strong>Parameters</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><span>An element to check.</span></td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td><span>A stereotype name (from the default profile) that should be applied.</span></td></tr><tr><td><pre>$propertyName</pre></td><td><pre>java.lang.String</pre></td><td><span>A property name which value will be retrieved.</span></td></tr><tr><td><strong>Return</strong></td><td>-</td><td><pre>boolean</pre></td><td><span>A boolean value of property (tag).</span></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e957cf58-d538-4e32-a0e2-4ea858f910df"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getPropertiesListFromDefaultProfile($element, $stereotypeName, $propertyName)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns a list of given property values, that exist on the given element with the applied stereotype from the Oracle profile.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="3"><strong>Parameters</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td>An element to <span>be tested.</span></td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td>A stereotype name which should be applied.</td></tr><tr><td><pre>$propertyName</pre></td><td><pre>java.lang.String</pre></td><td><span>A property (tag) name to get values from.</span></td></tr><tr><td><strong>Return</strong></td><td>-</td><td><pre><span>java.util.List</span></pre></td><td><span>A list of property values.</span></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="401c166f-8dbd-4932-82cb-02d284b91d0c"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getFirstPropertyValueFromProfile($element, $stereotypeName, $propertyName)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns teh first given tag property value from the given element, which has the applied given stereotype.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="3"><strong>Parameters</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td>An element to be tested.</td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td>A stereotype name <span> that should be applied to the element.</span></td></tr><tr><td><pre>$propertyName</pre></td><td><pre>java.lang.String</pre></td><td><span>A property name where to check for values.</span></td></tr><tr><td><strong>Return</strong></td><td>-</td><td><pre><span>java.lang.String</span></pre></td><td><span>The first property value in a string representation.</span></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6c613951-a87c-4360-aeba-19b40d8d5ac7"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getDefaultValueAsBoolean($property)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">From the given property returns the default value as boolean.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$property</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Property</pre></td><td><span>A boolean property to be check for the default value.</span></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td>-</td><td><pre>boolean</pre></td><td><p>The default boolean value of a property (tag).</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="874ce3c1-f1f0-4032-a3ae-e818af4c22ce"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getFirstPropertyValueFromGivenProfile($element, $profileName, $stereotypeName, $propertyName)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns first given tag property value from given element, which has applied given stereotype from profile.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="4"><strong><span style="color: rgb(0,0,0);">Parameters</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><pre>$profileName</pre></td><td><pre>java.lang.String</pre></td><td><p>A profile name where the stereotype exists.</p></td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td><p>A stereotype name.</p></td></tr><tr><td><pre>$propertyName</pre></td><td><pre>java.lang.String</pre></td><td><p>A property (tag) name, which value will be checked.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>The first value in a property list in <em>String</em>.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5ff77733-4f82-4cc1-a15c-19ce64ecf92c"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getPropertiesListFromProfile($element, $profileName, $stereotypeName, $propertyName) ]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns a list of given property values, that exist on a given element with an applied stereotype from the given profile.</p><div><p> </p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="4"><strong>Parameters</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><pre>$profileName</pre></td><td><pre>java.lang.String</pre></td><td><p>A profile name where the stereotype exists.</p></td></tr><tr><td><pre>$stereotypeName</pre></td><td><pre>java.lang.String</pre></td><td><p>A stereotype name.</p></td></tr><tr><td><pre>$propertyName</pre></td><td><pre>java.lang.String</pre></td><td><p>A property (tag) name, which value will be checked.</p></td></tr><tr><td><strong>Return</strong></td><td><pre>-</pre></td><td><pre>java.lang.<span>List</span></pre></td><td><p><span>A list of property values.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e8af7f85-8513-45a0-950b-ec6dcfa0c3a1"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getStringValue($object)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">From the given tag value returns the <em>String</em> representation.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th colspan="1"><strong>Description</strong></th></tr><tr><td><strong>Parameter</strong></td><td><pre>$object</pre></td><td><pre>java.lang.Object</pre></td><td colspan="1"><p><span>An objectto be tested.</span></p></td></tr><tr><td><strong>Return</strong></td><td><p>-</p></td><td><pre>java.lang.String</pre></td><td colspan="1"><p><span>A string representation of the object.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ffe87551-7747-41e0-bec8-07cf3ad29d2c"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.isDataType($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns <em>true</em> if element is data type.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th colspan="1"><strong>Description</strong></th></tr><tr><td><strong>Parameter</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td colspan="1"><p>An element to be tested.</p></td></tr><tr><td><strong>Return</strong></td><td><p>-</p></td><td><pre>boolean</pre></td><td colspan="1"><p><em>true</em> if the element is the datatype.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d321f56b-2fc4-4f4d-9547-9796b43b544f"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getType($type, $modifier)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">From the given type and modifier returns it's description.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="2"><strong>Parameters</strong></td><td><pre>$type</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Type</pre></td><td><p>A type of an element.</p></td></tr><tr><td><pre>$modifier</pre></td><td><pre>java.lang.String</pre></td><td><p>A modifier of the type.</p></td></tr><tr><td><strong>Return</strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>A type definition for Oracle DDL.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a81a6204-b644-4036-b561-278c19e2eb34"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[      $oracleHelper.getTypeModifier($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns the Type modifier for the given element.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameters</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>The Type modifier description.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1038c4d3-73e1-425e-9c08-20edc0004d1e"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getParameters($operation)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns the list of operation parameters.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Operation</pre></td><td><p>An operation to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.util.List</pre></td><td><p>A list of operation parameters.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="05017225-17bf-409f-a0dc-ffa532daa71f"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getColumnConstraint($column)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns the given property constraint.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong>Parameter</strong></td><td><pre><span>$column</span></pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Property</pre></td><td><p><span>A column to check for the constraint.</span></p></td></tr><tr><td><strong>Return</strong></td><td><pre>-</pre></td><td><pre>java.util.List</pre></td><td><p><span>A constraint definition.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="bb7afbf4-2c1f-48b1-8ebd-e7c7fa2f7d58"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getCreate($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns the CREATE statement for the given element.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong>Parameter</strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p><span>An element to be tested.</span></p></td></tr><tr><td><strong>Return</strong></td><td><pre>-</pre></td><td><pre><span>Java.lang.String</span></pre></td><td><p><span>A description - CREATE or CREATE OR REPLACE.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="99561a98-d436-4c7f-b121-c47c1dfd30d3"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getReturnParameter($operation, $createIfNeeded)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns the Return type parameter of a given Operation.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td rowspan="2"><strong><span style="color: rgb(0,0,0);">Parameters</span></strong></td><td><pre>$operation</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.BehavioralFeature</pre></td><td><p>An operation to check.</p></td></tr><tr><td><pre>$createIfNeeded</pre></td><td><pre>boolean</pre></td><td><p>A flag to create a return parameter if it does not exist.</p></td></tr><tr><td><strong>Return</strong></td><td><pre>-</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Parameter</pre></td><td><p>Return the parameter of a given Operation.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="815f7dc3-341b-4aed-a5fa-6e1882ba9f9f"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getIndexNameDefinition($index)]]></ac:plain-text-body></ac:structured-macro><div class="WordSection1"><p style="margin-left: 30.0px;">Returns a name of a given index.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$index</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.BehavioralFeature</pre></td><td><p>BehavioralFeature as an Oracle index to be checked for a name.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>A name of an index.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a1dd0e6d-8026-418f-a4ce-7a55cd75253e"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getTableConstraintDefinition($dependency)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">From the given dependency, returns a table constraint definition.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$dependency</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.ddependencies.Dependency</pre></td><td><p>A dependency to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>A definition of the table constraint.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6c3d6aaa-1217-4945-92a2-2cd353ae01ed"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.isObjectPackage($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Checks if a given element is a package.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>boolean</pre></td><td><p><em>true</em> if the element is a package.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="aa423649-4bb8-4a56-b190-3e6d38227809"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.isPackageDatabase($package)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns <em>true,</em> if a given package is a database.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$package</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Package</pre></td><td><p>A package to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>boolean</pre></td><td><p><em>true</em> if a package is a database.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="caaaccab-203d-460c-8513-b339eb91f400"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.isPublic($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns <em>true,</em> if a given element has the public visibility.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>boolean</pre></td><td><p><em>true</em> if an element has the public visibility.</p></td></tr></tbody></table><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ccd16ee0-d209-4447-8755-7638f038e9d0"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.reverseList($list)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Reverses a given list.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$list</pre></td><td><pre>Java.util.List</pre></td><td><p>A list to be reversed.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>Java.util.List</pre></td><td><span>A reversed list.</span></td></tr></tbody></table><div class="WordSection1"><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a9f024d0-cf58-4282-a61b-59397e2cd184"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[     $oracleHelper.getRefName($element)]]></ac:plain-text-body></ac:structured-macro><p style="margin-left: 30.0px;">Returns a reference name description for the element with the &quot;Ref:Element&quot; tag.</p><table><tbody><tr><th> </th><th><strong>Name</strong> </th><th> <strong>T</strong><strong>ype</strong></th><th><strong>Description</strong></th></tr><tr><td><strong><span style="color: rgb(0,0,0);">Parameter</span></strong></td><td><pre>$element</pre></td><td><pre>com.nomagic.uml2.ext.magicdraw.<br />classes.mdkernel.Element</pre></td><td><p>An element to be tested.</p></td></tr><tr><td><strong><span style="color: rgb(0,0,0);">Return</span></strong></td><td><pre>-</pre></td><td><pre>java.lang.String</pre></td><td><p>A reference element name.</p></td></tr></tbody></table><p> </p></div></div></div><div class="WordSection1" style="margin-left: 30.0px;"><pre> </pre></div></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347392 space=DEVG2024xR3 version=1 -->
## PAGE 00227: Validation rule developer's roadmap

- page_id: `225347392`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347392/Validation+rule+developer+s+roadmap
- version_number: 1
- version_date: `2023-12-08T15:24:39.287+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Creating validation rules
- labels: []

### NORMALIZED CONTENT

Validation rule developer’s roadmap allows faster understanding of steps required for creating a validation rule.

[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Creating validation rules' space='DEVG2024xR3']Creating validation rules

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Validation rule developer’s roadmap allows faster understanding of steps required for creating a validation rule.</p><p><ac:image><ri:attachment ri:filename="validationRuleRoadmap.png"><ri:page ri:content-title="Validation rule developer's roadmap" ri:space-key="DEVG2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f368d5fe-805a-447b-a01b-fca122ddd589"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Creating validation rules" ri:space-key="DEVG2024xR3" /><ac:link-body>Creating validation rules<br /></ac:link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347262 space=DEVG2024xR3 version=1 -->
## PAGE 00228: Visitors

- page_id: `225347262`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347262/Visitors
- version_number: 1
- version_date: `2024-02-13T09:34:45.414+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML model > Working with UML model > Model traversing, Visitor pattern
- labels: []

### NORMALIZED CONTENT

Visitor design pattern is implemented in UML model structure. Every *com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element* has the *accept(**AbstractVisitor)*method for visiting it*.*

The *com.nomagic.uml2.impl.ModelVisitor* has the *visit<element_metatype>*method for all types of model elements. This is very useful when you are working with a large collection of elements**and need to perform actions, specific for every type of *Element*(for example, save/load, copy/paste, or a specific properties setting).

Just derive your class from *com.nomagic.magicdraw.uml.InheritanceVisitor* and override some *visit.*methods and call *accept(**AbstractVisitor)* for *Elements.*

```java
it = root.getOwnedElement().iterator();
    while (it.hasNext())
    {
        it.next().accept(myVisitor);
    }]]>
```

****You can find the code examples in *<installation_directory>\openapi\examples\statistics*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Visitor design pattern is implemented in UML model structure. Every <em>com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element</em> has the <em>accept(</em><em>AbstractVisitor) </em>method for visiting it<em style="line-height: 1.4285715;">. </em></p><p>The <em>com.nomagic.uml2.impl.ModelVisitor</em> has the <em>visit&lt;element_metatype&gt; </em>method for all types of model elements. This is very useful when you are working with a large collection of elements<em style="line-height: 1.4285715;"> </em>and need to perform actions, specific for every type of <em style="line-height: 1.4285715;">Element </em>(for example, save/load, copy/paste, or a specific properties setting).</p><p>Just derive your class from <em>com.nomagic.magicdraw.uml.InheritanceVisitor</em> and override some <em>visit. </em>methods and call <em>accept(</em><em>AbstractVisitor)</em> for <em>Elements.</em></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="79f767f1-b453-4cbc-823c-e1689c691119"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[    ModelVisitor myVisitor = new ModelVisitor()
    {
        // override some visit methods ...
        public void visitClass(Class element, VisitorContext context)
        {
        	//this is my UML Class 
        }
    };
    Project project = ...;
    Package root = project.getPrimaryModel(); 
    Iterator<Element> it = root.getOwnedElement().iterator();
    while (it.hasNext())
    {
        it.next().accept(myVisitor);
    }]]></ac:plain-text-body></ac:structured-macro><br /><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="149c6619-33cd-40ac-aa63-ffaeb054ed5d"><ac:rich-text-body><p><strong> </strong>You can find the code examples in <em>&lt;installation_directory&gt;\openapi\examples\statistics</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347347 space=DEVG2024xR3 version=2 -->
## PAGE 00229: Working with Dependency Matrix

- page_id: `225347347`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347347/Working+with+Dependency+Matrix
- version_number: 2
- version_date: `2025-04-24T08:17:45.687+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with diagrams
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3'] is a special type of diagram, that is, a diagram with a specific stereotype applied. Our modeling tools provide an API to:

- Create custom types of the Dependency Matrix.
- Customize a Dependency Matrix as follows:
  - Configure the command bar, shortcut menus of the row or column header element, cell, and filter panel.
  - Assign shortcut keys for commands.
  - Define custom dependencies that can be created in the matrix.
  - Specify the appearance of the matrix, that is, change the default colors of the cell and both row and column headers, assign custom icons to represent dependencies, and so forth.
  - Define cases when specific dependencies should be updated without rebuilding the whole matrix.
  - Export the data of a Dependency Matrix to any format.

****You can find the code examples in

- <installation_directory>\openapi\examples\dependencymatrix

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:link><ri:page ri:content-title="Dependency Matrix" ri:space-key="MD2024xR3" /></ac:link> is a special type of diagram, that is, a diagram with a specific stereotype applied. Our modeling tools provide an API to:</p><ul><li>Create custom types of the Dependency Matrix.</li><li>Customize a Dependency Matrix as follows:<ul><li>Configure the command bar, shortcut menus of the row or column header element, cell, and filter panel.</li><li>Assign shortcut keys for commands.</li><li>Define custom dependencies that can be created in the matrix.</li><li>Specify the appearance of the matrix, that is, change the default colors of the cell and both row and column headers, assign custom icons to represent dependencies, and so forth.</li><li>Define cases when specific dependencies should be updated without rebuilding the whole matrix.</li><li>Export the data of a Dependency Matrix to any format.</li></ul></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="149c6619-33cd-40ac-aa63-ffaeb054ed5d"><ac:rich-text-body><p><strong> </strong>You can find the code examples in</p><ul><li><em>&lt;installation_directory&gt;\openapi\examples\dependencymatrix</em></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2ec81986-1195-4a33-b3e7-c53171711e90"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="020d5294-9339-4f3e-ac93-82cb86709a4c"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347289 space=DEVG2024xR3 version=1 -->
## PAGE 00230: Working with diagrams

- page_id: `225347289`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347289/Working+with+diagrams
- version_number: 1
- version_date: `2023-12-08T15:23:59.782+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide
- labels: []

### NORMALIZED CONTENT

Diagrams are not a part of UML metamodel, but we extended it and introduced a new Diagram element. Diagram element extends a standard UML NamedElement.

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Diagrams are not a part of UML metamodel, but we extended it and introduced a new Diagram element. Diagram element extends a standard UML NamedElement.</p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a074d2fc-ee1f-4fc4-aaae-f2073920d554"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5f33f1b4-4842-4f30-9938-416ac1254e80"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347360 space=DEVG2024xR3 version=1 -->
## PAGE 00231: Working with Gantt Chart

- page_id: `225347360`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347360/Working+with+Gantt+Chart
- version_number: 1
- version_date: `2023-12-08T15:24:05.386+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with diagrams
- labels: []

### NORMALIZED CONTENT

**Refreshing Gantt Chart**

To refresh the gantt chart, use the GanttChartUtilities.refreshChart(diagram) method:

```text

```

```text

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><span><strong>Refreshing Gantt Chart<br /></strong></span></p><p>To refresh the gantt chart, use the GanttChartUtilities.refreshChart(diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c4e582fc-94ba-4db7-83d9-bbf0bf654cc0"><ac:plain-text-body><![CDATA[GanttChartUtilities.refreshChart(Diagram)]]></ac:plain-text-body></ac:structured-macro><p><br /></p><pre><br /></pre>
````

<!--NOMAGIC_PAGE id=225347345 space=DEVG2024xR3 version=2 -->
## PAGE 00232: Working with Generic tables

- page_id: `225347345`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347345/Working+with+Generic+tables
- version_number: 2
- version_date: `2025-04-24T08:17:45.512+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with diagrams
- labels: []

### NORMALIZED CONTENT

A generic table is a diagram with a specific stereotype. It is used to represent the element properties in a table form. It can represent different element types in one table and show all their properties. Table rows represent elements, and columns represent element properties. For more information about generic tables and their managing, see [CONFLUENCE_PAGE title='Generic table' space='MD2024xR3'].

The Open API of modeling tools provides the***com.nomagic.generictable.GenericTableManager* class for creating and manipulating generic tables.

This API is used for creating a generic table, adding, editing, and removing table columns and rows, as well as getting cell values.

Find the Generic Table Manager Example Plugin in <*MagicDraw_installation_directory>\openapi\examples\generictablemanager*.

###### **Creatin****g generic table**

To create a generic table, use the *GenericTableManager.createGenericTable(**Project**, java.lang.String)* method.

```java

```

```text

```

###### **Settin****g generic table filter**

To set a generic table element types, use the *GenericTableManager.setTableElementTypes(**Diagram**, java.util.List<java.lang.Object>)***method. The type of the element types list could be the Class or the Stereotype. See an example of the table element types:

```java
set = new HashSet();
List tableElementTypes = new ArrayList();
 
//Get all row elements
rowElements = GenericTableManager.getRowElements(createdDiagram);
for (int i = 0; i < rowElements.size(); i++)
{
	set.add(rowElements.get(i).getClassType());
}
tableElementTypes.addAll(set);]]>
```

###### **Gettin****g generic table element types**

To get the generic table element types, use the *GenericTableManager.getTableElementTypes(**Diagram)***method:

```java
setElementTypes = GenericTableManager.getTableElementTypes(createdDiagram);]]>
```

###### **Adding/gettin****g columns**

To add columns to the generic table, use the *GenericTableManager.addColumnsById(Diagram, java.util.List<java.lang.String>)*method.

To get all possible columns from the generic table, use the *GenericTableManager.getPossibleColumnIDs(**Element)***method. To get set columns for the generic table, use the *GenericTableManager.getColumnIds(**Diagram)***method.

```java
columnIDs = GenericTableManager.getPossibleColumnIDs(elementType);]]>
```

*getColumnIds(**Diagram)* returns columns from the generic table:

```java
columnIDs = GenericTableManager.getColumnIds(createdDiagram); 
GenericTableManager.addColumnsById(createdDiagram, columnIDs);]]>
```

How to get *columnIDs*, please look at the *com.nomagic.magicdraw.examples.generictablemanager.GenericTableManagerExamplePlugin.GenericTableManagerAction* class in the *GenericTableManagerExamplePlugin.java*file. The file can be found in *<program_installation_directory>\openapi\examples\generictablemanager*.

###### **Gettin****g cell value**

To get a value of the generic table call, use the *GenericTableManager.getCellValue(Diagram[,](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getCellValue-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-java.lang.String-)Element, java.lang.String)*method:

```java

```

###### **Gettin****g column names**

To get column names from the generic table, use the *GenericTableManager.getColumnNames(Diagram[)](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getColumnNames-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-)*method.

To get a single column name from the generic table, use the *GenericTableManager.getColumnNameById(**Diagram**, java.lang.String)***method.

```java
columnNames = GenericTableManager.getColumnNames(createdDiagram);
String columnName = GenericTableManager.getColumnNameById(createdDiagram, columnID);]]>
```

###### **Gettin****g row elements**

To get row elements from the generic table, use the *GenericTableManager.getRowElements(**Diagram)***method:

```java
rows = GenericTableManager.getRowElements(createdDiagram);]]>
```

******Gettin****g visible row elements**

To get visible row elements from the generic table, use the *GenericTableManager.getVisibleRowElements(**Diagram)***method:

```java
rows = GenericTableManager.getVisibleRowElements(createdDiagram);]]>
```

###### **Addin****g row element**

To add a new row for the model element to the generic table, use the *GenericTableManager.addRowElement(Diagram[,](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-)Element[)](http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-)*method:

```java

```

The element you want to add must be of the same type as one of generic table filter types.

###### **Removin****g row element**

To remove a row from the generic table, use the *GenericTableManager.removeRowElement(**Diagram, Element)***method:

```java

```

**Setting table scope**

To set a scope for the generic table, use the *GenericTableManager.removeRowElement(**Diagram, Element)***method:

```java

```

**Refreshing table**

To refresh the table, use the GenericTableManager.refreshTable(Diagram) method:

```java

```

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Session management' space='DEVG2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A generic table is a diagram with a specific stereotype. It is used to represent the element properties in a table form. It can represent different element types in one table and show all their properties. Table rows represent elements, and columns represent element properties. For more information about generic tables and their manag<span style="color: rgb(0,0,0);">ing, see <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Generic table" /><ac:plain-text-link-body><![CDATA[Generic Table]]></ac:plain-text-link-body></ac:link>.</span></p><p>The Open API of modeling tools provides the<em> </em><em>com.nomagic.generictable.GenericTableManager</em> class for creating and manipulating generic tables.</p><div class="WordSection1"><p>This API is used for creating a generic table, adding, editing, and removing table columns and rows, as well as getting cell values.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1b944d37-d25a-4e2b-af42-bd6490c10121"><ac:rich-text-body><p>Find the Generic Table Manager Example Plugin in &lt;<em style="line-height: 1.4285715;">MagicDraw_installation_directory&gt;\openapi\examples\generictablemanager</em>.</p></ac:rich-text-body></ac:structured-macro><h4><strong style="color: rgb(0,0,0);line-height: 1.4285715;">Creatin</strong><strong style="color: rgb(0,0,0);line-height: 1.4285715;">g generic table</strong></h4><p>To create a generic table, use the <em>GenericTableManager.createGenericTable(</em><em>Project</em><em>, java.lang.String)</em> method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3c092b5b-12cf-4a75-92a0-fb1862597c7d"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[Diagram createdDiagram = GenericTableManager.createGenericTable(project, "Generic table name");]]></ac:plain-text-body></ac:structured-macro><pre><br /></pre><h4><strong>Settin</strong><strong>g generic table filter</strong></h4><p>To set a generic table element types, use the <em>GenericTableManager.setTableElementTypes(</em><em>Diagram</em><em>, java.util.List&lt;java.lang.Object&gt;)</em><em> </em>method. The type of the element types list could be the Class or the Stereotype. See an example of the table element types:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="42d3b258-b3cd-4227-995f-95557f7cd731"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[//The table element types list
Set<Class> set = new HashSet<Class>();
List<Object> tableElementTypes = new ArrayList<Object>();
 
//Get all row elements
rowElements = GenericTableManager.getRowElements(createdDiagram);
for (int i = 0; i < rowElements.size(); i++)
{
	set.add(rowElements.get(i).getClassType());
}
tableElementTypes.addAll(set);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div><div class="WordSection2"><h4><strong>Gettin</strong><strong>g generic table element types</strong></h4><p>To get the generic table element types, use the <em style="line-height: 1.4285715;">GenericTableManager.getTableElementTypes(</em><em style="line-height: 1.4285715;">Diagram)</em><em style="line-height: 1.4285715;"> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="685db55f-3f2e-400e-83a3-435e3dd89cca"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Object> setElementTypes = GenericTableManager.getTableElementTypes(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><h4><strong>Adding/gettin</strong><strong>g columns</strong></h4><p>To add columns to the generic table, use the <em>GenericTableManager.addColumnsById(Diagram, java.util.List&lt;java.lang.String&gt;) </em>method.</p><p>To get all possible columns from the generic table, use the <em>GenericTableManager.getPossibleColumnIDs(</em><em>Element)</em><em> </em>method. To get set columns for the generic table, use the <em>GenericTableManager.getColumnIds(</em><em>Diagram)</em><em> </em>method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7db69c7c-fa56-479b-a51d-ef5e68761182"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnIDs = GenericTableManager.getPossibleColumnIDs(elementType);]]></ac:plain-text-body></ac:structured-macro><p><em>getColumnIds(</em><em>Diagram)</em> returns columns from the generic table:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="017b2a32-14ba-4359-9ae0-530a9f42c2bd"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnIDs = GenericTableManager.getColumnIds(createdDiagram); 
GenericTableManager.addColumnsById(createdDiagram, columnIDs);]]></ac:plain-text-body></ac:structured-macro><br /><p>How to get <em>columnIDs</em>, please look at the <em>com.nomagic.magicdraw.examples.generictablemanager.GenericTableManagerExamplePlugin.GenericTableManagerAction</em> class in the <em>GenericTableManagerExamplePlugin.java </em>file. The file can be found in <em>&lt;program_installation_directory&gt;\openapi\examples\generictablemanager</em>.</p><p><br /></p><h4><strong>Gettin</strong><strong>g cell value</strong></h4><p>To get a value of the generic table call, use the <em>GenericTableManager.getCellValue(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getCellValue-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-java.lang.String-">, </a>Element, java.lang.String) </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="13ffc60b-1f89-4985-bb39-9f0f8f088edb"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[Property mdProperty = GenericTableManager.getCellValue(createdDiagram, element, columnId);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Gettin</strong><strong>g column names</strong></h4><p>To get column names from the generic table, use the <em>GenericTableManager.getColumnNames(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#getColumnNames-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-">)</a> </em>method.</p><p>To get a single column name from the generic table, use the <em>GenericTableManager.getColumnNameById(</em><em>Diagram</em><em>, java.lang.String)</em><em> </em>method.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9a55642b-51f3-4569-99f5-42c37f05b311"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<String> columnNames = GenericTableManager.getColumnNames(createdDiagram);
String columnName = GenericTableManager.getColumnNameById(createdDiagram, columnID);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Gettin</strong><strong>g row elements</strong></h4><p>To get row elements from the generic table, use the <em>GenericTableManager.getRowElements(</em><em>Diagram)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="205ace80-6605-4aed-a640-2ef86c8f1e51"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Element> rows = GenericTableManager.getRowElements(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><p><strong style="color: rgb(0,0,0);line-height: 1.42857;"><br /></strong><strong style="color: rgb(0,0,0);line-height: 1.42857;">Gettin</strong><strong style="color: rgb(0,0,0);line-height: 1.42857;">g visible row elements</strong></p><p>To get visible row elements from the generic table, use the <em>GenericTableManager.getVisibleRowElements(</em><em>Diagram)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f47b5ee1-f6bc-4f76-9454-49f77f37e812"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[List<Element> rows = GenericTableManager.getVisibleRowElements(createdDiagram);]]></ac:plain-text-body></ac:structured-macro><br /><h4><strong>Addin</strong><strong>g row element</strong></h4><p>To add a new row for the model element to the generic table, use the <em>GenericTableManager.addRowElement(Diagram<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-">, </a>Element<a href="http://jdocs.nomagic.com/2024x/com/nomagic/generictable/GenericTableManager.html#addRowElement-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Diagram-com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element-">)</a> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ef82abee-a4a6-4134-923d-067125559f06"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.addRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p>The element you want to add must be of the same type as one of generic table filter types.</p></div><h4><strong>Removin</strong><strong>g row element</strong></h4><p>To remove a row from the generic table, use the <em>GenericTableManager.removeRowElement(</em><em>Diagram, Element)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="499d517d-469b-46e7-be89-f50dcfb26dc5"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.removeRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="letter-spacing: -0.042px;"><strong>Setting table scope</strong></span></p><p>To set a scope for  the generic table, use the <em>GenericTableManager.removeRowElement(</em><em>Diagram, Element)</em><em> </em>method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8b9a558c-c187-42b8-b1b4-1ec07ade738f"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.removeRowElement(createdDiagram, element);]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><span><strong>Refreshing table<br /></strong></span></p><p>To refresh the table, use the GenericTableManager.refreshTable(Diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d0465c4b-41d4-413a-8088-961710f0f49a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[GenericTableManager.refreshTable(diagram)]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="84ace198-a24b-457d-a46e-cc18a8db8595"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f616bdf8-03b9-420a-b222-ef83b9be7c5f" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="becf631e-811b-484c-90d3-30aaa50ab94c"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Session management" ri:space-key="DEVG2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347217 space=DEVG2024xR3 version=1 -->
## PAGE 00233: Working with icons

- page_id: `225347217`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347217/Working+with+icons
- version_number: 1
- version_date: `2024-02-13T09:37:24.955+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Adding new functionality
- labels: []

### NORMALIZED CONTENT

Use *com.nomagic.magicdraw.icons.IconsFactory*to load the icons.

As of version 18.2, modeling tools support HiDPI/Retina monitors and chooses dynamically which icon to load - a lower or higher resolution. All this logic is encapsulated in *com.nomagic.ui.ScalableImageIcon*. *IconsFactory*adds additional caching and ensures that icon from the same URL will be loaded just once.

The HiDPI/Retina compatibility requires two images - for a normal resolution and for a high resolution. Use the SVG format for a high resolution image. Put both icons with the same name (but a different extension) at the same location. Use a normal icon URL to load the icon, but the SVG icon will be loaded on the high resolution monitor.

##### Icon classes

| Class | Description |
| --- | --- |
| com.nomagic.ui.ResizableIcon | The extended version of javax.swing.Icon. It can be scaled (resized) during the painting. |
| com.nomagic.ui.ResizableIconAdapter | An adapter of a simple javax.swing.Icon to a com.nomagic.ui.ResizableIcon. |
| com.nomagic.ui.SquareIcon | An icon which fits another icon into a square of a given size. |
| com.nomagic.ui.ScalableImageIcon | The HiDPI (Retina) friendly javax.swing.ImageIcon implementation. This class dynamically chooses a right image by the current screen dpi and/or the scaling factor defined in the system (Retina and etc). If scaling is needed and the SVG icon with the same name is available at the given location, the SVG icon will be used instead of a bitmap icon. Dynamic choosing will work only if two icons are provided at the same location. For example, /com/product/icons/a.png and /com/product/icons/a.svg. ScalableImageIcon(Product.class, "/com/product/icons/a.png") will load a.png on a regular dpi monitor, but a.svg will be loaded on the HiDPI monitor. Keep in mind that the SVG icon size can be any. The SVG icon will be resized according to the size of the a.png icon and a scaling factor. For example, if a size of a.png is 16x16 and a scaling factor is 2, the loaded SVG icon will be resized to 32x32 if needed. The original icon will be loaded and scaled if the SVG icon is not provided, but HiDPI with scaling is used. |

##### Utility classes

| Class | Description |
| --- | --- |
| com.nomagic.magicdraw.icons.IconsFactory | A utility class to load icons from the MagicDraw icons package or other locations. |
| com.nomagic.ui.IconUtilities | A utility class to work with Icons. |

```text

```

##### Advanced icons classes

| Class | Description |
| --- | --- |
| com.nomagic.ui.AlphaCompositeIcon | Paints a wrapped icon with an alpha composite. |
| com.nomagic.ui.BorderIcon | An icon for adding a border around a wrapped icon. |
| com.nomagic.ui.DoubleIcon | An Icon for painting two wrapped icons on a top of each other. |
| com.nomagic.ui.RetinaImageIcon | A retina friendly image icon implementation. The icon (and the image returned by this icon) is twice smaller then the wrapped icon itself.A wrapped icon is used for painting. On painting, Graphics is scaled down by a retina scale factor and the wrapped icon is painted. |
| com.nomagic.ui.DoubleSizeImageIcon | An icon combines two other icons and chooses which one to paint depending on the graphics scaling. |
| com.nomagic.ui.ResizableIconImageIcon | An image icon which wraps other icon and provides an image for a wrapped icon. The provided image is HiDPI/Retina friendly. On Mac, a special instance of java.awt.Image (sun.awt.image.MultiResolutionToolkitImage) is returned which supports multi-resolution. |

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Use <em>com.nomagic.magicdraw.icons.IconsFactory </em>to load the icons. </p><p>As of version 18.2, modeling tools support HiDPI/Retina monitors and chooses dynamically which icon to load - a lower or higher resolution. All this logic is encapsulated in <em>com.nomagic.ui.ScalableImageIcon</em>. <em>IconsFactory </em>adds additional caching and ensures that icon from the same URL will be loaded just once.</p><p><span style="color: rgb(0,0,0);">The HiDPI/Retina compatibility requires two images - for a normal resolution and for a high resolution. Use the SVG format for a high resolution image. Put both icons with the same name (but a different extension) at the same location. Use a normal icon URL to load the icon, but the SVG icon will be loaded on the high resolution monitor.</span></p><h3><span>Icon classes</span></h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ResizableIcon</span></em></td><td colspan="1">The extended version of <em>javax.swing.Icon.</em> It can be scaled (resized) during the painting.</td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ResizableIconAdapter</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">An adapter of a simple <em>javax.swing.Icon</em> to a <em>com.nomagic.ui.ResizableIcon</em><em>.</em></span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.SquareIcon</span></em></td><td colspan="1"><p>An icon which fits another icon into a square of a given size.</p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.ScalableImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">The HiDPI (Retina) friendly <em>javax.swing.ImageIcon</em> implementation. This class dynamically chooses a right image by the current screen dpi and/or the scaling factor defined in the system (Retina and etc). If scaling is needed and the SVG icon with the same name is available at the given location, the SVG icon will be used instead of a bitmap icon. Dynamic choosing will work only if two icons are provided at the same location. </span></p><p><span style="color: rgb(0,0,0);">For example, </span><em><span style="color: rgb(0,0,0);">/com/product/icons/a.png </span></em><span style="color: rgb(0,0,0);">and </span><em><span style="color: rgb(0,0,0);">/com/product/icons/a.svg. </span>ScalableImageIcon</em><span style="color: rgb(0,0,0);"><em>(Product.class, &quot;/com/product/icons/a.png&quot;)</em> will load <em>a.png</em> on a regular dpi monitor, but <em>a.svg</em> will be loaded on the HiDPI monitor. </span><span style="color: rgb(0,0,0);">Keep in mind that the SVG icon size can be any. The SVG icon will be resized according to the size of the<em> a.png</em> icon and a scaling factor. </span><span style="color: rgb(0,0,0);">For example, if a size of <em>a.png</em> is 16x16 and a scaling factor is 2, the loaded SVG icon will be resized to 32x32 if needed. </span><span style="color: rgb(0,0,0);">The original icon will be loaded and scaled if the SVG</span><span> </span><span style="color: rgb(0,0,0);">icon is not provided, but HiDPI with scaling is used.</span></p><div><span style="color: rgb(0,0,0);"><br /></span></div></td></tr></tbody></table><h3>Utility classes</h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td><em>com.nomagic.magicdraw.icons.IconsFactory</em></td><td><span style="color: rgb(0,0,0);">A utility class to load icons from the MagicDraw icons package or other locations.</span></td></tr><tr><td><em>com.nomagic.ui.IconUtilities</em></td><td><span style="color: rgb(0,0,0);">A u</span><span style="color: rgb(0,0,0);">tility class to work with Icons.</span></td></tr></tbody></table><pre><br /></pre><h3><span style="color: rgb(0,0,0);">Advanced icons classes</span></h3><table><colgroup><col /><col /></colgroup><tbody><tr><th>Class</th><th>Description</th></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.AlphaCompositeIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">Paints a wrapped icon with an alpha composite.</span></p></td></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.BorderIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">An icon for adding a border around a wrapped icon.</span></p></td></tr><tr><td><em><span style="color: rgb(0,0,0);">com.nomagic.ui.DoubleIcon</span></em></td><td><p><span style="color: rgb(0,0,0);">An Icon for painting two wrapped icons on a top of each other.</span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.RetinaImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">A retina friendly image icon implementation. The icon (and the image returned by this icon) is twice smaller then the wrapped icon itself.</span></p><p><span style="color: rgb(0,0,0);">A wrapped icon is used for painting. On painting, Graphics is scaled down by a retina scale factor and the wrapped icon is painted.</span></p></td></tr><tr><td colspan="1"><em><span style="color: rgb(0,0,0);">com.nomagic.ui.DoubleSizeImageIcon</span></em></td><td colspan="1"><p><span style="color: rgb(0,0,0);">An icon combines two other icons and chooses which one to paint depending on the graphics scaling.</span></p></td></tr><tr><td colspan="1"><em>com.nomagic.ui.ResizableIconImageIcon</em></td><td colspan="1"><span style="color: rgb(0,0,0);"><span>An image icon which wraps other icon and provides an image for a wrapped icon. The p</span></span><span style="color: rgb(0,0,0);">rovided image is HiDPI/Retina friendly. On Mac, a special instance of <em>java.awt.Image</em> (<em>sun.awt.image.MultiResolutionToolkitImage</em>) is returned which supports multi-resolution.</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="83e819a2-cb1b-43fb-9c59-c36f9667233d"><ac:parameter ac:name="title">On this page</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7fded546-72ea-40a4-b103-845a3fa165dc" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="36954480-067d-430e-bdb9-742c68a9a8c1"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6c4cedb7-d96b-477c-924e-b34dc831c71a"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347310 space=DEVG2024xR3 version=1 -->
## PAGE 00234: Working with presentation elements

- page_id: `225347310`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347310/Working+with+presentation+elements
- version_number: 1
- version_date: `2024-02-13T09:38:50.110+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with diagrams > Presentation elements (symbols)
- labels: []

### NORMALIZED CONTENT

706297666

INLINE

706297668

INLINE

706297667

INLINE

Use only getter in Presentation elements’ classes even if setters are available. Setters are not part of OpenAPI and in most cases should not be called directly.

Majority of functions for manipulating/creating/deleting the symbols is available in utility class *com.nomagic.magicdraw.openapi.uml.PresentationElementsManager**.*

*PresentationElementManager* can be used only inside the created session with *com.nomagic.magicdraw.openapi.uml.SessionManager*. If a session is not created, *java.lang.IllegalStateException* is thrown.

*PresentationElementManager* can be used only in already loaded and active project. In other cases, results can be unpredictable.

*PresentationElementManager* is implemented as a singleton. Use method *PresentationElementManager.getInstance()*to get a shared instance of this manager.

706297665

INLINE

**Related pages**

- [CONFLUENCE_PAGE title='Session management' space='DEVG2024xR3']

true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c938f53a-5c7c-4427-822b-ba6db3822b35"><ac:parameter ac:name="id">706297666</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cdfae3ad-ea5f-484a-a06e-075f454d6ee3"><ac:parameter ac:name="id">706297668</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6a993cf2-94d7-4484-9117-d034054a7650"><ac:parameter ac:name="id">706297667</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="WordSection1"><p>Use only getter in Presentation elements’ classes even if setters are available. Setters are not part of OpenAPI and in most cases should not be called directly.</p><p><br /></p><p>Majority of functions for manipulating/creating/deleting the symbols is available in utility class <em>com.nomagic.magicdraw.openapi.uml.PresentationElementsManager</em><em>. </em></p><p><em>PresentationElementManager</em> can be used only inside the created session with <em>com.nomagic.magicdraw.openapi.uml.SessionManager</em>. If a session is not created, <em>java.lang.IllegalStateException</em> is thrown.</p></div><p><em>PresentationElementManager</em> can be used only in already loaded and active project. In other cases, results can be unpredictable.</p><p><em>PresentationElementManager</em> is implemented as a singleton. Use method <em>PresentationElementManager.getInstance() </em>to get a shared instance of this manager.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aaa930a4-864a-4f26-9658-07bcc0ce2e04"><ac:parameter ac:name="id">706297665</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Session management" ri:space-key="DEVG2024xR3" /></ac:link></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7c7ab909-e217-4362-9dd2-78168dfe4f57"><ac:parameter ac:name="all">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=225347220 space=DEVG2024xR3 version=1 -->
## PAGE 00235: Working with project

- page_id: `225347220`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347220/Working+with+project
- version_number: 1
- version_date: `2024-01-31T16:09:05.261+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a8251faf-7ec9-4e57-8f64-a886115f67a2" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347233 space=DEVG2024xR3 version=2 -->
## PAGE 00236: Working with projects from Teamwork Cloud server

- page_id: `225347233`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347233/Working+with+projects+from+Teamwork+Cloud+server
- version_number: 2
- version_date: `2025-04-24T08:17:44.973+02:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with project
- labels: []

### NORMALIZED CONTENT

Use the *com.nomagic.magicdraw.esi.EsiUtils* utility class to work with projects from [CONFLUENCE_PAGE title='Using Teamwork Cloud' space='MD2024xR3'].

Check javadoc for more details.

****You can find the code examples in <*modeling tool**installation direc**tory>\openapi\examples\teamworkcloud*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Use the <em>com.nomagic.magicdraw.esi.EsiUtils</em> utility class to work with projects from <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Using Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link>. </p><p>Check javadoc for more details.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="149c6619-33cd-40ac-aa63-ffaeb054ed5d"><ac:rich-text-body><p><strong> </strong>You can find the code examples in <span style="line-height: 1.4285715;">&lt;<em>modeling tool</em> </span><em style="line-height: 1.4285715;">installation direc</em><em style="line-height: 1.4285715;">tory&gt;\openapi\examples\teamworkcloud</em></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347359 space=DEVG2024xR3 version=1 -->
## PAGE 00237: Working with Relation Map

- page_id: `225347359`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347359/Working+with+Relation+Map
- version_number: 1
- version_date: `2023-12-08T15:24:05.277+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Working with diagrams
- labels: []

### NORMALIZED CONTENT

A relation map is a diagram with a specific stereotype. It is used to represent the element properties in a relation based form.It can represent elements connected via various relation criteria

The Open API of our modeling tools provides the**com.nomagic.magicdraw.visualization.relationshipmap.RelationshipMapUtilities****to work with Relation maps.

**Refreshing relation map**

To refresh the relation map, use the RelationshipMapUtilities.refreshMap(Diagram) method:

```java

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>A relation map is a diagram with a specific stereotype. It is used to represent the element properties in a relation based form.It can represent elements connected via various relation criteria</span></p><p><span>The Open API of our modeling tools provides the<em> </em>com.nomagic.magicdraw.visualization.relationshipmap.RelationshipMapUtilities<strong>  </strong>to work with Relation maps.</span></p><p class="auto-cursor-target"><br /></p><p><br /></p><p><span><strong>Refreshing relation map<br /></strong></span></p><p>To refresh the relation map, use the RelationshipMapUtilities.refreshMap(Diagram) method:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d0465c4b-41d4-413a-8088-961710f0f49a"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[RelationshipMapUtilities.refreshMap(diagram)]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><br /></p>
````

<!--NOMAGIC_PAGE id=225347280 space=DEVG2024xR3 version=1 -->
## PAGE 00238: Working with stereotypes and tagged values

- page_id: `225347280`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347280/Working+with+stereotypes+and+tagged+values
- version_number: 1
- version_date: `2024-02-13T09:40:20.796+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML model
- labels: ['stereotypes-helper', 'helper-class']

### NORMALIZED CONTENT

Standard UML metamodel is extended with additional meta-classes and meta-properties to support stereotypes applications.

[IMAGE alt='' src='']

There are two ways to work with stereotypes applications

- We provide a com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper helper class for hiding this mapping complexity. It has set of useful methods for assigning or unassigning stereotypes, creating TaggedValues
- Use profile implementation classes

#### PANEL: Related pages

Related pages

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> Standard UML metamodel is extended with additional meta-classes and meta-properties to support stereotypes applications.</p><p><ac:image ac:height="400"><ri:attachment ri:filename="image2020-3-12_9-29-28.png"><ri:page ri:content-title="Working with stereotypes and tagged values" ri:space-key="DEVG2024xR3" /></ri:attachment></ac:image></p><p>There are two ways to work with stereotypes applications</p><ul><li>We provide a <em>com.nomagic.uml2.ext.jmi.helpers.StereotypesHelper</em> helper class  for hiding this mapping complexity. It has set of useful methods for assigning or unassigning stereotypes, creating <em style="line-height: 1.4285715;">TaggedValues</em></li><li>Use profile implementation classes</li></ul><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c8695294-59d4-411e-80f7-18d01b1e07b6"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="428cfc7e-97da-4269-aec3-ce828becf8cb" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347182 space=DEVG2024xR3 version=1 -->
## PAGE 00239: Working with test resources

- page_id: `225347182`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347182/Working+with+test+resources
- version_number: 1
- version_date: `2024-02-13T09:57:27.813+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Plugins > Creating test cases
- labels: []

### NORMALIZED CONTENT

Test cases may use external resources such as configuration files and projects for testing purposes. It is recommended to keep external test resources apart from test case implementation class files. The test framework provides methods for retrieving test resources from the one specific resource directory.

Resource directory can be accessed by calling the *com.nomagic.magicdraw.tests.common.TestEnvironment.getResourceDir()* method. This method obtains the directory specified by the *tests.resources* system property. For information about specifying the *tests.resources* system property see [CONFLUENCE_PAGE title='Configure test environment' space='DEVG2024xR3']. The test framework also provides methods for collecting projects from the resource directory. Developers may use *TestEnvironment.getProjects(java.io.File)* for collecting projects recursively from a specific directory. Unnecessary projects can be filtered out by specifying their names in *skip.txt* files that are placed in the same directory as project files.

Test cases may produce some resources as a test output. The output directory for a specific test case can be created using *TestEnvironment.getOutputDir(java.lang.Class)*. The class here specifies a class of the test case which output directory should be accessed.

There are also methods for working with output files. An output file for a specific project can be simply created by changing the project file extension (*TestEnvironment.getFileWithExtension(java.io.File, java.lang.String)*) or adding a special prefix to its name (*TestEnvironment.createFileNameWithPrefix(**java.io.File, java.lang.String)* ).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><div class="WordSection1"><p>Test cases may use external resources such as configuration files and projects for testing purposes. It is recommended to keep external test resources apart from test case implementation class files. The test framework provides methods for retrieving test resources from the one specific resource directory.</p><p>Resource directory can be accessed by calling the <em>com.nomagic.magicdraw.tests.common.TestEnvironment.getResourceDir()</em> method. This method obtains the directory specified by the <em>tests.resources</em> system property. For information about specifying the <em>tests.resources</em> system property see <ac:link><ri:page ri:content-title="Configure test environment" ri:space-key="DEVG2024xR3" /></ac:link>. The test framework also provides methods for collecting projects from the resource directory. Developers may use <em>TestEnvironment.getProjects(java.io.File)</em> for collecting projects recursively from a specific directory. Unnecessary projects can be filtered out by specifying their names in <em>skip.txt</em> files that are placed in the same directory as project files.</p><p>Test cases may produce some resources as a test output. The output directory for a specific test case can be created using <em>TestEnvironment.getOutputDir(java.lang.Class)</em>. The class here specifies a class of the test case which output directory should be accessed.</p><p>There are also methods for working with output files. An output file for a specific project can be simply created by changing the project file extension (<em>TestEnvironment.getFileWithExtension(java.io.File, java.lang.String)</em>) or adding a special prefix to its name (<em>TestEnvironment.createFileNameWithPrefix(</em><em>java.io.File, java.lang.String)</em> ).</p></div></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347242 space=DEVG2024xR3 version=1 -->
## PAGE 00240: Working with UML model

- page_id: `225347242`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347242/Working+with+UML+model
- version_number: 1
- version_date: `2023-12-08T15:23:57.477+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > UML model
- labels: []

### NORMALIZED CONTENT

trueh4

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3a046f2e-f011-496e-a6b9-12c2589ee797"><ac:parameter ac:name="all">true</ac:parameter><ac:parameter ac:name="style">h4</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225347158 space=DEVG2024xR3 version=1 -->
## PAGE 00241: Writing plugins

- page_id: `225347158`
- space_key: `DEVG2024xR3`
- source_url: https://docs.nomagic.com/spaces/DEVG2024xR3/pages/225347158/Writing+plugins
- version_number: 1
- version_date: `2024-02-13T10:16:18.698+01:00`
- ancestors: Developer Guides Home > Modeling Tools Developer Guide > Plugins
- labels: []

### NORMALIZED CONTENT

With this example, we will create a plugin that displays a message on the program startup. To create the plugin, you need to write a plugin descriptor.

###### **Step** **#1:** **Create** **your** **plugin** **folder** **in** **a** *plugins* **folder**

Create a *myplugin* folder in the *plugins* folder in the installation directory of the modeling tool.

###### **Step** **#2:** **Write** **a plugin** **code**

The plugin must contain at least one class derived from the *com.nomagic.magicdraw.plugins.Plugin* class.

```java

```

This plugin shows the one message when it is initialized, and another message when it is closed.

###### **Step #3: Compile and pack the plugin to a *.jar* file**

For more information on the classpath specification details, see [CONFLUENCE_PAGE title='Compilation classpath' space='DEVG2024xR3'].

The compiled code must be packed to a *.jar* file.

To create a .jar file, use a jar command in the plugins directory:

```bash

```

###### **Step #4: Write a plugin descriptor**

The plugin descriptor is a file named*plugin.xml*. This file should be placed in the *myplugin* folder.

```xml
]]>
```

For detailed information about the plugin descriptor, see [CONFLUENCE_PAGE title='Plugin descriptor' space='DEVG2024xR3'].

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Compilation classpath' space='DEVG2024xR3']
- [CONFLUENCE_PAGE title='Plugin descriptor' space='DEVG2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>With this example, we will create a plugin that displays a message on the program startup. To create the plugin, you need to write a plugin descriptor.</p><h4><br /><strong>Step</strong> <strong>#1:</strong> <strong>Create</strong> <strong>your</strong> <strong>plugin</strong> <strong>folder</strong> <strong>in</strong> <strong>a</strong> <em>plugins</em> <strong>folder</strong></h4><p>Create a <em>myplugin</em> folder in the <em>plugins</em> folder in the installation directory of the modeling tool.</p><h4><br class="atl-forced-newline" /><strong>Step</strong> <strong>#2:</strong> <strong>Write</strong> <strong>a plugin</strong> <strong>code</strong></h4><p>The plugin must contain at least one class derived from the <em>com.nomagic.magicdraw.plugins.Plugin</em> class.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c123c8e2-6dac-4853-90a4-0c0609196328"><ac:parameter ac:name="language">java</ac:parameter><ac:plain-text-body><![CDATA[package myplugin;
import com.nomagic.magicdraw.plugins.Plugin;
import javax.swing.*;
public class MyPlugin extends Plugin
{
    @Override
    public void init()
    {
        JOptionPane.showMessageDialog(null, "My Plugin init");
    }
    @Override
    public boolean close()
    {
        JOptionPane.showMessageDialog( null, "My Plugin close"); 
        return true;
    }
    @Override
    public boolean isSupported()
    {
        //plugin can check here for specific conditions
        //if false is returned plugin is not loaded.
        return true;
    }
}

]]></ac:plain-text-body></ac:structured-macro><p>This plugin shows the one message when it is initialized, and another message when it is closed.</p><h4><strong>Step #3: Compile and pack the plugin to a <em>.jar</em> file </strong></h4><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="385a8e42-7013-49ba-a45a-6987c7292678"><ac:rich-text-body><p><span>For more information on the classpath specification details, see <ac:link><ri:page ri:content-title="Compilation classpath" ri:space-key="DEVG2024xR3" /><ac:plain-text-link-body><![CDATA[Classpath]]></ac:plain-text-link-body></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p>The compiled code must be packed to a <em>.jar</em> file.</p><p>To create a .jar file, use a jar command in the plugins directory:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="88154e09-3d7e-4879-8b3d-0aa3d34d8672"><ac:parameter ac:name="language">bash</ac:parameter><ac:plain-text-body><![CDATA[ jar -cf myplugin.jar myplugin/*.class]]></ac:plain-text-body></ac:structured-macro><h4><strong>Step #4: Write a plugin descriptor</strong></h4><p>The plugin descriptor is a file named<em> plugin.xml</em>. This file should be placed in the <em>myplugin</em> folder.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8026d05b-3932-4e9a-800e-4ac970f3f541"><ac:parameter ac:name="language">xml</ac:parameter><ac:plain-text-body><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<plugin id="my.first.plugin" name="My First Plugin" version="1.0" provider-name="Coder" class="myplugin.MyPlugin"> 
    <requires>
        <api version="1.0"/>
    </requires> 
    <runtime>
        <library name="myplugin.jar"/>
    </runtime>
</plugin>]]></ac:plain-text-body></ac:structured-macro><p>For detailed information about the plugin descriptor, see <ac:link><ri:page ri:content-title="Plugin descriptor" ri:space-key="DEVG2024xR3" /></ac:link>.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8f28f0cc-f589-4636-9cbc-3542147b42a9"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Compilation classpath" ri:space-key="DEVG2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Plugin descriptor" ri:space-key="DEVG2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
