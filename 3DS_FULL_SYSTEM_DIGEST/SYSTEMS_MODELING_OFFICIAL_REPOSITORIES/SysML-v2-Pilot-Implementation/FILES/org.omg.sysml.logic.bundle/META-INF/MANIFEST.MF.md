# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.logic.bundle/META-INF/MANIFEST.MF

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.logic.bundle/META-INF/MANIFEST.MF`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.logic.bundle/META-INF/MANIFEST.MF
- source_bytes: 1072
- source_sha256: `5dcb115c5860befec879d72bf4ca7a7bb0b32226552379c14a3036453869f12d`
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
Export-Package: org.omg.sysml.adapter,
 org.omg.sysml.delegate.invocation,
 org.omg.sysml.delegate.setting,
 org.omg.sysml.expressions,
 org.omg.sysml.expressions.functions,
 org.omg.sysml.expressions.functions.base,
 org.omg.sysml.expressions.functions.bool,
 org.omg.sysml.expressions.functions.control,
 org.omg.sysml.expressions.functions.data,
 org.omg.sysml.expressions.functions.trig,
 org.omg.sysml.logic,
 org.omg.sysml.logic.api,
 org.omg.sysml.util
Require-Bundle: org.eclipse.emf.common;bundle-version="2.44.0",
 org.eclipse.emf.ecore;bundle-version="2.41.0",
 org.omg.sysml.model.bundle;bundle-version="0.60.1"
Bundle-ClassPath: .,
 lib/org.omg.sysml.logic-0.60.1-SNAPSHOT.jar
Bundle-SymbolicName: org.omg.sysml.logic.bundle;singleton:=true
Bundle-ActivationPolicy: lazy
Automatic-Module-Name: org.omg.sysml.logic.bundle

````
