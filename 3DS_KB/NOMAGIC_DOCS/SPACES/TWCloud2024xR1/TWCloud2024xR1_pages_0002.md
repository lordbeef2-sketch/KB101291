# NOMAGIC DOCUMENTATION SPACE: Teamwork Cloud and Services 2024x Refresh1

<!--NOMAGIC_SPACE key=TWCloud2024xR1 chunk=2 -->

<!--NOMAGIC_PAGE id=170491221 space=TWCloud2024xR1 version=1 -->
## PAGE 00137: Installing Cassandra on Windows

- page_id: `170491221`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491221/Installing+Cassandra+on+Windows
- version_number: 1
- version_date: `2024-03-22T12:27:58.747+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Windows
- labels: []

### NORMALIZED CONTENT

**On this page**

**Downloads**

[ATTACHMENT filename='CustomTWC_Cassandra4_DockerImg.zip']

#### WARNING: Important! Cassandra is not supported on Windows!

Important! Cassandra is not supported on Windows!

We do not provide support for Cassandra installations on Windows as those installations are not natively supported by Apache. **We strongly recommend using Linux deployments.**The information below is provided as a courtesy only.

One option for running Cassandra 4.1 on Windows is Docker. See [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/) for official installation instructions.

Additional resources:

- https://hub.docker.com/_/cassandra/ – official Cassandra Docker image
- https://docs.docker.com/ – Docker documentation
- https://github.com/apache/cassandra/blob/cassandra-4.1/NEWS.txt – Cassandra’s migration notes

##### Docker Cassandra basics

This section provides the basics for starting a Docker Cassandra 4.1 container, for testing purposes only. For production deployment, we recommend generating a custom Docker image as described in the section [Custom Docker Cassandra image for Teamwork Cloud](#InstallingCassandraonWindows-CustomDockerCassandraimageforTeamworkCloud).

Start an instance of the official Cassandra 4.1 Docker image by executing this command:

```bash

```

| Parameter | Value | Description |
| --- | --- | --- |
| --name | cassandra4_test | User-defined container instance name. This is an optional parameter. The name must be unique and cannot be the same as the official Docker image name. |
| -v | e:/cassandra/data/:/var/lib/cassandra | Mount an external drive to a path in the Docker container instance. /var/lib/cassandra is the default Cassandra path for data and commit log storage. An external drive must be mounted for permanent data storage. |
| -d |  | Detach and run in the background. |
| -p | 9042:9042 | Publish port 9042 to Windows host. 9042 is the native client port. |
| [image name]:version | cassandra:4.1.3 | Pull the official Apache Cassandra 4.1 Docker image for this running instance. |

If this is a new Docker installation, the first **docker run** execution downloads the Cassandra image to the local system.

To access logs:

```bash
]]>
```

To access nodetool (or other tools):

```bash
nodetool status]]>
```

Newer Java versions require the **-Dcom.sun.jndi.rmiURLParsing=legacy** option. If the “Malformed IPv6 address” error occurs, use:

```bash
nodetool -Dcom.sun.jndi.rmiURLParsing=legacy status]]>
```

Docker instances are ephemeral by design. If an instance terminates or is deleted, all data, logs, and configuration files modified inside the instance are lost.

##### Custom Docker Cassandra image for Teamwork Cloud

Production deployment of Cassandra 4.1 on Windows requires modifying system configurations. Therefore, a custom Docker image must be created with the configuration changes. This section covers setting up and running a custom Docker image. Details of the configuration changes are discussed in section [Cassandra configuration](#InstallingCassandraonWindows-Cassandraconfiguration).

1. Download and extract the [ZIP file](https://docs.nomagic.com/download/attachments/137986348/CustomTWC_Cassandra4_DockerImg.zip?version=1&modificationDate=1695376234919&api=v2) package into an empty working directory.
2. Execute the following command to build the custom Docker image named *cassandra4_twc*: bashDJangotrue
3. Start an instance of the custom Docker Cassandra 4.1 image you just built: bashDJangotrue The data and commit log directories are mounted separately, to different paths.

With the custom Docker Cassandra instance running and mounted to permanent storage, the database is ready to connect to your Teamwork Cloud installation.

If more configuration changes are needed, the running instance has to be terminated and a new Docker image needs to be built. Edit the configuration file from the working directory in Step 1. Proceed with steps 2-3 to redeploy the Cassandra node on Windows.

##### Cassandra configuration

This section is a summary of the configuration changes to optimize Docker Cassandra deployment for Teamwork Cloud. If additional configuration changes are needed, the Docker Cassandra image has to be rebuilt. All configuration files are located in */etc/cassandra*.

Synchronize the CPU clocks on all Cassandra cluster nodes. Otherwise, you may encounter issues when creating an empty Cassandra cluster.

###### Modification of the *cassandra.yaml* file

If the new Cassandra 4.x node is going to access existing data from a Cassandra 3.x database, please make a note of the previous **cluster_name** and **num_tokens**settings. These parameters must match in the new Cassandra 4.1 *cassandra.yaml* configuration.

The following parameters are for controlling thresholds to ensure that the data being sent is processed properly.

```bash

```

```bash

```

Ensure that the default commit log size is 8GB (recommended).

```bash

```

```bash

```

Point the data to the appropriate locations.

```text

```

###### JVM configuration for Cassandra Node

To change the amount of RAM used by Cassandra, activate the -Xms4G and -Xmx4g properties in *jvm-server.options* (remove leading ‘#’) and specify their values. By default, Cassandra uses no more than 8 GB of RAM.

- In the jvm11-server.options and jvm8-server.options files, CMS Settings are disabled.
- In the jvm11-server.options and jvm8-server.options files, the parameters below are activated

```text

```

- In the jvm11-server.options and jvm8-server.options files, the two parameters below are set to the physical CPU core count (the values of both parameters should be the same):

```text

```

- In the jvm8-server.options file, disable all GC logging options.
- In the logback.xml file, disable debug.log by commenting out "<appender-ref ref="ASYNCDEBUGLOG" />"

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:macro-id="d5def57e-211a-467e-802c-8dd688e3c0a5" ac:name="toc" ac:schema-version="1" /></p></ac:layout-cell><ac:layout-cell><p><strong>Downloads</strong></p><p><ac:link><ri:attachment ri:filename="CustomTWC_Cassandra4_DockerImg.zip"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Installing Cassandra on Windows" /></ri:attachment></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><ac:structured-macro ac:macro-id="cd476f02-b3fd-4b2e-8de2-dbc909dd4aab" ac:name="warning" ac:schema-version="1"><ac:parameter ac:name="title">Important! Cassandra is not supported on Windows!</ac:parameter><ac:rich-text-body><p>We do not provide support for Cassandra installations on Windows as those installations are not natively supported by Apache. <strong>We strongly recommend using Linux deployments. </strong>The information below is provided as a courtesy only.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">O</span></span><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">ne option for running Cassandra 4.1 on Windows is Docker. See <a href="https://docs.docker.com/desktop/install/windows-install/">Install Docker Desktop on Windows</a> for official installation instructions</span>.</span></p><ac:structured-macro ac:macro-id="cb6a4db7-8911-4629-a4fd-65794d703b8f" ac:name="info" ac:schema-version="1"><ac:rich-text-body><p>Additional resources:</p><ul><li><a class="external-link" href="https://hub.docker.com/_/cassandra/">https://hub.docker.com/_/cassandra/</a><span> <span style="color: rgb(59,62,77);">–</span></span> official Cassandra Docker image</li><li><a class="external-link" href="https://docs.docker.com/">https://docs.docker.com/</a><span> <span style="color: rgb(59,62,77);">–</span></span> Docker documentation</li><li><a href="https://github.com/apache/cassandra/blob/cassandra-4.1/NEWS.txt">https://github.com/apache/cassandra/blob/cassandra-4.1/NEWS.txt</a> <span style="color: rgb(59,62,77);">–</span> Cassandra’s migration notes</li></ul></ac:rich-text-body></ac:structured-macro><h3>Docker Cassandra basics</h3><p><span>This section provides the basics for starting a Docker Cassandra 4.1 container, for testing purposes only. For production deployment, we recommend generating a custom Docker image as described in the section <a href="#InstallingCassandraonWindows-CustomDockerCassandraimageforTeamworkCloud">Custom Docker Cassandra image for Teamwork Cloud</a>.</span></p><p><span>Start an instance of the official Cassandra 4.1 Docker image by executing this command:</span></p><ac:structured-macro ac:macro-id="93b36dcb-6670-47a7-b42a-201e8de1defb" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker run --name cassandra4_test –p 9042:9042 –v e:\cassandra\data:/var/lib/cassandra -d cassandra:4.1.3]]></ac:plain-text-body></ac:structured-macro><p><br /></p><table><colgroup> <col /> <col /> <col /> </colgroup><tbody><tr><td><p><strong>Parameter</strong></p></td><td><p><strong>Value</strong></p></td><td><p><strong>Description</strong></p></td></tr><tr><td><p>--name</p></td><td><p>cassandra4_test</p></td><td><p>User-defined container instance name. This is an optional parameter. The name must be unique and cannot be the same as the official Docker image name.</p></td></tr><tr><td><p>-v</p></td><td><p>e:/cassandra/data/:/var/lib/cassandra</p></td><td><p>Mount an external drive to a path in the Docker container instance. <em>/var/lib/cassandra</em> is the default Cassandra path for data and commit log storage. An external drive must be mounted for permanent data storage.</p></td></tr><tr><td><p>-d</p></td><td><br /></td><td><p>Detach and run in the background.</p></td></tr><tr><td><p>-p</p></td><td><p>9042:9042</p></td><td><p>Publish port 9042 to Windows host. 9042 is the native client port.</p></td></tr><tr><td><p>[image name]:version</p></td><td><p>cassandra:4.1.3</p></td><td><p>Pull the official Apache Cassandra 4.1 Docker image for this running instance.</p></td></tr></tbody></table><p><br /></p><ac:structured-macro ac:macro-id="407abb9f-f047-4bde-b701-4c0df16c5e8c" ac:name="note" ac:schema-version="1"><ac:rich-text-body><p>If this is a new Docker installation, the first <strong>docker run</strong> execution downloads the Cassandra image to the local system.</p></ac:rich-text-body></ac:structured-macro><p><span>To access logs:</span></p><ac:structured-macro ac:macro-id="0ee4f42b-5383-4f6c-8263-8ecdb77c87d4" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker logs <container name or ID>]]></ac:plain-text-body></ac:structured-macro><p><span>To access nodetool (or other tools):</span></p><ac:structured-macro ac:macro-id="61c9a14a-ca73-47d7-aba3-e4fcd7b5db55" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker exec -it <container name or ID> nodetool status]]></ac:plain-text-body></ac:structured-macro><p><span>Newer Java versions require the <strong>-Dcom.sun.jndi.rmiURLParsing=legacy</strong> option. If the “Malformed IPv6 address” error occurs, use:</span></p><ac:structured-macro ac:macro-id="3d819407-fb99-492e-b896-103aada6fb21" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker exec -it <container name or ID> nodetool -Dcom.sun.jndi.rmiURLParsing=legacy status]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:macro-id="5efaa53d-82fd-4b6e-9307-dd84497bfabc" ac:name="note" ac:schema-version="1"><ac:rich-text-body>Docker instances are ephemeral by design. If an instance terminates or is deleted, all data, logs, and configuration files modified inside the instance are lost.</ac:rich-text-body></ac:structured-macro><h3>Custom Docker Cassandra image for Teamwork Cloud</h3><p><span>Production deployment of Cassandra 4.1 on Windows requires modifying system configurations. Therefore, a custom Docker image must be created with the configuration changes. This section covers setting up and running a custom Docker image. Details of the configuration changes are discussed in section <a href="#InstallingCassandraonWindows-Cassandraconfiguration">Cassandra configuration</a>.</span></p><ol><li><span>Download and extract the <a href="https://docs.nomagic.com/download/attachments/137986348/CustomTWC_Cassandra4_DockerImg.zip?version=1&amp;modificationDate=1695376234919&amp;api=v2">ZIP file</a> package into an empty working directory.</span></li><li><p><span>Execute the <ac:inline-comment-marker ac:ref="3445f840-9a05-4cb8-b339-6c154de833e0">following</ac:inline-comment-marker> command to build the custom Docker image named <em>cassandra4_twc</em>:</span></p><ac:structured-macro ac:macro-id="286a7979-36eb-4e4b-b28e-6e8a59974b1a" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker build –t cassandra4_twc:latest .]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><span>Start an instance of the custom Docker Cassandra 4.1 image you just built:</span></p><ac:structured-macro ac:macro-id="3904ca1e-101c-4e70-aa0f-15bb864a354f" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[docker run –p 9042:9042 –v d:\data:/data –v e:\log\commitlog:/logs/commitlog -d cassandra4_twc:latest]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:macro-id="4106f393-3cdb-47a7-8d9c-657730c6316c" ac:name="info" ac:schema-version="1"><ac:rich-text-body><p>The data and commit log directories are mounted separately, to different paths.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><span>With the custom Docker Cassandra instance running and mounted to permanent storage, the database is ready to connect to your Teamwork Cloud installation.</span></p><p><span>If more configuration changes are needed, the running instance has to be terminated and a new Docker image needs to be built. Edit the configuration file from the working directory in Step 1. Proceed with steps 2-3 to redeploy the Cassandra node on Windows.</span></p><h3>Cassandra configuration</h3><p><span>This section is a summary of the configuration changes to optimize Docker Cassandra deployment for Teamwork Cloud. If additional configuration changes are needed, the Docker Cassandra image has to be rebuilt. All configuration files are located in <em>/etc/cassandra</em>.</span></p><ac:structured-macro ac:macro-id="44bae19f-b953-4a3b-92fe-e38c5a186636" ac:name="info" ac:schema-version="1"><ac:rich-text-body>Synchronize the CPU clocks on all Cassandra cluster nodes. Otherwise, you may encounter issues when creating an empty Cassandra cluster.</ac:rich-text-body></ac:structured-macro><h4><span>Modification of the <em>cassandra.yaml</em> file</span></h4><p><span>If the new Cassandra 4.x node is going to access existing data from a Cassandra 3.x database, please make a note of the previous <strong>cluster_name</strong> and <strong>num_tokens </strong>settings. These parameters must match in the new Cassandra 4.1 <em>cassandra.yaml</em> configuration.</span></p><p><span>The following parameters are for controlling thresholds to ensure that the data being sent is processed properly.</span></p><ac:structured-macro ac:macro-id="03fbd01c-5306-462b-8149-9fd58fc1fcb1" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example (Cassandra 4.0)</ac:parameter><ac:plain-text-body><![CDATA[commitlog_segment_size_in_mb: 192
read_request_timeout_in_ms: 1800000
range_request_timeout_in_ms: 1800000
write_request_timeout_in_ms: 1800000
cas_contention_timeout_in_ms: 1000
truncate_request_timeout_in_ms: 1800000
request_timeout_in_ms: 1800000
batch_size_warn_threshold_in_kb: 3000
batch_size_fail_threshold_in_kb: 5000]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:macro-id="4ea39d10-ff91-4894-b2ef-0cfc8f3ce976" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example (Cassandra 4.1)</ac:parameter><ac:plain-text-body><![CDATA[commitlog_segment_size: 192MiB
read_request_timeout: 1800000ms
range_request_timeout: 1800000ms
write_request_timeout: 1800000ms
cas_contention_timeout: 1000ms
truncate_request_timeout: 1800000ms
request_timeout: 1800000ms
batch_size_warn_threshold: 3000KiB
batch_size_fail_threshold: 5000KiB]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p><span>Ensure that the default commit log size is 8GB (recommended).</span></p><ac:structured-macro ac:macro-id="cc0b951f-a2a4-4aa4-ab91-576995495f7f" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example (Cassandra 4.0)</ac:parameter><ac:plain-text-body><![CDATA[commitlog_total_space_in_mb: 8192]]></ac:plain-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:macro-id="316545b4-5b92-41e3-9e3a-4b782d47f5ec" ac:name="code" ac:schema-version="1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example (Cassandra 4.1)</ac:parameter><ac:plain-text-body><![CDATA[commitlog_total_space: 8192MiB]]></ac:plain-text-body></ac:structured-macro><p><br /></p><p><span>Point the data to the appropriate locations.</span></p><ac:structured-macro ac:macro-id="3e09c508-0aca-4a7f-9f34-32c24dbc41a4" ac:name="code" ac:schema-version="1"><ac:plain-text-body><![CDATA[data_file_directories:
- /data/data
commitlog_directory: /logs/commitlog
hints_directory: /data/hints
saved_caches_directory: /data/saved_caches]]></ac:plain-text-body></ac:structured-macro><h4>JVM configuration for Cassandra Node</h4><p>To change the amount of RAM used by Cassandra, activate the -Xms4G and -Xmx4g properties in <em>jvm-server.options</em> (remove leading ‘#’) and specify their values. By default, Cassandra uses no more than 8 GB of RAM.</p><ul><li>In the <em>jvm11-server.options </em>and <em>jvm8-server.options</em> files, CMS Settings are disabled.</li><li>In the <em>jvm11-server.options </em>and <em>jvm8-server.options</em> files, the parameters below are activated</li></ul><ac:structured-macro ac:macro-id="3c10ca81-73af-4413-8d87-84ed98ffffba" ac:name="code" ac:schema-version="1"><ac:plain-text-body><![CDATA[-XX:+UseG1GC
-XX:MaxGCPauseMillis=500]]></ac:plain-text-body></ac:structured-macro><ul><li>In the <em>jvm11-server.options </em>and <em>jvm8-server.options</em> files, the two parameters below are set to the physical CPU core count (the values of both parameters should be the same):</li></ul><ac:structured-macro ac:macro-id="9d8bb447-5bfe-41d2-838c-176e83bf2c25" ac:name="code" ac:schema-version="1"><ac:plain-text-body><![CDATA[-XX:ParallelGCThreads=16
-XX:ConcGCThreads=16]]></ac:plain-text-body></ac:structured-macro><ul><li>In the <em>jvm8-server.options </em>file, disable all GC logging options.</li><li>In the logback.xml file, disable debug.log by commenting out &quot;&lt;appender-ref ref=&quot;ASYNCDEBUGLOG&quot; /&gt;&quot;</li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=225350113 space=TWCloud2024xR1 version=3 -->
## PAGE 00138: Installing Microsoft TrueType fonts for Document Exporter

- page_id: `225350113`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/225350113/Installing+Microsoft+TrueType+fonts+for+Document+Exporter
- version_number: 3
- version_date: `2025-05-14T12:03:49.968+02:00`
- ancestors: Teamwork Cloud and Services > Administration Guide > Cameo Collaborator for Teamwork Cloud Administration
- labels: []

### NORMALIZED CONTENT

**On this page**

42

Document Exporter for Cameo Collaborator requires Microsoft TrueType fonts to be installed on the server. Otherwise, PDF/HTML document export will fail. Alternative font packages, such as dejavu-serif-fonts, provide support for TrueType fonts and will work with Document Exporter. However, only Microsoft TrueType font will guarantee that the exported document retains original document formatting.

##### Prerequisites

- EPEL package repository must be installed and enabled.
- cabextract package must be installed from EPEL repo.

##### 1General method for installing font package

The steps provided here describes a universal method for installing the Microsoft TrueType font package on a Linux system. An online staging environment is required if installing on an air-gapped system.

To install the Microsoft TrueType font package:

1. D ownload font installer package to a predefined working path and extract : bashDJangotrue
2. Verify font extraction and generate the font package for installation : bashDJangotrue
3. If installing to an air-gapped environment, copy font package to the Document Exporter server.
4. Install fonts to the server and verify installation: bashDJangotrue
5. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''].

##### 2Online RPM installation method for RHEL 8

To install the Microsoft TrueType fonts directly from online RPM package on a Red Hat 8 system:

1. I nstall Microsoft TrueType Core RPM package: bashDJangotrue
2. After installation, use the fc-list command to verify installation: bashDJangotrue]]>
3. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] .

The URLs used in the commands above are subject to change. Always make sure that you install the latest versions of fonts.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7149ed51-b4dc-4e5f-a9f7-7878f23cfe41"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">2</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Document Exporter for Cameo Collaborator requires Microsoft TrueType fonts to be installed on the server. Otherwise, PDF/HTML document export will fail. Alternative font packages, such as dejavu-serif-fonts, provide support for TrueType fonts and will work with Document Exporter. However, only Microsoft TrueType font will guarantee that the exported document retains original document formatting. </p><h3>Prerequisites</h3><ul style="text-align: left;"><li><span>EPEL package repository must be installed and enabled.</span></li><li>cabextract package must be installed from EPEL repo.</li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0140651e-9b15-4488-8686-3edb9dc3dd4f"><ac:parameter ac:name="">1</ac:parameter></ac:structured-macro>General method for installing font package</h3><p>The steps provided here describes a universal method for installing the Microsoft TrueType font package on a Linux system. An online staging environment is required if installing on an air-gapped system.</p><p>To install the Microsoft TrueType font package:</p><hr /><ol><li>D<span style="color: rgb(23,43,77);">ownload font installer package to a predefined working path and extract</span>:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9b0b645d-338b-496e-9bac-59865cd8e94f"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[WORK_PATH=/opt/local/install/temp
sudo mkdir -p $WORK_PATH && cd $WORK_PATH
wget  https://phoenixnap.dl.sourceforge.net/project/mscorefonts2/sources/msttcore-fonts-installer-2.6.tar.gz
tar --strip-components=4 -xzf msttcore-fonts-installer-2.6.tar.gz -C $WORK_PATH msttcore-fonts-installer-2.6/usr/lib/msttcore-fonts-installer/
sudo mkdir -p $WORK_PATH/msttcore-fonts
./refresh-msttcore-fonts.sh -d $WORK_PATH/msttcore-fonts]]></ac:plain-text-body></ac:structured-macro></li><li><span style="color: rgb(23,43,77);">Verify font extraction and generate the font package for installation</span>:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="546828d6-6047-4b81-a3a1-9bc1ad32b9a3"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[ls -la $WORK_PATH/*.ttf
sudo pushd $WORK_PATH/msttcore-fonts && tar -cvzf $WORK_PATH/msttcore-fonts.tar.gz *.ttf && popd]]></ac:plain-text-body></ac:structured-macro></li><li><span style="color: rgb(23,43,77);">If installing to an air-gapped environment, copy font package to the Document Exporter server.</span></li><li><span style="color: rgb(23,43,77);">Install fonts to the server and verify installation:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d880eeab-42d5-4523-a302-af9e711b9bcf"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo mkdir -p /usr/share/fonts/msttcore
tar -xzf msttcore-fonts.tar.gz -C /usr/share/fonts/msttcore/
ls -la /usr/share/fonts/msttcore
sudo fc-cache -fv]]></ac:plain-text-body></ac:structured-macro></li><li><p><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Restart Web Application Platform]]></ac:plain-text-link-body></ac:link>.</p></li></ol><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="b7c06111-135e-424e-8cb9-b927f826f6a5"><ac:parameter ac:name="">2</ac:parameter></ac:structured-macro>Online RPM installation method for RHEL 8</h3><p>To install the Microsoft TrueType fonts directly from online RPM package on a Red Hat 8 system:</p><hr /><ol><li>I nstall Microsoft TrueType Core RPM package:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ece21b70-12f9-45a6-9e5f-9baea42dc6f8"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm]]></ac:plain-text-body></ac:structured-macro></li><li>After installation, use the fc-list command to verify installation:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="30d71a4d-7344-4a0b-862d-146e3ad948d2"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[fc-list | grep -i <font name>]]></ac:plain-text-body></ac:structured-macro></li><li><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Restart Web Application Platform]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5f063d9f-9e13-4819-8183-c6435ae097df"><ac:rich-text-body><p>The URLs used in the commands above are subject to change. Always make sure that you install the latest versions of fonts.</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491233 space=TWCloud2024xR1 version=2 -->
## PAGE 00139: Installing Teamwork Cloud and services on Windows

- page_id: `170491233`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491233/Installing+Teamwork+Cloud+and+services+on+Windows
- version_number: 2
- version_date: `2024-05-20T12:36:36.418+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Windows
- labels: []

### NORMALIZED CONTENT

This section provides instructions on installing Teamwork Cloud using either the installer or the zip file. 
Once the installation is complete, you need to [CONFLUENCE_PAGE title='Applying Teamwork Cloud license' space=''] before starting to use Teamwork Cloud with the modeling tool and Teamwork Cloud Admin.

**IMPORTANT**. To use modeling tools with DSLS licenses,Microsoft Visual C++ Redistributable must be installed (see[Latest supported Visual C++ Redistributable downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)). This applies to Windows OS only.

The following sections provide instructions on setting up Teamwork Cloud on Windows using the installer or the zip file.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides instructions on installing Teamwork Cloud using either the installer or the zip file. <br />Once the installation is complete, you need to <ac:link><ri:page ri:content-title="Applying Teamwork Cloud license" /><ac:plain-text-link-body><![CDATA[apply the Teamwork Cloud license]]></ac:plain-text-link-body></ac:link> before starting to use Teamwork Cloud with the modeling tool and Teamwork Cloud <ac:inline-comment-marker ac:ref="22174434-dbe2-421c-a044-d6d784b16392">Admin</ac:inline-comment-marker>.</p><p><span style="color: rgb(68,68,68);"><span style="color: rgb(255,0,0);"><strong>IMPORTANT</strong></span>. To use modeling tools with DSLS licenses, </span><span>Microsoft Visual C++ Redistributable must be installed (see </span><a class="external-link" href="https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022" style="">Latest supported Visual C++ Redistributable downloads</a><span>). This applies to Windows OS only.</span></p><p><br /></p><p><span style="color: rgb(62,63,64);">The following sections provide instructions on setting up Teamwork Cloud on Windows using the installer or the zip file.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="06462469-5b89-42ec-9cf9-2e2d6212f709" /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170491210 space=TWCloud2024xR1 version=7 -->
## PAGE 00140: Installing Teamwork Cloud services

- page_id: `170491210`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491210/Installing+Teamwork+Cloud+services
- version_number: 7
- version_date: `2025-04-25T13:25:23.822+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Linux
- labels: []

### NORMALIZED CONTENT

**On this page**

4

The installation of Teamwork Cloud services and initial configuration is described in this section. Installation using the provided script is highly recommended. The process involves installing the service(s), generating an initial self-signed SSL certificate, creating the twcloud user for file and service ownership, then configuring the Linux environment for performance and security.

##### Prerequisites

- OpenJDK Java 17.0 (see [CONFLUENCE_PAGE title='System requirements' space=''] for version information)

##### Installing Teamwork Cloud services

To install Teamwork Cloud services

1. To install OpenJDK 17 on a new Teamwork Cloud server, execute the following command: bashDJangotrue
2. [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the <*product>_<version_number>_installer_linux64.bin* file and place it in the same location as the install_twc_mcs_ol_rhel.sh script.
3. Install Teamwork Cloud by executing the *install_twc_mcs_ol_rhel.sh* script. Example
4. Follow the on-screen installation guidance.
5. When the Teamwork Cloud pre-installation summary is displayed, check if the information is correct and press **ENTER.**
6. Start the twcloud, zookeeper, and webapp services (in this particular order) by executing the following commands: bashDJangotrue
7. Make sure that Teamwork Cloud is operational by going to *https://<server_address>:8443/webapp.* You should see the Teamwork Cloud login screen. For more information, see [CONFLUENCE_PAGE title='Accessing Teamwork Cloud web applications' space=''].

When you complete the steps above, the preliminary Teamwork Cloud configuration is created. This means that your system is functional and you can login to Teamwork Cloud. After making sure that Teamwork Cloud is operational, you can optionally perform the described in the section below.

##### Post-installation Teamwork Cloud configuration

The post-installation configuration is an optional step and you should only perform it after making sure that Teamwork Cloud is operational.

To perform the post-installation Teamwork Cloud configuration

1. Edit the <install_root>/CATIANoMagicServices/TeamworkCloud/configuration/application.conf configuration file and make the following changes:
  - Change the value of the contact-points property to point to the listen_address you set in the cassandra.yaml file (i.e., contact-points = ["192.168.130.10:9042"]). This points Teamwork Cloud to the Cassandra database.
  - Use this parameter only if you need to deploy Teamwork Cloud in private network but client connect from public network. Change the value of the server-broadcast-host property to the public IP address instead of the local IP address. This way upon the initial connection the client application will know the external IP address to which it must connect (if Teamwork Cloud is installed behind a proxy or firewall with NAT).
2. Edit the*<install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/authserver.properties* configuration file and make the following changes:
  - If you are accessing the server by FQDN, change the value of the **authentication.redirect.uri.whitelist** property by adding an the FQDN entry to the whitelist (e.g., **authentication.redirect.uri.whitelist=[https://FQDN:8443/,https://FQDN:8111/,https://md_redirect](https://FQDN:8443/,https://FQDN:8111/,https://md_redirect)**). Make sure to add the public IP and/or FQDN for ports 8443 and 8111 to the whitelist.
3. Edit the <install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties configuration file and make the following changes:
  - Change the value of the twc.admin.username property to the username of a local account with Administrator privileges (the default value is Administrator).
  - Change the value of the twc.admin.password property to the password corresponding to the Administrator user (the default value is Administrator).
4. Restart the affected Teamwork Cloud services.

###### Document exporter font package

To use Cameo Collaborator document exporter, a TrueType font package is required in order to generate PDF/HTML files. Please see [CONFLUENCE_PAGE title='Installing Microsoft TrueType fonts for Document Exporter' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b59483f4-518b-4ff2-bd3e-24de45b5373f"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span>The installation of Teamwork Cloud services and initial configuration is described in this section. Installation using the provided script is highly recommended. The process <span style="color: rgb(23,43,77);">involves installing the service(s), generating an initial self-signed SSL certificate</span>, creating the twcloud user for file and service ownership, then configuring the Linux environment for performance and security. </span></p><h3><span>Prerequisites</span></h3><ul><li>OpenJDK Java 17.0 (see <ac:link><ri:page ri:content-title="System requirements" /><ac:plain-text-link-body><![CDATA[system requirements]]></ac:plain-text-link-body></ac:link> for version information)</li></ul><h3>Installing Teamwork Cloud services</h3><p>To install Teamwork Cloud services</p><hr /><ol><li><p>To install OpenJDK 17 on a new Teamwork Cloud server, execute the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0252ed62-d0f8-4cae-8674-479305a87444"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[yum -y install java-17-openjdk]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the &lt;<em>product&gt;_&lt;version_number&gt;_installer_linux64.bin</em> file</ac:link-body></ac:link> and place it in the same location as the <em><ac:inline-comment-marker ac:ref="d1afe86f-cfd7-45b4-b0da-35d0811a5fdb"><span style="color: rgb(62,63,64);">install_twc_mcs_ol_rhel.sh</span></ac:inline-comment-marker></em> script.</li><li><p class="auto-cursor-target">Install Teamwork Cloud by executing the <em>install_twc_mcs_ol_rhel.sh</em> script.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="71e20ced-0d6a-4c68-8dfe-59bc9ab41bb7"><ac:parameter ac:name="title">Example</ac:parameter><ac:plain-text-body><![CDATA[sudo ./install_twc_mcs_ol_rhel.sh]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><span style="letter-spacing: 0.0px;">Follow the on-screen installation guidance.</span></li><li><p class="auto-cursor-target">When the Teamwork Cloud pre-installation summary is displayed, check if the information is correct and press <strong>ENTER.</strong></p></li><li><p class="auto-cursor-target">Start the twcloud, zookeeper, and webapp services (in this particular order) by executing the following commands:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ee20ace7-8bc6-4e88-9173-78e241eb1d0d"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl start twcloud
sudo systemctl start zookeeper
sudo systemctl start webapp]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">Make sure that Teamwork Cloud is operational by going to <em>https://&lt;server_address&gt;:8443/webapp.</em> You should see the Teamwork Cloud login screen.<br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="60704efe-55f4-467e-9f63-8e3e94932cf5"><ac:rich-text-body>For more information, see <ac:link><ri:page ri:content-title="Accessing Teamwork Cloud web applications" /></ac:link>.</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p>When you complete the steps above, the preliminary Teamwork Cloud configuration is created. This means that your system is functional and you can login to Teamwork Cloud. After making sure that Teamwork Cloud is operational, you can optionally perform the <ac:link ac:anchor="Post-installation Teamwork Cloud Configuration"><ac:plain-text-link-body><![CDATA[post-installation configuration]]></ac:plain-text-link-body></ac:link> described in the section below.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Post-installation Teamwork Cloud configuration</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2af96a7b-cc5b-4950-ac44-25d70fcffc5b"><ac:rich-text-body><p>The post-installation configuration is an optional step and you should only perform it after making sure that Teamwork Cloud is operational.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To perform the post-installation Teamwork Cloud configuration</p><hr /><ol><li>Edit the<em> <span style="color: rgb(0,0,0);">&lt;install_root&gt;</span>/CATIANoMagicServices/TeamworkCloud/configuration/application.conf</em> configuration file and make the following changes:<br /><ul><li>Change the value of the <strong>contact-points</strong> property to point to the <strong>listen_address</strong> you set in the <em>cassandra.yaml</em> file (i.e., contact-points = [&quot;192.168.130.10:9042&quot;]). This points Teamwork Cloud to the Cassandra database.</li><li>Use this parameter only if you need to deploy Teamwork Cloud in private network but client connect from public network. Change the value of the <strong>server-broadcast-host</strong> property to the public IP address instead of the local IP address. This way upon the initial connection the client application will know the <span style="color: rgb(62,63,64);">external IP address to which it must connect (if Teamwork Cloud is installed behind a proxy or firewall with NAT).</span></li></ul></li><li><p class="auto-cursor-target">Edit the<em> <span style="color: rgb(0,0,0);">&lt;install_root&gt;</span>/CATIANoMagicServices/WebAppPlatform/shared/conf/authserver.properties</em> configuration file and make the following changes:</p><ul><li><p class="auto-cursor-target">If you are accessing the server by FQDN, change the value of the <strong>authentication.redirect.uri.whitelist</strong> property by adding an the FQDN entry to the whitelist (e.g., <strong>authentication.redirect.uri.whitelist=<span class="nolink"><a href="https://FQDN:8443/,https://FQDN:8111/,https://md_redirect">https://FQDN:8443/,https://FQDN:8111/,https://md_redirect</a></span></strong>). Make sure to add the public IP and/or FQDN for ports 8443 and 8111 to the whitelist.</p></li></ul></li><li>Edit the<em> <span style="color: rgb(0,0,0);">&lt;install_root&gt;</span>/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties</em> configuration file and make the following changes:<br /><ul><li>Change the value of the<strong> twc.admin.username</strong> property to the username of a local account with Administrator privileges (the default value is Administrator).</li><li>Change the value of the<strong> twc.admin.password</strong> property to the password corresponding to the Administrator user (the default value is Administrator).</li></ul></li><li>Restart the affected Teamwork Cloud services.</li></ol><h4>Document exporter font package</h4><p>To use Cameo Collaborator document exporter, a TrueType font package is required in order to generate PDF/HTML files. Please see <ac:link><ri:page ri:content-title="Installing Microsoft TrueType fonts for Document Exporter" /></ac:link>. </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491208 space=TWCloud2024xR1 version=5 -->
## PAGE 00141: Installing the FlexNet server

- page_id: `170491208`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491208/Installing+the+FlexNet+server
- version_number: 5
- version_date: `2026-03-06T14:36:49.861+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Linux
- labels: []

### NORMALIZED CONTENT

**On this page**

4

Teamwork Cloud can be configured to access a FlexNet server for license checkout and validation. The FlexNet server can be installed on the same system or on a separate machine.

##### Prerequisites

- OpenJDK Java (see [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''] for version information)
- Linux utility package unzip (respository)
- [FlexNet 11.19.6 64-bit: lmadmin installer](https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmadmin-x64_linux-11_19_6_0.bin)
- [FlexNet 11.19.6 64-bit utilities: lmgrd (zip file)](https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmgrd.zip)
- [Cameo daemon for FlexNet 11.19.6 64-bit (zip file)](https://d1g91r27pzl568.cloudfront.net/Cameo_daemon/FlexNet_11_19_6/linux64/cameo.zip)

##### Installing FlexNet server

The *install_flex_ol_rhel.sh* script will download all required components, deploy the server, create the systemd service entry to control it, and create the necessary firewall rules to allow the required traffic (if firewalld is running). The script may require modification depending on the zone where the interface is located. In addition, the script creates the lmadmin user, which runs the lmadmin service.

The script can also be used for offline installation. Download and place the FlexNet and Cameo daemon packages in the same location as the script. The lmadmin installer can work with several versions of Java, but at least one version needs to be installed on the system in order for the installer to run. On some systems, the ld-linux.so* dynamic linker/loader package may need to be installed in order for FlexNet to run. Most systems will work with the existing ld-linux library.

To install the FlexNet server

1. Run the *install_flex_ol_rhel.sh* script to start the installation and follow the installer instructions. All the default values presented by the installer should be accepted, except for the installation path, which can be a custom path.
2. After the lmadmin service is installed, start it by executing the following command: bashDJangotrue
3. To check if the service is running, execute the following command: bashDJangotrue

##### Troubleshooting

If the Imadmin service failed to start, it is often because the built-in web server cannot resolve the hostname.

To check if this is the case, execute the following commands:

```bash
/FNPLicenseServerManager/logs
tail web.log]]>
```

You will see output similar to the following where *yourhostname* is the name of the host:

```bash

```

If this is the case, edit the */etc/hosts* file and add the following entry so the webserver could resolve the host:

```bash

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="400ef5d8-2fcd-4d45-93b2-3dfb745c6e44"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span>Teamwork Cloud can be configured to access a FlexNet server for license checkout and validation. The FlexNet server can be installed on the same system or on a separate machine.</span></p><h3>Prerequisites</h3><ul><li>OpenJDK Java (see <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /></ac:link><span style="letter-spacing: 0.0px;"> for version information)</span></li><li><span style="color:var(--ds-text,#172b4d);">Linux utility package unzip (respository)</span></li><li><span style="color:var(--ds-text,#172b4d);"><a href="https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmadmin-x64_linux-11_19_6_0.bin">FlexNet 11.19.6 64-bit: lmadmin installer</a></span></li><li><span style="color:var(--ds-text,#172b4d);"><a href="https://d1oqhepk9od1tu.cloudfront.net/Flex_License_Server_Utilities/v11.19.6/linux64/lmgrd.zip">FlexNet 11.19.6 64-bit utilities: lmgrd (zip file)</a></span></li><li><span style="color:var(--ds-text,#172b4d);"><a href="https://d1g91r27pzl568.cloudfront.net/Cameo_daemon/FlexNet_11_19_6/linux64/cameo.zip">Cameo daemon for FlexNet 11.19.6 64-bit (zip file)</a></span></li></ul><h3>Installing FlexNet server</h3><p><span>The <em>install_flex_ol_rhel.sh</em> script will download all required components, deploy the server, create the systemd service entry to control it, and create the necessary firewall rules to allow the required traffic (if firewalld is running). The script may require modification depending on the zone where the interface is located. In addition, the script creates the lmadmin user, which runs the lmadmin service.</span></p><p><span>The script can also be used for offline installation. Download and place the FlexNet and Cameo daemon packages in the same location as the script. <span style="color:var(--ds-text,#172b4d);">The lmadmin installer can work with several versions of Java, but at least one version needs to be installed on the system in order for the installer to run. On some systems, the ld-linux.so* dynamic linker/loader package may need to be installed in order for FlexNet to run. Most systems will work with the existing ld-linux library.</span></span></p><p>To install the FlexNet server</p><hr /><ol><li><p class="auto-cursor-target">Run the <em>install_flex_ol_rhel.sh</em> script to start the installation and follow the installer instructions.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="46feebe0-02c6-4b8b-b000-1aefc549fc8b"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">All the default values presented by the installer should be accepted, except for the installation path, which can be a custom path.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">After the lmadmin service is installed, start it by executing the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1043dded-efca-4094-bcb4-72b9baf47043"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl start lmadmin]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">To check if the service is running, execute the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a25d24e9-27af-4c17-94e5-e587daca12af"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl status lmadmin]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><h3 class="auto-cursor-target">Troubleshooting</h3><p>If the Imadmin service failed to start, it is often because the built-in web server cannot resolve the hostname.</p><p>To check if this is the case, execute the following commands:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7f9a49d3-00f0-417c-b792-395cae3f8739"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[cd <install_root>/FNPLicenseServerManager/logs
tail web.log]]></ac:plain-text-body></ac:structured-macro><p>You will see output similar to the following where <em>yourhostname</em> is the name of the host:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0ac3268d-3c04-400c-9055-a12cd1d530f2"><ac:parameter ac:name="language">bash</ac:parameter><ac:plain-text-body><![CDATA[[Tue May 02 18:43:27 2017] [alert] (EAI 2)Name or service not known:
mod_unique_id: unable to find IPv4 address of "yourhostname"
Configuration Failed]]></ac:plain-text-body></ac:structured-macro><p>If this is the case, edit the <em>/etc/hosts</em> file and add the following entry so the webserver could resolve the host:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ead0927b-5a60-4189-9887-25f891abc2e2"><ac:parameter ac:name="language">bash</ac:parameter><ac:plain-text-body><![CDATA[192.168.130.10  yourhostname]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491234 space=TWCloud2024xR1 version=5 -->
## PAGE 00142: Installing using the installer file on Windows

- page_id: `170491234`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491234/Installing+using+the+installer+file+on+Windows
- version_number: 5
- version_date: `2025-10-30T13:36:19.409+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Windows > Installing Teamwork Cloud and services on Windows
- labels: []

### NORMALIZED CONTENT

The installer file includes both Teamwork Cloud and Web Application Platform with its services in its installation package.

#### WARNING: Warning

Warning

If the installation path contains any of the following characters, like '[', ']', '(', ')', '!', '@', '#', '$', '#', '%', '{', '}', '+', '=', or ';' the installation procedure cannot be completed successfully and the login page will not load. If, for example, the installation path is *C:\Program Files\TeamworkCloud*, which does not contain any of the special characters, the installation will not fail.

****

To install Teamwork Cloud by using the installer file on Windows

1. [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the <*product>_<version_number>_installer_win64.exe* file .
2. Run the installer file as administrator to start the installation wizard.
3. Read the installation introduction and click Next .
4. Select the Advanced Install radio button and click Next .
5. Select the components you want to install and click **Next**. We recommend installing Web Application Platform and Teamwork Cloud on different machines for better performance. If you decide to install Web Application Platform on a separate machine, clear the appropriate checkbox. [IMAGE alt='' src='']
6. Follow the on-screen instructions in the installation wizard and click Next after each step.
7. When the Pre-Installation Summary is displayed, check if all properties are specified correctly and click **Install**. 
 
[IMAGE alt='' src='']
8. After successful installation, click **Done** to close the installation wizard.
9. Open the Task Manager and start the following services:
  - Teamwork Cloud service
  - Zookeeper service
  - WebApp service
10. Wait a few minutes until all services have started, then check if the system is working. You should be able to access Teamwork Cloud via https://FQDN:8443/webapp/ .

After completing the steps above, you can [CONFLUENCE_PAGE title='Starting Teamwork Cloud on Windows' space=''].

##### Post-installation configuration (optional)

The installer created a preliminary configuration. If your system is still not operational, you may need to configure the following parameters manually.

- Edit the configuration file <install_root> \TeamworkCloud\configuration\application.conf . Search for contact-points = , located under the persistence esi.persistence. datastax-java-driver section, and replace localhost with ip_address_of_cassandra_node . Search for url = , located in the esi.auth section. Enter your server’s IP address or FQDN (if accessing via FQDN), for example, https://127.0.0.1:8443 .
- If you are accessing Teamwork Cloud Web UI via its FQDN:
  - Edit the configuration file <install_root> \ WebAppPlatform\shared\conf\authserver.properties . Search for authentication.redirect.uri.whitelist and append the following to the entry: https://FQDN:8443/webapp/
  - Edit the configuration file <install_root> \WebAppPlatform\shared\conf\webappplatform.properties. Add server.public.host and set it to FQDN.
- Edit the configuration file for Teamwork Cloud Admin: *<install_root>**\WebAppPlatform\shared\conf\webappplatform.properties*.
  - twc.admin.username - Set it to the username of a local account with Administrator privileges (default is Administrator).
  - twc.admin.password - Set it to the password corresponding to the Administrator user (default is Administrator).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The installer file includes both Teamwork Cloud and Web Application Platform with its services in its installation package.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1452eb56-3a9d-4c11-9641-55b49874337a"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>If the installation path contains any of the following characters, like '[', ']', '(', ')', '!', '@', '#', '$', '#', '%', '{', '}', '+', '=', or ';' the installation procedure cannot be completed successfully and the login page will not load. If, for example, the installation path is <em>C:\Program Files\TeamworkCloud</em>, which does not contain any of the special characters, the installation will not fail.</p></ac:rich-text-body></ac:structured-macro><p><strong> </strong></p><p>To install Teamwork Cloud by using the installer file on Windows</p><hr style="" /><ol><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the &lt;<em>product&gt;_&lt;version_number&gt;_installer_win64.exe</em> file</ac:link-body></ac:link>.</li><li>Run the installer file as administrator to start the installation wizard.</li><li>Read the installation introduction and click <strong>Next</strong>.</li><li>Select the <strong>Advanced Install</strong> radio button and click <strong>Next</strong>.</li><li><p>Select the components you want to install and click <strong>Next</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d751e7b5-13c8-45f1-8635-4da6e0fac5b9"><ac:rich-text-body><p>We recommend installing Web Application Platform and Teamwork Cloud on different machines for better performance. If you decide to install Web Application Platform on a separate machine, clear the appropriate checkbox.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="selecting_install_components.png" /></ac:image><br /><br /></p></li><li>Follow the on-screen instructions in the installation wizard and click <strong>Next</strong> after each step.</li><li><p class="auto-cursor-target">When the Pre-Installation Summary is displayed, check if all properties are specified correctly and click <strong>Install</strong>.<br /><br /><ac:image><ri:attachment ri:filename="twc_pre-installation-summary.png" /></ac:image><br /><br /></p></li><li><p>After successful installation, click <strong>Done</strong> to close the installation wizard.</p></li><li><p>Open the Task Manager and start the following services:</p><ul><li>Teamwork Cloud service</li><li>Zookeeper service</li><li><p class="auto-cursor-target">WebApp service</p></li></ul></li><li>Wait a few minutes until all services have started, then check if the system is working. You should be able to access Teamwork Cloud via <a href="https://fqdn:8443/webapp/" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">https://FQDN:8443/webapp/</a>.</li></ol><p><br />After completing the steps above, you can <ac:link><ri:page ri:content-title="Starting Teamwork Cloud on Windows" /><ac:plain-text-link-body><![CDATA[start Teamwork Cloud on Windows]]></ac:plain-text-link-body></ac:link>.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Post-installation configuration (optional)</h3><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c928b67a-2bcf-46e3-916c-4eba93640265"><ac:rich-text-body><p>The installer created a preliminary configuration. If your system is still not operational, you may need to configure the following parameters manually.</p></ac:rich-text-body></ac:structured-macro><ul><li>Edit the configuration file <em>&lt;install_root&gt;</em><em>\TeamworkCloud\configuration\application.conf</em>. Search for <strong>contact-points =</strong>, located under the persistence <strong>esi.persistence.</strong><strong>datastax-java-driver</strong> section, and replace <strong>localhost </strong>with <strong>ip_address_of_cassandra_node</strong>. Search for <strong>url =</strong>, located in the <strong>esi.auth</strong> section. Enter your server’s IP address or FQDN (if accessing via FQDN), for example, <em><span class="nolink"><span class="nolink">https://127.0.0.1:8443</span></span></em>.</li><li><p>If you are accessing Teamwork Cloud Web UI via its FQDN:</p><ul><li>Edit the configuration file <em>&lt;install_root&gt;</em>\<em>WebAppPlatform\shared\conf\authserver.properties</em>. Search for <strong>authentication.redirect.uri.whitelist</strong> and append the following to the entry: <a class="external-link" href="https://fqdn:8443/webapp/" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" title="Follow link">https://FQDN:8443/webapp/</a></li><li>Edit the configuration file<em> </em><em>&lt;install_root&gt;</em><em>\WebAppPlatform\shared\conf\webappplatform.properties.</em> Add <strong>server.public.host</strong> and set it to FQDN.</li></ul></li><li><p class="auto-cursor-target">Edit the configuration file for Teamwork Cloud Admin: <em>&lt;install_root&gt;</em><em>\WebAppPlatform\shared\conf\webappplatform.properties</em>.</p><ul><li><strong>twc.admin.username</strong> - Set it to the username of a local account with Administrator privileges (default is Administrator).</li><li><strong>twc.admin.password</strong> - Set it to the password corresponding to the Administrator user (default is Administrator).</li></ul></li></ul>
````

<!--NOMAGIC_PAGE id=170491251 space=TWCloud2024xR1 version=7 -->
## PAGE 00143: Installing using the zip file on Windows

- page_id: `170491251`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491251/Installing+using+the+zip+file+on+Windows
- version_number: 7
- version_date: `2026-03-04T15:45:33.182+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Windows > Installing Teamwork Cloud and services on Windows
- labels: []

### NORMALIZED CONTENT

**On this page**

This section explains how to install Teamwork Cloud on a single server by using zip files and setting up its configuration file to allow access to the authentication server.

##### Prerequisites

- OpenJDK Java (see [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''] for version information)

##### Installing Teamwork Cloud on Windows by unzipping the file

To install Teamwork Cloud on Windows by unzipping the file

1. Unzip the contents of the TeamworkCloudSuite directory to the installation directory (for example, <install_root> \TeamworkCloud ).
2. Open the server configuration file *<install_root>**\TeamworkCloud\configuration\application.conf* and edit the following lines (the hostname and seed-nodes) to use the node's own IP address. 
You must also set the IP address of the Cassandra node in the seeds section. If your Cassandra instance is on the same server, then use the node's own IP address. hostname = "10.1.1.123" seed-nodes = ["akka://twcloud@10.1.1.123:2552"] text contact-points = ["10.1.1.123:9042"] text
3. Update the AuthServer configuration: *<install_root>\shared\conf\authserver.properties* by specifying the IP address instead of *<serverIP>*: text:8443>/
twc.server.host=]]>
4. Update the configuration file: *<install_root>* \TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties - the configuration file for Teamwork Cloud Admin Console
  - twc.admin.username - Set it to the username of a local account with Administrator privileges (default is Administrator)
  - twc.admin.password - Set it to the password corresponding to the Administrator user (default is Administrator).
  - If you changed the pswd field in <install_root> \TeamworkCloud\configuration\application.conf from the default, you must modify this file accordingly. Search for authentication.client.secret .and replace the CHANGE_ME value with the same value as that in application.conf .
5. Generate default keypair and certificate by running the following command from the command prompt. If your TeamworkCloudSuite is under a folder that requires Administrative permission, for example, *C:\Program Files*, make sure that you start the command prompt using**"Run as administrator"**. bashDJangotruecd C:\TeamworkCloudSuite\scripts\windows
C:\> genkey]]>

```text
authentication.redirect.uri.whitelist=https://<serverIP>:8443>/webapp/,https://<PublicIP>:8443>/webapp/,https://<FQDN>:8443>/webapp/,https://md_redirect/
```

There are additional steps to run Teamwork Cloud as a service on Windows. Before proceeding, make sure the server's log configuration points to the file location that is writable. You can find the log config in the file*<install_root>\TeamworkCloud\configuration\logback.xml*.

You need to check if the file location path is editable.

##### Running Teamwork Cloud on Windows

To run Teamwork Cloud on Windows

1. Set the necessary environment variables in the shell that will execute the service installation script where: For example: bashDJangotrueset TWCLOUD_HOME=C:\Program Files\TeamworkCloud
C:\> set JAVA_HOME=C:\Program Files\Java\jdk-11.0.12+7]]> Alternatively, set the environment variables by adding them through the**Environment Variables**dialog (click**Control Panel**>**System**>**Advanced**>**Environment Variables**>**New**).
  - TWCLOUD_HOME is the path that points to the directory where Teamwork Cloud was installed.
  - JAVA_HOME is a directory containing a Java JDK or JRE.
2. Run the Teamwork Cloud service installation script, for example: textinstallService.bat]]>
3. Run the WebApp and the Zookeeper service installation script
  - The WebApp service requires its bundled Java. Therefore, prior to executing the service install script, we must set **JRE_HOME** and **CATALINA_HOME_WEBAPP** to point to it. textset JRE_HOME=C:\Program Files\TeamworkCloud\WebAppPlatform\jre 
C:\> set CATALINA_HOME_WEBAPP=C:\Program Files\TeamworkCloud\WebAppPlatform
C:\Program Files\TeamworkCloud\WebAppPlatform\bin\>service.bat install 
C:\Program Files\TeamworkCloud\WebAppPlatform\zookeeper\bin\>zkService.cmd install]]>
4. Set service dependencies: bashDJangotruesc config webapp depend= teamworkcloud]]>

- The scripts should be executed from an elevated command prompt ( Run as Administrator ).
- On Windows, the values of the environment variables are evaluated only once, when the service is installed. Subsequent changes to these variables will not affect the service startup. Therefore, if the values are modified and the service must use the new values, the service must be re-installed.

##### Uninstalling Teamwork Cloud on Windows

To uninstall Teamwork Cloud:

- Run the service uninstallation scripts:

```text
uninstallService.bat 
C:\Program Files\TeamworkCloud\AuthServer\bin\unregisterWindowsService.bat
C:\Program Files\TeamworkCloud\WebAppPlatform\bin\>service.bat uninstall 
C:\Program Files\TeamworkCloud\WebAppPlatform\zookeeper\bin\>zkService.cmd remove]]>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6a5cecfa-e229-4006-893e-db1d13fb7e3b" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This section explains how to install Teamwork Cloud on a single server by using zip files and setting up its configuration file to allow access to the authentication server.</p><h3><span>Prerequisites</span></h3><ul><li>OpenJDK Java (see <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /></ac:link><span style="letter-spacing: 0.0px;"> for version information)</span></li></ul><h3>Installing Teamwork Cloud on Windows by unzipping the file</h3><p><br /></p><p>To install Teamwork Cloud on Windows by unzipping the file</p><hr /><ol><li><span style="letter-spacing: 0.0px;">Unzip the contents of the TeamworkCloudSuite directory to the installation directory (for example, </span><em style="letter-spacing: 0.0px;">&lt;install_root&gt;</em><em style="letter-spacing: 0.0px;">\TeamworkCloud</em><span style="letter-spacing: 0.0px;">).</span></li><li><p>Open the server configuration file <em>&lt;install_root&gt;</em><em>\TeamworkCloud\configuration\application.conf</em> and edit the following lines (the hostname and seed-nodes) to use the node's own IP address.<br />You must also set the IP address of the Cassandra node in the seeds section. If your Cassandra instance is on the same server, then use the node's own IP address.</p><pre>hostname = &quot;10.1.1.123&quot;</pre><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="34871a18-c07b-42db-a7d0-28bfb2a2180b"><ac:plain-text-body><![CDATA[### Configuration for the Netty based transport drivers
	artery.canonical {
 		# The hostname or ip clients should connect to.
 		# If it is not set, it will be set automatically to the IP that can connect to the seed node.
		hostname = "10.1.1.123"

		# The default remote server port clients should connect to.
      		# Default is 2552 (AKKA). Use 0 if you want a random available port.
      		# This port needs to be unique for each actor system on the same machine.
		port = 2552]]></ac:plain-text-body></ac:structured-macro><pre>seed-nodes = [&quot;akka://twcloud@10.1.1.123:2552&quot;]</pre><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ae0e24aa-ea78-43a6-a32f-1f92ab696836"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[cluster {
		# Initial contact points of the cluster.
    		# The nodes to join automatically at startup.
    		# The comma separating full URIs defined by a String in the form of
    		# "akka://system@hostname:port"
		# Can be set by system property. 
		# e.g. ["akka://twcloud@10.1.1.123:2552","akka://twcloud@10.1.1.124:2552"]
		# The default value depends on the operation mode. In cluster mode, the seed node is mandatory in all nodes.
		# In single server mode, the seed node configuration is optional. It is set to 127.0.0.1 by default at runtime.
		seed-nodes = ["akka://twcloud@10.1.1.123:2552"]]]></ac:plain-text-body></ac:structured-macro><pre>contact-points = [&quot;10.1.1.123:9042&quot;]</pre><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="825587f7-3596-4c34-af4f-5496c97f1b45"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[esi.persistence.datastax-java-driver {
                basic {
                                contact-points = ["10.1.1.123:9042"]]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Update the AuthServer configuration: <em>&lt;install_root&gt;\shared\conf\authserver.properties</em> by specifying the IP address instead of <em>&lt;serverIP&gt;</em>:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b7045396-9880-498a-9633-35a52e588e91"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[authentication.redirect.uri.whitelist=https://<serverIP>:8443>/
twc.server.host=<serverIP>]]></ac:plain-text-body></ac:structured-macro><p><span> </span></p></li><li><span>Update the configuration file: <em>&lt;install_root&gt;</em></span><em>\TeamworkCloud\WebAppPlatform\shared\conf\webappplatform.properties</em><strong> </strong><span>- the configuration file for Teamwork Cloud Admin Console</span><ul><li><strong>twc.admin.username</strong> - Set it to the username of a local account with Administrator privileges (default is Administrator)</li><li><strong>twc.admin.password</strong> - Set it to the password corresponding to the Administrator user (default is Administrator).</li><li>If you changed the <strong>pswd</strong> field in <em>&lt;install_root&gt;</em><em>\TeamworkCloud\configuration\application.conf</em> from the default, you must modify this file accordingly. Search for <strong>authentication.client.secret</strong>.and replace the <strong>CHANGE_ME</strong> value with the same value as that in <strong>application.conf</strong>.</li></ul><p><br /></p></li><li><p class="auto-cursor-target">Generate default keypair and certificate by running the following command from the command prompt. If your TeamworkCloudSuite is under a folder that requires Administrative permission, for example, <em>C:\Program Files</em>, make sure that you start the command prompt using<strong> &quot;Run as administrator&quot;</strong>.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="649529e7-97de-4dba-bfe0-5bd73df70e71"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[C:\> cd C:\TeamworkCloudSuite\scripts\windows
C:\> genkey]]></ac:plain-text-body></ac:structured-macro></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eed5ef97-6f9e-4ef6-87f7-dbe5c059cd5d"><ac:rich-text-body>If the server is accessed via FQDN or public IP address, then the authentication.redirect.url must also contain entries for them, accordingly, in the format:<pre>authentication.redirect.uri.whitelist=https://&lt;serverIP&gt;:8443&gt;/webapp/,https://&lt;PublicIP&gt;:8443&gt;/webapp/,https://&lt;FQDN&gt;:8443&gt;/webapp/,<span class="nolink">https://md_redirect/</span></pre></ac:rich-text-body></ac:structured-macro><p>There are additional steps to run Teamwork Cloud as a service on Windows. Before proceeding, make sure the server's log configuration points to the file location that is writable. You can find the log config in the file<em> &lt;install_root&gt;\TeamworkCloud\configuration\logback.xml</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="443c2fda-8806-4a26-b700-9b2dea6df368"><ac:rich-text-body><p>You need to check if the file location path is editable.</p></ac:rich-text-body></ac:structured-macro><h3><span>Running Teamwork Cloud on Windows<br /></span></h3><p><span>To run Teamwork Cloud on Windows</span></p><hr /><ol><li><span>Set the necessary environment variables in the shell that will execute the service installation script where:</span><ul><li><strong>TWCLOUD_HOME</strong> is the path that points to the directory where Teamwork Cloud was installed. </li><li><strong>JAVA_HOME </strong>is a directory containing a Java JDK or JRE. <br /><br /></li></ul><p>For example:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c26cffee-b5dc-4cd8-8393-521bc54c2c9f"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[C:\> set TWCLOUD_HOME=C:\Program Files\TeamworkCloud
C:\> set JAVA_HOME=C:\Program Files\Java\jdk-11.0.12+7]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="675c75a8-bacb-406d-ad88-8f0e63f8b4b0"><ac:rich-text-body><p><span>Alternatively, set the environment variables by adding them through the </span><strong>Environment Variables</strong><span> dialog (click </span><strong>Control Panel</strong><span> &gt; </span><strong>System</strong><span> &gt; </span><strong>Advanced</strong><span> &gt; </span><strong>Environment Variables</strong><span> &gt; </span><strong>New</strong><span>). </span></p></ac:rich-text-body></ac:structured-macro></li><li><p> Run the Teamwork Cloud service installation script, for example: </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8db20a1c-77b9-4e78-81ae-91c2e8fd88c4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[C:\Program Files\TeamworkCloud\scripts\windows>installService.bat]]></ac:plain-text-body></ac:structured-macro></li><li><p><span style="color:var(--ds-text,#333333);">Run the WebApp and the Zookeeper service installation script</span></p><ul><li><p>The WebApp service requires its bundled Java.  Therefore, prior to executing the service install script, we must set <strong>JRE_HOME</strong> and <strong>CATALINA_HOME_WEBAPP</strong> to point to it.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="590a1fe4-aad4-42b5-8cfb-b4e7a9e673b4"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[C:\> set JRE_HOME=C:\Program Files\TeamworkCloud\WebAppPlatform\jre 
C:\> set CATALINA_HOME_WEBAPP=C:\Program Files\TeamworkCloud\WebAppPlatform
C:\Program Files\TeamworkCloud\WebAppPlatform\bin\>service.bat install 
C:\Program Files\TeamworkCloud\WebAppPlatform\zookeeper\bin\>zkService.cmd install]]></ac:plain-text-body></ac:structured-macro></li></ul></li><li><p><span style="color:var(--ds-text,#333333);">Set service dependencies:</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ca808acd-3a82-47e2-ae0e-e08390fa85ed"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[C:\> sc config webapp depend= teamworkcloud]]></ac:plain-text-body></ac:structured-macro></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5bcc6b01-7045-4042-8cf1-e06fee51aa0a"><ac:rich-text-body><ul><li>The scripts should be executed from an elevated command prompt (<strong>Run as Administrator</strong>).</li><li>On Windows, the values of the environment variables are evaluated only once, when the service is installed. Subsequent changes to these variables will not affect the service startup. Therefore, if the values are modified and the service must use the new values, the service must be re-installed.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Uninstalling Teamwork Cloud on Windows</h3><p>To uninstall Teamwork Cloud:</p><ul><li>Run the service uninstallation scripts: </li></ul><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="503645fe-de8a-4ff3-9d39-75412d7221b3"><ac:parameter ac:name="language">text</ac:parameter><ac:plain-text-body><![CDATA[C:\Program Files\TeamworkCloud\scripts\windows>uninstallService.bat 
C:\Program Files\TeamworkCloud\AuthServer\bin\unregisterWindowsService.bat
C:\Program Files\TeamworkCloud\WebAppPlatform\bin\>service.bat uninstall 
C:\Program Files\TeamworkCloud\WebAppPlatform\zookeeper\bin\>zkService.cmd remove]]></ac:plain-text-body></ac:structured-macro><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491294 space=TWCloud2024xR1 version=5 -->
## PAGE 00144: Installing Web Application Platform manually

- page_id: `170491294`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491294/Installing+Web+Application+Platform+manually
- version_number: 5
- version_date: `2025-09-15T12:57:10.535+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: ['installing-and-configuring']

### NORMALIZED CONTENT

The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform and its services without using the installer file.

Web Application Platform, with its services, can run on the following web application containers:

- Apache Tomcat
- GlassFish
- WildFly
- Eclipse Jetty

#### NOTE: Installation prerequisites and other important information

Installation prerequisites and other important information

Before installing Web Application Platform with services, you need to:

- Have a working instance of Teamwork Cloud.
- If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that [CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024xR1'] or [CONFLUENCE_PAGE title='Installing the FlexNet server' space=''] is installed beforehand.
- For deployment on Linux, increase the open file limit for the OS (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.
- Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.
- [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the *Web_App_Platform_<version number>_<operating system>_no_install.zip* file which includes the following web applications:
  - admin.war - The service for managing Teamwork Cloud users, roles, and resource assignments.
  - authentication.war - The service allowing users to authenticate access to Teamwork Cloud.
  - collaborator.war - The service allowing users to review, edit, and collaborate on Cameo Collaborator documents.
  - document-exporter.war - The service allowing users to export Cameo Collaborator documents to PDF and HTML.
  - oslc.war - The service allowing users to browse the model through OSLC.
  - reports.war - The service allowing users to export Teamwork Cloud server-related data to XLSX or CSV.
  - resources.war - The service for managing Teamwork Cloud resources.
  - resource-usage-map.war - The service with live visual graph capabilities representing Teamwork Cloud resource usages and identifying potential problem areas.
  - simulation.war - The service allowing users to simulate Teamwork Cloud projects on the server side.
  - webapp.war - The core Web Application Platform service.

Before starting the installation, you should know the following:

- We recommend installing Web Application Platform and Teamwork Cloud on different machines.
- Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <install_root>/TeamworkCloud/configuration directory). You will need this data during installation.
- After installing Web Application Platform, it is recommended to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] on the machine where Teamwork Cloud is installed.

To install Web Application Platform

1. Download and install the web server on which Web Application Platform will run. For installation instructions, see the documentation of the server you intend to install.
2. [CONFLUENCE_PAGE title='Downloading installation files' space='NMDOC'] and extract the Web_App_Platform_<version number>_<operating system>_no_install.zip file.
3. Open for editing the <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties file, read the comments with property descriptions, and specify the following:
  - Web Application Platform properties
  - Authentication server properties
  - Teamwork Cloud server properties
  - FlexNet/DSLS server properties
  - Platform service discovery-related properties
4. If you want to install the Authentication server ( authentication.war ) together with Web Application Platform, do the following:
  1. Copy the KeyStore file to the <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/ directory.
  2. Open for editing the <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/*authserver.properties* file, read the comments with property descriptions, and specify the following:
    - [CONFLUENCE_PAGE title='General parameters' space='']
    - [CONFLUENCE_PAGE title='Keystore parameters' space='']
5. Place the following files into the location that is on the classpath of the web server you have installed:
  - <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties file
  - <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/authserver.properties file (if you plan to install the Authentication server ( authentication.war ))
  - *<no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/data* directory containing email notifications and document exporter templates (if you plan to install Cameo Collaborator for Teamwork Cloud (*collaborator.war*) and/or document exporter (*document-exporter.war*)) ExampleIf you have installed Apache Tomcat 10.1 or a later version, you can choose from the following options (refer to server documentation for all available options):Place the *webappplatform.properties* file in the *<tomcat_home>/shared/conf* directory. Then open the *<tomcat_home>/conf/catalina.properties* file and set the **shared.loader** property as **shared.loader="<catalina_base>/shared/conf"**.Place the *webappplatform.properties* file in a custom directory. Add the path to the directory to the list of shared classloader paths defined by the "shared.loader" property in the *${tomcat.home}/conf/catalina.properties* file.If you have installed a different web application server, refer to its user manual.
6. Deploy the desired web applications, e.g., webapp.war , admin.war , collaborator.war , resources.war , etc.
7. If you chose to install Cameo Collaborator for Teamwork Cloud, apply the Cameo Collaborator license.

For information on how to start Web Application Platform, refer to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space='']. You can access Web Application Platform by opening a web browser and navigating to *http(s)://<domain_name>:<port>/webapp*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#333333);">The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform and its services without using the installer file.</span></p><p>Web Application Platform, with its services, can run on the following <span>web application container</span>s:</p><ul><li>Apache Tomcat</li><li>GlassFish</li><li>WildFly</li><li>Eclipse Jetty<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="265a25a2-18bc-4ad8-8c9b-354bcfe415b6"><ac:parameter ac:name="title">Installation prerequisites and other important information</ac:parameter><ac:rich-text-body><p>Before installing Web Application Platform with services, you need to:</p><ul><li>Have a working instance of Teamwork Cloud.</li><li><span style="color:var(--ds-text,#333333);">If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[DSLS]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Installing the FlexNet server" /><ac:plain-text-link-body><![CDATA[the FlexNet license server]]></ac:plain-text-link-body></ac:link> is installed beforehand.</span></li><li>For deployment on Linux, increase the open file limit for the OS (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.</li><li>Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.</li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the <em>Web_App_Platform_&lt;version number&gt;_&lt;operating system&gt;_no_install.zip</em> file</ac:link-body></ac:link> which includes the following web applications:<br /><ul><li><em>admin.war</em> - The service for managing Teamwork Cloud users, roles, and resource assignments.</li><li><em>authentication.war</em> - The service allowing users to authenticate access to Teamwork Cloud.</li><li><em>collaborator.war</em> - The service allowing users to review, edit, and collaborate on Cameo Collaborator documents.</li><li><em>document-exporter.war</em> - The service allowing users to export Cameo Collaborator documents to PDF and HTML.</li><li><em>oslc.war</em> - The service allowing users to browse the model through OSLC.</li><li><em>reports.war</em> - The service allowing users to export Teamwork Cloud server-related data to XLSX or CSV.</li><li><em>resources.war</em> - The service for managing Teamwork Cloud resources.</li><li><em>resource-usage-map.war</em> - The service with live visual graph capabilities representing Teamwork Cloud resource usages and identifying potential problem areas.</li><li><em>simulation.war</em> - The service allowing users to simulate Teamwork Cloud projects on the server side.</li><li><em>webapp.war</em> - The core Web Application Platform service.</li></ul></li></ul><p><span style="color:var(--ds-text,#333333);">Before starting the installation, you should know the following:</span></p><ul><li>We recommend installing Web Application Platform and Teamwork Cloud on different machines.</li><li>Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <em>&lt;install_root&gt;/TeamworkCloud/configuration</em> directory). You will need this data during installation.</li><li>After installing Web Application Platform, it is recommended to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[stop the WebApp service]]></ac:plain-text-link-body></ac:link> on the machine where Teamwork Cloud is installed.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To install Web Application Platform</p><hr /><ol><li>Download and install the web server on which Web Application Platform will run. For installation instructions, see the documentation of the server you intend to install.</li><li><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Downloading installation files" /><ac:plain-text-link-body><![CDATA[Download]]></ac:plain-text-link-body></ac:link> and extract the <em>Web_App_Platform_&lt;version number&gt;_&lt;operating system&gt;_no_install.zip</em> file.</li><li>Open for editing the <em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties</em> file, read the comments with property descriptions, and specify the following:<ul><li><span style="color:var(--ds-text,#333333);">Web Application Platform properties</span></li><li><span style="color:var(--ds-text,#333333);">Authentication server properties</span></li><li><span style="color:var(--ds-text,#333333);">Teamwork Cloud server properties</span></li><li><span style="color:var(--ds-text,#333333);">FlexNet/DSLS server properties</span><span style="color:var(--ds-text,#333333);"><br /></span></li><li><span style="color:var(--ds-text,#333333);">Platform service discovery-related properties</span></li></ul></li><li>If you want to install the Authentication server (<em>authentication.war</em>)<em> </em>together with Web Application Platform, do the following:<ol><li>Copy the KeyStore file to the <em style="text-align: left;">&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/</em> directory.</li><li>Open for editing the <em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/<em style="text-align: left;">authserver.properties</em></em> file, read the comments with property descriptions, and specify the following:<ul><li><ac:link><ri:page ri:content-title="General parameters" /><ac:plain-text-link-body><![CDATA[General properties]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Keystore parameters" /><ac:plain-text-link-body><![CDATA[Keystore properties]]></ac:plain-text-link-body></ac:link></li></ul></li></ol></li><li>Place the following files into the location that is on the classpath of the web server you have installed:<ul><li><em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/webappplatform.properties</em> file</li><li><em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/authserver.properties</em> file (if you plan to install the Authentication server (<em>authentication.war</em>))</li><li><p><em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/data</em> directory containing email notifications and document exporter templates (if you plan to install Cameo Collaborator for Teamwork Cloud (<em>collaborator.war</em>) and/or document exporter (<em>document-exporter.war</em>))</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b3d37a0a-183a-4a76-9b62-88d0c4b507a9"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>If you have installed Apache Tomcat 10.1 or a later version, you can choose from the following options (refer to server documentation for all available options):</p><ul><li>Place the <em>webappplatform.properties</em> file in the <em>&lt;tomcat_home&gt;/shared/conf</em> directory. Then open the <em>&lt;tomcat_home&gt;/conf/catalina.properties</em> file and set the <strong>shared.loader</strong> property as <strong>shared.loader=&quot;&lt;catalina_base&gt;/shared/conf&quot;</strong>.</li><li>Place the <em>webappplatform.properties</em> file in a custom directory. Add the path to the directory to the list of shared classloader paths defined by the &quot;shared.loader&quot; property in the <em>${tomcat.home}/conf/catalina.properties</em> file. </li></ul><p>If you have installed a different web application server, refer to its user manual.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li><li>Deploy the desired web applications, e.g., <em>webapp.war</em>,<em> admin.war</em>,<em> collaborator.war</em>, <em>resources.war</em>, etc.</li><li>If you chose to install Cameo Collaborator for Teamwork Cloud, apply the Cameo Collaborator license.</li></ol><p><span style="color:var(--ds-text,#333333);"><br />For information on how to start Web Application Platform, refer to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /></ac:link>. You can access Web Application Platform by opening a web browser and navigating to <em>http(s)://&lt;domain_name&gt;:&lt;port&gt;/webapp</em>.</span></p>
````

<!--NOMAGIC_PAGE id=170491278 space=TWCloud2024xR1 version=4 -->
## PAGE 00145: Installing Web Application Platform on Linux

- page_id: `170491278`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491278/Installing+Web+Application+Platform+on+Linux
- version_number: 4
- version_date: `2025-12-10T10:34:45.586+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: []

### NORMALIZED CONTENT

The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services by using the command-line interface.

#### NOTE: Installation prerequisites and other important information

Installation prerequisites and other important information

Before installing Web Application Platform with services, you need to:

- Have a working instance of Teamwork Cloud.
- If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that [CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024xR1'] or [CONFLUENCE_PAGE title='Installing the FlexNet server' space=''] is installed beforehand.
- [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the *Web_App_Platform_<version number>_unix.sh* file .
- Increase the open file limit for the OS (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.
- Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.

Before starting the installation, you should know the following:

- We recommend installing Web Application Platform and Teamwork Cloud on different machines.
- Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <install_root>/TeamworkCloud/configuration directory). You will need this data during installation.
- After installing Web Application Platform, it is recommended to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] on the machine where Teamwork Cloud is installed.

To install Web Application Platform and services (advanced installation)

1. Open the terminal and go to the directory where the Web_App_Platform_<version number>_unix.sh file is stored.
2. Execute the following command: bashDJangotrue_unix.sh -i console]]>
3. When the introduction to Web Application Platform installation is displayed, press **Enter** to continue.
4. Specify the location where you want to install Web Application Platform:
  - Press Enter to use the default installation directory.
  - Enter the full path to the installation directory and press Enter .
5. Type "2" to select the Advanced installation option and press Enter .
6. Follow the on-screen installation instructions.
7. When the Pre-Installation Summary is displayed, check if properties are specified correctly, and press Enter to start the installation.
8. When Web Application Platform is successfully installed , press Enter .
9. If you want to start the WebApp service right after installation, press Enter . Otherwise, type "0" and press Enter .
10. If you installed the Came Collaborator for Teamwork Cloud service, apply the Cameo Collaborator license.

Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space='']. To access Web Application Platform, open a web browser and go to *http(s)://<domain_name>:<port>/webapp*.

**Scripts for upgrading Java and Tomcat in the Linux environment:**

- Java: [ATTACHMENT filename='upgrade_jdk_webapp.sh']
- Tomcat: [ATTACHMENT filename='upgrade_tomcat_webapp.sh']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services by using the command-line interface.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="23a637d8-0dc4-4e2f-8517-02e8093618f4"><ac:parameter ac:name="title">Installation prerequisites and other important information</ac:parameter><ac:rich-text-body><p>Before installing Web Application Platform with services, you need to:</p><ul><li>Have a working instance of Teamwork Cloud.</li><li><span style="color:var(--ds-text,#333333);">If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[DSLS]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Installing the FlexNet server" /><ac:plain-text-link-body><![CDATA[the FlexNet license server]]></ac:plain-text-link-body></ac:link> is installed beforehand.</span></li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the <em>Web_App_Platform_&lt;version number&gt;_unix.sh</em> file</ac:link-body></ac:link>.</li><li><a href="https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491407/Advanced+services+configuration#Advancedservicesconfiguration-IncreasingopenfilelimitonLinux">Increase the open file limit for the OS</a> (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.</li><li>Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.</li></ul><p>Before starting the installation, you should know the following:</p><ul><li>We recommend installing Web Application Platform and Teamwork Cloud on different machines.</li><li>Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <em>&lt;install_root&gt;/TeamworkCloud/configuration</em> directory). You will need this data during installation.</li><li>After installing Web Application Platform, it is recommended to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[stop the WebApp service]]></ac:plain-text-link-body></ac:link> on the machine where Teamwork Cloud is installed.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To install Web Application Platform and services (advanced installation)</p><hr /><ol><li>Open the terminal and go to the directory where the <em>Web_App_Platform_&lt;version number&gt;_unix.sh</em> file is stored.</li><li><p class="auto-cursor-target">Execute the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="38f815bf-1afd-492d-964d-ed09416afe46"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo ./Web_App_Platform_<version number>_unix.sh -i console]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">When the introduction to Web Application Platform installation is displayed, press <strong>Enter</strong> to continue.</p></li><li><span style="color:var(--ds-text,#333333);">Specify the location where you want to install Web Application Platform:</span><ul><li>Press <strong>Enter</strong> to use the default installation directory.</li><li>Enter the full path to the installation directory and press <strong>Enter</strong>.</li></ul></li><li>Type &quot;2&quot; to select the <strong>Advanced</strong> installation option and press <strong>Enter</strong>.</li><li>Follow the on-screen installation instructions.</li><li><span style="color:var(--ds-text,#333333);">When the Pre-Installation Summary is displayed, check if properties are specified correctly, and</span> press <strong>Enter</strong> to start the installation.</li><li><span style="color:var(--ds-text,#333333);">When Web Application Platform is successfully installed</span>, press <strong>Enter</strong>.</li><li>If you want to start the WebApp service right after installation, press <strong>Enter</strong>. Otherwise, type &quot;0&quot; and press <strong>Enter</strong>.</li><li><span style="color:var(--ds-text,#333333);">If you installed the</span><span style="color:var(--ds-text,#333333);"><span> </span>Came Collaborator for Teamwork Cloud service,</span> apply the Cameo Collaborator license.</li></ol><p><span style="color:var(--ds-text,#333333);"><br />Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /></ac:link>. To access Web Application Platform, open a web browser and go to <em>http(s)://&lt;domain_name&gt;:&lt;port&gt;/webapp</em>.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Scripts for upgrading Java and Tomcat in the Linux environment:</strong></p><ul><li>Java: <ac:link><ri:attachment ri:filename="upgrade_jdk_webapp.sh" /></ac:link></li><li>Tomcat: <ac:link><ri:attachment ri:filename="upgrade_tomcat_webapp.sh" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491281 space=TWCloud2024xR1 version=3 -->
## PAGE 00146: Installing Web Application Platform on Linux with GUI

- page_id: `170491281`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491281/Installing+Web+Application+Platform+on+Linux+with+GUI
- version_number: 3
- version_date: `2025-12-10T10:34:26.666+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: []

### NORMALIZED CONTENT

The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services used with Teamwork Cloud.

#### NOTE: Installation prerequisites and other important information

Installation prerequisites and other important information

Before installing Web Application Platform with services, you need to:

- Have a working instance of Teamwork Cloud.
- If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that [CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024xR1'] or [CONFLUENCE_PAGE title='Installing the FlexNet server' space=''] is installed beforehand.
- [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the *Web_App_Platform_<version number>_unix.sh* file.
- Increase the open file limit for the OS (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.
- Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.

Before starting the installation, you should know the following:

- We recommend installing Web Application Platform and Teamwork Cloud on different machines.
- Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <install_root>/TeamworkCloud/configuration directory). You will need this data during installation.
- After installing Web Application Platform, it is recommended to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] on the machine where Teamwork Cloud is installed.

To install Web Application Platform and services (advanced installation)

1. Run the Web_App_Platform_<version number>_unix.sh file as an administrator to start the installation wizard.
2. Specify the location where you want to install the Web Application Platform and click Next .
3. Select the Advanced Install radio button and click Next .
4. Follow the on-screen instructions in the installation wizard and click Next after each step.
5. When the Pre-Installation Summary is displayed, check if all the installation properties are specified correctly and click Install .
6. After successful installation, click Next .
7. If you do not want to start the WebApp service right after installation, clear the Start WebApp Service check box.
8. Click Done to close the installation wizard.
9. If you installed Cameo Collaborator for Teamwork Cloud service, apply the Cameo Collaborator license.

Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space='']. To access Web Application Platform, open a web browser and go to *http(s)://<domain_name>:<port>/webapp*.

**Scripts for upgrading Java and Tomcat in the Linux environment:**

- Java: [ATTACHMENT filename='upgrade_jdk_webapp.sh']
- Tomcat: [ATTACHMENT filename='upgrade_tomcat_webapp.sh']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services used with Teamwork Cloud.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="265a25a2-18bc-4ad8-8c9b-354bcfe415b6"><ac:parameter ac:name="title">Installation prerequisites and other important information</ac:parameter><ac:rich-text-body><p>Before installing Web Application Platform with services, you need to:</p><ul><li>Have a working instance of Teamwork Cloud.</li><li><span style="color:var(--ds-text,#333333);">If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[DSLS]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Installing the FlexNet server" /><ac:plain-text-link-body><![CDATA[the FlexNet license server]]></ac:plain-text-link-body></ac:link> is installed beforehand.</span></li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the <em>Web_App_Platform_&lt;version number&gt;_unix.sh</em> file.</ac:link-body></ac:link></li><li><a href="https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491407/Advanced+services+configuration#Advancedservicesconfiguration-IncreasingopenfilelimitonLinux">Increase the open file limit for the OS</a> (or for Web Application Platform/Tomcat) to a minimum of 20 000 files.</li><li>Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.</li></ul><p><span style="color:var(--ds-text,#333333);">Before starting the installation, you should know the following:</span></p><ul><li>We recommend installing Web Application Platform and Teamwork Cloud on different machines.</li><li>Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <em>&lt;install_root&gt;/TeamworkCloud/configuration</em> directory). You will need this data during installation.</li><li>After installing Web Application Platform, it is recommended to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[stop the WebApp service]]></ac:plain-text-link-body></ac:link> on the machine where Teamwork Cloud is installed.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To install Web Application Platform and services (advanced installation)</p><hr /><ol><li>Run the <em>Web_App_Platform_&lt;version number&gt;_unix.sh</em> file as an administrator to start the installation wizard.</li><li>Specify the location where you want to install the Web Application Platform and click <strong>Next</strong>.</li><li>Select the <strong>Advanced Install</strong> radio button and click <strong>Next</strong>.</li><li>Follow the on-screen instructions in the installation wizard and click<span> </span><strong>Next</strong><span> </span>after each step.</li><li><span style="color:var(--ds-text,#333333);">When the Pre-Installation Summary is displayed, check if all the installation properties are specified correctly and click<span> </span></span><strong style="text-align: left;">Install</strong><span style="color:var(--ds-text,#333333);">.</span></li><li>After successful installation, click<span> </span><strong>Next</strong>.</li><li>If you do not want to start the WebApp service right after installation, clear the<span> </span><strong>Start WebApp Service</strong><span> </span>check box.</li><li>Click <strong>Done</strong> to close the installation wizard.</li><li>If you installed Cameo Collaborator for Teamwork Cloud service, apply the Cameo Collaborator license.</li></ol><p><br />Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /></ac:link>. To access Web Application Platform, open a web browser and go to <em>http(s)://&lt;domain_name&gt;:&lt;port&gt;/webapp</em>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Scripts for upgrading Java and Tomcat in the Linux environment:</strong></p><ul><li>Java: <ac:link><ri:attachment ri:filename="upgrade_jdk_webapp.sh" /></ac:link></li><li>Tomcat: <ac:link><ri:attachment ri:filename="upgrade_tomcat_webapp.sh" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491284 space=TWCloud2024xR1 version=3 -->
## PAGE 00147: Installing Web Application Platform on Windows

- page_id: `170491284`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491284/Installing+Web+Application+Platform+on+Windows
- version_number: 3
- version_date: `2025-10-30T13:40:37.380+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: []

### NORMALIZED CONTENT

The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services used with Teamwork Cloud.

#### NOTE: Installation prerequisites and other important information

Installation prerequisites and other important information

Before installing Web Application Platform with services, you need to:

- Have a working instance of Teamwork Cloud.
- If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that [CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024xR1'] or the [CONFLUENCE_PAGE title='Installing the FlexNet server' space='TWCloud2024x'] is installed beforehand.
- [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the *Web_App_Platform_<version number>_win64.exe* file .
- Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.

Before starting the installation, you should know the following:

- We recommend installing Web Application Platform and Teamwork Cloud on different machines.
- Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <install_root>\TeamworkCloud\configuration directory). You will need this data during installation.
- After installing Web Application Platform, it is recommended to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] on the machine where Teamwork Cloud is installed.

To install Web Application Platform and services (advanced installation)

1. Run the Web_App_Platform_<version number>_win64.exe file as an administrator to start the installation wizard.
2. Specify the location where you want to install Web Application Platform and click Next .
3. Select the Advanced Install radio button and click Next .
4. Follow the on-screen instructions in the installation wizard and click Next after each step.
5. When the Pre-Installation Summary is displayed, check if all the installation properties are specified correctly and click **Install**.
6. After successful installation, click Next .
7. If you do not want to start the WebApp service right after installation, clear the Start WebApp Service check box.
8. Click Done to close the installation wizard.
9. If you installed the Came Collaborator for Teamwork Cloud service, apply the Cameo Collaborator license.

Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space='']. To access Web Application Platform, open a web browser and go to *http(s)://<domain_name>:<port>/webapp*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The content of this chapter is intended for system administrators. Here, you can learn how to install and configure Web Application Platform with Cameo Collaborator and other services used with Teamwork Cloud. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="23a637d8-0dc4-4e2f-8517-02e8093618f4"><ac:parameter ac:name="title">Installation prerequisites and other important information</ac:parameter><ac:rich-text-body><p>Before installing Web Application Platform with services, you need to:</p><ul><li>Have a working instance of Teamwork Cloud.</li><li>If you intend to install the Cameo Collaborator for Teamwork Cloud service, make sure that <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[DSLS]]></ac:plain-text-link-body></ac:link> or the <ac:link><ri:page ri:space-key="TWCloud2024x" ri:content-title="Installing the FlexNet server" /><ac:plain-text-link-body><![CDATA[FlexNet license server]]></ac:plain-text-link-body></ac:link> is installed beforehand.</li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the <em>Web_App_Platform_&lt;version number&gt;_win64.exe</em> file</ac:link-body></ac:link>.</li><li>Have access to the KeyStore file with the same certificate that is used in Teamwork Cloud for authentication configuration.</li></ul><p>Before starting the installation, you should know the following:</p><ul><li>We recommend installing Web Application Platform and Teamwork Cloud on different machines.</li><li>Before installing Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <em>&lt;install_root&gt;\TeamworkCloud\configuration</em> directory). You will need this data during installation.</li><li>After installing Web Application Platform, it is recommended to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[stop the WebApp service]]></ac:plain-text-link-body></ac:link> on the machine where Teamwork Cloud is installed.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To install Web Application Platform and services (advanced installation)</p><hr style="" /><ol><li>Run the <em>Web_App_Platform_&lt;version number&gt;_win64.exe</em> file as an administrator to start the installation wizard.</li><li>Specify the location where you want to install Web Application Platform and click <strong>Next</strong>.</li><li>Select the <strong>Advanced Install</strong> radio button and click <strong>Next</strong>.</li><li>Follow the on-screen instructions in the installation wizard and click <strong>Next</strong> after each step.</li><li><p class="auto-cursor-target">When the Pre-Installation Summary is displayed, check if all the installation properties are specified correctly and click <strong>Install</strong>.</p></li><li>After successful installation, click <strong>Next</strong>.</li><li>If you do not want to start the WebApp service right after installation, clear the <strong>Start WebApp Service</strong> check box.</li><li>Click <strong>Done</strong> to close the installation wizard.</li><li>If you installed the Came Collaborator for Teamwork Cloud service, apply the Cameo Collaborator license.</li></ol><p><br />Web Application Platform is now installed with the selected services. For information on how to start Web Application Platform, refer to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /></ac:link>. To access Web Application Platform, open a web browser and go to <em>http(s)://&lt;domain_name&gt;:&lt;port&gt;/webapp</em>.</p>
````

<!--NOMAGIC_PAGE id=170491383 space=TWCloud2024xR1 version=3 -->
## PAGE 00148: Integrating authentication server with ForgeRock

- page_id: `170491383`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491383/Integrating+authentication+server+with+ForgeRock
- version_number: 3
- version_date: `2024-10-17T15:18:11.138+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration > Authentication server
- labels: []

### NORMALIZED CONTENT

**On this page**

5

This page contains the instructions to integrate the authentication server with the ForgeRock application (ForgeRock is the company that develops open-source identity and access management products for cloud, social, mobile, and enterprise environments). This documentation is based on ForgeRock version 13.0.0.

##### Integrating the authentication server with ForgeRock

To integrate the authentication server with ForgeRock

1. Log in to ForgeRock as administrator.
2. Either select or create the realm, which will be used for integration. Make sure that the realm uses stateful sessions. The realm in this example is "twc".
3. In the realm overview select **Authentication** > **Settings**.
4. Click the **General** tab and clear the **Use Stateless Sessions** check box.
5. Click **Save Changes**. 
[IMAGE alt='' src='']
6. Go back to Dashboard and in the realm overview, select Create SAMLv2 Providers and then Create Hosted Identity Provider . [ATTACHMENT filename='realm-settings (2).png'] [ATTACHMENT filename='realm-settings (3).png']
7. Fill in the Identity Provider data by selecting the realm, the signing key, and entering a new circle of trust's name. 
[IMAGE alt='' src='']
8. Click **Configure** to save the Identity Provider.
9. Return to the main page.
10. Select **FEDERATION** menu item and select to modify the newly created Identity Provider in the**Entity Providers** table in the **Circle of Trust Configuration** section.
11. Remove the value "**urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=**" in **NameID Value Map** in the **Assertion Content** tab, if any.
12. Add the value "**urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=uid**" to the map. By default, this nameID is used in the Authentication Server for user identification (**authserver.properties** parameter **[authentication.saml.name.id](http://authentication.saml.name.id).format**). 
[IMAGE alt='' src='']
13. Save the configuration changes.

##### Deploying the authentication server

To deploy the authentication server

1. During the deployment process add the SAML integration configuration parameters to the file authserver.properties .
  - Se t **authentication.saml.enabled** to true .
  - If the authentication server is deployed on a cluster, set value for the parameter **[authentication.saml.entity.id](http://authentication.saml.entity.id)**(default is **com.nomagic.authentication.server**).This value should be unique for each authentication server instance.
  - Set **authentication.saml.idp.metadata.url** t o the appropriate ForgeRock server address (should be [http://<server>:<port>/openam/saml2/jsp/exportmetadata.jsp?entityid=http://<server>:<port>/openam&realm=/<realm name>](http://openam.nomagic.com:8080/openam/saml2/jsp/exportmetadata.jsp?entityid=http://openam.nomagic.com:8080/openam&realm=/twc) ).
  - Set the name of the button to the parameter **authentication.saml.link** . Users will click this button to log in using ForgeRock as the Identity Provider.
2. Save the authserver.properties file and (re)start the WebApp service.

##### Configuring SAMLv2 Remote Service Provider

To configure SAMLv2 Remote Service Provider

1. Go back to ForgeRock and, in the realm overview, select Create SAMLv2 Providers and then Register Remote Service Provider .
2. Select the realm.
3. Specify the URL of Authentication Server metadata: *http[s]://<auth-server-host>:<auth-server-port>/authentication/saml2/metadata* (if such URL is accessible from ForgeRock) or select a file of stored Authentication Server metadata (usually used in **https** case).
4. Enter or select the same circle of trust as that of the Identity Provider and click Configure . [ATTACHMENT filename='realm-settings (6).png']
5. A Service Provider with the default name **com.nomagic.authentication.server** w ill be created. The name of the service provider is configured in the Authentication Server's authserver.properties file (paramet er **[authentication.saml.entity.id](http://authentication.saml.entity.id)**).

Once you have completed the steps on this page, you should be able to log in through ForgeRock by clicking the SAML integration button on the**Authentication Server** login page. If later the Authentication Server configuration, related to SAML or server keystore file is changed, delete the remote service provider and add a new one (see Register Remote Service Provider]]>).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d36871dd-69bb-48b3-bad0-93b215e0bebe"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This page contains the instructions to integrate the authentication server with the ForgeRock application (ForgeRock is t<span style="color: rgb(34,34,34);">he company that develops open-source identity and access management products for cloud, social, mobile, and enterprise environments</span>). <span>This documentation is based on ForgeRock version 13.0.0.</span></p><h3>Integrating the authentication server with ForgeRock</h3><p>To integrate the authentication server with ForgeRock</p><hr /><ol><li><p>Log in to ForgeRock as administrator.</p></li><li><p>Either select or create the realm, which will be used for integration. Make sure that the realm uses stateful sessions. The realm in this example is &quot;twc&quot;.</p></li><li><p>In the realm overview select <strong>Authentication</strong> &gt; <strong>Settings</strong>.</p></li><li><p>Click the <strong>General</strong> tab and clear the <strong>Use Stateless Sessions</strong> check box.</p></li><li><p>Click <strong>Save Changes</strong>.<br /><ac:image ac:border="true" ac:height="505" ac:width="1003"><ri:attachment ri:filename="realm-settings (1).png" /></ac:image></p></li><li>Go back to <strong>Dashboard </strong>and in the realm overview, select <strong>Create SAMLv2 Providers </strong>and then <strong>Create Hosted Identity Provider</strong>.<br /><br /><ac:image ac:border="true" ac:height="602" ac:width="1124"><ri:attachment ri:filename="realm-settings (2).png" /></ac:image><br /><br /><br /><br /><br /><ac:image ac:border="true" ac:height="465" ac:width="1114"><ri:attachment ri:filename="realm-settings (3).png" /></ac:image><br /><br /><br /><br /></li><li><p>Fill in the Identity Provider data by selecting the realm, the signing key, and entering a new circle of trust's name.<br /><ac:image ac:border="true" ac:height="660" ac:width="1214"><ri:attachment ri:filename="realm-settings (4).png" /></ac:image></p></li><li><p>Click <strong>Configure</strong> to save the Identity Provider.</p></li><li><p>Return to the main page.</p></li><li><p>Select <strong>FEDERATION</strong> menu item and select to modify the newly created Identity Provider in the<strong> Entity Providers</strong> table in the <strong>Circle of Trust Configuration</strong> section.</p></li><li><p>Remove the value &quot;<strong><span style="color: rgb(0,0,128);"><span style="color: rgb(51,51,51);">urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</span></span>=</strong>&quot; in <strong>NameID Value Map</strong> in the <strong>Assertion Content</strong> tab, if any.</p></li><li><p>Add the value &quot;<strong><span style="color: rgb(0,0,128);"><span style="color: rgb(51,51,51);">urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</span></span>=uid</strong>&quot; to the map. By default, this nameID is used in the Authentication Server for user identification (<strong>authserver.properties</strong> parameter <strong><span style="color: rgb(0,0,128);"><a href="http://authentication.saml.name.id">authentication.saml.name.id</a>.format</span></strong>).<br /><ac:image ac:border="true" ac:height="229" ac:width="713"><ri:attachment ri:filename="realm-settings (5).png" /></ac:image></p></li><li><p>Save the configuration changes.</p></li></ol><h3>Deploying the authentication server</h3><p>To deploy the authentication server</p><hr /><ol><li>During the deployment process add the SAML integration configuration parameters to the file <strong>authserver.properties</strong>.<br /><br /><ul><li>Se<span style="color: rgb(0,51,102);">t </span><span style="color: rgb(0,51,102);"><strong>authentication.saml.enabled</strong></span> to <em>true</em>.</li><li><p>If the authentication server is deployed on a cluster, set value for the parameter <span style="color: rgb(0,0,128);"><strong><a href="http://authentication.saml.entity.id">authentication.saml.entity.id</a></strong><span style="color: rgb(51,51,51);"> (default is <strong>com.nomagic.authentication.server</strong>)</span>.<span style="color: rgb(51,51,51);"> This value should be unique for each authentication server instance.</span></span></p></li><li>Set <span style="color: rgb(0,51,102);"><strong>authentication.saml.idp.metadata.url</strong> t</span>o the appropriate ForgeRock server address (should be <em><span style="color: rgb(0,128,0);"><a class="external-link" href="http://openam.nomagic.com:8080/openam/saml2/jsp/exportmetadata.jsp?entityid=http://openam.nomagic.com:8080/openam&amp;realm=/twc" rel="nofollow">http://&lt;server&gt;:&lt;port&gt;/openam/saml2/jsp/exportmetadata.jsp?entityid=http://&lt;server&gt;:&lt;port&gt;/openam&amp;realm=/&lt;realm name&gt;</a></span></em>).</li><li>Set the name of the button to the parameter <span style="color: rgb(0,51,102);"><strong>authentication.saml.link</strong></span>. Users will click this button to log in using ForgeRock as the Identity Provider.<br /><br /></li></ul></li><li>Save the <strong>authserver.properties</strong> file and (re)start the WebApp service.</li></ol><h3>Configuring SAMLv2 Remote Service Provider</h3><p>To configure SAMLv2 Remote Service Provider</p><hr /><ol><li>Go back to ForgeRock and, in the realm overview, select <strong>Create SAMLv2 Providers</strong> and then <strong>Register Remote Service Provider</strong>.</li><li>Select the realm.</li><li>Specify the URL of Authentication Server metadata: <span class="nolink"><em>http[s]://&lt;auth-server-host&gt;:&lt;auth-server-port&gt;/authentication/saml2/metadata</em> (if such URL is accessible from ForgeRock) or select a file of stored Authentication Server metadata (usually used in <strong>https</strong> case).</span></li><li><span class="nolink">Enter or select </span>the same circle of trust as that of the Identity Provider and click <strong>Configure</strong>.<br /><br /><ac:image ac:border="true" ac:height="531" ac:width="1214"><ri:attachment ri:filename="realm-settings (6).png" /></ac:image><br /><br /><br /></li><li>A Service Provider with the default name <span style="color: rgb(0,51,102);"><strong>com.nomagic.authentication.server</strong> w</span>ill be created. The name of the service provider is configured in the Authentication Server's <strong><span style="color: rgb(62,63,64);">authserver</span>.properties</strong> file (paramet<span style="color: rgb(0,51,102);">er <strong><a href="http://authentication.saml.entity.id">authentication.saml.entity.id</a></strong>).</span></li></ol><p><br /></p><p>Once you have completed the steps on this page, you should be able to log in through ForgeRock by clicking the SAML integration button on the<strong> Authentication Server</strong> login page. <span>If later the Authentication Server configuration, related to SAML or server keystore file is changed, delete the remote service provider and add a new one (see <ac:link ac:anchor="SAMLv2"><ac:plain-text-link-body><![CDATA[Create SAMLv2 Providers > Register Remote Service Provider]]></ac:plain-text-link-body></ac:link>).</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491398 space=TWCloud2024xR1 version=3 -->
## PAGE 00149: Keystore parameters

- page_id: `170491398`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491398/Keystore+parameters
- version_number: 3
- version_date: `2024-12-09T15:39:21.062+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration > Authentication server
- labels: []

### NORMALIZED CONTENT

The following parameters are required by the authentication server to sign the authentication token.

| Parameter | Required | Description | Default value |
| --- | --- | --- | --- |
| authentication.server.key-store | yes | The path to a keystore file in the file system. It can be relative to the WebAppPlatform directory or absolute. | ./shared/conf/keystore.p12 |
| authentication.server.key-store-type | yes | A keystore type. The available types are PKCS12 and JKS. | PKCS12 |
| authentication.server.key-store-password | no | A keystore password (required if the keystore is password-protected). It should be changed for a production environment. | nomagic |
| authentication.server.key-password | no | A private key password (required if the private key is password-protected). It should be changed for a production environment. | nomagic |
| authentication.server.key-alias | yes | A private key alias used to identify a key in the keystore. | webapp |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="903a5f5f-e303-476d-aa02-f0d4a58a6dbe">The following parameters are required by the authentication server to sign the authentication token.<br /></ac:inline-comment-marker></p><table class="relative-table wrapped" style="width: 97.3984%;"><colgroup><col style="width: 18.1562%;" /><col style="width: 6.66138%;" /><col style="width: 60.7177%;" /><col style="width: 14.5096%;" /></colgroup><thead><tr><th><p>Parameter</p></th><th colspan="1"><p>Required</p></th><th><p>Description</p></th><th colspan="1">Default value</th></tr></thead><tbody><tr><td><ac:inline-comment-marker ac:ref="f376aef2-6e56-4725-95f9-79a3026beb12">authentication.server.key-store<br /></ac:inline-comment-marker></td><td colspan="1">yes</td><td>The path to a keystore file in the file system. It can be relative to the <em>WebAppPlatform</em> directory or absolute.</td><td colspan="1">./shared/conf/keystore.p12</td></tr><tr><td><p>authentication.server.key-store-type</p></td><td colspan="1">yes</td><td>A keystore type. The available types are PKCS12 and JKS.</td><td colspan="1">PKCS12</td></tr><tr><td><p>authentication.server.key-store-password</p></td><td colspan="1">no</td><td>A keystore password (required if the keystore is password-protected). It should be changed for a production environment.</td><td colspan="1">nomagic</td></tr><tr><td><p>authentication.server.key-password</p></td><td colspan="1">no</td><td>A private key password (required if the private key is password-protected). It should be changed for a production environment.</td><td colspan="1">nomagic</td></tr><tr><td><p>authentication.server.key-alias</p></td><td colspan="1">yes</td><td>A private key alias used to identify a key in the keystore.</td><td colspan="1">webapp</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170491401 space=TWCloud2024xR1 version=8 -->
## PAGE 00150: Layer 4 and Layer 7 proxy setup

- page_id: `170491401`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491401/Layer+4+and+Layer+7+proxy+setup
- version_number: 8
- version_date: `2024-12-17T15:50:09.620+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration
- labels: []

### NORMALIZED CONTENT

**On this page**

42

**Scripts**

- [ATTACHMENT filename='nGinx-Proxy-Pkg.zip']
- [ATTACHMENT filename='HAProxy-Pkg.zip']

Please note that this information is provided as a courtesy only and support services are not offered for any of the features described in this article.

#### Introduction

There are environments in which Teamwork Cloud applications need to be fronted by a proxy. The most widespread use case for this is port restrictions, where the native ports cannot be exposed. Typically, all external traffic is restricted to a single port, such as 443, which is allowed to traverse corporate firewalls or proxies.

To configure a proxy, you first need to understand the traffic flows, since each traffic flow needs to be addressed. Teamwork Cloud is composed of two services (Webapp and Teamwork Cloud), which need to expose three traffic flows (or port bindings) to function.

- Webapp (native port 8443 - http/s)
- Teamwork Cloud
  - REST API (native port 8111 - http/s)
  - Client Communication (native port 3579 -TCP cleartext or native port 10002 - TLS/TCP encrypted) - 10002 is the default port used by the client and is configured in the Teamwork Cloud Admin Settings page

Additionally, if the FlexNet license server is running on the same instance with the same port constraints, a TCP proxy must be created for it, forwarding to our cameo vendor daemon (native port 1101 - TCP).

Because you can only bind a single instance of a port to an IP address in TCP/IP, the instance will need to have multiple IP addresses in which to bind each traffic flow. Traffic flows are tied to frontends (the part of the proxy exposed to the external world that receives requests and forwards them to the backends) and backends (handling of the actual requests). The number of IP addresses required depends on the type of proxying you configure.

There are two types of proxying: TCP (the proxying is done at Layer 4 of the OSI model); or HTTP (the proxying is done at Layer 7 of the OSI).

###### Layer 4 (TCP) Proxy

Layer 4 proxying is the lighter-weight of the 2 methods as it simply forwards incoming packets from the frontend to its associated backend. In this case, you need 3 IP addresses (4 if proxying FlexNet as well) in order to bind to each data flow.

[IMAGE alt='' src='']

###### Layer 4 proxy configuration example.

###### Layer 7 (HTTPS) Proxy

Layer 7 proxying inspects the actual content of the data coming through the proxy. Therefore, SSL termination takes place at the proxy, so you can now manipulate the data coming through and take specific actions. Since each of the HTTPS services exposes a path (/webapp for authentication and Web Platform applications, /osmc for REST API), you can treat the incoming data as a single flow (a single frontend), and have the proxy send the request to the respective backend based on the path of the request.

Please note that the diagram below depicts a hybrid layer 7 configuration.

[IMAGE alt='' src='']

###### Layer 7 proxy configuration example.

There are 2 classes of proxies/load balancers: hardware (such as F5 Big-IP, Cirtix NetScaler) which is external to the application instance; and software (such as nGinx, HAProxy) which can be run externally (on a dedicated instance) or on the same instance as the application.

#### Proxy configuration

This section provides an outline and examples of how to deploy both Layer 4 (TCP) and Layer 7 Hybrid (HTTPS) proxies for [ATTACHMENT filename='nGinx-Proxy-Pkg.zip'] and [ATTACHMENT filename='HAProxy-Pkg.zip']. The Layer 7 configuration is a hybrid configuration in that it also includes Layer 4 proxying for the modeling tool client data stream and FlexNet server. Prepackaged configuration scripts and template files are provided here to generate the basic configuration files.

Teamwork Cloud is initially deployed with a local IP address. This will become the IP address for the Webapp frontend. Keep in mind that the native ports (8443, 8111, client↔Teamwork Cloud port, and the cameo vendor daemon for FlexNet) bind to all interfaces.

The example configuration packages use four IP addresses - 10.254.254.31 (Webapp), 10.254.254.32 (REST), 10.254.254.34 (client↔Teamwork Cloud), and 10.254.254.35 (FlexNet). These are the most basic configurations that allow the system to operate. You may add features or change behaviors by modifying these files.

Note that to simplify all of the aspects of certificates, you should either use a wildcard certificate or one that contains SANs for all of the public FQDNs and/or IP addresses.

In a Layer 7 Hybrid HTTPS proxy, SSL termination occurs at the proxy. A PEM-encoded file containing the private key and certificates is needed for the server, including the full certificate chain.

#### Proxy configuration in Web Application Platform

For security reasons, we recommend leaving port 8080 disabled and not allowing external access to port 8443.

After deploying a Layer 4 (TCP) or Layer 7 (HTTPS) proxy, complete the steps below to configure Web Application Platform.

To configure Web Application Platform after deploying a proxy

1. Go to the *<install_root>/WebAppPlatform/shared/conf* directory and open for editing the *authserver.properties* file.
2. Add the Web Application Platform URL to the values of the **authentication.redirect.uri.whitelist** property to allow the proxied Teamwork Cloud web access. If port 443 is used as the public port for Web Application Platform, omit the port number. bashExample of authserver.properties
3. Go to the *<install_root>/WebAppPlatform/shared/conf* directory and open for editing the *webappplatform.properties*file.
4. Update the Authentication server address and port. bashExample of webappplatform.properties
5. Update the service.url property to the public URL of service(s). bashExample of webappplatform.properties
6. Restart Web Application Platform.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"> <strong style="letter-spacing: 0.0px;">On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="2c627834-cd60-4794-b84e-e29024465346"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">2</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><strong>Scripts</strong></p><ul><li><ac:link><ri:attachment ri:filename="nGinx-Proxy-Pkg.zip" /></ac:link></li><li><ac:link><ri:attachment ri:filename="HAProxy-Pkg.zip" /></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0a1a3c66-850f-4f9a-81f7-b0e801ddab0c"><ac:rich-text-body><p>Please note that this information is provided as a courtesy only and support services are not offered for any of the features described in this article.</p></ac:rich-text-body></ac:structured-macro><h2><span>Introduction</span></h2><p>There are environments in which Teamwork Cloud applications need to be fronted by a proxy. The most widespread use case for this is port restrictions, where the native ports cannot be exposed.  Typically, all external traffic is restricted to a single port, such as 443, which is allowed to traverse corporate firewalls or proxies.</p><p>To configure a proxy, you first need to understand the traffic flows, since each traffic flow needs to be addressed. Teamwork Cloud is composed of two services (Webapp and Teamwork Cloud), which need to expose three traffic flows (or port bindings) to function.</p><ul><li>Webapp (native port 8443 - http/s)</li><li>Teamwork Cloud<ul><li>REST API (native port 8111 - http/s)</li><li>Client Communication (native port 3579 -TCP cleartext or native port 10002 - TLS/TCP encrypted) - 10002 is the default port used by the client and is configured in the Teamwork Cloud Admin Settings page</li></ul></li></ul><p>Additionally, if the FlexNet license server is running on the same instance with the same port constraints, a TCP proxy must be created for it, forwarding to our cameo vendor daemon (native port 1101 - TCP).</p><p>Because you can only bind a single instance of a port to an IP address in TCP/IP, the instance will need to have multiple IP addresses in which to bind each traffic flow. Traffic flows are tied to frontends (the part of the proxy exposed to the external world that receives requests and forwards them to the backends) and backends (handling of the actual requests). The number of IP addresses required depends on the type of proxying you configure.</p><p>There are two types of proxying: TCP (the proxying is done at Layer 4 of the OSI model); or HTTP (the proxying is done at Layer 7 of the OSI).</p><h4>Layer 4 (TCP) Proxy</h4><p>Layer 4 proxying is the lighter-weight of the 2 methods as it simply forwards incoming packets from the frontend to its associated backend. In this case, you need 3 IP addresses (4 if proxying FlexNet as well) in order to bind to each data flow.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Layer4_TCPProxy.png" /></ac:image></p><h6 style="text-align: center;">Layer 4 proxy configuration example.</h6><h4 style="text-align: left;">Layer 7 (HTTPS) Proxy</h4><p>Layer 7 proxying inspects the actual content of the data coming through the proxy. Therefore, SSL termination takes place at the proxy, so you can now manipulate the data coming through and take specific actions. Since each of the HTTPS services exposes a path (<span style="color: rgb(62,63,64);">/webapp for authentication and Web Platform applications, /osmc for REST API</span>), you can treat the incoming data as a single flow (a single frontend), and have the proxy send the request to the respective backend based on the path of the request.</p><p><span style="color: rgb(62,63,64);">Please note that the diagram below depicts a hybrid layer 7 configuration.</span></p><p><ac:image><ri:attachment ri:filename="Layer7Hyb_HTTPProxy.png" /></ac:image></p><h6 style="text-align: center;">Layer 7 proxy configuration example.</h6><p>There are 2 classes of proxies/load balancers: hardware (such as F5 Big-IP, Cirtix NetScaler) which is external to the application instance; and software (such as nGinx, HAProxy) which can be run externally (on a dedicated instance) or on the same instance as the application.</p><h2><span>Proxy configuration</span></h2><p style="text-align: left;">This section provides an outline and examples of how to deploy both Layer 4 (TCP) and Layer 7 Hybrid (HTTPS) proxies for <ac:link><ri:attachment ri:filename="nGinx-Proxy-Pkg.zip" /><ac:plain-text-link-body><![CDATA[nGinx]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:attachment ri:filename="HAProxy-Pkg.zip" /><ac:plain-text-link-body><![CDATA[HAProxy]]></ac:plain-text-link-body></ac:link>. The Layer 7 configuration is a hybrid configuration in that it also includes Layer 4 proxying for the modeling tool client data stream and FlexNet server. Prepackaged configuration scripts and template files are provided here to generate the basic configuration files.</p><p style="text-align: left;">Teamwork Cloud is initially deployed with a local IP address. This will become the IP address for the Webapp frontend. Keep in mind that the native ports (8443, 8111, client↔Teamwork Cloud port, and the cameo vendor daemon for FlexNet) bind to all interfaces.</p><p style="text-align: left;">The example configuration packages use four IP addresses - 10.254.254.31 (Webapp), 10.254.254.32 (REST), 10.254.254.34 (client↔Teamwork Cloud), and 10.254.254.35 (FlexNet). These are the most basic configurations that allow the system to operate. You may add features or change behaviors by modifying these files.</p><p style="text-align: left;">Note that to simplify all of the aspects of certificates, you should either use a wildcard certificate or one that contains SANs for all of the public FQDNs and/or IP addresses.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="b9753844-3fe0-4b4f-bacb-57007892ceb2"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">In a Layer 7 Hybrid HTTPS proxy, SSL termination occurs at the proxy. A PEM-encoded file containing the private key and certificates is needed for the server, including the full certificate chain.</span></p></ac:rich-text-body></ac:structured-macro><h2><span>Proxy configuration in Web Application Platform</span></h2><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="70a11874-55d7-4c47-b45e-cb68d666f602"><ac:rich-text-body>For security reasons, we recommend leaving port 8080 disabled and not allowing external access to port 8443.</ac:rich-text-body></ac:structured-macro><p style="text-align: left;">After deploying a Layer 4 (TCP) or Layer 7 (HTTPS) proxy, complete the steps below to configure Web Application Platform.</p><p style="text-align: left;"><br /></p><p style="text-align: left;">To configure Web Application Platform after deploying a proxy</p><hr /><ol><li><p class="auto-cursor-target">Go to the <em>&lt;install_root&gt;/WebAppPlatform/shared/conf</em> directory and open for editing the <em>authserver.properties</em> file.</p></li><li><p class="auto-cursor-target">Add the Web Application Platform URL to the values of the <strong>authentication.redirect.uri.whitelist</strong> property to allow the proxied Teamwork Cloud web access. If port 443 is used as the public port for Web Application Platform, omit the port number.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ee81813a-3232-4415-ad5e-39cdf4d98db5"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example of authserver.properties</ac:parameter><ac:plain-text-body><![CDATA[authentication.redirect.uri.whitelist=https://10.254.254.31:8443/,https://10.254.254.31:8111/,https://md_redirect,https://10.254.254.31/]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Go to the <em>&lt;install_root&gt;/WebAppPlatform/shared/conf</em> directory and open for editing the <em>webappplatform.properties</em><span> file.</span></p></li><li><p class="auto-cursor-target"><span>Update the Authentication server address and port.<br /></span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d45e1c64-af4e-41fd-9162-175bc2220044"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example of webappplatform.properties</ac:parameter><ac:plain-text-body><![CDATA[# Specify the WebApp authentication server location.
# IP address or domain name.
authentication.server.ip=10.254.254.31
# Specify the Authentication server port.
authentication.server.port=443]]></ac:plain-text-body></ac:structured-macro></li><li>Update the <strong>service.url </strong>property to the public URL of service(s). <br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3ae3bc02-d3c1-4cdf-8060-5887241375ed"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example of webappplatform.properties</ac:parameter><ac:plain-text-body><![CDATA[# Specify the public URL of service(s),
# for example, http(s)://my.domain:8443/
service.url=https://proxy.domain.name:443/]]></ac:plain-text-body></ac:structured-macro></li><li>Restart Web Application Platform.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180157 space=TWCloud2024xR1 version=2 -->
## PAGE 00151: LDAP setup for Active Directory

- page_id: `171180157`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180157/LDAP+setup+for+Active+Directory
- version_number: 2
- version_date: `2025-10-30T14:43:57.932+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Managing LDAP servers
- labels: []

### NORMALIZED CONTENT

The following is an example of the LDAP Structure for Active Directory.

[IMAGE alt='' src='']

###### LDAP structure (Active Directory).

To configure [CONFLUENCE_PAGE title='Adding and configuring LDAP server' space=''] for Active Directory

1. Go to the Settings application to open the LDAP m anagement page.
2. Click Create LDAP configuration button to open t he Create LDAP configuration pane.
3. Configure the LDAP settings, for example:
  - The LDAP users are under CN=Users record.
  - The LDAP server is starting at machine IP address 127.0.0.1 with a default LDAP port 389.

The following figure represents a simple LDAP (Active Directory) configuration example in Teamwork Cloud Admin:

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following is an example of the LDAP Structure for Active Directory.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="image2017-4-10_15-30-10.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">LDAP structure (Active Directory).</h6><p>To configure <ac:link><ri:page ri:content-title="Adding and configuring LDAP server" /><ac:plain-text-link-body><![CDATA[LDAP properties]]></ac:plain-text-link-body></ac:link> for Active Directory</p><hr style="" /><ol><li class="Standard">Go to the <strong>Settings </strong>application to open the <strong>LDAP m</strong><strong>anagement</strong> page.</li><li class="Standard">Click <strong>Create LDAP configuration</strong><span class="confluence-embedded-file-wrapper"> button to open t</span>he <strong>Create LDAP configuration</strong> pane.</li><li class="Standard">Configure the LDAP settings, for example:<ul><li class="Standard">The LDAP users are under <strong>CN=Users</strong> record.</li><li class="Standard">The LDAP server is starting at machine IP address <strong>127.0.0.1</strong> with a default LDAP port <strong>389.</strong></li></ul></li></ol><p class="Standard">The following figure represents a simple LDAP (Active Directory) configuration example in Teamwork Cloud Admin:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="image2017-4-10_15-32-54.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=171180156 space=TWCloud2024xR1 version=1 -->
## PAGE 00152: LDAP TLS setup

- page_id: `171180156`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180156/LDAP+TLS+setup
- version_number: 1
- version_date: `2023-07-07T08:50:54.916+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Managing LDAP servers
- labels: []

### NORMALIZED CONTENT

You can integrate Teamwork Cloud with TLS-enabled Microsoft Windows Active Directory.

To complete this integration successfully, the following requirements should be passed:

- Windows Server Active Directory should have TLS enabled. This includes a valid Certificate Authority (CA) and a valid certificate for Active Directory (AD) server certificate (for more information on installing and configuring Certificate Services for Windows Server, see Microsoft documentation).
- Any TLS-aware LDAP client should be able to connect to your AD server port 636 with TLS-enabled and should have access to its contents (for more information on setting TLS-enabled connections to AD, refer to the specific LDAP client documentation).

#### WARNING: Warning

Warning

Do not include private keys while exporting.

To export TLS certificates to be used for communication with TLS-Enabled Active Directories (LDAP) in Teamwork Cloud Admin console

- Export the CA and AD server certificates to the DER encoded binary.cer files using the Microsoft Management Console, the Certificates Snap-in.

The subsequent steps for the Teamwork Cloud integration with TLS-enabled Active Directory are the same as for the integration with any other LDAP server. This procedure is described in Teamwork Cloud documentation, section [CONFLUENCE_PAGE title='Enabling secure connection between client and server' space='TWCloud2024xR1'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can integrate Teamwork Cloud with TLS-enabled Microsoft Windows Active Directory.</p><p>To complete this integration successfully, the following requirements should be passed:</p><ul><li>Windows Server Active Directory should have TLS enabled. This includes a valid Certificate Authority (CA) and a valid certificate for Active Directory (AD) server certificate (for more information on installing and configuring Certificate Services for Windows Server, see Microsoft documentation).</li><li>Any TLS-aware LDAP client should be able to connect to your AD server port 636 with TLS-enabled and should have access to its contents (for more information on setting TLS-enabled connections to AD, refer to the specific LDAP client documentation).</li></ul><p><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="99c04d14-7b9c-449c-a71d-3b51500b0f24"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>Do not include private keys while exporting.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To export TLS certificates to be used for communication with TLS-Enabled Active Directories (LDAP) in Teamwork Cloud Admin console</p><hr /><ul><li>Export the CA and AD server certificates to the DER encoded binary.cer files using the Microsoft Management Console, the Certificates Snap-in.</li></ul><p><br /></p><p>The subsequent steps for the Teamwork Cloud integration with TLS-enabled Active Directory are the same as for the integration with any other LDAP server. This procedure is described in Teamwork Cloud documentation, section <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Enabling secure connection between client and server" /></ac:link>.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170491326 space=TWCloud2024xR1 version=3 -->
## PAGE 00153: License management

- page_id: `170491326`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491326/License+management
- version_number: 3
- version_date: `2026-01-27T15:40:29.825+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: []

### NORMALIZED CONTENT

This section explains everything you need to know to activate and/or update the license required to access and use the features of the Teamwork Cloud system. After installing Teamwork Cloud on either a single or cluster server, you need to first install a FlexNet License Server or a DSLS (Dassault Systèmes License Server) before activating the Teamwork Cloud license. Teamwork Cloud uses either the FlexNet License server or a DSLSto protect its licenses and help manage the number of Teamwork Cloud licenses used by concurrent clients.

###### Teamwork Cloud Editions

| Edition | Concurrent Connections | Configuration | Data Replication | High Availability |
| --- | --- | --- | --- | --- |
| Standard | 10 | Single-node server | - | - |
| Business | 25+ | Single-node server | - | - |
| Business Pro | Unlimited | Single-node server can be expanded to Cassandra Cluster | Automatic | - |
| Enterprise | Unlimited | Unlimited | Automatic | + |

Once you have applied the Teamwork Cloud license, you can start working with Teamwork Cloud.

The following topics provide instructions on license management:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section explains everything you need to know to activate and/or update the license required to access and use the features of the Teamwork Cloud system. After installing Teamwork Cloud on either a single or cluster server, you need to first install a FlexNet License Server or a <span style="color:var(--ds-text,#333333);">DSLS (Dassault Systèmes License Server)</span> before activating the Teamwork Cloud license. Teamwork Cloud uses either the FlexNet License server or a <span style="color:var(--ds-text,#333333);">DSLS </span>to protect its licenses and help manage the number of Teamwork Cloud licenses used by concurrent clients.</p><h4>Teamwork Cloud Editions</h4><table class="relative-table" style="width: 39.4051%;"><colgroup class=""><col class="" style="width: 15.6317%;" /><col class="" style="width: 20.7042%;" /><col class="" style="width: 22.3591%;" /><col class="" style="width: 22.3606%;" /><col class="" style="width: 18.9444%;" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;">Edition</th><th style="text-align: center;"><span style="color:var(--ds-text,#000000);">Concurrent Connections</span></th><th style="text-align: center;"><span style="color:var(--ds-text,#000000);">Configuration</span></th><th style="text-align: center;"><span style="color:var(--ds-text,#000000);">Data Replication</span></th><th style="text-align: center;"><span style="color:var(--ds-text,#000000);">High Availability</span></th></tr><tr class=""><th style="text-align: center;">Standard</th><td style="text-align: center;">10</td><td style="text-align: center;"><span style="color:var(--ds-text,#000000);">Single-node server</span></td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr><tr class=""><th style="text-align: center;">Business</th><td style="text-align: center;">25+</td><td style="text-align: center;"><span style="color:var(--ds-text,#000000);">Single-node server</span></td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr><tr class=""><th style="text-align: center;">Business Pro</th><td style="text-align: center;"><span style="color:var(--ds-text,#000000);">Unlimited</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#000000);">Single-node server can be expanded to Cassandra Cluster</span></td><td style="text-align: center;">Automatic</td><td style="text-align: center;">-</td></tr><tr class=""><th style="text-align: center;">Enterprise</th><td style="text-align: center;"><span style="color:var(--ds-text,#000000);">Unlimited</span></td><td style="text-align: center;">Unlimited</td><td style="text-align: center;">Automatic</td><td style="text-align: center;">+</td></tr></tbody></table><p>Once you have applied the Teamwork Cloud license, you can start working with Teamwork Cloud.</p><p><span style="color:var(--ds-text,#333333);">The following topics provide instructions on license management:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491273 space=TWCloud2024xR1 version=2 -->
## PAGE 00154: Load-balancing proxy

- page_id: `170491273`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491273/Load-balancing+proxy
- version_number: 2
- version_date: `2025-10-30T13:39:29.648+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation
- labels: []

### NORMALIZED CONTENT

A load-balancing proxy builds on top of [CONFLUENCE_PAGE title='Layer 4 and Layer 7 proxy setup' space='']. The main difference in this topology is that the load balancer (proxy) is external to the application nodes.

Unlike the use case for the proxy, where the constraint was one where we needed to bind all services to a given port, the load balancer can have 2 distinct topologies.

- As in the former use case, all services will be bound to a single port (443) and balanced among nodes listening to the native ports
- The load balancer will listen to the native ports, and load balance to the various nodes

In the diagram below, we are depicting the second topology, where each front end is bound to the native port and forwarded to the load-balanced backend.

Analogous to the HTTP Proxy depiction in [CONFLUENCE_PAGE title='Layer 4 and Layer 7 proxy setup' space=''], a single front end can be configured to handle all of the HTTPS services on a single port and route to the respective load-balanced backend.

[ATTACHMENT filename='Load Balancer.png'][IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A load-balancing proxy builds on top of <ac:link><ri:page ri:content-title="Layer 4 and Layer 7 proxy setup" /><ac:plain-text-link-body><![CDATA[proxy setup]]></ac:plain-text-link-body></ac:link>. The main difference in this topology is that the load balancer (proxy) is external to the application nodes.</p><p>Unlike the use case for the proxy, where the constraint was one where we needed to bind all services to a given port, the load balancer can have 2 distinct topologies.</p><ul><li>As in the former use case, all services will be bound to a single port (443) and balanced among nodes listening to the native ports</li><li>The load balancer will listen to the native ports, and load balance to the various nodes</li></ul><p>In the diagram below, we are depicting the second topology, where each front end is bound to the native port and forwarded to the load-balanced backend.</p><p>Analogous to the HTTP Proxy depiction in <ac:link><ri:page ri:content-title="Layer 4 and Layer 7 proxy setup" /></ac:link>, a single front end can be configured to handle all of the HTTPS services on a single port and route to the respective load-balanced backend.</p><p><ac:link><ri:attachment ri:filename="Load Balancer.png" /><ac:link-body><ac:image><ri:attachment ri:filename="Load Balancer.png" /></ac:image></ac:link-body></ac:link></p>
````

<!--NOMAGIC_PAGE id=171180800 space=TWCloud2024xR1 version=1 -->
## PAGE 00155: Log file collection

- page_id: `171180800`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180800/Log+file+collection
- version_number: 1
- version_date: `2024-03-29T12:46:06.174+01:00`
- ancestors: Teamwork Cloud and Services > FAQ and Troubleshooting
- labels: []

### NORMALIZED CONTENT

**Scripts**

- [ATTACHMENT filename='TWC-Log-Script-Pkg.zip']

The [ATTACHMENT filename='TWC-Log-Script-Pkg.zip'] contains utilities for gathering and managing log files on your Teamwork Cloud server. These scripts are designed to run from a Linux or Windows Cygwin command line. This package is already included with Admin Tools for 2024x and newer releases.

- **Create log file package** Use the *getlogfiles.sh* script to create a package of all log files associated with Teamwork Cloud operations. This script will create a TAR archive file containing all the latest logs, as well as some system information. The TAR package can be sent along with your support request to help analyze Teamwork Cloud-related issues.
- **Reset log files** Sometimes you may need to create a fresh set of log files. Use the *clearlogfiles.sh* script to reset the log files associated with Teamwork Cloud operations. Please make sure all Teamwork Cloud services are stopped before running the script. This script will then rename all the current log files so that new log files can be generated when the Teamwork Cloud services are restarted. Resetting the log files will ensure that the logs will only contain the latest startup information.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Scripts</strong></p><ul><li><ac:link><ri:attachment ri:filename="TWC-Log-Script-Pkg.zip"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Log file collection" /></ri:attachment></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The <ac:link><ri:attachment ri:filename="TWC-Log-Script-Pkg.zip"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Log file collection" /></ri:attachment><ac:plain-text-link-body><![CDATA[script package]]></ac:plain-text-link-body></ac:link> contains utilities for gathering and managing log files on your Teamwork Cloud server. These scripts are designed to run from a Linux or Windows Cygwin command line. <span style="color: rgb(23,43,77);">This package is already included with Admin Tools for 2024x and newer releases.</span></p><ul><li><p><strong>Create log file package</strong></p><p>Use the <em>getlogfiles.sh</em> script to create a package of all log files associated with Teamwork Cloud operations. This script will create a TAR archive file containing all the latest logs, as well as some system information. The TAR package can be sent along with your support request to help analyze Teamwork Cloud-related issues.</p></li><li><p><strong>Reset log files</strong></p><p>Sometimes you may need to create a fresh set of log files. Use the <em>clearlogfiles.sh</em> script to reset the log files associated with Teamwork Cloud operations. Please make sure all Teamwork Cloud services are stopped before running the script. This script will then rename all the current log files so that new log files can be generated when the Teamwork Cloud services are restarted. Resetting the log files will ensure that the logs will only contain the latest startup information.</p></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180784 space=TWCloud2024xR1 version=3 -->
## PAGE 00156: Managing active simulations

- page_id: `171180784`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180784/Managing+active+simulations
- version_number: 3
- version_date: `2024-06-07T10:02:33.340+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Managing active simulations' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="f2fc34b8-ab60-41e9-b17e-acd000aa5e53"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Managing active simulations" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=171180229 space=TWCloud2024xR1 version=2 -->
## PAGE 00157: Managing announcements

- page_id: `171180229`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180229/Managing+announcements
- version_number: 2
- version_date: `2024-10-15T12:16:11.447+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

You can set up custom announcements in the Settings application and show them when users log into the server or open specified resources. Displayed both in a modeling tool and web applications, these notifications are a convenient way to announce early server upgrades, project deadlines, or any other organization-specific information.

[IMAGE alt='' src='']

###### Announcement displayed in Web Application Platform and a modeling tool.

##### Creating announcement

To create an announcement

1. In the left-side menu of the Settings application, select **Announcements**.
2. Click [IMAGE alt='' src=''] on the bottom right corner of the screen to create a new announcement.
3. Enter the title and description of your announcement.
4. Choose the announcement type.
  - **Display when user logs in/switches apps:** announcements of this type are displayed when a user logs into the server from a modeling tool or web application.
  - **Display on resource access:** these project-specific announcements are shown when a user opens a project. [ATTACHMENT filename='creating_announcement.png']
5. Click Next .
6. In the Target box, select the target of the announcement , i.e., the users and/or groups who need to see the announcement or the resources on which the announcement is to be displayed.
7. In the Schedule box, choose the schedule to display the announcement. If you do not choose a schedule, the announcement remains active until manually deleted.
8. Click Create .

##### Viewing announcement details

You can view the details of an announcement on the **Announcements**page of the Settings application. The following information is available on this page:

- Title: the title of the announcement.
- Description: the description of the announcement.
- Scheduled: the period that the announcement is scheduled to be displayed. If no schedule is set, this column shows Permanent. This means that the announcement remains active until manually deleted.
- Status: the status of the announcement. There are three possible statuses:
  - Scheduled – this means that the announcement is yet to be displayed.
  - Active – the announcement is currently displayed because the current date and time fall into the scheduled period or the announcement is permanent.
  - Expired – this means that the scheduled period has passed and the announcement is no longer active.

To view even more details of an announcement, such as its type and target, click the announcement.

[IMAGE alt='' src='']

###### Viewing announcement details.

##### Editing an announcement

To edit an announcement

1. In the left-side menu of the Settings application, select **Announcements**.
2. Click [IMAGE alt='' src=''] on the right of the relevant announcement.
3. Select **Edit. 
[IMAGE alt='' src='']**
4. Edit the required information in each box and proceed by clicking **Next.**
5. After you have finished editing, click **Save.**

##### Deleting announcement

To delete an announcement

1. In the left-side menu of the Settings application, select **Announcements**.
2. Click [IMAGE alt='' src=''] on the right of the relevant announcement.
3. Select **Delete.**
4. Click **Delete**in the dialog to confirm.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">You can set up custom announcements in the Settings application and show them when users log into the server or open specified resources. Displayed both in a modeling tool and web applications, these notifications are a convenient way to announce early server upgrades, project deadlines, or any other organization-specific information.</span></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"> <ac:image><ri:attachment ri:filename="announcements.png" /></ac:image><br /></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">Announcement displayed in Web Application Platform and a modeling tool.</span></h6><h3>Creating announcement</h3><p>To create an announcement</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the left-side menu of the Settings application, select <strong>Announcements</strong>.</span></li><li><span style="color: rgb(62,63,64);">Click </span> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"> <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="create_index.png" /></ac:image> </span> <span style="color: rgb(62,63,64);"> on the bottom right corner of the screen to create a new announcement.</span></li><li><span style="color: rgb(62,63,64);">Enter the title and description of your announcement.</span></li><li><span style="color: rgb(62,63,64);">Choose the announcement type.</span><ul><li><span style="color: rgb(62,63,64);"> <strong>Display when user logs in/switches apps:</strong> announcements of this type are displayed when a user logs into the server from a modeling tool or web application.</span></li><li><span style="letter-spacing: 0.0px;"> <strong>Display on resource access:</strong> these project-specific announcements are shown when a user opens a </span>project.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="creating_announcement.png" /></ac:image><br /><br /></li></ul></li><li>Click <strong>Next</strong>.</li><li>In the <strong>Target </strong><ac:inline-comment-marker ac:ref="43067d20-6b1c-48d2-85dd-c8c4dd348750">box,</ac:inline-comment-marker> select the <ac:inline-comment-marker ac:ref="606911cc-5b7b-42f4-9092-8df917c8bc7d">target of the announcement</ac:inline-comment-marker>, i.e., the users and/or groups who need to see the announcement or the resources on which the announcement is to be displayed.</li><li>In the <strong>Schedule </strong><ac:inline-comment-marker ac:ref="f37413fa-b7f3-49cc-b93c-32da0c743476">box,</ac:inline-comment-marker> choose the schedule to display the announcement. If you do not choose a schedule, the announcement remains active until manually deleted.</li><li>Click <strong>Create</strong>.</li></ol><h3>Viewing announcement details</h3><p>You can view the details of an announcement on the <strong>Announcements </strong>page of the Settings application. The following information is available on this page:</p><ul style="text-align: left;"><li><strong>Title: </strong>the<strong> </strong>title of the announcement.</li><li><strong>Description:</strong> the description of the announcement.</li><li><strong>Scheduled:</strong> the period that the announcement is scheduled to be displayed. If no schedule is set, this column shows <em>Permanent. </em>This means that the announcement remains active until manually deleted.</li><li><strong>Status:</strong> the status of the announcement. There are three possible statuses:<ul><li><em>Scheduled –</em> this means that the announcement is yet to be displayed.</li><li><em>Active –</em> the announcement is currently displayed because the current date and time fall into the scheduled period or the announcement is permanent.</li><li><em>Expired –</em> this means that the scheduled period has <ac:inline-comment-marker ac:ref="8ccb92f8-711a-499d-afec-6319f6e53e63">passed <span style="color: rgb(62,63,64);">and the announcement is no longer active.</span></ac:inline-comment-marker></li></ul></li></ul><p>To view even more details of an announcement, such as its type and target, click the announcement.</p><p style="text-align: center;"><ac:image ac:align="center" ac:width="900"><ri:attachment ri:filename="announcement_details.png" /></ac:image></p><h6 style="text-align: center;">Viewing announcement details.</h6><h3>Editing an announcement</h3><p>To edit an announcement</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the left-side menu of the Settings application, select <strong>Announcements</strong>.</span></li><li><span style="color: rgb(62,63,64);">Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"> </span><span style="color: rgb(62,63,64);">on the right of the relevant announcement.</span></li><li><span style="color: rgb(62,63,64);">Select <strong>Edit.<br /><ac:image><ri:attachment ri:filename="editing_announcement.png" /></ac:image><br /><br /></strong></span></li><li><span style="color: rgb(62,63,64);">Edit the required information in each <ac:inline-comment-marker ac:ref="6f680489-cd2e-4bf7-bf62-4c57910243b7">box</ac:inline-comment-marker> and proceed by clicking <strong>Next.</strong></span></li><li><span style="color: rgb(62,63,64);">After you have finished editing, click <strong>Save.</strong> </span></li></ol><h3><span style="color: rgb(62,63,64);">Deleting announcement</span></h3><p><span style="color: rgb(62,63,64);">To delete an announcement</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the left-side menu of the Settings application, select <strong>Announcements</strong>.</span></li><li><span style="color: rgb(62,63,64);">Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"> </span><span style="color: rgb(62,63,64);">on the right of the relevant announcement.</span></li><li><span style="color: rgb(62,63,64);">Select <strong>Delete.</strong></span></li><li><span style="color: rgb(62,63,64);">Click <strong>Delete </strong>in the dialog to confirm.</span></li></ol>
````

<!--NOMAGIC_PAGE id=171180263 space=TWCloud2024xR1 version=2 -->
## PAGE 00158: Managing category assignments

- page_id: `171180263`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180263/Managing+category+assignments
- version_number: 2
- version_date: `2025-10-30T14:48:14.679+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application > Working with categories
- labels: []

### NORMALIZED CONTENT

**On this page**

4

##### Assigning users to categories

In the Resources application, you can assign users to a specific category by giving them a certain role. As a result, the permissions of that role are applied to the user in the scope of the category.

To assign users to a category

1. In the Resources application, find the category that you want to assign users to.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Change assignments .
3. In the category assignments screen, use the search box to find and select the user you want to assign. The selected user is added and displayed in the **Assigned users/groups** list.
4. Click the **Add new role** box and select the role you want to add. The assigned role is displayed on the bottom of the user card. Changing roles of assigned usersIf you want to change the roles of the user who is already assigned to the category, select the **Find user/group** tab and use the search box to find the user whose roles you want to change. 
 
[IMAGE alt='' src='']
5. If needed, repeat steps 2 and 3 to assign more users to the category.
6. Click [ATTACHMENT filename='save_users.png'] in the top right corner of the resource assignments screen to save the assigned users. [ATTACHMENT filename='category_assignments_screen.png']

The added users are assigned to the category and given the selected roles in the category scope.

##### Removing users from categories

You can use the Resources application to remove the users assigned to a specific category.

To remove users from a category

1. In the Resources application, find the category that you want to remove users from.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Change assignments .
3. In the category assignments screen, select the Find user/group tab and use the search box to find the user you want to remove.
4. In the bottom right corner of the user card, click [ATTACHMENT filename='delete_user.png'] to remove the user.
5. Click [ATTACHMENT filename='save_users.png'] in the top right corner of the category assignments screen to save the changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4ed75cd6-3e80-49c6-93f0-f29b39b6e6af"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3 style="color:var(--ds-text,#172b4d);">Assigning users to categories</h3><p>In the Resources application, you can assign users to a specific category by giving them a certain role. As a result, the permissions of that role are applied to the user in the scope of the category.</p><p><br /></p><p>To assign users to a category</p><hr style="" /><ol><li>In the Resources application, find the category that you want to assign users to.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image><span style="letter-spacing: 0.0px;"> next to the category and select </span><strong style="letter-spacing: 0.0px;">Change assignments</strong><span style="letter-spacing: 0.0px;">.</span></li><li><p class="auto-cursor-target">In the category assignments screen, use the search box to find and select the user you want to assign. The selected user is added and displayed in the <strong>Assigned users/groups</strong> list.</p></li><li><p class="auto-cursor-target">Click the <strong>Add new role</strong> box and select the role you want to add. The assigned role is displayed on the bottom of the user card.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9976359d-a19c-494c-9fdf-6a3adef6c9b5"><ac:parameter ac:name="title">Changing roles of assigned users</ac:parameter><ac:rich-text-body><p>If you want to change the roles of the user who is already assigned to the category, select the <strong>Find user/group</strong> tab and use the search box to find the user whose roles you want to change.<br /><br /><ac:image ac:align="center" ac:height="111"><ri:attachment ri:filename="finding_users_assigned_to_category.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></li><li>If needed, repeat steps 2 and 3 to assign more users to the category.</li><li>Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_users.png" /></ac:image> in the top right corner of the resource assignments screen to save the assigned users.<br /><br /><ac:image><ri:attachment ri:filename="category_assignments_screen.png" /></ac:image></li></ol><p><br />The added users are assigned to the category and given the selected roles in the category scope.</p><p><br /></p><h3 style="color:var(--ds-text,#172b4d);">Removing users from categories</h3><p>You can use the Resources application to remove the users assigned to a specific category.</p><p><br /></p><p>To remove users from a category</p><hr style="" /><ol><li>In the Resources application, find the category that you want to remove users from.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image><span style="letter-spacing: 0.0px;"> next to the category and select </span><strong style="letter-spacing: 0.0px;">Change assignments</strong><span style="letter-spacing: 0.0px;">.</span></li><li>In the category assignments screen, select the <strong>Find user/group</strong> tab and use the search box to find the user you want to remove.</li><li>In the bottom right corner of the user card, click <ac:image><ri:attachment ri:filename="delete_user.png" /></ac:image> to remove the user.</li><li>Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_users.png" /></ac:image> in the top right corner of the category assignments screen to save the changes.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180104 space=TWCloud2024xR1 version=1 -->
## PAGE 00159: Managing data markings in Teamwork Cloud Admin

- page_id: `171180104`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180104/Managing+data+markings+in+Teamwork+Cloud+Admin
- version_number: 1
- version_date: `2023-09-22T10:53:36.027+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

Data markings allow you to classify resources, categories, users, and user groups with custom-defined access levels. You can define hierarchical, non-hierarchical (flat) classifiers, or a combination of both. This also means you can assign multiple data markings to a resource, category, user, or group.

The video below explains how the Data markings feature works:

##### Enabling data markings

To use data markings, you must enable them in the Settings app, where you can also create, reorder, edit, and remove data markings.

If data markings are not enabled on the server, only [CONFLUENCE_PAGE title='Role-Based Access Control concept' space='TWCloud2024xR1']data access restrictions are applied. Once enabled, data markings act as the initial guard in determining whether a request to see/open a resource should be allowed to undergo the further usual RBAC access rules checks.

To enable data markings

1. In the Settings application, go to the Data markings page.
2. Choose the Enable data markings option.

Once you enable data markings, you see the data markings configuration page:

[IMAGE alt='' src='']

###### Data markings configuration page.

##### Creating data markings

Once you enable data markings in the Data markings configuration page, no data markings are shown. You have to create them first. Before creating any data markings, you first have to create a data marking group.

To create a data marking group

1. In the Settings application, go to the Data markings configuration page.
2. Click [ATTACHMENT filename='create.png'] at the bottom right corner.
3. In the dialog that opens, enter the name of the data marking group.
4. Choose the data marking group type.
  - Hierarchical: T his type of data marking group works hierarchically; i.e., the top-most data marking in the group reflects the most restrictive access level, while the bottom one is the least restrictive access level. The parent data marking allows access to data marked with child markings but not vice-versa. 
[IMAGE alt='' src='']
  - Flat: These are non-hierarchical data markings. For example, in a data markings group *Suppliers (Supplier A, Supplier B),* a user may be marked with data marking *SupplierA* or data marking *SupplierB.*Data marking *SupplierA* does not grant broader access rights than data marking *SupplierB*and vice versa. This also means that both data marking *SupplierA* and data marking *SupplierB* can be assigned to the same user. In other words, entries in a flat data marking group act like tags. 
[IMAGE alt='' src='']
5. Click Create .

To create a single data marking

1. In the Settings application, go to the Data markings configuration page.
2. Click [ATTACHMENT filename='create.png'] at the bottom right corner.
3. Choose [ATTACHMENT filename='create_single_data_marking.png'] to create a single data marking.
4. In the dialog that opens, choose the Data marking group for the new data marking.
5. Enter the name for the data marking in the Data marking field.
6. Enter the abbreviated portion marking in the Portion marking field.
7. Optionally, choose the color of the portion marking by clicking the palette icon.
8. Click Create .

##### Reordering hierarchical data markings

As the name implies, hierarchical data markings work hierarchically, so their order in the table is important. Thus, the data marking at the very top of the table will have the broadest access rights and will include all of the levels below it. To change the restriction level of data markings, reorder them in the table.

To reorder data markings

1. In the Data markings page select the hierarchical data marking group to reorder.
2. Click the menu on the left side of the table: [ATTACHMENT filename='reordering_hierarchical_markings.png']
3. Once the moving pointer appears, drag the data marking up or down to the preferred position.

##### Editing data markings

To edit data markings

1. In the Data markings page select a data marking group.
2. In the data markings table select [ATTACHMENT filename='menu.png'] .
3. Choose Edit .
4. Make your changes in the dialog and select Save.

##### Deleting data markings

All data markings inside the deleted group will also be deleted. All users and resources will lose the data markings from this group as well.

To delete data markings

1. In the Data markings page select a data marking group.
2. In the data markings table select [ATTACHMENT filename='menu.png'] .
3. Choose Delete.
4. Confirm by selecting Delete.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Data markings allow you to classify resources, categories, users, and user groups with custom-defined access levels. You can <span style="color: rgb(62,63,64);">define hierarchical, non-hierarchical (flat) classifiers, or a combination of both. This also means you can assign multiple data markings to a<span> </span> </span> <span style="color: rgb(62,63,64);">resource, category, user, or group.</span></p><p><span style="color: rgb(62,63,64);">The video below explains how the Data markings feature works:</span></p><p><span style="color: rgb(62,63,64);"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="8f023306-536f-4403-834a-5020929cd1b3"><ac:parameter ac:name="url"><ri:url ri:value="http://youtube.com/watch?v=QClyIJVs94g" /></ac:parameter></ac:structured-macro></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b6c4b80-439f-4bad-82d3-2afc0c41b268"><ac:rich-text-body>In order to use data markings, you need sufficient <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[permissions]]></ac:plain-text-link-body></ac:link>, either the Mark Data permission assigned to the Data Markings Manager role or the Configure Data Markings permission assigned to the Security Manager role.</ac:rich-text-body></ac:structured-macro><h3>Enabling data markings</h3><p>To use data markings, you must enable them in the Settings app, where you can also create, reorder, edit, and remove data markings.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cd3ac131-5977-4286-a825-7ae0c0cde1f9"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If data markings are not enabled on the server, only <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Role-Based Access Control concept" /><ac:plain-text-link-body><![CDATA[ RBAC ]]></ac:plain-text-link-body></ac:link>data access restrictions are applied. Once enabled, data markings act as the initial guard in determining whether a request to see/open a resource should be allowed to undergo the further usual RBAC access rules checks.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To enable data markings</p><hr /><ol><li>In the <strong>Settings </strong>application, go to the <strong>Data markings</strong> page. </li><li>Choose the <strong>Enable data markings</strong> option.</li></ol><p>Once you enable data markings, you see the data markings configuration page:</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="empty_data_markings_page.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Data markings configuration page.</h6><h3>Creating data markings</h3><p>Once you enable data markings in the Data markings configuration page, no data markings are shown. You have to create them first. Before creating any data markings, you first have to create a data marking group.</p><p style="text-align: left;">To create a data marking group</p><hr /><ol><li>In the <strong>Settings </strong>application, go to the <strong>Data markings </strong>configuration page.</li><li>Click <ac:image ac:thumbnail="true" ac:width="20"><ri:attachment ri:filename="create.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image> at the bottom right corner.</li><li>In the dialog that opens, enter the name of the data marking group.</li><li>Choose the data marking group type.<ul><li><strong>Hierarchical: </strong>T<span style="color: rgb(62,63,64);">his type of data marking group works hierarchically; i.e., the top-most data marking in the group reflects the most restrictive access level, while the bottom one is the least restrictive access level. The parent data marking allows access to data marked with child markings but not vice-versa.<br /><ac:image><ri:attachment ri:filename="hierarchical_data_markings_group.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image><br /></span></li><li><strong> <span style="color: rgb(62,63,64);">Flat: </span></strong><span style="color: rgb(62,63,64);">These are <span style="color: rgb(23,43,77);">non-hierarchical data markings. For example, in a data markings group <em>Suppliers (Supplier A, Supplier B),</em> a user may be marked with data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>A</em> or data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>B. </em>Data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>A</em> does not grant broader access rights than data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>B </em>and vice versa. This also means that both data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>A</em> and data marking <em>Supplier<span style="color: rgb(32,33,34);"> </span>B</em> can be assigned to the same user. In other words, entries in a flat data marking group act like tags.<br /><ac:image><ri:attachment ri:filename="flat_data_markings_group.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image><br /></span></span></li></ul></li><li>Click <strong>Create</strong><span>.</span></li></ol><p style="text-align: left;">To create a single data marking</p><hr /><ol><li>In the <strong>Settings </strong>application, go to the <strong>Data markings </strong>configuration page.</li><li>Click <ac:image ac:thumbnail="true" ac:width="20"><ri:attachment ri:filename="create.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image> at the bottom right corner.</li><li>Choose<ac:image ac:thumbnail="true" ac:width="23"><ri:attachment ri:filename="create_single_data_marking.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image> to create a single data marking.</li><li>In the dialog that opens, choose the <strong>Data marking group </strong>for the new data marking.</li><li>Enter the name for the data marking in the<strong> Data marking</strong> field.</li><li>Enter the abbreviated portion marking in the <strong>Portion marking</strong> field.</li><li>Optionally, choose the color of the portion marking by clicking the palette icon.</li><li>Click <strong>Create</strong>.</li></ol><h3 style="text-align: left;">Reordering hierarchical data markings</h3><p>As the name implies, hierarchical data markings work hierarchically, so their order in the table is important. Thus, the data marking at the very top of the table will have the broadest access rights and will include all of the levels below it. To change the restriction level of data markings, reorder them in the table.</p><p style="text-align: left;">To reorder data markings</p><hr /><ol><li>In the <strong>Data markings </strong>page select the hierarchical data marking group to reorder.</li><li>Click the menu on the left side of the table:<br /><ac:image><ri:attachment ri:filename="reordering_hierarchical_markings.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image></li><li>Once the moving pointer appears, drag the data marking up or down to the preferred position.</li></ol><h3 style="text-align: left;">Editing data markings</h3><p style="text-align: left;">To edit data markings</p><hr /><ol><li>In the <strong>Data markings </strong>page select a data marking group.</li><li>In the data markings table select <ac:image><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image>.</li><li>Choose <strong>Edit</strong> <strong>.</strong></li><li>Make your changes in the dialog and select<strong> Save.</strong></li></ol><h3>Deleting data markings</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="53098caa-56a3-4ee8-8481-51466768125a"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">All data markings inside the deleted group will also be deleted. All users and resources will lose the data markings from this group as well.</span></p></ac:rich-text-body></ac:structured-macro><p>To delete data markings</p><hr /><ol><li>In the <strong>Data markings </strong>page select a data marking group.</li><li>In the data markings table select <ac:image><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ri:attachment></ac:image>.</li><li>Choose <strong>Delete.</strong></li><li>Confirm by selecting<strong> Delete.</strong></li></ol>
````

<!--NOMAGIC_PAGE id=171180118 space=TWCloud2024xR1 version=2 -->
## PAGE 00160: Managing LDAP servers

- page_id: `171180118`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180118/Managing+LDAP+servers
- version_number: 2
- version_date: `2025-10-30T14:37:34.496+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

LDAP stands for Lightweight Directory Access Protocol. It is an open standard protocol used over an IP network to locate and access directory servers. Teamwork Cloud Admin makes use of LDAP to access data, in this case, users on LDAP servers. Therefore, with Teamwork Cloud Admin, you can easily import users from other external databases or LDAP servers. Once you import users, you can assign them some roles or resources and even convert them into internal users. Teamwork Cloud Admin uses LDAP to import users only. The users' data are still stored on the LDAP servers. You cannot edit information or profiles of the users imported from LDAP servers.

The **LDAP management** page allows you to add LDAP servers before you can import users from them. It also shows information about LDAP servers that are external but configured for Teamwork Cloud. Teamwork Cloud Admin's user authentication during login also searches for the user in those directories. The authentication process starts from the first LDAP server on the directory list. You can, however, select which server gets authenticated first by changing the order using the up and down arrow buttons.

[IMAGE alt='' src='']

###### The LDAP management page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>LDAP stands for Lightweight Directory Access Protocol. It is an open standard protocol used over an IP network to locate and access directory servers. Teamwork Cloud Admin makes use of LDAP to access data, in this case, users on LDAP servers. Therefore, with Teamwork Cloud Admin, you can easily import users from other external databases or LDAP servers. Once you import users, you can assign them some roles or resources and even convert them into internal users. Teamwork Cloud Admin uses LDAP to import users only. The users' data are still stored on the LDAP servers. You cannot edit information or profiles of the users imported from LDAP servers.</p><p>The <strong>LDAP management</strong> page allows you to add LDAP servers before you can import users from them. It also shows information about LDAP servers that are external but configured for Teamwork Cloud. Teamwork Cloud Admin's user authentication during login also searches for the user in those directories. The authentication process starts from the first LDAP server on the directory list. You can, however, select which server gets authenticated first by changing the order using the up and down arrow buttons.</p><p><ac:image ac:align="center" ac:border="true"><ri:attachment ri:filename="LDAP_page.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">The LDAP management page.</h6>
````

<!--NOMAGIC_PAGE id=171180767 space=TWCloud2024xR1 version=2 -->
## PAGE 00161: Managing long-running tasks

- page_id: `171180767`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180767/Managing+long-running+tasks
- version_number: 2
- version_date: `2024-05-09T13:41:32.826+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Other features
- labels: []

### NORMALIZED CONTENT

Cameo Collaborator for Teamwork Cloud has a task manager that you can use to monitor and manage long-running tasks, such as exporting documents to PDF or HTML.

To open Task Manager

1. Open the Resources web application or a Cameo Collaborator document.
2. In the top right corner of the screen, click [ATTACHMENT filename='menu.png'] and select Task manager .
3. In the **Collaborator** tab of the **Task manager** dialog, do one or several of the following actions: Simulation tasksIf you work with the [CONFLUENCE_PAGE title='Server-side simulation' space='CST2024xR1'] in Teamwork Cloud, select the Simulation tab in the task manager to manage active simulations.
  - View the status of the active long-running tasks.
  - Click [ATTACHMENT filename='download.png'] next to a completed task to download the [CONFLUENCE_PAGE title='Exporting documents to PDF and HTML' space='TWCloud2024xR1'] .
  - Click [ATTACHMENT filename='delete.png'] next to a task to remove it from the task manager.

[IMAGE alt='' src='']

###### The **Task manager** dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Cameo Collaborator for Teamwork Cloud has a task manager that you can use to monitor and manage long-running tasks, such as exporting documents to PDF or HTML.</span></p><p><br /></p><p><span style="color: rgb(62,63,64);">To open Task Manager</span></p><hr /><ol><li>Open the Resources web application or a Cameo Collaborator document.</li><li>In the top right corner of the screen, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing long-running tasks" /></ri:attachment></ac:image> and select <strong>Task manager</strong>.</li><li><p class="auto-cursor-target">In the <strong>Collaborator</strong> tab of the <strong>Task manager</strong> dialog, do one or several of the following actions:</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="bf61f988-08c5-44be-9e66-fe7748691780"><ac:parameter ac:name="title">Simulation tasks</ac:parameter><ac:rich-text-body><p>If you work with the <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Server-side simulation" /><ac:plain-text-link-body><![CDATA[server-side simulation]]></ac:plain-text-link-body></ac:link> in Teamwork Cloud, select the Simulation tab in the task manager to manage active simulations.</p></ac:rich-text-body></ac:structured-macro><ul><li>View the status of the active long-running tasks.</li><li>Click <ac:image><ri:attachment ri:filename="download.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing long-running tasks" /></ri:attachment></ac:image> next to a completed task to download the <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Exporting documents to PDF and HTML" /><ac:plain-text-link-body><![CDATA[exported Cameo Collaborator document]]></ac:plain-text-link-body></ac:link>.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="delete.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing long-running tasks" /></ri:attachment></ac:image> next to a task to remove it from the task manager.</li></ul></li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="task_manager_dialog.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing long-running tasks" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The <strong>Task manager</strong> dialog.</h6><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=178160013 space=TWCloud2024xR1 version=1 -->
## PAGE 00162: Managing OAuth client keys

- page_id: `178160013`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/178160013/Managing+OAuth+client+keys
- version_number: 1
- version_date: `2024-07-01T14:32:33.520+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

**On this page**

4

OAuth is an open-standard authorization protocol. It allows you to authorize API access to Teamwork Cloud Admin and other modeling tools. Once access has been granted, the authorized application can utilize the API on behalf of the user. Only users with *Configure Server permission* can create and manage client keys. After creating the key, you must approve it, which can be done in the **Client keys** (Consumer keys for OAuth 1.0a) data table. When the client key is approved, its status will change to *Approved*. This feature enables you to easily change the status of client keys, allowing you to control users' sign-in requests.

The client key is unique, but the assigned client name and client secret can be changed. If changes occurred, the Administrator should provide a new client name and secret to the user.

The supported client types are OAuth 1.0a, OAuth 2.0*****, and OpenID Connect

*****OAuth 2.0, which stands for “Open Authorization”, is a standard designed to allow a website or application to access resources hosted by other web apps on behalf of a user. OAuth 2.0 provides consented access and restricts actions of what the client app can perform on resources on behalf of the user, without ever sharing the user's credentials.

##### registerCreating the OAuth client keys

To create a **OAuth 1.0a**client

1. In the Settings application, go to the OAuth clients page.
2. Select a client type tab - OAuth 1.0a. You can also choose the Client type in the client creation dialog.
3. In the right-bottom corner, click the Create client [IMAGE alt='' src='']button.
4. In the open dialog, enter the Consumer name and Consumer secret .
5. Re-type the consumer secret.
6. Click Save .

To create a **OAuth 2.0** or **OpenID** Connectclient

1. In the Settings application, go to the OAuth clients page.
2. Select a client type tab - OAuth 2.0 or OpenID Connect. You can also choose the Client type in the client creation dialog.
3. In the right-bottom corner, click the Create client [IMAGE alt='' src='']button.
4. In the open dialog, enter the Client name and Client secret .
5. Re-type the client secret.
6. Enter Redirect URIs . Multiple enties are available by pressing enter after each URI.
7. Choose the needed Grant types and Response types .
8. Click Save .

When you click the **Save**bytton, a client key (consumer key for OAuth 1.0a) is immediately generated and added to the **Client keys** data table. Now, to activate the new client key, you have to.

###### Supported Grant and Response types

| Client type | Grant types | Response types |
| --- | --- | --- |
| OAuth 2.0 | authorization_codepasswordrefresh_tokenurb:ietf:params:oauth:grant-type:device_code | codetoken |
| OpenID Connect | authorization_codepasswordrefresh_tokenurb:ietf:params:oauth:grant-type:device_code | codecode id_tokencode id_token tokencode tokenid_tokenid_token token |

##### Actions with created client keys

editTo edit the client name, secret, or redirect URIs

1. In the client key table, indicate the client key row you want to change.
2. At the end of a needed row, click [ATTACHMENT filename='menu.png'] and select Edit . The confirmation dialog opens.
3. In this dialog, change the client name, client secret, or redirect URIs (for OAuth 2.0 and OpenID Connect) . Note that the client key is unique and cannot be changed.
4. Click Save to save changes.

approveTo approve or disapprove the client key

1. In the client key table, indicate the client key row you want to approve (or disapprove).
2. At the end of a needed row, click [ATTACHMENT filename='menu.png'] and select Approve (or Disapprove ). The confirmation dialog opens.
3. In this dialog, confirm that this client key will be approved (or disapproved).

removeTo remove a client key

1. In the client key table, indicate the client key row you want to change
2. At the end of a needed row, click [ATTACHMENT filename='menu.png'] and select Remove . The confirmation dialog opens.
3. Click Remove to permanently remove client key.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong><ac:inline-comment-marker ac:ref="ea02d75d-5925-406b-a5d7-e6f77b6b10bd">On this page</ac:inline-comment-marker></strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bba1e23d-2d22-4df8-af98-eff898ad8592"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>OAuth is an open-standard authorization protocol. It allows you to authorize API access to Teamwork Cloud Admin and other modeling tools. Once access has been granted, the authorized application can utilize the API on behalf of the user. Only users with <em>Configure Server permission</em> can create and manage client keys. After creating the key, you must approve it, which can be done in the <strong>Client keys</strong> (Consumer keys for OAuth 1.0a) data table. When the client key is approved, its status will change to <em>Approved</em>. This feature enables you to easily change the status of client keys, allowing you to control users' sign-in requests. </p><p>The client key is unique, but the assigned client name and client secret can be changed. If changes occurred, the Administrator should provide a new client name and secret to the user. </p><p>The supported client types are OAuth 1.0a, OAuth 2.0<strong>*</strong>, and OpenID Connect</p><p style="margin-left: 40.0px;"><span style="color: rgb(23,43,77);"><strong>*</strong>OAuth 2.0, which stands for “Open Authorization”, is a standard designed to allow a website or application to access resources hosted by other web apps on behalf of a user. OAuth 2.0 provides consented access and restricts actions of what the client app can perform on resources on behalf of the user, without ever sharing the user's credentials.</span></p><p><br /></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fab18da9-06b6-4c30-a5e9-718e3b36b183"><ac:parameter ac:name="">register</ac:parameter></ac:structured-macro>Creating the OAuth client keys</h3><p>To create a <span><strong>OAuth 1.0a</strong> </span>client</p><hr /><ol><li>In the <strong>Settings </strong>application, go to the <strong>OAuth clients</strong> page. </li><li><span style="letter-spacing: 0.0px;">Select a client type tab - OAuth 1.0a.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ab5b8129-1fdd-4a09-b6e8-2a242ed2740c"><ac:rich-text-body><p>You can also choose the Client type in the client creation dialog.</p></ac:rich-text-body></ac:structured-macro><span style="letter-spacing: 0.0px;"><br /></span></li><li><span style="letter-spacing: 0.0px;">In the right-bottom corner, click the Create client <ac:image ac:thumbnail="true" ac:width="36"><ri:attachment ri:filename="create_client_button.png" /></ac:image>button.</span></li><li><span style="letter-spacing: 0.0px;">In the open dialog, </span>enter the <strong style="letter-spacing: 0.0px;">Consumer name</strong><span style="letter-spacing: 0.0px;"> and </span><strong style="letter-spacing: 0.0px;">Consumer secret</strong><span style="letter-spacing: 0.0px;">.</span></li><li>Re-type the consumer secret.</li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p>To create a <span><strong>OAuth 2.0</strong> or <strong>OpenID</strong> Connect </span>client</p><hr /><ol><li>In the <strong>Settings </strong>application, go to the <strong>OAuth clients</strong> page. </li><li><span>Select a client type tab - OAuth 2.0 or OpenID Connect.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8857cccd-5774-4bb2-b065-c9097d2fb2a9"><ac:rich-text-body><p>You can also choose the Client type in the client creation dialog.</p></ac:rich-text-body></ac:structured-macro><span><br /></span></li><li><span>In the right-bottom corner, click the Create client <ac:image ac:thumbnail="true" ac:width="36"><ri:attachment ri:filename="create_client_button.png" /></ac:image>button.</span></li><li><span>In the open dialog, </span>enter the <strong>Client name</strong><span> and </span><strong>Client secret</strong><span>.</span></li><li>Re-type the client secret.</li><li>Enter <strong>Redirect URIs</strong>. Multiple enties are available by pressing enter after each URI.</li><li>Choose the needed <strong>Grant types</strong> and <strong>Response types</strong>.</li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p>When you click the <strong>Save </strong>bytton, a client key (consumer key for OAuth 1.0a) is immediately generated and added to the <strong>Client keys</strong> data table. Now, to <span style="letter-spacing: 0.0px;">activate the new client key, you have to </span><ac:link ac:anchor="approve"><ac:plain-text-link-body><![CDATA[approve it]]></ac:plain-text-link-body></ac:link><span style="letter-spacing: 0.0px;">. </span></p><p><br /></p><h4 style="margin-left: 40.0px;"><span style="letter-spacing: 0.0px;">Supported Grant and Response types</span></h4><table class="relative-table wrapped" style="width: 38.5469%;"><colgroup><col style="width: 18.8749%;" /><col style="width: 48.9921%;" /><col style="width: 32.133%;" /></colgroup><tbody><tr><th scope="col">Client type</th><th scope="col">Grant types</th><th scope="col">Response types</th></tr><tr><td>OAuth 2.0</td><td><p>authorization_code</p><p>password</p><p>refresh_token</p><p>urb:ietf:params:oauth:grant-type:device_code</p></td><td><p>code</p><p>token</p></td></tr><tr><td>OpenID Connect</td><td><p>authorization_code</p><p>password</p><p>refresh_token</p><p>urb:ietf:params:oauth:grant-type:device_code</p></td><td><p>code</p><p>code id_token</p><p>code id_token token</p><p>code token</p><p>id_token</p><p>id_token token</p></td></tr></tbody></table><h3>Actions with created client keys</h3><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="00f33d2b-36b3-4df7-a8bb-5f540c75e1ae"><ac:parameter ac:name="">edit</ac:parameter></ac:structured-macro>To edit the client name, secret, or redirect URIs</p><hr /><ol><li>In the client key table, indicate the client key row you want to change.</li><li>At the end of a needed row, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> and select <strong>Edit</strong>. The confirmation dialog opens.</li><li>In this dialog, change the client name, client secret, or redirect URIs (for OAuth 2.0 and OpenID Connect) . Note that the client key is unique and cannot be changed. </li><li>Click <strong>Save</strong> to save changes. </li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="3501dad8-f07d-4929-bead-dcbcfc3ea87b"><ac:parameter ac:name="">approve</ac:parameter></ac:structured-macro>To approve or disapprove the client key</p><hr /><ol><li>In the client key table, indicate the client key row you want to approve (or disapprove). </li><li>At the end of a needed row, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> and select <strong>Approve</strong> (or <strong>Disapprove</strong>). The confirmation dialog opens.</li><li>In this dialog, confirm that this client key will be approved (or disapproved). </li></ol><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6581532e-2e80-4b0e-9012-ae8eeb9279b8"><ac:parameter ac:name="">remove</ac:parameter></ac:structured-macro>To remove a client key</p><hr /><ol><li>In the client key table, indicate the client key row you want to change</li><li>At the end of a needed row, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> and select <strong>Remove</strong>. The confirmation dialog opens.</li><li>Click <strong>Remove</strong> to permanently remove client key. </li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180087 space=TWCloud2024xR1 version=2 -->
## PAGE 00163: Managing password complexity and lifecycle

- page_id: `171180087`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180087/Managing+password+complexity+and+lifecycle
- version_number: 2
- version_date: `2026-02-23T14:27:27.064+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Managing server settings
- labels: []

### NORMALIZED CONTENT

**On this page**

4

In this section of the **Server settings** page, you can specify the password complexity and lifecycle requirements for internal users.

Every time the password complexity rules are changed, all internal users must change their password, even if the current password complies with the requirements.

##### Setting password complexity requirements

To set the requirements of password complexity

1. In the Server settings page, select the Complexity tab in the **Password complexity & lifecycle requirements** section. 
 
[IMAGE alt='' src='']
2. Enable the password complexity requirements that passwords must meet.
  - Select if the password must contain the following:
    - Lowercase letters and/or
    - Uppercase letters and/or
    - Special characters and/or
    - Numbers;
  - Select if the password must be of any minimum length.
3. If you selected the **Minimum length**requirement, enter the minimum length in the **Password minimum length** field.
4. Click **SAVE**.

##### Setting password lifecycle requirements

To set the requirements of password lifecycle

1. In the Server settings page, select the Lifecycle tab in the **Password complexity & lifecycle requirements** section. 
 
[IMAGE alt='' src='']
2. Enable the password lifecycle requirements that passwords must meet.
  - Password history: you can forbid users from selecting previously used passwords. If you enable this option, enter a number in the Number of passwords field. This number defines how many previous passwords cannot be used as the current password, i.e. if the number is 5, then the user cannot use the last 5 passwords they used before.
  - User lockout: you can choose to disable a user upon reaching a defined number of subsequent unsuccessful login attempts. If you enable this option, enter the number of allowed unsuccessful login attempts in the Number of tries field.
  - Password age: you can force users to change the password after a defined number of days. If you enable this option, specify the value in the Number of days field. This determines how many days must pass before users are prompted to change their password.
3. Click **SAVE**.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="29f6bd9c-9214-44ef-afa4-9e9328568199"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>In this section of the <strong>Server settings</strong> page, you can s<span>pecify the password complexity and lifecycle requirements for internal users.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="23a8ac84-5e51-4ab1-a1fa-23bd3a709c6d"><ac:rich-text-body>Every time the password complexity rules are changed, all internal users must change their password, even if the current password complies with the requirements.</ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Setting password complexity requirements</h3><p>To set the requirements of password complexity</p><hr /><ol><li>In the <strong>Server settings</strong> page, select the <strong>Complexity </strong>tab in the <span><strong>Password complexity &amp; lifecycle requirements</strong> section.<br /><br /><ac:image ac:width="464"><ri:attachment ri:filename="password_complexity_management.png" /></ac:image><br /><br /></span></li><li><span>Enable the password complexity requirements that passwords must meet.<br /></span><ul><li>Select if the password must contain the following:<ul><li>Lowercase letters and/or</li><li>Uppercase letters and/or</li><li>Special characters and/or</li><li>Numbers;</li></ul></li><li>Select if the password must be of any minimum length.<span> </span></li></ul></li><li><span>If you selected the <strong>Minimum length </strong>requirement, enter the minimum length in the <strong>Password minimum length</strong> field.</span></li><li><span>Click <strong>SAVE</strong>.</span></li></ol><h3 class="auto-cursor-target">Setting password lifecycle requirements</h3><p>To set the requirements of password lifecycle</p><hr /><ol><li>In the <strong>Server settings</strong> page, select the <strong>Lifecycle </strong>tab in the <span><strong>Password complexity &amp; lifecycle requirements</strong> section.<br /><br /><ac:image ac:width="464"><ri:attachment ri:filename="password_lifecycle_management.png" /></ac:image><br /><br /></span></li><li><span>Enable the password lifecycle requirements that passwords must meet.<br /></span><ul><li><strong>Password history:</strong> you can forbid users from selecting previously used passwords.<br />If you enable this option, enter a number in the <strong>Number of passwords </strong>field. This number defines how many previous passwords cannot be used as the current password, i.e. if the number is 5, then the user cannot use the last 5 passwords they used before.</li><li><strong>User lockout:</strong> you can choose to disable a user upon reaching a defined number of subsequent unsuccessful login attempts.<br />If you enable this option, enter the number of allowed unsuccessful login attempts in the <strong style="letter-spacing: 0.0px;">Number of tries </strong><span style="letter-spacing: 0.0px;">field.</span></li><li><strong>Password age:</strong> you can force users to change the password after a defined number of days. If you enable this option, specify the value in the <strong style="letter-spacing: 0.0px;">Number of days</strong><span style="letter-spacing: 0.0px;"> field. This determines how many days must pass before users are prompted to change their password.</span></li></ul></li><li><span>Click <strong>SAVE</strong>.</span></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=172163132 space=TWCloud2024xR1 version=1 -->
## PAGE 00164: Managing resource branches

- page_id: `172163132`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/172163132/Managing+resource+branches
- version_number: 1
- version_date: `2024-05-20T15:26:47.350+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application
- labels: []

### NORMALIZED CONTENT

**On this page**

5

You can conveniently view and manage the branches of modeling tool resources through the Resources application.

##### Viewing resource branches

To view resource branches

1. In the Resources application, find the resource whose branches you want to view.
2. Click [ATTACHMENT filename='menu.png'] next to the resource and select View resource details .
3. Look for the Branches card at the bottom of the Resource details pane. [IMAGE alt='' src='']Viewing resource Branches card in Resource details pane.

##### Managing resource branches

###### Renaming, archiving, and deleting branches

Click [IMAGE alt='' src=''] next to a branch in the Branches card to view branch managing options:

- Rename: click to edit the branch name.
- Archive: click to move the branch to the archive,
- Delete: click to delete the resource branch.

###### Unarchiving branches

To unarchive a branch

1. Click View all at the bottom of the Branches card.
2. In the Resource branches pane that opens, enable the Show archived branches option: [ATTACHMENT filename='archived_branches.png']
3. To unarchive a branch, click [ATTACHMENT filename='menu.png'] next to an archived (greyed-out) branch and select Unarchive.

###### Filtering branches

To filter out branches, type the branch name into the search field at the top of the Resource branches pane:

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="69e8d57c-2f2c-4c38-a390-cd6038453580"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p style="text-align: left;">You can conveniently view and manage the branches of modeling tool resources through the Resources application.</p><h3 style="text-align: left;">Viewing resource branches</h3><p>To view resource branches</p><hr /><ol><li>In the Resources application, find the resource whose branches you want to view.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource and select <strong>View resource details</strong>.</li><li style="text-align: left;">Look for the Branches card at the bottom of the Resource details pane.<br /><h6 style="text-align: center;"><ac:image ac:align="center" ac:width="1200"><ri:attachment ri:filename="resource_branches_in twc_admin.png" /></ac:image>Viewing resource Branches card in Resource details pane.</h6></li></ol><h3>Managing resource branches</h3><h4>Renaming, archiving, and deleting branches</h4><p>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to a branch in the Branches card to view branch managing options:</p><ul><li><strong>Rename:</strong> click to edit the branch name.</li><li><strong>Archive: </strong>click to move the branch to the archive,</li><li><strong>Delete:</strong> click to delete the resource branch.</li></ul><h4>Unarchiving branches</h4><p>To unarchive a branch</p><hr /><ol><li>Click <strong>View all </strong>at the bottom of the Branches card.</li><li>In the <strong>Resource branches </strong>pane that opens, enable the <strong>Show archived branches </strong>option:<br /><br /><ac:image><ri:attachment ri:filename="archived_branches.png" /></ac:image><br /><br /></li><li>To unarchive a branch, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image><span style="letter-spacing: 0.0px;"> next to an archived (greyed-out) branch and select </span><strong style="letter-spacing: 0.0px;">Unarchive.</strong></li></ol><h4>Filtering branches</h4><p>To filter out branches, type the branch name into the search field at the top of the Resource branches pane:</p><p><br /><ac:image><ri:attachment ri:filename="filtering_branches.png" /></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491875 space=TWCloud2024xR1 version=1 -->
## PAGE 00165: Managing roles

- page_id: `170491875`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491875/Managing+roles
- version_number: 1
- version_date: `2024-01-29T09:42:44.816+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application
- labels: []

### NORMALIZED CONTENT

To learn how to manage roles using the Roles application of Teamwork Cloud Admin, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn how to manage roles using the Roles application of Teamwork Cloud Admin, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=171180068 space=TWCloud2024xR1 version=1 -->
## PAGE 00166: Managing server settings

- page_id: `171180068`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180068/Managing+server+settings
- version_number: 1
- version_date: `2024-01-29T09:31:16.560+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

You can manage Teamwork Cloud settings by selecting **Server settings** in the left-side menu of the Settings application. For more information about the available actions, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can manage Teamwork Cloud settings by selecting <strong>Server settings</strong> in the left-side menu of the Settings application. For more information about the available actions, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="cec6e8a6-ce94-483a-88de-f79893f468a8" /></p>
````

<!--NOMAGIC_PAGE id=170491362 space=TWCloud2024xR1 version=3 -->
## PAGE 00167: Managing SSL certificate

- page_id: `170491362`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491362/Managing+SSL+certificate
- version_number: 3
- version_date: `2025-10-30T13:59:07.496+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration
- labels: []

### NORMALIZED CONTENT

**On this page**

4

By default, Teamwork Cloud and Web Application Platform use a self-signed certificate generated during installation. However, for production environments, it is strongly recommended that you use a certificate signed by a trusted Certificate Authority (CA). Follow the steps outlined on this page to replace the self-signed certificate with a CA certificate and Java keystore, provided that you either have a private key and certificate signed by a trusted CA, or a PFX file containing the private key and signed certificate.

##### Changing the self-signed certificate to a CA certificate

If you have PFX file, expand the section below to prepare the files needed.

#### EXPAND: Procedure for processing PFX certificate files

Procedure for processing PFX certificate files

Use the following steps to extract the key and certificate into separate files first. PFX is a PKCS#12 certificate archive file. This procedure uses the OpenSSL command line tool.

To process PFX certificate files

1. Extract the private key to key.pem file. bashDJangotrue-nocerts -out key.pem -nodes]]>
2. If there is a passphrase associated with the private key, remove the passphrase and generate a new private key file *server.key* bashDJangotrue
3. Extract the certificate to *teamworkcloud.crt* bashDJangotrue-nokeys -out teamworkcloud.crt]]> The .pfx file has now been converted to a private key file and a public certificate file. You can now proceed to use these two files to generate the keystore file required by Teamwork Cloud components.

The new certificate will have to be converted to a Java keystore for Teamwork Cloud components. Use the following procedure to update the keystore file with your new certificate and private key files.

To change the self-signed certificate using the keystore file

1. Locate the default keystore file at *<install_root>/configuration/keystore.p12*.
2. Update the keystore file with the new private/public key:
  1. Create a PKCS 12 file with the OpenSSL tool: bashDJangotrue In the example above, *teamworkcloud*is a sample alias. If you use a different alias, remember to update it in the *<install_root>\WebAppPlatform\shared\conf\authserver.properties* file.
  2. Copy the **keystore.p12** file to the *<install_root>/configuration* directory, replacing the default file with the new one.
3. Add the public certificate file to the *<install_root>/configuration* directory. The public certificate file, or .crt, is the public key from the private/public (.key/.crt) key pair.
4. (Recommended) Secure .key and .p12 files with a password. Make sure to keep the .key file in a safe place.
5. If you need to switch from IP to FQDN, see [CONFLUENCE_PAGE title='Changing server or service address' space=''].

If the default configuration (file names, locations, passwords, aliases, etc.) is not changed, no additional steps are necessary. However, if you are changing the default configuration, then you also need to update the relevant properties in the corresponding files, as described below.

#### INFO: OpenSSL on Windows

OpenSSL on Windows

- OpenSSL for Windows operating systems can be downloaded from http://gnuwin32.sourceforge.net/packages/openssl.htm .
- All commands should be run with administrator rights in the directory containing the OpenSSL executable file.

##### Updating service configuration

###### Updating Teamwork Cloud configuration

Update the default values for the properties indicated below in the*<install_root>/configuration/application.conf*file if any of the applicable values were changed.

```text

```

#### INFO: Certificate File

Certificate File

You can customize both the name and the path of the *teamworkcloud.crt* file. We recommend using the default file name and path to minimize configuration changes. If necessary, make configuration changes after confirming that the initial installation is successful.

```text

```

###### Updating Authentication server configuration

Update the default values for the properties indicated below in the*<install_root>/WebAppPlatform/shared/conf/authserver.properties*file if any of the applicable values were changed.

```text

```

###### Updating Web Application Platform configuration

Update the default values for the properties indicated below in the*<install_root>/WebAppPlatform/conf/server.xml*file if any of the applicable values were changed.

```text
]]>
```

Both services (Teamwork Cloud and Web Application Platform) must be restarted once all of the configuration changes are completed.

##### Regenerating self-signed keystore

You may need to regenerate the self-signed keystore and certificate from the initial Teamwork Cloud installation. Restoring the system with the self-signed certificate will help with troubleshooting keystore/certificate issues.

To regenerate self-signed keystore and certificate for Teamwork Cloud

1. Move or delete the current keystore.p12 and teamworkcloud.crt files located in the configuration directory (default path: <install_root>/TeamworkCloud/configuration ).
2. Execute the genkey script associated with the server's operating system, located in the scripts directory (default path: <install_root>/TeamworkCloud/scripts ).
3. Confirm the newly-generated keystore.p12 and teamworkcloud.crt files exist in the configuration directory. Ensure there is a read permission and ownership to user "twcloud." The keystore is reset to original parameters ( alias: teamworkcloud; password: nomagic )
4. Restore keystore/certificate service configurations specified in the previous section.
5. Restart twcloud and webapp services.

##### Useful OpenSSL Commands

To check a private key:

```bash
-check]]>
```

To check a signed certificate:

```bash
-text -noout]]>
```

To check a PKCS#12 file (.pfx or .p12):

```bash

```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ebe413e7-6d39-4696-889b-2b914e11f2f4"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>By default, Teamwork Cloud and Web Application Platform use a self-signed certificate <span style="color:var(--ds-text,#333333);">generated during installation</span>. However, for production environments, it is strongly recommended that you use a certificate signed by a trusted Certificate Authority (CA). Follow the steps outlined on this page to replace the self-signed certificate with a CA certificate and Java keystore, <span style="color:var(--ds-text,#333333);">provided that you either have a private key and certificate signed by a trusted CA, or a PFX file containing the private key and signed certificate.</span></p><h3><span style="color:var(--ds-text,#000000);">Changing the self-signed certificate to a CA certificate</span></h3><p>If you have PFX file, expand the section below to prepare the files needed.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="53536815-0c63-44c3-9a80-56930745c327"><ac:parameter ac:name="title">Procedure for processing PFX certificate files</ac:parameter><ac:rich-text-body><p>Use the following steps to extract the key and certificate into separate files first. PFX is a PKCS#12 certificate archive file. This procedure uses the OpenSSL command line tool.</p><p>To process PFX certificate files</p><hr /><ol><li><p>Extract the private key to key.pem file.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="64bfcb9b-8f36-45e0-9cfc-135db409c8fd"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl pkcs12 -in <certname.pfx> -nocerts -out key.pem -nodes]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>If there is a passphrase associated with the private key, remove the passphrase and generate a new private key file <em>server.key</em></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="45405d57-b391-4d47-a1b2-0bbee2bce5f2"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl rsa -in key.pem -out server.key]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>Extract the certificate to <em>teamworkcloud.crt</em></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="62bed80b-fa10-4010-9ede-b97bf019ee3f"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl pkcs12 -in <certname.pfx> -nokeys -out teamworkcloud.crt]]></ac:plain-text-body></ac:structured-macro><p>The .pfx file has now been converted to a private key file and a public certificate file. You can now proceed to use these two files to generate the keystore file required by Teamwork Cloud components.</p></li></ol></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">The new certificate will have to be converted to a Java keystore for Teamwork Cloud components. Use the following procedure to update the keystore file with your new certificate and private key files.</span></p><p>To change the self-signed certificate using the keystore file</p><hr /><ol><li style="list-style-type: decimal;"><p><span>Locate the default keystore file at <em>&lt;install_root&gt;/configuration/keystore.p12</em>.</span></p></li><li style="list-style-type: decimal;"><p>Update the keystore file with the new private/public key:</p><ol><li><p>Create a PKCS 12 file with the OpenSSL tool:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="973484dc-f890-497b-a2ac-fb89e873d0ef"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl pkcs12 -export -name teamworkcloud -in teamworkcloud.crt -inkey server.key -out keystore.p12]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a1a7ea41-f581-4850-bee2-90ac46f75a6d"><ac:rich-text-body><p>In the example above, <em>teamworkcloud </em>is a sample alias. If you use a different alias, remember to update it in the <em>&lt;install_root&gt;\WebAppPlatform\shared\conf\authserver.properties</em> file.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Copy the <strong>keystore.p12</strong> file to the <em>&lt;<span>install_root</span>&gt;/configuration</em> directory, replacing the default file with the new one.</p></li></ol></li><li style="list-style-type: decimal;"><p><span>Add the public certificate file to the <em>&lt;install_root&gt;/configuration</em> directory.<br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4756a43f-1b9d-43cd-b4c5-dab3b4035451"><ac:rich-text-body><p>The public certificate file, or .crt, is the public key from the private/public (<span>.key/.crt</span>) key pair.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li style="list-style-type: decimal;"><p>(Recommended) Secure .key and .p12 files with a password. Make sure to keep the .key file in a safe place.</p></li><li style="list-style-type: decimal;"><p>If you need to switch from IP to FQDN, see <ac:link><ri:page ri:content-title="Changing server or service address" /><ac:plain-text-link-body><![CDATA[how to change server or service address]]></ac:plain-text-link-body></ac:link>.</p></li></ol><p><span>If the default configuration (file names, locations, passwords, aliases, etc.) is not changed, no additional steps are necessary. However, if you are changing the default configuration, then you also need to update the relevant properties in the corresponding files, as described below.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ccb33ada-2c8b-472a-9c92-02304b892030"><ac:parameter ac:name="title">OpenSSL on Windows</ac:parameter><ac:rich-text-body><ul><li>OpenSSL for Windows operating systems can be downloaded from <a class="external-link" href="http://gnuwin32.sourceforge.net/packages/openssl.htm" rel="nofollow">http://gnuwin32.sourceforge.net/packages/openssl.htm</a>.</li><li>All commands should be run with administrator rights in the directory containing the OpenSSL executable file.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><span>Updating service configuration</span></h3><h4><span>Updating Teamwork Cloud configuration</span></h4><p><span>Update the default values for the properties indicated below in the </span><em>&lt;<span>install_root</span>&gt;/configuration/application.conf</em><span> file if any of the applicable values were changed.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="27c19b26-4408-4c22-a1cf-6ea4af9c6121"><ac:parameter ac:name="title">application.conf</ac:parameter><ac:plain-text-body><![CDATA[https {
        # the file name of the certificate or the key store (should be a full path)
        file = "configuration/teamworkcloud.crt"
}]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="93951186-ce41-4aa1-b2dc-c84ad4b6fec7"><ac:parameter ac:name="title">Certificate File</ac:parameter><ac:rich-text-body><p>You can customize both the name and the path of the <em>teamworkcloud.crt</em> file. We recommend using the default file name and path to minimize configuration changes. If necessary, make configuration changes after confirming that the initial installation is successful.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="60dfebd2-7521-4e5b-aed7-7b6e5be5fac4"><ac:parameter ac:name="title">application.conf</ac:parameter><ac:plain-text-body><![CDATA[ssl {
		keystorePath = "configuration/keystore.p12"
		keystoreType = "pkcs12"
		keystorePassword = "nomagic"
		keyPassword = "nomagic"
}]]></ac:plain-text-body></ac:structured-macro><h4 class="auto-cursor-target"><span style="color:var(--ds-text,#000000);">Updating Authentication server configuration</span></h4><p><span>Update the default values for the properties indicated below in the </span><em>&lt;<span>install_root</span>&gt;/WebAppPlatform/shared/conf/authserver.properties</em><span> file if any of the applicable values were changed.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="254878fe-2132-40dd-8a2f-19f4eae060d5"><ac:parameter ac:name="title">authserver.properties</ac:parameter><ac:plain-text-body><![CDATA[authentication.server.key-store=../configuration/keystore.p12
authentication.server.key-store-type=PKCS12
authentication.server.key-store-password=nomagic
authentication.server.key-password=nomagic
authentication.server.key-alias=teamworkcloud]]></ac:plain-text-body></ac:structured-macro><h4><span style="color:var(--ds-text,#000000);">Updating Web Application Platform configuration</span></h4><p><span>Update the default values for the properties indicated below in the </span><em>&lt;<span>install_root</span>&gt;/WebAppPlatform/conf/server.xml</em><span> file if any of the applicable values were changed.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="74793c41-13f3-4a5b-829c-317ef8e87688"><ac:parameter ac:name="title">server.xml</ac:parameter><ac:plain-text-body><![CDATA[<Certificate    certificateKeystoreFile="../configuration/keystore.p12" 
				certificateKeystorePassword="nomagic" 
				type="RSA" 
/>]]></ac:plain-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#000000);">Both services (Teamwork Cloud and Web Application Platform) must be restarted once all of the configuration changes are completed.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Regenerating self-signed keystore</h3><p>You may need to regenerate the self-signed keystore and certificate from the initial Teamwork Cloud installation. Restoring the system with the self-signed certificate will help with troubleshooting keystore/certificate issues. </p><p>To regenerate self-signed keystore and certificate for Teamwork Cloud</p><hr /><ol><li>Move or delete the current <strong>keystore.p12</strong> and <strong>teamworkcloud.crt</strong> files located in the configuration directory (default path: <em>&lt;install_root&gt;/TeamworkCloud/configuration</em>).</li><li>Execute the <em>genkey</em> script associated with the server's operating system, located in the <em>scripts</em> directory (default path: <em>&lt;install_root&gt;/TeamworkCloud/scripts</em>).</li><li>Confirm the newly-generated <strong>keystore.p12</strong> and <strong>teamworkcloud.crt</strong> files exist in the configuration directory. Ensure there is a <em>read </em>permission and ownership to user <em>&quot;twcloud.&quot; </em>The keystore is reset to original parameters (<em>alias: teamworkcloud; password: nomagic</em>)</li><li>Restore <em>keystore/certificate</em> service configurations specified in the previous section.</li><li>Restart twcloud and webapp services.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Useful OpenSSL Commands</h3><p>To check a private key:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ecf5bf5b-f7f0-471a-8655-d596509c0ca7"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl rsa -in <private_key_file> -check]]></ac:plain-text-body></ac:structured-macro><p>To check a signed certificate:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f29873b6-617e-4540-907d-57a3d36660bf"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl x509 -in <certificate.crt> -text -noout]]></ac:plain-text-body></ac:structured-macro><p>To check a PKCS#12 file (.pfx or .p12):</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="06340a93-3bb7-452e-a1ea-a3f7073be05f"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[openssl pkcs12 -info -in keystore.p12]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491727 space=TWCloud2024xR1 version=2 -->
## PAGE 00168: Managing user groups

- page_id: `170491727`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491727/Managing+user+groups
- version_number: 2
- version_date: `2025-10-30T14:18:20.565+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

A user group enables you to group users into different categories. You can assign roles to all users in a user group. The user group members will take up the roles and assignments (including the scope) that have been assigned to the user group. You can create a user group, update information, and assign roles to the user group once. They will then be assigned to the members of the user group.

You can create, import, update, or remove a user group. When you import a user group from an LDAP server, Teamwork Cloud imports the user group as an external user group. The external user group can be resynchronized to update its information with the one in the LDAP server.Moreover, it is possible to assign roles only to the external users in the external user group. You can update the external user group information with the one in the LDAP server by clicking the **Synchronize** button.

You can see both external and internal user groups on the **Users**application.

[IMAGE alt='' src='']

###### You will find user groups in the left side menu on the Users application.

#### editUserGroupEditing user group information

Clicking a user group name opens the **User Group**pane, where you will see the name and description of the group, roles assigned to the group, and the users in the group.

To edit an internal user group name and description

1. Go to the **Users**application and from the left side menu select a **User group**. Do one of the following:****
  - Click a user group name and from the **Group details** card select **Edit**.
  - Click [IMAGE alt='' src=''] and from the option list select **Edit group details.**
2. Edit the name and description.
3. Click the Save button to save the changes.

To edit internal or external user group roles

1. Click a user group name. The **User Group**pane opens.
2. In the **Roles** card click the **Change**button. The **Change roles** pane opens.
3. Add/Remove roles and select a scope (if a role is resource-related).
4. Click the Save button to save the changes.

To edit the members of an internal user group

1. Click a user group name. The **User Group**pane opens.
2. In the **Group members** card click the **Change**button. The **Change group members** pane opens.
3. Add or remove members.
4. Click the Save button to save the changes.

To edit an external user group information

1. Click a user group name. The User Group pane opens.
2. In the User Group pane, you can synchronize the user group, remove, and change role assignments.
3. Click the Save button to save the changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A user group enables you to group users into different categories. You can assign roles to all users in a user group. The user group members will take up the roles and assignments (including the scope) that have been assigned to the user group. You can create a user group, update information, and assign roles to the user group once. They will then be assigned to the members of the user group.</p><p>You can create, import, update, or remove a user group. When you import a user group from an LDAP server, Teamwork Cloud imports the user group as an external user group. The external user group can be resynchronized to update its information with the one in the LDAP s<ac:inline-comment-marker ac:ref="1cbd6d3d-fa6b-43bf-8dae-d24e40bc4325">erver. </ac:inline-comment-marker>Moreover, it is possible to assign roles only to the external users in the external user group. You can update the external user group information with the one in the LDAP server by clicking the <strong>Synchronize</strong> button.</p><p>You can see both external and internal user groups on the <strong>Users </strong>application.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="User_groups.PNG" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">You will find user groups in the left side menu on the Users application.</h6><p><br /></p><h2 style="color:var(--ds-text,#172b4d);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7647329b-22fe-4690-be21-5477f3991d68"><ac:parameter ac:name="">editUserGroup</ac:parameter></ac:structured-macro>Editing user group information</h2><p>Clicking a user group name o<ac:inline-comment-marker ac:ref="2b30ca92-fef9-4ce7-b0be-9fafe976c09f">pe</ac:inline-comment-marker>ns the <strong>User Group </strong>pane, where you will see the name and description of the group, roles assigned to the group, and the users in the group.</p><p><br /></p><p>To edit an internal user group name and description</p><hr style="" /><ol><li><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Go to the <strong>Users </strong>application and from the left side menu select a <strong>User group</strong>. Do one of the following:<strong> </strong></ac:inline-comment-marker><ul><li><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Click a user group name and from the <strong>Group details</strong> card </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">select <strong>Edit</strong>.</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:content-title="Using the app bar" /></ri:attachment></ac:image> and from the option list select <strong>Edit group details.</strong></ac:inline-comment-marker></li></ul></li><li><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Edit the name and description.</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Click the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05">Save</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="82a42758-3632-497e-ba6b-1973dbb39d05"> button to save the changes.</ac:inline-comment-marker></li></ol><p><br /></p><p>To edit internal or external user group roles</p><hr style="" /><ol><li><p>Click a user group name. The <strong>User Group </strong>pane opens.</p></li><li><p>In the <strong>Roles</strong> card click the <strong>Change </strong>button. The <strong>Change roles</strong> pane opens.</p></li><li><p>Add/Remove roles and select a scope (if a role is resource-related).</p></li><li>Click the <strong>Save</strong> button to save the changes.</li></ol><p><br /></p><p>To edit the members of an internal user group</p><hr style="" /><ol><li><p>Click a user group name. The <strong>User Group </strong>pane opens.</p></li><li><p>In the <strong>Group members</strong> card click the <strong>Change </strong>button. The <strong>Change group members</strong> pane opens.</p></li><li><p>Add or remove members.</p></li><li>Click the <strong>Save</strong> button to save the changes.</li></ol><p><br /></p><p>To edit an external user group information</p><hr style="" /><ol><li>Click a user group name. The <strong>User Group </strong>pane opens.</li><li>In the<strong> User Group</strong> pane, you can synchronize<strong> </strong>the user group, remove, and change role assignments.   </li><li>Click the <strong>Save</strong> button to save the changes.</li></ol>
````

<!--NOMAGIC_PAGE id=170491704 space=TWCloud2024xR1 version=1 -->
## PAGE 00169: Managing user roles and assignments

- page_id: `170491704`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491704/Managing+user+roles+and+assignments
- version_number: 1
- version_date: `2024-01-29T09:33:12.752+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing users
- labels: []

### NORMALIZED CONTENT

The **Roles** card provides information about the role (along with the scope) assigned to the user. Users can see assigned roles and resources, by clicking the **Change** button. In the open screen, you can see all assigned roles and their scope. You can also change user roles and assignments.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong>Roles</strong> card provides information about the role (along with the scope) assigned to the user. Users can see assigned roles and resources, by clicking the <strong>Change</strong> button. In the open screen, you can see all assigned roles and their scope. You can also change user roles and assignments.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491665 space=TWCloud2024xR1 version=2 -->
## PAGE 00170: Managing users

- page_id: `170491665`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491665/Managing+users
- version_number: 2
- version_date: `2025-10-30T14:15:34.054+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

In the Users application, you can manage not only user details like resetting user passwords or changing role assignments but also add or remove users from user groups and release locked elements.

Learn more about user management features:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>In the Users application, you can manage not only user details like resetting user passwords or changing role assignments but also add or remove users from user groups and release locked elements.</p><p><span style="letter-spacing: 0.0px;">Learn more about user management features:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="12992783-67e0-4033-b14d-2dce77a203c9" /></p>
````

<!--NOMAGIC_PAGE id=170491688 space=TWCloud2024xR1 version=3 -->
## PAGE 00171: Managing users details

- page_id: `170491688`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491688/Managing+users+details
- version_number: 3
- version_date: `2025-10-30T14:16:37.386+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing users
- labels: []

### NORMALIZED CONTENT

**On this page**

**5**

##### Viewing user details

The way you view user details depends on the type of role you are assigned. Users with the following roles can view user details: **User Manager, Security Manager, Resource Manager**.

##### User categories

- To see all users in the system, select Users from the left-side menu.
- To view only internal or external users, select Internal or External from the right-side menu category.

To view user details, do one of the following:

- Click [IMAGE alt='' src=''] next to the user and from the menu select View user details .
- Click on the user row. The User pane for the selected user will open.

##### Editing user details

When you are viewing user details in the **User** pane, you can select to edit the details in the**User details**card.

- To edit user details, click Edit .

[IMAGE alt='' src='']

###### User details card.

A User Manager can edit an internal user's data, except the username. Information cannot be directly edited via **User**pane for external users imported from servers. If you need to edit the information (except the username), you must [CONFLUENCE_PAGE title='Importing users and groups' space=''].

##### Resource details preferred management

You can set how users will be able to use Resource application.

- If you enable **Resource details preferred management**,****the **Resource details**open with a single click in the Resources application.
- If you disable Resource details preferred management , the resource opens with a single click in the Resources application.

Changes related to **Resource details preferred management** switcher will take some time (about 1 minute) to be updated in the system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="64878eb4-604a-4fdb-9266-e6f4b7012860"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Viewing user details</h3><p>The way you view user details depends on the type of role you are assigned. Users with the following roles can view user details: <strong>User Manager, Security Manager, Resource Manager</strong>. </p><h3>User categories</h3><ul><li>To see all users in the system, select <strong>Users </strong>from the left-side menu.</li><li>To view only internal or external users, select <strong>Internal </strong>or <strong>External </strong>from the right-side menu category.</li></ul><p><br /></p><p>To view user details, do one of the following:  </p><hr /><ul><li>Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"> <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> </span> next to the user and from the menu select <strong>View user details</strong>.</li><li>Click on the user row. The <strong>User </strong>pane for the selected user will open. </li></ul><h3 class="title">Editing user details</h3><p>When you are viewing user details in the <strong>User</strong> pane, you can select to edit the details in the<strong> User details </strong>card.</p><ul><li>To edit user details, click <strong>Edit</strong>.<br /><br /></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Account_card.PNG" /></ac:image></p><h6 style="text-align: center;">User details card. </h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1e0fbc7d-554c-4e90-a52e-46a7bbd38842"><ac:rich-text-body><p>A User Manager can edit an internal user's data, except the username. Information cannot be directly edited via <strong>User </strong>pane for external users imported from servers. If you need to edit the information (except the username), you must <ac:link><ri:page ri:content-title="Importing users and groups" /><ac:plain-text-link-body><![CDATA[convert the user to internal first]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Resource details preferred management</h3><p>You can set how users will be able to use Resource application.</p><ul><li><p>If you enable <strong>Resource details preferred management</strong>,<strong> </strong>the <strong>Resource details </strong>open with a single click in the Resources application.</p></li><li>If you disable <strong>Resource details preferred management</strong>, the <strong>resource </strong>opens with a single click in the Resources application.<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b9422266-92f3-4cc4-bc41-4e7f63c6981f"><ac:rich-text-body><p><span>Changes related to <strong>Resource details preferred management</strong> switcher will take some time (about 1 minute) to be updated in the system. </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180248 space=TWCloud2024xR1 version=2 -->
## PAGE 00172: Managing webhooks

- page_id: `171180248`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180248/Managing+webhooks
- version_number: 2
- version_date: `2025-10-30T14:46:53.609+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Working with webhooks
- labels: []

### NORMALIZED CONTENT

**On this page**

**4**

You can find the actions you need to manage a webhook by selecting the **Actions**[IMAGE alt='' src=''] buttonon the right of the webhook row:

[IMAGE alt='' src='']

###### Selecting the Actions button for a webhook.

The actions you can select in this menu are described below.

##### Viewing the history of a webhook

To view the history of a webhook

1. Select the Actions [ATTACHMENT filename='actions.png'] button on the right of the webhook row.
2. Select History. In the dialog that opens, you can see up to 10 most recent webhook history events: [ATTACHMENT filename='webhook_history.png']

##### Disabling a webhook

To disable a webhook

1. Select the Actions [ATTACHMENT filename='actions.png'] button on the right of the webhook row.
2. Select Disable.
3. In the dialog that opens, click DISABLE.

##### Editing a webhook

To edit a webhook

1. Select the Actions [ATTACHMENT filename='actions.png'] button on the right of the webhook row.
2. Make your edits and choose the options as you would when [CONFLUENCE_PAGE title='Creating a webhook' space=''] .

##### Deleting a webhook

To delete a webhook

1. Select the Actions [ATTACHMENT filename='actions.png'] button on the right of the webhook row.
2. In the dialog that opens, click DELETE.

##### **Bulk actions with webhooks**

You can enable, disable, or delete multiple webhooks at once.

To manage webhooks in bulk

1. In the Webhooks section of the Settings app, either:
  - Select the checkbox next to Title to select all webhooks : [ATTACHMENT filename='managing_webhooks_in_bulk.png'] OR
  - Select the checkboxes of individual webhooks that you want to manage.
2. At the top of the page, click the button of the action you want - Enable, Disable, or Delete: 
 
[IMAGE alt='' src='']
3. In the dialog that opens, confirm your action by selecting ENABLE, DISABLE, or DELETE, accordingly.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bb07406b-8bc9-43f1-ab4e-faf9175751ce"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>You can find the actions you need to manage a webhook by selecting the <strong>Actions </strong><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png"><ri:page ri:space-key="MCS2021xR1" ri:content-title="Converting users to internal or external" /></ri:attachment></ac:image> <span style="letter-spacing: 0.0px;">button</span><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">on the right of the webhook row:</span></p><p style="text-align: center;"> <ac:image><ri:attachment ri:filename="webhooks_actions_button.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Selecting the Actions button for a webhook.</h6><p>The actions you can select in this menu are described below.</p><h3 style="color:var(--ds-text,#172b4d);">Viewing the history of a webhook</h3><p>To view the history of a webhook</p><hr style="" /><ol><li>Select the <strong>Actions </strong><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png" /></ac:image> button on the right of the webhook row.</li><li>Select <strong>History. </strong>In the dialog that opens, you can see up to 10 most recent webhook history events:<br /><br /><ac:image><ri:attachment ri:filename="webhook_history.png" /></ac:image><strong><br /></strong></li></ol><h3 style="color:var(--ds-text,#172b4d);">Disabling a webhook</h3><p>To disable a webhook</p><hr style="" /><ol><li>Select the <strong>Actions </strong><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png" /></ac:image> button on the right of the webhook row.</li><li>Select <strong>Disable.</strong></li><li>In the dialog that opens, click <strong>DISABLE.</strong></li></ol><h3 style="color:var(--ds-text,#172b4d);">Editing a webhook</h3><p>To edit a webhook</p><hr style="" /><ol><li>Select the <strong>Actions </strong><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png" /></ac:image> button on the right of the webhook row.</li><li>Make your edits and choose the options as you would when <ac:link><ri:page ri:content-title="Creating a webhook" /><ac:plain-text-link-body><![CDATA[creating a webhook]]></ac:plain-text-link-body></ac:link>.</li></ol><h3 style="color:var(--ds-text,#172b4d);">Deleting a webhook</h3><p>To delete a webhook</p><hr style="" /><ol><li>Select the <strong>Actions </strong><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png" /></ac:image> button on the right of the webhook row.</li><li>In the dialog that opens, click <strong>DELETE.</strong></li></ol><h3 style="color:var(--ds-text,#172b4d);"><strong>Bulk actions with webhooks</strong></h3><p>You can enable, disable, or delete multiple webhooks at once.</p><p>To manage webhooks in bulk</p><hr style="" /><ol><li>In the <strong>Webhooks </strong>section of the <strong>Settings </strong>app, either:<ul><li>Select the checkbox next to <strong>Title </strong>to select <u>all webhooks</u>:<br /><br /><ac:image><ri:attachment ri:filename="managing_webhooks_in_bulk.png" /></ac:image><br /><br />OR</li><li>Select the checkboxes of individual webhooks that you want to manage.</li></ul></li><li>At the top of the page, click the button of the action you want - <strong>Enable, Disable,</strong> or <strong>Delete:<br /><br /><ac:image><ri:attachment ri:filename="webhooks_bulk_actions.png" /></ac:image><br /><br /></strong></li><li>In the dialog that opens, confirm your action by selecting<strong> ENABLE, DISABLE, </strong>or <strong>DELETE, </strong>accordingly.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=218759491 space=TWCloud2024xR1 version=2 -->
## PAGE 00173: Manual installation

- page_id: `218759491`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/218759491/Manual+installation
- version_number: 2
- version_date: `2025-03-18T14:06:17.212+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Monitoring stack
- labels: []

### NORMALIZED CONTENT

**Prerequisite**

- Download [ATTACHMENT filename='monitoring-stack_2024xRefresh2.zip']

In this section you will be walked through manual Monitoring Stack Installation.

- [CONFLUENCE_PAGE title='Monitoring node' space='']
- [CONFLUENCE_PAGE title='Telemetry Node' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong><span style="color: rgb(62,63,64);">Prerequisite</span></strong></p><ul><li><span style="color: rgb(62,63,64);">Download <ac:link><ri:attachment ri:filename="monitoring-stack_2024xRefresh2.zip" /></ac:link></span></li></ul><p><span style="color: rgb(62,63,64);">In this section you will be walked through manual Monitoring Stack Installation. </span></p><ul><li><ac:link><ri:page ri:content-title="Monitoring node" /></ac:link></li><li><ac:link><ri:page ri:content-title="Telemetry Node" /></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=171180636 space=TWCloud2024xR1 version=1 -->
## PAGE 00174: Model editing behavior and constraints

- page_id: `171180636`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180636/Model+editing+behavior+and+constraints
- version_number: 1
- version_date: `2024-03-26T09:36:08.374+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Editing and contextualizing
- labels: []

### NORMALIZED CONTENT

**On this page**

**4**

##### What model elements can be edited

In Cameo Collaborator for Teamwork Cloud, you can edit the following model element properties:

- Properties
- Stereotype tag, and slot value of the String type
- Property, stereotype tags
- Slot values of the Integer, Real, Boolean, and Enumeration types
- Slot values for Instance Specifications
- Bullet lists created by using document templates

##### What model elements can be created

In Cameo Collaborator for Teamwork Cloud, you can create the following model element properties:

- Documentation metaproperty and other textual properties except for slot values
- Stereotype tag values
- Paragraphs
- Slot values for Instance Specifications

##### Model editing constraints

There are several constraints related to model editing in Cameo Collaborator for Teamwork Cloud:

- You can only edit the property, stereotype tag, or slot values displayed in tables.
- You can edit only existing property values. Cameo Collaborator does not allow to enter property values that have not been specified.
- You can only edit a slot with a single value and the upper multiplicity of 0, 1, or Unspecified.
- You can only edit a stereotype tag with the upper multiplicity of 0, 1, or Unspecified.

##### How does model editing work

When you edit a model in Cameo Collaborator, it is automatically committed to Teamwork Cloud. Also, every time you refresh a document, model data is resent from the Teamwork Cloud project, so you can always see the latest information.

To fully understand the behavior of the model editing feature, note the following model editing use cases:

- In Cameo Collaborator, you can edit a password protected project.
- In Cameo Collaborator, you can edit an element even if it is locked by another user in a modeling tool.
- If two users edit the same property with a single value in a modeling tool and Cameo Collaborator simultaneously, the value that is saved first is lost after the second value is saved.
- If two users edit the same property with multiple values in a modeling tool and Cameo Collaborator simultaneously and the Cameo Collaborator user saves their value first, both values are merged after the value is saved in the modeling tool.
- If two users edit the same property with multiple values in a modeling tool and Cameo Collaborator simultaneously and the modeling tool user saves their value first, this value is lost after the second user saves the value in Cameo Collaborator.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4b1c4cba-c066-4879-a2f1-3e0e0d785aed"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3 style="color: rgb(23,43,77);">What model elements can be edited</h3><p>In Cameo Collaborator for Teamwork Cloud, you can edit the following model element properties:</p><ul><li><ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c">Properties</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c">Stereotype tag, and slot value of the String type</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c">Property, stereotype tags</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c">Slot values of the Integer, Real, Boolean, and Enumeration types</ac:inline-comment-marker></li><li>Slot values for Instance Specifications<ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c"><br /></ac:inline-comment-marker></li><li><span style="color: rgb(62,63,64);">Bullet lists created by using document templates</span></li></ul><h3 style="color: rgb(23,43,77);"><ac:inline-comment-marker ac:ref="11ca8226-9537-477f-876b-4be5b4fc213c">What model elements can be created</ac:inline-comment-marker></h3><p>In <ac:inline-comment-marker ac:ref="cf0c4896-6805-4ad0-a471-24cd6e57892f">Cameo Collaborator f</ac:inline-comment-marker>or Teamwork Cloud, you can create the following model element properties:</p><ul><li>Documentation metaproperty and other textual properties except for slot values</li><li>Stereotype tag values</li><li>Paragraphs</li><li>Slot values for Instance Specifications</li></ul><h3 style="color: rgb(23,43,77);">Model editing constraints</h3><p>There are several constraints related to model editing in Cameo Collaborator for Teamwork Cloud:</p><ul><li>You can only edit the property, stereotype tag, or slot values displayed in tables.</li><li>You can edit only existing property values. Cameo Collaborator does not allow to enter property values that have not been specified.</li><li><span style="color: rgb(62,63,64);">You can only edit a slot with a single value and the upper multiplicity of 0, 1, or Unspecified.</span></li><li>You can only edit a stereotype tag with the upper multiplicity of 0, 1, or Unspecified.</li></ul><h3 style="color: rgb(23,43,77);">How does model editing work</h3><p><ac:inline-comment-marker ac:ref="c1e9a94d-5019-4bd8-aaba-81622a166ae7">When you edit a model in Cameo Collaborator, it is automatically committed to Teamwork Cloud. Also, every time you refresh a document, model data is resent from the Teamwork Cloud project, so you can always see the latest information.</ac:inline-comment-marker></p><p><ac:inline-comment-marker ac:ref="c1e9a94d-5019-4bd8-aaba-81622a166ae7">To fully understand the behavior of the model editing feature, note the following model editing use cases:</ac:inline-comment-marker></p><ul><li>In Cameo Collaborator, you can edit a password protected project.</li><li>In Cameo Collaborator, you can edit an element even if it is locked by another user in a modeling tool.</li><li>If two users edit the same property with a single value in a modeling tool and Cameo Collaborator simultaneously, the value that is saved first is lost after the second value is saved.</li><li>If two users edit the same property with multiple values in a modeling tool and Cameo Collaborator simultaneously and the Cameo Collaborator user saves their value first, both values are merged after the value is saved in the modeling tool. </li><li><p>If two users edit the same property with multiple values in a modeling tool and Cameo Collaborator simultaneously and the modeling tool user saves their value first, this value is lost after the second user saves the value in Cameo Collaborator.</p></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180654 space=TWCloud2024xR1 version=1 -->
## PAGE 00175: Model editing use cases

- page_id: `171180654`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180654/Model+editing+use+cases
- version_number: 1
- version_date: `2024-01-29T09:36:08.301+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Editing and contextualizing
- labels: []

### NORMALIZED CONTENT

Analyze the following model editing use cases that can help you get the most out of this feature:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Analyze the following model editing use cases that can help you get the most out of this feature:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=218759493 space=TWCloud2024xR1 version=1 -->
## PAGE 00176: Monitoring node

- page_id: `218759493`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/218759493/Monitoring+node
- version_number: 1
- version_date: `2025-03-18T14:05:04.958+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Monitoring stack > Manual installation
- labels: []

### NORMALIZED CONTENT

**On this page**

5

**Downloads**

- [ATTACHMENT filename='monitoring-stack_2024xRefresh2.zip']

Install the following components which constitute the monitoring node:

- InfluxDB - time-series database for collecting the metric data
- Grafana - dashboard visualization layer
- Jmxtrans - Collector to retrieve JMX metrics from remote hosts

#### Installing and configuring InfluxDB

To install and configure InfluxDB

1. Install InfluxDB from yum repository.
  1. Create */etc/yum.repos.d/influxdb.repo* with the following: bashDJangotrue
  2. Install with the command: bashDJangotrue
2. Use custom configuration file
  1. Locate /etc/influxdb/influxdb.conf. Make a note of the file ownership and permission.
  2. Locate influxdb.conf from the extracted Monitoring-Node-Install folder and replace the existing file in /etc/influxdb/; be sure to reset ownership and permission after replacement
3. Open ports for InfluxDB, if needed. Refer to port table.
4. Enable and start service
  1. Enable the InfluxDB service for startup with the command: bashDJangotrue
  2. Start InfluxDB with the command: bashDJangotrue
5. Create InfluxDB databases with a 35-day retention policy using the following commands: bashDJangotrue

#### Installing Grafana

To install Grafana on the monitoring node

1. Determine a Grafana version and use the following command to install (example for version 9.2.10): bashDJangotrue
2. Open port for Grafana, if needed. Refer to port table.
3. Enable and start servicel
  1. Enable the Grafana service for startup with the command: bashDJangotrue
  2. Start Grafana with the command: bashDJangotrue

****

#### Installing and configuring Jmxtrans

To install Jmxtrans on the monitoring node

1. Install with the command: bashDJangotrue
2. Delete the Jmxtrans System V service autostart: bashDJangotrue
3. Create configuration file for each telemetry node
  1. Locate twcloud.json.template from the extracted Monitoring-Node-Install folder
  2. Create a copy of this template file for each telemetry node in /var/lib/jmxtrans. We recommend using the twcloud-[hostname].json naming convention, where [hostname] is associated with the telemetry node.
  3. Edit each JSON file
    1. Replace IP_ADDRESS with the IP address or FQDN of the telemetry node
    2. Replace HOST_NAME with the hostname of the telemetry node (as per the command "hostname")

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ba629d00-9b82-4de9-9f73-0f4872211f45"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro> </p></ac:layout-cell><ac:layout-cell><p><strong>Downloads</strong></p><ul><li style="font-style: italic;"><em><ac:link><ri:attachment ri:filename="monitoring-stack_2024xRefresh2.zip"><ri:page ri:content-title="Monitoring node" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:link></em></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Install the following components which constitute the monitoring node:</p><ul><li>InfluxDB - time-series database for collecting the metric data</li><li>Grafana - dashboard visualization layer</li><li>Jmxtrans - Collector to retrieve JMX metrics from remote hosts</li></ul><h2>Installing and configuring InfluxDB</h2><p>To install and configure InfluxDB</p><hr /><ol><li>Install InfluxDB from yum repository.<ol><li><span>Create <em>/etc/yum.repos.d/influxdb.repo</em> with the following:</span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a6ad71e7-a44e-4685-9be2-3b124855b5d1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[[influxdata]

name = InfluxData Repository - Stable
baseurl = https://repos.influxdata.com/stable/\$basearch/main
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdata-archive_compat.key]]></ac:plain-text-body></ac:structured-macro></li><li><span style="letter-spacing: 0.0px;">Install with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="f50e2300-ffb2-4daa-99ff-f2da012f48b2"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo yum install -y influxdb]]></ac:plain-text-body></ac:structured-macro></li></ol></li><li><span style="letter-spacing: 0.0px;">Use custom configuration file</span><ol><li><span>Locate /etc/influxdb/influxdb.conf. Make a note of the file ownership and permission.</span></li><li><span>Locate influxdb.conf from the extracted Monitoring-Node-Install folder and replace the existing file in /etc/influxdb/; be sure to reset ownership and permission after replacement</span></li></ol></li><li>Open ports for InfluxDB, if needed. Refer to port table.</li><li><span>Enable and start service</span><ol><li><span>Enable the InfluxDB service for startup with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="03da00c0-965e-4e13-b8ee-c8ad79ff1508"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl enable influxdb]]></ac:plain-text-body></ac:structured-macro></li><li><span>Start InfluxDB with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a446aad6-3589-4ce2-8dce-febd331af3e5"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl start influxdb]]></ac:plain-text-body></ac:structured-macro><span><br /></span></li></ol></li><li>Create InfluxDB databases with a 35-day retention policy using the following commands:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4a7e4ef7-ea57-4787-8205-8b3200e057f8"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo influx -execute "CREATE DATABASE graphite with duration 35d"
sudo influx -execute "CREATE DATABASE telegraf with duration 35d"
sudo influx -execute "CREATE DATABASE twcloud with duration 35d"
sudo influx -execute "CREATE DATABASE webapp with duration 35d"]]></ac:plain-text-body></ac:structured-macro></li></ol><h2>Installing Grafana</h2><p>To install Grafana on the monitoring node</p><hr /><ol><li><p class="auto-cursor-target">Determine a Grafana version and use the following command to install (example for version 9.2.10):</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a34f103b-f62d-43e4-a708-c77a227722b6"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[GRAFANA_VER=9.2.10
sudo yum install -y https://dl.grafana.com/oss/release/grafana-$GRAFANA_VER-1.x86_64.rpm]]></ac:plain-text-body></ac:structured-macro></li><li>Open port for Grafana, if needed. Refer to port table.</li><li>Enable and start servicel<ol><li><p class="auto-cursor-target">Enable the Grafana service for startup with the command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="73e97079-3404-46ad-9210-da645e2b4fb8"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl enable grafana-server]]></ac:plain-text-body></ac:structured-macro></li><li class="auto-cursor-target"><p class="auto-cursor-target">Start Grafana with the command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="9c89fe3d-fbe0-48b8-94e4-b63265565451"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl start grafana-server]]></ac:plain-text-body></ac:structured-macro></li></ol></li></ol><p><strong style="letter-spacing: 0.0px;"> </strong></p><h2>Installing and configuring Jmxtrans</h2><p>To install Jmxtrans on the monitoring node</p><hr /><ol><li><p class="auto-cursor-target">Install with the command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="150cdfd2-659c-4ff7-85ae-65706dd3b7aa"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo yum -y install  https://repo.maven.apache.org/maven2/org/jmxtrans/jmxtrans/270/jmxtrans-270.rpm]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Delete the Jmxtrans System V service autostart:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2fbfa694-264c-492b-84c3-fdd2ca0b1e08"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[chkconfig --del jmxtrans
and remove the System V startup script
rm -f /etc/init.d/jmxtrans]]></ac:plain-text-body></ac:structured-macro></li><li>Create configuration file for each telemetry node<ol><li>Locate twcloud.json.template from the extracted Monitoring-Node-Install folder</li><li>Create a copy of this template file for each telemetry node in /var/lib/jmxtrans. We recommend using the twcloud-[hostname].json naming convention, where [hostname] is associated with the telemetry node.</li><li>Edit each JSON file<ol><li>Replace IP_ADDRESS with the IP address or FQDN of the telemetry node</li><li>Replace HOST_NAME with the hostname of the telemetry node (as per the command &quot;hostname&quot;)</li></ol></li></ol></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=218759435 space=TWCloud2024xR1 version=1 -->
## PAGE 00177: Monitoring stack

- page_id: `218759435`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/218759435/Monitoring+stack
- version_number: 1
- version_date: `2025-03-18T14:05:04.426+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: []

### NORMALIZED CONTENT

**On this page**

5

The monitoring stack is a Linux server toolkit for tracking and visualizing application resource usage in real time. This stack uses a set of open-source tools, including InfluxDB and Grafana, as well as Java Management Extensions (JMX) and various server agent plugins to collect and display metrics. The monitoring stack can be used to evaluate Teamwork Cloud/Magic Collaboration Studio system usage and performance. Metrics for Java operations, database backend processes, and server resource usages can be tracked to isolate performance issues, as well as optimize system resources.

#### Components

The following components constitute the monitoring node:

- InfluxDB - time series database for collecting the metric data
- Grafana - dashboard visualization layer
- Jmxtrans - Collector to retrieve JMX metrics from remote hosts

The following components are deployed on each Teamwork Cloud/Cassandra node:

- Telegraf - system metrics collector
- Dropwizard metrics-graphite-3.1.2.jar - metrics publishing agent for Java

On a single node installation, all components may be installed on the same node. On multi-node systems, the monitoring node components may be installed on one of the nodes (or on a separate machine), while the other components are deployed on each node.

[IMAGE alt='' src='']

#### Ports

The following are default ports used by services running on the monitoring node.

| Service | Default Port |
| --- | --- |
| InfluxDB | 2003, 8086 |
| Grafana | 3000 |

The following sections provide instructions on how to set up the monitoring stack.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="31d98fd2-f649-4ceb-9d7d-62ca515b0e23"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The monitoring stack is a Linux server toolkit for tracking and visualizing application resource usage in real time. This stack uses a set of open-source tools, including InfluxDB and Grafana, as well as Java Management Extensions (JMX) and various server agent plugins to collect and display metrics. The monitoring stack can be used to evaluate Teamwork Cloud/Magic Collaboration Studio system usage and performance. Metrics for Java operations, database backend processes, and server resource usages can be tracked to isolate performance issues, as well as optimize system resources.</p><h2><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">Components</span></h2><p>The following components constitute the monitoring node:</p><ul><li>InfluxDB - time series database for collecting the metric data</li><li>Grafana - dashboard visualization layer</li><li>Jmxtrans - Collector to retrieve JMX metrics from remote hosts</li></ul><p>The following components are deployed on each Teamwork Cloud/Cassandra node:</p><ul><li>Telegraf - system metrics collector</li><li>Dropwizard metrics-graphite-3.1.2.jar - metrics publishing agent for Java</li></ul><p>On a single node installation, all components may be installed on the same node. On multi-node systems, the monitoring node components may be installed on one of the nodes (or on a separate machine), while the other components are deployed on each node.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="monitoring stack diagram.png"><ri:page ri:content-title="Monitoring stack" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></p><h2><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">Ports</span></h2><p><span style="letter-spacing: 0.0px;">The following are default ports used by services running on the monitoring node.</span></p><table class="wrapped"><tbody class=""><tr class=""><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7" title="Background colour : Light grey 100%"><p title=""><strong><span>Service</span></strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7" title="Background colour : Light grey 100%"><p title=""><strong><span>Default Port</span></strong></p></td></tr><tr class=""><td><p><span>InfluxDB</span></p></td><td><p><span>2003, 8086</span></p></td></tr><tr class=""><td><p><span>Grafana</span></p></td><td><p><span>3000</span></p></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p style="margin-top: 10.0px;"><span style="color: rgb(62,63,64);">The following sections provide instructions on how to set up the monitoring stack.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c08aab57-fd67-426e-bd9d-e370a594ac4e" /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491549 space=TWCloud2024xR1 version=3 -->
## PAGE 00178: My account application

- page_id: `170491549`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491549/My+account+application
- version_number: 3
- version_date: `2025-10-30T14:13:13.228+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

**On this page**

4

In My account, you can manage your account data - add or remove your name, phone number, email address, and department. You can also change your password and generate a permissions report.

##### Opening My account

To open My account

- In the upper right corner click [ATTACHMENT filename='menu.png'] button and select My account application.

The user without assigned roles or resources will be automatically redirected to the **My account** page after signing in.

###### [IMAGE alt='' src='']Viewing My account application.

##### Changing password

To change the password

1. Open My account application.
2. Choose Change Password .
3. Enter your old and new passwords, then select Save .

You can also change your password in the **User details**pane by clicking**[IMAGE alt='' src='']**and selecting**Change password**option. Your new password cannot be the same as your previous password.

To change the Administrator’s password

1. Change the password using My account.
2. Update the properties file at <install_root>/WebAppPlatform/shared/conf/webappplatform.properties with the new Teamwork Cloud Admin password.
3. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] .

##### Generating permissions report

In the My account application, you can generate your permissions report. Click[IMAGE alt='' src='']at the bottom left corner to download the report in Excel format.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="98eea27e-1947-4a11-8807-c2747deee2f6"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>In My account, you can manage your account data - add or remove your name, phone number, email address, and department. You can also change your password and generate a permissions report. </p><h3 style="color:var(--ds-text,#172b4d);">Opening My account</h3><p>To open My account  </p><hr style="" /><ul><li>In the upper right corner click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> button and select <strong style="letter-spacing: 0.0px;">My account </strong>application.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f6048187-2730-4add-9a9f-1c05fe0a0f5c"><ac:rich-text-body><p>The user without assigned roles or resources will be automatically redirected to the <strong>My account</strong> page after signing in.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);"><ac:image ac:align="center" ac:width="500"><ri:attachment ri:filename="my_account_app_view.jpg" /></ac:image>Viewing My account application.</h6><h3 style="color:var(--ds-text,#172b4d);">Changing password</h3><p>To change the password</p><hr style="" /><ol><li>Open <strong>My account</strong> application. </li><li>Choose <strong>Change </strong><strong>Password</strong>. </li><li>Enter your old and new passwords, then select <strong>Save</strong>.</li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="361a928b-18fc-4f9c-88fc-dbfb71a9d6a6"><ac:rich-text-body><p>You can also change your password in the <strong>User details </strong>pane by clicking<strong> <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> </strong>and selecting<strong> Change password </strong>option. Your new password cannot be the same as your previous password.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>To change the Administrator’s password</p><hr style="" /><ol><li>Change the password using <strong>My account.</strong></li><li>Update the <em>properties</em> file at <em>&lt;install_root&gt;/WebAppPlatform/shared/conf/webappplatform.properties</em> with the new Teamwork Cloud Admin password.</li><li><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Restart CATIA No Magic WebApp Service]]></ac:plain-text-link-body></ac:link>.</li></ol><h3 style="color:var(--ds-text,#172b4d);">Generating permissions report</h3><p>In the My account application, you can generate your permissions report. Click<ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="Download icon.png"><ri:page ri:space-key="MCS2022x" ri:content-title="Viewing server status" /></ri:attachment></ac:image>at the bottom left corner to download the report in Excel format.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180524 space=TWCloud2024xR1 version=2 -->
## PAGE 00179: Navigation and filtering

- page_id: `171180524`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180524/Navigation+and+filtering
- version_number: 2
- version_date: `2025-10-31T12:30:33.370+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in a modeling tool
- labels: []

### NORMALIZED CONTENT

**On this page**

4

##### Navigating between comments and commented items

After [CONFLUENCE_PAGE title='Opening the comments panel' space=''], you can navigate from comments to commented items and vice versa the following way:

- Click a textual comment in the comments panel to navigate to the commented element and its commented properties. [ATTACHMENT filename='navigating_from_textual_comment.png']
- Click a graphical comment in the comments panel to navigate to the commented diagram and the graphical comment in that diagram. Other comments in the diagram will be shaded. [ATTACHMENT filename='navigating_from_graphical_comment.png']
- In the Specification window or the Quick properties panel, right-click a commented element property and select Navigate to Cameo Collaborator Comment to navigate to the comment in the comments panel. Commented properties are highlighted in yellow. [ATTACHMENT filename='navigating_from_commented property.png']
- Click a graphical comment in a diagram to navigate to the comment in the comments panel. [ATTACHMENT filename='navigating_to_graphical_comment.png']

#### TIP: Working with the comments panel

Working with the comments panel

In the Cameo Collaborator comments panel you can:

- Select comment text to automatically copy it to the clipboard.
- Click [ATTACHMENT filename='refresh.png'] on the top left corner of the comments panel to see if there are any new comments in the document.

##### Filtering commented elements

When addressing Cameo Collaborator comments in a modeling tool, you can quickly find commented elements and commented properties by filtering them out.

To filter commented elements

1. In a modeling tool, open the model that has Cameo Collaborator comments.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space=''] .
3. On the top of the Cameo Collaborator comments panel, click [ATTACHMENT filename='show_commented_elements.png'] .

After completing the above steps, all the model elements that have comments are displayed in the **Validation Results** panel on the bottom of your modeling tool.

[IMAGE alt='' src='']

###### The Validation Results panel displaying commented elements of a model.

To filter commented properties

1. In a modeling tool, open the model that has Cameo Collaborator comments.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space=''] .
3. Find the model element that has commented properties and do one of the following:
  - In the toolbar of the Quick Properties panel of the element, select [ATTACHMENT filename='show_commented_properties.png'] .
  - Open the Specification window of the element and select [ATTACHMENT filename='show_commented_properties.png'] .

[IMAGE alt='' src='']

After selecting the commented properties filter icon, only the element properties that have comments are shown as displayed above.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="8456084a-0483-4af9-88cc-cccc8d28043f"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3 class="auto-cursor-target" style="color:var(--ds-text,#172b4d);">Navigating between comments and commented items</h3><p>After <ac:link><ri:page ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[opening the comments panel]]></ac:plain-text-link-body></ac:link>, you can navigate from comments to commented items and vice versa the following way:</p><ul><li>Click a textual comment in the comments panel to navigate to the commented element and its commented properties.<br /><br /><ac:image><ri:attachment ri:filename="navigating_from_textual_comment.png" /></ac:image><br /><br /></li><li>Click a graphical comment in the comments panel to navigate to the commented diagram and the graphical comment in that diagram. Other comments in the diagram will be shaded.<br /><br /><ac:image><ri:attachment ri:filename="navigating_from_graphical_comment.png" /></ac:image><br /><br /></li><li>In the Specification window or the Quick properties panel, right-click a commented element property and select <strong>Navigate to Cameo Collaborator Comment</strong> to navigate to the comment in the comments panel. Commented properties are highlighted in yellow.<br /><br /><ac:image><ri:attachment ri:filename="navigating_from_commented property.png" /></ac:image><br /><br /></li><li>Click a graphical comment in a diagram to navigate to the comment in the comments panel.<br /><br /><ac:image><ri:attachment ri:filename="navigating_to_graphical_comment.png" /></ac:image></li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="515d6090-9999-4984-a8f6-18133993aa08"><ac:parameter ac:name="title">Working with the comments panel</ac:parameter><ac:rich-text-body><p>In the Cameo Collaborator comments panel you can:</p><ul><li><ac:inline-comment-marker ac:ref="064131d8-ad74-48fc-8d47-48780384094c">Select comment text to automatically copy it to the clipboard.</ac:inline-comment-marker></li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="refresh.png" /></ac:image> on the top left corner of the comments panel to see if there are any new comments in the document.</li></ul></ac:rich-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);"><br />Filtering commented elements</h3><p>When addressing Cameo Collaborator comments in a modeling tool, you can quickly find commented elements and commented properties by filtering them out.</p><p><br /></p><p>To filter commented elements</p><hr style="" /><ol><li><p>In a modeling tool, open the model that has Cameo Collaborator comments.</p></li><li><ac:link><ri:page ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator comments panel]]></ac:plain-text-link-body></ac:link>.</li><li>On the top of the Cameo Collaborator comments panel, click <ac:image><ri:attachment ri:filename="show_commented_elements.png" /></ac:image>.</li></ol><p><br />After completing the above steps, all the model elements that have comments are displayed in the <strong>Validation Results</strong> panel on the bottom of your modeling tool.<br /><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="filtering_commented_elements.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">The Validation Results panel displaying commented elements of a model.</h6><p>To filter commented properties</p><hr style="" /><ol><li><p>In a modeling tool, open the model that has Cameo Collaborator comments.</p></li><li><ac:link><ri:page ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator comments panel]]></ac:plain-text-link-body></ac:link>.</li><li>Find the model element that has commented properties and do one of the following:<br /><ul><li>In the toolbar of the Quick Properties panel of the element, select <ac:image><ri:attachment ri:filename="show_commented_properties.png" /></ac:image>.</li><li>Open the Specification window of the element and select <ac:image><ri:attachment ri:filename="show_commented_properties.png" /></ac:image>.</li></ul></li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="filtering_commented_properties.png" /></ac:image></p><p><br /></p><p><br />After selecting the commented properties filter icon, only the element properties that have comments are shown as displayed above.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180478 space=TWCloud2024xR1 version=2 -->
## PAGE 00180: Navigation pane

- page_id: `171180478`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180478/Navigation+pane
- version_number: 2
- version_date: `2025-10-31T12:26:39.187+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Structure of the document portal
- labels: ['navigating-document', 'navigating-published-model', 'published-model-views', 'changing-published-model-view', 'changing-model-view']

### NORMALIZED CONTENT

**On this page**

4

The navigation pane is located on the left side of a published model portal, as shown below. It displays the structure of the published model or the structure of the selected view of the published model. To view the desired content, click the relevant item in the navigation pane.

[IMAGE alt='' src='']

###### A published model portal with the navigation pane.

The navigation pane can be shown or hidden.

To show/hide the navigation pane

- Click [ATTACHMENT filename='show-hide_navigation_pane.png'] in the title bar of a published model portal.

##### Switching between model views

A published model can have one or more views, depending on the [CONFLUENCE_PAGE title='Document templates' space=''] that was used when [CONFLUENCE_PAGE title='Publishing documents' space='']. If a published model has multiple views, the navigation pane displays only the structure of the selected view.

To change the view of a published model

1. Click [ATTACHMENT filename='model_view_list.png'] next to the model view name in the title bar.
2. In the drop-down list of model views, select the view you want to display.

After selecting a model view from the drop-down list, the published model portal switches to that view and the navigation pane displays its structure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ac61bbbd-22ba-45c5-98ee-ffd447e0c8bc"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The navigation pane is located on the left side of a published model portal, as shown below. It displays the structure of the published model or the structure of the selected view of the published model. To view the desired content, click the relevant item in the navigation pane.</p><p><br /></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="navigation_pane_and_navigation_actions.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">A published model portal with the navigation pane.</h6><p>The navigation pane can be shown or hidden.</p><p><br /></p><p>To show/hide the navigation pane</p><hr style="" /><ul><li>Click <ac:image><ri:attachment ri:filename="show-hide_navigation_pane.png" /></ac:image> in the title bar of a published model portal.</li></ul><h3 style="color:var(--ds-text,#172b4d);"><br />Switching between model views</h3><p>A published model can have one or more views, depending on the <ac:link><ri:page ri:content-title="Document templates" /><ac:plain-text-link-body><![CDATA[template]]></ac:plain-text-link-body></ac:link> that was used when <ac:link><ri:page ri:content-title="Publishing documents" /><ac:plain-text-link-body><![CDATA[publishing]]></ac:plain-text-link-body></ac:link>. If a published model has multiple views, the navigation pane displays only the structure of the selected view.</p><p><br /></p><p>To change the view of a published model</p><hr style="" /><ol><li>Click <ac:image><ri:attachment ri:filename="model_view_list.png" /></ac:image> next to the model view name in the title bar.</li><li>In the drop-down list of model views, select the view you want to display.</li></ol><p><br />After selecting a model view from the drop-down list, the published model portal switches to that view and the navigation pane displays its structure.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180275 space=TWCloud2024xR1 version=3 -->
## PAGE 00181: Opening a resource

- page_id: `171180275`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180275/Opening+a+resource
- version_number: 3
- version_date: `2024-08-14T09:28:56.242+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application > Working with resources
- labels: []

### NORMALIZED CONTENT

You can open a Teamwork Cloud resource as described below.

To open a resource

1. [CONFLUENCE_PAGE title='Accessing Teamwork Cloud web applications' space=''] and click the category where the relevant resource is located. Using search barResources enables non case-sensitive keyword search.You can start typing a keyword in the Resource search bar to display all the resources that contain that keyword.
2. Click [ATTACHMENT filename='menu.png'] next to the resource that you want to open.
3. From the menu, select Open resource .

UML/SysML models are opened in your modeling tool, and Cameo Collaborator documents are opened in [CONFLUENCE_PAGE title='Cameo Collaborator for Teamwork Cloud' space='']. OSLC resourcesallow you to seethe OSLC UI previewsof model elements in the environment of a synchronized tool and they cannot be opened.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can open a Teamwork Cloud resource as described below.</p><p><br /></p><p>To open a resource</p><hr /><ol><li><p class="auto-cursor-target"><ac:link><ri:page ri:content-title="Accessing Teamwork Cloud web applications" /><ac:plain-text-link-body><![CDATA[Open the Resources application]]></ac:plain-text-link-body></ac:link> and click the category where the relevant resource is located.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="a2a02974-b4b0-4de4-9a99-e662d72d128d"><ac:parameter ac:name="title">Using search bar</ac:parameter><ac:rich-text-body><ul><li>Resources enables non case-sensitive keyword search.</li><li>You can start typing a keyword in the Resource search bar to display all the resources that contain that keyword.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource that you want to open.</li><li>From the menu, select <strong>Open resource</strong>.</li></ol><p><br />UML/SysML models are opened in your modeling tool, and Cameo Collaborator documents are opened in <ac:link><ri:page ri:content-title="Cameo Collaborator for Teamwork Cloud" /></ac:link>. <span>OSLC resources </span><span style="color: rgb(62,63,64);">allow you to see </span><span>the OSLC UI previews</span><span style="color: rgb(62,63,64);"> of model elements in the environment of a synchronized tool and they cannot be opened.</span></p><p><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180453 space=TWCloud2024xR1 version=1 -->
## PAGE 00182: Opening Cameo Collaborator for Teamwork Cloud

- page_id: `171180453`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180453/Opening+Cameo+Collaborator+for+Teamwork+Cloud
- version_number: 1
- version_date: `2024-03-26T09:26:58.142+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

Once you install Cameo Collaborator for Teamwork Cloud, you can access all published documents via the Resources application in a web browser.

To open Cameo Collaborator for TWC (the Resources application)

1. In an internet browser, go to *http(s)://<domain_name>:<port>/webapp/resources*. By default, Cameo Collaborator for Teamwork Cloud uses the 8443 port. Unsupported internet browsersCameo Collaborator for Teamwork Cloud does not support Internet Explorer. Use a different internet browser instead.
2. When the authentication page opens, enter your user name and password to sign in.
3. On the welcome page, click Open on the [CONFLUENCE_PAGE title='Resources application' space='TWCloud2024xR1'] which allows accessing Cameo Collaborator documents.

**Related pages**

- [CONFLUENCE_PAGE title='Teamwork Cloud and Services Installation' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Publishing documents' space='TWCloud2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Once you install Cameo Collaborator for Teamwork Cloud, you can access all published documents via the Resources application in a web browser.</p><p><br /></p><p>To open Cameo Collaborator for TWC (the Resources application)</p><hr /><ol><li><p class="auto-cursor-target">In an internet browser, go to <em>http(s)://&lt;domain_name&gt;:&lt;port&gt;/webapp/resources</em>. By default, Cameo Collaborator for Teamwork Cloud uses the 8443 port.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5400232-1f9d-4df1-95b1-eb5002055a8b"><ac:parameter ac:name="title">Unsupported internet browsers</ac:parameter><ac:rich-text-body><p>Cameo Collaborator for Teamwork Cloud does not support Internet Explorer. Use a different internet browser instead.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>When the authentication page opens, enter your user name and password to sign in.</li><li>On the welcome page, click <strong>Open</strong> on the <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resources application" /></ac:link> which allows accessing Cameo Collaborator documents.</li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Teamwork Cloud and Services Installation" /></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024x" ri:content-title="Publishing documents" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180456 space=TWCloud2024xR1 version=1 -->
## PAGE 00183: Opening historical version document

- page_id: `171180456`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180456/Opening+historical+version+document
- version_number: 1
- version_date: `2024-04-26T15:26:02.290+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Opening Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

**On this page**

4

You can open previous document versions to easily track content changes made by you or other users. Additionally, you can share links to specific document versions to show a snapshot of contents to your team members from specific points in time.

##### Accessing historical version document

To view historical version of a Cameo Collaborator document

1. Open the Resources application.
2. Click [IMAGE alt='' src=''] next to a Cameo Collaborator document. Then:
  1. Select Resource history. [IMAGE alt='' src=''] OR
  2. Select Resource details and click View all at the bottom of the History card in the Resource pane. [ATTACHMENT filename='view_all_history.png']
3. In the document history view, click [ATTACHMENT filename='menu.png'] next to the version you want to open and select Open. 
 
[IMAGE alt='' src='']
4. The [ATTACHMENT filename='history.png'] icon on the right of the app bar indicates that you are viewing a historical document version. Click this icon to see version information: [ATTACHMENT filename='historical_version_document.png']

##### Sharing link to historical version

You can share a link to a specific historical version of a Cameo Collaborator document. The recipient can access the document exactly as it appeared at that point in time.

To share historical version link

1. Follow the steps to [CONFLUENCE_PAGE title='Opening historical version document' space='TWCloud2024xR1'] .
2. In the document history view, click [ATTACHMENT filename='menu.png'] next to the version you want to share and select Get resource link.
3. In the dialog that opens with the document link:
  - Click Copy to copy the document link;
  - Toggle the Public switch if you need a public link, then click Copy.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="8825f7d4-d439-4ec3-be28-b2d6ec334e3d"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>You can open previous document versions to easily track content changes made by you or other users. Additionally, you can share links to specific document versions to show a snapshot of contents to your team members from specific points in time.</p><h3>Accessing historical version document</h3><p>To view historical version of a Cameo Collaborator document</p><hr /><ol><li>Open the <strong>Resources </strong>application.</li><li><span style="color: rgb(23,43,77);">Click </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(23,43,77);"><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image></span><span style="color: rgb(23,43,77);"> next to a Cameo Collaborator document. Then:</span><ol><li><span style="color: rgb(23,43,77);">Select </span><strong style="text-align: left;">Resource history.<br /></strong><strong style="text-align: left;"><br /><ac:image ac:width="700"><ri:attachment ri:filename="open_resource_history.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image><br /><br /></strong>OR<br /><br /></li><li>Select <strong>Resource details</strong> and click <strong>View all </strong>at the bottom of the <strong>History </strong>card in the Resource pane.<br /><br /><ac:image ac:width="350"><ri:attachment ri:filename="view_all_history.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image><br /><br /><br /></li></ol></li><li>In the document history view, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image> next to the version you want to open and select <strong>Open.<br /><br /><ac:image ac:width="700"><ri:attachment ri:filename="open_historical_version.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image><br /><br /></strong></li><li>The <ac:image ac:thumbnail="true" ac:height="24"><ri:attachment ri:filename="history.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="App bar" /></ri:attachment></ac:image> icon on the right of the app bar indicates that you are viewing a historical document version. Click this icon to see version information:<br /><br /><ac:image ac:width="500"><ri:attachment ri:filename="historical_version_document.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image></li></ol><h3>Sharing link to historical version</h3><p>You can share a link to a specific historical version of a Cameo Collaborator document. The recipient can access the document exactly as it appeared at that point in time.</p><p>To share historical version link</p><hr /><ol><li>Follow the steps to <ac:link ac:anchor="Accessing historical version document"><ac:plain-text-link-body><![CDATA[open document history view]]></ac:plain-text-link-body><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ac:link>.</li><li>In the document history view, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening historical version document" /></ri:attachment></ac:image> next to the version you want to share and select <strong>Get resource link.</strong></li><li>In the dialog that opens with the document link:<ul><li>Click <strong>Copy </strong>to copy the document link;</li><li>Toggle the <strong>Public </strong>switch if you need a public link, then click <strong>Copy.</strong> </li></ul></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=189136929 space=TWCloud2024xR1 version=2 -->
## PAGE 00184: Opening projects in Cameo Collaborator without publishing

- page_id: `189136929`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/189136929/Opening+projects+in+Cameo+Collaborator+without+publishing
- version_number: 2
- version_date: `2024-09-17T13:35:34.422+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Editing and contextualizing
- labels: []

### NORMALIZED CONTENT

To share ideas more quickly and efficiently, you can open and work with a project in Cameo Collaborator without publishing it. This enables you to add content to the projectin a wiki form, which can later be used to build a model. After opening a project in Cameo Collaborator, you will see a document-like environment, where you can create new sections and paragraphs, or add media, just like you would in a Cameo Collaborator document). However, you do not create a new document, instead, all the created content is added to the project.

#### NOTE: Prerequisite

Prerequisite

To open a project in Cameo Collaborator, the *Document View Collaborator Profile* must be used in that project. For more information, see [CONFLUENCE_PAGE title='Using other projects in a project' space='MD2024xR1'].

To work with a project in Cameo Collaborator

1. [CONFLUENCE_PAGE title='Accessing Teamwork Cloud web applications' space=''] and navigate to the project you want to open.
2. Click [IMAGE alt='' src=''] on the right side of the project line and select **Open in Collaborator**. When the project opens, you will see an empty document, like the one displayed below. 
 
[IMAGE alt='' src='']
3. Do the following to add new content to the project:
  - [CONFLUENCE_PAGE title='Creating and managing document sections' space=''].
  - [CONFLUENCE_PAGE title='Creating paragraphs' space=''].
  - [CONFLUENCE_PAGE title='Adding media' space=''].
4. Commit changes to the server.

When you finish adding content and open the project in a modeling tool, you will find the new content under the Package with the «CollaboratorDocument» stereotype as shown below.

[IMAGE alt='' src='']

###### The content added to the project via Cameo Collaborator.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(23,43,77);">To share ideas more quickly and efficiently, you can open and work with a project in Cameo Collaborator without publishing it. This enables you to add content to the project</span><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">in a wiki form, which can later be used to build a model. After opening a project in Cameo Collaborator, you will see a document-like environment, where you can create new sections and paragraphs, or add media, just like you would in a Cameo Collaborator document). However, you do not create a new document, instead, all the created content is added to the project.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="52629f85-a048-433f-95e9-dbba45b5fc4e"><ac:parameter ac:name="title">Prerequisite</ac:parameter><ac:rich-text-body><p>To open a project in Cameo Collaborator, the <em>Document View Collaborator Profile</em> must be used in that project. For more information, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using other projects in a project" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p><p><span style="letter-spacing: 0.0px;">To work with a project in Cameo Collaborator</span></p><hr /><ol><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Accessing Teamwork Cloud web applications" /><ac:plain-text-link-body><![CDATA[Go to the Resources application]]></ac:plain-text-link-body></ac:link> and navigate to the project you want to open.</span></li><li><span style="letter-spacing: 0.0px;">Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="project_menu_icon.png" /></ac:image> on the right side of the project line and select <strong>Open in Collaborator</strong>. When the project opens, you will see an empty document, like the one displayed below.<br /><br /><ac:image><ri:attachment ri:filename="open_project_in_cameo_collaborator.png" /></ac:image><br /><br /></span></li><li><span style="letter-spacing: 0.0px;">Do the following to add new content to the project:</span><ul><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Creating and managing document sections" /><ac:plain-text-link-body><![CDATA[Create and manage new sections]]></ac:plain-text-link-body></ac:link>.</span></li><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Creating paragraphs" /><ac:plain-text-link-body><![CDATA[Create paragraphs]]></ac:plain-text-link-body></ac:link>.</span></li><li><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:content-title="Adding media" /><ac:plain-text-link-body><![CDATA[Add images and videos]]></ac:plain-text-link-body></ac:link>.</span></li></ul></li><li><span style="letter-spacing: 0.0px;">Commit changes to the server.</span></li></ol><p><span style="letter-spacing: 0.0px;"><br />When you finish adding content and open the project in a modeling tool, you will find the new content under the Package with the «CollaboratorDocument» stereotype as shown below.</span></p><p><br /></p><p style="text-align: center;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="document_content_in_the_project.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="letter-spacing: 0.0px;">The content added to the project via Cameo Collaborator.</span></h6>
````

<!--NOMAGIC_PAGE id=171180521 space=TWCloud2024xR1 version=2 -->
## PAGE 00185: Opening the comments panel

- page_id: `171180521`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180521/Opening+the+comments+panel
- version_number: 2
- version_date: `2024-10-21T06:49:14.680+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in a modeling tool
- labels: []

### NORMALIZED CONTENT

You can view comments in a Cameo Collaborator document and respond to them right from a modeling tool where you work with your model. To do this, you have to open the Cameo Collaborator comments panel in the modeling tool, as described below.

To open the comments panel

1. In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.
2. In the main menu, select Tools > Cameo Collaborator > Show Comments .
3. If the model is related to more than one document, select the desired document in the Select Document dialog and click Select . [ATTACHMENT filename='select_document_dialog.png']

The Cameo Collaborator comments panel opens on the right side of the modeling tool window. It displays the comments of the related Cameo Collaborator document, allowing you to work with them.

[IMAGE alt='' src='']

###### A modeling tool with an open comments panel.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can view comments in a Cameo Collaborator document and respond to them right from a modeling tool where you work with your model. To do this, you have to open the Cameo Collaborator comments panel in the modeling tool, as described below.</p><p><br /></p><p>To open the comments panel</p><hr /><ol><li>In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.</li><li>In the main menu, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Show Comments</strong>.</li><li>If the model is related to more than one document, select the desired document in the <strong>Select Document</strong> dialog and click <strong>Select</strong>.<br /><br /><ac:image><ri:attachment ri:filename="select_document_dialog.png" /></ac:image></li></ol><p><br />The Cameo Collaborator comments panel opens on the right side of the modeling tool window. It displays the comments of the related Cameo Collaborator document, allowing you to work with them.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="comments_panel.png" /></ac:image></p><h6 style="text-align: center;">A modeling tool with an open comments panel.</h6>
````

<!--NOMAGIC_PAGE id=171180766 space=TWCloud2024xR1 version=1 -->
## PAGE 00186: Other features

- page_id: `171180766`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180766/Other+features
- version_number: 1
- version_date: `2024-01-29T09:36:37.754+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491314 space=TWCloud2024xR1 version=5 -->
## PAGE 00187: Passing properties to services

- page_id: `170491314`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491314/Passing+properties+to+services
- version_number: 5
- version_date: `2026-01-30T14:48:46.636+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Enterprise deployment > Building Web Application Platform containers
- labels: []

### NORMALIZED CONTENT

**On this page**

The properties of the Web Application Platform application are configured in the *webappplatform.properties* file. The sections below explain how these properties can be passed to a Docker container.

##### Copying properties to the classpath

By default, the *webappplatform.properties* file should be saved in the classpath. You can prepare the properties file and copy it to the classpath, as shown in bold in the example below:

#### PANEL: Docker file example

lightgrey

1

Docker file example

FROM tomcat:x.x.x-jrexx-temurin-jammy 
 
ARG TOMCAT_HOME=/usr/local/tomcat

COPY logback.xml ${TOMCAT_HOME}/shared/conf/ 
**COPY webappplatform.properties ${TOMCAT_HOME}/shared/conf/**COPY <service_name>.war ${TOMCAT_HOME}/webapps/ 
 
RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_HOME}/conf/catalina.properties 
 
EXPOSE 8080 
CMD ["catalina.sh", "run"]

For the correct version of Tomcat and JRE, please check the [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''] page.

Then one can use the following command to run the Docker container:

```text
]]>
```

##### Passing Location of the Properties File as an ENV Parameter

You can also put the *webappplatform.properties* file in a location of your choice (not in the Tomcat classpath). This can be achieved if the path to the properties file is passed as the *service.properties.file.location* Java system property. The following sample script copies the *webappplatform.properties* file to the */srv/config/* location. The system property with such a location value is added to the *setenv.sh* file used by the Tomcat server. In the script, *PROP_FILE_LOCATION_ENV* is used as the environment variable and it needs to be passed when running the container.

#### PANEL: Dockerfile example

lightgrey

solid

Dockerfile example

FROM tomcat:x.x.x-jrexx-temurin-jammy

To pass the location value, the PROP_FILE_LOCATION_ENV environment variable value needs to be provided when running the container:

lightgrey

solid

PROP_FILE_LOCATION_ENV='/srv/config/webappplatform.properties'

##### Using a File from a Mounted Volume

If there are multiple Tomcat instances (e.g., due to multiple Docker containers), then you may want to store and maintain a single copy of the *webappplatform.properties* file. This can be achieved by keeping the file in the path that is external to the Docker container running an application. In such case, the properties file should be manually copied to the location of your choice leaving the Dockerfile with the following statements:

#### PANEL: Dockerfile example

lightgrey

solid

Dockerfile example

FROM tomcat:x.x.x-jrexx-temurin-jammy 
 
ARG TOMCAT_HOME=/usr/local/tomcat 
**ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh** 
 
COPY logback.xml ${TOMCAT_HOME}/shared/conf/ 
COPY <service_name>.war ${TOMCAT_HOME}/webapps/ 
 
**RUN echo '#!/usr/bin/env bash' >> ${SET_ENV_FILE} RUN echo 'export JAVA_OPTS="$JAVA_OPTS –Dservice.properties.file.location=${PROP_FILE_LOCATION_ENV}"' >> ${SET_ENV_FILE}** 
**RUN chmod o+x ${SET_ENV_FILE}** 
 
EXPOSE 8080 
CMD ["catalina.sh", "run"]

When running a Docker image, the location must be mounted using the volume –v option. For more information, see [https://docs.docker.com/get-started/06_bind_mounts/](https://docs.docker.com/get-started/06_bind_mounts/). Assuming that the properties file is stored in the */mnt/<path>*directory accessible to Docker containers, the following command will mount the path */mnt/<path>*to *the /opt/<path>*of the Docker container:

```text
/webappplatform.properties' –v /mnt/:/opt/  ]]>
```

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="17890226-deb6-4519-aa91-6c683f2995c6" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The properties of the Web Application Platform application are configured in the <em>webappplatform.properties</em> file. The sections below explain how these properties can be passed to a Docker container.<br /><br /></p><h3 style="color:var(--ds-text,#172b4d);">Copying properties to the classpath</h3><p>By default, the <em>webappplatform.properties</em> file should be saved in the classpath. You can prepare the properties file and copy it to the classpath, as shown in bold in the example below:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="45ee7c70-af11-4c38-9426-d292245d1edc"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderWidth">1</ac:parameter><ac:parameter ac:name="title">Docker file example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">FROM tomcat:x.x.x-jrexx-temurin-jammy</span><br /><br />ARG TOMCAT_HOME=/usr/local/tomcat</p><p>COPY logback.xml ${TOMCAT_HOME}/shared/conf/<br /><strong>COPY webappplatform.properties ${TOMCAT_HOME}/shared/conf/<br /></strong>COPY &lt;service_name&gt;.war ${TOMCAT_HOME}/webapps/<br /><br />RUN sed -i &quot;s|shared\.loader=*$|shared\.loader=\&quot;\${catalina.base}/shared/conf\&quot;|&quot; ${TOMCAT_HOME}/conf/catalina.properties<br /><br />EXPOSE 8080<br />CMD [&quot;catalina.sh&quot;, &quot;run&quot;]</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d0093cdc-9c14-405a-aaef-a072f3178eb1"><ac:rich-text-body><p>For the correct version of Tomcat and JRE, please check the <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /></ac:link> page.</p></ac:rich-text-body></ac:structured-macro><p><br />Then one can use the following command to run the Docker container:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="340f824c-bc68-43e3-8c71-2c81550207bf"><ac:plain-text-body><![CDATA[docker run -p 8080:8080 <image_name:version>]]></ac:plain-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);"><br />Passing Location of the Properties File as an ENV Parameter</h3><p>You can also put the <em>webappplatform.properties</em> file in a location of your choice (not in the Tomcat classpath). This can be achieved if the path to the properties file is passed as the <em>service.properties.file.location</em> Java system property. The following sample script copies the <em>webappplatform.properties</em> file to the <em>/srv/config/</em> location. The system property with such a location value is added to the <em>setenv.sh</em> file used by the Tomcat server. In the script, <em>PROP_FILE_LOCATION_ENV</em> is used as the environment variable and it needs to be passed when running the container.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="262cf1c5-facf-4e91-b7ff-2e5c9f3aa7d8"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:parameter ac:name="title">Dockerfile example</ac:parameter><ac:rich-text-body><span style="color:var(--ds-text,#333333);">FROM tomcat:x.x.x-jrexx-temurin-jammy</span><br /><br />ARG TOMCAT_HOME=/usr/local/tomcat<br /><strong>ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh<br /><br /></strong>COPY logback.xml ${TOMCAT_HOME}/shared/conf/<br />COPY &lt;service_name&gt;.war ${TOMCAT_HOME}/webapps/<br />COPY webappplatform.properties /srv/config/<br /><br /><strong>RUN echo '#!/usr/bin/env bash' &gt;&gt; ${SET_ENV_FILE} RUN echo 'export JAVA_OPTS=&quot;$JAVA_OPTS –Dservice.properties.file.location=${PROP_FILE_LOCATION_ENV}&quot;' &gt;&gt; ${SET_ENV_FILE}<br />RUN chmod o+x ${SET_ENV_FILE}<br /><br /></strong>EXPOSE 8080<br />CMD [&quot;catalina.sh&quot;, &quot;run&quot;]</ac:rich-text-body></ac:structured-macro><p><br />To pass the location value, the PROP_FILE_LOCATION_ENV environment variable value needs to be provided when running the container:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2f3cf253-e628-4047-8d5f-bb73897da86f"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:rich-text-body>docker run -p 8080:8080 -e <strong>PROP_FILE_LOCATION_ENV='/srv/config/webappplatform.properties'</strong> &lt;image_name:version&gt;</ac:rich-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);"><br />Using a File from a Mounted Volume</h3><p>If there are multiple Tomcat instances (e.g., due to multiple Docker containers), then you may want to store and maintain a single copy of the <em>webappplatform.properties</em> file. This can be achieved by keeping the file in the path that is external to the Docker container running an application. In such case, the properties file should be manually copied to the location of your choice leaving the Dockerfile with the following statements:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2ca5bdcb-e4e1-4898-acbb-0f28eff06d7f"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:parameter ac:name="title">Dockerfile example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">FROM tomcat:x.x.x-jrexx-temurin-jammy</span><br /><br />ARG TOMCAT_HOME=/usr/local/tomcat<br /><strong>ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh</strong><br /><br />COPY logback.xml ${TOMCAT_HOME}/shared/conf/<br />COPY &lt;service_name&gt;.war ${TOMCAT_HOME}/webapps/<br /><br /><strong>RUN echo '#!/usr/bin/env bash' &gt;&gt; ${SET_ENV_FILE} RUN echo 'export JAVA_OPTS=&quot;$JAVA_OPTS –Dservice.properties.file.location=${PROP_FILE_LOCATION_ENV}&quot;' &gt;&gt; ${SET_ENV_FILE}</strong><br /><strong>RUN chmod o+x ${SET_ENV_FILE}</strong><br /><br />EXPOSE 8080<br />CMD [&quot;catalina.sh&quot;, &quot;run&quot;]</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>When running a Docker image, the location must be mounted using the volume –v option. For more information, see <a href="https://docs.docker.com/get-started/06_bind_mounts/">https://docs.docker.com/get-started/06_bind_mounts/</a>. Assuming that the properties file is stored in the <em>/mnt/&lt;path&gt; </em>directory accessible to Docker containers, the following command will mount the path <em>/mnt/&lt;path&gt; </em>to <em>the /opt/&lt;path&gt; </em>of the Docker container:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b98fd51c-03f1-4b64-81d3-342ca3ce6fd0"><ac:plain-text-body><![CDATA[docker run -p 8080:8080 --env PROP_FILE_LOCATION_ENV='/<path.to>/webappplatform.properties' –v /mnt/<path>:/opt/<path>  <image_name:version>]]></ac:plain-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491863 space=TWCloud2024xR1 version=3 -->
## PAGE 00188: Permissions

- page_id: `170491863`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491863/Permissions
- version_number: 3
- version_date: `2026-04-24T09:15:02.275+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application > User roles and permissions
- labels: []

### NORMALIZED CONTENT

**On this page**

4

Permission in Teamwork Cloud is an approval to perform a particular task or access one or more data or resource objects in the system. Permissions are associated with roles. A role contains a set of permissions allowing a user with that role to perform specific tasks or work on a resource. For example, a Resource Contributor role has permission to edit and read resources or edit resource properties. The permissions enable that role to perform specific operations that are forbidden to other users.

#### NOTE: Assigning permissions

Assigning permissions

You cannot directly assign permissions to a user. You must assign permissions to a role first and then assign the role to a user.

When you select a role in the Roles application, you can see its details and the permissions assigned to it. The figure below shows the permissions of the **User Manager**role.

###### [IMAGE alt='' src='']

###### The details of the selected role are displayed on the right-hand pane of the Roles application.

##### Default roles and their permissions

The table below describes all default roles and their permissions.

| Role | Permissions | Description | Scope |
| --- | --- | --- | --- |
| Data Markings Manager | Mark Data | The user with this role can mark or unmark Users, User Groups, Resources, and Categories with predefined clearance and classification levels. | Global |
| Index Manager | Administer Resources | The user must also have the Edit Resources and Edit Resource Properties permissions to enable listed actions; otherwise, the resources will be read-only.The user with these three permissions can:Use local and server resourcesStop using resources in the resource (including Standard/System Profiles)Lock/Unlock usages. Change versions of used resourcesUpdate resources from a local fileReload usages from a local fileImport usage to a resourceMigrate resources to a newer versionUpgrade resources to new versions of Standard/System ProfilesSet a resource as the latestExport packages to a new resourceReset element IDs (reset resource IDs)Create a branchRemove a branchRename a branch | Global/Resource specific |
| List All Resources | The user with this permission can see all resources and access them. | Global/Resource specific |  |
| Reports Manager | Access Reports | Users with this permission can access the Reports application. | Global |
| Resource Contributor | Edit Resources | The user with this permission can edit the resource contents. This includes the ability to change or augment the model. | Global/Resource specific |
| Edit Resource Properties | The user with this permission can edit resource properties, or change the name or description of the resource. | Global/Resource specific |  |
| Read Resources | The user with this permission can read the resource contents. This includes the ability to open and review models. | Global/Resource specific |  |
| Resource Creator | Create Resource | The user with this permission can create resources. This also includes the ability to add resources to the server. | Global/Category specific |
| Manage Categories | The user with this permission can categorize resources, including the ability to create, delete, or edit existing categories. | Global/Category specific |  |
| Resource Locks Administrator | Read Resources | The user with this permission can read the resource contents. This includes the ability to open and review models. | Global/Resource specific |
| Release Resource Locks | The user with this permission can release other users' locks in a resource. | Global/Resource specific |  |
| Resource Manager | Administer Resources permissionAdminister Resources | The user is required to also have the Edit Resources and Edit Resource Properties permissions to enable listed actions, otherwise, the resources will be read-only.The user with these three permissions can:Use local and server resourcesStop using resources in the resource (including Standard/System Profiles)Lock/Unlock usages. Change versions of used resourcesUpdate resources from a local fileReload usages from a local fileImport usage to a resourceMigrate resources to a newer versionUpgrade resources to new versions of Standard/System ProfilesSet a resource as the latestExport packages to a new resourceReset element IDs (reset resource IDs)Create a branchRemove a branch | Global/Resource specific |
| Edit Resources | The user with this permission can edit the resource contents. This includes the ability to change or augment the model. | Global/Resource specific |  |
| Edit Resource Properties | The user with this permission can edit resource properties, or change the name or description of the resource. | Global/Resource specific |  |
| List All Users permissionList All Users | The user with this permission can see all users. | Global |  |
| Manage Model Permissions | The user with this permission can manage model-level permissions. This permission automatically includes the List All Users permission. | Global/Resource specific |  |
| Manage Owned Resource Access Right | The user with this permission can manage resource-specific access rights, including the ability to grant or revoke user roles in the limited resource scope. This permission automatically includes the List All Users permission. | Global/Resource specific |  |
| Read Resources | The user with this permission can read the resource contents. This includes the ability to open and review models. | Global/Resource specific |  |
| Remove Resource | The user with this permission can delete resources. | Global/Resource specific |  |
| Resource Reviewer | Read Resources | The user with this permission can read the resource contents. This includes the ability to open and review models. | Global/Resource specific |
| Resource Synchronization Manager | Create Resource | The user with this permission can create resources. This also includes the ability to add resources to the server. | Category-specific |
| Manage Categories | The user with this permission can categorize resources, including the ability to create, delete, or edit existing categories. | Category-specific |  |
| Administer Resources | The user is required to also have the Edit Resources and Edit Resource Properties permissions to enable listed actions, otherwise, the resources will be read-only.The user with these permissions can:Use local and server resourcesStop using resources in the resource (including Standard/System Profiles)Lock/Unlock usages. Change versions of used resourcesUpdate resources from a local fileReload usages from a local fileImport usage to a resourceMigrate resources to a newer versionUpgrade resources to new versions of Standard/System ProfilesSet a resource as the latestExport packages to a new resourceReset element IDs (reset resource IDs)Create a branchRemove a branch | Category-specific |  |
| Security Manager | Configure Data Markings | The user with this permission can see the Data markings menu item in the Settings application. | Global |
| List All Resources | The user with this permission can see all resources and access them. | Global |  |
| List All Users | The user with this permission can see all users. | Global |  |
| Manage Security Roles | The user with this permission can manage roles, including the ability to create, edit, or delete roles. | Global |  |
| Manage User Permissions | The user with this permission can manage user-level permissions, including the ability to grant or revoke roles in unlimited scope. | Global |  |
| Server Administrator | Configure Server | The user with this permission can configure server settings, including the ability to configure a secured connection, LDAP connection, and manage server licenses. | Global |
| Simulation Manager | Manage Simulations | This permission allows users to manage all simulations, including the ability to get and review simulation results, and terminate simulations executed by other users. | Global |
| User Group Membership Manager | List All Users | The user with this permission can see all users. | Global |
| Manage User Group Membership | This permission allows users to manage assigned user group(s). If set to global scope, users can manage all user groups. | Global/user group-specific |  |
| User Manager | Create User | The user with this permission can create new server users. | Global |
| Edit User Properties | The user with this permission can edit user details. | Global |  |
| List All Users | The user with this permission can see all users. | Global |  |
| Manage User Groups | The user with this permission can manage user groups, including the ability to create, edit, or delete user groups. | Global |  |
| Remove User | The user with this permission can delete users. | Global |  |

- If a user with the Resource Creator role creates a resource, that user will be assigned as the Resource Manager for that particular resource.
- To be able to read-write resources, the user must have the Read Resources, Edit Resources, and Edit Resource Properties permissions. Otherwise, the user will see resources as read-only.
- To work with webhooks, a user needs the following permissions: Read Resources (global or resource-specific), Configure Server, and Administer Resources (global or resource-specific). With resource-specific permissions, the user can create and/or see the webhooks created for the resources that this user can read.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><strong>On this page</strong></p><p class="auto-cursor-target"><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="33265513-c5c6-4952-88cc-fa5dd1d72ef5"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Permission in Teamwork Cloud is an approval to perform a particular task or access one or more data or resource objects in the system. Permissions are associated with roles. A role contains a set of permissions allowing a user with that role to perform specific tasks or work on a resource. For example, a Resource Contributor role has permission to edit and read resources or edit resource properties. The permissions enable that role to perform specific operations that are forbidden to other users.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="66b0806e-e749-4eca-a1ba-5ee706fe8d5a"><ac:parameter ac:name="title">Assigning permissions</ac:parameter><ac:rich-text-body><p>You cannot directly assign permissions to a user. You must assign permissions to a role first and then assign the role to a user. </p></ac:rich-text-body></ac:structured-macro><p>When you select a role in the Roles application, you can see its details and the permissions assigned to it. The figure below shows the permissions of the <strong>User Manager </strong>role.<br /><br /></p><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="role_details.png" /></ac:image></h6><h6 style="text-align: center;">The details of the selected role are displayed on the right-hand pane of the Roles application.</h6><h3>Default roles and their permissions</h3><p>The table below describes all default roles and their permissions. </p><table class="relative-table wrapped" style="width: 76.3028%;"><colgroup><col style="width: 15.7121%;" /><col style="width: 23.35%;" /><col style="width: 46.118%;" /><col style="width: 14.8392%;" /></colgroup><tbody style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><th><strong>Role</strong></th><th><strong>Permissions</strong></th><th><strong>Description</strong></th><th><strong>Scope</strong></th></tr><tr style="margin-left: 30.0px;"><td><strong>Data Markings Manager</strong></td><td>Mark Data</td><td>The user with this role can mark or unmark Users, User Groups, Resources, and Categories with predefined clearance and classification levels.</td><td>Global</td></tr><tr><td rowspan="2"><strong>Index Manager</strong><br /><strong><br /></strong></td><td><span style="color:var(--ds-text,#333333);">Administer Resources</span></td><td><p>The user must also have the Edit Resources and Edit Resource Properties permissions to enable listed actions; otherwise, the resources will be read-only.</p><p>The user with these three permissions can:</p><ul><li>Use local and server resources</li><li>Stop using resources in the resource (including Standard/System Profiles)</li><li>Lock/Unlock usages. Change versions of used resources</li><li>Update resources from a local file</li><li>Reload usages from a local file</li><li>Import usage to a resource</li><li>Migrate resources to a newer version</li><li>Upgrade resources to new versions of Standard/System Profiles</li><li>Set a resource as the latest</li><li>Export packages to a new resource</li><li>Reset element IDs (reset resource IDs)</li><li>Create a branch</li><li>Remove a branch</li><li>Rename a branch</li></ul></td><td><span style="color:var(--ds-text,#333333);">Global/Resource specific</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">List All Resources</span></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all resources and access them.</span></td><td><span style="color:var(--ds-text,#333333);">Global/Resource specific</span></td></tr><tr><td><strong>Reports Manager</strong></td><td>Access Reports</td><td>Users with this permission can access the Reports application.</td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td rowspan="3"><strong>Resource Contributor</strong></td><td><p>Edit Resources</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can edit the resource contents. This includes the ability to change or augment the model.</span></td><td>Global/Resource specific</td></tr><tr style="margin-left: 30.0px;"><td>Edit Resource Properties</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can edit resource properties, or change the name or description of the resource.</span></td><td>Global/Resource specific</td></tr><tr style="margin-left: 30.0px;"><td>Read Resources</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can read the resource contents. This includes the ability to open and review models.</span></td><td>Global/Resource specific</td></tr><tr style="margin-left: 30.0px;"><td rowspan="2"><strong>Resource Creator</strong></td><td><p>Create Resource</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can create resources. This also includes the ability to add resources to the server.</span></td><td>Global/Category specific</td></tr><tr style="margin-left: 30.0px;"><td>Manage Categories</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can categorize resources, including the ability to create, delete, or edit existing categories.</span></td><td><span style="color:var(--ds-text,#172b4d);">Global/Category specific</span></td></tr><tr style="margin-left: 30.0px;"><td rowspan="2"><strong>Resource Locks Administrator</strong></td><td><p><span style="color:var(--ds-chart-gray-bold,#8590a2);"><span style="color:var(--ds-text,#000000);">Read Resources</span></span></p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can read the resource contents. This includes the ability to open and review models.</span></td><td>Global/Resource specific</td></tr><tr style="margin-left: 30.0px;"><td><p><span style="color:var(--ds-chart-gray-bold,#8590a2);"><span style="color:var(--ds-text,#000000);">Release Resource Locks</span></span></p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can release other users' locks in a resource. </span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td rowspan="8"><strong>Resource Manager </strong></td><td><div class="content-wrapper"><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="babc9bab-ab83-4985-8087-7e2b6ab7924d"><ac:parameter ac:name="">Administer Resources permission</ac:parameter></ac:structured-macro>Administer Resources</p></div></td><td><p>The user is required to also have the Edit Resources and Edit Resource Properties permissions to enable listed actions, otherwise, the resources will be read-only.</p><p>The user with these three permissions can:</p><ul><li>Use local and server resources</li><li>Stop using resources in the resource (including Standard/System Profiles)</li><li>Lock/Unlock usages. Change versions of used resources</li><li>Update resources from a local file</li><li>Reload usages from a local file</li><li>Import usage to a resource</li><li>Migrate resources to a newer version</li><li>Upgrade resources to new versions of Standard/System Profiles</li><li>Set a resource as the latest</li><li>Export packages to a new resource</li><li>Reset element IDs (reset resource IDs)</li><li>Create a branch</li><li>Remove a branch</li></ul></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td>Edit Resources</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can edit the resource contents. This includes the ability to change or augment the model.</span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td><span>Edit Resource Properties</span></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can edit resource properties, or change the name or description of the resource.</span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td><div class="content-wrapper"><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="b36e7dfb-6d25-4b22-805c-4e42b212c84e"><ac:parameter ac:name="">List All Users permission</ac:parameter></ac:structured-macro>List All Users</p></div></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all users.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Manage Model Permissions</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can manage model-level permissions. This permission automatically </span>includes the<span style="color:var(--ds-text,#000000);"> List All Users permission. </span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td>Manage Owned Resource Access Right</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can manage resource-specific access rights, including the ability to grant or revoke user roles in the limited resource scope. </span><span style="color:var(--ds-text,#000000);">This permission automatically includes the List All Users permission. </span><span style="color:var(--ds-text,#000000);"> </span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td>Read Resources</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can read the resource contents. This includes the ability to open and review models.</span></td><td><span>Global/Resource specific</span></td></tr><tr style="margin-left: 30.0px;"><td>Remove Resource</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can delete resources.</span></td><td><span>Global/Resource specific</span></td></tr><tr><td><strong>Resource Reviewer</strong></td><td><p>Read Resources</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can read the resource contents. This includes the ability to open and review models.</span></td><td>Global/Resource specific</td></tr><tr style="margin-left: 30.0px;"><td rowspan="3"><strong>Resource Synchronization Manager</strong></td><td><p>Create Resource</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can create resources. This also includes the ability to add resources to the server.</span></td><td>Category-specific</td></tr><tr style="margin-left: 30.0px;"><td>Manage Categories</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can categorize resources, including the ability to create, delete, or edit existing categories.</span></td><td><span>Category-specific</span></td></tr><tr style="margin-left: 30.0px;"><td><span>Administer Resources</span></td><td><p><span>The user is required to also have the Edit Resources and Edit Resource Properties permissions to enable listed actions, otherwise, the resources will be read-only.</span></p><p>The user with these permissions can:</p><ul><li>Use local and server resources</li><li>Stop using resources in the resource (including Standard/System Profiles)</li><li>Lock/Unlock usages. Change versions of used resources</li><li>Update resources from a local file</li><li>Reload usages from a local file</li><li>Import usage to a resource</li><li>Migrate resources to a newer version</li><li>Upgrade resources to new versions of Standard/System Profiles</li><li>Set a resource as the latest</li><li>Export packages to a new resource</li><li>Reset element IDs (reset resource IDs)</li><li>Create a branch</li><li>Remove a branch</li></ul></td><td><span>Category-specific</span></td></tr><tr style="margin-left: 30.0px;"><td rowspan="5"><strong>Security Manager</strong></td><td>Configure Data Markings</td><td>The user with this permission can see the Data markings menu item in the Settings application.</td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td><p>List All Resources</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all resources and access them.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>List All Users</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all users.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Manage Security Roles</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can manage roles, including the ability to create, edit, or delete roles.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Manage User Permissions</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can manage user-level permissions, including the ability to grant or revoke roles in unlimited scope.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td><strong>Server Administrator</strong></td><td><p>Configure Server</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can configure server settings, including the ability to configure a secured connection, LDAP connection, and manage server licenses.</span></td><td>Global</td></tr><tr><td><strong>Simulation Manager</strong></td><td><p>Manage Simulations</p></td><td style="text-align: left;"><p>This permission allows users to manage all simulations, including the ability to get and review simulation results, and terminate simulations executed by other users.</p></td><td>Global</td></tr><tr><td rowspan="2"><strong>User Group Membership Manager</strong><strong><br /></strong></td><td><p>List All Users</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all users.</span></td><td>Global</td></tr><tr><td><p>Manage User Group Membership</p></td><td style="text-align: left;"><p>This permission allows users to manage assigned user group(s). If set to global scope, users can manage all user groups.</p></td><td><span style="color:var(--ds-text,#172b4d);">Global/user group-specific</span></td></tr><tr style="margin-left: 30.0px;"><td rowspan="5"><strong>User Manager</strong></td><td><p>Create User</p></td><td><span style="color:var(--ds-text,#000000);">The user with this permission can create new server users.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Edit User Properties</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can edit user details.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>List All Users</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can see all users.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Manage User Groups</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can manage user groups, including the ability to create, edit, or delete user groups.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td>Remove User</td><td><span style="color:var(--ds-text,#000000);">The user with this permission can delete users.</span></td><td>Global</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a6be7a4-c93a-4ce9-a8fb-089253a92e03"><ac:rich-text-body><ul><li>If a user with the Resource Creator role creates a resource, that user will be assigned as the Resource Manager for that particular resource.</li><li><span>To be able to read-write resources, the user must have the Read Resources, Edit Resources, and Edit Resource Properties permissions. Otherwise, the user will see resources as read-only.</span></li><li>To work with webhooks, a user needs the following permissions: Read Resources (global or resource-specific), Configure Server, and Administer Resources (global or resource-specific). With resource-specific permissions, the user can create and/or see the webhooks created for the resources that this user can read.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491315 space=TWCloud2024xR1 version=1 -->
## PAGE 00189: Persisting logs for services

- page_id: `170491315`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491315/Persisting+logs+for+services
- version_number: 1
- version_date: `2023-07-07T08:50:25.045+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Enterprise deployment > Building Web Application Platform containers
- labels: []

### NORMALIZED CONTENT

If you want logs to be persistent when a container restarts (e.g., due to a container crash), they should be stored in a location outside Docker containers and mounted when running them. The location can be mounted by using the volume –v option when running a container (to learn more, see [https://docs.docker.com/get-started/06_bind_mounts/](https://docs.docker.com/get-started/06_bind_mounts/)). For example:

```text
]]>
```

This command will mount the */var/logs/wap* directory to the */user/local/logs* directory of the container. In this example, logs will be saved in the */var/logs/wap* directory of the host machine. The */usr/local/tomcat/logs* directory is the location where logs are configured to be saved on the container. For example, it may be different if Windows Tomcat is used as the base image or if logging configuration points to a different location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you want logs to be persistent when a container restarts (e.g., due to a container crash), they should be stored in a location outside Docker containers and mounted when running them. The location can be <ac:inline-comment-marker ac:ref="19e8cf52-831d-4389-a9b1-88be58752d14">mounted</ac:inline-comment-marker> by using the volume –v option when running a container (to learn more, see <a href="https://docs.docker.com/get-started/06_bind_mounts/">https://docs.docker.com/get-started/06_bind_mounts/</a>). For example:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6280ace1-3984-4ef9-ba9d-310f7b499ec2"><ac:plain-text-body><![CDATA[docker run -p 8080:8080 –v /var/logs/wap:/usr/local/tomcat/logs <image_name:version>]]></ac:plain-text-body></ac:structured-macro><p><br />This command will mount the <em>/var/logs/wap</em> directory to the <em>/user/local/logs</em> directory of the container. In this example, logs will be saved in the <em>/var/logs/wap</em> directory of the host machine. The <em style="letter-spacing: 0.0px;">/usr/local/tomcat/logs</em> directory is the location where logs are configured to be saved on the container. For example, it may be different if Windows Tomcat is used as the base image or if logging configuration points to a different location.</p>
````

<!--NOMAGIC_PAGE id=170491206 space=TWCloud2024xR1 version=2 -->
## PAGE 00190: Preparing the operating system

- page_id: `170491206`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491206/Preparing+the+operating+system
- version_number: 2
- version_date: `2025-09-26T11:11:00.550+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Linux
- labels: []

### NORMALIZED CONTENT

Prior to installing Cassandra, it is important to understand how Cassandra utilizes disk space. Disk space depends on usage. The database writes data to disk when appending data to the commit log for durability and when flushing memtables to SSTable data files for persistent storage. The commit log has a different access pattern (read/writes ratio) than the pattern for accessing data from SSTables. This is more important for spinning disks than for SSDs.

SSTables are periodically compacted. Compaction improves performance by merging and rewriting data as well as discarding old data. However, depending on the type and size of the compactions, disk utilization and data directory volume temporarily increases during compaction. For this reason, be sure to leave an adequate amount of free disk space available on a node.

Cassandra's data and commit logs should not, under any circumstances, be placed on the drive where the operating system is installed. Ideally, a server should have 3-4 drives or partitions. The root, /, or OS partition can be used as the target for the application. The /data partition should have adequate amounts of storage to accommodate your data. The /logs partition should hold your commit logs and (unless it is SSD) be on a different physical disk than the /data partition). The /backup partition should be allocated for backups.

For information about selecting hardware, see [https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hardware.html](https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hardware.html)

To achieve adequate performance, create separate partitions, ideally on separate drives. This helps to avoid I/O contention. We recommend 3 separate storage devicesor at least 3 separate partitions for non-production environments:

1. */opt/local*(the first block device should contain the operating system as well as a mount for the programs) .
2. The second block device ( NVMe/SSD ) should contain a mount point at /data (the device must have high storage capacity for all the data).
3. The third block device ( NVMe/SSD, but does not need to be of high capacity) should contain a mount point at /logs.

If you use SSD, the device can be a partition on the same block device as the /data partition. All partitions should be formatted using the XFS file system, and there should not be a swap partition. The /backup partition can be a mount on a shared storage device but should not be on the same physical drive as the /data partition. 
 
See an example of the contents of*/etc/fstab* after partitioning where the partitions were created using LVM (without a mount for the /backup partition).

```text

```

In the above example:

- Disk 1 contains the following partitions: /opt/local (40GB) and / (rest of the drive capacity).
- Disk 2 (the disk with the highest capacity) contains the /data partition (at least 250GB). Due to the way compactions are handled by Cassandra, up to 50% of headroom may be needed in a worst-case scenario.
- Disk 3 contains the /logs partition (at least 10 GB).
- You should also create an additional mount for backups. Unlike the data and commit log partitions, which should be on SSD storage, this mount can be of any type (including centralized storage such as a SAN or NAS). It should have at least the same capacity as the /data partition.

The partitioning scheme above is an example. Internal security protocols in your organization may dictate that other directories may not be located in the main partition. During the installation, all applications will be installed in*/opt/local*. By default, Cassandra will be installed install in */var/lib*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Prior to installing Cassandra, it is important to understand how Cassandra utilizes disk space. Disk space depends on usage. The database writes data to disk when appending data to the commit log for durability and when flushing memtables to SSTable data files for persistent storage. The commit log has a different access pattern (read/writes ratio) than the pattern for accessing data from SSTables. This is more important for spinning disks than for SSDs.</p><p class="p">SSTables are periodically compacted. Compaction improves performance by merging and rewriting data as well as discarding old data. However, depending on the type and size of the compactions, disk utilization and data directory volume temporarily increases during compaction. For this reason, be sure to leave an adequate amount of free disk space available on a node.</p><p>Cassandra's data and commit logs should not, under any circumstances, be placed on the drive where the operating system is installed. Ideally, a server should have 3-4 drives or partitions. The root, /, or OS partition can be used as the target for the application. The /data partition should have adequate amounts of storage to accommodate your data. The /logs partition should hold your commit logs and (unless it is SSD) be on a different physical disk than the /data partition). The /backup partition should be allocated for backups.</p><p>For information about selecting hardware, see <a href="https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hardware.html" class="">https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hardware.html</a></p><p>To achieve adequate performance, create separate partitions, ideally on separate drives. This helps to avoid I/O contention. We recommend 3 separate <span style="color:var(--ds-text,#172b4d);">storage devices </span>or at least 3 separate partitions for non-production environments:</p><ol><li data-uuid="a9b61c11-7cb7-4e74-a8b2-a576c4cd05ea"><span data-teams="true"><em>/opt/local </em>(the first block device should contain the operating system as well as a mount for the programs)</span>.</li><li data-uuid="8efeed75-e260-4923-a999-e2663ff6139d">The second block device (<span style="color:var(--ds-text,#172b4d);">NVMe/SSD</span>) should contain a mount point at /data (the device must have high storage capacity for all the data).</li><li data-uuid="d628cb77-48a2-47e6-a11b-1c033b61ba0f">The third block device (<span style="color:var(--ds-text,#172b4d);">NVMe/SSD,</span> but does not need to be of high capacity) should contain a mount point at /logs.</li></ol><p>If you use SSD, the device can be a partition on the same block device as the /data partition. All partitions should be formatted using the XFS file system, and there should not be a swap partition. The /backup partition can be a mount on a shared storage device but should not be on the same physical drive as the /data partition.<br /><br />See an example of the contents of<em> /etc/fstab</em> after partitioning where the partitions were created using LVM (without a mount for the /backup partition).</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6569206b-ae3b-4996-986d-483d1008619b"><ac:parameter ac:name="language">text</ac:parameter><ac:parameter ac:name="title">fstab</ac:parameter><ac:plain-text-body><![CDATA[#
# /etc/fstab
# Created by anaconda on Tue May  2 16:31:05 2017
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/cl_twccentos7-root /                       xfs     defaults        0 0
/dev/mapper/cl_twccentos7-data /data                   xfs     defaults        0 0
/dev/mapper/cl_twccentos7-logs /logs                   xfs     defaults        0 0
/dev/mapper/cl_twccentos7-opt_local /opt/local         xfs     defaults        0 0]]></ac:plain-text-body></ac:structured-macro><p>In the above example:</p><ul><li data-uuid="f2a841fb-0f6b-4f7b-b743-1e13a40022b3">Disk 1 contains the following partitions:  <em>/opt/local</em> (40GB) and<em> /</em> (rest of the drive capacity).</li><li data-uuid="1a9820c5-b0d6-4406-89df-ccf44d308b3f">Disk 2 (the disk with the highest capacity) contains the <em>/data</em> partition (at least 250GB). Due to the way compactions are handled by Cassandra, up to 50% of headroom may be needed in a worst-case scenario.</li><li data-uuid="b91527c9-bdbe-4b18-9124-1cef52687738">Disk 3 contains the<em> /logs</em> partition (at least 10 GB).</li><li data-uuid="4b4d9bab-9ae3-4228-9778-fabdb617a2f9">You should also create an additional mount for backups. Unlike the data and commit log partitions, which should be on SSD storage, this mount can be of any type (including centralized storage such as a SAN or NAS). It should have at least the same capacity as the /data partition.</li></ul><p>The partitioning scheme above is an example. Internal security protocols in your organization may dictate that other directories may not be located in the main partition. During the installation, all applications will be installed in<em> /opt/local</em>. By default, Cassandra will be installed install in <em>/var/lib</em>.</p>
````

<!--NOMAGIC_PAGE id=171180714 space=TWCloud2024xR1 version=1 -->
## PAGE 00191: Printing document sections

- page_id: `171180714`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180714/Printing+document+sections
- version_number: 1
- version_date: `2023-07-07T08:51:28.666+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Sharing and exporting
- labels: []

### NORMALIZED CONTENT

You can print the loaded section of a Cameo Collaborator document as described below.

To print a section of a Cameo Collaborator document

1. Open a Cameo Collaborator document.
2. In the navigation pane, select the item whose information you want to print. The information is loaded in the content pane. Opening the navigation paneTo show the navigation pane, click [IMAGE alt='' src=''] in the app bar.
3. Press Ctrl+P. The print window opens as displayed in the figure below.
4. Specify the printing settings, such as the number of copies, layout, and color.
5. Click the Print button.

The loaded section of a Cameo Collaborator document is now printed.

#### INFO: Printing in Model and Document views

Printing in Model and Document views

- If you print a document section in the [CONFLUENCE_PAGE title='Document view modes' space='TWCloud2024xR1'] , all the content of the element selected in the navigation pane is printed.
- If you print a document section in the [CONFLUENCE_PAGE title='Document view modes' space='TWCloud2024xR1'] , the loaded content starting with the content of the selected element is printed. The printed content may include information for several elements.

[IMAGE alt='' src='']

###### The print preview window of a document section.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can print the loaded section of a Cameo Collaborator document as described below.</p><p><br /></p><p>To print a section of a Cameo Collaborator document</p><hr /><ol><li>Open a Cameo Collaborator document.</li><li><p class="auto-cursor-target">In the navigation pane, select the item whose information you want to print. The information is loaded in the content pane.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="a0b32a9b-3347-4c15-a9c5-afb0b983ed8b"><ac:parameter ac:name="title">Opening the navigation pane</ac:parameter><ac:rich-text-body><p>To show the navigation pane, click <ac:image><ri:attachment ri:filename="show-hide_navigation_pane.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Printing document sections" /></ri:attachment></ac:image> in the app bar.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Press Ctrl+P. The print window opens as displayed in the figure below.</li><li>Specify the printing settings, such as the number of copies, layout, and color.</li><li>Click the <strong>Print</strong> button.</li></ol><p><br />The loaded section of a Cameo Collaborator document is now printed.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="bb691e54-2ee9-4998-9806-4d3697c41181"><ac:parameter ac:name="title">Printing in Model and Document views</ac:parameter><ac:rich-text-body><ul><li>If you print a document section in the <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Document view modes" /><ac:plain-text-link-body><![CDATA[Model view mode]]></ac:plain-text-link-body></ac:link>, all the content of the element selected in the navigation pane is printed.</li><li>If you print a document section in the <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Document view modes" /><ac:plain-text-link-body><![CDATA[Document view mode]]></ac:plain-text-link-body></ac:link>, the loaded content starting with the content of the selected element is printed. The printed content may include information for several elements.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="printing_document_section.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Printing document sections" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The print preview window of a document section.</h6>
````

<!--NOMAGIC_PAGE id=171180374 space=TWCloud2024xR1 version=2 -->
## PAGE 00192: Publishing documents

- page_id: `171180374`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180374/Publishing+documents
- version_number: 2
- version_date: `2024-05-09T13:41:30.413+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: ['publishing-to-cameo-collaborator', 'publishing-projects']

### NORMALIZED CONTENT

Publishing models to Cameo Collaborator for Teamwork Cloudallows you to present them in a simplified form for users who do not know modeling languages, such as UML or SysML.Publishing is the beginning step of the model review workflow, as displayed in the following figure:

#### NOTE: Prerequisites

Prerequisites

To publish documents to Cameo Collaborator for Teamwork Cloud, you must [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space='TWCloud2024xR1'] in your modeling tool.

[IMAGE alt='' src='']

###### Publishing a model is the first step in the workflow for reviewing models and providing feedback.

You can republish a model each time you update it while[CONFLUENCE_PAGE title='Reacting to feedback' space='TWCloud2024xR1']. When republishing the model, you can either create a new document with a different name or update the one already stored in Teamwork Cloud. The updated document includes all the comments from the previous version unless the comments are disabled when republishing.

To learn more, see the following topics:

#### NOTE: Publishing documents from synchronized projects

Publishing documents from synchronized projects

If you want to publish a Cameo Collaborator document from a synchronized project on the target Teamwork Cloud server, the project must already have the Cameo Collaborator profile used in it. In addition, the commenting and model editing capabilities in such a document will be disabled so that the synchronized project on the target server cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space='TWCloud2024xR1'].

#### NOTE: Cameo Collaborator and 3DEXPERIENCE platform

Cameo Collaborator and 3DEXPERIENCE platform

If [CONFLUENCE_PAGE title='Enabling 3DEXPERIENCE collaboration in a modeling tool' space='MD2024xR1']collaboration powered by the **3D**EXPERIENCE platform is enabled in the Environment Options, The Cameo Collaborator Publisher plugin is disabled in the modeling tool, and you cannot work with Cameo Collaborator for Teamwork Cloud.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);"><span style="color: rgb(24,24,24);">Publishing models to Cameo Collaborator for Teamwork Cloud </span><span style="color: rgb(24,24,24);">allows you to present them in a simplified form for users who do not know modeling languages, such as UML or SysML. </span>Publishing is the beginning step of the model review workflow, as displayed in the following figure:<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dd518cb5-3be9-4ff7-9fc3-911d561a6cfb"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To publish documents to Cameo Collaborator for Teamwork Cloud, you must <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[install the Cameo Collaborator Publisher plugin]]></ac:plain-text-link-body></ac:link> in your modeling tool.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><br /></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="main_workflow_publishing.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Publishing documents" /></ri:attachment></ac:image></span></p><h6 style="line-height: 1.66667;text-align: center;">Publishing a model is the first step in the workflow for reviewing models and providing feedback.<span style="color: rgb(62,63,64);"><br /></span></h6><p><br /></p><p><span style="color: rgb(62,63,64);">You can republish a model each time you update it while </span><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Reacting to feedback" /><ac:plain-text-link-body><![CDATA[reacting to the reviewer's feedback]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);">. When republishing the model, you can either create a new document with a different name or update the one already stored in Teamwork Cloud. The updated document includes all the comments from the previous version unless the comments are disabled when republishing.<br /></span></p><p>To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f646a71d-6e9b-4f95-a76f-ab6b5b220655"><ac:parameter ac:name="title">Publishing documents from synchronized projects</ac:parameter><ac:rich-text-body><p>If you want to publish a Cameo Collaborator document from a synchronized project on the target Teamwork Cloud server, the project must already have the Cameo Collaborator profile used in it. In addition, the commenting and model editing capabilities in such a document will be disabled so that the synchronized project on the target server cannot be modified. <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d91ba1c8-fbaf-4f6b-8bc8-b511516d007b"><ac:parameter ac:name="title">Cameo Collaborator and 3DEXPERIENCE platform</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Enabling 3DEXPERIENCE collaboration in a modeling tool" /><ac:link-body>collaboration powered by the <strong>3D</strong>EXPERIENCE platform is enabled in the Environment Options</ac:link-body></ac:link>, The Cameo Collaborator Publisher plugin is disabled in the modeling tool, and you cannot work with Cameo Collaborator for Teamwork Cloud.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180386 space=TWCloud2024xR1 version=7 -->
## PAGE 00193: Publishing from command line

- page_id: `171180386`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180386/Publishing+from+command+line
- version_number: 7
- version_date: `2025-04-18T10:30:57.763+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents
- labels: ['publish-in-the-headless-mode', 'publish-nogui']

### NORMALIZED CONTENT

**On this page**

4

Publishing Cameo Collaborator documents is the simplest way to present models tostakeholders, sponsors, customers, and engineering teams. Cameo Collaborator documents can be used not only to review model information and provide feedback but also to edit models directly from the web without using a modeling tool.

This chapter explains how to publish documents from the command line, which is useful if you want to publish them periodically, e.g., once a day or during non-business hours to save time.

#### NOTE: Prerequisites

Prerequisites

- [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space=''] .
- Cameo Collaborator for Teamwork Cloud works only with Teamwork Cloud projects. If you want to publish a local model, [CONFLUENCE_PAGE title='Adding projects to Teamwork Cloud' space='MD2024xR1'] .
- You must have the [CONFLUENCE_PAGE title='Roles and permissions' space=''] necessary for document publishing.

#### TIP: Recommendations

Recommendations

- If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:
  1. Go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory and open the *publish.properties* file.
  2. Increase the *-Xmx*value, e.g.,*-Xmx4000M*. It is recommended to set a larger heap size value than the one defined foryour modeling tool.
  3. Save and close the file.
- Depending on the size of the model you intend to publish, [CONFLUENCE_PAGE title='Memory allocation' space='MD2024xR1'] to your modeling tool:
  - 2 million element model - 24 GB of RAM
  - 1 million element model - 15 GB of RAM
  - 500k element model - 7 GB of RAM

#### TIP: Publishing tips

Publishing tips

- You can publish a Cameo Collaborator document from a historic version of a model as well. However, note that the commenting, editing, and comment import functionalities in such a document will be disabled.
- To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to Options > Project Options and specify the Decimal Places option. The setting is remembered and used for the documents published from the project.
- You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to [CONFLUENCE_PAGE title='Diagram image export' space='MD2024xR1'] .

#### INFO: Project permissions

Project permissions

When you publish a new document with the Administer Resources permission, it inherits [CONFLUENCE_PAGE title='Permissions' space='']. When you update a document, project permissions are not affected.

Publishing from the command-line interface consists of these steps:

1. 
2. or

##### Configuring publishing options

Before publishing a project from the command line interface, specify publishing properties by modifying a properties file. You can modify the file for every model you publish or reuse it for several models if you do not need to change the values of publishing properties.

To configure the properties for publishing to Cameo Collaborator

1. In the <modeling tool installation directory>/plugins/com.nomagic.collaborator.publisher directory, open for editing the template.properties file.
2. Read the comments in the file and specify the publishing options.

##### Publishing a Cameo Collaborator document

To publish a Cameo Collaborator document from the command line interface, you need to execute a specific command outlined below.

To publish a Cameo Collaborator document from the command line interface

1. Open the command line interface.
2. Go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory containing the executive file for model publishing.
3. Execute the following command:
  - On Windows \plugins\com.nomagic.collaborator.publisher\template.properties]]>
  - On OS X or Linux /plugins/com.nomagic.collaborator.publisher/template.properties]]>

After completing the steps above, your model is published to Cameo Collaborator. If you want to publish the same model frequently, you do not need to do it manually every time. Instead, schedule publishing as a background task to save time.

#### TIP: Logging

Logging

When publishing, all information is logged to the log file of your modeling tool. If you want the information to be logged to the command line interface, open the *<modeling_tool_intallation_directory>\plugins\com.nomagic.collaborator.publisher\publish.properties* file and add **-verbose** to the **APP_ARGS** line.

##### Scheduling to publish a document

If you need to publish your models periodically and/or during non-business hours, you can schedule them to be published automatically. The following procedures describe the scheduling process on Windows and Linux operating systems.

To schedule a publishing task on Windows

1. Open the Task Scheduler from the Start menu of your Windows computer and select the option to create a basic task.
2. Type the task name, an optional description and click Next .
3. Select how often you want the task to reoccur and click Next .
4. Specify when you want the task to start and click Next .
5. To schedule the publishing to start automatically, select the **Start a program** radio button and click **Next**.
6. Click the **Browse** button, go to the *<modeling tool installationdirectory>/plugins/com.nomagic.collaborator.publisher*directory, and open the *publish.exe* file.
7. In the **Add Arguments (optional)** box, type *properties=<modeling_tool_installation_directory>\plugins\com.nomagic.collaborator.publisher\template.properties* and click **Next**. 
 
[IMAGE alt='' src='']
8. Click Finish .

To schedule a publishing task on Linux

1. Connect to the remote server using SSH, or open the terminal directly.
2. Type the following command to open the *crontab*file with the default text editor: # crontab -e
3. Using the Cron syntax create a *cronjob* to run the model publishing task once a day at midnight: 0 0 * * * <modeling tool installation directory>/plugins/com.nomagic.collaborator.publisher/publish.sh -properties template.properties
4. Save the *crontab* file.

After completing the steps described above, your model is published automatically on a regular basis at a specified time.

##### Improving publishing performance

You can improve publishing performance by changing environment options in your modeling tool, as described below.

To improve publishing performance

1. In the main menu of your modeling tool, select Options > Environment .
2. On the left side of the Environment Options dialog, select the Collaboration option group.
3. On the right side of the dialog, set the Notify About New Project Versions on the Server option to false .
4. On the right side of the dialog, set the Notify About Newer Project Usages option to Never .
5. Click OK .

Now Teamwork Cloud will use fewer connections when publishing, so the publishing performance will improve.

[IMAGE alt='' src='']

###### Changing the highlighted environment options improves publishing performance.

**Related pages**

- [CONFLUENCE_PAGE title='Publishing documents' space='']
  - [CONFLUENCE_PAGE title='Publishing from graphical user interface' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="aecff9bc-9d8d-429c-bb6d-f7ea9a55d3dd"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(62,63,64);">Publishing Cameo Collaborator documents is the simplest way to present models to </span>stakeholders, sponsors, customers, and engineering teams. Cameo Collaborator documents can be used not only to review model information and provide feedback but also to edit models directly from the web without using a modeling tool.</p><p>This chapter explains how to publish documents from the command line, which is useful if you want to publish them periodically, e.g., once a day or during non-business hours to save time.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="61942541-1e20-48ba-86a6-a6971994dce5"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[The Cameo Collaborator Publisher plugin must be installed in your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li>Cameo Collaborator for Teamwork Cloud works only with Teamwork Cloud projects. If you want to publish a local model, <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Adding projects to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[add it to Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li><li>You must have the <ac:link><ri:page ri:content-title="Roles and permissions" /><ac:plain-text-link-body><![CDATA[user permissions]]></ac:plain-text-link-body></ac:link> necessary for document publishing.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="174b72be-2c84-421a-87ac-d4a5e8905adf"><ac:parameter ac:name="title">Recommendations</ac:parameter><ac:rich-text-body><ul><li>If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:<ol><li><p>Go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion</span><span style="color: rgb(0,0,0);"> directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory and open the <em>publish.properties</em> file.</p></li><li><p>Increase the <em>-Xmx</em><span style="color: rgb(0,0,0);"> value, e.g., </span><em>-Xmx4000M</em>. It is recommended to set a larger <span style="color: rgb(0,0,0);">heap size value than the one defined for</span><span style="color: rgb(0,0,0);"> your modeling tool.</span></p></li><li><p>Save and close the file.</p></li></ol></li><li>Depending on the size of the model you intend to publish, <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Memory allocation" /><ac:plain-text-link-body><![CDATA[allocate a sufficient amount of memory]]></ac:plain-text-link-body></ac:link> to your modeling tool:<ul><li><p>2 million element model - 24 GB of RAM</p></li><li><p>1 million element model - 15 GB of RAM</p></li><li><p>500k element model - 7 GB of RAM</p></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="dd769109-cbb1-4d6f-9581-3a50ef4eb4f8"><ac:parameter ac:name="title">Publishing tips</ac:parameter><ac:rich-text-body><ul><li>You can publish a Cameo Collaborator document from a historic version of a model as well. However, note that the commenting, editing, and comment import functionalities in such a document will be disabled.</li><li>To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to <strong>Options</strong> &gt; <strong>Project Options</strong> and specify the <strong>Decimal Places</strong> option. The setting is remembered and used for the documents published from the project.</li><li>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5e5fa403-8733-41b3-bfbf-8611500a852b"><ac:parameter ac:name="title">Project permissions</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);">When you publish a new document with the Administer Resources permission</span>, it inherits <ac:link><ri:page ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud project permissions]]></ac:plain-text-link-body></ac:link>. When you update a document, project permissions are not affected.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>Publishing from the command-line interface consists of these steps:</p><ol><li><ac:link ac:anchor="Configuring publishing options" /></li><li><ac:link ac:anchor="Publishing a Cameo Collaborator document" /> or <ac:link ac:anchor="Scheduling to publish a document"><ac:plain-text-link-body><![CDATA[scheduling publishing as a background task]]></ac:plain-text-link-body></ac:link></li></ol><h3>Configuring publishing options</h3><p>Before publishing a project from the command line interface, specify publishing properties by modifying a properties file. You can modify the file for every model you publish or reuse it for several models if you do not need to change the values of publishing properties.</p><p><br /></p><p>To configure the properties for publishing to Cameo Collaborator</p><hr /><ol><li>In the <em>&lt;modeling tool installation directory&gt;/plugins/com.nomagic.collaborator.publisher </em>directory, open for editing the <em>template.properties</em> file.</li><li><p class="auto-cursor-target">Read the comments in the file and specify the publishing options.</p></li></ol><h3>Publishing a Cameo Collaborator document</h3><p>To publish a Cameo Collaborator document from the command line interface, you need to execute a specific command outlined below.</p><p><br /></p><p>To publish a Cameo Collaborator document from the command line interface</p><hr /><ol><li>Open the command line interface.</li><li><p>Go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory containing the executive file for model publishing.</p></li><li><p>Execute the following command:</p><ul><li><p>On Windows</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="16283a09-a9e5-419d-b702-1102e6505938"><ac:plain-text-body><![CDATA[publish.exe properties=<modeling_tool_installation_directory>\plugins\com.nomagic.collaborator.publisher\template.properties]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">On OS X or Linux</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="ceab7baa-ff77-457d-a86a-ae6f4adf8ffe"><ac:plain-text-body><![CDATA[./publish properties=<modeling_tool_installation_directory>/plugins/com.nomagic.collaborator.publisher/template.properties]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li></ol><p><span style="color: rgb(0,51,102);"><span style="color: rgb(51,51,51);"><br />After completing the steps above, yo</span></span>ur model is published to Cameo Collaborator. If you want to publish the same model frequently, you do not need to do it manually every time. Instead, schedule publishing as a background task to save time.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="bb84e174-6024-42b2-a8cb-fdf78e725451"><ac:parameter ac:name="title">Logging</ac:parameter><ac:rich-text-body><p class="code-java">When publishing, all information is logged to the log file of your modeling tool. If you want the information to be logged to the command line interface, open the <em>&lt;modeling_tool_intallation_directory&gt;\plugins\com.nomagic.collaborator.publisher\publish.properties</em> file and add <strong>-verbose</strong> to the <strong>APP_ARGS</strong> line.</p></ac:rich-text-body></ac:structured-macro><h3>Scheduling to publish a document</h3><p>If you need to publish your models periodically and/or during non-business hours, you can schedule them to be published automatically. The following procedures describe the scheduling process on Windows and Linux operating systems.<br /> </p><p>To schedule a publishing task on Windows</p><hr /><ol><li>Open the <strong>Task Scheduler</strong> from the<strong> Start</strong> menu of your Windows computer and select the option to create a basic task.</li><li>Type the task name, an optional description and click <strong>Next</strong>.</li><li>Select how often you want the task to reoccur and click <strong>Next</strong>.</li><li>Specify when you want the task to start and click <strong>Next</strong>.</li><li><p>To schedule the publishing to start automatically, select the <strong>Start a program</strong> radio button and click <strong>Next</strong>.</p></li><li><p>Click the <strong>Browse</strong> button, go to the <em><span style="color: rgb(0,0,0);">&lt;modeling tool installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.collaborator.publisher </span></em>directory, and open the <em>publish.exe</em> file.</p></li><li><p>In the <strong>Add Arguments (optional)</strong> box, type <em><span style="color: rgb(23,43,77);">properties=&lt;modeling_tool_installation_directory&gt;\plugins\com.nomagic.collaborator.publisher\template.properties</span></em> and click <strong>Next</strong>.<br /><br /><ac:image><ri:attachment ri:filename="basic_task_creation_wizard.png" /></ac:image><br /><br /></p></li><li>Click <strong>Finish</strong>.</li></ol><p><br /></p><p>To schedule a publishing task on Linux</p><hr /><ol><li>Connect to the remote server using SSH, or open the terminal directly.</li><li><p>Type the following command to open the <em>crontab </em>file with the default text editor:</p><pre># crontab -e<br /><br /></pre></li><li><p>Using the Cron syntax create a <em>cronjob</em> to run the model publishing task once a day at midnight:</p><pre>0 0 * * * &lt;modeling tool installation directory&gt;/plugins/com.nomagic.collaborator.publisher/publish.sh -properties template.properties<br /><br /></pre></li><li><p>Save the <em>crontab</em> file.</p></li></ol><p><br />After completing the steps described above, your model is published automatically on a regular basis at a specified time.</p><h3>Improving publishing performance</h3><p>You can improve publishing performance by changing environment options in your modeling tool, as described below.</p><p><br /></p><p>To improve publishing performance</p><hr /><ol><li>In the main menu of your modeling tool, select <strong>Options</strong> &gt; <strong>Environment</strong>.</li><li>On the left side of the <strong>Environment Options</strong> dialog, select the <strong>Collaboration</strong> option group.</li><li>On the right side of the dialog, set the <strong>Notify About New Project Versions on the Server</strong> option to <em>false</em>.</li><li>On the right side of the dialog, set the <strong>Notify About Newer Project Usages</strong> option to <strong>Never</strong>.</li><li>Click <strong>OK</strong>.</li></ol><p><br />Now Teamwork Cloud will use fewer connections when publishing, so the publishing performance will improve.<br /><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="improving_publishing_performance.png" /></ac:image></p><h6 style="text-align: center;line-height: 1.66667;letter-spacing: normal;">Changing the highlighted environment options improves publishing performance.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Publishing documents" /></ac:link><ul><li><ac:link><ri:page ri:content-title="Publishing from graphical user interface" /></ac:link></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180377 space=TWCloud2024xR1 version=7 -->
## PAGE 00194: Publishing from graphical user interface

- page_id: `171180377`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180377/Publishing+from+graphical+user+interface
- version_number: 7
- version_date: `2024-10-25T08:54:26.168+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents
- labels: ['publishing-to-cameo-collaborator', 'publishing-projects']

### NORMALIZED CONTENT

**On this page**

4

Publishing documents from the graphical user interface is the simplest way to present models tostakeholders, sponsors, customers, and engineering teams. Cameo Collaborator documents can be used not only to review model information and provide feedback but also to edit models directly from the web without using a modeling tool.

#### NOTE: Prerequisites

Prerequisites

- [CONFLUENCE_PAGE title='Installing Cameo Collaborator Publisher plugin' space=''] .
- Cameo Collaborator for Teamwork Cloud works only with Teamwork Cloud projects. If you want to publish a local model, [CONFLUENCE_PAGE title='Adding projects to Teamwork Cloud' space='MD2024xR1'] .
- You must have the [CONFLUENCE_PAGE title='Roles and permissions' space=''] necessary for document publishing.

#### TIP: Recommendations

Recommendations

- If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:
  1. Go to the *<modeling_tool_installation_directory>/bin*directory and open the *<modeling_tool_name>.properties* file.
  2. Increase the *-Xmx*value, e.g.,*-Xmx4000M*.
  3. Save and close the file.
- Depending on the size of the model you intend to publish, [CONFLUENCE_PAGE title='Memory allocation' space='MD2024xR1'] to your modeling tool:
  - 2 million element model - 24 GB of RAM
  - 1 million element model - 15 GB of RAM
  - 500k element model - 7 GB of RAM

#### TIP: Publishing tips

Publishing tips

- To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to **Options** > **Project Options** and specify the Decimal Places option. The setting is remembered and used for the documents published from the project.
- You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to [CONFLUENCE_PAGE title='Diagram image export' space='MD2024xR1'] .

#### INFO: Project permissions

Project permissions

When you publish a new document with the Administer Resources permission, it inherits [CONFLUENCE_PAGE title='Permissions' space='']. When you update a document, project permissions are not affected.

To publish a Cameo Collaborator document

1. Start your modeling tool and open the server project you want to publish. Publishing from a historical version of a modelYou can publish a Cameo Collaborator document from a historic version of a model as well. However, note that the commenting, editing, and comment import functionalities in such a document will be disabled.
2. In the main menu, select Tools > Cameo Collaborator > Publish .
3. In the **Cameo Collaborator Publisher** dialog, specify the publishing options . [ATTACHMENT filename='cameo_collaborator_publisher_dialog.png']
4. Click the **Publish** button.
5. Wait until you get the message that the document is successfully published. The message about a successfully published document allows you to copy or open the document URL.

Now you can [CONFLUENCE_PAGE title='Opening Cameo Collaborator for Teamwork Cloud' space=''], navigate to the category where the document was published, and [CONFLUENCE_PAGE title='Opening a resource' space=''].

##### Publishing options

The table below explains all the publishing options available in the **Cameo Collaborator Publisher** dialog.

| Publishing option | Description |
| --- | --- |
| Document box | Enter the document name. By default, the document name is the same as the project name. |
| Document type drop-down box | If you want to publish a resource other than a Cameo Collaborator document, select the type of resource you want to publish. Available values are Collaborator (default), OSLC, and 3DEXPERIENCE Systems Traceability.To see this publishing option, click the Options button in the bottom left corner of the Cameo Collaborator Publisher dialog. |
| Category name box | Click next to the box and select the Teamwork Cloud category where the published resource will be stored. |
| Scope box | Click next to the Scope box and select one or several Packages containing the data you want to publish. |
| Template drop-down box | Select one of the predefined document to be used for publishing. If you want to select a , click and select Use Local Template or Use Server Template (depending on where the template is stored)If you update a published document, specify the same template that was used when publishing it the first time. Otherwise, the navigation between comments and commented items will be corrupted. To restore corrupted navigation, update the document again using the initial template. |
| Comments in project check box | Select the check box to save Cameo Collaborator comments inside the project as model elements.If you save Cameo Collaborator comments in the project when updating a document, you will be offered the option to migrate the existing comments from the document to the project. However, you will not be able to migrate the comments from the project back to the document. If you clear the Comments in project check box when updating the document, the comments previously saved in the project will no longer be visible in the document. |
| Enable editing check box | Select the check box to allow .Note that table legends are displayed only in non-editable Cameo Collaborator documents. |
| Enable commenting check box | Select the check box to allow reviewers to create comments in a Cameo Collaborator document.To see this publishing option, click the Options button in the bottom left corner of the Cameo Collaborator Publisher dialog. |
| Update previously published document check box | Select the check box to update the document previously published from this project. After selecting the check box, click the Document drop-down box and select the document you want to update.To see this publishing option, click the Options button in the bottom left corner of the Cameo Collaborator Publisher dialog. |

##### Publishing other types of resources

In addition to Cameo Collaborator documents, Cameo Collaborator for Teamwork Cloud allows you to publish other types of resources - OSLC and **3D**EXPERIENCE Systems Traceability - described in the sections below.

To publish other types of resources

1. Start your modeling tool and open the server project you want to publish.
2. In the main menu, select Tools > Cameo Collaborator > Publish .
3. Click the Options button in the bottom left corner of the Cameo Collaborator Publisher dialog.
4. In the Document type drop-down box, select the type of resource you want to publish: OSLC or 3DEXPERIENCE Systems Traceability .
5. In the Template drop-down box, make sure to select the template depending on which type of resource you want to publish:
  - If you want to publish an OSLC resource, select OSLC .
  - If you want to publish a **3D**EXPERIENCE Systems Traceability resource, select **TRA**. 
 
[IMAGE alt='' src=''] When publishing an OSLC or **3D**EXPERIENCE Systems Traceability resource, other publishing options are specified automatically and cannot be changed.
6. Click the Publish button.
7. Wait until you get the message that the document is successfully published.

###### OSLC resources

Modeling tools with Cameo Data Hub plugin makes it possible to link and share data using Open Services for Lifecycle Collaboration (OSLC) integration. Publishing projects as OSLC resources allows you to seethe OSLC UI previewsof model elements in the environment of a synchronized tool, e.g.,Doors Next Generation.

[IMAGE alt='' src='']

###### An OSLC resource in the Resources application.

###### 3DEXPERIENCE Systems Traceability resources

The Cameo Collaborator for Teamwork Cloud allows you to publish**3D**EXPERIENCE Systems Traceability resources (TRA) - which can be used in the Systems Traceability app on the**3D**EXPERIENCE platform.

[IMAGE alt='' src='']

###### 3DEXPERIENCE Systems Traceability resource in the Resources application.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f3d099ab-99a3-45f2-80fc-b0c197c12d49"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(62,63,64);">Publishing documents from the graphical user interface is the simplest way to present models to </span>stakeholders, sponsors, customers, and engineering teams. Cameo Collaborator documents can be used not only to review model information and provide feedback but also to edit models directly from the web without using a modeling tool.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="61942541-1e20-48ba-86a6-a6971994dce5"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Installing Cameo Collaborator Publisher plugin" /><ac:plain-text-link-body><![CDATA[The Cameo Collaborator Publisher plugin must be installed in your modeling tool]]></ac:plain-text-link-body></ac:link>.</li><li>Cameo Collaborator for Teamwork Cloud works only with Teamwork Cloud projects. If you want to publish a local model, <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Adding projects to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[add it to Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</li><li>You must have the <ac:link><ri:page ri:content-title="Roles and permissions" /><ac:plain-text-link-body><![CDATA[user permissions]]></ac:plain-text-link-body></ac:link> necessary for document publishing.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="174b72be-2c84-421a-87ac-d4a5e8905adf"><ac:parameter ac:name="title">Recommendations</ac:parameter><ac:rich-text-body><ul><li>If you intend to publish a large model, increase the default JVM heap size of the Cameo Collaborator Publisher plugin as follows:<ol><li><p>Go to the <em><span style="color: rgb(0,0,0);">&lt;modeling_tool_installa</span><span style="color: rgb(0,0,0);">tion_</span><span style="color: rgb(0,0,0);">directory&gt;/bin </span></em>directory and open the <em>&lt;modeling_tool_name&gt;.properties</em> file.</p></li><li><p>Increase the <em>-Xmx</em><span style="color: rgb(0,0,0);"> value, e.g., </span><em>-Xmx4000M</em>.</p></li><li><p>Save and close the file.</p></li></ol></li><li>Depending on the size of the model you intend to publish, <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Memory allocation" /><ac:plain-text-link-body><![CDATA[allocate a sufficient amount of memory]]></ac:plain-text-link-body></ac:link> to your modeling tool:<ul><li><p>2 million element model - 24 GB of RAM</p></li><li><p>1 million element model - 15 GB of RAM</p></li><li><p>500k element model - 7 GB of RAM</p></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="fb8c52e5-ffb0-485e-bec1-a6c3149cbf73"><ac:parameter ac:name="title">Publishing tips</ac:parameter><ac:rich-text-body><ul><li><span>To change the number of decimals displayed in Cameo Collaborator documents, in the main menu, go to <strong>Options</strong> &gt; <strong>Project Options</strong> and specify the </span><strong>Decimal Places</strong><span> option. The setting is remembered and used for the documents published from the project.</span></li><li>You can specify the diagram export options, such as dimensions and building time (the latter applies only to tables and matrices). To learn more, refer to <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5e5fa403-8733-41b3-bfbf-8611500a852b"><ac:parameter ac:name="title">Project permissions</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);">When you publish a new document with the Administer Resources permission</span>, it inherits <ac:link><ri:page ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud project permissions]]></ac:plain-text-link-body></ac:link>. When you update a document, project permissions are not affected.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To publish a Cameo Collaborator document</p><hr /><ol><li><p class="auto-cursor-target">Start your modeling tool and open the server project you want to publish.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cc17fc6d-b5ec-4b8e-9fcd-9ce9301afa81"><ac:parameter ac:name="title">Publishing from a historical version of a model</ac:parameter><ac:rich-text-body><p>You can publish a Cameo Collaborator document from a historic version of a model as well. However, note that the commenting, editing, and comment import functionalities in such a document will be disabled.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>In the main menu, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Publish</strong>.</li><li><ac:link ac:anchor="Publishing options"><ac:link-body>In the <strong>Cameo Collaborator Publisher</strong> dialog, specify the publishing options</ac:link-body></ac:link>.<br /><br /><ac:image><ri:attachment ri:filename="cameo_collaborator_publisher_dialog.png" /></ac:image></li><li><p>Click the <strong>Publish</strong> button.</p></li><li><p>Wait until you get the message that the document is successfully published.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="76e8edbf-a07c-411e-a234-b883e72be7fd"><ac:rich-text-body><p>The message about a successfully published document allows you to copy or open the document URL.</p></ac:rich-text-body></ac:structured-macro></li></ol><p><br />Now you can <ac:link><ri:page ri:content-title="Opening Cameo Collaborator for Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[go to the Resources application]]></ac:plain-text-link-body></ac:link>, navigate to the category where the document was published, and <ac:link><ri:page ri:content-title="Opening a resource" /><ac:plain-text-link-body><![CDATA[open the document]]></ac:plain-text-link-body></ac:link>.</p><h3>Publishing options</h3><p>The table below explains all the publishing options available in the <strong>Cameo Collaborator Publisher</strong> dialog.</p><table class="relative-table wrapped" style="width: 90.6747%;"><colgroup><col style="width: 20.8178%;" /><col style="width: 79.1822%;" /></colgroup><tbody><tr><th scope="col">Publishing option</th><th scope="col">Description</th></tr><tr><td><strong>Document</strong> box</td><td>Enter the document name. By default, the document name is the same as the project name.</td></tr><tr><td><strong>Document type</strong> drop-down box</td><td><div class="content-wrapper"><p>If you want to publish a resource other than a Cameo Collaborator document, select the type of resource you want to publish. Available values are <strong>Collaborator</strong> (default), <strong>OSLC</strong>, and <strong>3DEXPERIENCE Systems Traceability</strong>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="21cd60b6-816e-46bb-b0dd-1a1a5310de2b"><ac:rich-text-body><p>To see this publishing option, click the <strong>Options</strong> button in the bottom left corner of the <strong>Cameo Collaborator Publisher</strong> dialog.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Category name</strong> box</td><td><div class="content-wrapper"><p>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="select_button.png" /></ac:image> next to the box and select the Teamwork Cloud category where the published resource will be stored.</p></div></td></tr><tr><td><strong>Scope</strong> box</td><td><div class="content-wrapper"><p>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="select_button.png" /></ac:image> next to the <strong>Scope</strong> box and select one or several Packages containing the data you want to publish.</p></div></td></tr><tr><td><strong>Template</strong> drop-down box</td><td><div class="content-wrapper"><p>Select one of the predefined document <ac:link><ri:page ri:content-title="Document templates" /><ac:plain-text-link-body><![CDATA[templates]]></ac:plain-text-link-body></ac:link> to be used for publishing. If you want to select a <ac:link><ri:page ri:content-title="Working with custom document templates" /><ac:plain-text-link-body><![CDATA[custom template]]></ac:plain-text-link-body></ac:link>, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="select_button.png" /></ac:image> and select <strong>Use Local Template</strong> or <strong>Use Server Template</strong> (depending on where the template is stored)</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cdc2d630-342f-4417-8b48-e5015be40ae5"><ac:parameter ac:name="title" /><ac:rich-text-body><p>If you update a published document, specify the same template that was used when publishing it the first time. Otherwise, the navigation between comments and commented items will be corrupted. To restore corrupted navigation, update the document again using the initial template.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Comments in project</strong> check box</td><td><div class="content-wrapper"><p>Select the check box to save Cameo Collaborator comments inside the project as model elements.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="d95f84f2-c114-4a84-b74c-7133c5b22ff6"><ac:rich-text-body><p><span style="color: rgb(55,65,81);">If you save Cameo Collaborator comments in the project when updating a document, you will be offered the option to migrate the existing comments from the document to the project. However, you will not be able to migrate the comments from the project back to the document. If you clear the <strong>Comments in project</strong> check box when updating the document, the comments previously saved in the project will no longer be visible in the document.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Enable editing</strong> check box</td><td><div class="content-wrapper"><p>Select the check box to allow <ac:link><ri:page ri:content-title="Editing and contextualizing" /><ac:plain-text-link-body><![CDATA[editing of the model from a Cameo Collaborator document]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="68434628-e4ca-4ba8-bebd-b955219850a9"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">Note that table legends are displayed only in non-editable Cameo Collaborator documents.</span></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>Enable commenting</strong> check box</td><td><div class="content-wrapper"><p>Select the check box to allow reviewers to create comments in a Cameo Collaborator document.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a41b395e-ca10-4745-af9e-6978a24a539c"><ac:rich-text-body><p>To see this publishing option, click the <strong>Options</strong> button in the bottom left corner of the <strong>Cameo Collaborator Publisher</strong> dialog.</p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr><td><strong>Update previously published document</strong> check box</td><td><div class="content-wrapper"><p>Select the check box to update the document previously published from this project. After selecting the check box, click the <strong>Document</strong> drop-down box and select the document you want to update.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d0dacffe-ba22-41d8-9611-43ff383a408a"><ac:rich-text-body><p>To see this publishing option, click the <strong>Options</strong> button in the bottom left corner of the <strong>Cameo Collaborator Publisher</strong> dialog.</p></ac:rich-text-body></ac:structured-macro></div></td></tr></tbody></table><p><br /></p><h3>Publishing other types of resources</h3><p>In addition to Cameo Collaborator documents, Cameo Collaborator for Teamwork Cloud allows you to publish other types of resources - OSLC and <strong>3D</strong>EXPERIENCE Systems Traceability - described in the sections below.</p><p><br /></p><p>To publish other types of resources</p><hr /><ol><li><p class="auto-cursor-target">Start your modeling tool and open the server project you want to publish.</p></li><li>In the main menu, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Publish</strong>.</li><li>Click the <strong>Options</strong> button in the bottom left corner of the <strong>Cameo Collaborator Publisher</strong> dialog.</li><li>In the <strong>Document type</strong> drop-down box, select the type of resource you want to publish: <strong>OSLC</strong> or <strong>3DEXPERIENCE Systems Traceability</strong>.</li><li>In the <strong>Template</strong> drop-down box, make sure to select the template depending on which type of resource you want to publish:<ul><li>If you want to publish an OSLC resource, select <strong>OSLC</strong>.</li><li><p>If you want to publish a <strong>3D</strong>EXPERIENCE Systems Traceability resource, select <strong>TRA</strong>.<br /><br /><ac:image><ri:attachment ri:filename="publishing_tra.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e89c227e-2ea3-4cd9-98d5-c44a252d1eb4"><ac:rich-text-body><p>When publishing an OSLC or <strong>3D</strong>EXPERIENCE Systems Traceability resource, other publishing options are specified automatically and cannot be changed. </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li><li>Click the <strong>Publish</strong> button.</li><li>Wait until you get the message that the document is successfully published.</li></ol><h4>OSLC resources</h4><p><span style="color: rgb(62,63,64);">Modeling tools with Cameo Data Hub plugin makes it possible to link and share data using Open Services for Lifecycle Collaboration (OSLC) integration. Publishing projects as OSLC resources allows you to see </span>the OSLC UI previews<span style="color: rgb(62,63,64);"> of model elements in the environment of a synchronized tool, e.g., </span><span style="color: rgb(62,63,64);">Doors Next Generation.</span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="oslc.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">An OSLC resource in the Resources application.</span></h6><h4>3DEXPERIENCE Systems Traceability resources</h4><p><span style="color: rgb(62,63,64);"><span style="color: rgb(55,65,81);">The Cameo Collaborator for Teamwork Cloud allows you to publish </span><strong>3D</strong><span style="color: rgb(55,65,81);">EXPERIENCE Systems Traceability resources (TRA) - which can be used in the Systems Traceability app on the </span><strong>3D</strong><span style="color: rgb(55,65,81);">EXPERIENCE platform.</span></span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"><span style="color: rgb(55,65,81);"><ac:image><ri:attachment ri:filename="tra.png" /></ac:image></span></span></p><h6 style="text-align: center;"><span style="color: rgb(122,134,154);">3DEXPERIENCE Systems Traceability resource in the Resources application.</span></h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180623 space=TWCloud2024xR1 version=2 -->
## PAGE 00195: Reacting to feedback

- page_id: `171180623`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180623/Reacting+to+feedback
- version_number: 2
- version_date: `2025-10-31T12:35:44.446+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ["reacting-to-reviewer's-comments", 'unrestored-unknown-attachment']

### NORMALIZED CONTENT

After a reviewer informs you that he/she has completed reviewing a published model, you can react to the feedback by replying to their comments and updating the model.

[IMAGE alt='' src='']

###### Reacting to feedback is the last step in the workflow for reviewing models and providing feedback.

To react to a reviewer's feedback

1. [CONFLUENCE_PAGE title='Opening Cameo Collaborator for Teamwork Cloud' space=''] that has been reviewed.
2. In the app bar click [IMAGE alt='' src=''] to open the [CONFLUENCE_PAGE title='Comments pane' space='']. Working with commentsIf there are new comments in the document, the comments pane icon changes to [IMAGE alt='' src=''].New comments are displayed in bold.To view only unresolved and/or high priority comments, click the comment search box on the comments pane and select the **Unresolved** and/or **High priority** check boxes.Use the comment search box on the comments pane to [CONFLUENCE_PAGE title='Comments pane' space=''] by comment name, text, or author.
3. Read the comments you need to respond to and do the following:
  1. Click a comment to navigate to the commented item on the [CONFLUENCE_PAGE title='Content pane' space=''] . The commented item is also selected in the [CONFLUENCE_PAGE title='Navigation pane' space=''] .
  2. If needed, fix the appropriate part of the model in your modeling tool. To open a commented item in a modeling tool, find the **Open in Model Editor** property of the item you want to open and click its value.
  3. Reply to comments to notify the author of model changes or ask for more information.
4. If you have updated the model, [CONFLUENCE_PAGE title='Publishing documents' space=''] it.
5. Inform the reviewer that the document is ready for another round of review.

#### NOTE: Documents published from synchronized projects

Documents published from synchronized projects

If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After a reviewer informs you that he/she has completed reviewing a published model, you can react to the feedback by replying to their comments and updating the model.</p><p><ac:inline-comment-marker ac:ref="d63a9bf4-938f-4880-b18f-783c6a914f30"> </ac:inline-comment-marker></p><p style="text-align: center;"><ac:inline-comment-marker ac:ref="d63a9bf4-938f-4880-b18f-783c6a914f30"><ac:image><ri:attachment ri:filename="main_workflow_reacting.png" /></ac:image></ac:inline-comment-marker></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Reacting to feedback is the last step in the workflow for reviewing models and providing feedback.</h6><p><br /></p><p>To react to a reviewer's feedback</p><hr style="" /><ol><li><ac:link><ri:page ri:content-title="Opening Cameo Collaborator for Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator document]]></ac:plain-text-link-body></ac:link> that has been reviewed.</li><li><p>In the app bar click <ac:image><ri:attachment ri:filename="show-hide_comments_pane.png" /></ac:image> to open the <ac:link><ri:page ri:content-title="Comments pane" /><ac:plain-text-link-body><![CDATA[comments pane]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ff5584d7-6983-4d71-89e1-1ebae5566da8"><ac:parameter ac:name="title">Working with comments</ac:parameter><ac:rich-text-body><ul><li>If there are new comments in the document, the comments pane icon changes to <ac:image ac:thumbnail="true" ac:height="26"><ri:attachment ri:filename="new_comments_notification.png" /></ac:image>.</li><li>New comments are displayed in bold.</li><li>To view only unresolved and/or high priority comments, click the comment search box on the comments pane and select the <strong><ac:inline-comment-marker ac:ref="0b6f15f7-c7d1-471c-aaa1-e1b63d43c0db">Unresolved</ac:inline-comment-marker></strong> and/or <strong>High priority</strong> check boxes.</li><li>Use the comment search box on the comments pane to <ac:link ac:anchor="Searching in comments"><ri:page ri:content-title="Comments pane" /><ac:plain-text-link-body><![CDATA[search for comments]]></ac:plain-text-link-body></ac:link> by comment name, text, or author.</li></ul></ac:rich-text-body></ac:structured-macro></li><li>Read the comments you need to respond to and do the following:<br /><ol><li>Click a comment to navigate to the commented item on the <ac:link><ri:page ri:content-title="Content pane" /><ac:plain-text-link-body><![CDATA[content pane]]></ac:plain-text-link-body></ac:link>. The commented item is also selected in the <ac:link><ri:page ri:content-title="Navigation pane" /><ac:plain-text-link-body><![CDATA[navigation pane]]></ac:plain-text-link-body></ac:link>.</li><li><p class="auto-cursor-target">If needed, fix the appropriate part of the model in your modeling tool. To open a commented item in a modeling tool, find the <strong>Open in Model Editor</strong> property of the item you want to open and click its value.</p></li><li>Reply to comments to notify the author of model changes or ask for more information.</li></ol></li><li>If you have updated the model, <ac:link><ri:page ri:content-title="Publishing documents" /><ac:plain-text-link-body><![CDATA[republish]]></ac:plain-text-link-body></ac:link> it.</li><li>Inform the reviewer that the document is ready for another round of review.</li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d4b9e3df-df5e-4c01-a067-cd699751e701"><ac:parameter ac:name="title">Documents published from synchronized projects</ac:parameter><ac:rich-text-body><p>If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. <ac:link><ri:page ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170491694 space=TWCloud2024xR1 version=4 -->
## PAGE 00196: Releasing locked elements

- page_id: `170491694`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491694/Releasing+locked+elements
- version_number: 4
- version_date: `2025-03-24T10:07:25.696+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing users > Managing users details
- labels: []

### NORMALIZED CONTENT

A user can [CONFLUENCE_PAGE title='Locking model for edit' space='MD2024xR1'] in several different projects. The Users application allows you to unlock all the elements locked by a specific user.

You can use the Resources application to [CONFLUENCE_PAGE title='Unlocking resource elements' space='TWCloud2024xR1'].

#### NOTE: Prerequisites

Prerequisites

To release locked elements, you must have the Resource Locks Administrator role (or the Read Resources and Release Resource Locks permissions) for the resources you want to unlock. [CONFLUENCE_PAGE title='Permissions' space='TWCloud2024xR1'].

To release locked elements

1. Navigate to the Users application and do one of the following:
  - Click [IMAGE alt='' src=''] next to a user and select Release locked elements .
  - Click a user and in the**User**pane, click**[IMAGE alt='' src='']**and select**Release locked elements**.
2. In the **Release locked elements** pane, select the elements you want to unlock. You can use a locked element filter to search for elements according to the resource or branch name.
3. Click the **Unlock**button. If a project is locked in different branches, releasing lock(s) on a branch will not release other locks in the other branches.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">A user can <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[lock elements for editing]]></ac:plain-text-link-body></ac:link> in several different projects. The Users application allows you to unlock all the elements locked by a specific user.</span></p><p><span style="color: rgb(62,63,64);">You can use the Resources application to <span style="color: rgb(23,43,77);"><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Unlocking resource elements" /><ac:plain-text-link-body><![CDATA[unlock the elements of a specific project locked by several different users]]></ac:plain-text-link-body></ac:link>.</span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ac674c0d-a573-42db-a380-800552bf59bf"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To release locked elements, you must have the Resource Locks Administrator role (or the Read Resources and Release Resource Locks permissions) for the resources you want to unlock. <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[Learn more about roles and their permissions]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To release locked elements</p><hr /><ol><li>Navigate to the Users application and do one of the following: <ul><li>Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span> next to a user and select<strong> Release locked </strong><strong>elements</strong>.</li><li><p class="auto-cursor-target">Click a user and in the<strong> User </strong>pane, click<strong> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span> </strong>and select<strong> Release locked elements</strong>.</p></li></ul></li><li><p>In the <strong>Release locked elements</strong> pane, select the elements you want to unlock. </p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="3d54a58e-7d99-47b6-b3ae-79157454631e"><ac:rich-text-body><p>You can use a locked element filter to search for elements according to the resource or branch name.</p></ac:rich-text-body></ac:structured-macro></li><li><p>Click the <strong>Unlock </strong>button.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="223ff402-4cf0-4b8e-b990-714055aa9d63"><ac:rich-text-body><p class="title">If a project is locked in different branches, releasing lock(s) on a branch will not release other locks in the other branches.</p></ac:rich-text-body></ac:structured-macro></li></ol>
````

<!--NOMAGIC_PAGE id=171180041 space=TWCloud2024xR1 version=1 -->
## PAGE 00197: Removing custom roles

- page_id: `171180041`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180041/Removing+custom+roles
- version_number: 1
- version_date: `2023-07-07T08:50:49.409+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application > Managing roles
- labels: []

### NORMALIZED CONTENT

You can remove custom roles from Teamwork Cloud Admin through the **Role**application. If you remove a custom role, the user/group with that role will be unable to use the permissions associated with it to work on any resource. The changes will only be effective once the user refreshes the page or tries to do any action.

To remove a custom role

1. In the Roles application, do one of the following:
  - Click a role. The Role pane opens. Click the Remove button.
  - Select a role and click [ATTACHMENT filename='menu.png'] . From the list select Remove role .
2. A dialog will appear asking if you want to remove the role. Click Remove . The role will be removed from the Teamwork Cloud system.

Preexisting roles cannot be removed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can remove custom roles from Teamwork Cloud Admin through the <strong>Role </strong>application. If you remove a custom role, the user/group with that role will be unable to use the permissions associated with it to work on any resource. <ac:inline-comment-marker ac:ref="80f7b4a6-6d39-4d88-8cd4-31835ea6822e">The changes will only be effective once the user refreshes the page or tries to do any action.</ac:inline-comment-marker> </p><p><br /></p><p>To remove a custom role</p><hr /><ol><li>In the <strong style="line-height: 1.42857;">Roles </strong>application, do one of the following: <ul><li>Click a role. The <strong>Role</strong> pane opens. Click the <strong>Remove </strong>button.</li><li>Select a role and click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using the app bar" /></ri:attachment></ac:image>. From the list select <strong>Remove role</strong>. </li></ul></li><li>A dialog will appear asking if you want to remove the role. Click <strong>Remove</strong>. The role will be removed <ac:inline-comment-marker ac:ref="e330e782-72ca-4fbe-86d8-4246f5eab919">from the Teamwork Cloud system.</ac:inline-comment-marker></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7ebf3dc9-ae71-45ad-8227-7e28b8d12396"><ac:rich-text-body><p>Preexisting roles cannot be removed.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180284 space=TWCloud2024xR1 version=1 -->
## PAGE 00198: Removing resources

- page_id: `171180284`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180284/Removing+resources
- version_number: 1
- version_date: `2024-01-29T10:13:06.612+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application > Working with resources
- labels: []

### NORMALIZED CONTENT

You can remove any type of resource from the Resources app as described below.

To remove a resource

1. Open the Resources app and go the category where the relevant resource is located.
2. Click [ATTACHMENT filename='menu.png'] next to the resource you want to remove.
3. From the menu, select Remove resource .
4. When you get the message asking if you want to remove the resource, click Remove .

When you get a confirmation message, it means the resource is successfully removed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can remove any type of resource from the Resources app as described below.</p><p><br /></p><p>To remove a resource</p><hr /><ol><li>Open the Resources app and go the category where the relevant resource is located.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Removing resources" /></ri:attachment></ac:image> next to the resource you want to remove.</li><li>From the menu, select <strong>Remove resource</strong>.</li><li>When you get the message asking if you want to remove the resource, click <strong>Remove</strong>.</li></ol><p><br />When you get a confirmation message, it means the resource is successfully removed.</p>
````

<!--NOMAGIC_PAGE id=170491726 space=TWCloud2024xR1 version=1 -->
## PAGE 00199: Removing roles and assignments

- page_id: `170491726`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491726/Removing+roles+and+assignments
- version_number: 1
- version_date: `2023-07-07T08:50:43.948+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing users > Managing user roles and assignments
- labels: []

### NORMALIZED CONTENT

To remove a role

1. On the Users application , click the usern ame you want to assign a role to. The User pane will open.
2. Go to the Roles card, and click Change button. The Change roles pane opens.
3. For a predefined role: click the **Save** button to save the changes.

To remove an assignment

1. On the Users application , click the username you want to assign a role to. The User pane will open.
2. Go to the Roles card, and click Change button. The Change roles pane opens.
3. For a predefined role: click the **Save** button to save the changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To remove a role</p><hr /><ol><li>On the <strong>Users applicatio<ac:inline-comment-marker ac:ref="2362b109-53c5-4db3-a3ad-830d20422bd6">n</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="2362b109-53c5-4db3-a3ad-830d20422bd6">, click the usern</ac:inline-comment-marker>ame you want to assign a role to. The <strong>User </strong>pane will open.</li><li>Go to the <strong>Roles</strong> card, and click <strong>Change</strong> button. The <strong>Change roles</strong> pane opens. </li><li><p class="auto-cursor-target">For a predefined role: click the <strong style="letter-spacing: 0.0px;">Save</strong> button to save the changes. </p></li></ol><p><br /></p><p>To remove an assignment</p><hr /><ol><li>On the <strong>Users application</strong>, click the username you want to assign a role to. The <strong>User </strong>pane will open.</li><li>Go to the <strong>Roles</strong> card, and click <strong>Change</strong> button. The <strong>Change roles</strong> pane opens. </li><li><p class="auto-cursor-target">For a predefined role: click the <strong>Save</strong> button to save the changes. </p></li></ol>
````

<!--NOMAGIC_PAGE id=170491754 space=TWCloud2024xR1 version=1 -->
## PAGE 00200: Removing users from user groups

- page_id: `170491754`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491754/Removing+users+from+user+groups
- version_number: 1
- version_date: `2023-09-27T14:34:03.755+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing user groups
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

You can remove users from user groups in the Users application. After removing a user from a user group, they loose all permissions of the roles assigned to that user group.

To remove a user from a user group

1. Go to the Users application and select User groups in the user/user group filter on the left side of the screen.
2. In the content pane, select the user group you want to remove a user from.
3. When the User group pane opens, click the change button in the Group members card. [ATTACHMENT filename='changing_user_group_members.png']
4. When the **Change group members** pane opens, click [IMAGE alt='' src=''] next to the name of the user you want to remove. Finding usersIf the group has a lot of users, select the **Search member** radio button and type the user name in the search bar to find the user you need. [IMAGE alt='' src='']
5. Click [ATTACHMENT filename='save_roles.png'] to save the changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can remove users from user groups in the Users application. After removing a user from a user group, they loose all permissions of the roles assigned to that user group.</p><p><br /></p><p>To remove a user from a user group</p><hr /><ol><li>Go to the Users application and select <strong>User groups</strong> in the user/user group filter on the left side of the screen.</li><li>In the content pane, select the user group you want to remove a user from.</li><li>When the <strong>User group</strong> pane opens, click the change button in the <strong>Group members</strong> card.<br /><br /><ac:image><ri:attachment ri:filename="changing_user_group_members.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Removing users from user groups" /></ri:attachment></ac:image><br /><br /></li><li><p class="auto-cursor-target">When the <strong>Change group members</strong> pane opens, click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="delete_icon.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Removing users from user groups" /></ri:attachment></ac:image> next to the name of the user you want to remove.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0e578489-5baa-4975-8325-be7b6c88106b"><ac:parameter ac:name="title">Finding users</ac:parameter><ac:rich-text-body><p>If the group has a lot of users, select the <strong>Search member</strong> radio button and type the user name in the search bar to find the user you need.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="removing_user_from_user_group.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Removing users from user groups" /></ri:attachment></ac:image><br /><br /></p></li><li>Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_roles.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Removing users from user groups" /></ri:attachment></ac:image> to save the changes.</li></ol>
````

<!--NOMAGIC_PAGE id=171180535 space=TWCloud2024xR1 version=3 -->
## PAGE 00201: Replying to a comment

- page_id: `171180535`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180535/Replying+to+a+comment
- version_number: 3
- version_date: `2025-10-31T12:31:24.770+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in a modeling tool
- labels: []

### NORMALIZED CONTENT

**On this page**

4

You can react to reviewer's feedback by replying to his/her comments right from the modeling tool.

To reply to a comment

1. In a modeling tool, open the model related to the Cameo Collaborator for Teamwork Cloud document with comments you want to reply to.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space=''] .
3. In the comments panel, find the comment you want to reply to and click [IMAGE alt='' src=''] on the right side of the comment to show available actions.
4. Click [IMAGE alt='' src=''] on the bottom of the comment. The **Reply** pane (displayed below) opens. 
 
[IMAGE alt='' src='']
5. Enter your reply in the appropriate box (highlighted above).
6. Click [IMAGE alt='' src=''] on the top right corner of the pane to save the reply.

##### Discarding comment replies

If you started writing a reply to a comment but do not want to save it, you can discard the reply.

To discard a comment reply

- Click [ATTACHMENT filename='cancel_comment.png'] on the top left corner of the Reply pane.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="558c4a25-5530-4a3b-bb7d-bd9e71672370"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>You can react to reviewer's feedback by replying to his/her comments right from the modeling tool.</p><p><br /></p><p>To reply to a comment</p><hr /><ol><li><p>In a modeling tool, open the model related to the Cameo Collaborator for Teamwork Cloud document with comments you want to reply to.</p></li><li><ac:link><ri:page ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator comments panel]]></ac:plain-text-link-body></ac:link>.</li><li><p>In the comments panel, find the comment you want to reply to and click <ac:image><ri:attachment ri:filename="expand.png" /></ac:image> on the right side of the comment to show available actions.</p></li><li><p>Click <ac:image><ri:attachment ri:filename="reply.png" /></ac:image> on the bottom of the comment. The <strong>Reply</strong> pane (displayed below) opens.<br /><br /><ac:image><ri:attachment ri:filename="reply_pane.png" /></ac:image><br /><br /></p></li><li>Enter your reply in the appropriate box (highlighted above).</li><li><p>Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save.png" /></ac:image> on the top right corner of the pane to save the reply.</p></li></ol><h3 style="color:var(--ds-text,#172b4d);"><br />Discarding comment replies</h3><p>If you started writing a reply to a comment but do not want to save it, you can discard the reply.</p><p><br /></p><p>To discard a comment reply</p><hr /><ul><li>Click <ac:image><ri:attachment ri:filename="cancel_comment.png" /></ac:image> on the top left corner of the <strong>Reply</strong> pane.</li></ul><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180600 space=TWCloud2024xR1 version=2 -->
## PAGE 00202: Replying to comments

- page_id: `171180600`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180600/Replying+to+comments
- version_number: 2
- version_date: `2025-10-31T12:34:21.465+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in Cameo Collaborator
- labels: ['reply-to-a-textual-comment', 'reply-to-a-comment', 'reply-to-comments']

### NORMALIZED CONTENT

**On this page**

4

You can react to reviewer's feedback by replying to his/her comments.

To reply to a comment

1. In the [CONFLUENCE_PAGE title='Comments pane' space=''], find the comment you want to reply to.
2. Click [IMAGE alt='' src=''] on the right side of the comment to show available actions.
3. Click [IMAGE alt='' src=''] on the bottom of the comment. The **Reply** pane (displayed below) opens. 
 
[IMAGE alt='' src='']
4. Enter your reply in the appropriate box (highlighted above).
5. Click [IMAGE alt='' src=''] on the top right corner of the pane to save the reply.

##### Discarding comment replies

If you started writing a reply to a comment but do not want to save it, you can discard the reply.

To discard a comment reply

- Click [ATTACHMENT filename='cancel_comment.png'] on the top left corner of the Reply pane.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="434efdc0-eb86-45ad-810c-e94a570ca5ad"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>You can react to reviewer's feedback by replying to his/her comments.</p><p><br /></p><p><ac:inline-comment-marker ac:ref="3e258bf4-be79-4e26-a23b-e674f0f33137">To reply to a comment</ac:inline-comment-marker></p><hr style="" /><ol><li><p>In the <ac:link><ri:page ri:content-title="Comments pane" /><ac:plain-text-link-body><![CDATA[comments pane]]></ac:plain-text-link-body></ac:link>, find the comment you want to reply to.</p></li><li><p>Click <ac:image><ri:attachment ri:filename="expand.png" /></ac:image> on the right side of the comment to show available actions.</p></li><li><p>Click <ac:image><ri:attachment ri:filename="reply.png" /></ac:image> on the bottom of the comment. The <strong>Reply</strong> pane (displayed below) opens.<br /><br /><ac:image><ri:attachment ri:filename="reply_pane.png" /></ac:image><br /><br /></p></li><li>Enter your reply in the appropriate box (highlighted above).</li><li><p>Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save.png" /></ac:image> on the top right corner of the pane to save the reply.</p></li></ol><h3 style="color:var(--ds-text,#172b4d);"><br />Discarding comment replies</h3><p>If you started writing a reply to a comment but do not want to save it, you can discard the reply.</p><p><br /></p><p>To discard a comment reply</p><hr style="" /><ul><li>Click <ac:image><ri:attachment ri:filename="cancel_comment.png" /></ac:image> on the top left corner of the <strong>Reply</strong> pane.</li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180357 space=TWCloud2024xR1 version=2 -->
## PAGE 00203: Reports application

- page_id: `171180357`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180357/Reports+application
- version_number: 2
- version_date: `2025-05-19T11:29:57.506+02:00`
- ancestors: Teamwork Cloud and Services > User Guide
- labels: []

### NORMALIZED CONTENT

The Reports application provides better insights into what’s happening with your Teamwork Cloud data. With just a few clicks, you can generate audit-oriented, exportable reports on user, resource activity, permission changes, and much more. You can alsotrack, record, and export information related to Teamwork Cloud usageand other general information to Excel or CSV formats.

To access the Reports application, you need the [CONFLUENCE_PAGE title='Types of roles' space=''].

- [CONFLUENCE_PAGE title='Accessing the Reports application' space='']
- [CONFLUENCE_PAGE title='Available report types' space='']
- [CONFLUENCE_PAGE title='Generating a report' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);"><span>The Reports application provides <span style="color: rgb(62,63,64);">better insights into what’s happening with your Teamwork Cloud data</span>. With just a few clicks, you can generate audit-oriented, exportable reports on user, resource activity, permission changes, and much more. You can also </span></span><span style="color: rgb(62,63,64);">track, record, and export information related to Teamwork Cloud usage </span><span style="color: rgb(14,16,26);">and other general information to Excel or CSV formats.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b50dd1a6-60ba-496a-a493-13a3606341a6"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">To access the Reports application, you need the <ac:link><ri:page ri:content-title="Types of roles" /><ac:plain-text-link-body><![CDATA[Reports Manager role]]></ac:plain-text-link-body></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><ul><li><span style="color: rgb(14,16,26);"><ac:link><ri:page ri:content-title="Accessing the Reports application" /></ac:link></span></li><li><span style="color: rgb(14,16,26);"><ac:link><ri:page ri:content-title="Available report types" /></ac:link><br class="_mce_tagged_br" /></span></li><li><ac:link><ri:page ri:content-title="Generating a report" /></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=170491701 space=TWCloud2024xR1 version=1 -->
## PAGE 00204: Resetting user password

- page_id: `170491701`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491701/Resetting+user+password
- version_number: 1
- version_date: `2023-07-07T08:50:43.390+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application > Managing users > Managing users details
- labels: []

### NORMALIZED CONTENT

Only a**User Manager**can reset another user's password. Therefore, an unauthorized user cannot see the**Reset Password**section on the**User**.Only internal user password can be reset.

To reset password, do one of the following

- Click [IMAGE alt='' src=''] next to the user and from menu select to Reset password .
- Go to User pane click [ATTACHMENT filename='menu.png'] on Account card, Actions menu will open.
  - From menu select **Reset password** , ****Reset password pane will open. Write the new password and click [IMAGE alt='' src=''] .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Only a </span><strong>User Manager</strong><span style="color: rgb(62,63,64);"> can reset another user's password. Therefore, an unauthorized user cannot see the </span><strong>Reset Password</strong><span style="color: rgb(62,63,64);"> section on the </span><strong>User</strong><span style="color: rgb(62,63,64);">. </span><span style="color: rgb(62,63,64);">Only internal user password can be reset.</span></p><p><br /></p><p>To reset password, do one of the following</p><hr /><ul><li>Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"> <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resetting user password" /></ri:attachment></ac:image> </span> next to the user and from menu select to <strong>Reset password</strong>.</li><li>Go to <strong>User</strong> pane click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resetting user password" /></ri:attachment></ac:image> on <strong>Account </strong>card, <strong>Actions</strong> menu will open. <br /><ul><li>From menu select <strong><strong>Reset password</strong></strong>,<strong><strong> </strong>Reset password </strong>pane will open.<strong> </strong>Write the new password and click <strong><ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="Save_button.PNG"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resetting user password" /></ri:attachment></ac:image></strong>.</li></ul></li></ul>
````

<!--NOMAGIC_PAGE id=171180541 space=TWCloud2024xR1 version=1 -->
## PAGE 00205: Resolving a comment

- page_id: `171180541`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180541/Resolving+a+comment
- version_number: 1
- version_date: `2023-07-07T08:51:25.678+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in a modeling tool
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

When you get a reply to your comment and/or the comment is no longer relevant, you can resolve it.

To resolve a comment

1. In a modeling tool, open the model related to the Cameo Collaborator for Teamwork Cloud document with comments you want to resolve.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space='TWCloud2024xR1'].
3. In the comments panel, find the comment you want to resolve.
4. Click [IMAGE alt='' src=''] on the right side of the comment to show available actions.
5. Click [ATTACHMENT filename='resolve.png'] on the bottom of the comment.

You can identify which comments are resolved by their appearance in the comments panel and in diagrams in case of graphical comments.

[IMAGE alt='' src='']

###### In the Cameo Collaborator comments panel, resolved comments are shaded.

[IMAGE alt='' src='']

###### In diagrams, resolved graphical comments are grayed out.

#### TIP: Useful to know

Useful to know

- Resolving a comment also resolves all of its replies.
- You can unresolve the comments that are resolved. To do that, click [ATTACHMENT filename='expand.png'] on the right side of a comment to show available actions, and click [ATTACHMENT filename='unresolve.png'] .
- You can resolve or unresolve individual comment replies without resolving or unresolving the comment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When you get a reply to your comment and/or the comment is no longer relevant, you can resolve it.</p><p><br /></p><p>To resolve a comment</p><hr /><ol><li><p>In a modeling tool, open the model related to the Cameo Collaborator for Teamwork Cloud document with comments you want to resolve.</p></li><li><p><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator comments panel]]></ac:plain-text-link-body></ac:link>.</p></li><li><p>In the comments panel, find the comment you want to resolve.</p></li><li><p>Click <ac:image><ri:attachment ri:filename="expand.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image> on the right side of the comment to show available actions.</p></li><li>Click <ac:image><ri:attachment ri:filename="resolve.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image> on the bottom of the comment.</li></ol><p><br />You can identify which comments are resolved by their appearance in the comments panel and in diagrams in case of graphical comments.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="resolved_comments_on_comments_pane.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image></p><h6 style="text-align: center;">In the Cameo Collaborator comments panel, resolved comments are shaded.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="resolved_graphical_comments.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image></p><h6 style="text-align: center;">In diagrams, resolved graphical comments are grayed out.</h6><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="56fb77d1-bb95-41e6-88f6-2980e3ca8e77"><ac:parameter ac:name="title">Useful to know</ac:parameter><ac:rich-text-body><ul><li>Resolving a comment also resolves all of its replies.</li><li>You can unresolve the comments that are resolved. To do that, click <ac:image><ri:attachment ri:filename="expand.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image> on the right side of a comment to show available actions, and click <ac:image><ri:attachment ri:filename="unresolve.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resolving a comment" /></ri:attachment></ac:image>.</li><li>You can resolve or unresolve individual comment replies without resolving or unresolving the comment.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180606 space=TWCloud2024xR1 version=2 -->
## PAGE 00206: Resolving comments

- page_id: `171180606`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180606/Resolving+comments
- version_number: 2
- version_date: `2025-10-31T12:34:51.557+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments > Working with comments in Cameo Collaborator
- labels: ['resolve-a-comment', 'resolving-comments', 'unrestored-unknown-attachment']

### NORMALIZED CONTENT

When you get a reply to your comment and/or the comment is no longer relevant, you can resolve it.

To resolve a comment

1. On the [CONFLUENCE_PAGE title='Comments pane' space=''], find the comment you want to resolve.
2. Click [IMAGE alt='' src=''] on the right side of the comment to show available actions.
3. Click [ATTACHMENT filename='resolve.png'] on the bottom of the comment.

You can identify which comments are resolved by their appearance both on the comments pane and content pane, as shown bellow.

[IMAGE alt='' src='']

###### On the comments pane, resolved comments are shaded.

[IMAGE alt='' src='']

###### In images, resolved graphical comments are grayed out.

[IMAGE alt='' src='']

###### On the content pane, items with resolved textual comments are highlighted in gray.

#### TIP: Useful to know

Useful to know

- Resolving a comment also resolves all of its replies.
- You can unresolve the comments that are resolved. To do that, click [ATTACHMENT filename='expand.png'] on the right side of a comment to show available actions, and click [ATTACHMENT filename='unresolve.png'] .
- You can resolve or unresolve individual comment replies without resolving or unresolving the comment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When you get a reply to your comment and/or the comment is no longer relevant, you can resolve it.</p><p><br /></p><p><ac:inline-comment-marker ac:ref="b842fe33-ae36-4666-9e8a-5011df165f8d">To resolve a comment</ac:inline-comment-marker></p><hr style="" /><ol><li><p>On the <ac:link><ri:page ri:content-title="Comments pane" /><ac:plain-text-link-body><![CDATA[comments pane]]></ac:plain-text-link-body></ac:link>, find the comment you want to resolve.</p></li><li><p>Click <ac:image><ri:attachment ri:filename="expand.png" /></ac:image> on the right side of the comment to show available actions.</p></li><li>Click <ac:image><ri:attachment ri:filename="resolve.png" /></ac:image> on the bottom of the comment.</li></ol><p><br />You can identify which comments are resolved by their appearance both on the comments pane and content pane, as shown bellow.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="resolved_comments_on_comments_pane.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">On the comments pane, resolved comments are shaded.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="resolved_graphical_comments.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">In images, resolved graphical comments are grayed out.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="items_with_resolved_comments.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">On the content pane, items with resolved textual comments are highlighted in gray.</h6><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="56fb77d1-bb95-41e6-88f6-2980e3ca8e77"><ac:parameter ac:name="title">Useful to know</ac:parameter><ac:rich-text-body><ul><li>Resolving a comment also resolves all of its replies.</li><li>You can unresolve the comments that are resolved. To do that, click <ac:image><ri:attachment ri:filename="expand.png" /></ac:image> on the right side of a comment to show available actions, and click <ac:image><ri:attachment ri:filename="unresolve.png" /></ac:image>.</li><li>You can resolve or unresolve individual comment replies without resolving or unresolving the comment.</li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=171180331 space=TWCloud2024xR1 version=1 -->
## PAGE 00207: Resource Usage Map

- page_id: `171180331`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180331/Resource+Usage+Map
- version_number: 1
- version_date: `2024-04-18T09:11:07.911+02:00`
- ancestors: Teamwork Cloud and Services > User Guide
- labels: []

### NORMALIZED CONTENT

Resource Usage Map allows you to create graphical representations of Teamwork Cloud project usages, analyze dependencies among projects in the Teamwork Cloud repository, and identify potentially problematic usage areas.

In Resource Usage Map you can:

- Create usage maps for one or multiple resources.
- Quickly access the resource usage map of an open project right from a modeling tool.
- Identify three types of suspicious usages: inconsistent version usages, cyclic usages, and unused resources.
- Use filters to choose what types of usages you want to see in a usage map.
- Search for resources in a large usage map and view their details in the Resource pane.

For instructions how to use Resource Usage Map, refer to:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">Resource Usage Map allows you to create graphical representations of Teamwork Cloud project usages, analyze dependencies among projects in the Teamwork Cloud repository, and identify potentially problematic usage areas.</span></p><p><span style="color: rgb(62,63,64);">In Resource Usage Map you can:</span></p><ul><li><span style="color: rgb(62,63,64);">Create usage maps for one or multiple resources.</span></li><li><span style="color: rgb(62,63,64);">Quickly access the resource usage map of an open project right from a modeling tool.</span></li><li><span style="color: rgb(62,63,64);">Identify three types of suspicious usages: inconsistent version usages, cyclic usages, and unused resources.<br /></span></li><li><p>Use filters to choose what types of usages you want to see in a usage map.</p></li><li><p><span style="color: rgb(62,63,64);">Search for resources in a large usage map and view their details in the Resource pane.</span></p></li></ul><p>For instructions how to use Resource Usage Map, refer to:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180332 space=TWCloud2024xR1 version=1 -->
## PAGE 00208: Resource Usage Map application structure

- page_id: `171180332`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180332/Resource+Usage+Map+application+structure
- version_number: 1
- version_date: `2023-07-07T08:51:06.837+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resource Usage Map
- labels: []

### NORMALIZED CONTENT

The Resource Usage Map application allows you to see graphical representation of Teamwork Cloud project usages. You can create usage maps for one or several resources, and have multiple usage maps open simultaneously. It is helpful when you need to compare the usages of different projects and identify potential problem areas, such as cyclic project usages or inconsistent usages of project versions.

The figure below displays the structure of the Resource Usage Map application.

[IMAGE alt='' src='']

###### The components of the Resource Usage Map application.

See following table explains the components of the Resource Usage Map application user interface:

| User interface component | Description |
| --- | --- |
| App bar | is located at the top of the web application portal. You can use it to search for resources by resource name and navigate through different Teamwork Cloud Admin web applications. |
| Content pane | The content pane displays the resource usage map of the selected resources. You can navigate through all the open maps by using the tabs at the top of the content pane. The tab of a current map is green and the tabs of other open maps are grey. |
|  | Click this icon to create a new resource usage map. |
|  | Click this icon to view the resource usage map legend explaining what different resource symbols in the map mean. |
| Filters pane | The Filters pane is located on the left side of the Resource Usage Map application portal. It allows you to choose what types of usages should be displayed in a currently open resource usage map. Select the check-boxes next to the types of usages you want to view and clear the check-boxes next to the types of usages you want to hide.The lower part of the Filters pane displays different types of suspicious usages if they exist. You can expand each type of suspicious usages to see the full list. |
| Resource pane | The Resource pane is located on the right side of the Resource Usage Map application portal. It displays details and usages of the resource selected in the content pane. Here, you can also find all the resources that use the selected resource in the their latest versions. |
| Resource details card | The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource. |
|  | Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource. |
| Used resources card | After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects. |
| Used by resources card | In the Used by resources card, click the Find all usages button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Resource Usage Map application allows you to see graphical representation of Teamwork Cloud project usages. You can create usage maps for one or several resources, and have multiple usage maps open simultaneously. It is helpful when you need to compare the usages of different projects and identify potential problem areas, such as cyclic project usages or inconsistent usages of project versions.</p><p>The figure below displays the structure of the Resource Usage Map application.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="resource_usage_map_structure.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resource Usage Map application structure" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The components of the Resource Usage Map application.</h6><p>See following table explains the components of the Resource Usage Map application user interface:</p><table class="relative-table" style="width: 79.9232%;"><colgroup><col style="width: 13.1868%;" /><col style="width: 86.8132%;" /></colgroup><tbody><tr><th>User interface component</th><th>Description</th></tr><tr><td><strong title="">App bar</strong></td><td><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using the app bar" /><ac:plain-text-link-body><![CDATA[The app bar]]></ac:plain-text-link-body></ac:link> is located at the top of the web application portal. You can use it to search for resources by resource name and navigate through different Teamwork Cloud Admin web applications.</td></tr><tr><td><strong title="">Content pane</strong></td><td><div class="content-wrapper"><p>The content pane displays the resource usage map of the selected resources. You can navigate through all the open maps by using the tabs at the top of the content pane. The tab of a current map is green and the tabs of other open maps are grey.</p></div></td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="create_map.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resource Usage Map application structure" /></ri:attachment></ac:image></p></div></td><td>Click this icon to create a new resource usage map.</td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="map_legend.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resource Usage Map application structure" /></ri:attachment></ac:image></p></div></td><td>Click this icon to view the resource usage map legend explaining what different resource symbols in the map mean.</td></tr><tr><td><strong>Filters pane</strong></td><td><p>The Filters pane is located on the left side of the Resource Usage Map application portal. It allows you to choose what types of usages should be displayed in a currently open resource usage map. Select the check-boxes <span style="color: rgb(62,63,64);">next to the types of usages you want to view and clear the check-boxes next to the types of usages you want to hide.</span></p><p>The lower part of the Filters pane displays different types of suspicious usages if they exist. You can expand each type of suspicious usages to see the full list.</p></td></tr><tr><td colspan="1"><strong>Resource pane</strong></td><td colspan="1">The Resource pane is located on the right side of the Resource Usage Map application portal. It displays details and usages of the resource selected in the content pane. Here, you can also find all the resources that use the selected resource in the their latest versions.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Resource details card</strong></td><td colspan="1">The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource.</td></tr><tr><td style="text-align: left;" colspan="1"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="switch_resource_version.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resource Usage Map application structure" /></ri:attachment></ac:image></strong></p></div></td><td colspan="1">Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used resources card</strong></td><td colspan="1">After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used by resources card</strong></td><td colspan="1">In the Used by resources card, click the <strong>Find all usages</strong> button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are<span> divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects.</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180254 space=TWCloud2024xR1 version=1 -->
## PAGE 00209: Resources application

- page_id: `171180254`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180254/Resources+application
- version_number: 1
- version_date: `2023-07-07T08:51:00.872+02:00`
- ancestors: Teamwork Cloud and Services > User Guide
- labels: []

### NORMALIZED CONTENT

Resources in Teamwork Cloud include projects and documents. Resource Manager and Resource Contributor roles enable users to work on document resources.

One of the goals of Teamwork Cloud is to allow multiple users across different locations to access the same resource (project or document) and work on it concurrently. To accomplish this, you must import files to the server first and then open them on Teamwork Cloud Admin. Resources listed on the Resource application in Teamwork Cloud Admin are either newly created or imported ones. With the resource management capability, you can assign resources to users, monitor progress, edit resource properties, and rename and edit their categories.

You can import a resource to a specific category or import it first and create a category for that project/document later. 
 
Read more about different Resources application capabilities in the articles listed below.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Resources in Teamwork Cloud include projects and documents. <ac:inline-comment-marker ac:ref="b0920ac0-9584-4400-bf0f-c03143f14c9d">Resource</ac:inline-comment-marker> Manager and Resource Contributor roles enable users to work on document resources. </p><p>One of the goals of Teamwork Cloud is to allow multiple users across different locations to access the same resource (project or document) and work on it concurrently. To accomplish this, you must import files to the server first and then open them on Teamwork Cloud Admin. Resources listed on the Resource application in Teamwork Cloud Admin are either newly created or imported ones. With the resource management capability, you can assign resources to users, monitor progress, edit resource properties, and rename and edit their categories.</p><p>You can import a resource to a specific category or import it first and create a category for that project/document later. <br class="atl-forced-newline" /><br class="atl-forced-newline" />Read more about different Resources application capabilities in the articles listed below.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="64dd783e-140b-459e-b468-d627a7854ab6" /></p>
````

<!--NOMAGIC_PAGE id=171180628 space=TWCloud2024xR1 version=2 -->
## PAGE 00210: Reviewing documents and providing feedback

- page_id: `171180628`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180628/Reviewing+documents+and+providing+feedback
- version_number: 2
- version_date: `2025-10-31T12:36:15.316+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['providing-feedback', 'giving-comments', 'drawing-graphics']

### NORMALIZED CONTENT

After an author [CONFLUENCE_PAGE title='Sharing document links' space=''], you can start reviewing the model and give feedback to the author.

[IMAGE alt='' src='']

###### When you are provided with the link to a published model, you can review it and give feedback.

You can provide feedback in a form of textual and graphical comments. [CONFLUENCE_PAGE title='Creating and editing textual comments' space=''] can be written for any element, including its properties displayed on the content pane. [CONFLUENCE_PAGE title='Creating and editing graphical comments' space=''] can be drawn on all images, e.g., diagrams, maps, and matrices.

To review a published model and give feedback

1. [CONFLUENCE_PAGE title='Opening Cameo Collaborator for Teamwork Cloud' space=''] you want to review. Non-public documentsIf the document you are trying to open is not shared publicly and you are directed to the login screen, log in to Teamwork Cloud.
2. Do the following:
  - Review the document, including its structure, element characteristics, and diagrams. NavigatingUse the [CONFLUENCE_PAGE title='Navigation pane' space=''] to navigate to the content you want to review.
  - [CONFLUENCE_PAGE title='Creating and editing textual comments' space=''] for individual items on the [CONFLUENCE_PAGE title='Content pane' space=''] .
  - Draw on diagrams to [CONFLUENCE_PAGE title='Creating and editing graphical comments' space=''] .
  - [CONFLUENCE_PAGE title='Replying to comments' space=''] , if there are other reviewer's or author's comments.
  - [CONFLUENCE_PAGE title='Resolving comments' space=''].
3. When you finish, notify the author so that he/she can [CONFLUENCE_PAGE title='Reacting to feedback' space=''] .

When an author updates a model and/or replies to your comments, you can repeat the cycle shown in the figure above.

#### NOTE: Documents published from synchronized projects

Documents published from synchronized projects

If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>After an author <ac:link><ri:page ri:content-title="Sharing document links" /><ac:plain-text-link-body><![CDATA[shares a published model]]></ac:plain-text-link-body></ac:link>, you can start reviewing the model and give feedback to the author.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="main_workflow_reviewing.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">When you are provided with the link to a published model, you can review it and give feedback.</h6><p>You can provide feedback in a form of textual and graphical comments. <ac:link><ri:page ri:content-title="Creating and editing textual comments" /><ac:plain-text-link-body><![CDATA[Textual comments]]></ac:plain-text-link-body></ac:link> can be written for any element, including its properties displayed on the content pane. <ac:link><ri:page ri:content-title="Creating and editing graphical comments" /><ac:plain-text-link-body><![CDATA[Graphical comments]]></ac:plain-text-link-body></ac:link> can be drawn on all images, e.g., diagrams, maps, and matrices.</p><p><br /></p><p>To review a published model and give feedback</p><hr style="" /><ol><li><p><ac:link><ri:page ri:content-title="Opening Cameo Collaborator for Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator document]]></ac:plain-text-link-body></ac:link> you want to review.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d7438f44-5d54-4784-a188-8bb1731406f1"><ac:parameter ac:name="title">Non-public documents</ac:parameter><ac:rich-text-body><p>If the document you are trying to open is not shared publicly and you are directed to the login screen, log in to Teamwork Cloud.</p></ac:rich-text-body></ac:structured-macro></li><li>Do the following:<ul><li><p class="auto-cursor-target">Review the document, including its structure, element characteristics, and diagrams.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="2141af56-19ef-48ca-aa1b-eb38a3362215"><ac:parameter ac:name="title">Navigating</ac:parameter><ac:rich-text-body><p>Use the <ac:link><ri:page ri:content-title="Navigation pane" /><ac:plain-text-link-body><![CDATA[navigation pane]]></ac:plain-text-link-body></ac:link> to navigate to the content you want to review.</p></ac:rich-text-body></ac:structured-macro></li><li><ac:link><ri:page ri:content-title="Creating and editing textual comments" /><ac:plain-text-link-body><![CDATA[Write textual comments]]></ac:plain-text-link-body></ac:link> for individual items on the <ac:link><ri:page ri:content-title="Content pane" /><ac:plain-text-link-body><![CDATA[content pane]]></ac:plain-text-link-body></ac:link>.</li><li>Draw on diagrams to <ac:link><ri:page ri:content-title="Creating and editing graphical comments" /><ac:plain-text-link-body><![CDATA[give graphical comments]]></ac:plain-text-link-body></ac:link>.</li><li><ac:link><ri:page ri:content-title="Replying to comments" /><ac:plain-text-link-body><![CDATA[Write replies]]></ac:plain-text-link-body></ac:link>, if there are other reviewer's or author's comments.</li><li><p><ac:link><ri:page ri:content-title="Resolving comments" /><ac:plain-text-link-body><![CDATA[Resolve comments]]></ac:plain-text-link-body></ac:link>.</p></li></ul></li><li>When you finish, notify the author so that he/she can <ac:link><ri:page ri:content-title="Reacting to feedback" /><ac:plain-text-link-body><![CDATA[react to your feedback]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br />When an author updates a model and/or replies to your comments, you can repeat the cycle shown in the figure above.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7d97f782-c848-43c7-ba14-ba43dbea8abc"><ac:parameter ac:name="title">Documents published from synchronized projects</ac:parameter><ac:rich-text-body><p>If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. <ac:link><ri:page ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=171180051 space=TWCloud2024xR1 version=2 -->
## PAGE 00211: Role-Based Access Control concept

- page_id: `171180051`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180051/Role-Based+Access+Control+concept
- version_number: 2
- version_date: `2025-10-30T14:35:24.147+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application
- labels: []

### NORMALIZED CONTENT

A major benefit of the Teamwork Cloud system is being able to control how and which user can access the resources in the system. Superior management is essential for large and complex systems in order for a substantial number of users to access the system, and use its resources at the same time. Teamwork Cloud uses role-based access control (RBAC) to regulate permissions and access to its system resources based on the roles of individual users. RBAC is a way to provide quick access, and, at the same time, control the actions a user can perform based on their roles. With RBAC, you can assign general permissions quickly through the use of roles, but you cannot modify the permissions in a pre-existing role. You can also create custom roles for users with particular needs.

Your password and username are associated with your role in the Teamwork Cloud system, meaning that your user account comes with role-specific authorizations. Authorizations are permissions that enable a role or a user to accomplish specific actions. Permissions vary according to the role. For example, some permissions enable a user or a role to:

- Create a user account, assign roles and permissions, and assign resources to each role.
- Modify user information and password.
- Configure the Teamwork Cloud's settings.
- Assign resources to specific users in a particular role.
- Allow and deny user login to Teamwork Cloud Admin.

#### PANEL: What's next?

What's next?

[CONFLUENCE_PAGE title='Case study' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A major benefit of the Teamwork Cloud system is being able to control how and which user can access the resources in the system. Superior management is essential for large and complex systems in order for a substantial number of users to access the system, and use its resources at the same time. Teamwork Cloud uses role-based access control (RBAC) to regulate permissions and access to its system resources based on the roles of individual users. RBAC is a way to provide quick access, and, at the same time, control the actions a user can perform based on their roles. With RBAC, you can assign general permissions quickly through the use of roles, but you cannot modify the permissions in a pre-existing role. You can also create custom roles for users with particular needs.</p><p>Your password and username are associated with your role in the Teamwork Cloud system, meaning that your user account comes with role-specific authorizations. Authorizations are permissions that enable a role or a user to accomplish specific actions. Permissions vary according to the role. For example, some permissions enable a user or a role to:</p><ul><li>Create a user account, assign roles and permissions, and assign resources to each role.</li><li>Modify user information and password. </li><li>Configure the Teamwork Cloud's settings. </li><li>Assign resources to specific users in a particular role. </li><li>Allow and deny user login to Teamwork Cloud Admin. </li></ul><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d8cf9a2a-0ff5-4007-85a6-fec4d6f127a7"><ac:parameter ac:name="title">What's next?</ac:parameter><ac:rich-text-body><p><ac:link><ri:page ri:content-title="Case study" /></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180373 space=TWCloud2024xR1 version=1 -->
## PAGE 00212: Roles and permissions

- page_id: `171180373`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180373/Roles+and+permissions
- version_number: 1
- version_date: `2023-07-07T08:51:28.828+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

To be able to publish documents to Cameo Collaborator for Teamwork Cloud and work with comments in these documents, users need to have roles with certain permissions assigned to them. The table below shows what roles and permissions are required to perform specific actions.

To learn more about Teamwork Cloud roles and permissions, see the following topics:

- [CONFLUENCE_PAGE title='Permissions' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Assigning roles' space='TWCloud2024xR1']

| Actions | Required Teamwork Cloud permissions or roles |
| --- | --- |
| Comments stored in a document |  |
| Read Comments | Read Resources permission or Resource Reviewer role for a document |
| Read comments in a modeling tool | Read Resources permission or Resource Reviewer role for a documentRead Resources permission or Resource Reviewer role for the project from which the document was published |
| Create, edit, reply, resolve, delete comments | Read Resources and Edit Resources permissions or Resource Contributor role for a document |
| Edit, reply, resolve, delete comments in a modeling tool | Read Resources and Edit Resources permissions or Resource Contributor role for a documentRead Resources permission or Resource Reviewer role for the project from which the document was published |
| Publish new documents when Cameo Collaborator template is used in a model | Read Resources permission or Resource Reviewer role for a projectResource Creator role for the category where the document will be published |
| Publish new documents when Cameo Collaborator template is not used in a model | Administer Resources, Edit Resources, Edit Resource Properties and Read Resources Permissions or Resource Manager role for a project with read-write permissions for the project branchResource Creator role for the category where the document will be published |
| Update documents (without changing Cameo Collaborator template) | Read Resources permission or Resource Reviewer role for a projectEdit resources, Edit Resource Properties, Read Resources permissions or Resource Contributor role for the documentResource Creator role for the category where the document is stored |
| Edit a model in Cameo Collaborator | Read Resources permission or Resource Reviewer role for a documentRead Resources and Edit Resources permission or Resource Contributor role for the project with read-write permissions for the project branch |
| Comments stored in a model |  |
| Read comments | Read Resources permission or Resource Reviewer role for a documentRead Resources permission or Resource Reviewer role for the project from which the document was published |
| Create, edit, reply, resolve, delete comments | Read Resources permission or Resource Reviewer role for a documentRead Resources and Edit Resources permissions or Resource Contributor role for the project from which the document was published with read-write permissions for the project branch |
| Publish new documents when Cameo Collaborator template is used in a model | Read Resources permission or Resource Reviewer role for a projectResource Creator role for the category where the document will be published |
| Publish new documents when Cameo Collaborator template is not used in a model | Administer Resources, Edit Resources, Edit Resource Properties and Read Resources Permissions or Resource Manager role for a project with read-write permissions for the project branchResource Creator role for the category where the document will be published |
| Update documents (without changing Cameo Collaborator template) | Read Resources permission or Resource Reviewer role for a projectEdit resources, Edit Resource Properties, Read Resources permissions or Resource Contributor role for the documentResource Creator role for the category where the document is stored |
| Edit a model in Cameo Collaborator | Read Resources permission or Resource Reviewer role for a documentRead Resources and Edit Resources permission or Resource Contributor role for the project with read-write permissions for the project branch |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To be able to publish documents to Cameo Collaborator for Teamwork Cloud and work with comments in these documents, users need to have roles with certain permissions assigned to them. The table below shows what roles and permissions are required to perform specific actions.</p><p>To learn more about Teamwork Cloud roles and permissions, see the following topics:</p><ul><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Permissions" /></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Assigning roles" /></ac:link></li></ul><p><br /></p><table class="relative-table" style="width: 86.2863%;"><colgroup><col style="width: 26.5903%;" /><col style="width: 73.4097%;" /></colgroup><tbody><tr><th style="text-align: center;"><strong>Actions</strong></th><th style="text-align: center;"><strong>Required Teamwork Cloud permissions or roles</strong></th></tr><tr><th style="text-align: center;" colspan="2"><strong>Comments stored in a document</strong></th></tr><tr><td><strong>Read Comments</strong></td><td><ul><li>Read Resources permission or Resource Reviewer role for a document</li></ul></td></tr><tr><td colspan="1"><strong>Read comments in a modeling tool</strong></td><td colspan="1"><ul><li><span>Read Resources permission or Resource Reviewer role for a document</span></li><li><span><span>Read Resources permission or Resource Reviewer role for</span> the project from which the document was published</span></li></ul></td></tr><tr><td><strong>Create, edit, reply, resolve, delete comments</strong></td><td><ul><li>Read Resources and Edit Resources permissions or Resource Contributor role for a document</li></ul></td></tr><tr><td><strong>Edit, reply, resolve, delete comments in a modeling tool</strong></td><td><ul><li><span>Read Resources and Edit Resources permissions or Resource Contributor role for a document</span></li><li>Read Resources permission or Resource Reviewer role for the project from which the document was published<span><br /></span></li></ul></td></tr><tr><td><strong>Publish new documents when Cameo Collaborator template is used in a model</strong></td><td><ul><li>Read Resources permission or Resource Reviewer role for a project</li><li>Resource Creator role for the category where the document will be published</li></ul></td></tr><tr><td><strong>Publish new documents when Cameo Collaborator template is not used in a model</strong></td><td><ul><li>Administer Resources, Edit Resources, Edit Resource Properties and Read Resources Permissions or Resource Manager role for a project <span>with read-write permissions for the project branch</span></li><li>Resource Creator role for the category where the document will be published</li></ul></td></tr><tr><td><strong>Update documents (without changing Cameo Collaborator template)</strong></td><td><ul><li>Read Resources permission or Resource Reviewer role for a project</li><li>Edit resources, Edit Resource Properties, Read Resources permissions or Resource Contributor role for the document</li><li><span>Resource Creator role for the category where the document is stored</span></li></ul></td></tr><tr><td><strong>Edit a model in Cameo Collaborator</strong></td><td><ul><li>Read Resources permission or Resource Reviewer role for a document</li><li>Read Resources and Edit Resources permission or Resource Contributor role for the project with read-write permissions for the project branch</li></ul></td></tr><tr><th style="text-align: center;" colspan="2"><strong>Comments stored in a model</strong></th></tr><tr><td colspan="1"><strong>Read comments</strong></td><td colspan="1"><ul><li>Read Resources permission or Resource Reviewer role for a document</li><li>Read Resources permission or Resource Reviewer role for the project from which the document was published</li></ul></td></tr><tr><td colspan="1"><strong>Create, edit, reply, resolve, delete comments</strong></td><td colspan="1"><ul><li>Read Resources permission or Resource Reviewer role for a document</li><li><span>Read Resources and Edit Resources permissions or Resource Contributor role </span>for the project from which the document was published <span>with read-write permissions for the project branch</span></li></ul></td></tr><tr><td colspan="1"><strong>Publish new documents when Cameo Collaborator template is used in a model</strong></td><td colspan="1"><ul><li>Read Resources permission or Resource Reviewer role for a project</li><li>Resource Creator role for the category where the document will be published</li></ul></td></tr><tr><td colspan="1"><strong>Publish new documents when Cameo Collaborator template is not used in a model</strong></td><td colspan="1"><ul><li>Administer Resources, Edit Resources, Edit Resource Properties and Read Resources Permissions or Resource Manager role for a project <span>with read-write permissions for the project branch</span></li><li>Resource Creator role for the category where the document will be published</li></ul></td></tr><tr><td colspan="1"><strong>Update documents (without changing Cameo Collaborator template)</strong></td><td colspan="1"><ul><li>Read Resources permission or Resource Reviewer role for a project</li><li>Edit resources, Edit Resource Properties, Read Resources permissions or Resource Contributor role for the document</li><li>Resource Creator role for the category where the document is stored</li></ul></td></tr><tr><td colspan="1"><strong>Edit a model in Cameo Collaborator</strong></td><td colspan="1"><ul><li>Read Resources permission or Resource Reviewer role for a document</li><li>Read Resources and Edit Resources permission or Resource Contributor role for the project with read-write permissions for the project branch</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170491778 space=TWCloud2024xR1 version=2 -->
## PAGE 00213: Roles application

- page_id: `170491778`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491778/Roles+application
- version_number: 2
- version_date: `2025-10-30T14:20:38.739+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications
- labels: []

### NORMALIZED CONTENT

As explained in the section [CONFLUENCE_PAGE title='User roles and permissions' space=''], the scopes of pre-existing (i.e., pre-defined) roles in the Teamwork Cloud system fall under two categories: Global and Resource-specific.

A role with a global scope allows a user to work on any protected objects in Teamwork Cloud; the permissions coverage is comprehensive and not limited to a specific resource. Users whose role scope is global are authorized to carry out their tasks (aligned with the permissions) anywhere within Teamwork Cloud. For example, a User Manager maintains and manages all user accounts on the Teamwork Cloud system. There is no need to assign resources for this role.

A role with a resource-specific scope allows a user to work on a local project. The permissions of this role are graded on a resource basis. A user who reviews a project or document has a resource-specific role. A user can have more than one resource-specific role (for example, user A can be both the Resource Contributor of Project A and the Resource Manager of Project B). This supports the working concept of different roles in each project of an organization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>As explained in the section <ac:link><ri:page ri:content-title="User roles and permissions" /></ac:link>, the scopes of pre-existing (i.e., pre-defined) roles in the Teamwork Cloud system fall under two categories: Global and Resource-specific.</p><p>A role with a global scope allows a user to work on any protected objects in Teamwork Cloud; the permissions coverage is comprehensive and not limited to a specific resource. Users whose role scope is global are authorized to carry out their tasks (aligned with the permissions) anywhere within Teamwork Cloud. For example, a User Manager maintains and manages all user accounts on the Teamwork Cloud system. There is no need to assign resources for this role. </p><p>A role with a resource-specific scope allows a user to work on a local project. The permissions of this role are graded on a resource basis. A user who reviews a project or document has a resource-specific role. A user can have more than one resource-specific role (for example, user A can be both the Resource Contributor of Project A and the Resource Manager of Project B). This supports the working concept of different roles in each project of an organization. </p><p class="auto-cursor-target"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="551b8c59-dfe8-4634-a15d-a08aa622e1b8" /></p>
````

<!--NOMAGIC_PAGE id=170491781 space=TWCloud2024xR1 version=2 -->
## PAGE 00214: Roles application structure

- page_id: `170491781`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491781/Roles+application+structure
- version_number: 2
- version_date: `2025-10-30T14:21:08.274+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application
- labels: []

### NORMALIZED CONTENT

The Roles application is a role management application for Teamwork Cloud. There are two types of roles in the Roles application: predefined and custom. Predefined roles are the roles that come with the installation and cannot be edited, (to learn more about predefined roles, see [CONFLUENCE_PAGE title='Types of roles' space='']) whereas custom roles are created by users. These roles can be [CONFLUENCE_PAGE title='Editing custom roles' space=''] by changing their names, descriptions, and adding or removing permissions.

The Roles application allows you to:

- View role details such as description, permissions, and assigned users.
- [CONFLUENCE_PAGE title='Creating roles' space=''] .
- Add or remove permissions of a custom role.
- Add or remove users and user groups assigned to a role.
- Add or remove assigned resources for users and user groups with a custom role scope
- [CONFLUENCE_PAGE title='Removing custom roles' space=''] .

#### NOTE: Creating and editing roles

Creating and editing roles

- Only users with the Security Manager role can create or modify custom roles.
- It is impossible to edit predefined roles and their permissions.

The following figure displays the Roles application structure.

[IMAGE alt='' src='']

###### The components of the Roles application.

As you can see in the above figure, all available roles are listed in the content pane of the Roles application. You can easily identify if a role is predefined or custom by its icon. After selecting a role, the **Role** pane opens displaying the details of the role such as permissions and assigned users. See the table below for detailed descriptions of the Roles application user interface components.

| User interface component | Description |
| --- | --- |
| App bar | is located at the top of the web application portal. You can use it to search for roles by role name and navigate through different Teamwork Cloud Admin web applications. |
| Content pane | In the Roles application, the content pane lists all available roles (both predefined and custom) and allows you to access various role-related actions, e.g., view role details or change role assignments. You can also click on the top right corner of the content pane to sort roles by name. |
|  | This icon next to a role name means that the role is predefined. Such a role comes with the installation and you cannot change its name, description, or permissions. To learn more about predefined roles, see . |
|  | This icon next to a role name means that the role is custom. Custom roles are user-created roles and can be by changing their names, descriptions, and adding or removing permissions. |
|  | Select this icon next to a role to open the menu with role-related actions. The list of available actions depends on the type of role.If a role is predefined, you can: View role details, Change role assignmentsIf a role is custom, you can: View role details, Edit role details, Change permissions, Change role assignments, Remove role. |
|  | Click this icon to create a new role. |
| Role pane | The Role pane is located on the right side of the Roles application portal. It displays information about the selected role. You can use different cards of the pane to view or change role permissions and assignments. To open the Role pane, select a role in the content pane of the Roles application. |
| Role details card | The role details card displays the name and description of the selected role. If the role is custom, you can use this card to change the role name and description or remove the role. |
| Role permissions card | The role permissions card displays the permissions assigned to the selected role. You can also use this card to add or remove permissions of a custom role. |
| Role assignments card | The role assignments card displays the users and user groups assigned to the selected role. You can use this card to assign new users and user groups to the role or remove existing ones. Here, you can also change the role scope for the assigned users and user groups. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="confluence-link">The R<ac:inline-comment-marker ac:ref="232dda64-078f-414b-a9c9-b9f47972907c">oles applicat</ac:inline-comment-marker>ion is a role management application for Teamwork Cloud. There are two types of roles in the Roles application: predefined and custom. Predefined roles are the roles that come with the installation and cannot be edited, (to learn more about predefined roles, see <ac:link><ri:page ri:content-title="Types of roles" /></ac:link>) whereas custom roles are created by users. These roles can be <ac:link><ri:page ri:content-title="Editing custom roles" /><ac:plain-text-link-body><![CDATA[edited]]></ac:plain-text-link-body></ac:link> by changing their names, descriptions, and adding or removing permissions.</p><p class="confluence-link">The Roles application allows you to:</p><ul><li>View role details such as description, permissions, and assigned users.</li><li><ac:link><ri:page ri:content-title="Creating roles" /><ac:plain-text-link-body><![CDATA[Create a role]]></ac:plain-text-link-body></ac:link>.</li><li>Add or remove permissions of a custom role.</li><li>Add or remove users and user groups assigned to a role.</li><li>Add or remove assigned resources for users and user groups with a custom role scope</li><li><ac:link><ri:page ri:content-title="Removing custom roles" /><ac:plain-text-link-body><![CDATA[Remove a custom role]]></ac:plain-text-link-body></ac:link>.<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7debf35a-6898-48a1-b59b-fbc13a07c281"><ac:parameter ac:name="title">Creating and editing roles</ac:parameter><ac:rich-text-body><ul><li>Only users with the Security Manager role can create or modify custom roles.</li><li>It is impossible to edit predefined roles and their permissions.</li></ul></ac:rich-text-body></ac:structured-macro><p><br />The following figure displays the Roles application structure.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="role_app_structure.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">The components of the Roles application.</h6><p><br /></p><p>As you can see in the above figure, all available roles are listed in the content pane of the Roles application. You can easily identify if a role is predefined or custom by its icon. After selecting a role, the <strong>Role</strong> pane opens displaying the details of the role such as permissions and assigned users. See the table below for detailed descriptions of the Roles application user interface components.<br /><br /></p><table class="relative-table wrapped" style="width: 1907.77px;"><colgroup><col style="width: 251.438px;" /><col style="width: 1655.33px;" /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">User interface component</th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Description</th></tr><tr><td style=""><strong title="">App bar</strong></td><td style=""><ac:link><ri:page ri:content-title="Using the app bar" /><ac:plain-text-link-body><![CDATA[The app bar]]></ac:plain-text-link-body></ac:link> is located at the top of the web application portal. You can use it to search for roles by role name and navigate through different Teamwork Cloud Admin web applications.</td></tr><tr><td style=""><strong title="">Content pane</strong></td><td style=""><div class="content-wrapper"><p>In the Roles application, the content pane lists all available roles (both predefined and custom) and allows you to access various role-related actions, e.g., view role details or change role assignments. You can also click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="sorting_by_name.png" /></ac:image> on the top right corner of the content pane to sort roles by name.</p></div></td></tr><tr><td style=""><div class="content-wrapper" title=""><p><ac:image ac:align="center"><ri:attachment ri:filename="predefined_role.png" /></ac:image></p></div></td><td style="">This icon next to a role name means that the role is predefined. Such a role comes with the installation and you cannot change its name, description, or permissions. To learn more about predefined roles, see <ac:link><ri:page ri:content-title="Types of roles" /></ac:link>.</td></tr><tr><td style=""><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="custom_role.png" /></ac:image></p></div></td><td style="">This icon next to a role name means that the role is custom. Custom roles are user-created roles and can be <ac:link><ri:page ri:content-title="Editing custom roles" /><ac:plain-text-link-body><![CDATA[edited]]></ac:plain-text-link-body></ac:link> by changing their names, descriptions, and adding or removing permissions.</td></tr><tr><td style=""><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="actions_icon.png" /></ac:image></p></div></td><td style=""><p>Select this icon next to a role to open the menu with role-related actions. The list of available actions depends on the type of role.</p><ul><li>If a role is predefined, you can: View role details, Change role assignments</li><li>If a role is custom, you can: View role details, Edit role details, Change permissions, Change role assignments, Remove role.</li></ul></td></tr><tr><td style="" colspan="1"><div class="content-wrapper"><p><ac:image ac:align="center" ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="create_role.png" /></ac:image></p></div></td><td style="" colspan="1">Click this icon to create a new role.</td></tr><tr><td style=""><strong>Role pane</strong></td><td style="">The Role pane is located on the right side of the Roles application portal. It displays information about the selected role. You can use different cards of the pane to view or change role permissions and assignments. To open the Role pane, select a role in the content pane of the Roles application.</td></tr><tr><td style=""><strong>Role details card</strong></td><td style="">The role details card displays the name and description of the selected role. If the role is custom, you can use this card to change the role name and description or remove the role.</td></tr><tr><td style=""><strong>Role permissions card</strong></td><td style="">The role permissions card displays the permissions assigned to the selected role. You can also use this card to add or remove permissions of a custom role.</td></tr><tr><td style=""><strong>Role assignments card</strong></td><td style="">The role assignments card displays the users and user groups assigned to the selected role. You can use this card to assign new users and user groups to the role or remove existing ones. Here, you can also change the role scope for the assigned users and user groups.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=171180779 space=TWCloud2024xR1 version=3 -->
## PAGE 00215: Running server-side simulation with SSL

- page_id: `171180779`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180779/Running+server-side+simulation+with+SSL
- version_number: 3
- version_date: `2024-06-07T10:01:08.152+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation > Simulation using Jupyter Notebook
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Running server-side simulation with SSL' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b46bcdf7-3319-4b56-a6df-18d7351c9de8"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Running server-side simulation with SSL" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170491390 space=TWCloud2024xR1 version=4 -->
## PAGE 00216: SAML integration

- page_id: `170491390`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491390/SAML+integration
- version_number: 4
- version_date: `2025-08-14T13:03:43.904+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration > Authentication server
- labels: []

### NORMALIZED CONTENT

**On this page**

5

Teamwork Cloud authentication server can be integrated with a 3rd party Identity Provider, which supports SAML v2.0 protocol. In this integration, the authentication server acts as a Service Provider.

Integration with the SAML v2.0 Identity Provider allows authentication to Teamwork Cloud with users from the Identity Provider. Successful authentication requires one of the following two conditions to be true:

- [CONFLUENCE_PAGE title='Importing users and groups from LDAP' space='']
- [CONFLUENCE_PAGE title='Enabling external user creation' space=''] .

SAML integration requires [CONFLUENCE_PAGE title='SAML parameters' space=''], these parameters are configured in the **authserver.properties** file.

To integrate with the SAML v2.0 based Identity Provider follow the steps below.

##### Installing/configuring the SAML v2.0 Identity Provider

To install/configure the SAML v2.0 Identity Provider

1. Follow your particular product's instructions to configure the Identity Provider.
2. Make sure that Identity Provider uses stateful sessions.
3. Configure Name ID value mapping; for example, add *urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=uid* to the mapping. The authentication server needs to know which user's attribute should be used to identify the user. The value of this attribute will be used as the username in the Teamwork Cloud. By default, it uses *urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName* format (configured in **authserver.properties**, parameter **authentication.saml.name.id.format**). Thus, if the Identity Provider has mapping *urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=uid* or similar, then the *uid* attribute will be used as the username.

##### Configuring authentication server parameters in *authserver.properties*

To configure authentication server parameters in **authserver.properties**

1. Set **authentication.saml.enabled**to *true*.
2. If needed, change the Service Provider ID in **authentication.saml.entity.id**parameter. This ID should be unique for each Service Provider. In the case of a cluster, this ID should be unique for each authentication server instance.
3. Set **authentication.saml.idp.metadata.url**or **authentication.saml.idp.metadata.file**to the appropriate value (only one of these parameters can be activated). If the Identity Provider has a URL address that provides its metadata, use **authentication.saml.idp.metadata.url**parameter. If there is no such ability, store the Identity Provider's metadata in a file and set the path to the file (absolute or relative to the WebAppPlatform directory) in **authentication.saml.idp.metadata.file**parameter.
4. Set the name of the button to the parameter **authentication.saml.link**. The user will click this button on the login page to authenticate using the SAML v2.0 Identity Provider.

(Re)start the authentication server.

##### Register an authentication server as a remote SAML v2.0 Service Provider in a 3rd party product

To register an authentication server as a remote SAML v2.0 Service Provider in a 3rd party product

1. While registering, you should provide your authentication server's metadata. This information can be retrieved from URL *https://<auth-server-host>:<auth-server-port>/authentication/saml2/metadata*.
2. If needed, fill in attributes mapping in the registered Service Provider if the 3rd party product has that ability. You can select the Identity Provider's user attribute and map it to the Teamwork Cloud user attribute. Currently, Teamwork Cloud supports the following attribute names: **name**, **email**, **mobile**, **department**. Values of mapped attributes can be saved in Teamwork Cloud *only if*a new Teamwork Cloud user is created automatically after the first successful authentication.Attributes are not updated after subsequent successful authentications.

After these steps, users should be able to log in to the Teamwork Cloud through SAML v2.0 Identity Provider by clicking the SAML integration button on the authentication server's login page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong> On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f81276f5-2301-4cf7-85b0-62e89a94e6b3"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Teamwork Cloud authentication server can be integrated with a 3rd party Identity Provider, which supports SAML v2.0 protocol. In this integration, the authentication server acts as a Service Provider.</p><p>Integration with the SAML v2.0 Identity Provider allows authentication to Teamwork Cloud with users from the Identity Provider. Successful authentication requires one of the following two conditions to be true:</p><ul><li><ac:link><ri:page ri:content-title="Importing users and groups from LDAP" /><ac:plain-text-link-body><![CDATA[an external user with the same username is already imported in Teamwork Cloud Admin]]></ac:plain-text-link-body></ac:link></li><li class="auto-cursor-target"><ac:link><ri:page ri:content-title="Enabling external user creation" /><ac:plain-text-link-body><![CDATA[the option to automatically create an external user after successful authentication is activated in Teamwork Cloud Admin Settings application]]></ac:plain-text-link-body></ac:link>.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1041268c-3716-486e-9b58-6dd8c707f2b8"><ac:rich-text-body><p>SAML integration requires <ac:link><ri:page ri:content-title="SAML parameters" /></ac:link>, these parameters are configured in the <strong>authserver.properties</strong> file.</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);">To integrate with the SAML v2.0 based Identity Provider follow the steps below.</span></p><h3><span style="color:var(--ds-text,#333333);">I</span><span style="color:var(--ds-text,#333333);">nstalling/configuring the SAML v2.0 Identity Provider</span></h3><p><span style="color:var(--ds-text,#333333);">To install/configure the SAML v2.0 Identity Provider</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Follow your particular product's instructions to configure the Identity Provider.</span></li><li><span style="color:var(--ds-text,#333333);">Make sure that Identity Provider uses stateful sessions.</span></li><li><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Configure Name ID value mapping; for example, add <em>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=uid</em> to the mapping. The authentication server needs to know which user's attribute should be used to identify the user. The value of this attribute will be used as the username in the Teamwork Cloud. By default, it uses <em>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</em> format (configured in <strong>authserver.properties</strong>, parameter <strong>authentication.saml.name.id.format</strong>). Thus, if the Identity Provider has mapping <em>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName=uid</em> or similar, then the <em>uid</em> attribute will be used as the username. </span></p></li></ol><h3><span style="color:var(--ds-text,#333333);">Configuring authentication server parameters in <em>authserver.properties</em><br /></span></h3><p><span style="color:var(--ds-text,#333333);">To configure authentication server parameters in <strong>authserver.properties</strong></span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Set <strong>authentication.saml.enabled </strong>to <em>true</em>.</span></li><li><span style="color:var(--ds-text,#333333);">If needed, change the Service Provider ID in <strong>authentication.saml.entity.id </strong>parameter. This ID should be unique for each Service Provider. In the case of a cluster, this ID should be unique for each authentication server instance.</span></li><li><span style="color:var(--ds-text,#333333);">Set <strong>authentication.saml.idp.metadata.url </strong>or <strong>authentication.saml.idp.metadata.file </strong>to the appropriate value (only one of these parameters can be activated). If the Identity Provider has a URL address that provides its metadata, use <strong>authentication.saml.idp.metadata.url </strong>parameter. If there is no such ability, store the Identity Provider's metadata in a file and set the path to the file (absolute or relative to the WebAppPlatform directory) in <strong>authentication.saml.idp.metadata.file </strong>parameter.</span></li><li><span style="color:var(--ds-text,#333333);">Set the name of the button to the parameter <strong>authentication.saml.link</strong>. The user will click this button on the login page to authenticate using the SAML v2.0 Identity Provider.</span></li></ol><p><span style="color:var(--ds-text,#333333);">(Re)start the authentication server.</span></p><h3><span style="color:var(--ds-text,#333333);">Register an authentication server as a remote SAML v2.0 Service Provider in a 3rd party product</span></h3><p><span style="color:var(--ds-text,#333333);">To register an authentication server as a remote SAML v2.0 Service Provider in a 3rd party product</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">While registering, you should provide your authentication server's metadata. This information can be retrieved from URL <em>https://&lt;auth-server-host&gt;:&lt;auth-server-port&gt;/authentication/saml2/metadata</em><span class="nolink">.</span></span></li><li><p><span style="color:var(--ds-text,#333333);">If needed, fill in attributes mapping in the registered Service Provider if the 3rd party product has that ability. You can select the Identity Provider's user attribute and map it to the Teamwork Cloud user attribute. Currently, Teamwork Cloud supports the following attribute names: <strong>name</strong>, <strong>email</strong>, <strong>mobile</strong>, <strong>department</strong>.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b7fded94-a476-4175-823b-e32a7a35dda5"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">Values of mapped attributes can be saved in Teamwork Cloud <em>only if </em>a new Teamwork Cloud user is created automatically after the first successful authentication.</span></p><p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Attributes are not updated after subsequent successful authentications.</span></span></p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);"> </span></p></li></ol><p><span style="color:var(--ds-text,#333333);">After these steps, users should be able to log in to the Teamwork Cloud through SAML v2.0 Identity Provider by clicking the SAML integration button on the authentication server's login page.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491391 space=TWCloud2024xR1 version=4 -->
## PAGE 00217: SAML parameters

- page_id: `170491391`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491391/SAML+parameters
- version_number: 4
- version_date: `2026-03-30T11:10:44.212+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Configuration > Authentication server > SAML integration
- labels: []

### NORMALIZED CONTENT

To integrate the Authentication Server with any SAML Identity Provider (see instructions for [CONFLUENCE_PAGE title='SAML integration' space='']), you need to add the Authentication Server configuration into the SAML Identity Provider (it should be registered as SAML v2 remote service provider). Next, you need to configure the following additional parameters in the **authserver.properties** file.

| Parameter | Description | Default value |
| --- | --- | --- |
| authentication.saml.enabled | Sets the value to true. | false |
| authentication.saml.entity.id | Sets an authentication server as a service provider ID if it is different than the default server. You can use letters, digits and the following characters: -+&@#%?=~_\|!:,.; | com.nomagic.authentication.server |
| authentication.saml.name.id.format | Specifies the format of a username identifier. | urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName |
| authentication.saml.name.id.attribute | SAML user attribute to map to username instead of SAML user name ID, which is used by default. | - |
| authentication.saml.name.id.allow.create | AllowCreate Name ID policy (true, false). | true |
| authentication.saml.idp.metadata.url | Specifies an Identity Provider metadata URL address if SAML Identity Provider supports metadata retrieval from the URL (e.g., ForgeRock OpenAM). | - |
| authentication.saml.idp.metadata.file | Specifies the path and/or name of a metadata file. You can use either an absolute or a relative path. If the path is relative, the location is the WebAppPlatform directory. | - |
| authentication.saml.link | The title of the button for SAML user login is displayed on the login page. | SAML User |
| authentication.saml.disable.force.authentication | Sets ForceAuthn to true or false in the AuthnRequest in SAML-based authentication. Change it carefully as you won't be able to log in with another user after user logout if the value is true. | false |
| authentication.saml.signature.algorithm | SAML integration requests a signature algorithm. Available values - SHA1, SHA256. and SHA512. | SHA256 |
| authentication.saml.authn.contexts | List of AuthN Contexts separated by a comma. | - |
| authentication.saml.authn.context.comparison.type | AuthN Context comparison type (exact, better, maximum, minimum). | exact |
| authentication.saml.error.visible | Flag indicating if SAML authentication detailed error text should be displayed for the user. | false |
| authentication.saml.login.relay.state.format | RelayState format for authentication request (uuid, query). | uuid |
| authentication.saml.logout.relay.state.format | RelayState format for logout request (uuid, query). | uuid |
| authentication.saml.attributes | A comma-separated list of SAML attributes that can be used in conditional group permissions. | - |

**Related pages**

- [CONFLUENCE_PAGE title='SAML integration' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>To integrate the Authentication Server with any SAML Identity Provider (see instructions for <ac:link><ri:page ri:content-title="SAML integration" /></ac:link>), you need to add the Authentication Server configuration into the SAML Identity Provider (it should be registered as SAML v2 remote service provider). Next, you need to configure the following additional parameters in the <strong>authserver.properties</strong> file.</p><table class="relative-table wrapped" style="width: 89.6063%;"><colgroup><col style="width: 21.987%;" /><col style="width: 55.2461%;" /><col style="width: 22.7921%;" /></colgroup><tbody><tr><th>Parameter</th><th>Description</th><th>Default value</th></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.enabled</span></td><td><span style="color:var(--ds-text,#333333);">Sets the value to </span><span style="color:var(--ds-text,#333333);"><strong>true</strong>.</span></td><td><span style="color:var(--ds-text,#333333);">false</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.entity.id</span></td><td><span style="color:var(--ds-text,#333333);">Sets an authentication server as a service provider ID if it is different than the default server. <span data-teams="true">You can use letters, digits and the following characters: -+&amp;@#%?=~_|!:,.;</span></span></td><td><span style="color:var(--ds-text,#333333);">com.nomagic.authentication.server</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.name.id.format</span></td><td><span style="color:var(--ds-text,#333333);">Specifies the format of a username identifier. </span></td><td><span style="color:var(--ds-text,#333333);">urn:oasis:names:</span>tc<span style="color:var(--ds-text,#333333);">:SAML:1.1:</span>nameid<span style="color:var(--ds-text,#333333);">-format:X509SubjectName</span></td></tr><tr><td>authentication.saml.name.id.attribute</td><td><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">SAML user attribute to map to username instead of SAML user name ID, which is used by default.</span></span></td><td><span style="color:var(--ds-text,#333333);">-</span></td></tr><tr><td><span style="color:var(--ds-text,#172b4d);">authentication.saml.name.id.allow.create</span></td><td><span style="color:var(--ds-text,#172b4d);">AllowCreate Name ID policy (<strong>true</strong>, <strong>false</strong>).</span></td><td>true</td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.idp.metadata.url</span></td><td><span style="color:var(--ds-text,#333333);">Specifies an Identity Provider metadata URL address if SAML Identity Provider supports metadata retrieval from the URL (e.g., ForgeRock OpenAM).</span></td><td><span style="color:var(--ds-text,#333333);">-</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.idp.metadata.file</span></td><td>Specifies the path and/or name of a metadata file. You can use either an absolute or a relative path. If the path is relative, the location is the <em><span style="color:var(--ds-text,#333333);">WebAppPlatform</span></em> directory.</td><td>-</td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.link</span></td><td><span style="color:var(--ds-text,#333333);">The title of the button for SAML user login is displayed on the login page.</span></td><td><span style="color:var(--ds-text,#333333);">SAML User</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.disable.force.authentication</span></td><td><p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Sets ForceAuthn to true or false in the AuthnRequest in SAML-based authentication. Change it carefully as you won't be able to log in with another user after user logout if the value is<span> </span></span><strong style="text-align: left;">true</strong>.</span></p></td><td><span style="color:var(--ds-text,#333333);">false</span></td></tr><tr><td>authentication.saml.signature.algorithm</td><td>SAML integration requests a signature algorithm. Available values - SHA1, SHA256. and SHA512.</td><td>SHA256</td></tr><tr><td>authentication.saml.authn.contexts</td><td>List of AuthN Contexts separated by a comma.</td><td>-</td></tr><tr><td>authentication.saml.authn.context.comparison.type</td><td>AuthN Context comparison type (exact, better, maximum, minimum).</td><td>exact</td></tr><tr><td>authentication.saml.error.visible</td><td>Flag indicating if SAML authentication detailed error text should be displayed for the user.</td><td>false</td></tr><tr><td><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">authentication.saml.login.relay.state.format</span></span></td><td><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">RelayState format for authentication request (<strong>uuid</strong>, <strong>query</strong>).</span></span></td><td><span style="color:var(--ds-text,#333333);">uuid</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">authentication.saml.logout.relay.state.format</span></span></td><td><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">RelayState format for logout request (<strong>uuid</strong>, <strong>query</strong>).</span></span></td><td><span style="color:var(--ds-text,#333333);">uuid</span></td></tr><tr><td><span style="color:var(--ds-text,#333333);">authentication.saml.attributes</span></td><td><span style="color:var(--ds-text,#333333);">A comma-separated list of SAML attributes that can be used in conditional group permissions. </span></td><td><span style="color:var(--ds-text,#333333);">-</span></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SAML integration" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180780 space=TWCloud2024xR1 version=3 -->
## PAGE 00218: Sample projects for simulation with Jupyter Notebook

- page_id: `171180780`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180780/Sample+projects+for+simulation+with+Jupyter+Notebook
- version_number: 3
- version_date: `2024-06-07T10:01:25.031+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation > Simulation using Jupyter Notebook
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Sample projects for simulation with Jupyter Notebook' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="c076da55-d83c-47d9-8cbc-e38b74a1eff0"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Sample projects for simulation with Jupyter Notebook" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170491850 space=TWCloud2024xR1 version=2 -->
## PAGE 00219: Scopes of roles

- page_id: `170491850`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491850/Scopes+of+roles
- version_number: 2
- version_date: `2025-01-22T15:16:58.651+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application > User roles and permissions
- labels: []

### NORMALIZED CONTENT

**On this page**

4

The scope of a role in Teamwork Cloud is the extent of the area to which the role is relevant. There are two scopes of roles: global scope and custom scope. A role with global scope is not limited to any resource or category and applies to all resources in the server. A role with a custom scope applies only to specific resources, project branches, and/or categories.

#### NOTE: Setting role scopes

Setting role scopes

To change the scope of roles, you need to have the Manage User Permissions permission.

##### **Global scope**

The permissions of a role with a global scope extend across all resources, protected objects, and users in Teamwork Cloud. When you assign a role to a user or user group, its scope is set to global by default, but you can change that scope to custom at any time. Most roles in Teamwork Cloud can have either a global or a custom scope. However, some roles can only be global because of the nature of their permissions. For example, a user with the User Manager role does not need and cannot have a custom scope (resource assignment). Such user is authorized to carry out their tasks related to this role anywhere in the Teamwork Cloud server.

The following table lists all default Teamwork Cloud roles that can have only a global scope:

| Global scope role | Permissions |
| --- | --- |
| Data Markings Manager | Mark data. |
| Security Manager | List all resources/users and manage user permissions and security roles. |
| Server Administrator | Configure server. |
| User Manager | Create users, edit user properties, list all users, and remove users. |

##### **Custom scope**

The permissions of a role with a custom scope apply only to specific resources, project branches, or categories. Note that a user or user group can have more than one role with different scopes.

The following table lists all default Teamwork Cloud roles that can have a custom scope:

| Custom scope role | Permissions |
| --- | --- |
| Resource Creator | (Only category-specific custom scope) Add resources to the selected scope of categories, including the ability to categorize them, create new categories, or manage the existing ones. |
| Resource Manager | Administer/read/remove resources, edit resources, and their properties, list all users, manage model permissions and manage owned resource access rights. |
| Resource Contributor | Edit resources and their properties, read resources. |
| Resource Reviewer | Read resources. |
| Resource Locks Administrator | Release locked elements. |

The following figure illustrates the use of roles and their scopes.

[IMAGE alt='' src='']

###### A user can have more than one role with different scopes.

##### Setting resource and category-specific scope

You can limit the scope of a role assigned to a user or user group to specific resources or all the resources contained in a specific category. When role scope is resource-specific, the role applies only to the selected resources even after they are moved from one category to another. However, when role scope is category-specific, the role applies to all resources in a specific category. This means that the role no longer applies to the resources that are removed from the category. In addition, all new resources added to the category automatically inherit the role with its assignments.

To set resource or category-specific scope from the Roles application

1. In the Roles application, select the role whose scope you want to change.
2. In the Role pane on the right side of the application portal, click the Change button in the Role assignments card.
3. In the Assigned users/groups list, find the user (or user group) whose role scope you want to change. If the user (or user group) is not assigned to this role yet, use the search box to find and add them.
4. Click the user's scope selection box and select the Custom scope . If the user already has a custom scope specified for this role, click the Assignments button.
5. Do one of the following:
  - Select desired resources, to set a resource-specific scope.
  - Select desired categories, to set a category-specific scope.
6. Click [ATTACHMENT filename='back.png'] to go back to the role assignments window and click [ATTACHMENT filename='save_role.png'] .

To set resource or category-specific scope from the Users application

1. In the Users application, select the user (or user group) whose role scope you want to change.
2. In the User pane on the right side of the application portal, click the Change button in the Roles card.
3. In the Assigned roles list, find the role whose scope you want to change. If the role is not assigned to this user yet, use the search box to find and add it.
4. Click the scope selection box of the role and select the Custom scope . If the role already has a custom scope specified, click the Assignments button.
5. Do one of the following:
  - Select desired resources, to set a resource-specific scope.
  - Select desired categories, to set a category-specific scope.
6. Click [ATTACHMENT filename='back.png'] to go back to the user roles window and click [ATTACHMENT filename='save_users.png'] .

##### Setting project branch-specific scope

You can limit the scope of a role assigned to a user or user group not only to specific resources but to specific branches of a resource as well. For example, you can give permissions for different branches of a model to different teams of engineers who need to work on separate parts of a project independently. Then you can merge the branches when the work is complete.

The branch-specific scope can only be set for roles that contain the Edit Resources permission, e.g., Resource Contributor or Resource Manager roles.

You can specify branch level permissions either from the Roles or from the Users application as described below.

To set branch-specific scope from the Roles application

1. In the Roles application, select the role whose scope you want to change.
2. In the Role pane on the right side of the application portal, click the Change button in the Role assignments card.
3. In the Assigned users/groups list, find the user (or user group) whose role scope you want to change. If the user (or user group) is not assigned to this role yet, use the search box to find and add them.
4. Click the user's scope selection box and select the Custom scope . If the user already has a custom scope specified for this role, click the Assignments button.
5. Select the desired resource and click [ATTACHMENT filename='change_branch_permissions.png'] next to it.
6. In the open dialog, select the branches that should be Read-only for the user. The user will have the read-write permissions for all the branches (or trunk) that are not selected.
7. Click the Select button.
8. Click [ATTACHMENT filename='back.png'] to go back to the role assignments window and click [ATTACHMENT filename='save_role.png'] .

To set branch-specific scope from the Users application

1. In the Users application, select the user (or user group) whose role scope you want to change.
2. In the User pane on the right side of the application portal, click the Change button in the Roles card.
3. In the Assigned roles list, find the role whose scope you want to change. If the role is not assigned to this user yet, use the search box to find and add it.
4. Click the scope selection box of the role and select the Custom scope . If the role already has a custom scope specified, click the Assignments button.
5. Select the desired resource and click [ATTACHMENT filename='change_branch_permissions.png'] next to it.
6. In the open dialog, select the branches that should be Read-only for the user. The user will have the read-write permissions for all the branches (or trunk) that are not selected.
7. Click the Select button.
8. Click [ATTACHMENT filename='back.png'] to go back to the user roles window and click [ATTACHMENT filename='save_users.png'] .

Now the user has read-write permissions only for those branches of the project that you did not select as read-only. For example, if you set branch level permissions as displayed below, a user will only be able to edit the *Climate Control - Heating* branch of the *Climate Control System* project.

[IMAGE alt='' src='']

###### This example demonstrates how to specify branch-level permissions.

**Related pages**

- [CONFLUENCE_PAGE title='Types of roles' space='']
- [CONFLUENCE_PAGE title='Assigning roles' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="cabed915-04da-4b83-951d-5fede5200296"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The scope of a role in Teamwork Cloud is the extent of the area to which the role is relevant. There are two scopes of roles: global scope and custom scope. A role with global scope is not limited to any resource or category and applies to all resources in the server. A role with a custom scope applies only to specific resources, project branches, and/or categories.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="718931e1-f453-4101-a195-86f6b4f38fa9"><ac:parameter ac:name="title">Setting role scopes</ac:parameter><ac:rich-text-body><p>To change the scope of roles, you need to have the Manage User Permissions permission.</p></ac:rich-text-body></ac:structured-macro><h3><strong>Global scope</strong></h3><p>The permissions of a role with a global scope extend across all resources, protected objects, and users in Teamwork Cloud. When you assign a role to a user or user group, its scope is set to global by default, but you can change that scope to custom at any time. Most roles in Teamwork Cloud can have either a global or a custom scope. However, some roles can only be global because of the nature of their permissions. For example, a user with the User Manager role does not need and cannot have a custom scope (resource assignment). Such user is authorized to carry out their tasks related to this role anywhere in the Teamwork Cloud server.</p><p>The following table lists all default Teamwork Cloud roles that can have only a global scope:</p><table class="wrapped"><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Global scope role</th><th>Permissions</th></tr><tr class=""><td colspan="1"><strong>Data Markings Manager</strong></td><td colspan="1">Mark data.</td></tr><tr class=""><td><strong>Security Manager</strong></td><td>List all resources/users and manage user permissions and security roles.</td></tr><tr class=""><td><strong>Server Administrator</strong></td><td>Configure server.</td></tr><tr class=""><td><strong>User Manager</strong></td><td>Create users, edit user properties, list all users, and remove users.</td></tr></tbody></table><h3><strong>Custom scope</strong></h3><p>The permissions of a role with a custom scope apply only to specific resources, project branches, or categories. Note that a user or user group can have more than one role with different scopes.</p><p>The following table lists all default Teamwork Cloud roles that can have a custom scope:</p><table class="relative-table wrapped" style="width: 100.0%;"><colgroup class=""><col class="" style="width: 26.3521%;" /><col class="" style="width: 73.6479%;" /></colgroup><tbody class=""><tr class=""><th>Custom scope role</th><th>Permissions</th></tr><tr class=""><td colspan="1"><strong>Resource Creator</strong></td><td colspan="1"><span>(Only category-specific custom scope) Add resources to the selected scope of categories, including the ability to categorize them, create new categories, or manage the existing ones.</span></td></tr><tr class=""><td><strong>Resource Manager</strong></td><td>Administer/read/remove resources, edit resources, and their properties, list all users, manage model permissions and manage owned resource access rights.</td></tr><tr class=""><td><strong>Resource Contributor</strong></td><td>Edit resources and their properties, read resources.</td></tr><tr class=""><td><strong>Resource Reviewer</strong></td><td>Read resources.</td></tr><tr class=""><td><strong>Resource Locks Administrator</strong></td><td>Release locked elements.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p>The following figure illustrates the use of roles and their scopes.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Use of Roles and Scopes.png" /></ac:image></p><h6 style="text-align: center;">A user can have more than one role with different scopes.</h6><h3>Setting resource and category-specific scope</h3><p>You can limit the scope of a role assigned to a user or user group to specific resources or all the resources contained in a specific category. When role scope is resource-specific, the role applies only to the selected resources even after they are moved from one category to another. However, when role scope is category-specific, the role applies to all resources in a specific category. This means that the role no longer applies to the resources that are removed from the category. In addition, all new resources added to the category automatically inherit the role with its assignments.</p><p><br /></p><p>To set resource or category-specific scope from the Roles application</p><hr /><ol><li>In the Roles application, select the role whose scope you want to change.</li><li>In the <strong>Role</strong> pane on the right side of the application portal, click the <strong>Change</strong> button in the <strong>Role assignments</strong> card.</li><li>In the <strong>Assigned users/groups</strong> list, find the user (or user group) whose role scope you want to change. If the user (or user group) is not assigned to this role yet, use the search box to find and add them.</li><li>Click the user's scope selection box and select the <strong>Custom scope</strong>. If the user already has a custom scope specified for this role, click the <strong>Assignments</strong> button.</li><li>Do one of the following:<ul><li>Select desired resources, to set a resource-specific scope.</li><li>Select desired categories, to set a category-specific scope.</li></ul></li><li>Click <ac:image><ri:attachment ri:filename="back.png" /></ac:image> to go back to the role assignments window and click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_role.png" /></ac:image>.</li></ol><p><br /></p><p>To set resource or category-specific scope from the Users application</p><hr /><ol><li>In the Users application, select the user (or user group) whose role scope you want to change.</li><li>In the <strong>User</strong> pane on the right side of the application portal, click the <strong>Change</strong> button in the <strong>Roles</strong> card.</li><li>In the <strong>Assigned roles</strong> list, find the role whose scope you want to change. If the role is not assigned to this user yet, use the search box to find and add it.</li><li>Click the scope selection box of the role and select the <strong>Custom scope</strong>. If the role already has a custom scope specified, click the <strong>Assignments</strong> button.</li><li>Do one of the following:<ul><li>Select desired resources, to set a resource-specific scope.</li><li>Select desired categories, to set a category-specific scope.</li></ul></li><li>Click <ac:image><ri:attachment ri:filename="back.png" /></ac:image> to go back to the user roles window and click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_users.png" /></ac:image>.</li></ol><h3>Setting project branch-specific scope</h3><p>You can limit the scope of a role assigned to a user or user group not only to specific resources but to specific branches of a resource as well. For example, you can give permissions for different branches of a model to different teams of engineers who need to work on separate parts of a project independently. Then you can merge the branches when the work is complete.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a59763b8-e96b-423f-b9b2-f78599d5f9a7"><ac:rich-text-body><p>The branch-specific scope can only be set for roles that contain the Edit Resources permission, e.g., Resource Contributor or Resource Manager roles.</p></ac:rich-text-body></ac:structured-macro><p>You can specify branch level permissions either from the Roles or from the Users application as described below.</p><p><br /></p><p>To set branch-specific scope from the Roles application</p><hr /><ol><li>In the Roles application, select the role whose scope you want to change.</li><li>In the <strong>Role</strong> pane on the right side of the application portal, click the <strong>Change</strong> button in the <strong>Role assignments</strong> card.</li><li>In the <strong>Assigned users/groups</strong> list, find the user (or user group) whose role scope you want to change. If the user (or user group) is not assigned to this role yet, use the search box to find and add them.</li><li>Click the user's scope selection box and select the <strong>Custom scope</strong>. If the user already has a custom scope specified for this role, click the <strong>Assignments</strong> button.</li><li>Select the desired resource and click <ac:image><ri:attachment ri:filename="change_branch_permissions.png" /></ac:image> next to it.</li><li>In the open dialog, select the branches that should be <strong>Read-only</strong> for the user. The user will have the read-write permissions for all the branches (or trunk) that are not selected.</li><li>Click the <strong>Select</strong> button.</li><li>Click <ac:image><ri:attachment ri:filename="back.png" /></ac:image> to go back to the role assignments window and click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_role.png" /></ac:image>.</li></ol><p><br /></p><p>To set branch-specific scope from the Users application</p><hr /><ol><li>In the Users application, select the user (or user group) whose role scope you want to change.</li><li>In the <strong>User</strong> pane on the right side of the application portal, click the <strong>Change</strong> button in the <strong>Roles</strong> card.</li><li>In the <strong>Assigned roles</strong> list, find the role whose scope you want to change. If the role is not assigned to this user yet, use the search box to find and add it.</li><li>Click the scope selection box of the role and select the <strong>Custom scope</strong>. If the role already has a custom scope specified, click the <strong>Assignments</strong> button.</li><li>Select the desired resource and click <ac:image><ri:attachment ri:filename="change_branch_permissions.png" /></ac:image> next to it.</li><li>In the open dialog, select the branches that should be <strong>Read-only</strong> for the user. The user will have the read-write permissions for all the branches (or trunk) that are not selected.</li><li>Click the <strong>Select</strong> button.</li><li>Click <ac:image><ri:attachment ri:filename="back.png" /></ac:image> to go back to the user roles window and click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="save_users.png" /></ac:image>.</li></ol><p><br />Now the user has read-write permissions only for those branches of the project that you did not select as read-only. For example, if you set branch level permissions as displayed below, a user will only be able to edit the <em>Climate Control - Heating</em> branch of the <em>Climate Control System</em> project.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="setting_branch_level_permissions.png" /></ac:image></p><h6 style="text-align: center;">This example demonstrates how to specify branch-level permissions.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Types of roles" /></ac:link></li><li><ac:link><ri:page ri:content-title="Assigning roles" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180511 space=TWCloud2024xR1 version=2 -->
## PAGE 00220: Searching in a document

- page_id: `171180511`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180511/Searching+in+a+document
- version_number: 2
- version_date: `2025-10-31T12:28:28.652+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Structure of the document portal
- labels: ['searching-for-elements', 'find']

### NORMALIZED CONTENT

You can quickly find the items you need to review in a published model portal. Cameo Collaborator for TWC allows you to search for element names and content that matches or includes the search phrase you enter.

To find an item in a published model

1. In the document search box on the left side of the app bar, enter the search phrase. Minimal number of charactersEnter at least 3 characters.
2. In the search result list, click the item you want to find.

Search results are grouped by model views, as shown below. Clicking an item in the search result list selects it in the navigation pane and opens the related content in the content pane. If there are a large number search results, only the first one hundred search results are shown.

[IMAGE alt='' src='']

###### When you search for items in a document, search results are grouped by model views.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can quickly find the items you need to review in a published model portal. Cameo Collaborator for TWC allows you to search for element names and content that matches or includes the search phrase you enter.</p><p><br /></p><p>To find an item in a published model</p><hr style="" /><ol><li><p class="auto-cursor-target">In the document search box on the left side of the app bar, enter the search phrase.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c8c7dc9c-79b9-43e9-b671-ef6d256616c0"><ac:parameter ac:name="title">Minimal number of characters</ac:parameter><ac:rich-text-body><p>Enter at least 3 characters.</p></ac:rich-text-body></ac:structured-macro></li><li><p>In the search result list, click the item you want to find.</p></li></ol><p><br />Search results are grouped by model views, as shown below. Clicking an item in the search result list selects it in the navigation pane and opens the related content in the content pane. If there are a large number search results, only the first one hundred search results are shown.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="searching_in_document.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">When you search for items in a document, search results are grouped by model views.</h6>
````

<!--NOMAGIC_PAGE id=171180776 space=TWCloud2024xR1 version=3 -->
## PAGE 00221: Server-side simulation

- page_id: `171180776`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180776/Server-side+simulation
- version_number: 3
- version_date: `2024-06-07T09:59:28.379+02:00`
- ancestors: Teamwork Cloud and Services > User Guide
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Server-side simulation' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="8ee2a937-8c93-48df-91c2-e3803623622f"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Server-side simulation" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=218759464 space=TWCloud2024xR1 version=1 -->
## PAGE 00222: Setting up Grafana dashboard

- page_id: `218759464`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/218759464/Setting+up+Grafana+dashboard
- version_number: 1
- version_date: `2025-03-18T14:05:04.657+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Monitoring stack
- labels: []

### NORMALIZED CONTENT

**Prerequisites**

- Fully deployed monitoring and telemetry nodes
- Grafana dashboard JSON file for Teamwork Cloud

##### Import Dashboard

To set up Grafana dashboard

1. Go to the Grafana home page at http://<monitoring-node>:3000 (note the HTTP address) in a web browser.
2. Log in to the Grafana dashboard. Use default credentials of admin/admin for new installation; You will be prompted to change the admin password after initial login.
3. From the home page, locate the Dashboards menu on the left menu and select Import
4. Click the Upload JSON File button. Locate and select the Grafana dashboard from the monitoring stack package.
5. Map the three data sources as shown below (Telegraf:Telegraf, Cassandra:Cassandra, and Teamwork Cloud:Teamwork Cloud). Click the Import button. [ATTACHMENT filename='image-2025-3-17_10-34-34-1.png']
6. To set this dashboard as the default Home Dashboard, go to Configuration and select Preferences. Select the Teamwork Cloud dashboard under Home Dashboard and save.

The monitoring node installation script creates a guest user, with credentials guest/guest, who can view the dashboard but cannot make any changes to it.

##### Configure Grafana

The following information is provided as example guidance. Grafana interface and exact procedure will differ by version.

1. Configuring Grafana monitoring dashboard
  1. Log in to http://MONTORINGNODE_IP:3000 - you will be displayed the Grafana Login Screen - default credentials are admin/admin. Upon logging in, you will be prompted to change the admin password.
  2. You will be presented with the following screen, click Add data source : [ATTACHMENT filename='Add_data_source.png']
  3. Create the data sources, enter the information as in the following screenshots, and press **Save & Test** for each. After the data source gets created, click the **Data Sources** link to continue adding data sources. [ATTACHMENT filename='Data_source_New.png'] [IMAGE alt='' src=''] [IMAGE alt='' src=''] [IMAGE alt='' src=''] [IMAGE alt='' src=''] **[IMAGE alt='' src='']**
  4. Now that the data sources have been added, select the option to import a dashboard [ATTACHMENT filename='Import_dashboard.png']
  5. To upload .json file, click the Upload .json File [ATTACHMENT filename='upload_json.png']
    1. Select the provided [ATTACHMENT filename='Teamwork Cloud Dashboard.json'].
  6. At this point, you will be presented with the following screen, in which you will need to map the data sources [ATTACHMENT filename='mapping_data_sources.png']
  7. Map the data sources as shown below and click the Import button [ATTACHMENT filename='Import_data_sources.png']
  8. To make the Teamwork Cloud dashboard your home dashboard, perform the following steps:
    1. Mark the Teamwork Cloud Dashboard as a favorite [ATTACHMENT filename='TWC_dashboard.png']
    2. Select Configuration > Preferences [IMAGE alt='' src='']
    3. Select the Teamwork Cloud Dashboard to be your Home Dashboard and click Save. [ATTACHMENT filename='TWC_dashboard_Home.png']
    4. The admin user has permissions allowing full access. Create a limited access user who will be allowed to view the dashboard without the ability to make modifications. Click Users. [ATTACHMENT filename='Create_user.png']
    5. You will be presented with the following screen. Click Invite. [ATTACHMENT filename='Invite user.png']
    6. Create a guest user by entering the information as below, and clicking Invite. [IMAGE alt='' src='']
    7. You will be shown a screen as below. Click the Pending Invites button. [ATTACHMENT filename='Pending_invites_button.png']
    8. Click the Copy Invite button. [ATTACHMENT filename='Copy_invite.png']
    9. Paste the link which was copied to your clipboard on a new browser window, and replace "localhost" with the IP address of the monitoring node. You will be presented with the following screen. Change the email field from "guest" to "guest@localhost", enter a password and click on the Sign Up button. [ATTACHMENT filename='Hello_guest.png'] At this point, you will be redirected to the Grafana dashboard under the new login. Sign out, and sign back in as admin. [ATTACHMENT filename='Grafana_dashboard.png']
    10. At this point, change the default admin password. [ATTACHMENT filename='admin.png'] [ATTACHMENT filename='change_admin_password.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Prerequisites</strong></p><ul><li><span>Fully deployed monitoring and telemetry nodes</span></li><li><span>Grafana dashboard JSON file for Teamwork Cloud</span></li></ul><h3><span>Import Dashboard</span></h3><p><span>To set up Grafana dashboard</span></p><hr /><ol><li>Go to the Grafana home page at http://&lt;monitoring-node&gt;:3000 (note the HTTP address) in a web browser.  </li><li>Log in to the Grafana dashboard. Use default credentials of admin/admin for new installation; You will be prompted to change the admin password after initial login.</li><li>From the home page, locate the Dashboards menu on the left menu and select Import</li><li>Click the <strong>Upload JSON File </strong>button.<strong> </strong>Locate and select the Grafana dashboard from the monitoring stack package.  <span class="confluence-embedded-file-wrapper"><br /></span></li><li>Map the three data sources as shown below (Telegraf:Telegraf, Cassandra:Cassandra, and Teamwork Cloud:Teamwork Cloud). Click the <strong>Import</strong> button.<br /><ac:image ac:border="true" ac:width="521"><ri:attachment ri:filename="image-2025-3-17_10-34-34-1.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>To set this dashboard as the default Home Dashboard, go to Configuration and select Preferences. Select the Teamwork Cloud dashboard under Home Dashboard and save.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e71a9496-ff10-4ae0-99b2-43fee55cda27"><ac:rich-text-body>The monitoring node installation script creates a guest user, with credentials guest/guest, who can view the dashboard but cannot make any changes to it.</ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">Configure Grafana</h3><p>The following information is provided as example guidance. <u>Grafana interface and exact procedure will differ by version.</u></p><ol><li>Configuring Grafana monitoring dashboard  <ol><li>Log in to <a href="http://montoringnode_ip:3000/">http://MONTORINGNODE_IP:3000</a> - you will be displayed the Grafana Login Screen - default credentials are admin/admin. Upon logging in, you will be prompted to change the admin password.</li><li>You will be presented with the following screen, click <strong>Add data source</strong>: <br /><ac:image><ri:attachment ri:filename="Add_data_source.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li><p>Create the data sources, enter the information as in the following screenshots, and press <strong>Save &amp; Test</strong> for each. After the data source gets created, click the <strong>Data Sources</strong> link to continue adding data sources. </p><ac:image><ri:attachment ri:filename="Data_source_New.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image><h1><ac:image><ri:attachment ri:filename="Data_source_Cassandra.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></h1><h1><ac:image><ri:attachment ri:filename="Configuration.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></h1><h1><ac:image><ri:attachment ri:filename="Data_source_Telegraf.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></h1><h1><ac:image><ri:attachment ri:filename="Telegraf_configuration.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></h1><p><strong><ac:image><ri:attachment ri:filename="image2018-7-9_15-9-59.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image><br /></strong></p></li><li>Now that the data sources have been added, select the option to import a dashboard<br /> <ac:image><ri:attachment ri:filename="Import_dashboard.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>To upload .json file, click the <strong>Upload .json File </strong><br /><ac:image><ri:attachment ri:filename="upload_json.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image><ol><li>Select the provided <em><ac:link><ri:attachment ri:filename="Teamwork Cloud Dashboard.json"><ri:page ri:content-title="Telemetry Node" ri:space-key="TWCloud2024xR1" /></ri:attachment><ac:plain-text-link-body><![CDATA[Teamwork_Cloud_Dashboard.json]]></ac:plain-text-link-body></ac:link>. </em></li></ol></li><li>At this point, you will be presented with the following screen, in which you will need to map the data sources <br /><ac:image><ri:attachment ri:filename="mapping_data_sources.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>Map the data sources as shown below and click the <strong>Import</strong> button <br /><ac:image><ri:attachment ri:filename="Import_data_sources.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>To make the Teamwork Cloud dashboard your home dashboard, perform the following steps:<ol><li>Mark the Teamwork Cloud Dashboard as a favorite<br /><ac:image><ri:attachment ri:filename="TWC_dashboard.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li> Select <strong>Configuration</strong> &gt;<strong> Preferences</strong><br /><strong> <ac:image><ri:attachment ri:filename="Configuration_preferences.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></strong></li><li>Select the Teamwork Cloud Dashboard to be your Home Dashboard and click <strong>Save.</strong><br /> <ac:image ac:thumbnail="true" ac:height="170"><ri:attachment ri:filename="TWC_dashboard_Home.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>The admin user has permissions allowing full access. Create a limited access user who will be allowed to view the dashboard without the ability to make modifications. Click <strong>Users.</strong><br /><ac:image><ri:attachment ri:filename="Create_user.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>You will be presented with the following screen. Click <strong>Invite.</strong><br /><ac:image><ri:attachment ri:filename="Invite user.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>Create a guest user by entering the information as below, and clicking <strong>Invite.</strong><br /><strong> <ac:image><ri:attachment ri:filename="Guest_user_invite.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></strong></li><li>You will be shown a screen as below. Click the <strong>Pending Invites</strong> button.<br /><ac:image><ri:attachment ri:filename="Pending_invites_button.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>Click the <strong>Copy Invite</strong> button.<br /><ac:image><ri:attachment ri:filename="Copy_invite.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>Paste the link which was copied to your clipboard on a new browser window, and replace &quot;localhost&quot; with the IP address of the monitoring node. You will be presented with the following screen. Change the email field from &quot;guest&quot; to &quot;guest@localhost&quot;, enter a password and click on the <strong>Sign Up</strong> button. <br /><ac:image><ri:attachment ri:filename="Hello_guest.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image><br />At this point, you will be redirected to the Grafana dashboard under the new login. Sign out, and sign back in as admin.<br /> <ac:image ac:thumbnail="true" ac:height="146"><ri:attachment ri:filename="Grafana_dashboard.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li><li>At this point, change the default admin password. <br /><ac:image><ri:attachment ri:filename="admin.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image><br /><ac:image><ri:attachment ri:filename="change_admin_password.png"><ri:page ri:content-title="Setting up Grafana dashboard" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:image></li></ol></li></ol></li></ol>
````

<!--NOMAGIC_PAGE id=170491488 space=TWCloud2024xR1 version=2 -->
## PAGE 00223: Setting up Guest User

- page_id: `170491488`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491488/Setting+up+Guest+User
- version_number: 2
- version_date: `2025-10-30T14:06:57.629+01:00`
- ancestors: Teamwork Cloud and Services > Administration Guide > Web Application Platform Administration
- labels: []

### NORMALIZED CONTENT

After installing Web Application Platform, you need to create and set up the Guest user.

#### WARNING: Important

Important

- Before setting up the Guest user, [CONFLUENCE_PAGE title='Creating users and user groups' space=''] in the [CONFLUENCE_PAGE title='Users application' space=''] of Teamwork Cloud Admin.
- Make sure to [CONFLUENCE_PAGE title='Assigning roles' space=''] to the Guest user:
  - You can use default user roles with default permissions or [CONFLUENCE_PAGE title='Creating roles' space=''] and [CONFLUENCE_PAGE title='Editing custom roles' space=''] .
  - You can use the [CONFLUENCE_PAGE title='Scopes of roles' space=''] for Guest user roles or set a [CONFLUENCE_PAGE title='Scopes of roles' space=''] , meaning that user role permissions are only applied to specific resources.

To set up the Guest user

1. Go to the *<**install_root>/WebAppPlatform/shared/conf* directory and open for editing the *webappplatform.properties* file. (If you installed Cameo Collaborator for Teamwork Cloud) manually, the file may be placed in a custom directory.)
2. Edit the values in the file as shown below: wap.guest.password=]]>
3. Replace the placeholders in the added properties (between angle brackets (<>) with the actual user name and password used in Teamwork Cloud.
4. Restart Web Application Platform.

#### NOTE: Important

Important

The Guest user takes one connection from the Cameo Collaborator license.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">After installing Web Application Platform, you need to create and set up the Guest user.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="7617ff62-1395-4fd1-9ee8-82ad4eb36ab0"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><ul><li>Before setting up the Guest user, <ac:link><ri:page ri:content-title="Creating users and user groups" /><ac:plain-text-link-body><![CDATA[create this user]]></ac:plain-text-link-body></ac:link> in the <ac:link><ri:page ri:content-title="Users application" /></ac:link> of Teamwork Cloud Admin.</li><li>Make sure to <ac:link><ri:page ri:content-title="Assigning roles" /><ac:plain-text-link-body><![CDATA[assign appropriate roles]]></ac:plain-text-link-body></ac:link> to the Guest user:<ul><li>You can use default user roles with default permissions or <ac:link><ri:page ri:content-title="Creating roles" /><ac:plain-text-link-body><![CDATA[create custom roles]]></ac:plain-text-link-body></ac:link> and <ac:link ac:anchor="Add or remove permissions"><ri:page ri:content-title="Editing custom roles" /><ac:plain-text-link-body><![CDATA[add appropriate permissions]]></ac:plain-text-link-body></ac:link>.</li><li>You can use the <ac:link ac:anchor="Global scope"><ri:page ri:content-title="Scopes of roles" /><ac:plain-text-link-body><![CDATA[global scope]]></ac:plain-text-link-body></ac:link> for Guest user roles or set a <ac:link ac:anchor="Custom scope"><ri:page ri:content-title="Scopes of roles" /><ac:plain-text-link-body><![CDATA[custom scope]]></ac:plain-text-link-body></ac:link>, meaning that user role permissions are only applied to specific resources.</li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To set up the Guest user</p><hr /><ol><li><span style="color:var(--ds-text,#333333);"> Go to the <em>&lt;</em><em style="text-align: left;">install_root&gt;/WebAppPlatform/shared/conf</em></span><span style="color:var(--ds-text,#333333);"> directory and open for editing the <em>webappplatform.properties</em> file. (If you installed Cameo Collaborator for Teamwork Cloud) manually, the file may be placed in a custom directory.)</span></li><li><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Edit the values in the file as shown below:<br /></span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="96f66394-290b-4752-b828-1dbe8e368129"><ac:plain-text-body><![CDATA[# Specify the user name and password of the Guest user.
wap.guest.username=<guest_username>
wap.guest.password=<guest_password>]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><span style="color:var(--ds-text,#333333);">Replace the placeholders in the added properties (between angle brackets (&lt;&gt;) with the actual user name and password used in Teamwork Cloud.</span></li><li><span style="color:var(--ds-text,#333333);">Restart Web Application Platform.</span></li></ol><p><span style="color:var(--ds-text,#333333);"> </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4a0fa791-0d42-4467-a054-67cbb91779a0"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>The Guest user takes one connection from the Cameo Collaborator license.</p></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);"> </span></p>
````

<!--NOMAGIC_PAGE id=170491771 space=TWCloud2024xR1 version=2 -->
## PAGE 00224: Setting user clearance

- page_id: `170491771`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491771/Setting+user+clearance
- version_number: 2
- version_date: `2024-10-28T18:35:26.788+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

Data markings can be used to control the user access level. A person granted the Data Markings Manager role can define the access level for all users in the Users App. Depending on their clearance level, users will be able to view resources marked with the appropriate classification level.

To set a user’s clearance level

1. Open the Users app.
2. Click [IMAGE alt='' src=''] next to a user and from the menu select Set access level .
3. Choose the desired clearance level: [ATTACHMENT filename='set_access_level.png']
4. Click the Set button to save your changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(23,43,77);">Data markings can be used to control the user access level. A person granted the Data Markings Manager role can define the access level for all users in the Users App</span>. Depending on their clearance level, users will be able to view resources marked with the appropriate classification level.</p><p>To set a user’s clearance level</p><hr /><ol><li>Open the <strong>Users</strong> app.</li><li>Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span> </span> next to a user and from the menu select <strong>Set access level</strong>.</li><li>Choose the desired clearance level:<br /><br /><ac:image ac:width="350"><ri:attachment ri:filename="set_access_level.png" /></ac:image><br /><br /></li><li>Click the <strong>Set</strong> button to save your changes.</li></ol>
````

<!--NOMAGIC_PAGE id=170491775 space=TWCloud2024xR1 version=2 -->
## PAGE 00225: Setting user group clearance

- page_id: `170491775`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491775/Setting+user+group+clearance
- version_number: 2
- version_date: `2025-10-30T14:20:07.695+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

Data markings in the Users app allow you to define a user’s clearance level.

To set a user’s clearance level

1. Open the Users app.
2. Select User groups in the left menu.
3. Click [IMAGE alt='' src=''] next to a user group and from the menu select Edit group details .
4. Click the Clearance drop-down and choose the desired clearance level.
5. Click the Save button to save your changes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Data markings in the Users app allow you to define a user’s clearance level.</p><p>To set a user’s clearance level</p><hr /><ol><li>Open the <strong>Users</strong> app.</li><li>Select <strong>User groups</strong> in the left menu.</li><li>Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image></span> </span> next to a user group and from the menu select <strong>Edit group details</strong>.</li><li>Click the Clearance drop-down and choose the desired clearance level.</li><li>Click the <strong>Save</strong> button to save your changes.</li></ol><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180058 space=TWCloud2024xR1 version=1 -->
## PAGE 00226: Settings application

- page_id: `171180058`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180058/Settings+application
- version_number: 1
- version_date: `2024-02-20T16:37:57.080+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications
- labels: []

### NORMALIZED CONTENT

In the **Settings**application, you can set all required server configurations. For example, toenable a secure connection to Teamwork Cloud, you must enable TLS (Transport Layer Security) on the Teamwork CloudAdmin**Settings**application. In this application, you can also manage external LDAP servers. **Settings** application functionality:

- [CONFLUENCE_PAGE title='Enabling secure connection between client and server' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Enabling external user creation' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Viewing server status' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Managing LDAP servers' space='TWCloud2024xR1']
- [CONFLUENCE_PAGE title='Managing data markings in Teamwork Cloud Admin' space='TWCloud2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);letter-spacing: 0.0px;">In the <strong>Settings</strong><span> <ac:inline-comment-marker ac:ref="e8aab636-9c06-45e7-a1ff-b188606e5024">application</ac:inline-comment-marker>, you can set all required server configurations. For example, to </span></span><span style="color: rgb(62,63,64);letter-spacing: 0.0px;">enable a secure connection to Teamwork Cloud, you must enable TLS (Transport Layer Security) on the <span style="color: rgb(62,63,64);">Teamwork Cloud </span>Admin </span><strong style="letter-spacing: 0.0px;">Settings</strong><span style="color: rgb(62,63,64);letter-spacing: 0.0px;"> application. In this application, you can also manage external LDAP servers. <strong>Settings</strong> application functionality: </span></p><ul><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Enabling secure connection between client and server" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Enabling external user creation" /></ac:link></li><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Viewing server status" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing LDAP servers" /><ac:plain-text-link-body><![CDATA[Connecting to LDAP server]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Managing data markings in Teamwork Cloud Admin" /></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=171180060 space=TWCloud2024xR1 version=2 -->
## PAGE 00227: Settings application structure

- page_id: `171180060`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180060/Settings+application+structure
- version_number: 2
- version_date: `2024-10-15T12:28:30.446+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

In the Settings application you can specify all required Teamwork Cloud configurations, e.g.,enable a secure connection to Teamwork Cloud and manageexternal LDAP servers. The following figure illustrates the Settings application structure.

[IMAGE alt='' src='']

###### The Settings application structure.

The table below provides detailed descriptions of the Settings application user interface components.

| User interface component | Description |
| --- | --- |
| App bar | is located at the top of the web application portal. You can use it to navigate through different Teamwork Cloud Admin web applications. |
| Menu | The menu is located on the left side of the Settings application. It allows you to select the group of actions you want to perform. |
| Content pane | In the Settings application, the content pane allows you to perform specific actions depending on the action group selected in the menu on the left side of the application screen. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">In the Settings application you can specify all required Teamwork Cloud configurations, <span style="font-size: 14.0px;">e.g.</span>,</span><span style="color: rgb(62,63,64);"> enable a secure connection to Teamwork Cloud and manage </span><span style="color: rgb(62,63,64);">external LDAP servers. The following figure illustrates the Settings application structure.</span></p><p><span style="color: rgb(94,108,132);"><ac:image ac:align="center" ac:border="true" ac:height="438" ac:width="900"><ri:attachment ri:filename="settings_application_structure.jpg" /></ac:image><br /></span></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">The Settings application structure.</span></h6><p><span style="color: rgb(62,63,64);">The table below provides detailed descriptions of the Settings application user interface components.</span></p><table class="relative-table wrapped" style="width: 79.9232%;"><colgroup><col style="width: 13.1868%;" /><col style="width: 86.8132%;" /></colgroup><tbody><tr><th>User interface component</th><th>Description</th></tr><tr><th class="highlight-grey" data-highlight-colour="grey">App bar</th><td><ac:link><ri:page ri:content-title="Using the app bar" /><ac:plain-text-link-body><![CDATA[The app bar]]></ac:plain-text-link-body></ac:link> is located at the top of the web application portal. You can use it to navigate through different Teamwork Cloud Admin web applications.</td></tr><tr><th class="highlight-grey" colspan="1" data-highlight-colour="grey" title="Background colour : Grey">Menu</th><td colspan="1">The menu is located on the left side of the Settings application. It allows you to select the group of actions you want to perform.</td></tr><tr><th class="highlight-grey" data-highlight-colour="grey">Content pane</th><td><div class="content-wrapper"><p>In the Settings application, the content pane allows you to perform specific actions depending on the action group selected in the menu on the left side of the application screen.</p></div></td></tr></tbody></table><p style="text-align: center;"><br /><br /></p>
````

<!--NOMAGIC_PAGE id=171180703 space=TWCloud2024xR1 version=1 -->
## PAGE 00228: Sharing and exporting

- page_id: `171180703`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180703/Sharing+and+exporting
- version_number: 1
- version_date: `2024-01-29T09:42:29.831+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=171180709 space=TWCloud2024xR1 version=2 -->
## PAGE 00229: Sharing diagrams

- page_id: `171180709`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180709/Sharing+diagrams
- version_number: 2
- version_date: `2025-10-31T12:49:06.387+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Sharing and exporting
- labels: []

### NORMALIZED CONTENT

**On this page**

4

You can share diagrams published in Cameo Collaborator documents without showing the whole document and even embed them into other web pages or documents.

##### Sharing diagram links

The steps below explain how to share diagram links with other Cameo Collaborator users or people outside of your organization (public links).

To get a diagram link

1. In a Cameo Collaborator document, open a diagram you want to share.
2. Click [ATTACHMENT filename='menu.png'] in the top-right corner of the diagram card and select Get diagram link .
3. Optionally, enable one or several of the following options:
  - Turn on the Public switch to get a link that can be shared publicly.
  - Turn on the **Embed diagram** switch to get a link allowing you to embed the diagram into any content supporting the iFrame component.
  - Select the Get link to latest version radio button to get a link that always opens the latest version of the diagram.
  - Select the Get link to current version radio button to get a link that opens the current version of the diagram even if it is updated.
4. In the open window, click the **Copy** button.

[IMAGE alt='' src='']

After completing the steps above, the link is copied to your clipboard, and you can share it with others.

##### Embedding dynamic diagrams

When copying a diagram link, you can select to get the URL designed to create an inline frame and easily embed it into any content supporting the iFrame component. Furthermore, such a URL is dynamic and always displays the latest version of the embedded diagram after a Cameo Collaborator document is updated.

To get a diagram link for embedding the diagram into other content

1. In a Cameo Collaborator document, open a diagram you want to embed.
2. Click [ATTACHMENT filename='menu.png'] in the top-right corner of the diagram card and select Get diagram link .
3. In the open window, turn the **Embed diagram** switch on. If you are going to embed the diagram in the content that is viewed by people who cannot connect to Cameo Collaborator for Teamwork Cloud, turn the **Public** switch on as well.
4. Click the **Copy** button.

After completing the steps above, the link is copied to your clipboard, and you can paste it into the content supporting the iFrame component.

[IMAGE alt='' src='']

###### Embedding a diagram from Cameo Collaborator into a Confluence page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f4eaf8bb-b304-4137-a722-fc404d99c90f"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>You can share diagrams published in Cameo Collaborator documents without showing the whole document and even embed them into other web pages or documents.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Sharing diagram links</h3><p>The steps below explain how to share diagram links with other Cameo Collaborator users or people outside of your organization (public links).</p><p><br /></p><p>To get a diagram link</p><hr style="" /><ol><li>In a Cameo Collaborator document, open a diagram you want to share.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> in the top-right corner of the diagram card and select <strong>Get diagram link</strong>.</li><li>Optionally, enable one or several of the following options:<ul><li>Turn on the <strong>Public</strong> switch to get a link that can be shared publicly.</li><li>Turn on the <ac:link ac:anchor="Embedding dynamic diagrams"><ac:link-body><strong>Embed diagram</strong> switch</ac:link-body></ac:link> to get a link allowing you to embed the diagram into any content supporting the iFrame component.</li><li>Select the <strong>Get link to latest version</strong> radio button to get a link that always opens the latest version of the diagram.</li><li>Select the <strong>Get link to current version</strong> radio button to get a link that opens the current version of the diagram even if it is updated.</li></ul></li><li><p class="auto-cursor-target">In the open window, click the <strong>Copy</strong> button.</p></li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="getting_diagram_link.png" /></ac:image></p><p><br />After completing the steps above, the link is copied to your clipboard, and you can share it with others.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Embedding dynamic diagrams</h3><p>When copying a diagram link, you can select to get the URL designed to create an inline frame and easily embed it into any content supporting the iFrame component. Furthermore, such a URL is dynamic and always displays the latest version of the embedded diagram after a Cameo Collaborator document is updated.</p><p><br /></p><p>To get a diagram link for embedding the diagram into other content</p><hr style="" /><ol><li>In a Cameo Collaborator document, open a diagram you want to embed.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> in the top-right corner of the diagram card and select <strong>Get diagram link</strong>.</li><li><p>In the open window, turn the <strong>Embed diagram</strong> switch on.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2d071736-f51c-401a-9ebb-52afb160f304"><ac:rich-text-body><p>If you are going to embed the diagram in the content that is viewed by people who cannot connect to Cameo Collaborator for Teamwork Cloud, turn the <strong>Public</strong> switch on as well.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Click the <strong>Copy</strong> button.</p></li></ol><p><br />After completing the steps above, the link is copied to your clipboard, and you can paste it into the content supporting the iFrame component.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="embeding_diagrams.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Embedding a diagram from Cameo Collaborator into a Confluence page.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180704 space=TWCloud2024xR1 version=2 -->
## PAGE 00230: Sharing document links

- page_id: `171180704`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180704/Sharing+document+links
- version_number: 2
- version_date: `2025-10-31T12:48:30.687+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Sharing and exporting
- labels: ['sharing-published-project', 'sharing-published-model', 'getting-document-link', 'getting-model-link', 'getting-link-to-published-model', 'getting-link-to-document', 'rewriting-link', 'rewriting-document-link', 'rewriting-published-model-link', 'unrestored-unknown-attachment']

### NORMALIZED CONTENT

**On this page**

4

After a document is [CONFLUENCE_PAGE title='Publishing documents' space=''] to Cameo Collaborator for Teamwork Cloud, you can share it with reviewers by providing a link to a Cameo Collaborator document.

[IMAGE alt='' src='']

###### Sharing a published model is the second step in the workflow for reviewing models and providing feedback.

getting_linkTo get a link to a Cameo Collaborator document

1. Open the Resources application in one of the following ways:
  - In an internet browser, go to *https://<domain_name>:<port>/resources*. Not supported internet browsersCameo Collaborator for Teamwork Cloud does not support Internet Explorer. Use a different internet browser instead.
  - In the app bar of the document portal, click [ATTACHMENT filename='plugins.png'] and select Resources .
2. Go to the category containing the Cameo Collaborator document you want to share.
3. Click [ATTACHMENT filename='menu.png'] next to the document, and do one of the following and select Get resource link .
4. If you want to copy a public link, in the open window, turn on the **Public** switch as shown below. Prerequisite for public linksFor public links to work, the Guest user needs to be configured for Teamwork Cloud. For more information, refer to [CONFLUENCE_PAGE title='Setting up Guest User' space=''] [IMAGE alt='' src='']
5. Click Copy button.

After you complete the above steps, the link to a document is copied to your clipboard and you can share it with reviewers.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="39160323-e03f-43c4-b86d-0595e3b108a7"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>After a document is <ac:link><ri:page ri:content-title="Publishing documents" /><ac:plain-text-link-body><![CDATA[published]]></ac:plain-text-link-body></ac:link> to Cameo Collaborator for Teamwork Cloud, you can share it with reviewers by providing a link to a Cameo Collaborator document.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="main_workflow_sharing.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Sharing a published model is the second step in the workflow for reviewing models and providing feedback.</h6><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="db6ca856-ac0a-41d7-a89c-a7e9b6bdae82"><ac:parameter ac:name="">getting_link</ac:parameter></ac:structured-macro>To get a link to a Cameo Collaborator document</p><hr style="" /><ol><li>Open the Resources application in one of the following ways:<br /><ul><li><p>In an internet browser, go to <em>https://&lt;domain_name&gt;:&lt;port&gt;/resources</em>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="83f0faad-e90d-42d1-bf8f-ae23be1824c5"><ac:parameter ac:name="title">Not supported internet browsers</ac:parameter><ac:rich-text-body><p>Cameo Collaborator for Teamwork Cloud does not support Internet Explorer. Use a different internet browser instead.</p></ac:rich-text-body></ac:structured-macro></li><li>In the app bar of the document portal, click <ac:image><ri:attachment ri:filename="plugins.png" /></ac:image> and select <strong>Resources</strong>.</li></ul></li><li>Go to the category containing the Cameo Collaborator document you want to share.</li><li>Click <ac:image><ri:attachment ri:filename="menu.png" /></ac:image> next to the document, and do one of the following and select <strong>Get resource link</strong>.</li><li><p>If you want to copy a public link, in the open window, turn on the <strong>Public</strong> switch as shown below.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c7e7e937-5448-4ed0-bbda-2a809cb183ac"><ac:parameter ac:name="title">Prerequisite for public links</ac:parameter><ac:rich-text-body><p>For public links to work, the Guest user needs to be configured for Teamwork Cloud. For more information, refer to <ac:link><ri:page ri:content-title="Setting up Guest User" /><ac:plain-text-link-body><![CDATA[Setting up Guest user]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p><br /><ac:image><ri:attachment ri:filename="public_link.png" /></ac:image></p></li><li>Click <strong>Copy</strong> button.</li></ol><p><br />After you complete the above steps, the link to a document is copied to your clipboard and you can share it with reviewers.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180782 space=TWCloud2024xR1 version=3 -->
## PAGE 00231: Simulation in Cameo Collaborator for Teamwork Cloud

- page_id: `171180782`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180782/Simulation+in+Cameo+Collaborator+for+Teamwork+Cloud
- version_number: 3
- version_date: `2024-06-07T10:01:56.022+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Simulation in Cameo Collaborator for Teamwork Cloud' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="be3a7fb7-76df-4d7e-8aba-1479996fa397"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation in Cameo Collaborator for Teamwork Cloud" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=171180781 space=TWCloud2024xR1 version=3 -->
## PAGE 00232: Simulation in the Resources application

- page_id: `171180781`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180781/Simulation+in+the+Resources+application
- version_number: 3
- version_date: `2024-06-07T10:01:41.369+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Simulation in the Resources application' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="62c22c67-9443-471d-a190-cdc16f7c3d6d"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation in the Resources application" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=171180778 space=TWCloud2024xR1 version=3 -->
## PAGE 00233: Simulation using Jupyter Notebook

- page_id: `171180778`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180778/Simulation+using+Jupyter+Notebook
- version_number: 3
- version_date: `2024-06-07T10:00:17.312+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Simulation using Jupyter Notebook' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="89fbd420-2715-4b7f-ba4c-9204a20eb9de"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation using Jupyter Notebook" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=171180777 space=TWCloud2024xR1 version=3 -->
## PAGE 00234: Simulation using REST API

- page_id: `171180777`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180777/Simulation+using+REST+API
- version_number: 3
- version_date: `2024-06-07T09:59:45.758+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Simulation using REST API' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="d506a364-1dec-414f-ab0e-7539a1fd6ac7"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation using REST API" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=171180783 space=TWCloud2024xR1 version=3 -->
## PAGE 00235: Simulation with UI

- page_id: `171180783`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180783/Simulation+with+UI
- version_number: 3
- version_date: `2024-06-07T10:02:11.621+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Server-side simulation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Simulation with UI' space='CST2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="f9f218a9-e36e-4789-8a14-a076149f22d2"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation with UI" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170491316 space=TWCloud2024xR1 version=4 -->
## PAGE 00236: Solution for long-running tasks

- page_id: `170491316`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491316/Solution+for+long-running+tasks
- version_number: 4
- version_date: `2026-01-28T10:55:56.453+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Enterprise deployment > Building Web Application Platform containers
- labels: []

### NORMALIZED CONTENT

**On this page**

5

Some of the functionalities provided by Web Application Platform are long-running tasks that take longer time periods and machine resources to be executed. One notable example is exporting Cameo Collaborator documents to various formats (pdf, html) that is provided by the Document Exporter web application. It is possible to deploy such applications on a separate web container instance to withdraw load from the server where remaining web applications are deployed.

To make the solution scalable, you can use the Docker as the container platform to run web applications. For example, you can run a single instance of Web Application Platform applications on one Tomcat instance and run one or more instances of the Document Exporter as the Docker containers.

To run a Docker container

1. [CONFLUENCE_PAGE title='Building Web Application Platform containers' space=''] .
2. Specify the external host/port information as the value of the service.uri parameter in the webappplatform.properties file. This host/port must be accessible from the outside of the Docker container (e.g., from a user‘s browser).
3. If needed, run multiple instances of the web application simultaneously and manage them using, for example, container orchestration tools.

The following section provides an example how to create a container for the Document Exporter web application.

##### Creating a container for Document Exporter

This section provides an example how to create a container for the Document Exporter web application.

To create a container for Document exporter

1. Prepare a Dockerfile for the Document Exporter with image build instructions. For simplicity, the *webappplatform.properties* file will be copied to the Tomcat classpath within the container. > ${SET_ENV_FILE} && \
 chmod o+x ${SET_ENV_FILE} && \
 groupadd --gid ${USER_GID} tomcat && \
 useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
 chown -R tomcat:tomcat ${TOMCAT_DIR} && \
 chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
 rm -rf webapps.dist && \ 
 apt-get update -y && \
 apt install dialog apt-utils -y && \
 echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
 apt-get install ttf-mscorefonts-installer -y && \
 apt-get clean
 
USER tomcat

EXPOSE 8080
CMD ["catalina.sh", "run"]]]> For the correct version of Tomcat and JRE, please check the [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''] page.
2. Put the following files in a single directory:
  - Dockerfile
  - document-exporter.war
  - logback.xml
  - webappplatform.properties
  - templates.zip that contains templates used during export
3. Use the following command to build the Docker image:
4. Run the container on port 8080 by executing the following command:

To test that if Document Exporter is accessible, send a request to this address://<host>:8080/document-exporter. If the container runs and the application is successfully started, a 404 page should be displayed with a custom error text and image.

##### Scaling Document Exporter

This section does not cover a particular scaling method. You can choose it based on the infrastructure available and your own preferences. There are several ways to scale the containerized Document Exporter application:

- If a container orchestration tool is used to run Docker containers, it will provide means to create multiple instances of the container and take care of their management.
- You can create multiple containers manually and involve other network tools for management, e.g., a load balancer.

You need to have sticky sessions for the scaling to work.

##### Fonts

When a document is exported to the pdf format, fonts are required to be installed on the OS where the document is being generated. If fonts installed on the OS and used for creating models and fonts of the deployment OS are different, you may need to install additional fonts. For example, if the deployment OS is Linux-based, and models are created using a Windows version of the modeling tool, then Microsoft true type fonts should be installed to have an expected output.

**Microsoft True Type Fonts**

General instructions describing how to add Microsft True Type fonts to the Linux-based OS are provided in the [CONFLUENCE_PAGE title='Exporting documents to PDF and HTML' space=''] chapter. However, the installation of the fonts depends on the Docker container OS. Assuming that font files are pre-downloaded and put to the *msttcore* folder, this folder can be moved to the folder with the Dockerfile. Then you can copy fonts to the Linux font folder by using the following script:

#### PANEL: Dockerfile example

lightgrey

solid

Dockerfile example

FROM tomcat:x.x.x-jrexx-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat 
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh 
ARG USER_UID=5000 
ARG USER_GID=${USER_UID}

COPY logback.xml ${TOMCAT_DIR}/shared/conf/ 
COPY document-exporter.war ${TOMCAT_DIR}/webapps/ 
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/ 
COPY data ${TOMCAT_DIR}/shared/conf/data

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \ 
 echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \ 
 chmod o+x ${SET_ENV_FILE} && \ 
 groupadd --gid ${USER_GID} tomcat && \ 
 useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \ 
 chown -R tomcat:tomcat ${TOMCAT_DIR} && \ 
 chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \ 
 rm -rf webapps.dist && \ 
 apt-get update -y && \ 
 apt install dialog apt-utils -y && \ 
 **echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \** 
 **apt-get install ttf-mscorefonts-installer -y && \** 
 apt-get clean 
 
USER tomcat

EXPOSE 8080 
CMD ["catalina.sh", "run"]

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f75ca596-5e32-44ec-8c32-fdab1838718e"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Some of the functionalities provided by Web Application Platform are long-running tasks that take longer time periods and machine resources to be executed. One notable example is exporting Cameo Collaborator documents to various formats (pdf, html) that is provided by the Document Exporter web application. It is possible to deploy such applications on a separate web container instance to withdraw load from the server where remaining web applications are deployed.</p><p>To make the solution scalable, you can use the Docker as the container platform to run web applications. For example, you can run a single instance of Web Application Platform applications on one Tomcat instance and run one or more instances of the Document Exporter as the Docker containers.</p><p><br /></p><p>To run a Docker container</p><hr /><ol><li><ac:link><ri:page ri:content-title="Building Web Application Platform containers" /><ac:plain-text-link-body><![CDATA[Create a Dockerfile for a web application]]></ac:plain-text-link-body></ac:link>.</li><li>Specify the external host/port information as the value of the <strong>service.uri</strong> parameter in the <em>webappplatform.properties</em> file. This host/port must be accessible from the outside of the Docker container (e.g., from a user‘s browser).</li><li>If needed, run multiple instances of the web application simultaneously and manage them using, for example, container orchestration tools.</li></ol><p><br />The following section provides an example how to create a container for the Document Exporter web application.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Creating a container for Document Exporter</h3><p>This section provides an example how to create a container for the Document Exporter web application.</p><p><br /></p><p>To create a container for Document exporter</p><hr /><ol><li><p class="auto-cursor-target"><ac:inline-comment-marker ac:ref="414c2ab9-1d5c-47ea-879a-0d973d2e4f0f">Prepare a Dockerfile</ac:inline-comment-marker> for the Document Exporter with image build instructions. For simplicity, the <em style="letter-spacing: 0.0px;">webappplatform.properties</em> file will be copied to the Tomcat classpath within the container.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b74ea99a-058e-458c-8f35-7cf1e6a2e403"><ac:plain-text-body><![CDATA[FROM tomcat:x.x.x-jrexx-temurin-jammy

ARG TOMCAT_DIR=/usr/local/tomcat
ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh
ARG USER_UID=5000
ARG USER_GID=${USER_UID}

COPY logback.xml ${TOMCAT_DIR}/shared/conf/
COPY document-exporter.war ${TOMCAT_DIR}/webapps/
COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/
COPY data ${TOMCAT_DIR}/shared/conf/data

RUN sed -i "s|shared\.loader=*$|shared\.loader=\"\${catalina.base}/shared/conf\"|" ${TOMCAT_DIR}/conf/catalina.properties && \
    echo 'export JAVA_OPTS="$JAVA_OPTS ${WEBAPP_PROPERTIES}"' >> ${SET_ENV_FILE} && \
    chmod o+x ${SET_ENV_FILE} && \
    groupadd --gid ${USER_GID} tomcat && \
    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c "Tomcat user" tomcat && \
    chown -R tomcat:tomcat ${TOMCAT_DIR} && \
    chown -R root:root ${TOMCAT_DIR}/bin/*.sh && \
    rm -rf webapps.dist && \    
    apt-get update -y && \
    apt install dialog apt-utils -y && \
    echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections && \
    apt-get install ttf-mscorefonts-installer -y && \
    apt-get clean
	
USER tomcat

EXPOSE 8080
CMD ["catalina.sh", "run"]]]></ac:plain-text-body></ac:structured-macro><br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d0093cdc-9c14-405a-aaef-a072f3178eb1"><ac:rich-text-body><p>For the correct version of Tomcat and JRE, please check the <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /></ac:link> page.</p></ac:rich-text-body></ac:structured-macro></li><li>Put the following files in a single directory:<br /><ul><li><em>Dockerfile</em></li><li><em>document-exporter.war</em></li><li><em>logback.xml</em></li><li><em>webappplatform.properties</em></li><li><em>templates.zip</em> that contains templates used during export</li></ul></li><li><p class="auto-cursor-target">Use the following command to build the Docker image:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="88f5ac29-df0d-4284-badd-f79ca32b40a8"><ac:plain-text-body><![CDATA[docker build --tag document-exporter .]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Run the container on port 8080 by executing the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="4358b400-d36e-41a0-b1ca-e68fa20e05dd"><ac:plain-text-body><![CDATA[docker run -p 8080:8080 document-exporter]]></ac:plain-text-body></ac:structured-macro></li></ol><p>To test that if Document Exporter is accessible, send a request to this address://&lt;host&gt;:8080/document-exporter. If the container runs and the application is successfully started, a 404 page should be displayed with a custom error text and image.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Scaling Document Exporter</h3><p><ac:inline-comment-marker ac:ref="5c79af74-1293-4e73-b7d4-8b7ad0bf1ecd">This section does not cover a particular scaling method. You can choose it based on the infrastructure available and your own preferences. There are several ways to scale the containerized Document Exporter application:</ac:inline-comment-marker></p><ul><li>If a container orchestration tool is used to run Docker containers, it will provide means to create multiple instances of the container and take care of their management.</li><li>You can create multiple containers manually and involve other network tools for management, e.g., a load balancer.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="796883bd-cd63-46ce-b86c-b6bbafe4458a"><ac:rich-text-body><p>You need to have sticky sessions for the scaling to work.</p></ac:rich-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);"><br />Fonts</h3><p>When a document is exported to the pdf format, fonts are required to be installed on the OS where the document is being generated. If fonts installed on the OS and used for creating models and fonts of the deployment OS are different, you may need to install additional fonts. For example, if the deployment OS is Linux-based, and models are created using a Windows version of the modeling tool, then Microsoft true type fonts should be installed to have an expected output.<br /><br /></p><p><strong>Microsoft True Type Fonts</strong></p><p>General instructions describing how to add Microsft True Type fonts to the Linux-based OS are provided in the <ac:link><ri:page ri:content-title="Exporting documents to PDF and HTML" /></ac:link> chapter. However, the installation of the fonts depends on the Docker container OS. Assuming that font files are pre-downloaded and put to the <em>msttcore</em> folder, this folder can be moved to the folder with the Dockerfile. Then you can copy fonts to the Linux font folder by using the following script:</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0f69545a-5114-49f4-bc05-50a2ac024b02"><ac:parameter ac:name="borderColor">lightgrey</ac:parameter><ac:parameter ac:name="borderStyle">solid</ac:parameter><ac:parameter ac:name="title">Dockerfile example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">FROM tomcat:x.x.x-jrexx-temurin-jammy</span></p><p>ARG TOMCAT_DIR=/usr/local/tomcat<br />ARG SET_ENV_FILE=/usr/local/tomcat/bin/setenv.sh<br />ARG USER_UID=5000<br />ARG USER_GID=${USER_UID}</p><p>COPY logback.xml ${TOMCAT_DIR}/shared/conf/<br />COPY document-exporter.war ${TOMCAT_DIR}/webapps/<br />COPY webappplatform.properties ${TOMCAT_DIR}/shared/conf/<br />COPY data ${TOMCAT_DIR}/shared/conf/data</p><p>RUN sed -i &quot;s|shared\.loader=*$|shared\.loader=\&quot;\${catalina.base}/shared/conf\&quot;|&quot; ${TOMCAT_DIR}/conf/catalina.properties &amp;&amp; \<br />    echo 'export JAVA_OPTS=&quot;$JAVA_OPTS ${WEBAPP_PROPERTIES}&quot;' &gt;&gt; ${SET_ENV_FILE} &amp;&amp; \<br />    chmod o+x ${SET_ENV_FILE} &amp;&amp; \<br />    groupadd --gid ${USER_GID} tomcat &amp;&amp; \<br />    useradd -r --uid ${USER_UID} --gid ${USER_GID} -s /sbin/nologin -d ${TOMCAT_DIR} -c &quot;Tomcat user&quot; tomcat &amp;&amp; \<br />    chown -R tomcat:tomcat ${TOMCAT_DIR} &amp;&amp; \<br />    chown -R root:root ${TOMCAT_DIR}/bin/*.sh &amp;&amp; \<br />    rm -rf webapps.dist &amp;&amp; \    <br />    apt-get update -y &amp;&amp; \<br />    apt install dialog apt-utils -y &amp;&amp; \<br />    <strong>echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections &amp;&amp; \</strong><br />    <strong>apt-get install ttf-mscorefonts-installer -y &amp;&amp; \</strong><br />    apt-get clean<br /><br />USER tomcat</p><p>EXPOSE 8080<br />CMD [&quot;catalina.sh&quot;, &quot;run&quot;]</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491769 space=TWCloud2024xR1 version=1 -->
## PAGE 00237: Sorting users and user groups

- page_id: `170491769`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491769/Sorting+users+and+user+groups
- version_number: 1
- version_date: `2023-07-07T08:50:44.956+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

Sort users according to their username or group name (click **Username**or**Name** for group) or last activity date (click **Last activity date**).

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Sort users according to their <ac:inline-comment-marker ac:ref="9a69f839-0622-49c3-be55-3f87573f4d84">usernam</ac:inline-comment-marker>e or group name (click <strong>Username </strong>or<strong> Name</strong> for group) or last activity date (click <strong>Last activity date</strong>).</p><p style="text-align: center;"><ac:image ac:align="left"><ri:attachment ri:filename="Sorting_users.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Sorting users and user groups" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=170491486 space=TWCloud2024xR1 version=2 -->
## PAGE 00238: Starting and Stopping Web Application Platform

- page_id: `170491486`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491486/Starting+and+Stopping+Web+Application+Platform
- version_number: 2
- version_date: `2025-09-03T10:22:46.926+02:00`
- ancestors: Teamwork Cloud and Services > Administration Guide > Web Application Platform Administration
- labels: []

### NORMALIZED CONTENT

**On this page**

4

This chapter explains how to start and stop Web Application Platform as a service. See the sections below to find the instructions applicable to your operating system.

To be able to start or stop Web Application Platform, services must be installed.

##### Starting and stopping Web Application Platform on Linux

When using Linux, you can start and stop Web Application Platform as described below.

To start/stop Web Application Platform on Linux

1. Use the terminal to do one of the following:
  - To start Web Application platform, execute one of the following commands: For systemd system and service manager
  - To stop Web Application platform, execute one of the following commands: For systemd system and service manager

Web Application Platform is started or stopped depending on which command you execute.

##### Starting and stopping Web Application Platform on Windows

When using Windows OS, you can start and stop Web Application Platform as described below.

To start/stop Web Application Platform on Windows

1. Open Windows Service Manager.
2. Find the CATIA No Magic WebApp Service and start/stop it.

**Related pages**

- [CONFLUENCE_PAGE title='Installing Web Application Platform on Windows' space='']
- [CONFLUENCE_PAGE title='Installing Web Application Platform on Linux with GUI' space='']
- [CONFLUENCE_PAGE title='Using no-installer' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="75497544-e5d3-4cbd-9f38-1a2d77090347"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This chapter explains how to start and stop Web Application Platform as a service. See the sections below to find the instructions applicable to your operating system.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ecd3491b-4ecc-4452-946e-63670a61ba4d"><ac:rich-text-body><p>To be able to start or stop Web Application Platform, services must be installed.</p></ac:rich-text-body></ac:structured-macro><h3><br />Starting and stopping Web Application Platform on Linux</h3><p>When using Linux, you can start and stop Web Application Platform as described below.</p><p><br /></p><p>To start/stop Web Application Platform on Linux</p><hr /><ol><li>Use the terminal to do one of the following:<br /><ul><li><p class="auto-cursor-target">To start Web Application platform, execute one of the following commands:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d75da47d-5d01-42c5-9a2f-9a92c61b20d2"><ac:parameter ac:name="title">For systemd system and service manager</ac:parameter><ac:plain-text-body><![CDATA[service webapp start
OR
systemctl start webapp]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">To stop Web Application platform, execute one of the following commands:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5186bb7d-d482-4d6b-be32-b9999f4d7859"><ac:parameter ac:name="title">For systemd system and service manager</ac:parameter><ac:plain-text-body><![CDATA[service webapp stop
OR
systemctl stop webapp]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li></ol><p>Web Application Platform is started or stopped depending on which command you execute.</p><h3><br />Starting and stopping Web Application Platform on Windows</h3><p>When using Windows OS, you can start and stop Web Application Platform as described below.</p><p><br /></p><p>To start/stop Web Application Platform on Windows</p><hr /><ol><li>Open Windows Service Manager.</li><li> Find the <strong style="letter-spacing: 0.0px;">CATIA No Magic WebApp Service</strong><span style="letter-spacing: 0.0px;"> and start/stop it.</span></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Installing Web Application Platform on Windows" /></ac:link></li><li><ac:link><ri:page ri:content-title="Installing Web Application Platform on Linux with GUI" /></ac:link></li><li><ac:link><ri:page ri:content-title="Using no-installer" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491257 space=TWCloud2024xR1 version=3 -->
## PAGE 00239: Starting Teamwork Cloud on Windows

- page_id: `170491257`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491257/Starting+Teamwork+Cloud+on+Windows
- version_number: 3
- version_date: `2025-10-30T13:36:51.786+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Installation on Windows
- labels: []

### NORMALIZED CONTENT

For Teamwork Cloud to operate, the Cassandra database must already be running.

To start Teamwork Cloud on Windows

1. Open the Windows Services panel.
2. Locate the Zookeeper service and start it.
3. Locate the Teamwork Cloud service and start it. (As with a normal startup, Cassandra must already be running).
4. Locate the WebApp service and start it. Before you start the WebApp service, make sure that the Teamwork Cloud service is successfully started.

To stop Teamwork Cloud on Windows

1. Open the Windows Services panel.
2. Locate the Teamwork Cloud service and stop it.
3. Locate the WebApp service and stop it.
4. Locate the Zookeeper service and stop it.

The services may take a long time to stop, please be patient.

To get started working with Teamwork Cloud in MagicDraw and using Teamwork Cloud Admin, you need to [CONFLUENCE_PAGE title='Accessing Teamwork Cloud web applications' space=''] to [CONFLUENCE_PAGE title='Applying Teamwork Cloud license' space=''] so that you can enable other users to [CONFLUENCE_PAGE title='Using Teamwork Cloud' space='MD2024xR1'] and Teamwork Cloud Admin. To start the collaboration session, you need to [CONFLUENCE_PAGE title='Starting a collaboration session' space='MD2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>For Teamwork Cloud to operate, the Cassandra database must already be running.</p><p>To start Teamwork Cloud on Windows</p><hr /><ol><li data-uuid="0c803e2a-593c-43a1-b283-e356c8cccc86">Open the Windows Services panel.</li><li data-uuid="9007b926-7e75-4d64-915c-183e3dfaef5c">Locate the Zookeeper service and start it.</li><li data-uuid="34ccb292-4324-42c6-9026-d110a0b07eaa">Locate the Teamwork Cloud service and start it. (As with a normal startup, Cassandra must already be running).</li><li data-uuid="760bf0c1-f5ed-4b69-9bd0-576b5dbf5454"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Locate the WebApp service and start it.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="06fdc29f-b163-4108-9222-fcf164b166f5"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">Before you start the WebApp service, make sure that the Teamwork Cloud service is successfully started. </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);"> </span></p></li></ol><p>To stop Teamwork Cloud on Windows</p><hr /><ol><li data-uuid="df77609a-402d-4fe9-a277-38fb98a4c624">Open the Windows Services panel.</li><li data-uuid="5f89da83-5fd6-4586-bb8e-46124dc993bc">Locate the Teamwork Cloud service and stop it.</li><li data-uuid="4dea0c48-0c44-4034-afc0-8646c2c558cb"><span style="color:var(--ds-text,#333333);">Locate the WebApp service and stop it.</span></li><li data-uuid="16de30da-ace5-422c-b162-64378ec4ab08"><span style="color:var(--ds-text,#333333);">Locate the Zookeeper service and stop it.</span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="27be2edd-edf9-4403-886b-beebe489b881"><ac:rich-text-body><p>The services may take a long time to stop, please be patient.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To get started working with Teamwork Cloud in MagicDraw and using Teamwork Cloud Admin, you need to <ac:link><ri:page ri:content-title="Accessing Teamwork Cloud web applications" /><ac:plain-text-link-body><![CDATA[access Teamwork Cloud Admin]]></ac:plain-text-link-body></ac:link> to <ac:link><ri:page ri:content-title="Applying Teamwork Cloud license" /><ac:plain-text-link-body><![CDATA[apply the Teamwork Cloud license]]></ac:plain-text-link-body></ac:link> so that you can enable other users to <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[use Teamwork Cloud in MagicDraw]]></ac:plain-text-link-body></ac:link> and Teamwork Cloud Admin. To start the collaboration session, you need to <span style="color:var(--ds-text,#333333);"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Starting a collaboration session" /><ac:plain-text-link-body><![CDATA[log in to a server.]]></ac:plain-text-link-body></ac:link></span></p>
````

<!--NOMAGIC_PAGE id=171180464 space=TWCloud2024xR1 version=2 -->
## PAGE 00240: Structure of the document portal

- page_id: `171180464`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180464/Structure+of+the+document+portal
- version_number: 2
- version_date: `2025-10-31T09:12:05.138+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: ['panes', 'structure-of-published-project-page']

### NORMALIZED CONTENT

The Cameo Collaborator for Teamwork Cloud document portal consists of:

- [CONFLUENCE_PAGE title='App bar' space='']
- [CONFLUENCE_PAGE title='Navigation pane' space='']
- [CONFLUENCE_PAGE title='Content pane' space='']
- [CONFLUENCE_PAGE title='Comments pane' space='']Comments pane

The titles and colors in the document portal may differ, depending on the applied [CONFLUENCE_PAGE title='Document templates' space=''].

[IMAGE alt='' src='']

###### A published model portal.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Cameo Collaborator for Teamwork Cloud document portal consists of:</p><ul><li><ac:link><ri:page ri:content-title="App bar" /></ac:link></li><li><ac:link><ri:page ri:content-title="Navigation pane" /></ac:link></li><li><ac:link><ri:page ri:content-title="Content pane" /></ac:link></li><li><ac:link><ri:page ri:content-title="Comments pane" /><ac:link-body>Comments pane<br /> </ac:link-body></ac:link></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b498f1e4-d00b-49c0-b2cf-919774877389"><ac:rich-text-body><p>The titles and colors in the document portal may differ, depending on the applied <ac:link><ri:page ri:content-title="Document templates" /><ac:plain-text-link-body><![CDATA[template]]></ac:plain-text-link-body></ac:link><ac:inline-comment-marker ac:ref="67bed32a-9d64-44be-90e1-4ce20b4ab322">.</ac:inline-comment-marker></p></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="published_model_portal.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">A published model portal.</h6>
````

<!--NOMAGIC_PAGE id=171180631 space=TWCloud2024xR1 version=2 -->
## PAGE 00241: Subscribing to email notifications

- page_id: `171180631`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180631/Subscribing+to+email+notifications
- version_number: 2
- version_date: `2024-11-26T16:01:05.977+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['subscribe-to-email-notifications', 'unsubscribe-from-email-notifications', 'email-notifications']

### NORMALIZED CONTENT

**On this page**

5

Cameo Collaborator for Teamwork Cloud allows you to subscribe to email notifications about all new and modified comments in a Cameo Collaborator document. Once subscribed, you get email notifications as soon as:

- A new comment is created
- A comment has a new reply
- A comment is edited (for example, when a subject or priority is changed)
- A comment's status changes (resolved or unresolved)

As you see in the example below, an email notification displays the entire conversation thread. Also, you can navigate to the commented item in a document right from the email notification.

#### TIP: Customizing email templates

Customizing email templates

Email templates are customizable and can be modified according to your needs. You can find them in the *Web_App_Platform_installation_directory\apache-tomcat\shared\conf\data\collaborator\email* directory.

##### [IMAGE alt='' src='']

###### An example of an email notification.

You can subscribe to or unsubscribe from email notifications about comment changes in a certain document as described below.

#### Prerequisites

To receive email notifications, ensure that:

- Your email address is included in your user account details (in the [CONFLUENCE_PAGE title='My account application' space=''] );
- The platform mailing engine is configured correctly. For more information, see [CONFLUENCE_PAGE title='Configuring email notifications for services' space=''] . You may also need to contact your system administrator.

#### Subscribing to email notifications

To subscribe to/unsubscribe from email notifications in a Cameo Collaborator document

1. [CONFLUENCE_PAGE title='Opening a resource' space=''] that you want to get email notifications about.
2. Click [ATTACHMENT filename='menu.png'] on the right side of the app bar and select one of the following:
  - Subscribe to email notifications - to subscribe to email notifications.
  - Unsubscribe from email notifications - to unsubscribe from email notifications.

#### Unsubscribing from email notifications

To subscribe to/unsubscribe from email notifications in the Resources application

1. Open the Resources application and find the Cameo Collaborator document you want to get email notifications about.
2. Click [ATTACHMENT filename='menu.png'] next to the document and select one of the following:
  - Subscribe to email notifications - to subscribe to email notifications.
  - Unsubscribe - to unsubscribe from email notifications.

Depending on your selection, you will start or stop getting email notifications about all new and edited comments in the document.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7c96cd23-7466-489e-9eef-e8d696bab914"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Cameo Collaborator for Teamwork Cloud allows you to subscribe to email notifications about all new and modified comments in a Cameo Collaborator document. Once subscribed, you get email notifications as soon as:</p><ul><li>A new comment is created</li><li>A comment has a new reply</li><li>A comment is edited (for example, when a subject or priority is changed)</li><li>A comment's status changes (resolved or unresolved)</li></ul><p>As you see in the example below, an email notification displays the entire conversation thread. Also, you can navigate to the commented item in a document right from the email notification.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="b356d2bd-d73a-42ad-b7b7-bffbae1c37b2"><ac:parameter ac:name="title">Customizing email templates</ac:parameter><ac:rich-text-body><p>Email templates are customizable and can be modified according to your needs. You can find them in the <em>Web_App_Platform_installation_directory\apache-tomcat\shared\conf\data\collaborator\email</em> directory.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3 style="text-align: center;"><ac:image><ri:attachment ri:filename="cc_email_notification.png" /></ac:image></h3><h6 style="text-align: center;">An example of an email notification.</h6><p>You can subscribe to or unsubscribe from email notifications about comment changes in a certain document as described below.</p><h2>Prerequisites</h2><p>To receive email notifications, ensure that:</p><ul><li>Your email address is included in your user account details (in the <ac:link><ri:page ri:content-title="My account application" /></ac:link>);</li><li>The platform mailing engine is configured correctly. For more information, see <ac:link><ri:page ri:content-title="Configuring email notifications for services" /></ac:link>. You may also need to contact your system administrator.</li></ul><h2>Subscribing to email notifications</h2><p>To subscribe to/unsubscribe from email notifications in a Cameo Collaborator document</p><hr /><ol><li><ac:link><ri:page ri:content-title="Opening a resource" /><ac:plain-text-link-body><![CDATA[Open the Cameo Collaborator document]]></ac:plain-text-link-body></ac:link> that you want to get email notifications about.</li><li>Click <ac:image><ri:attachment ri:filename="menu.png" /></ac:image> on the right side of the app bar and select one of the following:<ul><li><strong>Subscribe to email notifications</strong> - to subscribe to email notifications.</li><li><strong>Unsubscribe from email notifications</strong> - to unsubscribe from email notifications.</li></ul></li></ol><h2>Unsubscribing from email notifications</h2><p>To subscribe to/unsubscribe from email notifications in the Resources application</p><hr /><ol><li>Open the Resources application and find the Cameo Collaborator document you want to get email notifications about.</li><li>Click <ac:image><ri:attachment ri:filename="menu.png" /></ac:image> next to the document and select one of the following:<ul><li><strong>Subscribe to email notifications </strong>- to subscribe to email notifications.</li><li><strong>Unsubscribe</strong> - to unsubscribe from email notifications.</li></ul></li></ol><p><br />Depending on your selection, you will start or stop getting email notifications about all new and edited comments in the document.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491660 space=TWCloud2024xR1 version=2 -->
## PAGE 00242: Synchronizing users and user groups

- page_id: `170491660`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491660/Synchronizing+users+and+user+groups
- version_number: 2
- version_date: `2024-05-09T13:41:28.338+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

To synchronize external users/user groups through the **User application**

1. Go to the **User application**, click the [IMAGE alt='' src=''] and choose [IMAGE alt='' src=''] **Import users & groups.**
2. Select a LDAP server from which you want to synchronize users and groups.
3. In the search bar, type a username, group name or LDAP query, and press **Enter**. A list of usernames that matches the username or LDAP query will appear.
4. Choose one or more usernames/group names to synchronize by selecting the check box(es).
5. Click Import .

New users and groups will be imported. When the imported user is new, an external user will be created and the role assignment will be assigned to the user. If the user has been imported before, the existing user information will be updated but the role assignment stays the same.

Upon importing users and groups, you can copy roles and assignments from other users to them. See the section [Copying roles and assignment](https://docs.nomagic.com/display/TWCloud2024xR1/Copying+roles+and+assignments) for more information.

[IMAGE alt='' src='']

###### Different icons will help you to identify users or user groups which will be imported or synchronized.

To synchronize an external user group

1. Go to the Users application and from the left side users/user groups filter select User groups . Then, do one of the following:
  - Click a user group name and from the Group details card click Synchronize button.
  - Click [ATTACHMENT filename='menu.png'] and from the option list select Synchronize group.
2. Synchronization process starts.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To synchronize external users/user groups through the <strong>User application</strong></p><hr /><ol><li><p>Go to the <strong>User application</strong>, click the <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="Action_button.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Synchronizing users and user groups" /></ri:attachment></ac:image></span> and choose <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:width="32"><ri:attachment ri:filename="Users_import_button.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Synchronizing users and user groups" /></ri:attachment></ac:image></span> <strong>Import users &amp; groups. </strong></p></li><li>Select a LDAP server from which you want to synchronize users and groups.</li><li><p>In the search bar, type a username, group name or LDAP query, and press <strong>Enter</strong>. A list of usernames that matches the username or LDAP query will appear. </p></li><li>Choose one or more usernames/group names to synchronize by selecting the check box(es).</li><li>Click <strong>Import</strong>. </li></ol><p>New users and groups will be imported. When the imported user is new, an external user will be created and the role assignment will be assigned to the user. If the user has been imported before, the existing user information will be updated but the role assignment stays the same.</p><p>Upon importing users and groups, you can copy roles and assignments from other users to them. See the section <a href="https://docs.nomagic.com/display/TWCloud2024xR1/Copying+roles+and+assignments">Copying roles and assignment</a> for more information.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Sync_import_userandgroup.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Synchronizing users and user groups" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Different icons will help you to identify users or user groups which will be imported or synchronized. </h6><p>To synchronize an external user group</p><hr /><ol><li>Go to the <strong>Users </strong>application and from the left side users/user groups filter select <strong>User groups</strong>. Then, do one of the following:<strong> </strong><ul><li>Click a user group name and from the <strong>Group details</strong> card click <strong>Synchronize </strong>button.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Synchronizing users and user groups" /></ri:attachment></ac:image> and from the option list select <strong>Synchronize group.</strong></li></ul></li><li>Synchronization process starts. </li></ol>
````

<!--NOMAGIC_PAGE id=170491190 space=TWCloud2024xR1 version=1 -->
## PAGE 00243: System architecture and design

- page_id: `170491190`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491190/System+architecture+and+design
- version_number: 1
- version_date: `2023-07-07T08:50:19.891+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: []

### NORMALIZED CONTENT

Teamwork Cloud is focused on the capability of creating highly scalable systems and collaborative modeling environments.

Scalability refers to the ability of Teamwork Cloud to support any number or type of internal or external users with larger volumes of data and applications. The purpose of scalability is to support potential growth of storage within the business without impacting performance. Teamwork Cloud is also dedicated to effectively integrate with MagicDraw by extending all of the capabilities of Teamwork Server to provide a collaborative modeling environment where multiple users across different platforms will be able to work on a model at the same time without concerns about data consistency and availability.

Teamwork Cloud is a model repository that is deployable as either a single-node server or multiple node servers (see the following figures).

[IMAGE alt='' src='']

###### A single-node server model repository.

A cluster is a group of servers working as a single consistent model repository. Clustering is transparent to the clients of the repository. Compared with single node-deployments, a cluster deployment has higher capacity, improved reliability, or both. A cluster can either use replication to increase reliability and enable failover, or it can simply increase the storage and processing capacity of the cluster.

[IMAGE alt='' src='']

###### A cluster node server model repository

A cluster consists of multiple servers connected through LAN, acting as a single repository. A server is a single computer which is part of a cluster and a client is a computer running, for example, MagicDraw, that accesses data in a repository, but is not part of the cluster.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>Teamwork Cloud is focused on the capability of creating highly scalable systems and collaborative modeling environments.</span></p><p>Scalability refers to the ability of Teamwork Cloud to support any number or type of internal or external users with larger volumes of data and applications. The purpose of scalability is to support potential growth of storage within the business without impacting performance. Teamwork Cloud is also dedicated to effectively integrate with MagicDraw by extending all of the capabilities of Teamwork Server to provide a collaborative modeling environment where multiple users across different platforms will be able to work on a model at the same time without concerns about data consistency and availability.</p><p>Teamwork Cloud is a model repository that is deployable as either a single-node server or multiple node servers (see the following figures). </p><p><ac:image ac:align="center"><ri:attachment ri:filename="single_node_server.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="System architecture and design" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A single-node server model repository.</h6><p>A cluster is a group of servers working as a single consistent model repository. Clustering is transparent to the clients of the repository. Compared with single node-deployments, a cluster deployment has higher capacity, improved reliability, or both. A cluster can either use replication to increase reliability and enable failover, or it can simply increase the storage and processing capacity of the cluster.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="multiple_node_servers.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="System architecture and design" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A cluster node server model repository</h6><p>A cluster consists of multiple servers connected through LAN, acting as a single repository. A server is a single computer which is part of a cluster and a client is a computer running, for example, MagicDraw, that accesses data in a repository, but is not part of the cluster.</p><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170491193 space=TWCloud2024xR1 version=16 -->
## PAGE 00244: System requirements

- page_id: `170491193`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491193/System+requirements
- version_number: 16
- version_date: `2026-03-30T11:54:32.384+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: []

### NORMALIZED CONTENT

**On this page**

4

#### EXCERPT: If deploying on Amazon EC2

INLINE

Before installing Teamwork Cloud, ensure that the system requirements described in this chapter are met.

##### Recommended system and storage requirements

#### NOTE: Multi-Node Clusters

Note on system requirements

System requirements are dictated by the intended deployment, taking into account the overall load which the environment will experience, including:

- Number of concurrent users
- Level of activity (commits) per day
- Overall number and size of the projects stored in Teamwork Cloud.

The database (Cassandra) can be located on the same server as Teamwork Cloud or on a separate server. Storage requirements apply only to the node where the database is located. The product hosting nodes can be virtualized without any issues if the host is not oversubscribed on its resources.

#### INFO: Multi-Node Clusters

Multi-Node Clusters

Recommended minimum sizing stated above applies to each node in a multi-node cluster.

#### NOTE: Note on storage requirements

Note on storage requirements

For on-premises deployment, Apache Cassandra is designed to run on multiple independent servers. Each Cassandra node should have Directly Attached Storage (DAS) composed of NVMe drives for optimum performance. Traditional network-attached storage solutions that rely on IP-based connections (iSCSI, NFS, or SAN) are not recommended for on-premises deployments, as they introduce additional latencies and anti-patterns. To learn more, see the following topics:

- Apache Cassandra Hardware Choices
- DataStax Apache Cassandra Capacity Planning Guide

For cloud deployment, use storage technologies that have been benchmarked for Cassandra. Modern solid-state/flash arrays with fast interconnects are preferred. Note that Teamwork Cloud is not compatible with managed Cassandra services, such as Amazon Keyspaces. To learn more, see the following topics:

- AWS EBS Cassandra Best Practices
- DataStax AWS EC2 Recommendations

| Resource requirements by deployment type |  |  |
| --- | --- | --- |
| Deployment type | Recommended system requirements | Recommended storage requirements |
| Teamwork Cloud AND Cassandra on Linux | 96 -128 GB ECC RAM>=16 processor threads (equivalent or better than the Intel Xeon E-2278G, or their AMD counterparts, supporting x86-64 architecture)1TB NVMe/SSD DAS storage | 3 Solid State Drives with high IOPS (recommended ~400K)NVMe or SSD drives are highly suitable due to their low latency and high throughput. 3 separate disk mountsData, commit logs, and applications have different access patterns and should reside on separate disks to avoid I/O contention. For a detailed example, please see |
| Only Cassandra (Linux only) | 48 - 64 GB ECC RAM>=8 processor threads (equivalent or better than the Intel Xeon E-2234, or their AMD counterparts, supporting x86-64 architecture)1TB NVMe/SSD DAS storage |  |
| Only Teamwork Cloud | 48 - 64 GB ECC RAM>=8 processor threads (equivalent or better than the Intel Xeon E-2234, or their AMD counterparts, supporting x86-64 architecture)>250GB storage |  |
| Web Application Platform for small and medium deployments (5, 10, 25, or 50 connection licenses) | 32 GB of RAM dedicated exclusively to Web Application Platform services and additional RAM per OS requirementsCPU with 8 cores running at 2.1 GHzFor deployments on Linux, the open file limit must be no less than 20,000 files. | 100 GB of free space on the disk, NVMe or SSD |
| Web Application Platform for large enterprise deployments (75, 100, or unlimited connection licenses) | 64 GB of RAM dedicated exclusively to Web Application Platform services and additional RAM per OS requirementsCPU with 16 cores running at 2.1 GHzFor deployments on Linux, the open file limit must be no less than 20,000 files. | 200 GB of free space on the disk, NVMe or SSD |

#### NOTE: Deployments with unlimited licenses

Deployments with unlimited licenses

If you have a deployment with an unlimited license or are in doubt about what hardware to use, contact your account executive for hardware recommendations to accommodate your specific needs.

#### NOTE: Note on Web Application Platform

Note on Web Application Platform

When installing Web Application Platform for production purposes, it is recommended to [CONFLUENCE_PAGE title='Web Application Platform Installation on a separate machine' space=''].

##### Software requirements

Teamwork Cloud supports the following operating systems:

- Linux 64-bit RedHat 8, RedHat 9, Oracle Linux 8.
- Windows 2016 or Windows 2019.

The Linux operating system is highly recommended for Teamwork Cloud deployment. Cassandra 4 does not have native Windows support.

For a fully working environment, you will also need the following:

- Cassandra (check the compatible version [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''])
- Java compatible with Teamwork Cloud (twcloud service) and Cassandra (check version [CONFLUENCE_PAGE title='Third-Party Component Compatibility' space=''])
- **IMPORTANT**. To use modeling tools with DSLS licenses,Microsoft Visual C++ Redistributable must be installed (see[Latest supported Visual C++ Redistributable downloads](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)). This applies to Windows OS only.
- [CONFLUENCE_PAGE title='FlexNet license server installation and licensing' space='ILTWRT'] or [CONFLUENCE_PAGE title='DSLS installation and licensing' space='ILTWRT'] license server
- A static IP address for each node.
- Open ports 1101, 2181, 2552, 4085, 7000, 7001, 7199, 9042, and 9142 between servers in a cluster.
- Open ports 3579, 8111, 8443, and 10002 (default) for clients. The port number 10002 can be changed according to the port assigned to secure connections between the client software and Teamwork Cloud.

The following table lists the ports that Teamwork Cloud services use and their descriptions. Port traffic is TCP unless otherwise specified.

| Service | Port | Description |
| --- | --- | --- |
| FlexNet server (lmadmin) | 1101 | FLEXnet server port |
|  | 8090 | License management web interface HTTP port |
|  | 27000-27009 | Internal license server manager port |
|  |  |  |
| DSLS (Dassault Systèmes License Server) | 4085 | DSLS licensing server port |
|  |  |  |
| Cassandra | 7000 | Internode cluster communication port (not used if TLS is enabled) |
|  | 7199 | JMX monitoring port of the Cassandra node |
|  | 9042 | Native client port for processing database operations |
|  |  |  |
| Teamwork Cloud | 2468 | JMX metrics reporting port for monitoring stack |
|  | 2552 | Teamwork Cloud default remote server port |
|  | 3579 | Default Teamwork Cloud port when SSL is not enabled |
|  | 8111 | REST API HTTPS port |
|  | 10002 | Default port for encrypted TLS client-server communication. |
|  |  |  |
| Web Application Platform | 8443 | Web Application Platform HTTPS port (Authentication, Collaborator…) |
|  |  |  |
| Zookeeper | 2181 | Zookeeper internal port |

#### INFO: If deploying on Amazon EC2

If deploying on Amazon EC2

When deploying on

, we recommend using the

, r5-2xlarge, or i3-2xlarge instances. Depending on the workload, you may want to go to the -4xlarge instances, but for most users, the -2xlarge will suffice. The m5 instances meet the minimum system requirements and will be acceptable for small deployments. The r5 instances provide more memory for the same CPU density. The i3 instances should be used when workloads have a higher level of user concurrency due to the significantly improved performance of the ephemeral NVMe storage.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="440a79eb-3439-4cea-a4f7-0b97a272f0f1"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="a875fdc8-07d2-4475-a061-d666bd9a0662"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p style="text-align: left;">Before installing Teamwork Cloud, ensure that the system requirements described in this chapter are met.</p><h3><span style="letter-spacing: -0.006em;">Recommended system and storage requirements</span></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="50e90850-eb7e-4207-89c7-4408add22621"><ac:parameter ac:name="title">Note on system requirements</ac:parameter><ac:rich-text-body><p>System requirements are dictated by the intended deployment, taking into account the overall load which the environment will experience, including:</p><ul><li data-uuid="82ae8bbb-b3c4-4788-9825-b7777894ee0a">Number of concurrent users</li><li data-uuid="b21451d9-df61-4996-b745-04512589567a">Level of activity (commits) per day</li><li data-uuid="9c115f88-125f-475e-ae38-6ebceede7399">Overall number and size of the projects stored in Teamwork Cloud.</li></ul><p>The database (Cassandra) can be located on the same server as Teamwork Cloud or on a separate server. Storage requirements apply only to the node where the database is located. The product hosting nodes can be virtualized without any issues if the host is not oversubscribed on its resources.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cd53e167-74c4-44dc-8676-770b6669864a"><ac:parameter ac:name="title">Multi-Node Clusters</ac:parameter><ac:rich-text-body><p>Recommended minimum sizing stated above applies to each node in a multi-node cluster.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dbc8d4ec-c6db-4c48-ba50-1275910bd624"><ac:parameter ac:name="title">Note on storage requirements</ac:parameter><ac:rich-text-body><p>For on-premises deployment, Apache Cassandra is designed to run on multiple independent servers. Each Cassandra node should have Directly Attached Storage (DAS) composed of NVMe drives for optimum performance. Traditional network-attached storage solutions that rely on IP-based connections (iSCSI, NFS, or SAN) are not recommended for on-premises deployments, as they introduce additional latencies and anti-patterns. To learn more, see the following topics:</p><ul><li data-uuid="071b9706-af77-4233-80b1-729598d82938"><a href="https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hardware.html">Apache Cassandra Hardware Choices</a></li><li data-uuid="2abca631-ab40-425f-97c4-534d5df8314b"><a class="external-link" href="https://docs.datastax.com/en/planning/oss/anti-patterns.html" title="Follow link">DataStax Apache Cassandra Capacity Planning Guide</a></li></ul><p>For cloud deployment, use storage technologies that have been benchmarked for Cassandra. Modern solid-state/flash arrays with fast interconnects are preferred. Note that Teamwork Cloud is not compatible with managed Cassandra services, such as Amazon Keyspaces. To learn more, see the following topics:</p><ul><li data-uuid="d285036c-73bf-42b8-9494-15a674a85492"><a class="external-link" href="https://aws.amazon.com/blogs/database/best-practices-for-running-apache-cassandra-with-amazon-ebs/" title="Follow link">AWS EBS Cassandra Best Practices</a></li><li data-uuid="c2785eda-091f-440e-9fe0-56eacb3c4cf9"><a class="external-link" href="https://docs.datastax.com/en/planning/oss/planning-ec2.html" title="Follow link">DataStax AWS EC2 Recommendations</a></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><table class="fixed-width wrapped"><colgroup class=""><col class="" style="width: 231.0px;" /><col class="" style="width: 286.0px;" /><col class="" style="width: 292.0px;" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;" colspan="3">Resource requirements by deployment type</th></tr><tr class=""><th>Deployment type</th><th>Recommended system requirements</th><th>Recommended storage requirements</th></tr><tr class=""><td>Teamwork Cloud AND Cassandra on Linux</td><td><ul><li data-uuid="91fe062b-5964-4154-8c78-e92c61731779">96 -128 GB ECC RAM</li><li data-uuid="f234d024-06f4-4ac9-a2c6-c7c96410a8e8">&gt;=16 processor threads (equivalent or better than the Intel Xeon E-2278G, or their AMD counterparts, supporting x86-64 architecture)</li><li data-uuid="32789782-4283-4ffe-9a21-f60690c6ed5f"><p>1TB NVMe/SSD DAS storage</p></li></ul></td><td rowspan="3"><ul><li data-uuid="28fcd317-4e41-46ce-84cc-b711da44fa27"><strong>3 Solid State Drives with high IOPS</strong> <strong style="text-align: left;">(recommended ~400K)</strong><br />NVMe or SSD drives are highly suitable due to their low latency and high throughput. </li><li data-uuid="0216d0bb-4356-4602-8afc-d209ff5345c8"><strong>3 separate disk mounts</strong><br />Data, commit logs, and applications have different access patterns and should reside on separate disks to avoid I/O contention. For a detailed example, please see <ac:link><ri:page ri:space-key="MCS" ri:content-title="Preparing the operating system" /></ac:link></li></ul><strong><br /></strong><strong><br /></strong><strong><br /></strong><strong><br /></strong></td></tr><tr class=""><td>Only Cassandra (Linux only)<u><br /></u></td><td><ul><li data-uuid="1d46d16e-6551-48f5-be35-4137ec8713ac">48 - 64 GB ECC RAM</li><li data-uuid="dcaa8133-8a2e-467e-8339-143d45ff5f9c">&gt;=8 processor threads (equivalent or better than the Intel Xeon E-2234, or their AMD counterparts, supporting x86-64 architecture)</li><li data-uuid="6ab3304c-57cd-47c4-8604-170a5b76cac9"><p>1TB NVMe/SSD DAS storage</p></li></ul></td></tr><tr class=""><td>Only Teamwork Cloud</td><td><ul><li data-uuid="26c6f44f-07c8-4967-895d-bb91665d926d">48 - 64 GB ECC RAM</li><li data-uuid="6c4bc2a7-d94b-4fee-9300-76f26ddf0a88">&gt;=8 processor threads (equivalent or better than the Intel Xeon E-2234, or their AMD counterparts, supporting x86-64 architecture)</li><li data-uuid="95162b58-9739-4215-93af-1ddff7dcb172">&gt;250GB storage</li></ul></td></tr><tr><td>Web Application Platform for small and medium deployments (5, 10, 25, or 50 connection licenses)</td><td><ul><li data-uuid="594d85ab-bfc0-40f1-8002-2968a75d286b"><span>32 GB of RAM dedicated exclusively to Web Application Platform services and additional RAM per OS requirements</span></li><li data-uuid="a24f883c-74da-460c-bf77-9f698b74c858">CPU with 8 cores running at 2.1 GHz</li><li data-uuid="2a275305-c1e4-430d-b2a6-52cb8da897c3">For deployments on Linux, the open file limit must be no less than 20,000 files.</li></ul></td><td><ul><li data-uuid="da0af6a6-3b32-4edc-8dbc-61a33c7702d6">100 GB of free space on the disk, NVMe or SSD</li></ul></td></tr><tr><td>Web Application Platform for large enterprise deployments (75, 100, or unlimited connection licenses)</td><td><ul><li data-uuid="0a904109-42c9-4e6e-adf8-0ed464e5a0d1"><span>64 GB of RAM dedicated exclusively to Web Application Platform services and additional RAM per OS requirements</span></li><li data-uuid="782dfcfe-ab7a-47cf-b6f0-f9d568b2c0c1">CPU with 16 cores running at 2.1 GHz</li><li data-uuid="04065f81-d911-4089-b296-60edc32cd8ba">For deployments on Linux, the open file limit must be no less than 20,000 files.</li></ul></td><td><ul><li data-uuid="404e4aa6-ae45-431b-8aea-559d4a28793b">200 GB of free space on the disk, NVMe or SSD</li></ul></td></tr></tbody></table><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7fbef871-442a-47af-aefa-9274794d74f7"><ac:parameter ac:name="title">Deployments with unlimited licenses</ac:parameter><ac:rich-text-body><p>If you have a deployment with an unlimited license or are in doubt about what hardware to use, contact your account executive <span>for hardware recommendations to accommodate your specific needs.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4938e330-0a4a-4a61-a581-62d9d31a4b4a"><ac:parameter ac:name="title">Note on Web Application Platform</ac:parameter><ac:rich-text-body><p>When installing Web Application Platform for production purposes, it is recommended to <ac:link><ri:page ri:content-title="Web Application Platform Installation on a separate machine" /><ac:plain-text-link-body><![CDATA[install it on a separate machine]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3>Software requirements</h3><p class="auto-cursor-target">Teamwork Cloud supports the following operating systems:</p><ul><li><p><span><span style="color:var(--ds-text,#172b4d);">Linux 64-bit RedHat 8, RedHat 9, Oracle Linux 8</span>.</span></p></li><li>Windows 2016 or Windows 2019.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="abbb2492-318e-4488-9433-bed73236f49d"><ac:rich-text-body><p>The Linux operating system is highly recommended for Teamwork Cloud deployment. Cassandra 4 does not have native Windows support.</p></ac:rich-text-body></ac:structured-macro><p>For a fully working environment, you will also need the following:</p><ul><li data-uuid="654675b9-f26a-4a0f-9e21-b55acb61ef8e"><span style="color:var(--ds-text,#172b4d);">Cassandra (check the compatible version <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>)</span></li><li data-uuid="fb526a32-0e16-40c8-8594-06819f0fb07a"><span>Java compatible with Teamwork Cloud (twcloud service) and Cassandra (check version <ac:link><ri:page ri:content-title="Third-Party Component Compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>)</span></li><li><span style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-background-accent-red-bolder,#c9372c);"><strong>IMPORTANT</strong></span>. To use modeling tools with DSLS licenses, </span><span>Microsoft Visual C++ Redistributable must be installed (see </span><a class="external-link" href="https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022">Latest supported Visual C++ Redistributable downloads</a><span>). This applies to Windows OS only.</span></span></li><li><ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="FlexNet license server installation and licensing" /><ac:plain-text-link-body><![CDATA[FlexNet ]]></ac:plain-text-link-body></ac:link>or <ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[ DSLS ]]></ac:plain-text-link-body></ac:link>license server</li><li>A static IP address for each node.</li><li><p class="auto-cursor-target">Open ports 1101, 2181, 2552, 4085, 7000, 7001, 7199, 9042, and 9142 between servers in a cluster.</p></li><li><p class="auto-cursor-target">Open ports 3579, 8111, 8443, and 10002 (default) for clients. The port number 10002 can be changed according to the port assigned to secure connections between the client software and Teamwork Cloud.</p></li></ul><p>The following table lists the ports that Teamwork Cloud services use and their descriptions. Port traffic is TCP unless otherwise specified.</p><table class="relative-table wrapped" style="width: 51.4262%;"><colgroup class=""><col class="" style="width: 30.3246%;" /><col class="" style="width: 17.9374%;" /><col class="" style="width: 51.7381%;" /></colgroup><tbody class=""><tr class=""><th>Service</th><th class="highlight-grey" data-highlight-colour="grey">Port</th><th class="highlight-grey" data-highlight-colour="grey">Description</th></tr><tr class=""><td>FlexNet server (lmadmin)</td><td>1101</td><td>FLEXnet server port</td></tr><tr class=""><td><br /></td><td>8090</td><td>License management web interface HTTP port</td></tr><tr class=""><td><br /></td><td>27000-27009</td><td>Internal license server manager port</td></tr><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td></tr><tr><td><span style="color:var(--ds-text,#172b4d);">DSLS (Dassault Systèmes License Server)</span></td><td>4085</td><td><span style="color:var(--ds-text,#172b4d);">DSLS licensing server port</span></td></tr><tr><th scope="col"><br /></th><th scope="col"><br /></th><th scope="col"><br /></th></tr><tr class=""><td>Cassandra</td><td>7000</td><td>Internode cluster communication port (not used if TLS is enabled)</td></tr><tr class=""><td><br /></td><td>7199</td><td>JMX monitoring port of the Cassandra node</td></tr><tr class=""><td><br /></td><td>9042</td><td>Native client port for processing database operations</td></tr><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td></tr><tr class=""><td>Teamwork Cloud</td><td>2468</td><td>JMX metrics reporting port for monitoring stack</td></tr><tr class=""><td><br /></td><td>2552</td><td>Teamwork Cloud default remote server port</td></tr><tr class=""><td><br /></td><td>3579</td><td>Default Teamwork Cloud port when SSL is not enabled</td></tr><tr class=""><td><br /></td><td>8111</td><td>REST API HTTPS port</td></tr><tr class=""><td><br /></td><td>10002 </td><td><span style="color:var(--ds-text,#172b4d);">Default port for encrypted TLS client-server communication.</span></td></tr><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td></tr><tr class=""><td>Web Application Platform</td><td>8443</td><td>Web Application Platform HTTPS port (Authentication, Collaborator…)</td></tr><tr class=""><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td><td class="highlight-grey" data-highlight-colour="grey"><br /></td></tr><tr class=""><td>Zookeeper</td><td>2181</td><td>Zookeeper internal port</td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f9b9fe9b-0661-45dd-a537-69a48ed7dad8"><ac:parameter ac:name="title">If deploying on Amazon EC2</ac:parameter><ac:rich-text-body><span style="color:var(--ds-text,#333333);">When deploying on </span>Amazon EC2<span style="color:var(--ds-text,#333333);">, we recommend using the </span>m5-2xlarge<span style="color:var(--ds-text,#333333);">, r5-2xlarge, or i3-2xlarge instances. Depending on the workload, you may want to go to the -4xlarge instances, but for most users, the -2xlarge will suffice. The m5 instances meet the minimum system requirements and will be acceptable for small deployments. The r5 instances provide more memory for the same CPU density. The i3 instances should be used when workloads have a higher level of user concurrency due to the significantly improved performance of the ephemeral NVMe storage.</span></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491469 space=TWCloud2024xR1 version=1 -->
## PAGE 00245: Teamwork Cloud administration

- page_id: `170491469`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491469/Teamwork+Cloud+administration
- version_number: 1
- version_date: `2024-01-29T09:36:49.767+01:00`
- ancestors: Teamwork Cloud and Services > Administration Guide
- labels: []

### NORMALIZED CONTENT

**In this section**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>In this section</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491095 space=TWCloud2024xR1 version=5 -->
## PAGE 00246: Teamwork Cloud and Services

- page_id: `170491095`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491095/Teamwork+Cloud+and+Services
- version_number: 5
- version_date: `2024-05-21T07:19:49.322+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

422970360

422970380

422970370

INLINE

Teamwork Cloud and Services is a compound product for collaborative model development and storage. It is designed to provide state-of-the-art model governance (merging, branching, access control), analysis, and integration with third-party tools. The product works along with Magic Software Engineer, Magic System of Systems Architect, and Magic Systems Modeler.

Teamwork Cloud enables wide collaboration capabilities with the following core components and services in its suite:

- **Web Application** **Platform**- the base for Cameo Collaborator for Teamwork Cloud and Teamwork Cloud Admin apps.
- **Teamwork Cloud Admin**- a set of web applications necessary to manage Teamwork Cloud. The apps are accessible through a convenient web-based, mobile-friendly administrative interface for simple management of user accounts, projects, RBAC settings, LDAP integration, and more.
- **Teamwork Cloud** - a model repository that enables parallel modeling, model storage, and version control with strict yet flexible access control in place.
- **Cameo Collaborator for Teamwork Cloud** - a web-based product designed to present models in a simplified form for stakeholders, sponsors, customers, and engineering teams. In addition to the commenting capability enabling you to review models and leave feedback, it also allows editing models directly on the web.
- **Apache Cassandra** - an open-source NoSQL distributed database that Teamwork Cloud uses as its storage engine.

[IMAGE alt='' src='']

###### The conceptual schema of Teamwork Cloud and Related Services.

For more information on how to use Teamwork Cloud and Related Services, see:

842556374

**Documentation of earlier versions**

- [CONFLUENCE_PAGE title='Teamwork Cloud and Services' space='TWCloud2022xR2']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud2022xR1']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud2022x']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud2021xR2']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud2021xR1']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud2021x']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud190SP4']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud190SP3']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud190SP2']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud190SP1']
- [CONFLUENCE_PAGE title='Teamwork Cloud Documentation' space='TWCloud190']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a739feef-ccdf-49fd-a4f0-32baf93936b7"><ac:parameter ac:name="id">422970360</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="108267a8-061b-464b-8347-72ec0c09468a"><ac:parameter ac:name="id">422970380</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b460154a-978b-484b-a949-18560ee4b024"><ac:parameter ac:name="id">422970370</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="54146ca7-b13e-4cd0-abe2-f7e6c3127887"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);"><ac:inline-comment-marker ac:ref="facdba59-b9db-49be-bbbd-41aa9f48d778">Teamwork Cloud and Services is a compound product</ac:inline-comment-marker> for collaborative model development and storage. It is designed to provide state-of-the-art model governance (merging, branching, access control), analysis, and integration with third-party tools. The product works along with <ac:inline-comment-marker ac:ref="9c614323-5160-4b1b-9d14-f504b690ddee">Magic Software Engineer, Magic System of Systems Architect, and Magic Systems Modeler</ac:inline-comment-marker>.</span></p><p><ac:inline-comment-marker ac:ref="ebb3b7de-a2f6-4567-bc3a-876a6ff9e027">Teamwork Cloud enables wide collaboration capabilities with the following core components and services in its suite:</ac:inline-comment-marker></p><ul><li><span style="color: rgb(0,0,0);"><strong>Web Application</strong> <strong>Platform </strong>- the base for Cameo Collaborator for Teamwork Cloud and Teamwork Cloud Admin apps.</span></li><li><span style="color: rgb(0,0,0);"><strong>Teamwork Cloud Admin </strong>- a set of web applications necessary to manage Teamwork Cloud. The apps are accessible through a convenient web-based, mobile-friendly administrative interface for simple management of user accounts, projects, RBAC settings, LDAP integration, and more.</span></li><li><span style="color: rgb(0,0,0);"><strong>Teamwork Cloud</strong> - a model repository that enables parallel modeling, model storage, and version control with strict yet flexible access control in place.</span></li><li><p><span style="color: rgb(0,0,0);"><strong>Cameo Collaborator for Teamwork Cloud</strong> - a web-based product designed to present models in a simplified form for stakeholders, sponsors, customers, and engineering teams. In addition to the commenting capability enabling you to review models and leave feedback, it also allows editing models directly on the web.</span></p></li><li><span style="color: rgb(0,0,0);"><strong>Apache Cassandra</strong> - an open-source NoSQL distributed database that Teamwork Cloud uses as its storage engine.</span></li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="CATIA-Magic-Collaboration-Studio_conceptual_schema.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Teamwork Cloud and Services" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="ec66702d-dede-4f59-9f99-afcb47578960">The conceptual schema of Teamwork Cloud and Related Services.</ac:inline-comment-marker></h6><p>For more information on how to use Teamwork Cloud and Related Services, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="06c423c1-5c8e-4330-bdba-686e582984aa"><ac:parameter ac:name="id">842556374</ac:parameter><ac:rich-text-body><p><strong>Documentation of earlier versions</strong></p><ul><li><ac:link><ri:page ri:space-key="TWCloud2022xR2" ri:content-title="Teamwork Cloud and Services" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud and Services 2022x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2022xR1" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 2022x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2022x" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 2022x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2021xR2" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2021xR1" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2021x" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 2021x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud190SP4" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 19.0 SP4]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud190SP3" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 19.0 SP3]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud190SP2" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 19.0 SP2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud190SP1" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 19.0 SP1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud190" ri:content-title="Teamwork Cloud Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud 19.0]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170491194 space=TWCloud2024xR1 version=1 -->
## PAGE 00247: Teamwork Cloud and Services Installation

- page_id: `170491194`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491194/Teamwork+Cloud+and+Services+Installation
- version_number: 1
- version_date: `2024-01-29T09:40:44.070+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: []

### NORMALIZED CONTENT

The following sections provide instructions on how to install and set up Teamwork Cloud.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">The following sections provide instructions on how to install and set up Teamwork Cloud.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=171180795 space=TWCloud2024xR1 version=4 -->
## PAGE 00248: Teamwork Cloud FAQ

- page_id: `171180795`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180795/Teamwork+Cloud+FAQ
- version_number: 4
- version_date: `2025-10-21T13:00:02.501+02:00`
- ancestors: Teamwork Cloud and Services > FAQ and Troubleshooting
- labels: []

### NORMALIZED CONTENT

#### EXPAND: How to address Apache Tomcat vulnerabilities found?

How to address Apache Tomcat vulnerabilities found?

Web Application Platform is a component of Teamwork Cloud. Apache Tomcat is the web server environment used by Web Application Platform. Frequent patching of Tomcat is needed to address the latest vulnerabilities (CVE) discovered.

For detailed instructions, refer to the[Upgrading and Patching Apache Tomcat](https://docs.nomagic.com/display/TWCloud2024xR1/Hardening+Web+Application+Platform#HardeningWebApplicationPlatform-UpgradingandpatchingApacheTomcat)documentation:

- For Teamwork Cloud 22x and older, find the latest patch for Tomcat 9.X
- For Teamwork Cloud 24x and newer, find the latest patch for Tomcat 10.X.

Patching on Linux servers can be performed using a script that we provide. Both online and offline patching are supported. Windows Servers will require a manual patching process.

#### EXPAND: Why is Cassandra failing to start?

Why is Cassandra failing to start?

Cassandra startup issue could be due to several reasons. The service log should provide clues on what is causing the issue. Use the *journalctl -u cassandra* command to look through the service startup log for errors.

For JVM error, make sure the default Java version is set to support your Cassandra version (Java 11 for 4.X and Java 1.8 for 3.X).

For JNA errors, such as “failed to link C library against JNA” or fatal error SIGSEGV, system mount is the issue. Verify whether */tmp* and */dev/shm* are mounted with the *noexec* option (command: *findmnt /tmp*). Note that the Cassandra installation script will also check these mounts.

Cassandra uses the Java Native Access (JNA) library to access platform-specific shared libraries. During startup, both */tmp* and */dev/shm* are used for execution.

While */tmp* can be configured to another path, */dev/shm* must be remounted with *exec*. To set the *tmp* directory to an alternate path, find or create a path where Cassandra will have permission to execute in. Then, append the following line to the *cassandra-env.sh* file in */etc/cassandra/conf*.

```text

```

Before restarting Cassandra, make sure to delete all the existing commitlogs. Previous startup attempts would have created numerous commitlog files.

Note that if */tmp* or */dev/shm* is mounted as *noexec*, changing permission or ownership of the directory will not resolve the issue. The directory either has to be remounted with *noexec* removed or use the solution provided above.

Error “/etc/rc.d/init.d/functions: No such file or directory” is related to RHEL 9. However, in some configurations, it can occur on older releases. You can try to solve it by installing *initscripts*:

```bash

```

or by copying */etc/rc.d/init.d/functions*file from an older machine.

#### EXPAND: Where can I find log files?

Where can I find log files?

Use the [CONFLUENCE_PAGE title='Log file collection' space=''] to automatically gather and package all the relevant log files. Specific log file paths can be found in [CONFLUENCE_PAGE title='File locations' space=''].

#### EXPAND: How to install and use Temurin OpenJDK or another Java release on Linux?

How to install and use Temurin OpenJDK or another Java release on Linux?

Download the desired version of Temurin OpenJDK ([https://adoptium.net/temurin/releases/](https://adoptium.net/temurin/releases/)). For most cases, the JRE package is adequate.

Unpack the tar.gz file on the Linux server (*/opt*path is recommended)

Add the newly-installed Java release as an alternative:

```bash
/bin/java ]]>
```

Set as the default system Java:

```bash

```

#### EXPAND: How do I upgrade Teamwork Cloud to a newer version?

How do I upgrade Teamwork Cloud to a newer version?

Open the[CONFLUENCE_PAGE title='Upgrade and data migration' space='']in a new tab and use it to determine what steps are required for the upgrade. Upgrading from older versions will require database migration and Cassandra upgrade. Minor upgrades will only involve uninstalling the current version and installing the latest version.

#### EXPAND: Does 2021x Refresh 2 work with Cassandra 4.1?

Does 2021x Refresh 2 work with Cassandra 4.1?

Teamwork Cloud 2021x Refresh 2 Hot Fix 5 supports Cassandra 4.0.X out of the box. For 2021x Refresh 2 to connect to Cassandra 4.1.X, add the following parameter to the end of the application.conf file in *<install_root>/<product>/configuration*.

```text

```

#### EXPAND: How to proceed with installation when encountering com.zerog.lax.LAX error?

How to proceed with installation when encountering com.zerog.lax.LAX error?

If the following error is encountered during installation:

```text

```

The best solution is to download the latest installer and installation scripts for your version. This issue is caused by newer versions of Java 11 and 17. Our scripts and installers (.bin) have been updated to address this issue.

If you are unable to use the latest installer and scripts, then add the following additional Java environment parameter when executing the installer. This environment parameter should either be added to the installation script, or on the command line if you are executing the .bin installer file directly.

```text

```

#### EXPAND: Is offline installation possible for Linux?

Is offline installation possible for Linux?

It is possible to install Teamwork Cloud without internet access, provided that the prerequisite packages are available locally. Access to a locally-managed repository server is a recommended for offline installation. Linux packages often have dependencies that are pulled and installed automatically when connecting to a repository. Manual download of Linux packages may require a trial-and-error process of retrieving dependencies.

###### Access to repository server

If you have access to a locally-managed repository server, go through the installation sections and download all prerequisite packages listed. If necessary, edit the installation scripts and replace all hyperlinks with local path to the downloaded package. Finally, execute the installation script. The local repository server will resolve all packages and dependencies needed during installation.

###### Manual installation

If your only option is to manually install all packages needed, then you will need to first download all the prerequisite packages from a machine with internet access. Then, as each package is installed, you will need to make a note of the dependencies required. This will be an iterative process in order to find all the dependencies that are needed to complete the installation.

To prepare for manual installation, an internet-accessible machine is initially needed to download all the required packages. This machine should mirror the environment of the deployment server. A mirrored environment will accurately resolve package dependencies. Use the DNF Download Plugin (dnf-plugins-core) to retrieve packages.

```bash
]]>
```

The command structure above will download the main package and any dependencies that is required. Dependencies are dictated by the Linux environment. If the deployment server has a very different Linux environment than the download machine, then resolving package dependencies can be a tedious process.

#### EXPAND: What is causing the System Error when trying to access the web login page?

What is causing the System Error when trying to access the web login page?

[IMAGE alt='' src='']

This error is typically due to an incorrect address entry in the authentication whitelist. Verify addresses specified for *authentication.redirect.uri.whitelist* in *authserver.properties* file are correct.

#### EXPAND: How to run Teamwork Cloud in FIPS Mode?

How to run Teamwork Cloud in FIPS Mode?

You may encounter an error message similar to the one shown below when running Teamwork Cloud in FIPS Mode. PKCS12 keystore creation and usage are blocked in FIPS Mode for Java 11 and older versions.

```text

```

First, make sure the initial installation was able to generate a self-signed certificate and keystore. Look for *keystore.p12* and *teamworkcloud.crt* files in *<install_root>/TeamworkCloud/configuration*. If these files were not generated, run the *genkey* script in *<install_root>/TeamworkCloud/script/linux*. Check for the *keystore.p12* and *teamworkcloud.crt* files again and change ownership to *twcloud (*or other username that you chose during installation.) Once these two files are generated, version 2024x should be able to run in FIPS Mode.

If the genkey script is not able to generate the self-signed certificate and keystore, set the system Java version to 17 (*alternatives --config java*) and try again.

For 2022x Refresh 2, append the following line to the end of the *jvm.options* file located in *<install_root>/TeamworkCloud*.

```text

```

This configuration will allow Teamwork Cloud to use PKCS #12 keystore in FIPS Mode. Similar configurations will have to be set for Cassandra if encrypted communication is enabled.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="210eddbd-e56e-4258-b9ee-53254c77bb3e"><ac:parameter ac:name="title">How to address Apache Tomcat vulnerabilities found?</ac:parameter><ac:rich-text-body><p style="text-align: left;">Web Application Platform is a component of Teamwork Cloud. Apache Tomcat is the web server environment used by Web Application Platform. Frequent patching of Tomcat is needed to address the latest vulnerabilities (CVE) discovered. </p><p style="text-align: left;">For detailed instructions, refer to the<span> </span><a href="https://docs.nomagic.com/display/TWCloud2024xR1/Hardening+Web+Application+Platform#HardeningWebApplicationPlatform-UpgradingandpatchingApacheTomcat"><span class="error">Upgrading and Patching Apache Tomcat</span><span> </span></a>documentation:</p><ul><li>For Teamwork Cloud 22x and older, find the latest patch for Tomcat 9.X</li><li>For Teamwork Cloud 24x and newer, find the latest patch for Tomcat 10.X.</li></ul><p style="text-align: left;">Patching on Linux servers can be performed using a script that we provide. Both online and offline patching are supported. Windows Servers will require a manual patching process.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="abfda091-0273-4bef-857e-9a6e080465f8"><ac:parameter ac:name="title">Why is Cassandra failing to start?</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Cassandra startup issue could be due to several reasons. The service log should provide clues on what is causing the issue. Use the <em>journalctl -u cassandra</em> command to look through the service startup log for errors.</span></p><p><span style="color:var(--ds-text,#000000);">For JVM error, make sure the default Java version is set to support your Cassandra version (Java 11 for 4.X and Java 1.8 for 3.X). </span></p><p><span style="color:var(--ds-text,#000000);">For JNA errors, such as “failed to link C library against JNA” or fatal error SIGSEGV, system mount is the issue. Verify whether <em>/tmp</em> and <em>/dev/shm</em> are mounted with the <em>noexec</em> option (command: <em>findmnt /tmp</em>). Note that the Cassandra installation script will also check these mounts.</span></p><p><span style="color:var(--ds-text,#000000);">Cassandra uses the Java Native Access (JNA) library to access platform-specific shared libraries. During startup, both <em>/tmp</em> and <em>/dev/shm</em> are used for execution.</span></p><p><span style="color:var(--ds-text,#000000);">While <em>/tmp</em> can be configured to another path, <em>/dev/shm</em> must be remounted with <em>exec</em>. To set the <em>tmp</em> directory to an alternate path, find or create a path where Cassandra will have permission to execute in. Then, append the following line to the <em>cassandra-env.sh</em> file in <em>/etc/cassandra/conf</em>.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="df342036-4948-4c5a-b491-701390e68173"><ac:plain-text-body><![CDATA[JVM_OPTS="$JVM_OPTS -Djna.tmpdir=[NEW_PATH] -Djava.io.tmpdir=[NEW_PATH]"]]></ac:plain-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#000000);">Before restarting Cassandra, make sure to delete all the existing commitlogs. Previous startup attempts would have created numerous commitlog files.</span></p><p><span style="color:var(--ds-text,#000000);">Note that if <em>/tmp</em> or <em>/dev/shm</em> is mounted as <em>noexec</em>, changing permission or ownership of the directory will not resolve the issue. The directory either has to be remounted with <em>noexec</em> removed or use the solution provided above.</span></p><p><span style="color:var(--ds-text,#000000);">Error “<span style="color:var(--ds-text,#172b4d);">/etc/rc.d/init.d/functions: No such file or directory</span>” is related to RHEL 9. However, in some configurations, it can occur on older releases. You can try to solve it by <span style="color:var(--ds-text,#172b4d);">installing <em>initscripts</em>:</span></span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="dca0b5b0-6720-4ddc-a956-3bbb1073d4d9"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[dnf install initscripts]]></ac:plain-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-text,#172b4d);">or by copying <em>/etc/rc.d/init.d/functions </em>file from an older machine.</span></span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="d844d9eb-cd5d-4d1d-a4a7-bb14cf8ee844"><ac:parameter ac:name="title">Where can I find log files?</ac:parameter><ac:rich-text-body><p><span>Use the <ac:link><ri:page ri:content-title="Log file collection" /><ac:plain-text-link-body><![CDATA[log file utility]]></ac:plain-text-link-body></ac:link> to automatically gather and package all the relevant log files. Specific log file paths can be found in <ac:link><ri:page ri:content-title="File locations" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="d3eecb79-e59c-4aae-a20f-f8b48ac3a4f9"><ac:parameter ac:name="title">How to install and use Temurin OpenJDK or another Java release on Linux?</ac:parameter><ac:rich-text-body><p><span>Download the desired version of Temurin OpenJDK (<a href="https://adoptium.net/temurin/releases/">https://adoptium.net/temurin/releases/</a>). For most cases, the JRE package is adequate.</span></p><p><span>Unpack the tar.gz file on the Linux server (<em>/opt </em>path is recommended)</span></p><p><span>Add the newly-installed Java release as an alternative:</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5d02f01a-85d2-4ee3-8ac5-1ea24e2abaf6"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[alternatives --install /usr/bin/java java <path to new java>/bin/java <priority number>]]></ac:plain-text-body></ac:structured-macro><p><span>Set as the default system Java:</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="edba08ba-b483-4f37-b544-5a22d5d429fb"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[alternatives --config java]]></ac:plain-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="0a229650-92c8-496b-a4cf-01af575a52fe"><ac:parameter ac:name="title">How do I upgrade Teamwork Cloud to a newer version?</ac:parameter><ac:rich-text-body><p><span><ac:inline-comment-marker ac:ref="b042abec-dc7a-4de7-9f7c-cde3b5c8c1d7">Open the </ac:inline-comment-marker><ac:link><ri:page ri:content-title="Upgrade and data migration" /><ac:plain-text-link-body><![CDATA[upgrade path diagram ]]></ac:plain-text-link-body></ac:link>in a new tab and use it to determine what steps are required for the upgrade. Upgrading from older versions will require database migration and Cassandra upgrade. Minor upgrades will only involve uninstalling the current version and installing the latest version.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="e871a0b3-a490-4071-a496-5dba38198273"><ac:parameter ac:name="title">Does 2021x Refresh 2 work with Cassandra 4.1?</ac:parameter><ac:rich-text-body><p><span>Teamwork Cloud 2021x Refresh 2 Hot Fix 5 supports Cassandra 4.0.X out of the box. For 2021x Refresh 2 to connect to Cassandra 4.1.X, add the following parameter to the end of the application.conf file in <em>&lt;install_root&gt;/&lt;product&gt;/configuration</em>.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2ef26641-2bcb-4e0d-8489-3b8b6a474ba5"><ac:plain-text-body><![CDATA[esi.persistence.cassandra.enable-check-version = false]]></ac:plain-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="6e51daef-5b9a-4a91-9de7-ec139f7d6bdc"><ac:parameter ac:name="title">How to proceed with installation when encountering com.zerog.lax.LAX error?</ac:parameter><ac:rich-text-body><p>If the following error is encountered during installation:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="0a46142b-d70b-43e6-9beb-6b1586a547e2"><ac:plain-text-body><![CDATA[Error: Could not find or load main class com.zerog.lax.LAX
Caused by: java.lang.ClassNotFoundException: com.zerog.lax.LAX]]></ac:plain-text-body></ac:structured-macro><p>The best solution is to download the latest installer and installation scripts for your version. This issue is caused by newer versions of Java <ac:inline-comment-marker ac:ref="bb70166d-62bb-4353-bfe3-d318ace22387">11 and 17</ac:inline-comment-marker>. Our scripts and installers (.bin) have been updated to address this issue.</p><p>If you are unable to use the latest installer and scripts, then add the following additional Java environment parameter when executing the installer. This environment parameter should either be added to the installation script, or on the command line if you are executing the .bin installer file directly.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e85202ab-1598-4864-ba8f-f47aa520efbf"><ac:plain-text-body><![CDATA[JAVA_TOOL_OPTIONS=-Djdk.util.zip.disableZip64ExtraFieldValidation=true ./$INSTALLER]]></ac:plain-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="9f7310cf-ead0-4edc-b85e-e523da70ccd3"><ac:parameter ac:name="title">Is offline installation possible for Linux?</ac:parameter><ac:rich-text-body><p><span>It is possible to install Teamwork Cloud without internet access, provided that the prerequisite packages are available locally. Access to a locally-managed repository server is a recommended for offline installation. Linux packages often have dependencies that are pulled and installed automatically when connecting to a repository. Manual download of Linux packages may require a trial-and-error process of retrieving dependencies. </span></p><h4><span>Access to repository server</span></h4><p><span>If you have access to a locally-managed repository server, go through the installation sections and download all prerequisite packages listed. If necessary, edit the installation scripts and replace all hyperlinks with local path to the downloaded package. Finally, execute the installation script. The local repository server will resolve all packages and dependencies needed during installation.</span></p><h4><span>Manual installation</span></h4><p><span>If your only option is to manually install all packages needed, then you will need to first download all the prerequisite packages from a machine with internet access. Then, as each package is installed, you will need to make a note of the dependencies required. This will be an iterative process in order to find all the dependencies that are needed to complete the installation.</span></p><p><span>To prepare for manual installation, an internet-accessible machine is initially needed to download all the required packages. This machine should mirror the environment of the deployment server. A mirrored environment will accurately resolve package dependencies. Use the DNF Download Plugin (dnf-plugins-core) to retrieve packages. </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a6b473a7-d015-4bf3-96b8-20999e3972bc"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo dnf download –resolve <package-name>]]></ac:plain-text-body></ac:structured-macro><p><span>The command structure above will download the main package and any dependencies that is required. Dependencies are dictated by the Linux environment. If the deployment server has a very different Linux environment than the download machine, then resolving package dependencies can be a tedious process.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="b900cd3b-9ca7-4232-9ff1-5a538a2bbf6f"><ac:parameter ac:name="title">What is causing the System Error when trying to access the web login page?</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);"><ac:image><ri:url ri:value="https://docs.nomagic.com/download/attachments/122978562/Authserver-error.png?version=1&amp;modificationDate=1682057399692&amp;api=v2" /></ac:image></span></p><p><span style="color:var(--ds-text,#172b4d);">This error is typically due to an incorrect address entry in the authentication whitelist. Verify addresses specified for <em>authentication.redirect.uri.whitelist</em> in <em>authserver.properties</em> file are correct.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="cc05f9e4-5e60-43f0-ba6f-51fe51424097"><ac:parameter ac:name="title">How to run Teamwork Cloud in FIPS Mode?</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">You may encounter an error message similar to the one shown below when running Teamwork Cloud in FIPS Mode. PKCS12 keystore creation and usage are blocked in FIPS Mode for Java 11 and older versions.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="86d01357-0175-4793-8be3-dfde57ce6cc0"><ac:plain-text-body><![CDATA[PBES2 AlgorithmParameters not available]]></ac:plain-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#000000);">First, make sure the initial installation was able to generate a self-signed certificate and keystore. Look for <em>keystore.p12</em> and <em>teamworkcloud.crt</em> files in <em>&lt;install_root&gt;/TeamworkCloud/configuration</em>. If these files were not generated, run the <em>genkey</em> script in <em>&lt;install_root&gt;/TeamworkCloud/script/linux</em>. Check for the <em>keystore.p12</em> and <em>teamworkcloud.crt</em> files again and change ownership to <em>twcloud (</em>or other username that you chose during installation.) Once these two files are generated, version 2024x should be able to run in FIPS Mode.</span></p><p><span style="color:var(--ds-text,#000000);">If the genkey script is not able to generate the self-signed certificate and keystore, set the system Java version to 17 (<em>alternatives --config java</em>) and try again.</span></p><p><span style="color:var(--ds-text,#000000);">For 2022x Refresh 2, append the following line to the end of the <em>jvm.options</em> file located in <em>&lt;install_root&gt;/TeamworkCloud</em>. </span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a756c9e1-8e57-4c91-9acd-04d19c205754"><ac:plain-text-body><![CDATA[-Dcom.redhat.fips=false]]></ac:plain-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#000000);">This configuration will allow Teamwork Cloud to use PKCS #12 keystore in FIPS Mode. Similar configurations will have to be set for Cassandra if encrypted communication is enabled.</span></p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=218759495 space=TWCloud2024xR1 version=1 -->
## PAGE 00249: Telemetry Node

- page_id: `218759495`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/218759495/Telemetry+Node
- version_number: 1
- version_date: `2025-03-18T14:05:05.035+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Monitoring stack > Manual installation
- labels: []

### NORMALIZED CONTENT

**On this page**

**33**

**Downloads**:

- [ATTACHMENT filename='monitoring-stack_2024xRefresh2.zip']

The following components are deployed on each Teamwork Cloud/Cassandra node:

- Telegraf - system metrics collector
- Dropwizard metrics-graphite-3.1.5.jar - metrics publishing agent for Java

##### Installing Telegraf

To install and configure Telegraf

1. Install Telegraf
  1. Create yum repo entry, if needed. Refer to step 1a from Monitoring node installation
  2. Install with the command: bashDJangotrue
2. Use custom configuration file
  1. Locate /etc/telegraf/telegraf.conf. Make a note of the file ownership and permission
  2. Locate telegraf.conf.template from the extracted Telemetry-Node-Install folder and replace the existing file in /etc/telegraf/telegraf.conf; be sure to reset ownership and permission after replacement
  3. Edit telegraf.conf and replace HOST_NAME with the monitoring node address
3. Enable and start service
  1. Enable the Telegraf service for startup with the command: bashDJangotrue
  2. Start Telegraf with the command: bashDJangotrue
4. Cycle Teamwork Cloud service (systemctl restart twcloud), if not proceeding with Cassandra metrics installation

##### Installing Cassandra metrics reporter

To install Cassandra metrics reporter

1. Stop Teamwork cloud service
2. Install metrics reporter for Cassandra
  1. Download the metrics reporter jar file with the command: bashDJangotrue
  2. Place the file in Cassandra lib (default path: /usr/share/cassandra/lib/)
3. Configure Cassandra to send metrics to the monitoring node
  1. Locate metrics-reporter-graphite.yaml.template from the extracted Telemetry-Node-Install folder. Copy and rename the template file to the Cassandra configuration path (default: /etc/cassandra/conf/): metrics-reporter-graphite.yaml
  2. Edit the YAML file
    1. Replace HOST_NAME with the Cassandra node's hostname
    2. Replace IP_ADDRESS with the monitoring node's address
  3. Edit cassandra-env.sh in the Cassandra configuration path by appending the following: bashDJangotrue
  4. Restart cassandra service and verify successful startup.
  5. Start Teamwork Cloud service.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="c2201b81-6b7a-4019-ad5c-eadc0f9f8974"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell><ac:layout-cell><p><ac:inline-comment-marker ac:ref="3c5b4b7c-e567-4fac-b321-6e8828c49949"><strong style="">Downloads</strong>:</ac:inline-comment-marker> </p><ul><li><ac:link><ri:attachment ri:filename="monitoring-stack_2024xRefresh2.zip"><ri:page ri:content-title="Telemetry Node" ri:space-key="TWCloud2024xR1" /></ri:attachment></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p> <span style="letter-spacing: 0.0px;">The following components are deployed on each Teamwork Cloud/Cassandra node:</span></p><ul><li>Telegraf - system metrics collector</li><li>Dropwizard metrics-graphite-3.1.5.jar - metrics publishing agent for Java</li></ul><h3>Installing Telegraf</h3><p>To install and configure Telegraf</p><hr /><ol><li><span>Install Telegraf</span><ol><li><span>Create yum repo entry, if needed. Refer to step 1a from Monitoring node installation</span></li><li><span>Install with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="33ab9fb8-7a3c-493e-a2d6-cc1afaffe906"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo yum install -y telegraf]]></ac:plain-text-body></ac:structured-macro></li></ol></li><li><span>Use custom configuration file</span><ol><li><span>Locate /etc/telegraf/telegraf.conf. Make a note of the file ownership and permission</span></li><li><span>Locate telegraf.conf.template from the extracted Telemetry-Node-Install folder and replace the existing file in /etc/telegraf/telegraf.conf; be sure to reset ownership and permission after replacement</span></li><li><span>Edit telegraf.conf and replace HOST_NAME with the monitoring node address</span></li></ol></li><li><span>Enable and start service</span><ol><li><span>Enable the Telegraf service for startup with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="79ba1e06-279d-4368-ade3-d21ceeb748c1"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl enable telegraf]]></ac:plain-text-body></ac:structured-macro></li><li><span>Start Telegraf with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="21244dc5-a950-4923-befa-0215526a8f9a"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo systemctl start telegraf]]></ac:plain-text-body></ac:structured-macro><span><br /></span></li></ol></li><li>Cycle Teamwork Cloud service (systemctl restart twcloud), if not proceeding with Cassandra metrics installation</li></ol><h3>Installing Cassandra metrics reporter</h3><p>To install Cassandra metrics reporter </p><hr /><ol><li><span>Stop Teamwork cloud service</span></li><li><span>Install metrics reporter for Cassandra</span><ol><li><span>Download the metrics reporter jar file with the command:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="30966bb5-e61d-42a1-8070-496875aaa804"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[wget https://_repo1.maven.org/maven2/io/dropwizard/metrics/metrics-graphite/3.1.5/metrics-graphite-3.1.5.jar]]></ac:plain-text-body></ac:structured-macro></li><li><span>Place the file in Cassandra lib (default path: /usr/share/cassandra/lib/)</span></li></ol></li><li><span>Configure Cassandra to send metrics to the monitoring node</span><ol><li><span>Locate metrics-reporter-graphite.yaml.template from the extracted Telemetry-Node-Install folder. Copy and rename the template file to the Cassandra configuration path (default: /etc/cassandra/conf/): metrics-reporter-graphite.yaml</span></li><li><span>Edit the YAML file</span><ol><li><span>Replace HOST_NAME with the Cassandra node's hostname</span></li><li><span>Replace IP_ADDRESS with the monitoring node's address</span></li></ol></li><li><span>Edit cassandra-env.sh in the Cassandra configuration path by appending the following:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8e864690-0f86-4466-ae31-0d14c9b0bc4c"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[# Enable metrics reporting to InfluxDB using the yammer library
METRICS_REPORTER_CFG="metrics-reporter-graphite.yaml"
JVM_OPTS="$JVM_OPTS -Dcassandra.metricsReporterConfigFile=$METRICS_REPORTER_CFG"]]></ac:plain-text-body></ac:structured-macro><span><br /></span></li><li>Restart cassandra service and verify successful startup.</li><li>Start Teamwork Cloud service.</li></ol></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=286556410 space=TWCloud2024xR1 version=1 -->
## PAGE 00250: Third-Party Component Compatibility

- page_id: `286556410`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/286556410/Third-Party+Component+Compatibility
- version_number: 1
- version_date: `2026-01-26T09:14:04.717+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide
- labels: ['mcs', 'twc']

### NORMALIZED CONTENT

patch

major/minor

This table shows the compatibility of Teamwork Cloud and Web Application Platform (web services) with third-party components.The listed versions are those against which the product was tested and officially released. (Java used: Eclipse Temurin™ by Adoptium)

| Release | Cassandra | Java for Cassandra | Java forTeamwork Cloud | Apache Tomcat | Java for Apache Tomcat (web services) | Apache ZooKeeper | Artemis | PrinceXML |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024x Refresh1 Hot Fix 1 | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.31 | 17.0.13 | 3.9.2 | 2.32.0 | 15.3 |
| 2024x Refresh1 | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.20 | 17.0.11 | 3.9.2 | 2.32.0 | 15.3 |
| 2024x Hot Fix 3 | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.29 | 17.0.12 | 3.9.2 | 2.32.0 | - |
| 2024x Hot Fix 2 | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.19 | 17.0.10 | 3.9.2 | 2.32.0 | - |
| 2024x Hot Fix 1 | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.11 | 17.0.8 | 3.8.1 | 2.28.0 | - |
| 2024x | 4.1.5 | 11.0.14 | 17.0.8 | 10.1.11 | 17.0.8 | 3.8.1 | 2.28.0 | - |
| 2022x Refresh2 Hot Fix 3 | 4.0.3 | 11.0 | 11.0.14 | 9.0.98 | 17.0.13 | 3.9.2 | 2.34.0 | - |
| 2022x Refresh2 Hot Fix 2 | 4.0.3 | 11.0 | 11.0.14 | 9.0.89 | 17.0.11 | 3.9.2 | 2.34.0 | - |
| 2022x Refresh2 Hot Fix 1 | 4.0.3 | 11.0 | 11.0.14 | 9.0.73 | 17.0.6 | 3.8.1 | 2.28.0 | - |
| 2022x Refresh2 | 4.0.3 | 11.0 | 11.0.14 | 9.0.73 | 17.0.6 | 3.8.1 | 2.28.0 | - |
| 2022x Refresh1 | 4.0.3 | 11.0 | 11.0.14 | 9.0.65 | 17.0.4 | 3.8.0 | 2.24.0 | - |
| 2022x | 4.0.3 | 11.0 | 11.0.14 | 9.0.62 | 17.0.2 | 3.6.3 | 2.20.0 | - |
| 2021x Refresh2; Hot Fix 2; Hot Fix 3; Hot Fix 4 | 4.0.3 | 1.8.0_202 | 11.0.12 | 9.0.52 | 16.0.1 | 3.6.3 | - | - |
| 2021x Refresh2 Hot Fix 5 | 4.0.3 | 1.8.0_202 | 11.0.12 | 9.0.73 | 17.0.6 | 3.8.1 | - | - |
| 2021x Refresh1; Hot Fix 1; Hot Fix 2; Hot Fix 3 | 3.11.10 | 1.8.0_202 | 11.0.12 | 9.0.43 | 15.0.2 | - | - | - |
| 2021x | 3.11.3 | 1.8.0_202 | 11.0.12 | 9.0.39 | 14.0.1 | - | - | - |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d4492a79-83f1-4079-b12b-c45695be8550"><ac:rich-text-body>Cassandra, Java, and Apache Tomcat can be updated to the latest <strong>patch</strong> version within the same <strong>major/minor</strong> line (e.g., from 1.0.1 to 1.0.x).</ac:rich-text-body></ac:structured-macro><p style="margin-left: 0.0px;"><span><br />This table shows the compatibility of Teamwork Cloud and Web Application Platform (web services) with third-party components. <br /></span><span>The listed versions are those against which the product was tested and officially released. (Java used: <span style="color:var(--ds-text,#172b4d);">Eclipse Temurin™ by Adoptium</span>)</span></p><table class="fixed-width"><colgroup class=""><col class="" style="width: 175.0px;" /><col class="" style="width: 119.0px;" /><col class="" style="width: 110.0px;" /><col class="" style="width: 111.0px;" /><col class="" style="width: 90.0px;" /><col class="" style="width: 98.0px;" /><col class="" style="width: 113.0px;" /><col class="" style="width: 93.0px;" /><col class="" style="width: 112.0px;" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;">Release</th><th style="text-align: center;">Cassandra</th><th style="text-align: center;"><a href="https://adoptium.net/">Java </a>for Cassandra</th><th style="text-align: center;"><a href="https://adoptium.net/">Java </a>for<br />Teamwork Cloud</th><th style="text-align: center;"><a href="https://tomcat.apache.org/">Apache Tomcat</a></th><th style="text-align: center;"><a href="https://adoptium.net/">Java</a> for Apache Tomcat (web services)</th><th style="text-align: center;"><a href="https://zookeeper.apache.org/">Apache ZooKeeper</a></th><th style="text-align: center;"><a href="https://artemis.apache.org/">Artemis</a></th><th style="text-align: center;"><a href="https://www.princexml.com/">PrinceXML</a></th></tr><tr class=""><td>2024x Refresh1 Hot Fix 1</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.31</td><td style="text-align: center;">17.0.13</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.32.0</td><td style="text-align: center;">15.3</td></tr><tr class=""><td>2024x Refresh1</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.20</td><td style="text-align: center;">17.0.11</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.32.0</td><td style="text-align: center;">15.3</td></tr><tr class=""><td>2024x Hot Fix 3</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.29</td><td style="text-align: center;">17.0.12</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.32.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2024x Hot Fix 2</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.19</td><td style="text-align: center;">17.0.10</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.32.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2024x Hot Fix 1</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.11</td><td style="text-align: center;">17.0.8</td><td style="text-align: center;">3.8.1</td><td style="text-align: center;">2.28.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2024x</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.1.5</span></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">11.0.14</span></p></td><td style="text-align: center;"><p><span style="color:var(--ds-text,#172b4d);">17.0.8</span></p></td><td style="text-align: center;">10.1.11</td><td style="text-align: center;">17.0.8</td><td style="text-align: center;">3.8.1</td><td style="text-align: center;">2.28.0</td><td style="text-align: center;">-</td></tr><tr class=""><td>2022x Refresh2 Hot Fix 3</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.98</td><td style="text-align: center;">17.0.13</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.34.0</td><td style="text-align: center;">-</td></tr><tr class=""><td>2022x Refresh2 Hot Fix 2</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.89</td><td style="text-align: center;">17.0.11</td><td style="text-align: center;">3.9.2</td><td style="text-align: center;">2.34.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2022x Refresh2 Hot Fix 1</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.73</td><td style="text-align: center;">17.0.6</td><td style="text-align: center;">3.8.1</td><td style="text-align: center;">2.28.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2022x Refresh2</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.73</td><td style="text-align: center;">17.0.6</td><td style="text-align: center;">3.8.1</td><td style="text-align: center;">2.28.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2022x Refresh1</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.65</td><td style="text-align: center;">17.0.4</td><td style="text-align: center;">3.8.0</td><td style="text-align: center;">2.24.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2022x</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.14</span></td><td style="text-align: center;">9.0.62</td><td style="text-align: center;">17.0.2</td><td style="text-align: center;">3.6.3</td><td style="text-align: center;">2.20.0</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2021x Refresh2; Hot Fix 2; Hot Fix 3; Hot Fix 4</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">1.8.0_202</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.12</span></td><td style="text-align: center;">9.0.52</td><td style="text-align: center;">16.0.1</td><td style="text-align: center;">3.6.3</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2021x Refresh2 Hot Fix 5</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">4.0.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">1.8.0_202</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.12</span></td><td style="text-align: center;">9.0.73</td><td style="text-align: center;">17.0.6</td><td style="text-align: center;">3.8.1</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2021x Refresh1; Hot Fix 1; Hot Fix 2; Hot Fix 3</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">3.11.10</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">1.8.0_202</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.12</span></td><td style="text-align: center;">9.0.43</td><td style="text-align: center;">15.0.2</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr><tr class=""><td style="text-align: justify;">2021x</td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">3.11.3</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">1.8.0_202</span></td><td style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">11.0.12</span></td><td style="text-align: center;">9.0.39</td><td style="text-align: center;">14.0.1</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td><td style="text-align: center;">-</td></tr></tbody></table><p><br /></p>
````

<!--NOMAGIC_PAGE id=170491844 space=TWCloud2024xR1 version=2 -->
## PAGE 00251: Types of roles

- page_id: `170491844`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491844/Types+of+roles
- version_number: 2
- version_date: `2025-10-30T14:21:39.299+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application > User roles and permissions
- labels: []

### NORMALIZED CONTENT

**On this page**

4

A role is assigned to a user who has the responsibility to perform specific actions on the assigned resource(s). There are two types of roles in Teamwork Cloud: **predefined**and **custom**.

- A predefined role is a ready-to-use role that an authorized user can assign to other users. A predefined role is not editable and cannot be deleted.
- A custom role is a role created by an authorized user. An authorized user can also edit a custom role and change its permissions.

##### **Predefined roles**

Predefined roles are default roles that come with your Teamwork Cloud installation. You can select these ready-to-use roles and assign them to one or more users. Each predefined role comes with its own default permissions, which you can see on the **Role detail** pane. You cannot delete a predefined role, or change its permissions.

The following table describes all predefined roles in Teamwork Cloud:

| Role | Description | Scope |
| --- | --- | --- |
| Data Markings Manager | The user with this role can mark or unmark Users, User Groups, Resources, and Categories with predefined clearance and classification levels. | Global |
| Index Manager | This role allows users to manage resource indexing configurations. To manage indexing configurations of all resources in the server, the role scope should be set to global. | Category or resource-specific |
| Resource Contributor | This role allows users to modify the contents of resources (projects or documents). | Category, resource, or branch-specific |
| Resource Creator | This role allows users to add new resources to the server, categorize them, create new categories or manage the existing ones. | Category-specific |
| Resource Locks Administrator | This role allows users to release other users' locks in the selected resources. | Category or resource-specific |
| Resource Manager | This role allows users to manage resources and grant permissions to other users to access resources. | Category, resource, or branch-specific |
| Resource Reviewer | This role allows users to open and review resources (projects or documents). | Category or resource-specific |
| Resource Synchronization Manager | Users with this role can set up and manage synchronization of remote Teamwork Cloud repository resources. | Category-specific |
| Reports Manager | This role allows users to access the Reports application. | Global |
| Security Manager | This global role allows users to grant permissions to other users, specify the scope, and assign any role in any scope to other users. | Global |
| Server Administrator | This global role allows users to configure server settings, LDAP integration, secure connection, and server licenses. | Global |
| Simulation Manager | This global role allows users to manage all simulations. This includes the ability to get and review simulation results and terminate simulations executed by other users. | Global |
| User Group Membership Manager | This role allows users to manage assigned user group(s). It can also be set to global scope, allowing users to manage all user groups. | Global or user group-specific |
| User Manager | This global role allows users to create, import, and manage users. | Global |

#### NOTE: Role scopes

Role scopes

- Global: users can carry out tasks (depending on role permissions) across all resources, protected objects, and users in Teamwork Cloud. The scope of any category or resource-specific role can be set to global as well. In this case, role permissions for the assigned users will be applied to all resources in Teamwork Cloud.
- Category-specific: users can carry out tasks across all resources stored in a specific category. All new resources added to such a category automatically inherit role permissions. Any resource removed from such a category automatically loses role permissions.
- Resource-specific: users can carry out tasks only across assigned resources.
- Branch-specific: allows users to carry out tasks only across the specific branches of the assigned resources.
- User group-specific: allows users to manage the specific user group or groups.

##### Custom roles

In Teamwork Cloud you can create a new role with a desired set of permissions. This type of role is called a custom role. You can delete a custom role or change its permissions. Even though the role name should be unique, it can have the same set of permissions as other roles.

- To create custom roles, you need to have the Manage Security Roles permission or the Security Manager role.
- You cannot give global scope permissions, such as Create Resource, Manage User Permissions, Mark Data, Configure Data Markings, etc., to a custom role.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="cad4fb99-3fd0-48f1-b7fb-5c5405dfda27"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>A role is assigned to a user who has the responsibility to perform specific actions on the assigned resource(s). There are two types of roles in Teamwork Cloud: <strong>predefined </strong>and <strong>custom</strong>.</p><ul><li>A <strong>predefined </strong>role is a ready-to-use role that an authorized user can assign to other users. A predefined role is not editable and cannot be deleted.</li><li>A <strong>custom </strong>role is a role created by an authorized user. An authorized user can also edit a custom role and change its permissions.</li></ul><h3 style="color:var(--ds-text,#172b4d);"><strong>Predefined roles</strong></h3><p>Predefined roles are default roles that come with your Teamwork Cloud installation. You can select these ready-to-use roles and assign them to one or more users. Each predefined role comes with its own default permissions, which you can see on the <strong>Role detail</strong> pane. You cannot delete a predefined role, or change its permissions.</p><p>The following table describes all predefined roles in Teamwork Cloud:<br /><br /></p><table class="wrapped" style="margin-left: 30.0px;"><colgroup><col /><col /><col /></colgroup><thead><tr style="margin-left: 30.0px;"><th><div class="tablesorter-header-inner"><strong>Role</strong></div></th><th><div class="tablesorter-header-inner"><strong>Description</strong></div></th><th>Scope</th></tr></thead><tbody style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><td><strong>Data Markings Manager</strong></td><td><span style="color:var(--ds-text,#333333);">The user with this role can mark or unmark Users, User Groups, Resources, and Categories with predefined clearance and classification levels.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td><strong>Index Manager</strong></td><td>This role allows users to manage resource indexing configurations. To manage indexing configurations of all resources in the server, the role scope should be set to global.</td><td>Category or resource-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>Resource Contributor</strong></td><td>This role allows users to modify the contents of resources (projects or documents).</td><td>Category, resource, or branch-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>Resource Creator</strong></td><td><p>This role allows users to add new resources to the server, categorize them, create new categories or manage the existing ones. </p></td><td>Category-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>Resource Locks Administrator</strong></td><td>This role allows users to release other users' locks in the selected resources.</td><td>Category or resource-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>Resource Manager</strong></td><td>This role allows users to manage resources and grant permissions to other users to access resources. </td><td>Category, resource, or branch-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>Resource Reviewer</strong></td><td>This role allows users to open and review resources (projects or documents). </td><td>Category or resource-specific</td></tr><tr><td><strong>Resource Synchronization Manager</strong></td><td>Users with this role can set up and manage synchronization of remote Teamwork Cloud repository resources.</td><td>Category-specific</td></tr><tr><td><strong>Reports Manager</strong></td><td><span style="color:var(--ds-text,#000000);">This role allows users to access the Reports application.</span></td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td><strong>Security Manager</strong></td><td>This global role allows users to grant permissions to other users, specify the scope, and assign any role in any scope to other users.</td><td>Global</td></tr><tr style="margin-left: 30.0px;"><td><strong>Server Administrator</strong></td><td>This global role allows users to configure server settings,<em> </em>LDAP integration, secure connection, and server licenses.</td><td>Global</td></tr><tr><td><strong>Simulation Manager</strong></td><td><p>This global role allows users to manage all simulations. This includes the ability to get and review simulation results and terminate simulations executed by other users.</p></td><td>Global</td></tr><tr><td><strong>User Group Membership Manager</strong></td><td><p>This role allows users to manage assigned user group(s). It can also be set to global scope, allowing users to manage all user groups.</p></td><td>Global or user group-specific</td></tr><tr style="margin-left: 30.0px;"><td><strong>User Manager</strong></td><td>This global role allows users to create, import, and manage users. </td><td>Global</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f1ce5909-5f4b-4488-ac39-9609524771de"><ac:parameter ac:name="title">Role scopes</ac:parameter><ac:rich-text-body><ul><li><strong>Global:</strong> users can carry out tasks (depending on role permissions) <span style="color:var(--ds-text,#333333);">across all resources, protected objects, and users in Teamwork Cloud. The scope of any category or resource-specific role can be set to global as well. In this case, role permissions for the assigned users will be applied to all resources in Teamwork Cloud.</span></li><li><strong>Category-specific: </strong>users can carry out tasks across all resources stored in a specific category. All new resources added to such a category automatically inherit role permissions. Any resource removed from such a category automatically loses role permissions.</li><li><strong>Resource-specific: </strong>users can carry out tasks only across assigned resources.</li><li><strong>Branch-specific:</strong> allows users to carry out tasks only across the specific branches of the assigned resources.</li><li><strong>User group-specific:</strong> allows users to manage the specific user group or groups.</li></ul></ac:rich-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);">Custom roles</h3><p>In Teamwork Cloud you can create a new role with a desired set of permissions. This type of role is called a custom role. You can delete a custom role or change its permissions. Even though the role name should be unique, it can have the same set of permissions as other roles.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e369e0b3-5b30-4a73-8708-e08a7b768d65"><ac:rich-text-body><ul><li>To create custom roles, you need to have the <strong>Manage Security Roles</strong> permission or the <strong>Security Manager</strong> role.</li><li>You cannot give global scope permissions, such as Create Resource, Manage User Permissions, Mark Data, <span style="color:var(--ds-text,#333333);">Configure Data Markings, </span>etc., to a custom role.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491537 space=TWCloud2024xR1 version=2 -->
## PAGE 00252: Understanding the user interface

- page_id: `170491537`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491537/Understanding+the+user+interface
- version_number: 2
- version_date: `2025-10-30T14:12:02.224+01:00`
- ancestors: Teamwork Cloud and Services > User Guide
- labels: []

### NORMALIZED CONTENT

The user interface of Teamwork Cloud Admin consists of 3 main sections displayed below:

[IMAGE alt='' src='']

###### Main structure of applications.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The user interface of Teamwork Cloud Admin consists of 3 main sections displayed below:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="settings_application_structure.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Main structure of applications.</h6>
````

<!--NOMAGIC_PAGE id=170491262 space=TWCloud2024xR1 version=3 -->
## PAGE 00253: Uninstallation

- page_id: `170491262`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491262/Uninstallation
- version_number: 3
- version_date: `2025-10-30T13:38:08.112+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation
- labels: []

### NORMALIZED CONTENT

**On this page**

****

This section describes how to uninstall Teamwork Cloud and Cassandra using uninstallation files. Teamwork Cloud uninstall file is located in the application installation folder (*<install_root>/UninstallerData/Uninstall*).

##### **Using the uninstall file for all services**

###### **On Linux**

To uninstall Teamwork Cloud using the uninstall file

1. Run the uninstall file to uninstall Teamwork Cloud and Teamwork Cloud Admin. bashDJangotrue/UninstallerData/Uninstall]]>
2. Press **Enter** to continue. 
[IMAGE alt='' src='']
3. Type either "1" to completely uninstall Teamwork Cloud and Teamwork Cloud Admin or "2" to uninstall selected features and follow the instructions. A message informing that Teamwork Cloud and Teamwork Cloud Admin uninstallation is complete will appear. 
[IMAGE alt='' src='']

**Managing separate services**

To uninstall Teamwork Cloud, Web Application Platform, and Cassandra

1. Stop Teamwork Cloud and WebApp Server.
2. Remove the services.
3. Delete the directory in which Teamwork Cloud is installed.
4. Uninstall Cassandra.

```text

```

If you need to remove only selected services, remove them using the following commands:

- Remove Teamwork Cloud service using the following script: bashDJangotrue/scripts/linux/uninstallservice.sh]]>
- Remove WebApp service using the following script: bashDJangotrue/WebAppPlatform/bin/service.sh remove]]>
- Remove Zookeeper service using the following script: bashDJangotrue/WebAppPlatform/zookeeper/bin/zkService.sh remove]]>

To uninstall Cassandra

1. Delete the directory in which Teamwork Cloud is installed (*<install_root>*).
2. Uninstall Cassandra using the following commands: bashDJangotrue

###### **On Windows**

To uninstall Teamwork Cloud using the uninstall file

1. Stop Teamwork Cloud, AuthServer, and WebApp services from the Services window.
2. Run the uninstall file, located at *<install_root>/UninstallerData/Uninstall.exe* to uninstall Teamwork Cloud. The **Uninstall Teamwork Cloud** dialog will open. [IMAGE alt='' src='']
3. Click [IMAGE alt='' src='']. Teamwork Cloud will uninstall itself. The dialog will close once the uninstallation is complete.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="495ea7fa-6fe0-438b-9481-61295770e1aa" /></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This section describes how to uninstall Teamwork Cloud and Cassandra using uninstallation files. Teamwork Cloud uninstall file is located in the application installation folder (<em>&lt;install_root&gt;/UninstallerData/Uninstall</em>).</p><h3 style="color:var(--ds-text,#172b4d);"><strong>Using the uninstall file for all services</strong></h3><h4 style="line-height: 1.42857;color:var(--ds-text,#172b4d);"><strong>On Linux</strong></h4><p>To uninstall Teamwork Cloud using the uninstall file</p><hr style="" /><ol><li><p>Run the uninstall file to uninstall Teamwork Cloud and Teamwork Cloud Admin. </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="057bcadb-460a-40f2-a898-7a27c535d103"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo <install_root>/UninstallerData/Uninstall]]></ac:plain-text-body></ac:structured-macro></li><li><p>Press <strong>Enter</strong> to continue.<br /><ac:image><ri:attachment ri:filename="1.prepare_to_uninstall.png" /></ac:image><br /><br /></p></li><li><p>Type either &quot;1&quot; to completely uninstall Teamwork Cloud and Teamwork Cloud Admin or &quot;2&quot; to uninstall selected features and follow the instructions. A message informing that Teamwork Cloud and Teamwork Cloud Admin uninstallation is complete will appear.<br /><ac:image><ri:attachment ri:filename="2.uninstall_option.png" /></ac:image></p></li></ol><p><br /></p><p><strong>Managing separate services</strong></p><p>To uninstall Teamwork Cloud<ac:inline-comment-marker ac:ref="223e9f07-5036-4b65-9102-4033bb9e3f4a">,</ac:inline-comment-marker> Web Application Platform, and Cassandra</p><hr style="" /><ol><li>Stop Teamwork Cloud and WebApp Server.</li><li>Remove the services.</li><li>Delete the directory in which Teamwork Cloud is installed. </li><li>Uninstall Cassandra.</li></ol><pre style="margin-top: 0.0px;">       </pre><p>If you need to remove only selected services, remove them using the following commands:</p><ul><li><p>Remove Teamwork Cloud service using the following script: </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="6111bd16-46c9-44ab-8ef5-76de40da04ff"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo <install_root>/scripts/linux/uninstallservice.sh]]></ac:plain-text-body></ac:structured-macro></li><li><p>Remove WebApp service using the following script: </p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="763424cd-1490-4a0c-988f-6112995442fd"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo <install_root>/WebAppPlatform/bin/service.sh remove]]></ac:plain-text-body></ac:structured-macro></li><li><p class="auto-cursor-target">Remove Zookeeper service using the following script:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="865a6a51-71a7-456e-8837-2b4357f0a4f2"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo <install_root>/WebAppPlatform/zookeeper/bin/zkService.sh remove]]></ac:plain-text-body></ac:structured-macro></li></ul><p><span style="letter-spacing: 0.0px;">To uninstall Cassandra</span></p><hr style="" /><ol><li><p>Delete the directory in which Teamwork Cloud is installed (<em>&lt;install_root&gt;</em>).</p></li><li><p>Uninstall Cassandra using the following commands:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1c897cfd-6a99-4fd3-8af9-8c03a21d0102"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo service cassandra stop
sudo yum remove cassandra]]></ac:plain-text-body></ac:structured-macro></li></ol><h4 style="line-height: 1.42857;color:var(--ds-text,#172b4d);"><strong>On Windows</strong></h4><p>To uninstall Teamwork Cloud using the uninstall file</p><hr style="" /><ol><li><p>Stop Teamwork Cloud, AuthServer, and WebApp services from the Services window.</p></li><li><p>Run the uninstall file, located at <em>&lt;install_root&gt;/UninstallerData/Uninstall.exe</em> to uninstall Teamwork Cloud. The <strong>Uninstall Teamwork Cloud</strong> dialog will open.</p><p><ac:image><ri:attachment ri:filename="uninstallstep1.png" /></ac:image></p></li><li><p>Click <ac:image><ri:attachment ri:filename="uninstall_button.png" /></ac:image>. Teamwork Cloud will uninstall itself. The dialog will close once the uninstallation is complete.</p></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180317 space=TWCloud2024xR1 version=6 -->
## PAGE 00254: Unlocking resource elements

- page_id: `171180317`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180317/Unlocking+resource+elements
- version_number: 6
- version_date: `2025-03-24T09:41:44.841+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application
- labels: []

### NORMALIZED CONTENT

When multiple users work on a single project, they may [CONFLUENCE_PAGE title='Locking model for edit' space='MD2024xR1'] different parts of that project. The Resources application allows you to unlock all the elements of a project locked by several different users.

You can use the Users application to [CONFLUENCE_PAGE title='Releasing locked elements' space=''].

#### NOTE: Prerequisites

Prerequisites

To release locked elements, you must have the Resource Locks Administrator role (or the Read Resources and Release Resource Locks permissions) for the resources you want to unlock. [CONFLUENCE_PAGE title='Permissions' space=''].

To release locked elements

1. Navigate to the Resources application and do one of the following:
  - Click [ATTACHMENT filename='menu.png'] next to the resource, and choose Release locked elements .
  - Click the resource and in the**Resource**pane, click**[IMAGE alt='' src='']**and choose**Release locked elements**. You can use the locked element filter to search for elements according to username or branch name.
2. **Release locked elements** pane opens. Select elements. If a project is locked in different branches, releasing the lock(s) on a branch will not release other locks in the other branches.
3. Click the **Unlock** button.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When multiple users work on a single project, they may <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Locking model for edit" /><ac:plain-text-link-body><![CDATA[lock]]></ac:plain-text-link-body></ac:link> different parts of that project. The Resources application allows you to unlock all the elements of a project locked by several different users.</p><p>You can use the Users application to <ac:link><ri:page ri:content-title="Releasing locked elements" /><ac:plain-text-link-body><![CDATA[unlock the elements of several different projects locked by a single user]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ac674c0d-a573-42db-a380-800552bf59bf"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>To release locked elements, you must have the Resource Locks Administrator role (or the Read Resources and Release Resource Locks permissions) for the resources you want to unlock. <ac:link><ri:page ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[Learn more about roles and their permissions]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To release locked elements</p><hr /><ol><li>Navigate to the Resources application and do one of the following: <ul><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource, and choose<strong> Release locked </strong><strong>elements</strong>.</li><li><p class="auto-cursor-target">Click the resource and in the<strong> Resource </strong>pane, click<strong> <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> </strong>and choose<strong> Release locked elements</strong>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2e3f6ae1-8b3f-45f2-9723-149b8ccb953c"><ac:rich-text-body><p><span>You can use the locked element filter to search for elements according to username or branch name.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li><li><p><strong> Release locked elements</strong> pane opens. Select elements. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="40f0e9b7-fd31-459d-977f-b05df72ad218"><ac:rich-text-body><p>If a project is locked in different branches, releasing the lock(s) on a branch will not release other locks in the other branches.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>Click the <strong>Unlock</strong> button.</p></li></ol>
````

<!--NOMAGIC_PAGE id=178166250 space=TWCloud2024xR1 version=10 -->
## PAGE 00255: Upgrade and data migration

- page_id: `178166250`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/178166250/Upgrade+and+data+migration
- version_number: 10
- version_date: `2025-06-04T13:55:41.408+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation
- labels: []

### NORMALIZED CONTENT

Refer to the table below to determine your Teamwork Cloud upgrade path.

| Teamwork Cloud Software Upgrade Path |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 19.0 | Database Migration 19.0 | 19.0 SP3 | Database Migration 2021x | 2021x | Cassandra Upgrade | 2021x Refresh2 HF5 |  |
| 19.0 SP1 | 19.0 SP4 | 2021x Refresh1 | 2022x |  |  |  |  |
| 19.0 SP2 | 2021x Refresh2 | 2022x Refresh1 |  |  |  |  |  |
| 2021x Refresh2 HF5 | 2022x Refresh2 |  |  |  |  |  |  |
| 2024x |  |  |  |  |  |  |  |
| 2024x Refresh1 |  |  |  |  |  |  |  |
| Cassandra 3 | Cassandra 4 |  |  |  |  |  |  |

How to use the table:

- Find the version of Teamwork Cloud you are currently running.
- Find the target version you would like to upgrade to.
- If you are upgrading from left to right, you need to migrate the database and/or upgrade Cassandra as well as the Teamwork Cloud software.
- You cannot skip database migration and upgrade steps when upgrading from left to right.
- You can upgrade directly between non-consecutive versions (for example, from 2021x to 2024x), but you may need to upgrade Cassandra.
- If you upgrade vertically down a single column, you only need to upgrade the Teamwork Cloud software. Intermediate versions can be skipped as well.

- The procedures of data migration for versions 19.0 & 2021x are completely different. See the following pages on migrating data and upgrading Teamwork Cloud for the relevant target version:
  - [CONFLUENCE_PAGE title='Migrating data and upgrading TWCloud' space='TWCloud190SP4']
  - [CONFLUENCE_PAGE title='Migrating data and upgrading Teamwork Cloud' space='TWCloud2021xR2']
- Teamwork Cloud 2021x Refresh 2 HF5 supports both Cassandra 3 and 4.

###### Upgrade guides

1. [CONFLUENCE_PAGE title='Backup and restore data procedures' space=''] before any upgrade! Once you upgrade Teamwork Cloud, you cannot downgrade it. Major database changes occur with each Teamwork Cloud upgrade and data cannot be reverted.
2. [CONFLUENCE_PAGE title='Upgrading Cassandra' space=''] (if needed).
3. [CONFLUENCE_PAGE title='Upgrading Teamwork Cloud and services' space=''].
4. [CONFLUENCE_PAGE title='Migrating projects' space='MD2024xR1'].

When migrating from the Teamwork Cloud server version earlier than 2022x Refresh1, you must**[CONFLUENCE_PAGE title='Data Manager' space='']** with usernames in different cases (e.g., *JOHN*and *john*) if such usernames exist. Leave just one user. Otherwise, authentication of these duplicate user entries might fail in 2022x Refresh1 or newer versions.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>Refer to the table below to determine your Teamwork Cloud upgrade path.</span></p><table class="relative-table wrapped" style="width: 73.6149%;"><colgroup><col style="width: 13.0501%;" /><col style="width: 13.945%;" /><col style="width: 14.0195%;" /><col style="width: 13.1992%;" /><col style="width: 13.7958%;" /><col style="width: 13.7202%;" /><col style="width: 15.3618%;" /><col style="width: 2.98288%;" /></colgroup><tbody><tr><th style="text-align: center;" colspan="8" scope="colgroup"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="black_arrow_right.png" /></ac:image> Teamwork Cloud Software Upgrade Path <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="black_arrow_right.png" /></ac:image></p></div></th></tr><tr><td>19.0</td><td rowspan="6"><div class="content-wrapper"><p style="text-align: center;"><br /></p><p style="text-align: center;">Database Migration 19.0</p><p style="text-align: center;"><ac:image ac:thumbnail="true" ac:height="40"><ri:attachment ri:filename="red_arrow_right.png" /></ac:image></p><p style="text-align: center;"><br /></p></div><strong><br /></strong></td><td>19.0 SP3</td><td style="text-align: center;" rowspan="6"><div class="content-wrapper"><p><br /></p><p>Database Migration 2021x</p><p><ac:image ac:thumbnail="true" ac:height="40"><ri:attachment ri:filename="red_arrow_right.png" /></ac:image></p><p><br /></p></div><strong><br /></strong></td><td>2021x</td><td style="text-align: center;" rowspan="7"><div class="content-wrapper"><p><br /></p><p>Cassandra Upgrade</p><p><br /><ac:image ac:thumbnail="true" ac:height="40"><ri:attachment ri:filename="red_arrow_right.png" /></ac:image></p><p><br /></p><p><br /></p></div></td><td>2021x Refresh2 HF5</td><th rowspan="7" scope="rowgroup"><div class="content-wrapper"><p><br /></p><p><br /></p><p><br /></p><p><ac:image ac:thumbnail="true" ac:height="40"><ri:attachment ri:filename="black_arrow_down.png" /></ac:image></p></div></th></tr><tr><td>19.0 SP1</td><td rowspan="5">19.0 SP4<br /><strong><br /></strong></td><td>2021x Refresh1</td><td>2022x</td></tr><tr><td rowspan="4">19.0 SP2<br /><strong><br /></strong></td><td>2021x Refresh2</td><td>2022x Refresh1</td></tr><tr><td rowspan="3">2021x Refresh2 HF5<br /><strong><br /></strong></td><td>2022x Refresh2</td></tr><tr><td><p>2024x</p></td></tr><tr><td><p>2024x Refresh1</p></td></tr><tr><td style="text-align: center;" colspan="5"><strong>Cassandra 3</strong></td><td><p style="text-align: center;"><strong>Cassandra 4</strong></p></td></tr></tbody></table><p style="text-align: center;"><br /></p><p><span>How to use the table:</span></p><ul><li><span>Find the version of Teamwork Cloud you are currently running.</span></li><li><span>Find the target version you would like to upgrade to.</span></li><li><span>If you are upgrading from left to right, you need to migrate the database and/or upgrade Cassandra as well as the Teamwork Cloud software.</span></li><li><span>You cannot skip database migration and upgrade steps when upgrading from left to right.</span></li><li><span>You can upgrade directly between non-consecutive versions (for example, from 2021x to 2024x), but you may need to upgrade Cassandra.</span></li><li><span style="color:var(--ds-text,#333333);">If you upgrade vertically down a single column, you only need to upgrade the Teamwork Cloud software. Intermediate versions can be skipped as well.<br /><br /></span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f9d524c5-40e1-4f0b-8c78-f7cd464f3d91"><ac:rich-text-body><ul><li><span>The procedures of data migration for versions 19.0 &amp; 2021x are completely different. See the following pages on migrating data and upgrading Teamwork Cloud for the relevant target version:</span><ul><li><span><ac:link><ri:page ri:space-key="TWCloud190SP4" ri:content-title="Migrating data and upgrading TWCloud" /><ac:plain-text-link-body><![CDATA[19.0 SP4]]></ac:plain-text-link-body></ac:link></span></li><li><span><ac:link><ri:page ri:space-key="TWCloud2021xR2" ri:content-title="Migrating data and upgrading Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[2021xR2]]></ac:plain-text-link-body></ac:link></span></li></ul></li><li>Teamwork Cloud 2021x Refresh 2 HF5 supports both Cassandra 3 and 4.</li></ul></ac:rich-text-body></ac:structured-macro><h4>Upgrade guides</h4><ol><li><span> <ac:link><ri:page ri:content-title="Backup and restore data procedures" /><ac:plain-text-link-body><![CDATA[Back up your current data]]></ac:plain-text-link-body></ac:link> before any upgrade! Once you upgrade Teamwork Cloud, you cannot downgrade it. Major database changes occur with each Teamwork Cloud upgrade and data cannot be reverted.</span></li><li><span><ac:link><ri:page ri:content-title="Upgrading Cassandra" /><ac:plain-text-link-body><![CDATA[Upgrade Apache Cassandra]]></ac:plain-text-link-body></ac:link> (if needed).</span></li><li><span><ac:link><ri:page ri:content-title="Upgrading Teamwork Cloud and services" /><ac:plain-text-link-body><![CDATA[Upgrade Teamwork Cloud]]></ac:plain-text-link-body></ac:link>.</span></li><li><span><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Migrating projects" /><ac:plain-text-link-body><![CDATA[Migrate Teamwork Cloud projects]]></ac:plain-text-link-body></ac:link>.</span><span><br /><br /></span></li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="f425329d-0b3b-4f8e-98a1-4e7fdc8dc6f0"><ac:rich-text-body><p>When migrating from the Teamwork Cloud server version earlier than 2022x Refresh1, you must<strong> <ac:link ac:anchor="Deleting selected user"><ri:page ri:content-title="Data Manager" /><ac:plain-text-link-body><![CDATA[delete duplicate external LDAP users]]></ac:plain-text-link-body></ac:link></strong> with usernames in different cases (e.g., <em>JOHN </em>and <em>john</em>) if such usernames exist. Leave just one user. Otherwise, authentication of these duplicate user entries might fail in 2022x Refresh1 or newer versions.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170491260 space=TWCloud2024xR1 version=5 -->
## PAGE 00256: Upgrading Cassandra

- page_id: `170491260`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491260/Upgrading+Cassandra
- version_number: 5
- version_date: `2025-05-08T12:07:32.329+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Upgrade and data migration
- labels: []

### NORMALIZED CONTENT

**On this page**

5

###### Preparing to upgrade Cassandra

To prepare for Cassandra upgrade

1. Ensure that all Cassandra nodes are ready. Run the following command and verify that all nodes are **Up**and **Normal**: bashDJangotrue
2. Leave the Cassandra service running but stop all Teamwork Cloud services.
3. [CONFLUENCE_PAGE title='Backup and restore data procedures' space=''] before upgrading.
4. Upgrade all Cassandra data tables to current version by running the following command: bashDJangotrue This process can take a long time for large databases. Use the *jobs* option to use more threads for the operation (0 for maximum threads available, default is 2). Also, use the nohup command to run the upgrade process in the background.bashDJangotrueMake sure this process is completed before proceeding!

###### Upgrading Cassandra

To upgrade Cassandra

1. **IMPORTANT!**Flush memtables to the disk by executing the following command: bashDJangotrue
2. Stop the Cassandra service.
3. Make a note of the existing cluster name and token count with the following command: bashDJangotrue
4. Uninstall/remove Cassandra (example with yum package manager) bashDJangotrue Cassandra configuration files are saved with .rpmsave extension after uninstallation (default path: /etc/cassandra/default.conf). Archive these files for future reference.
5. Install new version of Cassandra (for installation instructions, see [CONFLUENCE_PAGE title='Installing Apache Cassandra' space=''] ).
6. Check the cluster name and token count in*cassandra.yaml.*If needed, replace the default values with the values set in the previous version. The example below shows the default values for a Cassandra installation. bashExample Cassandra 4 ConfigurationThe cluster name and token count must match those values set in the previous version of Cassandra.
7. Start the Cassandra service.
8. Check if the service is running smoothly:
  - Check the log file for startup errors.
  - Verify that all nodes have a status of **Up**and **Normal**with this command: bashDJangotrue
9. Upgrade all Cassandra data tables to current version by running the following command: bashDJangotrue This process can take a long time for large databases. Use the *jobs* option to use more threads for the operation (0 for maximum threads available, default is 2). Also, use the nohup command to run the upgrade process in the background.bashDJangotrueMake sure this process is completed before proceeding!

**Additional resources**

For more information about upgrading Apache Cassandra, see [https://www.datastax.com/learn/whats-new-for-cassandra-4/migrating-cassandra-4x](https://www.datastax.com/learn/whats-new-for-cassandra-4/migrating-cassandra-4x).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="2412fb17-54f9-46b7-8ffe-35b7799fe554"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4>Preparing to upgrade Cassandra</h4><p>To prepare for Cassandra upgrade</p><hr /><ol><li><span>Ensure that </span><span style="color: rgb(45,49,51);">all Cassandra nodes are ready. Run the following command and verify that all nodes are <strong>Up </strong>and <strong>Normal</strong>:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="39388805-b134-4df8-831c-359ad42d8b97"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nodetool status]]></ac:plain-text-body></ac:structured-macro></li><li>Leave the Cassandra service running but stop all Teamwork Cloud services.</li><li><span style="color: rgb(23,43,77);"><ac:link><ri:page ri:content-title="Backup and restore data procedures" /><ac:plain-text-link-body><![CDATA[Back up your current database]]></ac:plain-text-link-body></ac:link> before upgrading.</span></li><li><span style="color: rgb(23,43,77);">Upgrade all Cassandra data tables to current version by running</span> the following command:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="944d4e71-0e00-4a85-a880-db37f9203df8"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nodetool upgradesstables]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="cb0f8498-b895-43b0-8bdb-58109a9f3ebd"><ac:rich-text-body><p>This process can take a long time for large databases. Use the <em>jobs</em> option to use more threads for the operation (0 for maximum threads available, default is 2). Also, use the nohup command to run the upgrade process in the background.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="7ecb5d9b-8df6-4aa6-998c-f0cb99b5943e"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nohup nodetool upgradesstables --jobs 0 &]]></ac:plain-text-body></ac:structured-macro><p>Make sure this process is completed before proceeding!</p></ac:rich-text-body></ac:structured-macro></li></ol><h4>Upgrading Cassandra</h4><p>To upgrade Cassandra</p><hr /><ol><li><p><span style="color: rgb(255,0,0);"><strong>IMPORTANT!</strong></span><span style="color: rgb(62,63,64);"><span> </span></span>Flush memtables to the disk by executing the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="b3027307-10b0-46c5-9a17-8d26a88b7b34"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nodetool drain]]></ac:plain-text-body></ac:structured-macro></li><li><p>Stop the Cassandra service.</p></li><li><p>Make a note of the existing cluster name and token count with the following command:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="1d4f6a9b-7588-4c13-876f-8ccddc0189f8"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[grep -E 'num_tokens:|cluster_name:' cassandra.yaml]]></ac:plain-text-body></ac:structured-macro></li><li><p>Uninstall/remove Cassandra (example with yum package manager)</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="34d2b498-ae0a-4e2c-b744-14a4590659dd"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[sudo yum remove -y cassandra]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="60168ca8-572e-441e-b6b7-20b1afcd783f"><ac:rich-text-body><p>Cassandra configuration files are saved with .rpmsave extension after uninstallation (default path: /etc/cassandra/default.conf). Archive these files for future reference.</p></ac:rich-text-body></ac:structured-macro></li><li>Install new version of Cassandra (for installation instructions, see <ac:link><ri:page ri:content-title="Installing Apache Cassandra" /><ac:plain-text-link-body><![CDATA[Installing Cassandra on Linux]]></ac:plain-text-link-body></ac:link>).</li><li><p><span>Check the cluster name and token count in </span><em>cassandra.yaml.</em><span> If needed, replace the default values with the values set in the previous version. The example below shows the default values for a Cassandra installation.</span></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="5699a9cb-251a-4223-8c53-1696f20dda66"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="title">Example</ac:parameter><ac:plain-text-body><![CDATA[cluster_name: 'Test Cluster'
num_tokens: 16]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7f562e9f-cb06-4d82-8558-0ed3a029ff01"><ac:parameter ac:name="title">Cassandra 4 Configuration</ac:parameter><ac:rich-text-body><p>The cluster name and token count must match those values set in the previous version of Cassandra.</p></ac:rich-text-body></ac:structured-macro></li><li>Start the Cassandra service.</li><li><p>Check if the service is running smoothly:</p><ul><li><p>Check the log file for startup errors.</p></li><li><p><span style="color: rgb(23,43,77);">Verify that all nodes have a status of <strong>Up </strong>and <strong>Normal </strong>with this command</span>:</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="78a2c606-57a6-4fd6-a946-69694be5b8ea"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nodetool status]]></ac:plain-text-body></ac:structured-macro></li></ul></li><li><span style="color: rgb(23,43,77);">Upgrade all Cassandra data tables to current version by running</span> the following command:<br /><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="c3d5a182-cf9c-47ff-ad59-af6f52f39e62"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nodetool upgradesstables]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7fc9cddd-619f-4de2-bab4-1ab3e62fa569"><ac:rich-text-body><p>This process can take a long time for large databases. Use the <em>jobs</em> option to use more threads for the operation (0 for maximum threads available, default is 2). Also, use the nohup command to run the upgrade process in the background.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="a925c9eb-2fa5-4ec5-833a-c71c698d01c9"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[nohup nodetool upgradesstables --jobs 0 &]]></ac:plain-text-body></ac:structured-macro><p>Make sure this process is completed before proceeding!</p></ac:rich-text-body></ac:structured-macro></li></ol></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><p>For more information about upgrading Apache Cassandra, see <a href="https://www.datastax.com/learn/whats-new-for-cassandra-4/migrating-cassandra-4x">https://www.datastax.com/learn/whats-new-for-cassandra-4/migrating-cassandra-4x</a>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491261 space=TWCloud2024xR1 version=1 -->
## PAGE 00257: Upgrading Teamwork Cloud and services

- page_id: `170491261`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491261/Upgrading+Teamwork+Cloud+and+services
- version_number: 1
- version_date: `2023-12-20T11:46:55.787+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Upgrade and data migration
- labels: []

### NORMALIZED CONTENT

This chapter explains how to upgrade Teamwork Cloud to a new version. After upgrading Teamwork Cloud, the database schema is updated automatically on the first Teamwork Cloud start-up.

#### NOTE: Prerequisites

Prerequisites

Before upgrading Teamwork Cloud, [CONFLUENCE_PAGE title='Upgrading Cassandra' space=''].

To upgrade Teamwork Cloud to a new version

1. Stop the Teamwork Cloud services.
2. (Optional) Make a copy of the installation directory - this will leave a reference to the existing configuration, as well as a source for your signed certificates if you are not using the self-signed certificates generated during installation.
3. [CONFLUENCE_PAGE title='Uninstallation' space=''] older versions from your machine.
4. Install the new version of Teamwork Cloud on [CONFLUENCE_PAGE title='Installation on Linux' space=''] or [CONFLUENCE_PAGE title='Installation on Windows' space='']. If you have changed the default Administrator username and password, you must update the **twc.admin.username** and **twc.admin.password** parameters, in the web application configuration file at *<install_root>/WebAppPlatform/shared/conf/webappplatform.properties*.
5. Start Teamwork Cloud, Zookeeper, and WebApp services. Initial Teamwork Cloud start-upmay take several minutes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter explains how to upgrade Teamwork Cloud to a new version. After upgrading Teamwork Cloud, the database schema is updated automatically on the first Teamwork Cloud start-up.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="796975eb-9f5e-405e-9459-9383b8ff56be"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p>Before upgrading Teamwork Cloud, <ac:link><ri:page ri:content-title="Upgrading Cassandra" /><ac:plain-text-link-body><![CDATA[upgrade Apache Cassandra 3.x to version 4.x]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To upgrade Teamwork Cloud to a new version</p><hr /><ol><li><p>Stop the Teamwork Cloud services.</p></li><li>(Optional) Make a copy of the installation directory - this will leave a reference to the existing configuration, as well as a source for your signed certificates if you are not using the self-signed certificates generated during installation.</li><li><p><ac:link><ri:page ri:content-title="Uninstallation" /><ac:plain-text-link-body><![CDATA[Uninstall]]></ac:plain-text-link-body></ac:link> older versions from your machine.</p></li><li><p class="auto-cursor-target">Install the new version of Teamwork Cloud on <ac:link><ri:page ri:content-title="Installation on Linux" /><ac:plain-text-link-body><![CDATA[Linux]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Installation on Windows" /><ac:plain-text-link-body><![CDATA[Windows]]></ac:plain-text-link-body></ac:link>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a0a0f717-7385-4b1e-a548-2adb3980fa97"><ac:rich-text-body><p>If you have changed the default Administrator username and password, you must update the <strong>twc.admin.username</strong> and <strong>twc.admin.password</strong> parameters, in the web application configuration file at <em>&lt;install_root&gt;/WebAppPlatform/shared/conf/webappplatform.properties</em>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">Start Teamwork Cloud, Zookeeper, and WebApp services.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="bf886744-3424-4e61-a3a4-bb7010c78352"><ac:rich-text-body><span>Initial Teamwork Cloud start-up </span>may take several minutes.</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol>
````

<!--NOMAGIC_PAGE id=170491303 space=TWCloud2024xR1 version=2 -->
## PAGE 00258: Upgrading Web Application Platform

- page_id: `170491303`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491303/Upgrading+Web+Application+Platform
- version_number: 2
- version_date: `2025-09-15T13:10:34.751+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: []

### NORMALIZED CONTENT

If you want to upgrade Web Application Platform and its plugins to a newer version, follow the instructions provided in the appropriate section depending on your installation tipe and operating system.

#### WARNING: Compatibility

Compatibility

Before starting, check [Web Application Platform compatibility with its plugins and Teamwork Cloud](https://www.nomagic.com/support/compatibility#Teamwork%2520Cloud).

##### Upgrading Web Application Platform on Linux

If you use Linux, upgrade Web Application Platform as described below.

To upgrade Web Application Platform on Linux

1. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] .
2. Run the <install_root>/UninstallerData / Uninstall.sh file to uninstall the current version of Web Application Platform.
3. [CONFLUENCE_PAGE title='Installing Web Application Platform on Linux' space=''] .

##### Upgrading Web Application Platform on Windows

If you use Windows, upgrade Web Application Platform as described below.

To upgrade Web Application Platform on Windows

1. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] .
2. Go to <install_root>\UninstallerData and run the Uninstall.exe file.
3. When the uninstaller is started, click the Uninstall button.
4. Wait until Web Application Platform is uninstalled and click Done .
5. [CONFLUENCE_PAGE title='Installing Web Application Platform on Windows' space=''] .

##### Upgrading the manual installation of Web Application Platform

If you [CONFLUENCE_PAGE title='Installing Web Application Platform manually' space=''], upgrade it by following the steps below.

To upgrade Web Application Platform

1. [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] .
2. Delete the installation directory of the web application container on which the Web Application Platform runs (e.g., Apache Tomcat).
3. [CONFLUENCE_PAGE title='Installing Web Application Platform manually' space=''] .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>If you want to upgrade Web Application Platform and its plugins to a newer version, follow the instructions provided in the appropriate section depending on your installation tipe and operating system.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="88ab235c-7a70-4f41-a7b5-62b661c7065a"><ac:parameter ac:name="title">Compatibility</ac:parameter><ac:rich-text-body><p>Before starting, check <a href="https://www.nomagic.com/support/compatibility#Teamwork%2520Cloud">Web Application Platform compatibility with its plugins and Teamwork Cloud</a>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Upgrading Web Application Platform on Linux</h3><p>If you use Linux, upgrade Web Application Platform as described below.</p><p><br /></p><p>To upgrade Web Application Platform on Linux</p><hr /><ol><li><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Stop Web Application Platform]]></ac:plain-text-link-body></ac:link>.</li><li>Run the <em>&lt;install_root&gt;/UninstallerData</em>/<em>Uninstall.sh</em> file to uninstall the current version of Web Application Platform.</li><li><ac:link><ri:page ri:content-title="Installing Web Application Platform on Linux" /><ac:plain-text-link-body><![CDATA[Install the new version of Web Application Platform and its plugins]]></ac:plain-text-link-body></ac:link>.</li></ol><h3><br />Upgrading Web Application Platform on Windows</h3><p>If you use Windows, upgrade Web Application Platform as described below.</p><p><br /></p><p>To upgrade Web Application Platform on Windows</p><hr /><ol><li><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Stop Web Application Platform]]></ac:plain-text-link-body></ac:link>.</li><li>Go to <em>&lt;install_root&gt;\UninstallerData</em> and run the <em>Uninstall.exe</em> file.</li><li>When the uninstaller is started, click the <strong>Uninstall</strong> button.</li><li>Wait until Web Application Platform is uninstalled and click <strong>Done</strong>.</li><li><ac:link><ri:page ri:content-title="Installing Web Application Platform on Windows" /><ac:plain-text-link-body><![CDATA[Install the new version of Web Application Platform and its plugins]]></ac:plain-text-link-body></ac:link>.</li></ol><h3><br />Upgrading the manual installation of Web Application Platform</h3><p>If you <ac:link><ri:page ri:content-title="Installing Web Application Platform manually" /><ac:plain-text-link-body><![CDATA[installed Web Application Platform manually]]></ac:plain-text-link-body></ac:link>, upgrade it by following the steps below.</p><p><br /></p><p>To upgrade Web Application Platform</p><hr /><ol><li><ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[Stop Web Application Platform]]></ac:plain-text-link-body></ac:link>.</li><li data-uuid="4b50913b-5350-40b9-beb9-d7bc7113f119">Delete the installation directory of the web application container<span style="color:var(--ds-text,#333333);"> on which the Web Application Platform runs (e.g., <span style="color:var(--ds-text,#333333);">Apache Tomcat).</span></span></li><li><ac:link><ri:page ri:content-title="Installing Web Application Platform manually" /><ac:plain-text-link-body><![CDATA[Install the new version of Web Application Platform and its plugins]]></ac:plain-text-link-body></ac:link>.</li></ol>
````

<!--NOMAGIC_PAGE id=170491499 space=TWCloud2024xR1 version=1 -->
## PAGE 00259: User Guide

- page_id: `170491499`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491499/User+Guide
- version_number: 1
- version_date: `2024-01-29T09:35:48.020+01:00`
- ancestors: Teamwork Cloud and Services
- labels: []

### NORMALIZED CONTENT

This guide explains how to use Teamwork Cloud Admin web applications and Cameo Collaborator for Teamwork Cloud.

To learn more, refer to:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="6085b51a-f948-4e5a-a650-89aaee822da6">This guide explains how to use Teamwork Cloud Admin web applications and Cameo Collaborator for Teamwork Cloud.</ac:inline-comment-marker></p><p>To learn more, refer to:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491841 space=TWCloud2024xR1 version=2 -->
## PAGE 00260: User roles and permissions

- page_id: `170491841`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491841/User+roles+and+permissions
- version_number: 2
- version_date: `2025-10-30T14:21:24.492+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Roles application
- labels: []

### NORMALIZED CONTENT

A role is an identity that distinguishes one user's rights from another's. It determines which job functions a user has in the Teamwork Cloud system by giving a set of permissions to a user to perform one or more operations within the Teamwork Cloud system. New permissions can be added as new resources or tasks are created. You can create a user without giving the user any role. You can also create a new role first and assign it to a user later. The Teamwork Cloud Admin displays all roles on the **[CONFLUENCE_PAGE title='Roles application structure' space='']**application.

An authorized user, such as a User Manager (role), can create a new user account in Teamwork Cloud Admin and can assign a role to access and work on a particular resource. A user can have more than one role and handle more than one resource. Creating a new user and assigning a role with a resource to the user can be done at the same time. In Teamwork Cloud Admin, you can assign a role to more than one user at the same time. Users can be reassigned from one role to another. Only authorized users can access Resources in Teamwork Cloud.

##### Resources

A document, project, or OSCL resource are called resources in the Teamwork Cloud environment. A modeling tool project (or document) in Teamwork Cloud is protected and only authorized users can access and work with them.

When assigning a resource to a user, you need to define the role scope. If you select the global scope, you authorize the user to work on any resource in the Teamwork Cloud system. For more information on the global and custom scope, see [CONFLUENCE_PAGE title='Scopes of roles' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A role is an identity that distinguishes one user's rights from another's. It determines which job functions a user has in the Teamwork Cloud system by giving a set of permissions to a user to perform one or more operations within the Teamwork Cloud system. New permissions can be added as new resources or tasks are created. You can create a user without giving the user any role. You can also create a new role first and assign it to a user later. The Teamwork Cloud Admin displays all roles on the <strong><ac:link><ri:page ri:content-title="Roles application structure" /><ac:plain-text-link-body><![CDATA[Roles ]]></ac:plain-text-link-body></ac:link></strong>application.</p><p>An authorized user, such as a User Manager (role), can create a new user account in Teamwork Cloud Admin and can assign a role to access and work on a particular resource. A user can have more than one role and handle more than one resource. Creating a new user and assigning a role with a resource to the user can be done at the same time. In Teamwork Cloud Admin, you can assign a role to more than one user at the same time. Users can be reassigned from one role to another. Only authorized users can access Resources in Teamwork Cloud. </p><h3 style="color:var(--ds-text,#172b4d);">Resources</h3><p>A document, project, or OSCL resource are called resources in the Teamwork Cloud environment. A modeling tool project (or document) in Teamwork Cloud is protected and only authorized users can access and work with them.  </p><p class="O1">When assigning a resource to a user, you need to define the role scope. If you select the global scope, you authorize the user to work on any resource in the Teamwork Cloud system. For more information on the global and custom scope, see <ac:link><ri:page ri:content-title="Scopes of roles" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=170491554 space=TWCloud2024xR1 version=2 -->
## PAGE 00261: Users application

- page_id: `170491554`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491554/Users+application
- version_number: 2
- version_date: `2024-05-09T13:41:28.009+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications
- labels: []

### NORMALIZED CONTENT

This section contains the information needed for managing Teamwork Cloud users and user groups.

The**User**is usually created to work on authorized resources via modeling tool. There are two categories of users in the Teamwork Cloud system: internal and external.

- Internal users are originally created in Teamwork Cloud Admin and therefore their usernames, passwords, and other data are stored in Teamwork Cloud.
- External users are from LDAP servers who were imported into the Teamwork Cloud system or SAML users who passed the [CONFLUENCE_PAGE title='Authentication server' space='TWC2024xR1'] and were automatically created as external users in Teamwork Cloud.

The**User group** is used to group users, assigning the same role to all users in the same group. You can manage both internal and external groups.

**Users**application structure and functionality:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section con<ac:inline-comment-marker ac:ref="06314f86-35cc-4e5a-8191-48031bae93a9">tains the info</ac:inline-comment-marker>rmation needed for managing Teamwork Cloud users and user groups.</p><p>The<strong> User </strong><span style="color: rgb(62,63,64);">is usually created to work on authorized resources via modeling tool. <span style="color: rgb(62,63,64);">There are two categories of users in the Teamwork Cloud system: internal and external.</span></span></p><ul><li><strong>Internal users</strong> <span style="color: rgb(62,63,64);">are originally created in Teamwork Cloud Admin and therefore their usernames, passwords, and other data are stored in Teamwork Cloud.</span></li><li><strong>External users </strong><span style="color: rgb(62,63,64);">are from LDAP servers who were imported into the Teamwork Cloud system or SAML users who passed the </span><ac:link><ri:page ri:space-key="TWC2024xR1" ri:content-title="Authentication server" /><ac:plain-text-link-body><![CDATA[authentication process]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"> and were automatically created as external users in Teamwork Cloud.</span></li></ul><p>The<strong> User group</strong> i<span style="color: rgb(62,63,64);">s used to group users, assigning the same role to all users in the same group. You can manage both internal and external groups. </span></p><p><strong>Users</strong><span style="color: rgb(62,63,64);"> application structure and functionality: </span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491559 space=TWCloud2024xR1 version=3 -->
## PAGE 00262: Users application structure

- page_id: `170491559`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491559/Users+application+structure
- version_number: 3
- version_date: `2025-10-30T14:13:52.704+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Users application
- labels: []

### NORMALIZED CONTENT

The **Users application** contains a list of all users and user groups. Information about them includes usernames (or group names), full names, last activity, and login status (**Enable** or **Disable**).

Only a user with a User Manager role can create a new user and/or change a user's password.

Only authorized users can view all users in the Teamwork Cloud system. There are individual users and user groups in Teamwork Cloud, which are classified as external/internal users and external/internal user groups. External users or user groups are imported from external LDAP servers. Internal users or user groups are created in Teamwork Cloud. You can learn more about internal and external users in the section [Managing users](https://docs.nomagic.com/display/TWCloud2024xR1/Managing+users), and internal and external user groups in the section [CONFLUENCE_PAGE title='Managing user groups' space=''].

To open Users application

- Click [ATTACHMENT filename='plugins.png'] and select Users application.

[IMAGE alt='' src='']

###### Users application structure.

The table below describes the UI components in the **User**application.

| UI Components | Description |
| --- | --- |
| App bar | >]]> |
| User/User group search bar | The textbox allows you to search for a user/user group by username or keyword. You can type any alphabetic character, numeric value, or symbol (such as @, &, or #), or a combination of them in the search box. The search is not case-sensitive. By default, the search result will return all usernames that match the keyword or letter(s) entered and display them on the page. |
| User/User group filters | The left side menu filters internal and external users/groups. Numbers next to each filter name show how many internal/external users/user groups there are. Internal users/groups can be distinguished from external users/groups by different icons: - Internal users - External users - Internal groups - External groupsYou can also opt in to in the user list. |
| Name column | This column shows a username or group name. You can sort internal and external users by clicking this column name (). Users will be sorted alphabetically ascending/descending. >]]> |
| Full Name or Description column | This column shows the full name of a user. When creating a new user, you may type the full name or leave it blank (optional). If it is a group, you can add a short group description. |
| Last Activity Date column | This column shows the time and date of the user's last activity on Teamwork Cloud. The time-date format is DD/MM/YYYY HH:MM. This data appears only for users and will not be shown when viewing group information. Internal and external users can be sorted by clicking this column name (). Users will be sorted by the last activity date ascending/descending. However, groups cannot be sorted. >]]> |
| Content pane | Different user colors show the user status in Teamwork Cloud Admin:A grey-colored user indicates that the user is disabled and not allowed to log into Teamwork Cloud Admin and Teamwork Cloud in MagicDraw. A black-colored user indicates that the user is enabled and they can use their user account (username and password) to log into Teamwork Cloud Admin.>]]> |
| User/User group activity button | The drop-down menu allows you to edit user information and change user login access (enable or disable). |
| Add button | The Add button opens the Create User/Group pane, which allows you to create a new user/group. See for more information. |

##### User group

A user group gathers multiple users and gives the same role assignments to the users in the same group. When you create a user group and assign role assignments (including the scope), you assign them to all of the members in the user group. You can update information and delete a user group. You can also [CONFLUENCE_PAGE title='Importing users and groups' space=''] a user group from an LDAP server as an external user group. All members of the user group will be imported to Teamwork Cloud as external users as well. To update the information for an external user group in Teamwork Cloud, you must resynchronize it with that of the LDAP server.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <strong>Users application</strong> contains a list of all users and user groups. Information about them includes usernames (or group names), full names, last activity, and login <ac:inline-comment-marker ac:ref="e088d8d9-6c45-43b8-a4a2-95e3a1c12ee2">status</ac:inline-comment-marker> (<strong>Enable</strong> or <strong>Disable</strong>).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0fd1b6f5-c566-47cd-b69e-9f2ed7eefb22"><ac:rich-text-body><p>Only a user with a User Manager role can create a new user and/or change a user's password.</p></ac:rich-text-body></ac:structured-macro><p>Only authorized users can view all users in the Teamwork Cloud system. There are individual users and user groups in Teamwork Cloud, which are classified as external/internal users and external/internal user groups. External users or user groups are imported from external LDAP servers. Internal users or user groups are created in Teamwork Cloud. You can learn more about internal and external users in the section <a href="https://docs.nomagic.com/display/TWCloud2024xR1/Managing+users" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Managing users</a>, and internal and external user groups in the section <ac:link><ri:page ri:content-title="Managing user groups" /></ac:link>.</p><p><br /></p><p>To open Users application </p><hr style="" /><ul><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="plugins.png" /></ac:image> and select <strong>Users</strong> application.</li></ul><p><br /></p><p><ac:image><ri:attachment ri:filename="Users_app_structure.png" /></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Users application structure.</h6><p>The table below describes the UI components in the <strong>User </strong>application.<br class="atl-forced-newline" /><br class="atl-forced-newline" /></p><table class="wrapped relative-table" style="margin-left: 30.0px;width: 2330.06px;"><colgroup><col style="width: 434.672px;" /><col style="width: 1894.39px;" /></colgroup><tbody style="margin-left: 30.0px;"><tr style="margin-left: 30.0px;"><th style="background-color: rgb(241,242,244);margin-left: 30.0px;color:var(--ds-text,#172b4d);"><strong>UI Components</strong></th><th style="background-color: rgb(241,242,244);margin-left: 30.0px;color:var(--ds-text,#172b4d);"><strong>Description</strong></th></tr><tr style="margin-left: 30.0px;"><td style=""><strong>App bar</strong></td><td style=""><ac:link><ri:page ri:content-title="Using the app bar" /><ac:plain-text-link-body><![CDATA[Learn more about app bar here >>]]></ac:plain-text-link-body></ac:link></td></tr><tr style="margin-left: 30.0px;"><td style=""><strong>User/User group search bar</strong></td><td style="">The textbox allows you to search for a user/user group by username or keyword. You can type any alphabetic character, numeric value, or symbol (such as @, &amp;, or #), or a combination of them in the search box. The search is not case-sensitive. By default, the search result will return all usernames that match the keyword or letter(s) entered and display them on the page.</td></tr><tr style="margin-left: 30.0px;"><td style=""><div class="content-wrapper"><p><strong>User/User group filters</strong></p></div></td><td style=""><div class="content-wrapper"><p>The left side menu filters internal and external users/groups. Numbers next to each filter name show how many internal/external users/user groups there are. Inte<ac:inline-comment-marker ac:ref="dfbb63f5-5418-4b2e-8e78-17a91d418744">rnal users/gro</ac:inline-comment-marker>ups can be distinguished from external users/groups by different icons:</p><p><ac:image><ri:attachment ri:filename="Internal_user.png" /></ac:image> - Internal users</p><p><ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="External_user.png" /></ac:image> - External users</p><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="Internal_groups.png" /></ac:image> - Internal groups</p><p><ac:image ac:thumbnail="true" ac:height="19"><ri:attachment ri:filename="External_groups.png" /></ac:image> - External groups</p><p>You can also opt in to <ac:link><ri:page ri:content-title="Displaying disabled users" /><ac:plain-text-link-body><![CDATA[display disabled users]]></ac:plain-text-link-body></ac:link> in the user list.</p></div></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><strong>Name column</strong></td><td style="margin-left: 30.0px;"><div class="content-wrapper"><p>This column shows a username or group name. You can sort internal and external users by clicking this column name (<ac:image><ri:attachment ri:filename="sorting.PNG" /></ac:image>). Users will be sorted alphabetically ascending/descending. <ac:link><ri:page ri:content-title="Sorting users and user groups" /><ac:plain-text-link-body><![CDATA[Learn more about sorting users and groups here >>]]></ac:plain-text-link-body></ac:link></p></div></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><strong>Full Name or Description column</strong></td><td style="margin-left: 30.0px;">This column shows the full name of a user. When creating a new user, you may type the full name or leave it blank (optional). If it is a group, you can add a short group description.</td></tr><tr style="margin-left: 30.0px;"><td style=""><strong>Last Activity Date column</strong></td><td style=""><div class="content-wrapper"><p>This column shows the time and date of the user's last activity on Teamwork Cloud. The time-date format is <strong>DD/MM/YYYY HH:MM</strong>. This data appears only for users and will not be shown when viewing group information. Internal and external users can be sorted by clicking this column name (<ac:image><ri:attachment ri:filename="sort_last_activity.PNG" /></ac:image>). Users will be sorted by the last activity date ascending/descending. However, groups cannot be sorted. <ac:link><ri:page ri:content-title="Sorting users and user groups" /><ac:plain-text-link-body><![CDATA[Learn more about sorting users and groups here >>]]></ac:plain-text-link-body></ac:link></p></div></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><div class="content-wrapper"><p><strong>Content pane</strong></p><p><ac:image><ri:attachment ri:filename="User_status.PNG" /></ac:image></p></div></td><td style="margin-left: 30.0px;"><div class="content-wrapper"><p>Different user colors show the user status in Teamwork Cloud Admin:</p><ul><li>A gr<ac:inline-comment-marker ac:ref="2b8575da-412a-4f9d-905d-87cdef8e9328">ey-</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="2b8575da-412a-4f9d-905d-87cdef8e9328">colored </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="2b8575da-412a-4f9d-905d-87cdef8e9328">user</ac:inline-comment-marker> indicates that the user is disabled and not allowed to log into Teamwork Cloud Admin and Teamwork Cloud in MagicDraw. </li><li>A black-colored user indicates that the user is enabled and they can use their user account (username and password) to log into Teamwork Cloud Admin.</li></ul><p><ac:link><ri:page ri:content-title="Enabling and disabling users" /><ac:plain-text-link-body><![CDATA[Learn more about enabling and disabling users here >>]]></ac:plain-text-link-body></ac:link></p></div></td></tr><tr style="margin-left: 30.0px;"><td style="margin-left: 30.0px;"><div class="content-wrapper"><p><strong>User/User group activity button</strong></p><p><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png"><ri:page ri:content-title="Managing users" /></ri:attachment></ac:image></p></div></td><td style="margin-left: 30.0px;"><div class="content-wrapper"><p>The drop-down menu allows you to edit user information and change user login access (enable or disable).</p></div></td></tr><tr style="margin-left: 30.0px;"><td style=""><div class="content-wrapper"><p><strong>Add button</strong></p><p><ac:image ac:thumbnail="true" ac:width="38"><ri:attachment ri:filename="Action_button.png"><ri:page ri:content-title="Creating users and user groups" /></ri:attachment></ac:image></p></div></td><td style=""><p>The <strong>Add</strong> button opens the <strong>Create User/Group </strong>pane, which allows you to create a new user/group. See <ac:link><ri:page ri:content-title="Managing user groups" /></ac:link> for more information.</p></td></tr></tbody></table><h3 style="color:var(--ds-text,#172b4d);">User group</h3><p><ac:inline-comment-marker ac:ref="999a2f4a-fbd3-4f4b-9852-2dfac7568107">A user group gathers multiple users and</ac:inline-comment-marker> gives the same role assignments to the users in the same group. When you create a user group and assign role assignments (including the scope), you assign them to all of the members in the user group. You can update information and delete a user group. You can also <ac:link><ri:page ri:content-title="Importing users and groups" /><ac:plain-text-link-body><![CDATA[import]]></ac:plain-text-link-body></ac:link> a user group from an LDAP server as an external user group. All members of the user group will be imported to Teamwork Cloud as external users as well. To update the information for an external user group in Teamwork Cloud, you must resynchronize it with that of the LDAP server. </p>
````

<!--NOMAGIC_PAGE id=171180428 space=TWCloud2024xR1 version=3 -->
## PAGE 00263: Using a custom template in a model

- page_id: `171180428`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180428/Using+a+custom+template+in+a+model
- version_number: 3
- version_date: `2025-10-31T09:10:07.224+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents > Document templates > Working with custom document templates
- labels: []

### NORMALIZED CONTENT

The appearance and content of a published model can be customized by applying a custom template. Creating custom templates allows you to define which elements of your model are displayed on the web, and how the data of these elements is represented. If a custom template is created as a separate .mdzip file, you can apply it to multiple models. In order to apply such a template for publishing, you need to use it in the model you intend to publish. This page describes how to accomplish this task.

To use a custom template in a model

1. Do one of the following:
  - From the File menu, select Use Project > Use Local Project .
  - From Options menu, select Project Usages and click the Use Project button.
2. In the open Use Project wizard, select a project to use From file system .
3. Near the Project file box, click [IMAGE alt='' src=''] .
4. In the open dialog, navigate to the directory in which you store your custom template, and select it.
5. Click the Open button.
6. In the Use Project wizard, click the Next button to specify project usage options.
7. In the Accessibility area of the wizard, select the Read-write option.
8. Click the Finish button.

Now that the template is used in your model, you can apply it when publishing the model on the web.Note that you can modify your custom template both before and after using it in a model. If you want to avoid changing the template after using it, skip steps 6 and 7 in the custom template usage procedure described above.

For more information about using projects, see [CONFLUENCE_PAGE title='Using other projects in a project' space='MD2024xR1'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The appearance and content of a published model can be customized by applying a custom template. Creating custom templates allows you to define which elements of your model are displayed on the web, and how the data of these elements is represented. If a custom template is created as a separate .mdzip file, you can apply it to multiple models. In order to apply such a template for publishing, you need to use it in the model you intend to publish. This page describes how to accomplish this task.</p><p><br /></p><p><ac:inline-comment-marker ac:ref="d429e2f7-ecc6-4a01-b047-5c760a72825a">To use a custom template in a model</ac:inline-comment-marker></p><p><br /></p><hr /><ol><li>Do one of the following:<br /><ul><li>From the <strong>File</strong> menu, select <strong>Use Project</strong> &gt; <strong>Use Local Project</strong>.</li><li>From <strong>Options</strong> menu, select <strong>Project Usages</strong> and click the <strong>Use Project</strong> button.</li></ul></li><li>In the open <strong>Use Project</strong> wizard, select a project to use <strong>From file system</strong>.</li><li>Near the <strong>Project file</strong> box, click <span class="confluence-embedded-file-wrapper"> <ac:image><ri:attachment ri:filename="select_project_button.png" /></ac:image> </span>.</li><li><p>In the open dialog, navigate to the directory in which you store your custom template, and select it.</p></li><li>Click the <strong>Open</strong> button.</li><li>In the<strong> Use Project</strong> wizard, click the <strong>Next</strong> button to specify project usage options.</li><li>In the <strong>Accessibility</strong> area of the wizard, select the <strong>Read-write</strong> option.</li><li>Click the <strong>Finish</strong> button.<br /><br /><br /></li></ol><p><span class="confluence-embedded-file-wrapper">Now that the template is used in your model, you can apply it when publishing the model on the web. </span>Note that you can modify your custom template both before and after using it in a model. If you want to avoid changing the template after using it, skip steps 6 and 7 in the custom template usage procedure described above.</p><p><span class="confluence-embedded-file-wrapper">For more information about using projects, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using other projects in a project" /></ac:link>.</span></p>
````

<!--NOMAGIC_PAGE id=171180759 space=TWCloud2024xR1 version=1 -->
## PAGE 00264: Using document information in the page header

- page_id: `171180759`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180759/Using+document+information+in+the+page+header
- version_number: 1
- version_date: `2023-11-13T11:08:52.660+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Sharing and exporting > Customizing PDF/HTML templates
- labels: []

### NORMALIZED CONTENT

By default, the page headers of exported documents are empty. If you want specific information to be displayed in the page header, you need to add it to the *<template_folder>/common/header.html*file.

The page header can also display document information. You should check API for specific pieces of information that are accessible for usage in the page header.

##### Example of adding a document name to the page header

Let’s say you want a document name displayed in the center of the page header with some space around it.

To use a document name in the page header

1. Open the <template_folder>/common/header.html file.
2. Find the header tag.
3. Add <div th:text="${[documentInfo.name](http://documentInfo.name)}"></div> .
4. To make the document name centered, do one of the following:
  - Add an inline style.
  - Change the header class CSS properties in the <template_folder/common/styles.html file.
  - Add a new <style> tag in the *header.html* file and make the same changes you would in any other HTML document. Example of a header tag when using inline styling]]>

After completing the steps above, the exported document will have its name displayed in the page header.

[IMAGE alt='' src='']

###### A sample document with the *Image template* document name displayed in the page header.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>By default, the page headers of exported documents are empty. If you want specific information to be displayed in the page header, you need to add it to the <em>&lt;template_folder&gt;/common/header.html </em>file.</p><p>The page header can also display document information. You should check API for specific pieces of information that are accessible for usage in the page header.</p><h3><br />Example of adding a document name to the page header</h3><p>Let’s say you want a document name displayed in the center of the page header with some space around it.</p><p><br /></p><p>To use a document name in the page header</p><hr /><ol><li>Open the <em>&lt;template_folder&gt;/common/header.html</em> file.</li><li>Find the <em>header</em> tag.</li><li>Add <em>&lt;div th:text=&quot;${<a href="http://documentInfo.name">documentInfo.name</a>}&quot;&gt;&lt;/div&gt;</em>.</li><li>To make the document name centered, do one of the following:<ul><li>Add an inline style.</li><li>Change the <em>header</em> class CSS properties in the <em>&lt;template_folder/common/styles.html</em> file.</li><li><p class="auto-cursor-target">Add a new &lt;style&gt; tag in the <em>header.html</em> file and make the same changes you would in any other HTML document.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="2e9e1a32-c458-448e-86c5-65e27b7e414f"><ac:parameter ac:name="title">Example of a header tag when using inline styling</ac:parameter><ac:plain-text-body><![CDATA[<header class="header">
   <div th:text="${documentInfo.name}" style="text-align: center; padding: 20px;"></div>
</header>]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul></li></ol><p>After completing the steps above, the exported document will have its name displayed in the page header.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="adding_document_info_to_header.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using document information in the page header" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A sample document with the <em>Image template</em> document name displayed in the page header.</h6>
````

<!--NOMAGIC_PAGE id=170491301 space=TWCloud2024xR1 version=4 -->
## PAGE 00265: Using no-installer

- page_id: `170491301`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491301/Using+no-installer
- version_number: 4
- version_date: `2024-12-13T14:35:10.750+01:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation > Web Application Platform Installation on a separate machine
- labels: []

### NORMALIZED CONTENT

**On this page**

42

Here, you can learn how to run Web Application Platform with its service by using the no-installer package.

#### NOTE: Before you start

Before you start

Before starting, you should know the following:

- It is recommended to run Web Application Platform and Teamwork Cloud on different machines.
- Before running Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <install_root>/TeamworkCloud/configuration directory).
- If Web Application Platform runs on a separate machine, it is recommended to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''] on the machine where Teamwork Cloud is running.
- You can run Authentication service or other services in different environments for scalability.

##### Prerequisites

Before running the Web Application Platform with services, you need to:

- Have a working instance of Teamwork Cloud.
- If you intend to use the Cameo Collaborator for Teamwork Cloud service, make sure that [CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024xR1'] or [CONFLUENCE_PAGE title='Installing the FlexNet server' space=''] is installed beforehand.
- [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']Download the *Web_App_Platform_<version number>_<operating_system>_no_install.zip* file .
- If you use Linux, increase the open file limit for the OS or Web Application Platform/Tomcat to a minimum of 20 000 files.

##### Running Web Application Platform with no-install package

To run Web Application Platform by using the no-install package

1. Download and extract the Web_App_Platform_<version number>_<operating system>_no_install.zip file.
2. Open for editing the <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf / webappplatform.properties file, r ead the comments with property descriptions, and specify the following:
  - Web Application Platform properties
  - Authentication server properties
  - Teamwork Cloud server properties
  - FlexNet/DSLS server properties
  - Platform service discovery-related properties
3. Open for editing the <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf/*authserver.properties* file, read the comments with property descriptions, and specify the following:
  - [CONFLUENCE_PAGE title='General parameters' space='']
  - [CONFLUENCE_PAGE title='Keystore parameters' space='']
4. Copy the keystore.p12 file from Teamwork Cloud server ( <install_root>/CATIANoMagicServices/TeamworkCloud/configuration) to Web Application Platform folder <no-install_root>/CATIANoMagicServices/WebAppPlatform/shared/conf .
5. Web Application Platform is released with pre-configured SSL certificates and keystore.Perform this step only if you need to change the default values when the keystore file name, path, or password changes.
  1. Go to the <no-install_root>/ CATIANoMagicServices/WebAppPlatform/conf directory and open the server.xml file.
  2. In the server.xml file, specify the following properties (use the same certificate file that is used in Teamwork Cloud):
    - certificateKeystoreFile="./shared/conf/keystore.p12"
    - certificateKeystorePassword="nomagic"
    - type="RSA" />
6. Install the webapp service and enable it to start automatically. For example: bashDJangotrue

For information on how to start Web Application Platform, refer to [CONFLUENCE_PAGE title='Starting and Stopping Web Application Platform' space=''].To access Web Application Platform, open a web browser and go to *http(s)://<domain_name>:8443/webapp*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d1a86b44-fb6c-431f-920a-54ba4e6ed2a9"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">2</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(62,63,64);">Here, you can learn how to run Web Application Platform with its service by using the no-installer package.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6891d6c1-7949-4085-9077-23a6d46c7782"><ac:parameter ac:name="title">Before you start</ac:parameter><ac:rich-text-body><p>Before starting, you should know the following:</p><ul><li>It is recommended to run Web Application Platform and Teamwork Cloud on different machines.</li><li>Before running Web Application Platform, make sure to note down Zookeeper, Cassandra, Teamwork Cloud, and the license server information (e.g., hostname and port), as well as the KeyStore file location (you can find it in the <em>&lt;install_root&gt;/TeamworkCloud/configuration</em> directory).</li><li>If Web Application Platform runs on a separate machine, it is recommended to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /><ac:plain-text-link-body><![CDATA[stop the WebApp service]]></ac:plain-text-link-body></ac:link> on the machine where Teamwork Cloud is running.</li><li><p>You can run Authentication service or other services in different environments for scalability.</p></li></ul></ac:rich-text-body></ac:structured-macro><h3>Prerequisites</h3><p>Before running the Web Application Platform with services, you need to:</p><ul><li>Have a working instance of Teamwork Cloud.</li><li><span style="color: rgb(62,63,64);">If you intend to use the Cameo Collaborator for Teamwork Cloud service, make sure that <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[DSLS]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Installing the FlexNet server" /><ac:plain-text-link-body><![CDATA[the FlexNet license server]]></ac:plain-text-link-body></ac:link> is installed beforehand.</span></li><li><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /><ac:link-body>Download the <em>Web_App_Platform_&lt;version number&gt;_&lt;operating_system&gt;_no_install.zip</em> file</ac:link-body></ac:link>.</li><li>If you use Linux, increase the open file limit for the OS or Web Application Platform/Tomcat to a minimum of 20 000 files.</li></ul><h3>Running Web Application Platform with no-install package</h3><p>To run Web Application Platform by using the no-install package</p><hr /><ol><li>Download and extract the <em>Web_App_Platform_&lt;version number&gt;_&lt;operating system&gt;_no_install.zip</em> file.</li><li>Open for editing the <em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf</em>/<em>webappplatform.properties </em>file, r<span>ead the comments with property descriptions, and specify the following:</span><ul><li><span style="color: rgb(62,63,64);">Web Application Platform properties</span></li><li><span style="color: rgb(62,63,64);">Authentication server properties</span></li><li><span style="color: rgb(62,63,64);">Teamwork Cloud server properties</span></li><li><span style="color: rgb(62,63,64);">FlexNet/DSLS server properties</span><span style="color: rgb(62,63,64);"><br /></span></li><li><span style="color: rgb(62,63,64);">Platform service discovery-related properties</span></li></ul></li><li>Open for editing the <em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf/<em style="text-align: left;">authserver.properties</em></em> file, read the comments with property descriptions, and specify the following:<ul><li><ac:link><ri:page ri:content-title="General parameters" /><ac:plain-text-link-body><![CDATA[General properties]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Keystore parameters" /><ac:plain-text-link-body><![CDATA[Keystore properties]]></ac:plain-text-link-body></ac:link></li></ul></li><li>Copy the<em> keystore.p12</em> file from Teamwork Cloud server <em>(</em><em>&lt;install_root&gt;/CATIANoMagicServices/TeamworkCloud/configuration)</em> to Web Application Platform folder<em>&lt;no-install_root&gt;/CATIANoMagicServices/WebAppPlatform/shared/conf</em>.<br /><br /></li><li><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="81641b2d-5f1e-4c2f-b8d2-7a994b38f2c6"><ac:rich-text-body><span style="color: rgb(23,43,77);">Web Application Platform is released with pre-configured SSL certificates and keystore.<br /></span>Perform this step only if you need to change the default values when the keystore file name, path, or password changes.</ac:rich-text-body></ac:structured-macro><br style="text-align: left;" /><ol><li>Go to the <em>&lt;no-install_root&gt;/</em><em>CATIANoMagicServices/WebAppPlatform/conf</em> directory and open the <em>server.xml</em> file.</li><li>In the <em>server.xml</em> file, specify the following properties (use the same certificate file that is used in Teamwork Cloud):<ul><li>certificateKeystoreFile=&quot;./shared/conf/keystore.p12&quot;</li><li>certificateKeystorePassword=&quot;nomagic&quot;</li><li><span style="color: rgb(23,43,77);">type=&quot;RSA&quot; /&gt;</span></li></ul></li></ol></li><li><span style="color: rgb(23,43,77);">Install the webapp service and enable it to start automatically. For example:<br /></span><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d3e494af-1e30-4710-b7d1-70280a13f5af"><ac:parameter ac:name="language">bash</ac:parameter><ac:parameter ac:name="theme">DJango</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[service.sh install
systemctl enable webapp
systemctl start webapp]]></ac:plain-text-body></ac:structured-macro><span style="color: rgb(23,43,77);"> </span></li></ol><p><span style="color: rgb(62,63,64);">For information on how to start Web Application Platform, refer to <ac:link><ri:page ri:content-title="Starting and Stopping Web Application Platform" /></ac:link>. </span>To access Web Application Platform, open a web browser and go to <em>http(s)://&lt;domain_name&gt;:8443/webapp</em>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491541 space=TWCloud2024xR1 version=1 -->
## PAGE 00266: Using the app bar

- page_id: `170491541`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491541/Using+the+app+bar
- version_number: 1
- version_date: `2024-01-29T10:10:30.889+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

The app bar allows you to navigate the Teamwork Cloud Admin functionality easily. The app bar is located on the upper right of the web app portal. You can perform the following actions from the app bar:

| App bar icon | Icon description |
| --- | --- |
| Search bar | You can use this search box to find a username by typing a keyword. Teamwork Cloud Admin will run the search and find matching usernames. |
|  | Click and select an application to open it (, , , , etc.). |
|  | Click and select Sign out to sign out of the current user account. |
|  | Click and select one of the following:Help - to open the web app documentationAbout - to view the web app information, such as the version number and copyright information. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The app bar allows you to navigate the Teamwork Cloud Admin functionality easily. The app bar is located on the <span style="color: rgb(33,33,33);">upper right</span> of the web app portal. You can perform the following actions from the app bar:</p><table><colgroup><col /><col /></colgroup><tbody><tr><th><span>App bar icon</span></th><th>Icon description</th></tr><tr><td colspan="1"><div class="content-wrapper"><strong>Search bar</strong></div></td><td colspan="1">You can use this search box to find a username by typing a keyword. Teamwork Cloud Admin will run the search and find matching usernames.</td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="plugins.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using the app bar" /></ri:attachment></ac:image></p></div></td><td>Click and select an application to open it (<ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Resources application" /><ac:plain-text-link-body><![CDATA[Resources]]></ac:plain-text-link-body></ac:link>, <ac:inline-comment-marker ac:ref="db8628e8-893c-4388-a2a5-4de93572f9d9"><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Users application" /><ac:plain-text-link-body><![CDATA[Users]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker>, <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Roles application" /><ac:plain-text-link-body><![CDATA[Roles]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Settings application" /><ac:plain-text-link-body><![CDATA[Settings]]></ac:plain-text-link-body></ac:link>, etc.).</td></tr><tr><td><div class="content-wrapper"><p><ac:image ac:align="center"><ri:attachment ri:filename="sign_out.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using the app bar" /></ri:attachment></ac:image></p></div></td><td><p>Click and select <strong>Sign out</strong> to sign out of the current user account.</p></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper image-center-wrapper"><ac:image ac:align="center"><ri:attachment ri:filename="menu.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using the app bar" /></ri:attachment></ac:image></span></p></div></td><td colspan="1"><p>Click and select one of the following:</p><ul><li><strong>Help</strong> - to open the web app documentation</li><li><strong>About</strong> - to view the web app information, such as the version number and copyright information.</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180277 space=TWCloud2024xR1 version=4 -->
## PAGE 00267: Viewing and editing resource details

- page_id: `171180277`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180277/Viewing+and+editing+resource+details
- version_number: 4
- version_date: `2024-10-29T14:19:55.030+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application > Working with resources
- labels: []

### NORMALIZED CONTENT

**On this page**

4

##### Viewing resource details

In the Resources app you can view the following resource information:

- Resource details, including the resource name, creation and last modification dates, and the user who created or modified the resource.
- Resource history information, including the user who created each version of the resource, the version creation date, and the type of changes that were made.
- The roles assigned to the resource.
- Resource branches.

To view resource details

1. In the Resources application, click the category where the relevant resource is located .
2. Click [ATTACHMENT filename='menu.png'] next to the resource and select Resource details .

Resource details, such as category, creation date, and last modification date, are shown on the **Resource** pane on the right side of the screen.

[IMAGE alt='' src='']

###### Viewing resource details, history, and other information.

##### Editing resource details

You can edit a resource name and description or move the resource to another category, as described below.

To edit resource details

1. Open the Resources application and go to the category where the relevant resource is located.
2. Click [ATTACHMENT filename='menu.png'] next to the resource with the details you want to edit and select Resource details.
3. To edit resource details,, click Edit on the bottom of the Resource details pane.
4. You can:
  - Change the resource name in the Resource name field.
  - Change or add a resource description in the Description field.
5. Click [ATTACHMENT filename='save_button.jpg'] on the top right corner of the Edit resource details pane to save resource details.

When you get a confirmation message, it means the resource details are successfully updated.

##### Setting resource classification

Resource classification that you set through data markings allows you to control access to that resource. To set resource classification, [CONFLUENCE_PAGE title='Managing data markings in Teamwork Cloud Admin' space=''] in the Settings app and ensure you have [CONFLUENCE_PAGE title='Permissions' space=''].

To set resource classification

1. Open the Resources application and go to the category where the relevant resource is located.
2. Click [ATTACHMENT filename='menu.png'] next to the resource and select Set data markings.
3. In the window that opens, select the desired data marking.
4. Click Set to set the selected data marking.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="95494d25-387b-49ae-9907-5003c18f9ab9"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Viewing resource details</h3><p>In the Resources app you can view the following resource information:</p><ul><li>Resource details, including the resource name, creation and last modification dates, and the user who created or modified the resource.</li><li>Resource history information, including the user who created each version of the resource, the version creation date, and the type of changes that were made.</li><li>The roles assigned to the resource.</li><li>Resource branches.</li></ul><p><br /></p><p>To view resource details</p><hr /><ol><li>In the Resources application, <span style="color: rgb(23,43,77);">click the category where the relevant resource is located</span>.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource and select <strong>Resource details</strong>.</li></ol><p><br />Resource details, such as category, creation date, and last modification date, are shown on the <strong>Resource</strong> pane on the right side of the screen.</p><p style="text-align: center;"><br /><ac:image ac:width="950"><ri:attachment ri:filename="resource_details_pane.png" /></ac:image></p><h6 style="text-align: center;">Viewing resource details, history, and other information.</h6><h3>Editing resource details</h3><p>You can edit a resource name and description or move the resource to another category, as described below.</p><p><br /></p><p>To edit resource details</p><hr /><ol><li>Open the Resources application and go to the category where the relevant resource is located.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource with the details you want to edit and select <strong>Resource details.</strong></li><li>To edit resource details,, click <strong>Edit</strong> on the bottom of the <strong>Resource details</strong> pane.</li><li>You can:<ul><li>Change the resource name in the <strong>Resource name</strong><span> field.</span></li><li>Change or add a resource description in the <strong>Description</strong> field.</li></ul></li><li>Click <ac:image ac:thumbnail="true" ac:width="32"><ri:attachment ri:filename="save_button.jpg" /></ac:image> on the top right corner of the <strong>Edit resource details</strong> pane to save resource details.</li></ol><p><br />When you get a confirmation message, it means the resource details are successfully updated.</p><h3>Setting resource classification</h3><p>Resource classification that you set through data markings allows you to control access to that resource. To set resource classification, <ac:link><ri:page ri:content-title="Managing data markings in Teamwork Cloud Admin" /><ac:plain-text-link-body><![CDATA[enable data markings]]></ac:plain-text-link-body></ac:link> in the Settings app and ensure you have <ac:link><ri:page ri:content-title="Permissions" /><ac:plain-text-link-body><![CDATA[sufficient permissions]]></ac:plain-text-link-body></ac:link>.</p><p>To set resource classification</p><hr /><ol><li>Open the Resources application and go to the category where the relevant resource is located.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the resource and select <strong>Set data markings.</strong></li><li>In the window that opens, select the desired data marking.</li><li>Click <strong>Set</strong> to set the selected data marking. </li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180319 space=TWCloud2024xR1 version=3 -->
## PAGE 00268: Viewing history

- page_id: `171180319`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180319/Viewing+history
- version_number: 3
- version_date: `2024-05-17T16:24:05.689+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application
- labels: []

### NORMALIZED CONTENT

**On this page**

**4**

INLINE

**History**allows you to track changes made to the project. The History card displays basic information, such as versions, contributors, and branches of each modification, while the visual representation of history provides a full-screen comprehensive viewof the project's evolution over time.

##### Viewing resource history

To view resource history

1. Navigate to the Resources application.
2. Then do one of the following:
  1. Click a resource name to open the Resource pane and find the History card: [ATTACHMENT filename='history.png'] Click View All at the bottom of the History card to view a . 
 
OR
  2. Select [ATTACHMENT filename='actions.png'] next to a resource and click Resource history to open the full-screen history view: [ATTACHMENT filename='history_option.png']

##### Navigating full-screen history view

[IMAGE alt='' src='']

###### Viewing full-screen visual history representation.

In the full-screen history view, you can:

- **View**branch structure, merge and commit information, as well as archived branches that are greyed-out;
- Search for a specific commit, message, or version using the search field at the top.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="aef5ffe1-8d94-4784-b77c-e9af34de25af"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="d97f9a9e-5d17-4b79-afe9-a2dc57277a4b"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>History </strong>allows you to track changes made to the project. The History card displays basic information, such as versions, contributors, and branches of each modification, while the visual representation of history provides a full-screen <span style="color: rgb(23,43,77);">comprehensive view </span>of the project's evolution over time.</p><h3>Viewing resource history</h3><p>To view resource history</p><hr /><ol><li>Navigate to the <strong>Resources</strong> application.</li><li>Then do one of the following:<ol><li>Click a resource name to open the <strong>Resource</strong> pane and find the <strong>History </strong>card:<br /><br /><ac:image><ri:attachment ri:filename="history.png" /></ac:image><br /><br />Click<strong> View All </strong><span>at the bottom of the History card to view a <ac:link ac:anchor="Navigating full-screen history view"><ac:plain-text-link-body><![CDATA[full-screen representation of resource history]]></ac:plain-text-link-body></ac:link>.<br /><br />OR<br /></span></li><li>Select <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="actions.png" /></ac:image> next to a resource and click <strong>Resource history </strong>to open the full-screen history view:<br /><br /><ac:image><ri:attachment ri:filename="history_option.png" /></ac:image></li></ol></li></ol><h3>Navigating full-screen history view</h3><p><ac:image><ri:attachment ri:filename="branch_visualization.png" /></ac:image></p><h6 style="text-align: center;">Viewing full-screen visual history representation.</h6><p>In the full-screen history view, you can:</p><ul><li><span style="color: rgb(23,43,77);"><strong>View </strong>branch structure, merge and commit information, as well as archived branches that are greyed-out;</span></li><li><strong>Search </strong>for a specific commit, message, or version using the search field at the top.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180354 space=TWCloud2024xR1 version=1 -->
## PAGE 00269: Viewing resource information

- page_id: `171180354`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180354/Viewing+resource+information
- version_number: 1
- version_date: `2023-07-07T08:51:08.576+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resource Usage Map
- labels: []

### NORMALIZED CONTENT

If you want to view the information of a particular resource in a resource usage map, simply select it to the Resource pane on the right side of the application portal. This pane displays details and usages of the selected resource. Here, you can also find all the resources that use the selected resource in the their latest versions.

The Resource pane has three cards displaying different types of resource information highlighted in the figure below.

[IMAGE alt='' src='']

| Resource details card | The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource. |
| --- | --- |
|  | Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource. |
| Used resources card | After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects. |
| Used by resources card | In the Used by resources card, click the Find all usages button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">If you want to view the information of a particular resource in a resource usage map, simply select it to the Resource pane on the right side of the application portal. This pane displays details and usages of the selected resource. Here, you can also find all the resources that use the selected resource in the their latest versions.</p><p>The Resource pane has three cards displaying different types of resource information highlighted in the figure below.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="resource_pane.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Viewing resource information" /></ri:attachment></ac:image></p><p><br /></p><table class="relative-table" style="width: 1118.0px;"><colgroup><col /><col /></colgroup><tbody><tr><td style="text-align: left;" colspan="1"><strong>Resource details card</strong></td><td colspan="1">The Resource details card displays the information of the resource selected in a resource usage map. The information includes resource name, creator, version, creation and modification time. You can also use this card to change the version of the selected resource.</td></tr><tr><td style="text-align: left;" colspan="1"><div class="content-wrapper"><p><strong><span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="switch_resource_version.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Viewing resource information" /></ri:attachment></ac:image></span></strong></p></div></td><td colspan="1">Click this icon to change the version of the resource selected in a resource usage map. Once you select a different resource version from the given list, a new resource usage map is created for that version of the resource.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used resources card</strong></td><td colspan="1">After selecting a resource in a resource usage map, the Used resources card displays the list of all Teamwork Cloud projects that the selected resource uses. Used projects are divided into two groups: direct usages - the projects that are directly used by the resource, and indirect usages - the projects that are used by the resource through other used projects.</td></tr><tr><td style="text-align: left;" colspan="1"><strong>Used by resources card</strong></td><td colspan="1">In the Used by resources card, click the <strong>Find all usages</strong> button to see the list of all Teamwork Cloud projects that use the resource selected in a resource usage map. The usages are divided into two groups: direct usages - the projects that use the resource directly, and indirect usages - the projects that use the resource through other used projects.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=171180102 space=TWCloud2024xR1 version=2 -->
## PAGE 00270: Viewing server license information

- page_id: `171180102`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180102/Viewing+server+license+information
- version_number: 2
- version_date: `2024-10-15T13:06:50.656+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

To set and view the server license, select**Server license**in the left-side menu of the Settings application. In the **Server license**page you can:

- [CONFLUENCE_PAGE title='License management' space='']
- 

[IMAGE alt='' src='']

##### Recently active users

The **Recently active users** section shows users who have recently logged in to Teamwork Cloud services, such as Teamwork Cloud Admin or Teamwork Cloud through a modeling tool. These users are either currently logged in or have logged out within the last 20 minutes (approximately).

The **Last activity date**column displays the last time the user performed any action in Teamwork Cloud or Teamwork Cloud Admin.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To set and view the server license, select<span> </span><strong>Server license</strong><span> </span>in the left-side menu of the Settings application. In the <strong>Server license </strong>page you can:</p><ul><li><ac:link><ri:page ri:content-title="License management" /><ac:plain-text-link-body><![CDATA[Manage server licenses]]></ac:plain-text-link-body></ac:link></li><li><ac:link ac:anchor="Recently active users"><ac:plain-text-link-body><![CDATA[View recently active users]]></ac:plain-text-link-body></ac:link></li></ul><p><ac:image ac:width="900"><ri:attachment ri:filename="server_license_page.jpg" /></ac:image></p><h3>Recently active users</h3><p>The <strong>Recently active users</strong> section shows users who have recently logged in to Teamwork Cloud services, such as Teamwork Cloud Admin or Teamwork Cloud through a modeling tool. These users <span style="color: rgb(31,31,31);">are either currently logged in or have logged out within the last 20 minutes (approximately).</span></p><p>The <strong>Last activity date </strong>column displays the last time the user performed any action in Teamwork Cloud or Teamwork Cloud Admin.</p>
````

<!--NOMAGIC_PAGE id=171180090 space=TWCloud2024xR1 version=2 -->
## PAGE 00271: Viewing server status

- page_id: `171180090`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180090/Viewing+server+status
- version_number: 2
- version_date: `2025-07-17T15:43:39.483+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application > Managing server settings
- labels: []

### NORMALIZED CONTENT

**On this page**

5

##### Viewing server status

The **Server status** table in the Teamwork Cloud Admin **Server settings**section****lists all connected Teamwork Cloud nodes in a cluster. Each server node in the cluster provides the IP address or domain name with port, RAM usage, CPU usage and operating system information. The server nodes are arranged in an ascending numerical order by default. In Linux, the RAM Usage includes RAM allocated to buffers and disk cache, so it is not indicative of the available RAM. For actual available RAM, you can use the monitoring stack, which will provide insight into OS, Cassandra, and Teamwork Cloud metrics.

The **Server Status** table will be automatically updated every 30 seconds. The last update time of the table is shown at the bottom of the table.

###### [IMAGE alt='' src=''] 
The server status and the log files on the Server Settings page.

##### Downloading log files

You can download log files that record all user activities in Teamwork Cloud and Web Application Platform.

To download a log file

1. Go to the Settings application.
2. Select Server Status from the left side menu.
3. Click [ATTACHMENT filename='Download icon.png'] next to Teamwork Cloud or WebApp to download a log file from a specific server node. The file will be downloaded and saved on your computer.

false

A log file downloaded from [IMAGE alt='' src=''] contains recent content with a capacity of 20,000 lines (the maximum size).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="68934416-bd23-40ce-87b8-4433712c4c5e"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3 style="text-align: left;">Viewing server status</h3><p style="text-align: left;">The <strong>Server status</strong> table in the Teamwork Cloud Admin <strong>Server settings </strong>section<strong> </strong>lists all connected Teamwork Cloud nodes in a cluster. Each server node in the cluster provides the IP address or domain name with port, RAM usage, CPU usage and operating system information. The server nodes are arranged in an ascending numerical order by default. In Linux, the RAM Usage includes RAM allocated to buffers and disk cache, so it is not indicative of the available RAM. For actual available RAM, you can use the monitoring stack, which will provide insight into OS, Cassandra, and Teamwork Cloud metrics.</p><p style="text-align: left;">The <strong>Server Status</strong> table will be automatically updated every 30 seconds. The last update time of the table is shown at the bottom of the table.</p><p style="text-align: left;"><br /></p><h6 style="text-align: center;"><ac:image ac:width="900"><ri:attachment ri:filename="server_status_table.jpg" /></ac:image><br /><span style="color:var(--ds-text,#707070);">The server status and the log files on the Server Settings page.<br /><br /></span></h6><h3><span>Downloading log files</span></h3><p>You can download log files that record all user activities in Teamwork Cloud and Web Application Platform.</p><p>To download a log file</p><hr /><ol><li data-uuid="f34408c1-e605-49e8-9801-43725011dd25">Go to the <strong>Settings</strong> application.</li><li data-uuid="616fc7f8-65bd-45ff-84a8-d2dee1fc6ef6">Select <strong>Server Status</strong> from the left side menu.</li><li data-uuid="fc12c5c9-faf7-4a71-ba53-2319291dfc07">Click <ac:image ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="Download icon.png" /></ac:image> next to Teamwork Cloud or WebApp to download a log file from a specific server node. The file will be downloaded and saved on your computer. <br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="461de44b-2f2b-453e-8e35-00f99f99d18b"><ac:parameter ac:name="icon">false</ac:parameter><ac:rich-text-body><p><span>A log file downloaded from <ac:image ac:thumbnail="true" ac:width="30"><ri:attachment ri:filename="Download icon.png" /></ac:image> contains recent content with a capacity of 20,000 lines (the maximum size).</span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491485 space=TWCloud2024xR1 version=1 -->
## PAGE 00272: Web Application Platform Administration

- page_id: `170491485`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491485/Web+Application+Platform+Administration
- version_number: 1
- version_date: `2024-01-29T09:33:57.247+01:00`
- ancestors: Teamwork Cloud and Services > Administration Guide
- labels: []

### NORMALIZED CONTENT

Web Application Platform is the platform for developing and running web applications. It is also the base for Cameo Collaborator for Teamwork Cloud, Resources, and TWCloud Admin apps.

To learn how to install and use Web Application platform, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Web Application Platform is the platform for developing and running web applications. It is also the base for Cameo Collaborator for Teamwork Cloud, Resources, and TWCloud Admin apps.</p><p>To learn how to install and use Web Application platform, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````

<!--NOMAGIC_PAGE id=170491275 space=TWCloud2024xR1 version=2 -->
## PAGE 00273: Web Application Platform Installation on a separate machine

- page_id: `170491275`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491275/Web+Application+Platform+Installation+on+a+separate+machine
- version_number: 2
- version_date: `2025-06-26T13:36:18.392+02:00`
- ancestors: Teamwork Cloud and Services > Deployment Guide > Teamwork Cloud and Services Installation > Advanced Teamwork Cloud and services installation
- labels: []

### NORMALIZED CONTENT

The following chapters will give you step by step instructions on how to install and upgrade Web Application Platform and its services:

[IMAGE alt='' src='']

###### The conceptual schema of the standard Web Application Platform deployment.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following chapters will give you step by step instructions on how to install and upgrade Web Application Platform and its services:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><p><br /></p><p style="text-align: center;"><ac:image ac:width="1000"><ri:attachment ri:filename="WAP standard deployment.jpg" /></ac:image></p><h6 style="text-align: center;">The conceptual schema of the standard Web Application Platform deployment.</h6>
````

<!--NOMAGIC_PAGE id=171180255 space=TWCloud2024xR1 version=3 -->
## PAGE 00274: Working with categories

- page_id: `171180255`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180255/Working+with+categories
- version_number: 3
- version_date: `2025-10-30T14:47:40.888+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application
- labels: []

### NORMALIZED CONTENT

**On this page**

All Teamwork Cloud and Cameo Collaborator for Teamwork Cloud resources are sorted by categories. The sections below explain how to create new categories and manage existing ones.

After creating/editing/removing a category, that category in other applications will not be updated immediately.

##### Creating categories

You can either create a category when publishing a model from a modeling tool or create it directly in the Resources app. Follow the steps below to create a category in the Resources app.

To create a category

1. Open the Resources application.
2. Click [IMAGE alt='' src=''] on the bottom right corner of the screen. The **Create category** dialog opens. Creating a nested categoryTo create a category nested in another category, navigate to the intended parent category before completing step 2.
3. Enter the new category name in the Category name field.
4. Click the Create button. [ATTACHMENT filename='creating_categories.png']

The category is created and shown in the repository together with other categories.

##### Renaming categories

If necessary, rename existing categories as described below.

To rename a category

1. Open the Resources application and navigate to the category you want to rename.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Rename category . The Rename category dialog opens.
3. Enter a new category name in the Category name field.
4. Click the Rename button. [ATTACHMENT filename='renaming_categories.png']

After completing the above steps, you can see the category with a new name in the repository.

##### Removing categories

You can remove categories without deleting the resources they contain.

To remove a category

1. Open the Resources application and navigate to the category you want to remove.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Remove category .
3. When you get the message asking if you want to remove the category, click Remove .

The category is removed and all the resources it contained are moved to the **Uncategorized**category.

##### Navigating in categories

Teamwork Cloud supports nested categories so you can organize your resources in a folder-like manner. To see the contents of a specific category, click it as displayed below. The full path to an open category is displayed just below the app bar.

[IMAGE alt='' src='']

##### Setting category classifications

Category classifications that you set through data markings allows you to control access to that category. To set a category classification, [CONFLUENCE_PAGE title='Managing data markings in TWCloud Admin' space='TWC2024xR1'] in the Settings menu and ensure you have [sufficient permissions](https://docs.nomagic.com/display/TWCloud2024xR1/Permissions).

To set a category classification

1. Go to the Resources application and locate the category to set its classification.
2. Click [ATTACHMENT filename='menu.png'] next to the category and select Edit category details .
3. In the Classification drop-down select the desired data marking.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="34181f02-c168-4184-8a3b-4b4afb4af04f" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>All Teamwork Cloud and Cameo Collaborator for Teamwork Cloud resources are sorted by categories. The sections below explain how to create new categories and manage existing ones.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f0191de0-02db-486a-8fe2-545299f52559"><ac:rich-text-body><p>After creating/editing/removing a category, that category in other applications will not be updated immediately.</p></ac:rich-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);"><br />Creating categories</h3><p>You can either create a category when publishing a model from a modeling tool or create it directly in the Resources app. Follow the steps below to create a category in the Resources app.</p><p><br /></p><p>To create a category</p><hr style="" /><ol><li><p class="auto-cursor-target">Open the Resources application.</p></li><li><p class="auto-cursor-target">Click <ac:image ac:thumbnail="true" ac:width="25"><ri:attachment ri:filename="create_category.png" /></ac:image> on the bottom right corner of the screen. The <strong>Create category</strong> dialog opens.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="943bf20d-586f-4e88-87a9-37dc4245166b"><ac:parameter ac:name="title">Creating a nested category</ac:parameter><ac:rich-text-body><p>To create a category nested in another category, navigate to the intended parent category before completing step 2.</p></ac:rich-text-body></ac:structured-macro></li><li>Enter the new category name in the <strong>Category name</strong> field.</li><li>Click the <strong>Create</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="creating_categories.png" /></ac:image></li></ol><p><br />The category is created and shown in the repository together with other categories.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Renaming categories</h3><p>If necessary, rename existing categories as described below.</p><p><br /></p><p>To rename a category</p><hr style="" /><ol><li>Open the Resources application and navigate to the category you want to rename.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Rename category</strong>. The <strong>Rename category</strong> dialog opens.</li><li>Enter a new category name in the <strong>Category name</strong> field.</li><li>Click the <strong>Rename</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="renaming_categories.png" /></ac:image></li></ol><p><br />After completing the above steps, you can see the category with a new name in the repository.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Removing categories</h3><p>You can remove categories without deleting the resources they contain.</p><p><br /></p><p>To remove a category</p><hr style="" /><ol><li>Open the Resources application and navigate to the category you want to remove.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Remove category</strong>.</li><li>When you get the message asking if you want to remove the category, click <strong>Remove</strong>.</li></ol><p><br />The category is removed and all the resources it contained are moved to the <strong>Uncategorized </strong>category.</p><h3 style="color:var(--ds-text,#172b4d);"><br />Navigating in categories</h3><p>Teamwork Cloud supports nested categories so you can organize your resources in a folder-like manner. To see the contents of a specific category, click it as displayed below. The full path to an open category is displayed just below the app bar.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="navigating_in_categories.png" /></ac:image></p><h3 style="color:var(--ds-text,#172b4d);">Setting category classifications</h3><p>Category classifications that you set through data markings allows you to control access to that category. To set a category classification, <ac:link><ri:page ri:space-key="TWC2024xR1" ri:content-title="Managing data markings in TWCloud Admin" /><ac:plain-text-link-body><![CDATA[enable data markings]]></ac:plain-text-link-body></ac:link> in the Settings menu and ensure you have <a href="https://docs.nomagic.com/display/TWCloud2024xR1/Permissions" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">sufficient permissions</a>.</p><p>To set a category classification</p><hr style="" /><ol><li>Go to the Resources application and locate the category to set its classification.</li><li>Click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="menu.png" /></ac:image> next to the category and select <strong>Edit category details</strong>.</li><li>In the <strong>Classification </strong>drop-down select the desired data marking.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180517 space=TWCloud2024xR1 version=2 -->
## PAGE 00275: Working with comments

- page_id: `171180517`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180517/Working+with+comments
- version_number: 2
- version_date: `2025-10-31T12:29:27.351+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud
- labels: []

### NORMALIZED CONTENT

**In this section**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>In this section</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4e0a7d28-f72e-4a39-b34e-998819c9d8a7" /></p>
````

<!--NOMAGIC_PAGE id=171180555 space=TWCloud2024xR1 version=2 -->
## PAGE 00276: Working with comments as model elements

- page_id: `171180555`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180555/Working+with+comments+as+model+elements
- version_number: 2
- version_date: `2024-10-21T06:53:03.293+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: []

### NORMALIZED CONTENT

**On this page**

4

By default, comments are stored in Cameo Collaborator documents. However, it is possible to store Cameo Collaborator comments as model elements inside a project. This allows you to work with them as any other UML elements and use the benefits of the modeling tool functionalities, such as calculating metrics, validating comments, and creating comment reports.

#### NOTE: Working with synchronized projects

Working with synchronized projects

Synchronized projects on the target Teamwork Cloud server are read-only. This means you cannot store Cameo Collaborator comments in such projects because they cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space=''].

##### Storing Cameo Collaborator Comments in a project

If you want to store Cameo Collaborator comments in a project rather than in a document, you have to choose the **Comments in project** check box when publishing the document, as shown below. For information on how to publish documents, refer to [CONFLUENCE_PAGE title='Publishing documents' space=''].

[IMAGE alt='' src='']

###### The **Cameo Collaborator Publisher** dialog with the highlighted option, which allows storing comments inside a project.

When Cameo Collaborator comments are saved in a project, they are automatically synchronized between the project and the document every time you commit changes to the server or update the project. This means you can work with comments both in a modeling tool and Cameo Collaborator without compromising consistency.

#### NOTE: Importing comments

Importing comments

If you select the **Comments in project** check box when updating an existing document with comments, a dialog will pop up, allowing you to import these comments from the document to the project (see the figure below). However, keep in mind that you will not be able to migrate the comments from the project back to the document, so be careful not to clear the**Comments in project**check box when updating the document at a later time.

[IMAGE alt='' src='']

###### A popup dialog allowing you to import Cameo Collaborator comments to a project automatically.

##### Importing Cameo Collaborator comments to a project manually

If you did not import Cameo Collaborator comments to a project when publishing a document with the **Comments in project** option enabled (as described in the above section), you can import them manually later.

To import Cameo Collaborator comments to a project

1. In the main menu of a modeling tool, select Tools > Cameo Collaborator > Import Comments .
2. When you get a notification that comments are being imported, wait until the import is complete and update the project.

You can find the imported comments in the containment tree of a modeling tool under the Package with the same name as the published document.

[IMAGE alt='' src='']

###### Imported Cameo Collaborator comments in the containment tree of a modeling tool.

##### Creating Cameo Collaborator comments and replies

You can create textual Cameo Collaborator comments and replies either directly in the diagram where the commented element is displayed or in the Containment tree.

To create a Cameo Collaborator comment in a diagram

1. Open the diagram where the element that you want to create a comment for is displayed.
2. In the diagram palette, click Collaborator Comment and click anywhere on the diagram pane to create a comment.
3. Enter comment text on the shape of the comment and click anywhere on the diagram pane to save it.
4. Create an Anchor from the comment to the commented element.
5. Find the new comment in the Containment tree of your project and move it to the Package with the «CollaboratorComments» stereotype. This Package name is typically the same as the project. Collaborator Comments PackageIf this is the first Cameo Collaborator comment created in the project and the Package with the «CollaboratorComments» stereotype does not exist, create a Package dedicated to comments and apply the «CollaboratorComments» stereotype to it. Then place the newly created comment in this Package. All Cameo Collaborator comments must be stored in that Package to be valid and visible in a published document.

The Cameo Collaborator Comment will be visible in a published document once you commit changes to the server and refresh the document. If you want to create comments in the Containment tree of your model, you can do it as described below.

To create a Cameo Collaborator comment in the Containment tree

1. In the Containment tree of your model, right-click the Package with the «CollaboratorComments» stereotype and select **Create Element** > **Comment**. Collaborator Comments PackageIf this is the first Cameo Collaborator comment created in the project and the Package with the «CollaboratorComments» stereotype does not exist, create a Package dedicated to comments and apply the «CollaboratorComments» stereotype to it. All Cameo Collaborator comments must be stored in such a Package to be valid and visible in a published document.
2. Type the text of the comment and press Enter.
3. Right-click the created comment and select Refactor > Convert To > More Elements > Collaborator Comment .
4. Open the Specification window of the new Cameo Collaborator comment, select the specification cell of the Annotated Element property, and click [ATTACHMENT filename='edit.png'] .
5. On the left side of the Select Elements dialog, select the element the comment is created for and click [ATTACHMENT filename='add.png'] to add it to the selected elements area.
6. Click OK and close the Specification window.

[IMAGE alt='' src='']

###### This figure shows Cameo Collaborator comments in a diagram and the Containment tree.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d2e18a37-d7ec-4f96-a809-4dfa1c7ea7ff"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>By default, comments are stored in Cameo Collaborator documents. However, it is possible to store Cameo Collaborator comments as model elements inside a project. This allows you to work with them as any other UML elements and use the benefits of the modeling tool functionalities, such as calculating metrics, validating comments, and creating comment reports.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b185f57-c071-4566-91dc-915a337dd531"><ac:parameter ac:name="title">Working with synchronized projects</ac:parameter><ac:rich-text-body><p>Synchronized projects on the target Teamwork Cloud server are read-only. This means you cannot store Cameo Collaborator comments in such projects because they cannot be modified. <ac:link><ri:page ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3><br />Storing Cameo Collaborator Comments in a project</h3><p>If you want to store Cameo Collaborator comments in a project rather than in a document, you have to choose the <strong>Comments in project</strong> check box when publishing the document, as shown below. For information on how to publish documents, refer to <ac:link><ri:page ri:content-title="Publishing documents" /></ac:link>.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="commnets_in_project_check_box.png" /></ac:image></p><h6 style="text-align: center;">The <strong>Cameo Collaborator Publisher</strong> dialog with the highlighted option, which allows storing comments inside a project.</h6><p><br />When Cameo Collaborator comments are saved in a project, they are automatically synchronized between the project and the document every time you commit changes to the server or update the project. This means you can work with comments both in a modeling tool and Cameo Collaborator without compromising consistency.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="240dd451-66e3-4ffc-81db-ae12bc2dbef1"><ac:parameter ac:name="title">Importing comments</ac:parameter><ac:rich-text-body><p>If you select the <strong>Comments in project</strong> check box when updating an existing document with comments, a dialog will pop up, allowing you to import these comments from the document to the project (see the figure below). <span style="color: rgb(55,65,81);"><span> </span>However, keep in mind that you will not be able to migrate the comments from the project back to the document, so be careful not to clear the </span><strong style="text-align: left;">Comments in project</strong><span style="color: rgb(55,65,81);"><span> </span>check box when updating the document at a later time.</span></p><p style="text-align: center;"><span style="color: rgb(55,65,81);"><ac:image ac:height="171"><ri:attachment ri:filename="importing_comments_automatically.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(55,65,81);">A popup dialog allowing you to import Cameo Collaborator comments to a project automatically.</span></h6></ac:rich-text-body></ac:structured-macro><h3><br />Importing Cameo Collaborator comments to a project manually</h3><p>If you did not import Cameo Collaborator comments to a project when publishing a document with the <strong>Comments in project</strong> option enabled (as described in the above section), you can import them manually later.</p><p><br /></p><p>To import Cameo Collaborator comments to a project</p><hr /><ol><li>In the main menu of a modeling tool, select <strong>Tools</strong> &gt; <strong>Cameo Collaborator</strong> &gt; <strong>Import Comments</strong>.</li><li>When you get a notification that comments are being imported, wait until the import is complete and update the project.</li></ol><p><br /></p><p>You can find the imported comments in the containment tree of a modeling tool under the Package with the same name as the published document.</p><p><br /></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="comments_in_project.png" /></ac:image></span></p><h6 style="text-align: center;">Imported Cameo Collaborator comments in the containment tree of a modeling tool.</h6><h3><br />Creating Cameo Collaborator comments and replies</h3><p>You can create textual Cameo Collaborator comments and replies either directly in the diagram where the commented element is displayed or in the Containment tree.</p><p><br /></p><p>To create a Cameo Collaborator comment in a diagram</p><hr /><ol><li>Open the diagram where the element that you want to create a comment for is displayed.</li><li>In the diagram palette, click <strong>Collaborator Comment</strong> and click anywhere on the diagram pane to create a comment.</li><li>Enter comment text on the shape of the comment and click anywhere on the diagram pane to save it.</li><li>Create an Anchor from the comment to the commented element.</li><li><p class="auto-cursor-target">Find the new comment in the Containment tree of your project and move it to the Package with the «CollaboratorComments» stereotype. This Package name is typically the same as the project.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3c7c7892-4b75-4f11-9c34-f8ffa251669d"><ac:parameter ac:name="title">Collaborator Comments Package</ac:parameter><ac:rich-text-body><p>If this is the first Cameo Collaborator comment created in the project and the Package with the «CollaboratorComments» stereotype does not exist, create a Package dedicated to comments and apply the <span>«CollaboratorComments» stereotype to it. Then place the newly created comment in this Package. All Cameo Collaborator comments must be stored in that Package to be valid and visible in a published document.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p>The Cameo Collaborator Comment will be visible in a published document once you commit changes to the server and refresh the document. If you want to create comments in the Containment tree of your model, you can do it as described below.</p><p><br /></p><p>To create a Cameo Collaborator comment in the Containment tree</p><hr /><ol><li><p class="auto-cursor-target">In the Containment tree of your model, right-click the Package with the «CollaboratorComments» stereotype and select <strong>Create Element</strong> &gt; <strong>Comment</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="94313c6f-4b4d-44c0-930c-c33f5a866914"><ac:parameter ac:name="title">Collaborator Comments Package</ac:parameter><ac:rich-text-body><p>If this is the first Cameo Collaborator comment created in the project and the Package with the «CollaboratorComments» stereotype does not exist, create a Package dedicated to comments and apply the «CollaboratorComments» stereotype to it. All Cameo Collaborator comments must be stored in such a Package to be valid and visible in a published document.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Type the text of the comment and press Enter.</li><li>Right-click the created comment and select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Elements</strong> &gt;<strong> Collaborator Comment</strong>.</li><li>Open the Specification window of the new Cameo Collaborator comment, select the specification cell of the <strong>Annotated Element</strong> property, and click <ac:image><ri:attachment ri:filename="edit.png" /></ac:image>.</li><li>On the left side of the Select Elements dialog, select the element the comment is created for and click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="add.png" /></ac:image> to add it to the selected elements area.</li><li>Click <strong>OK</strong> and close the Specification window.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="creating_comments_in_diagram.png" /></ac:image></p><h6 style="text-align: center;">This figure shows Cameo Collaborator comments in a diagram and the Containment tree.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180518 space=TWCloud2024xR1 version=2 -->
## PAGE 00277: Working with comments in a modeling tool

- page_id: `171180518`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180518/Working+with+comments+in+a+modeling+tool
- version_number: 2
- version_date: `2024-05-09T13:41:31.727+02:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: []

### NORMALIZED CONTENT

When you get feedback in a Cameo Collaborator document, you can address comments straight from the modeling tool. This saves time because you can quickly navigate from comments to commented elements and modify them without leaving the modeling environment.

#### NOTE: Cameo Collaborator and 3DEXPERIENCE platform

Cameo Collaborator and 3DEXPERIENCE platform

If [CONFLUENCE_PAGE title='Enabling 3DEXPERIENCE collaboration in a modeling tool' space='MD2024xR1']collaboration powered by the **3D**EXPERIENCE platform is enabled in the Environment Options, The Cameo Collaborator Publisher plugin is disabled in the modeling tool, and you cannot work with Cameo Collaborator for Teamwork Cloud.

Once a Cameo Collaborator document has comments you need to respond to, do the following:

1. In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.
2. [CONFLUENCE_PAGE title='Opening the comments panel' space='TWCloud2024xR1'] .
3. Do one or several of the following actions:
  1. Select a comment in the comments panel to navigate to the commented element and its commented properties.
4. Modify the model to address comments .
5. [CONFLUENCE_PAGE title='Replying to a comment' space='TWCloud2024xR1'] to confirm that they have been addressed or ask additional questions (you can also resolve, edit, and delete comments).
6. Save/commit and [CONFLUENCE_PAGE title='Publishing documents' space='TWCloud2024xR1'] the updated model.

[IMAGE alt='' src='']

###### Use the comments panel in your modeling tool to navigate to the commented element and update it in the model.

To learn more about working with comments in a modeling tool, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">When you get feedback in a Cameo Collaborator document, you can address comments straight from the modeling tool. This saves time because you can quickly navigate from comments to commented elements and <ac:inline-comment-marker ac:ref="be6f0423-73b9-4959-9c8d-c44d0313e3d5">modify</ac:inline-comment-marker> them without leaving the modeling environment.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d91ba1c8-fbaf-4f6b-8bc8-b511516d007b"><ac:parameter ac:name="title">Cameo Collaborator and 3DEXPERIENCE platform</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Enabling 3DEXPERIENCE collaboration in a modeling tool" /><ac:link-body>collaboration powered by the <strong>3D</strong>EXPERIENCE platform is enabled in the Environment Options</ac:link-body></ac:link>, The Cameo Collaborator Publisher plugin is disabled in the modeling tool, and you cannot work with Cameo Collaborator for Teamwork Cloud.</span></p></ac:rich-text-body></ac:structured-macro><p>Once a Cameo Collaborator document has comments you need to respond to, do the following:</p><ol><li>In a modeling tool, connect to Teamwork Cloud and open the model with Cameo Collaborator comments.</li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Opening the comments panel" /><ac:plain-text-link-body><![CDATA[Open the comments panel]]></ac:plain-text-link-body></ac:link>.</li><li>Do one or several of the following actions:<ol><li>Select a comment in the comments panel to navigate to the commented element and its commented properties.</li></ol></li><li><ac:inline-comment-marker ac:ref="f915abc6-3ea8-434d-a99a-3f01ed94103a">Modify the model to address comments</ac:inline-comment-marker>.</li><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Replying to a comment" /><ac:plain-text-link-body><![CDATA[Reply to comments]]></ac:plain-text-link-body></ac:link> to confirm that they have been addressed or ask additional questions</span> (you can also resolve, edit, and delete comments).</li><li><ac:inline-comment-marker ac:ref="f137d148-257c-452a-94dd-dfd941a798d6">Save/commit</ac:inline-comment-marker> and <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Publishing documents" /><ac:plain-text-link-body><![CDATA[publish]]></ac:plain-text-link-body></ac:link> the updated model.</li></ol><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="comments_panel.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Working with comments in a modeling tool" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Use the comments panel in your modeling tool to navigate to the commented element and update it in the model.</h6><p><ac:inline-comment-marker ac:ref="3ce71186-6f6c-47d1-b85d-cad9d2c9da4f">To learn more about working with comments in a modeling tool, see the following topics:</ac:inline-comment-marker></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180563 space=TWCloud2024xR1 version=2 -->
## PAGE 00278: Working with comments in Cameo Collaborator

- page_id: `171180563`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180563/Working+with+comments+in+Cameo+Collaborator
- version_number: 2
- version_date: `2025-10-31T12:32:51.627+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Working with comments
- labels: ['commenting', 'working-with-comments']

### NORMALIZED CONTENT

Comments can be either textual or graphical. Textual comments can be associated with any element or any of its standard properties, while graphical comments can be attached to diagrams, maps, and matrices. Both types of comments can be further edited, replied, resolved, or deleted. The full list of comments in the published project is displayed in the [CONFLUENCE_PAGE title='Comments pane' space='']**Comments** pane.

Learn more about working with comments in the following pages:

#### NOTE: Documents published from synchronized projects

Documents published from synchronized projects

If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. [CONFLUENCE_PAGE title='Cross-cluster resource synchronization' space=''].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Comments can be either textual or graphical. Textual comments can be associated with any element or any of its standard properties, while graphical comments can be attached to diagrams, maps, and matrices. Both types of comments can be further edited, replied, resolved, or deleted. The full list of comments in the published project is displayed in the <ac:link><ri:page ri:content-title="Comments pane" /><ac:link-body><strong>Comments</strong> pane</ac:link-body></ac:link>.</p><p>Learn more about working with comments in the following pages:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="802708fb-69cd-486a-b266-7e623ed7eac1" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="40ec8c45-01b7-4413-a02f-f98fbae18aba"><ac:parameter ac:name="title">Documents published from synchronized projects</ac:parameter><ac:rich-text-body><p>If a Cameo Collaborator document is published from a synchronized project on the target Teamwork Cloud server, the commenting and model editing capabilities in the document will be disabled so that the synchronized project on the target server cannot be modified. <ac:link><ri:page ri:content-title="Cross-cluster resource synchronization" /><ac:plain-text-link-body><![CDATA[Learn more about cross-cluster resource synchronization]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=171180396 space=TWCloud2024xR1 version=1 -->
## PAGE 00279: Working with custom document templates

- page_id: `171180396`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180396/Working+with+custom+document+templates
- version_number: 1
- version_date: `2024-03-12T11:32:19.112+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Cameo Collaborator for Teamwork Cloud > Publishing documents > Document templates
- labels: []

### NORMALIZED CONTENT

When configuring settings for publishing a model to Cameo Collaborator, you must choose a template to determine the appearance and content of a published document. If predefined templates do not meet your specific needs, you can create and applya custom template. In custom templates, you can specify which model elements are published, what element information is displayed, and the format in which it is displayed. A custom template can be stored within a model itself or as a separate .mdzip file, which allows you to reuse it in multiple models. The following topics will help you learn how to modify a predefined template or create your own template from scratch:

##### Document template samples

If you are new to working with custom document templates, you may find it useful to analyze our [ATTACHMENT filename='Cameo Collaborator Template Samples.mdzip'] project which you can find with the other sample projects in your modeling tool installation directory. These template samples give step by step instructions on how to model several different document templates. The Content Diagram below shows what template modeling use cases you can find in the *Cameo Collaborator Template Samples* project.

[IMAGE alt='' src='']

###### The content of the *Cameo Collaborator Template Samples* project.

**Related pages**

- [CONFLUENCE_PAGE title='Document templates' space='TWCloud2024xR1']
  - [CONFLUENCE_PAGE title='Using a custom template in a model' space='TWCloud2024xR1']
  - [CONFLUENCE_PAGE title='Customizing the appearance of a project portal' space='TWCloud2024xR1']
  - [CONFLUENCE_PAGE title='Enabling the Document View' space='TWCloud2024xR1']
  - [CONFLUENCE_PAGE title='Enabling the Single Tree View' space='TWCloud2024xR1']

**Additional resources**

- Webinar *Creating Templates in Cameo Collaborator*
- User Guide for Creating Cameo Collaborator Templates
- [ATTACHMENT filename='Cameo Collaborator Template Samples.mdzip']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(62,63,64);">When configuring settings for publishing a model to Cameo Collaborator, you must choose a template to determine the appearance and content of a published document. If predefined templates do not meet your specific needs, you can create and apply </span>a custom template. I<ac:inline-comment-marker ac:ref="34e1ac03-973a-4d3b-9990-6d0acc52d648"><ac:inline-comment-marker ac:ref="510a631f-76e4-4f7f-ae28-2379aa848ca4">n custom templates, you can specify which model elements are published, what element information is displayed, and the format in which it is displayed</ac:inline-comment-marker></ac:inline-comment-marker>. A custom template can be stored within a model itself or <span style="letter-spacing: 0.0px;">as a separate .mdzip file, which allows you to reuse it in multiple models</span>. The following topics will help you learn how to modify a predefined template or create your own template from scratch:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e05c3f95-95ee-4fb2-a650-cdabdd95f838" /></p><h3 style="color: rgb(23,43,77);"><br />Document template samples</h3><p>If you are new to working with custom document templates, you may find it useful to analyze our <ac:link><ri:attachment ri:filename="Cameo Collaborator Template Samples.mdzip"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Working with custom document templates" /></ri:attachment></ac:link> project which you can find with the other sample projects in your modeling tool installation directory. These template samples give step by step instructions on how to model several different document templates. The Content Diagram below shows what template modeling use cases you can find in the <em>Cameo Collaborator Template Samples</em> project.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="samples_content_diagram.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Working with custom document templates" /></ri:attachment></ac:image></p><h6 style="line-height: 1.66667;letter-spacing: normal;text-align: center;">The content of the <em>Cameo Collaborator Template Samples</em> project.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Document templates" /></ac:link><ul><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Using a custom template in a model" /></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Customizing the appearance of a project portal" /></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Enabling the Document View" /></ac:link></li><li><ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Enabling the Single Tree View" /></ac:link></li></ul></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Additional resources</strong></p><ul><li><a href="https://youtu.be/NAoYVUJhT2A">Webinar <em>Creating Templates in Cameo Collaborator</em></a></li><li><a href="https://ccexamples.nomagic.com/collaborator/document/66babacb-881a-480e-a104-86427d8fabe8?viewId=12dd9272-276a-4de4-99d5-598f1fcc3bfb&amp;viewType=document&amp;sectionId=f71e7d7a-55f0-487c-bb40-ba4fa335922f&amp;guest=true">User Guide for Creating Cameo Collaborator Templates</a></li><li><ac:link><ri:attachment ri:filename="Cameo Collaborator Template Samples.mdzip"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Working with custom document templates" /></ri:attachment></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170491484 space=TWCloud2024xR1 version=3 -->
## PAGE 00280: Working with keystores

- page_id: `170491484`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/170491484/Working+with+keystores
- version_number: 3
- version_date: `2025-10-30T14:06:09.299+01:00`
- ancestors: Teamwork Cloud and Services > Administration Guide > Teamwork Cloud administration
- labels: []

### NORMALIZED CONTENT

**On this page**

****

##### Keystore Types

There are two types of keystores that are supported by Java:

- JKS - Native Java archive, to be deprecated in favor of PKCS#12 standard
- PKCS#12 - archive format containing multiple cryptographic objects (also referred to as PFX)

##### Tools

There are two tools that are used when working with keystores and certificates:

- keytool - command-line tool, part of the java distribution, for manipulating keystores (JKS and PKCS#12)
- OpenSSL - client tool for manipulating certificates in multiple formats

All of the required tasks can be accomplished with keytool, so we will limit the scope of keystore management to keytool.

##### Create a keystore

Create a keystore in PKCS#12 format - the command below will create a keystore with a self-signed certificate for the given server. Please note that in order to have a signed certificate, the common name of the certificate cannot be an IP address.

Also, please note that in this example, we are also creating 3 subject alternative names: 1 for the common name (fqdn), 1 for the hostname (hostname), and one for the IP address of the server.

```text
-storetype  pkcs12 -storepass  -alias  -dname "CN=,OU=,O=,L=,S=,C=" -ext BasicConstraints:critical=ca:false -ext SAN=dns:,dns:,ip:]]>
```

##### View contents of a keystore

```text
-storepass ]]>
```

##### Create a CSR

Create a CSR from an existing keystore, adding the subject alternative names. The alias is that containing the entry of type **PrivateKeyEntry.**

```text
-storepass  -alias  -file  -ext SAN=dns:,dns:,ip: -ext BasicConstraints:critical=ca:false]]>
```

##### View contents of a CSR

```text
]]>
```

##### Import signed certificate into keystore

A signed server certificate must be imported into the keystore from which the CSR was generated, and into the same alias.

```text
-storepass  -alias  -file ]]>
```

When you obtain your signed certificate, it may be provided in a variety of ways. One possibility is that it is a PKCS#7 chained certificate (contains the signed server certificate as well as the certificate chain). Another option is that it is that you were provided a single signed certificate and a set of certificates comprising the certificate chain. If you were provided a PKCS#7, you will import it into the PrivateKeyEnty alias. If you were provided separate certificates, you will import the server certificate into the PrivateKeyEntry alias, and then import each of the other certificates into a different alias - for example -alias intermediate1, -alias intermediate2, -alias caroot.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="492e05f5-bc27-4e77-a1a7-1342a581852b" /></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3 style="color:var(--ds-text,#172b4d);">Keystore Types</h3><p>There are two types of keystores that are supported by Java:</p><ul><li>JKS - Native Java archive, to be deprecated in favor of PKCS#12 standard</li><li>PKCS#12 - archive format containing multiple cryptographic objects (also referred to as PFX)</li></ul><h3 style="color:var(--ds-text,#172b4d);">Tools</h3><p>There are two tools that are used when working with keystores and certificates:</p><ul><li>keytool - command-line tool, part of the java distribution, for manipulating keystores (JKS and PKCS#12)</li><li>OpenSSL - client tool for manipulating certificates in multiple formats<br /><br /></li></ul><p>All of the required tasks can be accomplished with keytool, so we will limit the scope of keystore management to keytool.</p><h3 style="color:var(--ds-text,#172b4d);">Create a keystore</h3><p>Create a keystore in PKCS#12 format - the command below will create a keystore with a self-signed certificate for the given server. Please note that in order to have a signed certificate, the common name of the certificate cannot be an IP address.</p><p>Also, please note that in this example, we are also creating 3 subject alternative names: 1 for the common name (fqdn), 1 for the hostname (hostname), and one for the IP address of the server.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="3b8eef0f-d20d-4fd2-9223-592b401f9535"><ac:plain-text-body><![CDATA[keytool -genkeypair -keyalg RSA -sigalg SHA256withRSA -keysize 2048 -validity 3650 -keystore <keystore.p12> -storetype  pkcs12 -storepass <storepass> -alias <aliasname> -dname "CN=<fqdn>,OU=<Org Unit>,O=<Company Name>,L=<City>,S=<State>,C=<Country>" -ext BasicConstraints:critical=ca:false -ext SAN=dns:<fqdn>,dns:<hostname>,ip:<ip_address>]]></ac:plain-text-body></ac:structured-macro><h3 class="auto-cursor-target" style="color:var(--ds-text,#172b4d);">View contents of a keystore</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="407d6ee5-d2b8-44c5-bbc3-3c1aec03571a"><ac:plain-text-body><![CDATA[keytool -list -v -keystore <keystore.p12> -storepass <storepass>]]></ac:plain-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);">Create a CSR</h3><p>Create a CSR from an existing keystore, adding the subject alternative names. The alias is that containing the entry of type <strong>PrivateKeyEntry.</strong></p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="63167c2b-89df-4fd7-9674-eb3d4abc36e0"><ac:plain-text-body><![CDATA[keytool -noprompt -certreq -keystore <keystore.p12> -storepass <storepass> -alias <aliasname> -file <server.csr> -ext SAN=dns:<fqdn>,dns:<hostname>,ip:<ipaddress> -ext BasicConstraints:critical=ca:false]]></ac:plain-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);">View contents of a CSR</h3><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="d48f098c-f6d2-4ddb-a685-9d91c3d01681"><ac:plain-text-body><![CDATA[keytool -printcertreq -file <server.csr>]]></ac:plain-text-body></ac:structured-macro><h3 style="color:var(--ds-text,#172b4d);">Import signed certificate into keystore</h3><p>A signed server certificate must be imported into the keystore from which the CSR was generated, and into the same alias.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="8b2a3a95-a182-4d78-8db6-343144e4f790"><ac:plain-text-body><![CDATA[keytool -importcert -trustcacerts -keystore <keystore.p12> -storepass <storepass> -alias <aliasname> -file <server.crt>]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8903cde7-446f-42c0-88cb-1e168bdff0fa"><ac:rich-text-body><p>When you obtain your signed certificate, it may be provided in a variety of ways. One possibility is that it is a PKCS#7 chained certificate (contains the signed server certificate as well as the certificate chain). Another option is that it is that you were provided a single signed certificate and a set of certificates comprising the certificate chain. If you were provided a PKCS#7, you will import it into the PrivateKeyEnty alias. If you were provided separate certificates, you will import the server certificate into the PrivateKeyEntry alias, and then import each of the other certificates into a different alias - for example -alias intermediate1, -alias intermediate2, -alias caroot.</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=171180272 space=TWCloud2024xR1 version=1 -->
## PAGE 00281: Working with resources

- page_id: `171180272`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180272/Working+with+resources
- version_number: 1
- version_date: `2024-01-29T09:32:50.134+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Resources application
- labels: []

### NORMALIZED CONTENT

The Resources app allows you to access and manage three types of resources:

- UML/SysML models (.mdzip files)
- Cameo Collaborator for Teamwork Could documents
- OSLC resources

See the following chapters to learn how to open, edit, or remove a resource:

Aftercreating/editing/removing a resource, the resource in the other applications will not be updated immediately.

[IMAGE alt='' src='']

###### Different types of resources in the Resources app.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Resources app allows you to access and manage three types of resources:</p><ul><li>UML/SysML models (.mdzip files)</li><li>Cameo Collaborator for Teamwork Could documents</li><li>OSLC resources</li></ul><p>See the following chapters to learn how to open, edit, or remove a resource:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5f4281b1-816c-45ed-859b-23bfd39c4cb4"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">After </span><span style="color: rgb(23,43,77);">creating/editing/removing a resource, the resource in the other applications will not be updated immediately.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="types_of_resources.png"><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Working with resources" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Different types of resources in the Resources app.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=171180238 space=TWCloud2024xR1 version=1 -->
## PAGE 00282: Working with webhooks

- page_id: `171180238`
- space_key: `TWCloud2024xR1`
- source_url: https://docs.nomagic.com/spaces/TWCloud2024xR1/pages/171180238/Working+with+webhooks
- version_number: 1
- version_date: `2024-01-29T09:41:34.129+01:00`
- ancestors: Teamwork Cloud and Services > User Guide > Admin web applications > Settings application
- labels: []

### NORMALIZED CONTENT

Webhooks allow you to get notifications pushed to a specified endpoint on predefined events in Teamwork Cloud instead of constantly polling for new data through REST APIs. You can listen to commit-type events in chosen resources or model elements and element-level events, such as commit or tagged commit.

To work with webhooks, a user needs the following permissions: **Read Resources**, **Configure Server,** and **Administer Resources**. For more information, see the article on [CONFLUENCE_PAGE title='Permissions' space='TWCloud2024xR1'].

For more information on creating and managing webhooks, see the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);">Webhooks allow you to get notifications pushed to a specified endpoint on predefined events in Teamwork Cloud instead of constantly polling for new data through REST APIs. You can listen to commit-type events in chosen resources or model elements and element-level events, such as commit or tagged commit.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9a7ff00f-a9dc-4603-ad59-5b7116a72ea8"><ac:rich-text-body><p><span style="color: rgb(0,0,0);">To work with webhooks, a user needs the following permissions: <strong>Read Resources</strong>, <strong>Configure Server,</strong> and <strong>Administer Resources</strong>. For more information, see the article on <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="Permissions" /></ac:link>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">For more information on creating and managing webhooks, see the following pages:</span></p><p class="auto-cursor-target"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1af390c3-7a92-4d14-bb6a-49fc02d6d986" /></p>
````
