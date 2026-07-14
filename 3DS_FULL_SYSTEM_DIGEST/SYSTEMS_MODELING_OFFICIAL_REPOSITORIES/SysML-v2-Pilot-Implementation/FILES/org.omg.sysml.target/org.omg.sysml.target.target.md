# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.target/org.omg.sysml.target.target

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.target/org.omg.sysml.target.target`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.target/org.omg.sysml.target.target
- source_bytes: 1921
- source_sha256: `a7d2d1b64ae127962e142200cbe5e8366d022ea1dc013d4b5a76447d0474914a`
- decoded_as: `utf-8`


## EXACT SOURCE

````text
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?pde version="3.8"?>
<target includeMode="feature" name="SysMLv2 2025-12 Target">
	<locations>
		<location includeAllPlatforms="false" includeConfigurePhase="true" includeMode="planner" includeSource="true" type="InstallableUnit">
			<repository location="https://download.eclipse.org/releases/2025-12/"/>
			<unit id="org.eclipse.platform.feature.group" version="4.38.0.v20251201-0920"/>
			<unit id="org.eclipse.xtext.sdk.feature.group" version="2.41.0.v20251124-0739"/>
			<unit id="org.eclipse.m2m.qvt.oml.runtime.feature.group" version="3.11.1.v20251124-1059"/>
			<unit id="org.eclipse.emf.ecore.feature.group" version="2.42.0.v20251025-0946"/>
			<unit id="org.eclipse.uml2.feature.group" version="5.5.3.v20221116-1811"/>
			<unit id="org.eclipse.egit.feature.group" version="7.5.0.202512021534-r"/>
			<unit id="org.eclipse.jgit.feature.group" version="7.5.0.202512021534-r"/>
			<unit id="com.google.gson" version="2.13.2"/>
		</location>
		<location includeAllPlatforms="false" includeConfigurePhase="true" includeMode="planner" includeSource="true" type="InstallableUnit">
			<repository location="https://github.com/himi/p2-update-puml-sysmlv2/raw/main/updates"/>
			<unit id="net.sourceforge.plantuml.ecore.feature.feature.group" version="1.1.25.202211040339"/>
			<unit id="net.sourceforge.plantuml.feature.feature.group" version="1.1.25.202211040339"/>
		</location>
		<location includeAllPlatforms="false" includeConfigurePhase="true" includeMode="planner" includeSource="true" type="InstallableUnit">
			<repository location="https://download.eclipse.org/xpect/updates/nightly/latest/"/>
			<unit id="org.eclipse.xpect.sdk.feature.group" version="0.0.0"/>
		</location>
	</locations>
	<targetJRE path="org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-21"/>
</target>
````
