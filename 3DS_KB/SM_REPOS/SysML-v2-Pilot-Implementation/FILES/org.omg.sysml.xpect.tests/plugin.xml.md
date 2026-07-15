# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/plugin.xml
- source_bytes: 1113
- source_sha256: `f96ad437736327f1bb64f04c1ebd3ae98a8fc83a02dcdd95903cba2f81f0eb66`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.4"?>
<plugin>
   <extension
         point="org.eclipse.xpect.fileExtensions">
      <fileExtension
            fileExtension="sysml"
            xtextLanguageName="org.omg.sysml.xtext.SysML"
            xtextRuntimeModule="org.omg.sysml.xpect.SysMLXpectRuntimeModule"
            xtextUiModule="org.omg.sysml.xtext.ui.SysMLUiModule">
      </fileExtension>
      <fileExtension
            fileExtension="kerml"
            xtextLanguageName="org.omg.sysml.xtext.KerML"
            xtextRuntimeModule="org.omg.kerml.xpect.KerMLXpectRuntimeModule"
            xtextUiModule="org.omg.kerml.xtext.ui.KerMLUiModule">
      </fileExtension>
   </extension>
   <extension
         point="org.eclipse.xpect.fileExtensions">
      <fileExtension
            fileExtension="sysml"
            xtextLanguageName="org.omg.sysml.xtext.SysML"
            xtextRuntimeModule="org.omg.sysml.xpect.SysMLXpectRuntimeModule"
            xtextUiModule="org.omg.sysml.xtext.ui.SysMLUiModule">
      </fileExtension>
   </extension>

</plugin>

````
