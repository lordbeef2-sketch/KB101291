# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.editor/META-INF/MANIFEST.MF

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.editor/META-INF/MANIFEST.MF`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.editor/META-INF/MANIFEST.MF
- source_bytes: 827
- source_sha256: `1b6c477a70a7d8dea1e931e25b58e9bf4d175526e4fa89b5ef6c442043033912`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: %pluginName
Bundle-SymbolicName: org.omg.sysml.editor;singleton:=true
Automatic-Module-Name: org.omg.sysml.editor
Bundle-Version: 0.60.1.qualifier
Bundle-ClassPath: .
Bundle-Activator: org.omg.sysml.lang.sysml.presentation.SysMLEditorPlugin$Implementation
Bundle-Vendor: %providerName
Bundle-Localization: plugin
Bundle-RequiredExecutionEnvironment: JavaSE-21
Export-Package: org.omg.sysml.lang.sysml.presentation
Require-Bundle: org.eclipse.core.runtime,
 org.eclipse.core.resources;visibility:=reexport,
 org.omg.sysml.edit;visibility:=reexport,
 org.eclipse.emf.ecore.xmi;visibility:=reexport,
 org.eclipse.emf.edit.ui;visibility:=reexport,
 org.eclipse.ui.ide;visibility:=reexport,
 org.eclipse.emf.ecore.editor
Bundle-ActivationPolicy: lazy

````
