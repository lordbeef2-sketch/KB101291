# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.model/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.model/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.model/pom.xml
- source_bytes: 1008
- source_sha256: `698c0e7659a9b3dbc45e33f5f75e493b0041ebc911639b670e0c4fc2b52efef0`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

	<modelVersion>4.0.0</modelVersion>

	<parent>
		<groupId>org.omg.sysml</groupId>
		<artifactId>org.omg.sysml.parent</artifactId>
		<version>${revision}</version>
	</parent>

	<artifactId>org.omg.sysml.model</artifactId>
	<packaging>jar</packaging>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.eclipse.emf</groupId>
			<artifactId>org.eclipse.emf.common</artifactId>
			<version>2.45.0</version>
		</dependency>
		<dependency>
			<groupId>org.eclipse.emf</groupId>
			<artifactId>org.eclipse.emf.ecore</artifactId>
			<version>2.42.0</version>
		</dependency>
	</dependencies>
</project>

````
