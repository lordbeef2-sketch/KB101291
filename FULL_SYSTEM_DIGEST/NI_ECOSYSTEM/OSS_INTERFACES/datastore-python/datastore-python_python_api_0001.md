# NI PYTHON API DIGEST: datastore-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/datastore-python commit=f78bf987f5b630b942f3f214a6a09d754331a05f -->

<!--NI_PYTHON_API repo=datastore-python path=docs/conf.py -->
## PYTHON MODULE: docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def process_docstring(app, what, name, obj, options, lines)`

Make edits to docstrings as necessary

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=datastore-python path=examples/overview/src/__init__.py -->
## PYTHON MODULE: examples/overview/src/__init__.py

### MODULE DOCSTRING

Overview example of NI Measurement Data Store usage.

<!--NI_PYTHON_API repo=datastore-python path=examples/overview/src/overview.py -->
## PYTHON MODULE: examples/overview/src/overview.py

### MODULE DOCSTRING

Overview example demonstrating data publishing and querying.

### `def main() -> None`

Main function to demonstrate data publishing and querying.

### `def publish_data() -> str`

Demonstrate data publishing of an AnalogWaveform.

### `def query_data(published_measurement_id: str) -> None`

Demonstrate querying a published AnalogWaveform measurement.

<!--NI_PYTHON_API repo=datastore-python path=examples/system/src/__init__.py -->
## PYTHON MODULE: examples/system/src/__init__.py

### MODULE DOCSTRING

Detect, publish, and query system hardware and software resources.

<!--NI_PYTHON_API repo=datastore-python path=examples/system/src/system.py -->
## PYTHON MODULE: examples/system/src/system.py

### MODULE DOCSTRING

How to detect, publish, and query system hardware and software resources.

### `class SystemMetadata()`

Represents the available resources on a system.

### `def main() -> None`

Detect, publish, and query hardware and software resources from the local system.

### `def detect_system_resources(system_target: str='localhost') -> SystemMetadata`

Scan the specified system_target and return SystemMetadata describing the system.

### `def create_hardware_item(hardware_entry: nisyscfg.hardware_resource.HardwareResource) -> HardwareItem`

Create a new HardwareItem instance from the specified nisyscfg entry.

### `def create_software_item(software_entry: nisyscfg.component_info.ComponentInfo) -> SoftwareItem`

Create a new SoftwareItem instance from the specified nisyscfg entry.

### `def create_test_station(session: nisyscfg.Session) -> TestStation`

Create a new TestStation instance from the specified nisyscfg session.

### `def create_operator(name: str='') -> Operator`

Create a new Operator instance using the specified name. Otherwise, use the active user.

### `def publish_empty_test_result(system_metadata: SystemMetadata) -> str`

Publish a TestResult with the specified system_metadata and return its ID.

### `def query_test_result(test_result_id: str) -> TestResult`

Query the NI DataStore Service for the specified TestResult and return it.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/__init__.py -->
## PYTHON MODULE: src/ni/datastore/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Data/Metadata Stores.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/__init__.py -->
## PYTHON MODULE: src/ni/datastore/data/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Data Store.

- `__all__ = ['DataStoreClient', 'ErrorInformation', 'Outcome', 'PublishedCondition', 'PublishedMeasurement', 'Step', 'TestResult']`

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_data_store_client.py -->
## PYTHON MODULE: src/ni/datastore/data/_data_store_client.py

### MODULE DOCSTRING

Data store client for publishing and reading data.

### `class DataStoreClient()`

Data store client for publishing and reading data.

#### `def __init__(self, discovery_client: DiscoveryClient | None=None, grpc_channel: Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the DataStoreClient.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional data store gRPC channel. Providing this channel will bypass
                discovery service resolution of the data store.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the data store client.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the data store client.

#### `def close(self) -> None`

Close the data store client and clean up resources that it owns.

#### `def publish_condition(self, name: str, condition_type: str, value: object, step_id: str) -> str`

Publish a condition value to the data store.

        Args:
            name: An identifier describing the condition value.
                For example, "Voltage" or "Temperature".

            condition_type: The type of this condition. For example, "Upper Limit",
                "Environment", or "Setup".

            value: The single value for this condition to publish on the test
                step. This should be a scalar value that can be converted to
                the appropriate protobuf scalar type.

            step_id: The ID of the step associated with this condition. This
                value is expected to be a parsable GUID.

        Returns:
            str: The condition id - the unique ID of the condition for
                referencing in queries
        

#### `def publish_condition_batch(self, name: str, condition_type: str, values: object, step_id: str) -> str`

Publish a batch of N values for a condition to the data store.

        Args:
            name: An identifier describing the condition values.
                For example, "Voltage" or "Temperature".

            condition_type: The type of this condition. For example, "Upper Limit",
                "Environment", or "Setup".

            values: The values for this condition across all publishes on the
                test step. This should be a Vector of N values.

            step_id: The ID of the step associated with this batch of condition
                values. This value is expected to be a parsable GUID.

        Returns:
            str: The condition id - the unique ID of the condition for
                referencing in queries
        

#### `def publish_measurement(self, name: str, value: object, step_id: str, timestamp: ht.datetime | None=None, outcome: Outcome=Outcome.UNSPECIFIED, error_information: ErrorInformation | None=None, hardware_item_ids: Iterable[str]=tuple(), test_adapter_ids: Iterable[str]=tuple(), software_item_ids: Iterable[str]=tuple(), notes: str='') -> str`

Publish a single measurement value associated with a test step.

        Args:
            name: The name used for associating/grouping
                conceptually alike measurements across multiple publish
                iterations. For example, "Temperature" can be used for
                associating temperature readings across multiple iterations.

            value: The value of the measurement being published. Supported types:

                - Scalar: Single float, int, str or boolean
                - Vector: Array of float, int, str or boolean values
                - DoubleAnalogWaveform: Analog waveform with double precision
                - DoubleXYData: XY coordinate data with double precision
                - I16AnalogWaveform: Analog waveform with 16-bit integer precision
                - DoubleComplexWaveform: Complex waveform with double precision
                - I16ComplexWaveform: Complex waveform with 16-bit integer precision
                - DoubleSpectrum: Frequency spectrum data with double precision
                - DigitalWaveform: Digital waveform data

            step_id: The ID of the step associated with this measurement. This
                value is expected to be a parsable GUID.

            timestamp: The timestamp of the measurement. If None, no timestamp
                will be specified.

            outcome: The outcome of the measurement (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).

            error_information: Error or exception information in case of
                measurement failure.

            hardware_item_ids: The IDs of the hardware items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            test_adapter_ids: The IDs of the test adapters associated with this
                measurement. These values are expected to be parsable GUIDs or
                aliases.

            software_item_ids: The IDs of the software items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            notes: Any notes to be associated with the captured measurement.

        Returns:
            str: The published measurement id.
        

#### `def publish_measurement_batch(self, name: str, values: object, step_id: str, timestamps: Iterable[ht.datetime]=tuple(), outcomes: Iterable[Outcome]=tuple(), error_information: Iterable[ErrorInformation]=tuple(), hardware_item_ids: Iterable[str]=tuple(), test_adapter_ids: Iterable[str]=tuple(), software_item_ids: Iterable[str]=tuple(), notes: str='') -> Sequence[str]`

Publish multiple measurements at once for parametric sweeps.

        Args:
            name: The name used for associating/grouping
                conceptually alike measurements across multiple publish
                iterations. For example, "Temperature" can be used for
                associating temperature readings across multiple iterations.

            values: The values of the measurement being published
                across N iterations.

            step_id: The ID of the step associated with this measurement. This
                value is expected to be a parsable GUID.

            timestamps: The timestamps corresponding to the N iterations of
                batched measurement being published. Can be empty (no timestamp
                info), single value (applied to all), or N values (one per
                measurement).

            outcomes: The outcomes corresponding to the N iterations of batched
                measurement being published. Can be empty (no outcome info),
                single value (applied to all), or N values (one per
                measurement).

            error_information: The error information corresponding to the N
                iterations of batched measurement being published. Can be empty
                (no error info), single value (applied to all), or N values
                (one per measurement).

            hardware_item_ids: The IDs of the hardware items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            test_adapter_ids: The IDs of the test adapters associated with this
                measurement. These values are expected to be parsable GUIDs or
                aliases.

            software_item_ids: The IDs of the software items associated with
                this measurement. These values are expected to be parsable
                GUIDs or aliases.

            notes: Any notes to be associated with the published measurements.

        Returns:
            Sequence[str]: The IDs of the corresponding PublishedMeasurements. A single
            ID will be returned when publishing scalar measurement values.
            N IDs will be returned when publishing (N) non-scalar measurement values.
        

#### `def read_condition_value(self, read_source: PublishedCondition, expected_type: Type[TRead]) -> TRead`

#### `def read_condition_value(self, read_source: PublishedCondition) -> object`

#### `def read_condition_value(self, read_source: PublishedCondition, expected_type: Type[TRead] | None=None) -> TRead | object`

Read data published to the data store.

        Args:
            read_source: The source from which to read data (PublishedCondition).

            expected_type: Optional type to validate the returned data against.
                If provided, a TypeError will be raised if the actual data type
                doesn't match.

        Returns:
            The data retrieved from the data store. The return type depends on
            what was originally published:
            - Scalar conditions return as Vectors
            - Other types are returned as originally published
            If expected_type is specified, the return value is guaranteed to be
            of that type.

        Raises:
            TypeError: If expected_type is provided and the actual data type
                doesn't match.
        

#### `def read_measurement_value(self, read_source: PublishedMeasurement, expected_type: Type[TRead]) -> TRead`

#### `def read_measurement_value(self, read_source: PublishedMeasurement) -> object`

#### `def read_measurement_value(self, read_source: PublishedMeasurement, expected_type: Type[TRead] | None=None) -> TRead | object`

Read data published to the data store.

        Args:
            read_source: The source from which to read data (PublishedMeasurement).

            expected_type: Optional type to validate the returned data against.
                If provided, a TypeError will be raised if the actual data type
                doesn't match.

        Returns:
            The data retrieved from the data store. The return type depends on
            what was originally published:
            - Scalar measurements return as Vectors
            - Other types are returned as originally published
            If expected_type is specified, the return value is guaranteed to be
            of that type.

        Raises:
            TypeError: If expected_type is provided and the actual data type
                doesn't match.
        

#### `def create_step(self, step: Step) -> str`

Create a new step in the data store.

        A step is owned by a test result and is a logical grouping of published
        measurements and conditions. All measurements and conditions must be
        associated with a step.

        Args:
            step: The metadata of the step to be created.

        Returns:
            str: The identifier of the created step.
        

#### `def get_step(self, step_id: str) -> Step`

Get the step associated with the given identifier.

        Args:
            step_id: The identifier of the desired step.

        Returns:
            Step: The metadata of the requested step.
        

#### `def get_measurement(self, measurement_id: str) -> PublishedMeasurement`

Get the measurement associated with the given identifier.

        Args:
            measurement_id: The identifier of the desired measurement.

        Returns:
            PublishedMeasurement: The metadata of the requested measurement.
        

#### `def get_condition(self, condition_id: str) -> PublishedCondition`

Get the condition associated with the given identifier.

        Args:
            condition_id: The identifier of the desired condition.

        Returns:
            PublishedCondition: The metadata of the requested condition.
        

#### `def create_test_result(self, test_result: TestResult) -> str`

Create a test result object for publishing measurements.

        Once a test result is created, you can publish an arbitrary number of
        measurements and conditions to a step which is owned by the test result.

        Args:
            test_result: The metadata of the test result to be created.

        Returns:
            str: The test result ID. Generated if not specified in the request.
        

#### `def get_test_result(self, test_result_id: str) -> TestResult`

Get the test result associated with the given identifier.

        Args:
            test_result_id: The ID of the desired test result. This value is
                expected to be a parsable GUID.

        Returns:
            TestResult: The TestResult object that corresponds to the
                requested ID.
        

#### `def query_conditions(self, odata_query: str='') -> Sequence[PublishedCondition]`

Query conditions using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all conditions. $expand,
                $count, and $select are not supported. For more information,
                see https://learn.microsoft.com/en-us/odata/concepts/
                queryoptions-overview.

        Returns:
            Sequence[PublishedCondition]: The list of matching conditions. Each
                item contains an id for retrieving the condition
                measurements, as well as the metadata associated with the
                condition.
        

#### `def query_measurements(self, odata_query: str='') -> Sequence[PublishedMeasurement]`

Query measurements using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all measurements.
                $expand, $count, and $select are not supported. For more
                information, see https://learn.microsoft.com/en-us/odata/
                concepts/queryoptions-overview.

        Returns:
            Sequence[PublishedMeasurement]: The list of matching measurements.
                Each item contains an id for retrieving the measurement, as
                well as the metadata associated with the measurement.
        

#### `def query_test_results(self, odata_query: str='') -> Sequence[TestResult]`

Query test results using OData query syntax.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all test results.
                $expand, $count, and $select are not supported. For more
                information, see https://learn.microsoft.com/en-us/odata/
                concepts/queryoptions-overview.

        Returns:
            Sequence[TestResult]: The list of matching test results. Each
                item contains the metadata associated with the test result,
                including test result ID, name, timestamps, and other
                properties.
        

#### `def query_steps(self, odata_query: str='') -> Sequence[Step]`

Query for steps matching the given OData query.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". An empty string will return all steps. $expand,
                $count, and $select are not supported. For more information,
                see https://learn.microsoft.com/en-us/odata/concepts/
                queryoptions-overview.

        Returns:
            Sequence[Step]: The list of steps that match the query.
        

#### `def _get_data_store_client(self) -> DataStoreServiceClient`

#### `def _instantiate_data_store_client(self) -> DataStoreServiceClient`

#### `def _read_measurement(self, published_measurement: PublishedMeasurement) -> object`

#### `def _read_condition(self, published_condition: PublishedCondition) -> object`

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_grpc_conversion.py -->
## PYTHON MODULE: src/ni/datastore/data/_grpc_conversion.py

### MODULE DOCSTRING

Helper methods to convert between python and protobuf types.

### `def _copy_batch_values(repeated_field: Any, batch_values: Iterable[object], is_supported: Callable[[object], bool], convert_value: Callable[[Any], Any], error_message: str) -> None`

### `def _populate_vector_batch_values(publish_request: PublishMeasurementBatchRequest, values: Iterable[object]) -> None`

### `def _populate_analog_waveform_batch_values(publish_request: PublishMeasurementBatchRequest, first_value: AnalogWaveform[Any], values: Iterable[object]) -> None`

### `def _populate_complex_waveform_batch_values(publish_request: PublishMeasurementBatchRequest, first_value: ComplexWaveform[Any], values: Iterable[object]) -> None`

### `def _populate_spectrum_batch_values(publish_request: PublishMeasurementBatchRequest, first_value: Spectrum[Any], values: Iterable[object]) -> None`

### `def _populate_digital_waveform_batch_values(publish_request: PublishMeasurementBatchRequest, values: Iterable[object]) -> None`

### `def _populate_xydata_batch_values(publish_request: PublishMeasurementBatchRequest, first_value: XYData[Any], values: Iterable[object]) -> None`

### `def populate_publish_condition_request_value(publish_request: PublishConditionRequest, value: object) -> None`

Assign a value to the scalar member of PublishConditionRequest.

### `def populate_publish_condition_batch_request_values(publish_request: PublishConditionBatchRequest, values: object) -> None`

Assign a value to the scalar_values vector member of PublishConditionBatchRequest.

### `def populate_publish_measurement_request_value(publish_request: PublishMeasurementRequest, value: object) -> None`

Assign a value to the appropriate field of a PublishMeasurementRequest object.

### `def populate_publish_measurement_batch_request_values(publish_request: PublishMeasurementBatchRequest, values: object) -> None`

Assign a value to the appropriate field of the PublishMeasurementBatchRequest object.

### `def convert_read_measurement_response_from_protobuf(response: ReadMeasurementValueResponse) -> object`

Convert the value in the ReadMeasurementValueResponse from protobuf and return it.

### `def convert_read_condition_response_from_protobuf(response: ReadConditionValueResponse) -> object`

Convert the value in the ReadConditionValueResponse from protobuf and return it.

### `def convert_measurement_timestamp_to_protobuf(client_provided_timestamp: ht.datetime | None) -> PrecisionTimestamp | None`

Convert the provided timestamp to PrecisionTimestamp if it's not None.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/__init__.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/__init__.py

### MODULE DOCSTRING

Types for use in accessing the NI Data Store.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_error_information.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_error_information.py

### MODULE DOCSTRING

Error Information data type for the Data Store Client.

### `class ErrorInformation()`

Represents error or exception information in case of measurement failure.

    An ErrorInformation contains an error code, descriptive message, and
    source information to help identify and diagnose issues during measurement
    execution.
    

#### `def __init__(self, *, error_code: int=0, message: str='', source: str='') -> None`

Initialize an ErrorInformation instance.

        Args:
            error_code: The numeric error code associated with the error.
            message: A descriptive message explaining the error.
            source: The source or location where the error occurred.
        

#### `def from_protobuf(error_information_proto: ErrorInformationProto) -> 'ErrorInformation'`

Create an ErrorInformation instance from a protobuf ErrorInformation message.

#### `def to_protobuf(self) -> ErrorInformationProto`

Convert this ErrorInformation instance to a protobuf ErrorInformation message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the ErrorInformation.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_outcome.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_outcome.py

### MODULE DOCSTRING

Outcome data type for the Data Store Client.

### `class Outcome(IntEnum)`

Represents the outcome of a measurement or test operation.

    The Outcome enum indicates whether a measurement or test passed, failed,
    or had an indeterminate result.
    

#### `def from_protobuf(cls, outcome_proto: OutcomeProto.ValueType) -> 'Outcome'`

Create an Outcome instance from a protobuf Outcome value.

        Args:
            outcome_proto: The protobuf Outcome value.

        Returns:
            The corresponding Outcome enum value.

        Raises:
            ValueError: If the protobuf value doesn't correspond to a known Outcome.
        

#### `def to_protobuf(self) -> OutcomeProto.ValueType`

Convert this Outcome instance to a protobuf Outcome value.

        Returns:
            The corresponding protobuf Outcome value.
        

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_published_condition.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_published_condition.py

### MODULE DOCSTRING

Published Condition data type for the Data Store Client.

### `class PublishedCondition()`

Represents a condition that has been published to the data store.

    A published condition contains metadata about a condition value that was
    published, including an id for data retrieval and associated metadata
    like condition name, type, and associated step/test result IDs.
    

#### `def __init__(self, *, id: str='', name: str='', condition_type: str='', step_id: str='', test_result_id: str='') -> None`

Initialize a PublishedCondition instance.

        Args:
            id: The unique identifier of the condition. This
                can be used to reference and find the condition in the data store.
            name: The name of the condition.
            condition_type: The type of the condition. For example, "Setup" or
                "Environment".
            step_id: The ID of the step with which this condition is associated.
            test_result_id: The ID of the test result with which this condition
                is associated.
        

#### `def from_protobuf(published_condition_proto: PublishedConditionProto) -> 'PublishedCondition'`

Create a PublishedCondition instance from a protobuf PublishedCondition message.

#### `def to_protobuf(self) -> PublishedConditionProto`

Convert this PublishedCondition instance to a protobuf PublishedCondition message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the PublishedCondition.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_published_measurement.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_published_measurement.py

### MODULE DOCSTRING

Published Measurement data type for the Data Store Client.

### `class PublishedMeasurement()`

Represents a measurement that has been published to the data store.

    A published measurement contains the measurement data and the associated
    metadata (name, type, timestamps, outcome, hardware, software, and test
    adapter IDs).
    

#### `def published_conditions(self) -> MutableSequence[PublishedCondition]`

The published conditions associated with the published measurement.

#### `def software_item_ids(self) -> MutableSequence[str]`

The software item IDs associated with the published measurement.

#### `def hardware_item_ids(self) -> MutableSequence[str]`

The hardware item IDs associated with the published measurement.

#### `def test_adapter_ids(self) -> MutableSequence[str]`

The test adapter IDs associated with the published measurement.

#### `def __init__(self, *, published_conditions: Iterable[PublishedCondition] | None=None, id: str='', test_result_id: str='', step_id: str='', software_item_ids: Iterable[str] | None=None, hardware_item_ids: Iterable[str] | None=None, test_adapter_ids: Iterable[str] | None=None, name: str='', value_type: str='', notes: str='', start_date_time: ht.datetime | None=None, end_date_time: ht.datetime | None=None, outcome: Outcome=Outcome.UNSPECIFIED, parametric_index: int=0, error_information: ErrorInformation | None=None) -> None`

Initialize a PublishedMeasurement instance.

        Args:
            published_conditions: The published conditions associated with this
                measurement from the test step.
            id: The unique identifier of the measurement.
                This can be used to reference and find the measurement in the
                data store.
            test_result_id: The ID of the test result with which this
                measurement is associated.
            step_id: The ID of the step with which this measurement is
                associated.
            software_item_ids: The IDs of the software items associated with
                this measurement.
            hardware_item_ids: The IDs of the hardware items associated with
                this measurement.
            test_adapter_ids: The IDs of the test adapters associated with this
                measurement.
            name: The name of the measurement.
            value_type: The data type of the measurement value.
            notes: Additional notes or comments about the
                measurement.
            start_date_time: The start timestamp of the measurement.
            end_date_time: The end timestamp of the measurement.
            outcome: The outcome of the measurement (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).
            parametric_index: The index of this measurement in a parametric
                sweep operation.
            error_information: Error or exception information in case of
                measurement failure.
        

#### `def from_protobuf(published_measurement_proto: PublishedMeasurementProto) -> 'PublishedMeasurement'`

Create a PublishedMeasurement instance from a protobuf PublishedMeasurement message.

#### `def to_protobuf(self) -> PublishedMeasurementProto`

Convert this PublishedMeasurement instance to a protobuf PublishedMeasurement message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the PublishedMeasurement.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_step.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_step.py

### MODULE DOCSTRING

Step data type for the Data Store Client.

### `class Step()`

Information about a step into which measurements and conditions are published.

    Represents a hierarchical execution step within a test result that can
    contain measurements and conditions. Steps are linked to a test result and
    can be organized into hierarchical structures using parent_step_id. Each
    step has test execution time, metadata, and optional extensions for custom
    metadata.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the step.

#### `def __init__(self, name: str, *, id: str='', parent_step_id: str='', test_result_id: str='', test_id: str='', step_type: str='', notes: str='', start_date_time: ht.datetime | None=None, end_date_time: ht.datetime | None=None, link: str='', extension: Mapping[str, str] | None=None, schema_id: str='', error_information: ErrorInformation | None=None, outcome: Outcome=Outcome.UNSPECIFIED) -> None`

Initialize a Step instance.

        Args:
            name: Human-readable name of the step.
            id (optional): Unique identifier for the step.
            parent_step_id (optional): ID of the parent step if this is a nested step.
            test_result_id (optional): ID of the test result this step belongs to.
            test_id (optional): ID of the test associated with this step.
            step_type (optional): Type or category of the step.
            notes (optional): Additional notes or comments about the step.
            start_date_time (optional): The start date and time of the step execution.
            end_date_time (optional): The end date and time of the step execution.
            link (optional): Optional link to external resources for this step.
            extension (optional): Additional extension attributes as key-value pairs.
            schema_id (optional): ID of the extension schema for validating extensions.
            error_information (optional): Error or exception information in case of
                step failure.
            outcome (optional): The outcome of the step (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).
        

#### `def from_protobuf(step_proto: StepProto) -> 'Step'`

Create a Step instance from a protobuf Step message.

#### `def to_protobuf(self) -> StepProto`

Convert this Step to a protobuf Step message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the Step.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/data/_types/_test_result.py -->
## PYTHON MODULE: src/ni/datastore/data/_types/_test_result.py

### MODULE DOCSTRING

Test Result data type for the Data Store Client.

### `class TestResult()`

Information about a test result.

    Represents the results of executing a test sequence, including metadata
    about the execution environment (UUT, operator, test station), test
    execution time, outcome, and associations with hardware/software components
    and test adapters. Each step which references measurement data and
    conditions is associated with a test result.
    

#### `def software_item_ids(self) -> MutableSequence[str]`

The software item IDs associated with the test result.

#### `def hardware_item_ids(self) -> MutableSequence[str]`

The hardware item IDs associated with the test result.

#### `def test_adapter_ids(self) -> MutableSequence[str]`

The test adapter IDs associated with the test result.

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the test result.

#### `def __init__(self, name: str, *, id: str='', uut_instance_id: str='', operator_id: str='', test_station_id: str='', test_description_id: str='', software_item_ids: Iterable[str] | None=None, hardware_item_ids: Iterable[str] | None=None, test_adapter_ids: Iterable[str] | None=None, start_date_time: ht.datetime | None=None, end_date_time: ht.datetime | None=None, outcome: Outcome=Outcome.UNSPECIFIED, link: str='', extension: Mapping[str, str] | None=None, schema_id: str='', error_information: ErrorInformation | None=None) -> None`

Initialize a TestResult instance.

        Args:
            name: Human-readable name for the test result.
            id (optional): Unique identifier for the test result.
            uut_instance_id (optional): ID of the UUT instance that was tested.
            operator_id (optional): ID of the operator who ran the test.
            test_station_id (optional): ID of the test station used.
            test_description_id (optional): ID of the test description that was executed.
            software_item_ids (optional): IDs of software items used in the test.
            hardware_item_ids (optional): IDs of hardware items used in the test.
            test_adapter_ids (optional): IDs of test adapters used in the test.
            start_date_time (optional): The start date and time of the test execution.
            end_date_time (optional): The end date and time of the test execution.
            outcome (optional): The outcome of the test execution (PASSED, FAILED,
                INDETERMINATE, or UNSPECIFIED).
            link (optional): Optional link to external resources for this test result.
            extension (optional): Additional extension attributes as key-value pairs.
            schema_id (optional): ID of the extension schema for validating extensions.
            error_information (optional): Error or exception information in case of
                test result failure.
        

#### `def from_protobuf(test_result_proto: TestResultProto) -> 'TestResult'`

Create a TestResult instance from a protobuf TestResult message.

#### `def to_protobuf(self) -> TestResultProto`

Convert this TestResult to a protobuf TestResult message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the TestResult.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/__init__.py -->
## PYTHON MODULE: src/ni/datastore/metadata/__init__.py

### MODULE DOCSTRING

Public API for accessing the NI Metadata Store.

- `__all__ = ['Alias', 'AliasTargetType', 'ExtensionSchema', 'HardwareItem', 'MetadataItems', 'MetadataStoreClient', 'Operator', 'SoftwareItem', 'Test', 'TestAdapter', 'TestDescription', 'TestStation', 'Uut', 'UutInstance']`

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_grpc_conversion.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_grpc_conversion.py

### MODULE DOCSTRING

Helper methods to convert between python and protobuf types.

### `def populate_extension_value_message_map(destination: MessageMap[str, ExtensionValue], source: MutableMapping[str, str]) -> None`

Populate a gRPC message map of string keys to ExtensionValue.

    The input is a mapping of string keys to string values.
    

### `def populate_from_extension_value_message_map(destination: MutableMapping[str, str], source: MessageMap[str, ExtensionValue]) -> None`

Populate a mapping of string keys to stringvalues.

    The input is a gRPC message map of string keys to ExtensionValue.
    

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_metadata_store_client.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_metadata_store_client.py

### MODULE DOCSTRING

Metadata store client for publishing and reading metadata.

### `class MetadataStoreClient()`

Metadata store client for publishing and reading metadata.

#### `def __init__(self, discovery_client: DiscoveryClient | None=None, grpc_channel: Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None) -> None`

Initialize the MetadataStoreClient.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional metadata store gRPC channel. Providing this channel
                will bypass discovery service resolution of the metadata store.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        

#### `def __enter__(self) -> Self`

Enter the runtime context of the metadata store client.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the runtime context of the metadata store client.

#### `def close(self) -> None`

Close the metadata store client and clean up resources that it owns.

#### `def create_uut_instance(self, uut_instance: UutInstance) -> str`

Create a new UUT instance in the metadata store.

        Args:
            uut_instance: The metadata of the UUT instance to be created.

        Returns:
            str: The identifier of the created UUT instance.
        

#### `def get_uut_instance(self, uut_instance_id: str) -> UutInstance`

Get the UUT instance associated with the given identifier.

        Args:
            uut_instance_id: The identifier of the desired UUT instance.

        Returns:
            UutInstance: The metadata of the requested UUT instance.
        

#### `def query_uut_instances(self, odata_query: str='') -> Sequence[UutInstance]`

Perform an OData query on UUT instances.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[UutInstance]: The list of UUT instances that match the
                query.
        

#### `def create_uut(self, uut: Uut) -> str`

Create a new UUT in the metadata store.

        Args:
            uut: The metadata of the UUT to be created.

        Returns:
            str: The identifier of the created UUT.
        

#### `def get_uut(self, uut_id: str) -> Uut`

Get the UUT associated with the given identifier.

        Args:
            uut_id: The identifier of the desired UUT.

        Returns:
            Uut: The metadata of the requested UUT.
        

#### `def query_uuts(self, odata_query: str='') -> Sequence[Uut]`

Perform an OData query on UUTs.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Uut]: The list of UUTs that match the query.
        

#### `def create_operator(self, operator: Operator) -> str`

Create a new operator in the metadata store.

        Args:
            operator: The metadata of the operator to be created.

        Returns:
            str: The identifier of the created operator.
        

#### `def get_operator(self, operator_id: str) -> Operator`

Get the operator associated with the given identifier.

        Args:
            operator_id: The identifier of the desired operator.

        Returns:
            Operator: The metadata of the requested operator.
        

#### `def query_operators(self, odata_query: str='') -> Sequence[Operator]`

Perform an OData query on operators.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Operator]: The list of operators that match the query.
        

#### `def create_test_description(self, test_description: TestDescription) -> str`

Create a test description in the metadata store.

        Args:
            test_description: The metadata of the test description to be created.

        Returns:
            str: The identifier of the created test description.
        

#### `def get_test_description(self, test_description_id: str) -> TestDescription`

Get a test description from the metadata store.

        Args:
            test_description_id: The identifier of the desired test description.

        Returns:
            TestDescription: The metadata of the requested test description.
        

#### `def query_test_descriptions(self, odata_query: str='') -> Sequence[TestDescription]`

Query test descriptions from the metadata store.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[TestDescription]: The list of test descriptions that match
                the query.
        

#### `def create_test(self, test: Test) -> str`

Create a test in the metadata store.

        Args:
            test: The metadata of the test to be created.

        Returns:
            str: The identifier of the created test.
        

#### `def get_test(self, test_id: str) -> Test`

Get a test from the metadata store.

        Args:
            test_id: The identifier of the desired test.

        Returns:
            Test: The metadata of the requested test.
        

#### `def query_tests(self, odata_query: str='') -> Sequence[Test]`

Query tests from the metadata store.

#### `def create_test_station(self, test_station: TestStation) -> str`

Create a test station in the metadata store.

        Args:
            test_station: The metadata of the test station to be created.

        Returns:
            str: The identifier of the created test station.
        

#### `def get_test_station(self, test_station_id: str) -> TestStation`

Get a test station from the metadata store.

        Args:
            test_station_id: The identifier of the desired test station.

        Returns:
            TestStation: The metadata of the requested test station.
        

#### `def query_test_stations(self, odata_query: str='') -> Sequence[TestStation]`

Query test stations from the metadata store.

#### `def create_hardware_item(self, hardware_item: HardwareItem) -> str`

Create a hardware item in the metadata store.

        Args:
            hardware_item: The metadata of the hardware item to be created.

        Returns:
            str: The identifier of the created hardware item.
        

#### `def get_hardware_item(self, hardware_item_id: str) -> HardwareItem`

Get a hardware item from the metadata store.

        Args:
            hardware_item_id: The identifier of the desired hardware item.

        Returns:
            HardwareItem: The metadata of the requested hardware item.
        

#### `def query_hardware_items(self, odata_query: str='') -> Sequence[HardwareItem]`

Query hardware items from the metadata store.

#### `def create_software_item(self, software_item: SoftwareItem) -> str`

Create a software item in the metadata store.

        Args:
            software_item: The metadata of the software item to be created.

        Returns:
            str: The identifier of the created software item.
        

#### `def get_software_item(self, software_item_id: str) -> SoftwareItem`

Get a software item from the metadata store.

        Args:
            software_item_id: The identifier of the desired software item.

        Returns:
            SoftwareItem: The metadata of the requested software item.
        

#### `def query_software_items(self, odata_query: str='') -> Sequence[SoftwareItem]`

Query software items from the metadata store.

#### `def create_test_adapter(self, test_adapter: TestAdapter) -> str`

Create a test adapter in the metadata store.

        Args:
            test_adapter: The metadata of the test adapter to be created.

        Returns:
            str: The identifier of the created test adapter.
        

#### `def get_test_adapter(self, test_adapter_id: str) -> TestAdapter`

Get a test adapter from the metadata store.

        Args:
            test_adapter_id: The identifier of the desired test adapter.

        Returns:
            TestAdapter: The metadata of the requested test adapter.
        

#### `def query_test_adapters(self, odata_query: str='') -> Sequence[TestAdapter]`

Query test adapters from the metadata store.

#### `def register_schema_from_file(self, schema_file_path: Path | str) -> str`

Register a schema obtained from the specified file in the metadata store.

        Args:
            schema_file_path: The path at which the schema file is located

        Raises:
            FileNotFoundError: If the schema file does not exist.
        

#### `def register_schema(self, schema_contents: str) -> str`

Register a schema in the metadata store.

        Once a schema has been published, it cannot be modified or removed.

        Args:
            schema_contents: The contents of the JSON or TOML schema. This
                should be a well-formed JSON or TOML schema. Validation will
                be performed, and an error will be returned if the schema is
                not valid.

        Returns:
            str: The ID of the schema.
        

#### `def list_schemas(self) -> Sequence[ExtensionSchema]`

List the schemas that have been previously registered.

        Returns:
            Sequence[ExtensionSchema]: The list of registered schemas.
        

#### `def get_alias(self, alias_name: str) -> Alias`

Get an alias and its target (the underlying metadata it represents).

        Args:
            alias_name: The name of the alias to retrieve.

        Returns:
            Alias: The alias containing the alias name, target type, and
                target ID of the underlying metadata.
        

#### `def query_aliases(self, odata_query: str='') -> Sequence[Alias]`

Perform an OData query on the registered aliases.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Alias]: The list of aliases that match the query.
        

#### `def create_alias(self, alias_name: str, alias_target: UutInstance | Uut | HardwareItem | SoftwareItem | Operator | TestDescription | Test | TestAdapter | TestStation) -> Alias`

Create (register) an alias of the specified metadata.

        The specified metadata must have already been created prior to the
        alias registration. This method may be called with an already
        registered alias name in order to update the target mapped for that
        existing alias.

        Args:
            alias_name: The alias name to register.

            alias_target: The metadata instance to alias. The metadata
                instance to alias must have already been created in the
                metadata store in order to register an alias for it.

        Returns:
            Alias: The created alias containing the alias name, target type,
                and target ID.
        

#### `def delete_alias(self, alias_name: str) -> bool`

Remove a registered alias.

        Args:
            alias_name: The name of the alias to unregister.

        Returns:
            bool: Whether the action resulted in the specified alias becoming
                unregistered. False if the alias does not exist.
        

#### `def create_from_json_file(self, metadata_file_path: Path | str) -> MetadataItems`

Create metadata items from a JSON file.

        Args:
            metadata_file_path: The path to the JSON file containing metadata definitions.

        Returns:
            MetadataItems: A collection of metadata items created from the JSON document.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
        

#### `def create_from_json(self, metadata_file_contents: str) -> MetadataItems`

Create metadata items from a JSON document.

        Args:
            metadata_file_contents: The JSON document content containing metadata definitions.

        Returns:
            MetadataItems: A collection of metadata items created from the JSON document.
        

#### `def _get_metadata_store_client(self) -> MetadataStoreServiceClient`

#### `def _instantiate_metadata_store_client(self) -> MetadataStoreServiceClient`

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/__init__.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/__init__.py

### MODULE DOCSTRING

Types for use in accessing the NI Metadata Store.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_alias.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_alias.py

### MODULE DOCSTRING

Alias data type for the Data Store Client.

### `class Alias()`

Represents an alias for metadata.

    An alias provides a user-friendly name that maps to a specific metadata
    instance, containing the alias name, the type of the aliased metadata
    instance, and the unique identifier for the aliased metadata instance.
    

#### `def __init__(self, *, name: str='', target_type: AliasTargetType=AliasTargetType.UNSPECIFIED, target_id: str='') -> None`

Initialize an Alias instance.

        Args:
            name: The registered alias name for the aliased metadata
                instance.
            target_type: The type of the aliased metadata instance.
            target_id: The unique identifier for the aliased metadata instance.
        

#### `def from_protobuf(alias_proto: AliasProto) -> 'Alias'`

Create an Alias instance from a protobuf Alias message.

#### `def to_protobuf(self) -> AliasProto`

Convert this Alias to a protobuf Alias message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the Alias.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_alias_target_type.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_alias_target_type.py

### MODULE DOCSTRING

AliasTargetType data type for the Data Store Client.

### `class AliasTargetType(IntEnum)`

Represents the type of target that an alias can reference.

    The AliasTargetType enum indicates what kind of metadata entity
    an alias is pointing to.
    

#### `def from_protobuf(cls, alias_target_type_proto: AliasTargetTypeProto.ValueType) -> 'AliasTargetType'`

Create an AliasTargetType instance from a protobuf AliasTargetType value.

        Args:
            alias_target_type_proto: The protobuf AliasTargetType value.

        Returns:
            The corresponding AliasTargetType enum value.

        Raises:
            ValueError: If the protobuf value doesn't correspond to a known AliasTargetType.
        

#### `def to_protobuf(self) -> AliasTargetTypeProto.ValueType`

Convert this AliasTargetType instance to a protobuf AliasTargetType value.

        Returns:
            The corresponding protobuf AliasTargetType value.
        

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_extension_schema.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_extension_schema.py

### MODULE DOCSTRING

Extension Schema data type for the Data Store Client.

### `class ExtensionSchema()`

Represents an extension schema stored in the system.

    An extension schema contains the schema ID and the schema definition
    itself, which can be used to validate extension data in metadata instances.
    

#### `def __init__(self, *, id: str='', schema: str='') -> None`

Initialize an ExtensionSchema instance.

        Args:
            id: The ID of the schema.
            schema: The schema itself.
        

#### `def from_protobuf(extension_schema_proto: ExtensionSchemaProto) -> 'ExtensionSchema'`

Create an ExtensionSchema instance from a protobuf ExtensionSchema message.

#### `def to_protobuf(self) -> ExtensionSchemaProto`

Convert this ExtensionSchema to a protobuf ExtensionSchema message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the ExtensionSchema.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_hardware_item.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_hardware_item.py

### MODULE DOCSTRING

Hardware Item data type for the Data Store Client.

### `class HardwareItem()`

Represents the metadata of a hardware item used to take measurements.

    A hardware item contains information about physical test equipment
    including manufacturer, model, serial number, calibration dates, and asset
    tracking information.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the hardware item.

#### `def id(self) -> str`

The string id of the hardware item.

#### `def __init__(self, *, manufacturer: str='', model: str='', serial_number: str='', part_number: str='', asset_identifier: str='', calibration_due_date: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a HardwareItem instance.

        Args:
            manufacturer: The manufacturer of the hardware item.
            model: The model of the hardware item.
            serial_number: The serial number of the hardware item.
            part_number: The part number of the hardware item.
            asset_identifier: The asset identifier of the hardware item.
            calibration_due_date: The calibration due date of the hardware item.
            link: A link to a resource that describes the hardware item. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the hardware item.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the hardware item
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(hardware_item_proto: HardwareItemProto) -> 'HardwareItem'`

Create a HardwareItem instance from a protobuf HardwareItem message.

#### `def to_protobuf(self) -> HardwareItemProto`

Convert this HardwareItem to a protobuf HardwareItem message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the HardwareItem.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_metadata_items.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_metadata_items.py

### MODULE DOCSTRING

MetadataItems data type for the Data Store Client.

### `class MetadataItems()`

Represents a collection of metadata items created from a JSON document.

    This class contains the results of creating metadata items from a JSON document,
    organizing them by type for easy access.
    

#### `def __init__(self, *, uut_instances: Sequence[UutInstance]=(), uuts: Sequence[Uut]=(), operators: Sequence[Operator]=(), test_descriptions: Sequence[TestDescription]=(), tests: Sequence[Test]=(), test_stations: Sequence[TestStation]=(), hardware_items: Sequence[HardwareItem]=(), software_items: Sequence[SoftwareItem]=(), test_adapters: Sequence[TestAdapter]=()) -> None`

Initialize a MetadataItems instance.

        Args:
            uut_instances: A sequence of UUT instances created from the JSON document.
            uuts: A sequence of UUTs created from the JSON document.
            operators: A sequence of operators created from the JSON document.
            test_descriptions: A sequence of test descriptions created from the JSON document.
            tests: A sequence of tests created from the JSON document.
            test_stations: A sequence of test stations created from the JSON document.
            hardware_items: A sequence of hardware items created from the JSON document.
            software_items: A sequence of software items created from the JSON document.
            test_adapters: A sequence of test adapters created from the JSON document.
        

#### `def from_protobuf(response: CreateFromJsonDocumentResponse) -> 'MetadataItems'`

Create a MetadataItems instance from a protobuf CreateFromJsonDocumentResponse.

        Args:
            response: The protobuf response containing the created metadata items.

        Returns:
            MetadataItems: A new MetadataItems instance with all the created items.
        

#### `def __eq__(self, other: object) -> bool`

Determine equality between MetadataItems instances.

#### `def __str__(self) -> str`

Return a string representation of the MetadataItems.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_operator.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_operator.py

### MODULE DOCSTRING

Operator data type for the Data Store Client.

### `class Operator()`

Represents the metadata of the operator that took the test step.

    An operator contains information about the person or entity responsible for
    conducting tests, including their name and role.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the operator.

#### `def id(self) -> str`

The string id of the operator.

#### `def __init__(self, *, name: str='', role: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize an Operator instance.

        Args:
            name: The name of the operator.
            role: The role of the operator.
            link: A link to a resource that describes the operator. This value
                is expected to be a valid URI.
            extension: Any extensions to be associated with the operator.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the operator is
                created within the context of a test result, in which case the
                test result must have a schema_id.
        

#### `def from_protobuf(operator_proto: OperatorProto) -> 'Operator'`

Create an Operator instance from a protobuf Operator message.

#### `def to_protobuf(self) -> OperatorProto`

Convert this Operator to a protobuf Operator message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the Operator.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_software_item.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_software_item.py

### MODULE DOCSTRING

Software Item data type for the Data Store Client.

### `class SoftwareItem()`

Represents the metadata of the software item used to take measurements.

    A software item contains information about the software product and version
    used during testing.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the software item.

#### `def id(self) -> str`

The string id of the software item.

#### `def __init__(self, *, product: str='', version: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a SoftwareItem instance.

        Args:
            product: The product name of the software item.
            version: The version of the software item.
            link: A link to a resource that describes the software item. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the software item.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the software item
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(software_item_proto: SoftwareItemProto) -> 'SoftwareItem'`

Create a SoftwareItem instance from a protobuf SoftwareItem message.

#### `def to_protobuf(self) -> SoftwareItemProto`

Convert this SoftwareItem to a protobuf SoftwareItem message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the SoftwareItem.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_test.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_test.py

### MODULE DOCSTRING

Test data type for the Data Store Client.

### `class Test()`

Represents the metadata of a test.

    A test contains information about a specific test procedure, including its
    name and description of what the test does.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the test.

#### `def id(self) -> str`

The string id of the test.

#### `def __init__(self, *, name: str='', description: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a Test instance.

        Args:
            name: The name of the test.
            description: A description of what the test does.
            link: A link to a resource that describes the test. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the test.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the test
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(test_proto: TestProto) -> 'Test'`

Create a Test instance from a protobuf Test message.

#### `def to_protobuf(self) -> TestProto`

Convert this Test to a protobuf Test message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the Test.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_test_adapter.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_test_adapter.py

### MODULE DOCSTRING

Test Adapter data type for the Data Store Client.

### `class TestAdapter()`

Represents a test adapter or mechanical setup.

    This is a board or device that is used to hold, connect, or interface the
    UUT with the test system. Test adapters may also be referred to as test
    fixtures, interface boards, breakout boxes, mechanical fixtures, or
    connection adapters.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the test adapter.

#### `def id(self) -> str`

The string id of the test adapter.

#### `def __init__(self, *, name: str='', manufacturer: str='', model: str='', serial_number: str='', part_number: str='', asset_identifier: str='', calibration_due_date: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a TestAdapter instance.

        Args:
            name: The name of the test adapter.
            manufacturer: The manufacturer of the test adapter.
            model: The model of the test adapter.
            serial_number: The serial number of the test adapter.
            part_number: The part number of the test adapter.
            asset_identifier: The asset identifier of the test adapter.
            calibration_due_date: The calibration due date of the test adapter.
            link: A link to a resource that describes the test adapter. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the test adapter.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the test adapter
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(test_adapter_proto: TestAdapterProto) -> 'TestAdapter'`

Create a TestAdapter instance from a protobuf TestAdapter message.

#### `def to_protobuf(self) -> TestAdapterProto`

Convert this TestAdapter to a protobuf TestAdapter message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the TestAdapter.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_test_description.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_test_description.py

### MODULE DOCSTRING

Test Description data type for the Data Store Client.

### `class TestDescription()`

Represents the metadata of a test description.

    A test description contains information about a test procedure designed for
    a specific UUT, including the UUT ID and test description name.
    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the test description.

#### `def id(self) -> str`

The string id of the test description.

#### `def __init__(self, *, uut_id: str='', name: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a TestDescription instance.

        Args:
            uut_id: The ID of the UUT associated with this test description.
                This value is expected to be a parsable GUID or an alias.
            name: The name of the test description.
            link: A link to a resource that describes the test description. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the test description.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the test description
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(test_description_proto: TestDescriptionProto) -> 'TestDescription'`

Create a TestDescription instance from a protobuf TestDescription message.

#### `def to_protobuf(self) -> TestDescriptionProto`

Convert this TestDescription to a protobuf TestDescription message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the TestDescription.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_test_station.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_test_station.py

### MODULE DOCSTRING

Test Station data type for the Data Store Client.

### `class TestStation()`

Represents the metadata of a test station.

    A test station contains information about the physical location or setup
    where testing is performed, including its name and asset identifier for
    tracking and inventory purposes.


    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the test station.

#### `def id(self) -> str`

The string id of the test station.

#### `def __init__(self, *, name: str='', asset_identifier: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a TestStation instance.

        Args:
            name: The name of the test station.
            asset_identifier: The asset identifier of the test station.
            link: A link to a resource that describes the test station. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the test station.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the test station
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(test_station_proto: TestStationProto) -> 'TestStation'`

Create a TestStation instance from a protobuf TestStation message.

#### `def to_protobuf(self) -> TestStationProto`

Convert this TestStation to a protobuf TestStation message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the TestStation.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_uut.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_uut.py

### MODULE DOCSTRING

UUT data type for the Data Store Client.

### `class Uut()`

Represents the metadata of a Unit Under Test (UUT).

    A UUT represents a model or type of device that can be tested, containing
    information like model name, family, manufacturers, and part number that
    describe the UUT type rather than specific instances.


    

#### `def manufacturers(self) -> MutableSequence[str]`

The manufacturers of the UUT.

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the UUT.

#### `def id(self) -> str`

The string id of the uut.

#### `def __init__(self, *, model_name: str='', family: str='', manufacturers: Iterable[str] | None=None, part_number: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a Uut instance.

        Args:
            model_name: The name of the UUT model.
            family: The UUT family.
            manufacturers: List of manufacturers of the UUT.
            part_number: The part number of the UUT.
            link: A link to a resource that describes the UUT. This value is
                expected to be a valid URI.
            extension: Any extensions to be associated with the UUT.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the UUT is
                created within the context of a test result, in which case the
                test result must have a schema_id.
        

#### `def from_protobuf(uut_proto: UutProto) -> 'Uut'`

Create a Uut instance from a protobuf Uut message.

#### `def to_protobuf(self) -> UutProto`

Convert this Uut to a protobuf Uut message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the Uut.

<!--NI_PYTHON_API repo=datastore-python path=src/ni/datastore/metadata/_types/_uut_instance.py -->
## PYTHON MODULE: src/ni/datastore/metadata/_types/_uut_instance.py

### MODULE DOCSTRING

UUT Instance data type for the Data Store Client.

### `class UutInstance()`

Represents the metadata of a UUT instance.

    A UUT instance represents a specific physical instance of a Unit Under
    Test, with properties like serial number, manufacture date, and firmware
    version that distinguish it from other instances of the same UUT model.


    

#### `def extension(self) -> MutableMapping[str, str]`

The extension of the UUT instance.

#### `def id(self) -> str`

The string id of the uut instance.

#### `def __init__(self, *, uut_id: str='', serial_number: str='', manufacture_date: str='', firmware_version: str='', hardware_version: str='', link: str='', extension: Mapping[str, str] | None=None, schema_id: str='') -> None`

Initialize a UutInstance instance.

        Args:
            uut_id: The ID of the UUT associated with this UUT instance. This
                value is expected to be a parsable GUID or an alias.
            serial_number: The serial number of the UUT instance.
            manufacture_date: The date the UUT instance was manufactured.
            firmware_version: Version of the firmware on the UUT instance.
            hardware_version: Hardware version of the UUT instance.
            link: A link to a resource that describes the UUT instance. This
                value is expected to be a valid URI.
            extension: Any extensions to be associated with the UUT instance.
            schema_id: The unique identifier of the schema that applies to this
                instance's extension. If any extension is associated with this
                instance, a schema_id must be provided, unless the UUT instance
                is created within the context of a test result, in which case
                the test result must have a schema_id.
        

#### `def from_protobuf(uut_instance_proto: UutInstanceProto) -> 'UutInstance'`

Create a UutInstance from a protobuf UutInstance message.

#### `def to_protobuf(self) -> UutInstanceProto`

Convert this UutInstance to a protobuf UutInstance message.

#### `def __eq__(self, other: object) -> bool`

Determine equality.

#### `def __str__(self) -> str`

Return a string representation of the UutInstance.

<!--NI_PYTHON_API repo=datastore-python path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/__init__.py -->
## PYTHON MODULE: tests/acceptance/__init__.py

### MODULE DOCSTRING

Acceptance Tests.

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/_utils.py -->
## PYTHON MODULE: tests/acceptance/_utils.py

### MODULE DOCSTRING

Acceptance test utility functions.

### `def create_test_result_and_step(data_store_client: DataStoreClient, description: str) -> str`

Create a single step within a single test result and return the step_id.

### `def create_test_result(data_store_client: DataStoreClient, description: str) -> str`

Create a single TestResult and return that test result's id.

### `def append_hashed_time(base_string: str) -> str`

Append the hash of the current time to a given string.

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/conftest.py -->
## PYTHON MODULE: tests/acceptance/conftest.py

### MODULE DOCSTRING

Contains test fixtures used by the data store and metadata store acceptance tests.

### `def acceptance_test_context() -> Generator[DataStoreContext, None, None]`

Returns the pytest fixture for launching the data store in a testing context.

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_publish_condition_and_read_data.py -->
## PYTHON MODULE: tests/acceptance/test_publish_condition_and_read_data.py

### MODULE DOCSTRING

Acceptance tests that publish various condition values then read the data back.

### `def test___publish_float_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_integer_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_bool_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_str_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_scalar_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_publish_condition_batch_and_read_data.py -->
## PYTHON MODULE: tests/acceptance/test_publish_condition_batch_and_read_data.py

### MODULE DOCSTRING

Acceptance tests that publish various batch condition values then read the data back.

### `def test___publish_batch_float_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_integer_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_bool_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_str_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_vector_condition___read_condition_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_publish_measurement_and_read_data.py -->
## PYTHON MODULE: tests/acceptance/test_publish_measurement_and_read_data.py

### MODULE DOCSTRING

Acceptance tests that publish various values then reads the data back.

### `def test___publish_float___read_measurement_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_scalar___read_measurement_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_xydata___read_measurement_value_returns_xydata(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_spectrum___read_measurement_value_returns_spectrum(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_analog_waveform___read_measurement_value_returns_analog_waveform(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_digital_waveform___read_measurement_value_returns_digital_waveform(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_complex_waveform___read_measurement_value_returns_complex_waveform(acceptance_test_context: DataStoreContext) -> None`

### `def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_publish_measurement_batch_and_read_data.py -->
## PYTHON MODULE: tests/acceptance/test_publish_measurement_batch_and_read_data.py

### MODULE DOCSTRING

Acceptance tests that publish various batch measurement values then reads the data back.

### `def test___publish_batch_floats___read_measurement_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_vector___read_measurement_value_returns_vector(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_double_analog_waveforms___read_measurement_value_returns_each_analog_waveform(acceptance_test_context: DataStoreContext) -> None`

### `def test___publish_batch_vectors___read_measurement_value_returns_each_vector(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_publish_with_metadata.py -->
## PYTHON MODULE: tests/acceptance/test_publish_with_metadata.py

### MODULE DOCSTRING

Acceptance test that publishes then queries waveform data and metadata.

### `def test___waveform_with_all_metadata___publish___query_read_returns_correct_data(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_query_conditions.py -->
## PYTHON MODULE: tests/acceptance/test_query_conditions.py

### MODULE DOCSTRING

Acceptance tests that exercise DataStoreClient.query_conditions().

### `def test___query_conditions___filter_by_id___single_condition_returned(acceptance_test_context: DataStoreContext) -> None`

### `def test___query_conditions___filter_by_name___correct_conditions_returned(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_query_measurements.py -->
## PYTHON MODULE: tests/acceptance/test_query_measurements.py

### MODULE DOCSTRING

Acceptance tests that exercise DataStoreClient.query_measurements().

### `def test___query_measurements___filter_by_id___single_measurement_returned(acceptance_test_context: DataStoreContext) -> None`

### `def test___query_measurements___filter_by_name___correct_measurements_returned(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_query_steps.py -->
## PYTHON MODULE: tests/acceptance/test_query_steps.py

### MODULE DOCSTRING

Acceptance tests that exercise DataStoreClient.query_steps().

### `def test___query_steps___filter_by_id___single_step_returned(acceptance_test_context: DataStoreContext) -> None`

### `def test___query_steps___filter_by_name___correct_steps_returned(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/acceptance/test_query_test_results.py -->
## PYTHON MODULE: tests/acceptance/test_query_test_results.py

### MODULE DOCSTRING

Acceptance tests that exercise DataStoreClient.query_test_results().

### `def test___query_test_results___filter_by_id___single_test_result_returned(acceptance_test_context: DataStoreContext) -> None`

### `def test___query_steps___filter_by_name___correct_steps_returned(acceptance_test_context: DataStoreContext) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/__init__.py -->
## PYTHON MODULE: tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/conftest.py -->
## PYTHON MODULE: tests/unit/conftest.py

### MODULE DOCSTRING

Contains test fixtures used by the data store and metadata store unit tests.

### `def data_store_client(mocked_data_store_service_client: NonCallableMock, mocker: MockerFixture) -> DataStoreClient`

Returns the pytest fixture for the data store client.

### `def metadata_store_client(mocked_metadata_store_service_client: NonCallableMock, mocker: MockerFixture) -> MetadataStoreClient`

Returns the pytest fixture for the metadata store client.

### `def mocked_data_store_service_client(mocker: MockerFixture) -> Any`

Returns the pytest fixture for a mocked data store service client.

### `def mocked_metadata_store_service_client(mocker: MockerFixture) -> Any`

Returns the pytest fixture for a mocked metadata store service client.

### `def schemas_directory(test_assets_directory: Path) -> Path`

Returns the test assets directory containing schemas.

### `def test_assets_directory() -> Path`

Returns the test assets directory.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/__init__.py -->
## PYTHON MODULE: tests/unit/data/__init__.py

### MODULE DOCSTRING

Unit tests for data.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_close_client.py -->
## PYTHON MODULE: tests/unit/data/test_close_client.py

### MODULE DOCSTRING

Contains tests related to closing the DataStoreClient.

### `def test___exit_data_store_client_context___calls_close_on_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___close_data_store_client___calls_close_on_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___exit_data_store_client_context___call_method___raises_error(data_store_client: DataStoreClient) -> None`

### `def test___close_data_store_client___call_method___raises_error(data_store_client: DataStoreClient) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_create_metadata.py -->
## PYTHON MODULE: tests/unit/data/test_create_metadata.py

### MODULE DOCSTRING

Contains tests to validate the create_* methods for the data store.

### `def test___create_step___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___create_test_result___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_error_information.py -->
## PYTHON MODULE: tests/unit/data/test_error_information.py

### MODULE DOCSTRING

Tests for the ErrorInformation wrapper type.

### `def test___init___with_defaults() -> None`

Test creating ErrorInformation with default values.

### `def test___init___with_values() -> None`

Test creating ErrorInformation with specific values.

### `def test___init___with_keyword_arguments() -> None`

Test creating ErrorInformation using keyword arguments in different order.

### `def test___from_protobuf___creates_instance_from_protobuf() -> None`

Test creating ErrorInformation from protobuf message.

### `def test___from_protobuf___with_empty_protobuf() -> None`

Test creating ErrorInformation from empty protobuf message.

### `def test___to_protobuf___converts_to_protobuf_message() -> None`

Test converting ErrorInformation to protobuf message.

### `def test___to_protobuf___with_defaults() -> None`

Test converting ErrorInformation with default values to protobuf.

### `def test___round_trip_conversion___preserves_values() -> None`

Test that converting to protobuf and back preserves all values.

### `def test___equality___same_values() -> None`

Test equality comparison with same values.

### `def test___equality___different_values() -> None`

Test equality comparison with different values.

### `def test___equality___with_defaults() -> None`

Test equality comparison with default values.

### `def test___equality___with_non_error_information_object() -> None`

Test equality comparison with non-ErrorInformation object.

### `def test___str___returns_protobuf_string() -> None`

Test string representation returns protobuf string.

### `def test___str___with_empty_values() -> None`

Test string representation with empty values.

### `def test___slots___attribute() -> None`

Test that __slots__ is properly defined.

### `def test___attribute_assignment___after_initialization() -> None`

Test that attributes can be modified after initialization.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_get_metadata.py -->
## PYTHON MODULE: tests/unit/data/test_get_metadata.py

### MODULE DOCSTRING

Contains tests to validate the get_* methods in the data store.

### `def test___get_step___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___get_test_result___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___get_measurement___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___get_condition___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_grpc_conversion.py -->
## PYTHON MODULE: tests/unit/data/test_grpc_conversion.py

### `def test___python_builtin_scalar___populate_condition___condition_updated_correctly(python_value: object, attr_to_check: str) -> None`

### `def test___python_scalar_object___populate_condition___condition_updated_correctly() -> None`

### `def test___python_vector_object___populate_condition_batch___condition_updated_correctly() -> None`

### `def test___python_scalar_iterable___populate_condition_batch___condition_updated_correctly() -> None`

### `def test___python_scalar_generator_iterable___populate_condition_batch___condition_updated_correctly() -> None`

### `def test___empty_iterable___populate_condition_batch___raises_error() -> None`

### `def test___empty_generator___populate_condition_batch___raises_error() -> None`

### `def test___python_unsupported_iterable___populate_condition_batch___raises_error() -> None`

### `def test___python_non_iterable___populate_condition_batch___raises_error() -> None`

### `def test___python_builtin_scalar___populate_measurement___measurement_updated_correctly(python_value: object, attr_to_check: str) -> None`

### `def test___python_vector_object___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_float64_analog_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_int16_analog_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_float64_complex_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_int16_complex_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_bool_digital_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_uint8_digital_waveform___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_float64_spectrum___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_float64_xydata___populate_measurement___measurement_updated_correctly() -> None`

### `def test___python_scalar_iterable___populate_measurement___measurement_updated_correctly(values: list[object], attribute_name: str) -> None`

### `def test___empty_iterable___populate_measurement___raises_value_error() -> None`

### `def test___unsupported_iterable___populate_measurement___raises_type_error() -> None`

### `def _assert_scalar_values(request: PublishMeasurementBatchRequest, attribute_name: str, expected_values: list[object]) -> None`

### `def test___python_vector_object___populate_measurement_batch___measurement_updated_correctly(values: Vector[Any], attribute_name: str, expected_unit: str) -> None`

### `def test___python_scalar_iterable___populate_measurement_batch___measurement_updated_correctly(values: list[object], attribute_name: str) -> None`

### `def test___python_vector_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_float64_analog_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_int16_analog_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_float64_complex_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_int16_complex_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_float64_spectrum_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_uint8_digital_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_float64_xydata_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_scalar_generator_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_non_scalar_generator_iterable___populate_measurement_batch___measurement_updated_correctly() -> None`

### `def test___python_iterable_with_mismatched_second_element___populate_measurement_batch___raises_error(values: list[object], error_message: str) -> None`

### `def test___python_iterable_with_mismatched_second_dtype___populate_measurement_batch___raises_error(values: list[object], error_message: str) -> None`

### `def test___python_unsupported_dtype_iterable___populate_measurement_batch___raises_error(values: list[object], error_message: str) -> None`

### `def test___empty_iterable___populate_measurement_batch___raises_error() -> None`

### `def test___empty_generator___populate_measurement_batch___raises_error() -> None`

### `def test___python_unsupported_iterable___populate_measurement_batch___raises_error() -> None`

### `def test___python_non_iterable___populate_measurement_batch___raises_error() -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_outcome.py -->
## PYTHON MODULE: tests/unit/data/test_outcome.py

### MODULE DOCSTRING

Tests for the Outcome wrapper enum.

### `def test___enum_values___match_protobuf_values() -> None`

Test that enum values match the protobuf enum values.

### `def test___enum_values___have_expected_integer_values() -> None`

Test that enum has the expected integer values.

### `def test___to_protobuf___converts_enum_to_protobuf_value() -> None`

Test converting enum to protobuf value.

### `def test___from_protobuf___converts_protobuf_value_to_enum() -> None`

Test converting protobuf value to enum.

### `def test___round_trip_conversion___preserves_enum_value() -> None`

Test that converting to protobuf and back gives the same result.

### `def test___invalid_value___from_protobuf___raises_value_error() -> None`

Test that from_protobuf raises ValueError for invalid values.

### `def test___enum___is_iterable() -> None`

Test that the enum can be iterated over.

### `def test___enum___has_correct_name_and_value_attributes() -> None`

Test that enum has correct name and value attributes.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_publish_condition.py -->
## PYTHON MODULE: tests/unit/data/test_publish_condition.py

### MODULE DOCSTRING

Contains tests to validate the data store client publish condition functionality.

### `def test___publish_condition___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___none___publish_condition___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___vector___publish_condition_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___int_list___publish_condition_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___float_list___publish_condition_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___bool_list___publish_condition_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___string_list___publish_condition_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___unsupported_list___publish_condition_batch___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___empty_list___publish_condition_batch___raises_value_error(data_store_client: DataStoreClient) -> None`

### `def test___none___publish_condition_batch___raises_type_error(data_store_client: DataStoreClient) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_publish_measurement.py -->
## PYTHON MODULE: tests/unit/data/test_publish_measurement.py

### MODULE DOCSTRING

Contains tests to validate the data store client publish functionality.

### `def test___publish_boolean_data___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock, value: bool) -> None`

### `def test___publish_analog_waveform_data___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___publish_float64_xydata___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___publish_basic_iterable_data___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock, value: Iterable[Any]) -> None`

### `def test___unsupported_list___publish_measurement___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___publish_analog_waveform_data_without_timestamp_parameter___timestamp_is_unset(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___publish_analog_waveform_data_without_t0___uses_timestamp_parameter(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___publish_analog_waveform_data_with_mismatched_timestamp_parameter___uses_provided_timestamp(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___publish_analog_waveform_data_without_t0_or_timestamp___timestamp_is_unset(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___none___publish_measurement___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___vector___publish_measurement_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___int_list___publish_measurement_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___float_list___publish_measurement_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___bool_list___publish_measurement_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___str_list___publish_measurement_batch___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___unsupported_list___publish_measurement_batch___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___empty_list___publish_measurement_batch___raises_type_error(data_store_client: DataStoreClient) -> None`

### `def test___none___publish_measurement_batch___raises_type_error(data_store_client: DataStoreClient) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_query_metadata.py -->
## PYTHON MODULE: tests/unit/data/test_query_metadata.py

### MODULE DOCSTRING

Contains tests to validate the query_* methods in the data store.

### `def test___query_steps___calls_data_store_service_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/data/test_read.py -->
## PYTHON MODULE: tests/unit/data/test_read.py

### MODULE DOCSTRING

Contains tests to validate the data store client read functionality.

### `def test___read_measurement_value___calls_data_store_client(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_double_analog_waveform___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_i16_analog_waveform___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_double_complex_waveform___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_i16_complex_waveform___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_digital_waveform___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_double_spectrum___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_vector___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_xydata___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_condition_value___value_correct(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_measurement_value___without_expected_type___returns_object(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_measurement_value___with_matching_expected_type___returns_typed_value(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_measurement_value___with_mismatched_expected_type___raises_type_error(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_measurement_value___unsupported_type___raises_type_error(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

### `def test___read_condition_value___unsupported_type___raises_type_error(data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/__init__.py -->
## PYTHON MODULE: tests/unit/metadata/__init__.py

### MODULE DOCSTRING

Unit tests for metadata.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_alias_target_type.py -->
## PYTHON MODULE: tests/unit/metadata/test_alias_target_type.py

### MODULE DOCSTRING

Tests for the AliasTargetType wrapper enum.

### `def test___enum_values___match_protobuf_values() -> None`

Test that enum values match the protobuf enum values.

### `def test___enum_values___have_expected_integer_values() -> None`

Test that enum has the expected integer values.

### `def test___to_protobuf___converts_enum_to_protobuf_value() -> None`

Test converting enum to protobuf value.

### `def test___from_protobuf___converts_protobuf_value_to_enum() -> None`

Test converting protobuf value to enum.

### `def test___round_trip_conversion___preserves_enum_value() -> None`

Test that converting to protobuf and back gives the same result.

### `def test___invalid_value___from_protobuf___raises_value_error() -> None`

Test that from_protobuf raises ValueError for invalid values.

### `def test___enum___is_iterable() -> None`

Test that the enum can be iterated over.

### `def test___enum___has_correct_name_and_value_attributes() -> None`

Test that enum has correct name and value attributes.

### `def test___enum___supports_comparison() -> None`

Test that enum supports comparison operations.

### `def test___enum___supports_integer_operations() -> None`

Test that enum supports integer operations since it inherits from IntEnum.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_close_client.py -->
## PYTHON MODULE: tests/unit/metadata/test_close_client.py

### MODULE DOCSTRING

Contains tests related to closing the MetadataStoreClient.

### `def test___exit_metadata_store_client_context___calls_close_on_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___close_metadata_store_client___calls_close_on_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___exit_metadata_store_client_context___call_method___raises_error(metadata_store_client: MetadataStoreClient) -> None`

### `def test___close_metadata_store_client___call_method___raises_error(metadata_store_client: MetadataStoreClient) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_create_from_json.py -->
## PYTHON MODULE: tests/unit/metadata/test_create_from_json.py

### MODULE DOCSTRING

Contains tests for validating JSON metadata creation.

### `def sample_metadata_json() -> str`

Sample JSON metadata for testing.

### `def mock_create_response() -> CreateFromJsonDocumentResponse`

Mock response for create_from_json_document.

### `def test___create_from_json_file_with_pathlib_path___calls_metadata_store_service_client_with_file_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, tmp_path: Path, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json_file with Path object calls service client with file contents.

### `def test___create_from_json_file_with_string_path___calls_metadata_store_service_client_with_file_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, tmp_path: Path, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json_file with string path calls service client with file contents.

### `def test___create_from_json_file_with_non_existent_pathlib_path___raises_error(metadata_store_client: MetadataStoreClient, tmp_path: Path) -> None`

Test that create_from_json_file raises FileNotFoundError for non-existent Path.

### `def test___create_from_json_file_with_non_existent_string_path___raises_error(metadata_store_client: MetadataStoreClient, tmp_path: Path) -> None`

Test that create_from_json_file raises FileNotFoundError for non-existent string path.

### `def test___create_from_json_file_with_utf8_bom___handles_encoding_correctly(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, tmp_path: Path, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json_file correctly handles UTF-8 BOM encoding.

### `def test___create_from_json___calls_metadata_store_service_client_with_json_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json calls service client with JSON contents.

### `def test___create_from_json___returns_metadata_items_from_protobuf_response(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json returns MetadataItems from protobuf response.

### `def test___create_from_json_with_minimal_json___handles_empty_collections(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json handles minimal JSON with empty collections.

### `def test___create_from_json_with_complex_extensions___preserves_extension_data(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json preserves complex extension data.

### `def test___create_from_json_file___returns_metadata_items_from_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, tmp_path: Path, sample_metadata_json: str, mock_create_response: CreateFromJsonDocumentResponse) -> None`

Test that create_from_json_file returns MetadataItems from service client.

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_create_metadata.py -->
## PYTHON MODULE: tests/unit/metadata/test_create_metadata.py

### MODULE DOCSTRING

Contains tests to validate the create_* methods for the metadata store.

### `def test___create_uut_instance___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_uut___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_operator___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_test_description___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_test___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_test_station___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_hardware_item___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_software_item___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___create_test_adapter___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_get_metadata.py -->
## PYTHON MODULE: tests/unit/metadata/test_get_metadata.py

### MODULE DOCSTRING

Contains tests to validate the get_* methods in the metadata store.

### `def test___get_uut_instance___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_uut___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_operator___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_test_description___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_test___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_test_station___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_hardware_item___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_software_item___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___get_test_adapter___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_query_metadata.py -->
## PYTHON MODULE: tests/unit/metadata/test_query_metadata.py

### MODULE DOCSTRING

Contains tests to validate the query_* methods in the metadata store.

### `def test___query_uut_instances___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_uuts___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_operators___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_test_descriptions___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_tests___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_test_stations___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_hardware_items___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_software_items___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

### `def test___query_test_adapters___calls_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock) -> None`

<!--NI_PYTHON_API repo=datastore-python path=tests/unit/metadata/test_register_schema.py -->
## PYTHON MODULE: tests/unit/metadata/test_register_schema.py

### MODULE DOCSTRING

Contains tests for validating schema registration.

### `def test___register_schema_from_file_with_pathlib_path___calls_metadata_store_service_client_with_file_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, schemas_directory: Path) -> None`

### `def test___register_schema_from_file_with_string_path___calls_metadata_store_service_client_with_file_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, schemas_directory: Path) -> None`

### `def test___register_schema_from_file_with_non_existent_pathlib_path___raises_error(metadata_store_client: MetadataStoreClient, schemas_directory: Path) -> None`

### `def test___register_schema_from_file_with_non_existent_string_path___raises_error(metadata_store_client: MetadataStoreClient, schemas_directory: Path) -> None`

### `def test___register_schema_from_file___returns_schema_id_from_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, schemas_directory: Path) -> None`

### `def test___register_schema___calls_metadata_store_service_client_with_schema_contents(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, schemas_directory: Path) -> None`

### `def test___register_schema___returns_schema_id_from_metadata_store_service_client(metadata_store_client: MetadataStoreClient, mocked_metadata_store_service_client: NonCallableMock, schemas_directory: Path) -> None`

<!--NI_PYTHON_API repo=datastore-python path=utilities/src/utilities/__init__.py -->
## PYTHON MODULE: utilities/src/utilities/__init__.py

### MODULE DOCSTRING

Utilities for development in datastore-python.

- `__all__ = ['DataStoreContext']`

<!--NI_PYTHON_API repo=datastore-python path=utilities/src/utilities/_data_store_context.py -->
## PYTHON MODULE: utilities/src/utilities/_data_store_context.py

- `DISCOVERY_SERVICE_CLUSTER_ID_ENV_VAR = 'NIDISCOVERY_CLUSTERID'`

- `DATA_STORE_DATABASE_PATH_ENV_VAR = 'NIDATASTORE_DATASTORESETTINGS__SQLITEDATABASEPATH'`

- `DATA_STORE_DATA_FILES_DIRECTORY_PATH_ENV_VAR = 'NIDATASTORE_DATASTORESETTINGS__DATAFILESDIRECTORY'`

- `DATA_STORE_INGEST_DIRECTORY_PATH_ENV_VAR = 'NIDATASTORE_DATASTORESETTINGS__INGESTDIRECTORY'`

- `DATA_STORE_FAILED_INGEST_DIRECTORY_PATH_ENV_VAR = 'NIDATASTORE_DATASTORESETTINGS__FAILEDINGESTDIRECTORY'`

- `DATA_STORE_TDMS_EXPIRATION_SECONDS_ENV_NAME = 'NIDATASTORE_DATASTORESETTINGS__TDMSFILECACHEEXPIRATIONSECONDS'`

- `DEFAULT_FOLDER_NAME = 'temp_data'`

### `class DataStoreContext()`

A context manager for running a data store in an isolated environment.

#### `def __init__(self, base_directory_path: Path | None=None) -> None`

Initialize the DataStoreContext.

        Args:
            base_directory_path: An optional base directory path specifying where
            the data store files will be located. If not provided, a default path
            in the repository directory will be used.
        

#### `def __enter__(self) -> Self`

Enter the data store context.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the data store context.

#### `def initialize(self) -> None`

Initializes the data store context by setting up necessary environment variables.

#### `def close(self) -> None`

Cleans up the data store context by resetting environment variables.

#### `def _initialize_environment(self) -> None`

#### `def _save_original_environment(self) -> None`

#### `def _initialize_cluster_id(self) -> None`

#### `def _initialize_data_store_paths(self) -> None`

#### `def _get_cluster_id(self) -> str`

#### `def _get_base_directory_hash(self) -> str`

#### `def _get_base_directory_path(self) -> Path`

#### `def _restore_environment(self) -> None`
