# NI DOCUMENT BUNDLE: labview-opc-ua-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-opc-ua-toolkit-api-ref start=1 end=59 -->
<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=alarms-and-conditions-vis.html language=enus -->
## TOPIC 00001: Alarms and Conditions VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `alarms-and-conditions-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/alarms-and-conditions-vis.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA client applications. Exa

### Alarms and Conditions VIs

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA client applications.

Example

| Palette Object | Description |
| --- | --- |
| Add Monitored Event Nodes | Adds notifiers to an event subscription to monitor condition event notifications. |
| Create Event Subscription | Creates a subscription to the notifiers of an OPC UA server. |
| Disable Condition | Moves a condition to disabled state. |
| Enable Condition | Moves a condition to enabled state. |
| Respond Acknowledgeable Condition | Responds to an acknowledgeable condition by confirming, acknowledging, or adding comments to the condition. Acknowledgeable conditions expose states to indicate whether a condition must be acknowledged or confirmed. |
| Respond Dialog Condition | Returns a response option and ends a dialog. |
| Shelve Alarm Condition | Transits among the one-shot shelved state, the timed shelved state, and the unshelved state for an alarm. The one-shot shelved state prevents an alarm from displaying for its current active state. The timed shelved state prevents an alarm from displaying for a definite time period. The unshelved state allows an alarm to display. You must manually select the polymorphic instance to use. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Alarms and Conditions VIs.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=alarms-and-conditions-vis2.html language=enus -->
## TOPIC 00002: Alarms and Conditions VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `alarms-and-conditions-vis2.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/alarms-and-conditions-vis2.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA server applications. Exa

### Alarms and Conditions VIs

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA server applications.

Example

| Palette Object | Description |
| --- | --- |
| Add Condition | Adds a condition node to the notifier. You must manually select the polymorphic instance to use. |
| Add Notifier | Adds a notifier to a parent folder. A notifier is an object that you can subscribe to get events from the associated condition nodes. To establish an event hierarchy, you can add a condition node and a source node as child nodes to a notifier. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Alarms and Conditions VIs.

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=browse-vi.html language=enus -->
## TOPIC 00003: Browse VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `browse-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/browse-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Browses a given node path and returns the path, name, and type of all its children nodes. OPC UA client refnum in specifies the reference for the OPC UA client. node path specifies the path of the node. If node path is empty, this VI browses from the root path. The

### Browse VI

**Owning Palette:** OPC UA Client VIs

Browses a given node path and returns the path, name, and type of all its children nodes.

[IMAGE alt='image' src='images/opcua_browse.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node path specifies the path of the node. If node path is empty, this VI browses from the root path. The node path consists of node names separated by a period between each name, with the parent node name before the period and child node name after the period. For example, a node path Device.folder.item indicates that Device is the parent node of folder, and folder is the parent node of item. You can use the Node Name Array To Node Path VI to convert the node names to node path. The following examples demonstrate how to specify node path. If a node name contains a period, use a pair of quotation marks around the node name. For example, if a node name is Device.1, and this node contains a child node folder, the node path of the child node is "Device.1".folder. If a node name contains one or more quotation marks, add one quotation mark beside each quotation mark and then a pair of quotation marks around the node name. For example, if a node name is Device1"Device2, and this node contains a child node folder, the node path of the child node is "Device1""Device2".folder. If a node name contains both a period and quotation mark, both of the previous rules still apply. For example, if a node name is Device1"Device2.Device3, and this node contains a child node folder, the node path of the child node is "Device1""Device2.Device3".folder. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default value is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | browse result returns an array of clusters containing the path, name, and type of all the children nodes. node path returns the path of the node. node name returns the name of the node. node type returns the type of the node. Digital Display Node Type 0 Other 1 Folder 2 Item/Property |
|  | node path returns the path of the node. |
|  | node name returns the name of the node. |
|  | node type returns the type of the node. Digital Display Node Type 0 Other 1 Folder 2 Item/Property |
| Digital Display | Node Type |
| 0 | Other |
| 1 | Folder |
| 2 | Item/Property |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=clear-all-trusted-clients-vi.html language=enus -->
## TOPIC 00004: Clear All Trusted Clients VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `clear-all-trusted-clients-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/clear-all-trusted-clients-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit Clears the OPC UA client certificates that an OPC UA server trusts. After you start an OPC UA server, you cannot clear the trusted client certificates until the OPC UA server stops. Use the Stop VI to stop an OPC UA server. OPC UA server ref

### Clear All Trusted Clients VI

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit

Clears the OPC UA client certificates that an OPC UA server trusts.

After you start an OPC UA server, you cannot clear the trusted client certificates until the OPC UA server stops. Use the Stop VI to stop an OPC UA server.

[IMAGE alt='image' src='images/opcua_clear_all_trusted_clients.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=close-vi.html language=enus -->
## TOPIC 00005: Close VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `close-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/close-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit Closes and destroys an OPC UA server. After you close an OPC UA server, you lose all the data that belongs to the OPC UA server. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. error in describes erro

### Close VI

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit

Closes and destroys an OPC UA server. After you close an OPC UA server, you lose all the data that belongs to the OPC UA server.

Example

[IMAGE alt='image' src='images/opcua_close.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Close VI.

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=connect-vi.html language=enus -->
## TOPIC 00006: Connect Server VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `connect-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/connect-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Creates a connection to an OPC UA server. Example trust any server specifies whether the OPC UA client trusts any OPC UA server without adding the server certificate to trusted server certificates. The default is FALSE, which specifies that

### Connect Server VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Creates a connection to an OPC UA server.

Example

[IMAGE alt='image' src='images/opcua_connect.gif']

|  | trust any server specifies whether the OPC UA client trusts any OPC UA server without adding the server certificate to trusted server certificates. The default is FALSE, which specifies that the OPC UA client trusts only OPC UA servers that have server certificates in trusted server certificates. |
| --- | --- |
|  | username/password specifies the username and password to authenticate when you create a connection to an OPC UA server. You must specify username/password if the OPC UA server requires authentication. username specifies the username for connecting to the OPC UA server. password specifies the password for connecting to the OPC UA server. |
|  | username specifies the username for connecting to the OPC UA server. |
|  | password specifies the password for connecting to the OPC UA server. |
|  | server endpoint URL specifies the hostname and the port of the OPC UA server. The format of server endpoint URL is opc.tcp://hostname:port. The hostname is the IP address or computer name. |
|  | security policy specifies the message mode and the corresponding security policy. message mode specifies the mode of the message. If the message mode is None, this VI ignores security. 0None (default)The OPC UA client and OPC UA server do not need to trust each other.1SignThe OPC UA server supports signed messages but not encrypted messages.2Sign and EncryptThe OPC UA server supports signed and encrypted messages. security specifies the security policy. 0Basic256Sha256 (default)1Aes128Sha256RsaOaep2Aes256Sha256RsaPss |
|  | message mode specifies the mode of the message. If the message mode is None, this VI ignores security. 0None (default)The OPC UA client and OPC UA server do not need to trust each other.1SignThe OPC UA server supports signed messages but not encrypted messages.2Sign and EncryptThe OPC UA server supports signed and encrypted messages. |
| 0 | None (default)The OPC UA client and OPC UA server do not need to trust each other. |
| 1 | SignThe OPC UA server supports signed messages but not encrypted messages. |
| 2 | Sign and EncryptThe OPC UA server supports signed and encrypted messages. |
|  | security specifies the security policy. 0Basic256Sha256 (default)1Aes128Sha256RsaOaep2Aes256Sha256RsaPss |
| 0 | Basic256Sha256 (default) |
| 1 | Aes128Sha256RsaOaep |
| 2 | Aes256Sha256RsaPss |
|  | client certificate file specifies the path or name of the public key. The file extension of the file you specify must be .der. The public key and private key must have the same name and reside in the same folder. If you do not specify client certificate file, this VI generates and uses a new certificate file. By default, an OPC UA client trusts the certificate it is using. You can specify a relative path or filename for client certificate file. If you specify a relative path, the path is relative to the caller VI or to the application directory. If you specify a filename, LabVIEW searches the certificate files only in the location where the caller VI resides or in the application directory. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | trusted server certificates specifies the paths or names of the public keys that the OPC UA client trusts. By default, OPC UA client applications trust the public key that the OPC UA client uses. You can specify a relative path or filename for trusted server certificates. If you specify a relative path, the path is relative to the caller VI or to the application directory. If you specify a filename, LabVIEW searches the certificate files only in the location where the caller VI resides or in the application directory. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | OPC UA data change event returns notifications to the OPC UA client from all the subscriptions that the OPC UA client has created. The notifications contain updates of the data on the OPC UA server. NI does not recommend using this output. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Connect Server VI.

#### History

- OPC UA Toolkit 2025 Q4:
 Introduced Basic256Sha256, Aes128Sha256RsaOaep and Aes256Sha256RsaPss security policies.
 Deprecated Basic128Rsa15 and Basic256 security policies.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=create-certificate-vi.html language=enus -->
## TOPIC 00007: Create Certificate VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `create-certificate-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/create-certificate-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA VIs Requires: OPC UA Toolkit Creates a pair of certificate files with the name you specify. You can use the certificate files to create an OPC UA server or connect to an OPC UA server. The start time of the certificate file is the current system time. The lifetime is four year

### Create Certificate VI

**Owning Palette:** OPC UA VIs

**Requires:** OPC UA Toolkit

Creates a pair of certificate files with the name you specify. You can use the certificate files to create an OPC UA server or connect to an OPC UA server.

The start time of the certificate file is the current system time. The lifetime is four years.

Example

[IMAGE alt='image' src='images/opcua_create_certificate.gif']

|  | certificate name in specifies the name of the certificates to create. If you do not specify this input, this VI creates a pair of certificates with the default name of Default OPC UA. |
| --- | --- |
|  | key length specifies number of bits for the encryption key to be used for certificates to create. If you do not specify this input, default key length would be 1024 bits. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | certificate name out returns the name of the certificates that you create. certificate name out contains only the filename without the file extension. Both the public key and the private key use the same certificate name but with different file extensions. Public key commonly appears with a .der file extension and private key has a .pem file extension. |
|  | certificate path returns the full path of the certificate file. You can find the public key file in this path. |
|  | exist? returns whether a certificate with the same name already exists. If a certificate with the same name already exists, this VI does not create the certificate. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Create Certificate VI.

#### History

- OPC UA Toolkit 2025 Q4: added support for **key length**.

Parent topic:

OPC UA VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=create-event-subscription-vi.html language=enus -->
## TOPIC 00008: Create Event Subscription VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `create-event-subscription-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/create-event-subscription-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Alarms and Conditions VIs Requires: OPC UA Toolkit Creates a subscription to the notifiers of an OPC UA server. A notifier is an object that you can subscribe to get events from the associated condition nodes. Example OPC UA client refnum in specifies the reference for the OPC UA cli

### Create Event Subscription VI

**Owning Palette:** Alarms and Conditions VIs

**Requires:** OPC UA Toolkit

Creates a subscription to the notifiers of an OPC UA server.

A notifier is an object that you can subscribe to get events from the associated condition nodes.

Example

[IMAGE alt='image' src='images/Create_Event_Subscription.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | publishing interval defines the rate, in milliseconds, that the OPC UA server returns event notifications to the OPC UA client. The default is 1000. publishing interval must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | subscription ID out returns the reference of the subscription that this VI accessed. |
|  | OPC UA condition event returns notifications to the OPC UA client if the client has created an event subscription. The notifications contain updates of the events on the OPC UA server. The publishing interval of Create Event Subscription VI defines the frequency of sending notifications. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Create Event Subscription VI.

Parent topic:

Alarms and Conditions VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=create-subscription-vi.html language=enus -->
## TOPIC 00009: Create Subscription VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `create-subscription-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/create-subscription-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Creates a subscription to the nodes of the OPC UA server. When the nodes that the OPC UA client subscribes to incur data changes, the OPC UA server collects the data changes and sends a notification message to the OPC UA client. Example OPC

### Create Subscription VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Creates a subscription to the nodes of the OPC UA server. When the nodes that the OPC UA client subscribes to incur data changes, the OPC UA server collects the data changes and sends a notification message to the OPC UA client.

Example

[IMAGE alt='image' src='images/opcua_create_subscription.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | publishing interval defines the rate, in milliseconds, that the OPC UA server returns data change notifications to the OPC UA client. The default is 1000. publishing interval must be greater than 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | subscription ID out returns the reference of the subscription that this VI accessed. |
|  | OPC UA data change event returns notifications to the OPC UA client if the client has created a subscription. The notifications contain updates of the data on the OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Create Subscription VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=create-vi.html language=enus -->
## TOPIC 00010: Create Server VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `create-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/create-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit Creates and initializes an OPC UA server. When you use the Connect Server VI to connect an OPC UA client to an OPC UA server and set the message mode as None, the OPC UA client and OPC UA server do not need to trust each other. Example trust

### Create Server VI

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit

Creates and initializes an OPC UA server.

When you use the Connect Server VI to connect an OPC UA client to an OPC UA server and set the **message mode** as None, the OPC UA client and OPC UA server do not need to trust each other.

Example

[IMAGE alt='image' src='images/opcua_create.gif']

|  | trust all clients specifies whether the OPC UA server trusts all OPC UA clients without adding the trusted client certificates to the OPC UA server. The default is FALSE, which specifies that the OPC UA server trusts only OPC UA clients that have trusted OPC UA client certificates added to the OPC UA server. You can use the Add Trusted Clients VI to add trusted OPC UA client certificates to an OPC UA server. |
| --- | --- |
|  | OPC UA server name specifies the name of the OPC UA server. |
|  | TCP port specifies the TCP port that the OPC UA server takes. The default is 49580. If the port that you specify is occupied, this VI is unable to create an OPC UA server. You can create multiple OPC UA servers on the same target with different ports. |
|  | supported security policies specifies the supported message modes and corresponding security policies. The default is None, which means the OPC UA client can connect without security. Use the Connect Server VI to determine which supported security policy to use when connecting the OPC UA client to the OPC UA server. None specifies that the OPC UA server supports no security. The OPC UA client can connect without security. Sign with Basic256Sha256 specifies that the OPC UA server supports signing messages using the Basic256Sha256 security policy. Sign and Encrypt with Basic256Sha256 specifies that the OPC UA server supports signing and encrypting messages using the Basic256Sha256 security policy. Sign with Aes128Sha256RsaOaep specifies that the OPC UA server supports signing messages using the Aes128Sha256RsaOaep security policy. Sign and Encrypt with Aes128Sha256RsaOaep specifies that the OPC UA server supports signing and encrypting messages using the Aes128Sha256RsaOaep security policy. Sign with Aes256Sha256RsaPss specifies that the OPC UA server supports signing messages using the Aes256Sha256RsaPss security policy. Sign and Encrypt with Aes256Sha256RsaPss specifies that the OPC UA server supports signing and encrypting messages using the Aes256Sha256RsaPss security policy. |
|  | None specifies that the OPC UA server supports no security. The OPC UA client can connect without security. |
|  | Sign with Basic256Sha256 specifies that the OPC UA server supports signing messages using the Basic256Sha256 security policy. |
|  | Sign and Encrypt with Basic256Sha256 specifies that the OPC UA server supports signing and encrypting messages using the Basic256Sha256 security policy. |
|  | Sign with Aes128Sha256RsaOaep specifies that the OPC UA server supports signing messages using the Aes128Sha256RsaOaep security policy. |
|  | Sign and Encrypt with Aes128Sha256RsaOaep specifies that the OPC UA server supports signing and encrypting messages using the Aes128Sha256RsaOaep security policy. |
|  | Sign with Aes256Sha256RsaPss specifies that the OPC UA server supports signing messages using the Aes256Sha256RsaPss security policy. |
|  | Sign and Encrypt with Aes256Sha256RsaPss specifies that the OPC UA server supports signing and encrypting messages using the Aes256Sha256RsaPss security policy. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | server certificate file specifies the path or name of the public key. You must name the public key and private key as the same and keep them in the same folder. If you do not specify the certificate file path, this VI generates and uses the default certificate. If you specify your own certificate, this VI uses and trusts your certificate. The OPC UA server always trusts the certificate that the OPC UA server is using. You can specify a relative path or filename for server certificate file. If you specify a relative path, the path is relative to the caller VI or to the application directory. If you specify a filename, LabVIEW searches the certificate file only in the location where the caller VI resides or in the application directory. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | server endpoint URL returns the unique identifier of the OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Create Server VI.

#### History

- OPC UA Toolkit 2025 Q4:
 Introduced Basic256Sha256, Aes128Sha256RsaOaep and Aes256Sha256RsaPss security policies.
 Deprecated Basic128Rsa15 and Basic256 security policies.

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=delete-monitored-nodes-vi.html language=enus -->
## TOPIC 00011: Delete Monitored Nodes VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `delete-monitored-nodes-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/delete-monitored-nodes-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Deletes one or multiple monitored nodes from a subscription. Example OPC UA client refnum in specifies the reference for the OPC UA client. subscription ID in specifies the ID of the subscription. node IDs specifies the IDs of the nodes. The

### Delete Monitored Nodes VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Deletes one or multiple monitored nodes from a subscription.

Example

[IMAGE alt='image' src='images/opcua_delete_monitored_nodes.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | subscription ID in specifies the ID of the subscription. |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | subscription ID out returns the reference of the subscription that this VI accessed. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Delete Monitored Nodes VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=delete-node-vi.html language=enus -->
## TOPIC 00012: Delete Node VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `delete-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/delete-node-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit Deletes a node, such as a folder, item, notifier, or condition. When you delete a folder, an item, or a notifier, you delete all the child nodes. After you start an OPC UA server, you cannot delete nodes until the OPC UA server stops. Use th

### Delete Node VI

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit

Deletes a node, such as a folder, item, notifier, or condition. When you delete a folder, an item, or a notifier, you delete all the child nodes.

After you start an OPC UA server, you cannot delete nodes until the OPC UA server stops. Use the Stop VI to stop an OPC UA server.

Example

[IMAGE alt='image' src='images/opcua_delete_node.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Delete Node VI.

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=delete-subscriptions-vi.html language=enus -->
## TOPIC 00013: Delete Subscriptions VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `delete-subscriptions-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/delete-subscriptions-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Deletes one or multiple subscriptions. By deleting a subscription, you delete all the monitored nodes from the subscription. Example OPC UA client refnum in specifies the reference for the OPC UA client. subscription IDs specifies the subscr

### Delete Subscriptions VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Deletes one or multiple subscriptions. By deleting a subscription, you delete all the monitored nodes from the subscription.

Example

[IMAGE alt='image' src='images/opcua_delete_subscriptions.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | subscription IDs specifies the subscriptions to delete. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Delete Subscriptions VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=dialog-condition-properties.html language=enus -->
## TOPIC 00014: Dialog Condition Properties

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `dialog-condition-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/dialog-condition-properties.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The dialog is a condition that a server uses to request user input. Wire the OPC UA dialog condition refnum out output of the Dialog Condition instance of the Add Condition VI to the reference input of a standard Property Node to get a Dialog Condition Property Node. This Property Node has the follo

### Dialog Condition Properties

The dialog is a condition that a server uses to request user input. Wire the **OPC UA dialog condition refnum out** output of the Dialog Condition instance of the Add Condition VI to the **reference** input of a standard Property Node to get a Dialog Condition Property Node. This Property Node has the following properties:

| Property | Description |
| --- | --- |
| Dialog State | Whether a dialog is active and waiting for a response. Details |
| Enabled State | Whether a condition is in the enabled state. Details |
| Prompt | A dialog prompt to display to the end user. Details |
| Retain | Whether an OPC UA client synchronizes the condition state with that of the server. Details |

Parent topic:

OPC UA Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=dialog-state-property.html language=enus -->
## TOPIC 00015: Dialog State Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `dialog-state-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/dialog-state-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Dialog Condition Properties Whether a dialog is active and waiting for a response. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Dialog State Property

**Requires:** OPC UA Toolkit

**Class:** [Dialog Condition Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_dialogcondition_prop)

Whether a dialog is active and waiting for a response.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Dialog Condition Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=disable-condition-vi.html language=enus -->
## TOPIC 00016: Disable Condition VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `disable-condition-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/disable-condition-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Alarms and Conditions VIs Requires: OPC UA Toolkit Moves a condition to disabled state. Example OPC UA client refnum in specifies the reference for the OPC UA client. condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifi

### Disable Condition VI

**Owning Palette:** Alarms and Conditions VIs

**Requires:** OPC UA Toolkit

Moves a condition to disabled state.

Example

[IMAGE alt='image' src='images/Disable_Condition.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Disable Condition VI.

Parent topic:

Alarms and Conditions VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=disconnect-vi.html language=enus -->
## TOPIC 00017: Disconnect VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `disconnect-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/disconnect-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Disconnects an OPC UA client from an OPC UA server. The OPC UA client automatically deletes all the subscriptions before disconnecting from the OPC UA server. Example OPC UA client refnum in specifies the reference for the OPC UA client. err

### Disconnect VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Disconnects an OPC UA client from an OPC UA server. The OPC UA client automatically deletes all the subscriptions before disconnecting from the OPC UA server.

Example

[IMAGE alt='image' src='images/opcua_disconnect.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Disconnect VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=enable-condition-vi.html language=enus -->
## TOPIC 00018: Enable Condition VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `enable-condition-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/enable-condition-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Alarms and Conditions VIs Requires: OPC UA Toolkit Moves a condition to enabled state. Example OPC UA client refnum in specifies the reference for the OPC UA client. condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifie

### Enable Condition VI

**Owning Palette:** Alarms and Conditions VIs

**Requires:** OPC UA Toolkit

Moves a condition to enabled state.

Example

[IMAGE alt='image' src='images/Enable_Condition.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Enable Condition VI.

Parent topic:

Alarms and Conditions VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=enabled-state-property.html language=enus -->
## TOPIC 00019: Enabled State Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `enabled-state-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/enabled-state-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties Whether a condition is in the enabled state. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Enabled State Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

Whether a condition is in the enabled state.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Dialog Condition Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=enabled-state-property_2.html language=enus -->
## TOPIC 00020: Enabled State Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `enabled-state-property_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/enabled-state-property_2.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties Whether a condition is in the enabled state. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Enabled State Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

Whether a condition is in the enabled state.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Limit Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=enabled-state-property_3.html language=enus -->
## TOPIC 00021: Enabled State Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `enabled-state-property_3.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/enabled-state-property_3.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties Whether a condition is in the enabled state. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Enabled State Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

Whether a condition is in the enabled state.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Off-Normal Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=forward-browse-vi.html language=enus -->
## TOPIC 00022: Forward Browse VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `forward-browse-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/forward-browse-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Browses a node and returns information about its child nodes. Example OPC UA client refnum in specifies the reference for the OPC UA client. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier

### Forward Browse VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Browses a node and returns information about its child nodes.

Example

[IMAGE alt='image' src='images/opcua_browse.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | browse result returns information about child nodes. reference type returns the type of the reference. 0Unspecified35Organizes36Has Event Source45Has Subtype46Has Property47Has Component48Has Notifier49Has Ordered Component node ID returns the ID of the child node. browse name returns the name of the child node. node class returns the node class. 0Unspecified1Object2Variable4Method8Object Type16Variable Type32Reference Type64Data Type128View node type returns the type of the child node. 0 Unspecified 24 BaseDataType 58 BaseObjectType 61 FolderType 62 BaseVariableType 63 BaseDataVariableType 68 PropertyType 69 DataTypeDescriptionType 72 DataTypeDictionaryType 75 DataTypeSystemType 76 DataTypeEncodingType 77 ModellingRuleType 120 NamingRuleType 256 IdType 303 UserTokenType 307 ApplicationType 315 SecurityTokenRequestType 398 EnumeratedTestType 399 ScalarTestType 402 ArrayTestType 405 CompositeTestType 718 DeadbandType 853 RedundantServerDataType 856 SamplingIntervalDiagnosticsDataType 859 ServerDiagnosticsSummaryDataType 862 ServerStatusDataType 865 SessionDiagnosticsDataType 868 SessionSecurityDiagnosticsDataType 871 ServiceCounterDataType 874 SubscriptionDiagnosticsDataType 877 ModelChangeStructureDataType 894 ProgramDiagnosticDataType 897 SemanticChangeStructureDataType 2004 ServerType 2013 ServerCapabilitiesType 2020 ServerDiagnosticsType 2026 SessionsDiagnosticsSummaryType 2029 SessionDiagnosticsObjectType 2033 VendorServerInfoType 2034 ServerRedundancyType 2036 TransparentRedundancyType 2039 NonTransparentRedundancyType 2041 BaseEventType 2052 AuditEventType 2058 AuditSecurityEventType 2059 AuditChannelEventType 2060 AuditOpenSecureChannelEventType 2069 AuditSessionEventType 2071 AuditCreateSessionEventType 2075 AuditActivateSessionEventType 2078 AuditCancelEventType 2080 AuditCertificateEventType 2082 AuditCertificateDataMismatchEventType 2085 AuditCertificateExpiredEventType 2086 AuditCertificateInvalidEventType 2087 AuditCertificateUntrustedEventType 2088 AuditCertificateRevokedEventType 2089 AuditCertificateMismatchEventType 2090 AuditNodeManagementEventType 2091 AuditAddNodesEventType 2093 AuditDeleteNodesEventType 2095 AuditAddReferencesEventType 2097 AuditDeleteReferencesEventType 2099 AuditUpdateEventType 2100 AuditWriteUpdateEventType 2104 AuditHistoryUpdateEventType 2127 AuditUpdateMethodEventType 2130 SystemEventType 2131 DeviceFailureEventType 2132 BaseModelChangeEventType 2133 GeneralModelChangeEventType 2137 ServerVendorCapabilityType 2138 ServerStatusType 2150 ServerDiagnosticsSummaryType 2164 SamplingIntervalDiagnosticsArrayType 2165 SamplingIntervalDiagnosticsType 2171 SubscriptionDiagnosticsArrayType 2172 SubscriptionDiagnosticsType 2196 SessionDiagnosticsArrayType 2197 SessionDiagnosticsVariableType 2243 SessionSecurityDiagnosticsArrayType 2244 SessionSecurityDiagnosticsType 2299 StateMachineType 2307 StateType 2309 InitialStateType 2310 TransitionType 2311 TransitionEventType 2315 AuditUpdateStateEventType 2318 HistoricalDataConfigurationType 2330 HistoryServerCapabilitiesType 2340 AggregateFunctionType 2365 DataItemType 2368 AnalogItemType 2372 DiscreteItemType 2373 TwoStateDiscreteType 2376 MultiStateDiscreteType 2378 ProgramTransitionEventType 2380 ProgramDiagnosticType 2391 ProgramStateMachineType 2738 SemanticChangeEventType 2748 AuditUrlMismatchEventType 2755 StateVariableType 2760 FiniteStateVariableType 2762 TransitionVariableType 2767 FiniteTransitionVariableType 2771 FiniteStateMachineType 2782 ConditionType 2787 RefreshStartEventType 2788 RefreshEndEventType 2789 RefreshRequiredEventType 2790 AuditConditionEventType 2803 AuditConditionEnableEventType 2829 AuditConditionCommentEventType 2830 DialogConditionType 2881 AcknowledgeableConditionType 2915 AlarmConditionType 2929 ShelvedStateMachineType 2955 LimitAlarmType 2999 AuditHistoryEventUpdateEventType 3006 AuditHistoryValueUpdateEventType 3012 AuditHistoryDeleteEventType 3014 AuditHistoryRawModifyDeleteEventType 3019 AuditHistoryAtTimeDeleteEventType 3022 AuditHistoryEventDeleteEventType 3035 EventQueueOverflowEventType 3051 BuildInfoType 3806 ProgramTransitionAuditEventType 7594 EnumValueType 8912 TimeZoneDataType 8921 LockType 8927 AuditConditionRespondEventType 8944 AuditConditionAcknowledgeEventType 8961 AuditConditionConfirmEventType 8995 TwoStateVariableType 9002 ConditionVariableType 9318 ExclusiveLimitStateMachineType 9341 ExclusiveLimitAlarmType 9482 ExclusiveLevelAlarmType 9623 ExclusiveRateOfChangeAlarmType 9764 ExclusiveDeviationAlarmType 9906 NonExclusiveLimitAlarmType 10060 NonExclusiveLevelAlarmType 10214 NonExclusiveRateOfChangeAlarmType 10368 NonExclusiveDeviationAlarmType 10523 DiscreteAlarmType 10637 OffNormalAlarmType 10751 TripAlarmType 11093 AuditConditionShelvingEventType 11163 BaseConditionClassType 11164 ProcessConditionClassType 11165 MaintenanceConditionClassType 11166 SystemConditionClassType 11187 AggregateConfigurationType 11234 HistoryUpdateType 11238 MultiStateValueDiscreteType 11293 PerformUpdateType 11436 ProgressEventType 11446 SystemStatusChangeEventType 11487 OptionSetType 11564 OperationLimitsType 11575 FileType 11595 AddressSpaceFileType 11616 NamespaceMetadataType 11645 NamespacesType 11737 BitFieldMaskDataType 11753 SystemOffNormalAlarmType 11856 AuditProgramTransitionEventType 11943 EndpointUrlListDataType 11944 NetworkGroupDataType 11945 NonTransparentNetworkRedundancyType 12021 ArrayItemType 12029 YArrayItemType 12038 XYArrayItemType 12047 ImageItemType 12057 CubeItemType 12068 NDimensionArrayItemType 12080 XVType 12171 ComplexNumberType 12172 DoubleComplexNumberType 12522 TrustListType 12554 TrustListDataType 12555 CertificateGroupType 12556 CertificateType 12557 ApplicationCertificateType 12558 HttpsCertificateType 12559 RsaMinApplicationCertificateType 12560 RsaSha256ApplicationCertificateType 12561 TrustListUpdatedAuditEventType 12581 ServerConfigurationType 12620 CertificateUpdatedAuditEventType 13225 CertificateExpirationAlarmType 13353 FileDirectoryType 13813 CertificateGroupFolderType |
|  | reference type returns the type of the reference. 0Unspecified35Organizes36Has Event Source45Has Subtype46Has Property47Has Component48Has Notifier49Has Ordered Component |
| 0 | Unspecified |
| 35 | Organizes |
| 36 | Has Event Source |
| 45 | Has Subtype |
| 46 | Has Property |
| 47 | Has Component |
| 48 | Has Notifier |
| 49 | Has Ordered Component |
|  | node ID returns the ID of the child node. |
|  | browse name returns the name of the child node. |
|  | node class returns the node class. 0Unspecified1Object2Variable4Method8Object Type16Variable Type32Reference Type64Data Type128View |
| 0 | Unspecified |
| 1 | Object |
| 2 | Variable |
| 4 | Method |
| 8 | Object Type |
| 16 | Variable Type |
| 32 | Reference Type |
| 64 | Data Type |
| 128 | View |
|  | node type returns the type of the child node. 0 Unspecified 24 BaseDataType 58 BaseObjectType 61 FolderType 62 BaseVariableType 63 BaseDataVariableType 68 PropertyType 69 DataTypeDescriptionType 72 DataTypeDictionaryType 75 DataTypeSystemType 76 DataTypeEncodingType 77 ModellingRuleType 120 NamingRuleType 256 IdType 303 UserTokenType 307 ApplicationType 315 SecurityTokenRequestType 398 EnumeratedTestType 399 ScalarTestType 402 ArrayTestType 405 CompositeTestType 718 DeadbandType 853 RedundantServerDataType 856 SamplingIntervalDiagnosticsDataType 859 ServerDiagnosticsSummaryDataType 862 ServerStatusDataType 865 SessionDiagnosticsDataType 868 SessionSecurityDiagnosticsDataType 871 ServiceCounterDataType 874 SubscriptionDiagnosticsDataType 877 ModelChangeStructureDataType 894 ProgramDiagnosticDataType 897 SemanticChangeStructureDataType 2004 ServerType 2013 ServerCapabilitiesType 2020 ServerDiagnosticsType 2026 SessionsDiagnosticsSummaryType 2029 SessionDiagnosticsObjectType 2033 VendorServerInfoType 2034 ServerRedundancyType 2036 TransparentRedundancyType 2039 NonTransparentRedundancyType 2041 BaseEventType 2052 AuditEventType 2058 AuditSecurityEventType 2059 AuditChannelEventType 2060 AuditOpenSecureChannelEventType 2069 AuditSessionEventType 2071 AuditCreateSessionEventType 2075 AuditActivateSessionEventType 2078 AuditCancelEventType 2080 AuditCertificateEventType 2082 AuditCertificateDataMismatchEventType 2085 AuditCertificateExpiredEventType 2086 AuditCertificateInvalidEventType 2087 AuditCertificateUntrustedEventType 2088 AuditCertificateRevokedEventType 2089 AuditCertificateMismatchEventType 2090 AuditNodeManagementEventType 2091 AuditAddNodesEventType 2093 AuditDeleteNodesEventType 2095 AuditAddReferencesEventType 2097 AuditDeleteReferencesEventType 2099 AuditUpdateEventType 2100 AuditWriteUpdateEventType 2104 AuditHistoryUpdateEventType 2127 AuditUpdateMethodEventType 2130 SystemEventType 2131 DeviceFailureEventType 2132 BaseModelChangeEventType 2133 GeneralModelChangeEventType 2137 ServerVendorCapabilityType 2138 ServerStatusType 2150 ServerDiagnosticsSummaryType 2164 SamplingIntervalDiagnosticsArrayType 2165 SamplingIntervalDiagnosticsType 2171 SubscriptionDiagnosticsArrayType 2172 SubscriptionDiagnosticsType 2196 SessionDiagnosticsArrayType 2197 SessionDiagnosticsVariableType 2243 SessionSecurityDiagnosticsArrayType 2244 SessionSecurityDiagnosticsType 2299 StateMachineType 2307 StateType 2309 InitialStateType 2310 TransitionType 2311 TransitionEventType 2315 AuditUpdateStateEventType 2318 HistoricalDataConfigurationType 2330 HistoryServerCapabilitiesType 2340 AggregateFunctionType 2365 DataItemType 2368 AnalogItemType 2372 DiscreteItemType 2373 TwoStateDiscreteType 2376 MultiStateDiscreteType 2378 ProgramTransitionEventType 2380 ProgramDiagnosticType 2391 ProgramStateMachineType 2738 SemanticChangeEventType 2748 AuditUrlMismatchEventType 2755 StateVariableType 2760 FiniteStateVariableType 2762 TransitionVariableType 2767 FiniteTransitionVariableType 2771 FiniteStateMachineType 2782 ConditionType 2787 RefreshStartEventType 2788 RefreshEndEventType 2789 RefreshRequiredEventType 2790 AuditConditionEventType 2803 AuditConditionEnableEventType 2829 AuditConditionCommentEventType 2830 DialogConditionType 2881 AcknowledgeableConditionType 2915 AlarmConditionType 2929 ShelvedStateMachineType 2955 LimitAlarmType 2999 AuditHistoryEventUpdateEventType 3006 AuditHistoryValueUpdateEventType 3012 AuditHistoryDeleteEventType 3014 AuditHistoryRawModifyDeleteEventType 3019 AuditHistoryAtTimeDeleteEventType 3022 AuditHistoryEventDeleteEventType 3035 EventQueueOverflowEventType 3051 BuildInfoType 3806 ProgramTransitionAuditEventType 7594 EnumValueType 8912 TimeZoneDataType 8921 LockType 8927 AuditConditionRespondEventType 8944 AuditConditionAcknowledgeEventType 8961 AuditConditionConfirmEventType 8995 TwoStateVariableType 9002 ConditionVariableType 9318 ExclusiveLimitStateMachineType 9341 ExclusiveLimitAlarmType 9482 ExclusiveLevelAlarmType 9623 ExclusiveRateOfChangeAlarmType 9764 ExclusiveDeviationAlarmType 9906 NonExclusiveLimitAlarmType 10060 NonExclusiveLevelAlarmType 10214 NonExclusiveRateOfChangeAlarmType 10368 NonExclusiveDeviationAlarmType 10523 DiscreteAlarmType 10637 OffNormalAlarmType 10751 TripAlarmType 11093 AuditConditionShelvingEventType 11163 BaseConditionClassType 11164 ProcessConditionClassType 11165 MaintenanceConditionClassType 11166 SystemConditionClassType 11187 AggregateConfigurationType 11234 HistoryUpdateType 11238 MultiStateValueDiscreteType 11293 PerformUpdateType 11436 ProgressEventType 11446 SystemStatusChangeEventType 11487 OptionSetType 11564 OperationLimitsType 11575 FileType 11595 AddressSpaceFileType 11616 NamespaceMetadataType 11645 NamespacesType 11737 BitFieldMaskDataType 11753 SystemOffNormalAlarmType 11856 AuditProgramTransitionEventType 11943 EndpointUrlListDataType 11944 NetworkGroupDataType 11945 NonTransparentNetworkRedundancyType 12021 ArrayItemType 12029 YArrayItemType 12038 XYArrayItemType 12047 ImageItemType 12057 CubeItemType 12068 NDimensionArrayItemType 12080 XVType 12171 ComplexNumberType 12172 DoubleComplexNumberType 12522 TrustListType 12554 TrustListDataType 12555 CertificateGroupType 12556 CertificateType 12557 ApplicationCertificateType 12558 HttpsCertificateType 12559 RsaMinApplicationCertificateType 12560 RsaSha256ApplicationCertificateType 12561 TrustListUpdatedAuditEventType 12581 ServerConfigurationType 12620 CertificateUpdatedAuditEventType 13225 CertificateExpirationAlarmType 13353 FileDirectoryType 13813 CertificateGroupFolderType |
| 0 | Unspecified |
| 24 | BaseDataType |
| 58 | BaseObjectType |
| 61 | FolderType |
| 62 | BaseVariableType |
| 63 | BaseDataVariableType |
| 68 | PropertyType |
| 69 | DataTypeDescriptionType |
| 72 | DataTypeDictionaryType |
| 75 | DataTypeSystemType |
| 76 | DataTypeEncodingType |
| 77 | ModellingRuleType |
| 120 | NamingRuleType |
| 256 | IdType |
| 303 | UserTokenType |
| 307 | ApplicationType |
| 315 | SecurityTokenRequestType |
| 398 | EnumeratedTestType |
| 399 | ScalarTestType |
| 402 | ArrayTestType |
| 405 | CompositeTestType |
| 718 | DeadbandType |
| 853 | RedundantServerDataType |
| 856 | SamplingIntervalDiagnosticsDataType |
| 859 | ServerDiagnosticsSummaryDataType |
| 862 | ServerStatusDataType |
| 865 | SessionDiagnosticsDataType |
| 868 | SessionSecurityDiagnosticsDataType |
| 871 | ServiceCounterDataType |
| 874 | SubscriptionDiagnosticsDataType |
| 877 | ModelChangeStructureDataType |
| 894 | ProgramDiagnosticDataType |
| 897 | SemanticChangeStructureDataType |
| 2004 | ServerType |
| 2013 | ServerCapabilitiesType |
| 2020 | ServerDiagnosticsType |
| 2026 | SessionsDiagnosticsSummaryType |
| 2029 | SessionDiagnosticsObjectType |
| 2033 | VendorServerInfoType |
| 2034 | ServerRedundancyType |
| 2036 | TransparentRedundancyType |
| 2039 | NonTransparentRedundancyType |
| 2041 | BaseEventType |
| 2052 | AuditEventType |
| 2058 | AuditSecurityEventType |
| 2059 | AuditChannelEventType |
| 2060 | AuditOpenSecureChannelEventType |
| 2069 | AuditSessionEventType |
| 2071 | AuditCreateSessionEventType |
| 2075 | AuditActivateSessionEventType |
| 2078 | AuditCancelEventType |
| 2080 | AuditCertificateEventType |
| 2082 | AuditCertificateDataMismatchEventType |
| 2085 | AuditCertificateExpiredEventType |
| 2086 | AuditCertificateInvalidEventType |
| 2087 | AuditCertificateUntrustedEventType |
| 2088 | AuditCertificateRevokedEventType |
| 2089 | AuditCertificateMismatchEventType |
| 2090 | AuditNodeManagementEventType |
| 2091 | AuditAddNodesEventType |
| 2093 | AuditDeleteNodesEventType |
| 2095 | AuditAddReferencesEventType |
| 2097 | AuditDeleteReferencesEventType |
| 2099 | AuditUpdateEventType |
| 2100 | AuditWriteUpdateEventType |
| 2104 | AuditHistoryUpdateEventType |
| 2127 | AuditUpdateMethodEventType |
| 2130 | SystemEventType |
| 2131 | DeviceFailureEventType |
| 2132 | BaseModelChangeEventType |
| 2133 | GeneralModelChangeEventType |
| 2137 | ServerVendorCapabilityType |
| 2138 | ServerStatusType |
| 2150 | ServerDiagnosticsSummaryType |
| 2164 | SamplingIntervalDiagnosticsArrayType |
| 2165 | SamplingIntervalDiagnosticsType |
| 2171 | SubscriptionDiagnosticsArrayType |
| 2172 | SubscriptionDiagnosticsType |
| 2196 | SessionDiagnosticsArrayType |
| 2197 | SessionDiagnosticsVariableType |
| 2243 | SessionSecurityDiagnosticsArrayType |
| 2244 | SessionSecurityDiagnosticsType |
| 2299 | StateMachineType |
| 2307 | StateType |
| 2309 | InitialStateType |
| 2310 | TransitionType |
| 2311 | TransitionEventType |
| 2315 | AuditUpdateStateEventType |
| 2318 | HistoricalDataConfigurationType |
| 2330 | HistoryServerCapabilitiesType |
| 2340 | AggregateFunctionType |
| 2365 | DataItemType |
| 2368 | AnalogItemType |
| 2372 | DiscreteItemType |
| 2373 | TwoStateDiscreteType |
| 2376 | MultiStateDiscreteType |
| 2378 | ProgramTransitionEventType |
| 2380 | ProgramDiagnosticType |
| 2391 | ProgramStateMachineType |
| 2738 | SemanticChangeEventType |
| 2748 | AuditUrlMismatchEventType |
| 2755 | StateVariableType |
| 2760 | FiniteStateVariableType |
| 2762 | TransitionVariableType |
| 2767 | FiniteTransitionVariableType |
| 2771 | FiniteStateMachineType |
| 2782 | ConditionType |
| 2787 | RefreshStartEventType |
| 2788 | RefreshEndEventType |
| 2789 | RefreshRequiredEventType |
| 2790 | AuditConditionEventType |
| 2803 | AuditConditionEnableEventType |
| 2829 | AuditConditionCommentEventType |
| 2830 | DialogConditionType |
| 2881 | AcknowledgeableConditionType |
| 2915 | AlarmConditionType |
| 2929 | ShelvedStateMachineType |
| 2955 | LimitAlarmType |
| 2999 | AuditHistoryEventUpdateEventType |
| 3006 | AuditHistoryValueUpdateEventType |
| 3012 | AuditHistoryDeleteEventType |
| 3014 | AuditHistoryRawModifyDeleteEventType |
| 3019 | AuditHistoryAtTimeDeleteEventType |
| 3022 | AuditHistoryEventDeleteEventType |
| 3035 | EventQueueOverflowEventType |
| 3051 | BuildInfoType |
| 3806 | ProgramTransitionAuditEventType |
| 7594 | EnumValueType |
| 8912 | TimeZoneDataType |
| 8921 | LockType |
| 8927 | AuditConditionRespondEventType |
| 8944 | AuditConditionAcknowledgeEventType |
| 8961 | AuditConditionConfirmEventType |
| 8995 | TwoStateVariableType |
| 9002 | ConditionVariableType |
| 9318 | ExclusiveLimitStateMachineType |
| 9341 | ExclusiveLimitAlarmType |
| 9482 | ExclusiveLevelAlarmType |
| 9623 | ExclusiveRateOfChangeAlarmType |
| 9764 | ExclusiveDeviationAlarmType |
| 9906 | NonExclusiveLimitAlarmType |
| 10060 | NonExclusiveLevelAlarmType |
| 10214 | NonExclusiveRateOfChangeAlarmType |
| 10368 | NonExclusiveDeviationAlarmType |
| 10523 | DiscreteAlarmType |
| 10637 | OffNormalAlarmType |
| 10751 | TripAlarmType |
| 11093 | AuditConditionShelvingEventType |
| 11163 | BaseConditionClassType |
| 11164 | ProcessConditionClassType |
| 11165 | MaintenanceConditionClassType |
| 11166 | SystemConditionClassType |
| 11187 | AggregateConfigurationType |
| 11234 | HistoryUpdateType |
| 11238 | MultiStateValueDiscreteType |
| 11293 | PerformUpdateType |
| 11436 | ProgressEventType |
| 11446 | SystemStatusChangeEventType |
| 11487 | OptionSetType |
| 11564 | OperationLimitsType |
| 11575 | FileType |
| 11595 | AddressSpaceFileType |
| 11616 | NamespaceMetadataType |
| 11645 | NamespacesType |
| 11737 | BitFieldMaskDataType |
| 11753 | SystemOffNormalAlarmType |
| 11856 | AuditProgramTransitionEventType |
| 11943 | EndpointUrlListDataType |
| 11944 | NetworkGroupDataType |
| 11945 | NonTransparentNetworkRedundancyType |
| 12021 | ArrayItemType |
| 12029 | YArrayItemType |
| 12038 | XYArrayItemType |
| 12047 | ImageItemType |
| 12057 | CubeItemType |
| 12068 | NDimensionArrayItemType |
| 12080 | XVType |
| 12171 | ComplexNumberType |
| 12172 | DoubleComplexNumberType |
| 12522 | TrustListType |
| 12554 | TrustListDataType |
| 12555 | CertificateGroupType |
| 12556 | CertificateType |
| 12557 | ApplicationCertificateType |
| 12558 | HttpsCertificateType |
| 12559 | RsaMinApplicationCertificateType |
| 12560 | RsaSha256ApplicationCertificateType |
| 12561 | TrustListUpdatedAuditEventType |
| 12581 | ServerConfigurationType |
| 12620 | CertificateUpdatedAuditEventType |
| 13225 | CertificateExpirationAlarmType |
| 13353 | FileDirectoryType |
| 13813 | CertificateGroupFolderType |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Forward Browse VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=get-node-attribute-vi.html language=enus -->
## TOPIC 00023: Get Node Attribute VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `get-node-attribute-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/get-node-attribute-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Gets the attributes of a node. Example OPC UA client refnum in specifies the reference for the OPC UA client. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID c

### Get Node Attribute VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Gets the attributes of a node.

Example

[IMAGE alt='image' src='images/opcua_get_node_attribute.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | node attribute returns the attributes of the node. name returns the name of the node. node class returns the node class. 0Unspecified1Object2Variable4Method8Object Type16Variable Type32Reference Type64Data Type128View data type returns the data type of the node. Value Data Type 1 Boolean 2 SByte 3 Byte 4 Int16 5 UInt16 6 Int32 7 UInt32 8 Int64 9 UInt64 10 Float 11 Double 12 String 13 DateTime 15 ByteString 101 Array of Boolean 102 Array of SByte 103 Array of Byte 104 Array of Int16 105 Array of UInt16 106 Array of Int32 107 Array of UInt32 108 Array of Int64 109 Array of UInt64 110 Array of Float 111 Array of Double 112 Array of String 113 Array of DateTime 115 Array of ByteString 201 Matrix of Boolean 202 Matrix of SByte 203 Matrix of Byte 204 Matrix of Int16 205 Matrix of UInt16 206 Matrix of Int32 207 Matrix of UInt32 208 Matrix of Int64 209 Matrix of UInt64 210 Matrix of Float 211 Matrix of Double 212 Matrix of String 213 Matrix of DateTime 215 Matrix of ByteString access returns the access level of the node. Digital Display Access 0 Null 1 Read 2 Write 3 Read&Write description returns the description of the node. |
|  | name returns the name of the node. |
|  | node class returns the node class. 0Unspecified1Object2Variable4Method8Object Type16Variable Type32Reference Type64Data Type128View |
| 0 | Unspecified |
| 1 | Object |
| 2 | Variable |
| 4 | Method |
| 8 | Object Type |
| 16 | Variable Type |
| 32 | Reference Type |
| 64 | Data Type |
| 128 | View |
|  | data type returns the data type of the node. Value Data Type 1 Boolean 2 SByte 3 Byte 4 Int16 5 UInt16 6 Int32 7 UInt32 8 Int64 9 UInt64 10 Float 11 Double 12 String 13 DateTime 15 ByteString 101 Array of Boolean 102 Array of SByte 103 Array of Byte 104 Array of Int16 105 Array of UInt16 106 Array of Int32 107 Array of UInt32 108 Array of Int64 109 Array of UInt64 110 Array of Float 111 Array of Double 112 Array of String 113 Array of DateTime 115 Array of ByteString 201 Matrix of Boolean 202 Matrix of SByte 203 Matrix of Byte 204 Matrix of Int16 205 Matrix of UInt16 206 Matrix of Int32 207 Matrix of UInt32 208 Matrix of Int64 209 Matrix of UInt64 210 Matrix of Float 211 Matrix of Double 212 Matrix of String 213 Matrix of DateTime 215 Matrix of ByteString |
| Value | Data Type |
| 1 | Boolean |
| 2 | SByte |
| 3 | Byte |
| 4 | Int16 |
| 5 | UInt16 |
| 6 | Int32 |
| 7 | UInt32 |
| 8 | Int64 |
| 9 | UInt64 |
| 10 | Float |
| 11 | Double |
| 12 | String |
| 13 | DateTime |
| 15 | ByteString |
| 101 | Array of Boolean |
| 102 | Array of SByte |
| 103 | Array of Byte |
| 104 | Array of Int16 |
| 105 | Array of UInt16 |
| 106 | Array of Int32 |
| 107 | Array of UInt32 |
| 108 | Array of Int64 |
| 109 | Array of UInt64 |
| 110 | Array of Float |
| 111 | Array of Double |
| 112 | Array of String |
| 113 | Array of DateTime |
| 115 | Array of ByteString |
| 201 | Matrix of Boolean |
| 202 | Matrix of SByte |
| 203 | Matrix of Byte |
| 204 | Matrix of Int16 |
| 205 | Matrix of UInt16 |
| 206 | Matrix of Int32 |
| 207 | Matrix of UInt32 |
| 208 | Matrix of Int64 |
| 209 | Matrix of UInt64 |
| 210 | Matrix of Float |
| 211 | Matrix of Double |
| 212 | Matrix of String |
| 213 | Matrix of DateTime |
| 215 | Matrix of ByteString |
|  | access returns the access level of the node. Digital Display Access 0 Null 1 Read 2 Write 3 Read&Write |
| Digital Display | Access |
| 0 | Null |
| 1 | Read |
| 2 | Write |
| 3 | Read&Write |
|  | description returns the description of the node. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Get Node Attribute VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-access-vis.html language=enus -->
## TOPIC 00024: Historical Access VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-access-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-access-vis.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the Historical Access VIs to access historical data and events for OPC UA client applications. Example

### Historical Access VIs

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Historical Access VIs to access historical data and events for OPC UA client applications.

Example

| Palette Object | Description |
| --- | --- |
| History Data Multiple Read | Reads history data for one or multiple nodes. |
| History Event Multiple Read | Reads one or multiple history events. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Historical Access VIs.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-access-vis2.html language=enus -->
## TOPIC 00025: Historical Access VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-access-vis2.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-access-vis2.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the Historical Access VIs to access historical data and events for OPC UA server applications. Example

### Historical Access VIs

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Historical Access VIs to access historical data and events for OPC UA server applications.

Example

| Palette Object | Description |
| --- | --- |
| History Data Delete | Deletes history data within a time range. |
| History Data Delete at Time | Deletes history data at specific timestamps. |
| History Data Read | Reads history data within a time range. |
| History Data Update | Updates history data at a specific timestamp. |
| History Event Delete | Deletes a history event. |
| History Event Read | Reads a notifier. A notifier node enables an OPC UA client, which subscribes to the node, to receive event notifications. |
| History Event Update | Updates a history event. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Historical Access VIs.

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-data-access-property.html language=enus -->
## TOPIC 00026: Historical Data Access Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-data-access-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-data-access-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Variable Node Properties Whether historical data access is available. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Historical Data Access Property

**Requires:** OPC UA Toolkit

**Class:** [Variable Node Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_node_prop)

Whether historical data access is available.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Variable Node Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-data-queue-size-property.html language=enus -->
## TOPIC 00027: Historical Data Queue Size Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-data-queue-size-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-data-queue-size-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Variable Node Properties The size of a historical data queue. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Read-only Data Type Default Value 1000 The default value i

### Historical Data Queue Size Property

**Requires:** OPC UA Toolkit

**Class:** [Variable Node Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_node_prop)

The size of a historical data queue.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |
| Default Value | 1000 |

Note

The default value is 1000 only if Historical Data Access is True.

Parent topic:

Variable Node Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-event-access-property.html language=enus -->
## TOPIC 00028: Historical Event Access Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-event-access-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-event-access-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Notifier Properties Whether historical event access is available. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read-only Permissions After Server Starts Read-only Data Type

### Historical Event Access Property

**Requires:** OPC UA Toolkit

**Class:** [Notifier Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_notifier_prop)

Whether historical event access is available.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read-only |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Notifier Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=historical-event-queue-size-property.html language=enus -->
## TOPIC 00029: Historical Event Queue Size Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `historical-event-queue-size-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/historical-event-queue-size-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Notifier Properties The size of a historical event queue. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Read-only Data Type Default Value 1000 The default value is 10

### Historical Event Queue Size Property

**Requires:** OPC UA Toolkit

**Class:** [Notifier Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_notifier_prop)

The size of a historical event queue.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |
| Default Value | 1000 |

Note

The default value is 1000 only if Historical Event Access is True.

Parent topic:

Notifier Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-data-delete-at-time-vi.html language=enus -->
## TOPIC 00030: History Data Delete at Time VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-data-delete-at-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-data-delete-at-time-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Deletes history data at specific timestamps. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier typ

### History Data Delete at Time VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Deletes history data at specific timestamps.

Example

[IMAGE alt='image' src='images/History_Data_Delete_At_Time_Server.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | timestamps specifies the timestamps at which this VI deletes history data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | operation status returns the status of the operation. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Data Delete at Time VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-data-delete-vi.html language=enus -->
## TOPIC 00031: History Data Delete VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-data-delete-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-data-delete-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Deletes history data within a time range. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=

### History Data Delete VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Deletes history data within a time range.

Example

[IMAGE alt='image' src='images/History_Data_Delete_Server.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies the start time and the end time that this VI deletes history data. start time specifies the timestamp at which this VI deletes the first history data. end time specifies the timestamp at which this VI deletes the last history data. |
|  | start time specifies the timestamp at which this VI deletes the first history data. |
|  | end time specifies the timestamp at which this VI deletes the last history data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Data Delete VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-data-multiple-read-vi.html language=enus -->
## TOPIC 00032: History Data Multiple Read VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-data-multiple-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-data-multiple-read-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Reads history data for one or multiple nodes. Example continuation points in specifies the continuation point and whether the history data has a continuation point. continuation point specifies the point from which this VI continues to r

### History Data Multiple Read VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Reads history data for one or multiple nodes.

Example

[IMAGE alt='image' src='images/History_Data_Multiple_Read_Raw_Client.gif']

|  | continuation points in specifies the continuation point and whether the history data has a continuation point. continuation point specifies the point from which this VI continues to read if the OPC UA server cannot return all values in one response. has continuation point? specifies whether the history data has a continuation point. The default is TRUE, which specifies that the history data has a continuation point. |
| --- | --- |
|  | continuation point specifies the point from which this VI continues to read if the OPC UA server cannot return all values in one response. |
|  | has continuation point? specifies whether the history data has a continuation point. The default is TRUE, which specifies that the history data has a continuation point. |
|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies the start time, the end time, the maximum number of values to return over the time range, and whether to return bounding values. start time specifies the timestamp at which this VI reads the first history data. end time specifies the timestamp at which this VI reads the last history data. num values per node specifies the maximum number of values to return over the time range. The default is 0, which specifies that this VI returns all values over the time range. return bounds specifies whether to return bounding values. The default is FALSE, which specifies that this VI does not return bounding values. Bounding values are values associated with the starting time and the ending time. An OPC UA client can require bounding values to determine the starting and ending values when requesting data over a time range. |
|  | start time specifies the timestamp at which this VI reads the first history data. |
|  | end time specifies the timestamp at which this VI reads the last history data. |
|  | num values per node specifies the maximum number of values to return over the time range. The default is 0, which specifies that this VI returns all values over the time range. |
|  | return bounds specifies whether to return bounding values. The default is FALSE, which specifies that this VI does not return bounding values. Bounding values are values associated with the starting time and the ending time. An OPC UA client can require bounding values to determine the starting and ending values when requesting data over a time range. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time that this VI waits to get a response from the OPC UA Server. The default value is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the history data, and the statuses of the nodes. node ID returns the ID of the node. history data returns history data that this VI reads. value returns the history data. timestamp returns the timestamp at which data is generated. node status returns the status of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | history data returns history data that this VI reads. value returns the history data. timestamp returns the timestamp at which data is generated. node status returns the status of the node. |
|  | value returns the history data. |
|  | timestamp returns the timestamp at which data is generated. |
|  | node status returns the status of the node. |
|  | status returns the status code. |
|  | continuation points out returns the continuation point and whether the history data has a continuation point. continuation point returns the point from which this VI continues reading if the OPC UA server cannot return all values in one response. has continuation point? returns whether the history data has a continuation point. |
|  | continuation point returns the point from which this VI continues reading if the OPC UA server cannot return all values in one response. |
|  | has continuation point? returns whether the history data has a continuation point. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Data Multiple Read VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-data-read-vi.html language=enus -->
## TOPIC 00033: History Data Read VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-data-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-data-read-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Reads history data within a time range. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<i

### History Data Read VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Reads history data within a time range.

Example

[IMAGE alt='image' src='images/History_Data_Read_Raw_Server.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies the start time, the end time, the maximum number of values to return over the time range, and whether to return bounding values. start time specifies the timestamp at which this VI reads the first history data. end time specifies the timestamp at which this VI reads the last history data. num values per node specifies the maximum number of values to return over the time range. The default is 0, which specifies that this VI returns all values over the time range. return bounds specifies whether to return bounding values. The default is FALSE, which specifies that this VI does not return bounding values. Bounding values are values associated with the starting time and the ending time. An OPC UA client can require bounding values to determine the starting and ending values when requesting data over a time range. |
|  | start time specifies the timestamp at which this VI reads the first history data. |
|  | end time specifies the timestamp at which this VI reads the last history data. |
|  | num values per node specifies the maximum number of values to return over the time range. The default is 0, which specifies that this VI returns all values over the time range. |
|  | return bounds specifies whether to return bounding values. The default is FALSE, which specifies that this VI does not return bounding values. Bounding values are values associated with the starting time and the ending time. An OPC UA client can require bounding values to determine the starting and ending values when requesting data over a time range. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | history data returns data from the history database. value returns the history data. timestamp returns the timestamp at which data is generated. node status specifies the status code of the node. |
|  | value returns the history data. |
|  | timestamp returns the timestamp at which data is generated. |
|  | node status specifies the status code of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Data Read VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-data-update-vi.html language=enus -->
## TOPIC 00034: History Data Update VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-data-update-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-data-update-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Updates history data at a specific timestamp. Example update type specifies the type of update operation this VI performs. 1InsertInserts new entries into the history database at the specified timestamps.2ReplaceReplaces existing entries

### History Data Update VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Updates history data at a specific timestamp.

Example

[IMAGE alt='image' src='images/History_Data_Update_Server.gif']

|  | update type specifies the type of update operation this VI performs. 1InsertInserts new entries into the history database at the specified timestamps.2ReplaceReplaces existing entries in the history database at the specified timestamps.3Update (default)Inserts new entries or replaces existing entries in the history database at the specified timestamps. |
| --- | --- |
| 1 | InsertInserts new entries into the history database at the specified timestamps. |
| 2 | ReplaceReplaces existing entries in the history database at the specified timestamps. |
| 3 | Update (default)Inserts new entries or replaces existing entries in the history database at the specified timestamps. |
|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | update values specifies the value to update with, the timestamp of the data to replace, and the status code. value specifies the value that this VI uses to update with. timestamp specifies the timestamp at which this VI updates history data. node status specifies the status code of the node. |
|  | value specifies the value that this VI uses to update with. |
|  | timestamp specifies the timestamp at which this VI updates history data. |
|  | node status specifies the status code of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | operation status returns the status of the operation. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Data Update VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-event-delete-vi.html language=enus -->
## TOPIC 00035: History Event Delete VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-event-delete-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-event-delete-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Deletes a history event. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. notifier node ID specifies the ID of the notifier. A notifier is an object that you can subscribe to get events from the as

### History Event Delete VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Deletes a history event.

Example

[IMAGE alt='image' src='images/History_Event_Delete_svr.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | notifier node ID specifies the ID of the notifier. A notifier is an object that you can subscribe to get events from the associated condition nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, notifier node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | event IDs specifies the event IDs to delete. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | operation status returns the status of the operation. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Event Delete VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-event-multiple-read-vi.html language=enus -->
## TOPIC 00036: History Event Multiple Read VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-event-multiple-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-event-multiple-read-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Reads one or multiple history events. Example continuation points in specifies the continuation point and whether the history event has a continuation point. continuation point specifies the point from which this VI continues to read if

### History Event Multiple Read VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Reads one or multiple history events.

Example

[IMAGE alt='image' src='images/History_Event_Multiple_Read_clnt.gif']

|  | continuation points in specifies the continuation point and whether the history event has a continuation point. continuation point specifies the point from which this VI continues to read if the OPC UA server cannot return all values in one response. has continuation point? specifies whether the history event has a continuation point. The default is TRUE, which specifies that the history event has a continuation point. |
| --- | --- |
|  | continuation point specifies the point from which this VI continues to read if the OPC UA server cannot return all values in one response. |
|  | has continuation point? specifies whether the history event has a continuation point. The default is TRUE, which specifies that the history event has a continuation point. |
|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
|  | notifier node IDs specifies the IDs of one or multiple notifier nodes. A notifier is an object that you can subscribe to get events from the associated condition nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, notifier node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies the start and end time to read history events and the maximum number of values to return for all event notifiers. start time specifies the timestamp at which this VI reads the first history event. end time specifies the timestamp at which this VI reads the last history event. num values per node specifies the maximum number of events to return for any event notifier over the time range. The default is 0, which specifies that this VI returns all events over the time range. |
|  | start time specifies the timestamp at which this VI reads the first history event. |
|  | end time specifies the timestamp at which this VI reads the last history event. |
|  | num values per node specifies the maximum number of events to return for any event notifier over the time range. The default is 0, which specifies that this VI returns all events over the time range. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns detailed information about the history events, the statuses of the notifier nodes, and the IDs of the notifier nodes. notifier node ID returns the ID of the notifier. history events returns detailed information about the history events that this VI reads. condition type affects the validity of the output data in history events. For the dialog condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked stateinvalidconfirmed stateinvalidpromptvalid For the off-normal alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked statevalidconfirmed statevalidpromptinvalid For the limit alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit statevalidacked statevalidconfirmed statevalidpromptinvalid condition node ID returns the ID of the condition node. condition type returns the type of the condition node. 0Dialog Condition1Off-Normal Alarm2Exclusive Level Alarm3Exclusive Deviation Alarm4Exclusive Rate of Change Alarm5Non Exclusive Level Alarm6Non Exclusive Deviation Alarm7Non Exclusive Rate of Change Alarm8Refresh Start Event9Refresh End Event source node ID/input node ID returns the ID of the source node or the input node. For nodes of the dialog condition type, source node ID/input node ID returns the ID of the source node. For nodes of the off-normal alarm type and the limit alarm type, source node ID/input node ID returns the ID of the input node. You can use the Add Condition VI to add dialog condition nodes, off-normal alarm nodes, or limit alarm nodes. event ID returns the event ID. active returns whether the situation the alarm is representing exists. time returns the timestamp at which the event occurs. severity returns a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. quality returns the status code to display the quality of the values that the condition depends on. comment returns the string to associate with a certain state of condition. limit state returns the state of the alarm. high high state returns whether the condition value exceeds the high high limit. high state returns whether the condition value exceeds the high limit. low state returns whether the condition value exceeds the low limit. low low state returns whether the condition value exceeds the low low limit. acked state returns whether the condition is acknowledged. confirmed state returns whether the condition is confirmed. prompt returns the textual content of a dialog prompt only when the condition type is dialog condition. status returns the status code. |
|  | notifier node ID returns the ID of the notifier. |
|  | history events returns detailed information about the history events that this VI reads. condition type affects the validity of the output data in history events. For the dialog condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked stateinvalidconfirmed stateinvalidpromptvalid For the off-normal alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked statevalidconfirmed statevalidpromptinvalid For the limit alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit statevalidacked statevalidconfirmed statevalidpromptinvalid condition node ID returns the ID of the condition node. condition type returns the type of the condition node. 0Dialog Condition1Off-Normal Alarm2Exclusive Level Alarm3Exclusive Deviation Alarm4Exclusive Rate of Change Alarm5Non Exclusive Level Alarm6Non Exclusive Deviation Alarm7Non Exclusive Rate of Change Alarm8Refresh Start Event9Refresh End Event source node ID/input node ID returns the ID of the source node or the input node. For nodes of the dialog condition type, source node ID/input node ID returns the ID of the source node. For nodes of the off-normal alarm type and the limit alarm type, source node ID/input node ID returns the ID of the input node. You can use the Add Condition VI to add dialog condition nodes, off-normal alarm nodes, or limit alarm nodes. event ID returns the event ID. active returns whether the situation the alarm is representing exists. time returns the timestamp at which the event occurs. severity returns a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. quality returns the status code to display the quality of the values that the condition depends on. comment returns the string to associate with a certain state of condition. limit state returns the state of the alarm. high high state returns whether the condition value exceeds the high high limit. high state returns whether the condition value exceeds the high limit. low state returns whether the condition value exceeds the low limit. low low state returns whether the condition value exceeds the low low limit. acked state returns whether the condition is acknowledged. confirmed state returns whether the condition is confirmed. prompt returns the textual content of a dialog prompt only when the condition type is dialog condition. |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | invalid |
| acked state | invalid |
| confirmed state | invalid |
| prompt | valid |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | invalid |
| acked state | valid |
| confirmed state | valid |
| prompt | invalid |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | valid |
| acked state | valid |
| confirmed state | valid |
| prompt | invalid |
|  | condition node ID returns the ID of the condition node. |
|  | condition type returns the type of the condition node. 0Dialog Condition1Off-Normal Alarm2Exclusive Level Alarm3Exclusive Deviation Alarm4Exclusive Rate of Change Alarm5Non Exclusive Level Alarm6Non Exclusive Deviation Alarm7Non Exclusive Rate of Change Alarm8Refresh Start Event9Refresh End Event |
| 0 | Dialog Condition |
| 1 | Off-Normal Alarm |
| 2 | Exclusive Level Alarm |
| 3 | Exclusive Deviation Alarm |
| 4 | Exclusive Rate of Change Alarm |
| 5 | Non Exclusive Level Alarm |
| 6 | Non Exclusive Deviation Alarm |
| 7 | Non Exclusive Rate of Change Alarm |
| 8 | Refresh Start Event |
| 9 | Refresh End Event |
|  | source node ID/input node ID returns the ID of the source node or the input node. For nodes of the dialog condition type, source node ID/input node ID returns the ID of the source node. For nodes of the off-normal alarm type and the limit alarm type, source node ID/input node ID returns the ID of the input node. You can use the Add Condition VI to add dialog condition nodes, off-normal alarm nodes, or limit alarm nodes. |
|  | event ID returns the event ID. |
|  | active returns whether the situation the alarm is representing exists. |
|  | time returns the timestamp at which the event occurs. |
|  | severity returns a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. |
|  | quality returns the status code to display the quality of the values that the condition depends on. |
|  | comment returns the string to associate with a certain state of condition. |
|  | limit state returns the state of the alarm. high high state returns whether the condition value exceeds the high high limit. high state returns whether the condition value exceeds the high limit. low state returns whether the condition value exceeds the low limit. low low state returns whether the condition value exceeds the low low limit. |
|  | high high state returns whether the condition value exceeds the high high limit. |
|  | high state returns whether the condition value exceeds the high limit. |
|  | low state returns whether the condition value exceeds the low limit. |
|  | low low state returns whether the condition value exceeds the low low limit. |
|  | acked state returns whether the condition is acknowledged. |
|  | confirmed state returns whether the condition is confirmed. |
|  | prompt returns the textual content of a dialog prompt only when the condition type is dialog condition. |
|  | status returns the status code. |
|  | continuation points out returns the continuation point and whether the history event has a continuation point. continuation point returns the point from which this VI continues reading if the OPC UA server cannot return all values in one response. has continuation point? returns whether the history event has a continuation point. |
|  | continuation point returns the point from which this VI continues reading if the OPC UA server cannot return all values in one response. |
|  | has continuation point? returns whether the history event has a continuation point. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Event Multiple Read VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-event-read-vi.html language=enus -->
## TOPIC 00037: History Event Read VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-event-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-event-read-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Reads a notifier. A notifier node enables an OPC UA client, which subscribes to the node, to receive event notifications. Example OPC UA server refnum in specifies the reference data value of the OPC UA server. notifier node ID specifies

### History Event Read VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Reads a notifier. A notifier node enables an OPC UA client, which subscribes to the node, to receive event notifications.

Example

[IMAGE alt='image' src='images/History_Event_Read_svr.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | notifier node ID specifies the ID of the notifier. A notifier is an object that you can subscribe to get events from the associated condition nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, notifier node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies the start time and the end time for the VI to read the notifier. start time specifies the timestamp at which this VI reads the first history event. end time specifies the timestamp at which this VI reads the last history event. |
|  | start time specifies the timestamp at which this VI reads the first history event. |
|  | end time specifies the timestamp at which this VI reads the last history event. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | history events returns the detailed information about the event that this VI reads from the history database. condition type affects the validity of the output data in history event. For the dialog condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked stateinvalidconfirmed stateinvalidpromptvalid For the off-normal alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit stateinvalidacked statevalidconfirmed statevalidpromptinvalid For the limit alarm condition type, the validity of the output data is shown in the following table: OutputValiditycondition node IDvalidsource node ID/input node IDvalidevent IDvalidactivevalidtimevalidseverityvalidqualityvalidcommentvalidlimit statevalidacked statevalidconfirmed statevalidpromptinvalid condition node ID returns the ID of the condition node. condition type returns the type of the condition node. 0Dialog Condition1Off-Normal Alarm2Exclusive Level Alarm3Exclusive Deviation Alarm4Exclusive Rate of Change Alarm5Non Exclusive Level Alarm6Non Exclusive Deviation Alarm7Non Exclusive Rate of Change Alarm8Refresh Start Event9Refresh End Event source node ID/input node ID returns the ID of the source node or the input node. For nodes of the dialog condition type, source node ID/input node ID returns the ID of the source node. For nodes of the off-normal alarm type and the limit alarm type, source node ID/input node ID returns the ID of the input node. You can use the Add Condition VI to add dialog condition nodes, off-normal alarm nodes, or limit alarm nodes. event ID returns the event ID. active returns whether the situation the alarm is representing exists. time returns the timestamp at which the event occurs. severity returns a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. quality returns the status code to display the quality of the values that the condition depends on. comment returns the string to associate with a certain state of condition. limit state returns the state of the alarm. high high state returns whether the condition value exceeds the high high limit. high state returns whether the condition value exceeds the high limit. low state returns whether the condition value exceeds the low limit. low low state returns whether the condition value exceeds the low low limit. acked state returns whether the condition is acknowledged. confirmed state returns whether the condition is confirmed. prompt returns the textual content of a dialog prompt only when the condition type is dialog condition. |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | invalid |
| acked state | invalid |
| confirmed state | invalid |
| prompt | valid |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | invalid |
| acked state | valid |
| confirmed state | valid |
| prompt | invalid |
| Output | Validity |
| condition node ID | valid |
| source node ID/input node ID | valid |
| event ID | valid |
| active | valid |
| time | valid |
| severity | valid |
| quality | valid |
| comment | valid |
| limit state | valid |
| acked state | valid |
| confirmed state | valid |
| prompt | invalid |
|  | condition node ID returns the ID of the condition node. |
|  | condition type returns the type of the condition node. 0Dialog Condition1Off-Normal Alarm2Exclusive Level Alarm3Exclusive Deviation Alarm4Exclusive Rate of Change Alarm5Non Exclusive Level Alarm6Non Exclusive Deviation Alarm7Non Exclusive Rate of Change Alarm8Refresh Start Event9Refresh End Event |
| 0 | Dialog Condition |
| 1 | Off-Normal Alarm |
| 2 | Exclusive Level Alarm |
| 3 | Exclusive Deviation Alarm |
| 4 | Exclusive Rate of Change Alarm |
| 5 | Non Exclusive Level Alarm |
| 6 | Non Exclusive Deviation Alarm |
| 7 | Non Exclusive Rate of Change Alarm |
| 8 | Refresh Start Event |
| 9 | Refresh End Event |
|  | source node ID/input node ID returns the ID of the source node or the input node. For nodes of the dialog condition type, source node ID/input node ID returns the ID of the source node. For nodes of the off-normal alarm type and the limit alarm type, source node ID/input node ID returns the ID of the input node. You can use the Add Condition VI to add dialog condition nodes, off-normal alarm nodes, or limit alarm nodes. |
|  | event ID returns the event ID. |
|  | active returns whether the situation the alarm is representing exists. |
|  | time returns the timestamp at which the event occurs. |
|  | severity returns a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. |
|  | quality returns the status code to display the quality of the values that the condition depends on. |
|  | comment returns the string to associate with a certain state of condition. |
|  | limit state returns the state of the alarm. high high state returns whether the condition value exceeds the high high limit. high state returns whether the condition value exceeds the high limit. low state returns whether the condition value exceeds the low limit. low low state returns whether the condition value exceeds the low low limit. |
|  | high high state returns whether the condition value exceeds the high high limit. |
|  | high state returns whether the condition value exceeds the high limit. |
|  | low state returns whether the condition value exceeds the low limit. |
|  | low low state returns whether the condition value exceeds the low low limit. |
|  | acked state returns whether the condition is acknowledged. |
|  | confirmed state returns whether the condition is confirmed. |
|  | prompt returns the textual content of a dialog prompt only when the condition type is dialog condition. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Event Read VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=history-event-update-vi.html language=enus -->
## TOPIC 00038: History Event Update VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `history-event-update-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/history-event-update-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Historical Access VIs Requires: OPC UA Toolkit Updates a history event. Example update type specifies the type of update operation this VI performs. 1InsertInserts new entries into the history database at the specified timestamps.2ReplaceReplaces existing entries in the history datab

### History Event Update VI

**Owning Palette:** Historical Access VIs

**Requires:** OPC UA Toolkit

Updates a history event.

Example

[IMAGE alt='image' src='images/History_Event_Update_svr.gif']

|  | update type specifies the type of update operation this VI performs. 1InsertInserts new entries into the history database at the specified timestamps.2ReplaceReplaces existing entries in the history database at the specified timestamps.3Update (default)Inserts new entries or replaces existing entries in the history database at the specified timestamps. |
| --- | --- |
| 1 | InsertInserts new entries into the history database at the specified timestamps. |
| 2 | ReplaceReplaces existing entries in the history database at the specified timestamps. |
| 3 | Update (default)Inserts new entries or replaces existing entries in the history database at the specified timestamps. |
|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
|  | notifier node ID specifies the ID of the notifier. A notifier is an object that you can subscribe to get events from the associated condition nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, notifier node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | event data specifies information about the events to update. condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. event ID specifies the event ID. active specifies whether an alarm is in active state. The default is FALSE, which specifies that the alarm is not in active state. time specifies the time at which the event occurred. severity specifies a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. The default is 100. quality specifies the quality of the values that the condition depends on. Refer to the status code for details. comment specifies the string to associate with a certain state of the condition. limit state specifies the state of the alarm. high high state specifies whether the condition value exceeds the high high limit. The default is FALSE, which specifies that the condition does not exceed the high high limit. high state specifies whether the condition value exceeds the high limit. The default is FALSE, which specifies that the condition does not exceed the high limit. low state specifies whether the condition value exceeds the low limit. The default is FALSE, which specifies that the condition does not exceed the low limit. low low state specifies whether the condition value exceeds the low low limit. The default is FALSE, which specifies that the condition does not exceed the low low limit. acked state specifies whether the condition is acknowledged. The default is FALSE, which specifies that the condition is not acknowledged. confirmed state specifies whether the condition is confirmed. The default is FALSE, which specifies that the condition is not confirmed. prompt specifies the textual content of a dialog prompt. |
|  | condition node ID specifies the ID of the condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | event ID specifies the event ID. |
|  | active specifies whether an alarm is in active state. The default is FALSE, which specifies that the alarm is not in active state. |
|  | time specifies the time at which the event occurred. |
|  | severity specifies a value that indicates the urgency of the event. The value ranges from 1 to 1000, with 1 being the lowest severity and 1000 being the highest severity. The default is 100. |
|  | quality specifies the quality of the values that the condition depends on. Refer to the status code for details. |
|  | comment specifies the string to associate with a certain state of the condition. |
|  | limit state specifies the state of the alarm. high high state specifies whether the condition value exceeds the high high limit. The default is FALSE, which specifies that the condition does not exceed the high high limit. high state specifies whether the condition value exceeds the high limit. The default is FALSE, which specifies that the condition does not exceed the high limit. low state specifies whether the condition value exceeds the low limit. The default is FALSE, which specifies that the condition does not exceed the low limit. low low state specifies whether the condition value exceeds the low low limit. The default is FALSE, which specifies that the condition does not exceed the low low limit. |
|  | high high state specifies whether the condition value exceeds the high high limit. The default is FALSE, which specifies that the condition does not exceed the high high limit. |
|  | high state specifies whether the condition value exceeds the high limit. The default is FALSE, which specifies that the condition does not exceed the high limit. |
|  | low state specifies whether the condition value exceeds the low limit. The default is FALSE, which specifies that the condition does not exceed the low limit. |
|  | low low state specifies whether the condition value exceeds the low low limit. The default is FALSE, which specifies that the condition does not exceed the low low limit. |
|  | acked state specifies whether the condition is acknowledged. The default is FALSE, which specifies that the condition is not acknowledged. |
|  | confirmed state specifies whether the condition is confirmed. The default is FALSE, which specifies that the condition is not confirmed. |
|  | prompt specifies the textual content of a dialog prompt. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | operation status returns the status of the operation. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the History Event Update VI.

Parent topic:

Historical Access VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=input-node-id-property.html language=enus -->
## TOPIC 00039: Input Node Id Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `input-node-id-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/input-node-id-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties The ID of the input node. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Read-only Data Type

### Input Node Id Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

The ID of the input node.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Limit Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=input-node-id-property_2.html language=enus -->
## TOPIC 00040: Input Node Id Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `input-node-id-property_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/input-node-id-property_2.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties The ID of the input node. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Read-only Data Type

### Input Node Id Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

The ID of the input node.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Off-Normal Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=limit-alarm-properties.html language=enus -->
## TOPIC 00041: Limit Alarm Properties

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `limit-alarm-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/limit-alarm-properties.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The limit alarm specifies limits that can generate an alarm when a value equals or exceeds the limit. There are four alarm limits: high high limit, high limit, low limit, and low low limit. Wire the OPC UA limit alarm refnum out output of the Exclusive Limit Alarm and Nonexclusive Limit Alarm instan

### Limit Alarm Properties

The limit alarm specifies limits that can generate an alarm when a value equals or exceeds the limit. There are four alarm limits: high high limit, high limit, low limit, and low low limit. Wire the **OPC UA limit alarm refnum out** output of the Exclusive Limit Alarm and Nonexclusive Limit Alarm instances of Add Condition VI to the **reference** input of a standard Property Node to get the Limit Alarm Property Node. This Property Node has the following properties:

| Property | Description |
| --- | --- |
| Active State | Whether a condition is in the active state. Details |
| Enabled State | Whether a condition is in the enabled state. Details |
| Input Node Id | The ID of an input node. Details |
| Limit | The values of the high high limit, high limit, low limit, and low low limit. Details |
| Max Time Shelved | The maximum time that an alarm condition is in shelved state. Details |
| Retain | Whether an OPC UA client synchronizes the condition state with that of the server. Details |
| Severity Level | The values of the high high severity, high severity, low severity, and low low severity. Details |
| Shelving State | Whether an alarm condition is in shelved state. In shelved state, an alarm cannot display to the end user. Details |
| Shelving Timer Resolution in mSecs | The smallest time unit, in milliseconds, for the timer to calculate shelving time. Details |
| Suppressed or Shelved | Whether an alarm condition is in suppressed or shelved state. Details |
| Suppressed State | Whether an alarm condition is in suppressed state. In suppressed state, an alarm does not occur at all circumstances. Details |

Parent topic:

OPC UA Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=limit-property.html language=enus -->
## TOPIC 00042: Limit Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `limit-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/limit-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties The values of the high high limit, high limit, low limit, and low low limit. Name Description Default Value High High Limit The value above which LabVIEW generates a high high limit alarm. 80 High Limit The value above which LabVIEW generates a

### Limit Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop)

The values of the high high limit, high limit, low limit, and low low limit.

| Name | Description | Default Value |
| --- | --- | --- |
| High High Limit | The value above which LabVIEW generates a high high limit alarm. | 80 |
| High Limit | The value above which LabVIEW generates a high limit alarm. | 60 |
| Low Limit | The value above which LabVIEW generates a low limit alarm. | 40 |
| Low Low Limit | The value above which LabVIEW generates a low low limit alarm. | 20 |

Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Note

You must provide values for all elements. Otherwise, LabVIEW initializes the elements that do not have input values to 0. The values of the elements must conform with the following requirement:

High High Limit > High Limit > Low Limit > Low Low Limit

Otherwise, LabVIEW reports an error.

Parent topic:

Limit Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=max-time-shelved-property.html language=enus -->
## TOPIC 00043: Max Time Shelved Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `max-time-shelved-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/max-time-shelved-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties The maximum time that an alarm condition is in shelved state. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Rea

### Max Time Shelved Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

The maximum time that an alarm condition is in shelved state.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |
| Default Value | 5,000,000 ms |

Parent topic:

Limit Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=max-time-shelved-property_2.html language=enus -->
## TOPIC 00044: Max Time Shelved Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `max-time-shelved-property_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/max-time-shelved-property_2.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Limit Alarm Properties and Off-Normal Alarm Properties The maximum time that an alarm condition is in shelved state. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Rea

### Max Time Shelved Property

**Requires:** OPC UA Toolkit

**Class:** [Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop) and [Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

The maximum time that an alarm condition is in shelved state.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |
| Default Value | 5,000,000 ms |

Parent topic:

Off-Normal Alarm Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=multiple-read-vi.html language=enus -->
## TOPIC 00045: Multiple Read VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `multiple-read-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/multiple-read-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Reads the value, timestamp, and status of one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use. Multiple Read (Variant) OPC UA client refnum in

### Multiple Read VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Reads the value, timestamp, and status of one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use.

Multiple Read (Variant)

[IMAGE alt='image' src='images/Multiple_Read_Variant_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. value can also return the Matrix data type. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. value can also return the Matrix data type. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Bool)

[IMAGE alt='image' src='images/Multiple_Read_Bool_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (SByte)

[IMAGE alt='image' src='images/Multiple_Read_SByte_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Byte)

[IMAGE alt='image' src='images/Multiple_Read_Byte_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int16)

[IMAGE alt='image' src='images/Multiple_Read_Int16_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value is the number read from shared memory. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value is the number read from shared memory. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt16)

[IMAGE alt='image' src='images/Multiple_Read_UInt16_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int32)

[IMAGE alt='image' src='images/Multiple_Read_Int32_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value of the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value of the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt32)

[IMAGE alt='image' src='images/Multiple_Read_UInt32_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int64)

[IMAGE alt='image' src='images/Multiple_Read_Int64_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt64)

[IMAGE alt='image' src='images/Multiple_Read_UInt64_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Float)

[IMAGE alt='image' src='images/Multiple_Read_Float_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Double)

[IMAGE alt='image' src='images/Multiple_Read_Double_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (String)

[IMAGE alt='image' src='images/Multiple_Read_String_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (DateTime)

[IMAGE alt='image' src='images/Multiple_Read_DateTime_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (ByteString)

[IMAGE alt='image' src='images/Multiple_Read_ByteString_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. value returns the value that this VI reads from the node. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | value returns the value that this VI reads from the node. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Bool Array)

[IMAGE alt='image' src='images/Multiple_Read_Bool_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (SByte Array)

[IMAGE alt='image' src='images/Multiple_Read_SByte_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Byte Array)

[IMAGE alt='image' src='images/Multiple_Read_Byte_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int16 Array)

[IMAGE alt='image' src='images/Multiple_Read_Int16_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt16 Array)

[IMAGE alt='image' src='images/Multiple_Read_UInt16_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int32 Array)

[IMAGE alt='image' src='images/Multiple_Read_Int32_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt32 Array)

[IMAGE alt='image' src='images/Multiple_Read_UInt32_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Int64 Array)

[IMAGE alt='image' src='images/Multiple_Read_Int64_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (UInt64 Array)

[IMAGE alt='image' src='images/Multiple_Read_UInt64_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Float Array)

[IMAGE alt='image' src='images/Multiple_Read_Float_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (Double Array)

[IMAGE alt='image' src='images/Multiple_Read_Double_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (String Array)

[IMAGE alt='image' src='images/Multiple_Read_String_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (DateTime Array)

[IMAGE alt='image' src='images/Multiple_Read_DateTime_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Read (ByteString Array)

[IMAGE alt='image' src='images/Multiple_Read_ByteString_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | node IDs specifies the IDs of the nodes. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node IDs also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs of the nodes, the values of the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID returns the ID of the node. values returns the values that this VI reads from the nodes. timestamp returns the date and time associated with value. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | values returns the values that this VI reads from the nodes. |
|  | timestamp returns the date and time associated with value. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Multiple Read VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=multiple-write-vi.html language=enus -->
## TOPIC 00046: Multiple Write VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `multiple-write-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/multiple-write-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Client VIs Requires: OPC UA Toolkit Writes values to one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use. Multiple Write (Variant) OPC UA client refnum in specifies the reference

### Multiple Write VI

**Owning Palette:** OPC UA Client VIs

**Requires:** OPC UA Toolkit

Writes values to one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use.

Multiple Write (Variant)

[IMAGE alt='image' src='images/Multiple_Write_Variant_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. value also supports the Matrix data type. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. value also supports the Matrix data type. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Bool)

[IMAGE alt='image' src='images/Multiple_Write_Bool_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (SByte)

[IMAGE alt='image' src='images/Multiple_Write_SByte_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Byte)

[IMAGE alt='image' src='images/Multiple_Write_Byte_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int16)

[IMAGE alt='image' src='images/Multiple_Write_Int16_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt16)

[IMAGE alt='image' src='images/Multiple_Write_UInt16_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int32)

[IMAGE alt='image' src='images/Multiple_Write_Int32_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt32)

[IMAGE alt='image' src='images/Multiple_Write_UInt32_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int64)

[IMAGE alt='image' src='images/Multiple_Write_Int64_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt64)

[IMAGE alt='image' src='images/Multiple_Write_UInt64_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Float)

[IMAGE alt='image' src='images/Multiple_Write_Float_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Double)

[IMAGE alt='image' src='images/Multiple_Write_Double_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (String)

[IMAGE alt='image' src='images/Multiple_Write_String_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (DateTime)

[IMAGE alt='image' src='images/Multiple_Write_DateTime_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (ByteString)

[IMAGE alt='image' src='images/Multiple_Write_ByteString_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. value specifies the value of the node. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | value specifies the value of the node. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (BoolArray)

[IMAGE alt='image' src='images/Multiple_Write_Bool_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (SByteArray)

[IMAGE alt='image' src='images/Multiple_Write_SByte_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (ByteArray)

[IMAGE alt='image' src='images/Multiple_Write_Byte_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int16 Array)

[IMAGE alt='image' src='images/Multiple_Write_Int16_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt16 Array)

[IMAGE alt='image' src='images/Multiple_Write_UInt16_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int32 Array)

[IMAGE alt='image' src='images/Multiple_Write_Int32_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt32 Array)

[IMAGE alt='image' src='images/Multiple_Write_UInt32_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Int64 Array)

[IMAGE alt='image' src='images/Multiple_Write_Int64_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (UInt64 Array)

[IMAGE alt='image' src='images/Multiple_Write_UInt64_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Float Array)

[IMAGE alt='image' src='images/Multiple_Write_Float_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (Double Array)

[IMAGE alt='image' src='images/Multiple_Write_Double_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (String Array)

[IMAGE alt='image' src='images/Multiple_Write_String_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (DateTime Array)

[IMAGE alt='image' src='images/Multiple_Write_DateTime_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Multiple Write (ByteString Array)

[IMAGE alt='image' src='images/Multiple_Write_ByteString_Array_clnt.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | requests specifies the IDs of the nodes, the values to write to the nodes, the timestamps associated with the values, and the statuses of the nodes. node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. values specifies the values of the nodes. timestamp specifies the date and time associated with value. node status specifies the status of the node. |
|  | node ID specifies the ID of the node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | values specifies the values of the nodes. |
|  | timestamp specifies the date and time associated with value. |
|  | node status specifies the status of the node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | results returns the IDs and the statuses of the nodes. node ID returns the ID of the node. status returns the status code. |
|  | node ID returns the ID of the node. |
|  | status returns the status code. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Multiple Write VI.

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=node-name-array-to-node-path-vi.html language=enus -->
## TOPIC 00047: Node Name Array To Node Path VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `node-name-array-to-node-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/node-name-array-to-node-path-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA VIs Generates the node path from an array of node names. You can use this VI both on OPC UA server and OPC UA client applications. node names specifies an array of node names that describes the path of the node location in the address space. error in describes error conditions

### Node Name Array To Node Path VI

**Owning Palette:** OPC UA VIs

Generates the node path from an array of node names. You can use this VI both on OPC UA server and OPC UA client applications.

[IMAGE alt='image' src='images/opcua_nodenamearraytonodepath.gif']

|  | node names specifies an array of node names that describes the path of the node location in the address space. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | node path returns the path of the node. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=node-path-to-node-name-array-vi.html language=enus -->
## TOPIC 00048: Node Path To Node Name Array VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `node-path-to-node-name-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/node-path-to-node-name-array-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA VIs Generates an array of node names from a node path. You can use this VI both on OPC UA server and OPC UA client applications. node path specifies the path of the node. The node path consists of node names separated by a period between each name, with the parent node name be

### Node Path To Node Name Array VI

**Owning Palette:** OPC UA VIs

Generates an array of node names from a node path. You can use this VI both on OPC UA server and OPC UA client applications.

[IMAGE alt='image' src='images/opcua_nodepathtonodenamearray.gif']

|  | node path specifies the path of the node. The node path consists of node names separated by a period between each name, with the parent node name before the period and child node name after the period. For example, a node path Device.folder.item indicates that Device is the parent node of folder, and folder is the parent node of item. The following examples demonstrate how to specify node path. If a node name contains a period, use a pair of quotation marks around the node name. For example, if a node name is Device.1, and this node contains a child node folder, the node path of the child node is "Device.1".folder. If a node name contains one or more quotation marks, add one quotation mark beside each quotation mark and then a pair of quotation marks around the node name. For example, if a node name is Device1"Device2, and this node contains a child node folder, the node path of the child node is "Device1""Device2".folder. If a node name contains both a period and quotation mark, both of the previous rules still apply. For example, if a node name is Device1"Device2.Device3, and this node contains a child node folder, the node path of the child node is "Device1""Device2.Device3".folder. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | node names returns an array of node names. |
|  | error out contains error information. This output provides standard error out functionality. |

Parent topic:

OPC UA Client VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=notifier-properties.html language=enus -->
## TOPIC 00049: Notifier Properties

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `notifier-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/notifier-properties.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A notifier node enables an OPC UA client, which subscribes to the node, to receive event notifications. Wire the notifier node ID output of the Add Notifier VI to the reference input of a standard Property Node to get the Variable Node Property Node. This Property Node has the following properties:

### Notifier Properties

A notifier node enables an OPC UA client, which subscribes to the node, to receive event notifications. Wire the **notifier node ID** output of the Add Notifier VI to the **reference** input of a standard Property Node to get the Variable Node Property Node. This Property Node has the following properties:

| Property | Description |
| --- | --- |
| Historical Event Access | Whether historical event access is available. Details |
| Historical Event Queue Size | The size of a historical event queue. You can add a history event queue only to a notifier. A history event queue can store one history event only. Details |

Parent topic:

OPC UA Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=off-normal-alarm-properties.html language=enus -->
## TOPIC 00050: Off-Normal Alarm Properties

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `off-normal-alarm-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/off-normal-alarm-properties.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The off-normal alarm specifies a condition that is not normal. Wire the OPC UA off normal alarm refnum out output of the Off-Normal Alarm instance of Add Condition VI to the reference input of a standard Property Node to get the Off Normal Alarm Property Node. This Property Node has the following pr

### Off-Normal Alarm Properties

The off-normal alarm specifies a condition that is not normal. Wire the **OPC UA off normal alarm refnum out** output of the Off-Normal Alarm instance of Add Condition VI to the **reference** input of a standard Property Node to get the Off Normal Alarm Property Node. This Property Node has the following properties:

| Property | Description |
| --- | --- |
| Active State | Whether a condition is in the active state. Details |
| Enabled State | Whether a condition is in the enabled state. Details |
| Retain | Whether the OPC UA client synchronizes the condition state with that of the server. Details |
| Input Node Id | The ID of an input node. Details |
| Max Time Shelved | The maximum time that an alarm condition is in shelved state. Details |
| Shelving State | Whether an alarm condition is in shelved state. In shelved state, an alarm cannot display to the end user. Details |
| Shelving Timer Resolution in mSecs | The smallest time unit, in milliseconds, for a timer to calculate shelving time. Details |
| Suppressed or Shelved | Whether an alarm condition is in suppressed or shelved state. Details |
| Suppressed State | Whether an alarm condition is in suppressed state. In suppressed state, an alarm does not occur at all circumstances. Details |

Parent topic:

OPC UA Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=opc-ua-client-vis.html language=enus -->
## TOPIC 00051: OPC UA Client VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `opc-ua-client-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/opc-ua-client-vis.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the OPC UA Client VIs to create a customized OPC UA client application. Example Palette ObjectDescriptionAdd M

### OPC UA Client VIs

**Owning Palette:** OPC UA VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the OPC UA Client VIs to create a customized OPC UA client application.

Example

| Palette Object | Description |
| --- | --- |
| Add Monitored Data Nodes | Adds nodes to a data subscription to monitor data changes. |
| Connect Server | Creates a connection to an OPC UA server. |
| Create Subscription | Creates a subscription to the nodes of the OPC UA server. When the nodes that the OPC UA client subscribes to incur data changes, the OPC UA server collects the data changes and sends a notification message to the OPC UA client. |
| Delete Monitored Nodes | Deletes one or multiple monitored nodes from a subscription. |
| Delete Subscriptions | Deletes one or multiple subscriptions. By deleting a subscription, you delete all the monitored nodes from the subscription. |
| Disconnect | Disconnects an OPC UA client from an OPC UA server. The OPC UA client automatically deletes all the subscriptions before disconnecting from the OPC UA server. |
| Forward Browse | Browses a node and returns information about its child nodes. |
| Get Node Attribute | Gets the attributes of a node. |
| Multiple Read | Reads the value, timestamp, and status of one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use. |
| Multiple Write | Writes values to one or multiple nodes. NI recommends choosing the Variant instance for all value data types. You must manually select the polymorphic instance to use. |

| Subpalette | Description |
| --- | --- |
| Alarms and Conditions VIs | Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA client applications. |
| Historical Access VIs | Use the Historical Access VIs to access historical data and events for OPC UA client applications. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the OPC UA Client VIs.

Parent topic:

OPC UA VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=opc-ua-common-operation-level-status-codes-op.html language=enus -->
## TOPIC 00052: OPC UA Common Operation Level Status Codes (OPC UA Toolkit)

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `opc-ua-common-operation-level-status-codes-op.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/opc-ua-common-operation-level-status-codes-op.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table contains descriptions of the codes returned by the status terminal. Good 0x00000000 The operation was successful. Uncertain 0x40000000 The value is uncertain but the reason is unknown. Bad 0x80000000 The value is bad but the reason is unknown. Bad_UnexpectedError 0x80010000 An un

### OPC UA Common Operation Level Status Codes (OPC UA Toolkit)

The following table contains descriptions of the codes returned by the **status** terminal.

| Good | 0x00000000 | The operation was successful. |
| --- | --- | --- |
| Uncertain | 0x40000000 | The value is uncertain but the reason is unknown. |
| Bad | 0x80000000 | The value is bad but the reason is unknown. |
| Bad_UnexpectedError | 0x80010000 | An unexpected error occurred. |
| Bad_InternalError | 0x80020000 | An internal error occurred as a result of a programming or configuration error. |
| Bad_OutOfMemory | 0x80030000 | Not enough memory to complete the operation. |
| Bad_ResourceUnavailable | 0x80040000 | An operating system resource is not available. |
| Bad_CommunicationError | 0x80050000 | A low level communication error occurred. |
| Bad_EncodingError | 0x80060000 | Encoding halted because of invalid data in the objects being serialized. |
| Bad_DecodingError | 0x80070000 | Decoding halted because of invalid data in the stream. |
| Bad_EncodingLimitsExceeded | 0x80080000 | The message encoding/decoding limits imposed by the stack have been exceeded. |
| Bad_RequestTooLarge | 0x80B80000 | The request message size exceeds limits set by the server. |
| Bad_ResponseTooLarge | 0x80B90000 | The response message size exceeds limits set by the client. |
| Bad_UnknownResponse | 0x80090000 | An unrecognized response was received from the server. |
| Bad_Timeout | 0x800A0000 | The operation timed out. |
| Bad_ServiceUnsupported | 0x800B0000 | The server does not support the requested service. |
| Bad_Shutdown | 0x800C0000 | The operation was cancelled because the application is shutting down. |
| Bad_ServerNotConnected | 0x800D0000 | The operation could not complete because the client is not connected to the server. |
| Bad_ServerHalted | 0x800E0000 | The server has stopped and cannot process any requests. |
| Bad_NothingToDo | 0x800F0000 | There was nothing to do because the client passed a list of operations with no elements. |
| Bad_TooManyOperations | 0x80100000 | The request could not be processed because it specified too many operations. |
| Bad_TooManyMonitoredItems | 0x80DB0000 | The request could not be processed because there are too many monitored items in the subscription. |
| Bad_DataTypeIdUnknown | 0x80110000 | The extension object cannot be (de)serialized because the data type ID is not recognized. |
| Bad_CertificateInvalid | 0x80120000 | The certificate provided as a parameter is not valid. |
| Bad_SecurityChecksFailed | 0x80130000 | An error occurred verifying security. |
| Bad_CertificateTimeInvalid | 0x80140000 | The certificate has expired or is not yet valid. |
| Bad_CertificateIssuerTimeInvalid | 0x80150000 | An Issuer certificate has expired or is not yet valid. |
| Bad_CertificateHostNameInvalid | 0x80160000 | The HostName used to connect to a serverdoes not match a HostName in the certificate. |
| Bad_CertificateUriInvalid | 0x80170000 | The URI specified in the ApplicationDescription does not match the URI in the certificate. |
| Bad_CertificateUseNotAllowed | 0x80180000 | The certificate may not be used for the requested operation. |
| Bad_CertificateIssuerUseNotAllowed | 0x80190000 | The Issuer certificate may not be used for the requested operation. |
| Bad_CertificateUntrusted | 0x801A0000 | The certificate is not trusted. |
| Bad_CertificateRevocationUnknown | 0x801B0000 | It was not possible to determine if the certificate has been revoked. |
| Bad_CertificateIssuerRevocationUnknown | 0x801C0000 | It was not possible to determine if the Issuer certificate has been revoked. |
| Bad_CertificateRevoked | 0x801D0000 | The certificate has been revoked. |
| Bad_CertificateIssuerRevoked | 0x801E0000 | The Issuer certificate has been revoked. |
| Bad_UserAccessDenied | 0x801F0000 | User does not have permission to perform the requested operation. |
| Bad_IdentityTokenInvalid | 0x80200000 | The user identity token is not valid. |
| Bad_IdentityTokenRejected | 0x80210000 | The user identity token is valid but the server has rejected it. |
| Bad_SecureChannelIdInvalid | 0x80220000 | The specified secure channel is no longer valid. |
| Bad_InvalidTimestamp | 0x80230000 | The timestamp is outside the range allowed by the server. |
| Bad_NonceInvalid | 0x80240000 | The nonce does appear to be not a random value or it is not the correct length. |
| Bad_SessionIdInvalid | 0x80250000 | The session ID is not valid. |
| Bad_SessionClosed | 0x80260000 | The session was closed by the client. |
| Bad_SessionNotActivated | 0x80270000 | The session cannot be used because ActivateSession has not been called. |
| Bad_SubscriptionIdInvalid | 0x80280000 | The subscription ID is not valid. |
| Bad_RequestHeaderInvalid | 0x802A0000 | The header for the request is missing or invalid. |
| Bad_TimestampsToReturnInvalid | 0x802B0000 | The timestamps to return parameter are invalid. |
| Bad_RequestCancelledByClient | 0x802C0000 | The request was cancelled by the client. |
| Good_SubscriptionTransferred | 0x002D0000 | The subscription was transferred to another session. |
| Good_CompletesAsynchronously | 0x002E0000 | The processing will complete asynchronously. |
| Good_Overload | 0x002F0000 | Sampling has slowed down due to resource limitations. |
| Good_Clamped | 0x00300000 | The value written was accepted but was clamped. |
| Bad_NoCommunication | 0x80310000 | Communication with the data source is defined but not established and there is no last known value available. |
| Bad_WaitingForInitialData | 0x80320000 | Waiting for the server to obtain values from the underlying data source. |
| Bad_NodeIdInvalid | 0x80330000 | The syntax of the node ID is not valid. |
| Bad_NodeIdUnknown | 0x80340000 | The node ID refers to a node that does not exist in the server address space. |
| Bad_AttributeIdInvalid | 0x80350000 | The attribute is not supported for the specified node. |
| Bad_IndexRangeInvalid | 0x80360000 | The syntax of the index range parameter is invalid. |
| Bad_IndexRangeNoData | 0x80370000 | No data exists within the range of indexes specified. |
| Bad_DataEncodingInvalid | 0x80380000 | The data encoding is invalid. |
| Bad_DataEncodingUnsupported | 0x80390000 | The server does not support the requested data encoding for the node. |
| Bad_NotReadable | 0x803A0000 | The access level does not allow reading or subscribing to the node. |
| Bad_NotWritable | 0x803B0000 | The access level does not allow writing to the node. |
| Bad_OutOfRange | 0x803C0000 | The value was out of range. |
| Bad_NotSupported | 0x803D0000 | The requested operation is not supported. |
| Bad_NotFound | 0x803E0000 | A requested item was not found or a search operation ended without success. |
| Bad_ObjectDeleted | 0x803F0000 | The object cannot be used because it has been deleted. |
| Bad_NotImplemented | 0x80400000 | Requested operation is not implemented. |
| Bad_MonitoringModeInvalid | 0x80410000 | The monitoring mode is invalid. |
| Bad_MonitoredItemIdInvalid | 0x80420000 | The monitoring item ID does not refer to a valid monitored item. |
| Bad_MonitoredItemFilterInvalid | 0x80430000 | The monitored item filter parameter is not valid. |
| Bad_MonitoredItemFilterUnsupported | 0x80440000 | The server does not support the requested monitored item filter. |
| Bad_FilterNotAllowed | 0x80450000 | A monitoring filter cannot be used in combination with the attribute specified. |
| Bad_StructureMissing | 0x80460000 | A mandatory structured parameter was missing or null. |
| Bad_EventFilterInvalid | 0x80470000 | The event filter is not valid. |
| Bad_ContentFilterInvalid | 0x80480000 | The content filter is not valid. |
| Bad_FilterOperatorInvalid | 0x80C10000 | An unregognized operator was provided in a filter. |
| Bad_FilterOperatorUnsupported | 0x80C20000 | A valid operator was provided but the server does not provide support for this filter operator. |
| Bad_FilterOperandCountMismatch | 0x80C30000 | The number of operands provided for the filter operator was less than expected for the operand provided. |
| Bad_FilterOperandInvalid | 0x80490000 | The operand used in a content filter is not valid. |
| Bad_FilterElementInvalid | 0x80C40000 | The referenced element is not a valid element in the content filter. |
| Bad_FilterLiteralInvalid | 0x80C50000 | The referenced literal is not a valid value. |
| Bad_ContinuationPointInvalid | 0x804A0000 | The continuation point is no longer valid. |
| Bad_NoContinuationPoints | 0x804B0000 | The operation could not be processed because all continuation points have been allocated. |
| Bad_ReferenceTypeIdInvalid | 0x804C0000 | The reference type ID is not valid. |
| Bad_BrowseDirectionInvalid | 0x804D0000 | The browse direction is not valid. |
| Bad_NodeNotInView | 0x804E0000 | The node is not part of the view. |
| Bad_ServerUriInvalid | 0x804F0000 | The ServerUri is not a valid URI. |
| Bad_ServerNameMissing | 0x80500000 | No ServerName was specified. |
| Bad_DiscoveryUrlMissing | 0x80510000 | No DiscoveryUrl was specified. |
| Bad_SempahoreFileMissing | 0x80520000 | The semaphore file specified by the client is not valid. |
| Bad_RequestTypeInvalid | 0x80530000 | The security token request type is not valid. |
| Bad_SecurityModeRejected | 0x80540000 | The security mode does not meet the requirements set by the server. |
| Bad_SecurityPolicyRejected | 0x80550000 | The security policy does not meet the requirements set by the server. |
| Bad_TooManySessions | 0x80560000 | The server has reached its maximum number of sessions. |
| Bad_UserSignatureInvalid | 0x80570000 | The user token signature is missing or invalid. |
| Bad_ApplicationSignatureInvalid | 0x80580000 | The signature generated with the client certificate is missing or invalid. |
| Bad_NoValidCertificates | 0x80590000 | The client did not provide at least one software certificate that is valid and meets the profile requirements for the server. |
| Bad_IdentityChangeNotSupported | 0x80C60000 | The server does not support changing the user identity assigned to the session. |
| Bad_RequestCancelledByRequest | 0x805A0000 | The request was cancelled by the client with the Cancel service. |
| Bad_ParentNodeIdInvalid | 0x805B0000 | The parent node ID does not refer to a valid node. |
| Bad_ReferenceNotAllowed | 0x805C0000 | The reference could not be created because it violates constraints imposed by the data model. |
| Bad_NodeIdRejected | 0x805D0000 | The requested node ID was rejected because it was invalid or server does not allow node IDs to be specified by the client. |
| Bad_NodeIdExists | 0x805E0000 | The requested node ID is already used by another node. |
| Bad_NodeClassInvalid | 0x805F0000 | The node class is not valid. |
| Bad_BrowseNameInvalid | 0x80600000 | The browse name is invalid. |
| Bad_BrowseNameDuplicated | 0x80610000 | The browse name is not unique among nodes that share the same relationship with the parent. |
| Bad_NodeAttributesInvalid | 0x80620000 | The node attributes are not valid for the node class. |
| Bad_TypeDefinitionInvalid | 0x80630000 | The type definition node ID does not reference an appropriate type node. |
| Bad_SourceNodeIdInvalid | 0x80640000 | The source node ID does not reference a valid node. |
| Bad_TargetNodeIdInvalid | 0x80650000 | The target node ID does not reference a valid node. |
| Bad_DuplicateReferenceNotAllowed | 0x80660000 | The reference type between the nodes is already defined. |
| Bad_InvalidSelfReference | 0x80670000 | The server does not allow this type of self-reference on this node. |
| Bad_ReferenceLocalOnly | 0x80680000 | The reference type is not valid for a reference to a remote server. |
| Bad_NoDeleteRights | 0x80690000 | The server will not allow the node to be deleted. |
| Uncertain_ReferenceNotDeleted | 0x40BC0000 | The server was not able to delete all target references. |
| Bad_ServerIndexInvalid | 0x806A0000 | The server index is not valid. |
| Bad_ViewIdUnknown | 0x806B0000 | The view ID does not refer to a valid view node. |
| Bad_ViewTimestampInvalid | 0x80C90000 | The view timestamp is not available or not supported. |
| Bad_ViewParameterMismatch | 0x80CA0000 | The view parameters are not consistent with each other. |
| Bad_ViewVersionInvalid | 0x80CB0000 | The view version is not available or not supported. |
| Uncertain_NotAllNodesAvailable | 0x40C00000 | The list of references may not be complete because the underlying system is not available. |
| Good_ResultsMayBeIncomplete | 0x00BA0000 | The server should have followed a reference to a node in a remote server but did not. The result set may be incomplete. |
| Bad_NotTypeDefinition | 0x80C80000 | The provided node ID was not a type definition node ID. |
| Uncertain_ReferenceOutOfServer | 0x406C0000 | One of the references to follow in the relative path references to a node in the address space in another server. |
| Bad_TooManyMatches | 0x806D0000 | The requested operation has too many matches to return. |
| Bad_QueryTooComplex | 0x806E0000 | The requested operation requires too many resources on the server. |
| Bad_NoMatch | 0x806F0000 | The requested operation has no match to return. |
| Bad_MaxAgeInvalid | 0x80700000 | The max age parameter is invalid. |
| Bad_HistoryOperationInvalid | 0x80710000 | The history details parameter is not valid. |
| Bad_HistoryOperationUnsupported | 0x80720000 | The server does not support the requested operation. |
| Bad_InvalidTimestampArgument | 0x80BD0000 | The defined timestamp to return was invalid. |
| Bad_WriteNotSupported | 0x80730000 | The server does not support writing the combination of value status and timestamps provided. |
| Bad_TypeMismatch | 0x80740000 | The value supplied for the attribute is not of the same type as the attribute's value. |
| Bad_MethodInvalid | 0x80750000 | The method ID does not refer to a method for the specified object. |
| Bad_ArgumentsMissing | 0x80760000 | The client did not specify all of the input arguments for the method. |
| Bad_TooManySubscriptions | 0x80770000 | The server has reached its maximum number of subscriptions. |
| Bad_TooManyPublishRequests | 0x80780000 | The server has reached the maximum number of queued publish requests. |
| Bad_NoSubscription | 0x80790000 | There is no subscription available for this session. |
| Bad_SequenceNumberUnknown | 0x807A0000 | The sequence number is unknown to the server. |
| Bad_MessageNotAvailable | 0x807B0000 | The requested notification message is no longer available. |
| Bad_InsufficientClientProfile | 0x807C0000 | The Client of the current Session does not support one or more Profiles that are necessary for the Subscription. |
| Bad_StateNotActive | 0x80BF0000 | The sub-state machine is not currently active. |
| Bad_TcpServerTooBusy | 0x807D0000 | The server cannot process the request because it is too busy. |
| Bad_TcpMessageTypeInvalid | 0x807E0000 | The type of the message specified in the header is invalid. |
| Bad_TcpSecureChannelUnknown | 0x807F0000 | The SecureChannelId and/or TokenId are not currently in use. |
| Bad_TcpMessageTooLarge | 0x80800000 | The size of the message specified in the header is too large. |
| Bad_TcpNotEnoughResources | 0x80810000 | There are not enough resources to process the request. |
| Bad_TcpInternalError | 0x80820000 | An internal error occurred. |
| Bad_TcpEndpointUrlInvalid | 0x80830000 | The serverdoes not recognize the QueryString specified. |
| Bad_RequestInterrupted | 0x80840000 | The request could not be sent because of a network interruption. |
| Bad_RequestTimeout | 0x80850000 | Timeout occurred while processing the request. |
| Bad_SecureChannelClosed | 0x80860000 | The secure channel has been closed. |
| Bad_SecureChannelTokenUnknown | 0x80870000 | The token has expired or is not recognized. |
| Bad_SequenceNumberInvalid | 0x80880000 | The sequence number is not valid. |
| Bad_ProtocolVersionUnsupported | 0x80BE0000 | The applications do not have compatible protocol versions. |
| Bad_ConfigurationError | 0x80890000 | There is a problem with the configuration that affects the usefulness of the value. |
| Bad_NotConnected | 0x808A0000 | The variable should receive its value from another variable but has never been configured to do so. |
| Bad_DeviceFailure | 0x808B0000 | There has been a failure in the device/data source that generates the value that has affected the value. |
| Bad_SensorFailure | 0x808C0000 | There has been a failure in the sensor from which the value is derived by the device/data source. |
| Bad_OutOfService | 0x808D0000 | The source of the data is not operational. |
| Bad_DeadbandFilterInvalid | 0x808E0000 | The deadband filter is not valid. |
| Uncertain_NoCommunicationLastUsableValue | 0x408F0000 | Communication to the data source has failed. The variable value is the last value that had a Good quality. |
| Uncertain_LastUsableValue | 0x40900000 | Whatever was updating this value has stopped doing so. |
| Uncertain_SubstituteValue | 0x40910000 | The value is an operational value that was manually overwritten. |
| Uncertain_InitialValue | 0x40920000 | The value is an initial value for a variable that normally receives its value from another variable. |
| Uncertain_SensorNotAccurate | 0x40930000 | The value is at one of the sensor limits. |
| Uncertain_EngineeringUnitsExceeded | 0x40940000 | The value is outside of the range of values defined for this parameter. |
| Uncertain_SubNormal | 0x40950000 | The value is derived from multiple sources and contains less than the required number of Good sources. |
| Good_LocalOverride | 0x00960000 | The value has been overridden. |
| Bad_RefreshInProgress | 0x80970000 | This Condition refresh failed or a Condition refresh operation is already in progress. |
| Bad_ConditionAlreadyDisabled | 0x80980000 | This condition has already been disabled. |
| Bad_ConditionAlreadyEnabled | 0x80CC0000 | This condition has already been enabled. |
| Bad_ConditionDisabled | 0x80990000 | The property is not available or this condition is disabled. |
| Bad_EventIdUnknown | 0x809A0000 | The specified event ID is not recognized. |
| Bad_EventNotAcknowledgeable | 0x80BB0000 | The event cannot be acknowledged. |
| Bad_DialogNotActive | 0x80CD0000 | The dialog condition is not active. |
| Bad_DialogResponseInvalid | 0x80CE0000 | The response is not valid for the dialog. |
| Bad_ConditionBranchAlreadyAcked | 0x80CF0000 | The condition branch has already been acknowledged. |
| Bad_ConditionBranchAlreadyConfirmed | 0x80D00000 | The condition branch has already been confirmed. |
| Bad_ConditionAlreadyShelved | 0x80D10000 | The condition has already been shelved. |
| Bad_ConditionNotShelved | 0x80D20000 | The condition is not currently shelved. |
| Bad_ShelvingTimeOutOfRange | 0x80D30000 | The shelving time is not within an acceptable range. |
| Bad_NoData | 0x809B0000 | No data exists for the requested time range or event filter. |
| Bad_BoundNotFound | 0x80D70000 | No data found to provide upper or lower bound value. |
| Bad_BoundNotSupported | 0x80D80000 | The server cannot retrieve a bound for the variable. |
| Bad_DataLost | 0x809D0000 | Data is missing due to collection started/stopped/lost. |
| Bad_DataUnavailable | 0x809E0000 | Expected data is unavailable for the requested time range due to an unmounted volume, an offline archive or tape, or similar reason for temporary unavailability. |
| Bad_EntryExists | 0x809F0000 | The data or event was not successfully inserted because a matching entry exists. |
| Bad_NoEntryExists | 0x80A00000 | The data or event was not successfully updated because no matching entry exists. |
| Bad_TimestampNotSupported | 0x80A10000 | The client requested history using a timestamp format the server does not support. In other words, the client requested ServerTimestamp when server only supports SourceTimestamp. |
| Good_EntryInserted | 0x00A20000 | The data or event was successfully inserted into the historical database. |
| Good_EntryReplaced | 0x00A30000 | The data or event was successfully replaced in the historical database. |
| Uncertain_DataSubNormal | 0x40A40000 | The value is derived from multiple values and contains less than the required number of Good values. |
| Good_NoData | 0x00A50000 | No data exists for the requested time range or event filter. |
| Good_MoreData | 0x00A60000 | More data exists for the requested time range or event filter. |
| Bad_AggregateListMismatch | 0x80D40000 | The requested number of Aggregates does not match the requested number of node IDs. |
| Bad_AggregateNotSupported | 0x80D50000 | The requested Aggregate is not support by the server. |
| Bad_AggregateInvalidInputs | 0x80D60000 | The aggregate value could not be derived due to invalid input data. |
| Bad_AggregateConfigurationRejected | 0x80DA0000 | The aggregate configuration is not valid for the specified node. |
| Good_DataIgnored | 0x00D90000 | The request specifies fields which are not valid for the EventType or cannot be saved by the historian. |
| Good_CommunicationEvent | 0x00A70000 | The communication layer has raised an event. |
| Good_ShutdownEvent | 0x00A80000 | The system is shutting down. |
| Good_CallAgain | 0x00A90000 | The operation is not finished and needs to be called again. |
| Good_NonCriticalTimeout | 0x00AA0000 | A non-critical timeout occurred. |
| Bad_InvalidArgument | 0x80AB0000 | One or more arguments are invalid. |
| Bad_ConnectionRejected | 0x80AC0000 | Could not establish a network connection to remote server. |
| Bad_Disconnect | 0x80AD0000 | The server has disconnected from the client. |
| Bad_ConnectionClosed | 0x80AE0000 | The network connection has been closed. |
| Bad_InvalidState | 0x80AF0000 | The operation cannot be completed because the object is closed, uninitialized or in some other invalid state. |
| Bad_EndOfStream | 0x80B00000 | Cannot move beyond end of the stream. |
| Bad_NoDataAvailable | 0x80B10000 | No data is currently available for reading from a non-blocking stream. |
| Bad_WaitingForResponse | 0x80B20000 | The asynchronous operation is waiting for a response. |
| Bad_OperationAbandoned | 0x80B30000 | The asynchronous operation was abandoned by the caller. |
| Bad_ExpectedStreamToBlock | 0x80B40000 | The stream did not return all data requested (possibly because it is a non-blocking stream). |
| Bad_WouldBlock | 0x80B50000 | Non-blocking behavior is required and the operation would block. |
| Bad_SyntaxError | 0x80B60000 | The value had an invalid syntax. |
| Bad_MaxConnectionsReached | 0x80B70000 | The operation could not be finished because all available connections are in use. |

Parent topic:

OPC UA VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=opc-ua-properties.html language=enus -->
## TOPIC 00053: OPC UA Properties

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `opc-ua-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/opc-ua-properties.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following properties with the Property Node to access OPC UA data. Dialog Condition Properties Limit Alarm Properties Notifier Properties Off-Normal Alarm Properties Variable Node Properties

### OPC UA Properties

Use the following properties with the Property Node to access OPC UA data.

[Dialog Condition Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_dialogcondition_prop)

[Limit Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_limitalarm_prop)

[Notifier Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_notifier_prop)

[Off-Normal Alarm Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_offnormalalarm_prop)

[Variable Node Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_node_prop)

Parent topic:

OPC UA VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=opc-ua-server-vis.html language=enus -->
## TOPIC 00054: OPC UA Server VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `opc-ua-server-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/opc-ua-server-vis.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA VIs Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the OPC UA Server VIs to create a customized OPC UA server application. Example Palette ObjectDescriptionAdd A

### OPC UA Server VIs

**Owning Palette:** OPC UA VIs

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the OPC UA Server VIs to create a customized OPC UA server application.

Example

| Palette Object | Description |
| --- | --- |
| Add Analog Item | Adds an analog item to the address space and configures the analog item. |
| Add Folder | Creates a folder under the parent folder in the address space. |
| Add Item | Adds an item as a child to a folder you specify. |
| Add Property | Adds a property to an item. |
| Add Trusted Clients | Adds trusted OPC UA client certificates to an OPC UA server. |
| Clear All Trusted Clients | Clears the OPC UA client certificates that an OPC UA server trusts. |
| Close | Closes and destroys an OPC UA server. After you close an OPC UA server, you lose all the data that belongs to the OPC UA server. |
| Create Server | Creates and initializes an OPC UA server. |
| Delete Node | Deletes a node, such as a folder, item, notifier, or condition. When you delete a folder, an item, or a notifier, you delete all the child nodes. |
| Read | Reads the value, timestamp, and status of a node. You must manually select the polymorphic instance to use. |
| Register Server | Registers an OPC UA server with the UA Local Discovery Server (LDS). This VI routinely registers the OPC UA server based on register rate. |
| Start | Starts an OPC UA server. After you start an OPC UA server, you cannot add or delete folders, items, notifiers, or conditions until the OPC UA server stops. Use the Stop VI to stop an OPC UA server. |
| Stop | Stops an OPC UA server and disconnects all OPC UA clients. When you stop an OPC UA server, you still keep all the folders, items, and properties. Use the Start VI to restart the OPC UA server. |
| Unregister Server | Unregisters a registered OPC UA server with the UA Local Discovery Server (LDS). |
| Write | Writes the value and status to a node from an OPC UA server. You must manually select the polymorphic instance to use. You can write to a node before the OPC UA server starts. |

| Subpalette | Description |
| --- | --- |
| Alarms and Conditions VIs | Use the Alarms and Conditions VIs to subscribe to alarms and conditions for OPC UA server applications. |
| Historical Access VIs | Use the Historical Access VIs to access historical data and events for OPC UA server applications. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the OPC UA Server VIs.

Parent topic:

OPC UA VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=opc-ua-vis.html language=enus -->
## TOPIC 00055: OPC UA VIs

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `opc-ua-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/opc-ua-vis.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: November 2020, 376802D-01Owning Palette: Data Communication VIs and Functions Requires: OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target. Use the OPC UA VIs to create a customized OPC UA server applica

### OPC UA VIs

November 2020, 376802D-01

**Owning Palette:** Data Communication VIs and Functions

**Requires:** OPC UA Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the OPC UA VIs to create a customized OPC UA server application or OPC UA client application. You can use the OPC UA Server VIs and the OPC UA Client VIs to exchange data between OPC UA client and OPC UA server applications.

You must activate the LabVIEW Real-Time Module to use the OPC UA VIs on a real-time target.

The VIs on this palette can return general LabVIEW error codes or specific OPC UA error codes.

| Palette Object | Description |
| --- | --- |
| Create Certificate | Creates a pair of certificate files with the name you specify. You can use the certificate files to create an OPC UA server or connect to an OPC UA server. |

| Subpalette | Description |
| --- | --- |
| OPC UA Client VIs | Use the OPC UA Client VIs to create a customized OPC UA client application. |
| OPC UA Server VIs | Use the OPC UA Server VIs to create a customized OPC UA server application. |

© 2017–2020 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=prompt-property.html language=enus -->
## TOPIC 00056: Prompt Property

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `prompt-property.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/prompt-property.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Requires: OPC UA Toolkit Class: Dialog Condition Properties A dialog prompt to display to the end user. Remarks The following table lists the characteristics of this property. Permissions Before Server Starts Read/Write Permissions After Server Starts Read-only Data Type

### Prompt Property

**Requires:** OPC UA Toolkit

**Class:** [Dialog Condition Properties](/csh?context=labview-opc-ua-toolkit_labview-opc-ua-toolkit-api-ref_opcua_dialogcondition_prop)

A dialog prompt to display to the end user.
Remarks

The following table lists the characteristics of this property.

| Permissions Before Server Starts | Read/Write |
| --- | --- |
| Permissions After Server Starts | Read-only |
| Data Type |  |

Parent topic:

Dialog Condition Properties

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=register-server-vi.html language=enus -->
## TOPIC 00057: Register Server VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `register-server-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/register-server-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: OPC UA Server VIs Requires: OPC UA Toolkit Registers an OPC UA server with the UA Local Discovery Server (LDS). This VI routinely registers the OPC UA server based on register rate. OPC UA server refnum in specifies the reference data value of the OPC UA server. local discovery serve

### Register Server VI

**Owning Palette:** OPC UA Server VIs

**Requires:** OPC UA Toolkit

Registers an OPC UA server with the UA Local Discovery Server (LDS). This VI routinely registers the OPC UA server based on **register rate**.

[IMAGE alt='image' src='images/opcua_register_server.gif']

|  | OPC UA server refnum in specifies the reference data value of the OPC UA server. |
| --- | --- |
|  | local discovery server certificate file specifies the path of the certificate file that the UA Local Discovery Server (LDS) uses. |
|  | register rate specifies the rate, in minutes, at which this VI registers the OPC UA server. The default is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | local discovery server URL specifies the URL of the UA Local Discovery Server (LDS) on the local MulticastSubnet. The default is opc.tcp://localhost:4840. Refer to the OPC UA specification for more information about the LDS. |
|  | OPC UA server refnum out returns the reference data value of the OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Register Server Details

Before you use the Register Server VI, you must install the UA Local Discovery Server (LDS) and make the OPC UA server and the LDS trust each other. Refer to the OPC Foundation website at www.opcfoundation.org to download the LDS. Visit ni.com/info and enter the Info Code ex9fm6 to access the How Do I Make an OPC UA Server and the UA Local Discovery Server Trust Each Other? NI support document, for information about making OPC UA servers and the LDS trust each other.

When you use the Register Server VI to register an OPC UA server, the status of the registered OPC UA server in the LDS is either online or offline. Whether the OPC UA client can connect to the registered OPC UA server depends on the status of the OPC UA server. You can use the Start VI and Stop VI to change the status of the registered OPC UA server.

The following table lists the status of the registered OPC UA server in the LDS.

| Registered OPC UA Server Status | Description | Effects on the OPC UA Client |
| --- | --- | --- |
| Online | The registered OPC UA server is running. | The OPC UA client can find the name and endpoint URL of the registered OPC UA server in the LDS and connect to the OPC UA server. |
| Offline | The registered OPC UA server is not running. | The OPC UA client can find the name of the registered OPC UA server in the LDS. However, the OPC UA client cannot connect to the OPC UA server. |

Parent topic:

OPC UA Server VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=respond-acknowledgeable-condition-vi.html language=enus -->
## TOPIC 00058: Respond Acknowledgeable Condition VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `respond-acknowledgeable-condition-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/respond-acknowledgeable-condition-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Alarms and Conditions VIs Requires: OPC UA Toolkit Responds to an acknowledgeable condition by confirming, acknowledging, or adding comments to the condition. Acknowledgeable conditions expose states to indicate whether a condition must be acknowledged or confirmed. Example OPC UA cl

### Respond Acknowledgeable Condition VI

**Owning Palette:** Alarms and Conditions VIs

**Requires:** OPC UA Toolkit

Responds to an acknowledgeable condition by confirming, acknowledging, or adding comments to the condition. Acknowledgeable conditions expose states to indicate whether a condition must be acknowledged or confirmed.

Example

[IMAGE alt='image' src='images/Respond_AcknowledgeableCondition.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | condition node ID specifies the ID of an acknowledgeable condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | request specifies information that this VI uses to respond to an acknowledgeable condition. method specifies the operation this VI executes. 0Add Comment1Acknowledge2Confirm event ID specifies the event ID. comment specifies the string to associate with a certain state of condition. |
|  | method specifies the operation this VI executes. 0Add Comment1Acknowledge2Confirm |
| 0 | Add Comment |
| 1 | Acknowledge |
| 2 | Confirm |
|  | event ID specifies the event ID. |
|  | comment specifies the string to associate with a certain state of condition. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Respond Acknowledgeable Condition VI.

Parent topic:

Alarms and Conditions VIs

<!--NI_TOPIC bundle=labview-opc-ua-toolkit-api-ref path=respond-dialog-condition-vi.html language=enus -->
## TOPIC 00059: Respond Dialog Condition VI

- bundle_id: `labview-opc-ua-toolkit-api-ref`
- source_path: `respond-dialog-condition-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-opc-ua-toolkit-api-ref/raw/resource/enus/respond-dialog-condition-vi.html
- document_id: `labview-opc-ua-toolkit-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Owning Palette: Alarms and Conditions VIs Requires: OPC UA Toolkit Returns a response option and ends a dialog. Example OPC UA client refnum in specifies the reference for the OPC UA client. condition node ID specifies the ID of the dialog condition node. The format of the node ID is ns=<namespace i

### Respond Dialog Condition VI

**Owning Palette:** Alarms and Conditions VIs

**Requires:** OPC UA Toolkit

Returns a response option and ends a dialog.

Example

[IMAGE alt='image' src='images/Respond_DialogCondition.gif']

|  | OPC UA client refnum in specifies the reference for the OPC UA client. |
| --- | --- |
|  | condition node ID specifies the ID of the dialog condition node. The format of the node ID is ns=<namespace index>;<identifier type>=<identifier>. A node ID contains the following components: namespace index is a base 10 number that indicates the namespace of the node ID. Note If namespace index is 0, the format of the node ID can be <identifier type>=<identifier>. The namespace index for a node that you created with the OPC UA Toolkit is 2. identifier type represents the type of the identifier and has the following values: ValueIdentifier TypeiNumericsStringgGUIDbOpaque identifier is a string value that represents the name of the identifier. The format of the node ID can also be ns=<namespace index>;<identifier type>=<identifier>@<index>:<index>. For example, ns=2;s=Folder.Array@1:2. This format only applies to the array data type and allows you to read a single element or a range of elements of an array. You cannot use @ in a node name. For backwards compatibility, condition node ID also accepts node paths as input for OPC UA servers only. You can regard the node path as the string type identifier of the node ID. For example, a node path can be Device.folder.item. |
| Value | Identifier Type |
| i | Numeric |
| s | String |
| g | GUID |
| b | Opaque |
|  | response specifies a response option. 1OK2Cancel |
| 1 | OK |
| 2 | Cancel |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | timeout specifies the maximum time, in milliseconds, that this VI waits to get a response from the OPC UA server. The default is 5000. |
|  | OPC UA client refnum out returns the reference for the OPC UA client. |
|  | service status returns the status of an OPC UA service call. OPC UA services contain parameters that are conveyed between an OPC UA client and an OPC UA server. |
|  | error out contains error information. This output provides standard error out functionality. |

Example

Refer to the OPC UA Demo.lvproj in the labview\examples\Data Communication\OPCUA directory for an example of using the Respond Dialog Condition VI.

Parent topic:

Alarms and Conditions VIs
