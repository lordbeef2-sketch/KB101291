# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.jupyter.kernel/assembly.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.jupyter.kernel/assembly.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.jupyter.kernel/assembly.xml
- source_bytes: 1024
- source_sha256: `8d093b9bd7b2da11e23b96a4fb9145dc32c4ff3cacd1d0e9a491f05d4b755655`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<assembly xmlns="http://maven.apache.org/ASSEMBLY/2.1.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/ASSEMBLY/2.1.0 http://maven.apache.org/xsd/assembly-2.1.0.xsd">
    <id>installer</id>
    <formats>
        <format>zip</format>
    </formats>
    <includeBaseDirectory>false</includeBaseDirectory>
    <fileSets>
		<!-- Include licence -->
        <fileSet>
            <directory>${project.basedir}/..</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>LICENSE</include>
                <include>LICENSE-GPL</include>
            </includes>
        </fileSet>
        <!-- zip the kernel -->
        <fileSet>
            <directory>${project.basedir}/target/kernel</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>*/**</include>
            </includes>
        </fileSet>
    </fileSets>
</assembly>
````
