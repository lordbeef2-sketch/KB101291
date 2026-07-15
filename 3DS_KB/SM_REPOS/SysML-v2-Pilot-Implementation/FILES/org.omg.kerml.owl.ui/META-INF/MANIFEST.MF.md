# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.kerml.owl.ui/META-INF/MANIFEST.MF

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.kerml.owl.ui/META-INF/MANIFEST.MF`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.kerml.owl.ui/META-INF/MANIFEST.MF
- source_bytes: 1077
- source_sha256: `aef042c2c73d6b4b39ba97380635c07dbc6421c96de73b1f6b6912681e342aba`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: org.omg.kerml.owl.ui
Bundle-RequiredExecutionEnvironment: JavaSE-21
Bundle-Vendor: My Company
Bundle-Version: 0.60.1.qualifier
Bundle-SymbolicName: org.omg.kerml.owl.ui;singleton:=true
Bundle-ActivationPolicy: lazy
Require-Bundle: org.omg.kerml.owl,
 org.omg.kerml.owl.ide,
 org.eclipse.xtext.ui,
 org.eclipse.xtext.ui.shared,
 org.eclipse.xtext.ui.codetemplates.ui,
 org.eclipse.ui.editors;bundle-version="3.5.0",
 org.eclipse.ui.ide;bundle-version="3.5.0",
 org.eclipse.ui,
 org.eclipse.compare,
 org.eclipse.xtext.builder,
 org.eclipse.xtend.lib;bundle-version="2.14.0";resolution:=optional,
 org.eclipse.xtext.xbase.lib;bundle-version="2.14.0"
Import-Package: org.apache.log4j
Export-Package: org.omg.kerml.owl.ui.internal,
 org.omg.kerml.owl.ui,
 org.omg.kerml.owl.ui.contentassist,
 org.omg.kerml.owl.ui.labeling,
 org.omg.kerml.owl.ui.outline,
 org.omg.kerml.owl.ui.quickfix
Bundle-Activator: org.omg.kerml.owl.ui.internal.OwlActivator
Automatic-Module-Name: org.omg.kerml.owl.ui

````
