# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.edit/META-INF/MANIFEST.MF

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.edit/META-INF/MANIFEST.MF`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.edit/META-INF/MANIFEST.MF
- source_bytes: 719
- source_sha256: `25ae4a6b8c2c43a4678e48bad05a4654ba4b1b4744e6685dfc4118b4e32602f3`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: %pluginName
Bundle-SymbolicName: org.omg.sysml.edit;singleton:=true
Automatic-Module-Name: org.omg.sysml.edit
Bundle-Version: 0.60.1.qualifier
Bundle-ClassPath: .
Bundle-Activator: org.omg.sysml.lang.sysml.provider.SysMLEditPlugin$Implementation
Bundle-Vendor: %providerName
Bundle-Localization: plugin
Bundle-RequiredExecutionEnvironment: JavaSE-21
Export-Package: org.omg.sysml.lang.sysml.provider
Require-Bundle: org.eclipse.core.runtime,
 org.eclipse.emf.edit;visibility:=reexport,
 org.eclipse.uml2.common.edit;visibility:=reexport,
 org.omg.sysml.model.bundle;bundle-version="0.60.1";visibility:=reexport
Bundle-ActivationPolicy: lazy

````
