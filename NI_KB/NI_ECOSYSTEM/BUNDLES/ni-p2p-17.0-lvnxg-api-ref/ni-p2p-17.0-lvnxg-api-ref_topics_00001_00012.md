# NI DOCUMENT BUNDLE: ni-p2p-17.0-lvnxg-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-p2p-17.0-lvnxg-api-ref start=1 end=12 -->
<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=advanced-streaming.html language=enus -->
## TOPIC 00001: Advanced Streaming

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `advanced-streaming.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/advanced-streaming.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Peer to Peer Streaming nodes link and unlink peer-to-peer streams. In general, you only need to use these functions when the targets are reset or encounter errors. Otherwise, use Create Peer to Peer Stream or Destroy Peer to Peer Stream to link and unlink streams.

Advanced Streaming

Advanced Peer to Peer Streaming nodes link and unlink peer-to-peer streams.

In general, you only need to use these functions when the targets are reset or encounter errors. Otherwise, use Create Peer to Peer Stream or Destroy Peer to Peer Stream to link and unlink streams.

Peer-to-Peer Streaming Nodes

Use NI Peer-to-Peer nodes to manage the streaming of data directly between peripherals without sending the data through a host device.

Link Peer to Peer Stream

Links the writer and reader in the stream you specify.

Unlink Peer to Peer Stream

Unlinks the reader and writer in the stream you specify.

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=create-peer-to-peer-stream.html language=enus -->
## TOPIC 00002: Create Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `create-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/create-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Links a writer and reader and creates a stream between them. writer The device resource that writes data to the stream. reader The device resource that reads data from the stream. error in Error conditions that occur before this node runs. The node responds to this input according to standard error

Create Peer to Peer Stream

Links a writer and reader and creates a stream between them.

[IMAGE alt='1378' src='Create_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### writer

The device resource that writes data to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### reader

The device resource that reads data from the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable stream

A Boolean control that prepares the stream to transmit data.

| True | Prepares the stream to transmit data. |
| --- | --- |
| False | Waits to enable the stream until Enable Peer to Peer Stream is called. |

Default value: True

##### Enabling the Stream Programmatically

To enable the stream when the writer and reader are ready to transfer data, set enable stream to 
 False and use Enable Peer to Peer Stream to enable the stream.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=default.html language=enus -->
## TOPIC 00003: Peer-to-Peer Streaming Nodes

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `default.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/default.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use NI Peer-to-Peer nodes to manage the streaming of data directly between peripherals without sending the data through a host device.

Peer-to-Peer Streaming Nodes

Use NI Peer-to-Peer nodes to manage the streaming of data directly between peripherals without sending the data through a host device.

Create Peer to Peer Stream

Links a writer and reader and creates a stream between them.

Destroy Peer to Peer Stream

Unlinks the writer and reader and purges data from the stream.

Enable Peer to Peer Stream

Prepares the stream for data transmission.

Flush and Disable Peer to Peer Stream Multimode Function

Immediately flushes data from the writer and disables the stream.

Disable Peer to Peer Stream

Immediately disables a stream without flushing data from the writer.

Peer-to-Peer Stream Properties

Changes or reads properties of a peer-to-peer stream.

Advanced Streaming

Advanced Peer to Peer Streaming nodes link and unlink peer-to-peer streams.

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=destroy-peer-to-peer-stream.html language=enus -->
## TOPIC 00004: Destroy Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `destroy-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/destroy-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlinks the writer and reader and purges data from the stream. Any existing data in the writer is lost. If a stream is enabled, this function disables the stream without flushing the writer before unlinking the reader and writer. session in A reference to the stream. error in Error conditions that o

Destroy Peer to Peer Stream

Unlinks the writer and reader and purges data from the stream.

Any existing data in the writer is lost. If a stream is enabled, this function disables the stream without flushing the writer before unlinking the reader and writer.

[IMAGE alt='1378' src='Destroy_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Flushing Existing Data

To guarantee all existing data in the writer is flushed to the reader before disabling the stream, use Flush and Disable Peer to Peer Stream.

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=disable-peer-to-peer-stream.html language=enus -->
## TOPIC 00005: Disable Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `disable-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/disable-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately disables a stream without flushing data from the writer. Any existing data in the writer is lost. To avoid data loss and guarantee all existing data in the writer is flushed to the reader before disabling the stream, use Flush and Disable Peer to Peer Stream. session in A reference to th

Disable Peer to Peer Stream

Immediately disables a stream without flushing data from the writer.

Any existing data in the writer is lost. To avoid data loss and guarantee all existing data in the writer is flushed to the reader before disabling the stream, use Flush and Disable Peer to Peer Stream.

[IMAGE alt='1378' src='Disable_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=enable-peer-to-peer-stream.html language=enus -->
## TOPIC 00006: Enable Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `enable-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/enable-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Prepares the stream for data transmission. After this function runs, the stream is capable of transmitting data from the writer to the reader. You must enable the stream before you can transmit data. session in A reference to the stream. error in Error conditions that occur before this node runs. Th

Enable Peer to Peer Stream

Prepares the stream for data transmission.

After this function runs, the stream is capable of transmitting data from the writer to the reader. You must enable the stream before you can transmit data.

[IMAGE alt='1378' src='Enable_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Enabling a Stream Without This Function

enable stream

Create Peer to Peer Stream

True

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=flush-disable-peer-to-peer-stream-no-timeout.html language=enus -->
## TOPIC 00007: No Timeout

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `flush-disable-peer-to-peer-stream-no-timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/flush-disable-peer-to-peer-stream-no-timeout.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately flushes data from the writer and disables the stream. This function waits indefinitely for the flush to complete. Flushing the writer prevents the writer from accepting new data and sends all existing data in the writer to the stream. If you do not want to flush the writer before disabli

No Timeout

Immediately flushes data from the writer and disables the stream. This function waits indefinitely for the flush to complete.

Flushing the writer prevents the writer from accepting new data and sends all existing data in the writer to the stream. If you do not want to flush the writer before disabling the stream, use Disable Peer to Peer Stream instead of this function.

[IMAGE alt='1378' src='Flush_and_Disable_Peer_to_Peer_Stream_(No_Timeout).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Flush and Disable Peer to Peer Stream Multimode Function

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=flush-disable-peer-to-peer-stream-timeout.html language=enus -->
## TOPIC 00008: Timeout

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `flush-disable-peer-to-peer-stream-timeout.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/flush-disable-peer-to-peer-stream-timeout.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately flushes data from the writer and disables the stream. In this mode, you specify an amount of time to wait for the flush to complete. Flushing the writer prevents the writer from accepting new data and sends all existing data in the writer to the stream. If you do not want to flush the wr

Timeout

Immediately flushes data from the writer and disables the stream. In this mode, you specify an amount of time to wait for the flush to complete.

Flushing the writer prevents the writer from accepting new data and sends all existing data in the writer to the stream.

If you do not want to flush the writer before disabling the stream, use Disable Peer to Peer Stream.

[IMAGE alt='1378' src='Flush_and_Disable_Peer_to_Peer_Stream_(Timeout).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### flush timeout

The amount of time, in milliseconds, to wait for the function to complete the flush of the writer.

If the flush does not complete within the time you specify in flush timeout, the function disables the stream and any data remaining in the writer is lost.

##### Specifying an Indefinite Timeout

To wait indefinitely, set flush timeout to 
 -1. Alternately, you can use Flush and Disable Peer to Peer Stream (No Timeout) to wait indefinitely.

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Specifying a Timeout

This function waits until the flush is complete or the time you specify in flush timeout is exceeded. If the function does not time out, the reader receives all data from the writer before the stream transitions to the Disabled state. If the function does time out, you lose any data remaining on the writer side of the stream. If this function times out, verify that the value for flush timeout is appropriate for the number of elements you expect to flush and that the reader continues to read data until the stream is empty.

Parent topic:

Flush and Disable Peer to Peer Stream Multimode Function

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=flush-disable-peer-to-peer-stream.html language=enus -->
## TOPIC 00009: Flush and Disable Peer to Peer Stream Multimode Function

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `flush-disable-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/flush-disable-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Immediately flushes data from the writer and disables the stream.

Flush and Disable Peer to Peer Stream Multimode Function

Immediately flushes data from the writer and disables the stream.

Peer-to-Peer Streaming Nodes

Use NI Peer-to-Peer nodes to manage the streaming of data directly between peripherals without sending the data through a host device.

No Timeout

Immediately flushes data from the writer and disables the stream. This function waits indefinitely for the flush to complete.

Timeout

Immediately flushes data from the writer and disables the stream. In this mode, you specify an amount of time to wait for the flush to complete.

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=link-peer-to-peer-stream.html language=enus -->
## TOPIC 00010: Link Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `link-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/link-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Links the writer and reader in the stream you specify. session in A reference to the stream. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error session out A reference to th

Link Peer to Peer Stream

Links the writer and reader in the stream you specify.

[IMAGE alt='1378' src='Link_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Linking a Stream

Linking a stream exchanges hardware addresses between the reader and the writer. You must use an application on the host to link the stream before you can enable the stream. If a stream is in the Unlinked state when this function runs. the stream becomes linked and transitions to the Disabled state. You can use the applications on the host, writer, or reader to enable the stream when the stream is in a Disabled state.

Parent topic:

Advanced Streaming

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=nip2p-stream-properties.html language=enus -->
## TOPIC 00011: Peer-to-Peer Stream Properties

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `nip2p-stream-properties.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/nip2p-stream-properties.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes or reads properties of a peer-to-peer stream. This Property Node is configured to access peer-to-peer stream properties. This function operates in the same way as a standard Property Node. stream in The session associated with the stream for which you want to get or alter properties. Use Cre

Peer-to-Peer Stream Properties

Changes or reads properties of a peer-to-peer stream.

This Property Node is configured to access peer-to-peer stream properties. This function operates in the same way as a standard Property Node.

[IMAGE alt='1378' src='PropertyNode.nip2pStream.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### stream in

The session associated with the stream for which you want to get or alter properties.

Use Create Peer to Peer Stream to create a reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### stream out

Returns stream in unchanged.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Peer-to-Peer Streaming Nodes

<!--NI_TOPIC bundle=ni-p2p-17.0-lvnxg-api-ref path=unlink-peer-to-peer-stream.html language=enus -->
## TOPIC 00012: Unlink Peer to Peer Stream

- bundle_id: `ni-p2p-17.0-lvnxg-api-ref`
- source_path: `unlink-peer-to-peer-stream.html`
- source_url: https://docs-be.ni.com/bundle/ni-p2p-17.0-lvnxg-api-ref/raw/resource/enus/unlink-peer-to-peer-stream.html
- document_id: `ni-p2p-17.0-lvnxg-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unlinks the reader and writer in the stream you specify. If the stream is enabled, this function disables the stream before un-linking the reader and writer. session in A reference to the stream. error in Error conditions that occur before this node runs. Unlike most nodes, this node runs normally e

Unlink Peer to Peer Stream

Unlinks the reader and writer in the stream you specify.

If the stream is enabled, this function disables the stream before un-linking the reader and writer.

[IMAGE alt='1378' src='Unlink_Peer_to_Peer_Stream.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cio.png']

##### session in

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/iio.png']

##### session out

A reference to the stream.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Advanced Streaming
