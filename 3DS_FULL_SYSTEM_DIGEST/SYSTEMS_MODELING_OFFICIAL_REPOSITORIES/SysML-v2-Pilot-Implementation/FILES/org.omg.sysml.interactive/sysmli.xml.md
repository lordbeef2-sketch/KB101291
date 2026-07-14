# OFFICIAL REPOSITORY FILE: SysML-v2-Pilot-Implementation/org.omg.sysml.interactive/sysmli.xml

- repository: `SysML-v2-Pilot-Implementation`
- source_path: `org.omg.sysml.interactive/sysmli.xml`
- source_url: https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/fa709f28dfd49dfdb7ee83e4e19da2f57e0eb3aa/org.omg.sysml.interactive/sysmli.xml
- source_bytes: 1453
- source_sha256: `419a87be844c8d5a649a3ae45b3b200ce70245178671cf1a356018550569b5ab`
- decoded_as: `utf-8`


## EXACT SOURCE

````xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<project default="create_jar" name="Create a fat jar for SysMLv2">
  <property name="project.build.directory" value="${basedir}/target"/>
  <property name="dir.buildfile" value="${project.build.directory}"/>
  <property name="dir.classes" value="${dir.buildfile}/classes"/>
  <property name="dir.libs" value="${dir.buildfile}/libs"/>
  <property name="jar.file" value="${dir.jarfile}/${jar.filename}"/>

  <path id="sysmlv2api-id">
    <fileset dir="${basedir}/../org.omg.sysml/lib"> 
      <include name="sysml-v2-api-*.jar"/> 
    </fileset>
  </path>
  <property name="sysmlv2api.jar" refid="sysmlv2api-id"/> 

  <target name="create_jar">
    <concat destfile="${dir.classes}/plugin.properties" fixlastline="yes" eol="unix">
      <fileset dir="${dir.libs}">
        <include name="*/plugin.properties"/>
      </fileset>
    </concat>
    <jar destfile="${jar.file}" update="true">
      <manifest>
        <attribute name="Main-Class" value="${main.class}" />
      </manifest>
      <fileset dir="${dir.classes}"/>
      <zipfileset src="${sysmlv2api.jar}"/>

      <mappedresources>
        <fileset dir="${dir.libs}">
          <exclude name="**/lib/sysml-v2-api-*.jar"/>
        </fileset>
        <regexpmapper from="^[^/]*/(plantuml-epl-[^/]*/)?([A-Za-z]*/.*)" to="\2" handledirsep="yes"/>
      </mappedresources>
    </jar>
  </target>
</project>

````
