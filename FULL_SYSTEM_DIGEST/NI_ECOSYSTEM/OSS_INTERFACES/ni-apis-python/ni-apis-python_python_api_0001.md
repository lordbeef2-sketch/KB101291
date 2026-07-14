# NI PYTHON API DIGEST: ni-apis-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/ni-apis-python commit=9a74b25be948b236787a899f5b2bfbecefeaa94d -->

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/docs/conf.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/src/ni_grpc_extensions/__init__.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/src/ni_grpc_extensions/__init__.py

### MODULE DOCSTRING

gRPC extensions.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/src/ni_grpc_extensions/_tracelogging.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/src/ni_grpc_extensions/_tracelogging.py

- `_LEVEL_LOG_ALWAYS = 0`

- `_LEVEL_CRITICAL = 1`

- `_LEVEL_ERROR = 3`

- `_LEVEL_WARNING = 3`

- `_LEVEL_INFO = 4`

- `_LEVEL_VERBOSE = 5`

- `_OPCODE_INFO = 0`

- `_OPCODE_START = 1`

- `_OPCODE_STOP = 2`

- `_KEYWORD_NONE = 0`

- `_KEYWORD_GRPC = 1 << 0`

- `_TASK_GRPC_CLIENT_CALL = 1`

- `_TASK_GRPC_SERVER_CALL = 2`

### `def is_enabled() -> bool`

Queries whether the event provider is enabled.

### `def log_grpc_client_call_start(method_name: str) -> uuid.UUID | None`

Log when starting a gRPC client call.

### `def log_grpc_client_call_stop(method_name: str, activity_id: uuid.UUID | None=None) -> None`

Log when a gRPC client call has completed.

### `def log_grpc_client_call_streaming_request(method_name: str) -> None`

Log when a gRPC client call is sending a client-streaming request.

### `def log_grpc_client_call_streaming_response(method_name: str) -> None`

Log when a gRPC client call has received a server-streaming response.

### `def log_grpc_server_call_start(method_name: str) -> uuid.UUID | None`

Log when starting a gRPC server call.

### `def log_grpc_server_call_stop(method_name: str, activity_id: uuid.UUID | None=None) -> None`

Log when a gRPC server call has completed.

### `def log_grpc_server_call_streaming_request(method_name: str) -> None`

Log when a gRPC server call is sending a server-streaming request.

### `def log_grpc_server_call_streaming_response(method_name: str) -> None`

Log when a gRPC server call has received a server-streaming response.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/src/ni_grpc_extensions/channelpool.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/src/ni_grpc_extensions/channelpool.py

### MODULE DOCSTRING

gRPC channel pool.

### `class GrpcChannelPool()`

Class that manages :any:`grpc.Channel` lifetimes.

#### `def __init__(self) -> None`

Initialize the :class:`GrpcChannelPool` object.

#### `def __enter__(self: Self) -> Self`

Enter the runtime context of the GrpcChannelPool.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> Literal[False]`

Exit the runtime context of the GrpcChannelPool.

#### `def get_channel(self, target: str) -> grpc.Channel`

Return a gRPC channel.

        Args:
            target (str): The server address

        

#### `def close(self) -> None`

Close channels opened by get_channel().

#### `def _create_channel(self, target: str) -> grpc.Channel`

#### `def _is_local(self, target: str) -> bool`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/src/ni_grpc_extensions/loggers.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/src/ni_grpc_extensions/loggers.py

### MODULE DOCSTRING

gRPC logging interceptors.

### `class ClientLogger(grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor, grpc.StreamUnaryClientInterceptor, grpc.StreamStreamClientInterceptor)`

Intercepts gRPC client calls and logs them for debugging.

#### `def is_enabled(cls) -> bool`

Indicates whether gRPC client call logging is enabled for the current log level.

#### `def intercept_unary_unary(self, continuation: Callable[[grpc.ClientCallDetails, grpc._TRequest], grpc._CallFuture[grpc._TResponse]], client_call_details: grpc.ClientCallDetails, request: grpc._TRequest) -> grpc._CallFuture[grpc._TResponse]`

Intercept and log a unary call.

#### `def intercept_unary_stream(self, continuation: Callable[[grpc.ClientCallDetails, grpc._TRequest], grpc._CallIterator[grpc._TResponse]], client_call_details: grpc.ClientCallDetails, request: grpc._TRequest) -> grpc._CallIterator[grpc._TResponse]`

Intercept and log a server-streaming call.

#### `def intercept_stream_unary(self, continuation: Callable[[grpc.ClientCallDetails, Iterator[grpc._TRequest]], grpc._CallFuture[grpc._TResponse]], client_call_details: grpc.ClientCallDetails, request_iterator: Iterator[grpc._TRequest]) -> grpc._CallFuture[grpc._TResponse]`

Intercept and log a client-streaming call.

#### `def intercept_stream_stream(self, continuation: Callable[[grpc.ClientCallDetails, Iterator[grpc._TRequest]], grpc._CallIterator[grpc._TResponse]], client_call_details: grpc.ClientCallDetails, request_iterator: Iterator[grpc._TRequest]) -> grpc._CallIterator[grpc._TResponse]`

Intercept and log a bidirectional streaming call.

### `class ServerLogger(grpc.ServerInterceptor)`

Intercepts gRPC server calls and logs them for debugging.

#### `def is_enabled(cls) -> bool`

Indicates whether gRPC client call logging is enabled for the current log level.

#### `def intercept_service(self, continuation: Callable[[grpc.HandlerCallDetails], grpc.RpcMethodHandler[grpc._TRequest, grpc._TResponse] | None], handler_call_details: grpc.HandlerCallDetails) -> grpc.RpcMethodHandler[grpc._TRequest, grpc._TResponse] | None`

Intercept and log a server call.

#### `def _log_unary_unary(self, call_logger: _CallLogger, handler_function: Callable[[grpc._TRequest, grpc.ServicerContext], grpc._TResponse], request: grpc._TRequest, context: grpc.ServicerContext) -> grpc._TResponse`

#### `def _log_unary_stream(self, call_logger: _CallLogger, handler_function: Callable[[grpc._TRequest, grpc.ServicerContext], Iterator[grpc._TResponse]], request: grpc._TRequest, context: grpc.ServicerContext) -> Iterator[grpc._TResponse]`

#### `def _log_stream_unary(self, call_logger: _CallLogger, handler_function: Callable[[Iterator[grpc._TRequest], grpc.ServicerContext], grpc._TResponse], request_iterator: Iterator[grpc._TRequest], context: grpc.ServicerContext) -> grpc._TResponse`

#### `def _log_stream_stream(self, call_logger: _CallLogger, handler_function: Callable[[Iterator[grpc._TRequest], grpc.ServicerContext], Iterator[grpc._TResponse]], request_iterator: Iterator[grpc._TRequest], context: grpc.ServicerContext) -> Iterator[grpc._TResponse]`

### `class _CallLogger(abc.ABC)`

Logs a single call.

#### `def __init__(self) -> None`

#### `def close(self, exception: BaseException | None=None) -> None`

#### `def _close(self, exception: BaseException | None) -> None`

#### `def __enter__(self: Self) -> Self`

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

#### `def log_streaming_request(self) -> None`

#### `def log_streaming_response(self) -> None`

### `class _ClientCallLogger(_CallLogger)`

#### `def is_enabled(cls) -> bool`

#### `def __init__(self, method_name: str) -> None`

#### `def _close(self, exception: BaseException | None=None) -> None`

#### `def log_streaming_request(self) -> None`

#### `def log_streaming_response(self) -> None`

### `class _ServerCallLogger(_CallLogger)`

#### `def is_enabled(cls) -> bool`

#### `def __init__(self, method_name: str) -> None`

#### `def _close(self, exception: BaseException | None=None) -> None`

#### `def log_streaming_request(self) -> None`

#### `def log_streaming_response(self) -> None`

### `def _get_status_code(exception: BaseException | None) -> grpc.StatusCode`

- `_T = TypeVar('_T')`

### `class _LoggingRequestIterator(Generic[_T])`

#### `def __init__(self, call_logger: _CallLogger, inner_iterator: Iterator[_T]) -> None`

#### `def __iter__(self) -> Iterator[_T]`

#### `def __next__(self) -> _T`

### `class _LoggingResponseIterator(Generic[_T])`

#### `def __init__(self, call_logger: _CallLogger, inner_iterator: Iterator[_T]) -> None`

#### `def __iter__(self) -> Iterator[_T]`

#### `def __next__(self) -> _T`

### `class _LoggingResponseCallFuture(_CallFuture[_T])`

#### `def __init__(self, call_logger: _CallLogger, inner_call_future: grpc._CallFuture[_T]) -> None`

#### `def __getattr__(self, name: str) -> Any`

#### `def result(self, timeout: float | None=None) -> _T`

#### `def exception(self, timeout: float | None=None) -> Exception | None`

#### `def traceback(self, timeout: float | None=None) -> Any`

### `class _LoggingResponseCallIterator(_CallIterator[_T])`

#### `def __init__(self, call_logger: _CallLogger, inner_call_iterator: grpc._CallIterator[_T]) -> None`

#### `def __getattr__(self, name: str) -> Any`

#### `def __iter__(self) -> Iterator[_T]`

#### `def __next__(self) -> _T`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for ni.grpc.extensions.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/tests/unit/test_channel_pool.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/tests/unit/test_channel_pool.py

### `def test___channel_pool___is_local___returns_expected_result(target: str, expected_result: bool) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni-grpc-extensions/tests/unit/test_loggers.py -->
## PYTHON MODULE: packages/ni-grpc-extensions/tests/unit/test_loggers.py

### `def test___client_logger___logs_grpc_call(caplog: LogCaptureFixture) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.client/src/ni/datamonikers/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.client/src/ni/datamonikers/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Data Moniker Service.

- `__all__ = ['MonikerClient']`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.client/src/ni/datamonikers/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.client/src/ni/datamonikers/v1/client/_client.py

### MODULE DOCSTRING

Client for accessing the NI Data Moniker Service.

### `class MonikerClient()`

Client for accessing the NI Data Moniker Service.

#### `def __init__(self, *, service_location: str | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the Moniker Client.

        Args:
            service_location: The address of the data moniker service location (recommended).

            grpc_channel: A data moniker gRPC channel (optional).

            grpc_channel_pool: A gRPC channel pool (recommended).

        Either `service_location` or `grpc_channel` must be provided. If both are provided,
        `grpc_channel` takes precedence.
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the MonikerClient.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the MonikerClient.

#### `def close(self) -> None`

Close the client and clean up resources that it owns.

#### `def _get_stub(self) -> data_moniker_pb2_grpc.MonikerServiceStub`

#### `def begin_sideband_stream(self, request: data_moniker_pb2.BeginMonikerSidebandStreamRequest) -> data_moniker_pb2.BeginMonikerSidebandStreamResponse`

Begin a sideband stream.

#### `def stream_read(self, moniker_list: data_moniker_pb2.MonikerList) -> Iterator[data_moniker_pb2.MonikerReadResult]`

Stream read data from monikers.

#### `def stream_write(self, requests: Iterator[data_moniker_pb2.MonikerWriteRequest]) -> Iterator[data_moniker_pb2.StreamWriteResponse]`

Stream write data to monikers.

#### `def stream_read_write(self, requests: Iterator[data_moniker_pb2.MonikerWriteRequest]) -> Iterator[data_moniker_pb2.MonikerReadResult]`

Stream read and write data with monikers.

#### `def read_from_moniker(self, moniker: data_moniker_pb2.Moniker) -> data_moniker_pb2.ReadFromMonikerResult`

Read data from a moniker.

#### `def write_to_moniker(self, request: data_moniker_pb2.WriteToMonikerRequest) -> data_moniker_pb2.WriteToMonikerResponse`

Write data to a moniker.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.client/tests/unit/test_moniker_client.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.client/tests/unit/test_moniker_client.py

### `def test__begin_sideband_stream__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def test__stream_read__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def test__stream_write__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def test__stream_read_write__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def test__read_from_moniker__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def test__write_to_moniker__request_and_response_pass_through(moniker_client: MonikerClient, moniker_stub: Mock) -> None`

### `def moniker_client(mocker: MockerFixture, moniker_stub: Mock) -> MonikerClient`

Create a Client with a mock MonikerServiceStub.

### `def moniker_stub(mocker: MockerFixture) -> Mock`

Create a mock MonikerServiceStub.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.proto/src/ni/datamonikers/v1/data_moniker_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.proto/src/ni/datamonikers/v1/data_moniker_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ni/datamonikers/v1/data_moniker.proto\x12\x12ni.datamonikers.v1\x1a\x19google/protobuf/any.proto"O\n\x07Moniker\x12\x18\n\x10service_location\x18\x01 \x01(\t\x12\x13\n\x0bdata_source\x18\x02 \x01(\t\x12\x15\n\rdata_instance\x18\x03 \x01(\x03"5\n\rMonikerValues\x12$\n\x06values\x18\x01 \x03(\x0b2\x14.google.protobuf.Any"\x94\x01\n\x0bMonikerList\x12\x1c\n\x10is_initial_write\x18\x01 \x01(\x08B\x02\x18\x01\x122\n\rread_monikers\x18\x02 \x03(\x0b2\x1b.ni.datamonikers.v1.Moniker\x123\n\x0ewrite_monikers\x18\x03 \x03(\x0b2\x1b.ni.datamonikers.v1.Moniker"\x8e\x01\n!BeginMonikerSidebandStreamRequest\x126\n\x08strategy\x18\x01 \x01(\x0e2$.ni.datamonikers.v1.SidebandStrategy\x121\n\x08monikers\x18\x02 \x01(\x0b2\x1f.ni.datamonikers.v1.MonikerList"\xa6\x01\n"BeginMonikerSidebandStreamResponse\x126\n\x08strategy\x18\x01 \x01(\x0e2$.ni.datamonikers.v1.SidebandStrategy\x12\x16\n\x0econnection_url\x18\x02 \x01(\t\x12\x1b\n\x13sideband_identifier\x18\x03 \x01(\t\x12\x13\n\x0bbuffer_size\x18\x04 \x01(\x12"\x8b\x01\n\x13MonikerWriteRequest\x123\n\x08monikers\x18\x01 \x01(\x0b2\x1f.ni.datamonikers.v1.MonikerListH\x00\x121\n\x04data\x18\x02 \x01(\x0b2!.ni.datamonikers.v1.MonikerValuesH\x00B\x0c\n\nwrite_data"D\n\x11MonikerReadResult\x12/\n\x04data\x18\x01 \x01(\x0b2!.ni.datamonikers.v1.MonikerValues"\x15\n\x13StreamWriteResponse"<\n\x15ReadFromMonikerResult\x12#\n\x05value\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"j\n\x15WriteToMonikerRequest\x12,\n\x07moniker\x18\x01 \x01(\x0b2\x1b.ni.datamonikers.v1.Moniker\x12#\n\x05value\x18\x02 \x01(\x0b2\x14.google.protobuf.Any"\x18\n\x16WriteToMonikerResponse*\xbd\x01\n\x10SidebandStrategy\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x11\n\rSHARED_MEMORY\x10\x02\x12!\n\x1dDOUBLE_BUFFERED_SHARED_MEMORY\x10\x03\x12\x0b\n\x07SOCKETS\x10\x04\x12\x17\n\x13SOCKETS_LOW_LATENCY\x10\x05\x12\x16\n\x12HYPERVISOR_SOCKETS\x10\x06\x12\x08\n\x04RDMA\x10\x07\x12\x14\n\x10RDMA_LOW_LATENCY\x10\x082\x8b\x05\n\x0eMonikerService\x12\x86\x01\n\x13BeginSidebandStream\x125.ni.datamonikers.v1.BeginMonikerSidebandStreamRequest\x1a6.ni.datamonikers.v1.BeginMonikerSidebandStreamResponse"\x00\x12X\n\nStreamRead\x12\x1f.ni.datamonikers.v1.MonikerList\x1a%.ni.datamonikers.v1.MonikerReadResult"\x000\x01\x12e\n\x0bStreamWrite\x12\'.ni.datamonikers.v1.MonikerWriteRequest\x1a\'.ni.datamonikers.v1.StreamWriteResponse"\x00(\x010\x01\x12g\n\x0fStreamReadWrite\x12\'.ni.datamonikers.v1.MonikerWriteRequest\x1a%.ni.datamonikers.v1.MonikerReadResult"\x00(\x010\x01\x12[\n\x0fReadFromMoniker\x12\x1b.ni.datamonikers.v1.Moniker\x1a).ni.datamonikers.v1.ReadFromMonikerResult"\x00\x12i\n\x0eWriteToMoniker\x12).ni.datamonikers.v1.WriteToMonikerRequest\x1a*.ni.datamonikers.v1.WriteToMonikerResponse"\x00B\x9f\x01\n\x16com.ni.datamonikers.v1B\x17DataMonikerServiceProtoP\x01Z\x0edatamonikersv1\xf8\x01\x01\xa2\x02\x04NIDM\xaa\x02#NationalInstruments.DataMonikers.V1\xca\x02\x12NI\\DataMonikers\\V1\xea\x02\x14NI::DataMonikers::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.datamonikers.v1.proto/src/ni/datamonikers/v1/data_moniker_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.datamonikers.v1.proto/src/ni/datamonikers/v1/data_moniker_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class MonikerServiceStub(object)`

Service for reading and writing data values using data monikers.

    Not all implementations implement all RPCs and clients should
    handle this gracefully.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class MonikerServiceServicer(object)`

Service for reading and writing data values using data monikers.

    Not all implementations implement all RPCs and clients should
    handle this gracefully.
    

#### `def BeginSidebandStream(self, request, context)`

Negotiates a sideband transport for the specified monikers.

        Use this RPC when higher throughput or lower latency are required
        beyond what is traditionally possible with the standard gRPC transport.
        The client supplies the preferred strategy and the list of monikers.
        The server responds with the selected strategy plus the connection
        metadata needed to establish the sideband channel. After this call,
        the actual data exchange is expected to happen over the selected
        sideband transport, not over this unary RPC.
        

#### `def StreamRead(self, request, context)`

Subscribes to updates from the requested monikers.

        A response message is returned once a data value is available from
        each read moniker. The order of data values returned matches the order
        of the read monikers. The semantics for when data is published and how
        updates are triggered is implementation dependent.

        Status codes for errors:

        - NOT_FOUND: Specified moniker does not exist
        

#### `def StreamWrite(self, request_iterator, context)`

Streams values to one or more monikers.

        The first request message specifies the write monikers that will be updated.
        Subsequent request messages supply new data values to be written to the
        monikers. The number of data values in each request message must match the
        number of monikers supplied in the original request. The data values are
        applied in order and are paired positionally with the monikers declared in
        the first message. Implementations may choose to return a response message
        after each request has been processed for flow control purposes or no
        response message at all.

        Status codes for errors:

        - NOT_FOUND: Specified moniker does not exist
        

#### `def StreamReadWrite(self, request_iterator, context)`

Streams data to and from the specified read and write monikers.

        The first request message is used to setup the stream and specifies the
        monikers that are to be read and written. No response message is sent for
        the first request message.

        The second and subsequent request messages carry new data values to be written
        to the write monikers similar to the StreamWrite RPC. For each of these request
        message, a response message is returned containing data values from the read
        monikers similar to the StreamRead RPC. Write monikers are always updated before
        data is read from the read monikers.Communication continues in this ping-pong
        fashion until the stream is closed.

        Status codes for errors:

        - NOT_FOUND: Specified moniker does not exist
        

#### `def ReadFromMoniker(self, request, context)`

Reads the current value for a single moniker.

        If no data value is available, implementations may choose to return an empty
        response or return an error.

        Status codes for errors:

        - NOT_FOUND: Specified moniker does not exist
        

#### `def WriteToMoniker(self, request, context)`

Writes a single value to a single moniker.

        Status codes for errors:

        - NOT_FOUND: Specified moniker does not exist
        - INVALID_ARGUMENT: Data type of the data value is not compatible with the moniker
        

### `def add_MonikerServiceServicer_to_server(servicer, server)`

### `class MonikerService(object)`

Service for reading and writing data values using data monikers.

    Not all implementations implement all RPCs and clients should
    handle this gracefully.
    

#### `def BeginSidebandStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamRead(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamWrite(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamReadWrite(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadFromMoniker(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteToMoniker(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.grpcdevice.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.grpcdevice.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.grpcdevice.v1.proto/src/session_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.grpcdevice.v1.proto/src/session_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsession.proto\x12\rnidevice_grpc"2\n\x07Session\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x0c\n\x02id\x18\x02 \x01(\rH\x00B\t\n\x07session"j\n\x10DeviceProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\x12\x12\n\nproduct_id\x18\x05 \x01(\r"\x19\n\x17EnumerateDevicesRequest"L\n\x18EnumerateDevicesResponse\x120\n\x07devices\x18\x01 \x03(\x0b2\x1f.nidevice_grpc.DeviceProperties";\n\x0eReserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t"&\n\x0fReserveResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08"F\n\x19IsReservedByClientRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t"1\n\x1aIsReservedByClientResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08"=\n\x10UnreserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t"*\n\x11UnreserveResponse\x12\x15\n\ris_unreserved\x18\x01 \x01(\x08"\x14\n\x12ResetServerRequest".\n\x13ResetServerResponse\x12\x17\n\x0fis_server_reset\x18\x01 \x01(\x08*\xbc\x01\n\x1dSessionInitializationBehavior\x12/\n+SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED\x10\x00\x122\n.SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW\x10\x01\x126\n2SESSION_INITIALIZATION_BEHAVIOR_ATTACH_TO_EXISTING\x10\x022\xd2\x03\n\x10SessionUtilities\x12c\n\x10EnumerateDevices\x12&.nidevice_grpc.EnumerateDevicesRequest\x1a\'.nidevice_grpc.EnumerateDevicesResponse\x12H\n\x07Reserve\x12\x1d.nidevice_grpc.ReserveRequest\x1a\x1e.nidevice_grpc.ReserveResponse\x12i\n\x12IsReservedByClient\x12(.nidevice_grpc.IsReservedByClientRequest\x1a).nidevice_grpc.IsReservedByClientResponse\x12N\n\tUnreserve\x12\x1f.nidevice_grpc.UnreserveRequest\x1a .nidevice_grpc.UnreserveResponse\x12T\n\x0bResetServer\x12!.nidevice_grpc.ResetServerRequest\x1a".nidevice_grpc.ResetServerResponseBB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.grpcdevice.v1.proto/src/session_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.grpcdevice.v1.proto/src/session_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class SessionUtilitiesStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class SessionUtilitiesServicer(object)`

Missing associated documentation comment in .proto file.

#### `def EnumerateDevices(self, request, context)`

Provides a list of devices or chassis connected to server under localhost
        

#### `def Reserve(self, request, context)`

Reserve a set of client defined resources for exclusive use
        

#### `def IsReservedByClient(self, request, context)`

Determines if a set of client defined resources is currently reserved by a
        specific client
        

#### `def Unreserve(self, request, context)`

Unreserves a previously reserved resource
        

#### `def ResetServer(self, request, context)`

Resets the server to a default state with no open sessions
        

### `def add_SessionUtilitiesServicer_to_server(servicer, server)`

### `class SessionUtilities(object)`

Missing associated documentation comment in .proto file.

#### `def EnumerateDevices(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reserve(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsReservedByClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Unreserve(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetServer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Discovery Service.

- `__all__ = ['DiscoveryClient', 'ServiceLocation', 'ComputeNodeDescriptor', 'ServiceInfo']`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_client.py

### MODULE DOCSTRING

Client for accessing the NI Discovery Service.

### `class DiscoveryClient()`

Client for accessing the NI Discovery Service.

#### `def __init__(self, stub: discovery_service_pb2_grpc.DiscoveryServiceStub | None=None, *, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the discovery client.

        Args:
            stub: An optional discovery service gRPC stub for unit testing.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def _get_stub(self) -> discovery_service_pb2_grpc.DiscoveryServiceStub`

#### `def register_service(self, service_info: ServiceInfo, service_location: ServiceLocation) -> str`

Register the specified service with the discovery service.

        Args:
            service_info: Information describing the service.

            service_location: The location of the service on the network.

        Returns:
            ID that can be used to unregister the service.
        

#### `def unregister_service(self, registration_id: str) -> bool`

Unregisters the specified service from the discovery service.

        This method should be called before the service exits.

        Args:
            registration_id: The registration ID returned from register_service.
                This argument should be omitted after calling the deprecated
                register_measurement_service method.

        Returns:
            Boolean indicating whether the service was unregistered.
        

#### `def resolve_service(self, provided_interface: str, service_class: str='', deployment_target: str='', version: str='') -> ServiceLocation`

Resolve the location of a service.

        Given a description of a service, returns information that can be used to establish
        communication with that service. If necessary, the service will be started by the
        discovery service if it has not already been started.

        Args:
            provided_interface: The gRPC full name of the service.
            service_class: The service "class" that should be matched. If the value is not
                specified and there is more than one matching service registered, an error
                is returned.
            deployment_target: The deployment target from which the service should be resolved.
                Callers should pass either the url string from a :class:`ComputeNodeSpecifier`
                or a blank string for local execution.
            version: The version of the service to resolve. If not specified, the latest version
                will be resolved.

        Returns:
            The service location.
        

#### `def resolve_service_with_information(self, provided_interface: str, service_class: str='', deployment_target: str='', version: str='') -> tuple[ServiceLocation, ServiceInfo]`

Resolve the location of a service along with its information.

        Given a description of a service, returns information for the service in addition to
        the location of the service. If necessary, the service will be started by the discovery
        service if it has not already been started.

        Args:
            provided_interface: The gRPC full name of the service.
            service_class: The service "class" that should be matched. If the value is not
                specified and there is more than one matching service registered, an error
                is returned.
            deployment_target: The deployment target from which the service should be resolved.
                Callers should pass either the url string from a :class:`ComputeNodeSpecifier`
                or a blank string for local execution.
            version: The version of the service to resolve. If not specified, the latest version
                will be resolved.

        Returns:
            A tuple containing the service location and service information.
        

#### `def enumerate_services(self, provided_interface: str) -> Sequence[ServiceInfo]`

Enumerates all the services for the provided interface.

        Args:
            provided_interface: The gRPC full name of the services.

        Returns:
            The list of information describing the services.
        

#### `def enumerate_compute_nodes(self) -> Sequence[ComputeNodeDescriptor]`

Enumerates all the compute nodes registered with the discovery service.

        Returns:
            The list of information describing the compute nodes.
        

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_support.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_support.py

### MODULE DOCSTRING

Support functions for the NI Discovery Service.

- `_START_SERVICE_TIMEOUT = 30.0`

- `_START_SERVICE_POLLING_INTERVAL = 0.1`

- `_DISCOVERY_SERVICE_ENV_VAR_PREFIX = 'NIDiscovery_'`

- `_DISCOVERY_SERVICE_CLUSTER_ID_ENV_VAR = 'ClusterId'`

### `def _get_discovery_service_address() -> str`

### `def _ensure_discovery_service_started(key_file_path: pathlib.Path) -> None`

Check whether discovery service already running, if not start the discovery service.

### `def _get_discovery_service_location() -> pathlib.PurePath`

Gets the location of the discovery service process executable.

### `def _get_registration_json_file_path() -> pathlib.Path`

### `def _key_file_exists(key_file_path: pathlib.Path) -> bool`

### `def _start_service(exe_file_path: pathlib.PurePath, key_file_path: pathlib.Path) -> subprocess.Popen[Any]`

Starts the service at the specified path and wait for the service to get up and running.

### `def _service_already_running(key_file_path: pathlib.Path) -> bool`

### `def _delete_existing_key_file(key_file_path: pathlib.Path) -> None`

### `def _get_key_file_path(cluster_id: str | None=None) -> pathlib.Path`

### `def _get_key_file_directory() -> pathlib.Path`

### `def _open_key_file(path: str) -> typing.TextIO`

### `def _get_nipath(name: str) -> pathlib.Path`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_types.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/src/ni/measurementlink/discovery/v1/client/_types.py

### MODULE DOCSTRING

Data types for the NI Discovery Service.

### `class ServiceInfo(NamedTuple)`

A named tuple providing information about a registered service.

    This class is used with the NI Discovery Service when registering and enumerating services.
    

#### `def _from_grpc(cls, other: discovery_service_pb2.ServiceDescriptor) -> ServiceInfo`

### `class ServiceLocation(typing.NamedTuple)`

Represents the location of a service.

#### `def insecure_address(self) -> str`

Get the service's insecure address in the format host:port.

#### `def ssl_authenticated_address(self) -> str`

Get the service's SSL-authenticated address in the format host:port.

#### `def _from_grpc(cls, other: discovery_service_pb2.ServiceLocation) -> ServiceLocation`

### `class ComputeNodeDescriptor(typing.NamedTuple)`

Represents a compute node.

#### `def _from_grpc(cls, other: discovery_service_pb2.ComputeNodeDescriptor) -> ComputeNodeDescriptor`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/tests/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/tests/unit/test_discovery_client.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/tests/unit/test_discovery_client.py

### MODULE DOCSTRING

Contains tests to validate the discovery_client.py.

- `_PROVIDED_MEASUREMENT_SERVICES = ['ni.measurementlink.measurement.v1.MeasurementService', 'ni.measurementlink.measurement.v2.MeasurementService']`

- `_PROVIDED_ANNOTATIONS = {'ni/service.description': 'This annotation is just an example for this test', 'ni/service.collection': 'CurrentTests.Inrush', 'ni/service.tags': '["NI_Example","Voltage"]', 'client/extra.NumberID': '500', 'client/extra.Parts': '["PartNumber_25898","PartNumber_25412"]'}`

- `_TEST_SERVICE_PORT = '9999'`

- `_TEST_SERVICE_SSL_PORT = '9998'`

- `_TEST_SERVICE_LOCATION = ServiceLocation('localhost', _TEST_SERVICE_PORT, _TEST_SERVICE_SSL_PORT)`

- `_TEST_SERVICE_INFO = ServiceInfo(service_class='TestServiceClass', description_url='TestUrl', provided_interfaces=_PROVIDED_MEASUREMENT_SERVICES, annotations=_PROVIDED_ANNOTATIONS, display_name='TestMeasurement', versions=['2.0.2'])`

- `_TEST_SERVICE_INFO_WITHOUT_DISPLAY_NAME = _TEST_SERVICE_INFO._replace(display_name='')`

- `_MOCK_KEY_FILE_CONTENT = {'SecurePort': '', 'InsecurePort': _TEST_SERVICE_PORT}`

- `_MOCK_REGISTRATION_FILE_CONTENT = {'discovery': {'path': 'Discovery/NI.Discovery.V1.Service.exe'}}`

### `def test___service_not_registered___register_service___sends_request_and_returns_id(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___service_registered___unregister_service___sends_request(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___service_registered___resolve_service_without_version___sends_request(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___service_registered___resolve_service_with_version___sends_request(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___service_not_registered___resolve_service___raises_not_found_error(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___discovery_service_not_running___get_discovery_service_address___starts_discovery_service(mocker: MockerFixture, temp_discovery_key_file_path: pathlib.Path, temp_registration_json_file_path: pathlib.Path, temp_directory: pathlib.Path, subprocess_popen_kwargs: dict[str, Any]) -> None`

### `def test___key_file_never_created___get_discovery_service_address___throws_timeout_error(mocker: MockerFixture, temp_discovery_key_file_path: pathlib.Path, temp_registration_json_file_path: pathlib.Path) -> None`

### `def test___key_file_not_exist___open_key_file___raises_file_not_found_error(mocker: MockerFixture, temp_discovery_key_file_path: pathlib.Path, windows_error_code: int) -> None`

### `def test___key_file_exist_after_poll___start_discovery_service___discovery_service_started(mocker: MockerFixture, temp_directory: pathlib.Path, temp_discovery_key_file_path: pathlib.Path, subprocess_popen_kwargs: dict[str, Any]) -> None`

### `def test___discovery_service_exe_unavailable___register_service___raises_file_not_found_error(mocker: MockerFixture, temp_discovery_key_file_path: pathlib.Path, temp_registration_json_file_path: pathlib.Path) -> None`

### `def test___registered_measurements___enumerate_services___returns_list_of_measurements(discovery_client: DiscoveryClient, discovery_service_stub: Mock, programming_language: str) -> None`

### `def test___no_registered_measurements___enumerate_services___returns_empty_list(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___registered_measurements___resolve_service_with_information___sends_request(discovery_client: DiscoveryClient, discovery_service_stub: Mock, programming_language: str) -> None`

### `def test___no_registered_measurements___resolve_service_with_information___raises_not_found_error(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___registered_compute_node___enumerate_compute_nodes___returns_node(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___multiple_registered_compute_nodes___enumerate_compute_nodes___returns_all_nodes(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___no_registered_compute_nodes___enumerate_compute_nodes___returns_empty_list(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def test___enumerate_compute_nodes___grpc_error___raises_rpc_error(discovery_client: DiscoveryClient, discovery_service_stub: Mock) -> None`

### `def grpc_channel_pool() -> Generator[GrpcChannelPool]`

Test fixture that creates a gRPC channel pool.

### `def subprocess_popen_kwargs() -> dict[str, Any]`

### `def discovery_client(discovery_service_stub: Mock, grpc_channel_pool: Mock, mocker: MockerFixture) -> DiscoveryClient`

Create a DiscoveryClient.

### `def discovery_service_stub(mocker: MockerFixture) -> Mock`

Create a mock DiscoveryServiceStub.

### `def temp_directory(tmp_path: pathlib.Path) -> pathlib.Path`

Create a temp directory to store discovery service key and registration files.

### `def temp_discovery_key_file_path(temp_directory: pathlib.Path) -> pathlib.Path`

Create a discovery service key file.

### `def temp_registration_json_file_path(temp_directory: pathlib.Path) -> pathlib.Path`

Create a discovery service registration json file.

### `def _assert_service_location_equal(expected: ServiceLocation, actual: ServiceLocation | GrpcServiceLocation) -> None`

### `def _assert_service_info_equal(expected: ServiceInfo, actual: ServiceInfo | GrpcServiceDescriptor) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/tests/utilities/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/tests/utilities/__init__.py

### MODULE DOCSTRING

Contains test utilities.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.client/tests/utilities/fake_rpc_error.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.client/tests/utilities/fake_rpc_error.py

### MODULE DOCSTRING

A throwable version of grpc.RpcError for testing.

### `class FakeRpcError(grpc.RpcError)`

A throwable version of grpc.RpcError for testing.

#### `def __init__(self, code: grpc.StatusCode, details: str) -> None`

Construct a FakeRpcError.

#### `def code(self) -> grpc.StatusCode`

Get the gRPC status code.

#### `def details(self) -> str`

Get the error details.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/annotations/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/annotations/__init__.py

### MODULE DOCSTRING

Constants for discovery service annotations.

- `SERVICE_COLLECTION_KEY = 'ni/service.collection'`

- `SERVICE_DESCRIPTION_KEY = 'ni/service.description'`

- `SERVICE_PROGRAMMINGLANGUAGE_KEY = 'ni/service.programminglanguage'`

- `SERVICE_TAGS_KEY = 'ni/service.tags'`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/discovery_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/discovery_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ni/measurementlink/discovery/v1/discovery_service.proto\x12\x1fni.measurementlink.discovery.v1"\x96\x02\n\x11ServiceDescriptor\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0fdescription_url\x18\x02 \x01(\t\x12\x1b\n\x13provided_interfaces\x18\x03 \x03(\t\x12\x15\n\rservice_class\x18\x04 \x01(\t\x12X\n\x0bannotations\x18\x05 \x03(\x0b2C.ni.measurementlink.discovery.v1.ServiceDescriptor.AnnotationsEntry\x12\x10\n\x08versions\x18\x06 \x03(\t\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"Z\n\x0fServiceLocation\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x15\n\rinsecure_port\x18\x02 \x01(\t\x12\x1e\n\x16ssl_authenticated_port\x18\x03 \x01(\t"\xad\x01\n\x16RegisterServiceRequest\x12O\n\x13service_description\x18\x01 \x01(\x0b22.ni.measurementlink.discovery.v1.ServiceDescriptor\x12B\n\x08location\x18\x02 \x01(\x0b20.ni.measurementlink.discovery.v1.ServiceLocation"2\n\x17RegisterServiceResponse\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t"3\n\x18UnregisterServiceRequest\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t"\x1b\n\x19UnregisterServiceResponse"M\n\x18EnumerateServicesRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\x12\x15\n\rservice_class\x18\x02 \x01(\t"\x80\x01\n\x19EnumerateServicesResponse\x12N\n\x12available_services\x18\x01 \x03(\x0b22.ni.measurementlink.discovery.v1.ServiceDescriptor\x12\x13\n\x0bunreachable\x18\x02 \x03(\t"v\n\x15ResolveServiceRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\x12\x15\n\rservice_class\x18\x02 \x01(\t\x12\x19\n\x11deployment_target\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t"\x85\x01\n$ResolveServiceWithInformationRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\x12\x15\n\rservice_class\x18\x02 \x01(\t\x12\x19\n\x11deployment_target\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t"\xc3\x01\n%ResolveServiceWithInformationResponse\x12J\n\x10service_location\x18\x01 \x01(\x0b20.ni.measurementlink.discovery.v1.ServiceLocation\x12N\n\x12service_descriptor\x18\x02 \x01(\x0b22.ni.measurementlink.discovery.v1.ServiceDescriptor"6\n\x15ComputeNodeDescriptor\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08is_local\x18\x02 \x01(\x08"S\n\x1eEnumerateActiveServicesRequest\x12\x1a\n\x12provided_interface\x18\x01 \x01(\t\x12\x15\n\rservice_class\x18\x02 \x01(\t"\xb6\x01\n\x18ActiveServiceInformation\x12N\n\x12service_descriptor\x18\x01 \x01(\x0b22.ni.measurementlink.discovery.v1.ServiceDescriptor\x12J\n\x10service_location\x18\x02 \x01(\x0b20.ni.measurementlink.discovery.v1.ServiceLocation"u\n\x1fEnumerateActiveServicesResponse\x12R\n\x0factive_services\x18\x01 \x03(\x0b29.ni.measurementlink.discovery.v1.ActiveServiceInformation"\x1e\n\x1cEnumerateComputeNodesRequest"n\n\x1dEnumerateComputeNodesResponse\x12M\n\rcompute_nodes\x18\x01 \x03(\x0b26.ni.measurementlink.discovery.v1.ComputeNodeDescriptor2\x98\x08\n\x10DiscoveryService\x12\x84\x01\n\x0fRegisterService\x127.ni.measurementlink.discovery.v1.RegisterServiceRequest\x1a8.ni.measurementlink.discovery.v1.RegisterServiceResponse\x12\x8a\x01\n\x11UnregisterService\x129.ni.measurementlink.discovery.v1.UnregisterServiceRequest\x1a:.ni.measurementlink.discovery.v1.UnregisterServiceResponse\x12\x8a\x01\n\x11EnumerateServices\x129.ni.measurementlink.discovery.v1.EnumerateServicesRequest\x1a:.ni.measurementlink.discovery.v1.EnumerateServicesResponse\x12z\n\x0eResolveService\x126.ni.measurementlink.discovery.v1.ResolveServiceRequest\x1a0.ni.measurementlink.discovery.v1.ServiceLocation\x12\xae\x01\n\x1dResolveServiceWithInformation\x12E.ni.measurementlink.discovery.v1.ResolveServiceWithInformationRequest\x1aF.ni.measurementlink.discovery.v1.ResolveServiceWithInformationResponse\x12\x96\x01\n\x15EnumerateComputeNodes\x12=.ni.measurementlink.discovery.v1.EnumerateComputeNodesRequest\x1a>.ni.measurementlink.discovery.v1.EnumerateComputeNodesResponse\x12\x9c\x01\n\x17EnumerateActiveServices\x12?.ni.measurementlink.discovery.v1.EnumerateActiveServicesRequest\x1a@.ni.measurementlink.discovery.v1.EnumerateActiveServicesResponseB\xcc\x01\n#com.ni.measurementlink.discovery.v1B\x15DiscoveryServiceProtoP\x01Z\x0bdiscoveryv1\xa2\x02\x04NIMD\xaa\x020NationalInstruments.MeasurementLink.Discovery.V1\xca\x02\x1fNI\\MeasurementLink\\Discovery\\V1\xea\x02"NI::MeasurementLink::Discovery::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/discovery_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.discovery.v1.proto/src/ni/measurementlink/discovery/v1/discovery_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class DiscoveryServiceStub(object)`

The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class DiscoveryServiceServicer(object)`

The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    

#### `def RegisterService(self, request, context)`

Registers a service instance with the discovery service.

        Status codes for errors:

        - INVALID_ARGUMENT:

        - ServiceDescriptor.display_name is empty
        - ServiceDescriptor.provided_interfaces is empty
        - ServiceDescriptor.service_class is empty
        - ServiceLocation.location is empty
        - Both ServiceLocation.insecure_port and ServiceLocation.ssl_authenticated_port are empty
        - Either ServiceLocation.insecure_port or ServiceLocation.ssl_authenticated_port contain an invalid port number
        

#### `def UnregisterService(self, request, context)`

Unregisters a service instance with the discovery service.
        

#### `def EnumerateServices(self, request, context)`

Enumerate all services which implement a specific service interface.
        This is useful for plugin type systems where the possible services are not known ahead of time.
        

#### `def ResolveService(self, request, context)`

Given a description of a service, returns information that can be used to establish communication
        with that service. If necessary, the service will be started by the discovery service if it has not
        already been started. Activation of the service is accomplished through use of a .serviceconfig file
        which includes information describing the service. Services that register a .serviceconfig file must
        call RegisterService when their service is started or this call will never complete successfully when
        the discovery service attempts to start it.

        Status codes for errors:

        - INVALID_ARGUMENT: provided_interfaces is empty
        - NOT_FOUND: No service matching the resolve request was found
        - FAILED_PRECONDITION: More than one service matching the resolve request was found
        

#### `def ResolveServiceWithInformation(self, request, context)`

Similar to ResolveService, returns information for the service in addition to the location of the service.
        This is useful if you want to avoid the overhead of having to call EnumerateServices to get this information as part of
        resolution of the service. See ResolveService for additional documentation related to resolving the service.
        

#### `def EnumerateComputeNodes(self, request, context)`

Enumerate all compute nodes that have registered themselves in the current session.
        These compute nodes are targets available for execution of services.
        A compute node can be used as an argument to the ResolveService method to
        get the service location for a service running on that compute node.
        

#### `def EnumerateActiveServices(self, request, context)`

Enumerate all service instances that are currently active (running).
        This RPC is intended for diagnostic and informational purposes, such as displaying the
        status of registered services to a user. It should not be used to obtain a service location
        for the purpose of communicating with that service; use ResolveService or
        ResolveServiceWithInformation for that purpose.

        Unlike EnumerateServices, this RPC returns individual active service instances rather than
        collapsing multiple registered versions into a single ServiceDescriptor entry, allowing
        callers to see each running instance independently when multiple versions are active side by side.
        

### `def add_DiscoveryServiceServicer_to_server(servicer, server)`

### `class DiscoveryService(object)`

The service used as a registry for other services. This service can be used to discover
    and activate other services present in the system.
    

#### `def RegisterService(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterService(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumerateServices(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResolveService(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResolveServiceWithInformation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumerateComputeNodes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumerateActiveServices(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/src/ni/measurementlink/measurement/v1/measurement_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/src/ni/measurementlink/measurement/v1/measurement_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;ni/measurementlink/measurement/v1/measurement_service.proto\x12!ni.measurementlink.measurement.v1\x1a\x19google/protobuf/any.proto\x1a\x1agoogle/protobuf/type.proto\x1a(ni/measurementlink/pin_map_context.proto"\x14\n\x12GetMetadataRequest"\x9a\x02\n\x13GetMetadataResponse\x12R\n\x13measurement_details\x18\x01 \x01(\x0b25.ni.measurementlink.measurement.v1.MeasurementDetails\x12V\n\x15measurement_signature\x18\x02 \x01(\x0b27.ni.measurementlink.measurement.v1.MeasurementSignature\x12W\n\x16user_interface_details\x18\x03 \x03(\x0b27.ni.measurementlink.measurement.v1.UserInterfaceDetails"\x84\x01\n\x0eMeasureRequest\x126\n\x18configuration_parameters\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12:\n\x0fpin_map_context\x18\x02 \x01(\x0b2!.ni.measurementlink.PinMapContext"8\n\x0fMeasureResponse\x12%\n\x07outputs\x18\x01 \x01(\x0b2\x14.google.protobuf.Any";\n\x12MeasurementDetails\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t"\xb2\x02\n\x14MeasurementSignature\x12-\n%configuration_parameters_message_type\x18\x01 \x01(\t\x12[\n\x18configuration_parameters\x18\x02 \x03(\x0b29.ni.measurementlink.measurement.v1.ConfigurationParameter\x124\n\x16configuration_defaults\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12\x1c\n\x14outputs_message_type\x18\x04 \x01(\t\x12:\n\x07outputs\x18\x05 \x03(\x0b2).ni.measurementlink.measurement.v1.Output"(\n\x14UserInterfaceDetails\x12\x10\n\x08file_url\x18\x01 \x01(\t"\x8e\x02\n\x16ConfigurationParameter\x12\x14\n\x0cfield_number\x18\x01 \x01(\x05\x12)\n\x04type\x18\x02 \x01(\x0e2\x1b.google.protobuf.Field.Kind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08repeated\x18\x04 \x01(\x08\x12_\n\x0bannotations\x18\x05 \x03(\x0b2J.ni.measurementlink.measurement.v1.ConfigurationParameter.AnnotationsEntry\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"i\n\x06Output\x12\x14\n\x0cfield_number\x18\x01 \x01(\x05\x12)\n\x04type\x18\x02 \x01(\x0e2\x1b.google.protobuf.Field.Kind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08repeated\x18\x04 \x01(\x082\x84\x02\n\x12MeasurementService\x12|\n\x0bGetMetadata\x125.ni.measurementlink.measurement.v1.GetMetadataRequest\x1a6.ni.measurementlink.measurement.v1.GetMetadataResponse\x12p\n\x07Measure\x121.ni.measurementlink.measurement.v1.MeasureRequest\x1a2.ni.measurementlink.measurement.v1.MeasureResponseB\xd8\x01\n%com.ni.measurementlink.measurement.v1B\x17MeasurementServiceProtoP\x01Z\rmeasurementv1\xa2\x02\x04NIMM\xaa\x022NationalInstruments.MeasurementLink.Measurement.V1\xca\x02!NI\\MeasurementLink\\Measurement\\V1\xea\x02$NI::MeasurementLink::Measurement::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/src/ni/measurementlink/measurement/v1/measurement_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/src/ni/measurementlink/measurement/v1/measurement_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class MeasurementServiceStub(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class MeasurementServiceServicer(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def GetMetadata(self, request, context)`

Returns information that describes the measurement.
        

#### `def Measure(self, request, context)`

API used to perform a measurement.
        

### `def add_MeasurementServiceServicer_to_server(servicer, server)`

### `class MeasurementService(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def GetMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Measure(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/tests/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/tests/__init__.py

### MODULE DOCSTRING

Tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v1.proto/tests/unit/test_ni_measurementlink_measurement_v1.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v1.proto/tests/unit/test_ni_measurementlink_measurement_v1.py

### MODULE DOCSTRING

Tests for the ni.measurementlink.measurement.v1.proto package.

### `def test___creategetmetadatarequest___message_created() -> None`

### `def test___creategetmetadataresponse___message_created() -> None`

### `def test___getmetadataresponse___with_measurementdetails___retrieved() -> None`

### `def test___getmetadataresponse___with_measurementsignature___retrieved() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/src/ni/measurementlink/measurement/v2/measurement_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/src/ni/measurementlink/measurement/v2/measurement_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;ni/measurementlink/measurement/v2/measurement_service.proto\x12!ni.measurementlink.measurement.v2\x1a\x19google/protobuf/any.proto\x1a\x1agoogle/protobuf/type.proto\x1a(ni/measurementlink/pin_map_context.proto"\x14\n\x12GetMetadataRequest"\x9a\x02\n\x13GetMetadataResponse\x12R\n\x13measurement_details\x18\x01 \x01(\x0b25.ni.measurementlink.measurement.v2.MeasurementDetails\x12V\n\x15measurement_signature\x18\x02 \x01(\x0b27.ni.measurementlink.measurement.v2.MeasurementSignature\x12W\n\x16user_interface_details\x18\x03 \x03(\x0b27.ni.measurementlink.measurement.v2.UserInterfaceDetails"\x84\x01\n\x0eMeasureRequest\x126\n\x18configuration_parameters\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12:\n\x0fpin_map_context\x18\x02 \x01(\x0b2!.ni.measurementlink.PinMapContext"8\n\x0fMeasureResponse\x12%\n\x07outputs\x18\x01 \x01(\x0b2\x14.google.protobuf.Any";\n\x12MeasurementDetails\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t"\xb2\x02\n\x14MeasurementSignature\x12-\n%configuration_parameters_message_type\x18\x01 \x01(\t\x12[\n\x18configuration_parameters\x18\x02 \x03(\x0b29.ni.measurementlink.measurement.v2.ConfigurationParameter\x124\n\x16configuration_defaults\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12\x1c\n\x14outputs_message_type\x18\x04 \x01(\t\x12:\n\x07outputs\x18\x05 \x03(\x0b2).ni.measurementlink.measurement.v2.Output"(\n\x14UserInterfaceDetails\x12\x10\n\x08file_url\x18\x01 \x01(\t"\xa4\x02\n\x16ConfigurationParameter\x12\x14\n\x0cfield_number\x18\x01 \x01(\x05\x12)\n\x04type\x18\x02 \x01(\x0e2\x1b.google.protobuf.Field.Kind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08repeated\x18\x04 \x01(\x08\x12_\n\x0bannotations\x18\x05 \x03(\x0b2J.ni.measurementlink.measurement.v2.ConfigurationParameter.AnnotationsEntry\x12\x14\n\x0cmessage_type\x18\x06 \x01(\t\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x84\x02\n\x06Output\x12\x14\n\x0cfield_number\x18\x01 \x01(\x05\x12)\n\x04type\x18\x02 \x01(\x0e2\x1b.google.protobuf.Field.Kind\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08repeated\x18\x04 \x01(\x08\x12O\n\x0bannotations\x18\x05 \x03(\x0b2:.ni.measurementlink.measurement.v2.Output.AnnotationsEntry\x12\x14\n\x0cmessage_type\x18\x06 \x01(\t\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\x86\x02\n\x12MeasurementService\x12|\n\x0bGetMetadata\x125.ni.measurementlink.measurement.v2.GetMetadataRequest\x1a6.ni.measurementlink.measurement.v2.GetMetadataResponse\x12r\n\x07Measure\x121.ni.measurementlink.measurement.v2.MeasureRequest\x1a2.ni.measurementlink.measurement.v2.MeasureResponse0\x01B\xd8\x01\n%com.ni.measurementlink.measurement.v2B\x17MeasurementServiceProtoP\x01Z\rmeasurementv2\xa2\x02\x04NIMM\xaa\x022NationalInstruments.MeasurementLink.Measurement.V2\xca\x02!NI\\MeasurementLink\\Measurement\\V2\xea\x02$NI::MeasurementLink::Measurement::V2b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/src/ni/measurementlink/measurement/v2/measurement_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/src/ni/measurementlink/measurement/v2/measurement_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class MeasurementServiceStub(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class MeasurementServiceServicer(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def GetMetadata(self, request, context)`

Returns information that describes the measurement.
        

#### `def Measure(self, request, context)`

API used to perform a measurement.
        

### `def add_MeasurementServiceServicer_to_server(servicer, server)`

### `class MeasurementService(object)`

Service that implements a measurement. Unlike other services, a MeasurementService is designed to be a plugin
    where there can be multiple implementations of the service that provide different measurement capabilities.
    

#### `def GetMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Measure(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/tests/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/tests/__init__.py

### MODULE DOCSTRING

Tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.measurement.v2.proto/tests/unit/test_ni_measurementlink_measurement_v2.py -->
## PYTHON MODULE: packages/ni.measurementlink.measurement.v2.proto/tests/unit/test_ni_measurementlink_measurement_v2.py

### MODULE DOCSTRING

Tests for the ni.measurementlink.measurement.v2.proto package.

### `def test___creategetmetadatarequest___message_created() -> None`

### `def test___creategetmetadataresponse___message_created() -> None`

### `def test___getmetadataresponse___with_measurementdetails___retrieved() -> None`

### `def test___getmetadataresponse___with_measurementsignature___retrieved() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Pin Map Service.

- `__all__ = ['PinMapClient']`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/_client.py

### MODULE DOCSTRING

Client for accessing the NI Pin Map Service.

### `class PinMapClient(GrpcServiceClientBase[pin_map_service_pb2_grpc.PinMapServiceStub])`

Client for accessing the NI Pin Map Service via gRPC.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the pin map client.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional pin map gRPC channel.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def update_pin_map(self, pin_map_path: str | pathlib.Path) -> str`

Update registered pin map contents.

        Create and register a pin map if a pin map resource for the specified pin map id is not
        found.

        Args:
            pin_map_path: The file path of the pin map to register as a pin map resource.

        Returns:
            The resource id of the pin map that is registered to the pin map service.
        

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/_client_base.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/src/ni/measurementlink/pinmap/v1/client/_client_base.py

### `class StubProtocol(Protocol)`

Protocol for gRPC stub classes.

#### `def __init__(self, channel: grpc.Channel) -> None`

Initialize the gRPC client.

### `class GrpcServiceClientBase(Generic[TStub])`

Base class for NI gRPC service clients.

#### `def __init__(self, service_interface_name: str, service_class: str, stub_class: type[TStub], *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the gRPC client.

        Args:
            service_interface_name: The fully qualified name of the service interface.
            service_class: The name of the service class.
            stub_class: The gRPC stub class for the service.
            discovery_client: An optional discovery client (recommended).
            grpc_channel: An optional pin map gRPC channel.
            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the GrpcServiceClientBase.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the GrpcServiceClientBase.

#### `def close(self) -> None`

Close the client and clean up resources that it owns.

#### `def _get_stub(self) -> TStub`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/conftest.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/conftest.py

### MODULE DOCSTRING

Pytest configuration file.

### `def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Test fixture that returns the pin map directory.

### `def test_assets_directory() -> pathlib.Path`

Gets path to test_assets directory.

### `def stub_v1(grpc_channel: grpc.Channel) -> v1_measurement_service_pb2_grpc.MeasurementServiceStub`

Test fixture that creates a MeasurementService v1 stub.

### `def stub_v2(grpc_channel: grpc.Channel) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub`

Test fixture that creates a MeasurementService v2 stub.

### `def discovery_service_process() -> Generator[DiscoveryServiceProcess]`

Test fixture that creates discovery service process.

### `def grpc_channel_pool() -> Generator[GrpcChannelPool]`

Test fixture that creates a gRPC channel pool.

### `def discovery_client(discovery_service_process: DiscoveryServiceProcess, grpc_channel_pool: GrpcChannelPool) -> DiscoveryClient`

Test fixture that creates a discovery client.

### `def pin_map_client(discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool) -> PinMapClient`

Test fixture that creates a pin map client.

### `def session_management_client(discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool) -> SessionManagementClient`

Test fixture that creates a session management client.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/unit/test_pin_map_client.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/unit/test_pin_map_client.py

### MODULE DOCSTRING

Contains tests to validate the pin_map_client.py.

### `def test___valid_pin_map_file___register_pin_map___returns_pin_map_id(pin_map_client: PinMapClient, pin_map_stub: Mock, pin_map_directory: pathlib.Path) -> None`

### `def test___invalid_pin_map_file_path___register_pin_map___raises_file_not_found_error(pin_map_client: PinMapClient) -> None`

### `def _get_pin_map_file_contents(pin_map_path: str) -> str`

### `def pin_map_client(discovery_client: Mock, grpc_channel_pool: Mock, mocker: MockerFixture, pin_map_stub: Mock) -> PinMapClient`

Create a Client with a mock PinMapServiceStub.

### `def pin_map_stub(mocker: MockerFixture) -> Mock`

Create a mock PinMapServiceStub.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/utilities/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/utilities/__init__.py

### MODULE DOCSTRING

Contains test utilities.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.client/tests/utilities/discovery_service_process.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.client/tests/utilities/discovery_service_process.py

### MODULE DOCSTRING

Class to create and terminate Discovery Service instance.

### `class DiscoveryServiceProcess()`

Maintains the processes involved in creating and terminating discovery service.

#### `def __init__(self) -> None`

Creates a DiscoveryServiceProcess instance.

#### `def __enter__(self: Self) -> Self`

Returns the DiscoveryServiceProcess instance.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None`

Closes the DiscoveryServiceProcess instance.

#### `def _close_discovery_service(self) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.proto/src/ni/measurementlink/pinmap/v1/pin_map_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.proto/src/ni/measurementlink/pinmap/v1/pin_map_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2ni/measurementlink/pinmap/v1/pin_map_service.proto\x12\x1cni.measurementlink.pinmap.v1"\x1c\n\x06PinMap\x12\x12\n\npin_map_id\x18\x01 \x01(\t"E\n\x1aCreatePinMapFromXmlRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x13\n\x0bpin_map_xml\x18\x02 \x01(\t"E\n\x1aUpdatePinMapFromXmlRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x13\n\x0bpin_map_xml\x18\x02 \x01(\t"&\n\x10GetPinMapRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t"B\n\x10QueryPinsRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x02 \x01(\t"\x94\x01\n\x11QueryPinsResponse\x129\n\x04pins\x18\x01 \x03(\x0b2+.ni.measurementlink.pinmap.v1.PinDefinition\x12D\n\npin_groups\x18\x02 \x03(\x0b20.ni.measurementlink.pinmap.v1.PinGroupDefinition"<\n\rPinDefinition\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x15\n\ris_system_pin\x18\x02 \x01(\x08"b\n\x12PinGroupDefinition\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x1f\n\x17pin_or_group_references\x18\x02 \x03(\t\x12\x15\n\rresolved_pins\x18\x03 \x03(\t"(\n\x12QueryRelaysRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t"\x9e\x01\n\x13QueryRelaysResponse\x12=\n\x06relays\x18\x01 \x03(\x0b2-.ni.measurementlink.pinmap.v1.RelayDefinition\x12H\n\x0crelay_groups\x18\x02 \x03(\x0b22.ni.measurementlink.pinmap.v1.RelayGroupDefinition"@\n\x0fRelayDefinition\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x17\n\x0fis_system_relay\x18\x02 \x01(\x08"h\n\x14RelayGroupDefinition\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12!\n\x19relay_or_group_references\x18\x02 \x03(\t\x12\x17\n\x0fresolved_relays\x18\x03 \x03(\t"\x82\x01\n%QueryResourceAccessInformationRequest\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05\x12\x1a\n\x12pin_or_relay_names\x18\x03 \x03(\t\x12\x1a\n\x12instrument_type_id\x18\x04 \x01(\t"\xe1\x02\n&QueryResourceAccessInformationResponse\x12\\\n\x1bresource_access_information\x18\x01 \x03(\x0b27.ni.measurementlink.pinmap.v1.ResourceAccessInformation\x12o\n\x0egroup_mappings\x18\x02 \x03(\x0b2W.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationResponse.GroupMappingsEntry\x1ah\n\x12GroupMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.ni.measurementlink.pinmap.v1.ResolvedPinsOrRelays:\x028\x01"\xac\x01\n\x19ResourceAccessInformation\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x03 \x01(\t\x12F\n\x10channel_mappings\x18\x04 \x03(\x0b2,.ni.measurementlink.pinmap.v1.ChannelMapping"\xa5\x01\n\x0eChannelMapping\x12\x19\n\x11pin_or_relay_name\x18\x01 \x01(\t\x12\x0c\n\x04site\x18\x02 \x01(\x05\x12\x0f\n\x07channel\x18\x03 \x01(\t\x12!\n\x19multiplexer_resource_name\x18\x04 \x01(\t\x12\x19\n\x11multiplexer_route\x18\x05 \x01(\t\x12\x1b\n\x13multiplexer_type_id\x18\x06 \x01(\t"2\n\x14ResolvedPinsOrRelays\x12\x1a\n\x12pin_or_relay_names\x18\x01 \x03(\t2\xf0\x05\n\rPinMapService\x12u\n\x13CreatePinMapFromXml\x128.ni.measurementlink.pinmap.v1.CreatePinMapFromXmlRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12u\n\x13UpdatePinMapFromXml\x128.ni.measurementlink.pinmap.v1.UpdatePinMapFromXmlRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12a\n\tGetPinMap\x12..ni.measurementlink.pinmap.v1.GetPinMapRequest\x1a$.ni.measurementlink.pinmap.v1.PinMap\x12l\n\tQueryPins\x12..ni.measurementlink.pinmap.v1.QueryPinsRequest\x1a/.ni.measurementlink.pinmap.v1.QueryPinsResponse\x12r\n\x0bQueryRelays\x120.ni.measurementlink.pinmap.v1.QueryRelaysRequest\x1a1.ni.measurementlink.pinmap.v1.QueryRelaysResponse\x12\xab\x01\n\x1eQueryResourceAccessInformation\x12C.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationRequest\x1aD.ni.measurementlink.pinmap.v1.QueryResourceAccessInformationResponseB\xba\x01\n com.ni.measurementlink.pinmap.v1B\x12PinMapServiceProtoP\x01Z\x08pinmapv1\xa2\x02\x04NIMP\xaa\x02-NationalInstruments.MeasurementLink.PinMap.V1\xca\x02\x1cNI\\MeasurementLink\\PinMap\\V1\xea\x02\x1fNI::MeasurementLink::PinMap::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.pinmap.v1.proto/src/ni/measurementlink/pinmap/v1/pin_map_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.pinmap.v1.proto/src/ni/measurementlink/pinmap/v1/pin_map_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class PinMapServiceStub(object)`

Service to keep track of pin map resources.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class PinMapServiceServicer(object)`

Service to keep track of pin map resources.
    

#### `def CreatePinMapFromXml(self, request, context)`

Registers pin map with the PinMapService and returns a pin map resource.

        Status codes for errors:

        - INVALID_ARGUMENT: Pin map id is empty or has whitespace, or pin map xml string is not valid
        - ALREADY_EXISTS: Pin map resource with the specified pin map id already exists
        

#### `def UpdatePinMapFromXml(self, request, context)`

Updates registered pin map contents and returns it.
        Creates and registers a pin map if a pin map resource for the specified pin map id is not found.

        Status codes for errors:

        - INVALID_ARGUMENT: Pin map xml string is not valid
        

#### `def GetPinMap(self, request, context)`

Get registered pin map resource.

        Status codes for errors:

        - NOT_FOUND: Pin map resource for the specified pin map id is not found
        

#### `def QueryPins(self, request, context)`

Returns list of pins from the registered pin map resource.

        Status codes for errors:

        - NOT_FOUND: Pin map resource for the specified pin map id is not found
        

#### `def QueryRelays(self, request, context)`

Returns list of relays from the registered pin map resource.

        Status codes for errors:

        - NOT_FOUND: Pin map resource for the specified pin map id is not found
        

#### `def QueryResourceAccessInformation(self, request, context)`

Get instrument resource names, channels, and instrument type for the specified sites, pins or pin groups, relays or relay groups, instrument type in the registered pin map resource.
        Status codes for errors:

        - NOT_FOUND:

        - Pin map resource for the specified pin map id is not found.
        - Specified site number is not in the valid range for the registered pin map.

        - INVALID_ARGUMENT:

        - Specified pin or relay is not present in the registered pin map resource.
        - Empty string specified for a pin or relay name.
        

### `def add_PinMapServiceServicer_to_server(servicer, server)`

### `class PinMapService(object)`

Service to keep track of pin map resources.
    

#### `def CreatePinMapFromXml(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UpdatePinMapFromXml(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPinMap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryPins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryRelays(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryResourceAccessInformation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.proto/src/ni/measurementlink/pin_map_context_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.proto/src/ni/measurementlink/pin_map_context_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ni/measurementlink/pin_map_context.proto\x12\x12ni.measurementlink"2\n\rPinMapContext\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05B\x96\x01\n\x16com.ni.measurementlinkB\x12PinMapContextProtoP\x01Z\x0fpinmapcontextv1\xa2\x02\x03NIM\xaa\x02#NationalInstruments.MeasurementLink\xca\x02\x12NI\\MeasurementLink\xea\x02\x13NI::MeasurementLinkb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the measurement plug-in management service.

- `__all__ = ['BaseReservation', 'ChannelMapping', 'Client', 'Connection', 'GRPC_SERVICE_CLASS', 'GRPC_SERVICE_INTERFACE_NAME', 'INSTRUMENT_TYPE_NI_DAQMX', 'INSTRUMENT_TYPE_NI_DCPOWER', 'INSTRUMENT_TYPE_NI_DIGITAL_PATTERN', 'INSTRUMENT_TYPE_NI_DMM', 'INSTRUMENT_TYPE_NI_FGEN', 'INSTRUMENT_TYPE_NI_HSDIO', 'INSTRUMENT_TYPE_NI_MODEL_BASED_INSTRUMENT', 'INSTRUMENT_TYPE_NI_RELAY_DRIVER', 'INSTRUMENT_TYPE_NI_RFMX', 'INSTRUMENT_TYPE_NI_RFPM', 'INSTRUMENT_TYPE_NI_RFSA', 'INSTRUMENT_TYPE_NI_RFSG', 'INSTRUMENT_TYPE_NI_SCOPE', 'INSTRUMENT_TYPE_NI_SWITCH_EXECUTIVE_VIRTUAL_DEVICE', 'INSTRUMENT_TYPE_NONE', 'MultiSessionReservation', 'PinMapContext', 'MultiplexerSessionContainer', 'MultiplexerSessionInformation', 'SessionInformation', 'SessionInitializationBehavior', 'SessionManagementClient', 'SingleSessionReservation', 'SITE_SYSTEM_PINS', 'TypedConnection', 'TypedConnectionWithMultiplexer', 'TypedMultiplexerSessionInformation', 'TypedSessionInformation']`

### `def __getattr__(name: str) -> Any`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_annotations.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_annotations.py

### `def get_machine_details() -> tuple[dict[str, str], dict[str, str]]`

Get the machine details for reserved and registered annotations.

### `def remove_reservation_annotations(annotations: dict[str, str] | None) -> dict[str, str]`

Remove reserved annotations from the provided annotations.

### `def _get_hostname() -> str`

### `def _get_username() -> str`

### `def _get_ip_address() -> str`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_client.py

### MODULE DOCSTRING

Session management client class.

### `class SessionManagementClient(GrpcServiceClientBase[session_management_service_pb2_grpc.SessionManagementServiceStub])`

Client for accessing the NI Session Management Service via gRPC.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize a SessionManagementClient instance.

#### `def reserve_session(self, context: PinMapContext, pin_or_relay_names: str | Iterable[str] | None=None, instrument_type_id: str | None=None, timeout: float | None=0.0) -> SingleSessionReservation`

Reserve a single session.

        Reserve the session matching the given pins, sites, and instrument type ID and return the
        information needed to create or access the session.

        Args:
            context: Includes the pin map ID for the pin map in the Pin Map Service,
                as well as the list of sites for the measurement.

            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to use
                for the measurement.

                If unspecified, reserve sessions for all pins and relays in the registered pin map
                resource.

            instrument_type_id: Instrument type ID for the measurement.

                If unspecified, this method reserve sessions for all instrument types connected
                in the registered pin map resource.

                For NI instruments, use instrument type id constants, such as
                :py:const:`INSTRUMENT_TYPE_NI_DCPOWER` or :py:const:`INSTRUMENT_TYPE_NI_DMM`.

                For custom instruments, use the instrument type id defined in the pin map file.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the session and
            unreserve it.
        

#### `def reserve_sessions(self, context: PinMapContext, pin_or_relay_names: str | Iterable[str] | None=None, instrument_type_id: str | None=None, timeout: float | None=0.0) -> MultiSessionReservation`

Reserve multiple sessions.

        Reserve sessions matching the given pins, sites, and instrument type ID and return the
        information needed to create or access the sessions.

        Args:
            context: Includes the pin map ID for the pin map in the Pin Map Service,
                as well as the list of sites for the measurement.

            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to use
                for the measurement.

                If unspecified, reserve sessions for all pins and relays in the registered pin map
                resource.

            instrument_type_id: Instrument type ID for the measurement.

                If unspecified, this method reserves sessions for all instrument types connected
                in the registered pin map resource.

                For NI instruments, use instrument type id constants, such as
                :py:const:`INSTRUMENT_TYPE_NI_DCPOWER` or :py:const:`INSTRUMENT_TYPE_NI_DMM`.

                For custom instruments, use the instrument type id defined in the pin map file.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the sessions and
            unreserve them.
        

#### `def _reserve_sessions(self, context: PinMapContext, pin_or_relay_names: str | Iterable[str] | None=None, instrument_type_id: str | None=None, timeout: float | None=0.0) -> session_management_service_pb2.ReserveSessionsResponse`

#### `def _unreserve_sessions(self, session_info: Iterable[session_management_service_pb2.SessionInformation]) -> None`

Unreserves sessions so they can be accessed by other clients.

#### `def register_sessions(self, session_info: Iterable[SessionInformation]) -> None`

Register sessions with the session management service.

        Indicates that the sessions are open and will need to be closed later.

        Args:
            session_info: Sessions to register.
        

#### `def unregister_sessions(self, session_info: Iterable[SessionInformation]) -> None`

Unregisters sessions from the session management service.

        Indicates that the sessions have been closed and will need to be reopened before they can be
        used again.

        Args:
            session_info: Sessions to unregister.
        

#### `def reserve_all_registered_sessions(self, instrument_type_id: str | None=None, timeout: float | None=10.0) -> MultiSessionReservation`

Reserve all sessions currently registered with the session management service.

        Args:
            instrument_type_id: Instrument type ID for the measurement.

                If unspecified, reserve sessions for all instrument types connected in the
                registered pin map resource.

                For NI instruments, use instrument type id constants, such as
                :py:const:`INSTRUMENT_TYPE_NI_DCPOWER` or :py:const:`INSTRUMENT_TYPE_NI_DMM`.

                For custom instruments, use the instrument type id defined in the pin map file.

            timeout: Timeout in seconds.

                An arbitrary timeout to wait for the measurement to complete or be canceled.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the sessions and
            unreserve them.
        

#### `def register_multiplexer_sessions(self, multiplexer_session_info: Iterable[MultiplexerSessionInformation]) -> None`

Register multiplexer sessions with the session management service.

        Indicates that the sessions are open and will need to be closed later.

        Args:
            multiplexer_session_info: Sessions to register.
        

#### `def unregister_multiplexer_sessions(self, multiplexer_session_info: Iterable[MultiplexerSessionInformation]) -> None`

Unregisters multiplexer sessions from the session management service.

        Indicates that the sessions have been closed and will need to be reopened before they can be
        used again.

        Args:
            multiplexer_session_info: Sessions to unregister.
        

#### `def get_multiplexer_sessions(self, pin_map_context: PinMapContext, multiplexer_type_id: str | None=None) -> MultiplexerSessionContainer`

Get all multiplexer session infos matching the specified criteria.

        Returns the information needed to create or access the multiplexer sessions
        without reserving the connected instruments.

        Args:
            pin_map_context: Includes the pin map ID for the pin map in the pin map service,
                as well as the list of sites for the measurement.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            The multiplexer session container with the matching session infos.
        

#### `def get_all_registered_multiplexer_sessions(self, multiplexer_type_id: str | None=None) -> MultiplexerSessionContainer`

Get all multiplexer session infos registered with the session management service.

        Args:
            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            The multiplexer session container with the matching session infos registered
            with the session management service.
        

### `def _timeout_to_milliseconds(timeout: float | None) -> int`

### `def _to_group_mappings_dict(mappings: google.protobuf.internal.containers.MessageMap[str, session_management_service_pb2.ResolvedPinsOrRelays]) -> Mapping[str, Iterable[str]]`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_client_base.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_client_base.py

### `class StubProtocol(Protocol)`

Protocol for gRPC stub classes.

#### `def __init__(self, channel: grpc.Channel) -> None`

Initialize the gRPC client.

### `class GrpcServiceClientBase(Generic[TStub])`

Base class for NI gRPC service clients.

#### `def __init__(self, service_interface_name: str, service_class: str, stub_class: type[TStub], *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the gRPC client.

        Args:
            service_interface_name: The fully qualified name of the service interface.
            service_class: The name of the service class.
            stub_class: The gRPC stub class for the service.
            discovery_client: An optional discovery client (recommended).
            grpc_channel: An optional pin map gRPC channel.
            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the GrpcServiceClientBase.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the GrpcServiceClientBase.

#### `def close(self) -> None`

Close the client and clean up resources that it owns.

#### `def _get_stub(self) -> TStub`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_constants.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_constants.py

### MODULE DOCSTRING

Session management constants.

- `GRPC_SERVICE_INTERFACE_NAME = 'ni.measurementlink.sessionmanagement.v1.SessionManagementService'`

- `GRPC_SERVICE_CLASS = 'ni.measurementlink.sessionmanagement.v1.SessionManagementService'`

- `INSTRUMENT_TYPE_NONE = ''`

- `INSTRUMENT_TYPE_NI_DCPOWER = 'niDCPower'`

- `INSTRUMENT_TYPE_NI_HSDIO = 'niHSDIO'`

- `INSTRUMENT_TYPE_NI_RFSA = 'niRFSA'`

- `INSTRUMENT_TYPE_NI_RFMX = 'niRFmx'`

- `INSTRUMENT_TYPE_NI_RFSG = 'niRFSG'`

- `INSTRUMENT_TYPE_NI_RFPM = 'niRFPM'`

- `INSTRUMENT_TYPE_NI_DMM = 'niDMM'`

- `INSTRUMENT_TYPE_NI_DIGITAL_PATTERN = 'niDigitalPattern'`

- `INSTRUMENT_TYPE_NI_SCOPE = 'niScope'`

- `INSTRUMENT_TYPE_NI_FGEN = 'niFGen'`

- `INSTRUMENT_TYPE_NI_DAQMX = 'niDAQmx'`

- `INSTRUMENT_TYPE_NI_RELAY_DRIVER = 'niRelayDriver'`

- `INSTRUMENT_TYPE_NI_MODEL_BASED_INSTRUMENT = 'niModelBasedInstrument'`

- `INSTRUMENT_TYPE_NI_SWITCH_EXECUTIVE_VIRTUAL_DEVICE = 'niSwitchExecutiveVirtualDevice'`

- `SITE_SYSTEM_PINS = -1`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/__init__.py

### MODULE DOCSTRING

Shared code for interfacing with driver APIs.

- `_EXISTING_BEHAVIORS = [SessionInitializationBehavior.AUTO, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION]`

### `def closing_session_with_ts_code_module_support(initialization_behavior: SessionInitializationBehavior, session: TSession) -> ContextManager[TSession]`

Create a context manager that closes the session.

    Emulates the behavior of INITIALIZE_SESSION_THEN_DETACH and ATTACH_TO_SESSION_THEN_CLOSE.
    

### `def closing_session(session: TSession) -> ContextManager[TSession]`

A context manager that yields the session and closes it.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_configuration.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_configuration.py

### MODULE DOCSTRING

Measurement plug-in configuration options.

- `_PREFIX = 'MEASUREMENT_PLUGIN'`

### `class MIDriverOptions(NamedTuple)`

Modular instrument driver options.

#### `def update_from_config(self) -> Self`

Read options from the configuration file and return a new options object.

#### `def to_dict(self) -> dict[str, Any]`

Convert options to a dict to pass to nimi-python.

### `class NISwitchOptions(NamedTuple)`

NI-SWITCH driver options.

#### `def update_from_config(self) -> Self`

Read options from the configuration file and return a new options object.

- `NIDCPOWER_OPTIONS = MIDriverOptions('nidcpower').update_from_config()`

- `NIDIGITAL_OPTIONS = MIDriverOptions('nidigital').update_from_config()`

- `NIDMM_OPTIONS = MIDriverOptions('nidmm').update_from_config()`

- `NIFGEN_OPTIONS = MIDriverOptions('nifgen').update_from_config()`

- `NISCOPE_OPTIONS = MIDriverOptions('niscope').update_from_config()`

- `NISWITCH_OPTIONS = NISwitchOptions('niswitch').update_from_config()`

- `NISWITCH_MULTIPLEXER_OPTIONS = NISwitchOptions('niswitch_multiplexer').update_from_config()`

- `USE_GRPC_DEVICE_SERVER = _config(f'{_PREFIX}_USE_GRPC_DEVICE_SERVER', default=True, cast=bool)`

- `GRPC_DEVICE_SERVER_ADDRESS = _config(f'{_PREFIX}_GRPC_DEVICE_SERVER_ADDRESS', default='')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_dotenvpath.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_dotenvpath.py

### `def get_dotenv_search_path() -> Path`

Get the search path for loading the `.env` file.

### `def _has_dotenv_file(dir: Path) -> bool`

Check whether the dir or its parents contains a `.env` file.

### `def _get_script_or_exe_path() -> Path | None`

Get the path of the top-level script or PyInstaller EXE, if possible.

### `def _get_caller_path() -> Path | None`

Get the path of the module calling into this package, if possible.

### `def _get_package_path() -> Path`

Get the path of this package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_grpcdevice.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_grpcdevice.py

### MODULE DOCSTRING

Shared functions for interacting with NI gRPC Device Server.

- `SERVICE_CLASS = 'ni.measurementlink.v1.grpcdeviceserver'`

### `def get_grpc_device_server_location(discovery_client: DiscoveryClient, provided_interface: str) -> ServiceLocation | None`

Get an address targeting NI gRPC Device Server for unencrypted communication.

### `def _parse_url_to_service_location(url: str) -> ServiceLocation`

### `def get_insecure_grpc_device_server_channel(discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, provided_interface: str) -> grpc.Channel | None`

Get an unencrypted gRPC channel targeting NI gRPC Device Server.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidaqmx.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidaqmx.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: nidaqmx.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: nidaqmx.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: nidaqmx.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: nidaqmx.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: nidaqmx.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> nidaqmx.Task`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidcpower.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidcpower.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: nidcpower.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: nidcpower.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: nidcpower.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: nidcpower.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: nidcpower.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, reset: bool, options: dict[str, Any] | None, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> nidcpower.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidigital.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidigital.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: nidigital.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: nidigital.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: nidigital.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: nidigital.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: nidigital.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, reset_device: bool, options: dict[str, Any] | None, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> nidigital.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidmm.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nidmm.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: nidmm.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: nidmm.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: nidmm.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: nidmm.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: nidmm.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, reset_device: bool, options: dict[str, Any] | None, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> nidmm.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nifgen.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_nifgen.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: nifgen.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: nifgen.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: nifgen.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: nifgen.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: nifgen.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, reset_device: bool, options: dict[str, Any] | None, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> nifgen.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_niscope.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_niscope.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: niscope.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: niscope.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: niscope.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: niscope.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: niscope.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, reset_device: bool, options: dict[str, Any] | None, initialization_behavior: SessionInitializationBehavior) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation) -> niscope.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_niswitch.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_drivers/_niswitch.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: niswitch.SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: niswitch.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: niswitch.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: niswitch.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: niswitch.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION}`

### `class SessionConstructor()`

Constructs sessions based on SessionInformation.

#### `def __init__(self, discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool, topology: str | None, simulate: bool | None, reset_device: bool, initialization_behavior: SessionInitializationBehavior, *, is_multiplexer: bool=False) -> None`

Initialize the session constructor.

#### `def __call__(self, session_info: SessionInformation | MultiplexerSessionInformation) -> niswitch.Session`

Construct a session object.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_reservation.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_reservation.py

### MODULE DOCSTRING

Session management reservation classes.

- `_T = TypeVar('_T')`

### `def _to_iterable(value: _T | Iterable[_T] | None, default: Iterable[_T] | None=None) -> Iterable[_T]`

### `def _to_ordered_set(values: Iterable[_T]) -> AbstractSet[_T]`

### `def _quote(value: str) -> str`

### `def _quote_if_str(value: object) -> str`

### `def _check_optional_str_param(name: str, value: str | None) -> None`

### `def _check_optional_int_param(name: str, value: int | None) -> None`

### `def _check_matching_criterion(name: str, requested_values: Iterable[_T], expected_values: AbstractSet[_T]) -> None`

### `def _check_matching_multiplexer_criterion(name: str, requested_values: Iterable[_T], expected_values: AbstractSet[_T]) -> None`

### `def _describe_matching_criteria(pin_or_relay_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None, instrument_type_id: str | None=None) -> str`

### `class _ConnectionKey(NamedTuple)`

### `class _BaseSessionContainer(abc.ABC)`

Contains session management client and related properties.

#### `def __init__(self, session_management_client: SessionManagementClient) -> None`

Initialize the base session container.

#### `def _discovery_client(self) -> DiscoveryClient`

#### `def _grpc_channel_pool(self) -> GrpcChannelPool`

### `class MultiplexerSessionContainer(_BaseSessionContainer)`

Manages multiplexer session information.

#### `def __init__(self, session_management_client: SessionManagementClient, multiplexer_session_info: None | Sequence[session_management_service_pb2.MultiplexerSessionInformation]) -> None`

Initialize multiplexer object.

#### `def _multiplexer_type_ids(self) -> AbstractSet[str]`

#### `def multiplexer_session_info(self) -> Sequence[MultiplexerSessionInformation]`

Multiplexer session information object.

#### `def __enter__(self: Self) -> Self`

Context management protocol. Returns self.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Context management protocol.

#### `def _get_multiplexer_session_info_for_resource_name(self, multiplexer_resource_name: str) -> MultiplexerSessionInformation | None`

#### `def _get_multiplexer_session_infos_for_type_id(self, multiplexer_type_id: str) -> list[MultiplexerSessionInformation]`

#### `def _validate_and_get_matching_multiplexer_session_infos(self, multiplexer_type_ids: Iterable[str]) -> list[MultiplexerSessionInformation]`

#### `def _cache_multiplexer_session(self, session_name: str, session: object) -> Generator[None]`

#### `def _initialize_multiplexer_session_core(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None, closing_function: None | Callable[[TMultiplexerSession], ContextManager[TMultiplexerSession]]=None) -> Generator[TypedMultiplexerSessionInformation[TMultiplexerSession]]`

#### `def _initialize_multiplexer_sessions_core(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None, closing_function: None | Callable[[TMultiplexerSession], ContextManager[TMultiplexerSession]]=None) -> Generator[Sequence[TypedMultiplexerSessionInformation[TMultiplexerSession]]]`

#### `def initialize_multiplexer_session(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None=None) -> ContextManager[TypedMultiplexerSessionInformation[TMultiplexerSession]]`

Initialize a single multiplexer session.

        This is a generic method that supports any multiplexer driver.

        Args:
            session_constructor: A function that constructs multiplexer sessions
                based on multiplexer session information.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a multiplexer session information
                object. The session object is available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available or
                too many multiplexer sessions are available.
        

#### `def initialize_multiplexer_sessions(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None=None) -> ContextManager[Sequence[TypedMultiplexerSessionInformation[TMultiplexerSession]]]`

Initialize multiple multiplexer sessions.

        This is a generic method that supports any multiplexer driver.

        Args:
            session_constructor: A function that constructs multiplexer sessions
                based on multiplexer session information.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a sequence of multiplexer session information
                objects. The session objects are available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available.
        

#### `def initialize_niswitch_multiplexer_session(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, multiplexer_type_id: str | None=None) -> ContextManager[TypedMultiplexerSessionInformation[niswitch.Session]]`

Initialize a single NI-SWITCH multiplexer session.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE`` in the
                configuration file (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a session information object. The
                multiplexer session object is available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available or
                too many multiplexer sessions are available.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

#### `def initialize_niswitch_multiplexer_sessions(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, multiplexer_type_id: str | None=None) -> ContextManager[Sequence[TypedMultiplexerSessionInformation[niswitch.Session]]]`

Initialize multiple NI-SWITCH multiplexer sessions.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE`` in the
                configuration file (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a sequence of multiplexer session
                information objects. The session objects are available via
                the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

### `class BaseReservation(_BaseSessionContainer)`

Manages session reservation.

#### `def __init__(self, session_management_client: SessionManagementClient, session_info: Sequence[session_management_service_pb2.SessionInformation], multiplexer_session_info: None | Sequence[session_management_service_pb2.MultiplexerSessionInformation]=None, pin_or_relay_group_mappings: Mapping[str, Iterable[str]] | None=None, reserved_pin_or_relay_names: str | Iterable[str] | None=None, reserved_sites: Iterable[int] | None=None) -> None`

Initialize reservation object.

#### `def _reserved_pin_or_relay_names(self) -> AbstractSet[str]`

#### `def _reserved_sites(self) -> AbstractSet[int]`

#### `def _reserved_instrument_type_ids(self) -> AbstractSet[str]`

#### `def _connection_cache(self) -> dict[_ConnectionKey, Connection]`

#### `def _multiplexer_session_cache(self) -> dict[str, object]`

#### `def multiplexer_session_info(self) -> Sequence[MultiplexerSessionInformation]`

Multiplexer session information object.

#### `def __enter__(self: Self) -> Self`

Context management protocol. Returns self.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> Literal[False]`

Context management protocol. Calls unreserve().

#### `def unreserve(self) -> None`

Unreserve sessions.

#### `def _cache_session(self, session_name: str, session: object) -> Generator[None]`

#### `def _get_matching_session_infos(self, instrument_type_id: str) -> list[SessionInformation]`

#### `def _get_resolved_pin_or_relay_names(self, reserved_pin_or_relay_names: Iterable[str]) -> Iterable[str]`

#### `def _initialize_session_core(self, session_constructor: Callable[[SessionInformation], TSession], instrument_type_id: str, closing_function: Callable[[TSession], ContextManager[TSession]] | None=None) -> Generator[TypedSessionInformation[TSession]]`

#### `def _initialize_sessions_core(self, session_constructor: Callable[[SessionInformation], TSession], instrument_type_id: str, closing_function: Callable[[TSession], ContextManager[TSession]] | None=None) -> Generator[Sequence[TypedSessionInformation[TSession]]]`

#### `def _get_connection_core(self, session_type: type[TSession], pin_or_relay_name: str | None=None, site: int | None=None, instrument_type_id: str | None=None, multiplexer_session_type: type[TMultiplexerSession] | None=None) -> TypedConnection[TSession]`

#### `def _get_connections_core(self, session_type: type[TSession], pin_or_relay_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None, instrument_type_id: str | None=None, multiplexer_session_type: type[TMultiplexerSession] | None=None) -> Sequence[TypedConnection[TSession]]`

#### `def initialize_session(self, session_constructor: Callable[[SessionInformation], TSession], instrument_type_id: str) -> ContextManager[TypedSessionInformation[TSession]]`

Initialize a single instrument session.

        This is a generic method that supports any instrument driver.

        Args:
            session_constructor: A function that constructs sessions based on
                session information.

            instrument_type_id: Instrument type ID for the session.

                For custom instruments, use the instrument type id defined in
                the pin map file.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If the instrument type ID is empty, no reserved sessions
                match the instrument type ID, or too many reserved sessions
                match the instrument type ID.
        

#### `def initialize_multiplexer_session(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None=None) -> ContextManager[TypedMultiplexerSessionInformation[TMultiplexerSession]]`

Initialize a single multiplexer session.

        This is a generic method that supports any multiplexer driver.

        Args:
            session_constructor: A function that constructs multiplexer sessions
                based on multiplexer session information.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a multiplexer session information
                object. The session object is available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available or
                too many multiplexer sessions are available.
        

#### `def initialize_sessions(self, session_constructor: Callable[[SessionInformation], TSession], instrument_type_id: str) -> ContextManager[Sequence[TypedSessionInformation[TSession]]]`

Initialize multiple instrument sessions.

        This is a generic method that supports any instrument driver.

        Args:
            session_constructor: A function that constructs sessions based on
                session information.

            instrument_type_id: Instrument type ID for the session.

                For custom instruments, use the instrument type id defined in
                the pin map file.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If the instrument type ID is empty or no reserved
                sessions matched the instrument type ID.
        

#### `def initialize_multiplexer_sessions(self, session_constructor: Callable[[MultiplexerSessionInformation], TMultiplexerSession], multiplexer_type_id: str | None=None) -> ContextManager[Sequence[TypedMultiplexerSessionInformation[TMultiplexerSession]]]`

Initialize multiple multiplexer sessions.

        This is a generic method that supports any multiplexer driver.

        Args:
            session_constructor: A function that constructs multiplexer sessions
                based on multiplexer session information.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a sequence of multiplexer session information
                objects. The session objects are available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available.
        

#### `def get_connection(self, session_type: type[TSession], pin_or_relay_name: str | None=None, site: int | None=None, instrument_type_id: str | None=None) -> TypedConnection[TSession]`

Get the connection matching the specified criteria.

        This is a generic method that supports any instrument driver.

        Args:
            session_type: The session type.

            pin_or_relay_name: The pin or relay name to match against. If not
                specified, the pin or relay name is ignored when matching
                connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

            instrument_type_id: The instrument type ID to match against. If not
                specified, the instrument type ID is ignored when matching
                connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_connection_with_multiplexer(self, session_type: type[TSession], multiplexer_session_type: type[TMultiplexerSession], pin_or_relay_name: str | None=None, site: int | None=None, instrument_type_id: str | None=None) -> TypedConnectionWithMultiplexer[TSession, TMultiplexerSession]`

Get the connection matching the specified criteria.

        This is a generic method that supports any instrument driver.

        Args:
            session_type: The instrument session type.

            multiplexer_session_type: The multiplexer session type.

            pin_or_relay_name: The pin or relay name to match against. If not
                specified, the pin or relay name is ignored when matching
                connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

            instrument_type_id: The instrument type ID to match against. If not
                specified, the instrument type ID is ignored when matching
                connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_connections(self, session_type: type[TSession], pin_or_relay_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None, instrument_type_id: str | None=None) -> Sequence[TypedConnection[TSession]]`

Get all connections matching the specified criteria.

        This is a generic method that supports any instrument driver.

        Args:
            session_type: The expected session type.

            pin_or_relay_names: The pin or relay name(s) to match against. If
                not specified, the pin or relay name is ignored when matching
                connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

            instrument_type_id: The instrument type ID to match against. If not
                specified, the instrument type ID is ignored when matching
                connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_connections_with_multiplexer(self, session_type: type[TSession], multiplexer_session_type: type[TMultiplexerSession], pin_or_relay_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None, instrument_type_id: str | None=None) -> Sequence[TypedConnectionWithMultiplexer[TSession, TMultiplexerSession]]`

Get all connections matching the specified criteria.

        This is a generic method that supports any instrument driver.

        Args:
            session_type: The instrument session type.

            multiplexer_session_type: The multiplexer session type.

            pin_or_relay_names: The pin or relay name(s) to match against. If
                not specified, the pin or relay name is ignored when matching
                connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

            instrument_type_id: The instrument type ID to match against. If not
                specified, the instrument type ID is ignored when matching
                connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def create_nidaqmx_task(self, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[nidaqmx.Task]]`

Create a single NI-DAQmx task.

        Args:
            initialization_behavior: Specifies whether the NI gRPC Device Server
                will create a new task or attach to an existing task.

        Returns:
            A context manager that yields a session information object. The task
            object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-DAQmx tasks are reserved or too many
                NI-DAQmx tasks are reserved.

        Note:
            If the ``session_exists`` field is ``False``, the returned task is
            empty and the caller is expected to add channels to it.

        See Also:
            For more details, see :py:class:`nidaqmx.Task`.
        

#### `def create_nidaqmx_tasks(self, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[nidaqmx.Task]]]`

Create multiple NI-DAQmx tasks.

        Args:
            initialization_behavior: Specifies whether the NI gRPC Device Server
                will create a new task or attach to an existing task.

        Returns:
            A context manager that yields a sequence of session information
            objects. The task objects are available via the ``session`` field.

        Raises:
            ValueError: If no NI-DAQmx tasks are reserved.

        Note:
            If the ``session_exists`` field is ``False``, the returned tasks are
            empty and the caller is expected to add channels to them.

        See Also:
            For more details, see :py:class:`nidaqmx.Task`.
        

#### `def get_nidaqmx_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[nidaqmx.Task]`

Get the NI-DAQmx connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidaqmx_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[nidaqmx.Task, TMultiplexerSession]`

Get the NI-DAQmx connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidaqmx_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[nidaqmx.Task]]`

Get all NI-DAQmx connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_nidaqmx_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[nidaqmx.Task, TMultiplexerSession]]`

Get all NI-DAQmx connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_nidcpower_session(self, reset: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[nidcpower.Session]]`

Initialize a single NI-DCPower instrument session.

        Args:
            reset: Specifies whether to reset channel(s) during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDCPOWER_SIMULATE``, ``NIDCPOWER_BOARD_TYPE``, and
                ``NIDCPOWER_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-DCPower sessions are reserved or too many
                NI-DCPower sessions are reserved.

        See Also:
            For more details, see :py:class:`nidcpower.Session`.
        

#### `def initialize_nidcpower_sessions(self, reset: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[nidcpower.Session]]]`

Initialize multiple NI-DCPower instrument sessions.

        Args:
            reset: Specifies whether to reset channel(s) during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDCPOWER_SIMULATE``, ``NIDCPOWER_BOARD_TYPE``, and
                ``NIDCPOWER_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no NI-DCPower sessions are reserved.

        See Also:
            For more details, see :py:class:`nidcpower.Session`.
        

#### `def get_nidcpower_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[nidcpower.Session]`

Get the NI-DCPower connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidcpower_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[nidcpower.Session, TMultiplexerSession]`

Get the NI-DCPower connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidcpower_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[nidcpower.Session]]`

Get all NI-DCPower connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_nidcpower_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[nidcpower.Session, TMultiplexerSession]]`

Get all NI-DCPower connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_nidigital_session(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[nidigital.Session]]`

Initialize a single NI-Digital Pattern instrument session.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDIGITAL_SIMULATE``, ``NIDIGITAL_BOARD_TYPE``, and
                ``NIDIGITAL_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-Digital sessions are reserved or too many
                NI-Digital sessions are reserved.

        See Also:
            For more details, see :py:class:`nidigital.Session`.
        

#### `def initialize_nidigital_sessions(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[nidigital.Session]]]`

Initialize multiple NI-Digital Pattern instrument sessions.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDIGITAL_SIMULATE``, ``NIDIGITAL_BOARD_TYPE``, and
                ``NIDIGITAL_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no NI-Digital sessions are reserved.

        See Also:
            For more details, see :py:class:`nidigital.Session`.
        

#### `def get_nidigital_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[nidigital.Session]`

Get the NI-Digital Pattern connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidigital_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[nidigital.Session, TMultiplexerSession]`

Get the NI-Digital Pattern connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidigital_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[nidigital.Session]]`

Get all NI-Digital Pattern connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_nidigital_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[nidigital.Session, TMultiplexerSession]]`

Get all NI-Digital Pattern connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_nidmm_session(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[nidmm.Session]]`

Initialize a single NI-DMM instrument session.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDMM_SIMULATE``, ``NIDMM_BOARD_TYPE``, and ``NIDMM_MODEL`` in
                the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-DMM sessions are reserved or too many
                NI-DMM sessions are reserved.

        See Also:
            For more details, see :py:class:`nidmm.Session`.
        

#### `def initialize_nidmm_sessions(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[nidmm.Session]]]`

Initialize multiple NI-DMM instrument sessions.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIDMM_SIMULATE``, ``NIDMM_BOARD_TYPE``, and ``NIDMM_MODEL`` in
                the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no NI-DMM sessions are reserved.

        See Also:
            For more details, see :py:class:`nidmm.Session`.
        

#### `def get_nidmm_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[nidmm.Session]`

Get the NI-DMM connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidmm_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[nidmm.Session, TMultiplexerSession]`

Get the NI-DMM connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nidmm_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[nidmm.Session]]`

Get all NI-DMM connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_nidmm_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[nidmm.Session, TMultiplexerSession]]`

Get all NI-DMM connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_nifgen_session(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[nifgen.Session]]`

Initialize a single NI-FGEN instrument session.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIFGEN_SIMULATE``, ``NIFGEN_BOARD_TYPE``, and ``NIFGEN_MODEL``
                in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-FGEN sessions are reserved or too many NI-FGEN
                sessions are reserved.

        See Also:
            For more details, see :py:class:`nifgen.Session`.
        

#### `def initialize_nifgen_sessions(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[nifgen.Session]]]`

Initialize multiple NI-FGEN instrument sessions.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NIFGEN_SIMULATE``, ``NIFGEN_BOARD_TYPE``, and ``NIFGEN_MODEL``
                in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no NI-FGEN sessions are reserved.

        See Also:
            For more details, see :py:class:`nifgen.Session`.
        

#### `def get_nifgen_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[nifgen.Session]`

Get the NI-FGEN connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nifgen_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[nifgen.Session, TMultiplexerSession]`

Get the NI-FGEN connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_nifgen_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[nifgen.Session]]`

Get all NI-FGEN connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_nifgen_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[nifgen.Session, TMultiplexerSession]]`

Get all NI-FGEN connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_niscope_session(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[niscope.Session]]`

Initialize a single NI-SCOPE instrument session.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NISCOPE_SIMULATE``, ``NISCOPE_BOARD_TYPE``, and
                ``NISCOPE_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no NI-SCOPE sessions are reserved or too many
                NI-SCOPE sessions are reserved.

        See Also:
            For more details, see :py:class:`niscope.Session`.
        

#### `def initialize_niscope_sessions(self, reset_device: bool=False, options: dict[str, Any] | None=None, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[niscope.Session]]]`

Initialize multiple NI-SCOPE instrument sessions.

        Args:
            reset_device: Specifies whether to reset the instrument during the
                initialization procedure.

            options: Specifies the initial value of certain properties for the
                session. If this argument is not specified, the default value is
                an empty dict, which you may override by specifying
                ``NISCOPE_SIMULATE``, ``NISCOPE_BOARD_TYPE``, and
                ``NISCOPE_MODEL`` in the configuration file (``.env``).

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no NI-SCOPE sessions are reserved.

        See Also:
            For more details, see :py:class:`niscope.Session`.
        

#### `def get_niscope_connection(self, pin_name: str | None=None, site: int | None=None) -> TypedConnection[niscope.Session]`

Get the NI-SCOPE connection matching the specified criteria.

        Args:
            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_niscope_connection_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_name: str | None=None, site: int | None=None) -> TypedConnectionWithMultiplexer[niscope.Session, TMultiplexerSession]`

Get the NI-SCOPE connection matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_name: The pin name to match against. If not specified, the pin
                name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection along with its multiplexer info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_niscope_connections(self, pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[niscope.Session]]`

Get all NI-SCOPE connections matching the specified criteria.

        Args:
            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def get_niscope_connections_with_multiplexer(self, multiplexer_session_type: type[TMultiplexerSession], pin_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnectionWithMultiplexer[niscope.Session, TMultiplexerSession]]`

Get all NI-SCOPE connections matching the specified criteria.

        Args:
            multiplexer_session_type: The multiplexer session type.

            pin_names: The pin name(s) to match against. If not specified, the
                pin name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections along with their multiplexer(s) info.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_niswitch_session(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[TypedSessionInformation[niswitch.Session]]`

Initialize a single NI-SWITCH relay driver instrument session.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_SIMULATE`` in the configuration file
                (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a session information object. The
            session object is available via the ``session`` field.

        Raises:
            ValueError: If no relay driver sessions are reserved or
                too many relay driver sessions are reserved.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

#### `def initialize_niswitch_sessions(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> ContextManager[Sequence[TypedSessionInformation[niswitch.Session]]]`

Initialize multiple NI-SWITCH relay driver instrument sessions.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_SIMULATE`` in the configuration file
                (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

        Returns:
            A context manager that yields a sequence of session information
            objects. The session objects are available via the ``session``
            field.

        Raises:
            ValueError: If no relay driver sessions are reserved.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

#### `def get_niswitch_connection(self, relay_name: str | None=None, site: int | None=None) -> TypedConnection[niswitch.Session]`

Get the NI-SWITCH relay driver connection matching the specified criteria.

        Args:
            relay_name: The relay name to match against. If not specified, the
                relay name is ignored when matching connections.

            site: The site number to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connection.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match or too many reserved
                connections match.
        

#### `def get_niswitch_connections(self, relay_names: str | Iterable[str] | None=None, sites: int | Iterable[int] | None=None) -> Sequence[TypedConnection[niswitch.Session]]`

Get all NI-SWITCH relay driver connections matching the specified criteria.

        Args:
            relay_names: The relay name(s) to match against. If not specified,
                the relay name is ignored when matching connections.

            sites: The site number(s) to match against. If not specified, the
                site number is ignored when matching connections.

        Returns:
            The matching connections.

        Raises:
            TypeError: If the argument types or session type are incorrect.

            ValueError: If no reserved connections match.
        

#### `def initialize_niswitch_multiplexer_session(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, multiplexer_type_id: str | None=None) -> ContextManager[TypedMultiplexerSessionInformation[niswitch.Session]]`

Initialize a single NI-SWITCH multiplexer session.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE`` in the configuration file
                (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a session information object. The
                multiplexer session object is available via the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available or
                too many multiplexer sessions are available.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

#### `def initialize_niswitch_multiplexer_sessions(self, topology: str | None=None, simulate: bool | None=None, reset_device: bool=False, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, multiplexer_type_id: str | None=None) -> ContextManager[Sequence[TypedMultiplexerSessionInformation[niswitch.Session]]]`

Initialize multiple NI-SWITCH multiplexer sessions.

        Args:
            topology: Specifies the switch topology. If this argument is not
                specified, the default value is "Configured Topology", which you
                may override by setting ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_TOPOLOGY`` in
                the configuration file (``.env``).

            simulate: Enables or disables simulation of the switch module. If
                this argument is not specified, the default value is ``False``,
                which you may override by setting
                ``MEASUREMENT_PLUGIN_NISWITCH_MULTIPLEXER_SIMULATE`` in the configuration file
                (``.env``).

            reset_device: Specifies whether to reset the switch module during
                the initialization procedure.

            initialization_behavior: Specifies whether the NI gRPC Device Server
                will initialize a new session or attach to an existing session.

            multiplexer_type_id: User-defined identifier for the multiplexer
                type in the pin map editor. If not specified, the multiplexer
                type id is ignored when matching multiplexer sessions.

        Returns:
            A context manager that yields a sequence of multiplexer session
                information objects. The session objects are available via
                the ``session`` field.

        Raises:
            TypeError: If the argument types are incorrect.

            ValueError: If no multiplexer sessions are available.

        See Also:
            For more details, see :py:class:`niswitch.Session`.
        

### `class SingleSessionReservation(BaseReservation)`

Manages reservation for a single session.

#### `def session_info(self) -> SessionInformation`

Single session information object.

### `class MultiSessionReservation(BaseReservation)`

Manages reservation for multiple sessions.

#### `def session_info(self) -> list[SessionInformation]`

Multiple session information objects.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_types.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/src/ni/measurementlink/sessionmanagement/v1/client/_types.py

### MODULE DOCSTRING

Session management data types.

### `class PinMapContext(NamedTuple)`

Container for the pin map and sites.

#### `def _from_grpc(cls, other: pin_map_context_pb2.PinMapContext) -> PinMapContext`

#### `def _to_grpc(self) -> pin_map_context_pb2.PinMapContext`

### `class ChannelMapping(NamedTuple)`

Mapping of each channel to the pin and site it is connected to.

#### `def _from_grpc_v1(cls, other: session_management_service_pb2.ChannelMapping) -> ChannelMapping`

#### `def _to_grpc_v1(self) -> session_management_service_pb2.ChannelMapping`

### `class SessionInformation(NamedTuple)`

Container for the session information.

#### `def _check_runtime_type(self, session_type: type) -> None`

#### `def _with_session(self, session: object) -> SessionInformation`

#### `def _from_grpc_v1(cls, other: session_management_service_pb2.SessionInformation) -> SessionInformation`

#### `def _to_grpc_v1(self) -> session_management_service_pb2.SessionInformation`

### `class TypedSessionInformation(Protocol, Generic[TSession_co])`

Generic version of :any:`SessionInformation` that preserves the session type.

    For more details, see the corresponding documentation for :any:`SessionInformation`.
    

#### `def session_name(self) -> str`

Session name used by the session management service and NI gRPC Device Server.

#### `def resource_name(self) -> str`

Resource name used to open this session in the driver.

#### `def channel_list(self) -> str`

Channel list used for driver initialization and measurement methods.

#### `def instrument_type_id(self) -> str`

Indicates the instrument type for this session.

#### `def session_exists(self) -> bool`

Indicates whether the session is registered with the session management service.

#### `def channel_mappings(self) -> Iterable[ChannelMapping]`

List of mappings from channels to pins and sites.

#### `def session(self) -> TSession_co`

The driver session object.

### `class MultiplexerSessionInformation(NamedTuple)`

Container for the multiplexer session information.

#### `def _check_runtime_type(self, multiplexer_session_type: type) -> None`

#### `def _with_session(self, session: object) -> MultiplexerSessionInformation`

#### `def _from_grpc_v1(cls, other: session_management_service_pb2.MultiplexerSessionInformation) -> MultiplexerSessionInformation`

#### `def _to_grpc_v1(self) -> session_management_service_pb2.MultiplexerSessionInformation`

### `class TypedMultiplexerSessionInformation(Protocol, Generic[TMultiplexerSession_co])`

Generic version of :any:`MultiplexerSessionInformation` that preserves the session type.

    For more details, see the corresponding documentation of :any:`MultiplexerSessionInformation`.
    

#### `def session_name(self) -> str`

Session name used by the session management service and NI gRPC Device Server.

#### `def resource_name(self) -> str`

Resource name used to open this session in the driver.

#### `def multiplexer_type_id(self) -> str`

User-defined identifier for the multiplexer type in the pin map editor.

#### `def session_exists(self) -> bool`

Indicates whether the session is registered with the session management service.

#### `def session(self) -> TMultiplexerSession_co`

The driver session object.

### `class Connection(NamedTuple)`

Describes the connection between an instance of a pin and an instrument channel.

    This object maps a pin or relay on a specific site to the corresponding
    instrument session and channel name.
    

#### `def session(self) -> object`

The instrument session.

#### `def multiplexer_session(self) -> object`

The multiplexer session.

#### `def _check_runtime_type(self, session_type: type) -> None`

#### `def _check_runtime_multiplexer_type(self, multiplexer_session_type: type) -> None`

#### `def _with_session(self, session: object) -> Connection`

#### `def _with_multiplexer_session(self, session: object) -> Connection`

### `class TypedConnection(Protocol, Generic[TSession_co])`

Generic version of :any:`Connection` that preserves the session type.

    For more details, see the corresponding documentation for :any:`Connection`.
    

#### `def pin_or_relay_name(self) -> str`

The pin or relay name.

#### `def site(self) -> int`

The site number.

        For system pins/relays, the site number is :any:`SITE_SYSTEM_PINS` (-1) as they
        do not belong to a specific site.
        

#### `def channel_name(self) -> str`

The instrument channel name.

#### `def session_info(self) -> TypedSessionInformation[TSession_co]`

The instrument session information.

#### `def session(self) -> TSession_co`

The instrument session.

### `class TypedConnectionWithMultiplexer(TypedConnection[TSession_co], Protocol, Generic[TSession_co, TMultiplexerSession_co])`

Generic version of `Connection` that preserves the instrument and multiplexer session type.

    For more details, see the corresponding documentation for `Connection`.
    

#### `def multiplexer_resource_name(self) -> str`

Resource name used to open this session in the driver.

#### `def multiplexer_type_id(self) -> str`

User-defined identifier for the multiplexer type in the pin map editor.

#### `def multiplexer_route(self) -> str`

The multiplexer route through which the pin is connected to an instrument's channel.

#### `def multiplexer_session_info(self) -> TypedMultiplexerSessionInformation[TMultiplexerSession_co]`

The multiplexer session information.

#### `def multiplexer_session(self) -> TMultiplexerSession_co`

The multiplexer session.

### `class SessionInitializationBehavior(IntEnum)`

Specifies whether to initialize a new session or attach to an existing session.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/tests/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.client/tests/unit/test_annotations.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.client/tests/unit/test_annotations.py

### `def test___machine_details___get_machine_details___returns_reserved_and_registered() -> None`

### `def test___annotations_dict_with_reserved_keys___remove_reservation_annotations___removes_reserved_keys() -> None`

### `def test___machine_details___get_machine_details___values_not_empty() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/annotations/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/annotations/__init__.py

### MODULE DOCSTRING

Constants for session client details annotations.

- `RESERVED_HOSTNAME = 'ni/reserved.hostname'`

- `RESERVED_USERNAME = 'ni/reserved.username'`

- `RESERVED_IPADDRESS = 'ni/reserved.ipaddress'`

- `REGISTERED_HOSTNAME = 'ni/registered.hostname'`

- `REGISTERED_USERNAME = 'ni/registered.username'`

- `REGISTERED_IPADDRESS = 'ni/registered.ipaddress'`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/session_management_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/session_management_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHni/measurementlink/sessionmanagement/v1/session_management_service.proto\x12\'ni.measurementlink.sessionmanagement.v1\x1a(ni/measurementlink/pin_map_context.proto\x1a\rsession.proto"\xa2\x03\n\x12SessionInformation\x12\'\n\x07session\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x14\n\x0cchannel_list\x18\x03 \x01(\t\x12\x1a\n\x12instrument_type_id\x18\x04 \x01(\t\x12\x16\n\x0esession_exists\x18\x05 \x01(\x08\x12\x18\n\x10session_reserved\x18\x07 \x01(\x08\x12Q\n\x10channel_mappings\x18\x06 \x03(\x0b27.ni.measurementlink.sessionmanagement.v1.ChannelMapping\x12a\n\x0bannotations\x18\x08 \x03(\x0b2L.ni.measurementlink.sessionmanagement.v1.SessionInformation.AnnotationsEntry\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x88\x01\n\x0eChannelMapping\x12\x19\n\x11pin_or_relay_name\x18\x01 \x01(\t\x12\x0c\n\x04site\x18\x02 \x01(\x05\x12\x0f\n\x07channel\x18\x03 \x01(\t\x12!\n\x19multiplexer_resource_name\x18\x04 \x01(\t\x12\x19\n\x11multiplexer_route\x18\x05 \x01(\t"\xb6\x02\n\x1dMultiplexerSessionInformation\x12\'\n\x07session\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x1b\n\x13multiplexer_type_id\x18\x03 \x01(\t\x12\x16\n\x0esession_exists\x18\x04 \x01(\x08\x12l\n\x0bannotations\x18\x05 \x03(\x0b2W.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation.AnnotationsEntry\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc8\x02\n\x16ReserveSessionsRequest\x12:\n\x0fpin_map_context\x18\x01 \x01(\x0b2!.ni.measurementlink.PinMapContext\x12\x1a\n\x12pin_or_relay_names\x18\x02 \x03(\t\x12\x1a\n\x12instrument_type_id\x18\x03 \x01(\t\x12\x1f\n\x17timeout_in_milliseconds\x18\x04 \x01(\x05\x12e\n\x0bannotations\x18\x05 \x03(\x0b2P.ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest.AnnotationsEntry\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xb0\x03\n\x17ReserveSessionsResponse\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation\x12d\n\x14multiplexer_sessions\x18\x02 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation\x12k\n\x0egroup_mappings\x18\x03 \x03(\x0b2S.ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse.GroupMappingsEntry\x1as\n\x12GroupMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12L\n\x05value\x18\x02 \x01(\x0b2=.ni.measurementlink.sessionmanagement.v1.ResolvedPinsOrRelays:\x028\x01"i\n\x18UnreserveSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1b\n\x19UnreserveSessionsResponse"h\n\x17RegisterSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1a\n\x18RegisterSessionsResponse"j\n\x19UnregisterSessionsRequest\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x1c\n\x1aUnregisterSessionsResponse"\x8a\x02\n#ReserveAllRegisteredSessionsRequest\x12\x1f\n\x17timeout_in_milliseconds\x18\x01 \x01(\x05\x12\x1a\n\x12instrument_type_id\x18\x02 \x01(\t\x12r\n\x0bannotations\x18\x03 \x03(\x0b2].ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest.AnnotationsEntry\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"u\n$ReserveAllRegisteredSessionsResponse\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation"\x8a\x01\n"RegisterMultiplexerSessionsRequest\x12d\n\x14multiplexer_sessions\x18\x01 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation"%\n#RegisterMultiplexerSessionsResponse"\x8c\x01\n$UnregisterMultiplexerSessionsRequest\x12d\n\x14multiplexer_sessions\x18\x01 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation"\'\n%UnregisterMultiplexerSessionsResponse"x\n\x1dGetMultiplexerSessionsRequest\x12:\n\x0fpin_map_context\x18\x01 \x01(\x0b2!.ni.measurementlink.PinMapContext\x12\x1b\n\x13multiplexer_type_id\x18\x02 \x01(\t"\x86\x01\n\x1eGetMultiplexerSessionsResponse\x12d\n\x14multiplexer_sessions\x18\x01 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation"I\n*GetAllRegisteredMultiplexerSessionsRequest\x12\x1b\n\x13multiplexer_type_id\x18\x01 \x01(\t"\x93\x01\n+GetAllRegisteredMultiplexerSessionsResponse\x12d\n\x14multiplexer_sessions\x18\x01 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation"2\n\x14ResolvedPinsOrRelays\x12\x1a\n\x12pin_or_relay_names\x18\x01 \x03(\t"M\n\x12GetSessionsRequest\x12\x1a\n\x12instrument_type_id\x18\x01 \x01(\t\x12\x1b\n\x13multiplexer_type_id\x18\x02 \x01(\t"\xca\x01\n\x13GetSessionsResponse\x12M\n\x08sessions\x18\x01 \x03(\x0b2;.ni.measurementlink.sessionmanagement.v1.SessionInformation\x12d\n\x14multiplexer_sessions\x18\x02 \x03(\x0b2F.ni.measurementlink.sessionmanagement.v1.MultiplexerSessionInformation2\xcc\r\n\x18SessionManagementService\x12\x94\x01\n\x0fReserveSessions\x12?.ni.measurementlink.sessionmanagement.v1.ReserveSessionsRequest\x1a@.ni.measurementlink.sessionmanagement.v1.ReserveSessionsResponse\x12\x9a\x01\n\x11UnreserveSessions\x12A.ni.measurementlink.sessionmanagement.v1.UnreserveSessionsRequest\x1aB.ni.measurementlink.sessionmanagement.v1.UnreserveSessionsResponse\x12\x97\x01\n\x10RegisterSessions\x12@.ni.measurementlink.sessionmanagement.v1.RegisterSessionsRequest\x1aA.ni.measurementlink.sessionmanagement.v1.RegisterSessionsResponse\x12\x9d\x01\n\x12UnregisterSessions\x12B.ni.measurementlink.sessionmanagement.v1.UnregisterSessionsRequest\x1aC.ni.measurementlink.sessionmanagement.v1.UnregisterSessionsResponse\x12\xbb\x01\n\x1cReserveAllRegisteredSessions\x12L.ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsRequest\x1aM.ni.measurementlink.sessionmanagement.v1.ReserveAllRegisteredSessionsResponse\x12\xb8\x01\n\x1bRegisterMultiplexerSessions\x12K.ni.measurementlink.sessionmanagement.v1.RegisterMultiplexerSessionsRequest\x1aL.ni.measurementlink.sessionmanagement.v1.RegisterMultiplexerSessionsResponse\x12\xbe\x01\n\x1dUnregisterMultiplexerSessions\x12M.ni.measurementlink.sessionmanagement.v1.UnregisterMultiplexerSessionsRequest\x1aN.ni.measurementlink.sessionmanagement.v1.UnregisterMultiplexerSessionsResponse\x12\xa9\x01\n\x16GetMultiplexerSessions\x12F.ni.measurementlink.sessionmanagement.v1.GetMultiplexerSessionsRequest\x1aG.ni.measurementlink.sessionmanagement.v1.GetMultiplexerSessionsResponse\x12\xd0\x01\n#GetAllRegisteredMultiplexerSessions\x12S.ni.measurementlink.sessionmanagement.v1.GetAllRegisteredMultiplexerSessionsRequest\x1aT.ni.measurementlink.sessionmanagement.v1.GetAllRegisteredMultiplexerSessionsResponse\x12\x88\x01\n\x0bGetSessions\x12;.ni.measurementlink.sessionmanagement.v1.GetSessionsRequest\x1a<.ni.measurementlink.sessionmanagement.v1.GetSessionsResponseB\xf5\x01\n+com.ni.measurementlink.sessionmanagement.v1B\x16SessionManagementProtoP\x01Z\x13sessionmanagementv1\xa2\x02\x04NIMS\xaa\x028NationalInstruments.MeasurementLink.SessionManagement.V1\xca\x02\'NI\\MeasurementLink\\SessionManagement\\V1\xea\x02*NI::MeasurementLink::SessionManagement::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/session_management_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurementlink.sessionmanagement.v1.proto/src/ni/measurementlink/sessionmanagement/v1/session_management_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class SessionManagementServiceStub(object)`

Service to keep track of open sessions used by measurement services, and to allow measurement services to access sessions by I/O resource and site.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class SessionManagementServiceServicer(object)`

Service to keep track of open sessions used by measurement services, and to allow measurement services to access sessions by I/O resource and site.
    

#### `def ReserveSessions(self, request, context)`

Reserve session(s) for the given I/O resources (pins, relays, channels), sites, and instrument type ID and returns the information needed to create or access the session.
        Also reserves the session so other processes cannot access it with a ReserveSessions() call.

        Status codes for errors:

        - INVALID_ARGUMENT:

        - Pin Map Context references a site number that is not defined in the pin map
        - Pin or relay name does not match any pin, pin group, relay, or relay group names in the pin map
        - Timeout specified is less than -1.

        - NOT_FOUND:

        - Pin Map Context has a pin map ID that does not match any pin maps registered with the Pin Map Service.

        - UNAVAILABLE:

        - Session(s) were already reserved and didn't become available before the specified timeout expired.
        

#### `def UnreserveSessions(self, request, context)`

Unreserves sessions so they can be accessed by other clients.

        - RESOURCE_EXHAUSTED:

        - Error occurred while unreserving sessions.
        

#### `def RegisterSessions(self, request, context)`

Registers the sessions with this service. Indicates that the sessions are open and will need to be closed later.
        Status codes for errors:

        - ALREADY_EXISTS:

        - Session by the same name is already registered.

        - INVALID_ARGUMENT:

        - Session names list has an empty string.
        

#### `def UnregisterSessions(self, request, context)`

Unregisters the sessions with this service. Indicates that the sessions have been closed and will need to be reopened before they can be used again.
        

#### `def ReserveAllRegisteredSessions(self, request, context)`

Reserves and gets all sessions currently registered with this service.

        - INVALID_ARGUMENT:

        - Timeout specified is less than -1.

        - UNAVAILABLE:

        - Session(s) were already reserved and didn't become available before the specified timeout expired.
        

#### `def RegisterMultiplexerSessions(self, request, context)`

Registers the multiplexer sessions with this service. Indicates that the sessions are open and will need to be closed later.

        Status codes for errors:

        - ALREADY_EXISTS:

        - Session by the same name is already registered.

        - INVALID_ARGUMENT:

        - Session names list has an empty string.
        

#### `def UnregisterMultiplexerSessions(self, request, context)`

Unregisters the multiplexer sessions with this service. Indicates that the sessions have been closed and will need to be reopened before they can be used again.
        

#### `def GetMultiplexerSessions(self, request, context)`

Gets all the connected multiplexer session(s) for the given pin map context and returns information needed to create or access the session.

        Status codes for errors:

        - INVALID_ARGUMENT:

        - Pin Map Context references a site number that is not defined in the pin map.

        - NOT_FOUND:

        - Pin Map Context has a pin map ID that does not match any pin maps registered with the Pin Map Service.
        

#### `def GetAllRegisteredMultiplexerSessions(self, request, context)`

Gets all multiplexer sessions currently registered with this service.
        

#### `def GetSessions(self, request, context)`

Gets all reserved or registered sessions for the specified instrument and multiplexer types.
        

### `def add_SessionManagementServiceServicer_to_server(servicer, server)`

### `class SessionManagementService(object)`

Service to keep track of open sessions used by measurement services, and to allow measurement services to access sessions by I/O resource and site.
    

#### `def ReserveSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnreserveSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReserveAllRegisteredSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterMultiplexerSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterMultiplexerSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetMultiplexerSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAllRegisteredMultiplexerSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Data Store Service.

- `__all__ = ['DataStoreClient']`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/_client.py

### MODULE DOCSTRING

Client for accessing the NI Data Store Service.

### `class DataStoreClient(GrpcServiceClientBase[data_store_service_pb2_grpc.DataStoreServiceStub])`

Client for accessing the NI Data Store Service.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the Data Store Client.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional data store gRPC channel.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def create_test_result(self, request: data_store_service_pb2.CreateTestResultRequest) -> data_store_service_pb2.CreateTestResultResponse`

Create a test result object for publishing measurements.

#### `def get_test_result(self, request: data_store_service_pb2.GetTestResultRequest) -> data_store_service_pb2.GetTestResultResponse`

Get the test result associated with the identifier given in the request.

#### `def query_test_results(self, request: data_store_service_pb2.QueryTestResultsRequest) -> data_store_service_pb2.QueryTestResultsResponse`

Query for test results matching the given OData query.

#### `def create_step(self, request: data_store_service_pb2.CreateStepRequest) -> data_store_service_pb2.CreateStepResponse`

Create a new step in the data store.

#### `def get_step(self, request: data_store_service_pb2.GetStepRequest) -> data_store_service_pb2.GetStepResponse`

Get the step associated with the identifier given in the request.

#### `def query_steps(self, request: data_store_service_pb2.QueryStepsRequest) -> data_store_service_pb2.QueryStepsResponse`

Query for steps matching the given OData query.

#### `def publish_condition(self, request: data_store_service_pb2.PublishConditionRequest) -> data_store_service_pb2.PublishConditionResponse`

Publish a single condition value for a step.

#### `def publish_condition_batch(self, request: data_store_service_pb2.PublishConditionBatchRequest) -> data_store_service_pb2.PublishConditionBatchResponse`

Publish multiple condition values at once for parametric sweeps.

#### `def publish_measurement(self, request: data_store_service_pb2.PublishMeasurementRequest) -> data_store_service_pb2.PublishMeasurementResponse`

Publish a single measurement value associated with a step.

#### `def publish_measurement_batch(self, request: data_store_service_pb2.PublishMeasurementBatchRequest) -> data_store_service_pb2.PublishMeasurementBatchResponse`

Publish multiple measurement values at once for parametric sweeps.

#### `def get_measurement(self, request: data_store_service_pb2.GetMeasurementRequest) -> data_store_service_pb2.GetMeasurementResponse`

Get the measurement associated with the identifier given in the request.

#### `def get_condition(self, request: data_store_service_pb2.GetConditionRequest) -> data_store_service_pb2.GetConditionResponse`

Get the condition associated with the identifier given in the request.

#### `def query_conditions(self, request: data_store_service_pb2.QueryConditionsRequest) -> data_store_service_pb2.QueryConditionsResponse`

Query conditions using OData query syntax.

#### `def query_measurements(self, request: data_store_service_pb2.QueryMeasurementsRequest) -> data_store_service_pb2.QueryMeasurementsResponse`

Query measurements using OData query syntax.

#### `def read_condition_value(self, request: data_store_service_pb2.ReadConditionValueRequest) -> data_store_service_pb2.ReadConditionValueResponse`

Read the value of a condition.

#### `def read_measurement_value(self, request: data_store_service_pb2.ReadMeasurementValueRequest) -> data_store_service_pb2.ReadMeasurementValueResponse`

Read the value of a measurement.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/_client_base.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/src/ni/measurements/data/v1/client/_client_base.py

### `class StubProtocol(Protocol)`

Protocol for gRPC stub classes.

#### `def __init__(self, channel: grpc.Channel) -> None`

Initialize the gRPC client.

### `class GrpcServiceClientBase(Generic[TStub])`

Base class for NI gRPC service clients.

#### `def __init__(self, service_interface_name: str, service_class: str, stub_class: type[TStub], *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the gRPC client.

        Args:
            service_interface_name: The fully qualified name of the service interface.
            service_class: The name of the service class.
            stub_class: The gRPC stub class for the service.
            discovery_client: An optional discovery client (recommended).
            grpc_channel: An optional pin map gRPC channel.
            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the GrpcServiceClientBase.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the GrpcServiceClientBase.

#### `def close(self) -> None`

Close the client and clean up resources that it owns.

#### `def _get_stub(self) -> TStub`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.client/tests/unit/test_data_store_client.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.client/tests/unit/test_data_store_client.py

### `def test__create_test_result__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__get_test_result__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__query_test_results__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__create_step__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__get_step__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__query_steps__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__publish_condition__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__publish_condition_batch__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__publish_measurement__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__publish_measurement_batch__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__query_conditions__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__query_measurements__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__get_condition__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__get_measurement__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__read_condition_value__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def test__read_measurement_value__request_and_response_pass_through(data_store_client: DataStoreClient, data_store_stub: Mock) -> None`

### `def data_store_client(mocker: MockerFixture, data_store_stub: Mock) -> DataStoreClient`

Create a Client with a mock DataStoreServiceStub.

### `def data_store_stub(mocker: MockerFixture) -> Mock`

Create a mock DataStoreServiceStub.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(ni/measurements/data/v1/data_store.proto\x12\x17ni.measurements.data.v1\x1a+ni/protobuf/types/precision_timestamp.proto\x1a%ni/datamonikers/v1/data_moniker.proto\x1a0ni/measurements/metadata/v1/metadata_store.proto"\x9d\x01\n\x12PublishedCondition\x12,\n\x07moniker\x18\x01 \x01(\x0b2\x1b.ni.datamonikers.v1.Moniker\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0econdition_type\x18\x04 \x01(\t\x12\x0f\n\x07step_id\x18\x05 \x01(\t\x12\x16\n\x0etest_result_id\x18\x06 \x01(\t"\xd6\x04\n\x14PublishedMeasurement\x12,\n\x07moniker\x18\x01 \x01(\x0b2\x1b.ni.datamonikers.v1.Moniker\x12I\n\x14published_conditions\x18\x02 \x03(\x0b2+.ni.measurements.data.v1.PublishedCondition\x12\n\n\x02id\x18\x03 \x01(\t\x12\x16\n\x0etest_result_id\x18\x04 \x01(\t\x12\x0f\n\x07step_id\x18\x05 \x01(\t\x12\x19\n\x11software_item_ids\x18\x06 \x03(\t\x12\x19\n\x11hardware_item_ids\x18\x07 \x03(\t\x12\x18\n\x10test_adapter_ids\x18\x08 \x03(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x12\n\nvalue_type\x18\n \x01(\t\x12\r\n\x05notes\x18\x0b \x01(\t\x12>\n\x0fstart_date_time\x18\x0c \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12<\n\rend_date_time\x18\r \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x121\n\x07outcome\x18\x0e \x01(\x0e2 .ni.measurements.data.v1.Outcome\x12\x18\n\x10parametric_index\x18\x0f \x01(\x05\x12D\n\x11error_information\x18\x10 \x01(\x0b2).ni.measurements.data.v1.ErrorInformation"\x98\x05\n\nTestResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0fuut_instance_id\x18\x02 \x01(\t\x12\x13\n\x0boperator_id\x18\x03 \x01(\t\x12\x17\n\x0ftest_station_id\x18\x04 \x01(\t\x12\x1b\n\x13test_description_id\x18\x05 \x01(\t\x12\x19\n\x11software_item_ids\x18\x06 \x03(\t\x12\x19\n\x11hardware_item_ids\x18\x07 \x03(\t\x12\x18\n\x10test_adapter_ids\x18\x08 \x03(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12>\n\x0fstart_date_time\x18\n \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12<\n\rend_date_time\x18\x0b \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x121\n\x07outcome\x18\x0c \x01(\x0e2 .ni.measurements.data.v1.Outcome\x12D\n\x11error_information\x18\r \x01(\x0b2).ni.measurements.data.v1.ErrorInformation\x12\x0c\n\x04link\x18\x0e \x01(\t\x12E\n\textension\x18\x0f \x03(\x0b22.ni.measurements.data.v1.TestResult.ExtensionEntry\x12\x11\n\tschema_id\x18\x10 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xbb\x04\n\x04Step\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0eparent_step_id\x18\x02 \x01(\t\x12\x16\n\x0etest_result_id\x18\x03 \x01(\t\x12\x0f\n\x07test_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\tstep_type\x18\x06 \x01(\t\x12\r\n\x05notes\x18\x07 \x01(\t\x12>\n\x0fstart_date_time\x18\x08 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12<\n\rend_date_time\x18\t \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x121\n\x07outcome\x18\n \x01(\x0e2 .ni.measurements.data.v1.Outcome\x12D\n\x11error_information\x18\x0b \x01(\x0b2).ni.measurements.data.v1.ErrorInformation\x12\x0c\n\x04link\x18\x0c \x01(\t\x12?\n\textension\x18\r \x03(\x0b2,.ni.measurements.data.v1.Step.ExtensionEntry\x12\x11\n\tschema_id\x18\x0e \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"G\n\x10ErrorInformation\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t*e\n\x07Outcome\x12\x17\n\x13OUTCOME_UNSPECIFIED\x10\x00\x12\x12\n\x0eOUTCOME_PASSED\x10\x01\x12\x12\n\x0eOUTCOME_FAILED\x10\x02\x12\x19\n\x15OUTCOME_INDETERMINATE\x10\x03B\xa0\x01\n\x1bcom.ni.measurements.data.v1B\x0eDataStoreProtoP\x01Z\x06datav1\xa2\x02\x04NIMD\xaa\x02(NationalInstruments.Measurements.Data.V1\xca\x02\x17NI\\Measurements\\Data\\V1\xea\x02\x1aNI::Measurements::Data::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0ni/measurements/data/v1/data_store_service.proto\x12\x17ni.measurements.data.v1\x1a+ni/protobuf/types/precision_timestamp.proto\x1a(ni/measurements/data/v1/data_store.proto\x1a\x1eni/protobuf/types/scalar.proto\x1a\x1eni/protobuf/types/vector.proto\x1a\'ni/protobuf/types/vector_wrappers.proto\x1a ni/protobuf/types/waveform.proto\x1a)ni/protobuf/types/waveform_wrappers.proto\x1a\x1eni/protobuf/types/xydata.proto\x1a\'ni/protobuf/types/xydata_wrappers.proto"S\n\x17CreateTestResultRequest\x128\n\x0btest_result\x18\x01 \x01(\x0b2#.ni.measurements.data.v1.TestResult"2\n\x18CreateTestResultResponse\x12\x16\n\x0etest_result_id\x18\x01 \x01(\t".\n\x14GetTestResultRequest\x12\x16\n\x0etest_result_id\x18\x01 \x01(\t"Q\n\x15GetTestResultResponse\x128\n\x0btest_result\x18\x01 \x01(\x0b2#.ni.measurements.data.v1.TestResult".\n\x17QueryTestResultsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"U\n\x18QueryTestResultsResponse\x129\n\x0ctest_results\x18\x01 \x03(\x0b2#.ni.measurements.data.v1.TestResult"@\n\x11CreateStepRequest\x12+\n\x04step\x18\x01 \x01(\x0b2\x1d.ni.measurements.data.v1.Step"%\n\x12CreateStepResponse\x12\x0f\n\x07step_id\x18\x01 \x01(\t"!\n\x0eGetStepRequest\x12\x0f\n\x07step_id\x18\x01 \x01(\t">\n\x0fGetStepResponse\x12+\n\x04step\x18\x01 \x01(\x0b2\x1d.ni.measurements.data.v1.Step"(\n\x11QueryStepsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"B\n\x12QueryStepsResponse\x12,\n\x05steps\x18\x01 \x03(\x0b2\x1d.ni.measurements.data.v1.Step"\x86\x01\n\x17PublishConditionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0econdition_type\x18\x02 \x01(\t\x12+\n\x06scalar\x18\x03 \x01(\x0b2\x19.ni.protobuf.types.ScalarH\x00\x12\x0f\n\x07step_id\x18\x04 \x01(\tB\x07\n\x05value"0\n\x18PublishConditionResponse\x12\x14\n\x0ccondition_id\x18\x01 \x01(\t"\x93\x01\n\x1cPublishConditionBatchRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0econdition_type\x18\x02 \x01(\t\x122\n\rscalar_values\x18\x03 \x01(\x0b2\x19.ni.protobuf.types.VectorH\x00\x12\x0f\n\x07step_id\x18\x04 \x01(\tB\x08\n\x06values"5\n\x1dPublishConditionBatchResponse\x12\x14\n\x0ccondition_id\x18\x01 \x01(\t"\x86\x07\n\x19PublishMeasurementRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06scalar\x18\x02 \x01(\x0b2\x19.ni.protobuf.types.ScalarH\x00\x12+\n\x06vector\x18\x03 \x01(\x0b2\x19.ni.protobuf.types.VectorH\x00\x12I\n\x16double_analog_waveform\x18\x04 \x01(\x0b2\'.ni.protobuf.types.DoubleAnalogWaveformH\x00\x123\n\x08x_y_data\x18\x05 \x01(\x0b2\x1f.ni.protobuf.types.DoubleXYDataH\x00\x12C\n\x13i16_analog_waveform\x18\x06 \x01(\x0b2$.ni.protobuf.types.I16AnalogWaveformH\x00\x12K\n\x17double_complex_waveform\x18\x07 \x01(\x0b2(.ni.protobuf.types.DoubleComplexWaveformH\x00\x12E\n\x14i16_complex_waveform\x18\x08 \x01(\x0b2%.ni.protobuf.types.I16ComplexWaveformH\x00\x12<\n\x0fdouble_spectrum\x18\t \x01(\x0b2!.ni.protobuf.types.DoubleSpectrumH\x00\x12>\n\x10digital_waveform\x18\n \x01(\x0b2".ni.protobuf.types.DigitalWaveformH\x00\x12\r\n\x05notes\x18\x0b \x01(\t\x128\n\ttimestamp\x18\x0c \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x121\n\x07outcome\x18\r \x01(\x0e2 .ni.measurements.data.v1.Outcome\x12D\n\x11error_information\x18\x0e \x01(\x0b2).ni.measurements.data.v1.ErrorInformation\x12\x0f\n\x07step_id\x18\x0f \x01(\t\x12\x19\n\x11hardware_item_ids\x18\x10 \x03(\t\x12\x18\n\x10test_adapter_ids\x18\x11 \x03(\t\x12\x19\n\x11software_item_ids\x18\x12 \x03(\tB\x07\n\x05value"4\n\x1aPublishMeasurementResponse\x12\x16\n\x0emeasurement_id\x18\x01 \x01(\t"\x9d\x08\n\x1ePublishMeasurementBatchRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x122\n\rscalar_values\x18\x02 \x01(\x0b2\x19.ni.protobuf.types.VectorH\x00\x12<\n\rvector_values\x18\x0b \x01(\x0b2#.ni.protobuf.types.VectorArrayValueH\x00\x12Z\n\x1ddouble_analog_waveform_values\x18\x0c \x01(\x0b21.ni.protobuf.types.DoubleAnalogWaveformArrayValueH\x00\x12D\n\x0fx_y_data_values\x18\r \x01(\x0b2).ni.protobuf.types.DoubleXYDataArrayValueH\x00\x12T\n\x1ai16_analog_waveform_values\x18\x0e \x01(\x0b2..ni.protobuf.types.I16AnalogWaveformArrayValueH\x00\x12\\\n\x1edouble_complex_waveform_values\x18\x0f \x01(\x0b22.ni.protobuf.types.DoubleComplexWaveformArrayValueH\x00\x12V\n\x1bi16_complex_waveform_values\x18\x10 \x01(\x0b2/.ni.protobuf.types.I16ComplexWaveformArrayValueH\x00\x12M\n\x16double_spectrum_values\x18\x11 \x01(\x0b2+.ni.protobuf.types.DoubleSpectrumArrayValueH\x00\x12O\n\x17digital_waveform_values\x18\x12 \x01(\x0b2,.ni.protobuf.types.DigitalWaveformArrayValueH\x00\x12\r\n\x05notes\x18\x03 \x01(\t\x129\n\ntimestamps\x18\x04 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x122\n\x08outcomes\x18\x05 \x03(\x0e2 .ni.measurements.data.v1.Outcome\x12D\n\x11error_information\x18\x06 \x03(\x0b2).ni.measurements.data.v1.ErrorInformation\x12\x0f\n\x07step_id\x18\x07 \x01(\t\x12\x19\n\x11hardware_item_ids\x18\x08 \x03(\t\x12\x18\n\x10test_adapter_ids\x18\t \x03(\t\x12\x19\n\x11software_item_ids\x18\n \x03(\tB\x08\n\x06values":\n\x1fPublishMeasurementBatchResponse\x12\x17\n\x0fmeasurement_ids\x18\x01 \x03(\t"/\n\x15GetMeasurementRequest\x12\x16\n\x0emeasurement_id\x18\x01 \x01(\t"f\n\x16GetMeasurementResponse\x12L\n\x15published_measurement\x18\x01 \x01(\x0b2-.ni.measurements.data.v1.PublishedMeasurement"+\n\x13GetConditionRequest\x12\x14\n\x0ccondition_id\x18\x01 \x01(\t"`\n\x14GetConditionResponse\x12H\n\x13published_condition\x18\x01 \x01(\x0b2+.ni.measurements.data.v1.PublishedCondition"-\n\x16QueryConditionsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"d\n\x17QueryConditionsResponse\x12I\n\x14published_conditions\x18\x01 \x03(\x0b2+.ni.measurements.data.v1.PublishedCondition"/\n\x18QueryMeasurementsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"j\n\x19QueryMeasurementsResponse\x12M\n\x16published_measurements\x18\x01 \x03(\x0b2-.ni.measurements.data.v1.PublishedMeasurement"1\n\x19ReadConditionValueRequest\x12\x14\n\x0ccondition_id\x18\x01 \x01(\t"R\n\x1aReadConditionValueResponse\x12+\n\x06vector\x18\x01 \x01(\x0b2\x19.ni.protobuf.types.VectorH\x00B\x07\n\x05value"5\n\x1bReadMeasurementValueRequest\x12\x16\n\x0emeasurement_id\x18\x01 \x01(\t"\xab\x04\n\x1cReadMeasurementValueResponse\x12+\n\x06vector\x18\x01 \x01(\x0b2\x19.ni.protobuf.types.VectorH\x00\x12I\n\x16double_analog_waveform\x18\x02 \x01(\x0b2\'.ni.protobuf.types.DoubleAnalogWaveformH\x00\x123\n\x08x_y_data\x18\x03 \x01(\x0b2\x1f.ni.protobuf.types.DoubleXYDataH\x00\x12C\n\x13i16_analog_waveform\x18\x04 \x01(\x0b2$.ni.protobuf.types.I16AnalogWaveformH\x00\x12K\n\x17double_complex_waveform\x18\x05 \x01(\x0b2(.ni.protobuf.types.DoubleComplexWaveformH\x00\x12E\n\x14i16_complex_waveform\x18\x06 \x01(\x0b2%.ni.protobuf.types.I16ComplexWaveformH\x00\x12<\n\x0fdouble_spectrum\x18\x07 \x01(\x0b2!.ni.protobuf.types.DoubleSpectrumH\x00\x12>\n\x10digital_waveform\x18\x08 \x01(\x0b2".ni.protobuf.types.DigitalWaveformH\x00B\x07\n\x05value2\x87\x0f\n\x10DataStoreService\x12w\n\x10CreateTestResult\x120.ni.measurements.data.v1.CreateTestResultRequest\x1a1.ni.measurements.data.v1.CreateTestResultResponse\x12n\n\rGetTestResult\x12-.ni.measurements.data.v1.GetTestResultRequest\x1a..ni.measurements.data.v1.GetTestResultResponse\x12w\n\x10QueryTestResults\x120.ni.measurements.data.v1.QueryTestResultsRequest\x1a1.ni.measurements.data.v1.QueryTestResultsResponse\x12e\n\nCreateStep\x12*.ni.measurements.data.v1.CreateStepRequest\x1a+.ni.measurements.data.v1.CreateStepResponse\x12\\\n\x07GetStep\x12\'.ni.measurements.data.v1.GetStepRequest\x1a(.ni.measurements.data.v1.GetStepResponse\x12e\n\nQuerySteps\x12*.ni.measurements.data.v1.QueryStepsRequest\x1a+.ni.measurements.data.v1.QueryStepsResponse\x12w\n\x10PublishCondition\x120.ni.measurements.data.v1.PublishConditionRequest\x1a1.ni.measurements.data.v1.PublishConditionResponse\x12\x86\x01\n\x15PublishConditionBatch\x125.ni.measurements.data.v1.PublishConditionBatchRequest\x1a6.ni.measurements.data.v1.PublishConditionBatchResponse\x12}\n\x12PublishMeasurement\x122.ni.measurements.data.v1.PublishMeasurementRequest\x1a3.ni.measurements.data.v1.PublishMeasurementResponse\x12\x8c\x01\n\x17PublishMeasurementBatch\x127.ni.measurements.data.v1.PublishMeasurementBatchRequest\x1a8.ni.measurements.data.v1.PublishMeasurementBatchResponse\x12q\n\x0eGetMeasurement\x12..ni.measurements.data.v1.GetMeasurementRequest\x1a/.ni.measurements.data.v1.GetMeasurementResponse\x12k\n\x0cGetCondition\x12,.ni.measurements.data.v1.GetConditionRequest\x1a-.ni.measurements.data.v1.GetConditionResponse\x12t\n\x0fQueryConditions\x12/.ni.measurements.data.v1.QueryConditionsRequest\x1a0.ni.measurements.data.v1.QueryConditionsResponse\x12z\n\x11QueryMeasurements\x121.ni.measurements.data.v1.QueryMeasurementsRequest\x1a2.ni.measurements.data.v1.QueryMeasurementsResponse\x12}\n\x12ReadConditionValue\x122.ni.measurements.data.v1.ReadConditionValueRequest\x1a3.ni.measurements.data.v1.ReadConditionValueResponse\x12\x83\x01\n\x14ReadMeasurementValue\x124.ni.measurements.data.v1.ReadMeasurementValueRequest\x1a5.ni.measurements.data.v1.ReadMeasurementValueResponseB\xa7\x01\n\x1bcom.ni.measurements.data.v1B\x15DataStoreServiceProtoP\x01Z\x06datav1\xa2\x02\x04NIMD\xaa\x02(NationalInstruments.Measurements.Data.V1\xca\x02\x17NI\\Measurements\\Data\\V1\xea\x02\x1aNI::Measurements::Data::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.data.v1.proto/src/ni/measurements/data/v1/data_store_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class DataStoreServiceStub(object)`

This service provides endpoints for the publishing of measurements.
    This includes associating measurements with the conditions associated with the measurement,
    querying for the published measurements with OData queries, and reading back these published values.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class DataStoreServiceServicer(object)`

This service provides endpoints for the publishing of measurements.
    This includes associating measurements with the conditions associated with the measurement,
    querying for the published measurements with OData queries, and reading back these published values.
    

#### `def CreateTestResult(self, request, context)`

Creates a test result object for publishing measurements.  Once a test result is created,
        you can publish an arbitrary number of measurements to the test result.  The measurements
        will be associated with each of the metadata types specified in the test result.  For instance,
        if you specify an operator when creating a test result, all measurements published to the test result
        will be associated with that operator.  The response will include the test result id,
        which can be used to reference the test result in subsequent requests, and to get the test result
        metadata via the GetTestResult method.
        

#### `def GetTestResult(self, request, context)`

Gets the test result associated with the identifier given in the request.
        

#### `def QueryTestResults(self, request, context)`

Query for test results matching the given OData query.  For information about the OData query syntax,
        see https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview.
        

#### `def CreateStep(self, request, context)`

Creates a new step in the data store.  A step is owned by a test result,
        and is a logical grouping of published measurements.  All published measurements must be associated
        with a step.
        

#### `def GetStep(self, request, context)`

Gets the step associated with the identifier given in the request.
        

#### `def QuerySteps(self, request, context)`

Query for steps matching the given OData query.  For information about the OData query syntax,
        see https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview.
        

#### `def PublishCondition(self, request, context)`

Publishes a single condition value for a test step. Conditions are contextual values
        like input voltage, temperature, or humidity present during measurement.
        

#### `def PublishConditionBatch(self, request, context)`

Publishes multiple condition values at once for parametric sweeps.
        

#### `def PublishMeasurement(self, request, context)`

Publishes a single measurement value associated with a test step.
        

#### `def PublishMeasurementBatch(self, request, context)`

Publishes multiple measurements at once for parametric sweeps.
        

#### `def GetMeasurement(self, request, context)`

Gets the measurement associated with the given id.
        

#### `def GetCondition(self, request, context)`

Gets the condition associated with the given id.
        

#### `def QueryConditions(self, request, context)`

Queries conditions using OData query syntax.
        See https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview.
        

#### `def QueryMeasurements(self, request, context)`

Queries measurements using OData query syntax.
        See https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview.
        

#### `def ReadConditionValue(self, request, context)`

Reads the value corresponding to the specified condition.
        

#### `def ReadMeasurementValue(self, request, context)`

Reads the value corresponding to the specified measurement.
        

### `def add_DataStoreServiceServicer_to_server(servicer, server)`

### `class DataStoreService(object)`

This service provides endpoints for the publishing of measurements.
    This includes associating measurements with the conditions associated with the measurement,
    querying for the published measurements with OData queries, and reading back these published values.
    

#### `def CreateTestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryTestResults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateStep(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetStep(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QuerySteps(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PublishCondition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PublishConditionBatch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PublishMeasurement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PublishMeasurementBatch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetMeasurement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCondition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryConditions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryMeasurements(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadConditionValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadMeasurementValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Metadata Store Service.

- `__all__ = ['MetadataStoreClient']`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/_client.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/_client.py

### MODULE DOCSTRING

Client for accessing the NI Metadata Store Service.

### `class MetadataStoreClient(GrpcServiceClientBase[metadata_store_service_pb2_grpc.MetadataStoreServiceStub])`

Client for accessing the NI Metadata Store Service.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the Metadata Store Client.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional metadata store gRPC channel.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def get_uut_instance(self, request: metadata_store_service_pb2.GetUutInstanceRequest) -> metadata_store_service_pb2.GetUutInstanceResponse`

Gets the UUT instance associated with the identifier given in the request.

#### `def query_uut_instances(self, request: metadata_store_service_pb2.QueryUutInstancesRequest) -> metadata_store_service_pb2.QueryUutInstancesResponse`

Perform an OData query on UUT instances.

#### `def create_uut_instance(self, request: metadata_store_service_pb2.CreateUutInstanceRequest) -> metadata_store_service_pb2.CreateUutInstanceResponse`

Creates a new UUT instance in the metadata store.

#### `def get_uut(self, request: metadata_store_service_pb2.GetUutRequest) -> metadata_store_service_pb2.GetUutResponse`

Gets the UUT associated with the identifier given in the request.

#### `def query_uuts(self, request: metadata_store_service_pb2.QueryUutsRequest) -> metadata_store_service_pb2.QueryUutsResponse`

Perform an OData query on UUTs.

#### `def create_uut(self, request: metadata_store_service_pb2.CreateUutRequest) -> metadata_store_service_pb2.CreateUutResponse`

Creates a new UUT in the metadata store.

#### `def get_operator(self, request: metadata_store_service_pb2.GetOperatorRequest) -> metadata_store_service_pb2.GetOperatorResponse`

Gets the operator associated with the identifier given in the request.

#### `def query_operators(self, request: metadata_store_service_pb2.QueryOperatorsRequest) -> metadata_store_service_pb2.QueryOperatorsResponse`

Perform an OData query on operators.

#### `def create_operator(self, request: metadata_store_service_pb2.CreateOperatorRequest) -> metadata_store_service_pb2.CreateOperatorResponse`

Creates a new operator in the metadata store.

#### `def get_test_description(self, request: metadata_store_service_pb2.GetTestDescriptionRequest) -> metadata_store_service_pb2.GetTestDescriptionResponse`

Gets the test description associated with the identifier given in the request.

#### `def query_test_descriptions(self, request: metadata_store_service_pb2.QueryTestDescriptionsRequest) -> metadata_store_service_pb2.QueryTestDescriptionsResponse`

Perform an OData query on test descriptions.

#### `def create_test_description(self, request: metadata_store_service_pb2.CreateTestDescriptionRequest) -> metadata_store_service_pb2.CreateTestDescriptionResponse`

Creates a new test description in the metadata store.

#### `def get_test(self, request: metadata_store_service_pb2.GetTestRequest) -> metadata_store_service_pb2.GetTestResponse`

Gets the test associated with the identifier given in the request.

#### `def query_tests(self, request: metadata_store_service_pb2.QueryTestsRequest) -> metadata_store_service_pb2.QueryTestsResponse`

Perform an OData query on tests.

#### `def create_test(self, request: metadata_store_service_pb2.CreateTestRequest) -> metadata_store_service_pb2.CreateTestResponse`

Creates a new test in the metadata store.

#### `def get_test_station(self, request: metadata_store_service_pb2.GetTestStationRequest) -> metadata_store_service_pb2.GetTestStationResponse`

Gets the test station associated with the identifier given in the request.

#### `def query_test_stations(self, request: metadata_store_service_pb2.QueryTestStationsRequest) -> metadata_store_service_pb2.QueryTestStationsResponse`

Perform an OData query on test stations.

#### `def create_test_station(self, request: metadata_store_service_pb2.CreateTestStationRequest) -> metadata_store_service_pb2.CreateTestStationResponse`

Creates a new test station in the metadata store.

#### `def get_hardware_item(self, request: metadata_store_service_pb2.GetHardwareItemRequest) -> metadata_store_service_pb2.GetHardwareItemResponse`

Gets the hardware item associated with the identifier given in the request.

#### `def query_hardware_items(self, request: metadata_store_service_pb2.QueryHardwareItemsRequest) -> metadata_store_service_pb2.QueryHardwareItemsResponse`

Perform an OData query on hardware items.

#### `def create_hardware_item(self, request: metadata_store_service_pb2.CreateHardwareItemRequest) -> metadata_store_service_pb2.CreateHardwareItemResponse`

Creates a new hardware item in the metadata store.

#### `def get_software_item(self, request: metadata_store_service_pb2.GetSoftwareItemRequest) -> metadata_store_service_pb2.GetSoftwareItemResponse`

Gets the software item associated with the identifier given in the request.

#### `def query_software_items(self, request: metadata_store_service_pb2.QuerySoftwareItemsRequest) -> metadata_store_service_pb2.QuerySoftwareItemsResponse`

Perform an OData query on software items.

#### `def create_software_item(self, request: metadata_store_service_pb2.CreateSoftwareItemRequest) -> metadata_store_service_pb2.CreateSoftwareItemResponse`

Creates a new software item in the metadata store.

#### `def get_test_adapter(self, request: metadata_store_service_pb2.GetTestAdapterRequest) -> metadata_store_service_pb2.GetTestAdapterResponse`

Gets the test adapter associated with the identifier given in the request.

#### `def query_test_adapters(self, request: metadata_store_service_pb2.QueryTestAdaptersRequest) -> metadata_store_service_pb2.QueryTestAdaptersResponse`

Perform an OData query on test adapters.

#### `def create_test_adapter(self, request: metadata_store_service_pb2.CreateTestAdapterRequest) -> metadata_store_service_pb2.CreateTestAdapterResponse`

Creates a new test adapter in the metadata store.

#### `def register_schema(self, request: metadata_store_service_pb2.RegisterSchemaRequest) -> metadata_store_service_pb2.RegisterSchemaResponse`

Registers a schema.

#### `def list_schemas(self, request: metadata_store_service_pb2.ListSchemasRequest) -> metadata_store_service_pb2.ListSchemasResponse`

List the schemas that have been previously registered.

#### `def get_alias(self, request: metadata_store_service_pb2.GetAliasRequest) -> metadata_store_service_pb2.GetAliasResponse`

Gets the target of a given alias.

#### `def query_aliases(self, request: metadata_store_service_pb2.QueryAliasesRequest) -> metadata_store_service_pb2.QueryAliasesResponse`

Perform an OData query on the created aliases.

#### `def create_alias(self, request: metadata_store_service_pb2.CreateAliasRequest) -> metadata_store_service_pb2.CreateAliasResponse`

Creates an alias of the specified metadata.

        This alias can be used when creating other metadata or publishing.
        

#### `def delete_alias(self, request: metadata_store_service_pb2.DeleteAliasRequest) -> metadata_store_service_pb2.DeleteAliasResponse`

Deletes a created alias.

#### `def create_from_json_document(self, request: metadata_store_service_pb2.CreateFromJsonDocumentRequest) -> metadata_store_service_pb2.CreateFromJsonDocumentResponse`

Creates metadata from a JSON document.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/_client_base.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/src/ni/measurements/metadata/v1/client/_client_base.py

### `class StubProtocol(Protocol)`

Protocol for gRPC stub classes.

#### `def __init__(self, channel: grpc.Channel) -> None`

Initialize the gRPC client.

### `class GrpcServiceClientBase(Generic[TStub])`

Base class for NI gRPC service clients.

#### `def __init__(self, service_interface_name: str, service_class: str, stub_class: type[TStub], *, discovery_client: DiscoveryClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the gRPC client.

        Args:
            service_interface_name: The fully qualified name of the service interface.
            service_class: The name of the service class.
            stub_class: The gRPC stub class for the service.
            discovery_client: An optional discovery client (recommended).
            grpc_channel: An optional pin map gRPC channel.
            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the GrpcServiceClientBase.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the GrpcServiceClientBase.

#### `def close(self) -> None`

Close the client and clean up resources that it owns.

#### `def _get_stub(self) -> TStub`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.client/tests/unit/test_metadata_store_client.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.client/tests/unit/test_metadata_store_client.py

### `def test__get_uut_instance__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_uut_instances__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_uut_instance__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_uut__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_uuts__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_uut__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_operator__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_operators__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_operator__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_test_description__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_test_descriptions__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_test_description__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_test__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_tests__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_test__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_test_station__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_test_stations__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_test_station__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_hardware_item__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_hardware_items__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_hardware_item__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_software_item__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_software_items__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_software_item__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_test_adapter__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_test_adapters__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_test_adapter__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__register_schema__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__list_schemas__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__get_alias__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__query_aliases__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__create_alias__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def test__delete_alias__request_and_response_pass_through(metadata_store_client: MetadataStoreClient, metadata_store_stub: Mock) -> None`

### `def metadata_store_client(mocker: MockerFixture, metadata_store_stub: Mock) -> MetadataStoreClient`

Create a Client with a mock MetadataStoreServiceStub.

### `def metadata_store_stub(mocker: MockerFixture) -> Mock`

Create a mock MetadataStoreServiceStub.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0ni/measurements/metadata/v1/metadata_store.proto\x12\x1bni.measurements.metadata.v1"\xda\x02\n\x0bUutInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06uut_id\x18\x02 \x01(\t\x12\x15\n\rserial_number\x18\x03 \x01(\t\x12\x18\n\x10manufacture_date\x18\x04 \x01(\t\x12\x18\n\x10firmware_version\x18\x05 \x01(\t\x12\x18\n\x10hardware_version\x18\x06 \x01(\t\x12\x0c\n\x04link\x18\x07 \x01(\t\x12J\n\textension\x18\x08 \x03(\x0b27.ni.measurements.metadata.v1.UutInstance.ExtensionEntry\x12\x11\n\tschema_id\x18\t \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xa5\x02\n\x03Uut\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x0e\n\x06family\x18\x03 \x01(\t\x12\x15\n\rmanufacturers\x18\x04 \x03(\t\x12\x13\n\x0bpart_number\x18\x05 \x01(\t\x12\x0c\n\x04link\x18\x06 \x01(\t\x12B\n\textension\x18\x07 \x03(\x0b2/.ni.measurements.metadata.v1.Uut.ExtensionEntry\x12\x11\n\tschema_id\x18\x08 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xf0\x02\n\x0cHardwareItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\x12\x13\n\x0bpart_number\x18\x05 \x01(\t\x12\x18\n\x10asset_identifier\x18\x06 \x01(\t\x12\x1c\n\x14calibration_due_date\x18\x07 \x01(\t\x12\x0c\n\x04link\x18\x08 \x01(\t\x12K\n\textension\x18\t \x03(\x0b28.ni.measurements.metadata.v1.HardwareItem.ExtensionEntry\x12\x11\n\tschema_id\x18\n \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xfc\x02\n\x0bTestAdapter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x15\n\rserial_number\x18\x05 \x01(\t\x12\x13\n\x0bpart_number\x18\x06 \x01(\t\x12\x18\n\x10asset_identifier\x18\x07 \x01(\t\x12\x1c\n\x14calibration_due_date\x18\x08 \x01(\t\x12\x0c\n\x04link\x18\t \x01(\t\x12J\n\textension\x18\n \x03(\x0b27.ni.measurements.metadata.v1.TestAdapter.ExtensionEntry\x12\x11\n\tschema_id\x18\x0b \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\x89\x02\n\x0cSoftwareItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12K\n\textension\x18\x05 \x03(\x0b28.ni.measurements.metadata.v1.SoftwareItem.ExtensionEntry\x12\x11\n\tschema_id\x18\x06 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xfb\x01\n\x08Operator\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12G\n\textension\x18\x05 \x03(\x0b24.ni.measurements.metadata.v1.Operator.ExtensionEntry\x12\x11\n\tschema_id\x18\x06 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\x8b\x02\n\x0fTestDescription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06uut_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12N\n\textension\x18\x05 \x03(\x0b2;.ni.measurements.metadata.v1.TestDescription.ExtensionEntry\x12\x11\n\tschema_id\x18\x06 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\xfa\x01\n\x04Test\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12C\n\textension\x18\x05 \x03(\x0b20.ni.measurements.metadata.v1.Test.ExtensionEntry\x12\x11\n\tschema_id\x18\x06 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"\x8d\x02\n\x0bTestStation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10asset_identifier\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\x12J\n\textension\x18\x05 \x03(\x0b27.ni.measurements.metadata.v1.TestStation.ExtensionEntry\x12\x11\n\tschema_id\x18\x06 \x01(\t\x1a]\n\x0eExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.ni.measurements.metadata.v1.ExtensionValue:\x028\x01"4\n\x0eExtensionValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00B\n\n\x08metadata"-\n\x0fExtensionSchema\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t"k\n\x05Alias\x12\x0c\n\x04name\x18\x01 \x01(\t\x12A\n\x0btarget_type\x18\x02 \x01(\x0e2,.ni.measurements.metadata.v1.AliasTargetType\x12\x11\n\ttarget_id\x18\x03 \x01(\t*\xe9\x02\n\x0fAliasTargetType\x12!\n\x1dALIAS_TARGET_TYPE_UNSPECIFIED\x10\x00\x12"\n\x1eALIAS_TARGET_TYPE_UUT_INSTANCE\x10\x01\x12\x19\n\x15ALIAS_TARGET_TYPE_UUT\x10\x02\x12#\n\x1fALIAS_TARGET_TYPE_HARDWARE_ITEM\x10\x03\x12#\n\x1fALIAS_TARGET_TYPE_SOFTWARE_ITEM\x10\x04\x12\x1e\n\x1aALIAS_TARGET_TYPE_OPERATOR\x10\x05\x12&\n"ALIAS_TARGET_TYPE_TEST_DESCRIPTION\x10\x06\x12\x1a\n\x16ALIAS_TARGET_TYPE_TEST\x10\x07\x12"\n\x1eALIAS_TARGET_TYPE_TEST_STATION\x10\x08\x12"\n\x1eALIAS_TARGET_TYPE_TEST_ADAPTER\x10\tB\xb8\x01\n\x1fcom.ni.measurements.metadata.v1B\x12MetadataStoreProtoP\x01Z\nmetadatav1\xa2\x02\x04NIMM\xaa\x02,NationalInstruments.Measurements.Metadata.V1\xca\x02\x1bNI\\Measurements\\Metadata\\V1\xea\x02\x1eNI::Measurements::Metadata::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_service_pb2/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_service_pb2/__init__.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8ni/measurements/metadata/v1/metadata_store_service.proto\x12\x1bni.measurements.metadata.v1\x1a0ni/measurements/metadata/v1/metadata_store.proto"0\n\x15GetUutInstanceRequest\x12\x17\n\x0fuut_instance_id\x18\x01 \x01(\t"X\n\x16GetUutInstanceResponse\x12>\n\x0cuut_instance\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.UutInstance"/\n\x18QueryUutInstancesRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"\\\n\x19QueryUutInstancesResponse\x12?\n\ruut_instances\x18\x01 \x03(\x0b2(.ni.measurements.metadata.v1.UutInstance"Z\n\x18CreateUutInstanceRequest\x12>\n\x0cuut_instance\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.UutInstance"4\n\x19CreateUutInstanceResponse\x12\x17\n\x0fuut_instance_id\x18\x01 \x01(\t"\x1f\n\rGetUutRequest\x12\x0e\n\x06uut_id\x18\x01 \x01(\t"?\n\x0eGetUutResponse\x12-\n\x03uut\x18\x01 \x01(\x0b2 .ni.measurements.metadata.v1.Uut"\'\n\x10QueryUutsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"C\n\x11QueryUutsResponse\x12.\n\x04uuts\x18\x01 \x03(\x0b2 .ni.measurements.metadata.v1.Uut"A\n\x10CreateUutRequest\x12-\n\x03uut\x18\x01 \x01(\x0b2 .ni.measurements.metadata.v1.Uut"#\n\x11CreateUutResponse\x12\x0e\n\x06uut_id\x18\x01 \x01(\t")\n\x12GetOperatorRequest\x12\x13\n\x0boperator_id\x18\x01 \x01(\t"N\n\x13GetOperatorResponse\x127\n\x08operator\x18\x01 \x01(\x0b2%.ni.measurements.metadata.v1.Operator",\n\x15QueryOperatorsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"R\n\x16QueryOperatorsResponse\x128\n\toperators\x18\x01 \x03(\x0b2%.ni.measurements.metadata.v1.Operator"P\n\x15CreateOperatorRequest\x127\n\x08operator\x18\x01 \x01(\x0b2%.ni.measurements.metadata.v1.Operator"-\n\x16CreateOperatorResponse\x12\x13\n\x0boperator_id\x18\x01 \x01(\t"8\n\x19GetTestDescriptionRequest\x12\x1b\n\x13test_description_id\x18\x01 \x01(\t"d\n\x1aGetTestDescriptionResponse\x12F\n\x10test_description\x18\x01 \x01(\x0b2,.ni.measurements.metadata.v1.TestDescription"3\n\x1cQueryTestDescriptionsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"h\n\x1dQueryTestDescriptionsResponse\x12G\n\x11test_descriptions\x18\x01 \x03(\x0b2,.ni.measurements.metadata.v1.TestDescription"f\n\x1cCreateTestDescriptionRequest\x12F\n\x10test_description\x18\x01 \x01(\x0b2,.ni.measurements.metadata.v1.TestDescription"<\n\x1dCreateTestDescriptionResponse\x12\x1b\n\x13test_description_id\x18\x01 \x01(\t"!\n\x0eGetTestRequest\x12\x0f\n\x07test_id\x18\x01 \x01(\t"B\n\x0fGetTestResponse\x12/\n\x04test\x18\x01 \x01(\x0b2!.ni.measurements.metadata.v1.Test"(\n\x11QueryTestsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"F\n\x12QueryTestsResponse\x120\n\x05tests\x18\x01 \x03(\x0b2!.ni.measurements.metadata.v1.Test"D\n\x11CreateTestRequest\x12/\n\x04test\x18\x01 \x01(\x0b2!.ni.measurements.metadata.v1.Test"%\n\x12CreateTestResponse\x12\x0f\n\x07test_id\x18\x01 \x01(\t"0\n\x15GetTestStationRequest\x12\x17\n\x0ftest_station_id\x18\x01 \x01(\t"X\n\x16GetTestStationResponse\x12>\n\x0ctest_station\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.TestStation"/\n\x18QueryTestStationsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"\\\n\x19QueryTestStationsResponse\x12?\n\rtest_stations\x18\x01 \x03(\x0b2(.ni.measurements.metadata.v1.TestStation"Z\n\x18CreateTestStationRequest\x12>\n\x0ctest_station\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.TestStation"4\n\x19CreateTestStationResponse\x12\x17\n\x0ftest_station_id\x18\x01 \x01(\t"2\n\x16GetHardwareItemRequest\x12\x18\n\x10hardware_item_id\x18\x01 \x01(\t"[\n\x17GetHardwareItemResponse\x12@\n\rhardware_item\x18\x01 \x01(\x0b2).ni.measurements.metadata.v1.HardwareItem"0\n\x19QueryHardwareItemsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"_\n\x1aQueryHardwareItemsResponse\x12A\n\x0ehardware_items\x18\x01 \x03(\x0b2).ni.measurements.metadata.v1.HardwareItem"]\n\x19CreateHardwareItemRequest\x12@\n\rhardware_item\x18\x01 \x01(\x0b2).ni.measurements.metadata.v1.HardwareItem"6\n\x1aCreateHardwareItemResponse\x12\x18\n\x10hardware_item_id\x18\x01 \x01(\t"2\n\x16GetSoftwareItemRequest\x12\x18\n\x10software_item_id\x18\x01 \x01(\t"[\n\x17GetSoftwareItemResponse\x12@\n\rsoftware_item\x18\x01 \x01(\x0b2).ni.measurements.metadata.v1.SoftwareItem"0\n\x19QuerySoftwareItemsRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"_\n\x1aQuerySoftwareItemsResponse\x12A\n\x0esoftware_items\x18\x01 \x03(\x0b2).ni.measurements.metadata.v1.SoftwareItem"]\n\x19CreateSoftwareItemRequest\x12@\n\rsoftware_item\x18\x01 \x01(\x0b2).ni.measurements.metadata.v1.SoftwareItem"6\n\x1aCreateSoftwareItemResponse\x12\x18\n\x10software_item_id\x18\x01 \x01(\t"0\n\x15GetTestAdapterRequest\x12\x17\n\x0ftest_adapter_id\x18\x01 \x01(\t"X\n\x16GetTestAdapterResponse\x12>\n\x0ctest_adapter\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.TestAdapter"/\n\x18QueryTestAdaptersRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"\\\n\x19QueryTestAdaptersResponse\x12?\n\rtest_adapters\x18\x01 \x03(\x0b2(.ni.measurements.metadata.v1.TestAdapter"Z\n\x18CreateTestAdapterRequest\x12>\n\x0ctest_adapter\x18\x01 \x01(\x0b2(.ni.measurements.metadata.v1.TestAdapter"4\n\x19CreateTestAdapterResponse\x12\x17\n\x0ftest_adapter_id\x18\x01 \x01(\t"\'\n\x15RegisterSchemaRequest\x12\x0e\n\x06schema\x18\x01 \x01(\t"+\n\x16RegisterSchemaResponse\x12\x11\n\tschema_id\x18\x01 \x01(\t"\x14\n\x12ListSchemasRequest"T\n\x13ListSchemasResponse\x12=\n\x07schemas\x18\x01 \x03(\x0b2,.ni.measurements.metadata.v1.ExtensionSchema"%\n\x0fGetAliasRequest\x12\x12\n\nalias_name\x18\x01 \x01(\t"E\n\x10GetAliasResponse\x121\n\x05alias\x18\x01 \x01(\x0b2".ni.measurements.metadata.v1.Alias"*\n\x13QueryAliasesRequest\x12\x13\n\x0bodata_query\x18\x01 \x01(\t"K\n\x14QueryAliasesResponse\x123\n\x07aliases\x18\x01 \x03(\x0b2".ni.measurements.metadata.v1.Alias"\xef\x04\n\x12CreateAliasRequest\x12\x12\n\nalias_name\x18\x01 \x01(\t\x12@\n\x0cuut_instance\x18\x02 \x01(\x0b2(.ni.measurements.metadata.v1.UutInstanceH\x00\x12/\n\x03uut\x18\x03 \x01(\x0b2 .ni.measurements.metadata.v1.UutH\x00\x12B\n\rhardware_item\x18\x04 \x01(\x0b2).ni.measurements.metadata.v1.HardwareItemH\x00\x12B\n\rsoftware_item\x18\x05 \x01(\x0b2).ni.measurements.metadata.v1.SoftwareItemH\x00\x129\n\x08operator\x18\x06 \x01(\x0b2%.ni.measurements.metadata.v1.OperatorH\x00\x12H\n\x10test_description\x18\x07 \x01(\x0b2,.ni.measurements.metadata.v1.TestDescriptionH\x00\x121\n\x04test\x18\x08 \x01(\x0b2!.ni.measurements.metadata.v1.TestH\x00\x12@\n\x0ctest_station\x18\t \x01(\x0b2(.ni.measurements.metadata.v1.TestStationH\x00\x12@\n\x0ctest_adapter\x18\n \x01(\x0b2(.ni.measurements.metadata.v1.TestAdapterH\x00B\x0e\n\x0calias_target"H\n\x13CreateAliasResponse\x121\n\x05alias\x18\x01 \x01(\x0b2".ni.measurements.metadata.v1.Alias"(\n\x12DeleteAliasRequest\x12\x12\n\nalias_name\x18\x01 \x01(\t"+\n\x13DeleteAliasResponse\x12\x14\n\x0cunregistered\x18\x01 \x01(\x08"6\n\x1dCreateFromJsonDocumentRequest\x12\x15\n\rjson_document\x18\x01 \x01(\t"\xce\x04\n\x1eCreateFromJsonDocumentResponse\x12?\n\ruut_instances\x18\x01 \x03(\x0b2(.ni.measurements.metadata.v1.UutInstance\x12.\n\x04uuts\x18\x02 \x03(\x0b2 .ni.measurements.metadata.v1.Uut\x128\n\toperators\x18\x03 \x03(\x0b2%.ni.measurements.metadata.v1.Operator\x12G\n\x11test_descriptions\x18\x04 \x03(\x0b2,.ni.measurements.metadata.v1.TestDescription\x120\n\x05tests\x18\x05 \x03(\x0b2!.ni.measurements.metadata.v1.Test\x12?\n\rtest_stations\x18\x06 \x03(\x0b2(.ni.measurements.metadata.v1.TestStation\x12A\n\x0ehardware_items\x18\x07 \x03(\x0b2).ni.measurements.metadata.v1.HardwareItem\x12A\n\x0esoftware_items\x18\x08 \x03(\x0b2).ni.measurements.metadata.v1.SoftwareItem\x12?\n\rtest_adapters\x18\t \x03(\x0b2(.ni.measurements.metadata.v1.TestAdapter2\x95!\n\x14MetadataStoreService\x12y\n\x0eGetUutInstance\x122.ni.measurements.metadata.v1.GetUutInstanceRequest\x1a3.ni.measurements.metadata.v1.GetUutInstanceResponse\x12\x82\x01\n\x11QueryUutInstances\x125.ni.measurements.metadata.v1.QueryUutInstancesRequest\x1a6.ni.measurements.metadata.v1.QueryUutInstancesResponse\x12\x82\x01\n\x11CreateUutInstance\x125.ni.measurements.metadata.v1.CreateUutInstanceRequest\x1a6.ni.measurements.metadata.v1.CreateUutInstanceResponse\x12a\n\x06GetUut\x12*.ni.measurements.metadata.v1.GetUutRequest\x1a+.ni.measurements.metadata.v1.GetUutResponse\x12j\n\tQueryUuts\x12-.ni.measurements.metadata.v1.QueryUutsRequest\x1a..ni.measurements.metadata.v1.QueryUutsResponse\x12j\n\tCreateUut\x12-.ni.measurements.metadata.v1.CreateUutRequest\x1a..ni.measurements.metadata.v1.CreateUutResponse\x12p\n\x0bGetOperator\x12/.ni.measurements.metadata.v1.GetOperatorRequest\x1a0.ni.measurements.metadata.v1.GetOperatorResponse\x12y\n\x0eQueryOperators\x122.ni.measurements.metadata.v1.QueryOperatorsRequest\x1a3.ni.measurements.metadata.v1.QueryOperatorsResponse\x12y\n\x0eCreateOperator\x122.ni.measurements.metadata.v1.CreateOperatorRequest\x1a3.ni.measurements.metadata.v1.CreateOperatorResponse\x12\x85\x01\n\x12GetTestDescription\x126.ni.measurements.metadata.v1.GetTestDescriptionRequest\x1a7.ni.measurements.metadata.v1.GetTestDescriptionResponse\x12\x8e\x01\n\x15QueryTestDescriptions\x129.ni.measurements.metadata.v1.QueryTestDescriptionsRequest\x1a:.ni.measurements.metadata.v1.QueryTestDescriptionsResponse\x12\x8e\x01\n\x15CreateTestDescription\x129.ni.measurements.metadata.v1.CreateTestDescriptionRequest\x1a:.ni.measurements.metadata.v1.CreateTestDescriptionResponse\x12d\n\x07GetTest\x12+.ni.measurements.metadata.v1.GetTestRequest\x1a,.ni.measurements.metadata.v1.GetTestResponse\x12m\n\nQueryTests\x12..ni.measurements.metadata.v1.QueryTestsRequest\x1a/.ni.measurements.metadata.v1.QueryTestsResponse\x12m\n\nCreateTest\x12..ni.measurements.metadata.v1.CreateTestRequest\x1a/.ni.measurements.metadata.v1.CreateTestResponse\x12y\n\x0eGetTestStation\x122.ni.measurements.metadata.v1.GetTestStationRequest\x1a3.ni.measurements.metadata.v1.GetTestStationResponse\x12\x82\x01\n\x11QueryTestStations\x125.ni.measurements.metadata.v1.QueryTestStationsRequest\x1a6.ni.measurements.metadata.v1.QueryTestStationsResponse\x12\x82\x01\n\x11CreateTestStation\x125.ni.measurements.metadata.v1.CreateTestStationRequest\x1a6.ni.measurements.metadata.v1.CreateTestStationResponse\x12|\n\x0fGetHardwareItem\x123.ni.measurements.metadata.v1.GetHardwareItemRequest\x1a4.ni.measurements.metadata.v1.GetHardwareItemResponse\x12\x85\x01\n\x12QueryHardwareItems\x126.ni.measurements.metadata.v1.QueryHardwareItemsRequest\x1a7.ni.measurements.metadata.v1.QueryHardwareItemsResponse\x12\x85\x01\n\x12CreateHardwareItem\x126.ni.measurements.metadata.v1.CreateHardwareItemRequest\x1a7.ni.measurements.metadata.v1.CreateHardwareItemResponse\x12|\n\x0fGetSoftwareItem\x123.ni.measurements.metadata.v1.GetSoftwareItemRequest\x1a4.ni.measurements.metadata.v1.GetSoftwareItemResponse\x12\x85\x01\n\x12QuerySoftwareItems\x126.ni.measurements.metadata.v1.QuerySoftwareItemsRequest\x1a7.ni.measurements.metadata.v1.QuerySoftwareItemsResponse\x12\x85\x01\n\x12CreateSoftwareItem\x126.ni.measurements.metadata.v1.CreateSoftwareItemRequest\x1a7.ni.measurements.metadata.v1.CreateSoftwareItemResponse\x12y\n\x0eGetTestAdapter\x122.ni.measurements.metadata.v1.GetTestAdapterRequest\x1a3.ni.measurements.metadata.v1.GetTestAdapterResponse\x12\x82\x01\n\x11QueryTestAdapters\x125.ni.measurements.metadata.v1.QueryTestAdaptersRequest\x1a6.ni.measurements.metadata.v1.QueryTestAdaptersResponse\x12\x82\x01\n\x11CreateTestAdapter\x125.ni.measurements.metadata.v1.CreateTestAdapterRequest\x1a6.ni.measurements.metadata.v1.CreateTestAdapterResponse\x12y\n\x0eRegisterSchema\x122.ni.measurements.metadata.v1.RegisterSchemaRequest\x1a3.ni.measurements.metadata.v1.RegisterSchemaResponse\x12p\n\x0bListSchemas\x12/.ni.measurements.metadata.v1.ListSchemasRequest\x1a0.ni.measurements.metadata.v1.ListSchemasResponse\x12g\n\x08GetAlias\x12,.ni.measurements.metadata.v1.GetAliasRequest\x1a-.ni.measurements.metadata.v1.GetAliasResponse\x12s\n\x0cQueryAliases\x120.ni.measurements.metadata.v1.QueryAliasesRequest\x1a1.ni.measurements.metadata.v1.QueryAliasesResponse\x12p\n\x0bCreateAlias\x12/.ni.measurements.metadata.v1.CreateAliasRequest\x1a0.ni.measurements.metadata.v1.CreateAliasResponse\x12p\n\x0bDeleteAlias\x12/.ni.measurements.metadata.v1.DeleteAliasRequest\x1a0.ni.measurements.metadata.v1.DeleteAliasResponse\x12\x91\x01\n\x16CreateFromJsonDocument\x12:.ni.measurements.metadata.v1.CreateFromJsonDocumentRequest\x1a;.ni.measurements.metadata.v1.CreateFromJsonDocumentResponseB\xbf\x01\n\x1fcom.ni.measurements.metadata.v1B\x19MetadataStoreServiceProtoP\x01Z\nmetadatav1\xa2\x02\x04NIMM\xaa\x02,NationalInstruments.Measurements.Metadata.V1\xca\x02\x1bNI\\Measurements\\Metadata\\V1\xea\x02\x1eNI::Measurements::Metadata::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_service_pb2_grpc/__init__.py -->
## PYTHON MODULE: packages/ni.measurements.metadata.v1.proto/src/ni/measurements/metadata/v1/metadata_store_service_pb2_grpc/__init__.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class MetadataStoreServiceStub(object)`

This service is responsible for storing and retrieving metadata associated with test step measurements.
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class MetadataStoreServiceServicer(object)`

This service is responsible for storing and retrieving metadata associated with test step measurements.
    

#### `def GetUutInstance(self, request, context)`

Gets the UUT instance associated with the identifier given in the request.
        

#### `def QueryUutInstances(self, request, context)`

Perform an OData query
        

#### `def CreateUutInstance(self, request, context)`

Creates a new UUT instance in the metadata store.
        

#### `def GetUut(self, request, context)`

Gets the UUT associated with the identifier given in the request.
        

#### `def QueryUuts(self, request, context)`

Perform an OData query
        

#### `def CreateUut(self, request, context)`

Creates a new UUT in the metadata store.
        

#### `def GetOperator(self, request, context)`

Gets the operator associated with the identifier given in the request.
        

#### `def QueryOperators(self, request, context)`

Perform an OData query
        

#### `def CreateOperator(self, request, context)`

Creates a new operator in the metadata store.
        

#### `def GetTestDescription(self, request, context)`

Gets the test description associated with the identifier given in the request.
        

#### `def QueryTestDescriptions(self, request, context)`

Perform an OData query
        

#### `def CreateTestDescription(self, request, context)`

Creates a new test description in the metadata store.
        

#### `def GetTest(self, request, context)`

Gets the test associated with the identifier given in the request.
        

#### `def QueryTests(self, request, context)`

Perform an OData query
        

#### `def CreateTest(self, request, context)`

Creates a new test in the metadata store.
        

#### `def GetTestStation(self, request, context)`

Gets the test station associated with the identifier given in the request.
        

#### `def QueryTestStations(self, request, context)`

Perform an OData query
        

#### `def CreateTestStation(self, request, context)`

Creates a new test station in the metadata store.
        

#### `def GetHardwareItem(self, request, context)`

Gets the hardware item associated with the identifier given in the request.
        

#### `def QueryHardwareItems(self, request, context)`

Perform an OData query
        

#### `def CreateHardwareItem(self, request, context)`

Creates a new hardware item in the metadata store.
        

#### `def GetSoftwareItem(self, request, context)`

Gets the software item associated with the identifier given in the request.
        

#### `def QuerySoftwareItems(self, request, context)`

Perform an OData query
        

#### `def CreateSoftwareItem(self, request, context)`

Creates a new software item in the metadata store.
        

#### `def GetTestAdapter(self, request, context)`

Gets the test adapter associated with the identifier given in the request.
        

#### `def QueryTestAdapters(self, request, context)`

Perform an OData query
        

#### `def CreateTestAdapter(self, request, context)`

Creates a new test adapter in the metadata store.
        

#### `def RegisterSchema(self, request, context)`

Registers a schema. Once a schema has been published, it cannot be modified or removed.
        

#### `def ListSchemas(self, request, context)`

Lists the schemas that have been previously registered
        

#### `def GetAlias(self, request, context)`

Gets the alias and its target (i.e., the underlying metadata that it represents)
        

#### `def QueryAliases(self, request, context)`

Perform an OData query on the registered aliases
        

#### `def CreateAlias(self, request, context)`

Creates (registers) an alias of the specified metadata for use/reference when creating other metadata or publishing.
        Notes:
        - The specified metadata must have already been created prior to the alias registration.
        - This method may be called with an already registered alias name in order to update the target mapped for that existing alias.
        

#### `def DeleteAlias(self, request, context)`

Removes a registered alias
        

#### `def CreateFromJsonDocument(self, request, context)`

Creates all of the metadata entries contained in the provided JSON document.
        The JSON document should conform to the schema defined by
        https://raw.githubusercontent.com/ni/ni-apis/main/ni/measurements/metadata/v1/registration.schema.json
        The response will contain all of the associated objects from the metadata store.  If the object
        already exists, the existing object will be returned; otherwise, a new object will be created
        

### `def add_MetadataStoreServiceServicer_to_server(servicer, server)`

### `class MetadataStoreService(object)`

This service is responsible for storing and retrieving metadata associated with test step measurements.
    

#### `def GetUutInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryUutInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateUutInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetUut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryUuts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateUut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetOperator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryOperators(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateOperator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTestDescription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryTestDescriptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTestDescription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryTests(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTestStation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryTestStations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTestStation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetHardwareItem(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryHardwareItems(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateHardwareItem(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSoftwareItem(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QuerySoftwareItems(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateSoftwareItem(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTestAdapter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryTestAdapters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTestAdapter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterSchema(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ListSchemas(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAlias(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryAliases(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAlias(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteAlias(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateFromJsonDocument(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/docs/conf.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip aliases as needed.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/src/ni/panels/v1/__init__.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/src/ni/panels/v1/__init__.py

### MODULE DOCSTRING

Package for ni.panels.v1.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/src/ni/panels/v1/panel_service_pb2.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/src/ni/panels/v1/panel_service_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ni/panels/v1/panel_service.proto\x12\x0cni.panels.v1\x1a\x19google/protobuf/any.proto"X\n\x11StartPanelRequest\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x121\n\x13panel_configuration\x18\x02 \x01(\x0b2\x14.google.protobuf.Any"\'\n\x12StartPanelResponse\x12\x11\n\tpanel_url\x18\x01 \x01(\t"3\n\x10StopPanelRequest\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x12\r\n\x05reset\x18\x02 \x01(\x08"\x13\n\x11StopPanelResponse"\x18\n\x16EnumeratePanelsRequest"J\n\x10PanelInformation\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x12\x11\n\tpanel_url\x18\x02 \x01(\t\x12\x11\n\tvalue_ids\x18\x03 \x03(\t"I\n\x17EnumeratePanelsResponse\x12.\n\x06panels\x18\x01 \x03(\x0b2\x1e.ni.panels.v1.PanelInformation"5\n\x0fGetValueRequest\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x12\x10\n\x08value_id\x18\x02 \x01(\t"7\n\x10GetValueResponse\x12#\n\x05value\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"8\n\x12TryGetValueRequest\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x12\x10\n\x08value_id\x18\x02 \x01(\t":\n\x13TryGetValueResponse\x12#\n\x05value\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"j\n\x0fSetValueRequest\x12\x10\n\x08panel_id\x18\x01 \x01(\t\x12\x10\n\x08value_id\x18\x02 \x01(\t\x12#\n\x05value\x18\x03 \x01(\x0b2\x14.google.protobuf.Any\x12\x0e\n\x06notify\x18\x04 \x01(\x08"\x12\n\x10SetValueResponse2\xf7\x03\n\x0cPanelService\x12O\n\nStartPanel\x12\x1f.ni.panels.v1.StartPanelRequest\x1a .ni.panels.v1.StartPanelResponse\x12L\n\tStopPanel\x12\x1e.ni.panels.v1.StopPanelRequest\x1a\x1f.ni.panels.v1.StopPanelResponse\x12^\n\x0fEnumeratePanels\x12$.ni.panels.v1.EnumeratePanelsRequest\x1a%.ni.panels.v1.EnumeratePanelsResponse\x12I\n\x08GetValue\x12\x1d.ni.panels.v1.GetValueRequest\x1a\x1e.ni.panels.v1.GetValueResponse\x12R\n\x0bTryGetValue\x12 .ni.panels.v1.TryGetValueRequest\x1a!.ni.panels.v1.TryGetValueResponse\x12I\n\x08SetValue\x12\x1d.ni.panels.v1.SetValueRequest\x1a\x1e.ni.panels.v1.SetValueResponseBu\n\x10com.ni.panels.v1B\x0bPanelsProtoP\x01Z\x08panelsv1\xf8\x01\x01\xa2\x02\x04NIPS\xaa\x02\x1dNationalInstruments.Panels.V1\xca\x02\x0cNI\\Panels\\V1\xea\x02\x0eNI::Panels::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/src/ni/panels/v1/panel_service_pb2_grpc.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/src/ni/panels/v1/panel_service_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class PanelServiceStub(object)`

Service interface for interacting with NI panels
    

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class PanelServiceServicer(object)`

Service interface for interacting with NI panels
    

#### `def StartPanel(self, request, context)`

Start a panel using the provided configuration (or connect to if it has already been started)
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - The panel identifier contains invalid characters.
        - The panel configuration has an invalid argument.
        - NOT_FOUND:
        - The panel configuration includes a file that was not found.
        

#### `def StopPanel(self, request, context)`

Stop a panel
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - The panel identifier contains invalid characters.
        

#### `def EnumeratePanels(self, request, context)`

Enumerate the panels available in the system, including information about the state of the panels and what values they have.
        Status Codes for errors:
        

#### `def GetValue(self, request, context)`

Get a value for a control on the panel
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - The panel identifier contains invalid characters.
        - The value identifier contains invalid characters.
        - NOT_FOUND:
        - The value with the specified identifier was not found.
        

#### `def TryGetValue(self, request, context)`

Try to get a value for a control on the panel
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - The panel identifier contains invalid characters.
        - The value identifier contains invalid characters.
        

#### `def SetValue(self, request, context)`

Set a value for a control on the panel
        Status Codes for errors:
        - INVALID_ARGUMENT:
        - The panel identifier contains invalid characters.
        - The value identifier contains invalid characters.
        

### `def add_PanelServiceServicer_to_server(servicer, server)`

### `class PanelService(object)`

Service interface for interacting with NI panels
    

#### `def StartPanel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StopPanel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumeratePanels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def TryGetValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/src/ni/panels/v1/streamlit_panel_configuration_pb2.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/src/ni/panels/v1/streamlit_panel_configuration_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0ni/panels/v1/streamlit_panel_configuration.proto\x12\x0cni.panels.v1"W\n\x1bStreamlitPanelConfiguration\x12\x18\n\x10panel_script_url\x18\x01 \x01(\t\x12\x1e\n\x16python_interpreter_url\x18\x02 \x01(\tB\x8a\x01\n\x10com.ni.panels.v1B StreamlitPanelConfigurationProtoP\x01Z\x08panelsv1\xf8\x01\x01\xa2\x02\x04NIPS\xaa\x02\x1dNationalInstruments.Panels.V1\xca\x02\x0cNI\\Panels\\V1\xea\x02\x0eNI::Panels::V1b\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/tests/__init__.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/tests/__init__.py

### MODULE DOCSTRING

Tests for the ni.panels.v1.proto package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/tests/unit/test_panel_service_pb2.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/tests/unit/test_panel_service_pb2.py

### `def test___panel_service_module___check_messages___has_correct_messages() -> None`

### `def test___start_panel_request___create___created_successfully() -> None`

### `def test___start_panel_response___create___created_successfully() -> None`

### `def test___stop_panel_request___create___created_successfully() -> None`

### `def test___enumerate_panels_response___create___created_successfully() -> None`

### `def test___get_value_request___create___created_successfully() -> None`

### `def test___get_value_response___create___created_successfully() -> None`

### `def test___try_get_value_request___create___created_successfully() -> None`

### `def test___try_get_value_response___create___created_successfully() -> None`

### `def test___set_value_request___create___created_successfully() -> None`

### `def _get_configuration_as_any() -> any_pb2.Any`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.panels.v1.proto/tests/unit/test_panel_service_pb2_grpc.py -->
## PYTHON MODULE: packages/ni.panels.v1.proto/tests/unit/test_panel_service_pb2_grpc.py

### `def test___panel_service_stub___contains_correct_methods() -> None`

### `def test_add_servicer_to_server_exists() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/docs/conf.py -->
## PYTHON MODULE: packages/ni.protobuf.types/docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip aliases as needed.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/__init__.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/__init__.py

### MODULE DOCSTRING

Package for ni.protobuf.types.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/array_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/array_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dni/protobuf/types/array.proto\x12\x11ni.protobuf.types"\x1b\n\tBoolArray\x12\x0e\n\x06values\x18\x01 \x03(\x08"\x1c\n\nBytesArray\x12\x0e\n\x06values\x18\x01 \x03(\x0c"\x1d\n\x0bDoubleArray\x12\x0e\n\x06values\x18\x01 \x03(\x01"\x1d\n\x0bSInt32Array\x12\x0e\n\x06values\x18\x01 \x03(\x11"\x1d\n\x0bSInt64Array\x12\x0e\n\x06values\x18\x01 \x03(\x12"\x1d\n\x0bStringArray\x12\x0e\n\x06values\x18\x01 \x03(\t"<\n\rDouble2DArray\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0f\n\x07columns\x18\x02 \x01(\x05\x12\x0c\n\x04data\x18\x03 \x03(\x01"<\n\rString2DArray\x12\x0c\n\x04rows\x18\x01 \x01(\x05\x12\x0f\n\x07columns\x18\x02 \x01(\x05\x12\x0c\n\x04data\x18\x03 \x03(\tB\x82\x01\n\x15com.ni.protobuf.typesB\nArrayProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/attribute_value_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/attribute_value_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ni/protobuf/types/attribute_value.proto\x12\x11ni.protobuf.types"|\n\x0eAttributeValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x05H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00B\x0b\n\tattributeB\x8b\x01\n\x15com.ni.protobuf.typesB\x13AttributeValueProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/extended_property_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/extended_property_conversion.py

### MODULE DOCSTRING

Methods to convert between ExtendedPropertyDictionaries and AttributeValue maps.

### `def extended_properties_to_protobuf(extended_properties: ExtendedPropertyDictionary) -> dict[str, AttributeValue]`

Convert an ExtendedPropertyDictionary to an AttributeValue map.

### `def _value_to_attribute(value: ExtendedPropertyValue) -> AttributeValue`

### `def extended_properties_from_protobuf(attributes: Mapping[str, AttributeValue], extended_properties: ExtendedPropertyDictionary) -> None`

Convert an AttributeValue map and insert values into an ExtendedPropertyDictionary.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/precision_duration_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/precision_duration_conversion.py

### MODULE DOCSTRING

Methods to convert to and from PrecisionDuration protobuf messages.

### `def bintime_timedelta_to_protobuf(value: bt.TimeDelta, /) -> PrecisionDuration`

Convert a NI-BTF TimeDelta to a protobuf PrecisionDuration.

### `def bintime_timedelta_from_protobuf(message: PrecisionDuration, /) -> bt.TimeDelta`

Convert a protobuf PrecisionDuration to a NI-BTF TimeDelta.

### `def hightime_timedelta_to_protobuf(value: ht.timedelta, /) -> PrecisionDuration`

Convert a hightime.timedelta to a protobuf PrecisionDuration.

### `def hightime_timedelta_from_protobuf(message: PrecisionDuration, /) -> ht.timedelta`

Convert a protobuf PrecisionDuration to a hightime.timedelta.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/precision_duration_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/precision_duration_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*ni/protobuf/types/precision_duration.proto\x12\x11ni.protobuf.types"@\n\x11PrecisionDuration\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\x1a\n\x12fractional_seconds\x18\x02 \x01(\x04B\x8e\x01\n\x15com.ni.protobuf.typesB\x16PrecisionDurationProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/precision_timestamp_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/precision_timestamp_conversion.py

### MODULE DOCSTRING

Methods to convert to and from PrecisionTimestamp protobuf messages.

### `def bintime_datetime_to_protobuf(value: bt.DateTime, /) -> PrecisionTimestamp`

Convert a NI-BTF DateTime to a protobuf PrecisionTimestamp.

### `def bintime_datetime_from_protobuf(message: PrecisionTimestamp, /) -> bt.DateTime`

Convert a protobuf PrecisionTimestamp to a NI-BTF DateTime.

### `def hightime_datetime_to_protobuf(value: ht.datetime, /) -> PrecisionTimestamp`

Convert a hightime.datetime to a protobuf PrecisionTimestamp.

### `def hightime_datetime_from_protobuf(message: PrecisionTimestamp, /) -> ht.datetime`

Convert a protobuf PrecisionTimestamp to a hightime.datetime.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/precision_timestamp_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/precision_timestamp_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+ni/protobuf/types/precision_timestamp.proto\x12\x11ni.protobuf.types"A\n\x12PrecisionTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\x1a\n\x12fractional_seconds\x18\x02 \x01(\x04B\x8a\x01\n\x15com.ni.protobuf.typesB\x12PrecisionTimeProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/scalar_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/scalar_conversion.py

### MODULE DOCSTRING

Methods to convert to and from scalar protobuf messages.

- `_SCALAR_TYPE_TO_PB_ATTR_MAP = {bool: 'bool_value', int: 'sint32_value', float: 'double_value', str: 'string_value'}`

### `def scalar_to_protobuf(value: Scalar[AnyScalarType], /) -> scalar_pb2.Scalar`

Convert a Scalar python object to a protobuf scalar_pb2.Scalar.

### `def scalar_from_protobuf(message: scalar_pb2.Scalar, /) -> Scalar[AnyScalarType]`

Convert the protobuf scalar_pb2.Scalar to a Python Scalar.

### `def _check_scalar_value(value: AnyScalarType) -> None`

Perform value checking on a scalar value.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/scalar_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/scalar_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eni/protobuf/types/scalar.proto\x12\x11ni.protobuf.types\x1a\'ni/protobuf/types/attribute_value.proto"\x84\x02\n\x06Scalar\x12=\n\nattributes\x18\x01 \x03(\x0b2).ni.protobuf.types.Scalar.AttributesEntry\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0csint32_value\x18\x03 \x01(\x11H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x05 \x01(\tH\x00\x1aT\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x120\n\x05value\x18\x02 \x01(\x0b2!.ni.protobuf.types.AttributeValue:\x028\x01B\x07\n\x05valueB\x83\x01\n\x15com.ni.protobuf.typesB\x0bScalarProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/vector_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/vector_conversion.py

### MODULE DOCSTRING

Methods to convert to and from scalar protobuf messages.

- `_VECTOR_TYPE_TO_PB_ATTR_MAP = {bool: 'bool_array', int: 'sint32_array', float: 'double_array', str: 'string_array'}`

### `def vector_to_protobuf(value: Vector[Any], /) -> vector_pb2.Vector`

Convert a Vector python object to a protobuf vector_pb2.Vector.

### `def vector_from_protobuf(message: vector_pb2.Vector, /) -> Vector[AnyScalarType]`

Convert the protobuf vector_pb2.Vector to a Python Vector.

### `def _create_vector_message(vector_obj: Vector[Any], attributes: dict[str, AttributeValue]) -> vector_pb2.Vector`

### `def _check_vector_values(vector: Vector[AnyScalarType]) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/vector_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/vector_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eni/protobuf/types/vector.proto\x12\x11ni.protobuf.types\x1a\x1dni/protobuf/types/array.proto\x1a\'ni/protobuf/types/attribute_value.proto"\x82\x03\n\x06Vector\x12=\n\nattributes\x18\x01 \x03(\x0b2).ni.protobuf.types.Vector.AttributesEntry\x126\n\x0cdouble_array\x18\x02 \x01(\x0b2\x1e.ni.protobuf.types.DoubleArrayH\x00\x126\n\x0csint32_array\x18\x03 \x01(\x0b2\x1e.ni.protobuf.types.SInt32ArrayH\x00\x122\n\nbool_array\x18\x04 \x01(\x0b2\x1c.ni.protobuf.types.BoolArrayH\x00\x126\n\x0cstring_array\x18\x05 \x01(\x0b2\x1e.ni.protobuf.types.StringArrayH\x00\x1aT\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x120\n\x05value\x18\x02 \x01(\x0b2!.ni.protobuf.types.AttributeValue:\x028\x01B\x07\n\x05valueB\x83\x01\n\x15com.ni.protobuf.typesB\x0bVectorProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/vector_wrappers_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/vector_wrappers_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ni/protobuf/types/vector_wrappers.proto\x12\x11ni.protobuf.types\x1a\x1eni/protobuf/types/vector.proto">\n\x10VectorArrayValue\x12*\n\x07vectors\x18\x01 \x03(\x0b2\x19.ni.protobuf.types.VectorB\x8b\x01\n\x15com.ni.protobuf.typesB\x13VectorWrappersProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/waveform_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/waveform_conversion.py

### MODULE DOCSTRING

Methods to convert to and from waveform protobuf messages.

- `DEFAULT_PRECISION_TIMESTAMP = PrecisionTimestamp()`

### `def float64_analog_waveform_to_protobuf(value: AnalogWaveform[np.float64], /) -> DoubleAnalogWaveform`

Convert the Python AnalogWaveform to a protobuf DoubleAnalogWaveform.

### `def float64_analog_waveform_from_protobuf(message: DoubleAnalogWaveform, /) -> AnalogWaveform[np.float64]`

Convert the protobuf DoubleAnalogWaveform to a Python AnalogWaveform.

### `def float64_complex_waveform_to_protobuf(value: ComplexWaveform[np.complex128], /) -> DoubleComplexWaveform`

Convert the Python ComplexWaveform to a protobuf DoubleComplexWaveform.

### `def float64_complex_waveform_from_protobuf(message: DoubleComplexWaveform, /) -> ComplexWaveform[np.complex128]`

Convert the protobuf DoubleComplexWaveform to a Python ComplexWaveform.

### `def int16_complex_waveform_to_protobuf(value: ComplexWaveform[ComplexInt32Base], /) -> I16ComplexWaveform`

Convert the Python ComplexWaveform to a protobuf DoubleComplexWaveform.

### `def int16_complex_waveform_from_protobuf(message: I16ComplexWaveform, /) -> ComplexWaveform[ComplexInt32Base]`

Convert the protobuf DoubleComplexWaveform to a Python ComplexWaveform.

### `def float64_spectrum_to_protobuf(value: Spectrum[np.float64], /) -> DoubleSpectrum`

Convert the Python Spectrum to a protobuf DoubleSpectrum.

### `def float64_spectrum_from_protobuf(message: DoubleSpectrum, /) -> Spectrum[np.float64]`

Convert the protobuf DoubleSpectrum to a Python Spectrum.

### `def int16_analog_waveform_to_protobuf(value: AnalogWaveform[np.int16], /) -> I16AnalogWaveform`

Convert the Python AnalogWaveform to a protobuf I16AnalogWaveform.

### `def int16_analog_waveform_from_protobuf(message: I16AnalogWaveform, /) -> AnalogWaveform[np.int16]`

Convert the protobuf I16AnalogWaveform to a Python AnalogWaveform.

### `def digital_waveform_to_protobuf(value: DigitalWaveform[Any], /) -> DigitalWaveformProto`

Convert the Python DigitalWaveform to a protobuf DigitalWaveform.

### `def digital_waveform_from_protobuf(message: DigitalWaveformProto, /) -> DigitalWaveform[np.uint8]`

Convert the protobuf DigitalWaveform to a Python DigitalWaveform.

### `def _attributes_to_extended_properties(attributes: Mapping[str, WaveformAttributeValue]) -> Mapping[str, ExtendedPropertyValue]`

### `def _extended_properties_to_attributes(extended_properties: ExtendedPropertyDictionary) -> Mapping[str, WaveformAttributeValue]`

### `def _value_to_attribute(value: ExtendedPropertyValue) -> WaveformAttributeValue`

### `def _t0_from_waveform(waveform: AnyNiWaveform) -> PrecisionTimestamp | None`

### `def _timestamp_from_waveform(waveform: AnyNiWaveform) -> PrecisionTimestamp | None`

### `def _time_offset_from_waveform(waveform: AnyNiWaveform) -> float`

### `def _timestamps_from_waveform(waveform: AnyNiWaveform) -> Iterable[PrecisionTimestamp] | None`

### `def _time_interval_from_waveform(waveform: AnyNiWaveform) -> float`

### `def _timing_from_waveform_message(message: AnyWaveformProto) -> Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]`

### `def _check_regular_vs_irregular_fields(message: AnyWaveformProto) -> None`

### `def _calculate_raw_timestamp(message: AnyWaveformProto) -> PrecisionTimestamp | None`

### `def _verify_t0_timestamp_offset_relationship(message: AnyWaveformProto) -> None`

### `def _has_timestamp(message: AnyWaveformProto) -> bool`

### `def _has_t0(message: AnyWaveformProto) -> bool`

### `def _scale_from_waveform(waveform: AnalogWaveform[Any] | ComplexWaveform[Any]) -> Scale | None`

### `def _scale_mode_from_waveform_message(message: I16AnalogWaveform | I16ComplexWaveform) -> LinearScaleMode | NoneScaleMode`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/waveform_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/waveform_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ni/protobuf/types/waveform.proto\x12\x11ni.protobuf.types\x1a+ni/protobuf/types/precision_timestamp.proto"\x9a\x03\n\x14DoubleAnalogWaveform\x121\n\x02t0\x18\x01 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\n\n\x02dt\x18\x02 \x01(\x01\x12\x0e\n\x06y_data\x18\x03 \x03(\x01\x12K\n\nattributes\x18\x04 \x03(\x0b27.ni.protobuf.types.DoubleAnalogWaveform.AttributesEntry\x128\n\ttimestamp\x18\x05 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\x13\n\x0btime_offset\x18\x06 \x01(\x01\x129\n\ntimestamps\x18\x07 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"\xbd\x03\n\x11I16AnalogWaveform\x121\n\x02t0\x18\x01 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\n\n\x02dt\x18\x02 \x01(\x01\x12\x0e\n\x06y_data\x18\x03 \x03(\x11\x12H\n\nattributes\x18\x04 \x03(\x0b24.ni.protobuf.types.I16AnalogWaveform.AttributesEntry\x12\'\n\x05scale\x18\x05 \x01(\x0b2\x18.ni.protobuf.types.Scale\x128\n\ttimestamp\x18\x06 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\x13\n\x0btime_offset\x18\x07 \x01(\x01\x129\n\ntimestamps\x18\x08 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"\x9c\x03\n\x15DoubleComplexWaveform\x121\n\x02t0\x18\x01 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\n\n\x02dt\x18\x02 \x01(\x01\x12\x0e\n\x06y_data\x18\x03 \x03(\x01\x12L\n\nattributes\x18\x04 \x03(\x0b28.ni.protobuf.types.DoubleComplexWaveform.AttributesEntry\x128\n\ttimestamp\x18\x05 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\x13\n\x0btime_offset\x18\x06 \x01(\x01\x129\n\ntimestamps\x18\x07 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"\xbf\x03\n\x12I16ComplexWaveform\x121\n\x02t0\x18\x01 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\n\n\x02dt\x18\x02 \x01(\x01\x12\x0e\n\x06y_data\x18\x03 \x03(\x11\x12I\n\nattributes\x18\x04 \x03(\x0b25.ni.protobuf.types.I16ComplexWaveform.AttributesEntry\x12\'\n\x05scale\x18\x05 \x01(\x0b2\x18.ni.protobuf.types.Scale\x128\n\ttimestamp\x18\x06 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\x13\n\x0btime_offset\x18\x07 \x01(\x01\x129\n\ntimestamps\x18\x08 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"\xf9\x01\n\x0eDoubleSpectrum\x12\x17\n\x0fstart_frequency\x18\x01 \x01(\x01\x12\x1b\n\x13frequency_increment\x18\x02 \x01(\x01\x12\x0c\n\x04data\x18\x03 \x03(\x01\x12E\n\nattributes\x18\x04 \x03(\x0b21.ni.protobuf.types.DoubleSpectrum.AttributesEntry\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"\x84\x01\n\x16WaveformAttributeValue\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x05H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00B\x0b\n\tattribute"\xa6\x03\n\x0fDigitalWaveform\x121\n\x02t0\x18\x01 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\n\n\x02dt\x18\x02 \x01(\x01\x12\x14\n\x0csignal_count\x18\x03 \x01(\x05\x12\x0e\n\x06y_data\x18\x04 \x01(\x0c\x12F\n\nattributes\x18\x05 \x03(\x0b22.ni.protobuf.types.DigitalWaveform.AttributesEntry\x128\n\ttimestamp\x18\x06 \x01(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x12\x13\n\x0btime_offset\x18\x07 \x01(\x01\x129\n\ntimestamps\x18\x08 \x03(\x0b2%.ni.protobuf.types.PrecisionTimestamp\x1a\\\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).ni.protobuf.types.WaveformAttributeValue:\x028\x01"G\n\x05Scale\x126\n\x0clinear_scale\x18\x01 \x01(\x0b2\x1e.ni.protobuf.types.LinearScaleH\x00B\x06\n\x04mode"+\n\x0bLinearScale\x12\x0c\n\x04gain\x18\x01 \x01(\x01\x12\x0e\n\x06offset\x18\x02 \x01(\x01B\x85\x01\n\x15com.ni.protobuf.typesB\rWaveformProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/waveform_wrappers_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/waveform_wrappers_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)ni/protobuf/types/waveform_wrappers.proto\x12\x11ni.protobuf.types\x1a ni/protobuf/types/waveform.proto"\\\n\x1eDoubleAnalogWaveformArrayValue\x12:\n\twaveforms\x18\x01 \x03(\x0b2\'.ni.protobuf.types.DoubleAnalogWaveform"V\n\x1bI16AnalogWaveformArrayValue\x127\n\twaveforms\x18\x01 \x03(\x0b2$.ni.protobuf.types.I16AnalogWaveform"^\n\x1fDoubleComplexWaveformArrayValue\x12;\n\twaveforms\x18\x01 \x03(\x0b2(.ni.protobuf.types.DoubleComplexWaveform"X\n\x1cI16ComplexWaveformArrayValue\x128\n\twaveforms\x18\x01 \x03(\x0b2%.ni.protobuf.types.I16ComplexWaveform"P\n\x18DoubleSpectrumArrayValue\x124\n\twaveforms\x18\x01 \x03(\x0b2!.ni.protobuf.types.DoubleSpectrum"R\n\x19DigitalWaveformArrayValue\x125\n\twaveforms\x18\x01 \x03(\x0b2".ni.protobuf.types.DigitalWaveformB\x8d\x01\n\x15com.ni.protobuf.typesB\x15WaveformWrappersProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/xydata_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/xydata_conversion.py

### MODULE DOCSTRING

Methods to convert to and from DoubleXYData protobuf messages.

### `def float64_xydata_to_protobuf(value: XYData[np.float64], /) -> xydata_pb2.DoubleXYData`

Convert a XYData python object to a protobuf xydata_pb2.DoubleXYData.

### `def float64_xydata_from_protobuf(message: xydata_pb2.DoubleXYData, /) -> XYData[np.float64]`

Convert the protobuf xydata_pb2.DoubleXYData to a Python XYData.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/xydata_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/xydata_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eni/protobuf/types/xydata.proto\x12\x11ni.protobuf.types\x1a\'ni/protobuf/types/attribute_value.proto"\xc9\x01\n\x0cDoubleXYData\x12\x0e\n\x06x_data\x18\x01 \x03(\x01\x12\x0e\n\x06y_data\x18\x02 \x03(\x01\x12C\n\nattributes\x18\x03 \x03(\x0b2/.ni.protobuf.types.DoubleXYData.AttributesEntry\x1aT\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x120\n\x05value\x18\x02 \x01(\x0b2!.ni.protobuf.types.AttributeValue:\x028\x01B\x83\x01\n\x15com.ni.protobuf.typesB\x0bXYDataProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/src/ni/protobuf/types/xydata_wrappers_pb2.py -->
## PYTHON MODULE: packages/ni.protobuf.types/src/ni/protobuf/types/xydata_wrappers_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ni/protobuf/types/xydata_wrappers.proto\x12\x11ni.protobuf.types\x1a\x1eni/protobuf/types/xydata.proto"K\n\x16DoubleXYDataArrayValue\x121\n\x08x_y_data\x18\x01 \x03(\x0b2\x1f.ni.protobuf.types.DoubleXYDataB\x8b\x01\n\x15com.ni.protobuf.typesB\x13XYDataWrappersProtoP\x01Z\x05types\xa2\x02\x04NIPT\xaa\x02"NationalInstruments.Protobuf.Types\xca\x02\x11NI\\PROTOBUF\\TYPES\xea\x02\x13NI::Protobuf::Typesb\x06proto3')`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/__init__.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/__init__.py

### MODULE DOCSTRING

Tests for the ni.protobuf.types package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/__init__.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the package.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/base_waveform_conversion_tests.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/base_waveform_conversion_tests.py

### MODULE DOCSTRING

Unit tests for conversion of the timing aspects of various types of waveforms.

### `class BaseWaveformConversionTests(ABC, Generic[TWaveform, TWaveformProto])`

Base class for testing waveform conversion.

    Subclasses implement more specific or typed waveform conversion tests.
    

#### `def make_waveform(self) -> TWaveform`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> TWaveformProto`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: TWaveform) -> TWaveformProto`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: TWaveformProto) -> TWaveform`

Convert a proto message to the corresponding Python waveform.

#### `def test___waveform_with_standard_timing___convert___valid_protobuf(self) -> None`

#### `def test___waveform_with_standard_timing_and_offset___convert___valid_protobuf(self) -> None`

#### `def test___waveform_with_standard_timing___round_trip___waveforms_match(self) -> None`

#### `def test___waveform_with_irregular_timing___convert___valid_protobuf(self) -> None`

#### `def test___waveform_with_regular_timing___round_trip___waveforms_match(self, timestamp_seconds: float, time_offset: float) -> None`

#### `def test___waveform_with_none_timing___round_trip___waveforms_match(self, timestamp_seconds: int, time_offset: float) -> None`

#### `def test___waveform_with_extended_properties___convert___valid_protobuf(self) -> None`

#### `def test____waveform_with_scaling___convert___valid_protobuf(self) -> None`

#### `def test___waveform_proto_with_timing___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_timing___round_trip___waveforms_match(self) -> None`

#### `def test___waveform_proto_regular_timing___round_trip___timing_equivalent(self, timestamp_seconds: int, start_time_seconds: int, offset: float, normalized_timestamp_seconds: int, normalized_start_time_seconds: int) -> None`

#### `def test___waveform_proto_with_timing_no_t0___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_timing_no_dt___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_dt_and_offset___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_t0_and_timestamp_and_offset___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_timestamps___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_t0_and_offset_no_timestamp___convert___raises_exception(self) -> None`

#### `def test___waveform_proto_with_attributes___convert___valid_python_object(self) -> None`

#### `def test___waveform_proto_with_scaling___convert___valid_python_object(self) -> None`

#### `def _to_proto_timestamps(self, timestamps: list[dt.datetime]) -> list[PrecisionTimestamp]`

#### `def _assert_proto_standard_timing(self, waveform_proto: TWaveformProto, t0_dt: dt.datetime, sample_interval: float) -> None`

#### `def _assert_proto_standard_timing_with_offset(self, waveform_proto: TWaveformProto, t0_dt: dt.datetime, time_offset: dt.timedelta, sample_interval: float) -> None`

#### `def _assert_waveform_irregular_timing_with_timestamps(self, waveform: TWaveform, expected_timestamps: list[PrecisionTimestamp]) -> None`

#### `def _assert_waveform_timestamp_and_t0_timing(self, waveform: TWaveform, t0_seconds: int, timestamp_seconds: int, sample_interval: float, time_offset: float) -> None`

#### `def _normalize_precision_timestamp(self, timestamp: PrecisionTimestamp) -> PrecisionTimestamp`

### `class SupportsScaleMode(Protocol)`

A protocol to test if something has the scale_mode property.

#### `def scale_mode(self) -> ScaleMode`

The scale mode.

#### `def scale_mode(self, value: ScaleMode) -> None`

The scale mode setter.

### `class SupportsScale(Protocol)`

A protocol to test if something has the scale property.

#### `def scale(self) -> Scale`

The scale.

#### `def scale(self, value: Scale) -> None`

The scale setter.

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_ni_protobuf_types.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_ni_protobuf_types.py

### MODULE DOCSTRING

Tests for the ni.protobuf.types package.

- `EXPECTED_T0 = PrecisionTimestamp(seconds=5, fractional_seconds=0)`

- `EXPECTED_DT = 0.01`

- `EXPECTED_ATTRIBUTES = {'attr1': WaveformAttributeValue(integer_value=1), 'attr2': WaveformAttributeValue(string_value='two')}`

- `EXPECTED_SCALAR_ATTRIBUTES = {'attr1': AttributeValue(integer_value=1), 'attr2': AttributeValue(string_value='two')}`

### `def test___valid_inputs___createdouble2darray___message_created() -> None`

### `def test___valid_inputs___createstring2darray___message_created() -> None`

### `def test___valid_inputs___create_doubleanalogwaveform___message_created() -> None`

### `def test___valid_inputs___create_i16analogwaveform___message_created() -> None`

### `def test___valid_inputs___create_doublecomplexwaveform___message_created() -> None`

### `def test___valid_inputs___create_i16complexwaveform___message_created() -> None`

### `def test___valid_inputs___create_doublespectrum___message_created() -> None`

### `def test___valid_inputs___create_doublexydata___message_created() -> None`

### `def test___valid_inputs___create_double_scalar___message_created() -> None`

### `def test___valid_inputs___create_int_scalar___message_created() -> None`

### `def test___valid_inputs___create_bool_scalar___message_created() -> None`

### `def test___valid_inputs___create_string_scalar___message_created() -> None`

### `def test___valid_inputs___create_double_vector___message_created() -> None`

### `def test___valid_inputs___create_int_vector___message_created() -> None`

### `def test___valid_inputs___create_bool_vector___message_created() -> None`

### `def test___valid_inputs___create_string_vector___message_created() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_precision_duration_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_precision_duration_conversion.py

### `def test___precision_duration___convert___valid_bintime_timedelta() -> None`

### `def test___bintime_timedelta___convert___valid_precision_duration() -> None`

### `def test___precision_duration___convert___valid_hightime_timedelta() -> None`

### `def test___hightime_timedelta___convert___valid_precision_duration() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_precision_timestamp_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_precision_timestamp_conversion.py

### `def test___precision_timestamp___convert___valid_bintime_datetime() -> None`

### `def test___bintime_datetime___convert___valid_precision_timestamp() -> None`

### `def test___precision_timestamp___convert___valid_hightime_datetime() -> None`

### `def test___hightime_datetime___convert___valid_precision_timestamp() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_scalar_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_scalar_conversion.py

### `def test___bool_scalar_protobuf___convert___valid_bool_scalar() -> None`

### `def test___int32_scalar_protobuf___convert___valid_int_scalar() -> None`

### `def test___double_scalar_protobuf___convert___valid_float_scalar() -> None`

### `def test___string_scalar_protobuf___convert___valid_str_scalar() -> None`

### `def test___scalar_protobuf_value_unset___convert___throws_value_error() -> None`

### `def test___scalar_protobuf_units_unset___convert___python_units_blank() -> None`

### `def test___non_units_attributes___to_python___attributes_converted() -> None`

### `def test___bool_scalar___convert___valid_bool_scalar_protobuf() -> None`

### `def test___int_scalar___convert___valid_int32_scalar_protobuf() -> None`

### `def test___float_scalar___convert___valid_double_scalar_protobuf() -> None`

### `def test___str_scalar___convert___valid_string_scalar_protobuf() -> None`

### `def test___scalar_units_unset___convert___protobuf_units_blank() -> None`

### `def test___non_units_attributes___to_protobuf___attributes_converted() -> None`

### `def test___int_scalar_out_of_range___convert___raises_value_error() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_spectrum_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_spectrum_conversion.py

### `def test___default_spectrum___convert___valid_protobuf() -> None`

### `def test___spectrum_with_data___convert___valid_protobuf() -> None`

### `def test___spectrum_with_extended_properties___convert___valid_protobuf() -> None`

### `def test___default_dbl_spectrum___convert___valid_python_object() -> None`

### `def test___dbl_spectrum_with_data___convert___valid_python_object() -> None`

### `def test___dbl_spectrum_with_attributes___convert___valid_python_object() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_vector_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_vector_conversion.py

### `def test___bool_vector_protobuf___convert___valid_bool_vector() -> None`

### `def test___int32_vector_protobuf___convert___valid_int_vector() -> None`

### `def test___double_vector_protobuf___convert___valid_float_vector() -> None`

### `def test___string_vector_protobuf___convert___valid_str_vector() -> None`

### `def test___vector_protobuf_value_unset___convert___throws_value_error() -> None`

### `def test___vector_protobuf_units_unset___convert___python_units_blank() -> None`

### `def test___vector_with_non_units_attributes___to_python___attributes_converted() -> None`

### `def test___bool_vector___convert___valid_bool_vector_protobuf() -> None`

### `def test___int_vector___convert___valid_int32_vector_protobuf() -> None`

### `def test___float_vector___convert___valid_double_vector_protobuf() -> None`

### `def test___str_vector___convert___valid_string_vector_protobuf() -> None`

### `def test___vector_units_unset___convert___protobuf_units_blank() -> None`

### `def test___vector_with_non_units_attributes___to_protobuf___attributes_converted() -> None`

### `def test___empty_vector___to_protobuf___raises_value_error() -> None`

### `def test___int_vector_out_of_range___convert___raises_value_error() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_waveform_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_waveform_conversion.py

### `class TestDoubleAnalogConversion(BaseWaveformConversionTests[AnalogWaveform[np.float64], DoubleAnalogWaveform])`

Test for converting double analog waveforms to/from protobuf messages.

#### `def make_waveform(self) -> AnalogWaveform[np.float64]`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> DoubleAnalogWaveform`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: AnalogWaveform[np.float64]) -> DoubleAnalogWaveform`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: DoubleAnalogWaveform) -> AnalogWaveform[np.float64]`

Convert a proto message to the corresponding Python waveform.

#### `def test___default_analog_waveform___convert___valid_protobuf(self) -> None`

#### `def test___analog_waveform_samples_only___convert___valid_protobuf(self) -> None`

#### `def test___analog_waveform_non_zero_samples___convert___valid_protobuf(self) -> None`

#### `def test___default_dbl_analog_wfm___convert___valid_python_object(self) -> None`

#### `def test___dbl_analog_wfm_with_y_data___convert___valid_python_object(self) -> None`

### `class TestDoubleComplexWaveformConversion(BaseWaveformConversionTests[ComplexWaveform[np.complex128], DoubleComplexWaveform])`

Test for converting double complex waveforms to/from protobuf messages.

#### `def make_waveform(self) -> ComplexWaveform[np.complex128]`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> DoubleComplexWaveform`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: ComplexWaveform[np.complex128]) -> DoubleComplexWaveform`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: DoubleComplexWaveform) -> ComplexWaveform[np.complex128]`

Convert a proto message to the corresponding Python waveform.

#### `def test___default_float64_complex_waveform___convert___valid_protobuf(self) -> None`

#### `def test___float64_complex_waveform_samples_only___convert___valid_protobuf(self) -> None`

#### `def test___float64_complex_waveform_non_zero_samples___convert___valid_protobuf(self) -> None`

#### `def test___default_dbl_complex_wfm___convert___valid_python_object(self) -> None`

#### `def test___dbl_complex_wfm_with_y_data___convert___valid_python_object(self) -> None`

### `class TestI16ComplexWaveformConversion(BaseWaveformConversionTests[ComplexWaveform[ComplexInt32Base], I16ComplexWaveform])`

Test for converting int complex waveforms to/from protobuf messages.

#### `def make_waveform(self) -> ComplexWaveform[ComplexInt32Base]`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> I16ComplexWaveform`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: ComplexWaveform[ComplexInt32Base]) -> I16ComplexWaveform`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: I16ComplexWaveform) -> ComplexWaveform[ComplexInt32Base]`

Convert a proto message to the corresponding Python waveform.

#### `def test___default_int16_complex_waveform___convert___valid_protobuf(self) -> None`

#### `def test___int16_complex_waveform_samples_only___convert___valid_protobuf(self) -> None`

#### `def test___int16_complex_waveform_non_zero_samples___convert___valid_protobuf(self) -> None`

#### `def test___default_int16_complex_wfm___convert___valid_python_object(self) -> None`

#### `def test___int16_complex_wfm_with_y_data___convert___valid_python_object(self) -> None`

### `class TestI16AnalogWaveformConversion(BaseWaveformConversionTests[AnalogWaveform[np.int16], I16AnalogWaveform])`

Test for converting int analog waveforms to/from protobuf messages.

#### `def make_waveform(self) -> AnalogWaveform[np.int16]`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> I16AnalogWaveform`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: AnalogWaveform[np.int16]) -> I16AnalogWaveform`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: I16AnalogWaveform) -> AnalogWaveform[np.int16]`

Convert a proto message to the corresponding Python waveform.

#### `def test___default_int16_analog_waveform___convert___valid_protobuf(self) -> None`

#### `def test___int16_analog_waveform_samples_only___convert___valid_protobuf(self) -> None`

#### `def test___int16_analog_waveform_non_zero_samples___convert___valid_protobuf(self) -> None`

#### `def test___default_i16_analog_wfm___convert___valid_python_object(self) -> None`

#### `def test___i16_analog_wfm_with_y_data___convert___valid_python_object(self) -> None`

### `class TestDigitalWaveformConversion(BaseWaveformConversionTests[DigitalWaveform[Any], DigitalWaveformProto])`

Test for converting digital waveforms to/from protobuf messages.

#### `def make_waveform(self) -> DigitalWaveform[Any]`

Create a waveform with small non-zero sample data.

#### `def make_waveform_proto(self, attributes: Mapping[str, WaveformAttributeValue] | None=None, scale: Scale | None=None) -> DigitalWaveformProto`

Create a waveform protobuf object with small non-zero sample data.

#### `def to_protobuf(self, waveform: DigitalWaveform[Any]) -> DigitalWaveformProto`

Convert a Python waveform to its corresponding proto message.

#### `def from_protobuf(self, waveform_proto: DigitalWaveformProto) -> DigitalWaveform[Any]`

Convert a proto message to the corresponding Python waveform.

#### `def test___default_digital_waveform___convert___valid_protobuf(self) -> None`

#### `def test___digital_waveform_with_data___convert___valid_protobuf(self) -> None`

#### `def test___default_digital_waveform_proto___convert___valid_python_object(self) -> None`

#### `def test___digital_waveform_proto_with_data___convert___valid_python_object(self) -> None`

#### `def test___digital_waveform_proto_with_attributes___convert___valid_python_object(self) -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=packages/ni.protobuf.types/tests/unit/test_xydata_conversion.py -->
## PYTHON MODULE: packages/ni.protobuf.types/tests/unit/test_xydata_conversion.py

### `def test___doublexydata_protobuf___convert___valid_xydata_default_units() -> None`

### `def test___doublexydata_protobuf_with_units___convert___valid_xydata() -> None`

### `def test___doublexydata_protobuf_with_other_attrs___convert___attrs_converted() -> None`

### `def test___float64_xydata___convert___valid_doublexydata_protobuf() -> None`

### `def test___int16_xydata___convert___causes_mypy_error() -> None`

### `def test___xydata_with_extended_properties___convert___valid_doublexydata_protobuf() -> None`

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/src/grpc_generator/__init__.py -->
## PYTHON MODULE: tools/grpc_generator/src/grpc_generator/__init__.py

### MODULE DOCSTRING

grpc_generator package.

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/src/grpc_generator/__main__.py -->
## PYTHON MODULE: tools/grpc_generator/src/grpc_generator/__main__.py

### MODULE DOCSTRING

grpc_generator entry points.

- `REPO_ROOT = next((p for p in pathlib.Path(__file__).parents if (p / 'third_party').exists()), pathlib.Path('.'))`

### `def cli(proto_basepath: pathlib.Path, proto_subpath: pathlib.Path, proto_include_path: list[pathlib.Path], output_basepath: pathlib.Path, output_format: str) -> None`

Generate gRPC Python stubs from proto files.

    Specifying input and output locations

      This script uses the protobuf files from the folder specified by
    --proto-basepath and --proto-subpath and emits Python files into the
    folder specified by --output-basepath:

    
      {proto-basepath}/{proto-subpath}  -->  {output-basepath}/{proto-subpath}

      The script resolves gRPC imports from --proto-basepath by default. Include
    additional paths by using --proto-include-path for each required folder.

    Specifying output format

      The script supports generating gRPC packages as either subpackages
    or submodules with --output-format.

      When generating submodules, the script creates Python files with names
    that match the source protobuf files:

    
      waveform.proto  -->  waveform_pb2.py

      When generating subpackages, the script creates folders with names
    that match the source protobuf files:

    
      waveform.proto  -->  waveform_pb2/__init__.py

      Clients use the same "import waveform_pb2" syntax.

    

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/src/grpc_generator/generate_stubs.py -->
## PYTHON MODULE: tools/grpc_generator/src/grpc_generator/generate_stubs.py

### MODULE DOCSTRING

Script to generate gRPC stubs for all packages in the repository.

### `def main() -> None`

Executes the generation of the gRPC stubs based on the specified package information.

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/src/grpc_generator/generator.py -->
## PYTHON MODULE: tools/grpc_generator/src/grpc_generator/generator.py

### MODULE DOCSTRING

Generate gRPC Python stubs from proto files.

- `USAGE_EXAMPLE = 'Example:\n\n\x08\ngrpc-generator  --proto-subpath ni/protobuf/types  --output-basepath ../../packages/ni.protobuf.types/src  --output-format submodule'`

### `class OutputFormat(str, enum.Enum)`

Supported Python output formats for generated gRPC packages.

### `class GenerationSpec()`

A NamedTuple that describes a gRPC package for code generation.

#### `def name(self) -> str`

Return the name of the protobuf package.

#### `def package_folder(self) -> pathlib.Path`

Return the full path to the folder for the generated files.

#### `def package_descriptor_file(self) -> pathlib.Path`

Return the path to use for the package's FileDescriptorSet.

#### `def proto_paths(self) -> list[pathlib.Path]`

Return a list of all proto files under proto_subpath.

#### `def get_matching_message_files(self, relative_proto_file_path: pathlib.Path) -> list[pathlib.Path]`

Get the full paths to the message files for the specified proto package path.

#### `def get_matching_service_files(self, relative_proto_file_path: pathlib.Path) -> list[pathlib.Path]`

Get the full paths to the service files for the specified proto package path.

### `def handle_cli(proto_basepath: pathlib.Path, proto_subpath: pathlib.Path, proto_include_paths: list[pathlib.Path], output_basepath: pathlib.Path, output_format: OutputFormat) -> None`

Handle the command line interface invocation.

### `def do_generation(generation_spec: GenerationSpec) -> None`

Regenerate the gRPC package according to the generation_spec.

### `def reset_python_package(generation_spec: GenerationSpec) -> None`

Delete all generated gRPC files to accommodate API name changes and deletions.

### `def generate_python_files(generation_spec: GenerationSpec) -> None`

Generate Python files from the Protobuf files.

### `def finalize_python_package(generation_spec: GenerationSpec) -> None`

Post process the generated files according to the generation_spec.

### `def transform_files_for_namespace(generation_spec: GenerationSpec) -> None`

Convert a submodule to a subpackage.

### `def add_submodule_files(generation_spec: GenerationSpec) -> None`

Add an __init__.py file to the specified protobuf package.

### `def remove_files(files: list[pathlib.Path]) -> None`

Delete the specified files.

### `def invoke_protoc(protoc_arguments: list[str]) -> None`

Invoke the Protobuf compiler.

### `def is_generated_subpackage_dir(candidate: pathlib.Path) -> bool`

Determine if the input path is named like a generated subpackage dir.

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/tests/__init__.py -->
## PYTHON MODULE: tools/grpc_generator/tests/__init__.py

### MODULE DOCSTRING

Tests for grpc_generator.

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/tests/unit/__init__.py -->
## PYTHON MODULE: tools/grpc_generator/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for grpc_generator.

<!--NI_PYTHON_API repo=ni-apis-python path=tools/grpc_generator/tests/unit/test_main.py -->
## PYTHON MODULE: tools/grpc_generator/tests/unit/test_main.py

### MODULE DOCSTRING

Acceptance tests for the command line interface.

### `def call_generate(args: list[str]) -> Result`

Invoke the 'generate' CLI command.

### `def assert_is_submodule(output_path: pathlib.Path) -> None`

Assert the output_path contains Python submodules.

### `def assert_is_subpackage(output_path: pathlib.Path) -> None`

Assert the output_path contains Python subpackages.

### `def test___generator___call_generator_help___succeeds() -> None`

### `def test___empty_package___generate_submodules___creates_submodules(tmp_path: pathlib.Path) -> None`

### `def test___empty_package___generate_subpackages___creates_subpackages(tmp_path: pathlib.Path) -> None`

### `def test___existing_package___generate_submodules___updates_submodules(tmp_path: pathlib.Path) -> None`

### `def test___existing_package___generate_subpackages___updates_subpackages(tmp_path: pathlib.Path) -> None`
