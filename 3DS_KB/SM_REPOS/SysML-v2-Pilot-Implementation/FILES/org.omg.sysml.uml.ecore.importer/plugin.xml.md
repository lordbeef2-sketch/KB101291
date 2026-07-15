# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.uml.ecore.importer/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.uml.ecore.importer/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.uml.ecore.importer/plugin.xml
- source_bytes: 1698
- source_sha256: `9861ace43c284903f2c076ab7d468b6af2cae29c9796350d0f21912be93d3be7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.0"?>

<!--
 Copyright (c) 2006, 2026 IBM Corporation, Embarcadero Technologies, and others.
 All rights reserved.   This program and the accompanying materials
 are made available under the terms of the Eclipse Public License v2.0
 which accompanies this distribution, and is available at
 http://www.eclipse.org/legal/epl-v20.html

 Contributors: 
   IBM - initial API and implementation
   Kenn Hussey (Embarcadero Technologies) - 226102
   Kenn Hussey - 535301
   Axel Richard - STR6I-916

-->

<plugin>

  <extension point="org.eclipse.emf.importer.modelImporterDescriptors">
    <modelImporterDescriptor
       id="org.omg.sysml.uml.ecore.importer"
       name="%_UI_UMLImporter_label"
       icon="platform:/plugin/org.eclipse.uml2.uml.editor/icons/full/obj16/UMLModelFile.gif"
       extensions="uml,UML,uml2,UML2,xmi,XMI,cmof,CMOF"
       description="%_UI_UMLModelImporter_description"
       wizard="org.omg.sysml.uml.ecore.importer.ui.CustomUMLImporterWizard"/>
  </extension>

  <!--
    Contribute a SysML-specific UML2 GenModel generator adapter factory for the
    UML2 GenModel namespace used by SysML.genmodel. The custom factory keeps
    the default UML2 generation behavior and only swaps in a GenClass adapter
    subclass that normalizes helper-list imports after each Java class is
    generated.
  -->
  <extension point="org.eclipse.emf.codegen.ecore.generatorAdapters">
    <adapterFactory
       modelPackage="http://www.eclipse.org/uml2/2.2.0/GenModel"
       class="org.omg.sysml.uml.ecore.importer.SysMLGenModelGeneratorAdapterFactory"/>
  </extension>

</plugin>

````
