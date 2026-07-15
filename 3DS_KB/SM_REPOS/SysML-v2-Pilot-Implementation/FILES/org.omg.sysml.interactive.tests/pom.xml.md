# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.interactive.tests/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.interactive.tests/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.interactive.tests/pom.xml
- source_bytes: 1759
- source_sha256: `246cb1e5437d41b8d3a666d4b408fd81588c0e6eb95b54b71032b2e7f7af7ce9`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<properties>
		<sysml.library.path>${project.build.directory}/../../sysml.library</sysml.library.path>
	</properties>
	
	<modelVersion>4.0.0</modelVersion>

	<parent>
		<groupId>org.omg.sysml</groupId>
		<artifactId>org.omg.sysml.parent</artifactId>
		<version>${revision}</version>
	</parent>

	<artifactId>org.omg.sysml.interactive.tests</artifactId>
	
	<packaging>eclipse-plugin</packaging>
	
	<build>
		<sourceDirectory>src</sourceDirectory>
		<testOutputDirectory>target/classes</testOutputDirectory>
		<plugins>
			<plugin>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>3.8.1</version>
				<configuration>
					<source>1.8</source>
					<target>1.8</target>
				</configuration>
			</plugin>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<version>${junit.version}</version>
				<configuration>
					<systemPropertyVariables>
						<libraryPath>${sysml.library.path}</libraryPath>
					</systemPropertyVariables>
					<testSourceDirectory>src</testSourceDirectory>
				</configuration>
				<executions>
					<execution>
						<phase>test</phase>
						<goals>
							<goal>test</goal>
						</goals>
					</execution>
				</executions>
				<dependencies>
					<dependency>
						<groupId>org.apache.maven.surefire</groupId>
						<artifactId>surefire-junit47</artifactId>
						<version>${junit.version}</version>
					</dependency>
				</dependencies>
			</plugin>
		</plugins>
	</build>
</project>
````
