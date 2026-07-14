# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.execution/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.execution/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.execution/pom.xml
- source_bytes: 800
- source_sha256: `d76cfb88af20fe297c204c18f196487046e0b693389a95f9c0440452ee9dce34`
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

	<artifactId>org.omg.sysml.execution</artifactId>
	<packaging>eclipse-plugin</packaging>
	
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
		</plugins>
	</build>
</project>
````
