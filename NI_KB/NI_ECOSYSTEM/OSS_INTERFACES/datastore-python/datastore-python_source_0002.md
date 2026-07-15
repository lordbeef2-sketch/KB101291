# NI OSS SOURCE SNAPSHOT: datastore-python

<!--NI_OSS_SNAPSHOT repo=ni/datastore-python commit=f78bf987f5b630b942f3f214a6a09d754331a05f -->

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/_test_result.py sha256=ab235ce1f75799fda7488b288fd3172798264c4367072e8dfce6b8a56d5e20cf bytes=9786 -->
## FILE: src/ni/datastore/data/_types/_test_result.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/_test_result.py`
- sha256: `ab235ce1f75799fda7488b288fd3172798264c4367072e8dfce6b8a56d5e20cf`
- bytes: 9786

````python
"""Test Result data type for the Data Store Client."""

from __future__ import annotations

from typing import Iterable, Mapping, MutableMapping, MutableSequence

import hightime as ht
from ni.measurements.data.v1.data_store_pb2 import TestResult as TestResultProto
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_from_protobuf,
    hightime_datetime_to_protobuf,
)

from ni.datastore.data._types._error_information import ErrorInformation
from ni.datastore.data._types._outcome import Outcome
from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class TestResult:
    """Information about a test result.

    Represents the results of executing a test sequence, including metadata
    about the execution environment (UUT, operator, test station), test
    execution time, outcome, and associations with hardware/software components
    and test adapters. Each step which references measurement data and
    conditions is associated with a test result.
    """

    __slots__ = (
        "name",
        "id",
        "uut_instance_id",
        "operator_id",
        "test_station_id",
        "test_description_id",
        "_software_item_ids",
        "_hardware_item_ids",
        "_test_adapter_ids",
        "start_date_time",
        "end_date_time",
        "outcome",
        "link",
        "_extension",
        "schema_id",
        "error_information",
    )

    @property
    def software_item_ids(self) -> MutableSequence[str]:
        """The software item IDs associated with the test result."""
        return self._software_item_ids

    @property
    def hardware_item_ids(self) -> MutableSequence[str]:
        """The hardware item IDs associated with the test result."""
        return self._hardware_item_ids

    @property
    def test_adapter_ids(self) -> MutableSequence[str]:
        """The test adapter IDs associated with the test result."""
        return self._test_adapter_ids

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the test result."""
        return self._extension

    def __init__(
        self,
        name: str,
        *,
        id: str = "",
        uut_instance_id: str = "",
        operator_id: str = "",
        test_station_id: str = "",
        test_description_id: str = "",
        software_item_ids: Iterable[str] | None = None,
        hardware_item_ids: Iterable[str] | None = None,
        test_adapter_ids: Iterable[str] | None = None,
        start_date_time: ht.datetime | None = None,
        end_date_time: ht.datetime | None = None,
        outcome: Outcome = Outcome.UNSPECIFIED,
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
        error_information: ErrorInformation | None = None,
    ) -> None:
        """Initialize a TestResult instance.

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
        """
        self.name = name
        self.id = id
        self.uut_instance_id = uut_instance_id
        self.operator_id = operator_id
        self.test_station_id = test_station_id
        self.test_description_id = test_description_id
        self._software_item_ids: MutableSequence[str] = (
            list(software_item_ids) if software_item_ids is not None else []
        )
        self._hardware_item_ids: MutableSequence[str] = (
            list(hardware_item_ids) if hardware_item_ids is not None else []
        )
        self._test_adapter_ids: MutableSequence[str] = (
            list(test_adapter_ids) if test_adapter_ids is not None else []
        )
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.outcome = outcome
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id
        self.error_information = error_information

    @staticmethod
    def from_protobuf(test_result_proto: TestResultProto) -> "TestResult":
        """Create a TestResult instance from a protobuf TestResult message."""
        test_result = TestResult(
            name=test_result_proto.name,
            id=test_result_proto.id,
            uut_instance_id=test_result_proto.uut_instance_id,
            operator_id=test_result_proto.operator_id,
            test_station_id=test_result_proto.test_station_id,
            test_description_id=test_result_proto.test_description_id,
            software_item_ids=test_result_proto.software_item_ids,
            hardware_item_ids=test_result_proto.hardware_item_ids,
            test_adapter_ids=test_result_proto.test_adapter_ids,
            start_date_time=(
                hightime_datetime_from_protobuf(test_result_proto.start_date_time)
                if test_result_proto.HasField("start_date_time")
                else None
            ),
            end_date_time=(
                hightime_datetime_from_protobuf(test_result_proto.end_date_time)
                if test_result_proto.HasField("end_date_time")
                else None
            ),
            outcome=Outcome.from_protobuf(test_result_proto.outcome),
            link=test_result_proto.link,
            schema_id=test_result_proto.schema_id,
            error_information=(
                ErrorInformation.from_protobuf(test_result_proto.error_information)
                if test_result_proto.HasField("error_information")
                else None
            ),
        )
        populate_from_extension_value_message_map(
            test_result.extension, test_result_proto.extension
        )
        return test_result

    def to_protobuf(self) -> TestResultProto:
        """Convert this TestResult to a protobuf TestResult message."""
        test_result_proto = TestResultProto(
            id=self.id,
            uut_instance_id=self.uut_instance_id,
            operator_id=self.operator_id,
            test_station_id=self.test_station_id,
            test_description_id=self.test_description_id,
            software_item_ids=self.software_item_ids,
            hardware_item_ids=self.hardware_item_ids,
            test_adapter_ids=self.test_adapter_ids,
            name=self.name,
            start_date_time=(
                hightime_datetime_to_protobuf(self.start_date_time)
                if self.start_date_time
                else None
            ),
            end_date_time=(
                hightime_datetime_to_protobuf(self.end_date_time) if self.end_date_time else None
            ),
            outcome=self.outcome.to_protobuf(),
            link=self.link,
            schema_id=self.schema_id,
            error_information=(
                self.error_information.to_protobuf() if self.error_information is not None else None
            ),
        )
        populate_extension_value_message_map(test_result_proto.extension, self.extension)
        return test_result_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, TestResult):
            return NotImplemented
        return (
            self.id == other.id
            and self.uut_instance_id == other.uut_instance_id
            and self.operator_id == other.operator_id
            and self.test_station_id == other.test_station_id
            and self.test_description_id == other.test_description_id
            and self.software_item_ids == other.software_item_ids
            and self.hardware_item_ids == other.hardware_item_ids
            and self.test_adapter_ids == other.test_adapter_ids
            and self.name == other.name
            and self.start_date_time == other.start_date_time
            and self.end_date_time == other.end_date_time
            and self.outcome == other.outcome
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
            and self.error_information == other.error_information
        )

    def __str__(self) -> str:
        """Return a string representation of the TestResult."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/_types/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/ni/datastore/data/_types/py.typed

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/_types/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/data/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/ni/datastore/data/py.typed

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/data/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/__init__.py sha256=97b98824dacd4e56480333e2d1a69dc8530f0d4509e045ac3ec829717a4b68df bytes=1848 -->
## FILE: src/ni/datastore/metadata/__init__.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/__init__.py`
- sha256: `97b98824dacd4e56480333e2d1a69dc8530f0d4509e045ac3ec829717a4b68df`
- bytes: 1848

````python
"""Public API for accessing the NI Metadata Store."""

from ni.datastore.metadata._metadata_store_client import MetadataStoreClient
from ni.datastore.metadata._types._alias import Alias
from ni.datastore.metadata._types._alias_target_type import AliasTargetType
from ni.datastore.metadata._types._extension_schema import ExtensionSchema
from ni.datastore.metadata._types._hardware_item import HardwareItem
from ni.datastore.metadata._types._metadata_items import MetadataItems
from ni.datastore.metadata._types._operator import Operator
from ni.datastore.metadata._types._software_item import SoftwareItem
from ni.datastore.metadata._types._test import Test
from ni.datastore.metadata._types._test_adapter import TestAdapter
from ni.datastore.metadata._types._test_description import TestDescription
from ni.datastore.metadata._types._test_station import TestStation
from ni.datastore.metadata._types._uut import Uut
from ni.datastore.metadata._types._uut_instance import UutInstance

__all__ = [
    "Alias",
    "AliasTargetType",
    "ExtensionSchema",
    "HardwareItem",
    "MetadataItems",
    "MetadataStoreClient",
    "Operator",
    "SoftwareItem",
    "Test",
    "TestAdapter",
    "TestDescription",
    "TestStation",
    "Uut",
    "UutInstance",
]

# Hide that it was not defined in this top-level package
Alias.__module__ = __name__
AliasTargetType.__module__ = __name__
ExtensionSchema.__module__ = __name__
HardwareItem.__module__ = __name__
MetadataItems.__module__ = __name__
MetadataStoreClient.__module__ = __name__
Operator.__module__ = __name__
SoftwareItem.__module__ = __name__
Test.__module__ = __name__
TestAdapter.__module__ = __name__
TestDescription.__module__ = __name__
TestStation.__module__ = __name__
Uut.__module__ = __name__
UutInstance.__module__ = __name__
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_grpc_conversion.py sha256=ea3181fb5d543557ad57141f81fe4772e4471195ab9bd19a7851b630903574fd bytes=1332 -->
## FILE: src/ni/datastore/metadata/_grpc_conversion.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_grpc_conversion.py`
- sha256: `ea3181fb5d543557ad57141f81fe4772e4471195ab9bd19a7851b630903574fd`
- bytes: 1332

````python
"""Helper methods to convert between python and protobuf types."""

from __future__ import annotations

import logging
from typing import MutableMapping

from google.protobuf.internal.containers import MessageMap
from ni.measurements.metadata.v1.metadata_store_pb2 import ExtensionValue

_logger = logging.getLogger(__name__)


def populate_extension_value_message_map(
    destination: MessageMap[str, ExtensionValue],
    source: MutableMapping[str, str],
) -> None:
    """Populate a gRPC message map of string keys to ExtensionValue.

    The input is a mapping of string keys to string values.
    """
    for key, value in source.items():
        destination[key].string_value = value


def populate_from_extension_value_message_map(
    destination: MutableMapping[str, str],
    source: MessageMap[str, ExtensionValue],
) -> None:
    """Populate a mapping of string keys to stringvalues.

    The input is a gRPC message map of string keys to ExtensionValue.
    """
    for key, extension_value in source.items():
        value_case = extension_value.WhichOneof("metadata")
        if value_case == "string_value":
            destination[key] = extension_value.string_value
        else:
            raise TypeError(f"Unsupported ExtensionValue type for key '{key}': {value_case}")
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_metadata_store_client.py sha256=3bbdad7b23d1e931eb342ecc6e549698a02b49ec26b56afe2c38e0b5c08ce0c1 bytes=28011 -->
## FILE: src/ni/datastore/metadata/_metadata_store_client.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_metadata_store_client.py`
- sha256: `3bbdad7b23d1e931eb342ecc6e549698a02b49ec26b56afe2c38e0b5c08ce0c1`
- bytes: 28011

````python
"""Metadata store client for publishing and reading metadata."""

from __future__ import annotations

import logging
import sys
from collections.abc import Sequence
from pathlib import Path
from threading import Lock
from types import TracebackType
from typing import TYPE_CHECKING

from grpc import Channel
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurements.metadata.v1.client import (
    MetadataStoreClient as MetadataStoreServiceClient,
)
from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    CreateAliasRequest,
    CreateFromJsonDocumentRequest,
    CreateHardwareItemRequest,
    CreateOperatorRequest,
    CreateSoftwareItemRequest,
    CreateTestAdapterRequest,
    CreateTestDescriptionRequest,
    CreateTestRequest,
    CreateTestStationRequest,
    CreateUutInstanceRequest,
    CreateUutRequest,
    DeleteAliasRequest,
    GetAliasRequest,
    GetHardwareItemRequest,
    GetOperatorRequest,
    GetSoftwareItemRequest,
    GetTestAdapterRequest,
    GetTestDescriptionRequest,
    GetTestRequest,
    GetTestStationRequest,
    GetUutInstanceRequest,
    GetUutRequest,
    ListSchemasRequest,
    QueryAliasesRequest,
    QueryHardwareItemsRequest,
    QueryOperatorsRequest,
    QuerySoftwareItemsRequest,
    QueryTestAdaptersRequest,
    QueryTestDescriptionsRequest,
    QueryTestsRequest,
    QueryTestStationsRequest,
    QueryUutInstancesRequest,
    QueryUutsRequest,
    RegisterSchemaRequest,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool

from ni.datastore.metadata._types._alias import Alias
from ni.datastore.metadata._types._extension_schema import ExtensionSchema
from ni.datastore.metadata._types._hardware_item import HardwareItem
from ni.datastore.metadata._types._metadata_items import MetadataItems
from ni.datastore.metadata._types._operator import Operator
from ni.datastore.metadata._types._software_item import SoftwareItem
from ni.datastore.metadata._types._test import Test
from ni.datastore.metadata._types._test_adapter import TestAdapter
from ni.datastore.metadata._types._test_description import TestDescription
from ni.datastore.metadata._types._test_station import TestStation
from ni.datastore.metadata._types._uut import Uut
from ni.datastore.metadata._types._uut_instance import UutInstance

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

_logger = logging.getLogger(__name__)


class MetadataStoreClient:
    """Metadata store client for publishing and reading metadata."""

    __slots__ = (
        "_closed",
        "_discovery_client",
        "_grpc_channel",
        "_grpc_channel_pool",
        "_metadata_store_client",
        "_metadata_store_client_lock",
    )

    _METADATA_STORE_CLIENT_CLOSED_ERROR = (
        "This MetadataStoreClient has been closed. Create a new MetadataStoreClient for "
        "further interaction with the metadata store."
    )

    _closed: bool
    _discovery_client: DiscoveryClient | None
    _grpc_channel: Channel | None
    _grpc_channel_pool: GrpcChannelPool | None
    _metadata_store_client: MetadataStoreServiceClient | None
    _metadata_store_client_lock: Lock

    def __init__(
        self,
        discovery_client: DiscoveryClient | None = None,
        grpc_channel: Channel | None = None,
        grpc_channel_pool: GrpcChannelPool | None = None,
    ) -> None:
        """Initialize the MetadataStoreClient.

        Args:
            discovery_client: An optional discovery client (recommended).

            grpc_channel: An optional metadata store gRPC channel. Providing this channel
                will bypass discovery service resolution of the metadata store.

            grpc_channel_pool: An optional gRPC channel pool (recommended).
        """
        self._discovery_client = discovery_client
        self._grpc_channel = grpc_channel
        self._grpc_channel_pool = grpc_channel_pool

        self._metadata_store_client = None
        self._metadata_store_client_lock = Lock()

        self._closed = False

    def __enter__(self) -> Self:
        """Enter the runtime context of the metadata store client."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the runtime context of the metadata store client."""
        self.close()

    def close(self) -> None:
        """Close the metadata store client and clean up resources that it owns."""
        self._closed = True

        with self._metadata_store_client_lock:
            if self._metadata_store_client is not None:
                self._metadata_store_client.close()
                self._metadata_store_client = None

    def create_uut_instance(self, uut_instance: UutInstance) -> str:
        """Create a new UUT instance in the metadata store.

        Args:
            uut_instance: The metadata of the UUT instance to be created.

        Returns:
            str: The identifier of the created UUT instance.
        """
        create_request = CreateUutInstanceRequest(uut_instance=uut_instance.to_protobuf())
        create_response = self._get_metadata_store_client().create_uut_instance(create_request)
        return create_response.uut_instance_id

    def get_uut_instance(self, uut_instance_id: str) -> UutInstance:
        """Get the UUT instance associated with the given identifier.

        Args:
            uut_instance_id: The identifier of the desired UUT instance.

        Returns:
            UutInstance: The metadata of the requested UUT instance.
        """
        get_request = GetUutInstanceRequest(uut_instance_id=uut_instance_id)
        get_response = self._get_metadata_store_client().get_uut_instance(get_request)
        return UutInstance.from_protobuf(get_response.uut_instance)

    def query_uut_instances(self, odata_query: str = "") -> Sequence[UutInstance]:
        """Perform an OData query on UUT instances.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[UutInstance]: The list of UUT instances that match the
                query.
        """
        query_request = QueryUutInstancesRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_uut_instances(query_request)
        return [
            UutInstance.from_protobuf(uut_instance) for uut_instance in query_response.uut_instances
        ]

    def create_uut(self, uut: Uut) -> str:
        """Create a new UUT in the metadata store.

        Args:
            uut: The metadata of the UUT to be created.

        Returns:
            str: The identifier of the created UUT.
        """
        create_request = CreateUutRequest(uut=uut.to_protobuf())
        create_response = self._get_metadata_store_client().create_uut(create_request)
        return create_response.uut_id

    def get_uut(self, uut_id: str) -> Uut:
        """Get the UUT associated with the given identifier.

        Args:
            uut_id: The identifier of the desired UUT.

        Returns:
            Uut: The metadata of the requested UUT.
        """
        get_request = GetUutRequest(uut_id=uut_id)
        get_response = self._get_metadata_store_client().get_uut(get_request)
        return Uut.from_protobuf(get_response.uut)

    def query_uuts(self, odata_query: str = "") -> Sequence[Uut]:
        """Perform an OData query on UUTs.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Uut]: The list of UUTs that match the query.
        """
        query_request = QueryUutsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_uuts(query_request)
        return [Uut.from_protobuf(uut) for uut in query_response.uuts]

    def create_operator(self, operator: Operator) -> str:
        """Create a new operator in the metadata store.

        Args:
            operator: The metadata of the operator to be created.

        Returns:
            str: The identifier of the created operator.
        """
        create_request = CreateOperatorRequest(operator=operator.to_protobuf())
        create_response = self._get_metadata_store_client().create_operator(create_request)
        return create_response.operator_id

    def get_operator(self, operator_id: str) -> Operator:
        """Get the operator associated with the given identifier.

        Args:
            operator_id: The identifier of the desired operator.

        Returns:
            Operator: The metadata of the requested operator.
        """
        get_request = GetOperatorRequest(operator_id=operator_id)
        get_response = self._get_metadata_store_client().get_operator(get_request)
        return Operator.from_protobuf(get_response.operator)

    def query_operators(self, odata_query: str = "") -> Sequence[Operator]:
        """Perform an OData query on operators.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Operator]: The list of operators that match the query.
        """
        query_request = QueryOperatorsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_operators(query_request)
        return [Operator.from_protobuf(operator) for operator in query_response.operators]

    def create_test_description(self, test_description: TestDescription) -> str:
        """Create a test description in the metadata store.

        Args:
            test_description: The metadata of the test description to be created.

        Returns:
            str: The identifier of the created test description.
        """
        create_request = CreateTestDescriptionRequest(
            test_description=test_description.to_protobuf()
        )
        create_response = self._get_metadata_store_client().create_test_description(create_request)
        return create_response.test_description_id

    def get_test_description(self, test_description_id: str) -> TestDescription:
        """Get a test description from the metadata store.

        Args:
            test_description_id: The identifier of the desired test description.

        Returns:
            TestDescription: The metadata of the requested test description.
        """
        get_request = GetTestDescriptionRequest(test_description_id=test_description_id)
        get_response = self._get_metadata_store_client().get_test_description(get_request)
        return TestDescription.from_protobuf(get_response.test_description)

    def query_test_descriptions(self, odata_query: str = "") -> Sequence[TestDescription]:
        """Query test descriptions from the metadata store.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[TestDescription]: The list of test descriptions that match
                the query.
        """
        query_request = QueryTestDescriptionsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_test_descriptions(query_request)
        return [
            TestDescription.from_protobuf(test_description)
            for test_description in query_response.test_descriptions
        ]

    def create_test(self, test: Test) -> str:
        """Create a test in the metadata store.

        Args:
            test: The metadata of the test to be created.

        Returns:
            str: The identifier of the created test.
        """
        create_request = CreateTestRequest(test=test.to_protobuf())
        create_response = self._get_metadata_store_client().create_test(create_request)
        return create_response.test_id

    def get_test(self, test_id: str) -> Test:
        """Get a test from the metadata store.

        Args:
            test_id: The identifier of the desired test.

        Returns:
            Test: The metadata of the requested test.
        """
        get_request = GetTestRequest(test_id=test_id)
        get_response = self._get_metadata_store_client().get_test(get_request)
        return Test.from_protobuf(get_response.test)

    def query_tests(self, odata_query: str = "") -> Sequence[Test]:
        """Query tests from the metadata store."""
        query_request = QueryTestsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_tests(query_request)
        return [Test.from_protobuf(test) for test in query_response.tests]

    def create_test_station(self, test_station: TestStation) -> str:
        """Create a test station in the metadata store.

        Args:
            test_station: The metadata of the test station to be created.

        Returns:
            str: The identifier of the created test station.
        """
        create_request = CreateTestStationRequest(test_station=test_station.to_protobuf())
        create_response = self._get_metadata_store_client().create_test_station(create_request)
        return create_response.test_station_id

    def get_test_station(self, test_station_id: str) -> TestStation:
        """Get a test station from the metadata store.

        Args:
            test_station_id: The identifier of the desired test station.

        Returns:
            TestStation: The metadata of the requested test station.
        """
        get_request = GetTestStationRequest(test_station_id=test_station_id)
        get_response = self._get_metadata_store_client().get_test_station(get_request)
        return TestStation.from_protobuf(get_response.test_station)

    def query_test_stations(self, odata_query: str = "") -> Sequence[TestStation]:
        """Query test stations from the metadata store."""
        query_request = QueryTestStationsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_test_stations(query_request)
        return [
            TestStation.from_protobuf(test_station) for test_station in query_response.test_stations
        ]

    def create_hardware_item(self, hardware_item: HardwareItem) -> str:
        """Create a hardware item in the metadata store.

        Args:
            hardware_item: The metadata of the hardware item to be created.

        Returns:
            str: The identifier of the created hardware item.
        """
        create_request = CreateHardwareItemRequest(hardware_item=hardware_item.to_protobuf())
        create_response = self._get_metadata_store_client().create_hardware_item(create_request)
        return create_response.hardware_item_id

    def get_hardware_item(self, hardware_item_id: str) -> HardwareItem:
        """Get a hardware item from the metadata store.

        Args:
            hardware_item_id: The identifier of the desired hardware item.

        Returns:
            HardwareItem: The metadata of the requested hardware item.
        """
        get_request = GetHardwareItemRequest(hardware_item_id=hardware_item_id)
        get_response = self._get_metadata_store_client().get_hardware_item(get_request)
        return HardwareItem.from_protobuf(get_response.hardware_item)

    def query_hardware_items(self, odata_query: str = "") -> Sequence[HardwareItem]:
        """Query hardware items from the metadata store."""
        query_request = QueryHardwareItemsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_hardware_items(query_request)
        return [
            HardwareItem.from_protobuf(hardware_item)
            for hardware_item in query_response.hardware_items
        ]

    def create_software_item(self, software_item: SoftwareItem) -> str:
        """Create a software item in the metadata store.

        Args:
            software_item: The metadata of the software item to be created.

        Returns:
            str: The identifier of the created software item.
        """
        create_request = CreateSoftwareItemRequest(software_item=software_item.to_protobuf())
        create_response = self._get_metadata_store_client().create_software_item(create_request)
        return create_response.software_item_id

    def get_software_item(self, software_item_id: str) -> SoftwareItem:
        """Get a software item from the metadata store.

        Args:
            software_item_id: The identifier of the desired software item.

        Returns:
            SoftwareItem: The metadata of the requested software item.
        """
        get_request = GetSoftwareItemRequest(software_item_id=software_item_id)
        get_response = self._get_metadata_store_client().get_software_item(get_request)
        return SoftwareItem.from_protobuf(get_response.software_item)

    def query_software_items(self, odata_query: str = "") -> Sequence[SoftwareItem]:
        """Query software items from the metadata store."""
        query_request = QuerySoftwareItemsRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_software_items(query_request)
        return [
            SoftwareItem.from_protobuf(software_item)
            for software_item in query_response.software_items
        ]

    def create_test_adapter(self, test_adapter: TestAdapter) -> str:
        """Create a test adapter in the metadata store.

        Args:
            test_adapter: The metadata of the test adapter to be created.

        Returns:
            str: The identifier of the created test adapter.
        """
        create_request = CreateTestAdapterRequest(test_adapter=test_adapter.to_protobuf())
        create_response = self._get_metadata_store_client().create_test_adapter(create_request)
        return create_response.test_adapter_id

    def get_test_adapter(self, test_adapter_id: str) -> TestAdapter:
        """Get a test adapter from the metadata store.

        Args:
            test_adapter_id: The identifier of the desired test adapter.

        Returns:
            TestAdapter: The metadata of the requested test adapter.
        """
        get_request = GetTestAdapterRequest(test_adapter_id=test_adapter_id)
        get_response = self._get_metadata_store_client().get_test_adapter(get_request)
        return TestAdapter.from_protobuf(get_response.test_adapter)

    def query_test_adapters(self, odata_query: str = "") -> Sequence[TestAdapter]:
        """Query test adapters from the metadata store."""
        query_request = QueryTestAdaptersRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_test_adapters(query_request)
        return [
            TestAdapter.from_protobuf(test_adapter) for test_adapter in query_response.test_adapters
        ]

    def register_schema_from_file(self, schema_file_path: Path | str) -> str:
        """Register a schema obtained from the specified file in the metadata store.

        Args:
            schema_file_path: The path at which the schema file is located

        Raises:
            FileNotFoundError: If the schema file does not exist.
        """
        if isinstance(schema_file_path, str):
            schema_file_path = Path(schema_file_path)

        if not schema_file_path.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_file_path}")

        schema_contents = schema_file_path.read_text(encoding="utf-8-sig")
        return self.register_schema(schema_contents=schema_contents)

    def register_schema(self, schema_contents: str) -> str:
        """Register a schema in the metadata store.

        Once a schema has been published, it cannot be modified or removed.

        Args:
            schema_contents: The contents of the JSON or TOML schema. This
                should be a well-formed JSON or TOML schema. Validation will
                be performed, and an error will be returned if the schema is
                not valid.

        Returns:
            str: The ID of the schema.
        """
        register_request = RegisterSchemaRequest(schema=schema_contents)
        register_response = self._get_metadata_store_client().register_schema(register_request)
        return register_response.schema_id

    def list_schemas(self) -> Sequence[ExtensionSchema]:
        """List the schemas that have been previously registered.

        Returns:
            Sequence[ExtensionSchema]: The list of registered schemas.
        """
        list_request = ListSchemasRequest()
        list_response = self._get_metadata_store_client().list_schemas(list_request)
        return [ExtensionSchema.from_protobuf(schema) for schema in list_response.schemas]

    def get_alias(self, alias_name: str) -> Alias:
        """Get an alias and its target (the underlying metadata it represents).

        Args:
            alias_name: The name of the alias to retrieve.

        Returns:
            Alias: The alias containing the alias name, target type, and
                target ID of the underlying metadata.
        """
        get_request = GetAliasRequest(alias_name=alias_name)
        get_response = self._get_metadata_store_client().get_alias(get_request)
        return Alias.from_protobuf(get_response.alias)

    def query_aliases(self, odata_query: str = "") -> Sequence[Alias]:
        """Perform an OData query on the registered aliases.

        Args:
            odata_query: An OData query string. Example: "$filter=name eq
                'Value'". $expand is not supported.

        Returns:
            Sequence[Alias]: The list of aliases that match the query.
        """
        query_request = QueryAliasesRequest(odata_query=odata_query)
        query_response = self._get_metadata_store_client().query_aliases(query_request)
        return [Alias.from_protobuf(alias) for alias in query_response.aliases]

    def create_alias(
        self,
        alias_name: str,
        alias_target: (
            UutInstance
            | Uut
            | HardwareItem
            | SoftwareItem
            | Operator
            | TestDescription
            | Test
            | TestAdapter
            | TestStation
        ),
    ) -> Alias:
        """Create (register) an alias of the specified metadata.

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
        """
        create_request = CreateAliasRequest(alias_name=alias_name)
        if isinstance(alias_target, UutInstance):
            create_request.uut_instance.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, Uut):
            create_request.uut.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, HardwareItem):
            create_request.hardware_item.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, SoftwareItem):
            create_request.software_item.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, Operator):
            create_request.operator.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, TestDescription):
            create_request.test_description.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, Test):
            create_request.test.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, TestAdapter):
            create_request.test_adapter.CopyFrom(alias_target.to_protobuf())
        elif isinstance(alias_target, TestStation):
            create_request.test_station.CopyFrom(alias_target.to_protobuf())
        response = self._get_metadata_store_client().create_alias(create_request)
        return Alias.from_protobuf(response.alias)

    def delete_alias(self, alias_name: str) -> bool:
        """Remove a registered alias.

        Args:
            alias_name: The name of the alias to unregister.

        Returns:
            bool: Whether the action resulted in the specified alias becoming
                unregistered. False if the alias does not exist.
        """
        delete_request = DeleteAliasRequest(alias_name=alias_name)
        delete_response = self._get_metadata_store_client().delete_alias(delete_request)
        return delete_response.unregistered

    def create_from_json_file(self, metadata_file_path: Path | str) -> MetadataItems:
        """Create metadata items from a JSON file.

        Args:
            metadata_file_path: The path to the JSON file containing metadata definitions.

        Returns:
            MetadataItems: A collection of metadata items created from the JSON document.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
        """
        if isinstance(metadata_file_path, str):
            metadata_file_path = Path(metadata_file_path)

        if not metadata_file_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {metadata_file_path}")

        metadata_contents = metadata_file_path.read_text(encoding="utf-8-sig")
        return self.create_from_json(metadata_contents)

    def create_from_json(self, metadata_file_contents: str) -> MetadataItems:
        """Create metadata items from a JSON document.

        Args:
            metadata_file_contents: The JSON document content containing metadata definitions.

        Returns:
            MetadataItems: A collection of metadata items created from the JSON document.
        """
        create_request = CreateFromJsonDocumentRequest(json_document=metadata_file_contents)
        create_response = self._get_metadata_store_client().create_from_json_document(
            create_request
        )
        return MetadataItems.from_protobuf(create_response)

    def _get_metadata_store_client(self) -> MetadataStoreServiceClient:
        if self._closed:
            raise RuntimeError(self._METADATA_STORE_CLIENT_CLOSED_ERROR)

        if self._metadata_store_client is None:
            with self._metadata_store_client_lock:
                if self._metadata_store_client is None:
                    self._metadata_store_client = self._instantiate_metadata_store_client()
        return self._metadata_store_client

    def _instantiate_metadata_store_client(self) -> MetadataStoreServiceClient:
        return MetadataStoreServiceClient(
            discovery_client=self._discovery_client,
            grpc_channel=self._grpc_channel,
            grpc_channel_pool=self._grpc_channel_pool,
        )
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/__init__.py sha256=9ef1926f9150e13bd51b59c0630b0fefd177f77e41639b1dc9dd1480c7ed026b bytes=57 -->
## FILE: src/ni/datastore/metadata/_types/__init__.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/__init__.py`
- sha256: `9ef1926f9150e13bd51b59c0630b0fefd177f77e41639b1dc9dd1480c7ed026b`
- bytes: 57

````python
"""Types for use in accessing the NI Metadata Store."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_alias.py sha256=03aaf5fec9aba2aab8c96c17f6524891e1b738db3a2964bb9d2fe8152f69cd32 bytes=2333 -->
## FILE: src/ni/datastore/metadata/_types/_alias.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_alias.py`
- sha256: `03aaf5fec9aba2aab8c96c17f6524891e1b738db3a2964bb9d2fe8152f69cd32`
- bytes: 2333

````python
"""Alias data type for the Data Store Client."""

from __future__ import annotations

from ni.measurements.metadata.v1.metadata_store_pb2 import Alias as AliasProto

from ni.datastore.metadata._types._alias_target_type import AliasTargetType


class Alias:
    """Represents an alias for metadata.

    An alias provides a user-friendly name that maps to a specific metadata
    instance, containing the alias name, the type of the aliased metadata
    instance, and the unique identifier for the aliased metadata instance.
    """

    __slots__ = (
        "name",
        "target_type",
        "target_id",
    )

    def __init__(
        self,
        *,
        name: str = "",
        target_type: AliasTargetType = AliasTargetType.UNSPECIFIED,
        target_id: str = "",
    ) -> None:
        """Initialize an Alias instance.

        Args:
            name: The registered alias name for the aliased metadata
                instance.
            target_type: The type of the aliased metadata instance.
            target_id: The unique identifier for the aliased metadata instance.
        """
        self.name = name
        self.target_type = target_type
        self.target_id = target_id

    @staticmethod
    def from_protobuf(alias_proto: AliasProto) -> "Alias":
        """Create an Alias instance from a protobuf Alias message."""
        return Alias(
            name=alias_proto.name,
            target_type=AliasTargetType.from_protobuf(alias_proto.target_type),
            target_id=alias_proto.target_id,
        )

    def to_protobuf(self) -> AliasProto:
        """Convert this Alias to a protobuf Alias message."""
        return AliasProto(
            name=self.name,
            target_type=self.target_type.to_protobuf(),
            target_id=self.target_id,
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, Alias):
            return NotImplemented
        return (
            self.name == other.name
            and self.target_type == other.target_type
            and self.target_id == other.target_id
        )

    def __str__(self) -> str:
        """Return a string representation of the Alias."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_alias_target_type.py sha256=f129eaedd20ed56a6930683c148530b564407324973a3ef42767fea6885f3daa bytes=2641 -->
## FILE: src/ni/datastore/metadata/_types/_alias_target_type.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_alias_target_type.py`
- sha256: `f129eaedd20ed56a6930683c148530b564407324973a3ef42767fea6885f3daa`
- bytes: 2641

````python
"""AliasTargetType data type for the Data Store Client."""

from __future__ import annotations

from enum import IntEnum

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    AliasTargetType as AliasTargetTypeProto,
)


class AliasTargetType(IntEnum):
    """Represents the type of target that an alias can reference.

    The AliasTargetType enum indicates what kind of metadata entity
    an alias is pointing to.
    """

    UNSPECIFIED = AliasTargetTypeProto.ALIAS_TARGET_TYPE_UNSPECIFIED
    """The alias target type is not specified or unknown."""

    UUT_INSTANCE = AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT_INSTANCE
    """The alias targets a UUT instance."""

    UUT = AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT
    """The alias targets a UUT."""

    HARDWARE_ITEM = AliasTargetTypeProto.ALIAS_TARGET_TYPE_HARDWARE_ITEM
    """The alias targets a hardware item."""

    SOFTWARE_ITEM = AliasTargetTypeProto.ALIAS_TARGET_TYPE_SOFTWARE_ITEM
    """The alias targets a software item."""

    OPERATOR = AliasTargetTypeProto.ALIAS_TARGET_TYPE_OPERATOR
    """The alias targets an operator."""

    TEST_DESCRIPTION = AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_DESCRIPTION
    """The alias targets a test description."""

    TEST = AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST
    """The alias targets a test."""

    TEST_STATION = AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_STATION
    """The alias targets a test station."""

    TEST_ADAPTER = AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_ADAPTER
    """The alias targets a test adapter."""

    @classmethod
    def from_protobuf(
        cls, alias_target_type_proto: AliasTargetTypeProto.ValueType
    ) -> "AliasTargetType":
        """Create an AliasTargetType instance from a protobuf AliasTargetType value.

        Args:
            alias_target_type_proto: The protobuf AliasTargetType value.

        Returns:
            The corresponding AliasTargetType enum value.

        Raises:
            ValueError: If the protobuf value doesn't correspond to a known AliasTargetType.
        """
        try:
            return cls(alias_target_type_proto)
        except ValueError as e:
            raise ValueError(f"Unknown alias target type value: {alias_target_type_proto}") from e

    def to_protobuf(self) -> AliasTargetTypeProto.ValueType:
        """Convert this AliasTargetType instance to a protobuf AliasTargetType value.

        Returns:
            The corresponding protobuf AliasTargetType value.
        """
        return AliasTargetTypeProto.ValueType(self.value)
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_extension_schema.py sha256=0af1314f973cffb1f6797aafdd996963a7a34b57bbf6f18802de6afac5571d3d bytes=1822 -->
## FILE: src/ni/datastore/metadata/_types/_extension_schema.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_extension_schema.py`
- sha256: `0af1314f973cffb1f6797aafdd996963a7a34b57bbf6f18802de6afac5571d3d`
- bytes: 1822

````python
"""Extension Schema data type for the Data Store Client."""

from __future__ import annotations

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    ExtensionSchema as ExtensionSchemaProto,
)


class ExtensionSchema:
    """Represents an extension schema stored in the system.

    An extension schema contains the schema ID and the schema definition
    itself, which can be used to validate extension data in metadata instances.
    """

    __slots__ = (
        "id",
        "schema",
    )

    def __init__(
        self,
        *,
        id: str = "",
        schema: str = "",
    ) -> None:
        """Initialize an ExtensionSchema instance.

        Args:
            id: The ID of the schema.
            schema: The schema itself.
        """
        self.id = id
        self.schema = schema

    @staticmethod
    def from_protobuf(extension_schema_proto: ExtensionSchemaProto) -> "ExtensionSchema":
        """Create an ExtensionSchema instance from a protobuf ExtensionSchema message."""
        return ExtensionSchema(
            id=extension_schema_proto.id,
            schema=extension_schema_proto.schema,
        )

    def to_protobuf(self) -> ExtensionSchemaProto:
        """Convert this ExtensionSchema to a protobuf ExtensionSchema message."""
        return ExtensionSchemaProto(
            id=self.id,
            schema=self.schema,
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, ExtensionSchema):
            return NotImplemented
        return self.id == other.id and self.schema == other.schema

    def __str__(self) -> str:
        """Return a string representation of the ExtensionSchema."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_hardware_item.py sha256=803752f941fdacc9d153b63e238da103e63c230fa62ba016df55f79327d20859 bytes=5598 -->
## FILE: src/ni/datastore/metadata/_types/_hardware_item.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_hardware_item.py`
- sha256: `803752f941fdacc9d153b63e238da103e63c230fa62ba016df55f79327d20859`
- bytes: 5598

````python
"""Hardware Item data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    HardwareItem as HardwareItemProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class HardwareItem:
    """Represents the metadata of a hardware item used to take measurements.

    A hardware item contains information about physical test equipment
    including manufacturer, model, serial number, calibration dates, and asset
    tracking information.
    """

    __slots__ = (
        "_id",
        "manufacturer",
        "model",
        "serial_number",
        "part_number",
        "asset_identifier",
        "calibration_due_date",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the hardware item."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the hardware item."""
        return self._id

    def __init__(
        self,
        *,
        manufacturer: str = "",
        model: str = "",
        serial_number: str = "",
        part_number: str = "",
        asset_identifier: str = "",
        calibration_due_date: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a HardwareItem instance.

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
        """
        self._id = ""
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.part_number = part_number
        self.asset_identifier = asset_identifier
        self.calibration_due_date = calibration_due_date
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(hardware_item_proto: HardwareItemProto) -> "HardwareItem":
        """Create a HardwareItem instance from a protobuf HardwareItem message."""
        hardware_item = HardwareItem(
            manufacturer=hardware_item_proto.manufacturer,
            model=hardware_item_proto.model,
            serial_number=hardware_item_proto.serial_number,
            part_number=hardware_item_proto.part_number,
            asset_identifier=hardware_item_proto.asset_identifier,
            calibration_due_date=hardware_item_proto.calibration_due_date,
            link=hardware_item_proto.link,
            schema_id=hardware_item_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            hardware_item.extension, hardware_item_proto.extension
        )
        hardware_item._id = hardware_item_proto.id
        return hardware_item

    def to_protobuf(self) -> HardwareItemProto:
        """Convert this HardwareItem to a protobuf HardwareItem message."""
        hardware_item_proto = HardwareItemProto(
            id=self.id,
            manufacturer=self.manufacturer,
            model=self.model,
            serial_number=self.serial_number,
            part_number=self.part_number,
            asset_identifier=self.asset_identifier,
            calibration_due_date=self.calibration_due_date,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(hardware_item_proto.extension, self.extension)
        return hardware_item_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, HardwareItem):
            return NotImplemented
        return (
            self.id == other.id
            and self.manufacturer == other.manufacturer
            and self.model == other.model
            and self.serial_number == other.serial_number
            and self.part_number == other.part_number
            and self.asset_identifier == other.asset_identifier
            and self.calibration_due_date == other.calibration_due_date
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the HardwareItem."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_metadata_items.py sha256=813b8f4cbe0d9339b69e369c43cf39d46cbf00f97c684bfce43509e0c7ef71f9 bytes=6659 -->
## FILE: src/ni/datastore/metadata/_types/_metadata_items.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_metadata_items.py`
- sha256: `813b8f4cbe0d9339b69e369c43cf39d46cbf00f97c684bfce43509e0c7ef71f9`
- bytes: 6659

````python
"""MetadataItems data type for the Data Store Client."""

from __future__ import annotations

from collections.abc import Sequence

from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    CreateFromJsonDocumentResponse,
)

from ni.datastore.metadata._types._hardware_item import HardwareItem
from ni.datastore.metadata._types._operator import Operator
from ni.datastore.metadata._types._software_item import SoftwareItem
from ni.datastore.metadata._types._test import Test
from ni.datastore.metadata._types._test_adapter import TestAdapter
from ni.datastore.metadata._types._test_description import TestDescription
from ni.datastore.metadata._types._test_station import TestStation
from ni.datastore.metadata._types._uut import Uut
from ni.datastore.metadata._types._uut_instance import UutInstance


class MetadataItems:
    """Represents a collection of metadata items created from a JSON document.

    This class contains the results of creating metadata items from a JSON document,
    organizing them by type for easy access.
    """

    __slots__ = (
        "uut_instances",
        "uuts",
        "operators",
        "test_descriptions",
        "tests",
        "test_stations",
        "hardware_items",
        "software_items",
        "test_adapters",
    )

    def __init__(
        self,
        *,
        uut_instances: Sequence[UutInstance] = (),
        uuts: Sequence[Uut] = (),
        operators: Sequence[Operator] = (),
        test_descriptions: Sequence[TestDescription] = (),
        tests: Sequence[Test] = (),
        test_stations: Sequence[TestStation] = (),
        hardware_items: Sequence[HardwareItem] = (),
        software_items: Sequence[SoftwareItem] = (),
        test_adapters: Sequence[TestAdapter] = (),
    ) -> None:
        """Initialize a MetadataItems instance.

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
        """
        self.uut_instances = uut_instances
        self.uuts = uuts
        self.operators = operators
        self.test_descriptions = test_descriptions
        self.tests = tests
        self.test_stations = test_stations
        self.hardware_items = hardware_items
        self.software_items = software_items
        self.test_adapters = test_adapters

    @staticmethod
    def from_protobuf(response: CreateFromJsonDocumentResponse) -> "MetadataItems":
        """Create a MetadataItems instance from a protobuf CreateFromJsonDocumentResponse.

        Args:
            response: The protobuf response containing the created metadata items.

        Returns:
            MetadataItems: A new MetadataItems instance with all the created items.
        """
        return MetadataItems(
            uut_instances=[
                UutInstance.from_protobuf(uut_instance) for uut_instance in response.uut_instances
            ],
            uuts=[Uut.from_protobuf(uut) for uut in response.uuts],
            operators=[Operator.from_protobuf(operator) for operator in response.operators],
            test_descriptions=[
                TestDescription.from_protobuf(test_description)
                for test_description in response.test_descriptions
            ],
            tests=[Test.from_protobuf(test) for test in response.tests],
            test_stations=[
                TestStation.from_protobuf(test_station) for test_station in response.test_stations
            ],
            hardware_items=[
                HardwareItem.from_protobuf(hardware_item)
                for hardware_item in response.hardware_items
            ],
            software_items=[
                SoftwareItem.from_protobuf(software_item)
                for software_item in response.software_items
            ],
            test_adapters=[
                TestAdapter.from_protobuf(test_adapter) for test_adapter in response.test_adapters
            ],
        )

    def __eq__(self, other: object) -> bool:
        """Determine equality between MetadataItems instances."""
        if not isinstance(other, MetadataItems):
            return False

        return (
            list(self.uut_instances) == list(other.uut_instances)
            and list(self.uuts) == list(other.uuts)
            and list(self.operators) == list(other.operators)
            and list(self.test_descriptions) == list(other.test_descriptions)
            and list(self.tests) == list(other.tests)
            and list(self.test_stations) == list(other.test_stations)
            and list(self.hardware_items) == list(other.hardware_items)
            and list(self.software_items) == list(other.software_items)
            and list(self.test_adapters) == list(other.test_adapters)
        )

    def __str__(self) -> str:
        """Return a string representation of the MetadataItems."""
        counts = []
        if self.uut_instances:
            counts.append(f"{len(self.uut_instances)} UUT instances")
        if self.uuts:
            counts.append(f"{len(self.uuts)} UUTs")
        if self.operators:
            counts.append(f"{len(self.operators)} operators")
        if self.test_descriptions:
            counts.append(f"{len(self.test_descriptions)} test descriptions")
        if self.tests:
            counts.append(f"{len(self.tests)} tests")
        if self.test_stations:
            counts.append(f"{len(self.test_stations)} test stations")
        if self.hardware_items:
            counts.append(f"{len(self.hardware_items)} hardware items")
        if self.software_items:
            counts.append(f"{len(self.software_items)} software items")
        if self.test_adapters:
            counts.append(f"{len(self.test_adapters)} test adapters")

        if counts:
            return f"MetadataItems({', '.join(counts)})"
        else:
            return "MetadataItems(empty)"
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_operator.py sha256=3f09f67821e3c9955ca9a9974a3a703738bb7a143120e5c45aae3ff93b68e774 bytes=3793 -->
## FILE: src/ni/datastore/metadata/_types/_operator.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_operator.py`
- sha256: `3f09f67821e3c9955ca9a9974a3a703738bb7a143120e5c45aae3ff93b68e774`
- bytes: 3793

````python
"""Operator data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    Operator as OperatorProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class Operator:
    """Represents the metadata of the operator that took the test step.

    An operator contains information about the person or entity responsible for
    conducting tests, including their name and role.
    """

    __slots__ = (
        "_id",
        "name",
        "role",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the operator."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the operator."""
        return self._id

    def __init__(
        self,
        *,
        name: str = "",
        role: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize an Operator instance.

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
        """
        self._id = ""
        self.name = name
        self.role = role
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(operator_proto: OperatorProto) -> "Operator":
        """Create an Operator instance from a protobuf Operator message."""
        operator = Operator(
            name=operator_proto.name,
            role=operator_proto.role,
            link=operator_proto.link,
            schema_id=operator_proto.schema_id,
        )
        populate_from_extension_value_message_map(operator.extension, operator_proto.extension)
        operator._id = operator_proto.id
        return operator

    def to_protobuf(self) -> OperatorProto:
        """Convert this Operator to a protobuf Operator message."""
        operator_proto = OperatorProto(
            id=self.id,
            name=self.name,
            role=self.role,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(operator_proto.extension, self.extension)
        return operator_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, Operator):
            return NotImplemented
        return (
            self.id == other.id
            and self.name == other.name
            and self.role == other.role
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the Operator."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_software_item.py sha256=5b65deb8cb2bc70b7432a4211b1ac5b16290f8880cef802310b900710e90db84 bytes=4041 -->
## FILE: src/ni/datastore/metadata/_types/_software_item.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_software_item.py`
- sha256: `5b65deb8cb2bc70b7432a4211b1ac5b16290f8880cef802310b900710e90db84`
- bytes: 4041

````python
"""Software Item data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    SoftwareItem as SoftwareItemProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class SoftwareItem:
    """Represents the metadata of the software item used to take measurements.

    A software item contains information about the software product and version
    used during testing.
    """

    __slots__ = (
        "_id",
        "product",
        "version",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the software item."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the software item."""
        return self._id

    def __init__(
        self,
        *,
        product: str = "",
        version: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a SoftwareItem instance.

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
        """
        self._id = ""
        self.product = product
        self.version = version
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(software_item_proto: SoftwareItemProto) -> "SoftwareItem":
        """Create a SoftwareItem instance from a protobuf SoftwareItem message."""
        software_item = SoftwareItem(
            product=software_item_proto.product,
            version=software_item_proto.version,
            link=software_item_proto.link,
            schema_id=software_item_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            software_item.extension, software_item_proto.extension
        )
        software_item._id = software_item_proto.id
        return software_item

    def to_protobuf(self) -> SoftwareItemProto:
        """Convert this SoftwareItem to a protobuf SoftwareItem message."""
        software_item_proto = SoftwareItemProto(
            id=self.id,
            product=self.product,
            version=self.version,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(software_item_proto.extension, self.extension)
        return software_item_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, SoftwareItem):
            return NotImplemented
        return (
            self.id == other.id
            and self.product == other.product
            and self.version == other.version
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the SoftwareItem."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_test.py sha256=71f43418bf9523d11ee1a0540c2a49f629d52a1aba60dea13bd636ec5d817d37 bytes=3699 -->
## FILE: src/ni/datastore/metadata/_types/_test.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_test.py`
- sha256: `71f43418bf9523d11ee1a0540c2a49f629d52a1aba60dea13bd636ec5d817d37`
- bytes: 3699

````python
"""Test data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    Test as TestProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class Test:
    """Represents the metadata of a test.

    A test contains information about a specific test procedure, including its
    name and description of what the test does.
    """

    __slots__ = (
        "_id",
        "name",
        "description",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the test."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the test."""
        return self._id

    def __init__(
        self,
        *,
        name: str = "",
        description: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a Test instance.

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
        """
        self._id = ""
        self.name = name
        self.description = description
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(test_proto: TestProto) -> "Test":
        """Create a Test instance from a protobuf Test message."""
        test = Test(
            name=test_proto.name,
            description=test_proto.description,
            link=test_proto.link,
            schema_id=test_proto.schema_id,
        )
        populate_from_extension_value_message_map(test.extension, test_proto.extension)
        test._id = test_proto.id
        return test

    def to_protobuf(self) -> TestProto:
        """Convert this Test to a protobuf Test message."""
        test_proto = TestProto(
            id=self.id,
            name=self.name,
            description=self.description,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(test_proto.extension, self.extension)
        return test_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, Test):
            return NotImplemented
        return (
            self.id == other.id
            and self.name == other.name
            and self.description == other.description
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the Test."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_test_adapter.py sha256=e1feccee19491017a5f395bcdb1f8320d5e7e2770d2eecb0f7d39a85085f27e2 bytes=5836 -->
## FILE: src/ni/datastore/metadata/_types/_test_adapter.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_test_adapter.py`
- sha256: `e1feccee19491017a5f395bcdb1f8320d5e7e2770d2eecb0f7d39a85085f27e2`
- bytes: 5836

````python
"""Test Adapter data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    TestAdapter as TestAdapterProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class TestAdapter:
    """Represents a test adapter or mechanical setup.

    This is a board or device that is used to hold, connect, or interface the
    UUT with the test system. Test adapters may also be referred to as test
    fixtures, interface boards, breakout boxes, mechanical fixtures, or
    connection adapters.
    """

    __slots__ = (
        "_id",
        "name",
        "manufacturer",
        "model",
        "serial_number",
        "part_number",
        "asset_identifier",
        "calibration_due_date",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the test adapter."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the test adapter."""
        return self._id

    def __init__(
        self,
        *,
        name: str = "",
        manufacturer: str = "",
        model: str = "",
        serial_number: str = "",
        part_number: str = "",
        asset_identifier: str = "",
        calibration_due_date: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a TestAdapter instance.

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
        """
        self._id = ""
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.part_number = part_number
        self.asset_identifier = asset_identifier
        self.calibration_due_date = calibration_due_date
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(test_adapter_proto: TestAdapterProto) -> "TestAdapter":
        """Create a TestAdapter instance from a protobuf TestAdapter message."""
        test_adapter = TestAdapter(
            name=test_adapter_proto.name,
            manufacturer=test_adapter_proto.manufacturer,
            model=test_adapter_proto.model,
            serial_number=test_adapter_proto.serial_number,
            part_number=test_adapter_proto.part_number,
            asset_identifier=test_adapter_proto.asset_identifier,
            calibration_due_date=test_adapter_proto.calibration_due_date,
            link=test_adapter_proto.link,
            schema_id=test_adapter_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            test_adapter.extension, test_adapter_proto.extension
        )
        test_adapter._id = test_adapter_proto.id
        return test_adapter

    def to_protobuf(self) -> TestAdapterProto:
        """Convert this TestAdapter to a protobuf TestAdapter message."""
        test_adapter_proto = TestAdapterProto(
            id=self.id,
            name=self.name,
            manufacturer=self.manufacturer,
            model=self.model,
            serial_number=self.serial_number,
            part_number=self.part_number,
            asset_identifier=self.asset_identifier,
            calibration_due_date=self.calibration_due_date,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(test_adapter_proto.extension, self.extension)
        return test_adapter_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, TestAdapter):
            return NotImplemented
        return (
            self.id == other.id
            and self.name == other.name
            and self.manufacturer == other.manufacturer
            and self.model == other.model
            and self.serial_number == other.serial_number
            and self.part_number == other.part_number
            and self.asset_identifier == other.asset_identifier
            and self.calibration_due_date == other.calibration_due_date
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the TestAdapter."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_test_description.py sha256=a069f24bbc9e340baf201c66e99127b9b39b76d7143cdd9b748023d10bbdf287 bytes=4213 -->
## FILE: src/ni/datastore/metadata/_types/_test_description.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_test_description.py`
- sha256: `a069f24bbc9e340baf201c66e99127b9b39b76d7143cdd9b748023d10bbdf287`
- bytes: 4213

````python
"""Test Description data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    TestDescription as TestDescriptionProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class TestDescription:
    """Represents the metadata of a test description.

    A test description contains information about a test procedure designed for
    a specific UUT, including the UUT ID and test description name.
    """

    __slots__ = (
        "_id",
        "uut_id",
        "name",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the test description."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the test description."""
        return self._id

    def __init__(
        self,
        *,
        uut_id: str = "",
        name: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a TestDescription instance.

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
        """
        self._id = ""
        self.uut_id = uut_id
        self.name = name
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(test_description_proto: TestDescriptionProto) -> "TestDescription":
        """Create a TestDescription instance from a protobuf TestDescription message."""
        test_description = TestDescription(
            uut_id=test_description_proto.uut_id,
            name=test_description_proto.name,
            link=test_description_proto.link,
            schema_id=test_description_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            test_description.extension, test_description_proto.extension
        )
        test_description._id = test_description_proto.id
        return test_description

    def to_protobuf(self) -> TestDescriptionProto:
        """Convert this TestDescription to a protobuf TestDescription message."""
        test_description_proto = TestDescriptionProto(
            id=self.id,
            uut_id=self.uut_id,
            name=self.name,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(test_description_proto.extension, self.extension)
        return test_description_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, TestDescription):
            return NotImplemented
        return (
            self.id == other.id
            and self.uut_id == other.uut_id
            and self.name == other.name
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the TestDescription."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_test_station.py sha256=fb0f4544b068d20a00b244b1c962f99ecc91230f364f7961224c14e45b50778c bytes=4132 -->
## FILE: src/ni/datastore/metadata/_types/_test_station.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_test_station.py`
- sha256: `fb0f4544b068d20a00b244b1c962f99ecc91230f364f7961224c14e45b50778c`
- bytes: 4132

````python
"""Test Station data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    TestStation as TestStationProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class TestStation:
    """Represents the metadata of a test station.

    A test station contains information about the physical location or setup
    where testing is performed, including its name and asset identifier for
    tracking and inventory purposes.


    """

    __slots__ = (
        "_id",
        "name",
        "asset_identifier",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the test station."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the test station."""
        return self._id

    def __init__(
        self,
        *,
        name: str = "",
        asset_identifier: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a TestStation instance.

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
        """
        self._id = ""
        self.name = name
        self.asset_identifier = asset_identifier
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(test_station_proto: TestStationProto) -> "TestStation":
        """Create a TestStation instance from a protobuf TestStation message."""
        test_station = TestStation(
            name=test_station_proto.name,
            asset_identifier=test_station_proto.asset_identifier,
            link=test_station_proto.link,
            schema_id=test_station_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            test_station.extension, test_station_proto.extension
        )
        test_station._id = test_station_proto.id
        return test_station

    def to_protobuf(self) -> TestStationProto:
        """Convert this TestStation to a protobuf TestStation message."""
        test_station_proto = TestStationProto(
            id=self.id,
            name=self.name,
            asset_identifier=self.asset_identifier,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(test_station_proto.extension, self.extension)
        return test_station_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, TestStation):
            return NotImplemented
        return (
            self.id == other.id
            and self.name == other.name
            and self.asset_identifier == other.asset_identifier
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the TestStation."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_uut.py sha256=aac1f2fe3f68fbc5c779d00f4da69c11a2d771fbd9b1c5f3e1089f29a91df2f2 bytes=4678 -->
## FILE: src/ni/datastore/metadata/_types/_uut.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_uut.py`
- sha256: `aac1f2fe3f68fbc5c779d00f4da69c11a2d771fbd9b1c5f3e1089f29a91df2f2`
- bytes: 4678

````python
"""UUT data type for the Data Store Client."""

from __future__ import annotations

from typing import Iterable, Mapping, MutableMapping, MutableSequence

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    Uut as UutProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class Uut:
    """Represents the metadata of a Unit Under Test (UUT).

    A UUT represents a model or type of device that can be tested, containing
    information like model name, family, manufacturers, and part number that
    describe the UUT type rather than specific instances.


    """

    __slots__ = (
        "_id",
        "model_name",
        "family",
        "_manufacturers",
        "part_number",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def manufacturers(self) -> MutableSequence[str]:
        """The manufacturers of the UUT."""
        return self._manufacturers

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the UUT."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the uut."""
        return self._id

    def __init__(
        self,
        *,
        model_name: str = "",
        family: str = "",
        manufacturers: Iterable[str] | None = None,
        part_number: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a Uut instance.

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
        """
        self._id = ""
        self.model_name = model_name
        self.family = family
        self._manufacturers: MutableSequence[str] = (
            list(manufacturers) if manufacturers is not None else []
        )
        self.part_number = part_number
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(uut_proto: UutProto) -> "Uut":
        """Create a Uut instance from a protobuf Uut message."""
        uut = Uut(
            model_name=uut_proto.model_name,
            family=uut_proto.family,
            manufacturers=uut_proto.manufacturers,
            part_number=uut_proto.part_number,
            link=uut_proto.link,
            schema_id=uut_proto.schema_id,
        )
        populate_from_extension_value_message_map(uut.extension, uut_proto.extension)
        uut._id = uut_proto.id
        return uut

    def to_protobuf(self) -> UutProto:
        """Convert this Uut to a protobuf Uut message."""
        uut_proto = UutProto(
            id=self.id,
            model_name=self.model_name,
            family=self.family,
            manufacturers=self.manufacturers,
            part_number=self.part_number,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(uut_proto.extension, self.extension)
        return uut_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, Uut):
            return NotImplemented
        return (
            self.id == other.id
            and self.model_name == other.model_name
            and self.family == other.family
            and self.manufacturers == other.manufacturers
            and self.part_number == other.part_number
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the Uut."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/_uut_instance.py sha256=76d2d3c78340b323936d0caa8f261874bc5a884cec9291ab1b0978491a2881ba bytes=5368 -->
## FILE: src/ni/datastore/metadata/_types/_uut_instance.py

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/_uut_instance.py`
- sha256: `76d2d3c78340b323936d0caa8f261874bc5a884cec9291ab1b0978491a2881ba`
- bytes: 5368

````python
"""UUT Instance data type for the Data Store Client."""

from __future__ import annotations

from typing import Mapping, MutableMapping

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    UutInstance as UutInstanceProto,
)

from ni.datastore.metadata._grpc_conversion import (
    populate_extension_value_message_map,
    populate_from_extension_value_message_map,
)


class UutInstance:
    """Represents the metadata of a UUT instance.

    A UUT instance represents a specific physical instance of a Unit Under
    Test, with properties like serial number, manufacture date, and firmware
    version that distinguish it from other instances of the same UUT model.


    """

    __slots__ = (
        "_id",
        "uut_id",
        "serial_number",
        "manufacture_date",
        "firmware_version",
        "hardware_version",
        "link",
        "_extension",
        "schema_id",
    )

    @property
    def extension(self) -> MutableMapping[str, str]:
        """The extension of the UUT instance."""
        return self._extension

    @property
    def id(self) -> str:
        """The string id of the uut instance."""
        return self._id

    def __init__(
        self,
        *,
        uut_id: str = "",
        serial_number: str = "",
        manufacture_date: str = "",
        firmware_version: str = "",
        hardware_version: str = "",
        link: str = "",
        extension: Mapping[str, str] | None = None,
        schema_id: str = "",
    ) -> None:
        """Initialize a UutInstance instance.

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
        """
        self._id = ""
        self.uut_id = uut_id
        self.serial_number = serial_number
        self.manufacture_date = manufacture_date
        self.firmware_version = firmware_version
        self.hardware_version = hardware_version
        self.link = link
        self._extension: MutableMapping[str, str] = dict(extension) if extension is not None else {}
        self.schema_id = schema_id

    @staticmethod
    def from_protobuf(uut_instance_proto: UutInstanceProto) -> "UutInstance":
        """Create a UutInstance from a protobuf UutInstance message."""
        uut_instance = UutInstance(
            uut_id=uut_instance_proto.uut_id,
            serial_number=uut_instance_proto.serial_number,
            manufacture_date=uut_instance_proto.manufacture_date,
            firmware_version=uut_instance_proto.firmware_version,
            hardware_version=uut_instance_proto.hardware_version,
            link=uut_instance_proto.link,
            schema_id=uut_instance_proto.schema_id,
        )
        populate_from_extension_value_message_map(
            uut_instance.extension, uut_instance_proto.extension
        )
        uut_instance._id = uut_instance_proto.id
        return uut_instance

    def to_protobuf(self) -> UutInstanceProto:
        """Convert this UutInstance to a protobuf UutInstance message."""
        uut_instance_proto = UutInstanceProto(
            id=self.id,
            uut_id=self.uut_id,
            serial_number=self.serial_number,
            manufacture_date=self.manufacture_date,
            firmware_version=self.firmware_version,
            hardware_version=self.hardware_version,
            link=self.link,
            schema_id=self.schema_id,
        )
        populate_extension_value_message_map(uut_instance_proto.extension, self.extension)
        return uut_instance_proto

    def __eq__(self, other: object) -> bool:
        """Determine equality."""
        if not isinstance(other, UutInstance):
            return NotImplemented
        return (
            self.id == other.id
            and self.uut_id == other.uut_id
            and self.serial_number == other.serial_number
            and self.manufacture_date == other.manufacture_date
            and self.firmware_version == other.firmware_version
            and self.hardware_version == other.hardware_version
            and self.link == other.link
            and self.extension == other.extension
            and self.schema_id == other.schema_id
        )

    def __str__(self) -> str:
        """Return a string representation of the UutInstance."""
        return str(self.to_protobuf())
````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/_types/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/ni/datastore/metadata/_types/py.typed

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/_types/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/metadata/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/ni/datastore/metadata/py.typed

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/metadata/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=datastore-python path=src/ni/datastore/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/ni/datastore/py.typed

- repository: `ni/datastore-python`
- source_path: `src/ni/datastore/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/__init__.py sha256=14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a bytes=14 -->
## FILE: tests/__init__.py

- repository: `ni/datastore-python`
- source_path: `tests/__init__.py`
- sha256: `14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a`
- bytes: 14

````python
"""Tests."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/__init__.py sha256=876e04c20a2a4da1b2247c54e30baed86c9143aab8daf18a4e31e6974f7b8ce5 bytes=25 -->
## FILE: tests/acceptance/__init__.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/__init__.py`
- sha256: `876e04c20a2a4da1b2247c54e30baed86c9143aab8daf18a4e31e6974f7b8ce5`
- bytes: 25

````python
"""Acceptance Tests."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/_utils.py sha256=9d62927324fb46c6326db0c879dd307d9170fbbe1d12ac5dd69cb37a633f18e1 bytes=1162 -->
## FILE: tests/acceptance/_utils.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/_utils.py`
- sha256: `9d62927324fb46c6326db0c879dd307d9170fbbe1d12ac5dd69cb37a633f18e1`
- bytes: 1162

````python
"""Acceptance test utility functions."""

import datetime as dt

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def create_test_result_and_step(data_store_client: DataStoreClient, description: str) -> str:
    """Create a single step within a single test result and return the step_id."""
    test_result_id = create_test_result(data_store_client, description)

    step = Step(name=f"{description} step", test_result_id=test_result_id)
    step_id = data_store_client.create_step(step)
    return step_id


def create_test_result(data_store_client: DataStoreClient, description: str) -> str:
    """Create a single TestResult and return that test result's id."""
    test_result_name = f"{description} test result"
    test_result = TestResult(name=test_result_name)
    test_result_id = data_store_client.create_test_result(test_result)
    return test_result_id


def append_hashed_time(base_string: str) -> str:
    """Append the hash of the current time to a given string."""
    current_time = dt.datetime.now()
    time_hash = hash(current_time)
    return f"{base_string}-{time_hash}"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/conftest.py sha256=56bb1a24f832fde66fd86b925490aede407e3b70c889b9d5f126a2470e26e4e3 bytes=466 -->
## FILE: tests/acceptance/conftest.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/conftest.py`
- sha256: `56bb1a24f832fde66fd86b925490aede407e3b70c889b9d5f126a2470e26e4e3`
- bytes: 466

````python
"""Contains test fixtures used by the data store and metadata store acceptance tests."""

from typing import Generator

import pytest
from utilities import DataStoreContext


@pytest.fixture(scope="module")
def acceptance_test_context() -> Generator[DataStoreContext, None, None]:
    """Returns the pytest fixture for launching the data store in a testing context."""
    with DataStoreContext() as data_store_context:
        yield data_store_context
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/schemas/extensions.toml sha256=699ba2fe018f283b5b1c1dfb938d48c7826f2c28171d9e5484097ffa7100d252 bytes=429 -->
## FILE: tests/acceptance/schemas/extensions.toml

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/schemas/extensions.toml`
- sha256: `699ba2fe018f283b5b1c1dfb938d48c7826f2c28171d9e5484097ffa7100d252`
- bytes: 429

````toml
id = "https://acceptancetests.com/custommetadata.schema.toml"

[uut]
u1 = "*"
u2 = "*"

[uut_instance]
ui1 = "*"
ui2 = "*"

[operator]
o1 = "*"
o2 = "*"

[test_station]
ts1 = "*"
ts2 = "*"

[test_description]
td1 = "*"
td2 = "*"

[software_item]
sw1 = "*"
sw2 = "*"

[hardware_item]
hw1 = "*"
hw2 = "*"

[test_result]
tr1 = "*"
tr2 = "*"

[step]
s1 = "*"
s2 = "*"

[test]
t1 = "*"
t2 = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_publish_condition_and_read_data.py sha256=b4da72951509840cac89598dac7f9d6813cb070bf3b341a27db29d5470c79801 bytes=5035 -->
## FILE: tests/acceptance/test_publish_condition_and_read_data.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_publish_condition_and_read_data.py`
- sha256: `b4da72951509840cac89598dac7f9d6813cb070bf3b341a27db29d5470c79801`
- bytes: 5035

````python
"""Acceptance tests that publish various condition values then read the data back."""

from nitypes.scalar import Scalar
from nitypes.vector import Vector
from utilities import DataStoreContext

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def test___publish_float_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "float condition")
        published_condition_id = data_store_client.publish_condition(
            name="python float condition",
            condition_type="Upper Limit",
            value=123.45,
            step_id=step_id,
        )

        # A published float will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert len(vector) == 1
        assert vector[0] == 123.45
        assert vector.units == ""


def test___publish_integer_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "integer condition")
        published_condition_id = data_store_client.publish_condition(
            name="python integer condition",
            condition_type="Lower Limit",
            value=123,
            step_id=step_id,
        )

        # A published integer will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert len(vector) == 1
        assert vector[0] == 123
        assert vector.units == ""


def test___publish_bool_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "bool condition")
        published_condition_id = data_store_client.publish_condition(
            name="python bool condition",
            condition_type="Flag",
            value=True,
            step_id=step_id,
        )

        # A published bool will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert len(vector) == 1
        assert vector[0] is True
        assert vector.units == ""


def test___publish_str_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "str condition")
        published_condition_id = data_store_client.publish_condition(
            name="python str condition",
            condition_type="Environment",
            value="condition value",
            step_id=step_id,
        )

        # A published str will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert len(vector) == 1
        assert vector[0] == "condition value"
        assert vector.units == ""


def test___publish_scalar_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "scalar condition")
        expected_scalar = Scalar(value=25, units="Volts")
        published_condition_id = data_store_client.publish_condition(
            name="python scalar condition",
            condition_type="Lower Limit",
            value=expected_scalar,
            step_id=step_id,
        )

        # A published Scalar will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector[0] == expected_scalar.value
        assert vector.units == expected_scalar.units


def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str:
    test_result_name = f"python publish {datatype_string} acceptance test"
    test_result = TestResult(name=test_result_name)
    test_result_id = data_store_client.create_test_result(test_result)

    # Publish the waveform data
    step = Step(name=f"Initial step: {datatype_string}", test_result_id=test_result_id)
    step_id = data_store_client.create_step(step)
    return step_id
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_publish_condition_batch_and_read_data.py sha256=92d91c5028005fe28e9662ec1a5b357d9205bf9ae1f66bbcebf593ded0c69c5c bytes=5207 -->
## FILE: tests/acceptance/test_publish_condition_batch_and_read_data.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_publish_condition_batch_and_read_data.py`
- sha256: `92d91c5028005fe28e9662ec1a5b357d9205bf9ae1f66bbcebf593ded0c69c5c`
- bytes: 5207

````python
"""Acceptance tests that publish various batch condition values then read the data back."""

from nitypes.vector import Vector
from utilities import DataStoreContext

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def test___publish_batch_float_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    expected_value = [1.0, 2.0, 3.0]
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "float condition batch")
        published_condition_id = data_store_client.publish_condition_batch(
            name="python float condition batch",
            condition_type="Upper Limits",
            values=expected_value,
            step_id=step_id,
        )

        # A batch published float will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector._values == expected_value
        assert vector.units == ""


def test___publish_batch_integer_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    expected_value = [5, 6, 7, 8]
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "integer condition batch")
        published_condition_id = data_store_client.publish_condition_batch(
            name="python integer condition batch",
            condition_type="Lower Limits",
            values=expected_value,
            step_id=step_id,
        )

        # A batch published integer will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector._values == expected_value
        assert vector.units == ""


def test___publish_batch_bool_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    expected_value = [True, False, True]
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "bool condition batch")
        published_condition_id = data_store_client.publish_condition_batch(
            name="python bool condition batch",
            condition_type="Flags",
            values=expected_value,
            step_id=step_id,
        )

        # A batch published bool will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector._values == expected_value
        assert vector.units == ""


def test___publish_batch_str_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    expected_value = ["one", "two", "three"]
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "str condition batch")
        published_condition_id = data_store_client.publish_condition_batch(
            name="python str condition batch",
            condition_type="Environments",
            values=expected_value,
            step_id=step_id,
        )

        # A published str will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector._values == expected_value
        assert vector.units == ""


def test___publish_batch_vector_condition___read_condition_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "scalar condition batch")
        expected_vector = Vector(values=[25, 50, 75], units="Amps")
        published_condition_id = data_store_client.publish_condition_batch(
            name="python vector condition batch",
            condition_type="Upper Limit",
            values=expected_vector,
            step_id=step_id,
        )

        # A batch published Vector will be read back as a Vector.
        published_condition = data_store_client.get_condition(published_condition_id)
        vector = data_store_client.read_condition_value(published_condition, expected_type=Vector)
        assert vector == expected_vector


def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str:
    test_result_name = f"python publish {datatype_string} acceptance test"
    test_result = TestResult(name=test_result_name)
    test_result_id = data_store_client.create_test_result(test_result)

    # Publish the waveform data
    step = Step(name=f"Initial step: {datatype_string}", test_result_id=test_result_id)
    step_id = data_store_client.create_step(step)
    return step_id
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_publish_measurement_and_read_data.py sha256=f54e9514f586f23743972a6706cdec8d277f78d163142e888c61c4f1f9e0574e bytes=7315 -->
## FILE: tests/acceptance/test_publish_measurement_and_read_data.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_publish_measurement_and_read_data.py`
- sha256: `f54e9514f586f23743972a6706cdec8d277f78d163142e888c61c4f1f9e0574e`
- bytes: 7315

````python
"""Acceptance tests that publish various values then reads the data back."""

import hightime as ht
import numpy as np
from nitypes.scalar import Scalar
from nitypes.vector import Vector
from nitypes.waveform import (
    AnalogWaveform,
    ComplexWaveform,
    DigitalWaveform,
    SampleIntervalMode,
    Spectrum,
    Timing,
)
from nitypes.xy_data import XYData
from utilities import DataStoreContext

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def test___publish_float___read_measurement_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "float")
        published_measurement_id = data_store_client.publish_measurement(
            name="python publish float",
            value=123.45,
            step_id=step_id,
        )

        # A published integer will be read back as a Vector.
        published_measurement = data_store_client.get_measurement(published_measurement_id)
        vector = data_store_client.read_measurement_value(
            published_measurement, expected_type=Vector
        )
        assert vector[0] == 123.45
        assert vector.units == ""


def test___publish_scalar___read_measurement_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "scalar")
        expected_scalar = Scalar(value=25, units="Volts")
        published_measurement_id = data_store_client.publish_measurement(
            name="python publish scalar",
            value=expected_scalar,
            step_id=step_id,
        )

        # A published Scalar will be read back as a Vector.
        published_measurement = data_store_client.get_measurement(published_measurement_id)
        vector = data_store_client.read_measurement_value(
            published_measurement, expected_type=Vector
        )
        assert vector[0] == expected_scalar.value
        assert vector.units == expected_scalar.units


def test___publish_xydata___read_measurement_value_returns_xydata(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "xydata")
        expected_xydata = XYData.from_arrays_1d(
            x_array=[1.0, 2.0],
            y_array=[3.0, 4.0],
            dtype=np.float64,
            x_units="Amps",
            y_units="Seconds",
        )
        published_measurement_id = data_store_client.publish_measurement(
            name="python publish xydata",
            value=expected_xydata,
            step_id=step_id,
        )

        published_measurement = data_store_client.get_measurement(published_measurement_id)
        xydata = data_store_client.read_measurement_value(
            published_measurement, expected_type=XYData
        )
        assert xydata == expected_xydata


def test___publish_spectrum___read_measurement_value_returns_spectrum(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "spectrum")
        expected_spectrum = Spectrum.from_array_1d(
            array=[1.0, 10.0, 100.0],
            dtype=np.float64,
            start_frequency=1.0,
            frequency_increment=1.0,
        )

        published_measurement_id = data_store_client.publish_measurement(
            name="python publish spectrum",
            value=expected_spectrum,
            step_id=step_id,
        )

        published_measurement = data_store_client.get_measurement(published_measurement_id)
        spectrum = data_store_client.read_measurement_value(
            published_measurement, expected_type=Spectrum
        )
        assert spectrum == expected_spectrum


def test___publish_analog_waveform___read_measurement_value_returns_analog_waveform(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "analog waveform")
        expected_waveform = AnalogWaveform(
            sample_count=3,
            raw_data=np.array([1.0, 2.0, 3.0]),
            timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
        )

        published_measurement_id = data_store_client.publish_measurement(
            name="python publish analog waveform",
            value=expected_waveform,
            step_id=step_id,
        )

        published_measurement = data_store_client.get_measurement(published_measurement_id)
        waveform = data_store_client.read_measurement_value(
            published_measurement, expected_type=AnalogWaveform
        )
        assert waveform == expected_waveform


def test___publish_digital_waveform___read_measurement_value_returns_digital_waveform(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "digital waveform")
        expected_waveform = DigitalWaveform(
            10,
            timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
        )
        published_measurement_id = data_store_client.publish_measurement(
            name="python publish digital waveform",
            value=expected_waveform,
            step_id=step_id,
        )

        published_measurement = data_store_client.get_measurement(published_measurement_id)
        waveform = data_store_client.read_measurement_value(
            published_measurement, expected_type=DigitalWaveform
        )
        assert waveform == expected_waveform


def test___publish_complex_waveform___read_measurement_value_returns_complex_waveform(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = _create_step(data_store_client, "complex waveform")
        expected_waveform = ComplexWaveform(
            10,
            timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
        )
        published_measurement_id = data_store_client.publish_measurement(
            name="python publish complex waveform",
            value=expected_waveform,
            step_id=step_id,
        )

        published_measurement = data_store_client.get_measurement(published_measurement_id)
        waveform = data_store_client.read_measurement_value(
            published_measurement, expected_type=ComplexWaveform
        )
        assert waveform == expected_waveform


def _create_step(data_store_client: DataStoreClient, datatype_string: str) -> str:
    test_result_name = f"python publish {datatype_string} acceptance test"
    test_result = TestResult(name=test_result_name)
    test_result_id = data_store_client.create_test_result(test_result)

    # Publish the waveform data
    step = Step(name=f"Initial step: {datatype_string}", test_result_id=test_result_id)
    step_id = data_store_client.create_step(step)
    return step_id
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_publish_measurement_batch_and_read_data.py sha256=488b327ed3b7d72a641521a64cf62a9dd826e7e4be4702be70d1c082fe4259e6 bytes=6869 -->
## FILE: tests/acceptance/test_publish_measurement_batch_and_read_data.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_publish_measurement_batch_and_read_data.py`
- sha256: `488b327ed3b7d72a641521a64cf62a9dd826e7e4be4702be70d1c082fe4259e6`
- bytes: 6869

````python
"""Acceptance tests that publish various batch measurement values then reads the data back."""

import hightime as ht
import numpy as np
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform, NoneScaleMode, SampleIntervalMode, Timing
from utilities import DataStoreContext

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def test___publish_batch_floats___read_measurement_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        # Create TestResult metadata
        test_result_name = "python publish batch floats acceptance test"
        test_result = TestResult(name=test_result_name)
        test_result_id = data_store_client.create_test_result(test_result)

        # Publish the waveform data
        step = Step(name="Initial step", test_result_id=test_result_id)
        step_id = data_store_client.create_step(step)
        published_measurement_ids = data_store_client.publish_measurement_batch(
            name="Test measurement",
            values=[1.0, 2.0, 3.0, 4.0],
            step_id=step_id,
        )
        published_measurement_id = next(iter(published_measurement_ids), None)
        assert published_measurement_id is not None and published_measurement_id != ""

        # Get the published measurement object to read data from it
        published_measurement = data_store_client.get_measurement(published_measurement_id)

        # A published batch floats will be read back as a Vector.
        vector = data_store_client.read_measurement_value(
            published_measurement, expected_type=Vector
        )
        assert vector._values == [1.0, 2.0, 3.0, 4.0]
        assert vector.units == ""


def test___publish_batch_vector___read_measurement_value_returns_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        # Create TestResult metadata
        test_result_name = "python publish batch Vector acceptance test"
        test_result = TestResult(name=test_result_name)
        test_result_id = data_store_client.create_test_result(test_result)

        # Create a Vector data to publish
        expected_vector = Vector(values=[1, 2, 3], units="Volts")

        # Batch publish the vector
        step = Step(name="Initial step", test_result_id=test_result_id)
        step_id = data_store_client.create_step(step)
        published_measurement_ids = data_store_client.publish_measurement_batch(
            name="Test measurement",
            values=expected_vector,
            step_id=step_id,
        )
        published_measurement_id = next(iter(published_measurement_ids), None)
        assert published_measurement_id is not None and published_measurement_id != ""

        # Get the published measurement object to read data from it
        published_measurement = data_store_client.get_measurement(published_measurement_id)

        # A batch published Vector will be read back as a Vector.
        vector = data_store_client.read_measurement_value(
            published_measurement, expected_type=Vector
        )
        assert vector == expected_vector


def test___publish_batch_double_analog_waveforms___read_measurement_value_returns_each_analog_waveform(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        test_result_name = "python publish batch AnalogWaveforms acceptance test"
        test_result = TestResult(name=test_result_name)
        test_result_id = data_store_client.create_test_result(test_result)
        expected_waveforms = [
            AnalogWaveform(
                sample_count=3,
                raw_data=np.array([1.0, 2.0, 3.0]),
                scale_mode=NoneScaleMode(),
                timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
            ),
            AnalogWaveform(
                sample_count=3,
                raw_data=np.array([4.0, 5.0, 6.0]),
                scale_mode=NoneScaleMode(),
                timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
            ),
        ]
        step = Step(name="Initial step", test_result_id=test_result_id)
        step_id = data_store_client.create_step(step)

        published_measurement_ids = data_store_client.publish_measurement_batch(
            name="Test measurement",
            values=expected_waveforms,
            step_id=step_id,
        )

        assert len(published_measurement_ids) == 2
        published_measurement_one = data_store_client.get_measurement(published_measurement_ids[0])
        published_measurement_two = data_store_client.get_measurement(published_measurement_ids[1])
        published_waveform_one = data_store_client.read_measurement_value(
            published_measurement_one, expected_type=AnalogWaveform
        )
        published_waveform_two = data_store_client.read_measurement_value(
            published_measurement_two, expected_type=AnalogWaveform
        )
        assert published_waveform_one == expected_waveforms[0]
        assert published_waveform_two == expected_waveforms[1]


def test___publish_batch_vectors___read_measurement_value_returns_each_vector(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        test_result_name = "python publish batch Vectors acceptance test"
        test_result = TestResult(name=test_result_name)
        test_result_id = data_store_client.create_test_result(test_result)
        expected_vectors = [
            Vector(values=[1, 2, 3], units="Volts"),
            Vector(values=[4, 5, 6], units="Volts"),
        ]
        step = Step(name="Initial step", test_result_id=test_result_id)
        step_id = data_store_client.create_step(step)

        published_measurement_ids = data_store_client.publish_measurement_batch(
            name="Test measurement",
            values=expected_vectors,
            step_id=step_id,
        )

        assert len(published_measurement_ids) == 2
        published_measurement_one = data_store_client.get_measurement(published_measurement_ids[0])
        published_measurement_two = data_store_client.get_measurement(published_measurement_ids[1])
        published_vector_one = data_store_client.read_measurement_value(
            published_measurement_one, expected_type=Vector
        )
        published_vector_two = data_store_client.read_measurement_value(
            published_measurement_two, expected_type=Vector
        )
        assert published_vector_one == expected_vectors[0]
        assert published_vector_two == expected_vectors[1]
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_publish_with_metadata.py sha256=95178133f5132a2c59b0390d94642432e21b0bdb73c40663f0d88e7ab37682b3 bytes=13684 -->
## FILE: tests/acceptance/test_publish_with_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_publish_with_metadata.py`
- sha256: `95178133f5132a2c59b0390d94642432e21b0bdb73c40663f0d88e7ab37682b3`
- bytes: 13684

````python
"""Acceptance test that publishes then queries waveform data and metadata."""

import datetime as dt
import os

import hightime as ht
import numpy as np
from nitypes.waveform import AnalogWaveform, NoneScaleMode, Timing, SampleIntervalMode
from utilities import DataStoreContext

from ni.datastore.data import (
    DataStoreClient,
    ErrorInformation,
    Outcome,
    Step,
    TestResult,
)
from ni.datastore.metadata import (
    HardwareItem,
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    Test,
    TestAdapter,
    TestDescription,
    TestStation,
    Uut,
    UutInstance,
)


def test___waveform_with_all_metadata___publish___query_read_returns_correct_data(
    acceptance_test_context: DataStoreContext,
) -> None:
    with MetadataStoreClient() as metadata_store_client, DataStoreClient() as data_store_client:
        # Load the extensions schema
        current_directory = os.path.dirname(os.path.abspath(__file__))
        schema_id = metadata_store_client.register_schema_from_file(
            os.path.join(current_directory, "schemas", "extensions.toml")
        )

        # Metadata: UUT
        uut = Uut(
            model_name="NI-9205",
            family="Analog",
            manufacturers=["Manufacturer A", "Manufacturer B"],
            part_number="Part Number",
            link="Uut Link",
            extension={"u1": "one", "u2": "two"},
            schema_id=schema_id,
        )
        uut_id = metadata_store_client.create_uut(uut)

        # Metadata: UUTInstance
        uut_instance = UutInstance(
            uut_id=uut_id,
            serial_number="A861-12345",
            manufacture_date="Manufacture Date",
            firmware_version="Firmware Version",
            hardware_version="Hardware Version",
            link="UutInstance Link",
            extension={"ui1": "one", "ui2": "two"},
            schema_id=schema_id,
        )
        uut_instance_id = metadata_store_client.create_uut_instance(uut_instance=uut_instance)

        # Metadata: Operator
        operator_name = "John Bowery"
        operator_role = "Test Operator II"
        operator = Operator(
            name=operator_name,
            role=operator_role,
            extension={"o1": "one", "o2": "two"},
            schema_id=schema_id,
        )
        operator_id = metadata_store_client.create_operator(operator)

        # Metadata: TestStation
        test_station = TestStation(
            name="TestStation_12",
            asset_identifier="Test Station Asset Identifier",
            link="Test Station Link",
            extension={"ts1": "one", "ts2": "two"},
            schema_id=schema_id,
        )
        test_station_id = metadata_store_client.create_test_station(test_station)

        # Metadata: TestDescription
        test_description = TestDescription(
            uut_id=uut_id,
            name="Metadata Acceptance Test",
            link="Test Description Link",
            extension={"td1": "one", "td2": "two"},
            schema_id=schema_id,
        )
        test_description_id = metadata_store_client.create_test_description(test_description)

        # Metadata: SoftwareItem
        software_item = SoftwareItem(
            product="Windows",
            version="10.0.19044",
            link="Windows Link",
            extension={"sw1": "one", "sw2": "two"},
            schema_id=schema_id,
        )
        software_item_id = metadata_store_client.create_software_item(software_item)
        software_item_ids = [software_item_id]

        # Metadata: HardwareItem
        hardware_item = HardwareItem(
            manufacturer="Test Manufacturer",
            model="Test Model",
            serial_number="Test Serial Number",
            part_number="Test Part Number",
            asset_identifier="Test Asset Identifier",
            calibration_due_date="Test Calibration Due Date",
            link="Hardware Item Link",
            extension={"hw1": "one", "hw2": "two"},
            schema_id=schema_id,
        )
        hardware_item_id = metadata_store_client.create_hardware_item(hardware_item)
        hardware_item_ids = [hardware_item_id]

        # Metadata: TestAdapter
        test_adapter = TestAdapter(
            name="Test Adapter Name",
            manufacturer="Test Adapter Manufacturer",
            serial_number="Test Adapter Serial Number",
            part_number="Test Adapter Part Number",
            asset_identifier="Test Adapter Asset Identifier",
            calibration_due_date="Test Adapter Calibration Due Date",
            link="Test Adapter Link",
        )
        test_adapter_id = metadata_store_client.create_test_adapter(test_adapter)
        test_adapter_ids = [test_adapter_id]

        # Metadata: TestResult
        test_result_name = "sample test result"
        test_result = TestResult(
            name=test_result_name,
            uut_instance_id=uut_instance_id,
            operator_id=operator_id,
            test_station_id=test_station_id,
            test_description_id=test_description_id,
            software_item_ids=software_item_ids,
            hardware_item_ids=hardware_item_ids,
            test_adapter_ids=test_adapter_ids,
            link="Test Result Link",
            extension={"tr1": "one", "tr2": "two"},
            schema_id=schema_id,
        )
        test_result_id = data_store_client.create_test_result(test_result)

        # Data: Waveform data to publish
        expected_waveform = AnalogWaveform(
            sample_count=3,
            raw_data=np.array([1.0, 2.0, 3.0]),
            scale_mode=NoneScaleMode(),
            timing=Timing(SampleIntervalMode.NONE, time_offset=ht.timedelta()),
        )

        # Metadata: Test
        test = Test(
            name="Test Name",
            description="Test Description",
            link="Test Link",
            extension={"t1": "one", "t2": "two"},
            schema_id=schema_id,
        )
        test_id = metadata_store_client.create_test(test)

        # Data: Step
        parent_step = Step(name="Parent Step")
        step = Step(
            name="Step Name",
            parent_step_id=parent_step.id,
            test_result_id=test_result_id,
            test_id=test_id,
            step_type="Step Type",
            notes="Step Notes",
            link="Step Link",
            extension={"s1": "one", "s2": "two"},
            schema_id=schema_id,
        )
        step_id = data_store_client.create_step(step)

        timestamp = ht.datetime.now(tz=dt.timezone.utc)
        error_information = ErrorInformation(
            error_code=123, message="Error Message", source="Error Source"
        )

        # Perform publish operation
        published_measurement_id = data_store_client.publish_measurement(
            name="Measurement Name",
            value=expected_waveform,
            step_id=step_id,
            timestamp=timestamp,
            outcome=Outcome.PASSED,
            error_information=error_information,
            hardware_item_ids=hardware_item_ids,
            test_adapter_ids=test_adapter_ids,
            software_item_ids=software_item_ids,
            notes="Measurement Notes",
        )

        published_measurements = data_store_client.query_measurements(
            odata_query=f"$filter=id eq {published_measurement_id}"
        )
        found_measurement = next(iter(published_measurements), None)
        assert found_measurement is not None

        # Check PublishedMeasurement
        assert found_measurement.notes == "Measurement Notes"
        assert found_measurement.name == "Measurement Name"
        assert sorted(found_measurement.software_item_ids) == sorted(software_item_ids)
        assert sorted(found_measurement.hardware_item_ids) == sorted(hardware_item_ids)
        assert found_measurement.test_adapter_ids == test_adapter_ids
        assert found_measurement.error_information == error_information
        assert found_measurement.outcome == Outcome.PASSED
        assert isinstance(found_measurement.start_date_time, ht.datetime)
        # We can't directly compare these datetimes because of bruising when converting
        # to bintime and back.
        assert found_measurement.start_date_time.day == timestamp.day

        # Check TestResult
        found_test_result = data_store_client.get_test_result(found_measurement.test_result_id)
        assert found_test_result.name == test_result_name
        assert found_test_result.operator_id == operator_id
        assert sorted(found_test_result.software_item_ids) == sorted(software_item_ids)
        assert sorted(found_test_result.hardware_item_ids) == sorted(hardware_item_ids)
        # assert sorted(queried_test_result.test_adapter_ids) == sorted(test_adapter_ids)
        assert found_test_result.test_description_id == test_description_id
        assert found_test_result.test_station_id == test_station_id
        assert found_test_result.uut_instance_id == uut_instance_id
        assert found_test_result.extension == test_result.extension

        # Check Step
        found_step = data_store_client.get_step(found_measurement.step_id)
        assert found_step.parent_step_id == step.parent_step_id
        assert found_step.test_result_id == step.test_result_id
        assert found_step.test_id == step.test_id
        assert found_step.name == step.name
        assert found_step.step_type == step.step_type
        assert found_step.notes == step.notes
        assert found_step.link == step.link
        assert found_step.extension == step.extension

        # Check Test
        found_test = metadata_store_client.get_test(found_step.test_id)
        assert found_test.description == test.description
        assert found_test.name == test.name
        assert found_test.link == test.link
        assert found_test.extension == test.extension

        # Check Operator
        found_operator = metadata_store_client.get_operator(found_test_result.operator_id)
        assert found_operator.name == operator.name
        assert found_operator.role == operator.role
        assert found_operator.extension == operator.extension

        # Check UutInstance
        found_uut_instance = metadata_store_client.get_uut_instance(
            found_test_result.uut_instance_id
        )
        assert found_uut_instance.serial_number == uut_instance.serial_number
        assert found_uut_instance.uut_id == uut_instance.uut_id
        assert found_uut_instance.firmware_version == uut_instance.firmware_version
        assert found_uut_instance.manufacture_date == uut_instance.manufacture_date
        assert found_uut_instance.hardware_version == uut_instance.hardware_version
        assert found_uut_instance.extension == uut_instance.extension

        # Check Uut
        found_uut = metadata_store_client.get_uut(found_uut_instance.uut_id)
        assert found_uut.model_name == uut.model_name
        assert found_uut.family == uut.family
        # TODO: File an issue about found_uut.manufacturers being a blank list.
        # assert found_uut.manufacturers == uut.manufacturers
        assert found_uut.part_number == uut.part_number
        assert found_uut.link == uut.link
        assert found_uut.extension == uut.extension

        # Check TestStation
        found_test_station = metadata_store_client.get_test_station(
            found_test_result.test_station_id
        )
        assert found_test_station.name == test_station.name
        assert found_test_station.asset_identifier == test_station.asset_identifier
        assert found_test_station.link == test_station.link
        assert found_test_station.extension == test_station.extension

        # Check TestDescription
        found_test_description = metadata_store_client.get_test_description(
            found_test_result.test_description_id
        )
        assert found_test_description.name == test_description.name
        assert found_test_description.link == test_description.link
        assert found_test_description.extension == test_description.extension

        # Check SoftwareItem
        found_sw_item = metadata_store_client.get_software_item(
            found_test_result.software_item_ids[0]
        )
        assert found_sw_item.product == software_item.product
        assert found_sw_item.version == software_item.version
        assert found_sw_item.link == software_item.link
        assert found_sw_item.extension == software_item.extension

        # Check HardwareItem
        found_hw_item = metadata_store_client.get_hardware_item(
            found_test_result.hardware_item_ids[0]
        )
        assert found_hw_item.manufacturer == hardware_item.manufacturer
        assert found_hw_item.model == hardware_item.model
        assert found_hw_item.serial_number == hardware_item.serial_number
        assert found_hw_item.part_number == hardware_item.part_number
        assert found_hw_item.asset_identifier == hardware_item.asset_identifier
        assert found_hw_item.calibration_due_date == hardware_item.calibration_due_date
        assert found_hw_item.link == hardware_item.link
        assert found_hw_item.extension == hardware_item.extension

        waveform = data_store_client.read_measurement_value(
            found_measurement, expected_type=AnalogWaveform
        )
        assert waveform == expected_waveform
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_query_conditions.py sha256=26b160e563ba218757ae2d140f0c53b88ceb1ca6b9c80e6da1352c158b26a8c0 bytes=3364 -->
## FILE: tests/acceptance/test_query_conditions.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_query_conditions.py`
- sha256: `26b160e563ba218757ae2d140f0c53b88ceb1ca6b9c80e6da1352c158b26a8c0`
- bytes: 3364

````python
"""Acceptance tests that exercise DataStoreClient.query_conditions()."""

from nitypes.vector import Vector
from utilities import DataStoreContext

from ni.datastore.data import DataStoreClient
from tests.acceptance._utils import append_hashed_time, create_test_result_and_step


def test___query_conditions___filter_by_id___single_condition_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = create_test_result_and_step(data_store_client, "query condition filter by id")

        # Publish a single condition
        condition_name = "query filter by id condition"
        published_condition_id = data_store_client.publish_condition(
            name=condition_name,
            condition_type="Upper Limit",
            value=123.45,
            step_id=step_id,
        )

        # Query conditions based on id.
        queried_conditions = data_store_client.query_conditions(
            odata_query=f"$filter=id eq {published_condition_id}"
        )

        #  We should get one condition back.
        assert len(queried_conditions) == 1
        first_condition = queried_conditions[0]
        assert first_condition is not None
        assert first_condition.name == condition_name

        # Check the value of the queried condition.
        vector = data_store_client.read_condition_value(first_condition, expected_type=Vector)
        assert len(vector) == 1
        assert vector[0] == 123.45
        assert vector.units == ""


def test___query_conditions___filter_by_name___correct_conditions_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = create_test_result_and_step(data_store_client, "query condition filter by name")

        # Publish several similarly named conditions. These names should be unique for each
        # run of this test to prevent previous results from causing the test to fail.
        condition_name_base = append_hashed_time("query filter by name condition")
        for index in range(0, 3):
            condition_name = f"{condition_name_base} {index}"
            data_store_client.publish_condition(
                name=condition_name,
                condition_type="Condition Type",
                value=index,
                step_id=step_id,
            )

        # Publish one differently named condition to adequately test filtering.
        data_store_client.publish_condition(
            name="some other condition",
            condition_type="Condition Type",
            value=123,
            step_id=step_id,
        )

        # Query conditions based on name.
        queried_conditions = data_store_client.query_conditions(
            odata_query=f"$filter=contains(Name,'{condition_name_base}')"
        )

        # We should get three conditions back.
        assert len(queried_conditions) == 3

        # Check the value of each queried condition.
        for condition in queried_conditions:
            assert condition is not None
            vector = data_store_client.read_condition_value(condition, expected_type=Vector)
            assert condition.name == f"{condition_name_base} {vector[0]}"
            assert vector.units == ""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_query_measurements.py sha256=bf2b4e03c810ac121d9fc4fd88db8bac7ae8f83730e711d0e284cc7468b9164d bytes=3294 -->
## FILE: tests/acceptance/test_query_measurements.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_query_measurements.py`
- sha256: `bf2b4e03c810ac121d9fc4fd88db8bac7ae8f83730e711d0e284cc7468b9164d`
- bytes: 3294

````python
"""Acceptance tests that exercise DataStoreClient.query_measurements()."""

from nitypes.vector import Vector
from utilities import DataStoreContext

from ni.datastore.data import DataStoreClient
from tests.acceptance._utils import append_hashed_time, create_test_result_and_step


def test___query_measurements___filter_by_id___single_measurement_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = create_test_result_and_step(data_store_client, "query measurement filter by id")

        # Publish a single measurement.
        measurement_name = "query filter by id measurement"
        published_measurement_id = data_store_client.publish_measurement(
            name=measurement_name,
            value=123.45,
            step_id=step_id,
        )

        # Query measurements based on id.
        queried_measurements = data_store_client.query_measurements(
            odata_query=f"$filter=id eq {published_measurement_id}"
        )

        # We should get one measurement back.
        assert len(queried_measurements) == 1
        first_measurement = queried_measurements[0]
        assert first_measurement is not None
        assert first_measurement.name == measurement_name

        # Check the value of the queried measurement.
        vector = data_store_client.read_measurement_value(first_measurement, expected_type=Vector)
        assert vector[0] == 123.45
        assert vector.units == ""


def test___query_measurements___filter_by_name___correct_measurements_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = create_test_result_and_step(data_store_client, "query measurement filter by name")

        # Publish several similarly named measurements. These names should be unique for each
        # run of this test to prevent previous results from causing the test to fail.
        measurement_name_base = append_hashed_time("query filter by name measurement")
        for index in range(0, 3):
            measurement_name = f"{measurement_name_base} {index}"
            data_store_client.publish_measurement(
                name=measurement_name,
                value=index,
                step_id=step_id,
            )

        # Publish one differently named measurement to adequately test filtering.
        data_store_client.publish_measurement(
            name="some other measurement",
            value=123,
            step_id=step_id,
        )

        # Query measurements based on name.
        queried_measurements = data_store_client.query_measurements(
            odata_query=f"$filter=contains(Name,'{measurement_name_base}')"
        )

        # We should get three measurements back.
        assert len(queried_measurements) == 3

        # Check the value of each queried measurement.
        for measurement in queried_measurements:
            assert measurement is not None
            vector = data_store_client.read_measurement_value(measurement, expected_type=Vector)
            assert measurement.name == f"{measurement_name_base} {vector[0]}"
            assert vector.units == ""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_query_steps.py sha256=8c760471826fd27ab48141a9bc0200c9cd1eb5e45109f82f0f0b71cf73c2cca8 bytes=2255 -->
## FILE: tests/acceptance/test_query_steps.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_query_steps.py`
- sha256: `8c760471826fd27ab48141a9bc0200c9cd1eb5e45109f82f0f0b71cf73c2cca8`
- bytes: 2255

````python
"""Acceptance tests that exercise DataStoreClient.query_steps()."""

from utilities import DataStoreContext

from ni.datastore.data import DataStoreClient, Step, TestResult
from tests.acceptance._utils import append_hashed_time, create_test_result_and_step


def test___query_steps___filter_by_id___single_step_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        step_id = create_test_result_and_step(data_store_client, "query steps filter by id")

        # Query steps based on id.
        queried_steps = data_store_client.query_steps(odata_query=f"$filter=id eq {step_id}")

        # We should get one step back.
        assert len(queried_steps) == 1
        first_step = queried_steps[0]
        assert first_step is not None
        assert first_step.name == "query steps filter by id step"


def test___query_steps___filter_by_name___correct_steps_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        description = "query steps filter by name"
        test_result_name = f"{description} test result"
        test_result = TestResult(name=test_result_name)
        test_result_id = data_store_client.create_test_result(test_result)

        # Create multiple similarly named steps and published a measurement for each.
        step_name_base = append_hashed_time(description)
        for index in range(0, 3):
            step_name = f"{step_name_base} {index}"
            step = Step(name=step_name, test_result_id=test_result_id)
            _ = data_store_client.create_step(step)

        # Create and publish one more step/measurement that doesn't match the naming pattern.
        step = Step(name="some other step name", test_result_id=test_result_id)
        _ = data_store_client.create_step(step)

        # Query steps based on name.
        queried_steps = data_store_client.query_steps(
            odata_query=f"$filter=contains(Name,'{step_name_base}')"
        )

        # We should get three steps back.
        assert len(queried_steps) == 3
        for queried_step in queried_steps:
            assert queried_step is not None
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/acceptance/test_query_test_results.py sha256=cfac0132f2ab9232777988fa8349ec5d8fb8943c32346ae6eb57d95d54238a39 bytes=2133 -->
## FILE: tests/acceptance/test_query_test_results.py

- repository: `ni/datastore-python`
- source_path: `tests/acceptance/test_query_test_results.py`
- sha256: `cfac0132f2ab9232777988fa8349ec5d8fb8943c32346ae6eb57d95d54238a39`
- bytes: 2133

````python
"""Acceptance tests that exercise DataStoreClient.query_test_results()."""

from utilities import DataStoreContext

from ni.datastore.data import DataStoreClient
from tests.acceptance._utils import append_hashed_time, create_test_result


def test___query_test_results___filter_by_id___single_test_result_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        description = "query test result filter by id"
        test_result_id = create_test_result(data_store_client, description)

        # Query test results based on id.
        queried_test_results = data_store_client.query_test_results(
            odata_query=f"$filter=id eq {test_result_id}"
        )

        # We should get one test result back.
        assert len(queried_test_results) == 1
        first_test_result = queried_test_results[0]
        assert first_test_result is not None
        assert first_test_result.name == f"{description} test result"


def test___query_steps___filter_by_name___correct_steps_returned(
    acceptance_test_context: DataStoreContext,
) -> None:
    with DataStoreClient() as data_store_client:
        description = "query test results filter by name"

        # Create multiple similarly named test results.
        test_result_name_base = append_hashed_time(description)
        for index in range(0, 3):
            test_result_name = f"{test_result_name_base} {index}"
            _ = create_test_result(data_store_client, test_result_name)

        # Create one more test result that doesn't match the naming pattern.
        _ = create_test_result(data_store_client, "some other test result name")

        # Query test results based on name.
        queried_test_results = data_store_client.query_test_results(
            odata_query=f"$filter=contains(Name,'{test_result_name_base}')"
        )

        # We should get three test results back.
        assert len(queried_test_results) == 3
        for queried_test_result in queried_test_results:
            assert queried_test_result is not None
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/assets/unit/metadata/schemas/hardware_item_schema.toml sha256=4a55e8ce7ca3fceae6a174497a36d2255cf5c6cf483da716a9a697dc9bc6ec42 bytes=93 -->
## FILE: tests/assets/unit/metadata/schemas/hardware_item_schema.toml

- repository: `ni/datastore-python`
- source_path: `tests/assets/unit/metadata/schemas/hardware_item_schema.toml`
- sha256: `4a55e8ce7ca3fceae6a174497a36d2255cf5c6cf483da716a9a697dc9bc6ec42`
- bytes: 93

````toml
id = "https://example.com/hardware.item.schema.toml"

[hardware_item]
cable_length = "*"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/__init__.py sha256=405938c7e4abf5f5e55e0656625f84385eb85e6453100fada3a3b3f369c284ba bytes=19 -->
## FILE: tests/unit/__init__.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/__init__.py`
- sha256: `405938c7e4abf5f5e55e0656625f84385eb85e6453100fada3a3b3f369c284ba`
- bytes: 19

````python
"""Unit tests."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/conftest.py sha256=e50f3141a7293ae2d073aa1dc8887034971d86109dc6fc911bc6acb6d1d18794 bytes=2441 -->
## FILE: tests/unit/conftest.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/conftest.py`
- sha256: `e50f3141a7293ae2d073aa1dc8887034971d86109dc6fc911bc6acb6d1d18794`
- bytes: 2441

````python
"""Contains test fixtures used by the data store and metadata store unit tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import NonCallableMock

import pytest
from pytest_mock import MockerFixture

from ni.datastore.data import DataStoreClient
from ni.datastore.metadata import MetadataStoreClient


@pytest.fixture
def data_store_client(
    mocked_data_store_service_client: NonCallableMock,
    mocker: MockerFixture,
) -> DataStoreClient:
    """Returns the pytest fixture for the data store client."""
    mocker.patch.object(
        DataStoreClient,
        "_instantiate_data_store_client",
        return_value=mocked_data_store_service_client,
    )
    return DataStoreClient()


@pytest.fixture
def metadata_store_client(
    mocked_metadata_store_service_client: NonCallableMock,
    mocker: MockerFixture,
) -> MetadataStoreClient:
    """Returns the pytest fixture for the metadata store client."""
    mocker.patch.object(
        MetadataStoreClient,
        "_instantiate_metadata_store_client",
        return_value=mocked_metadata_store_service_client,
    )
    return MetadataStoreClient()


@pytest.fixture
def mocked_data_store_service_client(mocker: MockerFixture) -> Any:
    """Returns the pytest fixture for a mocked data store service client."""
    mock_datastore_client = mocker.patch(
        "ni.measurements.data.v1.client.DataStoreClient", autospec=True
    )
    mock_datastore_instance = mock_datastore_client.return_value
    return mock_datastore_instance


@pytest.fixture
def mocked_metadata_store_service_client(mocker: MockerFixture) -> Any:
    """Returns the pytest fixture for a mocked metadata store service client."""
    mock_metadatastore_client = mocker.patch(
        "ni.measurements.metadata.v1.client.MetadataStoreClient", autospec=True
    )
    mock_metadatastore_instance = mock_metadatastore_client.return_value
    return mock_metadatastore_instance


@pytest.fixture(scope="module")
def schemas_directory(test_assets_directory: Path) -> Path:
    """Returns the test assets directory containing schemas."""
    return test_assets_directory / "unit" / "metadata" / "schemas"


@pytest.fixture(scope="module")
def test_assets_directory() -> Path:
    """Returns the test assets directory."""
    return Path(__file__).parent.parent / "assets"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/__init__.py sha256=0b89e1f6a1bd074f99f0905d7d726a1350dc15a85ecd353d1f594ede8d97c1d9 bytes=28 -->
## FILE: tests/unit/data/__init__.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/__init__.py`
- sha256: `0b89e1f6a1bd074f99f0905d7d726a1350dc15a85ecd353d1f594ede8d97c1d9`
- bytes: 28

````python
"""Unit tests for data."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_close_client.py sha256=e4af094f3caf31b7263023742160defb5cee2d2ef25f88a461bf374a37abb15b bytes=1589 -->
## FILE: tests/unit/data/test_close_client.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_close_client.py`
- sha256: `e4af094f3caf31b7263023742160defb5cee2d2ef25f88a461bf374a37abb15b`
- bytes: 1589

````python
"""Contains tests related to closing the DataStoreClient."""

from __future__ import annotations

from unittest.mock import NonCallableMock

import pytest

from ni.datastore.data import DataStoreClient


def test___exit_data_store_client_context___calls_close_on_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    data_store_client.query_measurements()

    with data_store_client:
        pass

    mocked_data_store_service_client.close.assert_called_once()


def test___close_data_store_client___calls_close_on_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    data_store_client.query_measurements()

    data_store_client.close()

    mocked_data_store_service_client.close.assert_called_once()


def test___exit_data_store_client_context___call_method___raises_error(
    data_store_client: DataStoreClient,
) -> None:
    with data_store_client:
        pass

    with pytest.raises(RuntimeError) as exc:
        data_store_client.query_measurements()

    assert exc.value.args[0] == DataStoreClient._DATA_STORE_CLIENT_CLOSED_ERROR


def test___close_data_store_client___call_method___raises_error(
    data_store_client: DataStoreClient,
) -> None:
    data_store_client.close()

    with pytest.raises(RuntimeError) as exc:
        data_store_client.query_measurements()

    assert exc.value.args[0] == DataStoreClient._DATA_STORE_CLIENT_CLOSED_ERROR
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_create_metadata.py sha256=a4573d3828095528b231818b7a714684c423d7331ef998415d7b576bec457ddc bytes=2287 -->
## FILE: tests/unit/data/test_create_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_create_metadata.py`
- sha256: `a4573d3828095528b231818b7a714684c423d7331ef998415d7b576bec457ddc`
- bytes: 2287

````python
"""Contains tests to validate the create_* methods for the data store."""

from __future__ import annotations

from typing import cast
from unittest.mock import NonCallableMock

from ni.measurements.data.v1.data_store_service_pb2 import (
    CreateStepRequest,
    CreateStepResponse,
    CreateTestResultRequest,
    CreateTestResultResponse,
)

from ni.datastore.data import (
    DataStoreClient,
    Step,
    TestResult,
)


def test___create_step___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    step = Step(
        name="step_name",
        id="step_id",
        parent_step_id="parent_step_id",
        test_result_id="test_result",
        test_id="test_id",
        step_type="step_type",
        notes="step_notes",
    )
    expected_response = CreateStepResponse(step_id="response_id")
    mocked_data_store_service_client.create_step.return_value = expected_response

    result = data_store_client.create_step(step)

    args, __ = mocked_data_store_service_client.create_step.call_args
    request = cast(CreateStepRequest, args[0])
    assert request.step == step.to_protobuf()
    assert result == "response_id"


def test___create_test_result___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    test_result = TestResult(
        name="test_result_name",
        id="test_result_id",
        uut_instance_id="uut_instance_id",
        operator_id="operator_id",
        test_station_id="test_station_id",
        test_description_id="test_description_id",
        software_item_ids=[],
        hardware_item_ids=[],
        test_adapter_ids=[],
    )
    expected_response = CreateTestResultResponse(test_result_id="response_id")
    mocked_data_store_service_client.create_test_result.return_value = expected_response

    result = data_store_client.create_test_result(test_result)

    args, __ = mocked_data_store_service_client.create_test_result.call_args
    request = cast(CreateTestResultRequest, args[0])
    assert request.test_result == test_result.to_protobuf()
    assert result == "response_id"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_error_information.py sha256=ebc6594d2dd40fabd968fdbb38fca369053b624be69fb0dd1610c465dda81ec4 bytes=6906 -->
## FILE: tests/unit/data/test_error_information.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_error_information.py`
- sha256: `ebc6594d2dd40fabd968fdbb38fca369053b624be69fb0dd1610c465dda81ec4`
- bytes: 6906

````python
"""Tests for the ErrorInformation wrapper type."""

from __future__ import annotations

import pytest
from ni.measurements.data.v1.data_store_pb2 import (
    ErrorInformation as ErrorInformationProto,
)

from ni.datastore.data import ErrorInformation


def test___init___with_defaults() -> None:
    """Test creating ErrorInformation with default values."""
    error_info = ErrorInformation()

    assert error_info.error_code == 0
    assert error_info.message == ""
    assert error_info.source == ""


def test___init___with_values() -> None:
    """Test creating ErrorInformation with specific values."""
    error_info = ErrorInformation(
        error_code=42, message="Test error occurred", source="test_module.py:123"
    )

    assert error_info.error_code == 42
    assert error_info.message == "Test error occurred"
    assert error_info.source == "test_module.py:123"


def test___init___with_keyword_arguments() -> None:
    """Test creating ErrorInformation using keyword arguments in different order."""
    error_info = ErrorInformation(
        source="some_file.py", message="An error happened", error_code=404
    )

    assert error_info.error_code == 404
    assert error_info.message == "An error happened"
    assert error_info.source == "some_file.py"


def test___from_protobuf___creates_instance_from_protobuf() -> None:
    """Test creating ErrorInformation from protobuf message."""
    proto = ErrorInformationProto(error_code=123, message="Protobuf error", source="proto_source")

    error_info = ErrorInformation.from_protobuf(proto)

    assert error_info.error_code == 123
    assert error_info.message == "Protobuf error"
    assert error_info.source == "proto_source"


def test___from_protobuf___with_empty_protobuf() -> None:
    """Test creating ErrorInformation from empty protobuf message."""
    proto = ErrorInformationProto()

    error_info = ErrorInformation.from_protobuf(proto)

    assert error_info.error_code == 0
    assert error_info.message == ""
    assert error_info.source == ""


def test___to_protobuf___converts_to_protobuf_message() -> None:
    """Test converting ErrorInformation to protobuf message."""
    error_info = ErrorInformation(
        error_code=789, message="Convert this error", source="conversion_test.py"
    )

    proto = error_info.to_protobuf()

    assert isinstance(proto, ErrorInformationProto)
    assert proto.error_code == 789
    assert proto.message == "Convert this error"
    assert proto.source == "conversion_test.py"


def test___to_protobuf___with_defaults() -> None:
    """Test converting ErrorInformation with default values to protobuf."""
    error_info = ErrorInformation()

    proto = error_info.to_protobuf()

    assert isinstance(proto, ErrorInformationProto)
    assert proto.error_code == 0
    assert proto.message == ""
    assert proto.source == ""


def test___round_trip_conversion___preserves_values() -> None:
    """Test that converting to protobuf and back preserves all values."""
    original = ErrorInformation(
        error_code=555, message="Round trip test", source="round_trip.py:42"
    )

    proto = original.to_protobuf()
    converted_back = ErrorInformation.from_protobuf(proto)

    assert converted_back.error_code == original.error_code
    assert converted_back.message == original.message
    assert converted_back.source == original.source


def test___equality___same_values() -> None:
    """Test equality comparison with same values."""
    error_info1 = ErrorInformation(error_code=100, message="Same error", source="same_source.py")
    error_info2 = ErrorInformation(error_code=100, message="Same error", source="same_source.py")

    assert error_info1 == error_info2
    assert error_info2 == error_info1


def test___equality___different_values() -> None:
    """Test equality comparison with different values."""
    error_info1 = ErrorInformation(error_code=100, message="Error 1", source="source1.py")
    error_info2 = ErrorInformation(error_code=200, message="Error 2", source="source2.py")
    error_info3 = ErrorInformation(error_code=100, message="Different message", source="source1.py")
    error_info4 = ErrorInformation(error_code=100, message="Error 1", source="different_source.py")

    assert error_info1 != error_info2
    assert error_info1 != error_info3
    assert error_info1 != error_info4


def test___equality___with_defaults() -> None:
    """Test equality comparison with default values."""
    error_info1 = ErrorInformation()
    error_info2 = ErrorInformation()

    assert error_info1 == error_info2


def test___equality___with_non_error_information_object() -> None:
    """Test equality comparison with non-ErrorInformation object."""
    error_info = ErrorInformation()

    assert error_info != "not an ErrorInformation"
    assert error_info != 42
    assert error_info is not None
    assert error_info != {}


def test___str___returns_protobuf_string() -> None:
    """Test string representation returns protobuf string."""
    error_info = ErrorInformation(error_code=999, message="String test", source="str_test.py")

    str_repr = str(error_info)
    proto_str = str(error_info.to_protobuf())

    assert str_repr == proto_str
    assert "999" in str_repr
    assert "String test" in str_repr
    assert "str_test.py" in str_repr


def test___str___with_empty_values() -> None:
    """Test string representation with empty values."""
    error_info = ErrorInformation()

    str_repr = str(error_info)

    # Should be a string (may be empty for empty protobuf)
    assert isinstance(str_repr, str)
    # Should match the protobuf string representation
    assert str_repr == str(error_info.to_protobuf())


def test___slots___attribute() -> None:
    """Test that __slots__ is properly defined."""
    error_info = ErrorInformation()

    # Should have the three expected slots
    expected_slots = ("error_code", "message", "source")
    assert hasattr(ErrorInformation, "__slots__")
    assert ErrorInformation.__slots__ == expected_slots

    # Should not allow arbitrary attribute assignment
    with pytest.raises(AttributeError):
        setattr(error_info, "unexpected_attribute", "this should fail")


def test___attribute_assignment___after_initialization() -> None:
    """Test that attributes can be modified after initialization."""
    error_info = ErrorInformation(error_code=1, message="initial", source="initial.py")

    # Should be able to modify existing attributes
    error_info.error_code = 2
    error_info.message = "modified"
    error_info.source = "modified.py"

    assert error_info.error_code == 2
    assert error_info.message == "modified"
    assert error_info.source == "modified.py"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_get_metadata.py sha256=30cb50d56e03c2e23a4b7e6637c72195b16f3845b3f7e1cc31ddf8c746e28bc2 bytes=5220 -->
## FILE: tests/unit/data/test_get_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_get_metadata.py`
- sha256: `30cb50d56e03c2e23a4b7e6637c72195b16f3845b3f7e1cc31ddf8c746e28bc2`
- bytes: 5220

````python
"""Contains tests to validate the get_* methods in the data store."""

from __future__ import annotations

import datetime as std_datetime
from typing import cast
from unittest.mock import NonCallableMock

from hightime import datetime
from ni.measurements.data.v1.data_store_pb2 import (
    PublishedCondition as PublishedConditionProto,
    PublishedMeasurement as PublishedMeasurementProto,
    Step as StepProto,
    TestResult as TestResultProto,
)
from ni.measurements.data.v1.data_store_service_pb2 import (
    GetConditionRequest,
    GetConditionResponse,
    GetMeasurementRequest,
    GetMeasurementResponse,
    GetStepRequest,
    GetStepResponse,
    GetTestResultRequest,
    GetTestResultResponse,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_to_protobuf,
)

from ni.datastore.data import (
    DataStoreClient,
    PublishedCondition,
    PublishedMeasurement,
    Step,
    TestResult,
)


def test___get_step___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    start_time = datetime.now(tz=std_datetime.timezone.utc)
    end_time = datetime.now(tz=std_datetime.timezone.utc)
    step = StepProto(
        id="step_id",
        parent_step_id="parent_step_id",
        test_result_id="test_result",
        test_id="test_id",
        name="step_name",
        step_type="step_type",
        notes="step_notes",
        start_date_time=hightime_datetime_to_protobuf(start_time),
        end_date_time=hightime_datetime_to_protobuf(end_time),
    )
    mocked_data_store_service_client.get_step.return_value = GetStepResponse(step=step)

    result = data_store_client.get_step(step_id="request_id")

    args, __ = mocked_data_store_service_client.get_step.call_args
    request = cast(GetStepRequest, args[0])
    assert request.step_id == "request_id"
    assert result == Step.from_protobuf(step)


def test___get_test_result___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    start_time = datetime.now(tz=std_datetime.timezone.utc)
    end_time = datetime.now(tz=std_datetime.timezone.utc)
    test_result = TestResultProto(
        id="test_result_id",
        uut_instance_id="uut_instance_id",
        operator_id="operator_id",
        test_station_id="test_station_id",
        test_description_id="test_description_id",
        software_item_ids=[],
        hardware_item_ids=[],
        test_adapter_ids=[],
        name="test_result_name",
        start_date_time=hightime_datetime_to_protobuf(start_time),
        end_date_time=hightime_datetime_to_protobuf(end_time),
    )
    expected_response = GetTestResultResponse(test_result=test_result)
    mocked_data_store_service_client.get_test_result.return_value = expected_response

    result = data_store_client.get_test_result(test_result_id="request_id")

    args, __ = mocked_data_store_service_client.get_test_result.call_args
    request = cast(GetTestResultRequest, args[0])
    assert request.test_result_id == "request_id"
    assert result == TestResult.from_protobuf(test_result)


def test___get_measurement___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    start_time = datetime.now(tz=std_datetime.timezone.utc)
    published_measurement = PublishedMeasurementProto(
        id="measurement_id",
        name="measurement_name",
        step_id="step_id",
        test_result_id="test_result_id",
        start_date_time=hightime_datetime_to_protobuf(start_time),
    )
    expected_response = GetMeasurementResponse(published_measurement=published_measurement)
    mocked_data_store_service_client.get_measurement.return_value = expected_response

    result = data_store_client.get_measurement(measurement_id="request_id")

    args, __ = mocked_data_store_service_client.get_measurement.call_args
    request = cast(GetMeasurementRequest, args[0])
    assert request.measurement_id == "request_id"
    assert result == PublishedMeasurement.from_protobuf(published_measurement)


def test___get_condition___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    published_condition = PublishedConditionProto(
        id="condition_id",
        name="condition_name",
        condition_type="condition_type",
        step_id="step_id",
        test_result_id="test_result_id",
    )
    expected_response = GetConditionResponse(published_condition=published_condition)
    mocked_data_store_service_client.get_condition.return_value = expected_response

    result = data_store_client.get_condition(condition_id="request_id")

    args, __ = mocked_data_store_service_client.get_condition.call_args
    request = cast(GetConditionRequest, args[0])
    assert request.condition_id == "request_id"
    assert result == PublishedCondition.from_protobuf(published_condition)
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_grpc_conversion.py sha256=96e5a51c5fa96a544852e0e471fcbdb87a24ad5a9ceec7f545d52fe6988a3eb1 bytes=30846 -->
## FILE: tests/unit/data/test_grpc_conversion.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_grpc_conversion.py`
- sha256: `96e5a51c5fa96a544852e0e471fcbdb87a24ad5a9ceec7f545d52fe6988a3eb1`
- bytes: 30846

````python
from collections.abc import Generator
from typing import Any, Iterable

import numpy as np
import pytest
from ni.measurements.data.v1.data_store_service_pb2 import (
    PublishConditionBatchRequest,
    PublishConditionRequest,
    PublishMeasurementBatchRequest,
    PublishMeasurementRequest,
)
from ni.protobuf.types import (
    scalar_pb2,
    vector_pb2,
    vector_wrappers_pb2,
    waveform_pb2,
    waveform_wrappers_pb2,
    xydata_pb2,
    xydata_wrappers_pb2,
)
from nitypes.complex import ComplexInt32DType
from nitypes.scalar import Scalar
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform, ComplexWaveform, DigitalWaveform, Spectrum
from nitypes.xy_data import XYData

from ni.datastore.data._grpc_conversion import (
    populate_publish_condition_batch_request_values,
    populate_publish_condition_request_value,
    populate_publish_measurement_batch_request_values,
    populate_publish_measurement_request_value,
)


# ========================================================
# Populate Condition
# ========================================================
@pytest.mark.parametrize(
    "python_value, attr_to_check",
    [
        (True, "bool_value"),
        (456.2, "double_value"),
        (123, "sint32_value"),
        ("mystr", "string_value"),
    ],
)
def test___python_builtin_scalar___populate_condition___condition_updated_correctly(
    python_value: object, attr_to_check: str
) -> None:
    request = PublishConditionRequest()
    populate_publish_condition_request_value(request, python_value)

    updated_value = request.scalar.__getattribute__(attr_to_check)
    assert isinstance(updated_value, type(python_value))
    assert updated_value == python_value


def test___python_scalar_object___populate_condition___condition_updated_correctly() -> None:
    scalar_obj = Scalar(1.0, "amps")
    request = PublishConditionRequest()
    populate_publish_condition_request_value(request, scalar_obj)

    assert isinstance(request.scalar, scalar_pb2.Scalar)
    assert request.scalar.double_value == 1.0
    assert request.scalar.attributes["NI_UnitDescription"].string_value == "amps"


# ========================================================
# Populate Condition Batch
# ========================================================
def test___python_vector_object___populate_condition_batch___condition_updated_correctly() -> None:
    vector_obj = Vector([1.0, 2.0, 3.0], "amps")
    request = PublishConditionBatchRequest()
    populate_publish_condition_batch_request_values(request, vector_obj)

    assert isinstance(request.scalar_values, vector_pb2.Vector)
    assert list(request.scalar_values.double_array.values) == [1.0, 2.0, 3.0]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == "amps"


def test___python_scalar_iterable___populate_condition_batch___condition_updated_correctly() -> (
    None
):
    request = PublishConditionBatchRequest()
    populate_publish_condition_batch_request_values(request, [1.5, 2.5, 3.5])

    assert isinstance(request.scalar_values, vector_pb2.Vector)
    assert list(request.scalar_values.double_array.values) == [1.5, 2.5, 3.5]


def test___python_scalar_generator_iterable___populate_condition_batch___condition_updated_correctly() -> (
    None
):
    def _values() -> Iterable[float]:
        yield 1.5
        yield 2.5
        yield 3.5

    request = PublishConditionBatchRequest()
    populate_publish_condition_batch_request_values(request, _values())

    assert isinstance(request.scalar_values, vector_pb2.Vector)
    assert list(request.scalar_values.double_array.values) == [1.5, 2.5, 3.5]


def test___empty_iterable___populate_condition_batch___raises_error() -> None:
    request = PublishConditionBatchRequest()

    with pytest.raises(ValueError, match="Cannot publish an empty Iterable."):
        populate_publish_condition_batch_request_values(request, [])


def test___empty_generator___populate_condition_batch___raises_error() -> None:
    def _values() -> Generator[float, None, None]:
        yield from []

    request = PublishConditionBatchRequest()

    with pytest.raises(ValueError, match="Cannot publish an empty Iterable."):
        populate_publish_condition_batch_request_values(request, _values())


def test___python_unsupported_iterable___populate_condition_batch___raises_error() -> None:
    values = [object(), object()]
    request = PublishConditionBatchRequest()

    with pytest.raises(
        TypeError,
        match="Unsupported iterable.",
    ):
        populate_publish_condition_batch_request_values(request, values)


def test___python_non_iterable___populate_condition_batch___raises_error() -> None:
    values = 42
    request = PublishConditionBatchRequest()

    with pytest.raises(
        TypeError,
        match="Unsupported condition values type",
    ):
        populate_publish_condition_batch_request_values(request, values)


# ========================================================
# Populate Measurement
# ========================================================
@pytest.mark.parametrize(
    "python_value, attr_to_check",
    [
        (True, "bool_value"),
        (456.2, "double_value"),
        (123, "sint32_value"),
        ("mystr", "string_value"),
    ],
)
def test___python_builtin_scalar___populate_measurement___measurement_updated_correctly(
    python_value: object, attr_to_check: str
) -> None:
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, python_value)

    updated_value = request.scalar.__getattribute__(attr_to_check)
    assert isinstance(updated_value, type(python_value))
    assert updated_value == python_value


def test___python_vector_object___populate_measurement___measurement_updated_correctly() -> None:
    vector_obj = Vector([1.0, 2.0, 3.0], "amps")
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, vector_obj)

    assert isinstance(request.vector, vector_pb2.Vector)
    assert list(request.vector.double_array.values) == [1.0, 2.0, 3.0]
    assert request.vector.attributes["NI_UnitDescription"].string_value == "amps"


def test___python_float64_analog_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    wfm_obj = AnalogWaveform(3, np.float64)
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.double_analog_waveform, waveform_pb2.DoubleAnalogWaveform)
    assert list(request.double_analog_waveform.y_data) == [0.0, 0.0, 0.0]


def test___python_int16_analog_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    wfm_obj = AnalogWaveform(3, np.int16)
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.i16_analog_waveform, waveform_pb2.I16AnalogWaveform)
    assert list(request.i16_analog_waveform.y_data) == [0, 0, 0]


def test___python_float64_complex_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    wfm_obj = ComplexWaveform(2, np.complex128)
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.double_complex_waveform, waveform_pb2.DoubleComplexWaveform)
    assert list(request.double_complex_waveform.y_data) == [0.0, 0.0, 0.0, 0.0]


def test___python_int16_complex_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    wfm_obj = ComplexWaveform(2, ComplexInt32DType)
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.i16_complex_waveform, waveform_pb2.I16ComplexWaveform)
    assert list(request.i16_complex_waveform.y_data) == [0, 0, 0, 0]


def test___python_bool_digital_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    data = np.array([[0, 1, 0], [1, 0, 1]], dtype=np.bool)
    wfm_obj = DigitalWaveform.from_lines(data, signal_count=3)

    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.digital_waveform, waveform_pb2.DigitalWaveform)
    assert request.digital_waveform.y_data == b"\x00\x01\x00\x01\x00\x01"
    assert request.digital_waveform.signal_count == 3


def test___python_uint8_digital_waveform___populate_measurement___measurement_updated_correctly() -> (
    None
):
    data = np.array([[0, 1, 3], [7, 5, 1]], dtype=np.uint8)
    wfm_obj = DigitalWaveform.from_lines(data, signal_count=3)

    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, wfm_obj)

    assert isinstance(request.digital_waveform, waveform_pb2.DigitalWaveform)
    assert request.digital_waveform.y_data == b"\x00\x01\x03\x07\x05\x01"
    assert request.digital_waveform.signal_count == 3


def test___python_float64_spectrum___populate_measurement___measurement_updated_correctly() -> None:
    spectrum = Spectrum.from_array_1d(np.array([1.0, 2.0, 3.0]))
    spectrum.start_frequency = 100.0
    spectrum.frequency_increment = 10.0

    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, spectrum)

    assert isinstance(request.double_spectrum, waveform_pb2.DoubleSpectrum)
    assert list(request.double_spectrum.data) == [1.0, 2.0, 3.0]
    assert request.double_spectrum.start_frequency == 100.0
    assert request.double_spectrum.frequency_increment == 10.0


def test___python_float64_xydata___populate_measurement___measurement_updated_correctly() -> None:
    xydata = XYData.from_arrays_1d(
        [1.0, 2.0], [3.0, 4.0], np.float64, x_units="Volts", y_units="Seconds"
    )

    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, xydata)

    assert isinstance(request.x_y_data, xydata_pb2.DoubleXYData)
    assert list(request.x_y_data.x_data) == [1.0, 2.0]
    assert list(request.x_y_data.y_data) == [3.0, 4.0]
    assert request.x_y_data.attributes["NI_UnitDescription_X"].string_value == "Volts"
    assert request.x_y_data.attributes["NI_UnitDescription_Y"].string_value == "Seconds"


@pytest.mark.parametrize(
    "values, attribute_name",
    [
        ([1.5, 2.5, 3.5], "double_array"),
        ([1, 2, 3], "sint32_array"),
        ([True, False, True], "bool_array"),
        (["one", "two", "three"], "string_array"),
    ],
)
def test___python_scalar_iterable___populate_measurement___measurement_updated_correctly(
    values: list[object], attribute_name: str
) -> None:
    request = PublishMeasurementRequest()
    populate_publish_measurement_request_value(request, values)

    assert isinstance(request.vector, vector_pb2.Vector)
    assert list(getattr(request.vector, attribute_name).values) == values


def test___empty_iterable___populate_measurement___raises_value_error() -> None:
    request = PublishMeasurementRequest()
    with pytest.raises(ValueError, match="Cannot publish an empty Iterable."):
        populate_publish_measurement_request_value(request, [])


def test___unsupported_iterable___populate_measurement___raises_type_error() -> None:
    request = PublishMeasurementRequest()
    with pytest.raises(TypeError, match="Unsupported iterable"):
        populate_publish_measurement_request_value(request, [object(), object()])


# ========================================================
# Populate Measurement Batch
# ========================================================
def _assert_scalar_values(
    request: PublishMeasurementBatchRequest, attribute_name: str, expected_values: list[object]
) -> None:
    assert isinstance(request.scalar_values, vector_pb2.Vector)
    assert list(getattr(request.scalar_values, attribute_name).values) == expected_values


@pytest.mark.parametrize(
    "values, attribute_name, expected_unit",
    [
        (Vector([1.5, 2.5, 3.5], "amps"), "double_array", "amps"),
        (Vector([1, 2, 3], "volts"), "sint32_array", "volts"),
        (Vector([True, False, True], "state"), "bool_array", "state"),
        (Vector(["one", "two", "three"], "labels"), "string_array", "labels"),
    ],
)
def test___python_vector_object___populate_measurement_batch___measurement_updated_correctly(
    values: Vector[Any], attribute_name: str, expected_unit: str
) -> None:
    request = PublishMeasurementBatchRequest()
    populate_publish_measurement_batch_request_values(request, values)

    _assert_scalar_values(request, attribute_name, list(values))
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == expected_unit


@pytest.mark.parametrize(
    "values, attribute_name",
    [
        ([1.5, 2.5, 3.5], "double_array"),
        ([1, 2, 3], "sint32_array"),
        ([True, False, True], "bool_array"),
        (["one", "two", "three"], "string_array"),
    ],
)
def test___python_scalar_iterable___populate_measurement_batch___measurement_updated_correctly(
    values: list[object], attribute_name: str
) -> None:
    request = PublishMeasurementBatchRequest()
    populate_publish_measurement_batch_request_values(request, values)

    _assert_scalar_values(request, attribute_name, values)


def test___python_vector_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [Vector([1.0, 2.0]), Vector([3.0, 4.0])]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(request.vector_values, vector_wrappers_pb2.VectorArrayValue)
    assert len(request.vector_values.vectors) == 2
    assert list(request.vector_values.vectors[0].double_array.values) == [1.0, 2.0]
    assert list(request.vector_values.vectors[1].double_array.values) == [3.0, 4.0]


def test___python_float64_analog_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        AnalogWaveform(sample_count=2, raw_data=np.array([1.25, -2.5], dtype=np.float64)),
        AnalogWaveform(sample_count=3, raw_data=np.array([3.5, 4.75, -6.0], dtype=np.float64)),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.double_analog_waveform_values, waveform_wrappers_pb2.DoubleAnalogWaveformArrayValue
    )
    assert len(request.double_analog_waveform_values.waveforms) == 2
    assert list(request.double_analog_waveform_values.waveforms[0].y_data) == [1.25, -2.5]
    assert list(request.double_analog_waveform_values.waveforms[1].y_data) == [3.5, 4.75, -6.0]


def test___python_int16_analog_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        AnalogWaveform(sample_count=2, raw_data=np.array([12, -3], dtype=np.int16)),
        AnalogWaveform(sample_count=3, raw_data=np.array([7, 0, -8], dtype=np.int16)),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.i16_analog_waveform_values, waveform_wrappers_pb2.I16AnalogWaveformArrayValue
    )
    assert len(request.i16_analog_waveform_values.waveforms) == 2
    assert list(request.i16_analog_waveform_values.waveforms[0].y_data) == [12, -3]
    assert list(request.i16_analog_waveform_values.waveforms[1].y_data) == [7, 0, -8]


def test___python_float64_complex_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        ComplexWaveform(
            sample_count=2, raw_data=np.array([1.0 + 2.0j, -3.0 + 4.5j], dtype=np.complex128)
        ),
        ComplexWaveform(
            sample_count=3,
            raw_data=np.array([0.5 - 1.5j, 2.25 + 0.75j, -4.0 - 2.0j], dtype=np.complex128),
        ),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.double_complex_waveform_values,
        waveform_wrappers_pb2.DoubleComplexWaveformArrayValue,
    )
    assert len(request.double_complex_waveform_values.waveforms) == 2
    assert list(request.double_complex_waveform_values.waveforms[0].y_data) == [1.0, 2.0, -3.0, 4.5]
    assert list(request.double_complex_waveform_values.waveforms[1].y_data) == [
        0.5,
        -1.5,
        2.25,
        0.75,
        -4.0,
        -2.0,
    ]


def test___python_int16_complex_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        ComplexWaveform(
            sample_count=2,
            raw_data=np.array([(11, -2), (5, 9)], dtype=ComplexInt32DType),
        ),
        ComplexWaveform(
            sample_count=3,
            raw_data=np.array([(-7, 4), (0, -6), (8, 3)], dtype=ComplexInt32DType),
        ),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.i16_complex_waveform_values, waveform_wrappers_pb2.I16ComplexWaveformArrayValue
    )
    assert len(request.i16_complex_waveform_values.waveforms) == 2
    assert list(request.i16_complex_waveform_values.waveforms[0].y_data) == [11, -2, 5, 9]
    assert list(request.i16_complex_waveform_values.waveforms[1].y_data) == [-7, 4, 0, -6, 8, 3]


def test___python_float64_spectrum_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        Spectrum.from_array_1d(np.array([1.0, 2.0])),
        Spectrum.from_array_1d(np.array([3.0, 4.0])),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.double_spectrum_values, waveform_wrappers_pb2.DoubleSpectrumArrayValue
    )
    assert len(request.double_spectrum_values.waveforms) == 2
    assert list(request.double_spectrum_values.waveforms[0].data) == [1.0, 2.0]
    assert list(request.double_spectrum_values.waveforms[1].data) == [3.0, 4.0]


def test___python_uint8_digital_waveform_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        DigitalWaveform.from_lines([1], np.uint8),
        DigitalWaveform.from_lines([0], np.uint8),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(
        request.digital_waveform_values, waveform_wrappers_pb2.DigitalWaveformArrayValue
    )
    assert len(request.digital_waveform_values.waveforms) == 2
    assert request.digital_waveform_values.waveforms[0].y_data == b"\x01"
    assert request.digital_waveform_values.waveforms[1].y_data == b"\x00"


def test___python_float64_xydata_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    values = [
        XYData.from_arrays_1d([1.0], [2.0], np.float64),
        XYData.from_arrays_1d([3.0], [4.0], np.float64),
    ]
    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, values)

    assert isinstance(request.x_y_data_values, xydata_wrappers_pb2.DoubleXYDataArrayValue)
    assert len(request.x_y_data_values.x_y_data) == 2
    assert list(request.x_y_data_values.x_y_data[0].x_data) == [1.0]
    assert list(request.x_y_data_values.x_y_data[0].y_data) == [2.0]
    assert list(request.x_y_data_values.x_y_data[1].x_data) == [3.0]
    assert list(request.x_y_data_values.x_y_data[1].y_data) == [4.0]


def test___python_scalar_generator_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    def _values() -> Iterable[float]:
        yield 1.5
        yield 2.5
        yield 3.5

    request = PublishMeasurementBatchRequest()
    populate_publish_measurement_batch_request_values(request, _values())

    _assert_scalar_values(request, "double_array", [1.5, 2.5, 3.5])


def test___python_non_scalar_generator_iterable___populate_measurement_batch___measurement_updated_correctly() -> (
    None
):
    def _values() -> Iterable[AnalogWaveform[np.float64]]:
        yield AnalogWaveform(sample_count=2, raw_data=np.array([1.25, -2.5], dtype=np.float64))
        yield AnalogWaveform(sample_count=3, raw_data=np.array([3.5, 4.75, -6.0], dtype=np.float64))

    request = PublishMeasurementBatchRequest()

    populate_publish_measurement_batch_request_values(request, _values())

    assert isinstance(
        request.double_analog_waveform_values, waveform_wrappers_pb2.DoubleAnalogWaveformArrayValue
    )
    assert len(request.double_analog_waveform_values.waveforms) == 2
    assert list(request.double_analog_waveform_values.waveforms[0].y_data) == [1.25, -2.5]
    assert list(request.double_analog_waveform_values.waveforms[1].y_data) == [3.5, 4.75, -6.0]


@pytest.mark.parametrize(
    "values, error_message",
    [
        pytest.param(
            [
                Vector([1.0, 2.0]),
                AnalogWaveform(sample_count=2, raw_data=np.array([1.0, 2.0])),
            ],
            "Unsupported iterable: all values must be Vector.",
            id="vector",
        ),
        pytest.param(
            [
                AnalogWaveform(sample_count=2, raw_data=np.array([1.25, -2.5], dtype=np.float64)),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be float64 AnalogWaveform.",
            id="float64_analog_waveform",
        ),
        pytest.param(
            [
                AnalogWaveform(sample_count=2, raw_data=np.array([12, -3], dtype=np.int16)),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be int16 AnalogWaveform.",
            id="int16_analog_waveform",
        ),
        pytest.param(
            [
                ComplexWaveform(
                    sample_count=2,
                    raw_data=np.array([1.0 + 2.0j, -3.0 + 4.5j], dtype=np.complex128),
                ),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be complex128 ComplexWaveform.",
            id="float64_complex_waveform",
        ),
        pytest.param(
            [
                ComplexWaveform(
                    sample_count=2,
                    raw_data=np.array([(11, -2), (5, 9)], dtype=ComplexInt32DType),
                ),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be ComplexWaveform with ComplexInt32DType.",
            id="int16_complex_waveform",
        ),
        pytest.param(
            [
                Spectrum.from_array_1d(np.array([1.0, 2.0])),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be float64 Spectrum.",
            id="spectrum",
        ),
        pytest.param(
            [
                DigitalWaveform.from_lines([1], np.uint8),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be DigitalWaveform.",
            id="digital_waveform",
        ),
        pytest.param(
            [
                XYData.from_arrays_1d([1.0], [2.0], np.float64),
                Vector([1.0, 2.0]),
            ],
            "Unsupported iterable: all values must be float64 XYData.",
            id="xydata",
        ),
    ],
)
def test___python_iterable_with_mismatched_second_element___populate_measurement_batch___raises_error(
    values: list[object], error_message: str
) -> None:
    request = PublishMeasurementBatchRequest()

    with pytest.raises(TypeError, match=error_message):
        populate_publish_measurement_batch_request_values(request, values)


@pytest.mark.parametrize(
    "values, error_message",
    [
        pytest.param(
            [
                AnalogWaveform(sample_count=2, raw_data=np.array([1.25, -2.5], dtype=np.float64)),
                AnalogWaveform(sample_count=3, raw_data=np.array([7, 0, -8], dtype=np.int16)),
            ],
            "Unsupported iterable: all values must be float64 AnalogWaveform.",
            id="float64_analog_waveform",
        ),
        pytest.param(
            [
                AnalogWaveform(sample_count=2, raw_data=np.array([12, -3], dtype=np.int16)),
                AnalogWaveform(
                    sample_count=3, raw_data=np.array([3.5, 4.75, -6.0], dtype=np.float64)
                ),
            ],
            "Unsupported iterable: all values must be int16 AnalogWaveform.",
            id="int16_analog_waveform",
        ),
        pytest.param(
            [
                ComplexWaveform(
                    sample_count=2,
                    raw_data=np.array([1.0 + 2.0j, -3.0 + 4.5j], dtype=np.complex128),
                ),
                ComplexWaveform(
                    sample_count=3,
                    raw_data=np.array([(-7, 4), (0, -6), (8, 3)], dtype=ComplexInt32DType),
                ),
            ],
            "Unsupported iterable: all values must be complex128 ComplexWaveform.",
            id="float64_complex_waveform",
        ),
        pytest.param(
            [
                ComplexWaveform(
                    sample_count=2,
                    raw_data=np.array([(11, -2), (5, 9)], dtype=ComplexInt32DType),
                ),
                ComplexWaveform(
                    sample_count=3,
                    raw_data=np.array([0.5 - 1.5j, 2.25 + 0.75j, -4.0 - 2.0j], dtype=np.complex128),
                ),
            ],
            "Unsupported iterable: all values must be ComplexWaveform with ComplexInt32DType.",
            id="int16_complex_waveform",
        ),
        pytest.param(
            [
                Spectrum.from_array_1d(np.array([1.0, 2.0])),
                Spectrum.from_array_1d(np.array([3.0, 4.0], dtype=np.float32)),
            ],
            "Unsupported iterable: all values must be float64 Spectrum.",
            id="spectrum",
        ),
        pytest.param(
            [
                XYData.from_arrays_1d([1.0], [2.0], np.float64),
                XYData.from_arrays_1d([3.0], [4.0], np.float32),
            ],
            "Unsupported iterable: all values must be float64 XYData.",
            id="xydata",
        ),
    ],
)
def test___python_iterable_with_mismatched_second_dtype___populate_measurement_batch___raises_error(
    values: list[object], error_message: str
) -> None:
    request = PublishMeasurementBatchRequest()

    with pytest.raises(TypeError, match=error_message):
        populate_publish_measurement_batch_request_values(request, values)


@pytest.mark.parametrize(
    "values, error_message",
    [
        pytest.param(
            [
                AnalogWaveform(sample_count=2, raw_data=np.array([1.25, -2.5], dtype=np.float32)),
                AnalogWaveform(
                    sample_count=3, raw_data=np.array([3.5, 4.75, -6.0], dtype=np.float32)
                ),
            ],
            "Unsupported AnalogWaveform dtype",
            id="analog_waveform",
        ),
        pytest.param(
            [
                ComplexWaveform(
                    sample_count=2,
                    raw_data=np.array([1.0 + 2.0j, -3.0 + 4.5j], dtype=np.complex64),
                ),
                ComplexWaveform(
                    sample_count=3,
                    raw_data=np.array([0.5 - 1.5j, 2.25 + 0.75j, -4.0 - 2.0j], dtype=np.complex64),
                ),
            ],
            "Unsupported ComplexWaveform dtype",
            id="complex_waveform",
        ),
        pytest.param(
            [
                Spectrum.from_array_1d(np.array([1.0, 2.0], dtype=np.float32)),
                Spectrum.from_array_1d(np.array([3.0, 4.0], dtype=np.float32)),
            ],
            "Unsupported Spectrum dtype",
            id="spectrum",
        ),
        pytest.param(
            [
                XYData.from_arrays_1d([1.0], [2.0], np.float32),
                XYData.from_arrays_1d([3.0], [4.0], np.float32),
            ],
            "Unsupported XYData dtype",
            id="xydata",
        ),
    ],
)
def test___python_unsupported_dtype_iterable___populate_measurement_batch___raises_error(
    values: list[object], error_message: str
) -> None:
    request = PublishMeasurementBatchRequest()

    with pytest.raises(TypeError, match=error_message):
        populate_publish_measurement_batch_request_values(request, values)


def test___empty_iterable___populate_measurement_batch___raises_error() -> None:
    request = PublishMeasurementBatchRequest()

    with pytest.raises(ValueError, match="Cannot publish an empty Iterable."):
        populate_publish_measurement_batch_request_values(request, [])


def test___empty_generator___populate_measurement_batch___raises_error() -> None:
    def _values() -> Generator[float, None, None]:
        yield from []

    request = PublishMeasurementBatchRequest()

    with pytest.raises(ValueError, match="Cannot publish an empty Iterable."):
        populate_publish_measurement_batch_request_values(request, _values())


def test___python_unsupported_iterable___populate_measurement_batch___raises_error() -> None:
    values = [object(), object()]
    request = PublishMeasurementBatchRequest()

    with pytest.raises(
        TypeError,
        match="Unsupported iterable. Subtype must be",
    ):
        populate_publish_measurement_batch_request_values(request, values)


def test___python_non_iterable___populate_measurement_batch___raises_error() -> None:
    values = 42
    request = PublishMeasurementBatchRequest()

    with pytest.raises(
        TypeError,
        match="Unsupported measurement values type",
    ):
        populate_publish_measurement_batch_request_values(request, values)
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_outcome.py sha256=4f3bc923c4e619d12ffda7e8ef510c3a93b5433488090f4f170537ddb677909e bytes=3085 -->
## FILE: tests/unit/data/test_outcome.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_outcome.py`
- sha256: `4f3bc923c4e619d12ffda7e8ef510c3a93b5433488090f4f170537ddb677909e`
- bytes: 3085

````python
"""Tests for the Outcome wrapper enum."""

from __future__ import annotations

from typing import cast

import pytest
from ni.measurements.data.v1.data_store_pb2 import Outcome as OutcomeProto

from ni.datastore.data import Outcome


def test___enum_values___match_protobuf_values() -> None:
    """Test that enum values match the protobuf enum values."""
    assert Outcome.UNSPECIFIED.value == OutcomeProto.OUTCOME_UNSPECIFIED
    assert Outcome.PASSED.value == OutcomeProto.OUTCOME_PASSED
    assert Outcome.FAILED.value == OutcomeProto.OUTCOME_FAILED
    assert Outcome.INDETERMINATE.value == OutcomeProto.OUTCOME_INDETERMINATE


def test___enum_values___have_expected_integer_values() -> None:
    """Test that enum has the expected integer values."""
    assert Outcome.UNSPECIFIED.value == 0
    assert Outcome.PASSED.value == 1
    assert Outcome.FAILED.value == 2
    assert Outcome.INDETERMINATE.value == 3


def test___to_protobuf___converts_enum_to_protobuf_value() -> None:
    """Test converting enum to protobuf value."""
    assert Outcome.UNSPECIFIED.to_protobuf() == OutcomeProto.OUTCOME_UNSPECIFIED
    assert Outcome.PASSED.to_protobuf() == OutcomeProto.OUTCOME_PASSED
    assert Outcome.FAILED.to_protobuf() == OutcomeProto.OUTCOME_FAILED
    assert Outcome.INDETERMINATE.to_protobuf() == OutcomeProto.OUTCOME_INDETERMINATE


def test___from_protobuf___converts_protobuf_value_to_enum() -> None:
    """Test converting protobuf value to enum."""
    assert Outcome.from_protobuf(OutcomeProto.OUTCOME_UNSPECIFIED) == Outcome.UNSPECIFIED
    assert Outcome.from_protobuf(OutcomeProto.OUTCOME_PASSED) == Outcome.PASSED
    assert Outcome.from_protobuf(OutcomeProto.OUTCOME_FAILED) == Outcome.FAILED
    assert Outcome.from_protobuf(OutcomeProto.OUTCOME_INDETERMINATE) == Outcome.INDETERMINATE


def test___round_trip_conversion___preserves_enum_value() -> None:
    """Test that converting to protobuf and back gives the same result."""
    for outcome in Outcome:
        pb_outcome = outcome.to_protobuf()
        back_to_enum = Outcome.from_protobuf(pb_outcome)
        assert outcome == back_to_enum


def test___invalid_value___from_protobuf___raises_value_error() -> None:
    """Test that from_protobuf raises ValueError for invalid values."""
    with pytest.raises(ValueError, match="Unknown outcome value"):
        Outcome.from_protobuf(cast(OutcomeProto.ValueType, 999))


def test___enum___is_iterable() -> None:
    """Test that the enum can be iterated over."""
    outcomes = list(Outcome)
    assert len(outcomes) == 4
    assert Outcome.UNSPECIFIED in outcomes
    assert Outcome.PASSED in outcomes
    assert Outcome.FAILED in outcomes
    assert Outcome.INDETERMINATE in outcomes


def test___enum___has_correct_name_and_value_attributes() -> None:
    """Test that enum has correct name and value attributes."""
    assert Outcome.PASSED.name == "PASSED"
    assert Outcome.PASSED.value == 1
    assert Outcome.FAILED.name == "FAILED"
    assert Outcome.FAILED.value == 2
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_publish_condition.py sha256=3a2309bb752046ee5f6179aa5259bfa399c5c44f87e48c40e92c31f1725f5b00 bytes=8092 -->
## FILE: tests/unit/data/test_publish_condition.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_publish_condition.py`
- sha256: `3a2309bb752046ee5f6179aa5259bfa399c5c44f87e48c40e92c31f1725f5b00`
- bytes: 8092

````python
"""Contains tests to validate the data store client publish condition functionality."""

from __future__ import annotations

from typing import cast
from unittest.mock import NonCallableMock

import pytest
from ni.measurements.data.v1.data_store_service_pb2 import (
    PublishConditionBatchRequest,
    PublishConditionBatchResponse,
    PublishConditionRequest,
    PublishConditionResponse,
)
from nitypes.vector import Vector

from ni.datastore.data import DataStoreClient


def test___publish_condition___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition.return_value = expected_response

    condition_id = data_store_client.publish_condition(
        name="TestCondition",
        condition_type="ConditionType",
        value=123,
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition.call_args
    request = cast(PublishConditionRequest, args[0])
    assert condition_id == "response_id"
    assert request.step_id == "MyStep"
    assert request.name == "TestCondition"
    assert request.condition_type == "ConditionType"
    assert request.scalar.sint32_value == 123


def test___none___publish_condition___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_condition(
            name="TestCondition",
            condition_type="ConditionType",
            value=None,
            step_id="MyStep",
        )

    assert exc.value.args[0].startswith("Unsupported condition value type")


def test___vector___publish_condition_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionBatchResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition_batch.return_value = expected_response

    condition_id = data_store_client.publish_condition_batch(
        name="TestCondition",
        condition_type="ConditionType",
        values=Vector(values=["one", "two", "three"], units="fake_units"),
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition_batch.call_args
    request = cast(PublishConditionBatchRequest, args[0])
    assert condition_id == "response_id"
    assert request.step_id == "MyStep"
    assert request.name == "TestCondition"
    assert request.condition_type == "ConditionType"
    assert list(request.scalar_values.string_array.values) == ["one", "two", "three"]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == "fake_units"


def test___int_list___publish_condition_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionBatchResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition_batch.return_value = expected_response

    condition_id = data_store_client.publish_condition_batch(
        name="TestCondition",
        condition_type="ConditionType",
        values=[1, 2, 3],
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition_batch.call_args
    request = cast(PublishConditionBatchRequest, args[0])
    assert condition_id == "response_id"
    assert list(request.scalar_values.sint32_array.values) == [1, 2, 3]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___float_list___publish_condition_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionBatchResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition_batch.return_value = expected_response

    condition_id = data_store_client.publish_condition_batch(
        name="TestCondition",
        condition_type="ConditionType",
        values=[1.0, 2.0, 3.0],
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition_batch.call_args
    request = cast(PublishConditionBatchRequest, args[0])
    assert condition_id == "response_id"
    assert list(request.scalar_values.double_array.values) == [1.0, 2.0, 3.0]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___bool_list___publish_condition_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionBatchResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition_batch.return_value = expected_response

    condition_id = data_store_client.publish_condition_batch(
        name="TestCondition",
        condition_type="ConditionType",
        values=[True, False, True],
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition_batch.call_args
    request = cast(PublishConditionBatchRequest, args[0])
    assert condition_id == "response_id"
    assert list(request.scalar_values.bool_array.values) == [True, False, True]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___string_list___publish_condition_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    expected_response = PublishConditionBatchResponse(condition_id="response_id")
    mocked_data_store_service_client.publish_condition_batch.return_value = expected_response

    condition_id = data_store_client.publish_condition_batch(
        name="TestCondition",
        condition_type="ConditionType",
        values=["one", "two", "three"],
        step_id="MyStep",
    )

    args, __ = mocked_data_store_service_client.publish_condition_batch.call_args
    request = cast(PublishConditionBatchRequest, args[0])
    assert condition_id == "response_id"
    assert list(request.scalar_values.string_array.values) == ["one", "two", "three"]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___unsupported_list___publish_condition_batch___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_condition_batch(
            name="TestCondition",
            condition_type="ConditionType",
            values=[[1, 2, 3], [4, 5, 6]],  # List of lists will error during vector creation.
            step_id="MyStep",
        )

    assert exc.value.args[0].startswith("Unsupported iterable:")


def test___empty_list___publish_condition_batch___raises_value_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(ValueError) as exc:
        _ = data_store_client.publish_condition_batch(
            name="TestCondition",
            condition_type="ConditionType",
            values=[],
            step_id="MyStep",
        )

    assert exc.value.args[0].startswith("Cannot publish an empty Iterable.")


def test___none___publish_condition_batch___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_condition_batch(
            name="TestCondition",
            condition_type="ConditionType",
            values=None,
            step_id="MyStep",
        )

    assert exc.value.args[0].startswith("Unsupported condition values type")
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_publish_measurement.py sha256=5889d8fa77b172379a5149bba62e7c2d2fb41ebdc839fe1edb0ebe559874e931 bytes=20291 -->
## FILE: tests/unit/data/test_publish_measurement.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_publish_measurement.py`
- sha256: `5889d8fa77b172379a5149bba62e7c2d2fb41ebdc839fe1edb0ebe559874e931`
- bytes: 20291

````python
"""Contains tests to validate the data store client publish functionality."""

from __future__ import annotations

import datetime as std_datetime
from typing import Any, cast, Iterable
from unittest.mock import NonCallableMock

import numpy as np
import pytest
from hightime import datetime, timedelta
from ni.measurements.data.v1.data_store_pb2 import (
    ErrorInformation as ErrorInformationProto,
    Outcome as OutcomeProto,
)
from ni.measurements.data.v1.data_store_service_pb2 import (
    PublishMeasurementBatchRequest,
    PublishMeasurementBatchResponse,
    PublishMeasurementRequest,
    PublishMeasurementResponse,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_to_protobuf,
)
from ni.protobuf.types.precision_timestamp_pb2 import PrecisionTimestamp
from ni.protobuf.types.vector_conversion import vector_to_protobuf
from ni.protobuf.types.vector_pb2 import Vector as VectorProto
from ni.protobuf.types.waveform_conversion import float64_analog_waveform_to_protobuf
from ni.protobuf.types.waveform_pb2 import DoubleAnalogWaveform
from ni.protobuf.types.xydata_conversion import float64_xydata_to_protobuf
from ni.protobuf.types.xydata_pb2 import DoubleXYData
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform, Timing
from nitypes.xy_data import XYData

from ni.datastore.data import DataStoreClient, ErrorInformation, Outcome


@pytest.mark.parametrize("value", [True, False])
def test___publish_boolean_data___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
    value: bool,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = expected_response

    measurement_id = data_store_client.publish_measurement(
        "name",
        value,
        "step_id",
        timestamp,
        Outcome.PASSED,
        ErrorInformation(),
        [],
        [],
        [],
        "notes",
    )

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = args[0]  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.notes == "notes"
    assert request.timestamp == hightime_datetime_to_protobuf(timestamp)
    assert request.scalar.bool_value == value
    assert request.outcome == OutcomeProto.OUTCOME_PASSED
    assert request.error_information == ErrorInformationProto()
    assert request.hardware_item_ids == []
    assert request.software_item_ids == []
    assert request.test_adapter_ids == []


def test___publish_analog_waveform_data___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    waveform_values = [1.0, 2.0, 3.0]
    analog_waveform = AnalogWaveform(
        sample_count=len(waveform_values),
        raw_data=np.array(waveform_values, dtype=np.float64),
        timing=Timing.create_with_regular_interval(timedelta(seconds=1), timestamp),
    )
    expected_protobuf_waveform = DoubleAnalogWaveform()
    expected_protobuf_waveform.CopyFrom(float64_analog_waveform_to_protobuf(analog_waveform))
    expected_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = expected_response

    # Now, when client.publish_measurement calls foo.MyClass().publish(), it will use the mock
    measurement_id = data_store_client.publish_measurement(
        "name",
        analog_waveform,
        "step_id",
        timestamp,
        Outcome.PASSED,
        ErrorInformation(),
        [],
        [],
        [],
        "notes",
    )

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.notes == "notes"
    assert request.timestamp == hightime_datetime_to_protobuf(timestamp)
    assert request.double_analog_waveform == expected_protobuf_waveform
    assert request.outcome == OutcomeProto.OUTCOME_PASSED
    assert request.error_information == ErrorInformationProto()
    assert request.hardware_item_ids == []
    assert request.software_item_ids == []
    assert request.test_adapter_ids == []


def test___publish_float64_xydata___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    xydata = XYData.from_arrays_1d(
        x_array=[1.0, 2.0],
        y_array=[3.0, 4.0],
        dtype=np.float64,
        x_units="Volts",
        y_units="Seconds",
    )
    expected_protobuf_xydata = DoubleXYData()
    expected_protobuf_xydata.CopyFrom(float64_xydata_to_protobuf(xydata))
    expected_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = expected_response

    # Now, when client.publish_measurement calls foo.MyClass().publish(), it will use the mock
    measurement_id = data_store_client.publish_measurement("name", xydata, "step_id")

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.x_y_data == expected_protobuf_xydata


@pytest.mark.parametrize(
    "value", [[1, 2, 3], [1.0, 2.0, 3.0], [True, False, True], ["one", "two", "three"]]
)
def test___publish_basic_iterable_data___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
    value: Iterable[Any],
) -> None:
    expected_vector = Vector(value)
    expected_protobuf_vector = VectorProto()
    expected_protobuf_vector.CopyFrom(vector_to_protobuf(expected_vector))
    expected_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = expected_response

    # Now, when client.publish_measurement calls foo.MyClass().publish(), it will use the mock
    measurement_id = data_store_client.publish_measurement("name", value, "step_id")

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.vector == expected_protobuf_vector


def test___unsupported_list___publish_measurement___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_measurement(
            name="name",
            value=[[1, 2, 3], [4, 5, 6]],  # List of lists will error during vector creation.
            step_id="step_id",
        )

    assert exc.value.args[0].startswith("Unsupported iterable:")


def test___publish_analog_waveform_data_without_timestamp_parameter___timestamp_is_unset(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    waveform_values = [1.0, 2.0, 3.0]
    analog_waveform = AnalogWaveform(
        sample_count=len(waveform_values),
        raw_data=np.array(waveform_values, dtype=np.float64),
        timing=Timing.create_with_regular_interval(timedelta(seconds=1), timestamp),
    )
    expected_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = expected_response

    measurement_id = data_store_client.publish_measurement("name", analog_waveform, "step_id")

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert not request.HasField("timestamp")
    assert request.timestamp == PrecisionTimestamp()


def test___publish_analog_waveform_data_without_t0___uses_timestamp_parameter(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    analog_waveform = AnalogWaveform.from_array_1d([1.0, 2.0, 3.0], dtype=float)
    publish_measurement_response = PublishMeasurementResponse(measurement_id="response_id")
    mocked_data_store_service_client.publish_measurement.return_value = publish_measurement_response

    measurement_id = data_store_client.publish_measurement(
        "name", analog_waveform, "step_id", timestamp
    )

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])  # The PublishMeasurementRequest object
    assert measurement_id == "response_id"
    assert request.timestamp == hightime_datetime_to_protobuf(timestamp)


def test___publish_analog_waveform_data_with_mismatched_timestamp_parameter___uses_provided_timestamp(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    waveform_values = [1.0, 2.0, 3.0]
    analog_waveform = AnalogWaveform(
        sample_count=len(waveform_values),
        raw_data=np.array(waveform_values, dtype=np.float64),
        timing=Timing.create_with_regular_interval(timedelta(seconds=1), timestamp),
    )
    mismatched_timestamp = timestamp + timedelta(seconds=1)
    mocked_data_store_service_client.publish_measurement.return_value = PublishMeasurementResponse(
        measurement_id="response_id"
    )

    measurement_id = data_store_client.publish_measurement(
        "name", analog_waveform, "step_id", mismatched_timestamp
    )

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])
    assert measurement_id == "response_id"
    assert request.timestamp == hightime_datetime_to_protobuf(mismatched_timestamp)


def test___publish_analog_waveform_data_without_t0_or_timestamp___timestamp_is_unset(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    analog_waveform = AnalogWaveform.from_array_1d([1.0, 2.0, 3.0], dtype=float)
    mocked_data_store_service_client.publish_measurement.return_value = PublishMeasurementResponse(
        measurement_id="response_id"
    )

    data_store_client.publish_measurement("name", analog_waveform, "step_id")

    args, __ = mocked_data_store_service_client.publish_measurement.call_args
    request = cast(PublishMeasurementRequest, args[0])
    assert not request.HasField("timestamp")
    assert request.timestamp == PrecisionTimestamp()


def test___none___publish_measurement___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_measurement(
            name="name",
            value=None,
            step_id="step_id",
        )

    assert exc.value.args[0].startswith("Unsupported measurement value type")


def test___vector___publish_measurement_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementBatchResponse(measurement_ids=["response_id"])
    mocked_data_store_service_client.publish_measurement_batch.return_value = expected_response

    measurement_ids = data_store_client.publish_measurement_batch(
        name="name",
        values=Vector(values=[1.0, 2.0, 3.0], units="BatchUnits"),
        step_id="step_id",
        timestamps=[timestamp],
        outcomes=[Outcome.PASSED],
        error_information=[ErrorInformation()],
        hardware_item_ids=[],
        test_adapter_ids=[],
        software_item_ids=[],
    )

    args, __ = mocked_data_store_service_client.publish_measurement_batch.call_args
    request = cast(PublishMeasurementBatchRequest, args[0])
    assert next(iter(measurement_ids)) == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.timestamps == [hightime_datetime_to_protobuf(timestamp)]
    assert request.scalar_values.double_array.values == [1.0, 2.0, 3.0]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == "BatchUnits"
    assert request.outcomes == [OutcomeProto.OUTCOME_PASSED]
    assert request.error_information == [ErrorInformationProto()]
    assert request.hardware_item_ids == []
    assert request.software_item_ids == []
    assert request.test_adapter_ids == []


def test___int_list___publish_measurement_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementBatchResponse(measurement_ids=["response_id"])
    mocked_data_store_service_client.publish_measurement_batch.return_value = expected_response

    measurement_ids = data_store_client.publish_measurement_batch(
        name="name",
        values=[1, 2, 3],
        step_id="step_id",
        timestamps=[timestamp],
        outcomes=[Outcome.PASSED],
        error_information=[ErrorInformation()],
        hardware_item_ids=[],
        test_adapter_ids=[],
        software_item_ids=[],
    )

    args, __ = mocked_data_store_service_client.publish_measurement_batch.call_args
    request = cast(PublishMeasurementBatchRequest, args[0])
    assert next(iter(measurement_ids)) == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.timestamps == [hightime_datetime_to_protobuf(timestamp)]
    assert request.scalar_values.sint32_array.values == [1, 2, 3]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___float_list___publish_measurement_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementBatchResponse(measurement_ids=["response_id"])
    mocked_data_store_service_client.publish_measurement_batch.return_value = expected_response

    measurement_ids = data_store_client.publish_measurement_batch(
        name="name",
        values=[1.0, 2.0, 3.0],
        step_id="step_id",
        timestamps=[timestamp],
        outcomes=[Outcome.PASSED],
        error_information=[ErrorInformation()],
        hardware_item_ids=[],
        test_adapter_ids=[],
        software_item_ids=[],
    )

    args, __ = mocked_data_store_service_client.publish_measurement_batch.call_args
    request = cast(PublishMeasurementBatchRequest, args[0])
    assert next(iter(measurement_ids)) == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.timestamps == [hightime_datetime_to_protobuf(timestamp)]
    assert request.scalar_values.double_array.values == [1.0, 2.0, 3.0]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___bool_list___publish_measurement_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementBatchResponse(measurement_ids=["response_id"])
    mocked_data_store_service_client.publish_measurement_batch.return_value = expected_response

    measurement_ids = data_store_client.publish_measurement_batch(
        name="name",
        values=[True, False, True],
        step_id="step_id",
        timestamps=[timestamp],
        outcomes=[Outcome.PASSED],
        error_information=[ErrorInformation()],
        hardware_item_ids=[],
        test_adapter_ids=[],
        software_item_ids=[],
    )

    args, __ = mocked_data_store_service_client.publish_measurement_batch.call_args
    request = cast(PublishMeasurementBatchRequest, args[0])
    assert next(iter(measurement_ids)) == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.timestamps == [hightime_datetime_to_protobuf(timestamp)]
    assert request.scalar_values.bool_array.values == [True, False, True]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___str_list___publish_measurement_batch___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    timestamp = datetime.now(tz=std_datetime.timezone.utc)
    expected_response = PublishMeasurementBatchResponse(measurement_ids=["response_id"])
    mocked_data_store_service_client.publish_measurement_batch.return_value = expected_response

    measurement_ids = data_store_client.publish_measurement_batch(
        name="name",
        values=["one", "two", "three"],
        step_id="step_id",
        timestamps=[timestamp],
        outcomes=[Outcome.PASSED],
        error_information=[ErrorInformation()],
        hardware_item_ids=[],
        test_adapter_ids=[],
        software_item_ids=[],
    )

    args, __ = mocked_data_store_service_client.publish_measurement_batch.call_args
    request = cast(PublishMeasurementBatchRequest, args[0])
    assert next(iter(measurement_ids)) == "response_id"
    assert request.step_id == "step_id"
    assert request.name == "name"
    assert request.timestamps == [hightime_datetime_to_protobuf(timestamp)]
    assert request.scalar_values.string_array.values == ["one", "two", "three"]
    assert request.scalar_values.attributes["NI_UnitDescription"].string_value == ""


def test___unsupported_list___publish_measurement_batch___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_measurement_batch(
            name="name",
            values=[[1, 2, 3], [4, 5, 6]],  # List of lists will error during vector creation.
            step_id="step_id",
        )

    assert exc.value.args[0].startswith("Unsupported iterable.")


def test___empty_list___publish_measurement_batch___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(ValueError) as exc:
        _ = data_store_client.publish_measurement_batch(
            name="name",
            values=[],
            step_id="step_id",
        )

    assert exc.value.args[0].startswith("Cannot publish an empty Iterable.")


def test___none___publish_measurement_batch___raises_type_error(
    data_store_client: DataStoreClient,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = data_store_client.publish_measurement_batch(
            name="name",
            values=None,
            step_id="step_id",
        )

    assert exc.value.args[0].startswith("Unsupported measurement values type")
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_query_metadata.py sha256=9f914fa1621dc9985a8ccafdb1143293d3ed46b74fcd792cb37c8f2de4fc28a0 bytes=1679 -->
## FILE: tests/unit/data/test_query_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_query_metadata.py`
- sha256: `9f914fa1621dc9985a8ccafdb1143293d3ed46b74fcd792cb37c8f2de4fc28a0`
- bytes: 1679

````python
"""Contains tests to validate the query_* methods in the data store."""

from __future__ import annotations

import datetime as std_datetime
from typing import cast
from unittest.mock import NonCallableMock

from hightime import datetime
from ni.measurements.data.v1.data_store_pb2 import Step as StepProto
from ni.measurements.data.v1.data_store_service_pb2 import (
    QueryStepsRequest,
    QueryStepsResponse,
)
from ni.protobuf.types.precision_timestamp_conversion import (
    hightime_datetime_to_protobuf,
)

from ni.datastore.data import (
    DataStoreClient,
    Step,
)


def test___query_steps___calls_data_store_service_client(
    data_store_client: DataStoreClient,
    mocked_data_store_service_client: NonCallableMock,
) -> None:
    start_time = datetime.now(tz=std_datetime.timezone.utc)
    end_time = datetime.now(tz=std_datetime.timezone.utc)
    step = StepProto(
        id="step_id",
        parent_step_id="parent_step_id",
        test_result_id="test_result",
        test_id="test_id",
        name="step_name",
        step_type="step_type",
        notes="step_notes",
        start_date_time=hightime_datetime_to_protobuf(start_time),
        end_date_time=hightime_datetime_to_protobuf(end_time),
    )
    mocked_data_store_service_client.query_steps.return_value = QueryStepsResponse(steps=[step])

    result = data_store_client.query_steps(odata_query="request_query")

    args, __ = mocked_data_store_service_client.query_steps.call_args
    request = cast(QueryStepsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [Step.from_protobuf(step)]
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/data/test_read.py sha256=47531fd6f48ac9c81d6c2b72b60a861d5ac6eb1272dd1e6d8a85abeeb4518221 bytes=13480 -->
## FILE: tests/unit/data/test_read.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/data/test_read.py`
- sha256: `47531fd6f48ac9c81d6c2b72b60a861d5ac6eb1272dd1e6d8a85abeeb4518221`
- bytes: 13480

````python
"""Contains tests to validate the data store client read functionality."""

from __future__ import annotations

from unittest.mock import Mock, NonCallableMock

import numpy as np
import pytest
from ni.protobuf.types import (
    array_pb2,
    attribute_value_pb2,
    vector_pb2,
    waveform_pb2,
    xydata_pb2,
)
from nitypes.complex import ComplexInt32DType
from nitypes.vector import Vector
from nitypes.waveform import AnalogWaveform, ComplexWaveform, DigitalWaveform, Spectrum
from nitypes.xy_data import XYData

from ni.datastore.data import DataStoreClient, PublishedCondition, PublishedMeasurement


def test___read_measurement_value___calls_data_store_client(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-123")
    expected_waveform = waveform_pb2.DoubleAnalogWaveform(y_data=[1.0, 2.0, 3.0])
    response = Mock()
    response.WhichOneof.return_value = "double_analog_waveform"
    response.double_analog_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, AnalogWaveform
    )

    mocked_data_store_service_client.read_measurement_value.assert_called_once()
    args, __ = mocked_data_store_service_client.read_measurement_value.call_args
    request = args[0]
    assert request.measurement_id == "measurement-123"
    assert isinstance(actual_waveform, AnalogWaveform)
    assert list(actual_waveform.scaled_data) == list(expected_waveform.y_data)


def test___read_double_analog_waveform___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-123")
    expected_waveform = waveform_pb2.DoubleAnalogWaveform(y_data=[1.0, 2.0, 3.0])
    response = Mock()
    response.WhichOneof.return_value = "double_analog_waveform"
    response.double_analog_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, AnalogWaveform
    )

    assert isinstance(actual_waveform, AnalogWaveform)
    assert list(actual_waveform.scaled_data) == list(expected_waveform.y_data)


def test___read_i16_analog_waveform___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-456")
    expected_waveform = waveform_pb2.I16AnalogWaveform(y_data=[1, 2, 3])
    response = Mock()
    response.WhichOneof.return_value = "i16_analog_waveform"
    response.i16_analog_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, AnalogWaveform
    )

    assert isinstance(actual_waveform, AnalogWaveform)
    assert list(actual_waveform.raw_data) == list(expected_waveform.y_data)


def test___read_double_complex_waveform___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-789")
    expected_waveform = waveform_pb2.DoubleComplexWaveform(y_data=[1.0, 2.0, 3.0, 4.0])
    response = Mock()
    response.WhichOneof.return_value = "double_complex_waveform"
    response.double_complex_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, ComplexWaveform
    )

    assert isinstance(actual_waveform, ComplexWaveform)
    assert actual_waveform.sample_count == actual_waveform.capacity == 2
    assert len(actual_waveform.raw_data) == 2
    assert actual_waveform.dtype == np.complex128


def test___read_i16_complex_waveform___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-101")
    expected_waveform = waveform_pb2.I16ComplexWaveform(y_data=[1, 2, 3, 4])
    response = Mock()
    response.WhichOneof.return_value = "i16_complex_waveform"
    response.i16_complex_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, ComplexWaveform
    )

    assert isinstance(actual_waveform, ComplexWaveform)
    assert actual_waveform.sample_count == actual_waveform.capacity == 2
    assert len(actual_waveform.raw_data) == 2
    assert actual_waveform.dtype == ComplexInt32DType


def test___read_digital_waveform___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-202")
    data = np.array([[0, 1, 0], [1, 0, 1]], dtype=np.bool)
    expected_waveform = waveform_pb2.DigitalWaveform(y_data=data.tobytes(), signal_count=3)
    response = Mock()
    response.WhichOneof.return_value = "digital_waveform"
    response.digital_waveform = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(
        published_measurement, DigitalWaveform
    )

    assert isinstance(actual_waveform, DigitalWaveform)
    assert np.array_equal(actual_waveform.data, data)
    assert actual_waveform.signal_count == 3


def test___read_double_spectrum___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-303")
    expected_waveform = waveform_pb2.DoubleSpectrum(
        data=[1.0, 2.0, 3.0],
        start_frequency=100.0,
        frequency_increment=10.0,
    )
    response = Mock()
    response.WhichOneof.return_value = "double_spectrum"
    response.double_spectrum = expected_waveform
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_waveform = data_store_client.read_measurement_value(published_measurement, Spectrum)

    assert isinstance(actual_waveform, Spectrum)
    assert list(actual_waveform.data) == [1.0, 2.0, 3.0]
    assert actual_waveform.start_frequency == 100.0
    assert actual_waveform.frequency_increment == 10.0


def test___read_vector___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-404")
    attrs = {"NI_UnitDescription": attribute_value_pb2.AttributeValue(string_value="amps")}
    expected_vector = vector_pb2.Vector(
        attributes=attrs,
        double_array=array_pb2.DoubleArray(values=[1.0, 2.0, 3.0]),
    )
    response = Mock()
    response.WhichOneof.return_value = "vector"
    response.vector = expected_vector
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_vector = data_store_client.read_measurement_value(published_measurement, Vector)

    assert isinstance(actual_vector, Vector)
    assert list(actual_vector) == [1.0, 2.0, 3.0]
    assert actual_vector.units == "amps"


def test___read_xydata___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-505")
    attrs = {
        "NI_UnitDescription_X": attribute_value_pb2.AttributeValue(string_value="amps"),
        "NI_UnitDescription_Y": attribute_value_pb2.AttributeValue(string_value="seconds"),
    }
    expected_xydata = xydata_pb2.DoubleXYData(
        x_data=[1.0, 2.0],
        y_data=[3.0, 4.0],
        attributes=attrs,
    )
    response = Mock()
    response.WhichOneof.return_value = "x_y_data"
    response.x_y_data = expected_xydata
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_xydata = data_store_client.read_measurement_value(published_measurement, XYData)

    assert isinstance(actual_xydata, XYData)
    assert list(actual_xydata.x_data) == [1.0, 2.0]
    assert list(actual_xydata.y_data) == [3.0, 4.0]
    assert actual_xydata.x_units == "amps"
    assert actual_xydata.y_units == "seconds"


def test___read_condition_value___value_correct(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_condition = PublishedCondition(id="condition-789")
    attrs = {"NI_UnitDescription": attribute_value_pb2.AttributeValue(string_value="volts")}
    expected_vector = vector_pb2.Vector(
        attributes=attrs,
        double_array=array_pb2.DoubleArray(values=[5.0, 6.0, 7.0]),
    )
    response = Mock()
    response.WhichOneof.return_value = "vector"
    response.vector = expected_vector
    mocked_data_store_service_client.read_condition_value.return_value = response

    actual_vector = data_store_client.read_condition_value(published_condition, Vector)

    mocked_data_store_service_client.read_condition_value.assert_called_once()
    args, __ = mocked_data_store_service_client.read_condition_value.call_args
    request = args[0]
    assert request.condition_id == "condition-789"
    assert isinstance(actual_vector, Vector)
    assert list(actual_vector) == [5.0, 6.0, 7.0]
    assert actual_vector.units == "volts"


def test___read_measurement_value___without_expected_type___returns_object(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-999")
    expected_vector = vector_pb2.Vector(
        double_array=array_pb2.DoubleArray(values=[1.0, 2.0, 3.0]),
    )
    response = Mock()
    response.WhichOneof.return_value = "vector"
    response.vector = expected_vector
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_value = data_store_client.read_measurement_value(published_measurement)

    # Without expected_type, it returns the converted Python object
    assert isinstance(actual_value, Vector)
    assert list(actual_value) == [1.0, 2.0, 3.0]


def test___read_measurement_value___with_matching_expected_type___returns_typed_value(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-888")
    expected_vector = vector_pb2.Vector(
        double_array=array_pb2.DoubleArray(values=[1.0, 2.0, 3.0]),
    )
    response = Mock()
    response.WhichOneof.return_value = "vector"
    response.vector = expected_vector
    mocked_data_store_service_client.read_measurement_value.return_value = response

    actual_value = data_store_client.read_measurement_value(published_measurement, Vector)

    assert isinstance(actual_value, Vector)
    assert list(actual_value) == [1.0, 2.0, 3.0]


def test___read_measurement_value___with_mismatched_expected_type___raises_type_error(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-777")
    expected_vector = vector_pb2.Vector(
        double_array=array_pb2.DoubleArray(values=[1.0, 2.0, 3.0]),
    )
    response = Mock()
    response.WhichOneof.return_value = "vector"
    response.vector = expected_vector
    mocked_data_store_service_client.read_measurement_value.return_value = response

    with pytest.raises(TypeError, match="Expected type.*AnalogWaveform.*got"):
        data_store_client.read_measurement_value(published_measurement, AnalogWaveform)


def test___read_measurement_value___unsupported_type___raises_type_error(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_measurement = PublishedMeasurement(id="measurement-666")
    response = Mock()
    response.WhichOneof.return_value = "unknown_type"
    mocked_data_store_service_client.read_measurement_value.return_value = response

    with pytest.raises(TypeError, match="Invalid read type: unknown_type"):
        data_store_client.read_measurement_value(published_measurement)


def test___read_condition_value___unsupported_type___raises_type_error(
    data_store_client: DataStoreClient, mocked_data_store_service_client: NonCallableMock
) -> None:
    published_condition = PublishedCondition(id="condition-555")
    response = Mock()
    response.WhichOneof.return_value = "unknown_type"
    mocked_data_store_service_client.read_condition_value.return_value = response

    with pytest.raises(TypeError, match="Invalid read type: unknown_type"):
        data_store_client.read_condition_value(published_condition)
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/__init__.py sha256=b2490319454fd5f5fff9dd7b854b32d96a5caf1768fb20f355ea65b24ee1ce19 bytes=32 -->
## FILE: tests/unit/metadata/__init__.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/__init__.py`
- sha256: `b2490319454fd5f5fff9dd7b854b32d96a5caf1768fb20f355ea65b24ee1ce19`
- bytes: 32

````python
"""Unit tests for metadata."""
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_alias_target_type.py sha256=be1c6cfaa261e4870cfab3e00fb64e09e38dac9deb0cc88cdb9eaa9bf975f875 bytes=8264 -->
## FILE: tests/unit/metadata/test_alias_target_type.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_alias_target_type.py`
- sha256: `be1c6cfaa261e4870cfab3e00fb64e09e38dac9deb0cc88cdb9eaa9bf975f875`
- bytes: 8264

````python
"""Tests for the AliasTargetType wrapper enum."""

from __future__ import annotations

from typing import cast

import pytest
from ni.measurements.metadata.v1.metadata_store_pb2 import (
    AliasTargetType as AliasTargetTypeProto,
)

from ni.datastore.metadata import AliasTargetType


def test___enum_values___match_protobuf_values() -> None:
    """Test that enum values match the protobuf enum values."""
    assert AliasTargetType.UNSPECIFIED.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UNSPECIFIED
    assert AliasTargetType.UUT_INSTANCE.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT_INSTANCE
    assert AliasTargetType.UUT.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT
    assert (
        AliasTargetType.HARDWARE_ITEM.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_HARDWARE_ITEM
    )
    assert (
        AliasTargetType.SOFTWARE_ITEM.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_SOFTWARE_ITEM
    )
    assert AliasTargetType.OPERATOR.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_OPERATOR
    assert (
        AliasTargetType.TEST_DESCRIPTION.value
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_DESCRIPTION
    )
    assert AliasTargetType.TEST.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST
    assert AliasTargetType.TEST_STATION.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_STATION
    assert AliasTargetType.TEST_ADAPTER.value == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_ADAPTER


def test___enum_values___have_expected_integer_values() -> None:
    """Test that enum has the expected integer values."""
    assert AliasTargetType.UNSPECIFIED.value == 0
    assert AliasTargetType.UUT_INSTANCE.value == 1
    assert AliasTargetType.UUT.value == 2
    assert AliasTargetType.HARDWARE_ITEM.value == 3
    assert AliasTargetType.SOFTWARE_ITEM.value == 4
    assert AliasTargetType.OPERATOR.value == 5
    assert AliasTargetType.TEST_DESCRIPTION.value == 6
    assert AliasTargetType.TEST.value == 7
    assert AliasTargetType.TEST_STATION.value == 8
    assert AliasTargetType.TEST_ADAPTER.value == 9


def test___to_protobuf___converts_enum_to_protobuf_value() -> None:
    """Test converting enum to protobuf value."""
    assert (
        AliasTargetType.UNSPECIFIED.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UNSPECIFIED
    )
    assert (
        AliasTargetType.UUT_INSTANCE.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT_INSTANCE
    )
    assert AliasTargetType.UUT.to_protobuf() == AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT
    assert (
        AliasTargetType.HARDWARE_ITEM.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_HARDWARE_ITEM
    )
    assert (
        AliasTargetType.SOFTWARE_ITEM.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_SOFTWARE_ITEM
    )
    assert AliasTargetType.OPERATOR.to_protobuf() == AliasTargetTypeProto.ALIAS_TARGET_TYPE_OPERATOR
    assert (
        AliasTargetType.TEST_DESCRIPTION.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_DESCRIPTION
    )
    assert AliasTargetType.TEST.to_protobuf() == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST
    assert (
        AliasTargetType.TEST_STATION.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_STATION
    )
    assert (
        AliasTargetType.TEST_ADAPTER.to_protobuf()
        == AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_ADAPTER
    )


def test___from_protobuf___converts_protobuf_value_to_enum() -> None:
    """Test converting protobuf value to enum."""
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_UNSPECIFIED)
        == AliasTargetType.UNSPECIFIED
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT_INSTANCE)
        == AliasTargetType.UUT_INSTANCE
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_UUT)
        == AliasTargetType.UUT
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_HARDWARE_ITEM)
        == AliasTargetType.HARDWARE_ITEM
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_SOFTWARE_ITEM)
        == AliasTargetType.SOFTWARE_ITEM
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_OPERATOR)
        == AliasTargetType.OPERATOR
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_DESCRIPTION)
        == AliasTargetType.TEST_DESCRIPTION
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST)
        == AliasTargetType.TEST
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_STATION)
        == AliasTargetType.TEST_STATION
    )
    assert (
        AliasTargetType.from_protobuf(AliasTargetTypeProto.ALIAS_TARGET_TYPE_TEST_ADAPTER)
        == AliasTargetType.TEST_ADAPTER
    )


def test___round_trip_conversion___preserves_enum_value() -> None:
    """Test that converting to protobuf and back gives the same result."""
    for alias_target_type in AliasTargetType:
        pb_alias_target_type = alias_target_type.to_protobuf()
        back_to_enum = AliasTargetType.from_protobuf(pb_alias_target_type)
        assert alias_target_type == back_to_enum


def test___invalid_value___from_protobuf___raises_value_error() -> None:
    """Test that from_protobuf raises ValueError for invalid values."""
    with pytest.raises(ValueError, match="Unknown alias target type value"):
        AliasTargetType.from_protobuf(cast(AliasTargetTypeProto.ValueType, 999))


def test___enum___is_iterable() -> None:
    """Test that the enum can be iterated over."""
    alias_target_types = list(AliasTargetType)
    assert len(alias_target_types) == 10
    assert AliasTargetType.UNSPECIFIED in alias_target_types
    assert AliasTargetType.UUT_INSTANCE in alias_target_types
    assert AliasTargetType.UUT in alias_target_types
    assert AliasTargetType.HARDWARE_ITEM in alias_target_types
    assert AliasTargetType.SOFTWARE_ITEM in alias_target_types
    assert AliasTargetType.OPERATOR in alias_target_types
    assert AliasTargetType.TEST_DESCRIPTION in alias_target_types
    assert AliasTargetType.TEST in alias_target_types
    assert AliasTargetType.TEST_STATION in alias_target_types
    assert AliasTargetType.TEST_ADAPTER in alias_target_types


def test___enum___has_correct_name_and_value_attributes() -> None:
    """Test that enum has correct name and value attributes."""
    assert AliasTargetType.UUT_INSTANCE.name == "UUT_INSTANCE"
    assert AliasTargetType.UUT_INSTANCE.value == 1
    assert AliasTargetType.TEST.name == "TEST"
    assert AliasTargetType.TEST.value == 7
    assert AliasTargetType.TEST_ADAPTER.name == "TEST_ADAPTER"
    assert AliasTargetType.TEST_ADAPTER.value == 9


def test___enum___supports_comparison() -> None:
    """Test that enum supports comparison operations."""
    assert AliasTargetType.UNSPECIFIED < AliasTargetType.UUT_INSTANCE
    assert AliasTargetType.UUT_INSTANCE <= AliasTargetType.UUT_INSTANCE
    assert AliasTargetType.UUT_INSTANCE <= AliasTargetType.UUT
    assert AliasTargetType.TEST_ADAPTER > AliasTargetType.TEST_STATION
    assert AliasTargetType.TEST_ADAPTER >= AliasTargetType.TEST_STATION
    assert AliasTargetType.TEST_ADAPTER >= AliasTargetType.TEST_ADAPTER


def test___enum___supports_integer_operations() -> None:
    """Test that enum supports integer operations since it inherits from IntEnum."""
    # Can be used as integers
    assert AliasTargetType.UNSPECIFIED + 1 == 1
    assert AliasTargetType.UUT_INSTANCE * 2 == 2
    assert AliasTargetType.TEST - 1 == 6

    # Can be compared with integers
    assert AliasTargetType.UNSPECIFIED.value == 0
    assert AliasTargetType.TEST_ADAPTER.value == 9

    # Can be used in arithmetic contexts
    values = [AliasTargetType.UNSPECIFIED, AliasTargetType.UUT_INSTANCE, AliasTargetType.UUT]
    assert sum(values) == 3  # 0 + 1 + 2
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_close_client.py sha256=40c7fb21fabed0918f99fee5523342f1b66019fd3ef9642839a86bf4dc452a2d bytes=1709 -->
## FILE: tests/unit/metadata/test_close_client.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_close_client.py`
- sha256: `40c7fb21fabed0918f99fee5523342f1b66019fd3ef9642839a86bf4dc452a2d`
- bytes: 1709

````python
"""Contains tests related to closing the MetadataStoreClient."""

from __future__ import annotations

from unittest.mock import NonCallableMock

import pytest

from ni.datastore.metadata import MetadataStoreClient


def test___exit_metadata_store_client_context___calls_close_on_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    metadata_store_client.query_operators()

    with metadata_store_client:
        pass

    mocked_metadata_store_service_client.close.assert_called_once()


def test___close_metadata_store_client___calls_close_on_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    metadata_store_client.query_operators()

    metadata_store_client.close()

    mocked_metadata_store_service_client.close.assert_called_once()


def test___exit_metadata_store_client_context___call_method___raises_error(
    metadata_store_client: MetadataStoreClient,
) -> None:
    with metadata_store_client:
        pass

    with pytest.raises(RuntimeError) as exc:
        metadata_store_client.query_operators()

    assert exc.value.args[0] == MetadataStoreClient._METADATA_STORE_CLIENT_CLOSED_ERROR


def test___close_metadata_store_client___call_method___raises_error(
    metadata_store_client: MetadataStoreClient,
) -> None:
    metadata_store_client.close()

    with pytest.raises(RuntimeError) as exc:
        metadata_store_client.query_operators()

    assert exc.value.args[0] == MetadataStoreClient._METADATA_STORE_CLIENT_CLOSED_ERROR
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_create_from_json.py sha256=1fdb7982d453f4ab4deeca379dc28c33bded2b1ca84e4ae743cf64b2f2df392e bytes=12104 -->
## FILE: tests/unit/metadata/test_create_from_json.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_create_from_json.py`
- sha256: `1fdb7982d453f4ab4deeca379dc28c33bded2b1ca84e4ae743cf64b2f2df392e`
- bytes: 12104

````python
"""Contains tests for validating JSON metadata creation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast
from unittest.mock import NonCallableMock

import pytest
from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    CreateFromJsonDocumentRequest,
    CreateFromJsonDocumentResponse,
)

from ni.datastore.metadata import (
    MetadataItems,
    MetadataStoreClient,
)


@pytest.fixture
def sample_metadata_json() -> str:
    """Sample JSON metadata for testing."""
    return json.dumps(
        {
            "uuts": [
                {"alias": "uut1", "modelName": "Model1", "partNumber": "PN001"},
                {"alias": "uut2", "modelName": "Model2", "family": "TestFamily"},
            ],
            "operators": [
                {"alias": "op1", "name": "John Doe", "role": "Test Engineer"},
                {"alias": "op2", "name": "Jane Smith", "role": "Lab Technician"},
            ],
            "tests": [
                {"alias": "test1", "name": "Test 1", "description": "First test description"},
                {"alias": "test2", "name": "Test 2", "description": "Second test description"},
            ],
            "hardwareItems": [
                {"alias": "hw1", "manufacturer": "NI", "model": "PXI-5172", "serialNumber": "SN001"}
            ],
            "softwareItems": [{"alias": "sw1", "product": "TestStand", "version": "2023"}],
            "testStations": [
                {"alias": "station1", "name": "Station Alpha", "assetIdentifier": "ASSET001"}
            ],
            "testAdapters": [
                {
                    "alias": "adapter1",
                    "name": "Test Fixture A",
                    "manufacturer": "Custom",
                    "serialNumber": "FIX001",
                }
            ],
            "uutInstances": [
                {
                    "alias": "instance1",
                    "uutAlias": "uut1",
                    "serialNumber": "UUT-SN001",
                    "firmwareVersion": "1.0.0",
                }
            ],
            "testDescriptions": [
                {"alias": "desc1", "uutAlias": "uut1", "name": "UUT1 Test Description"}
            ],
        },
        indent=2,
    )


@pytest.fixture
def mock_create_response() -> CreateFromJsonDocumentResponse:
    """Mock response for create_from_json_document."""
    response = CreateFromJsonDocumentResponse()
    # Add mock entities to the response as needed for testing
    return response


def test___create_from_json_file_with_pathlib_path___calls_metadata_store_service_client_with_file_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    tmp_path: Path,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json_file with Path object calls service client with file contents."""
    # Arrange
    metadata_file = tmp_path / "test_metadata.json"
    metadata_file.write_text(sample_metadata_json, encoding="utf-8")
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json_file(metadata_file)

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == sample_metadata_json
    assert isinstance(result, MetadataItems)


def test___create_from_json_file_with_string_path___calls_metadata_store_service_client_with_file_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    tmp_path: Path,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json_file with string path calls service client with file contents."""
    # Arrange
    metadata_file = tmp_path / "test_metadata.json"
    metadata_file.write_text(sample_metadata_json, encoding="utf-8")
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json_file(str(metadata_file))

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == sample_metadata_json
    assert isinstance(result, MetadataItems)


def test___create_from_json_file_with_non_existent_pathlib_path___raises_error(
    metadata_store_client: MetadataStoreClient,
    tmp_path: Path,
) -> None:
    """Test that create_from_json_file raises FileNotFoundError for non-existent Path."""
    # Arrange
    metadata_file = tmp_path / "non_existent_metadata.json"

    # Act & Assert
    with pytest.raises(FileNotFoundError, match="Metadata file not found"):
        metadata_store_client.create_from_json_file(metadata_file)


def test___create_from_json_file_with_non_existent_string_path___raises_error(
    metadata_store_client: MetadataStoreClient,
    tmp_path: Path,
) -> None:
    """Test that create_from_json_file raises FileNotFoundError for non-existent string path."""
    # Arrange
    metadata_file = tmp_path / "non_existent_metadata.json"

    # Act & Assert
    with pytest.raises(FileNotFoundError, match="Metadata file not found"):
        metadata_store_client.create_from_json_file(str(metadata_file))


def test___create_from_json_file_with_utf8_bom___handles_encoding_correctly(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    tmp_path: Path,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json_file correctly handles UTF-8 BOM encoding."""
    # Arrange - Write file with UTF-8 BOM
    metadata_file = tmp_path / "test_metadata_bom.json"
    metadata_file.write_text(sample_metadata_json, encoding="utf-8-sig")
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json_file(metadata_file)

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == sample_metadata_json  # BOM should be stripped
    assert isinstance(result, MetadataItems)


def test___create_from_json___calls_metadata_store_service_client_with_json_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json calls service client with JSON contents."""
    # Arrange
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json(sample_metadata_json)

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == sample_metadata_json
    assert isinstance(result, MetadataItems)


def test___create_from_json___returns_metadata_items_from_protobuf_response(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json returns MetadataItems from protobuf response."""
    # Arrange
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json(sample_metadata_json)

    # Assert
    assert isinstance(result, MetadataItems)
    # Verify that MetadataItems.from_protobuf was called with the mock response
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == sample_metadata_json


def test___create_from_json_with_minimal_json___handles_empty_collections(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json handles minimal JSON with empty collections."""
    # Arrange
    minimal_json = json.dumps({"uuts": [{"modelName": "SimpleModel"}]})
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json(minimal_json)

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == minimal_json
    assert isinstance(result, MetadataItems)


def test___create_from_json_with_complex_extensions___preserves_extension_data(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json preserves complex extension data."""
    # Arrange
    json_with_extensions = json.dumps(
        {
            "operators": [
                {
                    "name": "Test Operator",
                    "role": "Engineer",
                    "schemaId": "custom-schema-123",
                    "extension": {
                        "customField1": "value1",
                        "customField2": "value2",
                        "department": "R&D",
                    },
                }
            ],
            "hardwareItems": [
                {
                    "manufacturer": "NI",
                    "model": "PXI-5172",
                    "serialNumber": "12345",
                    "extension": {"calibrationDate": "2024-01-15", "location": "Lab A"},
                }
            ],
        }
    )
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json(json_with_extensions)

    # Assert
    args, __ = mocked_metadata_store_service_client.create_from_json_document.call_args
    request = cast(CreateFromJsonDocumentRequest, args[0])
    assert request.json_document == json_with_extensions
    assert isinstance(result, MetadataItems)


def test___create_from_json_file___returns_metadata_items_from_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    tmp_path: Path,
    sample_metadata_json: str,
    mock_create_response: CreateFromJsonDocumentResponse,
) -> None:
    """Test that create_from_json_file returns MetadataItems from service client."""
    # Arrange
    metadata_file = tmp_path / "test_metadata.json"
    metadata_file.write_text(sample_metadata_json, encoding="utf-8")
    mocked_metadata_store_service_client.create_from_json_document.return_value = (
        mock_create_response
    )

    # Act
    result = metadata_store_client.create_from_json_file(metadata_file)

    # Assert
    assert isinstance(result, MetadataItems)
    mocked_metadata_store_service_client.create_from_json_document.assert_called_once()
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_create_metadata.py sha256=837b015ab47b8e71ba65bf3575fed275b204ae8019728db0df8e98a770637d96 bytes=9215 -->
## FILE: tests/unit/metadata/test_create_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_create_metadata.py`
- sha256: `837b015ab47b8e71ba65bf3575fed275b204ae8019728db0df8e98a770637d96`
- bytes: 9215

````python
"""Contains tests to validate the create_* methods for the metadata store."""

from __future__ import annotations

from typing import cast
from unittest.mock import NonCallableMock

from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    CreateHardwareItemRequest,
    CreateHardwareItemResponse,
    CreateOperatorRequest,
    CreateOperatorResponse,
    CreateSoftwareItemRequest,
    CreateSoftwareItemResponse,
    CreateTestAdapterRequest,
    CreateTestAdapterResponse,
    CreateTestDescriptionRequest,
    CreateTestDescriptionResponse,
    CreateTestRequest,
    CreateTestResponse,
    CreateTestStationRequest,
    CreateTestStationResponse,
    CreateUutInstanceRequest,
    CreateUutInstanceResponse,
    CreateUutRequest,
    CreateUutResponse,
)

from ni.datastore.metadata import (
    HardwareItem,
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    Test,
    TestAdapter,
    TestDescription,
    TestStation,
    Uut,
    UutInstance,
)


def test___create_uut_instance___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut_instance = UutInstance(
        uut_id="uut_id",
        serial_number="serial_number",
        manufacture_date="manufacture_date",
        firmware_version="firmware_version",
        hardware_version="hardware_version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateUutInstanceResponse(uut_instance_id="response_id")
    mocked_metadata_store_service_client.create_uut_instance.return_value = expected_response

    result = metadata_store_client.create_uut_instance(uut_instance)

    args, __ = mocked_metadata_store_service_client.create_uut_instance.call_args
    request = cast(CreateUutInstanceRequest, args[0])
    assert request.uut_instance == uut_instance.to_protobuf()
    assert result == "response_id"


def test___create_uut___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut = Uut(
        model_name="model_name",
        family="family",
        manufacturers=None,
        part_number="part_number",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateUutResponse(uut_id="response_id")
    mocked_metadata_store_service_client.create_uut.return_value = expected_response

    result = metadata_store_client.create_uut(uut)

    args, __ = mocked_metadata_store_service_client.create_uut.call_args
    request = cast(CreateUutRequest, args[0])
    assert request.uut == uut.to_protobuf()
    assert result == "response_id"


def test___create_operator___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    operator = Operator(
        name="operator_name",
        role="role",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateOperatorResponse(operator_id="response_id")
    mocked_metadata_store_service_client.create_operator.return_value = expected_response

    result = metadata_store_client.create_operator(operator)

    args, __ = mocked_metadata_store_service_client.create_operator.call_args
    request = cast(CreateOperatorRequest, args[0])
    assert request.operator == operator.to_protobuf()
    assert result == "response_id"


def test___create_test_description___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_description = TestDescription(
        uut_id="uut_id",
        name="test_description_name",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateTestDescriptionResponse(test_description_id="response_id")
    mocked_metadata_store_service_client.create_test_description.return_value = expected_response

    result = metadata_store_client.create_test_description(test_description)

    args, __ = mocked_metadata_store_service_client.create_test_description.call_args
    request = cast(CreateTestDescriptionRequest, args[0])
    assert request.test_description == test_description.to_protobuf()
    assert result == "response_id"


def test___create_test___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test = Test(
        name="test_name",
        description="description",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateTestResponse(test_id="response_id")
    mocked_metadata_store_service_client.create_test.return_value = expected_response

    result = metadata_store_client.create_test(test)

    args, __ = mocked_metadata_store_service_client.create_test.call_args
    request = cast(CreateTestRequest, args[0])
    assert request.test == test.to_protobuf()
    assert result == "response_id"


def test___create_test_station___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_station = TestStation(
        name="test_station_name",
        asset_identifier="asset_identifier",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateTestStationResponse(test_station_id="response_id")
    mocked_metadata_store_service_client.create_test_station.return_value = expected_response

    result = metadata_store_client.create_test_station(test_station)

    args, __ = mocked_metadata_store_service_client.create_test_station.call_args
    request = cast(CreateTestStationRequest, args[0])
    assert request.test_station == test_station.to_protobuf()
    assert result == "response_id"


def test___create_hardware_item___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    hardware_item = HardwareItem(
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateHardwareItemResponse(hardware_item_id="response_id")
    mocked_metadata_store_service_client.create_hardware_item.return_value = expected_response

    result = metadata_store_client.create_hardware_item(hardware_item)

    args, __ = mocked_metadata_store_service_client.create_hardware_item.call_args
    request = cast(CreateHardwareItemRequest, args[0])
    assert request.hardware_item == hardware_item.to_protobuf()
    assert result == "response_id"


def test___create_software_item___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    software_item = SoftwareItem(
        product="product",
        version="version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateSoftwareItemResponse(software_item_id="response_id")
    mocked_metadata_store_service_client.create_software_item.return_value = expected_response

    result = metadata_store_client.create_software_item(software_item)

    args, __ = mocked_metadata_store_service_client.create_software_item.call_args
    request = cast(CreateSoftwareItemRequest, args[0])
    assert request.software_item == software_item.to_protobuf()
    assert result == "response_id"


def test___create_test_adapter___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_adapter = TestAdapter(
        name="test_adapter_name",
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = CreateTestAdapterResponse(test_adapter_id="response_id")
    mocked_metadata_store_service_client.create_test_adapter.return_value = expected_response

    result = metadata_store_client.create_test_adapter(test_adapter)

    args, __ = mocked_metadata_store_service_client.create_test_adapter.call_args
    request = cast(CreateTestAdapterRequest, args[0])
    assert request.test_adapter == test_adapter.to_protobuf()
    assert result == "response_id"
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_get_metadata.py sha256=bab5c92eb02ab9d31d1c09c4f4e0960c54ec0dd2d397b0b563b836a66f98af6e bytes=9859 -->
## FILE: tests/unit/metadata/test_get_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_get_metadata.py`
- sha256: `bab5c92eb02ab9d31d1c09c4f4e0960c54ec0dd2d397b0b563b836a66f98af6e`
- bytes: 9859

````python
"""Contains tests to validate the get_* methods in the metadata store."""

from __future__ import annotations

from typing import cast
from unittest.mock import NonCallableMock

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    HardwareItem as HardwareItemProto,
    Operator as OperatorProto,
    SoftwareItem as SoftwareItemProto,
    Test as TestProto,
    TestAdapter as TestAdapterProto,
    TestDescription as TestDescriptionProto,
    TestStation as TestStationProto,
    Uut as UutProto,
    UutInstance as UutInstanceProto,
)
from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    GetHardwareItemRequest,
    GetHardwareItemResponse,
    GetOperatorRequest,
    GetOperatorResponse,
    GetSoftwareItemRequest,
    GetSoftwareItemResponse,
    GetTestAdapterRequest,
    GetTestAdapterResponse,
    GetTestDescriptionRequest,
    GetTestDescriptionResponse,
    GetTestRequest,
    GetTestResponse,
    GetTestStationRequest,
    GetTestStationResponse,
    GetUutInstanceRequest,
    GetUutInstanceResponse,
    GetUutRequest,
    GetUutResponse,
)

from ni.datastore.metadata import (
    HardwareItem,
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    Test,
    TestAdapter,
    TestDescription,
    TestStation,
    Uut,
    UutInstance,
)


def test___get_uut_instance___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut_instance = UutInstanceProto(
        id="uut_instance_id",
        uut_id="uut_id",
        serial_number="serial_number",
        manufacture_date="manufacture_date",
        firmware_version="firmware_version",
        hardware_version="hardware_version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetUutInstanceResponse(uut_instance=uut_instance)
    mocked_metadata_store_service_client.get_uut_instance.return_value = expected_response

    result = metadata_store_client.get_uut_instance(uut_instance_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_uut_instance.call_args
    request = cast(GetUutInstanceRequest, args[0])
    assert request.uut_instance_id == "request_id"
    assert result == UutInstance.from_protobuf(uut_instance)


def test___get_uut___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut = UutProto(
        id="uut_id",
        model_name="model_name",
        family="family",
        manufacturers=None,
        part_number="part_number",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetUutResponse(uut=uut)
    mocked_metadata_store_service_client.get_uut.return_value = expected_response

    result = metadata_store_client.get_uut(uut_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_uut.call_args
    request = cast(GetUutRequest, args[0])
    assert request.uut_id == "request_id"
    assert result == Uut.from_protobuf(uut)


def test___get_operator___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    operator = OperatorProto(
        id="operator_id",
        name="name",
        role="role",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetOperatorResponse(operator=operator)
    mocked_metadata_store_service_client.get_operator.return_value = expected_response

    result = metadata_store_client.get_operator(operator_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_operator.call_args
    request = cast(GetOperatorRequest, args[0])
    assert request.operator_id == "request_id"
    assert result == Operator.from_protobuf(operator)


def test___get_test_description___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_description = TestDescriptionProto(
        id="test_description_id",
        uut_id="uut_id",
        name="name",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetTestDescriptionResponse(test_description=test_description)
    mocked_metadata_store_service_client.get_test_description.return_value = expected_response

    result = metadata_store_client.get_test_description(test_description_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_test_description.call_args
    request = cast(GetTestDescriptionRequest, args[0])
    assert request.test_description_id == "request_id"
    assert result == TestDescription.from_protobuf(test_description)


def test___get_test___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test = TestProto(
        id="test_id",
        name="name",
        description="description",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetTestResponse(test=test)
    mocked_metadata_store_service_client.get_test.return_value = expected_response

    result = metadata_store_client.get_test(test_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_test.call_args
    request = cast(GetTestRequest, args[0])
    assert request.test_id == "request_id"
    assert result == Test.from_protobuf(test)


def test___get_test_station___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_station = TestStationProto(
        id="test_station_id",
        name="name",
        asset_identifier="asset_identifier",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetTestStationResponse(test_station=test_station)
    mocked_metadata_store_service_client.get_test_station.return_value = expected_response

    result = metadata_store_client.get_test_station(test_station_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_test_station.call_args
    request = cast(GetTestStationRequest, args[0])
    assert request.test_station_id == "request_id"
    assert result == TestStation.from_protobuf(test_station)


def test___get_hardware_item___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    hardware_item = HardwareItemProto(
        id="hardware_item_id",
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetHardwareItemResponse(hardware_item=hardware_item)
    mocked_metadata_store_service_client.get_hardware_item.return_value = expected_response

    result = metadata_store_client.get_hardware_item(hardware_item_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_hardware_item.call_args
    request = cast(GetHardwareItemRequest, args[0])
    assert request.hardware_item_id == "request_id"
    assert result == HardwareItem.from_protobuf(hardware_item)


def test___get_software_item___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    software_item = SoftwareItemProto(
        id="software_item_id",
        product="product",
        version="version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetSoftwareItemResponse(software_item=software_item)
    mocked_metadata_store_service_client.get_software_item.return_value = expected_response

    result = metadata_store_client.get_software_item(software_item_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_software_item.call_args
    request = cast(GetSoftwareItemRequest, args[0])
    assert request.software_item_id == "request_id"
    assert result == SoftwareItem.from_protobuf(software_item)


def test___get_test_adapter___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_adapter = TestAdapterProto(
        id="test_adapter_id",
        name="test_adapter_name",
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = GetTestAdapterResponse(test_adapter=test_adapter)
    mocked_metadata_store_service_client.get_test_adapter.return_value = expected_response

    result = metadata_store_client.get_test_adapter(test_adapter_id="request_id")

    args, __ = mocked_metadata_store_service_client.get_test_adapter.call_args
    request = cast(GetTestAdapterRequest, args[0])
    assert request.test_adapter_id == "request_id"
    assert result == TestAdapter.from_protobuf(test_adapter)
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_query_metadata.py sha256=a59e0782e091e778551314f2d644f94bca61ca276c886183396bf6c352b0882b bytes=10188 -->
## FILE: tests/unit/metadata/test_query_metadata.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_query_metadata.py`
- sha256: `a59e0782e091e778551314f2d644f94bca61ca276c886183396bf6c352b0882b`
- bytes: 10188

````python
"""Contains tests to validate the query_* methods in the metadata store."""

from __future__ import annotations

from typing import cast
from unittest.mock import NonCallableMock

from ni.measurements.metadata.v1.metadata_store_pb2 import (
    HardwareItem as HardwareItemProto,
    Operator as OperatorProto,
    SoftwareItem as SoftwareItemProto,
    Test as TestProto,
    TestAdapter as TestAdapterProto,
    TestDescription as TestDescriptionProto,
    TestStation as TestStationProto,
    Uut as UutProto,
    UutInstance as UutInstanceProto,
)
from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    QueryHardwareItemsRequest,
    QueryHardwareItemsResponse,
    QueryOperatorsRequest,
    QueryOperatorsResponse,
    QuerySoftwareItemsRequest,
    QuerySoftwareItemsResponse,
    QueryTestAdaptersRequest,
    QueryTestAdaptersResponse,
    QueryTestDescriptionsRequest,
    QueryTestDescriptionsResponse,
    QueryTestsRequest,
    QueryTestsResponse,
    QueryTestStationsRequest,
    QueryTestStationsResponse,
    QueryUutInstancesRequest,
    QueryUutInstancesResponse,
    QueryUutsRequest,
    QueryUutsResponse,
)

from ni.datastore.metadata import (
    HardwareItem,
    MetadataStoreClient,
    Operator,
    SoftwareItem,
    Test,
    TestAdapter,
    TestDescription,
    TestStation,
    Uut,
    UutInstance,
)


def test___query_uut_instances___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut_instance = UutInstanceProto(
        id="uut_instance_id",
        uut_id="uut_id",
        serial_number="serial_number",
        manufacture_date="manufacture_date",
        firmware_version="firmware_version",
        hardware_version="hardware_version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryUutInstancesResponse(uut_instances=[uut_instance])
    mocked_metadata_store_service_client.query_uut_instances.return_value = expected_response

    result = metadata_store_client.query_uut_instances(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_uut_instances.call_args
    request = cast(QueryUutInstancesRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [UutInstance.from_protobuf(uut_instance)]


def test___query_uuts___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    uut = UutProto(
        id="uut_id",
        model_name="model_name",
        family="family",
        manufacturers=None,
        part_number="part_number",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryUutsResponse(uuts=[uut])
    mocked_metadata_store_service_client.query_uuts.return_value = expected_response

    result = metadata_store_client.query_uuts(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_uuts.call_args
    request = cast(QueryUutsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [Uut.from_protobuf(uut)]


def test___query_operators___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    operator = OperatorProto(
        id="operator_id",
        name="name",
        role="role",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryOperatorsResponse(operators=[operator])
    mocked_metadata_store_service_client.query_operators.return_value = expected_response

    result = metadata_store_client.query_operators(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_operators.call_args
    request = cast(QueryOperatorsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [Operator.from_protobuf(operator)]


def test___query_test_descriptions___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_description = TestDescriptionProto(
        id="test_description_id",
        uut_id="uut_id",
        name="name",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryTestDescriptionsResponse(test_descriptions=[test_description])
    mocked_metadata_store_service_client.query_test_descriptions.return_value = expected_response

    result = metadata_store_client.query_test_descriptions(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_test_descriptions.call_args
    request = cast(QueryTestDescriptionsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [TestDescription.from_protobuf(test_description)]


def test___query_tests___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test = TestProto(
        id="test_id",
        name="name",
        description="description",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryTestsResponse(tests=[test])
    mocked_metadata_store_service_client.query_tests.return_value = expected_response

    result = metadata_store_client.query_tests(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_tests.call_args
    request = cast(QueryTestsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [Test.from_protobuf(test)]


def test___query_test_stations___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_station = TestStationProto(
        id="test_station_id",
        name="name",
        asset_identifier="asset_identifier",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryTestStationsResponse(test_stations=[test_station])
    mocked_metadata_store_service_client.query_test_stations.return_value = expected_response

    result = metadata_store_client.query_test_stations(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_test_stations.call_args
    request = cast(QueryTestStationsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [TestStation.from_protobuf(test_station)]


def test___query_hardware_items___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    hardware_item = HardwareItemProto(
        id="hardware_item_id",
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryHardwareItemsResponse(hardware_items=[hardware_item])
    mocked_metadata_store_service_client.query_hardware_items.return_value = expected_response

    result = metadata_store_client.query_hardware_items(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_hardware_items.call_args
    request = cast(QueryHardwareItemsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [HardwareItem.from_protobuf(hardware_item)]


def test___query_software_items___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    software_item = SoftwareItemProto(
        id="software_item_id",
        product="product",
        version="version",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QuerySoftwareItemsResponse(software_items=[software_item])
    mocked_metadata_store_service_client.query_software_items.return_value = expected_response

    result = metadata_store_client.query_software_items(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_software_items.call_args
    request = cast(QuerySoftwareItemsRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [SoftwareItem.from_protobuf(software_item)]


def test___query_test_adapters___calls_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
) -> None:
    test_adapter = TestAdapterProto(
        id="test_adapter_id",
        name="test_adapter_name",
        manufacturer="manufacturer",
        model="model",
        serial_number="serial_number",
        part_number="part_number",
        asset_identifier="asset_identifier",
        calibration_due_date="calibration_due_date",
        link="link",
        extension=None,
        schema_id="schema_id",
    )
    expected_response = QueryTestAdaptersResponse(test_adapters=[test_adapter])
    mocked_metadata_store_service_client.query_test_adapters.return_value = expected_response

    result = metadata_store_client.query_test_adapters(odata_query="request_query")

    args, __ = mocked_metadata_store_service_client.query_test_adapters.call_args
    request = cast(QueryTestAdaptersRequest, args[0])
    assert request.odata_query == "request_query"
    assert list(result) == [TestAdapter.from_protobuf(test_adapter)]
````

<!--NI_OSS_SOURCE repo=datastore-python path=tests/unit/metadata/test_register_schema.py sha256=1846698b09689b00dcea3555c9b7dee3dfc8ade5116cf447beb20946163126a0 bytes=4011 -->
## FILE: tests/unit/metadata/test_register_schema.py

- repository: `ni/datastore-python`
- source_path: `tests/unit/metadata/test_register_schema.py`
- sha256: `1846698b09689b00dcea3555c9b7dee3dfc8ade5116cf447beb20946163126a0`
- bytes: 4011

````python
"""Contains tests for validating schema registration."""

from __future__ import annotations

from pathlib import Path
from typing import cast
from unittest.mock import NonCallableMock

import pytest
from ni.measurements.metadata.v1.metadata_store_service_pb2 import (
    RegisterSchemaRequest,
)

from ni.datastore.metadata import (
    MetadataStoreClient,
)


def test___register_schema_from_file_with_pathlib_path___calls_metadata_store_service_client_with_file_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    schemas_directory: Path,
) -> None:
    schema_path = schemas_directory / "hardware_item_schema.toml"

    metadata_store_client.register_schema_from_file(schema_path)

    args, __ = mocked_metadata_store_service_client.register_schema.call_args
    request = cast(RegisterSchemaRequest, args[0])
    assert request.schema == schema_path.read_text()


def test___register_schema_from_file_with_string_path___calls_metadata_store_service_client_with_file_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    schemas_directory: Path,
) -> None:
    schema_path = schemas_directory / "hardware_item_schema.toml"

    metadata_store_client.register_schema_from_file(str(schema_path))

    args, __ = mocked_metadata_store_service_client.register_schema.call_args
    request = cast(RegisterSchemaRequest, args[0])
    assert request.schema == schema_path.read_text()


def test___register_schema_from_file_with_non_existent_pathlib_path___raises_error(
    metadata_store_client: MetadataStoreClient, schemas_directory: Path
) -> None:
    schema_path = schemas_directory / "non_existent_schema.toml"

    with pytest.raises(FileNotFoundError):
        metadata_store_client.register_schema_from_file(schema_path)


def test___register_schema_from_file_with_non_existent_string_path___raises_error(
    metadata_store_client: MetadataStoreClient, schemas_directory: Path
) -> None:
    schema_path = schemas_directory / "non_existent_schema.toml"

    with pytest.raises(FileNotFoundError):
        metadata_store_client.register_schema_from_file(str(schema_path))


def test___register_schema_from_file___returns_schema_id_from_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    schemas_directory: Path,
) -> None:
    schema_path = schemas_directory / "hardware_item_schema.toml"
    expected_schema_id = "schema_id_123"
    mocked_metadata_store_service_client.register_schema.return_value.schema_id = expected_schema_id

    schema_id = metadata_store_client.register_schema_from_file(schema_path)

    assert schema_id == expected_schema_id


def test___register_schema___calls_metadata_store_service_client_with_schema_contents(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    schemas_directory: Path,
) -> None:
    schema_path = schemas_directory / "hardware_item_schema.toml"

    metadata_store_client.register_schema(schema_path.read_text())

    args, __ = mocked_metadata_store_service_client.register_schema.call_args
    request = cast(RegisterSchemaRequest, args[0])
    assert request.schema == schema_path.read_text()


def test___register_schema___returns_schema_id_from_metadata_store_service_client(
    metadata_store_client: MetadataStoreClient,
    mocked_metadata_store_service_client: NonCallableMock,
    schemas_directory: Path,
) -> None:
    schema_path = schemas_directory / "hardware_item_schema.toml"
    expected_schema_id = "schema_id_123"
    mocked_metadata_store_service_client.register_schema.return_value.schema_id = expected_schema_id

    schema_id = metadata_store_client.register_schema(schema_path.read_text())

    assert schema_id == expected_schema_id
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/poetry.lock sha256=c996ce823dd59ca242466574708238c9b879ed578865bf712882edfd7349c9b3 bytes=56560 -->
## FILE: utilities/poetry.lock

- repository: `ni/datastore-python`
- source_path: `utilities/poetry.lock`
- sha256: `c996ce823dd59ca242466574708238c9b879ed578865bf712882edfd7349c9b3`
- bytes: 56560

````text
# This file is automatically @generated by Poetry 2.1.4 and should not be changed by hand.

[[package]]
name = "ast-serialize"
version = "0.5.0"
description = "Python bindings for mypy AST serialization"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8f5c14f169eb0972c0c21bada5358b23d6047c76583b005234f865b11f1fa00a"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7d1a2de9de5be04652f0ed60738356ef94f66db37924a9499fffe98dc491aa0b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:be5173fb66f9b49026d9d5a2ff0fc7c7009077107c0eb285b2d60fdf1fe10bd1"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f8015cd071ac1339924ee2b8098c93e00e155f30a16f40ec9816fcf84f4753f6"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5499e8797edff2a9186aa313ed382c6b422e798e9332d9953badcee6e69a88f2"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6848f2a093fb5548751a9a09bff8fcd229e2bbeb0e3331f391b6ae6d26cd9903"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:832d4c998e0b091fd60a6d6bceee535483c4d490de9ba85003af835225719261"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:16db7c62ec0b8efe1d7afd283a388d8f74f2605d56032e5a37747d2de8dba027"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:baf5eb061eb5bccade4128ad42da33787d72f6013809cd1b590376ece8b3c937"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:104e4a35bd7c124173c41760ef9aaea17ddb3f86c65cb643671d59afbe3ee94c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:36be371028fc1675acb38a331bde160dbab7ff907fdf00b67eb6911aa106951b"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:061ee58bdb52341c8201a6df41182a977736bae3b7ded87ca7176ca25a8a47ab"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b15219e9cdc9f53f6f4cb51c009203507228226148c05c5e8fe451c28b435eb3"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win32.whl", hash = "sha256:842d1c004bb466c7df036f95fabef789570541922b10976b12f5592a69cf0b38"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b0c06d760909b095cc466356dfccd05a1c7233a6ca191c020dca2c6a6f16c24c"},
    {file = "ast_serialize-0.5.0-cp314-cp314t-win_arm64.whl", hash = "sha256:787baedb0262cc49e8ce37cc15c00ae818e46a165a3b36f5e21ed174998104cb"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:0668aa9459cfa8c9c49ddd2163ebcf43088ba045ef7492af6fe22e0098303101"},
    {file = "ast_serialize-0.5.0-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:bf683d6363edf2b39eed6b6d4fe22d34b6203867a67e27134d9e2a2680c4bc4a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9cc22cf0c9be65e71cf88fda130af60d61eb4a79370ad4cfe7900d48a4aa2211"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f66173891548c9f2726bf27957b41cabce12fa679dc6da505ddbde4d4b3b31cf"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e42d729ef2be96a14efbad355093284739e3670ece3e534f82cc8832790911d9"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b725026bafa801dbd7310eb13a75f0a2e370e7e51b2cb225f9d21fcfadf919ee"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b54f60c1d78767a53b67eaa663f0dfac3afe606aa07f1301572f588b73d64809"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_31_riscv64.whl", hash = "sha256:27d51654fc240a1e87e742d353d98eb45b75f62f129086b3596ab53df2ac2a43"},
    {file = "ast_serialize-0.5.0-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c36237c46dd1674542f2109740ea5ea485a169bf1431939ada0434e17934"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:1943db345233cc7194a470f13afa9c59772c0b123dea0c9414c4d4ca54369759"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:df1c00022cbbcb064bfaa505aa9c9295362443ce5dacb459d1331d3da353f887"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:cae65289fc456fde04af979a2be09302ef5d8ab92ef23e596d6746dc267ada27"},
    {file = "ast_serialize-0.5.0-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:239a4c354e8d676e9d94631d1d4a64edc6b266f86ff3a5a80aedd344f342c01d"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win32.whl", hash = "sha256:143a4ef63285a075871908fda3672dc21864b83a8ec3ee12304aa3e4c5387b9a"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_amd64.whl", hash = "sha256:cf25572c526add400f26a4750dc6ce0c3bb93fc1f75e7ae0cad4ce4f2cd5c590"},
    {file = "ast_serialize-0.5.0-cp39-abi3-win_arm64.whl", hash = "sha256:92a31c9c20d25a076edaeec76b128a3535d74a24f340b9a8a7e96c9b86dc9642"},
    {file = "ast_serialize-0.5.0.tar.gz", hash = "sha256:5880091bfe6f4f986f22866375c2e884843e7a0b6343ae41aeea659613d879b6"},
]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["lint"]
files = [
    {file = "better_diff-0.1.4-py3-none-any.whl", hash = "sha256:06e63358b2047ae2695abd96316f47c6d3c38b9e641f53012279878d66d8792e"},
    {file = "better_diff-0.1.4.tar.gz", hash = "sha256:920ca76bdbcd2f0c361fa5d9a2d4727624a3545d6cb467b1b6616cad8a634de7"},
]

[[package]]
name = "black"
version = "25.12.0"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "black-25.12.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f85ba1ad15d446756b4ab5f3044731bf68b777f8f9ac9cdabd2425b97cd9c4e8"},
    {file = "black-25.12.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:546eecfe9a3a6b46f9d69d8a642585a6eaf348bcbbc4d87a19635570e02d9f4a"},
    {file = "black-25.12.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:17dcc893da8d73d8f74a596f64b7c98ef5239c2cd2b053c0f25912c4494bf9ea"},
    {file = "black-25.12.0-cp310-cp310-win_amd64.whl", hash = "sha256:09524b0e6af8ba7a3ffabdfc7a9922fb9adef60fed008c7cd2fc01f3048e6e6f"},
    {file = "black-25.12.0-cp310-cp310-win_arm64.whl", hash = "sha256:b162653ed89eb942758efeb29d5e333ca5bb90e5130216f8369857db5955a7da"},
    {file = "black-25.12.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:d0cfa263e85caea2cff57d8f917f9f51adae8e20b610e2b23de35b5b11ce691a"},
    {file = "black-25.12.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a2f578ae20c19c50a382286ba78bfbeafdf788579b053d8e4980afb079ab9be"},
    {file = "black-25.12.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e1b65634b0e471d07ff86ec338819e2ef860689859ef4501ab7ac290431f9b"},
    {file = "black-25.12.0-cp311-cp311-win_amd64.whl", hash = "sha256:a3fa71e3b8dd9f7c6ac4d818345237dfb4175ed3bf37cd5a581dbc4c034f1ec5"},
    {file = "black-25.12.0-cp311-cp311-win_arm64.whl", hash = "sha256:51e267458f7e650afed8445dc7edb3187143003d52a1b710c7321aef22aa9655"},
    {file = "black-25.12.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:31f96b7c98c1ddaeb07dc0f56c652e25bdedaac76d5b68a059d998b57c55594a"},
    {file = "black-25.12.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:05dd459a19e218078a1f98178c13f861fe6a9a5f88fc969ca4d9b49eb1809783"},
    {file = "black-25.12.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c1f68c5eff61f226934be6b5b80296cf6939e5d2f0c2f7d543ea08b204bfaf59"},
    {file = "black-25.12.0-cp312-cp312-win_amd64.whl", hash = "sha256:274f940c147ddab4442d316b27f9e332ca586d39c85ecf59ebdea82cc9ee8892"},
    {file = "black-25.12.0-cp312-cp312-win_arm64.whl", hash = "sha256:169506ba91ef21e2e0591563deda7f00030cb466e747c4b09cb0a9dae5db2f43"},
    {file = "black-25.12.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:a05ddeb656534c3e27a05a29196c962877c83fa5503db89e68857d1161ad08a5"},
    {file = "black-25.12.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9ec77439ef3e34896995503865a85732c94396edcc739f302c5673a2315e1e7f"},
    {file = "black-25.12.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e509c858adf63aa61d908061b52e580c40eae0dfa72415fa47ac01b12e29baf"},
    {file = "black-25.12.0-cp313-cp313-win_amd64.whl", hash = "sha256:252678f07f5bac4ff0d0e9b261fbb029fa530cfa206d0a636a34ab445ef8ca9d"},
    {file = "black-25.12.0-cp313-cp313-win_arm64.whl", hash = "sha256:bc5b1c09fe3c931ddd20ee548511c64ebf964ada7e6f0763d443947fd1c603ce"},
    {file = "black-25.12.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:0a0953b134f9335c2434864a643c842c44fba562155c738a2a37a4d61f00cad5"},
    {file = "black-25.12.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:2355bbb6c3b76062870942d8cc450d4f8ac71f9c93c40122762c8784df49543f"},
    {file = "black-25.12.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9678bd991cc793e81d19aeeae57966ee02909877cb65838ccffef24c3ebac08f"},
    {file = "black-25.12.0-cp314-cp314-win_amd64.whl", hash = "sha256:97596189949a8aad13ad12fcbb4ae89330039b96ad6742e6f6b45e75ad5cfd83"},
    {file = "black-25.12.0-cp314-cp314-win_arm64.whl", hash = "sha256:778285d9ea197f34704e3791ea9404cd6d07595745907dd2ce3da7a13627b29b"},
    {file = "black-25.12.0-py3-none-any.whl", hash = "sha256:48ceb36c16dbc84062740049eef990bb2ce07598272e673c17d1a7720c71c828"},
    {file = "black-25.12.0.tar.gz", hash = "sha256:8d3dd9cea14bff7ddc0eb243c811cdb1a011ebb4800a5f0335a01a68654796a7"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=0.9.0"
platformdirs = ">=2"
pytokens = ">=0.3.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2)"]

[[package]]
name = "click"
version = "8.3.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6"},
    {file = "click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["lint"]
markers = "platform_system == \"Windows\""
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "flake8-5.0.4-py2.py3-none-any.whl", hash = "sha256:7a1cf6b73744f5806ab95e526f6f0d8c01c66d7bbe349562d22dfca20610b248"},
    {file = "flake8-5.0.4.tar.gz", hash = "sha256:6fbe320aad8d6b95cec8b8e47bc933004678dc63095be98528b7bdd2a9f510db"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.9.0,<2.10.0"
pyflakes = ">=2.5.0,<2.6.0"

[[package]]
name = "flake8"
version = "6.1.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.8.1"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "flake8-6.1.0-py2.py3-none-any.whl", hash = "sha256:ffdfce58ea94c6580c77888a86506937f9a1a227dfcd15f245d694ae20a6b6e5"},
    {file = "flake8-6.1.0.tar.gz", hash = "sha256:d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.11.0,<2.12.0"
pyflakes = ">=3.1.0,<3.2.0"

[[package]]
name = "flake8-black"
version = "0.4.0"
description = "flake8 plugin to call black as a code style validator"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_black-0.4.0-py3-none-any.whl", hash = "sha256:288762d0c9ea065782d87eeecbcc20c69079d17fe1d0f0445f0eb0b0ffb80c39"},
    {file = "flake8_black-0.4.0.tar.gz", hash = "sha256:bf226868f695dee48d55ff6d7747e900709bfd6f605b7a378c70e711e3fc26cb"},
]

[package.dependencies]
black = ">=22.1.0"
flake8 = ">=3"
tomli = {version = "*", markers = "python_version < \"3.11\""}

[package.extras]
develop = ["build", "twine"]

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["lint"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["lint"]
files = [
    {file = "flake8-import-order-0.18.2.tar.gz", hash = "sha256:e23941f892da3e0c09d711babbb0c73bc735242e9b216b726616758a920d900e"},
    {file = "flake8_import_order-0.18.2-py2.py3-none-any.whl", hash = "sha256:82ed59f1083b629b030ee9d3928d9e06b6213eb196fe745b3a7d4af2168130df"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "flake8-tidy-imports"
version = "4.12.0"
description = "A flake8 plugin that helps you write tidier imports."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "isort"
version = "7.0.0"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["lint"]
files = [
    {file = "isort-7.0.0-py3-none-any.whl", hash = "sha256:1bcabac8bc3c36c7fb7b98a76c8abb18e0f841a3ba81decac7691008592499c1"},
    {file = "isort-7.0.0.tar.gz", hash = "sha256:5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187"},
]

[package.extras]
colors = ["colorama"]
plugins = ["setuptools"]

[[package]]
name = "librt"
version = "0.11.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.11.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:6e94ebfcfa2d5e9926d6c3b9aa4617ffc42a845b4321fb84021b872358c82a0f"},
    {file = "librt-0.11.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:ae627397a2f351560440d872d6f7c8dbb4072e57868e7b2fc5b8b430fe489d45"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:dc329359321b67d24efdf4bc69012b0597001649544db662c001db5a0184794c"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:7e82e642ab0f7608ce2fe53d76ca2280a9ee33a1b06556142c7c6fe80a86fc33"},
    {file = "librt-0.11.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:88145c15c67731d54283d135b03244028c750cc9edc334a96a4f5950ebdb2884"},
    {file = "librt-0.11.0-cp310-cp310-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9d36a51b3d93320b686588e27123f4995804dbf1bce81df78c02fc3c6eea9280"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d00f3ac06a2a8b246327f11e186a53a100a4d5c7ed52346367e5ec751d51586c"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:461bbceede621f1ffb8839755f8663e886087ee7af16294cab7fb4d782c62eeb"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0cad8a4d6a8ff03c9b76f9414caccd78e7cfbc8a2e12fa334d8e1d9932753783"},
    {file = "librt-0.11.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f37aa505b3cf60701562eddb32df74b12a9e380c207fd8b06dd157a943ac7ea0"},
    {file = "librt-0.11.0-cp310-cp310-win32.whl", hash = "sha256:94663a21534637f0e787ec2a2a756022df6e5b7b2335a5cdd7d8e33d68a2af89"},
    {file = "librt-0.11.0-cp310-cp310-win_amd64.whl", hash = "sha256:dec7db73758c2b54953fd8b7fe348c45188fe26b39ee18446196edd08453a5d4"},
    {file = "librt-0.11.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:93d95bd45b7d58343d8b90d904450a545144eec19a002511163426f8ab1fae29"},
    {file = "librt-0.11.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ee278c769a713638cdacd4c0436d72156e75df3ebc0166ab2b9dc43acc386c9"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f230cb1cbc9faaa616f9a678f530ebcf186e414b6bcbd88b960e4ba1b92428d5"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:5d63c855d86938d9de93e265c9bd8c705b51ec494de5738340ee93767a686e4b"},
    {file = "librt-0.11.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:993f028be9e96a08d31df3479ac80d99be374d17f3b78e4796b3fd3c913d4e89"},
    {file = "librt-0.11.0-cp311-cp311-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:258d73a0aa66a055e65b2e4d1b8cdb23b9d132c5bb915d9547d804fcaed116cc"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0827efe7854718f04aaddf6496e96960a956e676fe1d0f04eb41511fd8ad06d5"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:7753e57d6e12d019c0d8786f1c09c709f4c3fcc57c3887b24e36e6c06ec938b7"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:11bd19822431cc21af9f27374e7ae2e58103c7d98bda823536a6c47f6bb2bb3d"},
    {file = "librt-0.11.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:22bdf239b219d3993761a148ffa134b19e52e9989c84f845d5d7b71d70a17412"},
    {file = "librt-0.11.0-cp311-cp311-win32.whl", hash = "sha256:46c60b61e308eb535fbd6fa622b1ee1bb2815691c1ad9c98bf7b84952ec3bc8d"},
    {file = "librt-0.11.0-cp311-cp311-win_amd64.whl", hash = "sha256:902e546ff044f579ff1c953ff5fce97b636fe9e3943996b2177710c6ef076f73"},
    {file = "librt-0.11.0-cp311-cp311-win_arm64.whl", hash = "sha256:65ac3bc20f78aa0ee5ae84baa68917f89fef4af63e941084dd019a0d0e749f0c"},
    {file = "librt-0.11.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b87504f1690a23b9a2cca841191a04f83895d4fc2dd04df91d82b1a04ca2ad46"},
    {file = "librt-0.11.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:40071fc5fe0ce8daa6de616702314a01e1250711682b0523d6ab8d4525910cb3"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:137e79445c896a0ea7b265f52d23954e05b64222ee1af69e2cb34219067cbb67"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:cca6644054e78746d8d4ef238681f9c34ff8b584fe6b988ecebb8db3b15e622a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5b0eea49f5562861ee8d757a32ef7d559c1d35be2aaaa1ec28941d74c9ffc8a"},
    {file = "librt-0.11.0-cp312-cp312-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0d1029d7e1ae1a7e647ed6fb5df8c4ce2dffefb7a9f5fd1376a4554d96dac09f"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:bc3ce6b33c5828d9e80592011a5c584cb2ce86edbc4088405f70da47dc1d1b3b"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:936c5995f3514a42111f20099397d8177c79b4d7e70961e396c6f5a0a3566766"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:9bc0ca6ad9381cbe8e4aa6e5726e4c80c78115a6e9723c599ed1d73e092bc49d"},
    {file = "librt-0.11.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:070aa8c26c0a74774317a72df8851facc7f0f012a5b406557ac56992d92e1ec8"},
    {file = "librt-0.11.0-cp312-cp312-win32.whl", hash = "sha256:6bf14feb84b05ae945277395451998c89c54d0def4070eb5c08de544930b245a"},
    {file = "librt-0.11.0-cp312-cp312-win_amd64.whl", hash = "sha256:75672f0bc524ede266287d532d7923dbce94c7514ad07627bac3d0c6d92cc4d9"},
    {file = "librt-0.11.0-cp312-cp312-win_arm64.whl", hash = "sha256:2f10cf143e4a9bb0f4f5af568a00df94a2d69ef41c2579584454bb0fe5cc642c"},
    {file = "librt-0.11.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:78dc31f7fdfe9c9d0eb0e8f42d139db230e826415bbcabd9f0e9faaaee909894"},
    {file = "librt-0.11.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:fa475675db22290c3158e1d42326d0f5a65f04f44a0e68c3630a25b53560fb9c"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:621db29691044bdeda22e789e482e1b0f3a985d90e3426c9c6d17606416205ea"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:a9010e2ed5b3a9e158c5fd966b3ab7e834bb3d3aacc8f66c91dd4b57a3799230"},
    {file = "librt-0.11.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7c39513d8b7477a2e1ed8c43fc21c524e8d5a0f8d4e8b7b074dbdbe7820a08e2"},
    {file = "librt-0.11.0-cp313-cp313-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7aef3cf1d5af86e770ab04bfd993dfc4ae8b8c17f66fb77dd4a7d50de7bbb1a3"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:557183ddc36babe46b27dd60facbd5adb4492181a5be887587d57cda6e092f21"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:83d3e1f72bd42f6c5c0b7daec530c3f829bd02db42c70b8ddf0c2d90a2459930"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:4ce1f21fbe589bc1afd7872dece84fb0e1144f794a288e58a10d2c54a55c43be"},
    {file = "librt-0.11.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b09f7044ea2b64c9da42fd3d335666518cfd1c6e8a182c95da73d0214b41e"},
    {file = "librt-0.11.0-cp313-cp313-win32.whl", hash = "sha256:78fddc31cd4d3caa897ad5d31f856b1faadc9474021ad6cb182b9018793e254e"},
    {file = "librt-0.11.0-cp313-cp313-win_amd64.whl", hash = "sha256:8ca8aa88751a775870b764e93bad5135385f563cb8dcee399abf034ea4d3cb47"},
    {file = "librt-0.11.0-cp313-cp313-win_arm64.whl", hash = "sha256:96f044bb325fd9cf1a723015638c219e9143f0dfbc0ca54c565df2b7fc748b44"},
    {file = "librt-0.11.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:4a017a95e5837dc15a8c5661d60e05daa96b90908b1aa6b7acdf443cd25c8ebd"},
    {file = "librt-0.11.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:b1ecbd9819deccc39b7542bf4d2a740d8a620694d39989e58661d3763458f8d4"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7da327dacd7be8f8ec36547373550744a3cc0e536d54665cd83f8bcd961200e8"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:0dc56b1f8d06e60db362cc3fdae206681817f86ce4725d34511473487f12a34b"},
    {file = "librt-0.11.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:05fb8fb2ab90e21c8d12ea240d744ad514da9baf381ebfa70d91d20d21713175"},
    {file = "librt-0.11.0-cp314-cp314-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cae74872be221df4374d10fec61f93ed1513b9546ea84f2c0bf73ab3e9bd0b03"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:32bcc918c0148eb7e3d57385125bac7e5f9e4359d05f07448b09f6f778c2f31c"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f9743fc99135d5f78d2454435615f6dec0473ca507c26ce9d92b10b562a280d3"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:5ba067f4aadae8fda802d91d2124c90c42195ff32d9161d3549e6d05cfe26f96"},
    {file = "librt-0.11.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:de3bf945454d032f9e390b85c4072e0a0570bf825421c8be0e71209fa65e1abe"},
    {file = "librt-0.11.0-cp314-cp314-win32.whl", hash = "sha256:d2277a05f6dcb9fd13db9566aac4fabd68c3ea1ea46ee5567d4eef8efa495a2f"},
    {file = "librt-0.11.0-cp314-cp314-win_amd64.whl", hash = "sha256:ab73e8db5e3f564d812c1f5c3a175930a5f9bc96ccb5e3b22a34d7858b401cf7"},
    {file = "librt-0.11.0-cp314-cp314-win_arm64.whl", hash = "sha256:aea3caa317752e3a466fa8af45d91ee0ea8c7fdd96e42b0a8dd9b76a7931eba1"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:d1b36540d7aaf9b9101b3a6f376c8d8e9f7a9aec93ed05918f2c69d493ffef72"},
    {file = "librt-0.11.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:efbb343ab2ce3540f4ecbe6315d677ed70f37cd9a72b1e58066c918ca83acbaa"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:aa0dd688aab3f7914d3e6e5e3554978e0383312fb8e771d84be008a35b9ee548"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:f5fb36b8c6c63fdcbb1d526d94c0d1331610d43f4118cc1beb4efef4f3faacb2"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4a9a237d13addb93715b6fee74023d5ee3469b53fce527626c0e088aa585805f"},
    {file = "librt-0.11.0-cp314-cp314t-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5ddd17bd87b2c56ddd60e546a7984a2e64c4e8eab92fb4cf3830a48ad5469d51"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:bd43992b4473d42f12ff9e68326079f0696d9d4e6000e8f39a0238d482ba6ee2"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:f8e3e8056dd674e279741485e2e512d6e9a751c7455809d0114e6ebf8d781085"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:c1f708d8ae9c56cf38a903c44297243d2ec83fd82b396b977e0144a3e76217e3"},
    {file = "librt-0.11.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0add982e0e7b9fc14cf4b33789d5f13f66581889b88c2f58099f6ce8f92617bd"},
    {file = "librt-0.11.0-cp314-cp314t-win32.whl", hash = "sha256:2b481d846ac894c4e8403c5fd0e87c5d11d6499e404b474602508a224ff531c8"},
    {file = "librt-0.11.0-cp314-cp314t-win_amd64.whl", hash = "sha256:28edb433edde181112a908c78907af28f964eabc15f4dd16c9d66c834302677c"},
    {file = "librt-0.11.0-cp314-cp314t-win_arm64.whl", hash = "sha256:dee008f20b542e3cd162ba338a7f9ec0f6d23d395f66fe8aeeec3c9d067ea253"},
    {file = "librt-0.11.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6bd72d903911d995ab666dbd1871f8b1e80925a699af8063fbf50053329fb05f"},
    {file = "librt-0.11.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0ef69ac715f3cd8e5cd252cb2aebfa72c015492aacc339d5d7bf8fef3c62c677"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:624a40c4a4ad7773315c287276cd024509b2c66ff5904f504bfc08d2c70293ab"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.manylinux_2_28_i686.whl", hash = "sha256:41dc19fe150b69716c8ece4f76773a9e8813fe3e35e032a58b4d46423fb8d7c0"},
    {file = "librt-0.11.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4e8bd98ea9c47ae90b319a087ab28dac493f1ffbc1ecd1f28fcdbf3b7e1108d1"},
    {file = "librt-0.11.0-cp39-cp39-manylinux_2_34_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:84308fc49423ce6475d1c5d1985cd69a8ca9f0325fc7d5f81bb690a3f3625d4e"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:ff0fbaf5f44a21beeb0110f2ab64f45135a9536a834b79c0d1ef018f2786bbfa"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9c028a9442a18e266955d364ce42259136e79a7ba14d773e0d778d5f70cd56f1"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:9f1692105a02bcf853f355032a5fdc5494358ef83d8fd22d16de375c85cec3f5"},
    {file = "librt-0.11.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7a80a71e1fda83cc752a9141e87aae7fef279538597564d670e9ce513f286192"},
    {file = "librt-0.11.0-cp39-cp39-win32.whl", hash = "sha256:140695816ddf3c86eb972981a26f35efd871c44b0c3aed44c8cd01749386617f"},
    {file = "librt-0.11.0-cp39-cp39-win_amd64.whl", hash = "sha256:92f7ff819c197fc30473190a12c2856f325ac90aabfccbeb2072d28cc2e234e3"},
    {file = "librt-0.11.0.tar.gz", hash = "sha256:075dc3ef4458a278e0195cbf6ac9d38808d9b906c5a6c7f7f79c3888276a3fb1"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mypy"
version = "2.1.0"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "mypy-2.1.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:11a6beb180257a805961aea9ec591bbd0bd17f1e18d35b8456d57aee5bedfedc"},
    {file = "mypy-2.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8ef78c1d306bbf9a8a12f526c44902c9c28dffd6c52c52bf6a72641ce18d3849"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c209a90853081ff01d01ee895cafe10f7db1474e0d95beaeef0f6c1db9119bbd"},
    {file = "mypy-2.1.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:47cebf61abde7c088a4e27718a8b13a81655686b2e9c251f5c0915a802248166"},
    {file = "mypy-2.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:d57a90ae5e872138a425ec328edbc9b235d1934c4377881a33ec05b341acc9a8"},
    {file = "mypy-2.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:aea7f7a8a55b459c34275fc468ada6ca7c173a5e43a68f5dbe588a563d8a06b8"},
    {file = "mypy-2.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:c989640253f0d76843e9c6c1bbf4bd48c5e85ada61bde4beb37cb3eca035685e"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a683016b16fe2f572dc04c72be7ee0504ac1605a265d0200f5cea695fb788f41"},
    {file = "mypy-2.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1a293c534adb55271fef24a26da04b855540a8c13cc07bc5917b9fd2c394f2ca"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7406f4d048e71e576f5356d317e5b0a9e666dfd966bd99f9d14ca06e1a341538"},
    {file = "mypy-2.1.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0210d626fc8b31ccc90233754c7bc90e1f43205e85d96387f7db1285b55c398"},
    {file = "mypy-2.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3712c20deed54e814eaaa825603bada8ea1c390670a397c95b98405347acc563"},
    {file = "mypy-2.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fcaa0e479066e31f7cceb6a3bea39cb22b2ff51a6b2f24f193d19179ba17c389"},
    {file = "mypy-2.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:0b1a5260c95aa443083f9ed3592662941951bca3d4ca224a5dc517c38b7cf666"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:244358bf1c0da7722230bce60683d52e8e9fd030554926f15b747a84efb5b3af"},
    {file = "mypy-2.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4ec7c57657493c7a75534df2751c8ae2cda383c16ecc55d2106c54476b1b16f6"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8161b6ff4392410023224f0969d17db93e1e154bc3e4ba62598e720723ae211"},
    {file = "mypy-2.1.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bf03e12003084a67395184d3eb8cbd6a489dc3655b5664b28c210a9e2403ab0b"},
    {file = "mypy-2.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:20509760fd791c51579d573153407d226385ec1f8bcce55d730b354f3336bc22"},
    {file = "mypy-2.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:6753d0c1fdd6b1a23b9e4f283ce80b2153b724adcb2653b20b85a8a28ac6436b"},
    {file = "mypy-2.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:98ebb6589bb3b6d0c6f0c459d53ca55b8091fbc13d277c4041c885392e8195e8"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:35aac3bb114e03888f535d5eb51b8bafbb3266586b599da1940f9b1be3ec5bd5"},
    {file = "mypy-2.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8de55a8c861f2a49331f807be98d90caeceeef520bde13d43a160207f8af613e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5fdf2941a07434af755837d9880f7d7d25f1dacb1af9dcd4b9b66f2220a3024e"},
    {file = "mypy-2.1.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e195b817c13f02352a9c124301f9f30f078405444679b6753c1b96b6eed37285"},
    {file = "mypy-2.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5431d42af987ebd92ba2f71d45c85ed41d8e6ca9f5fd209a69f68f707d2469e5"},
    {file = "mypy-2.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:767fe8c66dc3e01e19e1737d4c38ebefead16125e1b8e58ad421903b376f5c65"},
    {file = "mypy-2.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:ecfe70d43775ab99562ab128ce49854a362044c9f894961f68f898c23cb7429d"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:7354c5a7f69d9345c3d6e69921d57088eea3ddeeb6b20d34c1b3855b02c36ec2"},
    {file = "mypy-2.1.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:49890d4f76ac9e06ec117f9e09f3174da70a620a0c300953d8595c926e80947f"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:761be68e023ef5d94678772396a8af1220030f80837a3afd8d0aef3b419666f4"},
    {file = "mypy-2.1.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c90345fc182dc363b891350457ec69c35140858538f38b4540845afcc32b1aef"},
    {file = "mypy-2.1.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b84802e7b5a6daf1f5e15bc9fcd7ddae77be13981ffab037f1c67bb84d67d135"},
    {file = "mypy-2.1.0-cp314-cp314-win_amd64.whl", hash = "sha256:022c771234936ceac541ebaf836fe9e2abeb3f5e09aff21588fe543ff006fe21"},
    {file = "mypy-2.1.0-cp314-cp314-win_arm64.whl", hash = "sha256:498207db725cec88829a6a5c2fc771205fd043719ef98bc49aba8fb9fc4e6d57"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:7d5e5cad0efeba72b93cd17490cc0d69c5ac9ca132994fe3fb0314808aeeb83e"},
    {file = "mypy-2.1.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:ff715050c127d724fd260a2e666e7747fdd83511c0c47d449d98238970aef780"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:82208da9e09414d520e912d3e462d454854bed0810b71540bb016dcbca7308fd"},
    {file = "mypy-2.1.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e79ebc1b904b84f0310dff7469655a9c36c7a68bddb37bdd42b67a332df61d08"},
    {file = "mypy-2.1.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e583edc957cfb0deb142079162ae826f58449b116c1d442f2d91c69d9fced081"},
    {file = "mypy-2.1.0-cp314-cp314t-win_amd64.whl", hash = "sha256:b33b6cd332695bba180d55e717a79d3038e479a2c49cc5eb3d53603409b9a5d7"},
    {file = "mypy-2.1.0-cp314-cp314t-win_arm64.whl", hash = "sha256:4f910fe825376a7b66ef7ca8c98e5a149e8cd64c19ae71d84047a74ee060d4e6"},
    {file = "mypy-2.1.0-py3-none-any.whl", hash = "sha256:a663814603a5c563fb87a4f96fb473eeb30d1f5a4885afcf44f9db000a366289"},
    {file = "mypy-2.1.0.tar.gz", hash = "sha256:81e76ad12c2d804512e9b13240d1588316531bfba07558286078bfbce9613633"},
]

[package.dependencies]
ast-serialize = ">=0.3.0,<1.0.0"
librt = {version = ">=0.11.0", markers = "platform_python_implementation != \"PyPy\""}
mypy_extensions = ">=1.0.0"
pathspec = ">=1.0.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = [
    {version = ">=4.6.0", markers = "python_version < \"3.15\""},
    {version = ">=4.14.0", markers = "python_version >= \"3.15\""},
]

[package.extras]
dmypy = ["psutil (>=4.0)"]
faster-cache = ["orjson"]
install-types = ["pip"]
mypyc = ["setuptools (>=50)"]
reports = ["lxml"]

[[package]]
name = "mypy-extensions"
version = "1.1.0"
description = "Type system extensions for programs checked with the mypy type checker."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["lint"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "packaging"
version = "25.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484"},
    {file = "packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f"},
]

[[package]]
name = "pathspec"
version = "1.0.3"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pathspec-1.0.3-py3-none-any.whl", hash = "sha256:e80767021c1cc524aa3fb14bedda9c34406591343cc42797b386ce7b9354fb6c"},
    {file = "pathspec-1.0.3.tar.gz", hash = "sha256:bac5cf97ae2c2876e2d25ebb15078eb04d76e4b98921ee31c6f85ade8b59444d"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]
tests = ["pytest (>=9)", "typing-extensions (>=4.15)"]

[[package]]
name = "pep8-naming"
version = "0.15.1"
description = "Check PEP-8 naming conventions, plugin for flake8"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.5.1"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["lint"]
files = [
    {file = "platformdirs-4.5.1-py3-none-any.whl", hash = "sha256:d03afa3963c806a9bed9d5125c8f4cb2fdaf74a55ab60e5d59b3fde758104d31"},
    {file = "platformdirs-4.5.1.tar.gz", hash = "sha256:61d5cdcc6065745cdd94f0f878977f8de9437be93de97c1c12f853c9c0cdcbda"},
]

[package.extras]
docs = ["furo (>=2025.9.25)", "proselint (>=0.14)", "sphinx (>=8.2.3)", "sphinx-autodoc-typehints (>=3.2)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)"]
type = ["mypy (>=1.18.2)"]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pycodestyle-2.9.1-py2.py3-none-any.whl", hash = "sha256:d1735fc58b418fd7c5f658d28d943854f8a849b01a5d0a1e6f3f3fdd0166804b"},
    {file = "pycodestyle-2.9.1.tar.gz", hash = "sha256:2c9607871d58c76354b697b42f5d57e1ada7d261c261efac224b664affdc5785"},
]

[[package]]
name = "pycodestyle"
version = "2.11.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pycodestyle-2.11.1-py2.py3-none-any.whl", hash = "sha256:44fe31000b2d866f2e41841b18528a505fbd7fef9017b04eff4e2648a0fadc67"},
    {file = "pycodestyle-2.11.1.tar.gz", hash = "sha256:41ba0e7afc9752dfb53ced5489e89f8186be00e599e712660695b7a75ff2663f"},
]

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
files = [
    {file = "pydocstyle-6.3.0-py3-none-any.whl", hash = "sha256:118762d452a49d6b05e194ef344a55822987a462831ade91ec5c06fd2169d019"},
    {file = "pydocstyle-6.3.0.tar.gz", hash = "sha256:7ce43f0c0ac87b07494eb9c0b462c0b73e6ff276807f204d6b53edc72b7e44e1"},
]

[package.dependencies]
snowballstemmer = ">=2.2.0"

[package.extras]
toml = ["tomli (>=1.2.3) ; python_version < \"3.11\""]

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["lint"]
markers = "python_version < \"3.12\""
files = [
    {file = "pyflakes-2.5.0-py2.py3-none-any.whl", hash = "sha256:4579f67d887f804e67edb544428f264b7b24f435b263c4614f384135cea553d2"},
    {file = "pyflakes-2.5.0.tar.gz", hash = "sha256:491feb020dca48ccc562a8c0cbe8df07ee13078df59813b83959cbdada312ea3"},
]

[[package]]
name = "pyflakes"
version = "3.1.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pytokens"
version = "0.3.0"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["lint"]
files = [
    {file = "pytokens-0.3.0-py3-none-any.whl", hash = "sha256:95b2b5eaf832e469d141a378872480ede3f251a5a5041b8ec6e581d3ac71bbf3"},
    {file = "pytokens-0.3.0.tar.gz", hash = "sha256:2f932b14ed08de5fcf0b391ace2642f858f1394c0857202959000b68ed7a458a"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "setuptools"
version = "80.9.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "setuptools-80.9.0-py3-none-any.whl", hash = "sha256:062d34222ad13e0cc312a4c02d73f059e86a4acbfbdea8f8f76b28c99f306922"},
    {file = "setuptools-80.9.0.tar.gz", hash = "sha256:f36b47402ecde768dbfafc46e8e4207b4360c654f1f3bb84475f0a28628fb19c"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.8.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.14.*)", "pytest-mypy"]

[[package]]
name = "snowballstemmer"
version = "3.0.1"
description = "This package provides 32 stemmers for 30 languages generated from Snowball algorithms."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*"
groups = ["lint"]
files = [
    {file = "snowballstemmer-3.0.1-py3-none-any.whl", hash = "sha256:6cd7b3897da8d6c9ffb968a6781fa6532dce9c3618a4b127d920dab764a19064"},
    {file = "snowballstemmer-3.0.1.tar.gz", hash = "sha256:6d5eeeec8e9f84d4d56b847692bacf79bc2c8e90c7f80ca4444ff8b6f2e52895"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["lint"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.4.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["lint"]
markers = "python_version == \"3.10\""
files = [
    {file = "tomli-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:b5ef256a3fd497d4973c11bf142e9ed78b150d36f5773f1ca6088c230ffc5867"},
    {file = "tomli-2.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5572e41282d5268eb09a697c89a7bee84fae66511f87533a6f88bd2f7b652da9"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:551e321c6ba03b55676970b47cb1b73f14a0a4dce6a3e1a9458fd6d921d72e95"},
    {file = "tomli-2.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e3f639a7a8f10069d0e15408c0b96a2a828cfdec6fca05296ebcdcc28ca7c76"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1b168f2731796b045128c45982d3a4874057626da0e2ef1fdd722848b741361d"},
    {file = "tomli-2.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:133e93646ec4300d651839d382d63edff11d8978be23da4cc106f5a18b7d0576"},
    {file = "tomli-2.4.0-cp311-cp311-win32.whl", hash = "sha256:b6c78bdf37764092d369722d9946cb65b8767bfa4110f902a1b2542d8d173c8a"},
    {file = "tomli-2.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:d3d1654e11d724760cdb37a3d7691f0be9db5fbdaef59c9f532aabf87006dbaa"},
    {file = "tomli-2.4.0-cp311-cp311-win_arm64.whl", hash = "sha256:cae9c19ed12d4e8f3ebf46d1a75090e4c0dc16271c5bce1c833ac168f08fb614"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:920b1de295e72887bafa3ad9f7a792f811847d57ea6b1215154030cf131f16b1"},
    {file = "tomli-2.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7d6d9a4aee98fac3eab4952ad1d73aee87359452d1c086b5ceb43ed02ddb16b8"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36b9d05b51e65b254ea6c2585b59d2c4cb91c8a3d91d0ed0f17591a29aaea54a"},
    {file = "tomli-2.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c8a885b370751837c029ef9bc014f27d80840e48bac415f3412e6593bbc18c1"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8768715ffc41f0008abe25d808c20c3d990f42b6e2e58305d5da280ae7d1fa3b"},
    {file = "tomli-2.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b438885858efd5be02a9a133caf5812b8776ee0c969fea02c45e8e3f296ba51"},
    {file = "tomli-2.4.0-cp312-cp312-win32.whl", hash = "sha256:0408e3de5ec77cc7f81960c362543cbbd91ef883e3138e81b729fc3eea5b9729"},
    {file = "tomli-2.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:685306e2cc7da35be4ee914fd34ab801a6acacb061b6a7abca922aaf9ad368da"},
    {file = "tomli-2.4.0-cp312-cp312-win_arm64.whl", hash = "sha256:5aa48d7c2356055feef06a43611fc401a07337d5b006be13a30f6c58f869e3c3"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84d081fbc252d1b6a982e1870660e7330fb8f90f676f6e78b052ad4e64714bf0"},
    {file = "tomli-2.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9a08144fa4cba33db5255f9b74f0b89888622109bd2776148f2597447f92a94e"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c73add4bb52a206fd0c0723432db123c0c75c280cbd67174dd9d2db228ebb1b4"},
    {file = "tomli-2.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fb2945cbe303b1419e2706e711b7113da57b7db31ee378d08712d678a34e51e"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:bbb1b10aa643d973366dc2cb1ad94f99c1726a02343d43cbc011edbfac579e7c"},
    {file = "tomli-2.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4cbcb367d44a1f0c2be408758b43e1ffb5308abe0ea222897d6bfc8e8281ef2f"},
    {file = "tomli-2.4.0-cp313-cp313-win32.whl", hash = "sha256:7d49c66a7d5e56ac959cb6fc583aff0651094ec071ba9ad43df785abc2320d86"},
    {file = "tomli-2.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:3cf226acb51d8f1c394c1b310e0e0e61fecdd7adcb78d01e294ac297dd2e7f87"},
    {file = "tomli-2.4.0-cp313-cp313-win_arm64.whl", hash = "sha256:d20b797a5c1ad80c516e41bc1fb0443ddb5006e9aaa7bda2d71978346aeb9132"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:26ab906a1eb794cd4e103691daa23d95c6919cc2fa9160000ac02370cc9dd3f6"},
    {file = "tomli-2.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:20cedb4ee43278bc4f2fee6cb50daec836959aadaf948db5172e776dd3d993fc"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:39b0b5d1b6dd03684b3fb276407ebed7090bbec989fa55838c98560c01113b66"},
    {file = "tomli-2.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a26d7ff68dfdb9f87a016ecfd1e1c2bacbe3108f4e0f8bcd2228ef9a766c787d"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:20ffd184fb1df76a66e34bd1b36b4a4641bd2b82954befa32fe8163e79f1a702"},
    {file = "tomli-2.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:75c2f8bbddf170e8effc98f5e9084a8751f8174ea6ccf4fca5398436e0320bc8"},
    {file = "tomli-2.4.0-cp314-cp314-win32.whl", hash = "sha256:31d556d079d72db7c584c0627ff3a24c5d3fb4f730221d3444f3efb1b2514776"},
    {file = "tomli-2.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:43e685b9b2341681907759cf3a04e14d7104b3580f808cfde1dfdb60ada85475"},
    {file = "tomli-2.4.0-cp314-cp314-win_arm64.whl", hash = "sha256:3d895d56bd3f82ddd6faaff993c275efc2ff38e52322ea264122d72729dca2b2"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:5b5807f3999fb66776dbce568cc9a828544244a8eb84b84b9bafc080c99597b9"},
    {file = "tomli-2.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c084ad935abe686bd9c898e62a02a19abfc9760b5a79bc29644463eaf2840cb0"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f2e3955efea4d1cfbcb87bc321e00dc08d2bcb737fd1d5e398af111d86db5df"},
    {file = "tomli-2.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e0fe8a0b8312acf3a88077a0802565cb09ee34107813bba1c7cd591fa6cfc8d"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:413540dce94673591859c4c6f794dfeaa845e98bf35d72ed59636f869ef9f86f"},
    {file = "tomli-2.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0dc56fef0e2c1c470aeac5b6ca8cc7b640bb93e92d9803ddaf9ea03e198f5b0b"},
    {file = "tomli-2.4.0-cp314-cp314t-win32.whl", hash = "sha256:d878f2a6707cc9d53a1be1414bbb419e629c3d6e67f69230217bb663e76b5087"},
    {file = "tomli-2.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:2add28aacc7425117ff6364fe9e06a183bb0251b03f986df0e78e974047571fd"},
    {file = "tomli-2.4.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2b1e3b80e1d5e52e40e9b924ec43d81570f0e7d09d11081b797bc4692765a3d4"},
    {file = "tomli-2.4.0-py3-none-any.whl", hash = "sha256:1f776e7d669ebceb01dee46484485f43a4048746235e683bcdffacdf1fb4785a"},
    {file = "tomli-2.4.0.tar.gz", hash = "sha256:aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["lint"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "15e50c73673ea9bbfdd2f6672da6577c7724038a323573f17be2f21788789745"
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/poetry.toml sha256=ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e bytes=34 -->
## FILE: utilities/poetry.toml

- repository: `ni/datastore-python`
- source_path: `utilities/poetry.toml`
- sha256: `ab9805d8c59ec531486a127a4ad51adf2eb61c352b456eedf24185b33661829e`
- bytes: 34

````toml
[virtualenvs]
in-project = true
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/pyproject.toml sha256=2ccd78f3dad8ba2d8cb04be067b507b54ae3aff3291e521fd64428182351db67 bytes=1567 -->
## FILE: utilities/pyproject.toml

- repository: `ni/datastore-python`
- source_path: `utilities/pyproject.toml`
- sha256: `2ccd78f3dad8ba2d8cb04be067b507b54ae3aff3291e521fd64428182351db67`
- bytes: 1567

````toml
[project]
name = "datastore_utilities"
version = "0.1.0.dev0"
license = "MIT"
description = "Development utilities for datastore-python"
maintainers = [
  {name = "Johann Scholtz", email = "johann.scholtz@emerson.com"},
  {name = "Joel Dixon", email = "joel.dixon@emerson.com"}
]
readme = "README.md"
repository = "https://github.com/ni/datastore-python"
classifiers = [
  "Development Status :: 3 - Alpha",
  "Intended Audience :: Developers",
  "Intended Audience :: Manufacturing",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Operating System :: Microsoft :: Windows",
  "Operating System :: POSIX",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: 3.14",
  "Programming Language :: Python :: Implementation :: CPython",
]
dynamic = ["dependencies"]
requires-python = '>=3.10,<4.0'

[[tool.poetry.packages]]
include = "utilities"
from = "src"

[tool.poetry]
requires-poetry = '>=2.1,<3.0'

[tool.poetry.dependencies]
python = "^3.10"

[tool.poetry.group.lint.dependencies]
ni-python-styleguide = ">=0.4.1"
mypy = ">=1.0"

[build-system]
requires = ["poetry-core>=1.8"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 100

[tool.mypy]
mypy_path = "src"
files = "."
namespace_packages = true
strict = true
explicit_package_bases = true
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/README.md sha256=47cc2ef06b455de4268b1824942f980dd34bc58295069044a7f0ecfe0e78b718 bytes=92 -->
## FILE: utilities/README.md

- repository: `ni/datastore-python`
- source_path: `utilities/README.md`
- sha256: `47cc2ef06b455de4268b1824942f980dd34bc58295069044a7f0ecfe0e78b718`
- bytes: 92

````markdown
This project provides shared development utilities for use in the `datastore-python` repo.
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/src/utilities/__init__.py sha256=f49125e3b8b148584305e1397c85993c66060b0fa97a5d1e0699de2eef8926ab bytes=159 -->
## FILE: utilities/src/utilities/__init__.py

- repository: `ni/datastore-python`
- source_path: `utilities/src/utilities/__init__.py`
- sha256: `f49125e3b8b148584305e1397c85993c66060b0fa97a5d1e0699de2eef8926ab`
- bytes: 159

````python
"""Utilities for development in datastore-python."""

from utilities._data_store_context import DataStoreContext

__all__ = [
    "DataStoreContext",
]
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/src/utilities/_data_store_context.py sha256=898358b3ca91e43bce951186843145e1635238f8d59850bd1f3f6245c1a88bc6 bytes=5241 -->
## FILE: utilities/src/utilities/_data_store_context.py

- repository: `ni/datastore-python`
- source_path: `utilities/src/utilities/_data_store_context.py`
- sha256: `898358b3ca91e43bce951186843145e1635238f8d59850bd1f3f6245c1a88bc6`
- bytes: 5241

````python
import hashlib
import os
import sys
from pathlib import Path
from types import TracebackType

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

DISCOVERY_SERVICE_CLUSTER_ID_ENV_VAR = "NIDISCOVERY_CLUSTERID"

# Environment variables controlling files created or used by the Data Store service
DATA_STORE_DATABASE_PATH_ENV_VAR = "NIDATASTORE_DATASTORESETTINGS__SQLITEDATABASEPATH"
DATA_STORE_DATA_FILES_DIRECTORY_PATH_ENV_VAR = "NIDATASTORE_DATASTORESETTINGS__DATAFILESDIRECTORY"
DATA_STORE_INGEST_DIRECTORY_PATH_ENV_VAR = "NIDATASTORE_DATASTORESETTINGS__INGESTDIRECTORY"
DATA_STORE_FAILED_INGEST_DIRECTORY_PATH_ENV_VAR = (
    "NIDATASTORE_DATASTORESETTINGS__FAILEDINGESTDIRECTORY"
)
DATA_STORE_TDMS_EXPIRATION_SECONDS_ENV_NAME = (
    "NIDATASTORE_DATASTORESETTINGS__TDMSFILECACHEEXPIRATIONSECONDS"
)

DEFAULT_FOLDER_NAME = "temp_data"


class DataStoreContext:
    """A context manager for running a data store in an isolated environment."""

    __slots__ = "_base_directory_path", "_original_environment"

    def __init__(self, base_directory_path: Path | None = None) -> None:
        """Initialize the DataStoreContext.

        Args:
            base_directory_path: An optional base directory path specifying where
            the data store files will be located. If not provided, a default path
            in the repository directory will be used.
        """
        self._base_directory_path = base_directory_path
        self._original_environment: dict[str, str | None] = {}

    def __enter__(self) -> Self:
        """Enter the data store context."""
        self.initialize()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the data store context."""
        self.close()

    def initialize(self) -> None:
        """Initializes the data store context by setting up necessary environment variables."""
        self._initialize_environment()

    def close(self) -> None:
        """Cleans up the data store context by resetting environment variables."""
        self._restore_environment()

    def _initialize_environment(self) -> None:
        self._save_original_environment()
        self._initialize_cluster_id()
        self._initialize_data_store_paths()

    def _save_original_environment(self) -> None:
        # Save the original values (or None if not set)
        for environment_variable in [
            DISCOVERY_SERVICE_CLUSTER_ID_ENV_VAR,
            DATA_STORE_DATABASE_PATH_ENV_VAR,
            DATA_STORE_DATA_FILES_DIRECTORY_PATH_ENV_VAR,
            DATA_STORE_INGEST_DIRECTORY_PATH_ENV_VAR,
            DATA_STORE_FAILED_INGEST_DIRECTORY_PATH_ENV_VAR,
            DATA_STORE_TDMS_EXPIRATION_SECONDS_ENV_NAME,
        ]:
            self._original_environment[environment_variable] = os.environ.get(environment_variable)

    def _initialize_cluster_id(self) -> None:
        cluster_id = self._get_cluster_id()
        os.environ[DISCOVERY_SERVICE_CLUSTER_ID_ENV_VAR] = cluster_id

    def _initialize_data_store_paths(self) -> None:
        base_directory_path = self._get_base_directory_path()

        metadata_db_path = base_directory_path / "MetadataStore.db"
        data_files_dir = base_directory_path / "DataFiles"
        ingest_dir = base_directory_path / "Ingest"
        failed_ingest_dir = base_directory_path / "FailedIngest"

        os.environ[DATA_STORE_DATABASE_PATH_ENV_VAR] = str(metadata_db_path)
        os.environ[DATA_STORE_DATA_FILES_DIRECTORY_PATH_ENV_VAR] = str(data_files_dir)
        os.environ[DATA_STORE_INGEST_DIRECTORY_PATH_ENV_VAR] = str(ingest_dir)
        os.environ[DATA_STORE_FAILED_INGEST_DIRECTORY_PATH_ENV_VAR] = str(failed_ingest_dir)

        os.environ[DATA_STORE_TDMS_EXPIRATION_SECONDS_ENV_NAME] = str(0)

    def _get_cluster_id(self) -> str:
        # Generate a unique cluster ID based on the base directory path
        return self._get_base_directory_hash()

    def _get_base_directory_hash(self) -> str:
        base_directory_path = self._get_base_directory_path()
        base_directory_path_bytes = str(base_directory_path.resolve()).encode("utf-8")
        hash_object = hashlib.sha256(base_directory_path_bytes)
        return hash_object.hexdigest()[:32]

    def _get_base_directory_path(self) -> Path:
        if self._base_directory_path is not None:
            return self._base_directory_path

        repo_root = Path(__file__).resolve().parents[3]
        return repo_root / DEFAULT_FOLDER_NAME

    def _restore_environment(self) -> None:
        for environment_variable, original_value in self._original_environment.items():
            if original_value is None:
                # The environment variable was not originally set; remove it
                if environment_variable in os.environ:
                    del os.environ[environment_variable]
            else:
                # Restore the original value
                os.environ[environment_variable] = original_value
````

<!--NI_OSS_SOURCE repo=datastore-python path=utilities/src/utilities/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: utilities/src/utilities/py.typed

- repository: `ni/datastore-python`
- source_path: `utilities/src/utilities/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````
