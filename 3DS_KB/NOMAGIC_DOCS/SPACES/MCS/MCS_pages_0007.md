# NOMAGIC DOCUMENTATION SPACE: Server-Side Collaboration

<!--NOMAGIC_SPACE key=MCS chunk=7 -->

<!--NOMAGIC_PAGE id=247046882 space=MCS version=2 -->
## PAGE 00858: Users application structure

- page_id: `247046882`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046882/Users+application+structure
- version_number: 2
- version_date: `2025-08-12T13:45:42.118+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The **Users application** contains a list of all users and user groups. Information about them includes usernames (or group names), full names, last activity, and login status (**Enable** or **Disable**).

Only a user with a User Manager role can create a new user and/or change a user's password.

Only authorized users can view all users in the Teamwork Cloud system. There are individual users and user groups in Teamwork Cloud, which are classified as external/internal users and external/internal user groups. External users or user groups are imported from external LDAP servers. Internal users or user groups are created in Teamwork Cloud. You can learn more about internal and external users in the section [Managing users](https://docs.nomagic.com/display/MCS/Managing+users), and internal and external user groups in the section [CONFLUENCE_PAGE title='Managing user groups' space='MCS'].

To open Users application

- Click [ATTACHMENT filename='plugins.png'] and select Users application.

[IMAGE alt='' src='']

###### Users application structure.

The table below describes the UI components in the **User**application.

| UI Components | Description |
| --- | --- |
| App bar | >]]> |
| User/User group search bar | The textbox allows you to search for a user/user group by username or keyword. You can type any alphabetic character, numeric value, or symbol (such as @, &, or #), or a combination of them in the search box. The search is not case-sensitive. By default, the search result will return all usernames that match the keyword or letter(s) entered and display them on the page. |
| User/User group filters | The left side menu filters internal and external users/groups. Numbers next to each filter name show how many internal/external users/user groups there are. Internal users/groups can be distinguished from external users/groups by different icons: - Internal users - External users - Internal groups - External groupsYou can also opt in to in the user list. |
| Name column | This column shows a username or group name. You can sort internal and external users by clicking this column name (). Users will be sorted alphabetically ascending/descending. >]]> |
| Full Name or Description column | This column shows the full name of a user. When creating a new user, you may type the full name or leave it blank (optional). If it is a group, you can add a short group description. |
| Last Activity Date column | This column shows the time and date of the user's last activity on Teamwork Cloud. The time-date format is DD/MM/YYYY HH:MM. This data appears only for users and will not be shown when viewing group information. Internal and external users can be sorted by clicking this column name (). Users will be sorted by the last activity date ascending/descending. However, groups cannot be sorted. >]]> |
| Content pane | Different user colors show the user status in Teamwork Cloud Admin:A grey-colored user indicates that the user is disabled and not allowed to log into Teamwork Cloud Admin and Teamwork Cloud in MagicDraw. A black-colored user indicates that the user is enabled and they can use their user account (username and password) to log into Teamwork Cloud Admin.>]]> |
| User/User group activity button | The drop-down menu allows you to edit user information and change user login access (enable or disable). |
| Add button | The Add button opens the Create User/Group pane, which allows you to create a new user/group. See for more information. |

##### User group

A user group gathers multiple users and gives the same role assignments to the users in the same group. When you create a user group and assign role assignments (including the scope), you assign them to all of the members in the user group. You can update information and delete a user group. You can also[CONFLUENCE_PAGE title='Importing users and groups' space='MCS']a user group from an LDAP server as an external user group. All members of the user group will be imported to Teamwork Cloud as external users as well. To update the information for an external user group in Teamwork Cloud, you must resynchronize it with that of the LDAP server.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong>Users application</strong> contains a list of all users and user groups. Information about them includes usernames (or group names), full names, last activity, and login status (<strong>Enable</strong> or <strong>Disable</strong>).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0fd1b6f5-c566-47cd-b69e-9f2ed7eefb22"><ac:rich-text-body><p>Only <span style="color: rgb(62,63,64);">a user with a User Manager role</span> can create a new user and/or change a user's password.</p></ac:rich-text-body></ac:structured-macro><p>Only authorized users can view all users in the Teamwork Cloud system. There are individual users and user groups in Teamwork Cloud, which are classified as external/internal users and external/internal user groups. External users or user groups are imported from external LDAP servers. Internal users or user groups are created in Teamwork Cloud. You can learn more about internal and external users in the section <a href="https://docs.nomagic.com/display/MCS/Managing+users">Managing users</a>, and internal and external user groups in the section <ac:link><ri:page ri:space-key="MCS" ri:content-title="Managing user groups" /></ac:link>.</p><p><br /></p><p>To open Users application </p><hr /><ul><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="plugins.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image> and select <strong>Users</strong> application.</li></ul><p><br /></p><p><ac:image><ri:attachment ri:filename="Users_app_structure.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Users application structure.</h6><p>The table below describes the UI components in the <strong>User </strong>application.<br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><table class="relative-table" style="width: 97.6153%;"><colgroup class=""><col class="" style="width: 18.6634%;" /><col class="" style="width: 81.3366%;" /></colgroup><tbody class="" style="margin-left: 30.0px;"><tr class="" style="margin-left: 30.0px;"><th><strong>UI Components</strong></th><th><strong>Description</strong></th></tr><tr class="" style="margin-left: 30.0px;"><td><strong>App bar</strong></td><td><ac:link><ri:page ri:space-key="MCS" ri:content-title="Using the app bar" /><ac:plain-text-link-body><![CDATA[Learn more about app bar here >>]]></ac:plain-text-link-body></ac:link></td></tr><tr class="" style="margin-left: 30.0px;"><td><strong>User/User group search bar</strong></td><td>The textbox allows you to search for a user/user group by username or keyword. You can type any alphabetic character, numeric value, or symbol (such as @, &amp;, or #), or a combination of them in the search box. The search is not case-sensitive. By default, the search result will return all usernames that match the keyword or letter(s) entered and display them on the page.</td></tr><tr class="" style="margin-left: 30.0px;"><td><div class="content-wrapper"><p><strong>User/User group filters</strong></p></div></td><td><div class="content-wrapper"><p>The left side menu filters internal and external users/groups. Numbers next to each filter name show how many internal/external users/user groups there are. <span>Internal users/groups can be distinguished from external users/groups by different icons:</span></p><p><ac:image><ri:attachment ri:filename="Internal_user.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image> - Internal users</p><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="External_user.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image> - External users</p><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="Internal_groups.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image> - Internal groups</p><p><ac:image ac:thumbnail="true" ac:height="19"><ri:attachment ri:filename="External_groups.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image> - External groups</p><p>You can also opt in to <ac:link><ri:page ri:space-key="MCS" ri:content-title="Displaying disabled users" /><ac:plain-text-link-body><![CDATA[display disabled users]]></ac:plain-text-link-body></ac:link> in the user list.</p></div></td></tr><tr class="" style="margin-left: 30.0px;"><td><strong>Name column</strong></td><td><div class="content-wrapper"><p>This column shows a username or group name. You can sort internal and external users by clicking this column name (<ac:image><ri:attachment ri:filename="sorting.PNG"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image>). Users will be sorted alphabetically ascending/descending. <ac:link><ri:page ri:space-key="MCS" ri:content-title="Sorting users and user groups" /><ac:plain-text-link-body><![CDATA[Learn more about sorting users and groups here >>]]></ac:plain-text-link-body></ac:link></p></div></td></tr><tr class="" style="margin-left: 30.0px;"><td><strong>Full Name or Description column</strong></td><td>This column shows <span>the full name of a user</span>. When creating a new user, you may type the full name or leave it blank (optional). If it is a group, you can add a short group description.</td></tr><tr class="" style="margin-left: 30.0px;"><td><strong>Last Activity Date column</strong></td><td><div class="content-wrapper"><p>This column shows the time and date of the user's last activity on Teamwork Cloud. The time-date format is <strong>DD/MM/YYYY HH:MM</strong>. This data <span>appears only for users and will not be shown when viewing group information. <span>Internal and external users can be sorted by clicking this column name (<ac:image><ri:attachment ri:filename="sort_last_activity.PNG"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image>)</span><span>. Users will be sorted by the last activity date ascending/descending. However, groups cannot be sorted. <ac:link><ri:page ri:space-key="MCS" ri:content-title="Sorting users and user groups" /><ac:plain-text-link-body><![CDATA[Learn more about sorting users and groups here >>]]></ac:plain-text-link-body></ac:link></span></span></p></div></td></tr><tr class="" style="margin-left: 30.0px;"><td><div class="content-wrapper"><p><strong>Content pane</strong></p><p><ac:image><ri:attachment ri:filename="User_status.PNG"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image></p></div></td><td><div class="content-wrapper"><p>Different user colors show the user status in Teamwork Cloud Admin:</p><ul><li><span>A grey-colored user indicates that the user is disabled and not allowed to log into Teamwork Cloud Admin and Teamwork Cloud in MagicDraw. </span></li><li>A black-colored user indicates that the user is enabled and they can use their user account (username and password) to log into Teamwork Cloud Admin.</li></ul><p><ac:link><ri:page ri:space-key="MCS" ri:content-title="Enabling and disabling users" /><ac:plain-text-link-body><![CDATA[Learn more about enabling and disabling users here >>]]></ac:plain-text-link-body></ac:link></p></div></td></tr><tr class="" style="margin-left: 30.0px;"><td><div class="content-wrapper"><p><strong>User/User group activity button</strong></p><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image></p></div></td><td><div class="content-wrapper"><p>The drop-down menu allows you to edit user information and change user login access (enable or disable).</p></div></td></tr><tr class="" style="margin-left: 30.0px;"><td><div class="content-wrapper"><p><strong>Add button</strong></p><p><ac:image ac:thumbnail="true" ac:width="38"><ri:attachment ri:filename="Action_button.png"><ri:page ri:space-key="MCS" ri:content-title="Users application structure" /></ri:attachment></ac:image></p></div></td><td><p><span>The </span><strong>Add</strong><span> button opens the <strong>Create User/Group </strong>pane, which allows you to create a new user/group. See <ac:link><ri:page ri:space-key="MCS" ri:content-title="Managing user groups" /></ac:link> for more information.</span></p></td></tr></tbody></table><h3>User group</h3><p><span style="color: rgb(62,63,64);">A user group gathers multiple users and gives the same role assignments to the users in the same group. When you create a user group and assign role assignments (including the scope), you assign them to all of the members in the user group. You can update information and delete a user group. You can also </span><ac:link><ri:page ri:space-key="MCS" ri:content-title="Importing users and groups" /><ac:plain-text-link-body><![CDATA[import]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"> a user group from an LDAP server as an external user group. All members of the user group will be imported to Teamwork Cloud as external users as well. To update the information for an external user group in Teamwork Cloud, you must resynchronize it with that of the LDAP server. </span></p>
````

<!--NOMAGIC_PAGE id=247047658 space=MCS version=1 -->
## PAGE 00859: Using a custom template in a model

- page_id: `247047658`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047658/Using+a+custom+template+in+a+model
- version_number: 1
- version_date: `2025-08-11T16:48:42.623+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents > Document templates > Working with custom document templates
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The appearance and content of a published model can be customized by applying a custom template. Creating custom templates allows you to define which elements of your model are displayed on the web, and how the data of these elements is represented. If a custom template is created as a separate .mdzip file, you can apply it to multiple models. In order to apply such a template for publishing, you need to use it in the model you intend to publish. This page describes how to accomplish this task.

To use a custom template in a model

1. Do one of the following:
  - From the File menu, select Use Project > Use Local Project .
  - From Options menu, select Project Usages and click the Use Project button.
2. In the open Use Project wizard, select a project to use From file system .
3. Near the Project file box, click [IMAGE alt='' src=''] .
4. In the open dialog, navigate to the directory in which you store your custom template, and select it.
5. Click the Open button.
6. In the Use Project wizard, click the Next button to specify project usage options.
7. In the Accessibility area of the wizard, select the Read-write option.
8. Click the Finish button.

Now that the template is used in your model, you can apply it when publishing the model on the web.Note that you can modify your custom template both before and after using it in a model. If you want to avoid changing the template after using it, skip steps 6 and 7 in the custom template usage procedure described above.

For more information about using projects see [CONFLUENCE_PAGE title='Using other projects in a project' space='MD185'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The appearance and content of a published model can be customized by applying a custom template. Creating custom templates allows you to define which elements of your model are displayed on the web, and how the data of these elements is represented. If a custom template is created as a separate .mdzip file, you can apply it to multiple models. <span>In order to apply such a template for publishing, you need to use it in the model you intend to publish. This page describes how to accomplish this task</span>.</p><p><br /></p><p>To use a custom template in a model</p><p><br /></p><hr /><ol><li>Do one of the following:<br /><ul><li>From the <strong>File</strong> menu, select <strong>Use Project</strong> &gt; <strong>Use Local Project</strong>.</li><li>From <strong>Options</strong> menu, select <strong>Project Usages</strong> and click the <strong>Use Project</strong> button.</li></ul></li><li>In the open <strong>Use Project</strong> wizard, select a project to use <strong>From file system</strong>.</li><li>Near the <strong>Project file</strong> box, click <span class="confluence-embedded-file-wrapper"> <ac:image><ri:attachment ri:filename="select_project_button.png"><ri:page ri:space-key="MCS" ri:content-title="Using a custom template in a model" /></ri:attachment></ac:image> </span>.</li><li><p>In the open dialog, navigate to the directory in which you store your custom template, and select it.</p></li><li>Click the <strong>Open</strong> button.</li><li>In the<strong> Use Project</strong> wizard, click the <strong>Next</strong> button to specify project usage options.</li><li>In the <strong>Accessibility</strong> area of the wizard, select the <strong>Read-write</strong> option.</li><li>Click the <strong>Finish</strong> button.<br /><br /><br /></li></ol><p><span class="confluence-embedded-file-wrapper">Now that the template is used in your model, you can apply it when publishing the model on the web. </span>Note that you can modify your custom template both before and after using it in a model. If you want to avoid changing the template after using it, skip steps 6 and 7 in the custom template usage procedure described above.</p><p><span class="confluence-embedded-file-wrapper">For more information about using projects see <ac:link><ri:page ri:space-key="MD185" ri:content-title="Using other projects in a project" /></ac:link>.</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=247047997 space=MCS version=1 -->
## PAGE 00860: Using document information in the page header

- page_id: `247047997`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047997/Using+document+information+in+the+page+header
- version_number: 1
- version_date: `2025-08-11T16:48:50.276+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Sharing and exporting > Customizing PDF/HTML templates
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

By default, the page headers of exported documents are empty. If you want specific information to be displayed in the page header, you need to add it to the *<template_folder>/common/header.html*file.

The page header can also display document information. You should check API for specific pieces of information that are accessible for usage in the page header.

##### Example of adding a document name to the page header

Let’s say you want a document name displayed in the center of the page header with some space around it.

To use a document name in the page header

1. Open the <template_folder>/common/header.html file.
2. Find the header tag.
3. Add <div th:text="${[documentInfo.name](http://documentInfo.name)}"></div> .
4. To make the document name centered, do one of the following:
  - Add an inline style.
  - Change the header class CSS properties in the <template_folder/common/styles.html file.
  - Add a new <style> tag in the *header.html* file and make the same changes you would in any other HTML document. Example of a header tag when using inline styling]]>

After completing the steps above, the exported document will have its name displayed in the page header.

[IMAGE alt='' src='']

###### A sample document with the *Image template* document name displayed in the page header.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>By default, the page headers of exported documents are empty. If you want specific information to be displayed in the page header, you need to add it to the <em>&lt;template_folder&gt;/common/header.html </em>file.</p><p>The page header can also display document information. You should check API for specific pieces of information that are accessible for usage in the page header.</p><h3><br />Example of adding a document name to the page header</h3><p>Let’s say you want a document name displayed in the center of the page header with some space around it.</p><p><br /></p><p>To use a document name in the page header</p><hr /><ol><li>Open the <em>&lt;template_folder&gt;/common/header.html</em> file.</li><li>Find the <em>header</em> tag.</li><li>Add <em>&lt;div th:text=&quot;${<a href="http://documentInfo.name">documentInfo.name</a>}&quot;&gt;&lt;/div&gt;</em>.</li><li>To make the document name centered, do one of the following:<ul><li>Add an inline style.</li><li>Change the <em>header</em> class CSS properties in the <em>&lt;template_folder/common/styles.html</em> file.</li><li><p class="auto-cursor-target">Add a new &lt;style&gt; tag in the <em>header.html</em> file and make the same changes you would in any other HTML document.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2e9e1a32-c458-448e-86c5-65e27b7e414f"><ac:parameter ac:name="title">Example of a header tag when using inline styling</ac:parameter><ac:plain-text-body><![CDATA[<header class="header">
   <div th:text="${documentInfo.name}" style="text-align: center; padding: 20px;"></div>
</header>]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li></ol><p>After completing the steps above, the exported document will have its name displayed in the page header.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="adding_document_info_to_header.png"><ri:page ri:space-key="MCS" ri:content-title="Using document information in the page header" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A sample document with the <em>Image template</em> document name displayed in the page header.</h6>
````

<!--NOMAGIC_PAGE id=247046860 space=MCS version=1 -->
## PAGE 00861: Using the app bar

- page_id: `247046860`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046860/Using+the+app+bar
- version_number: 1
- version_date: `2025-08-11T16:48:27.564+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Understanding the user interface
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The app bar allows you to navigate the Teamwork Cloud Admin functionality easily. The app bar is located on the upper right of the web app portal. You can perform the following actions from the app bar:

| App bar icon | Icon description |
| --- | --- |
| Search bar | You can use this search box to find a username by typing a keyword. Teamwork Cloud Admin will run the search and find matching usernames. |
|  | Click and select an application to open it (, , , , etc.). |
|  | Click and select Sign out to sign out of the current user account. |
|  | Click and select one of the following:Help - to open the web app documentationAbout - to view the web app information, such as the version number and copyright information. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The app bar allows you to navigate the Teamwork Cloud Admin functionality easily. The app bar is located on the <span style="color: rgb(33,33,33);">upper right</span> of the web app portal. You can perform the following actions from the app bar:</p><table><colgroup><col /><col /></colgroup><tbody><tr><th><span>App bar icon</span></th><th>Icon description</th></tr><tr><td colspan="1"><div class="content-wrapper"><strong>Search bar</strong></div></td><td colspan="1">You can use this search box to find a username by typing a keyword. Teamwork Cloud Admin will run the search and find matching usernames.</td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="plugins.png"><ri:page ri:space-key="MCS" ri:content-title="Using the app bar" /></ri:attachment></ac:image></p></div></td><td>Click and select an application to open it (<ac:link><ri:page ri:space-key="MCS" ri:content-title="Resources application" /><ac:plain-text-link-body><![CDATA[Resources]]></ac:plain-text-link-body></ac:link>, <ac:inline-comment-marker ac:ref="db8628e8-893c-4388-a2a5-4de93572f9d9"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Users application" /><ac:plain-text-link-body><![CDATA[Users]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker>, <ac:link><ri:page ri:space-key="MCS" ri:content-title="Roles application" /><ac:plain-text-link-body><![CDATA[Roles]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:space-key="MCS" ri:content-title="Settings application" /><ac:plain-text-link-body><![CDATA[Settings]]></ac:plain-text-link-body></ac:link>, etc.).</td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="sign_out.png"><ri:page ri:space-key="MCS" ri:content-title="Using the app bar" /></ri:attachment></ac:image></p></div></td><td><p>Click and select <strong>Sign out</strong> to sign out of the current user account.</p></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper image-center-wrapper"><ac:image ac:align="center"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="MCS" ri:content-title="Using the app bar" /></ri:attachment></ac:image></span></p></div></td><td colspan="1"><p>Click and select one of the following:</p><ul><li><strong>Help</strong> - to open the web app documentation</li><li><strong>About</strong> - to view the web app information, such as the version number and copyright information.</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=247046487 space=MCS version=5 -->
## PAGE 00862: Using the installer file on Windows

- page_id: `247046487`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046487/Using+the+installer+file+on+Windows
- version_number: 5
- version_date: `2025-12-03T14:19:42.125+01:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > Deployment Guide > Installation > Installation on Windows > Installing services on Windows
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The installer file includes both Magic Collaboration Studio / Teamwork Cloudand Web Application Platform with its services in its installation package.

#### WARNING: Warning

Warning

If the installation path contains any of the following characters, like '[', ']', '(', ')', '!', '@', '#', '$', '#', '%', '{', '}', '+', '=', or ';' the installation procedure cannot be completed successfully and the login page will not load. If, for example, the installation path is *C:\Program Files\TeamworkCloud*, which does not contain any of the special characters, the installation will not fail.

****

To install the product by using the installer file on Windows

1. [CONFLUENCE_PAGE title='Downloading installation files' space='IL']Download the <*product_name>_<version_number>_installer_win64.exe* file .
2. Run the installer file as administrator to start the installation wizard.
3. Read the installation introduction and click **Next**.
4. Select the Advanced Install radio button and click Next .
5. Select the components you want to install and click **Next**. We recommend installing Web Application Platform and Magic Collaboration Studio / Teamwork Cloudon different machines for better performance. If you decide to install Web Application Platform on a separate machine, clear the appropriate checkbox. [IMAGE alt='' src='']
6. Follow the on-screen instructions in the installation wizard and click Next after each step.
7. When the Pre-Installation Summary is displayed, check if all properties are specified correctly and click**Install**. 
 
[IMAGE alt='' src='']
8. After successful installation, click **Done** to close the installation wizard.
9. Open the Task Manager and start the following services:
  - Teamwork Cloud service
  - Zookeeper service
  - WebApp service
10. Wait a few minutes until all services have started, then check if the system is working. You should be able to access Magic Collaboration Studio / Teamwork Cloud via https://FQDN:8443/webapp/ .After completing the steps above, you can [CONFLUENCE_PAGE title='Starting services on Windows' space=''] .

##### Post-installation configuration (optional)

The installer created a preliminary configuration. If your system is still not operational, you may need to configure the following parameters manually.

- Edit the configuration file <install_root> \TeamworkCloud\configuration\application.conf . Search for contact-points = , located under the persistence esi.persistence. datastax-java-driver section, and replace localhost with ip_address_of_cassandra_node . Search for url = , located in the esi.auth section. Enter your server’s IP address or FQDN (if accessing via FQDN), for example, [https://127.0.0.1:8443](https://127.0.0.1:8443) .
- If you are accessing Magic Collaboration Studio / Teamwork CloudWeb UI via its FQDN:
  - Edit the configuration file <install_root> \ WebAppPlatform\shared\conf\authserver.properties . Search for authentication.redirect.uri.whitelist and append the following to the entry: https://FQDN:8443/webapp/
  - Edit the configuration file <install_root> \WebAppPlatform\shared\conf\webappplatform.properties. Add server.public.host and set it to FQDN.
- Edit the configuration file for Teamwork Cloud Admin: *<install_root>**\WebAppPlatform\shared\conf\webappplatform.properties*.
  - twc.admin.username - Set it to the username of a local account with Administrator privileges (default is Administrator).
  - twc.admin.password - Set it to the password corresponding to the Administrator user (default is Administrator).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The installer file includes both <span>Magic Collaboration Studio / Teamwork Cloud </span>and Web Application Platform with its services in its installation package.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1452eb56-3a9d-4c11-9641-55b49874337a"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>If the installation path contains any of the following characters, like '[', ']', '(', ')', '!', '@', '#', '$', '#', '%', '{', '}', '+', '=', or ';' the installation procedure cannot be completed successfully and the login page will not load. If, for example, the installation path is <em>C:\Program Files\TeamworkCloud</em>, which does not contain any of the special characters, the installation will not fail.</p></ac:rich-text-body></ac:structured-macro><p><strong><span style="color:var(--ds-text,#000000);"> </span></strong></p><p><span style="color:var(--ds-text,#000000);">To install the product by using the installer file on Windows</span></p><hr /><ol><li><ac:link><ri:page ri:space-key="IL" ri:content-title="Downloading installation files" /><ac:link-body>Download the &lt;<em>product_name&gt;_&lt;version_number&gt;_installer_win64.exe</em> file</ac:link-body></ac:link>.</li><li><span style="color:var(--ds-text,#333333);">Run the installer file as administrator to start the installation wizard.</span></li><li><span style="color:var(--ds-text,#333333);">Read the installation introduction and click <strong>Next</strong>.</span></li><li>Select the <strong>Advanced Install</strong> radio button and click <strong>Next</strong>.</li><li><p>Select the components you want to install and click <strong>Next</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d751e7b5-13c8-45f1-8635-4da6e0fac5b9"><ac:rich-text-body><p>We recommend installing Web Application Platform and <span>Magic Collaboration Studio / Teamwork Cloud </span>on different machines for better performance. If you decide to install Web Application Platform on a separate machine, clear the appropriate checkbox.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="selecting_install_components.png" /></ac:image><br /><br /></p></li><li>Follow the on-screen instructions in the installation wizard and click<span> </span><strong>Next</strong><span> </span>after each step.</li><li><p class="auto-cursor-target">When the Pre-Installation Summary is displayed, check if all properties are specified correctly and click<span> </span><strong>Install</strong>.<br /><br /><ac:image><ri:attachment ri:filename="twc_pre-installation-summary.png" /></ac:image><br /><br /></p></li><li><p>After successful installation, click <strong>Done</strong> to close the installation wizard.</p></li><li><p>Open the Task Manager and start the following services:</p><ul><li>Teamwork Cloud service</li><li>Zookeeper service</li><li><p class="auto-cursor-target">WebApp service</p></li></ul></li><li>Wait a few minutes until all services have started, then check if the system is working. You should be able to access <span>Magic Collaboration Studio / Teamwork Cloud </span>via <a href="https://fqdn:8443/webapp/">https://FQDN:8443/webapp/</a>.After completing the steps above, you can <ac:link><ri:page ri:content-title="Starting services on Windows" /><ac:plain-text-link-body><![CDATA[start the product on Windows]]></ac:plain-text-link-body></ac:link>.</li></ol><h3>Post-installation configuration (optional)</h3><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c928b67a-2bcf-46e3-916c-4eba93640265"><ac:rich-text-body><p>The installer created a preliminary configuration. If your system is still not operational, you may need to configure the following parameters manually.</p></ac:rich-text-body></ac:structured-macro><ul><li>Edit the configuration file <em>&lt;install_root&gt;</em><em>\TeamworkCloud\configuration\application.conf</em>. Search for <strong>contact-points =</strong>, located under the persistence <strong>esi.persistence.</strong><strong>datastax-java-driver</strong> section, and replace <strong>localhost </strong>with <strong>ip_address_of_cassandra_node</strong>. Search for <strong>url =</strong>, located in the <strong>esi.auth</strong> section. Enter your server’s IP address or FQDN (if accessing via FQDN), for example, <em><span class="nolink"><a href="https://127.0.0.1:8443">https://127.0.0.1:8443</a></span></em>.</li><li><p><span style="color:var(--ds-text,#172b4d);">If you are accessing <span>Magic Collaboration Studio / Teamwork Cloud </span>Web UI via its FQDN:</span></p><ul><li>Edit the configuration file<span> </span><em>&lt;install_root&gt;</em>\<em>WebAppPlatform\shared\conf\authserver.properties</em>. Search for <strong>authentication.redirect.uri.whitelist</strong> and append the following to the entry: <a class="external-link" href="https://fqdn:8443/webapp/" title="Follow link">https://FQDN:8443/webapp/</a></li><li>Edit the configuration file<em> </em><em>&lt;install_root&gt;</em><em>\WebAppPlatform\shared\conf\webappplatform.properties.</em><span> </span>Add<span> </span><strong>server.public.host</strong><span> </span>and set it to FQDN.</li></ul></li><li><p class="auto-cursor-target">Edit the configuration file for Teamwork Cloud Admin: <em>&lt;install_root&gt;</em><em>\WebAppPlatform\shared\conf\webappplatform.properties</em>.</p><ul><li><strong>twc.admin.username</strong> - Set it to the username of a local account with Administrator privileges (default is Administrator).</li><li><strong>twc.admin.password</strong> - Set it to the password corresponding to the Administrator user (default is Administrator).</li></ul></li></ul>
````

<!--NOMAGIC_PAGE id=247048401 space=MCS version=1 -->
## PAGE 00863: Versions of Magic Collaboration Studio / Teamwork Cloud and Services

- page_id: `247048401`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247048401/Versions+of+Magic+Collaboration+Studio+Teamwork+Cloud+and+Services
- version_number: 1
- version_date: `2025-08-11T18:58:33.167+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

28cef3f74fe25ef77f51a8bab329f01f

Magic Collaboration Studio / Teamwork Cloud and Services

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="3572a9d0-a9ff-42e4-9dfa-2428f83acc5e"><ac:parameter ac:name="permaId">28cef3f74fe25ef77f51a8bab329f01f</ac:parameter><ac:parameter ac:name="documentTitle">Magic Collaboration Studio / Teamwork Cloud and Services</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=247047491 space=MCS version=3 -->
## PAGE 00864: Viewing and editing resource details

- page_id: `247047491`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047491/Viewing+and+editing+resource+details
- version_number: 3
- version_date: `2025-09-16T11:11:03.342+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Resources application > Working with resources
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

##### Viewing resource details

In the Resources app you can view the following resource information:

- Resource details, including the resource name, creation and last modification dates, and the user who created or modified the resource.
- Resource history information, including the user who created each version of the resource, the version creation date, and the type of changes that were made.
- The roles assigned to the resource.
- Resource branches.

To view resource details

1. In the Resources application, click the category where the relevant resource is located .
2. Click [ATTACHMENT filename='menu.png'] next to the resource and select Resource details .

Resource details, such as category, creation date, and last modification date, are shown on the **Resource** pane on the right side of the screen.

[IMAGE alt='' src='']

###### Viewing resource details, history, and other information.

##### Editing resource details

You can edit a resource name and description or move the resource to another category, as described below.

To edit resource details

1. Open the Resources application and go to the category where the relevant resource is located.
2. Click [ATTACHMENT filename='menu.png'] next to the resource with the details you want to edit and select Resource details.
3. To edit resource details,, click Edit on the bottom of the Resource details pane.
4. You can:
  - Change the resource name in the Resource name field.
  - Change or add a resource description in the Description field.
5. Click [ATTACHMENT filename='save_button.jpg'] on the top right corner of the Edit resource details pane to save resource details.

When you get a confirmation message, it means the resource details are successfully updated.

##### Setting resource classification

Resource classification that you set through data markings allows you to control access to that resource. To set resource classification, [CONFLUENCE_PAGE title='Managing data markings in Teamwork Cloud Admin' space=''] in the Settings app and ensure you have [sufficient permissions](https://docs.nomagic.com/display/MCS/Permissions).

To set resource classification

1. Open the Resources application and go to the category where the relevant resource is located.
2. Click [ATTACHMENT filename='menu.png'] next to the resource and select Set data markings.
3. In the window that opens, select the desired data marking.
4. Click Set to set the selected data marking.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3 style="color:var(--ds-text,#172b4d);">Viewing resource details</h3><p>In the Resources app you can view the following resource information:</p><ul><li>Resource details, including the resource name, creation and last modification dates, and the user who created or modified the resource.</li><li>Resource history information, including the user who created each version of the resource, the version creation date, and the type of changes that were made.</li><li>The roles assigned to the resource.</li><li>Resource branches.</li></ul><p><br /></p><p>To view resource details</p><hr /><ol><li>In the Resources application, <span style="color:var(--ds-text,#172b4d);">click the category where the relevant resource is located</span>.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource and select <strong>Resource details</strong>.</li></ol><p><br />Resource details, such as category, creation date, and last modification date, are shown on the <strong>Resource</strong> pane on the right side of the screen.</p><p style="text-align: center;"><br /><ac:image><ri:attachment ri:filename="resource_details_pane.png" /></ac:image></p><h6 style="text-align: center;line-height: 1.66667;letter-spacing: normal;">Viewing resource details, history, and other information.</h6><h3 style="color:var(--ds-text,#172b4d);">Editing resource details</h3><p>You can edit a resource name and description or move the resource to another category, as described below.</p><p><br /></p><p>To edit resource details</p><hr /><ol><li>Open the Resources application and go to the category where the relevant resource is located.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource with the details you want to edit and select <strong style="letter-spacing: 0.0px;">Resource details.</strong></li><li>To edit resource details,, click <strong>Edit</strong> on the bottom of the <strong>Resource details</strong> pane.</li><li>You can:<ul><li>Change the resource name in the <strong style="letter-spacing: 0.0px;">Resource name</strong><span style="letter-spacing: 0.0px;"> field.</span></li><li>Change or add a resource description in the <strong>Description</strong> field.</li></ul></li><li>Click <ac:image ac:thumbnail="true" ac:width="32"><ri:attachment ri:filename="save_button.jpg" /></ac:image> on the top right corner of the <strong>Edit resource details</strong> pane to save resource details.</li></ol><p><br />When you get a confirmation message, it means the resource details are successfully updated.</p><h3 style="color:var(--ds-text,#172b4d);">Setting resource classification</h3><p>Resource classification that you set through data markings allows you to control access to that resource. To set resource classification, <ac:link><ri:page ri:content-title="Managing data markings in Teamwork Cloud Admin" /><ac:plain-text-link-body><![CDATA[enable data markings]]></ac:plain-text-link-body></ac:link> in the Settings app and ensure you have <a href="https://docs.nomagic.com/display/MCS/Permissions">sufficient permissions</a>.</p><p>To set resource classification</p><hr /><ol><li>Open the Resources application and go to the category where the relevant resource is located.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource and select <strong>Set data markings.</strong></li><li>In the window that opens, select the desired data marking.</li><li>Click <strong>Set</strong> to set the selected data marking. </li></ol>
````

<!--NOMAGIC_PAGE id=247047534 space=MCS version=1 -->
## PAGE 00865: Viewing resource history

- page_id: `247047534`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047534/Viewing+resource+history
- version_number: 1
- version_date: `2025-08-11T16:48:40.171+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Resources application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

**History**allows you to track changes made to the project. The History card displays basic information, such as versions, contributors, and branches of each modification, while the visual representation of history provides a full-screen comprehensive viewof the project's evolution over time.

To view resource history

1. Go to the Resources application.
2. Do one of the following:
  - Click [ATTACHMENT filename='menu.png'] on the right side of the resource line and select Resource details . In the open Resource pane, the resource history is displayed on the History card. [ATTACHMENT filename='history.png'] Click**View All**at the bottom of the History card to open the full-screen history view.
  - Click [ATTACHMENT filename='menu.png'] on the right side of the resource line and select Resource history to open the full-screen history view displayed below.

[IMAGE alt='' src='']

###### The full-screen history view.

In the full-screen history view, you can:

- View branch structure, merge and commit information, as well as archived branches that are greyed-out;
- Search for a specific commit, message, or version using the search field at the top.
- [CONFLUENCE_PAGE title='Creating project branches' space='MCS'] .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>History </strong>allows you to track changes made to the project. The History card displays basic information, such as versions, contributors, and branches of each modification, while the visual representation of history provides a full-screen <span style="color: rgb(23,43,77);">comprehensive view </span>of the project's evolution over time.</p><p><br /></p><p>To view resource history</p><hr /><ol><li>Go to the <strong>Resources</strong> application.</li><li>Do one of the following:<ul><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource history" /></ri:attachment></ac:image> on the right side of the resource line and select <strong>Resource details</strong>. In the open <strong>Resource</strong> pane, the resource history is displayed on the <strong>History </strong>card.<br /><br /><ac:image ac:border="true" ac:height="436" ac:width="393"><ri:attachment ri:filename="history.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource history" /></ri:attachment></ac:image><br /><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="94cc92be-99b6-450a-ae18-d265f70b5cb6"><ac:rich-text-body>Click<strong> View All </strong><span>at the bottom of the History card to open the full-screen history view.</span></ac:rich-text-body></ac:structured-macro></li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource history" /></ri:attachment></ac:image> on the right side of the resource line and select <strong>Resource history</strong> to open the full-screen history view displayed below.<br /><br /><br /></li></ul></li></ol><p><ac:image><ri:attachment ri:filename="branch_visualization.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource history" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The full-screen history view.</h6><p>In the full-screen history view, you can:</p><ul><li><span style="color: rgb(23,43,77);">View branch structure, merge and commit information, as well as archived branches that are greyed-out;</span></li><li>Search<strong> </strong>for a specific commit, message, or version using the search field at the top.</li><li><ac:link><ri:page ri:space-key="MCS" ri:content-title="Creating project branches" /><ac:plain-text-link-body><![CDATA[Create new branches]]></ac:plain-text-link-body></ac:link>.</li></ul>
````

<!--NOMAGIC_PAGE id=247047582 space=MCS version=1 -->
## PAGE 00866: Viewing resource information

- page_id: `247047582`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047582/Viewing+resource+information
- version_number: 1
- version_date: `2025-08-11T16:48:41.013+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Resource Usage Map
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

If you want to view the information of a particular resource in a resource usage map, simply select it to the Resource pane on the right side of the application portal. This pane displays details and usages of the selected resource. Here, you can also find all the resources that use the selected resource in the their latest versions.

The Resource pane has three cards displaying different types of resource information highlighted in the figure below.

[IMAGE alt='' src='']

| Resource details card | The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource. |
| --- | --- |
|  | Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource. |
| Used resources card | After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects. |
| Used by resources card | In the Used by resources card, click the Find all usages button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">If you want to view the information of a particular resource in a resource usage map, simply select it to the Resource pane on the right side of the application portal. This pane displays details and usages of the selected resource. Here, you can also find all the resources that use the selected resource in the their latest versions.</p><p>The Resource pane has three cards displaying different types of resource information highlighted in the figure below.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="resource_pane.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource information" /></ri:attachment></ac:image></p><p><br /></p><table class="relative-table" style="width: 1118.0px;"><colgroup><col /><col /></colgroup><tbody><tr><td style="text-align: left;" colspan="1"><strong>Resource details card</strong></td><td colspan="1">The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource.</td></tr><tr><td style="text-align: left;" colspan="1"><div class="content-wrapper"><p><strong><span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="switch_resource_version.png"><ri:page ri:space-key="MCS" ri:content-title="Viewing resource information" /></ri:attachment></ac:image></span></strong></p></div></td><td colspan="1">Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used resources card</strong></td><td colspan="1">After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used by resources card</strong></td><td colspan="1">In the Used by resources card, click the <strong>Find all usages</strong> button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=247047308 space=MCS version=3 -->
## PAGE 00867: Viewing server license information

- page_id: `247047308`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047308/Viewing+server+license+information
- version_number: 3
- version_date: `2025-10-27T10:25:46.574+01:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

To set and view the server license, select**Server license**in the left-side menu of the Settings application. In the **Server license**page you can:

- [CONFLUENCE_PAGE title='License management' space='']
- 

[IMAGE alt='' src='']

##### Recently active users

The **Recently active users** section shows users who have recently logged in to Teamwork Cloud services, such as Teamwork Cloud Admin or Teamwork Cloud through a modeling tool. These users are either currently logged in or have logged out within the last 20 minutes (approximately).

The **Last activity date**column displays the last time the user performed any action in Teamwork Cloud or Teamwork Cloud Admin.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To set and view the server license, select<span> </span><strong>Server license</strong><span> </span>in the left-side menu of the Settings application. In the <strong>Server license </strong>page you can:</p><ul><li><ac:link><ri:page ri:content-title="License management" /><ac:plain-text-link-body><![CDATA[Manage server licenses]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Recently active users"><ac:plain-text-link-body><![CDATA[View recently active users]]></ac:plain-text-link-body></ac:link></li></ul><p><ac:image ac:border="true" ac:height="559" ac:width="1000"><ri:attachment ri:filename="server_license.png" /></ac:image></p><h3>Recently active users</h3><p>The <strong>Recently active users</strong> section shows users who have recently logged in to Teamwork Cloud services, such as Teamwork Cloud Admin or Teamwork Cloud through a modeling tool. These users <span style="color:var(--ds-text,#333333);">are either currently logged in or have logged out within the last 20 minutes (approximately).</span></p><p>The <strong>Last activity date </strong>column displays the last time the user performed any action in Teamwork Cloud or Teamwork Cloud Admin.</p>
````

<!--NOMAGIC_PAGE id=247047294 space=MCS version=2 -->
## PAGE 00868: Viewing server status

- page_id: `247047294`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047294/Viewing+server+status
- version_number: 2
- version_date: `2025-09-16T11:08:32.916+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Managing server settings
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

##### Viewing server status

The **Server status** table in the Teamwork Cloud Admin **Server settings**section****lists all connected Teamwork Cloud nodes in a cluster. Each server node in the cluster provides the IP address or domain name with port, RAM usage, CPU usage and operating system information. The server nodes are arranged in an ascending numerical order by default. In Linux, the RAM Usage includes RAM allocated to buffers and disk cache, so it is not indicative of the available RAM. For actual available RAM, you can use the monitoring stack, which will provide insight into OS, Cassandra, and Teamwork Cloud metrics.

The **Server Status** table will be automatically updated every 30 seconds. The last update time of the table is shown at the bottom of the table.

###### [IMAGE alt='' src=''] 
The server status and the log files on the Server Settings page.

##### Downloading log files

You can download log files that record all user activities in Teamwork Cloud and Web Application Platform.

To download a log file

1. Go to the Settings application.
2. Select Server Status from the left side menu.
3. Click [ATTACHMENT filename='Download icon.png'] next to Teamwork Cloud or WebApp to download a log file from a specific server node. The file will be downloaded and saved on your computer.

false

A log file downloaded from [IMAGE alt='' src=''] contains recent content with a capacity of 20,000 lines (the maximum size).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3 style="text-align: left;">Viewing server status</h3><p style="text-align: left;">The <strong>Server status</strong> table in the Teamwork Cloud Admin <strong>Server settings </strong>section<strong> </strong>lists all connected Teamwork Cloud nodes in a cluster. Each server node in the cluster provides the IP address or domain name with port, RAM usage, CPU usage and operating system information. The server nodes are arranged in an ascending numerical order by default. In Linux, the RAM Usage includes RAM allocated to buffers and disk cache, so it is not indicative of the available RAM. For actual available RAM, you can use the monitoring stack, which will provide insight into OS, Cassandra, and Teamwork Cloud metrics.</p><p style="text-align: left;">The <strong>Server Status</strong> table will be automatically updated every 30 seconds. The last update time of the table is shown at the bottom of the table.</p><p style="text-align: left;"><br /></p><h6 style="text-align: center;"><ac:image ac:width="900"><ri:attachment ri:filename="server_status_table.jpg" /></ac:image><br /><span style="color:var(--ds-text,#707070);">The server status and the log files on the Server Settings page.<br /><br /></span></h6><h3><span>Downloading log files</span></h3><p>You can download log files that record all user activities in Teamwork Cloud and Web Application Platform.</p><p>To download a log file</p><hr /><ol><li data-uuid="6b07b3c6-ba3d-4ff0-a8aa-19ec2feb959c">Go to the <strong>Settings</strong> application.</li><li data-uuid="49df047a-a66b-49d8-9ddc-d8b6372355d2">Select <strong>Server Status</strong> from the left side menu.</li><li data-uuid="6f7832e2-9e5c-44dd-b039-beaf2ee05ddd">Click <ac:image ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="Download icon.png" /></ac:image> next to Teamwork Cloud or WebApp to download a log file from a specific server node. The file will be downloaded and saved on your computer. <br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="461de44b-2f2b-453e-8e35-00f99f99d18b"><ac:parameter ac:name="icon">false</ac:parameter><ac:rich-text-body><p><span>A log file downloaded from <ac:image ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="Download icon.png" /></ac:image> contains recent content with a capacity of 20,000 lines (the maximum size).</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=247046800 space=MCS version=1 -->
## PAGE 00869: Web Application Platform Administration

- page_id: `247046800`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046800/Web+Application+Platform+Administration
- version_number: 1
- version_date: `2025-08-11T16:47:50.147+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > Administration Guide
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

Web Application Platform is the platform for developing and running web applications. It is also the base for Cameo Collaborator for Teamwork Cloud, Resources, and TWCloud Admin apps.

To learn how to install and use Web Application platform, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Web Application Platform is the platform for developing and running web applications. It is also the base for Cameo Collaborator for Teamwork Cloud, Resources, and TWCloud Admin apps.</p><p>To learn how to install and use Web Application platform, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=247046533 space=MCS version=2 -->
## PAGE 00870: Web Application Platform Installation on a separate machine

- page_id: `247046533`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046533/Web+Application+Platform+Installation+on+a+separate+machine
- version_number: 2
- version_date: `2026-01-16T13:39:40.727+01:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > Deployment Guide > Installation > Advanced installation
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The following chapters will give you step by step instructions on how to install and upgrade Web Application Platform and its services:

#### SCROLL-CONDITIONAL-CONTENT: Important

false

mcs

#### NOTE: Important

Important

When installing Web Application Platform on a separate machine, ensure you use the installation files from the specific Magic Collaboration Studio installation bundle. If you use any other version of files, the licensing system will not function properly, as the Web Application Platform will not be linked to Magic Collaboration Studio license management.

[IMAGE alt='' src='']

###### The conceptual schema of the standard Web Application Platform deployment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following chapters will give you step by step instructions on how to install and upgrade Web Application Platform and its services:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><ac:structured-macro ac:name="scroll-conditional-content" ac:schema-version="1" ac:macro-id="f769784e-2f21-45fc-9ba5-4bed01d5d799"><ac:parameter ac:name="fallback">false</ac:parameter><ac:parameter ac:name="labels">mcs</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f1145c11-8556-4174-abe8-1676b163e985"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p><span data-teams="true">When installing Web Application Platform on a separate machine, ensure you use the installation files from the specific Magic Collaboration Studio installation bundle. If you use any other version of files, the licensing system will not function properly, as the Web Application Platform will not be linked to Magic Collaboration Studio license management.</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><ac:image ac:width="1000"><ri:attachment ri:filename="WAP standard deployment.jpg" /></ac:image></p><h6 style="text-align: center;">The conceptual schema of the standard Web Application Platform deployment.</h6>
````

<!--NOMAGIC_PAGE id=290029625 space=MCS version=4 -->
## PAGE 00871: Web Application Platform services

- page_id: `290029625`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/290029625/Web+Application+Platform+services
- version_number: 4
- version_date: `2026-06-12T10:06:24.799+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > Deployment Guide > Installation > Advanced installation
- labels: ['twc', 'mcs']

### NORMALIZED CONTENT

Wheninstalling Web Application Platform with services, you need to download and extract the *Web_Application_Platform_<version>_war_files.zip*file. It includes the web applications described below.

To speed up server startup and conserve resources, you can remove any unnecessary .war files that are not in use.

| Service | File name | Service description |
| --- | --- | --- |
| Admin Console | admin.war | Service for managing Teamwork Cloud users, roles, and resource assignments. |
| Authentication | authentication.war | Service for authenticating access to Teamwork Cloud. |
| Cameo Collaborator for Teamwork Cloud | collaborator.war | Allows reviewing, editing, and collaborating on Cameo Collaborator documents. |
| Document Exporter | document-exporter.war | Allows exporting Cameo Collaborator documents to PDF and HTML. |
| Oslc | oslc.war | Enables model browsing through OSLC. |
| Reports | reports.war | Allows exporting Teamwork Cloud server-related data to XLSX or CSV. |
| Resource Usage Map | resource-usage-map.war | A service with live visual graph capabilities for representing Teamwork Cloud resource usages. allowing users to identify potential problem areas. |
| Resources | resources.war | The service for managing Teamwork Cloud resources. |
| Simulation | simulation.war | Allows users to simulate Teamwork Cloud projects on the server side. |
| Home page | webapp.war | Home page service. |
| Semantic Graph Index Crawler | sgi-crawler.war | Indexes Teamwork Cloud projects in the Semantic Graph Index of the 3DEXPERIENCE platform to enable CATIA Systems Traceability analysis. |
| SysML v2 API and Services | sysmlv2-api.war | REST/HTTP Platform-specific model (PSM) implementation of the SysML v2 API and Services standard. |
| Element Chooser | element-chooser.war | Allows users to select model elements in a modeling tool using the web UI. |
| MagicLab | magiclab.war | Allows reading SysMLv2 projects on the web. |
| MagicLab Collaborator | magiclab-collaborator.war | Enables collaboration on SysML v2 projects. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);"> When </span>installing Web Application Platform with services, you need to download and e<span style="color:var(--ds-text,#172b4d);">xtract the <em><ac:inline-comment-marker ac:ref="75f2685c-e6fd-41e0-9f49-1bfe34ed9cdd">Web_Application_Platform_&lt;version&gt;_war_files.zip</ac:inline-comment-marker></em><span> </span></span><span style="color:var(--ds-text,#172b4d);">file. It includes the web applications described below.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e5c5e936-6ca2-49f7-a477-8996a0fd8339"><ac:rich-text-body><p><span>To speed up server startup and conserve resources, you can remove any unnecessary .war files that are not in use.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p><table class="wrapped relative-table" style="width: 70.7641%;"><colgroup><col style="width: 29.7027%;" /><col style="width: 23.7693%;" /><col style="width: 46.528%;" /></colgroup><tbody><tr><th scope="col">Service</th><th scope="col">File name</th><th scope="col">Service description</th></tr><tr><td><span>Admin Console</span><span> </span></td><td><p><em>admin.war</em></p></td><td>Service for managing Teamwork Cloud users, roles, and resource assignments.</td></tr><tr><td>Authentication</td><td><p><em>authentication.war</em></p></td><td>Service for authenticating access to Teamwork Cloud.</td></tr><tr><td><span>Cameo Collaborator for Teamwork Cloud</span></td><td><p><em>collaborator.war</em></p></td><td><p>Allows reviewing, editing, and collaborating on Cameo Collaborator documents.</p></td></tr><tr><td><span><span>Document Exporter</span></span></td><td><p><em>document-exporter.war</em></p></td><td><p>Allows exporting Cameo Collaborator documents to PDF and HTML.</p></td></tr><tr><td><span>Oslc</span></td><td><em>oslc.war</em> </td><td><p>Enables model browsing through OSLC.</p></td></tr><tr><td><span>Reports</span></td><td><em>reports.war</em> </td><td><p>Allows exporting Teamwork Cloud server-related data to XLSX or CSV.</p></td></tr><tr><td><span><span>Resource Usage Map</span></span></td><td><em>resource-usage-map.war</em></td><td><p>A service with live visual graph capabilities for representing Teamwork Cloud resource usages. allowing users to identify potential problem areas.</p></td></tr><tr><td><span>Resources</span></td><td><em>resources.war</em> </td><td><p>The service for managing Teamwork Cloud resources.</p></td></tr><tr><td><span>Simulation</span></td><td><em>simulation.war</em></td><td><p>Allows users to simulate Teamwork Cloud projects on the server side.</p></td></tr><tr><td><span><ac:inline-comment-marker ac:ref="6e7436c0-eb14-4f36-9e6b-7844a3f0fd03">Home page</ac:inline-comment-marker></span></td><td><em>webapp.war</em></td><td><p><ac:inline-comment-marker ac:ref="c9ddb037-a55e-4d6b-8cf3-5766ff81fec6">Home page service.</ac:inline-comment-marker></p></td></tr><tr><td><span><span>Semantic Graph Index Crawler</span></span></td><td><em>sgi-crawler.war </em></td><td><p>Indexes Teamwork Cloud projects in the Semantic Graph Index of the 3DEXPERIENCE platform to enable CATIA Systems Traceability analysis.</p></td></tr><tr><td><span><span>SysML v2 API and Services</span></span></td><td><em>sysmlv2-api.war</em></td><td><p>REST/HTTP Platform-specific model (PSM) implementation of the SysML v2 API and Services standard.</p></td></tr><tr><td><span><span style="color:var(--ds-text,#172b4d);">Element Chooser</span><br style="text-align: left;" /></span></td><td><em>element-chooser.war</em></td><td><p>Allows users to select model elements in a modeling tool using the web UI.</p></td></tr><tr><td><span><span style="color:var(--ds-text,#172b4d);">MagicLab</span></span></td><td><em>magiclab.war</em></td><td><p>Allows reading SysMLv2 projects on the web.</p></td></tr><tr><td><span><span style="color:var(--ds-text,#172b4d);"><span>MagicLab Collaborator</span></span></span></td><td><em>magiclab-collaborator.war</em></td><td>Enables collaboration on SysML v2 projects.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=247047469 space=MCS version=3 -->
## PAGE 00872: Working with categories

- page_id: `247047469`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047469/Working+with+categories
- version_number: 3
- version_date: `2025-09-15T10:13:09.051+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Resources application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

All Teamwork Cloud and Cameo Collaborator for Teamwork Cloud resources are sorted by categories. The sections below explain how to create new categories and manage existing ones.

After creating/editing/removing a category, that category in other applications will not be updated immediately.

##### Creating categories

You can either create a category when publishing a model from a modeling tool or create it directly in the Resources app. Follow the steps below to create a category in the Resources app.

To create a category

1. Open the Resources application.
2. Click [IMAGE alt='' src=''] on the bottom right corner of the screen. The **Create category** dialog opens. Creating a nested categoryTo create a category nested in another category, navigate to the intended parent category before completing step 2.
3. Enter the new category name in the Category name field.
4. Click the Create button. [ATTACHMENT filename='creating_categories.png']

The category is created and shown in the repository together with other categories.

##### Renaming categories

If necessary, rename existing categories as described below.

To rename a category

1. Open the Resources application and navigate to the category you want to rename.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Rename category . The Rename category dialog opens.
3. Enter a new category name in the Category name field.
4. Click the Rename button. [ATTACHMENT filename='renaming_categories.png']

After completing the above steps, you can see the category with a new name in the repository.

##### Removing categories

You can remove categories without deleting the resources they contain.

To remove a category

1. Open the Resources application and navigate to the category you want to remove.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Remove category .
3. When you get the message asking if you want to remove the category, click Remove .

The category is removed and all the resources it contained are moved to the **Uncategorized**category.

##### Navigating in categories

Teamwork Cloud supports nested categories so you can organize your resources in a folder-like manner. To see the contents of a specific category, click it as displayed below. The full path to an open category is displayed just below the app bar.

[IMAGE alt='' src='']

##### Setting category classifications

Category classifications that you set through data markings allows you to control access to that category. To set a category classification, [CONFLUENCE_PAGE title='Managing data markings in Teamwork Cloud Admin' space=''] in the Settings menu and ensure you have [sufficient permissions](https://docs.nomagic.com/display/MCS/Permissions).

To set a category classification

1. Go to the Resources application and locate the category to set its classification.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Edit category details .
3. In the Classification drop-down select the desired data marking.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All Teamwork Cloud and Cameo Collaborator for Teamwork Cloud resources are sorted by categories. The sections below explain how to create new categories and manage existing ones.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f0191de0-02db-486a-8fe2-545299f52559"><ac:rich-text-body><p>After creating/editing/removing a category, that category in other applications will not be updated immediately.</p></ac:rich-text-body></ac:structured-macro><h3><br />Creating categories</h3><p>You can either create a category when publishing a model from a modeling tool or create it directly in the Resources app. Follow the steps below to create a category in the Resources app.</p><p><br /></p><p>To create a category</p><hr /><ol><li><p class="auto-cursor-target">Open the Resources application.</p></li><li><p class="auto-cursor-target">Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="create_category.png" /></ac:image> on the bottom right corner of the screen. The <strong>Create category</strong> dialog opens.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="943bf20d-586f-4e88-87a9-37dc4245166b"><ac:parameter ac:name="title">Creating a nested category</ac:parameter><ac:rich-text-body><p>To create a category nested in another category, navigate to the intended parent category before completing step 2.</p></ac:rich-text-body></ac:structured-macro></li><li>Enter the new category name in the <strong>Category name</strong> field.</li><li>Click the <strong>Create</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="creating_categories.png" /></ac:image></li></ol><p><br />The category is created and shown in the repository together with other categories.</p><h3><br />Renaming categories</h3><p>If necessary, rename existing categories as described below.</p><p><br /></p><p>To rename a category</p><hr /><ol><li>Open the Resources application and navigate to the category you want to rename.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Rename category</strong>. The <strong>Rename category</strong> dialog opens.</li><li>Enter a new category name in the <strong>Category name</strong> field.</li><li>Click the <strong>Rename</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="renaming_categories.png" /></ac:image></li></ol><p><br />After completing the above steps, you can see the category with a new name in the repository.</p><h3><br />Removing categories</h3><p>You can remove categories without deleting the resources they contain.</p><p><br /></p><p>To remove a category</p><hr /><ol><li>Open the Resources application and navigate to the category you want to remove.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Remove category</strong>.</li><li>When you get the message asking if you want to remove the category, click <strong>Remove</strong>.</li></ol><p><br />The category is removed and all the resources it contained are moved to the <strong>Uncategorized </strong>category.</p><h3><br />Navigating in categories</h3><p>Teamwork Cloud supports nested categories so you can organize your resources in a folder-like manner. To see the contents of a specific category, click it as displayed below. The full path to an open category is displayed just below the app bar.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="navigating_in_categories.png" /></ac:image></p><h3>Setting category classifications</h3><p>Category classifications that you set through data markings allows you to control access to that category. To set a category classification, <ac:link><ri:page ri:content-title="Managing data markings in Teamwork Cloud Admin" /><ac:plain-text-link-body><![CDATA[enable data markings]]></ac:plain-text-link-body></ac:link> in the Settings menu and ensure you have <a href="https://docs.nomagic.com/display/MCS/Permissions">sufficient permissions</a>.</p><p>To set a category classification</p><hr /><ol><li>Go to the Resources application and locate the category to set its classification.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Edit category details</strong>.</li><li>In the <strong>Classification </strong>drop-down select the desired data marking.</li></ol>
````

<!--NOMAGIC_PAGE id=247047747 space=MCS version=1 -->
## PAGE 00873: Working with comments

- page_id: `247047747`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047747/Working+with+comments
- version_number: 1
- version_date: `2025-08-11T16:48:44.685+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

After an author [CONFLUENCE_PAGE title='Sharing document links' space='MCS'], you can start reviewing it and give feedback to the author in the form of textual and graphical comments. [CONFLUENCE_PAGE title='Creating and editing textual comments' space='MCS'] can be written for any element, including its properties displayed on the content pane. [CONFLUENCE_PAGE title='Creating and editing graphical comments' space='MCS'] can be drawn on all images, e.g., diagrams, maps, and matrices.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After an author <ac:link><ri:page ri:space-key="MCS" ri:content-title="Sharing document links" /><ac:plain-text-link-body><![CDATA[shares a published document]]></ac:plain-text-link-body></ac:link>, you can start reviewing it and give feedback to the author in the form of textual and graphical comments. <ac:link><ri:page ri:space-key="MCS" ri:content-title="Creating and editing textual comments" /><ac:plain-text-link-body><![CDATA[Textual comments]]></ac:plain-text-link-body></ac:link> can be written for any element, including its properties displayed on the content pane. <ac:link><ri:page ri:space-key="MCS" ri:content-title="Creating and editing graphical comments" /><ac:plain-text-link-body><![CDATA[Graphical comments]]></ac:plain-text-link-body></ac:link> can be drawn on all images, e.g., diagrams, maps, and matrices.</p><p>For more information, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8874731f-3e46-4d84-b48e-d2c28c4d5253" /></p>
````

<!--NOMAGIC_PAGE id=247047838 space=MCS version=3 -->
## PAGE 00874: Working with comments as model elements

- page_id: `247047838`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047838/Working+with+comments+as+model+elements
- version_number: 3
- version_date: `2025-09-16T11:19:22.770+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

By default, comments are stored in Cameo Collaborator documents. However, it is possible to store Cameo Collaborator comments as model elements inside a project. This allows you to work with them as any other UML elements and use the benefits of the modeling tool functionalities, such as calculating metrics, validating comments, and creating comment reports.

#### NOTE: Working with synchronized projects

Working with synchronized projects

Synchronized projects on the target Teamwork Cloud server are read-only. This means you cannot store Cameo Collaborator comments in such projects because they cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space=''].

##### Storing Cameo Collaborator Comments in a project

If you want to store Cameo Collaborator comments in a project rather than in a document, you have to choose the **Comments in project** check box when publishing the document, as shown below. For information on how to publish documents, refer to [CONFLUENCE_PAGE title='Publishing documents' space=''].

[IMAGE alt='' src='']

###### The **Cameo Collaborator Publisher** dialog with the highlighted option, which allows storing comments inside a project.

When Cameo Collaborator comments are saved in a project, they are automatically synchronized between the project and the document every time you commit changes to the server or update the project. This means you can work with comments both in a modeling tool and Cameo Collaborator without compromising consistency.

#### NOTE: Importing comments

Importing comments

If you select the **Comments in project** check box when updating an existing document with comments, a dialog will pop up, allowing you to import these comments from the document to the project (see the figure below). However, keep in mind that you will not be able to migrate the comments from the project back to the document, so be careful not to clear the**Comments in project**check box when updating the document at a later time.

[IMAGE alt='' src='']

###### A popup dialog allowing you to import Cameo Collaborator comments to a project automatically.

##### Importing Cameo Collaborator comments to a project manually

If you did not import Cameo Collaborator comments to a project when publishing a document with the **Comments in project** option enabled (as described in the above section), you can import them manually later.

To import Cameo Collaborator comments to a project

1. In the main menu of a modeling tool, select Tools > Cameo Collaborator > Import Comments .
2. When you get a notification that comments are being imported, wait until the import is complete and update the project.

You can find the imported comments in the containment tree of a modeling tool under the Package with the same name as the published document.

[IMAGE alt='' src='']

###### Imported Cameo Collaborator comments in the containment tree of a modeling tool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>By default, comments are stored in Cameo Collaborator documents. However, it is possible to store Cameo Collaborator comments as model elements inside a project. This allows you to work with them as any other UML elements and use the benefits of the modeling tool functionalities, such as calculating metrics, validating comments, and creating comment reports.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b185f57-c071-4566-91dc-915a337dd531"><ac:parameter ac:name="title">Working with synchronized projects</ac:parameter><ac:rich-text-body><p>Synchronized projects on the target Teamwork Cloud server are read-only. This means you cannot store Cameo Collaborator comments in such projects because they cannot be modified. <ac:link><ri:page ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3><br />Storing Cameo Collaborator Comments in a project</h3><p>If you want to store Cameo Collaborator comments in a project rather than in a document, you have to choose the <strong>Comments in project</strong> check box when publishing the document, as shown below. For information on how to publish documents, refer to <ac:link><ri:page ri:content-title="Publishing documents" /></ac:link>.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="commnets_in_project_check_box.png" /></ac:image></p><h6 style="text-align: center;">The <strong>Cameo Collaborator Publisher</strong> dialog with the highlighted option, which allows storing comments inside a project.</h6><p><br />When Cameo Collaborator comments are saved in a project, they are automatically synchronized between the project and the document every time you commit changes to the server or update the project. This means you can work with comments both in a modeling tool and Cameo Collaborator without compromising consistency.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="240dd451-66e3-4ffc-81db-ae12bc2dbef1"><ac:parameter ac:name="title">Importing comments</ac:parameter><ac:rich-text-body><p>If you select the <strong>Comments in project</strong> check box when updating an existing document with comments, a dialog will pop up, allowing you to import these comments from the document to the project (see the figure below). <span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><span> </span>However, keep in mind that you will not be able to migrate the comments from the project back to the document, so be careful not to clear the </span><strong style="text-align: left;">Comments in project</strong><span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><span> </span>check box when updating the document at a later time.</span></p><p style="text-align: center;"><span style="color:var(--ds-text-accent-purple-bolder,#352c63);"><ac:image ac:height="171"><ri:attachment ri:filename="importing_comments_automatically.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text-accent-purple-bolder,#352c63);">A popup dialog allowing you to import Cameo Collaborator comments to a project automatically.</span></h6></ac:rich-text-body></ac:structured-macro><h3><br />Importing Cameo Collaborator comments to a project manually</h3><p>If you did not import Cameo Collaborator comments to a project when publishing a document with the <strong>Comments in project</strong> option enabled (as described in the above section), you can import them manually later.</p><p><br /></p><p>To import Cameo Collaborator comments to a project</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Import Comments</strong>.</li><li>When you get a notification that comments are being imported, wait until the import is complete and update the project.</li></ol><p><br /></p><p>You can find the imported comments in the containment tree of a modeling tool under the Package with the same name as the published document.</p><p><br /></p><p style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="comments_in_project.png" /></ac:image></span></p><h6 style="text-align: center;">Imported Cameo Collaborator comments in the containment tree of a modeling tool.</h6>
````

<!--NOMAGIC_PAGE id=247047801 space=MCS version=1 -->
## PAGE 00875: Working with comments in a modeling tool

- page_id: `247047801`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047801/Working+with+comments+in+a+modeling+tool
- version_number: 1
- version_date: `2025-08-11T16:48:45.470+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

When you get feedback in a Cameo Collaborator document, you can address comments straight from the modeling tool by using the comments panel. This saves time because you can quickly navigate from comments to commented elements and modify them without leaving the modeling environment.

Once a Cameo Collaborator document has comments you need to respond to, do the following:

1. In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space='MCS'] .
3. Do one or several of the following actions:
  1. Select a comment in the comments panel to navigate to the commented element and its commented properties.
4. Modify the model to address comments .
5. [CONFLUENCE_PAGE title='Replying to a comment' space='MCS'] to confirm that they have been addressed or ask additional questions (you can also resolve, edit, and delete comments).
6. Save/commit and [CONFLUENCE_PAGE title='Publishing documents' space='MCS'] the updated model.

[IMAGE alt='' src='']

###### Use the comments panel in your modeling tool to navigate to the commented element and update it in the model.

To learn more about working with comments in a modeling tool, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">When you get feedback in a Cameo Collaborator document, you can address comments straight from the modeling tool by using the comments panel. This saves time because you can quickly navigate from comments to commented elements and <ac:inline-comment-marker ac:ref="be6f0423-73b9-4959-9c8d-c44d0313e3d5">modify</ac:inline-comment-marker> them without leaving the modeling environment.</span></p><p>Once a Cameo Collaborator document has comments you need to respond to, do the following:</p><ol><li>In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.</li><li><ac:link><ri:page ri:space-key="MCS" ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the comments panel]]></ac:plain-text-link-body></ac:link>.</li><li>Do one or several of the following actions:<ol><li>Select a comment in the comments panel to navigate to the commented element and its commented properties.</li></ol></li><li><ac:inline-comment-marker ac:ref="f915abc6-3ea8-434d-a99a-3f01ed94103a">Modify the model to address comments</ac:inline-comment-marker>.</li><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="MCS" ri:content-title="Replying to a comment" /><ac:plain-text-link-body><![CDATA[Reply to comments]]></ac:plain-text-link-body></ac:link> to confirm that they have been addressed or ask additional questions</span> (you can also resolve, edit, and delete comments).</li><li><ac:inline-comment-marker ac:ref="f137d148-257c-452a-94dd-dfd941a798d6">Save/commit</ac:inline-comment-marker> and <ac:link><ri:page ri:space-key="MCS" ri:content-title="Publishing documents" /><ac:plain-text-link-body><![CDATA[publish]]></ac:plain-text-link-body></ac:link> the updated model.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="comments_panel.png"><ri:page ri:space-key="MCS" ri:content-title="Working with comments in a modeling tool" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Use the comments panel in your modeling tool to navigate to the commented element and update it in the model.</h6><p><ac:inline-comment-marker ac:ref="3ce71186-6f6c-47d1-b85d-cad9d2c9da4f">To learn more about working with comments in a modeling tool, see the following topics:</ac:inline-comment-marker></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=247047748 space=MCS version=2 -->
## PAGE 00876: Working with comments in Cameo Collaborator

- page_id: `247047748`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047748/Working+with+comments+in+Cameo+Collaborator
- version_number: 2
- version_date: `2025-08-12T13:45:45.295+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['commenting', 'working-with-comments', 'mcs', 'twc']

### NORMALIZED CONTENT

Comments can be either textual or graphical. Textual comments can be associated with any element or any of its standard properties, while graphical comments can be attached to diagrams, maps, and matrices. Both types of comments can be further edited, replied, resolved, or deleted. The full list of comments in the published project is displayed in the [CONFLUENCE_PAGE title='Comments pane' space='MCS']**Comments** pane.

Learn more about working with comments in the following pages:

#### NOTE: Documents published from synchronized projects

Documents published from synchronized projects

If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space='MCS'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Comments can be either textual or graphical. Textual comments can be associated with any element or any of its standard properties, while graphical comments can be attached to diagrams, maps, and matrices. Both types of comments can be further edited, replied, resolved, or deleted. The full list of comments in the published project is displayed in the <ac:link><ri:page ri:space-key="MCS" ri:content-title="Comments pane" /><ac:link-body><strong>Comments</strong> pane</ac:link-body></ac:link>.</p><p>Learn more about working with comments in the following pages:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="802708fb-69cd-486a-b266-7e623ed7eac1" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="40ec8c45-01b7-4413-a02f-f98fbae18aba"><ac:parameter ac:name="title">Documents published from synchronized projects</ac:parameter><ac:rich-text-body><p>If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. <ac:link><ri:page ri:space-key="MCS" ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=247047626 space=MCS version=2 -->
## PAGE 00877: Working with custom document templates

- page_id: `247047626`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047626/Working+with+custom+document+templates
- version_number: 2
- version_date: `2026-01-12T12:48:40.370+01:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents > Document templates
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

When configuring settings for publishing a model to Cameo Collaborator, you must choose a template to determine the appearance and content of a published document. If predefined templates do not meet your specific needs, you can create and applya custom template. In custom templates, you can specify which model elements are published, what element information is displayed, and the format in which it is displayed. A custom template can be stored within a model itself or as a separate .mdzip file, which allows you to reuse it in multiple models. The following topics will help you learn how to modify a predefined template or create your own template from scratch:

##### Document template samples

If you are new to working with custom document templates, you may find it useful to analyze our [ATTACHMENT filename='Cameo Collaborator Template Samples.mdzip'] project which you can find with the other sample projects in your modeling tool installation directory. These template samples give step by step instructions on how to model several different document templates. The Content Diagram below shows what template modeling use cases you can find in the *Cameo Collaborator Template Samples* project.

[IMAGE alt='' src='']

###### The content of the *Cameo Collaborator Template Samples* project.

**Additional resources**

- Webinar *Creating Templates in Cameo Collaborator*
- User Guide for Creating Cameo Collaborator Templates
- [ATTACHMENT filename='Cameo Collaborator Template Samples.mdzip']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color:var(--ds-text,#333333);">When configuring settings for publishing a model to Cameo Collaborator, you must choose a template to determine the appearance and content of a published document. If predefined templates do not meet your specific needs, you can create and apply </span>a custom template. I<ac:inline-comment-marker ac:ref="34e1ac03-973a-4d3b-9990-6d0acc52d648"><ac:inline-comment-marker ac:ref="510a631f-76e4-4f7f-ae28-2379aa848ca4">n custom templates, you can specify which model elements are published, what element information is displayed, and the format in which it is displayed</ac:inline-comment-marker></ac:inline-comment-marker>. A custom template can be stored within a model itself or <span style="letter-spacing: 0.0px;">as a separate .mdzip file, which allows you to reuse it in multiple models</span>. The following topics will help you learn how to modify a predefined template or create your own template from scratch:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e05c3f95-95ee-4fb2-a650-cdabdd95f838" /></p><h3 style="color:var(--ds-text,#172b4d);"><br />Document template samples</h3><p>If you are new to working with custom document templates, you may find it useful to analyze our <ac:link><ri:attachment ri:filename="Cameo Collaborator Template Samples.mdzip" /></ac:link> project which you can find with the other sample projects in your modeling tool installation directory. These template samples give step by step instructions on how to model several different document templates. The Content Diagram below shows what template modeling use cases you can find in the <em>Cameo Collaborator Template Samples</em> project.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="samples_content_diagram.png" /></ac:image></p><h6 style="line-height: 1.66667;letter-spacing: normal;text-align: center;">The content of the <em>Cameo Collaborator Template Samples</em> project.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><ul><li><a href="https://youtu.be/NAoYVUJhT2A">Webinar <em>Creating Templates in Cameo Collaborator</em></a></li><li><a href="https://ccexamples.nomagic.com/collaborator/document/66babacb-881a-480e-a104-86427d8fabe8?viewId=12dd9272-276a-4de4-99d5-598f1fcc3bfb&amp;viewType=document&amp;sectionId=f71e7d7a-55f0-487c-bb40-ba4fa335922f&amp;guest=true">User Guide for Creating Cameo Collaborator Templates</a></li><li><ac:link><ri:attachment ri:filename="Cameo Collaborator Template Samples.mdzip" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=247046799 space=MCS version=4 -->
## PAGE 00878: Working with keystores

- page_id: `247046799`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247046799/Working+with+keystores
- version_number: 4
- version_date: `2026-01-14T11:50:56.469+01:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > Administration Guide > Product administration
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

##### Keystore Types

We recommend using PKCS#12, an archive format containing multiple cryptographic objects (also referred to as PFX).

Java also supports JKS, a native Java archive. However, it is to be deprecated in favor of the PKCS#12 standard.

##### Tools

There are two tools that are used when working with keystores and certificates:

- keytool - command-line tool, part of the java distribution, for manipulating keystores
- OpenSSL - client tool for manipulating certificates in multiple formats

All of the required tasks can be accomplished with keytool, so we will limit the scope of keystore management to keytool.

##### Create a keystore

Create a keystore in PKCS#12 format - the command below will create a keystore with a self-signed certificate for the given server. Please note that in order to have a signed certificate, the common name of the certificate cannot be an IP address.

Also, please note that in this example, we are also creating 3 subject alternative names: 1 for the common name (fqdn), 1 for the hostname (hostname), and one for the IP address of the server.

```text
-storetype  pkcs12 -storepass  -alias  -dname "CN=,OU=,O=,L=,S=,C=" -ext BasicConstraints:critical=ca:false -ext SAN=dns:,dns:,ip:]]>
```

##### View contents of a keystore

```text
-storepass ]]>
```

##### Create a CSR

Create a CSR from an existing keystore, adding the subject alternative names. The alias is that containing the entry of type **PrivateKeyEntry.**

```text
-storepass  -alias  -file  -ext SAN=dns:,dns:,ip: -ext BasicConstraints:critical=ca:false]]>
```

##### View contents of a CSR

```text
]]>
```

##### Import signed certificate into keystore

A signed server certificate must be imported into the keystore from which the CSR was generated, and into the same alias.

```text
-storepass  -alias  -file ]]>
```

When you obtain your signed certificate, it may be provided in a variety of ways. One possibility is that it is a PKCS#7 chained certificate (contains the signed server certificate as well as the certificate chain). Another option is that it is that you were provided a single signed certificate and a set of certificates comprising the certificate chain. If you were provided a PKCS#7, you will import it into the PrivateKeyEnty alias. If you were provided separate certificates, you will import the server certificate into the PrivateKeyEntry alias, and then import each of the other certificates into a different alias - for example -alias intermediate1, -alias intermediate2, -alias caroot.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Keystore Types</h3><p>We recommend using <span style="letter-spacing: 0.0px;">PKCS#12, an archive format containing multiple cryptographic objects (also referred to as PFX).</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="175c42ab-3604-4741-ba94-7fa5d1e3bfce"><ac:rich-text-body><p>Java also supports JKS, a native Java archive. However, it is to be deprecated in favor of the PKCS#12 standard.</p></ac:rich-text-body></ac:structured-macro><h3>Tools</h3><p>There are two tools that are used when working with keystores and certificates:</p><ul><li>keytool - command-line tool, part of the java distribution, for manipulating keystores</li><li>OpenSSL - client tool for manipulating certificates in multiple formats<br /><br /></li></ul><p>All of the required tasks can be accomplished with keytool, so we will limit the scope of keystore management to keytool.</p><h3>Create a keystore</h3><p>Create a keystore in PKCS#12 format - the command below will create a keystore with a self-signed certificate for the given server. Please note that in order to have a signed certificate, the common name of the certificate cannot be an IP address.</p><p>Also, please note that in this example, we are also creating 3 subject alternative names: 1 for the common name (fqdn), 1 for the hostname (hostname), and one for the IP address of the server.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3b8eef0f-d20d-4fd2-9223-592b401f9535"><ac:plain-text-body><![CDATA[keytool -genkeypair -keyalg RSA -sigalg SHA256withRSA -keysize 2048 -validity 3650 -keystore <keystore.p12> -storetype  pkcs12 -storepass <storepass> -alias <aliasname> -dname "CN=<fqdn>,OU=<Org Unit>,O=<Company Name>,L=<City>,S=<State>,C=<Country>" -ext BasicConstraints:critical=ca:false -ext SAN=dns:<fqdn>,dns:<hostname>,ip:<ip_address>]]></ac:plain-text-body></ac:structured-macro><h3 class="auto-cursor-target">View contents of a keystore</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="407d6ee5-d2b8-44c5-bbc3-3c1aec03571a"><ac:plain-text-body><![CDATA[keytool -list -v -keystore <keystore.p12> -storepass <storepass>]]></ac:plain-text-body></ac:structured-macro><h3>Create a CSR</h3><p>Create a CSR from an existing keystore, adding the subject alternative names. The alias is that containing the entry of type <strong>PrivateKeyEntry.</strong></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="63167c2b-89df-4fd7-9674-eb3d4abc36e0"><ac:plain-text-body><![CDATA[keytool -noprompt -certreq -keystore <keystore.p12> -storepass <storepass> -alias <aliasname> -file <server.csr> -ext SAN=dns:<fqdn>,dns:<hostname>,ip:<ipaddress> -ext BasicConstraints:critical=ca:false]]></ac:plain-text-body></ac:structured-macro><h3>View contents of a CSR</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d48f098c-f6d2-4ddb-a685-9d91c3d01681"><ac:plain-text-body><![CDATA[keytool -printcertreq -file <server.csr>]]></ac:plain-text-body></ac:structured-macro><h3>Import signed certificate into keystore</h3><p>A signed server certificate must be imported into the keystore from which the CSR was generated, and into the same alias.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8b2a3a95-a182-4d78-8db6-343144e4f790"><ac:plain-text-body><![CDATA[keytool -importcert -trustcacerts -keystore <keystore.p12> -storepass <storepass> -alias <aliasname> -file <server.crt>]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8903cde7-446f-42c0-88cb-1e168bdff0fa"><ac:rich-text-body><p>When you obtain your signed certificate, it may be provided in a variety of ways. One possibility is that it is a <span style="color:var(--ds-text,#333333);">PKCS#7 chained certificate (contains the signed server certificate as well as the certificate chain). Another option is that it is that you were provided a single signed certificate and a set of certificates comprising the certificate chain. If you were provided a PKCS#7, you will import it into the PrivateKeyEnty alias. If you were provided separate certificates, you will import the server certificate into the PrivateKeyEntry alias, and then import each of the other certificates into a different alias - for example -alias intermediate1, -alias intermediate2, -alias caroot.</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=247047486 space=MCS version=2 -->
## PAGE 00879: Working with resources

- page_id: `247047486`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047486/Working+with+resources
- version_number: 2
- version_date: `2025-08-25T12:55:28.650+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Resources application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

The Resources app allows you to access and manage three types of resources:

- UML/SysML v1 models (.mdzip files)
- Cameo Collaborator for Teamwork Could documents
- OSLC resources

See the following chapters to learn how to open, edit, or remove a resource:

Aftercreating/editing/removing a resource, the resource in the other applications will not be updated immediately.

[IMAGE alt='' src='']

###### Different types of resources in the Resources app.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Resources app allows you to access and manage three types of resources:</p><ul><li>UML/SysML v1 models (.mdzip files)</li><li>Cameo Collaborator for Teamwork Could documents</li><li>OSLC resources</li></ul><p>See the following chapters to learn how to open, edit, or remove a resource:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5f4281b1-816c-45ed-859b-23bfd39c4cb4"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">After </span><span style="color:var(--ds-text,#172b4d);">creating/editing/removing a resource, the resource in the other applications will not be updated immediately.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="types_of_resources.png" /></ac:image></p><h6 style="text-align: center;">Different types of resources in the Resources app.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=247047447 space=MCS version=1 -->
## PAGE 00880: Working with webhooks

- page_id: `247047447`
- space_key: `MCS`
- source_url: https://docs.nomagic.com/spaces/MCS/pages/247047447/Working+with+webhooks
- version_number: 1
- version_date: `2025-08-11T16:48:38.520+02:00`
- ancestors: Magic Collaboration Studio / Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

Webhooks allow you to get notifications pushed to a specified endpoint on predefined events in Teamwork Cloud instead of constantly polling for new data through REST APIs. You can listen to commit-type events in chosen resources or model elements and element-level events, such as commit or tagged commit.

To work with webhooks, a user needs the following permissions: **Read Resources**, **Configure Server,** and **Administer Resources**. For more information, see the article on [CONFLUENCE_PAGE title='Permissions' space='MCS'].

For more information on creating and managing webhooks, see the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">Webhooks allow you to get notifications pushed to a specified endpoint on predefined events in Teamwork Cloud instead of constantly polling for new data through REST APIs. You can listen to commit-type events in chosen resources or model elements and element-level events, such as commit or tagged commit.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9a7ff00f-a9dc-4603-ad59-5b7116a72ea8"><ac:rich-text-body><p><span style="color: rgb(0,0,0);">To work with webhooks, a user needs the following permissions: <strong>Read Resources</strong>, <strong>Configure Server,</strong> and <strong>Administer Resources</strong>. For more information, see the article on <ac:link><ri:page ri:space-key="MCS" ri:content-title="Permissions" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">For more information on creating and managing webhooks, see the following pages:</span></p><p class="auto-cursor-target"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````
