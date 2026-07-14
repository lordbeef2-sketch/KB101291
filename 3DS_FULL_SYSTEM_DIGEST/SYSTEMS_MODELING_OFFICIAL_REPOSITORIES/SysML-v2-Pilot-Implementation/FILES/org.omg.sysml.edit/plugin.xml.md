# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.edit/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.edit/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.edit/plugin.xml
- source_bytes: 777
- source_sha256: `d970f25ccdeee5d9c97d4a3338bcdcca751b3bb394bb46eba33775892df0c4da`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.0"?>

<!--
-->

<plugin>

   <extension point="org.eclipse.emf.edit.itemProviderAdapterFactories">
      <!-- @generated SysML -->
      <factory
            uri="https://www.omg.org/spec/SysML/20250201"
            class="org.omg.sysml.lang.sysml.provider.SysMLItemProviderAdapterFactory"
            supportedTypes=
              "org.eclipse.emf.edit.provider.IEditingDomainItemProvider
               org.eclipse.emf.edit.provider.IStructuredItemContentProvider
               org.eclipse.emf.edit.provider.ITreeItemContentProvider
               org.eclipse.emf.edit.provider.IItemLabelProvider
               org.eclipse.emf.edit.provider.IItemPropertySource"/>
   </extension>

</plugin>

````
