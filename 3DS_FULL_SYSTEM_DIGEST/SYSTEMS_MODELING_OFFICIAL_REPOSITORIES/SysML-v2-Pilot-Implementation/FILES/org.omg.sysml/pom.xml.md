# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml/pom.xml
- source_bytes: 1270
- source_sha256: `c97b6760ffe390b93d537a97ef7d243ebbc3b62d44f911c2c5b9c8e7eb2e0a3a`
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

	<artifactId>org.omg.sysml</artifactId>
	<packaging>eclipse-plugin</packaging>

	<dependencies>
		<dependency>
			<groupId>org.omg.sysml</groupId>
			<artifactId>org.omg.sysml.model.bundle</artifactId>
			<version>${revision}</version>
		</dependency>
		<dependency>
			<groupId>org.omg.sysml</groupId>
			<artifactId>org.omg.sysml.logic.bundle</artifactId>
			<version>${revision}</version>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-clean-plugin</artifactId>
				<executions>
					<execution>
						<id>gen-clean</id>
						<phase>clean</phase>
					</execution>
				</executions>
			</plugin>
			<plugin>
				<groupId>org.eclipse.xtend</groupId>
				<artifactId>xtend-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>

````
