# NOMAGIC ATTACHMENT: TestSimulationCommandLine.zip

- attachment_id: `189153139`
- space_key: `CST2024xR2`
- parent_page_id: `189153134`
- parent_page_title: Using simulation command line and showing test results through Jenkins
- media_type: `application/zip`
- reported_bytes: 548744
- download_url: https://docs.nomagic.com/download/attachments/189153134/TestSimulationCommandLine.zip?version=1&modificationDate=1728045566793&api=v2
- payload_kind: `archive-expanded`
- downloaded_sha256: `bf12c8093e1a97c25ad85c1edcd5415770bd0f89b31c357e000ad9fc53700165`

## ARCHIVE CONTENTS

### ENTRY: TestSimulationCommandLine/lib/hamcrest-core-1.3.jar

- bytes: 45024
- crc32: `ac772733`
- sha256: `66fdef91e9739348df7a096aa384a5685f4e875584cce89386a7a47251c4d8e9`
- payload_status: binary metadata only

### ENTRY: TestSimulationCommandLine/lib/junit-4.12.jar

- bytes: 314932
- crc32: `50cb8f45`
- sha256: `59721f0805e223d84b90677887d9ff567dc534d7c502ca903c0c2b17f05c116a`
- payload_status: binary metadata only

### ENTRY: TestSimulationCommandLine/lib/TestSimulationCommandLine.jar

- bytes: 4308
- crc32: `f9f8cc2f`
- sha256: `b1c4326cd37bee2c0b1ec2740fda1a34c2d52911d3630db406b7a6363034010a`
- payload_status: binary metadata only

### ENTRY: TestSimulationCommandLine/run_junit.xml

- bytes: 1396
- crc32: `cbe2d988`
- decoded_as: `utf-8`

````xml
<project name="Run JUnit and Generate Reports" default="build" basedir=".">

	<target name="build" depends="set.properties, prepare, run.junit" />
	
	<target name="set.properties">
		<property name="md.root" location="${md.root}" />
		<property name="properties.files.dir" location="${properties.files.dir}" />
		<property name="test.reports.dir" location="test-reports"/>
	</target>
	
	<target name="prepare">
		<delete dir="${test.reports.dir}" />
		<mkdir dir="${test.reports.dir}" />
	</target>
	
	<target name="run.junit">
		<junit printsummary="yes" fork="yes">
			<classpath>
				<pathelement location="lib/TestSimulationCommandLine.jar"/>
				<pathelement location="lib/junit-4.12.jar"/>
				<pathelement location="lib/hamcrest-core-1.3.jar"/>
			</classpath>
			<jvmarg value="-Xmx1200m" />
			<jvmarg value="-Xms256m" />
			<jvmarg value="-XX:PermSize=128M" />
			<jvmarg value="-XX:MaxPermSize=256M" />
			<jvmarg value="-XX:-UseSplitVerifier" />
			<jvmarg value="-noverify" />

			<sysproperty key="md.root" value="${md.root}" />
			<sysproperty key="properties.files.dir" value="${properties.files.dir}" />

			<batchtest todir="${test.reports.dir}">
				<zipfileset src="lib/TestSimulationCommandLine.jar">
					<include name="**/*.class"/>
				</zipfileset>
			</batchtest>

			<formatter type="xml" />
		</junit>
	</target>

</project>

````

### ENTRY: TestSimulationCommandLine/test-reports/TEST-com.nomagic.magicdraw.simulation.TestSimulationCommandLine.xml

- bytes: 9378
- crc32: `a7e86d9c`
- decoded_as: `utf-8`

````xml
<?xml version="1.0" encoding="UTF-8" ?>
<testsuite errors="0" failures="1" hostname="chanon-s-2.local" name="com.nomagic.magicdraw.simulation.TestSimulationCommandLine" skipped="0" tests="2" time="87.313" timestamp="2018-09-07T09:48:25">
  <properties>
    <property name="java.vendor" value="Oracle Corporation" />
    <property name="sun.java.launcher" value="SUN_STANDARD" />
    <property name="sun.management.compiler" value="HotSpot 64-Bit Tiered Compilers" />
    <property name="os.name" value="Mac OS X" />
    <property name="sun.boot.class.path" value="/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/resources.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/rt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/sunrsasign.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/jsse.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/jce.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/charsets.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/jfr.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/classes" />
    <property name="test.reports.dir" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/test-reports" />
    <property name="user.country.format" value="TH" />
    <property name="java.vm.specification.vendor" value="Oracle Corporation" />
    <property name="ant.home" value="/Applications/apache-ant-1.9.5" />
    <property name="java.runtime.version" value="1.8.0_102-b14" />
    <property name="user.name" value="chanon_s" />
    <property name="properties.files.dir" value="tests" />
    <property name="user.language" value="en" />
    <property name="sun.boot.library.path" value="/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib" />
    <property name="ant.project.default-target" value="build" />
    <property name="DISPLAY" value="/tmp/launch-xddVu3/org.macosforge.xquartz:0" />
    <property name="ant.project.name" value="Run JUnit and Generate Reports" />
    <property name="java.version" value="1.8.0_102" />
    <property name="user.timezone" value="" />
    <property name="sun.arch.data.model" value="64" />
    <property name="http.nonProxyHosts" value="local|*.local|169.254/16|*.169.254/16" />
    <property name="java.endorsed.dirs" value="/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/endorsed" />
    <property name="sun.cpu.isalist" value="" />
    <property name="sun.jnu.encoding" value="UTF-8" />
    <property name="file.encoding.pkg" value="sun.io" />
    <property name="md.root" value="/Volumes/Data/MDs/190/fp1/MagicDraw_190_no_install" />
    <property name="ant.file.type.Run JUnit and Generate Reports" value="file" />
    <property name="file.separator" value="/" />
    <property name="java.specification.name" value="Java Platform API Specification" />
    <property name="java.class.version" value="52.0" />
    <property name="user.country" value="US" />
    <property name="java.home" value="/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre" />
    <property name="java.vm.info" value="mixed mode" />
    <property name="ant.file" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/run_junit.xml" />
    <property name="os.version" value="10.9.5" />
    <property name="path.separator" value=":" />
    <property name="java.vm.version" value="25.102-b14" />
    <property name="ant.library.dir" value="/Applications/apache-ant-1.9.5/lib" />
    <property name="java.awt.printerjob" value="sun.lwawt.macosx.CPrinterJob" />
    <property name="sun.io.unicode.encoding" value="UnicodeBig" />
    <property name="awt.toolkit" value="sun.lwawt.macosx.LWCToolkit" />
    <property name="socksNonProxyHosts" value="local|*.local|169.254/16|*.169.254/16" />
    <property name="ftp.nonProxyHosts" value="local|*.local|169.254/16|*.169.254/16" />
    <property name="ant.file.Run JUnit and Generate Reports" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/run_junit.xml" />
    <property name="user.home" value="/Users/chanon_s" />
    <property name="java.specification.vendor" value="Oracle Corporation" />
    <property name="java.library.path" value="/Applications/MATLAB_R2015b.app/bin/maci64:/Applications/MATLAB_R2015b.app/runtime/maci64:/Users/chanon_s/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:." />
    <property name="java.vendor.url" value="http://java.oracle.com/" />
    <property name="java.vm.vendor" value="Oracle Corporation" />
    <property name="gopherProxySet" value="false" />
    <property name="java.runtime.name" value="Java(TM) SE Runtime Environment" />
    <property name="sun.java.command" value="org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner com.nomagic.magicdraw.simulation.TestSimulationCommandLine skipNonTests=false filtertrace=true haltOnError=false haltOnFailure=false formatter=org.apache.tools.ant.taskdefs.optional.junit.SummaryJUnitResultFormatter showoutput=false outputtoformatters=true logfailedtests=true threadid=0 logtestlistenerevents=false formatter=org.apache.tools.ant.taskdefs.optional.junit.XMLJUnitResultFormatter,/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/test-reports/TEST-com.nomagic.magicdraw.simulation.TestSimulationCommandLine.xml crashfile=/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/junitvmwatcher6952756613659762042.properties propsfile=/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/junit5509140912686096467.properties" />
    <property name="java.class.path" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/lib/TestSimulationCommandLine.jar:/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/lib/junit-4.12.jar:/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/lib/hamcrest-core-1.3.jar:/Applications/apache-ant-1.9.5/lib/junit-4.12.jar:/Applications/apache-ant-1.9.5/lib/ant-launcher.jar:/Applications/apache-ant-1.9.5/lib/ant.jar:/Applications/apache-ant-1.9.5/lib/ant-junit.jar:/Applications/apache-ant-1.9.5/lib/ant-junit4.jar" />
    <property name="ant.version" value="Apache Ant(TM) version 1.9.5 compiled on May 31 2015" />
    <property name="java.vm.specification.name" value="Java Virtual Machine Specification" />
    <property name="ant.file.type" value="file" />
    <property name="java.vm.specification.version" value="1.8" />
    <property name="sun.cpu.endian" value="little" />
    <property name="sun.os.patch.level" value="unknown" />
    <property name="java.io.tmpdir" value="/var/folders/p6/xpvtqrln2nz8sn2plr01qhv80000gp/T/" />
    <property name="java.vendor.url.bug" value="http://bugreport.sun.com/bugreport/" />
    <property name="os.arch" value="x86_64" />
    <property name="java.awt.graphicsenv" value="sun.awt.CGraphicsEnvironment" />
    <property name="java.ext.dirs" value="/Users/chanon_s/Library/Java/Extensions:/Library/Java/JavaVirtualMachines/jdk1.8.0_102.jdk/Contents/Home/jre/lib/ext:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java" />
    <property name="user.dir" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine" />
    <property name="line.separator" value="&#xa;" />
    <property name="java.vm.name" value="Java HotSpot(TM) 64-Bit Server VM" />
    <property name="basedir" value="/Volumes/Data/jenkins/workspace/TestSimulationCommandLine" />
    <property name="ant.java.version" value="1.8" />
    <property name="ant.core.lib" value="/Applications/apache-ant-1.9.5/lib/ant.jar" />
    <property name="file.encoding" value="UTF-8" />
    <property name="java.specification.version" value="1.8" />
    <property name="ant.project.invoked-targets" value="build" />
  </properties>
  <testcase classname="com.nomagic.magicdraw.simulation.TestSimulationCommandLine" name="testGenerateFailResult" time="49.266">
    <failure message="Starting MagicDraw...&#xa;fail&#xa;" type="junit.framework.AssertionFailedError">junit.framework.AssertionFailedError: Starting MagicDraw...
fail

	at com.nomagic.magicdraw.simulation.TestSimulationCommandLine.testGenerateFailResult(TestSimulationCommandLine.java:71)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.lang.Thread.run(Thread.java:745)
</failure>
  </testcase>
  <testcase classname="com.nomagic.magicdraw.simulation.TestSimulationCommandLine" name="testGeneratePassResult" time="37.957" />
  <system-out><![CDATA[md.root=/Volumes/Data/MDs/190/fp1/MagicDraw_190_no_install
properties.files.dir=tests
Executing, command=/Volumes/Data/MDs/190/fp1/MagicDraw_190_no_install/plugins/com.nomagic.magicdraw.simulation/simulate.sh -properties "/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/tests/TestGenerateFailResult.properties"
md.root=/Volumes/Data/MDs/190/fp1/MagicDraw_190_no_install
properties.files.dir=tests
Executing, command=/Volumes/Data/MDs/190/fp1/MagicDraw_190_no_install/plugins/com.nomagic.magicdraw.simulation/simulate.sh -properties "/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/tests/TestGeneratePassResult.properties"
Console output=Starting MagicDraw...
pass

]]></system-out>
  <system-err><![CDATA[]]></system-err>
</testsuite>

````

### ENTRY: TestSimulationCommandLine/tests/TestGenerateFailResult.properties

- bytes: 123
- crc32: `b1996d58`
- decoded_as: `utf-8`

````text
project=/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/tests/TestVerdictKind.mdzip
config=Run GenerateFailResult
````

### ENTRY: TestSimulationCommandLine/tests/TestGeneratePassResult.properties

- bytes: 123
- crc32: `e7c45d33`
- decoded_as: `utf-8`

````text
project=/Volumes/Data/jenkins/workspace/TestSimulationCommandLine/tests/TestVerdictKind.mdzip
config=Run GeneratePassResult
````

### ENTRY: TestSimulationCommandLine/tests/TestVerdictKind.mdzip

- bytes: 224360
- crc32: `382b1187`
- sha256: `049d1b86d0085ad1fb3fc941ad06272ed8d75e8583753ab2fe3e0e7dc90ae465`
- payload_status: binary metadata only


## EXACT ATTACHMENT METADATA

````json
{
  "id": "189153139",
  "type": "attachment",
  "status": "current",
  "title": "TestSimulationCommandLine.zip",
  "version": {
    "by": {
      "type": "known",
      "username": "2c9f81f85d3bb686015e3865fafa0000",
      "userKey": "2c9f81f85d3bb686015e3865fafa0000",
      "profilePicture": {
        "path": "/images/icons/profilepics/default.svg",
        "width": 48,
        "height": 48,
        "isDefault": true
      },
      "displayName": "user-52ec1",
      "_links": {
        "self": "https://docs.nomagic.com/rest/api/user?key=2c9f81f85d3bb686015e3865fafa0000"
      },
      "_expandable": {
        "status": ""
      }
    },
    "when": "2024-10-04T14:39:26.793+02:00",
    "message": "",
    "number": 1,
    "minorEdit": true,
    "hidden": false,
    "_links": {
      "self": "https://docs.nomagic.com/rest/experimental/content/189153139/version/1"
    },
    "_expandable": {
      "content": "/rest/api/content/189153139"
    }
  },
  "position": -1,
  "container": {
    "id": "189153134",
    "type": "page",
    "status": "current",
    "title": "Using simulation command line and showing test results through Jenkins",
    "position": 4,
    "extensions": {
      "position": 4
    },
    "_links": {
      "webui": "/spaces/CST2024xR2/pages/189153134/Using+simulation+command+line+and+showing+test+results+through+Jenkins",
      "edit": "/pages/resumedraft.action?draftId=189153134",
      "tinyui": "/x/bj9GCw",
      "self": "https://docs.nomagic.com/rest/api/content/189153134"
    },
    "_expandable": {
      "container": "/rest/api/space/CST2024xR2",
      "metadata": "",
      "operations": "",
      "children": "/rest/api/content/189153134/child",
      "restrictions": "/rest/api/content/189153134/restriction/byOperation",
      "history": "/rest/api/content/189153134/history",
      "ancestors": "",
      "body": "",
      "version": "",
      "descendants": "/rest/api/content/189153134/descendant",
      "space": "/rest/api/space/CST2024xR2",
      "relevantViewRestrictions": "/rest/api/content/189153134/restriction/relevantViewRestrictions"
    }
  },
  "metadata": {
    "mediaType": "application/zip"
  },
  "extensions": {
    "mediaType": "application/zip",
    "fileSize": 548744,
    "comment": ""
  },
  "_links": {
    "download": "/download/attachments/189153134/TestSimulationCommandLine.zip?version=1&modificationDate=1728045566793&api=v2",
    "webui": "/spaces/CST2024xR2/pages/189153134/Using+simulation+command+line+and+showing+test+results+through+Jenkins?preview=%2F189153134%2F189153139%2FTestSimulationCommandLine.zip",
    "self": "https://docs.nomagic.com/rest/api/content/189153139"
  },
  "_expandable": {
    "operations": "",
    "children": "/rest/api/content/189153139/child",
    "restrictions": "/rest/api/content/189153139/restriction/byOperation",
    "history": "/rest/api/content/189153139/history",
    "ancestors": "",
    "body": "",
    "descendants": "/rest/api/content/189153139/descendant",
    "space": "/rest/api/space/CST2024xR2",
    "relevantViewRestrictions": "/rest/api/content/189153139/restriction/relevantViewRestrictions"
  }
}
````
