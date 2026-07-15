# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.editor/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.editor/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.editor/plugin.xml
- source_bytes: 2126
- source_sha256: `01ac5542760ca1b08349f4fb3ed93b32f9135026321f88bcae6eaa91727c16c3`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.0"?>

<!--
-->

<plugin>

   <extension point="org.eclipse.ui.newWizards">
      <!-- @generated SysML -->
      <category
            id="org.eclipse.emf.ecore.Wizard.category.ID"
            name="%_UI_Wizard_category"/>
      <wizard
            id="org.omg.sysml.lang.sysml.presentation.SysMLModelWizardID"
            name="%_UI_SysMLModelWizard_label"
            class="org.omg.sysml.lang.sysml.presentation.SysMLModelWizard"
            category="org.eclipse.emf.ecore.Wizard.category.ID"
            icon="icons/full/obj16/SysMLModelFile.gif">
         <description>%_UI_SysMLModelWizard_description</description>
         <selection class="org.eclipse.core.resources.IResource"/>
      </wizard>
   </extension>

   <extension point="org.eclipse.ui.editors">
      <!-- @generated SysML -->
      <editor
            id="org.omg.sysml.lang.sysml.presentation.SysMLEditorID"
            name="%_UI_SysMLEditor_label"
            icon="icons/full/obj16/SysMLModelFile.gif"
            extensions="sysml"
            class="org.omg.sysml.lang.sysml.presentation.SysMLEditor"
            contributorClass="org.omg.sysml.lang.sysml.presentation.SysMLActionBarContributor">
      </editor>
   </extension>
   <extension
         point="org.eclipse.ui.editors">
      <editor
            class="org.eclipse.emf.ecore.presentation.EcoreEditor"
            contributorClass="org.eclipse.emf.ecore.presentation.EcoreActionBarContributor"
            default="false"
            extensions="sysmlx"
            id="org.omg.sysml.lang.sysml.presentation.SysMLxEditorID"
            name="SysMLx Model Editor">
      </editor>
      <editor
            class="org.eclipse.emf.ecore.presentation.EcoreEditor"
            contributorClass="org.eclipse.emf.ecore.presentation.EcoreActionBarContributor"
            default="false"
            extensions="kermlx"
            id="org.omg.sysml.lang.sysml.presentation.KerMLxEditorID"
            name="KerMLx Model Editor">
      </editor>
   </extension>

</plugin>

````
