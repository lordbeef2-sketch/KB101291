# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.plantuml.eclipse/plugin.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.plantuml.eclipse/plugin.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.plantuml.eclipse/plugin.xml
- source_bytes: 715
- source_sha256: `690e395675f87176cfc561d1584825d9ac41bc09f301a09d97247a7ff8472aa7`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8"?>
<?eclipse version="3.2"?>
<plugin>

   <extension
         point="net.sourceforge.plantuml.eclipse.diagramTextProvider">

      <diagramTextProvider
            id="org.omg.sysml.plantuml.SysMLDiagramTextProvider"
            label="Diagrams generated from SysML models"
            priority="100"
            providerClass="org.omg.sysml.plantuml.eclipse.SysMLDiagramTextProvider">
      </diagramTextProvider>
   </extension>
   <extension
         point="net.sourceforge.plantuml.eclipse.linkOpener">
      <linkOpener
            linkOpenerClass="org.omg.sysml.plantuml.eclipse.SysMLDiagramLinkOpener">
      </linkOpener>
   </extension>

</plugin>

````
