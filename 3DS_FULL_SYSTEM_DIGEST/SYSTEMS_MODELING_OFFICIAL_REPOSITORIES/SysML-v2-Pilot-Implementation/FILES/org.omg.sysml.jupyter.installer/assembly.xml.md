# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.installer/assembly.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.installer/assembly.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.installer/assembly.xml
- source_bytes: 1447
- source_sha256: `284554b8aa0b1cac417a57d986cb75389a895c5fc30fcf8923090264c567d146`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<assembly xmlns="http://maven.apache.org/ASSEMBLY/2.1.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/ASSEMBLY/2.1.0 http://maven.apache.org/xsd/assembly-2.1.0.xsd">
    <id>installer</id>
    <formats>
        <format>dir</format>
        <format>tar.gz</format>
        <format>zip</format>
    </formats>
    <includeBaseDirectory>false</includeBaseDirectory>
    <fileSets>
        <fileSet>
            <directory>${project.basedir}</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>README*</include>
                <include>LICENSE*</include>
                <include>install.py</include>
            </includes>
        </fileSet>
        <fileSet>
            <directory>${project.basedir}</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>install.bat</include>
                <include>install.sh</include>
            </includes>
            <filtered>true</filtered>
            <fileMode>0755</fileMode>
        </fileSet>
        <fileSet>
            <directory>${project.basedir}/target/generated-docs</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>README.pdf</include>
            </includes>
        </fileSet>
    </fileSets>
</assembly>
````
