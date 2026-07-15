# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.site/pom.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.site/pom.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.site/pom.xml
- source_bytes: 2380
- source_sha256: `862689ed053a0755c439b5922398020fd8ca30ba37f6f21eba6463fc9104276f`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
         xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>org.omg.sysml</groupId>
    <artifactId>org.omg.sysml.parent</artifactId>
    <version>${revision}</version>
  </parent>
  <artifactId>org.omg.sysml.site</artifactId>

  <packaging>eclipse-repository</packaging>
  <build>
    <plugins>
      <plugin>
        <groupId>org.asciidoctor</groupId>
        <artifactId>asciidoctor-maven-plugin</artifactId>
        <version>${asciidoctor.maven.plugin.version}</version>
        <inherited>false</inherited>
        <dependencies>
          <dependency>
            <groupId>org.asciidoctor</groupId>
            <artifactId>asciidoctorj-pdf</artifactId>
            <version>${asciidoctorj.pdf.version}</version>
          </dependency>
        </dependencies>
        <configuration>
          <sourceDocumentName>README.adoc</sourceDocumentName>
          <sourceDirectory>${basedir}</sourceDirectory>
          <resources>
          	<!--
          	  This resource configuration is necessary as the readme file is in the project
          	  root and the default resource behaviour would cause asciidoctor to copy all files
          	  in the project without these exclusion rules
          	-->
            <resource>
              <directory>.</directory>
              <excludes>
	              <exclude>**/**</exclude>
              </excludes>
            </resource>
          </resources>
        </configuration>
        <executions>
          <execution>
            <id>generate-pdf-doc</id>
            <phase>generate-resources</phase>
            <goals>
              <goal>process-asciidoc</goal>
            </goals>
            <configuration>
              <backend>pdf</backend>
              <attributes>
                <source-highlighter>rogue</source-highlighter>
                <icons>font</icons>
                <pagenums />
                <idprefix />
                <idseparator>-</idseparator>
              </attributes>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
````
