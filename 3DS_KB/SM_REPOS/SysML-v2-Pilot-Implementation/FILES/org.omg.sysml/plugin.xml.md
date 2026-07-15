# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/plugin.xml
- source_bytes: 912
- source_sha256: `dc5cce751587c20e160efd976c5ab50cafaee7f79c989773ba3ff6bff4a302c3`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.0"?>

<!--
-->

<plugin>


   <extension point="org.eclipse.emf.ecore.generated_package">
      <!-- @generated sysml -->
      <package
            uri="https://www.omg.org/spec/SysML/20250201"
            class="org.omg.sysml.lang.sysml.SysMLPackage"
            genModel="platform:/plugin/org.omg.sysml/model/SysML.genmodel"/>
   </extension>
   
   <extension point = "org.eclipse.emf.ecore.setting_delegate">
      <factory
      		uri="http://www.omg.org/spec/SysML"
      		class="org.omg.sysml.delegate.setting.DerivedPropertySettingDelegateFactory" />
   </extension>
   
   <extension point = "org.eclipse.emf.ecore.invocation_delegate">
      <factory
      		uri="http://www.omg.org/spec/SysML"
      		class="org.omg.sysml.delegate.invocation.OperationInvocationDelegateFactory" />
   </extension>

</plugin>

````
