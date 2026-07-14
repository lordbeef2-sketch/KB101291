# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/META-INF/MANIFEST.MF

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/META-INF/MANIFEST.MF`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/META-INF/MANIFEST.MF
- source_bytes: 1521
- source_sha256: `f82a8c466588ac0510d8b1f337d76dc10b7f630671f2d4ba080209df973e87d1`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: %pluginName
Bundle-Vendor: %providerName
Bundle-Localization: plugin
Bundle-RequiredExecutionEnvironment: JavaSE-21
Bundle-Version: 0.60.1.qualifier
Bundle-ClassPath: .,
 lib/sysml-v2-api-client-all.jar
Bundle-SymbolicName: org.omg.sysml;singleton:=true
Bundle-ActivationPolicy: lazy
Require-Bundle: org.eclipse.xtext,
 org.eclipse.xtext.xbase,
 org.eclipse.xtext.xbase.lib;bundle-version="2.14.0",
 org.eclipse.xtext.util,
 org.eclipse.xtend.lib;bundle-version="2.14.0",
 org.antlr.runtime;bundle-version="[3.2.0,3.2.1)",
 org.eclipse.core.runtime,
 org.eclipse.emf.ecore;visibility:=reexport,
 org.eclipse.emf.ecore.xmi;visibility:=reexport,
 org.eclipse.uml2.common;visibility:=reexport,
 org.eclipse.ocl.ecore;visibility:=reexport,
 org.eclipse.emf.mwe2.launch;bundle-version="2.9.1",
 org.eclipse.xtext.xtext.generator;bundle-version="2.12.0",
 org.eclipse.m2m.qvt.oml,
 org.eclipse.uml2.uml.resources,
 org.eclipse.equinox.common;bundle-version="3.5.0",
 org.omg.sysml.model.bundle;bundle-version="0.60.1",
 org.omg.sysml.logic.bundle;bundle-version="0.60.1"
Export-Package: org.omg.sysml,
 org.omg.sysml.api,
 org.omg.sysml.io,
 org.omg.sysml.model,
 org.omg.sysml.qvt,
 org.omg.sysml.util.repository,
 org.omg.sysml.util.traversal,
 org.omg.sysml.util.traversal.facade,
 org.omg.sysml.util.traversal.facade.impl
Import-Package: org.apache.commons.logging,
 org.apache.log4j
Automatic-Module-Name: org.omg.sysml

````
