# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.xpect.tests/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.xpect.tests/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.xpect.tests/pom.xml
- source_bytes: 1779
- source_sha256: `316af0d64c20da47016c7615cc4d742b4df70fb1f2391a1e06111979dbc1d836`
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

	<artifactId>org.omg.sysml.xpect.tests</artifactId>
	<!-- ST6RI-318 This should not be an eclipse-test-plugin as tests are known not working in Eclipse environments -->
	<packaging>eclipse-plugin</packaging>

	<build>
		<!-- The test directory setting ensures that test classes and xpect test descriptors are found correctly by the JUnit test runner -->
		<testOutputDirectory>target/classes</testOutputDirectory>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<version>${junit.version}</version>
				<configuration>
					<includes>
						<include>**/AllSysMLXpectTests.java</include>
					</includes>
					<testSourceDirectory>src</testSourceDirectory>
                                        <argLine>-Dfile.encoding=UTF-8</argLine>
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
					<!--  This additional dependency is required for the test cases to be found by surefire -->
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
