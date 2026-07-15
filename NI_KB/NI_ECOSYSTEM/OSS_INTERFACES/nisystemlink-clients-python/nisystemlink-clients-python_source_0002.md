# NI OSS SOURCE SNAPSHOT: nisystemlink-clients-python

<!--NI_OSS_SNAPSHOT repo=ni/nisystemlink-clients-python commit=0bed315df7e0dd210396f3669d42211c96a641d5 -->

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plans_response.py sha256=00db9dbb0df821895d38e3b04b698c01ed0be5a1db54481b1447748bface59aa bytes=705 -->
## FILE: nisystemlink/clients/test_plan/models/_update_test_plans_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/test_plan/models/_update_test_plans_response.py`
- sha256: `00db9dbb0df821895d38e3b04b698c01ed0be5a1db54481b1447748bface59aa`
- bytes: 705

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._test_plan import TestPlan
from ._update_test_plan_request import UpdateTestPlanRequest


class UpdateTestPlansResponse(JsonModel):
    """Represents the response after attempting to update test plans."""

    updated_test_plans: List[TestPlan] | None = None
    """List of successfully updated test plans."""

    failed_test_plans: List[UpdateTestPlanRequest] | None = None
    """List of test plans that failed to update."""

    error: ApiError | None = None
    """The error that occurred when updating the test plans."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/__init__.py sha256=857d0c8f384718240a1db3adc7edc8c82b7abf06c51558f446a7780d2db49208 bytes=160 -->
## FILE: nisystemlink/clients/testmonitor/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/__init__.py`
- sha256: `857d0c8f384718240a1db3adc7edc8c82b7abf06c51558f446a7780d2db49208`
- bytes: 160

````python
"""Start here with TestMonitorClient for test monitor operations."""

from ._test_monitor_client import TestMonitorClient

__all__ = ["TestMonitorClient"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/_test_monitor_client.py sha256=1f3befd35713916a848bc5b7d9b8417bc6b972d8aea572fc72039cb044fcb418 bytes=17487 -->
## FILE: nisystemlink/clients/testmonitor/_test_monitor_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/_test_monitor_client.py`
- sha256: `1f3befd35713916a848bc5b7d9b8417bc6b972d8aea572fc72039cb044fcb418`
- bytes: 17487

````python
"""Implementation of TestMonitor Client"""

from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import delete, get, post
from nisystemlink.clients.testmonitor.models import (
    CreateResultRequest,
    UpdateResultRequest,
)
from uplink import Field, Path, Query, retry, returns

from . import models
from ..core.helpers._partial_success import unwrap_single_item_partial_success


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class TestMonitorClient(BaseClient):
    # prevent pytest from thinking this is a test class
    __test__ = False

    def __init__(self, configuration: core.HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the TestMonitor Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()
        super().__init__(configuration, base_path="/nitestmonitor/v2/")

    @get("")
    def api_info(self) -> models.ApiInfo:
        """Get information about the available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the `ni``/nitestmonitor``` service.
        """
        ...

    @post("results", args=[Field("results")])
    def create_results(
        self, results: List[CreateResultRequest]
    ) -> models.CreateResultsPartialSuccess:
        """Creates one or more results and returns errors for failed creations.

        Args:
            results: A list of results to attempt to create.

        Returns: A list of created results, results that failed to create, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` service of provided invalid
                arguments.
        """
        ...

    def create_result(self, result: CreateResultRequest) -> models.Result:
        """Creates a single result.

        Args:
            result: The result to create.

        Returns:
            The created result.

        Raises:
            ApiException: if the result could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_results([result])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.results,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to create result.",
            empty_message="Server returned no created results.",
        )

    @get(
        "results",
        args=[Query("continuationToken"), Query("take"), Query("returnCount")],
    )
    def get_results(
        self,
        continuation_token: str | None = None,
        take: int | None = None,
        return_count: bool | None = None,
    ) -> models.PagedResults:
        """Reads a list of results.

        Args:
            continuation_token: The token used to paginate results.
            take: The number of results to get in this request.
            return_count: Whether or not to return the total number of results available.

        Returns:
            A list of results.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @get("results/{id}")
    def get_result(self, id: str) -> models.Result:
        """Retrieves a single result by id.

        Args:
            id (str): Unique ID of a result.

        Returns:
            The single result matching `id`

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @post("query-results")
    def query_results(self, query: models.QueryResultsRequest) -> models.PagedResults:
        """Queries for results that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of results.

        Returns:
            A paged list of results with a continuation token to get the next page.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided invalid
                arguments.
        """
        ...

    @returns.json  # type: ignore
    @post("query-result-values")
    def query_result_values(self, query: models.QueryResultValuesRequest) -> List[str]:
        """Queries for results that match the query and returns a list of the requested field.

        Args:
            query : The query for the fields.

        Returns:
            A list of the values of the queried field.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided
                invalid arguments.
        """
        ...

    @post("update-results", args=[Field("results"), Field("replace")])
    def update_results(
        self, results: List[UpdateResultRequest], replace: bool = False
    ) -> models.UpdateResultsPartialSuccess:
        """Updates a list of results with optional field replacement.

        Args:
            `results`: A list of results to update. Results are matched for update by id.
            `replace`: Replace the existing fields instead of merging them. Defaults to `False`.
                If this is `True`, then `keywords` and `properties` for the result will be
                    replaced by what is in the `results` provided in this request.
                If this is `False`, then the `keywords` and `properties` in this request will
                    merge with what is already present in the server resource.

        Returns: A list of updates results, results that failed to update, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    def update_result(
        self, result: UpdateResultRequest, replace: bool = False
    ) -> models.Result:
        """Updates a single result.

        Args:
            result: The result to update.
            replace: Replace the existing fields instead of merging them.

        Returns:
            The updated result.

        Raises:
            ApiException: if the result could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_results([result], replace=replace)

        return unwrap_single_item_partial_success(
            response=response,
            items=response.results,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to update result.",
            empty_message="Server returned no updated results.",
        )

    @delete("results/{id}")
    def delete_result(self, id: str) -> None:
        """Deletes a single result by id.

        Args:
            id (str): Unique ID of a result.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @post("delete-results", args=[Field("ids")])
    def delete_results(
        self, ids: List[str]
    ) -> models.DeleteResultsPartialSuccess | None:
        """Deletes multiple results.

        Args:
            ids (List[str]): List of unique IDs of results.

        Returns:
            A partial success if any results failed to delete, or None if all
            results were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        """
        ...

    @post(
        "steps",
        args=[Field("steps"), Field("updateResultTotalTime")],
    )
    def create_steps(
        self,
        steps: List[models.CreateStepRequest],
        update_result_total_time: bool = False,
    ) -> models.CreateStepsPartialSuccess:
        """Creates one or more steps.

        Args:
            steps: A list of steps to create.
            update_result_total_time: Determine test result total time from the step total times.
                Defaults to False.

        Returns:
            A list of steps that were successfully created and ones that failed to be created.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...

    def create_step(
        self,
        step: models.CreateStepRequest,
        update_result_total_time: bool = False,
    ) -> models.Step:
        """Creates a single step.

        Args:
            step: The step to create.
            update_result_total_time: Determine test result total time from the step total times.

        Returns:
            The created step.

        Raises:
            ApiException: if the step could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_steps(
            [step],
            update_result_total_time=update_result_total_time,
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.steps,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to create step.",
            empty_message="Server returned no created steps.",
        )

    @post("delete-steps", args=[Field("steps")])
    def delete_steps(
        self, steps: List[models.StepIdResultIdPair]
    ) -> models.DeleteStepsPartialSuccess | None:
        """Deletes one or more steps by global ID.

        Args:
            steps: A list of step IDs and result IDs. Note that these are the global IDs and not the
            `step_id` that is local to a product and workspace.

        Returns:
            None if all deletes succeed otherwise a list of which IDs failed and which succeeded.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there
            invalid arguments.
        """
        ...

    @delete(
        "results/{resultId}/steps/{stepId}",
        args=[Path("resultId"), Path("stepId"), Query("updateResultTotalTime")],
    )
    def delete_step(
        self,
        result_id: str,
        step_id: str,
        update_result_total_time: bool | None = False,
    ) -> None:
        """Deletes a single step.

        Args:
            result_id: The resultId of the step to delete.
            step_id: The stepId of the step to delete.
            update_result_total_time: Determine test result total time from the step total times.
                Defaults to False.

        Returns:
            None

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...

    @post("query-steps")
    def query_steps(self, query: models.QueryStepsRequest) -> models.PagedSteps:
        """Queries for steps that match the filters.

        Args:
            query: The query contains a product ID as well as a filter for steps under that product.

        Returns:
            A list of steps that match the filter.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...

    @post(
        "update-steps",
        args=[
            Field("steps"),
            Field("updateResultTotalTime"),
            Field("replaceKeywords"),
            Field("replaceProperties"),
        ],
    )
    def update_steps(
        self,
        steps: List[models.UpdateStepRequest],
        update_result_total_time: bool = False,
        replace_keywords: bool = False,
        replace_properties: bool = False,
    ) -> models.UpdateStepsPartialSuccess:
        """Updates one or more steps.

        Update requires that the version field matches the version being updated from.

        Args:
            steps: a list of steps that are to be updated. Must include the global ID and
            each step being updated must match the version currently on the server.
            update_result_total_time: Determine test result total time from the step total times.
                Defaults to False.
            replace_keywords: Replace with existing keywords instead of merging them.
                Defaults to False.
            replace_properties: Replace with existing properties instead of merging them.
                Defaults to False.

        Returns
            A list of steps that were successfully updated and a list of ones that were not along
            with error messages for updates that failed.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...

    def update_step(
        self,
        step: models.UpdateStepRequest,
        update_result_total_time: bool = False,
        replace_keywords: bool = False,
        replace_properties: bool = False,
    ) -> models.Step:
        """Updates a single step.

        Args:
            step: The step to update.
            update_result_total_time: Determine test result total time from the step total times.
            replace_keywords: Replace existing keywords instead of merging them.
            replace_properties: Replace existing properties instead of merging them.

        Returns:
            The updated step.

        Raises:
            ApiException: if the step could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_steps(
            [step],
            update_result_total_time=update_result_total_time,
            replace_keywords=replace_keywords,
            replace_properties=replace_properties,
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.steps,
            failed=response.failed,
            error=response.error,
            failure_message="Failed to update step.",
            empty_message="Server returned no updated steps.",
        )

    @get(
        "steps",
        args=[Query("continuationToken"), Query("take"), Query("returnCount")],
    )
    def get_steps(
        self,
        continuation_token: str | None = None,
        take: int | None = None,
        return_count: bool | None = None,
    ) -> models.PagedSteps:
        """Reads a list of steps.

        Args:
            continuation_token: The token used to paginate steps.
            take: The number of steps to get in this request.
            return_count: Whether or not to return the total number of steps available.

        Returns:
            A list of steps.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments..
        """
        ...

    @get("results/{resultId}/steps/{stepId}", args=[Path("resultId"), Path("stepId")])
    def get_step(self, result_id: str, step_id: str) -> models.Step:
        """Gets a single step.

        Args:
            result_id: The resultId of the step to get.
            step_id: The stepId of the step to get.

        Returns:
            The step.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...

    @returns.json  # type: ignore
    @post("query-step-values")
    def query_step_values(self, query: models.QueryStepValuesRequest) -> List[str]:
        """Queries values for a step field.

        Args:
            query: The query parameters.

        Returns:
            A list of values for the specified step field.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/__init__.py sha256=44b2b55581c6174813c85ec1befbf38b4730ea45689582dfbf68d6d6d6d4c647 bytes=1297 -->
## FILE: nisystemlink/clients/testmonitor/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/__init__.py`
- sha256: `44b2b55581c6174813c85ec1befbf38b4730ea45689582dfbf68d6d6d6d4c647`
- bytes: 1297

````python
from ._api_info import Operation, V2Operations, ApiInfo
from ._named_value import NamedValue
from ._result import Result
from ._status import StatusType, Status
from ._step import Step
from ._step_data import Measurement, StepData
from ._paged_results import PagedResults
from ._paged_steps import PagedSteps
from ._delete_results_partial_success import DeleteResultsPartialSuccess
from ._delete_steps_partial_success import DeleteStepsPartialSuccess, StepIdResultIdPair
from ._create_results_partial_success import CreateResultsPartialSuccess
from ._create_steps_partial_success import CreateStepsPartialSuccess
from ._update_results_partial_success import UpdateResultsPartialSuccess
from ._update_steps_partial_success import UpdateStepsPartialSuccess
from ._create_result_request import CreateResultRequest
from ._create_steps_request import CreateStepRequest
from ._update_result_request import UpdateResultRequest
from ._update_steps_request import UpdateStepRequest
from ._query_results_request import (
    QueryResultsRequest,
    QueryResultValuesRequest,
    ResultField,
    ResultProjection,
)
from ._query_steps_request import (
    QueryStepsRequest,
    QueryStepValuesRequest,
    StepOrderBy,
    StepField,
    StepProjection,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_api_info.py sha256=90f890d8951d811ffd55fe757728ebec7a241319019e5b223d153d5c113dfa9f bytes=2070 -->
## FILE: nisystemlink/clients/testmonitor/models/_api_info.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_api_info.py`
- sha256: `90f890d8951d811ffd55fe757728ebec7a241319019e5b223d153d5c113dfa9f`
- bytes: 2070

````python
from nisystemlink.clients.core._api_info import Operation
from nisystemlink.clients.core._uplink._json_model import JsonModel


class V2Operations(JsonModel):
    """The operations available in the routes provided by the v2 HTTP API."""

    get_products: Operation
    """The ability to get a list of products."""

    query_products: Operation
    """The ability to query products based on their properties."""

    create_products: Operation
    """The ability to create one or more products."""

    update_products: Operation
    """The ability to update the properties of one or more products."""

    delete_products: Operation
    """The ability to delete a single products."""

    delete_many_products: Operation
    """The ability to delete a list of products."""

    get_results: Operation
    """The ability to get a list of results."""

    get_results_property_keys: Operation
    """The ability to get custom property keys."""

    query_results: Operation
    """"The ability to to query results based on their properties."""

    create_results: Operation
    """The ability to create results."""

    update_results: Operation
    """The ability to update results."""

    delete_result: Operation
    """The ability to delete a single results."""

    delete_many_results: Operation
    """The ability to delete multiple results."""

    get_steps: Operation
    """The ability to get a list of steps."""

    query_steps: Operation
    """The ability to query steps based on their properties."""

    create_steps: Operation
    """The ability to create steps."""

    update_steps: Operation
    """The ability to update steps."""

    delete_step: Operation
    """The ability to delete a single step."""

    delete_many_steps: Operation
    """The ability to delete multiple steps."""

    query_paths: Operation
    """The ability to query step paths."""


class ApiInfo(JsonModel):
    """Information about the available API operations."""

    operations: V2Operations
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_result_request.py sha256=2b5bc8625a9a0d5cf8afeeab6835e89602e8aff72bbacdaf6b42d41f1a8753ac bytes=1683 -->
## FILE: nisystemlink/clients/testmonitor/models/_create_result_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_create_result_request.py`
- sha256: `2b5bc8625a9a0d5cf8afeeab6835e89602e8aff72bbacdaf6b42d41f1a8753ac`
- bytes: 1683

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._status import Status


class CreateResultRequest(JsonModel):
    """Contains information about a result."""

    status: Status
    """The status of the result."""

    started_at: datetime | None = None
    """The time that the result started."""

    program_name: str
    """The name of the program that generated this result."""

    system_id: str | None = None
    """The id of the system that generated this result."""

    host_name: str | None = None
    """The name of the host that generated this result."""

    part_number: str | None = None
    """The part number is the unique identifier of a product within a single org."""

    serial_number: str | None = None
    """The serial number of the system that generated this result."""

    total_time_in_seconds: float | None = None
    """The total time that the result took to run in seconds."""

    keywords: List[str] | None = None
    """A list of keywords that categorize this result."""

    properties: Dict[str, str | None] | None = None
    """A list of custom properties for this result."""

    operator: str | None = None
    """The operator that ran the result."""

    file_ids: List[str] | None = None
    """A list of file ids that are attached to this result."""

    data_table_ids: List[str] | None = None
    """A list of data table ids that are attached to this result."""

    workspace: str | None = None
    """The id of the workspace that this product belongs to."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_results_partial_success.py sha256=474242cb077fa6e39a79c49151932f27b6ccc479ad1343dd7e19e1848d28e811 bytes=815 -->
## FILE: nisystemlink/clients/testmonitor/models/_create_results_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_create_results_partial_success.py`
- sha256: `474242cb077fa6e39a79c49151932f27b6ccc479ad1343dd7e19e1848d28e811`
- bytes: 815

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._create_result_request import (
    CreateResultRequest,
)
from nisystemlink.clients.testmonitor.models._result import Result


class CreateResultsPartialSuccess(JsonModel):
    results: List[Result]
    """The list of results that were successfully created."""

    failed: List[CreateResultRequest] | None = None
    """The list of results that were not created.
    If this is `None`, then all results were successfully created.
    """

    error: ApiError | None = None
    """Error messages for results that were not created.
    If this is `None`, then all results were successfully created.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_steps_partial_success.py sha256=b7a9a856afc9085151ab1fc3de3b94a8094300a461c4453b9cbfbdeafe83c27e bytes=792 -->
## FILE: nisystemlink/clients/testmonitor/models/_create_steps_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_create_steps_partial_success.py`
- sha256: `b7a9a856afc9085151ab1fc3de3b94a8094300a461c4453b9cbfbdeafe83c27e`
- bytes: 792

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._create_steps_request import (
    CreateStepRequest,
)
from nisystemlink.clients.testmonitor.models._step import Step


class CreateStepsPartialSuccess(JsonModel):
    steps: List[Step]
    """The list of steps that were successfully created."""

    failed: List[CreateStepRequest] | None = None
    """The list of step requests that failed.

    If this is `None`, then all steps were successfully created.
    """

    error: ApiError | None = None
    """Error messages for steps that were not created.

    If this is `None`, then all steps were successfully created.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_steps_request.py sha256=eb27c3386888b38d3d0c7dbbca3846b0422a4d26588d5052a57bb22083a4657f bytes=1605 -->
## FILE: nisystemlink/clients/testmonitor/models/_create_steps_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_create_steps_request.py`
- sha256: `eb27c3386888b38d3d0c7dbbca3846b0422a4d26588d5052a57bb22083a4657f`
- bytes: 1605

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._named_value import NamedValue
from nisystemlink.clients.testmonitor.models._step import Status
from nisystemlink.clients.testmonitor.models._step_data import StepData


class BaseStepRequest(JsonModel):
    step_id: str | None
    """Step ID."""

    result_id: str
    """Result ID."""

    parent_id: str | None = None
    """Parent step ID."""

    data: StepData | None = None
    """Data returned by the test step."""

    data_model: str | None = None
    """Data model for the step."""

    started_at: datetime | None = None
    """ISO-8601 formatted timestamp indicating when the test result began."""

    status: Status | None = None
    """The status of the step."""

    step_type: str | None = None
    """Step type."""

    total_time_in_seconds: float | None = None
    """Total number of seconds the step took to execute."""

    inputs: List[NamedValue] | None = None
    """Inputs and their values passed to the test."""

    outputs: List[NamedValue] | None = None
    """Outputs and their values logged by the test."""

    keywords: List[str] | None = None
    """Words or phrases associated with the step."""

    properties: Dict[str, str] | None = None
    """Test step properties."""


class CreateStepRequest(BaseStepRequest):
    name: str
    """Step name."""

    children: List["CreateStepRequest"] | None = None
    """Nested child steps."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_delete_results_partial_success.py sha256=1567744f6de1aad6633623eba07b19b635c7ba7536c4b071176bcb0cbf4ed4c4 bytes=580 -->
## FILE: nisystemlink/clients/testmonitor/models/_delete_results_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_delete_results_partial_success.py`
- sha256: `1567744f6de1aad6633623eba07b19b635c7ba7536c4b071176bcb0cbf4ed4c4`
- bytes: 580

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteResultsPartialSuccess(JsonModel):
    """The result of deleting multiple results when one or more results could not be deleted."""

    ids: List[str]
    """The IDs of the results that were successfully deleted."""

    failed: List[str] | None = None
    """The IDs of the results that could not be deleted."""

    error: ApiError | None = None
    """The error that occurred when deleting the results."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_delete_steps_partial_success.py sha256=9ed8af05a99caba29b578288383a48b39b7f867940f635f1e8a90f323232ef4a bytes=819 -->
## FILE: nisystemlink/clients/testmonitor/models/_delete_steps_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_delete_steps_partial_success.py`
- sha256: `9ed8af05a99caba29b578288383a48b39b7f867940f635f1e8a90f323232ef4a`
- bytes: 819

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class StepIdResultIdPair(JsonModel):
    step_id: str
    """The ID of the step."""

    result_id: str
    """The ID of the result associated with the step."""


class DeleteStepsPartialSuccess(JsonModel):
    """The result of deleting multiple steps when one or more steps could not be deleted."""

    steps: List[StepIdResultIdPair]
    """The step_id and result_id pairs of the steps that were successfully deleted."""

    failed: List[StepIdResultIdPair] | None = None
    """The step_id and result_id pairs of the steps that could not be deleted."""

    error: ApiError | None = None
    """The error that occurred when deleting the steps."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_named_value.py sha256=f6b12e937ec5ba012e49516dc94669b62652a59cb9248aa18e4fa3168339ee9f bytes=225 -->
## FILE: nisystemlink/clients/testmonitor/models/_named_value.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_named_value.py`
- sha256: `f6b12e937ec5ba012e49516dc94669b62652a59cb9248aa18e4fa3168339ee9f`
- bytes: 225

````python
from typing import Any

from nisystemlink.clients.core._uplink._json_model import JsonModel


class NamedValue(JsonModel):
    name: str
    """The name of the value."""

    value: Any = None
    """The value."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_paged_results.py sha256=06559752c2bbd59ec3d00fe9001b65b10f6020a7e79b23b4f53ee8ca113ff5ff bytes=446 -->
## FILE: nisystemlink/clients/testmonitor/models/_paged_results.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_paged_results.py`
- sha256: `06559752c2bbd59ec3d00fe9001b65b10f6020a7e79b23b4f53ee8ca113ff5ff`
- bytes: 446

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging
from nisystemlink.clients.testmonitor.models import Result


class PagedResults(WithPaging):
    """The response for a Results query containing matched results."""

    results: List[Result]
    """A list of all the results in this page."""

    total_count: int | None = None
    """The total number of results that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_paged_steps.py sha256=d99fbf222f92386040ee363586b4e6131561946b53c9098c1536b7740ec4de5f bytes=436 -->
## FILE: nisystemlink/clients/testmonitor/models/_paged_steps.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_paged_steps.py`
- sha256: `d99fbf222f92386040ee363586b4e6131561946b53c9098c1536b7740ec4de5f`
- bytes: 436

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging
from nisystemlink.clients.testmonitor.models._step import Step


class PagedSteps(WithPaging):
    """The response for a Steps query containing matched steps."""

    steps: List[Step]
    """A list of all the steps in this page."""

    total_count: int | None = None
    """The total number of steps that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_query_results_request.py sha256=3495cf3df30888a015d12e7c3811c44ef3a33bad19eb71b59ada0c5d276c6670 bytes=8724 -->
## FILE: nisystemlink/clients/testmonitor/models/_query_results_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_query_results_request.py`
- sha256: `3495cf3df30888a015d12e7c3811c44ef3a33bad19eb71b59ada0c5d276c6670`
- bytes: 8724

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.core._uplink._with_paging import WithPaging
from pydantic import AliasChoices, Field


class ResultField(str, Enum):
    """The allowed field for which the values can be queried for."""

    ID = "ID"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    PROGRAM_NAME = "PROGRAM_NAME"
    SYSTEM_ID = "SYSTEM_ID"
    HOST_NAME = "HOST_NAME"
    OPERATOR = "OPERATOR"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    PART_NUMBER = "PART_NUMBER"
    PRODUCT = "PRODUCT"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"


class ResultOrderByField(str, Enum):
    """The fields by which results can be ordered."""

    ID = "ID"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    PROGRAM_NAME = "PROGRAM_NAME"
    SYSTEM_ID = "SYSTEM_ID"
    HOST_NAME = "HOST_NAME"
    OPERATOR = "OPERATOR"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    PART_NUMBER = "PART_NUMBER"
    PRODUCT = "PRODUCT"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"
    PROPERTIES = "PROPERTIES"


class ComparisonType(str, Enum):
    """The valid ways to order a result query."""

    DEFAULT = "DEFAULT"
    NUMERIC = "NUMERIC"
    LEXICOGRAPHIC = "LEXICOGRAPHIC"


class ResultProjection(str, Enum):
    """The allowed projections for query.

    When using projection, only the fields specified by the projection element will be included in
    the response.
    """

    ID = "ID"
    STATUS = "STATUS"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    PROGRAM_NAME = "PROGRAM_NAME"
    SYSTEM_ID = "SYSTEM_ID"
    HOST_NAME = "HOST_NAME"
    OPERATOR = "OPERATOR"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    PART_NUMBER = "PART_NUMBER"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"
    KEYWORDS = "KEYWORDS"
    PROPERTIES = "PROPERTIES"
    FILE_IDS = "FILE_IDS"
    DATA_TABLE_IDS = "DATA_TABLE_IDS"
    STATUS_TYPE_SUMMARY = "STATUS_TYPE_SUMMARY"
    WORKSPACE = "WORKSPACE"


class QueryResultsBase(JsonModel):
    """Base class for result query requests."""

    filter: str | None = None
    """
    The result query filter in Dynamic Linq format.
    Allowed properties in the filter are:
    - `id`: String for the global identifier of the result
    - `status.statusType`: String enumeration representing the status of the result.
        Possible values are : LOOPING, SKIPPED, CUSTOM, DONE, PASSED, FAILED,
        RUNNING, WAITING, TERMINATED, ERRORED, TIMED_OUT
    - `systemId`: String for the system identifier of the result
    - `hostName`: String for the host name of the result
    - `operator`: String for the operator of the result
    - `serialNumber`: String for the serial number of the result
    - `totalTimeInSeconds`: Float for the total time in seconds of the result
    - `partNumber`: String representing the part number of the result
    - `programName`: String of the program name
    - `startedAt`: ISO-8601 formatted UTC timestamp indicating when the result was started.
    - `updatedAt`: ISO-8601 formatted UTC timestamp indicating when the result was last updated.
    - `keywords`: A list of keyword strings
    - `properties`: A dictionary of additional string to string properties
    - `fileIds`: A list of string ids for files stored in the file service (`/nifile`)
    - `dataTableIds`: A list of string ids for data tables stored in the
      data frame service (`/nidataframe`)
    - `workspaceId`: String for the workspace identifier of the result

    See the Dynamic Linq query language documentation:
    https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language
    documentation for more details.
    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable.
    """

    substitutions: List[str] | None = None
    """String substitutions into the `filter`.
    Makes substitutions in the query filter expression. Substitutions for the query expression are
    indicated by non-negative integers that are prefixed with the "at" symbol. Each substitution in
    the given expression will be replaced by the element at the corresponding index (zero-based) in
    this list. For example, "@0" in the filter expression will be replaced with the element at the
    zeroth index of the substitutions list.
    """


class QueryProductsBase(JsonModel):
    """Base class for product query requests."""

    product_filter: str | None = None
    """
    The product query filter in Dynamic Linq format.
    Allowed properties in the filter are:
    - `id`: String for the global identifier of the product
    - `partNumber`: String representing the part number of the product
    - `name`: String of the product name
    - `family`: String for the product family
    - `updatedAt`: ISO-8601 formatted UTC timestamp indicating when the product was last updated.
    - `keywords`: A list of keyword strings
    - `properties`: A dictionary of additional string to string properties
    - `fileIds`: A list of string ids for files stored in the file service (`/nifile`)

    See the Dynamic Linq query language documentation:
    https://github.com/ni/systemlink-OpenAPI-documents/wiki/Dynamic-Linq-Query-Language
    documentation for more details.
    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable.
    """

    product_substitutions: List[str] | None = None
    """String substitutions into the `filter`.
    Makes substitutions in the query filter expression. Substitutions for the query expression are
    indicated by non-negative integers that are prefixed with the "at" symbol. Each substitution in
    the given expression will be replaced by the element at the corresponding index (zero-based) in
    this list. For example, "@0" in the filter expression will be replaced with the element at the
    zeroth index of the substitutions list.
    """


class QueryResultsRequest(QueryResultsBase, QueryProductsBase, WithPaging):
    """Request model for querying results."""

    order_by: ResultOrderByField | None = Field(
        None,
        validation_alias=AliasChoices("order_by", "orderBy"),
        serialization_alias="orderBy",
    )
    """Specifies the fields to use to sort the results.
    By default, results are sorted by `id`
    """
    order_by_key: str | None = Field(
        None,
        validation_alias=AliasChoices("order_by_key", "orderByKey"),
        serialization_alias="orderByKey",
    )
    """Specifies the property to use to sort the results when ordering by PROPERTIES.
    Results that do not contain the orderByKey will be considered the smallest value.
    """
    order_by_comparison_type: ComparisonType | None = Field(
        None,
        validation_alias=AliasChoices(
            "order_by_comparison_type",
            "orderByComparisonType",
        ),
        serialization_alias="orderByComparisonType",
    )
    """An enumeration of comparison types that can be used for ordered queries.

    For non-DEFAULT comparisons, values that cannot be converted
    will be considered the smallest value.
    """
    descending: bool | None = None
    """Specifies whether to return the results in descending order.
    By default, this value is `false` and results are sorted in ascending order.
    """
    projection: List[ResultProjection] | None = None
    """Specifies the fields to include in the returned results.
    Fields you do not specify are excluded. Returns all fields if no value is specified.
    """
    take: int | None = None
    """Maximum number of results to return in the current API response.
    Uses the default if the specified value is negative. The default value is `1000` results.
    """
    return_count: bool | None = None
    """If true, the response will include a count of all results matching the filter.
    By default, this value is `False` and count is not returned. Note that returning the count may
    incur performance penalties as the service may have to do a complete walk of the database to
    compute count. """


class QueryResultValuesRequest(QueryResultsBase):
    """Request model for querying result values."""

    field: ResultField | None = None
    """The result field to return for this query."""

    starts_with: str | None = None
    """Only return string parameters prefixed by this value (case sensitive)."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_query_steps_request.py sha256=0c45f9e8f689945e3b70f7d99419c97c1add2259d1b4a976b1df0e611499b262 bytes=4004 -->
## FILE: nisystemlink/clients/testmonitor/models/_query_steps_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_query_steps_request.py`
- sha256: `0c45f9e8f689945e3b70f7d99419c97c1add2259d1b4a976b1df0e611499b262`
- bytes: 4004

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.core._uplink._with_paging import WithPaging


class StepOrderBy(str, Enum):
    """The valid ways to order steps query response.

    This contains only limited fields available in a Step.
    """

    NAME = "NAME"
    STEP_TYPE = "STEP_TYPE"
    STEP_ID = "STEP_ID"
    PARENT_ID = "PARENT_ID"
    RESULT_ID = "RESULT_ID"
    PATH = "PATH"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    DATA_MODEL = "DATA_MODEL"


class StepField(str, Enum):
    """The valid field values that can be queried.

    This contains only limited fields available in a Step.
    """

    NAME = "NAME"
    STEP_TYPE = "STEP_TYPE"
    STEP_ID = "STEP_ID"
    PARENT_ID = "PARENT_ID"
    RESULT_ID = "RESULT_ID"
    PATH = "PATH"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    DATA_MODEL = "DATA_MODEL"


class StepProjection(str, Enum):
    """An enumeration of all fields in a Step.

    This enumeration is used to specify the fields to project in a step query.
    """

    NAME = "NAME"
    STEP_TYPE = "STEP_TYPE"
    STEP_ID = "STEP_ID"
    PARENT_ID = "PARENT_ID"
    RESULT_ID = "RESULT_ID"
    PATH = "PATH"
    PATH_IDS = "PATH_IDS"
    STATUS = "STATUS"
    TOTAL_TIME_IN_SECONDS = "TOTAL_TIME_IN_SECONDS"
    STARTED_AT = "STARTED_AT"
    UPDATED_AT = "UPDATED_AT"
    INPUTS = "INPUTS"
    OUTPUTS = "OUTPUTS"
    DATA_MODEL = "DATA_MODEL"
    DATA = "DATA"
    HAS_CHILDREN = "HAS_CHILDREN"
    WORKSPACE = "WORKSPACE"
    KEYWORDS = "KEYWORDS"
    PROPERTIES = "PROPERTIES"


class QueryStepsBase(JsonModel):
    filter: str | None = None
    """The step query filter in Dynamic Linq format."""

    substitutions: List[str] | None = None
    """String substitutions into the `filter`.

    Makes substitutions in the query filter expression. Substitutions for the query expression are
    indicated by non-negative integers that are prefixed with the "at" symbol. Each substitution in
    the given expression will be replaced by the element at the corresponding index (zero-based) in
    this list. For example, "@0" in the filter expression will be replaced with the element at the
    zeroth index of the substitutions list.
    """


class QueryStepsRequest(QueryStepsBase, WithPaging):
    order_by: StepOrderBy | None = None
    """Specifies the fields to use to sort the steps."""

    descending: bool | None = None
    """Specifies whether to return the steps in descending order."""

    take: int | None = None
    """Maximum number of steps to return in the current API response."""

    return_count: bool | None = None
    """If true, the response will include a count of all steps matching the filter.

    By default, this value is `False` and count is not returned. Note that returning the count may
    incur performance penalties as the service may have to do a complete walk of the database to
    compute count.
    """

    result_filter: str | None = None
    """The result query filter in Dynamic Linq format."""

    result_substitutions: List[str] | None = None
    """String substitutions into the `result_filter`."""

    projection: List[StepProjection] | None = None
    """Specifies the step fields to project. When a field value is given here,
    the corresponding field will be present in all returned steps, and all
    unspecified fields will be excluded. If no projection is specified,
    all step fields will be returned.
    """


class QueryStepValuesRequest(QueryStepsBase):
    field: StepField
    """The step field to return for this query."""

    starts_with: str | None = None
    """Only return string parameters prefixed by this value (case sensitive)."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_result.py sha256=23442b5082d75e89dbd6267822c74446f961868b8610eb80b8dbd58f8ae5378e bytes=2106 -->
## FILE: nisystemlink/clients/testmonitor/models/_result.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_result.py`
- sha256: `23442b5082d75e89dbd6267822c74446f961868b8610eb80b8dbd58f8ae5378e`
- bytes: 2106

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._status import Status, StatusType
from pydantic import ConfigDict


class Result(JsonModel):
    """Contains information about a result."""

    status: Status | None = None
    """The status of the result."""

    started_at: datetime | None = None
    """The time that the result started."""

    updated_at: datetime | None = None
    """The last time that this result was updated."""

    program_name: str | None = None
    """The name of the program that generated this result."""

    id: str | None = None
    """The globally unique id of the result."""

    system_id: str | None = None
    """The id of the system that generated this result."""

    host_name: str | None = None
    """The name of the host that generated this result."""

    part_number: str | None = None
    """The part number is the unique identifier of a product within a single org."""

    serial_number: str | None = None
    """The serial number of the system that generated this result."""

    total_time_in_seconds: float | None = None
    """The total time that the result took to run in seconds."""

    keywords: List[str | None] | None = None
    """A list of keywords that categorize this result."""

    properties: Dict[str, str | None] | None = None
    """A list of custom properties for this result."""

    operator: str | None = None
    """The operator that ran the result."""

    file_ids: List[str | None] | None = None
    """A list of file ids that are attached to this result."""

    data_table_ids: List[str | None] | None = None
    """A list of data table ids that are attached to this result."""

    status_type_summary: Dict[StatusType, int] | None = None
    """A summary of the status types in the result."""

    workspace: str | None = None
    """The id of the workspace that this product belongs to."""
    model_config = ConfigDict(extra="ignore")
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_status.py sha256=590194367a6c8ad35937e0d7322059d16b5f030e458a342bca408a0dcf973b39 bytes=1760 -->
## FILE: nisystemlink/clients/testmonitor/models/_status.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_status.py`
- sha256: `590194367a6c8ad35937e0d7322059d16b5f030e458a342bca408a0dcf973b39`
- bytes: 1760

````python
from enum import Enum

from nisystemlink.clients.core._uplink._json_model import JsonModel


class StatusType(str, Enum):
    """The types of statuses that a result can have."""

    LOOPING = "LOOPING"
    SKIPPED = "SKIPPED"
    CUSTOM = "CUSTOM"
    DONE = "DONE"
    PASSED = "PASSED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    WAITING = "WAITING"
    TERMINATED = "TERMINATED"
    ERRORED = "ERRORED"
    TIMED_OUT = "TIMED_OUT"


class Status(JsonModel):
    """Contains information about a status object."""

    status_type: StatusType
    """The type of status."""

    status_name: str | None = None
    """The name of the status."""

    @staticmethod
    def LOOPING() -> "Status":
        return Status(status_type=StatusType.LOOPING)

    @staticmethod
    def SKIPPED() -> "Status":
        return Status(status_type=StatusType.SKIPPED)

    @staticmethod
    def DONE() -> "Status":
        return Status(status_type=StatusType.DONE)

    @staticmethod
    def PASSED() -> "Status":
        return Status(status_type=StatusType.PASSED)

    @staticmethod
    def FAILED() -> "Status":
        return Status(status_type=StatusType.FAILED)

    @staticmethod
    def RUNNING() -> "Status":
        return Status(status_type=StatusType.RUNNING)

    @staticmethod
    def WAITING() -> "Status":
        return Status(status_type=StatusType.WAITING)

    @staticmethod
    def TERMINATED() -> "Status":
        return Status(status_type=StatusType.TERMINATED)

    @staticmethod
    def ERRORED() -> "Status":
        return Status(status_type=StatusType.ERRORED)

    @staticmethod
    def TIMED_OUT() -> "Status":
        return Status(status_type=StatusType.TIMED_OUT)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_step.py sha256=98ab5d30a23e577220a01b6cf955c28edff6359c71fa5dc7cebdc7bd417dccf7 bytes=2068 -->
## FILE: nisystemlink/clients/testmonitor/models/_step.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_step.py`
- sha256: `98ab5d30a23e577220a01b6cf955c28edff6359c71fa5dc7cebdc7bd417dccf7`
- bytes: 2068

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._named_value import NamedValue
from nisystemlink.clients.testmonitor.models._status import Status
from nisystemlink.clients.testmonitor.models._step_data import StepData


class Step(JsonModel):
    name: str | None = None
    """The name of the step."""

    step_type: str | None = None
    """The type of the step."""

    step_id: str | None = None
    """The ID of the step."""

    parent_id: str | None = None
    """The ID of the parent step."""

    result_id: str | None = None
    """The ID of the result associated with the step."""

    path: str | None = None
    """The path of the step."""

    path_ids: List[str] | None = None
    """The IDs of the steps in the path."""

    status: Status | None = None
    """The status of the step."""

    total_time_in_seconds: float | None = None
    """The total time in seconds the step took to execute."""

    started_at: datetime | None = None
    """The ISO-8601 formatted timestamp indicating when the step started."""

    updated_at: datetime | None = None
    """The ISO-8601 formatted timestamp indicating when the step was last updated."""

    inputs: List[NamedValue] | None = None
    """Inputs and their values passed to the test."""

    outputs: List[NamedValue] | None = None
    """Outputs and their values logged by the test."""

    data_model: str | None = None
    """Custom string defining the model of the data object."""

    data: StepData | None = None
    """Data returned by the test step."""

    has_children: bool | None = None
    """Indicates if the step has child steps."""

    workspace: str | None = None
    """The workspace the test step belongs to."""

    keywords: List[str] | None = None
    """Words or phrases associated with the test step."""

    properties: Dict[str, str] | None = None
    """Test step properties."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_step_data.py sha256=59be972608b3b66d0469002d59dc94d46672a4745965f824d370a404ee2dead1 bytes=717 -->
## FILE: nisystemlink/clients/testmonitor/models/_step_data.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_step_data.py`
- sha256: `59be972608b3b66d0469002d59dc94d46672a4745965f824d370a404ee2dead1`
- bytes: 717

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import ConfigDict, Field


class Measurement(JsonModel):
    name: str | None = None
    status: str | None = None
    measurement: str | None = None
    lowLimit: str | None = None
    highLimit: str | None = None
    units: str | None = None
    comparisonType: str | None = None
    model_config = ConfigDict(extra="allow")
    __pydantic_extra__: Dict[str, str] = Field(init=False)


class StepData(JsonModel):
    text: str | None = None
    """Text string describing the output data."""

    parameters: List[Measurement] | None = None
    """List of properties objects."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_result_request.py sha256=36357bd08667197a1d39363de5b4dee4dc93e21acbe523a9b91a4d1100421398 bytes=1775 -->
## FILE: nisystemlink/clients/testmonitor/models/_update_result_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_update_result_request.py`
- sha256: `36357bd08667197a1d39363de5b4dee4dc93e21acbe523a9b91a4d1100421398`
- bytes: 1775

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._status import Status


class UpdateResultRequest(JsonModel):
    """Contains information about a result."""

    status: Status | None = None
    """The status of the result."""

    started_at: datetime | None = None
    """The time that the result started."""

    program_name: str | None = None
    """The name of the program that generated this result."""

    id: str
    """The globally unique id of the result."""

    system_id: str | None = None
    """The id of the system that generated this result."""

    host_name: str | None = None
    """The name of the host that generated this result."""

    part_number: str | None = None
    """The part number is the unique identifier of a product within a single org."""

    serial_number: str | None = None
    """The serial number of the system that generated this result."""

    total_time_in_seconds: float | None = None
    """The total time that the result took to run in seconds."""

    keywords: List[str] | None = None
    """A list of keywords that categorize this result."""

    properties: Dict[str, str | None] | None = None
    """A list of custom properties for this result."""

    operator: str | None = None
    """The operator that ran the result."""

    file_ids: List[str] | None = None
    """A list of file ids that are attached to this result."""

    data_table_ids: List[str] | None = None
    """A list of data table ids that are attached to this result."""

    workspace: str | None = None
    """The id of the workspace that this product belongs to."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_results_partial_success.py sha256=de83dd7213422748eabee4a9695773faf634f2eaf3726eae0f31833956f686b4 bytes=815 -->
## FILE: nisystemlink/clients/testmonitor/models/_update_results_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_update_results_partial_success.py`
- sha256: `de83dd7213422748eabee4a9695773faf634f2eaf3726eae0f31833956f686b4`
- bytes: 815

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._result import Result
from nisystemlink.clients.testmonitor.models._update_result_request import (
    UpdateResultRequest,
)


class UpdateResultsPartialSuccess(JsonModel):
    results: List[Result]
    """The list of results that were successfully created."""

    failed: List[UpdateResultRequest] | None = None
    """The list of results that were not created.
    If this is `None`, then all results were successfully created.
    """

    error: ApiError | None = None
    """Error messages for results that were not created.
    If this is `None`, then all results were successfully created.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_steps_partial_success.py sha256=08569118eea636c729f0dec9318f384ea04101115595a7cc64ac88f510f2b5d1 bytes=794 -->
## FILE: nisystemlink/clients/testmonitor/models/_update_steps_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_update_steps_partial_success.py`
- sha256: `08569118eea636c729f0dec9318f384ea04101115595a7cc64ac88f510f2b5d1`
- bytes: 794

````python
from typing import List

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._step import Step
from nisystemlink.clients.testmonitor.models._update_steps_request import (
    UpdateStepRequest,
)


class UpdateStepsPartialSuccess(JsonModel):
    steps: List[Step]
    """The list of steps that were successfully updated."""

    failed: List[UpdateStepRequest] | None = None
    """The list of steps that were not updated.

    If this is `None`, then all steps were successfully updated.
    """

    error: ApiError | None = None
    """Error messages for steps that were not updated.

    If this is `None`, then all steps were successfully updated.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_steps_request.py sha256=55968d6b57888011b579c3855463320c957cb04763a9c5d094aaa9a2d1716568 bytes=315 -->
## FILE: nisystemlink/clients/testmonitor/models/_update_steps_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/models/_update_steps_request.py`
- sha256: `55968d6b57888011b579c3855463320c957cb04763a9c5d094aaa9a2d1716568`
- bytes: 315

````python
from typing import List

from nisystemlink.clients.testmonitor.models._create_steps_request import (
    BaseStepRequest,
)


class UpdateStepRequest(BaseStepRequest):
    name: str | None = None
    """Step name."""

    children: List["UpdateStepRequest"] | None = None
    """Nested child steps."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/utilities/__init__.py sha256=e1376fd18429331c339d115fea0a86e192bb8b8a58bf054c53c77ce206753df0 bytes=157 -->
## FILE: nisystemlink/clients/testmonitor/utilities/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/utilities/__init__.py`
- sha256: `e1376fd18429331c339d115fea0a86e192bb8b8a58bf054c53c77ce206753df0`
- bytes: 157

````python
from ._dataframe_utilities import (
    convert_results_to_dataframe,
    convert_steps_to_dataframe,
    has_name_and_measurement,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/utilities/_dataframe_utilities.py sha256=8c20489a9fadddc877a518ebec897ca93c6a81a6689b2c577d7469cc8f7f6a58 bytes=13005 -->
## FILE: nisystemlink/clients/testmonitor/utilities/_dataframe_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/utilities/_dataframe_utilities.py`
- sha256: `8c20489a9fadddc877a518ebec897ca93c6a81a6689b2c577d7469cc8f7f6a58`
- bytes: 13005

````python
from typing import Any, Callable, Dict, List

import pandas as pd
from nisystemlink.clients.testmonitor.models import (
    Measurement,
    Result,
    Step,
    StepProjection,
)
from nisystemlink.clients.testmonitor.utilities.constants import DataFrameHeaders


def has_name_and_measurement(measurement: Measurement) -> bool:
    """Checks if a step data parameter is measurement data by ensuring it has both
    'name' and 'measurement' fields.

    Args:
        measurement: A measurement data object

    Returns:
        bool: True if the measurement has both 'name' and 'measurement' fields, False otherwise.
    """
    return measurement.name is not None and measurement.measurement is not None


def convert_results_to_dataframe(
    results: List[Result], set_id_as_index: bool = True
) -> pd.DataFrame:
    """Creates a Pandas DataFrame for the results.

    Args:
        results: The list of results to be included in the dataframe.
        set_id_as_index: If true (default value), result id will be set as index for the dataframe.
                         If false, index will not be set.

    Returns:
        A Pandas DataFrame with the each result fields having a separate column.
        Following fields are split into sub-columns.
            - status_type_summary: All the entries will be split into separate columns.
            For example, status_type_summary.LOOPING, status_type_summary.PASSED, etc
            - Properties: All the properties will be split into separate columns. For example,
            properties.property1, properties.property2, etc.
    """
    results_dict = []
    for result in results:
        data = result.model_dump(exclude_none=True)
        __normalize_status(data)
        results_dict.append(data)

    normalized_dataframe = pd.json_normalize(results_dict, sep=".")
    normalized_dataframe = __format_results_columns(
        results_dataframe=normalized_dataframe
    )
    if set_id_as_index and "id" in normalized_dataframe.columns:
        normalized_dataframe.set_index("id", inplace=True)

    return normalized_dataframe


def convert_steps_to_dataframe(
    steps: List[Step],
    is_valid_measurement: (
        Callable[[Measurement], bool] | None
    ) = has_name_and_measurement,
) -> pd.DataFrame:
    """Converts a list of steps into a normalized dataframe.

    Args:
        steps: A list of steps.
        is_valid_measurement: Optional callback function that checks if a step data parameter is a
            valid measurement so that only those are included in the returned dataframe. The method takes
            a measurement as input and returns a boolean value.
            The default behavior is to consider only measurement data that have both 'name' and 'measurement'
            fields with values as valid measurements.
            If none of the measurements have the required fields, the step data parameters will not
            appear in the dataframe.
            If the callback function is set to None, all step data parameters will be included in the dataframe.

    Returns:
        DataFrame:
            - A Pandas DataFrame containing the steps data. The DataFrame would consist of all the
            fields in the input steps.
            - A new column would be created for unique `properties` across all steps. The property
            columns would be named in the format `properties.property_name`.
            - A new column would be created for unique `Inputs` and `Outputs` across all steps. The columns
            would be named in the format `inputs.input_name` and `outputs.output_name` respectively.
            - The column headers for the step data parameters would differ based on the callback function. If
            the None is passed for the callback function, the column would be prefixed with `data.parameters.`.
            If the callback function is set, the column would be prefixed with `data.measurement.`.
    """
    DATA_PARAMETERS_PREFIX = (
        "data.parameters" if is_valid_measurement is None else "data.measurement"
    )
    step_dicts = __convert_steps_to_dict(steps, is_valid_measurement)
    steps_dataframe = pd.json_normalize(step_dicts, sep=".")
    steps_dataframe = __explode_and_normalize(
        steps_dataframe, "data.parameters", f"{DATA_PARAMETERS_PREFIX}."
    )
    grouped_columns = __group_step_columns(steps_dataframe.columns)
    return steps_dataframe.reindex(columns=grouped_columns, copy=False)


def __normalize_status(
    data: Dict[str, Any],
) -> None:
    """Normalizes the status object into a string.

    Args:
        data: Dictionary containing status information.

    """
    status = data.get("status", {})
    if status:
        if status.get("status_type") == "CUSTOM":
            data["status"] = status.get("status_name", None)
        else:
            data["status"] = getattr(status.get("status_type", None), "value", None)


def __format_results_columns(results_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Format results column to keep properties at the end.

    Args:
        results_dataframe: Dataframe of results.

    Returns:
        Formatted dataframe of results.
    """
    column_headers = results_dataframe.columns.to_list()
    standard_column_headers = [
        header for header in column_headers if __is_standard_column_header(header)
    ]
    status_type_summary_header = [
        header
        for header in column_headers
        if __is_status_type_summary_header(header=header)
    ]
    properties_headers = [
        header for header in column_headers if __is_property_header(header=header)
    ]
    standard_column_headers += status_type_summary_header + properties_headers

    return results_dataframe.reindex(columns=standard_column_headers, copy=False)


def __is_standard_column_header(header: str) -> bool:
    """Check if column header is not status type summary or property.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header doesn't start with 'status_type_summary.', 'properties.'. Else returns false.

    """
    return not (
        __is_status_type_summary_header(header=header)
        or __is_property_header(header=header)
    )


def __is_status_type_summary_header(header: str) -> bool:
    """Check if column header is not a status type summary.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header contains 'status_type_summary.'. Else returns false.

    """
    return header.startswith(DataFrameHeaders.STATUS_TYPE_SUMMARY_HEADER_PREFIX)


def __is_property_header(header: str) -> bool:
    """Check if column header is not a property.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header contains 'properties.'. Else returns false.

    """
    return header.startswith(DataFrameHeaders.PROPERTY_COLUMN_HEADER_PREFIX)


def __convert_steps_to_dict(
    steps: List[Step],
    is_valid_measurement: Callable[[Measurement], bool] | None,
) -> List[Dict[str, Any]]:
    """Converts a list of steps to dictionaries, excluding None values.

    Args:
        steps: A list of steps.
        is_valid_measurement: Optional callback function that checks if a step data
            parameter is a valid measurement so that only those are included in the returned dataframe.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing step information.
    """
    steps_dict = []
    for step in steps:

        single_step_dict = step.model_dump(exclude_none=True)
        __filter_invalid_measurements(single_step_dict, step, is_valid_measurement)
        __normalize_inputs_outputs(single_step_dict, step)
        __normalize_status(single_step_dict)
        steps_dict.append(single_step_dict)
    return steps_dict


def __filter_invalid_measurements(
    step_dict: Dict[str, Any],
    step: Step,
    is_valid_measurement: Callable[[Measurement], bool] | None,
) -> None:
    """Gets data parameters from the step dictionary and filters it based on the callback function.

    Args:
        step_dict: A dictionary with step information.
        step: A Step object containing data parameters.
        is_valid_measurement: Optional callback function to check if a measurement is valid. The method takes
            a Measurement as input and returns a boolean value. The default behavior is to consider only parameters
            that have both 'name' and 'measurement' fields with values as valid measurements.

    Returns:
        None: The function modifies step dictionary in place with filtered data parameters.
    """
    if step.data and step.data.parameters and is_valid_measurement is not None:
        valid_measurement_parameters = []
        for measurement in step.data.parameters:
            if measurement and is_valid_measurement(measurement):
                valid_measurement_parameters.append(measurement)

        step_dict["data"]["parameters"] = [
            measurement.model_dump(exclude_none=True)
            for measurement in valid_measurement_parameters
        ]


def __normalize_inputs_outputs(
    step_dict: Dict[str, Any],
    step: Step,
) -> None:
    """Normalizes the input and output fields by converting them into dictionaries.

    Args:
        step_dict: A dictionary with step information.
        step: A Step object containing inputs and outputs.

    Returns:
        None: The function modifies step_dict in place with normalized inputs and outputs.
    """
    STEP_INPUTS = StepProjection.INPUTS.lower()
    STEP_OUTPUTS = StepProjection.OUTPUTS.lower()
    if STEP_INPUTS in step_dict:
        step_dict[STEP_INPUTS] = (
            {item.name: item.value for item in step.inputs} if step.inputs else {}
        )
    if STEP_OUTPUTS in step_dict:
        step_dict[STEP_OUTPUTS] = (
            {item.name: item.value for item in step.outputs} if step.outputs else {}
        )


def __explode_and_normalize(
    dataframe: pd.DataFrame, column: str, prefix: str
) -> pd.DataFrame:
    """Explodes a specified column in the dataframe and normalizes its nested data.
    This function handles the process of exploding a column that contains lists or arrays,
    transforming each list element into a separate row. After exploding, it normalizes the
    nested data into flat columns using the specified prefix, making it easier to analyze
    and manipulate. The new columns are added to the original dataframe.

    Args:
        dataframe: The input DataFrame that contains the column to explode and normalize.
        column: The name of the column in the DataFrame that contains the list-like data to explode.
        prefix: The prefix to add to the new column names created during the normalization process.

    Returns:
        DataFrame:
        - A new DataFrame with the exploded rows and the normalized columns, all combined
        with the original data in the dataframe.
        - If the column is not found in the dataframe, the original dataframe is returned unchanged.
    """
    if column in dataframe:
        exploded_dataframe = dataframe.explode(column, ignore_index=True)
        normalized_dataframe = pd.json_normalize(
            exploded_dataframe.pop(column)
        ).add_prefix(prefix)
        return pd.concat([exploded_dataframe, normalized_dataframe], axis=1, copy=False)
    return dataframe


def __group_step_columns(dataframe_columns: List[str]) -> List[str]:
    """Groups and orders dataframe columns into predefined categories to maintain a consistent structure.
    When normalizing steps into a dataframe, new input, output, or property fields may be added at the end,
    disrupting the expected column order. This function ensures columns are grouped properly.

    Args:
        dataframe_columns: The list of all columns from the normalized dataframe.

    Returns:
        List[str]: A list containing grouped and ordered columns.
    """
    GENERAL_CATEGORIES = "general"
    CATEGORY_KEYS = DataFrameHeaders.CATEGORY_COLUMN_HEADERS
    grouped_columns: Dict[str, List[str]] = {category: [] for category in CATEGORY_KEYS}
    for column in dataframe_columns:
        column_lower = column.lower()
        key = next(
            (
                category
                for category in CATEGORY_KEYS[1:]
                if column_lower.startswith(category)
                and column != StepProjection.DATA_MODEL.lower()
            ),
            GENERAL_CATEGORIES,
        )
        grouped_columns[key].append(column)
    return [
        column
        for category_key in CATEGORY_KEYS
        for column in grouped_columns[category_key]
    ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/utilities/constants.py sha256=913c1a86f83106ccc250c871c59bee0607890edbafa631be152c09f51d943fb8 bytes=283 -->
## FILE: nisystemlink/clients/testmonitor/utilities/constants.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/testmonitor/utilities/constants.py`
- sha256: `913c1a86f83106ccc250c871c59bee0607890edbafa631be152c09f51d943fb8`
- bytes: 283

````python
class DataFrameHeaders:
    STATUS_TYPE_SUMMARY_HEADER_PREFIX = "status_type_summary."

    PROPERTY_COLUMN_HEADER_PREFIX = "properties."

    CATEGORY_COLUMN_HEADERS = [
        "general",
        "inputs",
        "outputs",
        "data",
        "properties",
    ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/__init__.py sha256=8343e8515d7b34ba56051f33b4f082b818cf7d3331c2bf0a83401584ca88d6ca bytes=205 -->
## FILE: nisystemlink/clients/work_item/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/__init__.py`
- sha256: `8343e8515d7b34ba56051f33b4f082b818cf7d3331c2bf0a83401584ca88d6ca`
- bytes: 205

````python
"""Start here with WorkItemClient for work item operations."""

from ._work_item_client import WorkItemClient, WorkItemExecuteApiException

__all__ = ["WorkItemClient", "WorkItemExecuteApiException"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/_work_item_client.py sha256=af15b059b4cb8cef84766b4d879c3a9e72bc99b633c3e4bbcd0bc409a932bf64 bytes=15342 -->
## FILE: nisystemlink/clients/work_item/_work_item_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/_work_item_client.py`
- sha256: `af15b059b4cb8cef84766b4d879c3a9e72bc99b633c3e4bbcd0bc409a932bf64`
- bytes: 15342

````python
from typing import List

from nisystemlink.clients import core
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients.core._uplink._methods import get, post
from nisystemlink.clients.work_item import models
from uplink import Field, Path, retry

from ..core.helpers._partial_success import unwrap_single_item_partial_success


class WorkItemExecuteApiException(core.ApiException):
    """Raised when the execute work item API returns an error with a structured response body.

    The API may return partial results (e.g. cancelled job IDs) alongside an error.
    This exception exposes those results via the :attr:`result` property.
    """

    def __init__(
        self,
        msg: str,
        *,
        http_status_code: int,
        error: core.ApiError | None,
        result: models.ExecutionResult | None,
    ) -> None:
        super().__init__(msg, error=error, http_status_code=http_status_code)
        self._result = result

    @property
    def result(self) -> models.ExecutionResult | None:
        """The partial execution result returned alongside the error, if any."""
        return self._result


@retry(
    when=retry.when.status(408, 429, 502, 503, 504),
    stop=retry.stop.after_attempt(5),
    on_exception=retry.CONNECTION_ERROR,
)
class WorkItemClient(BaseClient):
    def __init__(self, configuration: HttpConfiguration | None = None):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the WorkItem Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()

        super().__init__(configuration, base_path="/niworkitem/v1/")

    @get("workitems/{work_item_id}")
    def get_work_item(self, work_item_id: str) -> models.WorkItem:
        """Retrieves a work item by its ID.

        Args:
            work_item_id: The ID of the work item to retrieve.

        Returns:
            The work item corresponding to the given ID.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    @post("workitems", args=[Field("workItems")])
    def create_work_items(
        self, work_items: List[models.CreateWorkItemRequest]
    ) -> models.CreateWorkItemsPartialSuccessResponse:
        """Creates one or more work items.

        Args:
            work_items: A list of work items to create.

        Returns:
            A list of created work items, work items that failed to create, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def create_work_item(
        self, work_item: models.CreateWorkItemRequest
    ) -> models.WorkItem:
        """Creates a single work item.

        Args:
            work_item: The work item to create.

        Returns:
            The created work item.

        Raises:
            ApiException: if the work item could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_work_items([work_item])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.created_work_items,
            failed=response.failed_work_items,
            error=response.error,
            failure_message="Failed to create work item.",
            empty_message="Server returned no created work items.",
        )

    @post("query-workitems")
    def query_work_items(
        self, query_work_items: models.QueryWorkItemsRequest
    ) -> models.PagedWorkItems:
        """Queries one or more work items.

        Args:
            query_work_items: The query request for work items.

        Returns:
            A list of work items based on the query.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    @post("schedule-workitems")
    def schedule_work_items(
        self, schedule_work_items: models.ScheduleWorkItemsRequest
    ) -> models.ScheduleWorkItemsPartialSuccessResponse:
        """Schedule work items.

        Args:
            schedule_work_items: The schedule request for work item.

        Returns:
            A list of scheduled work items, work items that failed to schedule, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def schedule_work_item(
        self,
        work_item: models.ScheduleWorkItemRequest,
        replace: bool | None = None,
    ) -> models.WorkItem:
        """Schedules a single work item.

        Args:
            work_item: The work item schedule request.
            replace: When true, existing array fields are replaced instead of merged.

        Returns:
            The scheduled work item.

        Raises:
            ApiException: if the work item could not be scheduled or the service returns an
                unexpected partial-success payload.
        """
        response = self.schedule_work_items(
            models.ScheduleWorkItemsRequest(work_items=[work_item], replace=replace)
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.scheduled_work_items,
            failed=response.failed_work_items,
            error=response.error,
            failure_message="Failed to schedule work item.",
            empty_message="Server returned no scheduled work items.",
        )

    @post("update-workitems")
    def update_work_items(
        self, update_work_items: models.UpdateWorkItemsRequest
    ) -> models.UpdateWorkItemsPartialSuccessResponse:
        """Updates one or more work items.

        Args:
            update_work_items: The update request containing work items to update.

        Returns:
            A list of updated work items, work items that failed to update, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def update_work_item(
        self,
        work_item: models.UpdateWorkItemRequest,
        replace: bool | None = None,
    ) -> models.WorkItem:
        """Updates a single work item.

        Args:
            work_item: The work item to update.
            replace: When true, existing array and key-value pair fields are replaced instead of merged.

        Returns:
            The updated work item.

        Raises:
            ApiException: if the work item could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_work_items(
            models.UpdateWorkItemsRequest(work_items=[work_item], replace=replace)
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.updated_work_items,
            failed=response.failed_work_items,
            error=response.error,
            failure_message="Failed to update work item.",
            empty_message="Server returned no updated work items.",
        )

    @post("delete-workitems", args=[Field("ids")])
    def delete_work_items(
        self, ids: List[str]
    ) -> models.DeleteWorkItemsPartialSuccessResponse | None:
        """Deletes one or more work items by IDs.

        Args:
            ids: A list of work item IDs to delete.

        Returns:
            A partial success if any work items failed to delete, or None if all
            work items were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def execute_work_item(
        self, work_item_id: str, action: str
    ) -> models.ExecuteWorkItemResponse:
        """Executes the specified action for the work item.

        Args:
            work_item_id: The ID of the work item the action will be performed on.
            action: The action to execute on the work item.

        Returns:
            The response containing the execution result.

        Raises:
            WorkItemExecuteApiException: if the API returns an error response with
                an execute-specific body. The :attr:`~WorkItemExecuteApiException.result`
                property may contain partial results (e.g. cancelled job IDs).
            ApiException: if unable to communicate with the `/niworkitem` service
                or provided invalid arguments.
        """
        try:
            return self._execute_work_item(work_item_id=work_item_id, action=action)
        except core.ApiException as e:
            data = e.response_data
            if not data or "result" not in data:
                raise

            try:
                response = models.ExecuteWorkItemResponse.model_validate(data)
            except Exception:
                raise e

            raise WorkItemExecuteApiException(
                str(e),
                http_status_code=e.http_status_code or 0,
                error=response.error,
                result=response.result,
            ) from e

    @post(
        "workitems/{workItemId}/execute",
        args=[Path(name="workItemId"), Field("action")],
    )
    def _execute_work_item(
        self, work_item_id: str, action: str
    ) -> models.ExecuteWorkItemResponse:
        """Internal implementation of execute_work_item."""
        ...

    @post("workitem-templates", args=[Field("workItemTemplates")])
    def create_work_item_templates(
        self, work_item_templates: List[models.CreateWorkItemTemplateRequest]
    ) -> models.CreateWorkItemTemplatesPartialSuccessResponse:
        """Creates one or more work item templates.

        Args:
            work_item_templates: A list of work item templates to create.

        Returns:
            A list of created work item templates, templates that failed to create, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def create_work_item_template(
        self, work_item_template: models.CreateWorkItemTemplateRequest
    ) -> models.WorkItemTemplate:
        """Creates a single work item template.

        Args:
            work_item_template: The work item template to create.

        Returns:
            The created work item template.

        Raises:
            ApiException: if the work item template could not be created or the service returns an
                unexpected partial-success payload.
        """
        response = self.create_work_item_templates([work_item_template])

        return unwrap_single_item_partial_success(
            response=response,
            items=response.created_work_item_templates,
            failed=response.failed_work_item_templates,
            error=response.error,
            failure_message="Failed to create work item template.",
            empty_message="Server returned no created work item templates.",
        )

    @post("query-workitem-templates")
    def query_work_item_templates(
        self, query_work_item_templates: models.QueryWorkItemTemplatesRequest
    ) -> models.PagedWorkItemTemplates:
        """Queries one or more work item templates.

        Args:
            query_work_item_templates: The query request for work item templates.

        Returns:
            A list of work item templates based on the query.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    @post("update-workitem-templates")
    def update_work_item_templates(
        self, update_work_item_templates: models.UpdateWorkItemTemplatesRequest
    ) -> models.UpdateWorkItemTemplatesPartialSuccessResponse:
        """Updates one or more work item templates.

        Args:
            update_work_item_templates: The update request containing work item templates to update.

        Returns:
            A list of updated work item templates, templates that failed to update, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...

    def update_work_item_template(
        self,
        work_item_template: models.UpdateWorkItemTemplateRequest,
        replace: bool | None = None,
    ) -> models.WorkItemTemplate:
        """Updates a single work item template.

        Args:
            work_item_template: The work item template to update.
            replace: When true, existing key-value pair fields are replaced instead of merged.

        Returns:
            The updated work item template.

        Raises:
            ApiException: if the work item template could not be updated or the service returns an
                unexpected partial-success payload.
        """
        response = self.update_work_item_templates(
            models.UpdateWorkItemTemplatesRequest(
                work_item_templates=[work_item_template],
                replace=replace,
            )
        )

        return unwrap_single_item_partial_success(
            response=response,
            items=response.updated_work_item_templates,
            failed=response.failed_work_item_templates,
            error=response.error,
            failure_message="Failed to update work item template.",
            empty_message="Server returned no updated work item templates.",
        )

    @post("delete-workitem-templates", args=[Field("ids")])
    def delete_work_item_templates(
        self, ids: List[str]
    ) -> models.DeleteWorkItemTemplatesPartialSuccessResponse | None:
        """Deletes one or more work item templates.

        Args:
            ids: A list of work item template IDs to delete.

        Returns:
            A partial success if any work item templates failed to delete, or None if all
            work item templates were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        """
        ...
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/__init__.py sha256=a9d5ee153b60844dcb24094ad44db5ee74117bf13497be3aad39a2253b6e9664 bytes=3135 -->
## FILE: nisystemlink/clients/work_item/models/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/__init__.py`
- sha256: `a9d5ee153b60844dcb24094ad44db5ee74117bf13497be3aad39a2253b6e9664`
- bytes: 3135

````python
from ._work_item import WorkItem
from ._work_item_template import WorkItemTemplate, WorkItemTemplateBase

from ._state import State
from ._query_work_items_request import WorkItemField, WorkItemOrderBy
from ._query_work_item_templates_request import (
    WorkItemTemplateField,
    WorkItemTemplateOrderBy,
)
from ._dashboard import Dashboard, DashboardUrl
from ._resources_definition import (
    ResourceDefinition,
    ResourceSelectionDefinition,
    ResourcesDefinition,
    ScheduleResourceDefinition,
    ScheduleResourcesDefinition,
    ScheduleSystemResourceDefinition,
    SystemResourceDefinition,
    SystemResourceSelectionDefinition,
    TemplateResourceDefinition,
    TemplateResourcesDefinition,
)
from ._schedule_definition import ScheduleDefinition
from ._timeline_definition import TemplateTimelineDefinition, TimelineDefinition
from ._execution_definition import (
    ExecutionDefinition,
    Job,
    JobExecution,
    ManualExecution,
    NoneExecution,
    NotebookExecution,
)
from ._execution_event import (
    ExecutionEvent,
    ExecutionEventBase,
    JobExecutionEvent,
    ManualExecutionEvent,
    NotebookExecutionEvent,
)

from ._create_work_item_request import CreateWorkItemRequest
from ._create_work_items_partial_success_response import (
    CreateWorkItemsPartialSuccessResponse,
)
from ._delete_work_items_partial_success_response import (
    DeleteWorkItemsPartialSuccessResponse,
)
from ._paged_work_items import PagedWorkItems
from ._query_work_items_request import QueryWorkItemsRequest
from ._schedule_work_item_request import ScheduleWorkItemRequest
from ._schedule_work_items_partial_success_response import (
    ScheduleWorkItemsPartialSuccessResponse,
)
from ._schedule_work_items_request import ScheduleWorkItemsRequest
from ._update_work_item_request import UpdateWorkItemRequest
from ._update_work_items_partial_success_response import (
    UpdateWorkItemsPartialSuccessResponse,
)
from ._update_work_items_request import UpdateWorkItemsRequest

from ._execute_work_item_response import (
    ExecuteWorkItemResponse,
    ExecutionResult,
    ExecutionResultBase,
    JobExecutionResult,
    ManualExecutionResult,
    NoneExecutionResult,
    NotebookExecutionResult,
    ScheduleExecutionResult,
    UnscheduleExecutionResult,
)

from ._create_work_item_template_request import CreateWorkItemTemplateRequest
from ._create_work_item_templates_partial_success_response import (
    CreateWorkItemTemplatesPartialSuccessResponse,
)
from ._delete_work_item_templates_partial_success_response import (
    DeleteWorkItemTemplatesPartialSuccessResponse,
)
from ._paged_work_item_templates import PagedWorkItemTemplates
from ._query_work_item_templates_request import QueryWorkItemTemplatesRequest
from ._update_work_item_template_request import UpdateWorkItemTemplateRequest
from ._update_work_item_templates_request import UpdateWorkItemTemplatesRequest
from ._update_work_item_templates_partial_success_response import (
    UpdateWorkItemTemplatesPartialSuccessResponse,
)

# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_request.py sha256=499c44260ca25720757151a28856bfc4d7a18bf648b4b092761c7bd9852fd142 bytes=2116 -->
## FILE: nisystemlink/clients/work_item/models/_create_work_item_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_create_work_item_request.py`
- sha256: `499c44260ca25720757151a28856bfc4d7a18bf648b4b092761c7bd9852fd142`
- bytes: 2116

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import Dashboard
from ._execution_definition import ExecutionDefinition
from ._resources_definition import ResourcesDefinition
from ._timeline_definition import TimelineDefinition


class CreateWorkItemRequest(JsonModel):
    """Represents the request body content for creating a work item."""

    name: str | None = None
    """The name of the work item."""

    type: str | None = None
    """The type of the work item."""

    state: str | None = None
    """The state of the work item."""

    description: str | None = None
    """A description of the work item."""

    parent_id: str | None = None
    """The ID of the parent work item."""

    template_id: str | None = None
    """The ID of the template used to create the work item."""

    assigned_to: str | None = None
    """The user or group assigned to the work item."""

    requested_by: str | None = None
    """The user or group who requested the work item."""

    test_program: str | None = None
    """The test program associated with the work item."""

    part_number: str | None = None
    """The part number associated with the work item."""

    workspace: str | None = None
    """The workspace to which the work item belongs."""

    timeline: TimelineDefinition | None = None
    """Timeline properties for the work item."""

    resources: ResourcesDefinition | None = None
    """Resources reserved for the work item."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the work item."""

    file_ids_from_template: List[str] | None = None
    """The list of file IDs inherited from the template."""

    properties: Dict[str, str] | None = None
    """Additional properties for the work item."""

    dashboard: Dashboard | None = None
    """The dashboard associated with the work item."""

    workflow_id: str | None = None
    """The ID of the workflow associated with the work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_template_request.py sha256=ea65a98971ad980c84790f3155f8045bd98dc787ceeb4cb59d8b48bb73e5d841 bytes=421 -->
## FILE: nisystemlink/clients/work_item/models/_create_work_item_template_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_create_work_item_template_request.py`
- sha256: `ea65a98971ad980c84790f3155f8045bd98dc787ceeb4cb59d8b48bb73e5d841`
- bytes: 421

````python
from ._work_item_template import WorkItemTemplateBase


class CreateWorkItemTemplateRequest(WorkItemTemplateBase):
    """Represents the request body content for creating a work item template."""

    name: str
    """The name of the work item template."""

    template_group: str
    """The template group defined by the user."""

    type: str
    """The type of work item created from this template."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_templates_partial_success_response.py sha256=7e6a2694de21e4482a9ca8051621bbd0341717a3c42e65f893b5cfa58f5be480 bytes=823 -->
## FILE: nisystemlink/clients/work_item/models/_create_work_item_templates_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_create_work_item_templates_partial_success_response.py`
- sha256: `7e6a2694de21e4482a9ca8051621bbd0341717a3c42e65f893b5cfa58f5be480`
- bytes: 823

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._create_work_item_template_request import CreateWorkItemTemplateRequest
from ._work_item_template import WorkItemTemplate


class CreateWorkItemTemplatesPartialSuccessResponse(JsonModel):
    """Response for creating work item templates with partial success."""

    created_work_item_templates: List[WorkItemTemplate]
    """List of successfully created work item templates."""

    failed_work_item_templates: List[CreateWorkItemTemplateRequest] | None = None
    """List of work item template requests that failed during creation."""

    error: ApiError | None = None
    """The error that occurred when creating the work item templates."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_items_partial_success_response.py sha256=edfd77233804baf7e498c641b42b07c76768dea8f8d08bfc057feed117315440 bytes=711 -->
## FILE: nisystemlink/clients/work_item/models/_create_work_items_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_create_work_items_partial_success_response.py`
- sha256: `edfd77233804baf7e498c641b42b07c76768dea8f8d08bfc057feed117315440`
- bytes: 711

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._create_work_item_request import CreateWorkItemRequest
from ._work_item import WorkItem


class CreateWorkItemsPartialSuccessResponse(JsonModel):
    """Response for creating work items with partial success."""

    created_work_items: List[WorkItem]
    """List of successfully created work items."""

    failed_work_items: List[CreateWorkItemRequest] | None = None
    """List of work item requests that failed during creation."""

    error: ApiError | None = None
    """The error that occurred when creating the work items."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_dashboard.py sha256=2f142913ba973878656ab030ca8ab3f11a674e76f3cc48a1c0a73c53eb91dc78 bytes=549 -->
## FILE: nisystemlink/clients/work_item/models/_dashboard.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_dashboard.py`
- sha256: `2f142913ba973878656ab030ca8ab3f11a674e76f3cc48a1c0a73c53eb91dc78`
- bytes: 549

````python
from typing import Dict

from nisystemlink.clients.core._uplink._json_model import JsonModel


class Dashboard(JsonModel):
    """Represents a dashboard reference."""

    id: str | None = None
    """ID of the dashboard"""

    variables: Dict[str, str] | None = None
    """Variables for the dashboard"""


class DashboardUrl(Dashboard):
    """Definition and URL of the dashboard reference associated with this work item."""

    url: str | None = None
    """URL of the dashboard reference associated with this work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_delete_work_item_templates_partial_success_response.py sha256=9dbe2596ef05345e6f573f1b0281666ea5aa7ad0ce82b481d7b969f1ad0de2b8 bytes=636 -->
## FILE: nisystemlink/clients/work_item/models/_delete_work_item_templates_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_delete_work_item_templates_partial_success_response.py`
- sha256: `9dbe2596ef05345e6f573f1b0281666ea5aa7ad0ce82b481d7b969f1ad0de2b8`
- bytes: 636

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteWorkItemTemplatesPartialSuccessResponse(JsonModel):
    """Response for deleting work item templates with partial success."""

    deleted_ids: List[str] | None = None
    """List of work item template IDs that were successfully deleted."""

    failed_ids: List[str] | None = None
    """List of work item template IDs that failed to delete."""

    error: ApiError | None = None
    """The error that occurred when deleting the work item templates."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_delete_work_items_partial_success_response.py sha256=edeb713b7c75099352b4055c5d8dab08a7a41fe6faec239c9781c94e19e80328 bytes=592 -->
## FILE: nisystemlink/clients/work_item/models/_delete_work_items_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_delete_work_items_partial_success_response.py`
- sha256: `edeb713b7c75099352b4055c5d8dab08a7a41fe6faec239c9781c94e19e80328`
- bytes: 592

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel


class DeleteWorkItemsPartialSuccessResponse(JsonModel):
    """Response for deleting work items with partial success."""

    deleted_ids: List[str] | None = None
    """List of work item IDs that were successfully deleted."""

    failed_ids: List[str] | None = None
    """List of work item IDs that failed to delete."""

    error: ApiError | None = None
    """The error that occurred when deleting the work items."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execute_work_item_response.py sha256=d8bbdf2833f78e716590a201a150630dfc5581464c4bec4f553957b47b98b7a3 bytes=2386 -->
## FILE: nisystemlink/clients/work_item/models/_execute_work_item_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_execute_work_item_response.py`
- sha256: `d8bbdf2833f78e716590a201a150630dfc5581464c4bec4f553957b47b98b7a3`
- bytes: 2386

````python
from typing import Annotated, List, Literal

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field


class ExecutionResultBase(JsonModel):
    """Base class for execution results containing common attributes."""

    error: ApiError | None = None
    """Error information if the execution encountered an error."""


class NoneExecutionResult(ExecutionResultBase):
    """Result of executing a work item action with no execution implementation."""

    type: Literal["NONE"] = Field(default="NONE")
    """Type of execution."""


class ManualExecutionResult(ExecutionResultBase):
    """Result of executing a manual work item action."""

    type: Literal["MANUAL"] = Field(default="MANUAL")
    """Type of execution."""


class NotebookExecutionResult(ExecutionResultBase):
    """Result of executing a notebook work item action."""

    type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")
    """Type of execution."""

    execution_id: str | None = None
    """The notebook execution ID."""


class JobExecutionResult(ExecutionResultBase):
    """Result of executing a job work item action."""

    type: Literal["JOB"] = Field(default="JOB")
    """Type of execution."""

    job_ids: List[str] | None = None
    """The list of job IDs."""


class ScheduleExecutionResult(ExecutionResultBase):
    """Result of executing a schedule work item action."""

    type: Literal["SCHEDULE"] = Field(default="SCHEDULE")
    """Type of execution."""


class UnscheduleExecutionResult(ExecutionResultBase):
    """Result of executing an unschedule work item action."""

    type: Literal["UNSCHEDULE"] = Field(default="UNSCHEDULE")
    """Type of execution."""


ExecutionResult = Annotated[
    NoneExecutionResult
    | ManualExecutionResult
    | NotebookExecutionResult
    | JobExecutionResult
    | ScheduleExecutionResult
    | UnscheduleExecutionResult,
    Field(discriminator="type"),
]
"""Result of executing a work item action."""


class ExecuteWorkItemResponse(JsonModel):
    """Response for executing a work item action."""

    error: ApiError | None = None
    """Error information if the action failed."""

    result: ExecutionResult | None = None
    """Result of the action execution."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execution_definition.py sha256=bb50b10521ad0e6954eac0d020a80d930d25cc524e9ea13e15e6c880b760997d bytes=2108 -->
## FILE: nisystemlink/clients/work_item/models/_execution_definition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_execution_definition.py`
- sha256: `bb50b10521ad0e6954eac0d020a80d930d25cc524e9ea13e15e6c880b760997d`
- bytes: 2108

````python
from typing import Annotated, Any, Dict, List, Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field


class Job(JsonModel):
    """Defines a job to be executed by a work item job execution."""

    functions: List[str]
    """List of function names to execute."""

    arguments: List[List[Any]]
    """List of argument lists for each function."""

    metadata: Dict[str, Any]
    """Additional metadata for the job."""


class NotebookExecution(JsonModel):
    """Defines a notebook execution for a work item."""

    action: str
    """User defined action to perform in workflow."""

    type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")
    """Type of execution, default is 'NOTEBOOK'."""

    notebookId: str
    """ID of the notebook to execute."""

    parameters: Dict[str, str] | None = None
    """	Dictionary of parameters that will be passed to the notebook when the execution is run."""


class ManualExecution(JsonModel):
    """Defines a manual execution for a work item."""

    action: str
    """User defined action to perform in workflow."""

    type: Literal["MANUAL"] = Field(default="MANUAL")
    """Type of execution, default is 'MANUAL'."""


class JobExecution(JsonModel):
    """Defines a job execution for a work item."""

    action: str
    """User defined action to perform in workflow."""

    type: Literal["JOB"] = Field(default="JOB")
    """Type of execution, default is 'JOB'."""

    jobs: List[Job] | None = None
    """List of jobs to execute."""

    systemId: str | None = None
    """Optional system ID where jobs will run."""


class NoneExecution(JsonModel):
    """Defines an unimplemented execution for a work item."""

    action: str
    """User defined action to perform in workflow."""

    type: Literal["NONE"] = Field(default="NONE")
    """Type of execution, default is 'NONE'."""


ExecutionDefinition = Annotated[
    NotebookExecution | ManualExecution | JobExecution | NoneExecution,
    Field(discriminator="type"),
]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execution_event.py sha256=4cc787c910b3f62dc593dca74a093d5d49975080a0731a3aecf37378fd7de152 bytes=2164 -->
## FILE: nisystemlink/clients/work_item/models/_execution_event.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_execution_event.py`
- sha256: `4cc787c910b3f62dc593dca74a093d5d49975080a0731a3aecf37378fd7de152`
- bytes: 2164

````python
from datetime import datetime
from typing import Annotated, List, Literal

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import Field

from ._state import State


class ExecutionEventBase(JsonModel):
    """Base class for execution events containing common attributes."""

    action: str | None = None
    """The action the execution was triggered for."""

    triggered_at: datetime | None = None
    """The time the execution was triggered."""

    triggered_by: str | None = None
    """The user who triggered the execution."""

    previous_state: State | None = None
    """The state of the work item at the time of execution."""

    previous_substate: str | None = None
    """The substate of the work item at the time of execution."""

    new_state: State | None = None
    """The state of the work item resulting from execution."""

    new_substate: str | None = None
    """The substate of the work item resulting from execution."""

    error: ApiError | None = None
    """The error from the execution, if any."""


class NotebookExecutionEvent(ExecutionEventBase):
    """An event tracking a notebook execution triggered from a work item."""

    type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")
    """Type of execution, default is 'NOTEBOOK'."""

    execution_id: str | None = None
    """The ID of the triggered execution."""


class JobExecutionEvent(ExecutionEventBase):
    """An event tracking a job execution triggered from a work item."""

    type: Literal["JOB"] = Field(default="JOB")
    """Type of execution, default is 'JOB'."""

    job_ids: List[str] | None = None
    """The list of job IDs."""


class ManualExecutionEvent(ExecutionEventBase):
    """An event tracking a manual execution triggered from a work item."""

    type: Literal["MANUAL"] = Field(default="MANUAL")
    """Type of execution, default is 'MANUAL'."""


ExecutionEvent = Annotated[
    NotebookExecutionEvent | ManualExecutionEvent | JobExecutionEvent,
    Field(discriminator="type"),
]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_paged_work_item_templates.py sha256=5e694f3fe4ae2cbfa7f1e318e1f65ed154e5f6bdb958be9b13eb1f5ad62ea76a bytes=527 -->
## FILE: nisystemlink/clients/work_item/models/_paged_work_item_templates.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_paged_work_item_templates.py`
- sha256: `5e694f3fe4ae2cbfa7f1e318e1f65ed154e5f6bdb958be9b13eb1f5ad62ea76a`
- bytes: 527

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._work_item_template import WorkItemTemplate


class PagedWorkItemTemplates(WithPaging):
    """The response containing the list of work item templates, total count and continuation token."""

    work_item_templates: List[WorkItemTemplate]
    """A list of all the work item templates in this page."""

    total_count: int | None = None
    """The total number of work item templates that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_paged_work_items.py sha256=c44cf4248b8cb4abcf44310e6084c23234cea8d722269ce6003427c7f43e15ad bytes=458 -->
## FILE: nisystemlink/clients/work_item/models/_paged_work_items.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_paged_work_items.py`
- sha256: `c44cf4248b8cb4abcf44310e6084c23234cea8d722269ce6003427c7f43e15ad`
- bytes: 458

````python
from typing import List

from nisystemlink.clients.core._uplink._with_paging import WithPaging

from ._work_item import WorkItem


class PagedWorkItems(WithPaging):
    """The response containing the list of work items, total count and continuation token."""

    work_items: List[WorkItem]
    """A list of all the work items in this page."""

    total_count: int | None = None
    """The total number of work items that match the query."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_query_work_item_templates_request.py sha256=5acb73e84ffe202b6e4a661fa6a8a1d42ddffdfe83f540d608a0974d4455f431 bytes=3426 -->
## FILE: nisystemlink/clients/work_item/models/_query_work_item_templates_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_query_work_item_templates_request.py`
- sha256: `5acb73e84ffe202b6e4a661fa6a8a1d42ddffdfe83f540d608a0974d4455f431`
- bytes: 3426

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class WorkItemTemplateField(str, Enum):
    """Enumeration of work item template fields that can be projected in query results."""

    ID = "ID"
    PRODUCT_FAMILIES = "PRODUCT_FAMILIES"
    PART_NUMBERS = "PART_NUMBERS"
    NAME = "NAME"
    SUMMARY = "SUMMARY"
    DESCRIPTION = "DESCRIPTION"
    TEMPLATE_GROUP = "TEMPLATE_GROUP"
    TEST_PROGRAM = "TEST_PROGRAM"
    TYPE = "TYPE"
    TIMELINE = "TIMELINE"
    TIMELINE_ESTIMATED_DURATION_IN_SECONDS = "TIMELINE_ESTIMATED_DURATION_IN_SECONDS"
    RESOURCES = "RESOURCES"
    RESOURCES_SYSTEMS = "RESOURCES_SYSTEMS"
    RESOURCES_ASSETS = "RESOURCES_ASSETS"
    RESOURCES_DUTS = "RESOURCES_DUTS"
    RESOURCES_FIXTURES = "RESOURCES_FIXTURES"
    RESOURCES_ASSETS_FILTER = "RESOURCES_ASSETS_FILTER"
    RESOURCES_DUTS_FILTER = "RESOURCES_DUTS_FILTER"
    RESOURCES_FIXTURES_FILTER = "RESOURCES_FIXTURES_FILTER"
    RESOURCES_SYSTEMS_FILTER = "RESOURCES_SYSTEMS_FILTER"
    WORKSPACE = "WORKSPACE"
    CREATED_BY = "CREATED_BY"
    UPDATED_BY = "UPDATED_BY"
    EXECUTION_ACTIONS = "EXECUTION_ACTIONS"
    FILE_IDS = "FILE_IDS"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"
    PROPERTIES = "PROPERTIES"
    DASHBOARD = "DASHBOARD"
    WORKFLOW_ID = "WORKFLOW_ID"


class WorkItemTemplateOrderBy(str, Enum):
    """Enumeration of fields by which work item templates can be ordered."""

    ID = "ID"
    NAME = "NAME"
    TEMPLATE_GROUP = "TEMPLATE_GROUP"
    CREATED_AT = "CREATED_AT"
    UPDATED_AT = "UPDATED_AT"


class QueryWorkItemTemplatesRequest(JsonModel):
    """Represents the request body content for querying work item templates.
    Allows filtering, sorting, and pagination of work item template results.
    """

    filter: str | None = None
    """A string expression to filter the work item templates returned by the query.

    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable.
    """

    substitutions: List[bool | int | str | None] | None = None
    """Makes substitutions in the query filter expression.

    Substitutions for the query expression are indicated by non-negative integers that are
    prefixed with the @ symbol. Each substitution in the given expression will be replaced by
    the element at the corresponding index (zero-based) in this list.
    """

    take: int | None = None
    """The maximum number of work item templates to return in the response."""

    order_by: WorkItemTemplateOrderBy | None = None
    """The field name to use for sorting the work item templates."""

    descending: bool | None = None
    """Whether to return the work item templates in descending order."""

    continuation_token: str | None = None
    """A token which allows the user to resume a query at the next item in the matching results.

    When querying, a token will be returned if a query may be continued. To obtain the next page
    of results, pass the token to the service on a subsequent request.
    """

    projection: List[WorkItemTemplateField] | None = None
    """
    Gets or sets the projection to be used when retrieving the work item templates. If not specified,
    all properties will be returned.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_query_work_items_request.py sha256=a1a605c692f34a07a18b8c3c32415a8bcc41201d9cdac0899c6defcc8b6c87cb bytes=5516 -->
## FILE: nisystemlink/clients/work_item/models/_query_work_items_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_query_work_items_request.py`
- sha256: `a1a605c692f34a07a18b8c3c32415a8bcc41201d9cdac0899c6defcc8b6c87cb`
- bytes: 5516

````python
from enum import Enum
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class WorkItemField(str, Enum):
    """Enumeration of work item fields that can be projected in query results."""

    ID = "ID"
    NAME = "NAME"
    TYPE = "TYPE"
    STATE = "STATE"
    SUBSTATE = "SUBSTATE"
    DESCRIPTION = "DESCRIPTION"
    PARENT_ID = "PARENT_ID"
    TEMPLATE_ID = "TEMPLATE_ID"
    ASSIGNED_TO = "ASSIGNED_TO"
    REQUESTED_BY = "REQUESTED_BY"
    TEST_PROGRAM = "TEST_PROGRAM"
    PART_NUMBER = "PART_NUMBER"
    TIMELINE = "TIMELINE"
    TIMELINE_EARLIEST_START_DATE_TIME = "TIMELINE_EARLIEST_START_DATE_TIME"
    TIMELINE_DUE_DATE_TIME = "TIMELINE_DUE_DATE_TIME"
    TIMELINE_ESTIMATED_DURATION_IN_SECONDS = "TIMELINE_ESTIMATED_DURATION_IN_SECONDS"
    SCHEDULE = "SCHEDULE"
    SCHEDULE_PLANNED_START_DATE_TIME = "SCHEDULE_PLANNED_START_DATE_TIME"
    SCHEDULE_PLANNED_END_DATE_TIME = "SCHEDULE_PLANNED_END_DATE_TIME"
    SCHEDULE_PLANNED_DURATION_IN_SECONDS = "SCHEDULE_PLANNED_DURATION_IN_SECONDS"
    RESOURCES = "RESOURCES"
    RESOURCES_SYSTEMS = "RESOURCES_SYSTEMS"
    RESOURCES_ASSETS = "RESOURCES_ASSETS"
    RESOURCES_DUTS = "RESOURCES_DUTS"
    RESOURCES_FIXTURES = "RESOURCES_FIXTURES"
    RESOURCES_SYSTEMS_SELECTIONS = "RESOURCES_SYSTEMS_SELECTIONS"
    RESOURCES_SYSTEMS_SELECTIONS_ID = "RESOURCES_SYSTEMS_SELECTIONS_ID"
    RESOURCES_SYSTEMS_SELECTIONS_TARGET_LOCATION_ID = (
        "RESOURCES_SYSTEMS_SELECTIONS_TARGET_LOCATION_ID"
    )
    RESOURCES_ASSETS_SELECTIONS = "RESOURCES_ASSETS_SELECTIONS"
    RESOURCES_ASSETS_SELECTIONS_ID = "RESOURCES_ASSETS_SELECTIONS_ID"
    RESOURCES_ASSETS_SELECTIONS_TARGET_LOCATION_ID = (
        "RESOURCES_ASSETS_SELECTIONS_TARGET_LOCATION_ID"
    )
    RESOURCES_ASSETS_SELECTIONS_TARGET_SYSTEM_ID = (
        "RESOURCES_ASSETS_SELECTIONS_TARGET_SYSTEM_ID"
    )
    RESOURCES_ASSETS_SELECTIONS_TARGET_PARENT_ID = (
        "RESOURCES_ASSETS_SELECTIONS_TARGET_PARENT_ID"
    )
    RESOURCES_DUTS_SELECTIONS = "RESOURCES_DUTS_SELECTIONS"
    RESOURCES_DUTS_SELECTIONS_ID = "RESOURCES_DUTS_SELECTIONS_ID"
    RESOURCES_DUTS_SELECTIONS_TARGET_LOCATION_ID = (
        "RESOURCES_DUTS_SELECTIONS_TARGET_LOCATION_ID"
    )
    RESOURCES_DUTS_SELECTIONS_TARGET_PARENT_ID = (
        "RESOURCES_DUTS_SELECTIONS_TARGET_PARENT_ID"
    )
    RESOURCES_DUTS_SELECTIONS_TARGET_SYSTEM_ID = (
        "RESOURCES_DUTS_SELECTIONS_TARGET_SYSTEM_ID"
    )
    RESOURCES_FIXTURES_SELECTIONS = "RESOURCES_FIXTURES_SELECTIONS"
    RESOURCES_FIXTURES_SELECTIONS_ID = "RESOURCES_FIXTURES_SELECTIONS_ID"
    RESOURCES_FIXTURES_SELECTIONS_TARGET_LOCATION_ID = (
        "RESOURCES_FIXTURES_SELECTIONS_TARGET_LOCATION_ID"
    )
    RESOURCES_FIXTURES_SELECTIONS_TARGET_PARENT_ID = (
        "RESOURCES_FIXTURES_SELECTIONS_TARGET_PARENT_ID"
    )
    RESOURCES_FIXTURES_SELECTIONS_TARGET_SYSTEM_ID = (
        "RESOURCES_FIXTURES_SELECTIONS_TARGET_SYSTEM_ID"
    )
    RESOURCES_ASSETS_FILTER = "RESOURCES_ASSETS_FILTER"
    RESOURCES_DUTS_FILTER = "RESOURCES_DUTS_FILTER"
    RESOURCES_FIXTURES_FILTER = "RESOURCES_FIXTURES_FILTER"
    RESOURCES_SYSTEMS_FILTER = "RESOURCES_SYSTEMS_FILTER"
    FILE_IDS_FROM_TEMPLATE = "FILE_IDS_FROM_TEMPLATE"
    PROPERTIES = "PROPERTIES"
    DASHBOARD = "DASHBOARD"
    CREATED_BY = "CREATED_BY"
    CREATED_AT = "CREATED_AT"
    UPDATED_BY = "UPDATED_BY"
    UPDATED_AT = "UPDATED_AT"
    WORKSPACE = "WORKSPACE"
    WORKFLOW_ID = "WORKFLOW_ID"


class WorkItemOrderBy(str, Enum):
    """Enumeration of fields by which work items can be ordered."""

    ID = "ID"
    UPDATED_AT = "UPDATED_AT"


class QueryWorkItemsRequest(JsonModel):
    """Represents the request body content for querying work items.
    Allows filtering, sorting, and pagination of work item results.
    """

    filter: str | None = None
    """A string expression to filter the work items returned by the query.

    `"@0"`, `"@1"` etc. can be used in conjunction with the `substitutions` parameter to keep this
    query string more simple and reusable.
    """

    substitutions: List[bool | int | str | None] | None = None
    """Makes substitutions in the query filter expression.

    Substitutions for the query expression are indicated by non-negative integers that are
    prefixed with the @ symbol. Each substitution in the given expression will be replaced by
    the element at the corresponding index (zero-based) in this list.
    """

    take: int | None = None
    """The maximum number of work items to return in the response."""

    continuation_token: str | None = None
    """A token which allows the user to resume a query at the next item in the matching results.

    When querying, a token will be returned if a query may be continued. To obtain the next page
    of results, pass the token to the service on a subsequent request.
    """

    order_by: WorkItemOrderBy | None = None
    """The field name to use for sorting the work items."""

    descending: bool | None = None
    """Whether to sort the work items in descending order."""

    return_count: bool | None = None
    """Whether to include the total count of matching work items in the response."""

    projection: List[WorkItemField] | None = None
    """
    Gets or sets the projection to be used when retrieving the work items. If not specified,
    all properties will be returned.
    """
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_resources_definition.py sha256=1525270c9efb19fb4f92dd164b806a44eac6369f89584c3c99cd72412ace560f bytes=3884 -->
## FILE: nisystemlink/clients/work_item/models/_resources_definition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_resources_definition.py`
- sha256: `1525270c9efb19fb4f92dd164b806a44eac6369f89584c3c99cd72412ace560f`
- bytes: 3884

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel


class ResourceSelectionDefinition(JsonModel):
    """Selection metadata associated with the resource."""

    id: str | None = None
    """The ID of the resource reserved for the work item."""

    target_location_id: str | None = None
    """The ID of the location where the resource is to be moved."""

    target_system_id: str | None = None
    """The ID of the system where the resource is to be moved."""

    target_parent_id: str | None = None
    """The ID of the parent to which the resource is to be connected."""


class SystemResourceSelectionDefinition(JsonModel):
    """Selection metadata associated with the system resource."""

    id: str | None = None
    """The ID of the system reserved for the work item."""

    target_location_id: str | None = None
    """The ID of the location where the system is to be moved."""


class ResourceDefinition(JsonModel):
    """Resource reserved for the work item."""

    selections: List[ResourceSelectionDefinition] | None = None
    """Resource selections for the work item."""

    filter: str | None = None
    """The filter used to select the resources for the work item."""


class SystemResourceDefinition(JsonModel):
    """System resource reserved for the work item."""

    selections: List[SystemResourceSelectionDefinition] | None = None
    """System resource selections for the work item."""

    filter: str | None = None
    """The filter used to select the systems for the work item."""


class ResourcesDefinition(JsonModel):
    """Resources reserved for the work item."""

    assets: ResourceDefinition | None = None
    """Asset reservations for the work item."""

    duts: ResourceDefinition | None = None
    """DUT reservations for the work item."""

    fixtures: ResourceDefinition | None = None
    """Fixture reservations for the work item."""

    systems: SystemResourceDefinition | None = None
    """System reservations for the work item."""


class TemplateResourceDefinition(JsonModel):
    """Resource reserved for the work item created from a template."""

    filter: str | None = None
    """The filter used to select the resources for the work item."""


class TemplateResourcesDefinition(JsonModel):
    """Resources reserved for the work item created from a template."""

    assets: TemplateResourceDefinition | None = None
    """Asset reservations for the work item."""

    duts: TemplateResourceDefinition | None = None
    """DUT reservations for the work item."""

    fixtures: TemplateResourceDefinition | None = None
    """Fixture reservations for the work item."""

    systems: TemplateResourceDefinition | None = None
    """System reservations for the work item."""


class ScheduleResourceDefinition(JsonModel):
    """Resource reserved for scheduling the work item."""

    selections: List[ResourceSelectionDefinition] | None = None
    """Resource selections for the work item."""


class ScheduleSystemResourceDefinition(JsonModel):
    """System resource reserved for scheduling the work item."""

    selections: List[SystemResourceSelectionDefinition] | None = None
    """System resource selections for the work item."""


class ScheduleResourcesDefinition(JsonModel):
    """Resources reserved for scheduling the work item."""

    assets: ScheduleResourceDefinition | None = None
    """Asset reservations for the work item."""

    duts: ScheduleResourceDefinition | None = None
    """DUT reservations for the work item."""

    fixtures: ScheduleResourceDefinition | None = None
    """Fixture reservations for the work item."""

    systems: ScheduleSystemResourceDefinition | None = None
    """System reservations for the work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_definition.py sha256=416feff4d86dad89a3abc6961bf40e5acccc3cf42b301379d8d449d93f3dc4d4 bytes=541 -->
## FILE: nisystemlink/clients/work_item/models/_schedule_definition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_schedule_definition.py`
- sha256: `416feff4d86dad89a3abc6961bf40e5acccc3cf42b301379d8d449d93f3dc4d4`
- bytes: 541

````python
from datetime import datetime

from nisystemlink.clients.core._uplink._json_model import JsonModel


class ScheduleDefinition(JsonModel):
    """Scheduling properties for the work item."""

    planned_start_date_time: datetime | None = None
    """The planned start date and time for the work item."""

    planned_end_date_time: datetime | None = None
    """The planned end date and time for the work item."""

    planned_duration_in_seconds: int | None = None
    """The planned duration of the work item in seconds."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_item_request.py sha256=8e279fbf466cc593e8d426652bdd0743004bb6a3d23a834829eb38d92bc7971e bytes=710 -->
## FILE: nisystemlink/clients/work_item/models/_schedule_work_item_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_schedule_work_item_request.py`
- sha256: `8e279fbf466cc593e8d426652bdd0743004bb6a3d23a834829eb38d92bc7971e`
- bytes: 710

````python
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._resources_definition import ScheduleResourcesDefinition
from ._schedule_definition import ScheduleDefinition


class ScheduleWorkItemRequest(JsonModel):
    """Represents the request body content for scheduling a single work item."""

    id: str
    """The ID of the work item to be scheduled."""

    assigned_to: str | None = None
    """The ID of the user to whom the work item is assigned."""

    schedule: ScheduleDefinition | None = None
    """Scheduling properties for the work item."""

    resources: ScheduleResourcesDefinition | None = None
    """Resources reserved for scheduling the work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_items_partial_success_response.py sha256=2167574dffc5bd4f4404d651f9a295f990086b10bc863ffaec00a384a574f2a5 bytes=729 -->
## FILE: nisystemlink/clients/work_item/models/_schedule_work_items_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_schedule_work_items_partial_success_response.py`
- sha256: `2167574dffc5bd4f4404d651f9a295f990086b10bc863ffaec00a384a574f2a5`
- bytes: 729

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._schedule_work_items_request import ScheduleWorkItemRequest
from ._work_item import WorkItem


class ScheduleWorkItemsPartialSuccessResponse(JsonModel):
    """Response for scheduling one or more work items."""

    scheduled_work_items: List[WorkItem] | None = None
    """List of successfully scheduled work items."""

    failed_work_items: List[ScheduleWorkItemRequest] | None = None
    """List of work item requests that failed to schedule."""

    error: ApiError | None = None
    """The error that occurred when scheduling the work items."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_items_request.py sha256=fae930b747edc0b83088fe873c1f0f7b3eab119afeb1be342287a072a6d2ac78 bytes=502 -->
## FILE: nisystemlink/clients/work_item/models/_schedule_work_items_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_schedule_work_items_request.py`
- sha256: `fae930b747edc0b83088fe873c1f0f7b3eab119afeb1be342287a072a6d2ac78`
- bytes: 502

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._schedule_work_item_request import ScheduleWorkItemRequest


class ScheduleWorkItemsRequest(JsonModel):
    """Represents the request body content for scheduling multiple work items."""

    work_items: List[ScheduleWorkItemRequest]
    """List of work items to be scheduled."""

    replace: bool | None = None
    """When true, existing array fields are replaced instead of merged."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_state.py sha256=33efd8e308f50d24385b22b1bde29616def2d1ed660a7036a419e0d8cca57a74 bytes=312 -->
## FILE: nisystemlink/clients/work_item/models/_state.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_state.py`
- sha256: `33efd8e308f50d24385b22b1bde29616def2d1ed660a7036a419e0d8cca57a74`
- bytes: 312

````python
from enum import Enum


class State(Enum):
    """The state of the work item."""

    NEW = "NEW"
    DEFINED = "DEFINED"
    REVIEWED = "REVIEWED"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    CLOSED = "CLOSED"
    CANCELED = "CANCELED"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_timeline_definition.py sha256=77abc2905d7d66e16921776d47a1e4c85adf83ab1c9cec7f2e1a4ed8f9936e38 bytes=772 -->
## FILE: nisystemlink/clients/work_item/models/_timeline_definition.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_timeline_definition.py`
- sha256: `77abc2905d7d66e16921776d47a1e4c85adf83ab1c9cec7f2e1a4ed8f9936e38`
- bytes: 772

````python
from datetime import datetime

from nisystemlink.clients.core._uplink._json_model import JsonModel


class TimelineDefinition(JsonModel):
    """Timeline properties for the work item."""

    earliest_start_date_time: datetime | None = None
    """The earliest start date and time for the work item."""

    due_date_time: datetime | None = None
    """The due date and time for the work item."""

    estimated_duration_in_seconds: int | None = None
    """The estimated duration of the work item in seconds."""


class TemplateTimelineDefinition(JsonModel):
    """Timeline properties for the work item created from a template."""

    estimated_duration_in_seconds: int | None = None
    """The estimated duration of the work item in seconds."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_request.py sha256=1b6442c7a5d2354888e849efce612812c5a41b00c46d10813044f917776f76b6 bytes=1938 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_item_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_item_request.py`
- sha256: `1b6442c7a5d2354888e849efce612812c5a41b00c46d10813044f917776f76b6`
- bytes: 1938

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import Dashboard
from ._execution_definition import ExecutionDefinition
from ._resources_definition import ResourcesDefinition
from ._timeline_definition import TimelineDefinition


class UpdateWorkItemRequest(JsonModel):
    """Represents the request body content for updating a single work item."""

    id: str
    """The ID of the work item to update."""

    name: str | None = None
    """The new name for the work item."""

    state: str | None = None
    """The new state of the work item."""

    description: str | None = None
    """The new description for the work item."""

    parent_id: str | None = None
    """The ID of the parent work item."""

    assigned_to: str | None = None
    """The user or group assigned to the work item."""

    requested_by: str | None = None
    """The user or group who requested the work item."""

    test_program: str | None = None
    """The test program associated with the work item."""

    part_number: str | None = None
    """The part number associated with the work item."""

    workspace: str | None = None
    """The workspace to which the work item belongs."""

    timeline: TimelineDefinition | None = None
    """Timeline properties for the work item."""

    resources: ResourcesDefinition | None = None
    """Resources reserved for the work item."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the work item."""

    properties: Dict[str, str] | None = None
    """Additional properties for the work item."""

    file_ids_from_template: List[str] | None = None
    """The array of file IDs associated with the work item template."""

    dashboard: Dashboard | None = None
    """The dashboard associated with the work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_template_request.py sha256=7447e3a5c6bfd315de035436abb4d977b2617001a2673785d842196ce28928fb bytes=2298 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_item_template_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_item_template_request.py`
- sha256: `7447e3a5c6bfd315de035436abb4d977b2617001a2673785d842196ce28928fb`
- bytes: 2298

````python
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import DashboardUrl
from ._execution_definition import ExecutionDefinition
from ._resources_definition import TemplateResourcesDefinition
from ._timeline_definition import TemplateTimelineDefinition


class UpdateWorkItemTemplateRequest(JsonModel):
    """Represents the request body content for updating a single work item template."""

    id: str
    """The ID of the work item template."""

    product_families: List[str] | None = None
    """The array of product families to which the work item template belongs."""

    part_numbers: List[str] | None = None
    """The array of part numbers of the products linked to the work item template."""

    name: str | None = None
    """The name of the work item template."""

    summary: str | None = None
    """The summary of the work item template."""

    description: str | None = None
    """The description of the work item created from this template."""

    template_group: str | None = None
    """The template group defined by the user."""

    test_program: str | None = None
    """The test program associated with the work item created from this template."""

    timeline: TemplateTimelineDefinition | None = None
    """Timeline properties for the work item created from this template."""

    resources: TemplateResourcesDefinition | None = None
    """Resources selection criteria for the work item created from this template."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the work item."""

    file_ids: List[str] | None = None
    """The array of file IDs associated with the work item template."""

    workspace: str | None = None
    """The workspace to which the work item template belongs."""

    properties: Dict[str, str] | None = None
    """Additional properties associated with the work item created from this template."""

    dashboard: DashboardUrl | None = None
    """The dashboard data related to the work item created from this template."""

    workflow_id: str | None = None
    """The ID of the workflow associated with the work item created from this template."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_templates_partial_success_response.py sha256=2e94abe082cb6ab32e5f39b692999e7498141e0e1b68d211829d5d4bce3e542f bytes=817 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_item_templates_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_item_templates_partial_success_response.py`
- sha256: `2e94abe082cb6ab32e5f39b692999e7498141e0e1b68d211829d5d4bce3e542f`
- bytes: 817

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._update_work_item_template_request import UpdateWorkItemTemplateRequest
from ._work_item_template import WorkItemTemplate


class UpdateWorkItemTemplatesPartialSuccessResponse(JsonModel):
    """Response for updating work item templates with partial success."""

    updated_work_item_templates: List[WorkItemTemplate]
    """List of successfully updated work item templates."""

    failed_work_item_templates: List[UpdateWorkItemTemplateRequest] | None = None
    """List of work item template requests that failed to update."""

    error: ApiError | None = None
    """The error that occurred when updating the work item templates."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_templates_request.py sha256=2c6139d86e38c95aefec3dbe75d1a98b0b136635a4fc7ba17e8738e59486fbe5 bytes=555 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_item_templates_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_item_templates_request.py`
- sha256: `2c6139d86e38c95aefec3dbe75d1a98b0b136635a4fc7ba17e8738e59486fbe5`
- bytes: 555

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._update_work_item_template_request import UpdateWorkItemTemplateRequest


class UpdateWorkItemTemplatesRequest(JsonModel):
    """Represents the request body content for updating multiple work item templates."""

    work_item_templates: List[UpdateWorkItemTemplateRequest]
    """List of work item templates to update."""

    replace: bool | None = None
    """When true, existing key-value pair fields are replaced instead of merged."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_items_partial_success_response.py sha256=bdb7ed31f0a80436757a45492ba067641f21f3fafcd934bef78ba8ab33e9b212 bytes=719 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_items_partial_success_response.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_items_partial_success_response.py`
- sha256: `bdb7ed31f0a80436757a45492ba067641f21f3fafcd934bef78ba8ab33e9b212`
- bytes: 719

````python
from typing import List

from nisystemlink.clients.core._api_error import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._update_work_item_request import UpdateWorkItemRequest
from ._work_item import WorkItem


class UpdateWorkItemsPartialSuccessResponse(JsonModel):
    """Response for updating work items with partial success."""

    updated_work_items: List[WorkItem] | None = None
    """List of successfully updated work items."""

    failed_work_items: List[UpdateWorkItemRequest] | None = None
    """List of work item requests that failed to update."""

    error: ApiError | None = None
    """The error that occurred when updating the work items."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_items_request.py sha256=9a92089f01b0de0839e9aa64d987cf40e55c8c41ea3bd3d70817bc8ca45fcc4f bytes=505 -->
## FILE: nisystemlink/clients/work_item/models/_update_work_items_request.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_update_work_items_request.py`
- sha256: `9a92089f01b0de0839e9aa64d987cf40e55c8c41ea3bd3d70817bc8ca45fcc4f`
- bytes: 505

````python
from typing import List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._update_work_item_request import UpdateWorkItemRequest


class UpdateWorkItemsRequest(JsonModel):
    """Represents the request body content for updating multiple work items."""

    work_items: List[UpdateWorkItemRequest]
    """List of work items to update."""

    replace: bool | None = None
    """When true, existing array and key-value pair fields are replaced instead of merged."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_work_item.py sha256=95da0134eb610e8ad2277bf2d5fff357c1eb3bda5df35207111ea1e535b72f08 bytes=3009 -->
## FILE: nisystemlink/clients/work_item/models/_work_item.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_work_item.py`
- sha256: `95da0134eb610e8ad2277bf2d5fff357c1eb3bda5df35207111ea1e535b72f08`
- bytes: 3009

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import DashboardUrl
from ._execution_definition import ExecutionDefinition
from ._execution_event import ExecutionEvent
from ._resources_definition import ResourcesDefinition
from ._schedule_definition import ScheduleDefinition
from ._state import State
from ._timeline_definition import TimelineDefinition


class WorkItem(JsonModel):
    """Contains information about a work item."""

    id: str | None = None
    """The ID of the work item."""

    template_id: str | None = None
    """The ID of the template used to create the work item."""

    name: str | None = None
    """The name of the work item."""

    type: str | None = None
    """The type of the work item."""

    state: State | None = None
    """The state of the work item."""

    substate: str | None = None
    """The substate of the work item, if any."""

    description: str | None = None
    """The description of the work item."""

    parent_id: str | None = None
    """The ID of the parent work item."""

    assigned_to: str | None = None
    """The user or group assigned to the work item."""

    requested_by: str | None = None
    """The user or group who requested the work item."""

    test_program: str | None = None
    """The test program associated with the work item."""

    part_number: str | None = None
    """The part number associated with the work item."""

    workspace: str | None = None
    """The workspace to which the work item belongs."""

    timeline: TimelineDefinition | None = None
    """Timeline properties for the work item."""

    schedule: ScheduleDefinition | None = None
    """Scheduling properties for the work item."""

    resources: ResourcesDefinition | None = None
    """Resources reserved for the work item."""

    created_by: str | None = None
    """The user who created the work item."""

    updated_by: str | None = None
    """The user who last updated the work item."""

    created_at: datetime | None = None
    """The date and time when the work item was created."""

    updated_at: datetime | None = None
    """The date and time when the work item was last updated."""

    properties: Dict[str, str] | None = None
    """Additional properties associated with the work item."""

    file_ids_from_template: List[str] | None = None
    """The list of file IDs inherited from the template."""

    dashboard: DashboardUrl | None = None
    """The dashboard data related to the work item."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the work item."""

    execution_history: List[ExecutionEvent] | None = None
    """The execution history of the work item."""

    workflow_id: str | None = None
    """The ID of the workflow associated with the work item."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_work_item_template.py sha256=6f917b44c603d2d2bf3c5806c4cdd4989210fa5da4c5f65945662e6828bfaee8 bytes=3005 -->
## FILE: nisystemlink/clients/work_item/models/_work_item_template.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/clients/work_item/models/_work_item_template.py`
- sha256: `6f917b44c603d2d2bf3c5806c4cdd4989210fa5da4c5f65945662e6828bfaee8`
- bytes: 3005

````python
from datetime import datetime
from typing import Dict, List

from nisystemlink.clients.core._uplink._json_model import JsonModel

from ._dashboard import Dashboard
from ._execution_definition import ExecutionDefinition
from ._resources_definition import TemplateResourcesDefinition
from ._timeline_definition import TemplateTimelineDefinition


class WorkItemTemplateBase(JsonModel):
    """Contains information about a work item template."""

    name: str | None = None
    """The name of the work item template."""

    template_group: str | None = None
    """The template group defined by the user."""

    type: str | None = None
    """The type of work item created from this template."""

    product_families: List[str] | None = None
    """The array of product families to which the work item template belongs."""

    part_numbers: List[str] | None = None
    """The array of part numbers of the products linked to the work item template."""

    summary: str | None = None
    """The summary of the work item template."""

    description: str | None = None
    """The description of the work item created from this template."""

    test_program: str | None = None
    """The test program associated with the work item created from this template."""

    timeline: TemplateTimelineDefinition | None = None
    """Timeline properties for the work item created from this template."""

    resources: TemplateResourcesDefinition | None = None
    """Resources selection criteria for the work item created from this template."""

    execution_actions: List[ExecutionDefinition] | None = None
    """The execution actions defined for the work item."""

    file_ids: List[str] | None = None
    """The array of file IDs associated with the work item template."""

    workspace: str | None = None
    """The workspace to which the work item template belongs."""

    properties: Dict[str, str] | None = None
    """Additional properties associated with the work item created from this template."""

    dashboard: Dashboard | None = None
    """The dashboard data related to the work item created from this template."""

    workflow_id: str | None = None
    """The ID of the workflow associated with the work item created from this template."""


class WorkItemTemplate(WorkItemTemplateBase):
    """Contains response information for work item template."""

    id: str | None = None
    """The ID of the work item template."""

    name: str | None = None
    """The name of the work item template."""

    created_by: str | None = None
    """The user who created the work item template."""

    updated_by: str | None = None
    """The user who last updated the work item template."""

    created_at: datetime | None = None
    """The date and time when the work item template was created."""

    updated_at: datetime | None = None
    """The date and time when the work item template was last updated."""
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=nisystemlink/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: nisystemlink/py.typed

- repository: `ni/nisystemlink-clients-python`
- source_path: `nisystemlink/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=poetry.lock sha256=87ecad232f1fbbd23da47b7f499323f370f6a3b6345490d3c606f36a92794789 bytes=145290 -->
## FILE: poetry.lock

- repository: `ni/nisystemlink-clients-python`
- source_path: `poetry.lock`
- sha256: `87ecad232f1fbbd23da47b7f499323f370f6a3b6345490d3c606f36a92794789`
- bytes: 145290

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "aenum"
version = "3.1.16"
description = "Advanced Enumerations (compatible with Python's stdlib Enum), NamedTuples, and NamedConstants"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "aenum-3.1.16-py2-none-any.whl", hash = "sha256:7810cbb6b4054b7654e5a7bafbe16e9ee1d25ef8e397be699f63f2f3a5800433"},
    {file = "aenum-3.1.16-py3-none-any.whl", hash = "sha256:9035092855a98e41b66e3d0998bd7b96280e85ceb3a04cc035636138a1943eaf"},
    {file = "aenum-3.1.16.tar.gz", hash = "sha256:bfaf9589bdb418ee3a986d85750c7318d9d2839c1b1a1d6fe8fc53ec201cf140"},
]

[[package]]
name = "annotated-types"
version = "0.7.0"
description = "Reusable constraint types to use with typing.Annotated"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53"},
    {file = "annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89"},
]

[[package]]
name = "anyio"
version = "4.11.0"
description = "High-level concurrency and networking framework on top of asyncio or Trio"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "anyio-4.11.0-py3-none-any.whl", hash = "sha256:0287e96f4d26d4149305414d4e3bc32f0dcd0862365a4bddea19d7a1ec38c4fc"},
    {file = "anyio-4.11.0.tar.gz", hash = "sha256:82a8d0b81e318cc5ce71a5f1f8b5c4e63619620b63141ef8c995fa0db95a57c4"},
]

[package.dependencies]
exceptiongroup = {version = ">=1.0.2", markers = "python_version < \"3.11\""}
idna = ">=2.8"
sniffio = ">=1.1"
typing_extensions = {version = ">=4.5", markers = "python_version < \"3.13\""}

[package.extras]
trio = ["trio (>=0.31.0)"]

[[package]]
name = "backoff"
version = "2.2.1"
description = "Function decoration for backoff and retry"
optional = false
python-versions = ">=3.7,<4.0"
groups = ["dev"]
files = [
    {file = "backoff-2.2.1-py3-none-any.whl", hash = "sha256:63579f9a0628e06278f7e47b7d7d5b6ce20dc65c5e96a6f3ca99a6adca0396e8"},
    {file = "backoff-2.2.1.tar.gz", hash = "sha256:03f829f5bb1923180821643f8753b0502c3b682293992485b0eef2807afa5cba"},
]

[[package]]
name = "black"
version = "26.3.1"
description = "The uncompromising code formatter."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "black-26.3.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:86a8b5035fce64f5dcd1b794cf8ec4d31fe458cf6ce3986a30deb434df82a1d2"},
    {file = "black-26.3.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:5602bdb96d52d2d0672f24f6ffe5218795736dd34807fd0fd55ccd6bf206168b"},
    {file = "black-26.3.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6c54a4a82e291a1fee5137371ab488866b7c86a3305af4026bdd4dc78642e1ac"},
    {file = "black-26.3.1-cp310-cp310-win_amd64.whl", hash = "sha256:6e131579c243c98f35bce64a7e08e87fb2d610544754675d4a0e73a070a5aa3a"},
    {file = "black-26.3.1-cp310-cp310-win_arm64.whl", hash = "sha256:5ed0ca58586c8d9a487352a96b15272b7fa55d139fc8496b519e78023a8dab0a"},
    {file = "black-26.3.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:28ef38aee69e4b12fda8dba75e21f9b4f979b490c8ac0baa7cb505369ac9e1ff"},
    {file = "black-26.3.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:bf9bf162ed91a26f1adba8efda0b573bc6924ec1408a52cc6f82cb73ec2b142c"},
    {file = "black-26.3.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:474c27574d6d7037c1bc875a81d9be0a9a4f9ee95e62800dab3cfaadbf75acd5"},
    {file = "black-26.3.1-cp311-cp311-win_amd64.whl", hash = "sha256:5e9d0d86df21f2e1677cc4bd090cd0e446278bcbbe49bf3659c308c3e402843e"},
    {file = "black-26.3.1-cp311-cp311-win_arm64.whl", hash = "sha256:9a5e9f45e5d5e1c5b5c29b3bd4265dcc90e8b92cf4534520896ed77f791f4da5"},
    {file = "black-26.3.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b5e6f89631eb88a7302d416594a32faeee9fb8fb848290da9d0a5f2903519fc1"},
    {file = "black-26.3.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:41cd2012d35b47d589cb8a16faf8a32ef7a336f56356babd9fcf70939ad1897f"},
    {file = "black-26.3.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f76ff19ec5297dd8e66eb64deda23631e642c9393ab592826fd4bdc97a4bce7"},
    {file = "black-26.3.1-cp312-cp312-win_amd64.whl", hash = "sha256:ddb113db38838eb9f043623ba274cfaf7d51d5b0c22ecb30afe58b1bb8322983"},
    {file = "black-26.3.1-cp312-cp312-win_arm64.whl", hash = "sha256:dfdd51fc3e64ea4f35873d1b3fb25326773d55d2329ff8449139ebaad7357efb"},
    {file = "black-26.3.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:855822d90f884905362f602880ed8b5df1b7e3ee7d0db2502d4388a954cc8c54"},
    {file = "black-26.3.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8a33d657f3276328ce00e4d37fe70361e1ec7614da5d7b6e78de5426cb56332f"},
    {file = "black-26.3.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f1cd08e99d2f9317292a311dfe578fd2a24b15dbce97792f9c4d752275c1fa56"},
    {file = "black-26.3.1-cp313-cp313-win_amd64.whl", hash = "sha256:c7e72339f841b5a237ff14f7d3880ddd0fc7f98a1199e8c4327f9a4f478c1839"},
    {file = "black-26.3.1-cp313-cp313-win_arm64.whl", hash = "sha256:afc622538b430aa4c8c853f7f63bc582b3b8030fd8c80b70fb5fa5b834e575c2"},
    {file = "black-26.3.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:2d6bfaf7fd0993b420bed691f20f9492d53ce9a2bcccea4b797d34e947318a78"},
    {file = "black-26.3.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:f89f2ab047c76a9c03f78d0d66ca519e389519902fa27e7a91117ef7611c0568"},
    {file = "black-26.3.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b07fc0dab849d24a80a29cfab8d8a19187d1c4685d8a5e6385a5ce323c1f015f"},
    {file = "black-26.3.1-cp314-cp314-win_amd64.whl", hash = "sha256:0126ae5b7c09957da2bdbd91a9ba1207453feada9e9fe51992848658c6c8e01c"},
    {file = "black-26.3.1-cp314-cp314-win_arm64.whl", hash = "sha256:92c0ec1f2cc149551a2b7b47efc32c866406b6891b0ee4625e95967c8f4acfb1"},
    {file = "black-26.3.1-py3-none-any.whl", hash = "sha256:2bd5aa94fc267d38bb21a70d7410a89f1a1d318841855f698746f8e7f51acd1b"},
    {file = "black-26.3.1.tar.gz", hash = "sha256:2c50f5063a9641c7eed7795014ba37b0f5fa227f3d408b968936e24bc0566b07"},
]

[package.dependencies]
click = ">=8.0.0"
mypy-extensions = ">=0.4.3"
packaging = ">=22.0"
pathspec = ">=1.0.0"
platformdirs = ">=2"
pytokens = ">=0.4.0,<0.5.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = {version = ">=4.0.1", markers = "python_version < \"3.11\""}

[package.extras]
colorama = ["colorama (>=0.4.3)"]
d = ["aiohttp (>=3.10)"]
jupyter = ["ipython (>=7.8.0)", "tokenize-rt (>=3.2.0)"]
uvloop = ["uvloop (>=0.15.2) ; sys_platform != \"win32\"", "winloop (>=0.5.0) ; sys_platform == \"win32\""]

[[package]]
name = "certifi"
version = "2025.10.5"
description = "Python package for providing Mozilla's CA Bundle."
optional = false
python-versions = ">=3.7"
groups = ["main", "dev"]
files = [
    {file = "certifi-2025.10.5-py3-none-any.whl", hash = "sha256:0f212c2744a9bb6de0c56639a6f68afe01ecd92d91f14ae897c4fe7bbeeef0de"},
    {file = "certifi-2025.10.5.tar.gz", hash = "sha256:47c09d31ccf2acf0be3f701ea53595ee7e0b8fa08801c6624be771df09ae7b43"},
]

[[package]]
name = "charset-normalizer"
version = "3.4.4"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
optional = false
python-versions = ">=3.7"
groups = ["main", "dev"]
files = [
    {file = "charset_normalizer-3.4.4-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:e824f1492727fa856dd6eda4f7cee25f8518a12f3c4a56a74e8095695089cf6d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4bd5d4137d500351a30687c2d3971758aac9a19208fc110ccb9d7188fbe709e8"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:027f6de494925c0ab2a55eab46ae5129951638a49a34d87f4c3eda90f696b4ad"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f820802628d2694cb7e56db99213f930856014862f3fd943d290ea8438d07ca8"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:798d75d81754988d2565bff1b97ba5a44411867c0cf32b77a7e8f8d84796b10d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9d1bb833febdff5c8927f922386db610b49db6e0d4f4ee29601d71e7c2694313"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:9cd98cdc06614a2f768d2b7286d66805f94c48cde050acdbbb7db2600ab3197e"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:077fbb858e903c73f6c9db43374fd213b0b6a778106bc7032446a8e8b5b38b93"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:244bfb999c71b35de57821b8ea746b24e863398194a4014e4c76adc2bbdfeff0"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:64b55f9dce520635f018f907ff1b0df1fdc31f2795a922fb49dd14fbcdf48c84"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:faa3a41b2b66b6e50f84ae4a68c64fcd0c44355741c6374813a800cd6695db9e"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:6515f3182dbe4ea06ced2d9e8666d97b46ef4c75e326b79bb624110f122551db"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:cc00f04ed596e9dc0da42ed17ac5e596c6ccba999ba6bd92b0e0aef2f170f2d6"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win32.whl", hash = "sha256:f34be2938726fc13801220747472850852fe6b1ea75869a048d6f896838c896f"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win_amd64.whl", hash = "sha256:a61900df84c667873b292c3de315a786dd8dac506704dea57bc957bd31e22c7d"},
    {file = "charset_normalizer-3.4.4-cp310-cp310-win_arm64.whl", hash = "sha256:cead0978fc57397645f12578bfd2d5ea9138ea0fac82b2f63f7f7c6877986a69"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:6e1fcf0720908f200cd21aa4e6750a48ff6ce4afe7ff5a79a90d5ed8a08296f8"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5f819d5fe9234f9f82d75bdfa9aef3a3d72c4d24a6e57aeaebba32a704553aa0"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:a59cb51917aa591b1c4e6a43c132f0cdc3c76dbad6155df4e28ee626cc77a0a3"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:8ef3c867360f88ac904fd3f5e1f902f13307af9052646963ee08ff4f131adafc"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d9e45d7faa48ee908174d8fe84854479ef838fc6a705c9315372eacbc2f02897"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:840c25fb618a231545cbab0564a799f101b63b9901f2569faecd6b222ac72381"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:ca5862d5b3928c4940729dacc329aa9102900382fea192fc5e52eb69d6093815"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d9c7f57c3d666a53421049053eaacdd14bbd0a528e2186fcb2e672effd053bb0"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:277e970e750505ed74c832b4bf75dac7476262ee2a013f5574dd49075879e161"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:31fd66405eaf47bb62e8cd575dc621c56c668f27d46a61d975a249930dd5e2a4"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:0d3d8f15c07f86e9ff82319b3d9ef6f4bf907608f53fe9d92b28ea9ae3d1fd89"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:9f7fcd74d410a36883701fafa2482a6af2ff5ba96b9a620e9e0721e28ead5569"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ebf3e58c7ec8a8bed6d66a75d7fb37b55e5015b03ceae72a8e7c74495551e224"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win32.whl", hash = "sha256:eecbc200c7fd5ddb9a7f16c7decb07b566c29fa2161a16cf67b8d068bd21690a"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win_amd64.whl", hash = "sha256:5ae497466c7901d54b639cf42d5b8c1b6a4fead55215500d2f486d34db48d016"},
    {file = "charset_normalizer-3.4.4-cp311-cp311-win_arm64.whl", hash = "sha256:65e2befcd84bc6f37095f5961e68a6f077bf44946771354a28ad434c2cce0ae1"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:0a98e6759f854bd25a58a73fa88833fba3b7c491169f86ce1180c948ab3fd394"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b5b290ccc2a263e8d185130284f8501e3e36c5e02750fc6b6bdeb2e9e96f1e25"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:74bb723680f9f7a6234dcf67aea57e708ec1fbdf5699fb91dfd6f511b0a320ef"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f1e34719c6ed0b92f418c7c780480b26b5d9c50349e9a9af7d76bf757530350d"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:2437418e20515acec67d86e12bf70056a33abdacb5cb1655042f6538d6b085a8"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:11d694519d7f29d6cd09f6ac70028dba10f92f6cdd059096db198c283794ac86"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:ac1c4a689edcc530fc9d9aa11f5774b9e2f33f9a0c6a57864e90908f5208d30a"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:21d142cc6c0ec30d2efee5068ca36c128a30b0f2c53c1c07bd78cb6bc1d3be5f"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:5dbe56a36425d26d6cfb40ce79c314a2e4dd6211d51d6d2191c00bed34f354cc"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:5bfbb1b9acf3334612667b61bd3002196fe2a1eb4dd74d247e0f2a4d50ec9bbf"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:d055ec1e26e441f6187acf818b73564e6e6282709e9bcb5b63f5b23068356a15"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:af2d8c67d8e573d6de5bc30cdb27e9b95e49115cd9baad5ddbd1a6207aaa82a9"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:780236ac706e66881f3b7f2f32dfe90507a09e67d1d454c762cf642e6e1586e0"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win32.whl", hash = "sha256:5833d2c39d8896e4e19b689ffc198f08ea58116bee26dea51e362ecc7cd3ed26"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win_amd64.whl", hash = "sha256:a79cfe37875f822425b89a82333404539ae63dbdddf97f84dcbc3d339aae9525"},
    {file = "charset_normalizer-3.4.4-cp312-cp312-win_arm64.whl", hash = "sha256:376bec83a63b8021bb5c8ea75e21c4ccb86e7e45ca4eb81146091b56599b80c3"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:e1f185f86a6f3403aa2420e815904c67b2f9ebc443f045edd0de921108345794"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b39f987ae8ccdf0d2642338faf2abb1862340facc796048b604ef14919e55ed"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:3162d5d8ce1bb98dd51af660f2121c55d0fa541b46dff7bb9b9f86ea1d87de72"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:81d5eb2a312700f4ecaa977a8235b634ce853200e828fbadf3a9c50bab278328"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5bd2293095d766545ec1a8f612559f6b40abc0eb18bb2f5d1171872d34036ede"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a8a8b89589086a25749f471e6a900d3f662d1d3b6e2e59dcecf787b1cc3a1894"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc7637e2f80d8530ee4a78e878bce464f70087ce73cf7c1caf142416923b98f1"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f8bf04158c6b607d747e93949aa60618b61312fe647a6369f88ce2ff16043490"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:554af85e960429cf30784dd47447d5125aaa3b99a6f0683589dbd27e2f45da44"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:74018750915ee7ad843a774364e13a3db91682f26142baddf775342c3f5b1133"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:c0463276121fdee9c49b98908b3a89c39be45d86d1dbaa22957e38f6321d4ce3"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:362d61fd13843997c1c446760ef36f240cf81d3ebf74ac62652aebaf7838561e"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9a26f18905b8dd5d685d6d07b0cdf98a79f3c7a918906af7cc143ea2e164c8bc"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win32.whl", hash = "sha256:9b35f4c90079ff2e2edc5b26c0c77925e5d2d255c42c74fdb70fb49b172726ac"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win_amd64.whl", hash = "sha256:b435cba5f4f750aa6c0a0d92c541fb79f69a387c91e61f1795227e4ed9cece14"},
    {file = "charset_normalizer-3.4.4-cp313-cp313-win_arm64.whl", hash = "sha256:542d2cee80be6f80247095cc36c418f7bddd14f4a6de45af91dfad36d817bba2"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:da3326d9e65ef63a817ecbcc0df6e94463713b754fe293eaa03da99befb9a5bd"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:8af65f14dc14a79b924524b1e7fffe304517b2bff5a58bf64f30b98bbc5079eb"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:74664978bb272435107de04e36db5a9735e78232b85b77d45cfb38f758efd33e"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:752944c7ffbfdd10c074dc58ec2d5a8a4cd9493b314d367c14d24c17684ddd14"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d1f13550535ad8cff21b8d757a3257963e951d96e20ec82ab44bc64aeb62a191"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ecaae4149d99b1c9e7b88bb03e3221956f68fd6d50be2ef061b2381b61d20838"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cb6254dc36b47a990e59e1068afacdcd02958bdcce30bb50cc1700a8b9d624a6"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:c8ae8a0f02f57a6e61203a31428fa1d677cbe50c93622b4149d5c0f319c1d19e"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:47cc91b2f4dd2833fddaedd2893006b0106129d4b94fdb6af1f4ce5a9965577c"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:82004af6c302b5d3ab2cfc4cc5f29db16123b1a8417f2e25f9066f91d4411090"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:2b7d8f6c26245217bd2ad053761201e9f9680f8ce52f0fcd8d0755aeae5b2152"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:799a7a5e4fb2d5898c60b640fd4981d6a25f1c11790935a44ce38c54e985f828"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:99ae2cffebb06e6c22bdc25801d7b30f503cc87dbd283479e7b606f70aff57ec"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win32.whl", hash = "sha256:f9d332f8c2a2fcbffe1378594431458ddbef721c1769d78e2cbc06280d8155f9"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win_amd64.whl", hash = "sha256:8a6562c3700cce886c5be75ade4a5db4214fda19fede41d9792d100288d8f94c"},
    {file = "charset_normalizer-3.4.4-cp314-cp314-win_arm64.whl", hash = "sha256:de00632ca48df9daf77a2c65a484531649261ec9f25489917f09e455cb09ddb2"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:ce8a0633f41a967713a59c4139d29110c07e826d131a316b50ce11b1d79b4f84"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:eaabd426fe94daf8fd157c32e571c85cb12e66692f15516a83a03264b08d06c3"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:c4ef880e27901b6cc782f1b95f82da9313c0eb95c3af699103088fa0ac3ce9ac"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:2aaba3b0819274cc41757a1da876f810a3e4d7b6eb25699253a4effef9e8e4af"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:778d2e08eda00f4256d7f672ca9fef386071c9202f5e4607920b86d7803387f2"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f155a433c2ec037d4e8df17d18922c3a0d9b3232a396690f17175d2946f0218d"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:a8bf8d0f749c5757af2142fe7903a9df1d2e8aa3841559b2bad34b08d0e2bcf3"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_aarch64.whl", hash = "sha256:194f08cbb32dc406d6e1aea671a68be0823673db2832b38405deba2fb0d88f63"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_armv7l.whl", hash = "sha256:6aee717dcfead04c6eb1ce3bd29ac1e22663cdea57f943c87d1eab9a025438d7"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_ppc64le.whl", hash = "sha256:cd4b7ca9984e5e7985c12bc60a6f173f3c958eae74f3ef6624bb6b26e2abbae4"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_riscv64.whl", hash = "sha256:b7cf1017d601aa35e6bb650b6ad28652c9cd78ee6caff19f3c28d03e1c80acbf"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_s390x.whl", hash = "sha256:e912091979546adf63357d7e2ccff9b44f026c075aeaf25a52d0e95ad2281074"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:5cb4d72eea50c8868f5288b7f7f33ed276118325c1dfd3957089f6b519e1382a"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-win32.whl", hash = "sha256:837c2ce8c5a65a2035be9b3569c684358dfbf109fd3b6969630a87535495ceaa"},
    {file = "charset_normalizer-3.4.4-cp38-cp38-win_amd64.whl", hash = "sha256:44c2a8734b333e0578090c4cd6b16f275e07aa6614ca8715e6c038e865e70576"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:a9768c477b9d7bd54bc0c86dbaebdec6f03306675526c9927c0e8a04e8f94af9"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1bee1e43c28aa63cb16e5c14e582580546b08e535299b8b6158a7c9c768a1f3d"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:fd44c878ea55ba351104cb93cc85e74916eb8fa440ca7903e57575e97394f608"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:0f04b14ffe5fdc8c4933862d8306109a2c51e0704acfa35d51598eb45a1e89fc"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:cd09d08005f958f370f539f186d10aec3377d55b9eeb0d796025d4886119d76e"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4fe7859a4e3e8457458e2ff592f15ccb02f3da787fcd31e0183879c3ad4692a1"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fa09f53c465e532f4d3db095e0c55b615f010ad81803d383195b6b5ca6cbf5f3"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:7fa17817dc5625de8a027cb8b26d9fefa3ea28c8253929b8d6649e705d2835b6"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:5947809c8a2417be3267efc979c47d76a079758166f7d43ef5ae8e9f92751f88"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:4902828217069c3c5c71094537a8e623f5d097858ac6ca8252f7b4d10b7560f1"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:7c308f7e26e4363d79df40ca5b2be1c6ba9f02bdbccfed5abddb7859a6ce72cf"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:2c9d3c380143a1fedbff95a312aa798578371eb29da42106a29019368a475318"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:cb01158d8b88ee68f15949894ccc6712278243d95f344770fa7593fa2d94410c"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win32.whl", hash = "sha256:2677acec1a2f8ef614c6888b5b4ae4060cc184174a938ed4e8ef690e15d3e505"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win_amd64.whl", hash = "sha256:f8e160feb2aed042cd657a72acc0b481212ed28b1b9a95c0cee1621b524e1966"},
    {file = "charset_normalizer-3.4.4-cp39-cp39-win_arm64.whl", hash = "sha256:b5d84d37db046c5ca74ee7bb47dd6cbc13f80665fdde3e8040bdd3fb015ecb50"},
    {file = "charset_normalizer-3.4.4-py3-none-any.whl", hash = "sha256:7a32c560861a02ff789ad905a2fe94e3f840803362c84fecf1851cb4cf3dc37f"},
    {file = "charset_normalizer-3.4.4.tar.gz", hash = "sha256:94537985111c35f28720e43603b8e7b43a6ecfb2ce1d3058bbe955b73404e21a"},
]

[[package]]
name = "click"
version = "8.3.0"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "click-8.3.0-py3-none-any.whl", hash = "sha256:9b9f285302c6e3064f4330c05f05b81945b2a39544279343e6e7c5f27a9baddc"},
    {file = "click-8.3.0.tar.gz", hash = "sha256:e7b8232224eba16f4ebe410c25ced9f7875cb5f3263ffc93cc3e8da705e229c4"},
]

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["dev"]
markers = "platform_system == \"Windows\" or sys_platform == \"win32\""
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "events"
version = "0.4"
description = "Bringing the elegance of C# EventHandler to Python"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "Events-0.4.tar.gz", hash = "sha256:01d9dd2a061f908d74a89fa5c8f07baa694f02a2a5974983663faaf7a97180f5"},
]

[[package]]
name = "exceptiongroup"
version = "1.3.0"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
groups = ["main", "dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "exceptiongroup-1.3.0-py3-none-any.whl", hash = "sha256:4d111e6e0c13d0644cad6ddaa7ed0261a0b36971f6d23e7ec9b4b9097da78a10"},
    {file = "exceptiongroup-1.3.0.tar.gz", hash = "sha256:b241f5885f560bc56a59ee63ca4c6a8bfa46ae4ad651af316d4e81817bb9fd88"},
]

[package.dependencies]
typing-extensions = {version = ">=4.6.0", markers = "python_version < \"3.13\""}

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "flake8"
version = "7.3.0"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "flake8-7.3.0-py2.py3-none-any.whl", hash = "sha256:b9696257b9ce8beb888cdbe31cf885c90d31928fe202be0889a7cdafad32f01e"},
    {file = "flake8-7.3.0.tar.gz", hash = "sha256:fe044858146b9fc69b551a4b490d69cf960fcb78ad1edcb84e7fbb1b4a8e3872"},
]

[package.dependencies]
mccabe = ">=0.7.0,<0.8.0"
pycodestyle = ">=2.14.0,<2.15.0"
pyflakes = ">=3.4.0,<3.5.0"

[[package]]
name = "flake8-docstrings"
version = "1.7.0"
description = "Extension for flake8 which uses pydocstyle to check docstrings"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "flake8_docstrings-1.7.0-py2.py3-none-any.whl", hash = "sha256:51f2344026da083fc084166a9353f5082b01f72901df422f74b4d953ae88ac75"},
    {file = "flake8_docstrings-1.7.0.tar.gz", hash = "sha256:4c8cc748dc16e6869728699e5d0d685da9a10b0ea718e090b1ba088e67a941af"},
]

[package.dependencies]
flake8 = ">=3"
pydocstyle = ">=2.1"

[[package]]
name = "flake8-import-order"
version = "0.19.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "flake8_import_order-0.19.2-py3-none-any.whl", hash = "sha256:2dfe60175e7195cf36d4c573861fd2e3258cd6650cbd7616da3c6b8193b29b7c"},
    {file = "flake8_import_order-0.19.2.tar.gz", hash = "sha256:133b3c55497631e4235074fc98a95078bba817832379f22a31f0ad2455bcb0b2"},
]

[package.dependencies]
pycodestyle = "*"
setuptools = "*"

[[package]]
name = "h11"
version = "0.16.0"
description = "A pure-Python, bring-your-own-I/O implementation of HTTP/1.1"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86"},
    {file = "h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1"},
]

[[package]]
name = "httpcore"
version = "1.0.9"
description = "A minimal low-level HTTP client."
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55"},
    {file = "httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8"},
]

[package.dependencies]
certifi = "*"
h11 = ">=0.16"

[package.extras]
asyncio = ["anyio (>=4.0,<5.0)"]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (==1.*)"]
trio = ["trio (>=0.22.0,<1.0)"]

[[package]]
name = "httpx"
version = "0.28.1"
description = "The next generation HTTP client."
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad"},
    {file = "httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc"},
]

[package.dependencies]
anyio = "*"
certifi = "*"
httpcore = "==1.*"
idna = "*"

[package.extras]
brotli = ["brotli ; platform_python_implementation == \"CPython\"", "brotlicffi ; platform_python_implementation != \"CPython\""]
cli = ["click (==8.*)", "pygments (==2.*)", "rich (>=10,<14)"]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (==1.*)"]
zstd = ["zstandard (>=0.18.0)"]

[[package]]
name = "idna"
version = "3.15"
description = "Internationalized Domain Names in Applications (IDNA)"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
files = [
    {file = "idna-3.15-py3-none-any.whl", hash = "sha256:048adeaf8c2d788c40fee287673ccaa74c24ffd8dcf09ffa555a2fbb59f10ac8"},
    {file = "idna-3.15.tar.gz", hash = "sha256:ca962446ea538f7092a95e057da437618e886f4d349216d2b1e294abfdb65fdc"},
]

[package.extras]
all = ["mypy (>=1.11.2)", "pytest (>=8.3.2)", "ruff (>=0.6.2)"]

[[package]]
name = "iniconfig"
version = "2.3.0"
description = "brain-dead simple config-ini parsing"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12"},
    {file = "iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730"},
]

[[package]]
name = "mccabe"
version = "0.7.0"
description = "McCabe checker, plugin for flake8"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "mccabe-0.7.0-py2.py3-none-any.whl", hash = "sha256:6c2d30ab6be0e4a46919781807b4f0d834ebdd6c6e3dca0bda5a15f863427b6e"},
    {file = "mccabe-0.7.0.tar.gz", hash = "sha256:348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325"},
]

[[package]]
name = "mypy"
version = "1.18.2"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "mypy-1.18.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:c1eab0cf6294dafe397c261a75f96dc2c31bffe3b944faa24db5def4e2b0f77c"},
    {file = "mypy-1.18.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:7a780ca61fc239e4865968ebc5240bb3bf610ef59ac398de9a7421b54e4a207e"},
    {file = "mypy-1.18.2-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:448acd386266989ef11662ce3c8011fd2a7b632e0ec7d61a98edd8e27472225b"},
    {file = "mypy-1.18.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f9e171c465ad3901dc652643ee4bffa8e9fef4d7d0eece23b428908c77a76a66"},
    {file = "mypy-1.18.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:592ec214750bc00741af1f80cbf96b5013d81486b7bb24cb052382c19e40b428"},
    {file = "mypy-1.18.2-cp310-cp310-win_amd64.whl", hash = "sha256:7fb95f97199ea11769ebe3638c29b550b5221e997c63b14ef93d2e971606ebed"},
    {file = "mypy-1.18.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:807d9315ab9d464125aa9fcf6d84fde6e1dc67da0b6f80e7405506b8ac72bc7f"},
    {file = "mypy-1.18.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:776bb00de1778caf4db739c6e83919c1d85a448f71979b6a0edd774ea8399341"},
    {file = "mypy-1.18.2-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1379451880512ffce14505493bd9fe469e0697543717298242574882cf8cdb8d"},
    {file = "mypy-1.18.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1331eb7fd110d60c24999893320967594ff84c38ac6d19e0a76c5fd809a84c86"},
    {file = "mypy-1.18.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3ca30b50a51e7ba93b00422e486cbb124f1c56a535e20eff7b2d6ab72b3b2e37"},
    {file = "mypy-1.18.2-cp311-cp311-win_amd64.whl", hash = "sha256:664dc726e67fa54e14536f6e1224bcfce1d9e5ac02426d2326e2bb4e081d1ce8"},
    {file = "mypy-1.18.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:33eca32dd124b29400c31d7cf784e795b050ace0e1f91b8dc035672725617e34"},
    {file = "mypy-1.18.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a3c47adf30d65e89b2dcd2fa32f3aeb5e94ca970d2c15fcb25e297871c8e4764"},
    {file = "mypy-1.18.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5d6c838e831a062f5f29d11c9057c6009f60cb294fea33a98422688181fe2893"},
    {file = "mypy-1.18.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01199871b6110a2ce984bde85acd481232d17413868c9807e95c1b0739a58914"},
    {file = "mypy-1.18.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a2afc0fa0b0e91b4599ddfe0f91e2c26c2b5a5ab263737e998d6817874c5f7c8"},
    {file = "mypy-1.18.2-cp312-cp312-win_amd64.whl", hash = "sha256:d8068d0afe682c7c4897c0f7ce84ea77f6de953262b12d07038f4d296d547074"},
    {file = "mypy-1.18.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:07b8b0f580ca6d289e69209ec9d3911b4a26e5abfde32228a288eb79df129fcc"},
    {file = "mypy-1.18.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:ed4482847168439651d3feee5833ccedbf6657e964572706a2adb1f7fa4dfe2e"},
    {file = "mypy-1.18.2-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c3ad2afadd1e9fea5cf99a45a822346971ede8685cc581ed9cd4d42eaf940986"},
    {file = "mypy-1.18.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a431a6f1ef14cf8c144c6b14793a23ec4eae3db28277c358136e79d7d062f62d"},
    {file = "mypy-1.18.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:7ab28cc197f1dd77a67e1c6f35cd1f8e8b73ed2217e4fc005f9e6a504e46e7ba"},
    {file = "mypy-1.18.2-cp313-cp313-win_amd64.whl", hash = "sha256:0e2785a84b34a72ba55fb5daf079a1003a34c05b22238da94fcae2bbe46f3544"},
    {file = "mypy-1.18.2-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:62f0e1e988ad41c2a110edde6c398383a889d95b36b3e60bcf155f5164c4fdce"},
    {file = "mypy-1.18.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:8795a039bab805ff0c1dfdb8cd3344642c2b99b8e439d057aba30850b8d3423d"},
    {file = "mypy-1.18.2-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6ca1e64b24a700ab5ce10133f7ccd956a04715463d30498e64ea8715236f9c9c"},
    {file = "mypy-1.18.2-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d924eef3795cc89fecf6bedc6ed32b33ac13e8321344f6ddbf8ee89f706c05cb"},
    {file = "mypy-1.18.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:20c02215a080e3a2be3aa50506c67242df1c151eaba0dcbc1e4e557922a26075"},
    {file = "mypy-1.18.2-cp314-cp314-win_amd64.whl", hash = "sha256:749b5f83198f1ca64345603118a6f01a4e99ad4bf9d103ddc5a3200cc4614adf"},
    {file = "mypy-1.18.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:25a9c8fb67b00599f839cf472713f54249a62efd53a54b565eb61956a7e3296b"},
    {file = "mypy-1.18.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c2b9c7e284ee20e7598d6f42e13ca40b4928e6957ed6813d1ab6348aa3f47133"},
    {file = "mypy-1.18.2-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d6985ed057513e344e43a26cc1cd815c7a94602fb6a3130a34798625bc2f07b6"},
    {file = "mypy-1.18.2-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:22f27105f1525ec024b5c630c0b9f36d5c1cc4d447d61fe51ff4bd60633f47ac"},
    {file = "mypy-1.18.2-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:030c52d0ea8144e721e49b1f68391e39553d7451f0c3f8a7565b59e19fcb608b"},
    {file = "mypy-1.18.2-cp39-cp39-win_amd64.whl", hash = "sha256:aa5e07ac1a60a253445797e42b8b2963c9675563a94f11291ab40718b016a7a0"},
    {file = "mypy-1.18.2-py3-none-any.whl", hash = "sha256:22a1748707dd62b58d2ae53562ffc4d7f8bcc727e8ac7cbc69c053ddc874d47e"},
    {file = "mypy-1.18.2.tar.gz", hash = "sha256:06a398102a5f203d7477b2923dda3634c36727fa5c237d8f859ef90c42a9924b"},
]

[package.dependencies]
mypy_extensions = ">=1.0.0"
pathspec = ">=0.9.0"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing_extensions = ">=4.6.0"

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
groups = ["dev"]
files = [
    {file = "mypy_extensions-1.1.0-py3-none-any.whl", hash = "sha256:1be4cccdb0f2482337c4743e60421de3a356cd97508abadd57d47403e94f5505"},
    {file = "mypy_extensions-1.1.0.tar.gz", hash = "sha256:52e68efc3284861e772bbcd66823fde5ae21fd2fdb51c62a211403730b916558"},
]

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main"]
markers = "python_version == \"3.10\""
files = [
    {file = "numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163"},
    {file = "numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83"},
    {file = "numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680"},
    {file = "numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289"},
    {file = "numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d"},
    {file = "numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42"},
    {file = "numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a"},
    {file = "numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1"},
    {file = "numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab"},
    {file = "numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47"},
    {file = "numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3"},
    {file = "numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87"},
    {file = "numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49"},
    {file = "numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de"},
    {file = "numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4"},
    {file = "numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d"},
    {file = "numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f"},
    {file = "numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868"},
    {file = "numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d"},
    {file = "numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd"},
    {file = "numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40"},
    {file = "numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f"},
    {file = "numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571"},
    {file = "numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1"},
    {file = "numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff"},
    {file = "numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543"},
    {file = "numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00"},
    {file = "numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd"},
]

[[package]]
name = "numpy"
version = "2.3.4"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main"]
markers = "python_version >= \"3.11\""
files = [
    {file = "numpy-2.3.4-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:e78aecd2800b32e8347ce49316d3eaf04aed849cd5b38e0af39f829a4e59f5eb"},
    {file = "numpy-2.3.4-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7fd09cc5d65bda1e79432859c40978010622112e9194e581e3415a3eccc7f43f"},
    {file = "numpy-2.3.4-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:1b219560ae2c1de48ead517d085bc2d05b9433f8e49d0955c82e8cd37bd7bf36"},
    {file = "numpy-2.3.4-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:bafa7d87d4c99752d07815ed7a2c0964f8ab311eb8168f41b910bd01d15b6032"},
    {file = "numpy-2.3.4-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36dc13af226aeab72b7abad501d370d606326a0029b9f435eacb3b8c94b8a8b7"},
    {file = "numpy-2.3.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a7b2f9a18b5ff9824a6af80de4f37f4ec3c2aab05ef08f51c77a093f5b89adda"},
    {file = "numpy-2.3.4-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:9984bd645a8db6ca15d850ff996856d8762c51a2239225288f08f9050ca240a0"},
    {file = "numpy-2.3.4-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:64c5825affc76942973a70acf438a8ab618dbd692b84cd5ec40a0a0509edc09a"},
    {file = "numpy-2.3.4-cp311-cp311-win32.whl", hash = "sha256:ed759bf7a70342f7817d88376eb7142fab9fef8320d6019ef87fae05a99874e1"},
    {file = "numpy-2.3.4-cp311-cp311-win_amd64.whl", hash = "sha256:faba246fb30ea2a526c2e9645f61612341de1a83fb1e0c5edf4ddda5a9c10996"},
    {file = "numpy-2.3.4-cp311-cp311-win_arm64.whl", hash = "sha256:4c01835e718bcebe80394fd0ac66c07cbb90147ebbdad3dcecd3f25de2ae7e2c"},
    {file = "numpy-2.3.4-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:ef1b5a3e808bc40827b5fa2c8196151a4c5abe110e1726949d7abddfe5c7ae11"},
    {file = "numpy-2.3.4-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:c2f91f496a87235c6aaf6d3f3d89b17dba64996abadccb289f48456cff931ca9"},
    {file = "numpy-2.3.4-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:f77e5b3d3da652b474cc80a14084927a5e86a5eccf54ca8ca5cbd697bf7f2667"},
    {file = "numpy-2.3.4-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:8ab1c5f5ee40d6e01cbe96de5863e39b215a4d24e7d007cad56c7184fdf4aeef"},
    {file = "numpy-2.3.4-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:77b84453f3adcb994ddbd0d1c5d11db2d6bda1a2b7fd5ac5bd4649d6f5dc682e"},
    {file = "numpy-2.3.4-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4121c5beb58a7f9e6dfdee612cb24f4df5cd4db6e8261d7f4d7450a997a65d6a"},
    {file = "numpy-2.3.4-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:65611ecbb00ac9846efe04db15cbe6186f562f6bb7e5e05f077e53a599225d16"},
    {file = "numpy-2.3.4-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:dabc42f9c6577bcc13001b8810d300fe814b4cfbe8a92c873f269484594f9786"},
    {file = "numpy-2.3.4-cp312-cp312-win32.whl", hash = "sha256:a49d797192a8d950ca59ee2d0337a4d804f713bb5c3c50e8db26d49666e351dc"},
    {file = "numpy-2.3.4-cp312-cp312-win_amd64.whl", hash = "sha256:985f1e46358f06c2a09921e8921e2c98168ed4ae12ccd6e5e87a4f1857923f32"},
    {file = "numpy-2.3.4-cp312-cp312-win_arm64.whl", hash = "sha256:4635239814149e06e2cb9db3dd584b2fa64316c96f10656983b8026a82e6e4db"},
    {file = "numpy-2.3.4-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:c090d4860032b857d94144d1a9976b8e36709e40386db289aaf6672de2a81966"},
    {file = "numpy-2.3.4-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:a13fc473b6db0be619e45f11f9e81260f7302f8d180c49a22b6e6120022596b3"},
    {file = "numpy-2.3.4-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:3634093d0b428e6c32c3a69b78e554f0cd20ee420dcad5a9f3b2a63762ce4197"},
    {file = "numpy-2.3.4-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:043885b4f7e6e232d7df4f51ffdef8c36320ee9d5f227b380ea636722c7ed12e"},
    {file = "numpy-2.3.4-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4ee6a571d1e4f0ea6d5f22d6e5fbd6ed1dc2b18542848e1e7301bd190500c9d7"},
    {file = "numpy-2.3.4-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fc8a63918b04b8571789688b2780ab2b4a33ab44bfe8ccea36d3eba51228c953"},
    {file = "numpy-2.3.4-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:40cc556d5abbc54aabe2b1ae287042d7bdb80c08edede19f0c0afb36ae586f37"},
    {file = "numpy-2.3.4-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ecb63014bb7f4ce653f8be7f1df8cbc6093a5a2811211770f6606cc92b5a78fd"},
    {file = "numpy-2.3.4-cp313-cp313-win32.whl", hash = "sha256:e8370eb6925bb8c1c4264fec52b0384b44f675f191df91cbe0140ec9f0955646"},
    {file = "numpy-2.3.4-cp313-cp313-win_amd64.whl", hash = "sha256:56209416e81a7893036eea03abcb91c130643eb14233b2515c90dcac963fe99d"},
    {file = "numpy-2.3.4-cp313-cp313-win_arm64.whl", hash = "sha256:a700a4031bc0fd6936e78a752eefb79092cecad2599ea9c8039c548bc097f9bc"},
    {file = "numpy-2.3.4-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:86966db35c4040fdca64f0816a1c1dd8dbd027d90fca5a57e00e1ca4cd41b879"},
    {file = "numpy-2.3.4-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:838f045478638b26c375ee96ea89464d38428c69170360b23a1a50fa4baa3562"},
    {file = "numpy-2.3.4-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:d7315ed1dab0286adca467377c8381cd748f3dc92235f22a7dfc42745644a96a"},
    {file = "numpy-2.3.4-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:84f01a4d18b2cc4ade1814a08e5f3c907b079c847051d720fad15ce37aa930b6"},
    {file = "numpy-2.3.4-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:817e719a868f0dacde4abdfc5c1910b301877970195db9ab6a5e2c4bd5b121f7"},
    {file = "numpy-2.3.4-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:85e071da78d92a214212cacea81c6da557cab307f2c34b5f85b628e94803f9c0"},
    {file = "numpy-2.3.4-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2ec646892819370cf3558f518797f16597b4e4669894a2ba712caccc9da53f1f"},
    {file = "numpy-2.3.4-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:035796aaaddfe2f9664b9a9372f089cfc88bd795a67bd1bfe15e6e770934cf64"},
    {file = "numpy-2.3.4-cp313-cp313t-win32.whl", hash = "sha256:fea80f4f4cf83b54c3a051f2f727870ee51e22f0248d3114b8e755d160b38cfb"},
    {file = "numpy-2.3.4-cp313-cp313t-win_amd64.whl", hash = "sha256:15eea9f306b98e0be91eb344a94c0e630689ef302e10c2ce5f7e11905c704f9c"},
    {file = "numpy-2.3.4-cp313-cp313t-win_arm64.whl", hash = "sha256:b6c231c9c2fadbae4011ca5e7e83e12dc4a5072f1a1d85a0a7b3ed754d145a40"},
    {file = "numpy-2.3.4-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:81c3e6d8c97295a7360d367f9f8553973651b76907988bb6066376bc2252f24e"},
    {file = "numpy-2.3.4-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:7c26b0b2bf58009ed1f38a641f3db4be8d960a417ca96d14e5b06df1506d41ff"},
    {file = "numpy-2.3.4-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:62b2198c438058a20b6704351b35a1d7db881812d8512d67a69c9de1f18ca05f"},
    {file = "numpy-2.3.4-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:9d729d60f8d53a7361707f4b68a9663c968882dd4f09e0d58c044c8bf5faee7b"},
    {file = "numpy-2.3.4-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:bd0c630cf256b0a7fd9d0a11c9413b42fef5101219ce6ed5a09624f5a65392c7"},
    {file = "numpy-2.3.4-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5e081bc082825f8b139f9e9fe42942cb4054524598aaeb177ff476cc76d09d2"},
    {file = "numpy-2.3.4-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:15fb27364ed84114438fff8aaf998c9e19adbeba08c0b75409f8c452a8692c52"},
    {file = "numpy-2.3.4-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:85d9fb2d8cd998c84d13a79a09cc0c1091648e848e4e6249b0ccd7f6b487fa26"},
    {file = "numpy-2.3.4-cp314-cp314-win32.whl", hash = "sha256:e73d63fd04e3a9d6bc187f5455d81abfad05660b212c8804bf3b407e984cd2bc"},
    {file = "numpy-2.3.4-cp314-cp314-win_amd64.whl", hash = "sha256:3da3491cee49cf16157e70f607c03a217ea6647b1cea4819c4f48e53d49139b9"},
    {file = "numpy-2.3.4-cp314-cp314-win_arm64.whl", hash = "sha256:6d9cd732068e8288dbe2717177320723ccec4fb064123f0caf9bbd90ab5be868"},
    {file = "numpy-2.3.4-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:22758999b256b595cf0b1d102b133bb61866ba5ceecf15f759623b64c020c9ec"},
    {file = "numpy-2.3.4-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:9cb177bc55b010b19798dc5497d540dea67fd13a8d9e882b2dae71de0cf09eb3"},
    {file = "numpy-2.3.4-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:0f2bcc76f1e05e5ab58893407c63d90b2029908fa41f9f1cc51eecce936c3365"},
    {file = "numpy-2.3.4-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:8dc20bde86802df2ed8397a08d793da0ad7a5fd4ea3ac85d757bf5dd4ad7c252"},
    {file = "numpy-2.3.4-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5e199c087e2aa71c8f9ce1cb7a8e10677dc12457e7cc1be4798632da37c3e86e"},
    {file = "numpy-2.3.4-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:85597b2d25ddf655495e2363fe044b0ae999b75bc4d630dc0d886484b03a5eb0"},
    {file = "numpy-2.3.4-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:04a69abe45b49c5955923cf2c407843d1c85013b424ae8a560bba16c92fe44a0"},
    {file = "numpy-2.3.4-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e1708fac43ef8b419c975926ce1eaf793b0c13b7356cfab6ab0dc34c0a02ac0f"},
    {file = "numpy-2.3.4-cp314-cp314t-win32.whl", hash = "sha256:863e3b5f4d9915aaf1b8ec79ae560ad21f0b8d5e3adc31e73126491bb86dee1d"},
    {file = "numpy-2.3.4-cp314-cp314t-win_amd64.whl", hash = "sha256:962064de37b9aef801d33bc579690f8bfe6c5e70e29b61783f60bcba838a14d6"},
    {file = "numpy-2.3.4-cp314-cp314t-win_arm64.whl", hash = "sha256:8b5a9a39c45d852b62693d9b3f3e0fe052541f804296ff401a72a1b60edafb29"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:6e274603039f924c0fe5cb73438fa9246699c78a6df1bd3decef9ae592ae1c05"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:d149aee5c72176d9ddbc6803aef9c0f6d2ceeea7626574fc68518da5476fa346"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:6d34ed9db9e6395bb6cd33286035f73a59b058169733a9db9f85e650b88df37e"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:fdebe771ca06bb8d6abce84e51dca9f7921fe6ad34a0c914541b063e9a68928b"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:957e92defe6c08211eb77902253b14fe5b480ebc5112bc741fd5e9cd0608f847"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:13b9062e4f5c7ee5c7e5be96f29ba71bc5a37fed3d1d77c37390ae00724d296d"},
    {file = "numpy-2.3.4-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:81b3a59793523e552c4a96109dde028aa4448ae06ccac5a76ff6532a85558a7f"},
    {file = "numpy-2.3.4.tar.gz", hash = "sha256:a7d018bfedb375a8d979ac758b120ba846a7fe764911a64465fd87b8729f4a6a"},
]

[[package]]
name = "packaging"
version = "25.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484"},
    {file = "packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f"},
]

[[package]]
name = "pandas"
version = "2.3.3"
description = "Powerful data structures for data analysis, time series, and statistics"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pandas-2.3.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:376c6446ae31770764215a6c937f72d917f214b43560603cd60da6408f183b6c"},
    {file = "pandas-2.3.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e19d192383eab2f4ceb30b412b22ea30690c9e618f78870357ae1d682912015a"},
    {file = "pandas-2.3.3-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5caf26f64126b6c7aec964f74266f435afef1c1b13da3b0636c7518a1fa3e2b1"},
    {file = "pandas-2.3.3-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dd7478f1463441ae4ca7308a70e90b33470fa593429f9d4c578dd00d1fa78838"},
    {file = "pandas-2.3.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:4793891684806ae50d1288c9bae9330293ab4e083ccd1c5e383c34549c6e4250"},
    {file = "pandas-2.3.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:28083c648d9a99a5dd035ec125d42439c6c1c525098c58af0fc38dd1a7a1b3d4"},
    {file = "pandas-2.3.3-cp310-cp310-win_amd64.whl", hash = "sha256:503cf027cf9940d2ceaa1a93cfb5f8c8c7e6e90720a2850378f0b3f3b1e06826"},
    {file = "pandas-2.3.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:602b8615ebcc4a0c1751e71840428ddebeb142ec02c786e8ad6b1ce3c8dec523"},
    {file = "pandas-2.3.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8fe25fc7b623b0ef6b5009149627e34d2a4657e880948ec3c840e9402e5c1b45"},
    {file = "pandas-2.3.3-cp311-cp311-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b468d3dad6ff947df92dcb32ede5b7bd41a9b3cceef0a30ed925f6d01fb8fa66"},
    {file = "pandas-2.3.3-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b98560e98cb334799c0b07ca7967ac361a47326e9b4e5a7dfb5ab2b1c9d35a1b"},
    {file = "pandas-2.3.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37b5848ba49824e5c30bedb9c830ab9b7751fd049bc7914533e01c65f79791"},
    {file = "pandas-2.3.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:db4301b2d1f926ae677a751eb2bd0e8c5f5319c9cb3f88b0becbbb0b07b34151"},
    {file = "pandas-2.3.3-cp311-cp311-win_amd64.whl", hash = "sha256:f086f6fe114e19d92014a1966f43a3e62285109afe874f067f5abbdcbb10e59c"},
    {file = "pandas-2.3.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6d21f6d74eb1725c2efaa71a2bfc661a0689579b58e9c0ca58a739ff0b002b53"},
    {file = "pandas-2.3.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:3fd2f887589c7aa868e02632612ba39acb0b8948faf5cc58f0850e165bd46f35"},
    {file = "pandas-2.3.3-cp312-cp312-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ecaf1e12bdc03c86ad4a7ea848d66c685cb6851d807a26aa245ca3d2017a1908"},
    {file = "pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b3d11d2fda7eb164ef27ffc14b4fcab16a80e1ce67e9f57e19ec0afaf715ba89"},
    {file = "pandas-2.3.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a68e15f780eddf2b07d242e17a04aa187a7ee12b40b930bfdd78070556550e98"},
    {file = "pandas-2.3.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:371a4ab48e950033bcf52b6527eccb564f52dc826c02afd9a1bc0ab731bba084"},
    {file = "pandas-2.3.3-cp312-cp312-win_amd64.whl", hash = "sha256:a16dcec078a01eeef8ee61bf64074b4e524a2a3f4b3be9326420cabe59c4778b"},
    {file = "pandas-2.3.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:56851a737e3470de7fa88e6131f41281ed440d29a9268dcbf0002da5ac366713"},
    {file = "pandas-2.3.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:bdcd9d1167f4885211e401b3036c0c8d9e274eee67ea8d0758a256d60704cfe8"},
    {file = "pandas-2.3.3-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e32e7cc9af0f1cc15548288a51a3b681cc2a219faa838e995f7dc53dbab1062d"},
    {file = "pandas-2.3.3-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:318d77e0e42a628c04dc56bcef4b40de67918f7041c2b061af1da41dcff670ac"},
    {file = "pandas-2.3.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:4e0a175408804d566144e170d0476b15d78458795bb18f1304fb94160cabf40c"},
    {file = "pandas-2.3.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:93c2d9ab0fc11822b5eece72ec9587e172f63cff87c00b062f6e37448ced4493"},
    {file = "pandas-2.3.3-cp313-cp313-win_amd64.whl", hash = "sha256:f8bfc0e12dc78f777f323f55c58649591b2cd0c43534e8355c51d3fede5f4dee"},
    {file = "pandas-2.3.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:75ea25f9529fdec2d2e93a42c523962261e567d250b0013b16210e1d40d7c2e5"},
    {file = "pandas-2.3.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:74ecdf1d301e812db96a465a525952f4dde225fdb6d8e5a521d47e1f42041e21"},
    {file = "pandas-2.3.3-cp313-cp313t-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6435cb949cb34ec11cc9860246ccb2fdc9ecd742c12d3304989017d53f039a78"},
    {file = "pandas-2.3.3-cp313-cp313t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:900f47d8f20860de523a1ac881c4c36d65efcb2eb850e6948140fa781736e110"},
    {file = "pandas-2.3.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:a45c765238e2ed7d7c608fc5bc4a6f88b642f2f01e70c0c23d2224dd21829d86"},
    {file = "pandas-2.3.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:c4fc4c21971a1a9f4bdb4c73978c7f7256caa3e62b323f70d6cb80db583350bc"},
    {file = "pandas-2.3.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:ee15f284898e7b246df8087fc82b87b01686f98ee67d85a17b7ab44143a3a9a0"},
    {file = "pandas-2.3.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1611aedd912e1ff81ff41c745822980c49ce4a7907537be8692c8dbc31924593"},
    {file = "pandas-2.3.3-cp314-cp314-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d2cefc361461662ac48810cb14365a365ce864afe85ef1f447ff5a1e99ea81c"},
    {file = "pandas-2.3.3-cp314-cp314-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ee67acbbf05014ea6c763beb097e03cd629961c8a632075eeb34247120abcb4b"},
    {file = "pandas-2.3.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:c46467899aaa4da076d5abc11084634e2d197e9460643dd455ac3db5856b24d6"},
    {file = "pandas-2.3.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:6253c72c6a1d990a410bc7de641d34053364ef8bcd3126f7e7450125887dffe3"},
    {file = "pandas-2.3.3-cp314-cp314-win_amd64.whl", hash = "sha256:1b07204a219b3b7350abaae088f451860223a52cfb8a6c53358e7948735158e5"},
    {file = "pandas-2.3.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:2462b1a365b6109d275250baaae7b760fd25c726aaca0054649286bcfbb3e8ec"},
    {file = "pandas-2.3.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:0242fe9a49aa8b4d78a4fa03acb397a58833ef6199e9aa40a95f027bb3a1b6e7"},
    {file = "pandas-2.3.3-cp314-cp314t-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a21d830e78df0a515db2b3d2f5570610f5e6bd2e27749770e8bb7b524b89b450"},
    {file = "pandas-2.3.3-cp314-cp314t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2e3ebdb170b5ef78f19bfb71b0dc5dc58775032361fa188e814959b74d726dd5"},
    {file = "pandas-2.3.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d051c0e065b94b7a3cea50eb1ec32e912cd96dba41647eb24104b6c6c14c5788"},
    {file = "pandas-2.3.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:3869faf4bd07b3b66a9f462417d0ca3a9df29a9f6abd5d0d0dbab15dac7abe87"},
    {file = "pandas-2.3.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:c503ba5216814e295f40711470446bc3fd00f0faea8a086cbc688808e26f92a2"},
    {file = "pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a637c5cdfa04b6d6e2ecedcb81fc52ffb0fd78ce2ebccc9ea964df9f658de8c8"},
    {file = "pandas-2.3.3-cp39-cp39-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:854d00d556406bffe66a4c0802f334c9ad5a96b4f1f868adf036a21b11ef13ff"},
    {file = "pandas-2.3.3-cp39-cp39-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bf1f8a81d04ca90e32a0aceb819d34dbd378a98bf923b6398b9a3ec0bf44de29"},
    {file = "pandas-2.3.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:23ebd657a4d38268c7dfbdf089fbc31ea709d82e4923c5ffd4fbd5747133ce73"},
    {file = "pandas-2.3.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:5554c929ccc317d41a5e3d1234f3be588248e61f08a74dd17c9eabb535777dc9"},
    {file = "pandas-2.3.3-cp39-cp39-win_amd64.whl", hash = "sha256:d3e28b3e83862ccf4d85ff19cf8c20b2ae7e503881711ff2d534dc8f761131aa"},
    {file = "pandas-2.3.3.tar.gz", hash = "sha256:e05e1af93b977f7eafa636d043f9f94c7ee3ac81af99c13508215942e64c993b"},
]

[package.dependencies]
numpy = [
    {version = ">=1.22.4", markers = "python_version < \"3.11\""},
    {version = ">=1.23.2", markers = "python_version == \"3.11\""},
    {version = ">=1.26.0", markers = "python_version >= \"3.12\""},
]
python-dateutil = ">=2.8.2"
pytz = ">=2020.1"
tzdata = ">=2022.7"

[package.extras]
all = ["PyQt5 (>=5.15.9)", "SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "adbc-driver-sqlite (>=0.8.0)", "beautifulsoup4 (>=4.11.2)", "bottleneck (>=1.3.6)", "dataframe-api-compat (>=0.1.7)", "fastparquet (>=2022.12.0)", "fsspec (>=2022.11.0)", "gcsfs (>=2022.11.0)", "html5lib (>=1.1)", "hypothesis (>=6.46.1)", "jinja2 (>=3.1.2)", "lxml (>=4.9.2)", "matplotlib (>=3.6.3)", "numba (>=0.56.4)", "numexpr (>=2.8.4)", "odfpy (>=1.4.1)", "openpyxl (>=3.1.0)", "pandas-gbq (>=0.19.0)", "psycopg2 (>=2.9.6)", "pyarrow (>=10.0.1)", "pymysql (>=1.0.2)", "pyreadstat (>=1.2.0)", "pytest (>=7.3.2)", "pytest-xdist (>=2.2.0)", "python-calamine (>=0.1.7)", "pyxlsb (>=1.0.10)", "qtpy (>=2.3.0)", "s3fs (>=2022.11.0)", "scipy (>=1.10.0)", "tables (>=3.8.0)", "tabulate (>=0.9.0)", "xarray (>=2022.12.0)", "xlrd (>=2.0.1)", "xlsxwriter (>=3.0.5)", "zstandard (>=0.19.0)"]
aws = ["s3fs (>=2022.11.0)"]
clipboard = ["PyQt5 (>=5.15.9)", "qtpy (>=2.3.0)"]
compression = ["zstandard (>=0.19.0)"]
computation = ["scipy (>=1.10.0)", "xarray (>=2022.12.0)"]
consortium-standard = ["dataframe-api-compat (>=0.1.7)"]
excel = ["odfpy (>=1.4.1)", "openpyxl (>=3.1.0)", "python-calamine (>=0.1.7)", "pyxlsb (>=1.0.10)", "xlrd (>=2.0.1)", "xlsxwriter (>=3.0.5)"]
feather = ["pyarrow (>=10.0.1)"]
fss = ["fsspec (>=2022.11.0)"]
gcp = ["gcsfs (>=2022.11.0)", "pandas-gbq (>=0.19.0)"]
hdf5 = ["tables (>=3.8.0)"]
html = ["beautifulsoup4 (>=4.11.2)", "html5lib (>=1.1)", "lxml (>=4.9.2)"]
mysql = ["SQLAlchemy (>=2.0.0)", "pymysql (>=1.0.2)"]
output-formatting = ["jinja2 (>=3.1.2)", "tabulate (>=0.9.0)"]
parquet = ["pyarrow (>=10.0.1)"]
performance = ["bottleneck (>=1.3.6)", "numba (>=0.56.4)", "numexpr (>=2.8.4)"]
plot = ["matplotlib (>=3.6.3)"]
postgresql = ["SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "psycopg2 (>=2.9.6)"]
pyarrow = ["pyarrow (>=10.0.1)"]
spss = ["pyreadstat (>=1.2.0)"]
sql-other = ["SQLAlchemy (>=2.0.0)", "adbc-driver-postgresql (>=0.8.0)", "adbc-driver-sqlite (>=0.8.0)"]
test = ["hypothesis (>=6.46.1)", "pytest (>=7.3.2)", "pytest-xdist (>=2.2.0)"]
xml = ["lxml (>=4.9.2)"]

[[package]]
name = "pastel"
version = "0.2.1"
description = "Bring colors to your terminal."
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
groups = ["dev"]
files = [
    {file = "pastel-0.2.1-py2.py3-none-any.whl", hash = "sha256:4349225fcdf6c2bb34d483e523475de5bb04a5c10ef711263452cb37d7dd4364"},
    {file = "pastel-0.2.1.tar.gz", hash = "sha256:e6581ac04e973cac858828c6202c1e1e81fee1dc7de7683f3e1ffe0bfd8a573d"},
]

[[package]]
name = "pathspec"
version = "1.0.4"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pathspec-1.0.4-py3-none-any.whl", hash = "sha256:fb6ae2fd4e7c921a165808a552060e722767cfa526f99ca5156ed2ce45a5c723"},
    {file = "pathspec-1.0.4.tar.gz", hash = "sha256:0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645"},
]

[package.extras]
hyperscan = ["hyperscan (>=0.7)"]
optional = ["typing-extensions (>=4)"]
re2 = ["google-re2 (>=1.1)"]
tests = ["pytest (>=9)", "typing-extensions (>=4.15)"]

[[package]]
name = "platformdirs"
version = "4.5.0"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "platformdirs-4.5.0-py3-none-any.whl", hash = "sha256:e578a81bb873cbb89a41fcc904c7ef523cc18284b7e3b3ccf06aca1403b7ebd3"},
    {file = "platformdirs-4.5.0.tar.gz", hash = "sha256:70ddccdd7c99fc5942e9fc25636a8b34d04c24b335100223152c2803e4063312"},
]

[package.extras]
docs = ["furo (>=2025.9.25)", "proselint (>=0.14)", "sphinx (>=8.2.3)", "sphinx-autodoc-typehints (>=3.2)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)"]
type = ["mypy (>=1.18.2)"]

[[package]]
name = "pluggy"
version = "1.6.0"
description = "plugin and hook calling mechanisms for python"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746"},
    {file = "pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["coverage", "pytest", "pytest-benchmark"]

[[package]]
name = "poethepoet"
version = "0.16.5"
description = "A task runner that works well with poetry."
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "poethepoet-0.16.5-py3-none-any.whl", hash = "sha256:493d5d47b4cb0894dde6a69d14129ba39ef3f124fabda1f83ebb39bbf737a40e"},
    {file = "poethepoet-0.16.5.tar.gz", hash = "sha256:3c958792ce488661ba09df67ba832a1b3141aa640236505ee60c23f4b1db4dbc"},
]

[package.dependencies]
pastel = ">=0.2.1,<0.3.0"
tomli = ">=1.2.2"

[package.extras]
poetry-plugin = ["poetry (>=1.0,<2.0)"]

[[package]]
name = "pyarrow"
version = "24.0.0"
description = "Python library for Apache Arrow"
optional = true
python-versions = ">=3.10"
groups = ["main"]
markers = "extra == \"pyarrow\""
files = [
    {file = "pyarrow-24.0.0-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:7c2b98645d576a0b9616892ead22b64a83a5f043c5e2ca15ebcefcb5b70c80cb"},
    {file = "pyarrow-24.0.0-cp310-cp310-macosx_12_0_x86_64.whl", hash = "sha256:644a246325b8c69c595ad1dd4b463eba4b0cdb731370e4a86137d433208d6147"},
    {file = "pyarrow-24.0.0-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:3a577bd840ca83f646f0a625dbc571dba7044c43c2d1503afc378b570954345c"},
    {file = "pyarrow-24.0.0-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:e3268e43984d0b1a185c89b4cfff282a7ead12fc93f56cfd7088bdbcbe727041"},
    {file = "pyarrow-24.0.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:2392d954fcb920f42d230284b677605e4e2fbb11f2821e823e642abd67fbb491"},
    {file = "pyarrow-24.0.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:bec9373df11544592b0ba7ec2af0e35059e5f0e7647c6183a854dedd193298f1"},
    {file = "pyarrow-24.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:c42ab9439498270139cc63e18847a02afe5c8b3ed9c931266533cfe378bd3591"},
    {file = "pyarrow-24.0.0-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:b0e131f880cda8d04e076cee175a46fc0e8bc8b65c99c6c09dff6669335fde74"},
    {file = "pyarrow-24.0.0-cp311-cp311-macosx_12_0_x86_64.whl", hash = "sha256:1b2fe7f9a5566401a0ef2571f197eb92358925c1f0c8dba305d6e43ea0871bb3"},
    {file = "pyarrow-24.0.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:0b3537c00fb8d384f15ac1e79b6eb6db04a16514c8c1d22e59a9b95c8ba42868"},
    {file = "pyarrow-24.0.0-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:14e31a3c9e35f1ab6356c6378f6f72830e6d2d5f1791df3774a7b097d18a6a1e"},
    {file = "pyarrow-24.0.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:b7d9a514e73bc42711e6a35aaccf3587c520024fe0a25d830a1a8a27c15f4f57"},
    {file = "pyarrow-24.0.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:b196eb3f931862af3fa84c2a253514d859c08e0d8fe020e07be12e75a5a9780c"},
    {file = "pyarrow-24.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:35405aecb474e683fb36af650618fd5340ee5471fc65a21b36076a18bbc6c981"},
    {file = "pyarrow-24.0.0-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:6233c9ed9ab9d1db47de57d9753256d9dcffbf42db341576099f0fd9f6bf4810"},
    {file = "pyarrow-24.0.0-cp312-cp312-macosx_12_0_x86_64.whl", hash = "sha256:f7616236ec1bc2b15bfdec22a71ab38851c86f8f05ff64f379e1278cf20c634a"},
    {file = "pyarrow-24.0.0-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:1617043b99bd33e5318ae18eb2919af09c71322ef1ca46566cdafc6e6712fb66"},
    {file = "pyarrow-24.0.0-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:6165461f55ef6314f026de6638d661188e3455d3ec49834556a0ebbdbace18bb"},
    {file = "pyarrow-24.0.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3b13dedfe76a0ad2d1d859b0811b53827a4e9d93a0bcb05cf59333ab4980cc7e"},
    {file = "pyarrow-24.0.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:25ea65d868eb04015cd18e6df2fbe98f07e5bda2abefabcb88fce39a947716f6"},
    {file = "pyarrow-24.0.0-cp312-cp312-win_amd64.whl", hash = "sha256:295f0a7f2e242dabd513737cf076007dc5b2d59237e3eca37b05c0c6446f3826"},
    {file = "pyarrow-24.0.0-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:02b001b3ed4723caa44f6cd1af2d5c86aa2cf9971dacc2ffa55b21237713dfba"},
    {file = "pyarrow-24.0.0-cp313-cp313-macosx_12_0_x86_64.whl", hash = "sha256:04920d6a71aabd08a0417709efce97d45ea8e6fb733d9ca9ecffb13c67839f68"},
    {file = "pyarrow-24.0.0-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:a964266397740257f16f7bb2e4f08a0c81454004beab8ff59dd531b73610e9f2"},
    {file = "pyarrow-24.0.0-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:6f066b179d68c413374294bc1735f68475457c933258df594443bb9d88ddc2a0"},
    {file = "pyarrow-24.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:1183baeb14c5f587b1ec52831e665718ce632caab84b7cd6b85fd44f96114495"},
    {file = "pyarrow-24.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:806f24b4085453c197a5078218d1ee08783ebbba271badd153d1ae22a3ee804f"},
    {file = "pyarrow-24.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:e4505fc6583f7b05ab854934896bcac8253b04ac1171a77dfb73efef92076d91"},
    {file = "pyarrow-24.0.0-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:1a4e45017efbf115032e4475ee876d525e0e36c742214fbe405332480ecd6275"},
    {file = "pyarrow-24.0.0-cp313-cp313t-macosx_12_0_x86_64.whl", hash = "sha256:7986f1fa71cee060ad00758bcc79d3a93bab8559bf978fab9e53472a2e25a17b"},
    {file = "pyarrow-24.0.0-cp313-cp313t-manylinux_2_28_aarch64.whl", hash = "sha256:d3e0b61e8efb24ed38898e5cdc5fffa9124be480008d401a1f8071500494ae42"},
    {file = "pyarrow-24.0.0-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:55a3bc1e3df3b5567b7d27ef551b2283f0c68a5e86f1cd56abc569da4f31335b"},
    {file = "pyarrow-24.0.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:641f795b361874ac9da5294f8f443dfdbee355cf2bd9e3b8d97aaac2306b9b37"},
    {file = "pyarrow-24.0.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8adc8e6ce5fccf5dc707046ae4914fd537def529709cc0d285d37a7f9cd442ca"},
    {file = "pyarrow-24.0.0-cp313-cp313t-win_amd64.whl", hash = "sha256:9b18371ad2f44044b81a8d23bc2d8a9b6a6226dca775e8e16cfee640473d6c5d"},
    {file = "pyarrow-24.0.0-cp314-cp314-macosx_12_0_arm64.whl", hash = "sha256:1cc9057f0319e26333b357e17f3c2c022f1a83739b48a88b25bfd5fa2dc18838"},
    {file = "pyarrow-24.0.0-cp314-cp314-macosx_12_0_x86_64.whl", hash = "sha256:e6f1278ee4785b6db21229374a1c9e54ec7c549de5d1efc9630b6207de7e170b"},
    {file = "pyarrow-24.0.0-cp314-cp314-manylinux_2_28_aarch64.whl", hash = "sha256:adbbedc55506cbdabb830890444fb856bfb0060c46c6f8026c6c2f2cf86ae795"},
    {file = "pyarrow-24.0.0-cp314-cp314-manylinux_2_28_x86_64.whl", hash = "sha256:ae8a1145af31d903fa9bb166824d7abe9b4681a000b0159c9fb99c11bc11ad26"},
    {file = "pyarrow-24.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:d7027eba1df3b2069e2e8d80f644fa0918b68c46432af3d088ddd390d063ecde"},
    {file = "pyarrow-24.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:e56a1ffe9bf7b727432b89104cc0849c21582949dd7bdcb34f17b2001a351a76"},
    {file = "pyarrow-24.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:38be1808cdd068605b787e6ca9119b27eb275a0234e50212c3492331680c3b1e"},
    {file = "pyarrow-24.0.0-cp314-cp314t-macosx_12_0_arm64.whl", hash = "sha256:418e48ce50a45a6a6c73c454677203a9c75c966cb1e92ca3370959185f197a05"},
    {file = "pyarrow-24.0.0-cp314-cp314t-macosx_12_0_x86_64.whl", hash = "sha256:2f16197705a230a78270cdd4ea8a1d57e86b2fdcbc34a1f6aebc72e65c986f9a"},
    {file = "pyarrow-24.0.0-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:fb24ac194bfc5e86839d7dcd52092ee31e5fe6733fe11f5e3b06ef0812b20072"},
    {file = "pyarrow-24.0.0-cp314-cp314t-manylinux_2_28_x86_64.whl", hash = "sha256:9700ebd9a51f5895ce75ff4ac4b3c47a7d4b42bc618be8e713e5d56bacf5f931"},
    {file = "pyarrow-24.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d8ddd2768da81d3ee08cfea9b597f4abb4e8e1dc8ae7e204b608d23a0d3ab699"},
    {file = "pyarrow-24.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:61a3d7eaa97a14768b542f3d284dc6400dd2470d9f080708b13cd46b6ae18136"},
    {file = "pyarrow-24.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:c91d00057f23b8d353039520dc3a6c09d8608164c692e9f59a175a42b2ae0c19"},
    {file = "pyarrow-24.0.0.tar.gz", hash = "sha256:85fe721a14dd823aca09127acbb06c3ca723efbd436c004f16bca601b04dcc83"},
]

[[package]]
name = "pycodestyle"
version = "2.14.0"
description = "Python style guide checker"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pycodestyle-2.14.0-py2.py3-none-any.whl", hash = "sha256:dd6bf7cb4ee77f8e016f9c8e74a35ddd9f67e1d5fd4184d86c3b98e07099f42d"},
    {file = "pycodestyle-2.14.0.tar.gz", hash = "sha256:c4b5b517d278089ff9d0abdec919cd97262a3367449ea1c8b49b91529167b783"},
]

[[package]]
name = "pydantic"
version = "2.12.4"
description = "Data validation using Python type hints"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pydantic-2.12.4-py3-none-any.whl", hash = "sha256:92d3d202a745d46f9be6df459ac5a064fdaa3c1c4cd8adcfa332ccf3c05f871e"},
    {file = "pydantic-2.12.4.tar.gz", hash = "sha256:0f8cb9555000a4b5b617f66bfd2566264c4984b27589d3b845685983e8ea85ac"},
]

[package.dependencies]
annotated-types = ">=0.6.0"
pydantic-core = "2.41.5"
typing-extensions = ">=4.14.1"
typing-inspection = ">=0.4.2"

[package.extras]
email = ["email-validator (>=2.0.0)"]
timezone = ["tzdata ; python_version >= \"3.9\" and platform_system == \"Windows\""]

[[package]]
name = "pydantic-core"
version = "2.41.5"
description = "Core functionality for Pydantic validation and serialization"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146"},
    {file = "pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a"},
    {file = "pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c"},
    {file = "pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2"},
    {file = "pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556"},
    {file = "pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49"},
    {file = "pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba"},
    {file = "pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9"},
    {file = "pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6"},
    {file = "pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b"},
    {file = "pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b"},
    {file = "pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284"},
    {file = "pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594"},
    {file = "pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e"},
    {file = "pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b"},
    {file = "pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe"},
    {file = "pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f"},
    {file = "pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7"},
    {file = "pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c"},
    {file = "pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5"},
    {file = "pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c"},
    {file = "pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294"},
    {file = "pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1"},
    {file = "pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d"},
    {file = "pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815"},
    {file = "pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3"},
    {file = "pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9"},
    {file = "pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586"},
    {file = "pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d"},
    {file = "pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740"},
    {file = "pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e"},
    {file = "pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858"},
    {file = "pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36"},
    {file = "pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11"},
    {file = "pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd"},
    {file = "pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a"},
    {file = "pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375"},
    {file = "pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553"},
    {file = "pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90"},
    {file = "pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07"},
    {file = "pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb"},
    {file = "pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23"},
    {file = "pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf"},
    {file = "pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c"},
    {file = "pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008"},
    {file = "pydantic_core-2.41.5-cp39-cp39-macosx_10_12_x86_64.whl", hash = "sha256:8bfeaf8735be79f225f3fefab7f941c712aaca36f1128c9d7e2352ee1aa87bdf"},
    {file = "pydantic_core-2.41.5-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:346285d28e4c8017da95144c7f3acd42740d637ff41946af5ce6e5e420502dd5"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a75dafbf87d6276ddc5b2bf6fae5254e3d0876b626eb24969a574fff9149ee5d"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:7b93a4d08587e2b7e7882de461e82b6ed76d9026ce91ca7915e740ecc7855f60"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e8465ab91a4bd96d36dde3263f06caa6a8a6019e4113f24dc753d79a8b3a3f82"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:299e0a22e7ae2b85c1a57f104538b2656e8ab1873511fd718a1c1c6f149b77b5"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:707625ef0983fcfb461acfaf14de2067c5942c6bb0f3b4c99158bed6fedd3cf3"},
    {file = "pydantic_core-2.41.5-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:f41eb9797986d6ebac5e8edff36d5cef9de40def462311b3eb3eeded1431e425"},
    {file = "pydantic_core-2.41.5-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:0384e2e1021894b1ff5a786dbf94771e2986ebe2869533874d7e43bc79c6f504"},
    {file = "pydantic_core-2.41.5-cp39-cp39-musllinux_1_1_armv7l.whl", hash = "sha256:f0cd744688278965817fd0839c4a4116add48d23890d468bc436f78beb28abf5"},
    {file = "pydantic_core-2.41.5-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:753e230374206729bf0a807954bcc6c150d3743928a73faffee51ac6557a03c3"},
    {file = "pydantic_core-2.41.5-cp39-cp39-win32.whl", hash = "sha256:873e0d5b4fb9b89ef7c2d2a963ea7d02879d9da0da8d9d4933dee8ee86a8b460"},
    {file = "pydantic_core-2.41.5-cp39-cp39-win_amd64.whl", hash = "sha256:e4f4a984405e91527a0d62649ee21138f8e3d0ef103be488c1dc11a80d7f184b"},
    {file = "pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034"},
    {file = "pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c"},
    {file = "pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2"},
    {file = "pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad"},
    {file = "pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd"},
    {file = "pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc"},
    {file = "pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56"},
    {file = "pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963"},
    {file = "pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f"},
    {file = "pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51"},
    {file = "pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e"},
]

[package.dependencies]
typing-extensions = ">=4.14.1"

[[package]]
name = "pydocstyle"
version = "6.3.0"
description = "Python docstring style checker"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
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
version = "3.4.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pyflakes-3.4.0-py2.py3-none-any.whl", hash = "sha256:f742a7dbd0d9cb9ea41e9a24a918996e8170c799fa528688d40dd582c8265f4f"},
    {file = "pyflakes-3.4.0.tar.gz", hash = "sha256:b24f96fafb7d2ab0ec5075b7350b3d2d2218eab42003821c06344973d3ea2f58"},
]

[[package]]
name = "pygments"
version = "2.20.0"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pygments-2.20.0-py3-none-any.whl", hash = "sha256:81a9e26dd42fd28a23a2d169d86d7ac03b46e2f8b59ed4698fb4785f946d0176"},
    {file = "pygments-2.20.0.tar.gz", hash = "sha256:6757cd03768053ff99f3039c1a36d6c0aa0b263438fcab17520b30a303a82b5f"},
]

[package.extras]
windows-terminal = ["colorama (>=0.4.6)"]

[[package]]
name = "pytest"
version = "9.0.3"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "pytest-9.0.3-py3-none-any.whl", hash = "sha256:2c5efc453d45394fdd706ade797c0a81091eccd1d6e4bccfcd476e2b8e0ab5d9"},
    {file = "pytest-9.0.3.tar.gz", hash = "sha256:b86ada508af81d19edeb213c681b1d48246c1a91d304c6c81a427674c17eb91c"},
]

[package.dependencies]
colorama = {version = ">=0.4", markers = "sys_platform == \"win32\""}
exceptiongroup = {version = ">=1", markers = "python_version < \"3.11\""}
iniconfig = ">=1.0.1"
packaging = ">=22"
pluggy = ">=1.5,<2"
pygments = ">=2.7.2"
tomli = {version = ">=1", markers = "python_version < \"3.11\""}

[package.extras]
dev = ["argcomplete", "attrs (>=19.2)", "hypothesis (>=3.56)", "mock", "requests", "setuptools", "xmlschema"]

[[package]]
name = "pytest-asyncio"
version = "0.20.3"
description = "Pytest support for asyncio"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "pytest-asyncio-0.20.3.tar.gz", hash = "sha256:83cbf01169ce3e8eb71c6c278ccb0574d1a7a3bb8eaaf5e50e0ad342afb33b36"},
    {file = "pytest_asyncio-0.20.3-py3-none-any.whl", hash = "sha256:f129998b209d04fcc65c96fc85c11e5316738358909a8399e93be553d7656442"},
]

[package.dependencies]
pytest = ">=6.1.0"

[package.extras]
docs = ["sphinx (>=5.3)", "sphinx-rtd-theme (>=1.0)"]
testing = ["coverage (>=6.2)", "flaky (>=3.5.0)", "hypothesis (>=5.7.1)", "mypy (>=0.931)", "pytest-trio (>=0.7.0)"]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
description = "Extensions to the standard Python datetime module"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["main"]
files = [
    {file = "python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3"},
    {file = "python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427"},
]

[package.dependencies]
six = ">=1.5"

[[package]]
name = "pytokens"
version = "0.4.1"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pytokens-0.4.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:2a44ed93ea23415c54f3face3b65ef2b844d96aeb3455b8a69b3df6beab6acc5"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:add8bf86b71a5d9fb5b89f023a80b791e04fba57960aa790cc6125f7f1d39dfe"},
    {file = "pytokens-0.4.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:670d286910b531c7b7e3c0b453fd8156f250adb140146d234a82219459b9640c"},
    {file = "pytokens-0.4.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4e691d7f5186bd2842c14813f79f8884bb03f5995f0575272009982c5ac6c0f7"},
    {file = "pytokens-0.4.1-cp310-cp310-win_amd64.whl", hash = "sha256:27b83ad28825978742beef057bfe406ad6ed524b2d28c252c5de7b4a6dd48fa2"},
    {file = "pytokens-0.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:d70e77c55ae8380c91c0c18dea05951482e263982911fc7410b1ffd1dadd3440"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4a58d057208cb9075c144950d789511220b07636dd2e4708d5645d24de666bdc"},
    {file = "pytokens-0.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b49750419d300e2b5a3813cf229d4e5a4c728dae470bcc89867a9ad6f25a722d"},
    {file = "pytokens-0.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:d9907d61f15bf7261d7e775bd5d7ee4d2930e04424bab1972591918497623a16"},
    {file = "pytokens-0.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:ee44d0f85b803321710f9239f335aafe16553b39106384cef8e6de40cb4ef2f6"},
    {file = "pytokens-0.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:140709331e846b728475786df8aeb27d24f48cbcf7bcd449f8de75cae7a45083"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6d6c4268598f762bc8e91f5dbf2ab2f61f7b95bdc07953b602db879b3c8c18e1"},
    {file = "pytokens-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:24afde1f53d95348b5a0eb19488661147285ca4dd7ed752bbc3e1c6242a304d1"},
    {file = "pytokens-0.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5ad948d085ed6c16413eb5fec6b3e02fa00dc29a2534f088d3302c47eb59adf9"},
    {file = "pytokens-0.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:3f901fe783e06e48e8cbdc82d631fca8f118333798193e026a50ce1b3757ea68"},
    {file = "pytokens-0.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:8bdb9d0ce90cbf99c525e75a2fa415144fd570a1ba987380190e8b786bc6ef9b"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5502408cab1cb18e128570f8d598981c68a50d0cbd7c61312a90507cd3a1276f"},
    {file = "pytokens-0.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29d1d8fb1030af4d231789959f21821ab6325e463f0503a61d204343c9b355d1"},
    {file = "pytokens-0.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:970b08dd6b86058b6dc07efe9e98414f5102974716232d10f32ff39701e841c4"},
    {file = "pytokens-0.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:9bd7d7f544d362576be74f9d5901a22f317efc20046efe2034dced238cbbfe78"},
    {file = "pytokens-0.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4a14d5f5fc78ce85e426aa159489e2d5961acf0e47575e08f35584009178e321"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97f50fd18543be72da51dd505e2ed20d2228c74e0464e4262e4899797803d7fa"},
    {file = "pytokens-0.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dc74c035f9bfca0255c1af77ddd2d6ae8419012805453e4b0e7513e17904545d"},
    {file = "pytokens-0.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f66a6bbe741bd431f6d741e617e0f39ec7257ca1f89089593479347cc4d13324"},
    {file = "pytokens-0.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:b35d7e5ad269804f6697727702da3c517bb8a5228afa450ab0fa787732055fc9"},
    {file = "pytokens-0.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:8fcb9ba3709ff77e77f1c7022ff11d13553f3c30299a9fe246a166903e9091eb"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79fc6b8699564e1f9b521582c35435f1bd32dd06822322ec44afdeba666d8cb3"},
    {file = "pytokens-0.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d31b97b3de0f61571a124a00ffe9a81fb9939146c122c11060725bd5aea79975"},
    {file = "pytokens-0.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:967cf6e3fd4adf7de8fc73cd3043754ae79c36475c1c11d514fc72cf5490094a"},
    {file = "pytokens-0.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:584c80c24b078eec1e227079d56dc22ff755e0ba8654d8383b2c549107528918"},
    {file = "pytokens-0.4.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:da5baeaf7116dced9c6bb76dc31ba04a2dc3695f3d9f74741d7910122b456edc"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:11edda0942da80ff58c4408407616a310adecae1ddd22eef8c692fe266fa5009"},
    {file = "pytokens-0.4.1-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0fc71786e629cef478cbf29d7ea1923299181d0699dbe7c3c0f4a583811d9fc1"},
    {file = "pytokens-0.4.1-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:dcafc12c30dbaf1e2af0490978352e0c4041a7cde31f4f81435c2a5e8b9cabb6"},
    {file = "pytokens-0.4.1-cp38-cp38-win_amd64.whl", hash = "sha256:42f144f3aafa5d92bad964d471a581651e28b24434d184871bd02e3a0d956037"},
    {file = "pytokens-0.4.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:34bcc734bd2f2d5fe3b34e7b3c0116bfb2397f2d9666139988e7a3eb5f7400e3"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941d4343bf27b605e9213b26bfa1c4bf197c9c599a9627eb7305b0defcfe40c1"},
    {file = "pytokens-0.4.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:3ad72b851e781478366288743198101e5eb34a414f1d5627cdd585ca3b25f1db"},
    {file = "pytokens-0.4.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:682fa37ff4d8e95f7df6fe6fe6a431e8ed8e788023c6bcc0f0880a12eab80ad1"},
    {file = "pytokens-0.4.1-cp39-cp39-win_amd64.whl", hash = "sha256:30f51edd9bb7f85c748979384165601d028b84f7bd13fe14d3e065304093916a"},
    {file = "pytokens-0.4.1-py3-none-any.whl", hash = "sha256:26cef14744a8385f35d0e095dc8b3a7583f6c953c2e3d269c7f82484bf5ad2de"},
    {file = "pytokens-0.4.1.tar.gz", hash = "sha256:292052fe80923aae2260c073f822ceba21f3872ced9a68bb7953b348e561179a"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pytz"
version = "2025.2"
description = "World timezone definitions, modern and historical"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "pytz-2025.2-py2.py3-none-any.whl", hash = "sha256:5ddf76296dd8c44c26eb8f4b6f35488f3ccbf6fbbd7adee0b7262d43f0ec2f00"},
    {file = "pytz-2025.2.tar.gz", hash = "sha256:360b9e3dbb49a209c21ad61809c7fb453643e048b38924c765813546746e81c3"},
]

[[package]]
name = "pyyaml"
version = "6.0.3"
description = "YAML parser and emitter for Python"
optional = false
python-versions = ">=3.8"
groups = ["main"]
files = [
    {file = "PyYAML-6.0.3-cp38-cp38-macosx_10_13_x86_64.whl", hash = "sha256:c2514fceb77bc5e7a2f7adfaa1feb2fb311607c9cb518dbc378688ec73d8292f"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c57bb8c96f6d1808c030b1687b9b5fb476abaa47f0db9c0101f5e9f394e97f4"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:efd7b85f94a6f21e4932043973a7ba2613b059c4a000551892ac9f1d11f5baf3"},
    {file = "PyYAML-6.0.3-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:22ba7cfcad58ef3ecddc7ed1db3409af68d023b7f940da23c6c2a1890976eda6"},
    {file = "PyYAML-6.0.3-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:6344df0d5755a2c9a276d4473ae6b90647e216ab4757f8426893b5dd2ac3f369"},
    {file = "PyYAML-6.0.3-cp38-cp38-win32.whl", hash = "sha256:3ff07ec89bae51176c0549bc4c63aa6202991da2d9a6129d7aef7f1407d3f295"},
    {file = "PyYAML-6.0.3-cp38-cp38-win_amd64.whl", hash = "sha256:5cf4e27da7e3fbed4d6c3d8e797387aaad68102272f8f9752883bc32d61cb87b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:214ed4befebe12df36bcc8bc2b64b396ca31be9304b8f59e25c11cf94a4c033b"},
    {file = "pyyaml-6.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:02ea2dfa234451bbb8772601d7b8e426c2bfa197136796224e50e35a78777956"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b30236e45cf30d2b8e7b3e85881719e98507abed1011bf463a8fa23e9c3e98a8"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:66291b10affd76d76f54fad28e22e51719ef9ba22b29e1d7d03d6777a9174198"},
    {file = "pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c7708761fccb9397fe64bbc0395abcae8c4bf7b0eac081e12b809bf47700d0b"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:418cf3f2111bc80e0933b2cd8cd04f286338bb88bdc7bc8e6dd775ebde60b5e0"},
    {file = "pyyaml-6.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5e0b74767e5f8c593e8c9b5912019159ed0533c70051e9cce3e8b6aa699fcd69"},
    {file = "pyyaml-6.0.3-cp310-cp310-win32.whl", hash = "sha256:28c8d926f98f432f88adc23edf2e6d4921ac26fb084b028c733d01868d19007e"},
    {file = "pyyaml-6.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:bdb2c67c6c1390b63c6ff89f210c8fd09d9a1217a465701eac7316313c915e4c"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:44edc647873928551a01e7a563d7452ccdebee747728c1080d881d68af7b997e"},
    {file = "pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:652cb6edd41e718550aad172851962662ff2681490a8a711af6a4d288dd96824"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:10892704fc220243f5305762e276552a0395f7beb4dbf9b14ec8fd43b57f126c"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:850774a7879607d3a6f50d36d04f00ee69e7fc816450e5f7e58d7f17f1ae5c00"},
    {file = "pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b8bb0864c5a28024fac8a632c443c87c5aa6f215c0b126c449ae1a150412f31d"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37d57ad971609cf3c53ba6a7e365e40660e3be0e5175fa9f2365a379d6095a"},
    {file = "pyyaml-6.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:37503bfbfc9d2c40b344d06b2199cf0e96e97957ab1c1b546fd4f87e53e5d3e4"},
    {file = "pyyaml-6.0.3-cp311-cp311-win32.whl", hash = "sha256:8098f252adfa6c80ab48096053f512f2321f0b998f98150cea9bd23d83e1467b"},
    {file = "pyyaml-6.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f3bfb4965eb874431221a3ff3fdcddc7e74e3b07799e0e84ca4a0f867d449bf"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196"},
    {file = "pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c"},
    {file = "pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e"},
    {file = "pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea"},
    {file = "pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b"},
    {file = "pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8"},
    {file = "pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5"},
    {file = "pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6"},
    {file = "pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be"},
    {file = "pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c"},
    {file = "pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac"},
    {file = "pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788"},
    {file = "pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764"},
    {file = "pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac"},
    {file = "pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3"},
    {file = "pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702"},
    {file = "pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065"},
    {file = "pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9"},
    {file = "pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_10_13_x86_64.whl", hash = "sha256:b865addae83924361678b652338317d1bd7e79b1f4596f96b96c77a5a34b34da"},
    {file = "pyyaml-6.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c3355370a2c156cffb25e876646f149d5d68f5e0a3ce86a5084dd0b64a994917"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3c5677e12444c15717b902a5798264fa7909e41153cdf9ef7ad571b704a63dd9"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5ed875a24292240029e4483f9d4a4b8a1ae08843b9c54f43fcc11e404532a8a5"},
    {file = "pyyaml-6.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0150219816b6a1fa26fb4699fb7daa9caf09eb1999f3b70fb6e786805e80375a"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:fa160448684b4e94d80416c0fa4aac48967a969efe22931448d853ada8baf926"},
    {file = "pyyaml-6.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:27c0abcb4a5dac13684a37f76e701e054692a9b2d3064b70f5e4eb54810553d7"},
    {file = "pyyaml-6.0.3-cp39-cp39-win32.whl", hash = "sha256:1ebe39cb5fc479422b83de611d14e2c0d3bb2a18bbcb01f229ab3cfbd8fee7a0"},
    {file = "pyyaml-6.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:2e71d11abed7344e42a8849600193d15b6def118602c4c176f748e4583246007"},
    {file = "pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f"},
]

[[package]]
name = "requests"
version = "2.33.0"
description = "Python HTTP for Humans."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "requests-2.33.0-py3-none-any.whl", hash = "sha256:3324635456fa185245e24865e810cecec7b4caf933d7eb133dcde67d48cee69b"},
    {file = "requests-2.33.0.tar.gz", hash = "sha256:c7ebc5e8b0f21837386ad0e1c8fe8b829fa5f544d8df3b2253bff14ef29d7652"},
]

[package.dependencies]
certifi = ">=2023.5.7"
charset_normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.26,<3"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
test = ["PySocks (>=1.5.6,!=1.5.7)", "pytest (>=3)", "pytest-cov", "pytest-httpbin (==2.1.0)", "pytest-mock", "pytest-xdist"]
use-chardet-on-py3 = ["chardet (>=3.0.2,<8)"]

[[package]]
name = "responses"
version = "0.22.0"
description = "A utility library for mocking out the `requests` Python library."
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "responses-0.22.0-py3-none-any.whl", hash = "sha256:dcf294d204d14c436fddcc74caefdbc5764795a40ff4e6a7740ed8ddbf3294be"},
    {file = "responses-0.22.0.tar.gz", hash = "sha256:396acb2a13d25297789a5866b4881cf4e46ffd49cc26c43ab1117f40b973102e"},
]

[package.dependencies]
requests = ">=2.22.0,<3.0"
toml = "*"
types-toml = "*"
urllib3 = ">=1.25.10"

[package.extras]
tests = ["coverage (>=6.0.0)", "flake8", "mypy", "pytest (>=7.0.0)", "pytest-asyncio", "pytest-cov", "pytest-httpserver", "types-requests"]

[[package]]
name = "setuptools"
version = "80.9.0"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
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
name = "six"
version = "1.17.0"
description = "Python 2 and 3 compatibility utilities"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
groups = ["main"]
files = [
    {file = "six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274"},
    {file = "six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81"},
]

[[package]]
name = "sniffio"
version = "1.3.1"
description = "Sniff out which async library your code is running under"
optional = false
python-versions = ">=3.7"
groups = ["main"]
files = [
    {file = "sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2"},
    {file = "sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc"},
]

[[package]]
name = "snowballstemmer"
version = "3.0.1"
description = "This package provides 32 stemmers for 30 languages generated from Snowball algorithms."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*"
groups = ["dev"]
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
groups = ["dev"]
files = [
    {file = "toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b"},
    {file = "toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"},
]

[[package]]
name = "tomli"
version = "2.3.0"
description = "A lil' TOML parser"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "tomli-2.3.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:88bd15eb972f3664f5ed4b57c1634a97153b4bac4479dcb6a495f41921eb7f45"},
    {file = "tomli-2.3.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:883b1c0d6398a6a9d29b508c331fa56adbcdff647f6ace4dfca0f50e90dfd0ba"},
    {file = "tomli-2.3.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d1381caf13ab9f300e30dd8feadb3de072aeb86f1d34a8569453ff32a7dea4bf"},
    {file = "tomli-2.3.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a0e285d2649b78c0d9027570d4da3425bdb49830a6156121360b3f8511ea3441"},
    {file = "tomli-2.3.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:0a154a9ae14bfcf5d8917a59b51ffd5a3ac1fd149b71b47a3a104ca4edcfa845"},
    {file = "tomli-2.3.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:74bf8464ff93e413514fefd2be591c3b0b23231a77f901db1eb30d6f712fc42c"},
    {file = "tomli-2.3.0-cp311-cp311-win32.whl", hash = "sha256:00b5f5d95bbfc7d12f91ad8c593a1659b6387b43f054104cda404be6bda62456"},
    {file = "tomli-2.3.0-cp311-cp311-win_amd64.whl", hash = "sha256:4dc4ce8483a5d429ab602f111a93a6ab1ed425eae3122032db7e9acf449451be"},
    {file = "tomli-2.3.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d7d86942e56ded512a594786a5ba0a5e521d02529b3826e7761a05138341a2ac"},
    {file = "tomli-2.3.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:73ee0b47d4dad1c5e996e3cd33b8a76a50167ae5f96a2607cbe8cc773506ab22"},
    {file = "tomli-2.3.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:792262b94d5d0a466afb5bc63c7daa9d75520110971ee269152083270998316f"},
    {file = "tomli-2.3.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4f195fe57ecceac95a66a75ac24d9d5fbc98ef0962e09b2eddec5d39375aae52"},
    {file = "tomli-2.3.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:e31d432427dcbf4d86958c184b9bfd1e96b5b71f8eb17e6d02531f434fd335b8"},
    {file = "tomli-2.3.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b0882799624980785240ab732537fcfc372601015c00f7fc367c55308c186f6"},
    {file = "tomli-2.3.0-cp312-cp312-win32.whl", hash = "sha256:ff72b71b5d10d22ecb084d345fc26f42b5143c5533db5e2eaba7d2d335358876"},
    {file = "tomli-2.3.0-cp312-cp312-win_amd64.whl", hash = "sha256:1cb4ed918939151a03f33d4242ccd0aa5f11b3547d0cf30f7c74a408a5b99878"},
    {file = "tomli-2.3.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5192f562738228945d7b13d4930baffda67b69425a7f0da96d360b0a3888136b"},
    {file = "tomli-2.3.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:be71c93a63d738597996be9528f4abe628d1adf5e6eb11607bc8fe1a510b5dae"},
    {file = "tomli-2.3.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c4665508bcbac83a31ff8ab08f424b665200c0e1e645d2bd9ab3d3e557b6185b"},
    {file = "tomli-2.3.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4021923f97266babc6ccab9f5068642a0095faa0a51a246a6a02fccbb3514eaf"},
    {file = "tomli-2.3.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4ea38c40145a357d513bffad0ed869f13c1773716cf71ccaa83b0fa0cc4e42f"},
    {file = "tomli-2.3.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ad805ea85eda330dbad64c7ea7a4556259665bdf9d2672f5dccc740eb9d3ca05"},
    {file = "tomli-2.3.0-cp313-cp313-win32.whl", hash = "sha256:97d5eec30149fd3294270e889b4234023f2c69747e555a27bd708828353ab606"},
    {file = "tomli-2.3.0-cp313-cp313-win_amd64.whl", hash = "sha256:0c95ca56fbe89e065c6ead5b593ee64b84a26fca063b5d71a1122bf26e533999"},
    {file = "tomli-2.3.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:cebc6fe843e0733ee827a282aca4999b596241195f43b4cc371d64fc6639da9e"},
    {file = "tomli-2.3.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:4c2ef0244c75aba9355561272009d934953817c49f47d768070c3c94355c2aa3"},
    {file = "tomli-2.3.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c22a8bf253bacc0cf11f35ad9808b6cb75ada2631c2d97c971122583b129afbc"},
    {file = "tomli-2.3.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0eea8cc5c5e9f89c9b90c4896a8deefc74f518db5927d0e0e8d4a80953d774d0"},
    {file = "tomli-2.3.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b74a0e59ec5d15127acdabd75ea17726ac4c5178ae51b85bfe39c4f8a278e879"},
    {file = "tomli-2.3.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b5870b50c9db823c595983571d1296a6ff3e1b88f734a4c8f6fc6188397de005"},
    {file = "tomli-2.3.0-cp314-cp314-win32.whl", hash = "sha256:feb0dacc61170ed7ab602d3d972a58f14ee3ee60494292d384649a3dc38ef463"},
    {file = "tomli-2.3.0-cp314-cp314-win_amd64.whl", hash = "sha256:b273fcbd7fc64dc3600c098e39136522650c49bca95df2d11cf3b626422392c8"},
    {file = "tomli-2.3.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:940d56ee0410fa17ee1f12b817b37a4d4e4dc4d27340863cc67236c74f582e77"},
    {file = "tomli-2.3.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:f85209946d1fe94416debbb88d00eb92ce9cd5266775424ff81bc959e001acaf"},
    {file = "tomli-2.3.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a56212bdcce682e56b0aaf79e869ba5d15a6163f88d5451cbde388d48b13f530"},
    {file = "tomli-2.3.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c5f3ffd1e098dfc032d4d3af5c0ac64f6d286d98bc148698356847b80fa4de1b"},
    {file = "tomli-2.3.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:5e01decd096b1530d97d5d85cb4dff4af2d8347bd35686654a004f8dea20fc67"},
    {file = "tomli-2.3.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:8a35dd0e643bb2610f156cca8db95d213a90015c11fee76c946aa62b7ae7e02f"},
    {file = "tomli-2.3.0-cp314-cp314t-win32.whl", hash = "sha256:a1f7f282fe248311650081faafa5f4732bdbfef5d45fe3f2e702fbc6f2d496e0"},
    {file = "tomli-2.3.0-cp314-cp314t-win_amd64.whl", hash = "sha256:70a251f8d4ba2d9ac2542eecf008b3c8a9fc5c3f9f02c56a9d7952612be2fdba"},
    {file = "tomli-2.3.0-py3-none-any.whl", hash = "sha256:e95b1af3c5b07d9e643909b5abbec77cd9f1217e6d0bca72b0234736b9fb1f1b"},
    {file = "tomli-2.3.0.tar.gz", hash = "sha256:64be704a875d2a59753d80ee8a533c3fe183e3f06807ff7dc2232938ccb01549"},
]

[[package]]
name = "types-pyyaml"
version = "6.0.12.20250915"
description = "Typing stubs for PyYAML"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "types_pyyaml-6.0.12.20250915-py3-none-any.whl", hash = "sha256:e7d4d9e064e89a3b3cae120b4990cd370874d2bf12fa5f46c97018dd5d3c9ab6"},
    {file = "types_pyyaml-6.0.12.20250915.tar.gz", hash = "sha256:0f8b54a528c303f0e6f7165687dd33fafa81c807fcac23f632b63aa624ced1d3"},
]

[[package]]
name = "types-requests"
version = "2.32.4.20250913"
description = "Typing stubs for requests"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "types_requests-2.32.4.20250913-py3-none-any.whl", hash = "sha256:78c9c1fffebbe0fa487a418e0fa5252017e9c60d1a2da394077f1780f655d7e1"},
    {file = "types_requests-2.32.4.20250913.tar.gz", hash = "sha256:abd6d4f9ce3a9383f269775a9835a4c24e5cd6b9f647d64f88aa4613c33def5d"},
]

[package.dependencies]
urllib3 = ">=2"

[[package]]
name = "types-toml"
version = "0.10.8.20240310"
description = "Typing stubs for toml"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "types-toml-0.10.8.20240310.tar.gz", hash = "sha256:3d41501302972436a6b8b239c850b26689657e25281b48ff0ec06345b8830331"},
    {file = "types_toml-0.10.8.20240310-py3-none-any.whl", hash = "sha256:627b47775d25fa29977d9c70dc0cbab3f314f32c8d8d0c012f2ef5de7aaec05d"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
description = "Runtime typing introspection tools"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7"},
    {file = "typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464"},
]

[package.dependencies]
typing-extensions = ">=4.12.0"

[[package]]
name = "tzdata"
version = "2025.2"
description = "Provider of IANA time zone data"
optional = false
python-versions = ">=2"
groups = ["main"]
files = [
    {file = "tzdata-2025.2-py2.py3-none-any.whl", hash = "sha256:1a403fada01ff9221ca8044d701868fa132215d84beb92242d9acd2147f667a8"},
    {file = "tzdata-2025.2.tar.gz", hash = "sha256:b60a638fcc0daffadf82fe0f57e53d06bdec2f36c4df66280ae79bce6bd6f2b9"},
]

[[package]]
name = "uplink"
version = "0.10.0"
description = "A Declarative HTTP Client for Python."
optional = false
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "uplink-0.10.0-py3-none-any.whl", hash = "sha256:03212163f8a83a608480ec15122884988eb82cc7a2368b9072d9af8ede2246d9"},
    {file = "uplink-0.10.0.tar.gz", hash = "sha256:a3b76b1cac5394126a72698d72b209bb80c8a94bad091870e463919979e4ab63"},
]

[package.dependencies]
pydantic = {version = ">=2.0.0", optional = true, markers = "extra == \"pydantic\""}
requests = ">=2.18.0"
six = ">=1.13.0"
uritemplate = ">=3.0.0"

[package.extras]
aiohttp = ["aiohttp (>=3.8.1)"]
marshmallow = ["marshmallow (>=2.15.0)"]
pydantic = ["pydantic (>=2.0.0)"]
twisted = ["twisted (>=21.7.0)"]

[[package]]
name = "uritemplate"
version = "4.2.0"
description = "Implementation of RFC 6570 URI Templates"
optional = false
python-versions = ">=3.9"
groups = ["main"]
files = [
    {file = "uritemplate-4.2.0-py3-none-any.whl", hash = "sha256:962201ba1c4edcab02e60f9a0d3821e82dfc5d2d6662a21abd533879bdb8a686"},
    {file = "uritemplate-4.2.0.tar.gz", hash = "sha256:480c2ed180878955863323eea31b0ede668795de182617fef9c6ca09e6ec9d0e"},
]

[[package]]
name = "urllib3"
version = "2.7.0"
description = "HTTP library with thread-safe connection pooling, file post, and more."
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "urllib3-2.7.0-py3-none-any.whl", hash = "sha256:9fb4c81ebbb1ce9531cce37674bbc6f1360472bc18ca9a553ede278ef7276897"},
    {file = "urllib3-2.7.0.tar.gz", hash = "sha256:231e0ec3b63ceb14667c67be60f2f2c40a518cb38b03af60abc813da26505f4c"},
]

[package.extras]
brotli = ["brotli (>=1.2.0) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=1.2.0.0) ; platform_python_implementation != \"CPython\""]
h2 = ["h2 (>=4,<5)"]
socks = ["pysocks (>=1.5.6,!=1.5.7,<2.0)"]
zstd = ["backports-zstd (>=1.0.0) ; python_version < \"3.14\""]

[extras]
pyarrow = ["pyarrow"]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "df6c4c90a3b87f8fd06843b45f360cf40cec36845889d29730a52719e2f14259"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=pyproject.toml sha256=cd787049f9d050b3f6f16a8dad6119ea8cc9d1ce7b6cf3edc7e177badc84b0f1 bytes=3061 -->
## FILE: pyproject.toml

- repository: `ni/nisystemlink-clients-python`
- source_path: `pyproject.toml`
- sha256: `cd787049f9d050b3f6f16a8dad6119ea8cc9d1ce7b6cf3edc7e177badc84b0f1`
- bytes: 3061

````toml
[tool.poetry]
name = "nisystemlink-clients"
version = "2.32.1"
description = "NI-SystemLink Python API"
authors = ["National Instruments"]
maintainers = [
    "Richard Bell <richard.bell@emerson.com>",
    "Paul Spangler <paul.spangler@emerson.com>",
    "Cameron Waterman <cameron.waterman@emerson.com>",
]
keywords = ["nisystemlink", "systemlink"]
license = "MIT"
readme = "README.rst"
packages = [{ include = "nisystemlink" }]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Manufacturing",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Scientific/Engineering",
    "Topic :: System :: Hardware",
]

[tool.poetry.dependencies]
python   = "^3.10"
aenum    = "^3.1.11"
Events   = "^0.4"
httpx    = "^0.28.1"
requests = "^2.28.1"
uplink   = { version = "^0.10.0", extras = ["pydantic"] }
pydantic = "^2.11.3"
pyyaml = "^6.0.1"
pandas = "^2.1.0"
pyarrow = { version = ">=21,<25", optional = true }

[tool.poetry.extras]
pyarrow = ["pyarrow"]

[tool.poetry.group.dev.dependencies]
backoff             = "^2.2.1"
black               = ">=22.10,<27.0"
flake8              = "^7.3.0"
flake8-import-order = "^0.19.2"
pytest              = ">=7.2,<10.0"
pytest-asyncio      = "^0.20.1"
mypy                = "^1.18.2"
flake8-docstrings   = "^1.6.0"
poethepoet          = "^0.16.4"
types-requests      = "^2.28.11.4"
responses           = "^0.22.0"
types-pyyaml        = "^6.0.12"

[tool.poe.tasks]
test    = "pytest tests -m \"(not slow) and (not cloud) and (not enterprise)\""
doctest = "pytest --doctest-modules docs"
check   = "black --check nisystemlink examples tests"
format  = "black nisystemlink examples tests"
lint    = "flake8 nisystemlink examples tests"
types   = "mypy --config-file mypy.ini nisystemlink examples tests"

[tool.pytest.ini_options]
addopts = "--strict-markers"
testpaths = ["tests"]
markers = [
    "unit: mark a test as a unit test",
    "integration: mark a test as an integration test",
    "cloud: mark a test as a cloud integration test",
    "enterprise: mark a test as an enterprise integration test",
    "webserver: mark a test as a webserver integration test",
    "slow: mark a test as a slow test",
    "focus: focus a test during development",
]

[tool.black]
exclude = ".*\\.pyi"

[tool.semantic_release]
branch        = "master"
version_toml  = ["pyproject.toml:tool.poetry.version"]
build_command = "poetry build"



[build-system]
requires      = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=README.rst sha256=2aae23331a4e67eeb795e2be574f17ce05e48899e66d3c522c9ac68867c2668d bytes=3613 -->
## FILE: README.rst

- repository: `ni/nisystemlink-clients-python`
- source_path: `README.rst`
- sha256: `2aae23331a4e67eeb795e2be574f17ce05e48899e66d3c522c9ac68867c2668d`
- bytes: 3613

````rst
.. image:: https://img.shields.io/pypi/v/nisystemlink-clients.svg
    :target: https://pypi.org/project/nisystemlink-clients
    :alt: PyPI version


.. image:: https://img.shields.io/pypi/pyversions/nisystemlink-clients.svg
    :target: https://pypi.org/project/nisystemlink-clients
    :alt: Python versions


.. image:: https://img.shields.io/pypi/l/nisystemlink-clients.svg
    :target: https://github.com/ni/nisystemlink-clients-python/blob/master/LICENSE
    :alt: License


.. image:: https://img.shields.io/pypi/dm/nisystemlink-clients.svg
    :target: https://pypi.org/project/nisystemlink-clients
    :alt: Downloads


About
=====
The **nisystemlink-clients** package contains an API (Application Programming
Interface) for `SystemLink <https://ni.com/systemlink>`_ that uses HTTP to
interact with a SystemLink Server. The package is implemented in Python. NI
created and supports this package.


===========  ====================================================
Info         NI SystemLink API Clients for Python
Author       National Instruments
===========  ====================================================

Requirements
============
**nisystemlink-clients** has the following requirements:

* Access to a SystemLink Server or SystemLink Enterprise installation
* CPython 3.10+

.. _installation_section:

Installation
============
To install **nisystemlink-clients**, use one of the following methods:

1. `pip <https://pypi.python.org/pypi/pip>`_::

   $ python -m pip install nisystemlink-clients

2. **easy_install** from `setuptools <https://pypi.python.org/pypi/setuptools>`_::

   $ python -m easy_install nisystemlink-clients

Optional Arrow (pyarrow) Support
--------------------------------
The base install does not pull in ``pyarrow``. Arrow ``RecordBatch`` ingestion via
``DataFrameClient.append_table_data`` is available starting in
``nisystemlink-clients`` version 2.19.0. Install that version (or newer) with the
optional extra:

   $ python -m pip install "nisystemlink-clients[pyarrow]>=2.19.0"

If you already have an older version installed, upgrade with:

   $ python -m pip install --upgrade "nisystemlink-clients[pyarrow]>=2.19.0"

Without the extra (or when using a package version earlier than 2.19.0),
Arrow-specific code paths will raise a ``RuntimeError`` when attempting to
append ``pyarrow.RecordBatch`` instances.

.. _usage_section:

Usage
=====
Refer to the `documentation <https://python-docs.systemlink.io>`_
for detailed information on how to use **nisystemlink-clients**.

.. _support_section:

Support / Feedback
==================
The **nisystemlink-clients** package is supported by NI. For support for
**nisystemlink-clients**, open a request through the NI support portal at
`ni.com <https://www.ni.com>`_.

Bugs / Feature Requests
=======================
To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/nisystemlink-clients-python/issues>`_.

Documentation
=============
To view the documentation, visit the
`nisystemlink.clients Documentation Page <https://python-docs.systemlink.io>`_.

Changelog
=============
To view the changelog, visit the
`GitHub repository CHANGELOG <https://github.com/ni/nisystemlink-clients-python/blob/master/CHANGELOG.md>`_.

License
=======
**nisystemlink-clients** is licensed under an MIT-style license (see `LICENSE
<LICENSE>`_).  Other incorporated projects may be licensed under different
licenses. All licenses allow for non-commercial and commercial use.
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/anyorderlist.py sha256=9dfe464c28d6b49cea69c987bca2bec0c8cb5261fd1bdab5c5e34bebd22bebe2 bytes=533 -->
## FILE: tests/anyorderlist.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/anyorderlist.py`
- sha256: `9dfe464c28d6b49cea69c987bca2bec0c8cb5261fd1bdab5c5e34bebd22bebe2`
- bytes: 533

````python
class AnyOrderList:
    """Sequence that compares to a list, but allows any order.

    This is only intended for comparison purposes, not as an actual list replacement.
    """

    def __init__(self, list_):
        self._list = list_
        self._list.sort()

    def __eq__(self, other):
        assert isinstance(other, list)
        return self._list == sorted(other)

    def __str__(self):
        return str(self._list)

    def __repr__(self):
        return "AnyOrderList({})".format(repr(self._list))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/core/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_http_configuration.py sha256=62153708a497857a87f9be3157eef7d51160920aaa64f9984bd5bb3670122e8a bytes=10272 -->
## FILE: tests/core/test_http_configuration.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_http_configuration.py`
- sha256: `62153708a497857a87f9be3157eef7d51160920aaa64f9984bd5bb3670122e8a`
- bytes: 10272

````python
# -*- coding: utf-8 -*-

"""Tests for HttpConfiguration."""

import pathlib

import pytest
from nisystemlink.clients.core._http_configuration import HttpConfiguration


class TestHttpConfiguration:
    """Test cases for HttpConfiguration class."""

    def test__valid_server_uri__initializes_correctly(self):
        """Test that a valid server URI initializes the configuration correctly."""
        config = HttpConfiguration("https://example.com")

        assert config.server_uri == "https://example.com"
        assert config.api_keys is None
        assert config.username is None
        assert config.password is None
        assert config.cert_path is None
        assert config.workspace is None
        assert config.verify is True
        assert (
            config.timeout_milliseconds
            == HttpConfiguration.DEFAULT_TIMEOUT_MILLISECONDS
        )
        assert config.user_agent is None

    def test__server_uri_with_port__preserves_port(self):
        """Test that server URI with port preserves the port."""
        config = HttpConfiguration("https://example.com:8080")

        assert config.server_uri == "https://example.com:8080"

    def test__server_uri_with_path_and_query__strips_path_and_query(self):
        """Test that path and query components are stripped from server URI."""
        config = HttpConfiguration("https://example.com/path?query=value")

        assert config.server_uri == "https://example.com"

    def test__api_key_authentication__sets_api_keys(self):
        """Test that API key authentication sets the api_keys property."""
        config = HttpConfiguration("https://example.com", api_key="test-key")

        assert config.api_keys == {"x-ni-api-key": "test-key"}
        assert config.username is None
        assert config.password is None

    def test__username_password_authentication__sets_credentials(self):
        """Test that username/password authentication sets credentials."""
        config = HttpConfiguration(
            "https://example.com", username="testuser", password="testpass"
        )

        assert config.username == "testuser"
        assert config.password == "testpass"
        assert config.api_keys is None

    def test__all_optional_parameters__sets_all_properties(self):
        """Test that all optional parameters are set correctly."""
        cert_path = pathlib.Path("/path/to/cert.pem")
        config = HttpConfiguration(
            "https://example.com",
            api_key="test-key",
            cert_path=cert_path,
            workspace="workspace-123",
            verify=False,
        )

        assert config.server_uri == "https://example.com"
        assert config.api_keys == {"x-ni-api-key": "test-key"}
        assert config.cert_path == cert_path
        assert config.workspace == "workspace-123"
        assert config.verify is False

    def test__missing_scheme__raises_value_error(self):
        """Test that missing scheme in server URI raises ValueError."""
        with pytest.raises(ValueError, match="Scheme.*not included"):
            HttpConfiguration("example.com")

    def test__missing_hostname__raises_value_error(self):
        """Test that missing hostname in server URI raises ValueError."""
        with pytest.raises(ValueError, match="Host.*not included"):
            HttpConfiguration("https://")

    def test__username_without_password__raises_value_error(self):
        """Test that username without password raises ValueError."""
        with pytest.raises(
            ValueError, match="If username or password is set, both must be set"
        ):
            HttpConfiguration("https://example.com", username="testuser")

    def test__password_without_username__raises_value_error(self):
        """Test that password without username raises ValueError."""
        with pytest.raises(
            ValueError, match="If username or password is set, both must be set"
        ):
            HttpConfiguration("https://example.com", password="testpass")

    def test__timeout_milliseconds_property__getter_and_setter(self):
        """Test timeout_milliseconds property getter and setter."""
        config = HttpConfiguration("https://example.com")

        # Test default value
        assert (
            config.timeout_milliseconds
            == HttpConfiguration.DEFAULT_TIMEOUT_MILLISECONDS
        )

        # Test setter
        config.timeout_milliseconds = 30000
        assert config.timeout_milliseconds == 30000

    def test__user_agent_property__getter_and_setter(self):
        """Test user_agent property getter and setter."""
        config = HttpConfiguration("https://example.com")

        # Test default value
        assert config.user_agent is None

        # Test setter with value
        config.user_agent = "TestAgent/1.0"
        assert config.user_agent == "TestAgent/1.0"

        # Test setter with None
        config.user_agent = None
        assert config.user_agent is None

        # Test setter with empty string
        config.user_agent = ""
        assert config.user_agent is None

    def test__verify_property__getter_and_setter(self):
        """Test verify property getter and setter."""
        config = HttpConfiguration("https://example.com")

        # Test default value
        assert config.verify is True

        # Test setter
        config.verify = False
        assert config.verify is False

        config.verify = True
        assert config.verify is True

    def test__api_keys_property__returns_copy(self):
        """Test that api_keys property returns a copy of the internal dictionary."""
        config = HttpConfiguration("https://example.com", api_key="test-key")

        api_keys = config.api_keys
        assert api_keys == {"x-ni-api-key": "test-key"}

        # Modify the returned dictionary
        api_keys["new-key"] = "new-value"

        # Original should be unchanged
        assert config.api_keys == {"x-ni-api-key": "test-key"}

    def test__api_keys_property__returns_none_when_no_api_key(self):
        """Test that api_keys property returns None when no API key is set."""
        config = HttpConfiguration("https://example.com")

        assert config.api_keys is None

    def test__server_uri_property__is_read_only(self):
        """Test that server_uri property is read-only."""
        config = HttpConfiguration("https://example.com")

        # These properties should only have getters, not setters
        # We can test this by trying to set and expecting an AttributeError
        with pytest.raises(AttributeError):
            config.server_uri = "https://different.com"

    def test__username_property__is_read_only(self):
        """Test that username property is read-only."""
        config = HttpConfiguration(
            "https://example.com", username="test", password="test"
        )

        # Username should be read-only after initialization
        with pytest.raises(AttributeError):
            config.username = "different"

    def test__password_property__is_read_only(self):
        """Test that password property is read-only."""
        config = HttpConfiguration(
            "https://example.com", username="test", password="test"
        )

        # Password should be read-only after initialization
        with pytest.raises(AttributeError):
            config.password = "different"

    def test__cert_path_property__is_read_only(self):
        """Test that cert_path property is read-only."""
        config = HttpConfiguration("https://example.com")

        # Cert path should be read-only after initialization
        with pytest.raises(AttributeError):
            config.cert_path = pathlib.Path("/different/path")

    def test__workspace_property__is_read_only(self):
        """Test that workspace property is read-only."""
        config = HttpConfiguration("https://example.com")

        # Workspace should be read-only after initialization
        with pytest.raises(AttributeError):
            config.workspace = "different-workspace"

    def test__default_timeout_constant__has_expected_value(self):
        """Test that the default timeout constant has the expected value."""
        assert HttpConfiguration.DEFAULT_TIMEOUT_MILLISECONDS == 60000

    def test__http_scheme__is_accepted(self):
        """Test that HTTP scheme is accepted."""
        config = HttpConfiguration("http://example.com")

        assert config.server_uri == "http://example.com"

    def test__case_insensitive_scheme__is_normalized_to_lowercase(self):
        """Test that case-insensitive schemes are normalized to lowercase."""
        config = HttpConfiguration("HTTPS://example.com")

        assert config.server_uri == "https://example.com"

    def test__ipv4_address__is_accepted(self):
        """Test that IPv4 addresses are accepted as hostnames."""
        config = HttpConfiguration("https://192.168.1.1")

        assert config.server_uri == "https://192.168.1.1"

    def test__ipv6_address__is_accepted(self):
        """Test that IPv6 addresses are accepted as hostnames."""
        config = HttpConfiguration("https://[::1]")

        assert config.server_uri == "https://[::1]"

    def test__empty_api_key__does_not_set_api_keys(self):
        """Test that empty API key does not set api_keys."""
        config = HttpConfiguration("https://example.com", api_key="")

        assert config.api_keys is None

    def test__none_api_key__does_not_set_api_keys(self):
        """Test that None API key does not set api_keys."""
        config = HttpConfiguration("https://example.com", api_key=None)

        assert config.api_keys is None

    def test__pathlib_path__cert_path(self):
        """Test that pathlib.Path objects work for cert_path."""
        cert_path = pathlib.Path("/etc/ssl/certs/ca-bundle.crt")
        config = HttpConfiguration("https://example.com", cert_path=cert_path)

        assert config.cert_path == cert_path
        assert isinstance(config.cert_path, pathlib.Path)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_iterator_file_like.py sha256=1acbb84679af6e388e486b403c0ba24e63384afeb6e580bd50903bff3bd3ac32 bytes=852 -->
## FILE: tests/core/test_iterator_file_like.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_iterator_file_like.py`
- sha256: `1acbb84679af6e388e486b403c0ba24e63384afeb6e580bd50903bff3bd3ac32`
- bytes: 852

````python
from nisystemlink.clients.core.helpers import IteratorFileLike


class TestIteratorFileLike:
    def test__negative_size__read__reads_all_data(self):
        iterator_file_like = IteratorFileLike(iter([b"123", b"456", b"789"]))

        assert iterator_file_like.read(-1) == b"123456789"

    def test__size_smaller_than_chunk__read__reads_to_size(self):
        iterator_file_like = IteratorFileLike(iter([b"1234"]))

        assert iterator_file_like.read(1) == b"1"
        assert iterator_file_like.read(2) == b"23"

    def test__size_larger_than_chunk__read__reads_to_size(self):
        iterator_file_like = IteratorFileLike(iter([b"123", b"456789", b"abcde"]))

        assert iterator_file_like.read(4) == b"1234"
        assert iterator_file_like.read(6) == b"56789a"
        assert iterator_file_like.read(6) == b"bcde"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_json_model.py sha256=1cf615c382e9933a617765c547205841711c74871da49ab8bd752eea61452a9c bytes=4127 -->
## FILE: tests/core/test_json_model.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_json_model.py`
- sha256: `1cf615c382e9933a617765c547205841711c74871da49ab8bd752eea61452a9c`
- bytes: 4127

````python
"""Tests for JsonModel alias handling."""

from inspect import signature
from typing import Annotated, cast, Literal

from nisystemlink.clients.core._uplink._json_model import JsonModel
from pydantic import AliasChoices, Field, TypeAdapter


class ExampleJsonModel(JsonModel):
    """Simple model used to verify JsonModel alias behavior."""

    program_name: str


class ExampleExplicitAliasJsonModel(JsonModel):
    """Simple model used to verify explicit alias behavior."""

    program_name: str
    session_id: str = Field(
        validation_alias=AliasChoices("session_id", "id"),
        serialization_alias="id",
    )


class TestJsonModel:
    """Test cases for JsonModel alias behavior."""

    def test__signature__uses_snake_case_field_names(self):
        """Test that constructor signatures expose Pythonic snake_case names."""
        assert str(signature(ExampleJsonModel)) == "(*, program_name: str) -> None"

    def test__snake_case_input__deserializes_and_serializes_by_alias(self):
        """Test that snake_case input remains valid and serializes to camelCase."""
        model = ExampleJsonModel(program_name="My Program")

        assert model.program_name == "My Program"
        assert model.model_dump() == {"program_name": "My Program"}
        assert model.model_dump(by_alias=True) == {"programName": "My Program"}

    def test__camel_case_input__remains_backward_compatible(self):
        """Test that legacy camelCase input remains valid."""
        model = ExampleJsonModel.model_validate({"programName": "My Program"})

        assert model.program_name == "My Program"

    def test__snake_case_input__wins_when_both_names_are_provided(self):
        """Test that Python field names remain the primary input form."""
        model = ExampleJsonModel.model_validate(
            {
                "program_name": "Preferred Program",
                "programName": "Legacy Program",
            }
        )

        assert model.program_name == "Preferred Program"

    def test__explicit_alias_signature__uses_snake_case_field_names(self):
        """Test that explicit aliases preserve snake_case constructor signatures."""
        assert str(signature(ExampleExplicitAliasJsonModel)) == (
            "(*, program_name: str, session_id: str) -> None"
        )
        assert ExampleExplicitAliasJsonModel.model_fields["session_id"].alias is None

    def test__explicit_alias__accepts_both_input_names_and_serializes_wire_name(self):
        """Test that explicit aliases accept Python and wire names and serialize wire names."""
        snake_case_model = ExampleExplicitAliasJsonModel(
            program_name="My Program",
            session_id="session-1",
        )
        camel_case_model = ExampleExplicitAliasJsonModel.model_validate(
            {"program_name": "My Program", "id": "session-2"}
        )

        assert snake_case_model.session_id == "session-1"
        assert snake_case_model.model_dump(by_alias=True) == {
            "programName": "My Program",
            "id": "session-1",
        }
        assert camel_case_model.session_id == "session-2"

    def test__identical_wire_and_python_names__do_not_create_duplicate_aliases(self):
        """Test that identical Python and wire names remain valid for discriminated unions."""

        class NotebookExecution(JsonModel):
            type: Literal["NOTEBOOK"] = Field(default="NOTEBOOK")

        class JobExecution(JsonModel):
            type: Literal["JOB"] = Field(default="JOB")

        execution_type = Annotated[
            NotebookExecution | JobExecution,
            Field(discriminator="type"),
        ]
        adapter = TypeAdapter(list[execution_type])

        parsed = cast(
            list[NotebookExecution | JobExecution],
            adapter.validate_python(
                [
                    {"type": "NOTEBOOK"},
                    {"type": "JOB"},
                ]
            ),
        )

        assert [item.type for item in parsed] == ["NOTEBOOK", "JOB"]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_minion_id.py sha256=54874ffb1be11d033fbd45a661cdcd690eb05934d72d949c0bca6b1eead58e5f bytes=5611 -->
## FILE: tests/core/test_minion_id.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_minion_id.py`
- sha256: `54874ffb1be11d033fbd45a661cdcd690eb05934d72d949c0bca6b1eead58e5f`
- bytes: 5611

````python
# -*- coding: utf-8 -*-

"""Tests for read_minion_id helper function."""

from pathlib import Path
from unittest import mock

import pytest
from nisystemlink.clients.core.helpers._minion_id import read_minion_id


@pytest.fixture
def mock_path_constants():
    """Fixture to mock PathConstants."""
    with mock.patch(
        "nisystemlink.clients.core.helpers._minion_id.PathConstants"
    ) as mock_constants:
        yield mock_constants


@pytest.fixture
def mock_minion_id_path(mock_path_constants):
    """Fixture to set up the mock path structure for minion_id file.

    Returns a callable that accepts an exists parameter to configure
    whether the path exists.
    """

    def _create_mock_path(exists=True):
        mock_minion_id_path = mock.Mock(spec=Path)
        mock_minion_id_path.exists.return_value = exists

        # Set up the path chain: salt_data_directory / "conf" / "minion_id"
        mock_conf_path = mock.Mock(spec=Path)
        mock_conf_path.__truediv__ = mock.Mock(return_value=mock_minion_id_path)

        mock_salt_dir = mock.Mock(spec=Path)
        mock_salt_dir.__truediv__ = mock.Mock(return_value=mock_conf_path)

        mock_path_constants.salt_data_directory = mock_salt_dir

        return mock_minion_id_path

    return _create_mock_path


class TestReadMinionId:
    """Test cases for read_minion_id function."""

    def test__minion_id_file_exists__returns_content(self, mock_minion_id_path):
        """Test that the minion ID is read correctly when the file exists."""
        # Arrange
        expected_minion_id = "test-minion-123"
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open and read
        mock_open = mock.mock_open(read_data=f"{expected_minion_id}\n")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result == expected_minion_id
        minion_path.exists.assert_called_once()
        mock_open.assert_called_once_with(minion_path, "r", encoding="utf-8")

    def test__minion_id_file_exists_with_whitespace__returns_stripped_content(
        self, mock_minion_id_path
    ):
        """Test that the minion ID is stripped of leading/trailing whitespace."""
        # Arrange
        expected_minion_id = "test-minion-456"
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open with extra whitespace
        mock_open = mock.mock_open(read_data=f"  {expected_minion_id}  \n\t")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result == expected_minion_id
        minion_path.exists.assert_called_once()

    def test__minion_id_file_does_not_exist__returns_none(self, mock_minion_id_path):
        """Test that None is returned when the minion_id file does not exist."""
        # Arrange
        minion_path = mock_minion_id_path(exists=False)

        # Act
        result = read_minion_id()

        # Assert
        assert result is None
        minion_path.exists.assert_called_once()

    def test__minion_id_file_has_oserror__returns_none(self, mock_minion_id_path):
        """Test that None is returned when an OSError occurs reading the file."""
        # Arrange
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open to raise OSError
        mock_open = mock.mock_open()
        mock_open.side_effect = OSError("File access error")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result is None
        minion_path.exists.assert_called_once()

    def test__minion_id_file_has_permission_error__returns_none(
        self, mock_minion_id_path
    ):
        """Test that None is returned when a PermissionError occurs reading the file."""
        # Arrange
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open to raise PermissionError
        mock_open = mock.mock_open()
        mock_open.side_effect = PermissionError("Permission denied")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result is None
        minion_path.exists.assert_called_once()

    def test__minion_id_file_is_empty__returns_empty_string(self, mock_minion_id_path):
        """Test that an empty string is returned when the file is empty."""
        # Arrange
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open with empty content
        mock_open = mock.mock_open(read_data="")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result == ""
        minion_path.exists.assert_called_once()

    def test__minion_id_file_only_whitespace__returns_empty_string(
        self, mock_minion_id_path
    ):
        """Test that an empty string is returned when the file contains only whitespace."""
        # Arrange
        minion_path = mock_minion_id_path(exists=True)

        # Mock the file open with only whitespace
        mock_open = mock.mock_open(read_data="   \n\t  \n")

        # Act
        with mock.patch("builtins.open", mock_open):
            result = read_minion_id()

        # Assert
        assert result == ""
        minion_path.exists.assert_called_once()
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_multipart_retry.py sha256=c8f4db713e6bd98e0f8ccb13fe682458236deab1dbf5e3ec50d552007fb96192 bytes=11221 -->
## FILE: tests/core/test_multipart_retry.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_multipart_retry.py`
- sha256: `c8f4db713e6bd98e0f8ccb13fe682458236deab1dbf5e3ec50d552007fb96192`
- bytes: 11221

````python
import io
from typing import Any, cast

import pytest
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core._uplink._base_client import _handle_http_status
from nisystemlink.clients.core._uplink._multipart_retry import (
    _RetryableMultipartCleanupTemplate,
    _RetryableMultipartRequestTemplate,
    retryable_multipart_request,
)
from requests import Response
from uplink import Consumer, Part, post, retry
from uplink.clients.io import CompositeRequestTemplate
from uplink.clients.io import state as uplink_state
from uplink.clients.io.interfaces import RequestTemplate


class _NonSeekableStream:
    def seekable(self) -> bool:
        return False

    def seek(self, offset: int) -> None:
        raise AssertionError("seek should not be called for non-seekable streams")


class _FailingSeekStream:
    def __init__(self, data: bytes = b"artifact") -> None:
        self._buffer = io.BytesIO(data)

    def read(self, size: int = -1) -> bytes:
        return self._buffer.read(size)

    def seek(self, offset: int) -> None:
        raise OSError("cannot rewind")


class _StaticTransitionTemplate(RequestTemplate):
    def __init__(self, response_transition=None, exception_transition=None) -> None:
        self._response_transition = response_transition
        self._exception_transition = exception_transition

    def after_response(self, request, response):
        return self._response_transition

    def after_exception(self, request, exc_type, exc_val, exc_tb):
        return self._exception_transition


@retry(
    when=retry.when.status(429),
    stop=retry.stop.after_attempt(2),
    backoff=retry.backoff.fixed(0),
)
class _MultipartRetryTestConsumer(Consumer):
    def __init__(self):
        super().__init__(
            base_url="https://example.com/",
            hooks=[_handle_http_status],
        )

    @retryable_multipart_request()
    @post("upload", args=[Part("artifact")])
    def upload(self, artifact):
        pass


class TestRetryableMultipartRequestTemplate:
    def test__before_request_on_initial_attempt__does_not_rewind_parts(self):
        direct_part = io.BytesIO(b"direct")
        direct_part.seek(3)
        tuple_part = io.BytesIO(b"tuple")
        tuple_part.seek(2)
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "direct": direct_part,
                    "tuple": ("tuple.bin", tuple_part, "application/octet-stream"),
                }
            },
        )

        _RetryableMultipartRequestTemplate().before_request(request)

        assert direct_part.tell() == 3
        assert tuple_part.tell() == 2

    def test__before_request_on_retry__rewinds_parts(self):
        direct_part = io.BytesIO(b"direct")
        direct_part.seek(3)
        tuple_part = io.BytesIO(b"tuple")
        tuple_part.seek(2)
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "direct": direct_part,
                    "tuple": ("tuple.bin", tuple_part, "application/octet-stream"),
                }
            },
        )
        template = _RetryableMultipartRequestTemplate()

        template.before_request(request)
        direct_part.read()
        tuple_part.read()
        template.before_request(request)

        assert direct_part.tell() == 0
        assert tuple_part.tell() == 0

    def test__before_request_with_non_seekable_parts__does_not_raise(self):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "non_seekable": _NonSeekableStream(),
                    "failing_seek": _FailingSeekStream(),
                }
            },
        )
        template = _RetryableMultipartRequestTemplate()

        template.before_request(request)
        template.before_request(request)

    def test__before_request_when_rewind_fails_after_response__finishes_with_saved_response(
        self,
    ):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "failing_seek": _FailingSeekStream(),
                }
            },
        )
        response = Response()
        response.status_code = 429
        response.url = "https://example.com/upload"
        template = _RetryableMultipartRequestTemplate()

        template.before_request(request)
        template.after_response(request, response)
        action = template.before_request(request)

        assert action is not None
        next_state = action(uplink_state.BeforeRequest(request))
        assert isinstance(next_state, uplink_state.Finish)
        assert next_state.response is response
        request_id = id(request)
        assert request_id not in template._attempted_request_ids
        assert request_id not in template._responses_by_request_id
        assert request_id not in template._exceptions_by_request_id

    def test__terminal_response_after_retry_pipeline__clears_saved_retry_state(self):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "artifact": ("artifact.bin", io.BytesIO(b"artifact")),
                }
            },
        )
        response = Response()
        response.status_code = 200
        response.url = "https://example.com/upload"
        template = _RetryableMultipartRequestTemplate()
        composite = CompositeRequestTemplate(
            [
                template,
                _StaticTransitionTemplate(),
                _RetryableMultipartCleanupTemplate(template),
            ]
        )

        template.before_request(request)
        composite.after_response(request, response)

        request_id = id(request)
        assert request_id not in template._attempted_request_ids
        assert request_id not in template._responses_by_request_id
        assert request_id not in template._exceptions_by_request_id

    def test__retry_transition_after_response__preserves_saved_retry_state(self):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "artifact": ("artifact.bin", io.BytesIO(b"artifact")),
                }
            },
        )
        response = Response()
        response.status_code = 503
        response.url = "https://example.com/upload"
        retry_transition = object()
        template = _RetryableMultipartRequestTemplate()
        composite = CompositeRequestTemplate(
            [
                template,
                _StaticTransitionTemplate(response_transition=retry_transition),
                _RetryableMultipartCleanupTemplate(template),
            ]
        )

        template.before_request(request)

        assert composite.after_response(request, response) is retry_transition

        request_id = id(request)
        assert request_id in template._attempted_request_ids
        assert template._responses_by_request_id[request_id] is response
        assert request_id not in template._exceptions_by_request_id

    def test__terminal_exception_after_retry_pipeline__clears_saved_retry_state(self):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "artifact": ("artifact.bin", io.BytesIO(b"artifact")),
                }
            },
        )
        exception = RuntimeError("boom")
        template = _RetryableMultipartRequestTemplate()
        composite = CompositeRequestTemplate(
            [
                template,
                _StaticTransitionTemplate(),
                _RetryableMultipartCleanupTemplate(template),
            ]
        )

        template.before_request(request)
        composite.after_exception(request, RuntimeError, exception, None)

        request_id = id(request)
        assert request_id not in template._attempted_request_ids
        assert request_id not in template._responses_by_request_id
        assert request_id not in template._exceptions_by_request_id

    def test__before_request_on_retry_with_string_only_parts__allows_retry(self):
        request = (
            "POST",
            "https://example.com/upload",
            {
                "files": {
                    "workspace": "workspace-id",
                    "metadata": (None, '{"name": "example"}'),
                }
            },
        )
        response = Response()
        response.status_code = 429
        response.url = "https://example.com/upload"
        template = _RetryableMultipartRequestTemplate()

        template.before_request(request)
        template.after_response(request, response)
        action = template.before_request(request)

        assert action is None


class TestRetryableMultipartRequestIntegration:
    @responses.activate
    def test__upload_with_unrewindable_stream_after_rate_limit__raises_original_api_exception(
        self,
    ):
        responses.post("https://example.com/upload", status=429)
        consumer = _MultipartRetryTestConsumer()

        with pytest.raises(ApiException) as exc_info:
            consumer.upload(
                artifact=(
                    "artifact.bin",
                    _FailingSeekStream(),
                    "application/octet-stream",
                )
            )

        assert exc_info.value.http_status_code == 429
        assert len(responses.calls) == 1

    @responses.activate
    def test__upload_with_rewindable_stream_after_rate_limit__retries_and_succeeds(
        self,
    ):
        request_bodies = []

        def response_callback(request):
            body = request.body
            if isinstance(body, str):
                body = body.encode("utf-8")
            request_bodies.append(body)

            if len(request_bodies) == 1:
                return (429, {}, "")
            return (200, {}, "ok")

        responses.add_callback(
            responses.POST,
            "https://example.com/upload",
            callback=response_callback,
        )
        consumer = _MultipartRetryTestConsumer()
        artifact_content = b"rewindable-artifact"

        consumer.upload(
            artifact=(
                "artifact.bin",
                io.BytesIO(artifact_content),
                "application/octet-stream",
            )
        )

        assert len(responses.calls) == 2
        last_response = cast(Any, responses.calls[-1]).response
        assert last_response is not None
        assert last_response.status_code == 200
        assert len(request_bodies) == 2
        assert artifact_content in request_bodies[0]
        assert artifact_content in request_bodies[1]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_pagination.py sha256=812b1a77789f2398bc3d142ccbcb6d2a3dd58eb508a13291c8fe964d177d1d6d bytes=8394 -->
## FILE: tests/core/test_pagination.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_pagination.py`
- sha256: `812b1a77789f2398bc3d142ccbcb6d2a3dd58eb508a13291c8fe964d177d1d6d`
- bytes: 8394

````python
# -*- coding: utf-8 -*-
"""Tests for the pagination helper function."""

from typing import Any, List
from unittest.mock import MagicMock

import pytest
from nisystemlink.clients.core.helpers import paginate


class MockResponseWithItems:
    """Mock API response object with 'items' field for testing pagination."""

    def __init__(self, items: List[Any], continuation_token: str | None = None):
        self.items = items
        self.continuation_token = continuation_token


class MockResponseWithResults:
    """Mock API response object with 'results' field for testing pagination."""

    def __init__(self, results: List[Any], continuation_token: str | None = None):
        self.results = results
        self.continuation_token = continuation_token


class TestPaginate:
    """Tests for the paginate helper function."""

    def test__paginate_single_page__yields_all_items(self):
        """Test pagination with a single page of results."""
        # Arrange
        items = [1, 2, 3, 4, 5]
        mock_fetch = MagicMock(return_value=MockResponseWithItems(items, None))

        # Act
        result = list(paginate(mock_fetch, "items"))

        # Assert
        assert result == items
        assert mock_fetch.call_count == 1
        mock_fetch.assert_called_with(continuation_token=None)

    def test__paginate_multiple_pages__yields_all_items_in_order(self):
        """Test pagination with multiple pages."""
        # Arrange
        page1_items = [1, 2, 3]
        page2_items = [4, 5, 6]
        page3_items = [7, 8, 9]

        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems(page1_items, "token1"),
                MockResponseWithItems(page2_items, "token2"),
                MockResponseWithItems(page3_items, None),
            ]
        )

        # Act
        result = list(paginate(mock_fetch, "items"))

        # Assert
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert mock_fetch.call_count == 3
        assert mock_fetch.call_args_list[0][1]["continuation_token"] is None
        assert mock_fetch.call_args_list[1][1]["continuation_token"] == "token1"
        assert mock_fetch.call_args_list[2][1]["continuation_token"] == "token2"

    def test__paginate_with_results_field__yields_all_items(self):
        """Test pagination with 'results' as the items field name."""
        # Arrange
        page1_results = ["a", "b"]
        page2_results = ["c", "d"]

        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithResults(page1_results, "next1"),
                MockResponseWithResults(page2_results, None),
            ]
        )

        # Act
        result = list(paginate(mock_fetch, items_field="results"))

        # Assert
        assert result == ["a", "b", "c", "d"]
        assert mock_fetch.call_count == 2

    def test__paginate_with_additional_kwargs__passes_kwargs_to_fetch(self):
        """Test that additional keyword arguments are passed to the fetch function."""
        # Arrange
        items = [1, 2, 3]
        mock_fetch = MagicMock(return_value=MockResponseWithItems(items, None))

        # Act
        result = list(
            paginate(
                mock_fetch, "items", take=10, filter="status==PASSED", return_count=True
            )
        )

        # Assert
        assert result == items
        mock_fetch.assert_called_once_with(
            continuation_token=None, take=10, filter="status==PASSED", return_count=True
        )

    def test__paginate_empty_results__returns_empty(self):
        """Test pagination with no results."""
        # Arrange
        mock_fetch = MagicMock(return_value=MockResponseWithItems([], None))

        # Act
        result = list(paginate(mock_fetch, "items"))

        # Assert
        assert result == []
        assert mock_fetch.call_count == 1

    def test__paginate_empty_page_in_middle__yields_only_non_empty_pages(self):
        """Test pagination when a middle page is empty."""
        # Arrange
        page1_items = [1, 2, 3]
        page2_items = []
        page3_items = [4, 5]

        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems(page1_items, "token1"),
                MockResponseWithItems(page2_items, "token2"),
                MockResponseWithItems(page3_items, None),
            ]
        )

        # Act
        result = list(paginate(mock_fetch, "items"))

        # Assert
        assert result == [1, 2, 3, 4, 5]
        assert mock_fetch.call_count == 3

    def test__paginate_generator__can_be_used_in_for_loop(self):
        """Test that paginate works as expected in a for loop."""
        # Arrange
        page1_items = [1, 2]
        page2_items = [3, 4]
        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems(page1_items, "token1"),
                MockResponseWithItems(page2_items, None),
            ]
        )

        # Act
        collected = []
        for item in paginate(mock_fetch, "items"):
            collected.append(item * 2)

        # Assert
        assert collected == [2, 4, 6, 8]

    def test__paginate_lazy_evaluation__only_fetches_as_needed(self):
        """Test that pagination is lazy and doesn't fetch all pages immediately."""
        # Arrange
        page1_items = [1, 2, 3]
        page2_items = [4, 5, 6]
        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems(page1_items, "token1"),
                MockResponseWithItems(page2_items, None),
            ]
        )

        # Act
        gen = paginate(mock_fetch, "items")
        assert mock_fetch.call_count == 0  # Nothing called yet

        first_item = next(gen)
        assert first_item == 1
        assert mock_fetch.call_count == 1  # First page fetched

        # Consume rest of first page
        next(gen)  # 2
        next(gen)  # 3

        # First page exhausted, but second page not yet fetched
        assert mock_fetch.call_count == 1

        # Fetch first item of second page
        fourth_item = next(gen)
        assert fourth_item == 4
        assert mock_fetch.call_count == 2  # Second page fetched

    def test__paginate_with_kwargs_persisted_across_pages__kwargs_used_on_all_calls(
        self,
    ):
        """Test that kwargs are passed to all fetch function calls."""
        # Arrange
        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems([1, 2], "token1"),
                MockResponseWithItems([3, 4], None),
            ]
        )

        # Act
        list(paginate(mock_fetch, "items", take=100, filter="active==true"))

        # Assert
        for call in mock_fetch.call_args_list:
            assert call[1]["take"] == 100
            assert call[1]["filter"] == "active==true"

    def test__paginate_missing_items_field__yields_nothing(self):
        """Test pagination when the items field doesn't exist on the response."""
        # Arrange
        mock_response = MockResponseWithItems([], None)
        # Remove the items field
        delattr(mock_response, "items")
        mock_fetch = MagicMock(return_value=mock_response)

        # Act
        result = list(paginate(mock_fetch, "items"))

        # Assert
        assert result == []
        assert mock_fetch.call_count == 1

    def test__paginate_continuation_token_unchanged__raises_runtime_error(self):
        """Test that an error is raised if the continuation token doesn't change."""
        # Arrange
        # First call returns token1, second call returns token1 again (infinite loop)
        mock_fetch = MagicMock(
            side_effect=[
                MockResponseWithItems([1, 2], "token1"),
                MockResponseWithItems(
                    [3, 4], "token1"
                ),  # Same token - should raise error
            ]
        )

        # Act & Assert
        with pytest.raises(RuntimeError, match="Continuation token did not change"):
            list(paginate(mock_fetch, "items"))

        # Should have made 2 calls before detecting the issue
        assert mock_fetch.call_count == 2
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/core/test_partial_success.py sha256=62e3149031a446d027d88dacfe4749b95d307561b6c7e1046ff0be9f2993c9a5 bytes=4489 -->
## FILE: tests/core/test_partial_success.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/core/test_partial_success.py`
- sha256: `62e3149031a446d027d88dacfe4749b95d307561b6c7e1046ff0be9f2993c9a5`
- bytes: 4489

````python
import pytest
from nisystemlink.clients.core import ApiError, ApiException
from nisystemlink.clients.core.helpers._partial_success import (
    unwrap_single_item_partial_success,
)


class _FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def model_dump(self, *, mode, by_alias):
        assert mode == "json"
        assert by_alias is True
        return self._payload


def test__unwrap_single_item_partial_success__returns_first_item():
    """Return the first item when the partial-success response is successful."""
    response = _FakeResponse({"items": ["created-item"]})

    created_item = unwrap_single_item_partial_success(
        response=response,
        items=["created-item"],
        failed=None,
        error=None,
        failure_message="Failed to create item.",
        empty_message="Server returned no created items.",
    )

    assert created_item == "created-item"


def test__unwrap_single_item_partial_success__raises_on_partial_failure():
    """Raise ApiException when the response reports a structured partial failure."""
    response = _FakeResponse(
        {
            "items": [],
            "failed": [{"id": "request-id"}],
            "error": {"message": "Create failed"},
        }
    )
    error = ApiError(message="Create failed")

    with pytest.raises(ApiException) as exc_info:
        unwrap_single_item_partial_success(
            response=response,
            items=[],
            failed=[{"id": "request-id"}],
            error=error,
            failure_message="Failed to create item.",
            empty_message="Server returned no created items.",
        )

    assert exc_info.value.error == error
    assert exc_info.value.response_data == response.model_dump(
        mode="json", by_alias=True
    )


def test__unwrap_single_item_partial_success__unwraps_single_inner_error():
    """Raise ApiException with the inner error for one-or-more wrappers."""
    response = _FakeResponse(
        {
            "items": [],
            "failed": [{"id": "request-id"}],
            "error": {"message": "One or more errors occurred."},
        }
    )
    inner_error = ApiError(message="Create failed")
    error = ApiError(
        name="Skyline.OneOrMoreErrorsOccurred",
        code=-251041,
        message="One or more errors occurred.",
        inner_errors=[inner_error],
    )

    with pytest.raises(ApiException) as exc_info:
        unwrap_single_item_partial_success(
            response=response,
            items=[],
            failed=[{"id": "request-id"}],
            error=error,
            failure_message="Failed to create item.",
            empty_message="Server returned no created items.",
        )

    assert exc_info.value.error == inner_error
    assert exc_info.value.response_data == response.model_dump(
        mode="json", by_alias=True
    )


def test__unwrap_single_item_partial_success__raises_on_empty_success_payload():
    """Raise ApiException when the response succeeds but contains no created item."""
    response = _FakeResponse({"items": []})

    with pytest.raises(
        ApiException, match="Server returned no created items"
    ) as exc_info:
        unwrap_single_item_partial_success(
            response=response,
            items=[],
            failed=None,
            error=None,
            failure_message="Failed to create item.",
            empty_message="Server returned no created items.",
        )

    assert exc_info.value.response_data == response.model_dump(
        mode="json", by_alias=True
    )


def test__unwrap_single_item_partial_success__raises_on_multiple_success_items():
    """Raise ApiException when the response unexpectedly contains multiple items."""
    response = _FakeResponse({"items": ["created-item", "extra-item"]})

    with pytest.raises(
        ApiException, match="Expected exactly one successful item but received 2"
    ) as exc_info:
        unwrap_single_item_partial_success(
            response=response,
            items=["created-item", "extra-item"],
            failed=None,
            error=None,
            failure_message="Failed to create item.",
            empty_message="Server returned no created items.",
        )

    assert exc_info.value.response_data == response.model_dump(
        mode="json", by_alias=True
    )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: tests/integration/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/alarm/test_alarm_client.py sha256=80c252981d11461b661be5bdab86fba22517b2de76c4ed898515a6345fcc5d18 bytes=19597 -->
## FILE: tests/integration/alarm/test_alarm_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/alarm/test_alarm_client.py`
- sha256: `80c252981d11461b661be5bdab86fba22517b2de76c4ed898515a6345fcc5d18`
- bytes: 19597

````python
import uuid
from datetime import datetime, timezone
from typing import Callable, Generator, List

import pytest
from nisystemlink.clients.alarm import AlarmClient
from nisystemlink.clients.alarm.models import (
    AcknowledgeAlarmsResponse,
    AlarmOrderBy,
    AlarmSeverityLevel,
    AlarmTransitionType,
    ClearAlarmTransition,
    CreateOrUpdateAlarmRequest,
    DeleteAlarmsResponse,
    QueryAlarmsWithFilterRequest,
    QueryAlarmsWithFilterResponse,
    SetAlarmTransition,
    TransitionInclusionOption,
)
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> AlarmClient:
    """Fixture to create an AlarmClient instance."""
    return AlarmClient(enterprise_config)


@pytest.fixture
def unique_identifier() -> Callable[[], str]:
    """Unique alarm id for this test."""

    def _unique_identifier() -> str:
        return uuid.uuid1().hex

    return _unique_identifier


@pytest.fixture
def create_alarms(
    client: AlarmClient,
) -> Generator[Callable[[str, int, str], str], None, None]:
    """Fixture to return a factory that creates alarms.

    Returns instance_id (referred to as 'id' in tests) for each created alarm.
    """
    created_ids: List[str] = []

    def _create_alarms(
        alarm_id: str,
        severity_level: int = 3,
        condition: str = "Test Condition",
    ) -> str:
        """Create an alarm and return its instance_id."""
        request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=SetAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                severity_level=severity_level,
                condition=condition,
            ),
        )
        id = client.create_or_update_alarm(request)
        if id:
            created_ids.append(id)
        return id

    yield _create_alarms

    if created_ids:
        client.delete_alarms(instance_ids=created_ids)


@pytest.mark.integration
@pytest.mark.enterprise
class TestAlarmClient:

    def test__create_single_alarm__one_alarm_created_with_right_field_values(
        self, client: AlarmClient, unique_identifier: Callable[[], str]
    ):
        alarm_id = unique_identifier()
        occurred_at = datetime.now(timezone.utc)

        # Create alarm with all fields populated
        request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            workspace=None,  # Use default workspace
            transition=SetAlarmTransition(
                occurred_at=occurred_at,
                severity_level=AlarmSeverityLevel.HIGH,
                value="85.5",
                condition="Temperature exceeded threshold",
                short_text="High temp",
                detail_text="Temperature sensor reading exceeded the configured threshold of 80°C",
                keywords=["temperature", "sensor", "critical"],
                properties={"sensor_id": "temp_001", "location": "server_room"},
            ),
            notification_strategy_ids=[],
            created_by="test_automation",
            channel="sensors/temperature/room1",
            resource_type="temperature_sensor",
            display_name="Server Room Temperature",
            description="Monitors temperature in server room",
            keywords=["monitoring", "infrastructure"],
            properties={"department": "IT", "priority": "high"},
        )

        id = client.create_or_update_alarm(request)
        assert id is not None
        assert isinstance(id, str)
        assert len(id) > 0

        # Get alarm and verify all fields
        alarm = client.get_alarm(instance_id=id)
        assert alarm.instance_id == id
        assert alarm.alarm_id == alarm_id
        assert alarm.workspace is not None
        assert alarm.active is True
        assert alarm.clear is False
        assert alarm.acknowledged is False
        assert alarm.acknowledged_at is None
        assert alarm.acknowledged_by is None
        assert alarm.occurred_at is not None
        assert alarm.updated_at is not None
        assert alarm.created_by == "test_automation"
        assert len(alarm.transitions) >= 1
        assert alarm.transition_overflow_count == 0
        assert isinstance(alarm.notification_strategy_ids, List)
        assert alarm.current_severity_level == 3
        assert alarm.highest_severity_level == 3
        assert alarm.most_recent_set_occurred_at is not None
        assert alarm.most_recent_transition_occurred_at is not None
        assert alarm.channel == "sensors/temperature/room1"
        assert alarm.condition == "Temperature exceeded threshold"
        assert alarm.display_name == "Server Room Temperature"
        assert alarm.description == "Monitors temperature in server room"
        assert "monitoring" in alarm.keywords
        assert "infrastructure" in alarm.keywords
        assert isinstance(alarm.notes, List)
        assert "department" in alarm.properties
        assert alarm.properties["department"] == "IT"
        assert alarm.resource_type == "temperature_sensor"

        # Verify transition fields
        transition = alarm.transitions[0]
        assert transition.transition_type == AlarmTransitionType.SET
        assert transition.occurred_at is not None
        assert transition.severity_level == 3
        assert transition.value == "85.5"
        assert transition.condition == "Temperature exceeded threshold"
        assert transition.short_text == "High temp"
        assert (
            transition.detail_text
            == "Temperature sensor reading exceeded the configured threshold of 80°C"
        )
        assert "temperature" in transition.keywords
        assert "sensor_id" in transition.properties

        # Cleanup
        client.delete_alarm(instance_id=id)

    def test__query_alarms_with_all_fields__returns_complete_response(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        # Create two alarms with different severity levels
        alarm_id_1 = unique_identifier()
        alarm_id_2 = unique_identifier()
        create_alarms(alarm_id_1, 3, "Condition 1")
        create_alarms(alarm_id_2, 4, "Condition 2")

        # Add another transition to the first alarm
        update_request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id_1,
            transition=SetAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                severity_level=AlarmSeverityLevel.CRITICAL,
                condition="Condition 3",
            ),
        )
        client.create_or_update_alarm(update_request)

        # Query with all available fields, order by descending, and ALL transitions
        query_request = QueryAlarmsWithFilterRequest(
            filter=f'alarmId="{alarm_id_1}" OR alarmId="{alarm_id_2}"',
            substitutions=None,
            return_most_recently_occurred_only=False,
            transition_inclusion_option=TransitionInclusionOption.ALL,
            reference_time=None,
            take=10,
            order_by=AlarmOrderBy.UPDATED_AT,
            order_by_descending=True,
            continuation_token=None,
            return_count=True,
        )
        query_response: QueryAlarmsWithFilterResponse = client.query_alarms(
            query_request
        )

        # Assert all response fields
        assert query_response is not None
        assert isinstance(query_response.alarms, List)
        assert len(query_response.alarms) == 2
        assert query_response.total_count is not None
        assert query_response.total_count == 2
        assert hasattr(query_response, "continuation_token")

        # Verify order_by_descending works (alarm_id_1 was updated last, should be first)
        for i in range(len(query_response.alarms) - 1):
            assert (
                query_response.alarms[i].updated_at
                >= query_response.alarms[i + 1].updated_at
            )

        # Verify all transitions are included (TransitionInclusionOption.ALL) for alarm_id_1
        alarm_1_result = next(
            a for a in query_response.alarms if a.alarm_id == alarm_id_1
        )
        assert len(alarm_1_result.transitions) == 2

    def test__create_multiple_alarms_and_query_alarms_with_take__only_take_returned(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        create_alarms(unique_identifier(), 3, "Test Condition")
        create_alarms(unique_identifier(), 4, "Test Condition")

        query_request = QueryAlarmsWithFilterRequest(take=1)
        query_response = client.query_alarms(query_request)

        assert query_response is not None
        assert len(query_response.alarms) == 1

    def test__query_alarm_by_alarm_id__matches_expected(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        alarm_id = unique_identifier()
        id = create_alarms(alarm_id, 3, "Test Condition")
        assert id is not None

        query_request = QueryAlarmsWithFilterRequest(
            filter=f'alarmId="{alarm_id}"', return_count=True
        )
        query_response: QueryAlarmsWithFilterResponse = client.query_alarms(
            query_request
        )

        assert query_response.total_count == 1
        assert query_response.alarms[0].alarm_id == alarm_id

    def test__acknowledge_alarm__verifies_all_response_fields(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        # Create multiple alarms
        id1 = create_alarms(unique_identifier(), 3, "Test Condition")
        id2 = create_alarms(unique_identifier(), 4, "Test Condition")
        non_existent_id = unique_identifier()

        # Acknowledge with mix of valid and invalid IDs
        ack_response: AcknowledgeAlarmsResponse = client.acknowledge_alarms(
            instance_ids=[id1, id2, non_existent_id], force_clear=False
        )

        # Assert all response fields
        assert ack_response is not None
        assert isinstance(ack_response.acknowledged, List)
        assert isinstance(ack_response.failed, List)
        assert id1 in ack_response.acknowledged
        assert id2 in ack_response.acknowledged
        assert non_existent_id in ack_response.failed
        assert len(ack_response.acknowledged) == 2
        assert len(ack_response.failed) == 1
        assert hasattr(ack_response, "error")

        # Verify alarms were acknowledged
        alarm1 = client.get_alarm(instance_id=id1)
        assert alarm1.acknowledged is True
        assert alarm1.acknowledged_at is not None
        assert alarm1.acknowledged_by is not None

    def test__acknowledge_alarm_with_force_clear__alarm_cleared(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        id = create_alarms(unique_identifier(), 3, "Test Condition")

        ack_response: AcknowledgeAlarmsResponse = client.acknowledge_alarms(
            instance_ids=[id], force_clear=True
        )

        assert ack_response is not None
        assert id in ack_response.acknowledged

        alarm = client.get_alarm(instance_id=id)
        assert alarm.clear is True

    def test__delete_alarm__returns_none(
        self, client: AlarmClient, unique_identifier: Callable[[], str]
    ):
        alarm_id = unique_identifier()
        request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=SetAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                severity_level=AlarmSeverityLevel.HIGH,
                condition="Test Condition",
            ),
        )
        id = client.create_or_update_alarm(request)

        assert id is not None
        # Delete returns None on success
        result = client.delete_alarm(instance_id=id)
        assert result is None

        # Verify alarm is deleted
        query_request = QueryAlarmsWithFilterRequest(filter=f'alarmId="{alarm_id}"')
        query_response = client.query_alarms(query_request)
        assert len(query_response.alarms) == 0

    def test__delete_alarms__verifies_all_response_fields(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        alarm_id1 = unique_identifier()
        alarm_id2 = unique_identifier()
        # Create multiple alarms with different alarm IDs
        id1 = create_alarms(alarm_id1, 3, "Test Condition")
        id2 = create_alarms(alarm_id2, 4, "Test Condition")
        non_existent_id = unique_identifier()

        # Delete with mix of valid and invalid IDs
        delete_response: DeleteAlarmsResponse = client.delete_alarms(
            instance_ids=[id1, id2, non_existent_id]
        )

        # Assert all response fields
        assert delete_response is not None
        assert isinstance(delete_response.deleted, List)
        assert isinstance(delete_response.failed, List)
        assert id1 in delete_response.deleted
        assert id2 in delete_response.deleted
        assert non_existent_id in delete_response.failed
        assert len(delete_response.deleted) == 2
        assert len(delete_response.failed) == 1
        assert hasattr(delete_response, "error")

        # Verify alarms were deleted
        query_request = QueryAlarmsWithFilterRequest(
            filter=f'alarmId="{alarm_id1}" or alarmId="{alarm_id2}"'
        )
        query_response = client.query_alarms(query_request)
        assert len(query_response.alarms) == 0

    def test__update_alarm_severity__severity_updated(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        alarm_id = unique_identifier()
        create_alarms(alarm_id, 3, "Test Condition")

        update_request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=SetAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                severity_level=AlarmSeverityLevel.CRITICAL,
                condition="Updated Condition",
            ),
        )
        id = client.create_or_update_alarm(update_request)

        assert id is not None
        alarm = client.get_alarm(instance_id=id)
        assert alarm.current_severity_level == AlarmSeverityLevel.CRITICAL

    def test__clear_alarm__alarm_cleared(
        self,
        client: AlarmClient,
        create_alarms: Callable[[str, int, str], str],
        unique_identifier: Callable[[], str],
    ):
        alarm_id = unique_identifier()
        create_alarms(alarm_id, 3, "Test Condition")

        clear_request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=ClearAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                condition="Cleared",
            ),
        )
        id = client.create_or_update_alarm(clear_request)

        assert id is not None
        alarm = client.get_alarm(instance_id=id)
        assert alarm.clear is True

    def test__get_alarm_with_invalid_instance_id__raises_ApiException_NotFound(
        self, client: AlarmClient
    ):
        with pytest.raises(ApiException):
            client.get_alarm(instance_id="invalid_instance_id")

    def test__delete_alarm_with_invalid_instance_id__raises_ApiException_NotFound(
        self, client: AlarmClient
    ):
        with pytest.raises(ApiException):
            client.delete_alarm(instance_id="invalid_instance_id")

    def test__query_alarms_with_invalid_filter_syntax__raises_ApiException_BadRequest(
        self, client: AlarmClient
    ):
        query_request = QueryAlarmsWithFilterRequest(filter="invalid filter syntax")
        with pytest.raises(ApiException, match="Bad Request"):
            client.query_alarms(query_request)

    def test__query_alarm_with_non_existent_alarm_id__returns_empty_list(
        self, client: AlarmClient, unique_identifier: Callable[[], str]
    ):
        non_existent_alarm_id = f"non_existent_{unique_identifier()}"
        query_request = QueryAlarmsWithFilterRequest(
            filter=f'alarmId="{non_existent_alarm_id}"'
        )
        query_response = client.query_alarms(query_request)

        assert query_response is not None
        assert len(query_response.alarms) == 0

    def test__create_alarm_with_invalid_severity__raises_ApiException_BadRequest(
        self, client: AlarmClient, unique_identifier: Callable[[], str]
    ):
        request = CreateOrUpdateAlarmRequest(
            alarm_id=unique_identifier(),
            transition=SetAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                severity_level=-999,
                condition="Invalid Severity",
            ),
        )
        with pytest.raises(ApiException, match="Bad Request"):
            client.create_or_update_alarm(request)

    def test__create_or_update_alarm_with_conflict_and_ignore_conflict_true__returns_none(
        self,
        client: AlarmClient,
        unique_identifier: Callable[[], str],
    ):
        """Test that ignore_conflict=True returns None on 409 Conflict."""
        alarm_id = unique_identifier()

        # Try to clear an alarm that doesn't exist (causes 409)
        clear_request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=ClearAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                condition="Clearing non-existent alarm",
            ),
        )

        # With ignore_conflict=True, should return None instead of raising exception
        result = client.create_or_update_alarm(clear_request, ignore_conflict=True)
        assert result is None

    def test__create_or_update_alarm_with_conflict_and_ignore_conflict_false__raises_exception(
        self,
        client: AlarmClient,
        unique_identifier: Callable[[], str],
    ):
        """Test that ignore_conflict=False (default) raises ApiException on 409 Conflict."""
        alarm_id = unique_identifier()

        # Try to clear an alarm that doesn't exist (causes 409)
        clear_request = CreateOrUpdateAlarmRequest(
            alarm_id=alarm_id,
            transition=ClearAlarmTransition(
                occurred_at=datetime.now(timezone.utc),
                condition="Clearing non-existent alarm",
            ),
        )

        # With ignore_conflict=False (default), should raise ApiException
        with pytest.raises(ApiException) as exc_info:
            client.create_or_update_alarm(clear_request, ignore_conflict=False)
        assert exc_info.value.http_status_code == 409
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/artifact/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/artifact/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/artifact/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/artifact/test_artifact.py sha256=7e2238da9fbe41f1880cebc28625dd702f76a8298d0ec45524f0657e706a3e2a bytes=3502 -->
## FILE: tests/integration/artifact/test_artifact.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/artifact/test_artifact.py`
- sha256: `7e2238da9fbe41f1880cebc28625dd702f76a8298d0ec45524f0657e706a3e2a`
- bytes: 3502

````python
import io
from typing import List

import pytest
import responses
from nisystemlink.clients.artifact import ArtifactClient
from nisystemlink.clients.artifact.models._upload_artifact_response import (
    UploadArtifactResponse,
)
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from responses.registries import OrderedRegistry
from uplink.clients.io import blocking_strategy as uplink_blocking_strategy

BASE_URL = "https://test-api.lifecyclesolutions.ni.com"
DEFAULT_WORKSPACE = "2300760d-38c4-48a1-9acb-800260812337"


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> ArtifactClient:
    """Fixture to create an ArtifactClient instance."""
    return ArtifactClient(enterprise_config)


@pytest.fixture
def create_artifact(client: ArtifactClient):
    """Fixture to return a factory that creates artifact."""
    created_artifact_ids: List[str] = []

    def _create_artifact(
        content: bytes = b"test content",
        cleanup: bool = True,
        workspace: str = DEFAULT_WORKSPACE,
    ):
        # Used the main-test default workspace since the client for creating a workspace has not been added yet
        artifact_stream = io.BytesIO(content)
        response = client.upload_artifact(workspace=workspace, artifact=artifact_stream)
        if cleanup:
            created_artifact_ids.append(response.id)

        return response

    yield _create_artifact

    for artifact_id in created_artifact_ids:
        client.delete_artifact(artifact_id)


@pytest.mark.integration
@pytest.mark.enterprise
class TestArtifact:

    def test__upload_artifact__artifact_uploaded(
        self, client: ArtifactClient, create_artifact
    ):
        upload_response: UploadArtifactResponse = create_artifact()

        assert upload_response is not None
        assert upload_response.id is not None

    def test__upload_artifact_after_rate_limit_retry__artifact_uploaded(
        self, create_artifact, monkeypatch: pytest.MonkeyPatch
    ):
        monkeypatch.setattr(uplink_blocking_strategy.time, "sleep", lambda _: None)

        with responses.RequestsMock(registry=OrderedRegistry) as request_mock:
            request_mock.add(
                responses.POST,
                f"{BASE_URL}/ninbartifact/v1/artifacts",
                status=429,
            )
            request_mock.add_passthru(f"{BASE_URL}/ninbartifact/v1/artifacts")

            upload_response: UploadArtifactResponse = create_artifact()

        assert upload_response is not None
        assert upload_response.id is not None

    def test__download_artifact__artifact_downloaded(
        self, client: ArtifactClient, create_artifact
    ):
        artifact_content = b"test content"

        upload_response: UploadArtifactResponse = create_artifact(
            content=artifact_content
        )
        artifact_id = upload_response.id
        download_response = client.download_artifact(artifact_id)

        assert download_response is not None
        assert download_response.read() == artifact_content

    def test__delete_artifact__artifact_deleted(
        self, client: ArtifactClient, create_artifact
    ):
        upload_response: UploadArtifactResponse = create_artifact(cleanup=False)
        artifact_id = upload_response.id

        delete_response = client.delete_artifact(artifact_id)

        assert delete_response is None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/assetmanagement/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/assetmanagement/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/assetmanagement/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/assetmanagement/test_asset_management.py sha256=8588f8c9a046e2f372cf2e742fef02ba247ee1c131ee5fd1946140a17c46e869 bytes=22487 -->
## FILE: tests/integration/assetmanagement/test_asset_management.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/assetmanagement/test_asset_management.py`
- sha256: `8588f8c9a046e2f372cf2e742fef02ba247ee1c131ee5fd1946140a17c46e869`
- bytes: 22487

````python
from datetime import datetime, timezone
from typing import Callable, Generator, List
from uuid import uuid4

import pytest
from nisystemlink.clients.assetmanagement import AssetManagementClient
from nisystemlink.clients.assetmanagement.models import (
    Asset,
    AssetBusType,
    AssetDiscoveryType,
    AssetField,
    AssetIdentification,
    AssetLocationForCreate,
    AssetPresence,
    AssetPresenceStatus,
    AssetType,
    CreateAssetRequest,
    CreateAssetsPartialSuccessResponse,
    ExternalCalibration,
    QueryAssetsRequest,
    QueryAssetsResponse,
    QueryAssetUtilizationHistoryRequest,
    SelfCalibration,
    StartUtilizationRequest,
    TemperatureSensor,
    UtilizationOrderBy,
)
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration

# Type aliases for fixtures
CreateAssetFixture = Callable[
    [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
]
StartUtilizationFixture = Callable[[str, List[Asset], str, str, str, str], None]


@pytest.fixture
def create_asset(
    client: AssetManagementClient,
) -> Generator[CreateAssetFixture, None, None]:
    """Fixture to return a factory that creates assets."""
    responses: List[CreateAssetsPartialSuccessResponse] = []

    def _create_assets(
        new_assets: List[CreateAssetRequest],
    ) -> CreateAssetsPartialSuccessResponse:
        response = client.create_assets(assets=new_assets)
        responses.append(response)
        return response

    yield _create_assets

    created_assets: List[Asset] = []
    for response in responses:
        if response.assets:
            created_assets = created_assets + response.assets
    client.delete_assets(
        ids=[asset.id for asset in created_assets if asset.id is not None]
    )


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> AssetManagementClient:
    """Fixture to create an AssetManagementClient instance."""
    return AssetManagementClient(enterprise_config)


@pytest.fixture
def unique_identifier() -> str:
    """Fixture to generate a unique identifier using UUID."""
    return str(uuid4())


@pytest.fixture
def start_utilization(
    client: AssetManagementClient,
) -> Generator[StartUtilizationFixture, None, None]:
    """Fixture to start utilization and automatically clean up."""
    started_utilizations: List[str] = []

    def _start_utilization(
        utilization_id: str,
        assets: List[Asset],
        minion_id: str,
        task_name: str,
        category: str,
        user_name: str,
    ) -> None:
        asset_identifications = [
            AssetIdentification(
                model_name=asset.model_name,
                model_number=asset.model_number,
                serial_number=asset.serial_number,
                vendor_name=asset.vendor_name,
                vendor_number=asset.vendor_number,
                bus_type=asset.bus_type,
            )
            for asset in assets
        ]
        start_request = StartUtilizationRequest(
            utilization_identifier=utilization_id,
            minion_id=minion_id,
            asset_identifications=asset_identifications,
            utilization_category=category,
            task_name=task_name,
            user_name=user_name,
            utilization_timestamp=datetime.now(),
        )
        client.start_utilization(request=start_request)
        started_utilizations.append(utilization_id)

    yield _start_utilization

    # Cleanup: end all started utilizations
    if started_utilizations:
        client.end_utilization(
            ids=started_utilizations,
            timestamp=datetime.now(),
        )


@pytest.mark.integration
@pytest.mark.enterprise
class TestAssetManagement:
    """Integration tests for the asset management client."""

    _workspace = "2300760d-38c4-48a1-9acb-800260812337"
    """Use the main-test default workspace until workspace creation is supported."""

    _create_assets_request = [
        CreateAssetRequest(
            model_name="python integration test 1",
            serial_number="01BB8",
            vendor_name="NI",
            vendor_number=4244,
            bus_type=AssetBusType.ACCESSORY,
            name="Python Integration Tests 1",
            asset_type=AssetType.DEVICE_UNDER_TEST,
            firmware_version="A1",
            hardware_version="12A",
            visa_resource_name="vs-3144",
            temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
            supports_self_calibration=True,
            supports_external_calibration=True,
            custom_calibration_interval=24,
            self_calibration=SelfCalibration(
                temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
                is_limited=False,
                date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
            ),
            is_ni_asset=True,
            workspace=_workspace,
            location=AssetLocationForCreate(
                state=AssetPresence(asset_presence=AssetPresenceStatus.PRESENT)
            ),
            external_calibration=ExternalCalibration(
                temperature_sensors=[TemperatureSensor(name="Sensor0", reading=25.8)],
                date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
                recommended_interval=10,
                next_recommended_date=datetime(
                    2023, 11, 14, 20, 42, 11, 583000, tzinfo=timezone.utc
                ),
                next_custom_due_date=datetime(
                    2024, 11, 14, 20, 42, 11, 583000, tzinfo=timezone.utc
                ),
                resolved_due_date=datetime(2022, 6, 7, 18, 58, 5, tzinfo=timezone.utc),
            ),
            properties={"Key1": "Value1"},
            keywords=["Keyword1"],
            discovery_type=AssetDiscoveryType.AUTOMATIC,
            file_ids=["608a5684800e325b48837c2a"],
            supports_self_test=True,
            supports_reset=True,
            part_number="A1234",
        )
    ]
    """CreateAssetRequest object"""

    def test__create_asset__returns_created_asset(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
    ):
        self._create_assets_request[0].model_number = 101
        create_response = create_asset(self._create_assets_request)

        asset_id = (
            create_response.assets[0].id
            if create_response.assets and create_response.assets[0].id
            else None
        )

        assert asset_id is not None

        assert create_response is not None
        assets = create_response.assets or []
        assert len(assets) == 1
        asset_id = assets[0].id
        assert asset_id is not None

    def test__link_files__link_succeded(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
    ):
        self._create_assets_request[0].model_number = 101
        create_response = create_asset(self._create_assets_request)

        asset_id = (
            create_response.assets[0].id
            if create_response.assets and create_response.assets[0].id
            else None
        )

        assert asset_id is not None

        file_ids = ["608a5684800e325b48837c2a"]
        link_files_response = client.link_files(asset_id=asset_id, file_ids=file_ids)

        assert link_files_response is None

    def test__delete_asset__returns_deleted_asset(self, client: AssetManagementClient):
        self._create_assets_request[0].model_number = 102
        create_response: CreateAssetsPartialSuccessResponse = client.create_assets(
            assets=self._create_assets_request
        )
        asset_id = (
            create_response.assets[0].id
            if create_response.assets and create_response.assets[0].id
            else None
        )

        assert asset_id is not None

        delete_response = client.delete_assets(ids=[asset_id])

        assert delete_response is not None
        assert delete_response.ids is not None
        assert len(delete_response.ids) == 1
        assert delete_response.ids[0] == asset_id

    def test__query_assets_with_take_value__returns_specific_number_of_assets(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
    ):
        self._create_assets_request[0].model_number = 103
        create_assets_response = create_asset(self._create_assets_request)

        assert create_assets_response is not None
        assert create_assets_response.assets is not None
        assert len(create_assets_response.assets) == 1

        asset_id = (
            create_assets_response.assets[0].id
            if create_assets_response.assets and create_assets_response.assets[0].id
            else None
        )

        query_assets_request = QueryAssetsRequest(
            skip=0, take=1, return_count=True, filter=f'id = "{asset_id}"'
        )

        response: QueryAssetsResponse = client.query_assets(query=query_assets_request)

        assert response is not None
        assert response.assets is not None and len(response.assets) == 1
        assert response.total_count is not None and response.total_count == 1

    def test_query_assets_with_projections__returns_the_assets_with_projected_properties(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
    ):
        self._create_assets_request[0].model_number = 103
        create_assets_response = create_asset(self._create_assets_request)

        assert create_assets_response is not None
        assert create_assets_response.assets is not None
        assert len(create_assets_response.assets) == 1

        asset_id = (
            create_assets_response.assets[0].id
            if create_assets_response.assets and create_assets_response.assets[0].id
            else None
        )
        query_asset = QueryAssetsRequest(
            filter=f'id = "{asset_id}"',
            projection=[AssetField.ID, AssetField.NAME],
            take=1,
        )
        response = client.query_assets(query=query_asset)

        assert response is not None
        assert response.assets is not None
        assert all(
            asset.id is not None
            and asset.name is not None
            and asset.bus_type is None
            and asset.calibration_status is None
            and asset.custom_calibration_interval is None
            and asset.discovery_type is None
            and asset.external_calibration is None
            and asset.file_ids is None
            and asset.firmware_version is None
            and asset.hardware_version is None
            and asset.is_ni_asset is None
            and asset.is_system_controller is None
            and asset.keywords is None
            and asset.last_updated_timestamp is None
            and asset.location is None
            and asset.model_name is None
            and asset.model_number is None
            and asset.asset_type is None
            and asset.out_for_calibration is None
            and asset.part_number is None
            and asset.properties is None
            and asset.self_calibration is None
            and asset.serial_number is None
            and asset.supports_external_calibration is None
            and asset.supports_reset is None
            and asset.supports_self_calibration is None
            and asset.supports_self_test is None
            and asset.temperature_sensors is None
            and asset.vendor_name is None
            and asset.vendor_number is None
            and asset.visa_resource_name is None
            and asset.workspace is None
            for asset in response.assets
        )

    def test__start_utilization__returns_success_response(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
        unique_identifier: str,
        start_utilization: Callable[[str, List[Asset], str, str, str, str], None],
    ):
        # Create an asset to use for utilization tracking
        self._create_assets_request[0].model_number = 105
        create_response = create_asset(self._create_assets_request)

        assert create_response.assets is not None and len(create_response.assets) == 1
        created_asset = create_response.assets[0]

        # Start utilization tracking
        start_utilization(
            unique_identifier,
            [created_asset],
            "test-minion-python",
            "PythonIntegrationTest",
            "Testing",
            "test_user",
        )

        # Verify utilization was started by querying
        query_request = QueryAssetUtilizationHistoryRequest(
            utilization_filter=f'UtilizationIdentifier = "{unique_identifier}"',
            asset_filter=f'AssetIdentifier = "{created_asset.id}"',
        )
        query_response = client.query_asset_utilization_history(request=query_request)

        assert query_response is not None
        assert query_response.asset_utilizations is not None
        assert len(query_response.asset_utilizations) >= 1
        assert (
            query_response.asset_utilizations[0].utilization_identifier
            == unique_identifier
        )

    def test__utilization_heartbeat__returns_success_response(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
        unique_identifier: str,
        start_utilization: Callable[[str, List[Asset], str, str, str, str], None],
    ):
        # Create multiple assets for utilization tracking
        self._create_assets_request[0].model_number = 106
        self._create_assets_request[0].serial_number = "106A"
        create_response1 = create_asset(self._create_assets_request)

        self._create_assets_request[0].model_number = 106
        self._create_assets_request[0].serial_number = "106B"
        create_response2 = create_asset(self._create_assets_request)

        assert create_response1.assets is not None and len(create_response1.assets) == 1
        assert create_response2.assets is not None and len(create_response2.assets) == 1
        created_assets = [create_response1.assets[0], create_response2.assets[0]]

        utilization_id = unique_identifier
        start_utilization(
            utilization_id,
            created_assets,
            "test-minion-python",
            "PythonIntegrationTest",
            "Testing",
            "test_user",
        )

        # Send heartbeat
        heartbeat_response = client.utilization_heartbeat(
            ids=[utilization_id],
            timestamp=datetime.now(),
        )

        assert heartbeat_response is not None
        assert heartbeat_response.updated_utilization_ids is not None
        assert len(heartbeat_response.updated_utilization_ids) == 1
        assert heartbeat_response.updated_utilization_ids[0] == utilization_id

    def test__end_utilization__returns_success_response(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
        unique_identifier: str,
        start_utilization: Callable[[str, List[Asset], str, str, str, str], None],
    ):
        # Create multiple assets for utilization tracking
        self._create_assets_request[0].model_number = 107
        self._create_assets_request[0].serial_number = "107A"
        create_response1 = create_asset(self._create_assets_request)

        self._create_assets_request[0].model_number = 107
        self._create_assets_request[0].serial_number = "107B"
        create_response2 = create_asset(self._create_assets_request)

        assert create_response1.assets is not None and len(create_response1.assets) == 1
        assert create_response2.assets is not None and len(create_response2.assets) == 1
        created_assets = [create_response1.assets[0], create_response2.assets[0]]

        utilization_id = unique_identifier
        start_utilization(
            utilization_id,
            created_assets,
            "test-minion-python",
            "PythonIntegrationTest",
            "Testing",
            "test_user",
        )

        # End utilization
        end_response = client.end_utilization(
            ids=[utilization_id],
            timestamp=datetime.now(),
        )

        assert end_response is not None
        assert end_response.updated_utilization_ids is not None
        assert len(end_response.updated_utilization_ids) == 1
        assert end_response.updated_utilization_ids[0] == utilization_id

    def test__query_asset_utilization_history__returns_response(
        self,
        client: AssetManagementClient,
        create_asset: Callable[
            [List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse
        ],
        unique_identifier: str,
        start_utilization: Callable[[str, List[Asset], str, str, str, str], None],
    ):
        # Create an asset, start and end utilization to create history
        self._create_assets_request[0].model_number = 108
        create_response = create_asset(self._create_assets_request)

        assert create_response.assets is not None and len(create_response.assets) == 1
        created_asset = create_response.assets[0]

        utilization_id = unique_identifier
        minion_id = "test-minion-python"
        category = "Testing"
        task_name = "PythonQueryTest"
        user_name = "test_user"

        # Start utilization
        start_utilization(
            utilization_id, [created_asset], minion_id, task_name, category, user_name
        )

        # End utilization
        client.end_utilization(
            ids=[utilization_id],
            timestamp=datetime.now(),
        )

        # Query utilization history - filter by asset ID to limit scope
        query_request = QueryAssetUtilizationHistoryRequest(
            utilization_filter=f'UtilizationIdentifier = "{utilization_id}"',
            asset_filter=f'AssetIdentifier = "{created_asset.id}"',
            order_by=UtilizationOrderBy.START_TIMESTAMP,
            order_by_descending=True,
            take=10,
        )

        query_response = client.query_asset_utilization_history(request=query_request)

        assert query_response is not None
        assert query_response.asset_utilizations is not None
        assert len(query_response.asset_utilizations) >= 1

        # Verify continuation_token exists (from WithPaging)
        assert hasattr(query_response, "continuation_token")

        # Find our utilization record
        utilization = query_response.asset_utilizations[0]

        # Verify the utilization data matches what we created
        assert utilization.utilization_identifier == utilization_id
        assert utilization.minion_id == minion_id
        assert utilization.category == category
        assert utilization.task_name == task_name
        assert utilization.user_name == user_name
        assert utilization.asset_identifier == created_asset.id
        assert utilization.start_timestamp is not None
        assert isinstance(utilization.start_timestamp, datetime)
        assert utilization.end_timestamp is not None
        assert isinstance(utilization.end_timestamp, datetime)
        assert isinstance(utilization.heartbeat_timestamp, datetime)

    def test__start_utilization_with_nonexistent_asset__raises_api_exception(
        self, client: AssetManagementClient, unique_identifier: str
    ):
        start_request = StartUtilizationRequest(
            utilization_identifier=unique_identifier,
            minion_id="test-minion",
            asset_identifications=[
                AssetIdentification(
                    model_name="TestModel",
                    serial_number="TEST123",
                    vendor_name="TestVendor",
                    vendor_number=1234,
                    bus_type=AssetBusType.ACCESSORY,
                )
            ],
            utilization_timestamp=datetime.now(),
        )

        with pytest.raises(ApiException):
            client.start_utilization(request=start_request)

    def test__heartbeat_with_nonexistent_utilization_id__returns_empty_list(
        self, client: AssetManagementClient, unique_identifier: str
    ):
        response = client.utilization_heartbeat(
            ids=[unique_identifier],
            timestamp=datetime.now(),
        )

        assert response is not None
        assert response.updated_utilization_ids is not None
        assert len(response.updated_utilization_ids) == 0

    def test__end_utilization_with_nonexistent_utilization_id__returns_empty_list(
        self, client: AssetManagementClient, unique_identifier: str
    ):
        response = client.end_utilization(
            ids=[unique_identifier],
            timestamp=datetime.now(),
        )

        assert response is not None
        assert response.updated_utilization_ids is not None
        assert len(response.updated_utilization_ids) == 0

    def test__query_utilization_history_with_invalid_filter__raises_api_exception(
        self, client: AssetManagementClient
    ):
        query_request = QueryAssetUtilizationHistoryRequest(
            utilization_filter="InvalidField = 'test'",
        )

        with pytest.raises(ApiException):
            client.query_asset_utilization_history(request=query_request)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/dataframe/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: tests/integration/dataframe/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/dataframe/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/dataframe/test_dataframe.py sha256=8fbe32d80d489668379e79cca4360681dc2cb40d995af503dacd33a893abd195 bytes=36816 -->
## FILE: tests/integration/dataframe/test_dataframe.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/dataframe/test_dataframe.py`
- sha256: `8fbe32d80d489668379e79cca4360681dc2cb40d995af503dacd33a893abd195`
- bytes: 36816

````python
# -*- coding: utf-8 -*-
import csv
import io
import re
import time
import warnings
from datetime import datetime, timezone
from typing import Callable, List, TypedDict

import pytest  # type: ignore
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core.helpers._iterator_file_like import IteratorFileLike
from nisystemlink.clients.dataframe import DataFrameClient
from nisystemlink.clients.dataframe.models import (
    AppendTableDataRequest,
    Column,
    ColumnFilter,
    ColumnMetadataPatch,
    ColumnOrderBy,
    ColumnType,
    CreateTableRequest,
    DataFrame,
    DataType,
    DecimationMethod,
    DecimationOptions,
    ExportFormat,
    ExportTableDataRequest,
    FilterOperation,
    ModifyTableRequest,
    ModifyTablesRequest,
    QueryDecimatedDataRequest,
    QueryTableDataRequest,
    QueryTablesRequest,
    TableMetadataModification,
)

_DataElement = str | float | int | bool | datetime | None
_DataFrameData = List[List[_DataElement]]
_TestResultIdArg = TypedDict(
    "_TestResultIdArg", {"test_result_id": str | None}, total=False
)

int_index_column = Column(
    name="index", data_type=DataType.Int32, column_type=ColumnType.Index
)

table_with_data_columns = [
    int_index_column,
    Column(name="float", data_type=DataType.Float64),
    Column(
        name="int",
        data_type=DataType.Int64,
        column_type=ColumnType.Nullable,
    ),
    Column(name="bool", data_type=DataType.Bool),
    Column(name="string", data_type=DataType.String),
]

basic_table_model = CreateTableRequest(columns=[int_index_column])


@pytest.fixture(scope="class")
def client(enterprise_config):
    """Fixture to create a DataFrameClient instance."""
    return DataFrameClient(enterprise_config)


@pytest.fixture(scope="class")
def create_table(client: DataFrameClient):
    """Fixture to return a factory that creates tables."""
    tables = []

    def _create_table(table: CreateTableRequest | None = None) -> str:
        id = client.create_table(table or basic_table_model)
        tables.append(id)
        return id

    yield _create_table

    client.delete_tables(tables)


@pytest.fixture(scope="class")
def test_tables(create_table):
    """Fixture to create a set of test tables."""
    ids = []
    for i in range(1, 4):
        ids.append(
            create_table(
                CreateTableRequest(
                    columns=[
                        Column(
                            name="time",
                            data_type=DataType.Timestamp,
                            column_type=ColumnType.Index,
                            properties={"cat": "meow"},
                        ),
                        Column(name="value", data_type=DataType.Int32),
                    ],
                    name=f"Python API test table {i} (delete me)",
                    properties={"dog": "woof"},
                )
            )
        )
    return ids


@pytest.fixture(scope="class")
def supports_test_result_id(client: DataFrameClient) -> bool:
    """Fixture to determine if the server supports test result IDs."""
    api_info = client.api_info()
    result = api_info.operations.create_tables.version >= 2
    if not result:
        warnings.warn(
            (
                "The selected version of the DataFrame Service does not support test "
                "result IDs. Tests will not attempt to set a test result ID."
            )
        )
    return result


@pytest.fixture(scope="class")
def table_with_data(client: DataFrameClient, create_table) -> str:
    """Fixture to create a table with data."""
    id = create_table(CreateTableRequest(columns=table_with_data_columns))

    frame = TestDataFrame._create_data_frame(
        table_with_data_columns,
        data=[
            [1, 4.5, 30, False, "dog"],
            [2, 3.5, None, True, "cat"],
            [3, 2.5, 10, True, "bunny"],
            [4, 1.5, 40, False, "cow"],
        ],
    )
    client.append_table_data(id, AppendTableDataRequest(frame=frame, end_of_data=True))
    TestDataFrame._wait_for_table_data(client, id, minimum_row_count=len(frame.data))

    return id


@pytest.mark.enterprise
@pytest.mark.integration
class TestDataFrame:
    @staticmethod
    def _wait_for_table_data(
        client: DataFrameClient,
        table_id: str,
        minimum_row_count: int,
        index_column: str = "index",
        timeout: float = 5.0,
        sleep_duration: float = 0.2,
    ) -> int:
        """Helper function to wait for table data to be available by polling get_table_data.

        Args:
            client: The DataFrameClient to use for checking data availability
            table_id: ID of the table to check
            expected_row_count: Expected number of rows in the table
            index_column: Name of the index column to query (default: "index")
            timeout: Maximum time to wait in seconds (default: 2.0)
            sleep_duration: Sleep duration between attempts in seconds (default: 0.2)

        Returns:
            The actual number of rows found in the table
        """
        start_time = time.time()

        while True:
            response = client.get_table_data(table_id, columns=[index_column], take=1)
            actual_row_count = response.total_row_count
            if actual_row_count >= minimum_row_count:
                return actual_row_count

            elapsed_time = time.time() - start_time
            assert elapsed_time < timeout, (
                f"Failed to get expected row count {minimum_row_count} after "
                f"{elapsed_time:.2f} seconds (last count: {actual_row_count})"
            )

            time.sleep(sleep_duration)

    def _new_single_int_table(self, create_table, column_name: str = "a") -> str:
        return create_table(
            CreateTableRequest(
                columns=[
                    Column(
                        name=column_name,
                        data_type=DataType.Int64,
                        column_type=ColumnType.Index,
                    )
                ]
            )
        )

    @staticmethod
    def _create_data_frame(
        columns: List[Column],
        data: _DataFrameData,
        include_column_names: bool = False,
    ) -> DataFrame:
        column_names = [col.name for col in columns] if include_column_names else None
        converted_data = [
            [
                TestDataFrame._data_value_to_str(columns[col_idx], value)
                for col_idx, value in enumerate(row)
            ]
            for row in data
        ]
        return DataFrame(columns=column_names, data=converted_data)

    @staticmethod
    def _read_data_frame(
        columns: List[Column],
        frame: DataFrame,
    ) -> _DataFrameData:
        frame_columns = (
            frame.columns
            if frame.columns is not None
            else [col.name for col in columns]
        )
        column_map = {col.name: col for col in columns}
        return [
            [
                TestDataFrame._str_to_data_value(
                    column_map[frame_columns[col_idx]], value
                )
                for col_idx, value in enumerate(row)
            ]
            for row in frame.data
        ]

    @staticmethod
    def _data_value_to_str(column: Column, value: _DataElement) -> str | None:
        if value is None:
            assert column.column_type == ColumnType.Nullable
            return None
        if isinstance(value, bool):
            assert column.data_type == DataType.Bool
            return "true" if value else "false"
        if isinstance(value, int):
            assert column.data_type in (DataType.Int32, DataType.Int64)
            return str(value)
        if isinstance(value, float):
            if column.data_type == DataType.Float32:
                return f"{value:.9g}"
            assert column.data_type == DataType.Float64
            return f"{value:.17g}"
        if isinstance(value, datetime):
            assert column.data_type == DataType.Timestamp
            return value.isoformat()
        assert isinstance(value, str) and column.data_type == DataType.String
        return value

    @staticmethod
    def _str_to_data_value(column: Column, value: str | None) -> _DataElement:
        if value is None:
            assert column.column_type == ColumnType.Nullable
            return None
        if column.data_type == DataType.Bool:
            result = value.lower() == "true"
            assert result or value.lower() == "false"
            return result
        if column.data_type in (DataType.Int32, DataType.Int64):
            return int(value)
        if column.data_type in (DataType.Float32, DataType.Float64):
            return float(value)
        if column.data_type == DataType.Timestamp:
            return datetime.fromisoformat(value)
        assert column.data_type == DataType.String
        return value

    @staticmethod
    def _read_exported_csv(
        columns: List[Column], data: IteratorFileLike
    ) -> tuple[List[str], _DataFrameData]:
        column_map = {col.name: col for col in columns}
        csv_content = data.read().decode("utf-8")

        # The CSV reader doesn't distinguish between "" and an empty field (e.g., `,,`).
        # The server returns the former for empty strings and the latter for null values
        # (of any data type). So we replace empty fields with a placeholder value that
        # we convert back to None below.
        csv_content = re.sub(r"([,\n])([,\r])", r"\1NULL_PLACEHOLDER\2", csv_content)

        text_stream = io.StringIO(csv_content, newline="")
        reader = csv.reader(text_stream)

        # Read the column names from the header row.
        column_names = next(reader)
        csv_columns = []
        for name in column_names:
            column = column_map.get(name)
            assert column is not None, f"CSV includes unknown column {name}"
            csv_columns.append(column)

        rows = [
            [
                TestDataFrame._str_to_data_value(
                    csv_columns[col_idx],
                    value if value != "NULL_PLACEHOLDER" else None,
                )
                for col_idx, value in enumerate(row)
            ]
            for row in reader
        ]

        return (column_names, rows)

    def test__api_info__returns(self, client):
        response = client.api_info()

        assert len(response.model_dump()) != 0

    def test__create_table__metadata_is_correct(
        self, client: DataFrameClient, test_tables: List[str]
    ):
        table_metadata = client.get_table_metadata(test_tables[0])

        assert table_metadata.name == "Python API test table 1 (delete me)"
        assert table_metadata.properties == {"dog": "woof"}
        assert table_metadata.columns == [
            Column(
                name="time",
                data_type=DataType.Timestamp,
                column_type=ColumnType.Index,
                properties={"cat": "meow"},
            ),
            Column(
                name="value",
                data_type=DataType.Int32,
                column_type=ColumnType.Normal,
                properties={},
            ),
        ]
        assert table_metadata.test_result_id is None

    def test__create_table__supports_test_result(
        self,
        client: DataFrameClient,
        create_table: Callable[[CreateTableRequest], str],
        supports_test_result_id: bool,
    ):
        test_result_id = "Test result" if supports_test_result_id else None
        id = create_table(
            CreateTableRequest(
                columns=[
                    Column(
                        name="index",
                        data_type=DataType.Int32,
                        column_type=ColumnType.Index,
                    )
                ],
                name="Test table with test result ID",
                test_result_id=test_result_id,
            )
        )

        table = client.get_table_metadata(id)
        assert table.test_result_id == test_result_id

        page = client.list_tables(take=1, id=[id])
        assert len(page.tables) == 1
        assert page.tables[0].test_result_id == test_result_id
        assert page.continuation_token is None

        page = client.query_tables(
            QueryTablesRequest(filter="id == @0", substitutions=[id], take=1)
        )
        assert len(page.tables) == 1
        assert page.tables[0].test_result_id == test_result_id
        assert page.continuation_token is None

    def test__get_table__correct_timestamp(self, client: DataFrameClient, create_table):
        id = create_table(basic_table_model)
        table = client.get_table_metadata(id)

        now = datetime.now().timestamp()
        # Assert that timestamp is within 10 seconds of now
        assert table.created_at.timestamp() == pytest.approx(now, abs=10)

    def test__get_table_invalid_id__raises(self, client: DataFrameClient):
        with pytest.raises(ApiException, match="invalid table ID"):
            client.get_table_metadata("invalid_id")

    def test__list_tables__returns(
        self, client: DataFrameClient, test_tables: List[str]
    ):
        first_page = client.list_tables(
            take=2,
            id=test_tables[:3],
            order_by="NAME",
            order_by_descending=True,
        )

        assert len(first_page.tables) == 2
        assert first_page.tables[0].id == test_tables[-1]  # Asserts descending order
        assert first_page.continuation_token is not None

        second_page = client.list_tables(
            id=test_tables[:3],
            order_by="NAME",
            order_by_descending=True,
            continuation_token=first_page.continuation_token,
        )

        assert len(second_page.tables) == 1
        assert second_page.continuation_token is None

    def test__query_tables__returns(
        self, client: DataFrameClient, test_tables: List[str]
    ):
        query = QueryTablesRequest(
            filter="""(id == @0 or id == @1 or id == @2)
                and createdWithin <= RelativeTime.CurrentWeek
                and supportsAppend == @3 and rowCount < @4""",
            substitutions=[test_tables[0], test_tables[1], test_tables[2], True, 1],
            reference_time=datetime.now(tz=timezone.utc),
            take=2,
            order_by="NAME",
            order_by_descending=True,
        )
        first_page = client.query_tables(query)

        assert len(first_page.tables) == 2
        assert first_page.tables[0].id == test_tables[-1]  # Asserts descending order
        assert first_page.continuation_token is not None

        query.continuation_token = first_page.continuation_token

        second_page = client.query_tables(query)
        assert len(second_page.tables) == 1
        assert second_page.continuation_token is None

    def test__modify_table__returns(
        self, client: DataFrameClient, create_table, supports_test_result_id: bool
    ):
        id = create_table(basic_table_model)

        client.modify_table(
            id,
            ModifyTableRequest(
                metadata_revision=2,
                name="Modified table",
                properties={"cow": "moo"},
                columns=[
                    ColumnMetadataPatch(name="index", properties={"sheep": "baa"})
                ],
                **self._test_result_id_if_supported(
                    "Test result", supports_test_result_id
                ),
            ),
        )
        table = client.get_table_metadata(id)

        assert table.metadata_revision == 2
        assert table.name == "Modified table"
        assert table.test_result_id == (
            "Test result" if supports_test_result_id else None
        )
        assert table.properties == {"cow": "moo"}
        assert table.columns[0].properties == {"sheep": "baa"}

        client.modify_table(id, ModifyTableRequest(properties={"bee": "buzz"}))
        table = client.get_table_metadata(id)

        assert table.properties == {"cow": "moo", "bee": "buzz"}
        assert table.name == "Modified table"
        assert table.test_result_id == (
            "Test result" if supports_test_result_id else None
        )

        client.modify_table(
            id,
            ModifyTableRequest(
                metadata_revision=4,
                name=None,
                properties={"cow": None},
                columns=[ColumnMetadataPatch(name="index", properties={"sheep": None})],
                **self._test_result_id_if_supported(None, supports_test_result_id),
            ),
        )
        table = client.get_table_metadata(id)

        assert table.metadata_revision == 4
        assert table.name == id
        assert table.test_result_id is None
        assert table.properties == {"bee": "buzz"}
        assert table.columns[0].properties == {}

    @staticmethod
    def _test_result_id_if_supported(
        test_result_id: str | None, supports_test_result_id: bool
    ) -> _TestResultIdArg:
        return {"test_result_id": test_result_id} if supports_test_result_id else {}

    def test__delete_table__deletes(self, client: DataFrameClient):
        id = client.create_table(
            basic_table_model
        )  # Don't use fixture to avoid deleting the table twice

        assert client.delete_table(id) is None

        with pytest.raises(ApiException, match="404 Not Found"):
            client.get_table_metadata(id)

    def test__delete_tables__deletes(self, client: DataFrameClient):
        ids = [client.create_table(basic_table_model) for _ in range(3)]

        assert client.delete_tables(ids) is None

        assert client.list_tables(id=ids).tables == []

    def test__delete_tables__returns_partial_success(self, client: DataFrameClient):
        id = client.create_table(basic_table_model)

        response = client.delete_tables([id, "invalid_id"])

        assert response is not None
        assert response.deleted_table_ids == [id]
        assert response.failed_table_ids == ["invalid_id"]
        assert len(response.error.inner_errors) == 1

    def test__modify_tables__modifies_tables(
        self, client: DataFrameClient, create_table, supports_test_result_id: bool
    ):
        ids = [create_table(basic_table_model) for _ in range(3)]

        updates = [
            TableMetadataModification(
                id=id,
                name="Modified table",
                test_result_id="Test result" if supports_test_result_id else None,
                properties={"duck": "quack"},
            )
            for id in ids
        ]

        assert client.modify_tables(ModifyTablesRequest(tables=updates)) is None

        for table in client.list_tables(id=ids).tables:
            assert table.name == "Modified table"
            assert table.test_result_id == (
                "Test result" if supports_test_result_id else None
            )
            assert table.properties == {"duck": "quack"}

        updates = [
            TableMetadataModification(id=id, properties={"pig": "oink"}) for id in ids
        ]

        assert (
            client.modify_tables(ModifyTablesRequest(tables=updates, replace=True))
            is None
        )

        for table in client.list_tables(id=ids).tables:
            assert table.name == "Modified table"
            assert table.test_result_id == (
                "Test result" if supports_test_result_id else None
            )
            assert table.properties == {"pig": "oink"}

        if supports_test_result_id:
            updates = [
                TableMetadataModification(id=id, test_result_id="") for id in ids
            ]

            assert client.modify_tables(ModifyTablesRequest(tables=updates)) is None

            for table in client.list_tables(id=ids).tables:
                assert table.name == "Modified table"
                assert table.test_result_id is None

    def test__modify_tables__returns_partial_success(
        self, client: DataFrameClient, create_table, supports_test_result_id: bool
    ):
        id = create_table(basic_table_model)

        updates = [
            TableMetadataModification(
                id=id,
                name="Modified table",
                test_result_id="Test result" if supports_test_result_id else None,
            )
            for id in [id, "invalid_id"]
        ]

        response = client.modify_tables(ModifyTablesRequest(tables=updates))

        assert response is not None
        assert response.modified_table_ids == [id]
        assert response.failed_modifications == [updates[1]]
        assert len(response.error.inner_errors) == 1

    def test__get_table_data__returns_correct_data(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.get_table_data(
            table_with_data, columns=["index", "float"], order_by=["float"]
        )

        assert response.total_row_count == 4
        assert response.frame.columns == ["index", "float"]
        assert self._read_data_frame(table_with_data_columns, response.frame) == [
            [4, 1.5],
            [3, 2.5],
            [2, 3.5],
            [1, 4.5],
        ]

    def test__write_invalid_data__raises(
        self, client: DataFrameClient, test_tables: List[str]
    ):
        id = test_tables[0]

        frame = DataFrame(
            columns=["index", "non_existent_column"],
            data=[["1", "2"], ["2", "2"], ["3", "3"]],
        )

        with pytest.raises(ApiException, match="400 Bad Request"):
            client.append_table_data(id, AppendTableDataRequest(frame=frame))

    def test__query_table_data__sorts(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.query_table_data(
            table_with_data,
            QueryTableDataRequest(
                columns=["index", "float"],
                order_by=[
                    ColumnOrderBy(column="bool"),
                    ColumnOrderBy(column="float", descending=True),
                ],
            ),
        )

        assert response.total_row_count == 4
        assert response.frame.columns == ["index", "float"]
        assert self._read_data_frame(table_with_data_columns, response.frame) == [
            [1, 4.5],  # bool=False
            [4, 1.5],  # bool=False
            [2, 3.5],  # bool=True
            [3, 2.5],  # bool=True
        ]

    def test__query_table_data__filters(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.query_table_data(
            table_with_data,
            QueryTableDataRequest(
                columns=["index"],
                filters=[
                    ColumnFilter(
                        column="float",
                        operation=FilterOperation.GreaterThan,
                        value="1.5",
                    ),
                    ColumnFilter(
                        column="int",
                        operation=FilterOperation.NotEquals,
                        value=None,
                    ),
                    ColumnFilter(
                        column="string",
                        operation=FilterOperation.NotContains,
                        value="bun",
                    ),
                ],
            ),
        )

        assert response.total_row_count == 1
        assert response.frame.columns == ["index"]
        assert self._read_data_frame(table_with_data_columns, response.frame) == [[1]]

    def test__query_decimated_data__works(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.query_decimated_data(
            table_with_data,
            QueryDecimatedDataRequest(
                columns=["index", "float"],
                decimation=DecimationOptions(
                    x_column="index",
                    y_columns=["float"],
                    intervals=1,
                    method=DecimationMethod.MaxMin,
                ),
            ),
        )

        assert response.frame.columns == ["index", "float"]
        assert self._read_data_frame(table_with_data_columns, response.frame) == [
            [1, 4.5],
            [4, 1.5],
        ]

    def test__export_table_data__includes_all_rows(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.export_table_data(
            table_with_data,
            ExportTableDataRequest(
                order_by=[ColumnOrderBy(column="index")],
                response_format=ExportFormat.CSV,
            ),
        )

        column_names, data = self._read_exported_csv(table_with_data_columns, response)
        assert column_names == ["index", "float", "int", "bool", "string"]
        assert data == [
            [1, 4.5, 30, False, "dog"],
            [2, 3.5, None, True, "cat"],
            [3, 2.5, 10, True, "bunny"],
            [4, 1.5, 40, False, "cow"],
        ]

    def test__export_table_data__limits_to_take_rows(
        self, client: DataFrameClient, table_with_data: str
    ):
        response = client.export_table_data(
            table_with_data,
            ExportTableDataRequest(
                columns=["index"],
                order_by=[ColumnOrderBy(column="index", descending=True)],
                take=2,
                response_format=ExportFormat.CSV,
            ),
        )

        column_names, data = self._read_exported_csv(table_with_data_columns, response)
        assert column_names == ["index"]
        assert data == [[4], [3]]

    def test__append_table_data__append_request_success(
        self, client: DataFrameClient, create_table
    ):
        table_id = self._new_single_int_table(create_table)
        frame = DataFrame(columns=["a"], data=[["1"], ["2"]])
        client.append_table_data(
            table_id, AppendTableDataRequest(frame=frame, end_of_data=True)
        )
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 2
        assert metadata.supports_append is False

    def test__append_table_data__append_request_with_end_of_data_argument_disallowed(
        self, client: DataFrameClient, create_table
    ):
        request = AppendTableDataRequest(end_of_data=True)
        with pytest.raises(
            ValueError,
            match="end_of_data must not be provided separately when passing an AppendTableDataRequest.",
        ):
            client.append_table_data(
                self._new_single_int_table(create_table), request, end_of_data=True
            )

    def test__append_table_data__append_request_without_end_of_data_success(
        self, client: DataFrameClient, create_table
    ):
        table_id = self._new_single_int_table(create_table)
        frame = DataFrame(columns=["a"], data=[["7"], ["8"]])
        client.append_table_data(table_id, AppendTableDataRequest(frame=frame))
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 2
        assert metadata.supports_append is True

    def test__append_table_data__accepts_dataframe_model(
        self, client: DataFrameClient, create_table
    ):
        table_id = self._new_single_int_table(create_table)
        frame = DataFrame(columns=["a"], data=[["1"], ["2"]])
        client.append_table_data(table_id, frame, end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 2
        assert metadata.supports_append is False

    def test__append_table_data__dataframe_without_end_of_data_success(
        self, client: DataFrameClient, create_table
    ):
        table_id = self._new_single_int_table(create_table)
        frame = DataFrame(columns=["a"], data=[["10"], ["11"]])
        client.append_table_data(table_id, frame)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 2
        assert metadata.supports_append is True

    def test__append_table_data__none_without_end_of_data_raises(
        self, client: DataFrameClient, create_table
    ):
        table_id = create_table(basic_table_model)
        with pytest.raises(
            ValueError, match="end_of_data must be provided when data is None"
        ):
            client.append_table_data(table_id, None)

    def test__append_table_data__flush_only_with_none(
        self, client: DataFrameClient, create_table
    ):
        table_id = self._new_single_int_table(create_table)
        client.append_table_data(table_id, None, end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 0
        assert metadata.supports_append is False

    def test__append_table_data__arrow_ingestion_success(
        self, client: DataFrameClient, create_table
    ):
        pa = pytest.importorskip("pyarrow")
        table_id = self._new_single_int_table(create_table)
        batch = pa.record_batch([pa.array([10, 11, 12])], names=["a"])
        client.append_table_data(table_id, [batch], end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 3
        assert metadata.supports_append is False
        with pytest.raises(ApiException):
            client.append_table_data(table_id, None, end_of_data=True)

    def test__append_table_data__single_recordbatch_success(
        self, client: DataFrameClient, create_table
    ):
        pa = pytest.importorskip("pyarrow")
        table_id = self._new_single_int_table(create_table)
        batch = pa.record_batch([pa.array([1, 2, 3])], names=["a"])
        client.append_table_data(table_id, batch, end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 3
        assert metadata.supports_append is False
        with pytest.raises(ApiException):
            client.append_table_data(table_id, None, end_of_data=True)

    def test__append_table_data__arrow_ingestion_with_end_of_data_query_param_false(
        self, client: DataFrameClient, create_table
    ):
        pa = pytest.importorskip("pyarrow")
        table_id = self._new_single_int_table(create_table)
        batch1 = pa.record_batch([pa.array([4, 5, 6])], names=["a"])
        client.append_table_data(table_id, [batch1], end_of_data=False)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 3
        assert metadata.supports_append is True
        batch2 = pa.record_batch([pa.array([7, 8])], names=["a"])
        client.append_table_data(table_id, [batch2], end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 5
        assert metadata.supports_append is False

    def test__append_table_data__empty_iterator_requires_end_of_data(
        self, client: DataFrameClient, create_table
    ):
        table_id = create_table(basic_table_model)
        with pytest.raises(
            ValueError,
            match="end_of_data must be provided when data iterator is empty.",
        ):
            client.append_table_data(table_id, [])
        client.append_table_data(table_id, [], end_of_data=True)
        metadata = client.get_table_metadata(table_id)
        assert metadata.row_count == 0
        assert metadata.supports_append is False

    def test__append_table_data__arrow_iterable_with_non_recordbatch_elements_raises(
        self, client: DataFrameClient, create_table
    ):
        pytest.importorskip("pyarrow")
        table_id = create_table(basic_table_model)
        with pytest.raises(
            ValueError,
            match="Iterable provided to data must yield pyarrow.RecordBatch objects.",
        ):
            client.append_table_data(table_id, [1, 2, 3])

    def test__append_table_data__arrow_iterable_without_pyarrow_raises_runtime_error(
        self, client: DataFrameClient, create_table, monkeypatch
    ):
        import nisystemlink.clients.dataframe._data_frame_client as df_module

        monkeypatch.setattr(df_module, "pa", None)
        table_id = create_table(basic_table_model)
        with pytest.raises(
            RuntimeError,
            match="pyarrow is not installed. Install to stream RecordBatches.",
        ):
            client.append_table_data(table_id, [object()])

    def test__append_table_data__arrow_ingestion_400_unsupported(
        self, client: DataFrameClient
    ):
        pa = pytest.importorskip("pyarrow")
        table_id = "mock_table_id"
        bad_batch = pa.record_batch([pa.array([1, 2, 3])], names=["b"])
        api_info_json = {
            "operations": {
                "create_tables": {"available": True, "version": 1},
                "delete_tables": {"available": True, "version": 1},
                "modify_metadata": {"available": True, "version": 1},
                "list_tables": {"available": True, "version": 1},
                "read_data": {"available": True, "version": 3},
                "write_data": {"available": True, "version": 1},
            }
        }

        with responses.RequestsMock() as rsps:
            rsps.add(
                responses.GET,
                f"{client.session.base_url}",
                json=api_info_json,
            )
            rsps.add(
                responses.POST,
                f"{client.session.base_url}tables/{table_id}/data",
                status=400,
            )
            with pytest.raises(ApiException) as excinfo:
                client.append_table_data(table_id, [bad_batch], end_of_data=True)

        assert "Arrow ingestion request was rejected" in str(excinfo.value)

    def test__append_table_data__arrow_ingestion_400_supported_passthrough(
        self, client: DataFrameClient
    ):
        pa = pytest.importorskip("pyarrow")
        table_id = "mock_table_id"
        bad_batch = pa.record_batch([pa.array([1, 2, 3])], names=["b"])
        api_info_json = {
            "operations": {
                "create_tables": {"available": True, "version": 1},
                "delete_tables": {"available": True, "version": 1},
                "modify_metadata": {"available": True, "version": 1},
                "list_tables": {"available": True, "version": 1},
                "read_data": {"available": True, "version": 3},
                "write_data": {"available": True, "version": 2},
            }
        }

        with responses.RequestsMock() as rsps:
            rsps.add(
                responses.GET,
                f"{client.session.base_url}",
                json=api_info_json,
            )
            rsps.add(
                responses.POST,
                f"{client.session.base_url}tables/{table_id}/data",
                status=400,
            )
            with pytest.raises(ApiException) as excinfo:
                client.append_table_data(table_id, [bad_batch], end_of_data=True)

        assert "Arrow ingestion request was rejected" not in str(excinfo.value)

    def test__append_table_data__arrow_ingestion_non_400_passthrough(
        self, client: DataFrameClient
    ):
        pa = pytest.importorskip("pyarrow")
        batch = pa.record_batch([pa.array([1, 2, 3])], names=["a"])
        with pytest.raises(ApiException) as excinfo:
            client.append_table_data(
                "111111111111111111111111", [batch], end_of_data=True
            )
        assert "Arrow ingestion request was rejected" not in str(excinfo.value)

    def test__append_table_data__unsupported_type_raises(
        self, client: DataFrameClient, create_table
    ):
        table_id = create_table(basic_table_model)
        with pytest.raises(ValueError, match="Unsupported type"):
            client.append_table_data(table_id, 123)  # type: ignore[arg-type]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/feeds/test_feeds_client.py sha256=ec27c0a235ff928290697db71aef9edea1e80b89d579b6e212a93a3cee9a9116 bytes=10737 -->
## FILE: tests/integration/feeds/test_feeds_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/feeds/test_feeds_client.py`
- sha256: `ec27c0a235ff928290697db71aef9edea1e80b89d579b6e212a93a3cee9a9116`
- bytes: 10737

````python
"""Integration tests for FeedsClient."""

import uuid
from pathlib import Path
from random import randint
from typing import BinaryIO, Callable

import pytest
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.feeds import FeedsClient
from nisystemlink.clients.feeds.models import CreateFeedRequest, Platform
from responses.registries import OrderedRegistry
from uplink.clients.io import blocking_strategy as uplink_blocking_strategy

BASE_URL = "https://test-api.lifecyclesolutions.ni.com"
FEED_DESCRIPTION = "Sample feed for uploading packages"
PACKAGE_PATH = str(
    Path(__file__).parent.resolve()
    / "test_files"
    / "sample-measurement_0.5.0_windows_x64.nipkg"
)
PREFIX = "Feeds Client Test - "


@pytest.fixture(scope="class")
def client(enterprise_config) -> FeedsClient:
    """Fixture to create a FeedsClient instance."""
    return FeedsClient(enterprise_config)


@pytest.fixture(scope="class")
def create_feed(client: FeedsClient):
    """Fixture to return a object that creates feed."""
    feed_ids = []

    def _create_feed(feed):
        response = client.create_feed(feed)
        feed_ids.append(response.id)
        return response

    yield _create_feed

    # deleting the created feeds.
    for feed_id in feed_ids:
        client.delete_feed(id=feed_id)


@pytest.fixture(scope="class")
def create_feed_request():
    """Fixture to create a request body of create feed API."""

    def _create_feed_request(feed_name: str, description: str, platform: Platform):
        feed_request = CreateFeedRequest(
            name=feed_name,
            platform=platform,
            description=description,
        )
        return feed_request

    yield _create_feed_request


@pytest.fixture(scope="class")
def binary_pkg_file_data() -> BinaryIO:
    """Fixture to return package file in binary format."""
    package_data = open(PACKAGE_PATH, "rb")
    return package_data


@pytest.fixture(scope="class")
def invalid_id() -> str:
    """Generate a invalid id."""
    id = f"Invalid-id-{randint(1000, 9999)}"
    return id


@pytest.fixture(scope="class")
def get_feed_name():
    """Generate a feed name."""

    def _get_feed_name():
        uuid_part = uuid.uuid4().hex
        feed_name = f"{PREFIX}{uuid_part}"

        return feed_name

    yield _get_feed_name


@pytest.mark.enterprise
@pytest.mark.integration
class TestFeedsClient:
    def test__create_feed_windows_platform__succeeds(
        self,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case of a completely successful create feed API for Windows platform."""
        feed_name = get_feed_name()
        request_body = create_feed_request(
            feed_name=feed_name,
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        response = create_feed(request_body)

        assert response.id is not None
        assert response.workspace is not None
        assert response.name == feed_name
        assert response.platform == Platform.WINDOWS
        assert response.description == FEED_DESCRIPTION

    def test__create_feed_linux_platform__succeeds(
        self,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case of a completely successful create feed API for Linux platform."""
        feed_name = get_feed_name()
        request_body = create_feed_request(
            feed_name=feed_name,
            description=FEED_DESCRIPTION,
            platform=Platform.NI_LINUX_RT,
        )
        response = create_feed(request_body)

        assert response.id is not None
        assert response.workspace is not None
        assert response.name == feed_name
        assert response.platform == Platform.NI_LINUX_RT
        assert response.description == FEED_DESCRIPTION

    def test__query_feeds_windows_platform__succeeds(
        self,
        client: FeedsClient,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case for querying available feeds for Windows platform."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        create_feed_resp = create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        query_feed_resp = client.query_feeds(platform=Platform.WINDOWS)
        assert query_feed_resp is not None

    def test__query_feeds_linux_platform__succeeds(
        self,
        client: FeedsClient,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case for querying available feeds for Linux platform."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.NI_LINUX_RT,
        )
        create_feed_resp = create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        query_feed_resp = client.query_feeds(platform=Platform.NI_LINUX_RT)
        assert query_feed_resp is not None

    def test__query_feeds__invalid_workspace_raises(
        self,
        client: FeedsClient,
        invalid_id: str,
    ):
        """Test the case of query feeds API with invalid workspace id."""
        with pytest.raises(ApiException, match="UnauthorizedWorkspaceError"):
            client.query_feeds(workspace=invalid_id)

    def test__upload_package__succeeds(
        self,
        client: FeedsClient,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case of upload package to feed."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        create_feed_resp = create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        upload_pacakge_rsp = client.upload_package(
            package_file_path=PACKAGE_PATH,
            feed_id=create_feed_resp.id,
            overwrite=True,
        )
        assert upload_pacakge_rsp is not None

    def test__upload_package_content__succeeds(
        self,
        client: FeedsClient,
        create_feed: Callable,
        create_feed_request: Callable,
        binary_pkg_file_data: BinaryIO,
        get_feed_name: Callable,
    ):
        """Test the case of upload package content to feed."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        create_feed_resp = create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        upload_pacakge_rsp = client.upload_package_content(
            package=binary_pkg_file_data,
            feed_id=create_feed_resp.id,
            overwrite=True,
        )
        assert upload_pacakge_rsp is not None

    def test__upload_package_content__invalid_feed_id_raises(
        self,
        client: FeedsClient,
        binary_pkg_file_data: BinaryIO,
        invalid_id: str,
    ):
        """Test the case of uploading package to Invalid feed."""
        with pytest.raises(ApiException, match="FeedNotFoundError"):
            client.upload_package_content(
                package=binary_pkg_file_data,
                feed_id=invalid_id,
            )

    def test__upload_package_content_after_rate_limit_retry__upload_package_content_succeeds(
        self,
        client: FeedsClient,
        create_feed: Callable,
        create_feed_request: Callable,
        get_feed_name: Callable,
        monkeypatch: pytest.MonkeyPatch,
    ):
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        create_feed_resp = create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        response = None

        monkeypatch.setattr(uplink_blocking_strategy.time, "sleep", lambda _: None)

        with responses.RequestsMock(registry=OrderedRegistry) as request_mock:
            request_mock.add(
                responses.POST,
                f"{BASE_URL}/nifeed/v1/feeds/{create_feed_resp.id}/packages",
                status=429,
            )
            request_mock.add_passthru(
                f"{BASE_URL}/nifeed/v1/feeds/{create_feed_resp.id}/packages"
            )

            with open(PACKAGE_PATH, "rb") as package:
                response = client.upload_package_content(
                    feed_id=create_feed_resp.id,
                    package=package,
                    overwrite=True,
                )

        assert response is not None
        assert response.id is not None

    def test__delete_windows_feed__succeeds(
        self,
        client: FeedsClient,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case of deleting Windows feed."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.WINDOWS,
        )
        create_feed_resp = client.create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        delete_feed_resp = client.delete_feed(id=create_feed_resp.id)
        assert delete_feed_resp is None

    def test__delete__linux_feed__succeeds(
        self,
        client: FeedsClient,
        create_feed_request: Callable,
        get_feed_name: Callable,
    ):
        """Test the case of deleting Linux feed."""
        create_feed_request_body = create_feed_request(
            feed_name=get_feed_name(),
            description=FEED_DESCRIPTION,
            platform=Platform.NI_LINUX_RT,
        )
        create_feed_resp = client.create_feed(create_feed_request_body)
        assert create_feed_resp.id is not None

        delete_feed_resp = client.delete_feed(id=create_feed_resp.id)
        assert delete_feed_resp is None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/file/test_file_client.py sha256=5b5a382f0da6195fd5ebc3fb2aec13cb6da20839c1eec5f6b93b7df52300b9a3 bytes=23264 -->
## FILE: tests/integration/file/test_file_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/file/test_file_client.py`
- sha256: `5b5a382f0da6195fd5ebc3fb2aec13cb6da20839c1eec5f6b93b7df52300b9a3`
- bytes: 23264

````python
"""Integration tests for FileClient."""

import io
import string
from datetime import datetime
from io import BytesIO
from random import choices, randint
from typing import BinaryIO

import backoff  # type: ignore
import pytest  # type: ignore
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.file import FileClient
from nisystemlink.clients.file.models import (
    FileLinqQueryOrderBy,
    FileLinqQueryRequest,
    SearchFilesOrderBy,
    SearchFilesRequest,
    TotalCountRelation,
    UpdateMetadataRequest,
)
from nisystemlink.clients.file.utilities import rename_file
from responses.registries import OrderedRegistry
from uplink.clients.io import blocking_strategy as uplink_blocking_strategy

BASE_URL = "https://test-api.lifecyclesolutions.ni.com"
FILE_NOT_FOUND_ERR = "Not Found"
PREFIX = "File Client Tests-"
TEST_FILE_DATA = b"This is a test file binary content."
TEST_FILE_NAME = f"{PREFIX}Test File.bin"


@pytest.fixture(scope="class")
def client(enterprise_config) -> FileClient:
    """Fixture to create a FileClient instance."""
    return FileClient(enterprise_config)


@pytest.fixture
def binary_file_data() -> BinaryIO:
    """Test Binary file content."""
    return io.BytesIO(TEST_FILE_DATA)


@pytest.fixture(scope="class")
def test_file(client: FileClient):
    """Fixture to return a factory that uploads a file."""
    file_ids = []

    def _test_file(
        file_name: str = TEST_FILE_NAME, cleanup: bool = True, metadata: dict = {}
    ) -> str:
        test_file = io.BytesIO(TEST_FILE_DATA)
        test_file.name = file_name
        file_id = client.upload_file(file=test_file, metadata=metadata)

        if cleanup:
            file_ids.append(file_id)

        return file_id

    yield _test_file

    if file_ids:
        client.delete_files(ids=file_ids)


@pytest.fixture(scope="class")
def invalid_file_id(client: FileClient) -> str:
    """Generate a invalid file id."""
    MAX_RETRIES = 10
    attempts = 0

    while attempts < MAX_RETRIES:
        file_id = f"Invalid-File-Id-{randint(1000, 9999)}"
        files = client.get_files(ids=[file_id])
        if files.total_count == 0:
            return file_id

    raise Exception(f"Failed to generate a invalid-file-id in {MAX_RETRIES} attempts.")


@pytest.fixture
def random_filename_extension() -> str:
    """Generate a random filename and extension."""
    rand_file_name = "".join(choices(string.ascii_letters + string.digits, k=10))
    rand_file_extension = "".join(choices(string.ascii_letters, k=3))

    return f"{PREFIX}{rand_file_name}.{rand_file_extension}"


@pytest.mark.enterprise
@pytest.mark.integration
class TestFileClient:
    def test__api_info__returns(self, client: FileClient):
        api_info = client.api_info()
        assert len(api_info.model_dump()) != 0

    def test__upload_file_with_metadata__succeeds(
        self,
        client: FileClient,
        test_file,
        random_filename_extension: str,
    ):
        file_name = random_filename_extension
        metadata = {"CustomProp": "CustomValue"}

        file_id = test_file(file_name=file_name, metadata=metadata)

        # Verify the file was created with correct metadata
        files = client.get_files(ids=[file_id])
        assert files.total_count == 1
        assert len(files.available_files) == 1
        assert files.available_files[0].id == file_id
        assert files.available_files[0].properties is not None
        assert files.available_files[0].properties["Name"] == file_name
        assert (
            len(files.available_files[0].properties.keys()) == len(metadata) + 1
        )  # Name + 1 custom property

    def test__upload_file_after_rate_limit_retry__upload_file_succeeds(
        self, client: FileClient, monkeypatch: pytest.MonkeyPatch
    ):
        """Retrying a file upload should succeed against the real endpoint."""
        test_file = io.BytesIO(TEST_FILE_DATA)
        test_file.name = "retry-safe-file.bin"
        file_id = None

        monkeypatch.setattr(uplink_blocking_strategy.time, "sleep", lambda _: None)

        try:
            with responses.RequestsMock(registry=OrderedRegistry) as request_mock:
                request_mock.add(
                    responses.POST,
                    f"{BASE_URL}/nifile/v1/service-groups/Default/upload-files",
                    status=429,
                )
                request_mock.add_passthru(
                    f"{BASE_URL}/nifile/v1/service-groups/Default/upload-files"
                )

                file_id = client.upload_file(file=test_file)

            assert file_id is not None

            files = client.get_files(ids=[file_id])
            assert files.total_count == 1
            assert len(files.available_files) == 1
            assert files.available_files[0].id == file_id
            assert files.available_files[0].properties is not None
            assert files.available_files[0].properties["Name"] == test_file.name
        finally:
            if file_id:
                client.delete_file(id=file_id)

    def test__upload_get_delete_files__succeeds(
        self, client: FileClient, test_file, random_filename_extension
    ):
        # upload a file
        file_id = test_file(file_name=random_filename_extension, cleanup=False)
        assert file_id != ""

        files = client.get_files(ids=[file_id])
        assert files.total_count == 1
        assert len(files.available_files) == 1
        assert files.available_files[0].id == file_id
        assert files.available_files[0].properties is not None
        assert files.available_files[0].properties["Name"] == random_filename_extension

    def test__delete_file__invalid_id_raises(
        self, client: FileClient, invalid_file_id: str
    ):
        with pytest.raises(ApiException, match=FILE_NOT_FOUND_ERR):
            client.delete_file(id=invalid_file_id)

    def test__delete_files__succeeds(self, client: FileClient, test_file):
        # upload 2 files and delete them
        NUM_FILES = 2

        file_ids = [test_file(cleanup=False) for _ in range(NUM_FILES)]

        # confirm that files exist
        files = client.get_files(ids=file_ids)
        assert files.total_count == NUM_FILES

        client.delete_files(ids=file_ids)

        # confirm that files were deleted
        files = client.get_files(ids=file_ids)
        assert files.total_count == 0

    def test__download_file__invalid_id_raises(
        self, client: FileClient, invalid_file_id: str
    ):
        with pytest.raises(ApiException, match=FILE_NOT_FOUND_ERR):
            client.download_file(id=invalid_file_id)

    def test__download_file__succeeds(
        self,
        client: FileClient,
        test_file,
        binary_file_data: BinaryIO,
        random_filename_extension: str,
    ):
        # Upload the test file with random name
        file_id = test_file(file_name=random_filename_extension)

        # verify the file content
        downloaded_data = client.download_file(id=file_id)
        assert downloaded_data.read() == binary_file_data.read()

    def test__update_metadata__rename_utility_succeeds(
        self, client: FileClient, test_file
    ):
        OLD_NAME = f"{PREFIX}oldname.xyz"
        NEW_NAME = f"{PREFIX}newname.abc"

        file_id = test_file(file_name=OLD_NAME)

        rename_file(client=client, file_id=file_id, name=NEW_NAME)

        # verify the File Name and extension
        files = client.get_files(ids=[file_id])
        assert len(files.available_files) == 1
        assert files.available_files[0].properties is not None
        assert files.available_files[0].properties["Name"] == NEW_NAME

    def test__update_metadata__append_replace_succeeds(
        self, client: FileClient, test_file
    ):
        # Upload File-> Add 2 props-> Verify-> Replace 2 props with 3 new props-> Verify
        file_id = test_file()

        new_metadata = {"Prop1": "Value1", "Prop2": "Value2"}

        append_prop_request = UpdateMetadataRequest(
            replace_existing=False, properties=new_metadata
        )
        client.update_metadata(metadata=append_prop_request, id=file_id)

        # verify appended properties
        files = client.get_files(ids=[file_id])
        assert len(files.available_files) == 1
        assert files.available_files[0].properties is not None
        assert (
            len(files.available_files[0].properties.keys()) == len(new_metadata) + 1
        )  # Name + 2 added properties

        file_props = files.available_files[0].properties

        for prop_name, value in new_metadata.items():
            assert file_props[prop_name] == value

        # replace the properties by a new one
        replace_metadata = {"Prop3": "Value3", "Prop4": "Value4", "Prop5": "Value5"}

        append_prop_request = UpdateMetadataRequest(
            replace_existing=True, properties=replace_metadata
        )
        client.update_metadata(metadata=append_prop_request, id=file_id)
        # verify replaced properties
        files = client.get_files(ids=[file_id])
        assert len(files.available_files) == 1
        assert files.available_files[0].properties is not None
        assert (
            len(files.available_files[0].properties.keys()) == len(replace_metadata) + 1
        )  # Name + 3 replaced properties

    def test__back_off_retry__works(self, client: FileClient, test_file):
        file_id = test_file()

        for i in range(20):
            rename_file(client=client, file_id=file_id, name=f"{PREFIX}{i}.abc")

    def test__query_files_linq__filter_by_name_succeeds(
        self, client: FileClient, test_file, random_filename_extension: str
    ):
        file_id = test_file(file_name=random_filename_extension)

        query_request = FileLinqQueryRequest(
            filter=f'name == "{random_filename_extension}"',
            order_by=FileLinqQueryOrderBy.CREATED,
            order_by_descending=True,
            take=1,
        )
        response = client.query_files_linq(query=query_request)

        assert response.available_files is not None
        assert response.total_count is not None
        assert response.total_count.value == 1
        assert response.total_count.relation == TotalCountRelation.EQUALS
        assert len(response.available_files) == 1
        assert response.available_files[0].id == file_id
        assert response.available_files[0].created is not None
        assert isinstance(response.available_files[0].created, datetime)
        assert response.available_files[0].updated is not None
        assert isinstance(response.available_files[0].updated, datetime)
        assert response.available_files[0].workspace is not None
        assert response.available_files[0].size is not None
        assert response.available_files[0].size64 is not None
        assert response.available_files[0].properties is not None
        assert (
            response.available_files[0].properties["Name"] == random_filename_extension
        )

    def test__query_files_linq__invalid_filter_raises(self, client: FileClient):
        query_request = FileLinqQueryRequest(filter="invalid filter syntax:")

        with pytest.raises(ApiException):
            client.query_files_linq(query=query_request)

    def test__query_files_linq__filter_returns_no_results(self, client: FileClient):
        unique_nonexistent_name = (
            f"{PREFIX}nonexistent_file_{randint(100000, 999999)}.random_extension"
        )

        query_request = FileLinqQueryRequest(
            filter=f'name == "{unique_nonexistent_name}"'
        )
        response = client.query_files_linq(query=query_request)

        assert response.available_files is not None
        assert len(response.available_files) == 0
        assert response.total_count is not None
        assert response.total_count.value == 0
        assert response.total_count.relation == TotalCountRelation.EQUALS

    def test__query_files_linq__total_count_relation_accepts_string(
        self, client: FileClient, test_file, random_filename_extension
    ):
        """Test backward compatibility: TotalCountRelation should accept string values.

        TotalCountRelation was previously a plain str type. This test ensures that string
        values like 'eq' and 'gte' are still accepted for backward compatibility.
        """
        test_file(file_name=random_filename_extension)

        query_request = FileLinqQueryRequest(
            filter=f'name == "{random_filename_extension}"',
        )
        response = client.query_files_linq(query=query_request)

        assert response.total_count is not None
        # Test that the relation can be compared with string values
        assert response.total_count.relation == "eq"
        assert response.total_count.relation in ["eq", "gte"]
        # Also verify enum comparison still works
        assert response.total_count.relation == TotalCountRelation.EQUALS  # type: ignore[comparison-overlap]

    def test__query_files_linq__skip_and_take_pagination(
        self, client: FileClient, test_file
    ):
        """Test query_files_linq with skip and take for pagination."""
        # Upload 5 files to test pagination
        NUM_FILES = 5
        file_ids = []
        file_prefix = f"{PREFIX}pagination_test_"

        for i in range(NUM_FILES):
            file_name = f"{file_prefix}{i:02d}.bin"
            file_id = test_file(file_name=file_name)
            file_ids.append(file_id)

        # Query with skip=1, take=3
        query_request = FileLinqQueryRequest(
            filter=f'name.StartsWith("{file_prefix}")',
            skip=1,
            take=3,
            order_by=FileLinqQueryOrderBy.CREATED,
            order_by_descending=False,
        )
        response = client.query_files_linq(query=query_request)

        assert response.available_files is not None
        assert response.total_count is not None
        assert response.total_count.value == 3  # skip=1, take=3
        assert len(response.available_files) == 3

        # Verify that we skipped the first file
        returned_ids = [f.id for f in response.available_files]
        for file_id in returned_ids:
            assert file_id in file_ids

        # Verify skip=1 excluded the first file in creation order
        returned_names = [
            f.properties.get("Name", "")
            for f in response.available_files
            if f.properties
        ]
        expected_skipped_file = f"{file_prefix}00.bin"
        assert expected_skipped_file not in returned_names

    def test__search_files__succeeds(
        self, client: FileClient, test_file, random_filename_extension: str
    ):
        """Test search_files with filtering, pagination, and ordering.

        Note: search_files() is not guaranteed to return newly created files immediately
        due to indexing delay (a few seconds). Retry logic with backoff is used to handle
        this eventual consistency behavior.
        """
        # Upload 5 files to test various scenarios
        NUM_FILES = 5
        file_ids = []
        file_prefix = f"{PREFIX}search_test_"

        for i in range(NUM_FILES):
            file_name = f"{file_prefix}_{i}.bin"
            file_id = test_file(file_name=file_name)
            file_ids.append(file_id)

        # Search with filter (by name pattern), pagination, and ordering
        search_request = SearchFilesRequest(
            filter=f'(name: ("{file_prefix}*"))',
            skip=1,
            take=3,
            order_by=SearchFilesOrderBy.NAME,
            order_by_descending=True,
        )

        # Search with retry logic
        @backoff.on_exception(
            backoff.expo,
            (AssertionError, ApiException),
            max_tries=5,
            max_time=10,
        )
        def search_and_verify() -> None:
            response = client.search_files(request=search_request)

            assert response.available_files is not None
            assert response.total_count is not None
            assert response.total_count.value == 3
            assert response.total_count.relation is not None
            assert len(response.available_files) == 3  # skip=1, take=3

            # Verify all fields in response
            for file_metadata in response.available_files:
                assert file_metadata.id in file_ids
                assert file_metadata.properties is not None
                assert file_metadata.properties.get("Name") is not None
                assert file_metadata.properties.get("Name", "").startswith(file_prefix)
                assert file_metadata.created is not None
                assert isinstance(file_metadata.created, datetime)
                assert file_metadata.updated is not None
                assert isinstance(file_metadata.updated, datetime)
                assert file_metadata.workspace is not None
                assert file_metadata.size is not None

            # Verify descending order by name
            returned_names = [
                f.properties.get("Name", "")
                for f in response.available_files
                if f.properties
            ]
            assert returned_names == sorted(returned_names, reverse=True)

            # Verify skip=1 excluded the first file in descending order
            expected_skipped_file = f"{file_prefix}_4.bin"
            assert expected_skipped_file not in returned_names

        search_and_verify()

    def test__search_files__no_filter_succeeds(self, client: FileClient, test_file):
        test_file()

        search_request = SearchFilesRequest(skip=0, take=10)
        response = client.search_files(request=search_request)

        assert response.available_files is not None
        assert response.total_count is not None
        assert response.total_count.value >= 1
        assert len(response.available_files) >= 1

    def test__search_files__invalid_filter_raises(self, client: FileClient):
        search_request = SearchFilesRequest(filter="invalid filter syntax")

        with pytest.raises(ApiException):
            client.search_files(request=search_request)

    def test__search_files__filter_returns_no_results(self, client: FileClient):
        unique_nonexistent_name = (
            f"{PREFIX}nonexistent_search_file_{randint(100000, 999999)}.random_ext"
        )

        search_request = SearchFilesRequest(
            filter=f'(name: ("{unique_nonexistent_name}"))', skip=0, take=10
        )
        response = client.search_files(request=search_request)

        assert response.available_files is not None
        assert len(response.available_files) == 0
        assert response.total_count is not None
        assert response.total_count.value == 0

    def test__start_upload_session__with_invalid_workspace__raises(
        self, client: FileClient
    ):
        invalid_workspace_id = "invalid-workspace-id"

        with pytest.raises(ApiException):
            client.start_upload_session(workspace=invalid_workspace_id)

    def test__append_to_upload_session__uploads_file_in_chunks(
        self, client: FileClient
    ):
        # Create a test file with known content
        test_content = b"A" * 10485760 + b"B" * 5000000  # 10 MB + 5 MB
        chunk_size = 10485760  # 10 MB

        # Start upload session
        session_response = client.start_upload_session()

        # Verify session response
        assert session_response is not None
        assert session_response.session_id is not None
        assert isinstance(session_response.session_id, str)
        assert session_response.created_at is not None
        assert isinstance(session_response.created_at, datetime)

        session_id = session_response.session_id
        file_id = None

        try:
            # Upload first chunk
            first_chunk = BytesIO(test_content[:chunk_size])
            client.append_to_upload_session(
                session_id=session_id, chunk_index=1, chunk=first_chunk
            )

            # Upload second chunk (last chunk)
            second_chunk = BytesIO(test_content[chunk_size:])
            client.append_to_upload_session(
                session_id=session_id, chunk_index=2, chunk=second_chunk, close=True
            )

            # Finish the upload session
            file_name = f"{PREFIX}chunked_upload_test.bin"
            file_id = client.finish_upload_session(
                session_id=session_id,
                name=file_name,
                properties={
                    "Test": "ChunkedUpload",
                    "Description": "Test file from chunked upload",
                },
            )

            # Verify the file was created with correct metadata
            files = client.get_files(ids=[file_id])
            assert files.total_count == 1
            assert len(files.available_files) == 1
            assert files.available_files[0].id == file_id
            assert files.available_files[0].properties is not None
            assert files.available_files[0].properties.get("Name") == file_name
            assert files.available_files[0].properties.get("Test") == "ChunkedUpload"
            assert (
                files.available_files[0].properties.get("Description")
                == "Test file from chunked upload"
            )

            # Verify file content
            downloaded_data = client.download_file(id=file_id)
            assert downloaded_data.read() == test_content
        except ApiException:
            # Finish the upload session if it failed during chunk upload
            if not file_id:
                file_name = f"{PREFIX}chunked_upload_test.bin"
                try:
                    file_id = client.finish_upload_session(
                        session_id=session_id,
                        name=file_name,
                        properties={"Name": file_name, "Test": "ChunkedUpload"},
                    )
                except ApiException:
                    pass

            raise
        finally:
            # Clean up
            if file_id:
                try:
                    client.delete_file(id=file_id)
                except Exception:
                    pass  # Ignore cleanup errors

    def test__finish_upload_session__invalid_session_id_raises(
        self, client: FileClient, invalid_file_id: str
    ):
        file_name = f"{PREFIX}invalid_session.txt"
        properties = {"Name": file_name}

        with pytest.raises(ApiException):
            client.finish_upload_session(
                session_id=invalid_file_id, name=file_name, properties=properties
            )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/notebook/sample_file.ipynb sha256=b4791e1bae57cc73f095ee6b373125d8b62d863dcbdf224c6c3f39d70e6372aa bytes=1121 -->
## FILE: tests/integration/notebook/sample_file.ipynb

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/notebook/sample_file.ipynb`
- sha256: `b4791e1bae57cc73f095ee6b373125d8b62d863dcbdf224c6c3f39d70e6372aa`
- bytes: 1121

````text
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is an example file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with '.venv (Python 3.12.4)' requires the ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'd:/Documents/Python/nisystemlink-clients-python/.venv/Scripts/python.exe -m pip install ipykernel -U --force-reinstall'"
     ]
    }
   ],
   "source": [
    "a = [1,2,3,4,5,6,7,8,9,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/notebook/test_notebook_client.py sha256=0f7fb5b7292d58b9a89e3caec5df4ee75f34cee1fa26a5ab5818ff0d7e15ef2e bytes=35687 -->
## FILE: tests/integration/notebook/test_notebook_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/notebook/test_notebook_client.py`
- sha256: `0f7fb5b7292d58b9a89e3caec5df4ee75f34cee1fa26a5ab5818ff0d7e15ef2e`
- bytes: 35687

````python
import string
from random import choices

import pytest
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.notebook import NotebookClient
from nisystemlink.clients.notebook.models import (
    CreateExecutionRequest,
    ExecutionField,
    ExecutionSortField,
    ExecutionStatus,
    NotebookMetadata,
    QueryExecutionsRequest,
    QueryNotebookRequest,
)
from responses.registries import OrderedRegistry
from uplink.clients.io import blocking_strategy as uplink_blocking_strategy

TEST_FILE_DATA = b"This is a test notebook binary content."
PREFIX = "Notebook Client Tests-"
BASE_URL = "https://test-api.lifecyclesolutions.ni.com"


@pytest.fixture(scope="class")
def client(enterprise_config) -> NotebookClient:
    """Fixture to create a NotebookClient instance."""
    return NotebookClient(enterprise_config)


@pytest.fixture()
def random_filename() -> str:
    """Generate a random filename for each test in test class."""
    rand_file_name = "".join(choices(string.ascii_letters + string.digits, k=10))

    return f"{PREFIX}{rand_file_name}.ipynb"


@pytest.fixture()
def create_notebook(client: NotebookClient):
    """Fixture to return a factory that creates a notebook."""
    notebook_ids = []

    def _create_notebook(
        metadata: NotebookMetadata, cleanup: bool = True
    ) -> NotebookMetadata:

        # file_bytes = file.read()  # Read file as bytes
        with open("tests/integration/notebook/sample_file.ipynb", "rb") as file:
            notebook_response = client.create_notebook(metadata=metadata, content=file)
        if cleanup:
            notebook_ids.append(notebook_response.id)

        return notebook_response

    yield _create_notebook

    if notebook_ids:
        for notebook_id in filter(None, notebook_ids):
            client.delete_notebook(id=notebook_id)


@pytest.mark.enterprise
@pytest.mark.integration
class TestNotebookClient:
    def test__create_notebook_with_valid_file_and_metadata__notebook_created_with_valid_metadata(
        self, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        assert notebook.name == random_filename
        assert notebook.workspace is not None
        assert notebook.created_by is not None
        assert notebook.created_at is not None

    def test__create_notebook_with_invalid_file__raises_ApiException_BadRequest(
        self, client, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        with pytest.raises(ApiException, match="Bad Request"):
            with open(
                "tests/integration/notebook/test_notebook_client.py", "rb"
            ) as file:
                client.create_notebook(metadata=metadata, content=file)

    def test__create_notebook_with_duplicate_file_name__raises_ApiException_BadRequest(
        self, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        create_notebook(metadata=metadata)

        with pytest.raises(ApiException, match="409 Conflict"):
            create_notebook(metadata=metadata)

    def test__create_notebook_with_invalid_workspace__raises_ApiException_BadRequest(
        self, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename, workspace="invalid_workspace")
        with pytest.raises(ApiException, match="Bad Request"):
            create_notebook(metadata=metadata)

    def test__get_notebook_with_valid_id__returns_notebook_with_right_field_values(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        response = client.get_notebook(id=notebook.id)

        assert response.id == notebook.id
        assert response.workspace is not None
        assert response.created_by is not None
        assert response.created_at is not None
        assert response.name == notebook.name == random_filename

    def test__get_notebook_with_invalid_id__raises_ApiException_NotFound(self, client):
        with pytest.raises(ApiException, match="Not Found"):
            client.get_notebook(id="invalid_id")

    def test__update_existing_notebook_metadata__update_notebook_metadata_succeeds(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        [filename, extension] = random_filename.split(".")
        new_name = f"{filename}-updated.{extension}"
        notebook.name = new_name
        notebook.properties = {"key": "value"}

        response = client.update_notebook(id=notebook.id, metadata=notebook)

        assert response.id == notebook.id
        assert response.name != random_filename
        assert response.name == new_name
        assert response.properties == notebook.properties

    def test__update_existing_notebook_content__update_notebook_content_succeeds(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        with open("tests/integration/notebook/sample_file.ipynb", "rb") as file:
            response = client.update_notebook(id=notebook.id, content=file)

        assert response.id == notebook.id

    def test__update_notebook_metadata_with_invalid_id__raises_ApiException_NotFound(
        self, client: NotebookClient
    ):
        metadata = NotebookMetadata(name="invalid_name")
        with pytest.raises(ApiException, match="Not Found"):
            client.update_notebook(id="invalid_id", metadata=metadata)

    def test__update_notebook_content_with_invalid_file__raises_ApiException_BadRequest(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        with open("tests/integration/notebook/test_notebook_client.py", "rb") as file:
            with pytest.raises(ApiException, match="Bad Request"):
                client.update_notebook(id=notebook.id, content=file)

    def test__update_notebook_content_with_duplicate_file_name__raises_ApiException_BadRequest(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        metadata.name = notebook.name = "duplicate_name"
        create_notebook(metadata=metadata)

        with pytest.raises(ApiException, match="409 Conflict"):
            client.update_notebook(id=notebook.id, metadata=notebook)

    def test__update_notebook_with_invalid_workspace__raises_ApiException_BadRequest(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        metadata.workspace = "invalid_workspace"
        with pytest.raises(ApiException, match="Bad Request"):
            client.update_notebook(id=notebook.id, metadata=metadata)

    def test__delete_notebook_with_valid_id__notebook_should_delete_successfully(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata, cleanup=False)

        client.delete_notebook(id=notebook.id)

        with pytest.raises(ApiException, match="Not Found"):
            client.get_notebook(id=notebook.id)

    def test__delete_notebook_with_invalid_id__raises_ApiException_NotFound(
        self, client
    ):
        with pytest.raises(ApiException, match="Not Found"):
            client.delete_notebook(id="invalid_id")

    def test__query_notebook_by_id__return_notebook_matches_id(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        request = QueryNotebookRequest(filter=f'id="{notebook.id}"')
        print(request)
        response = client.query_notebooks(request)

        assert response.notebooks is not None
        assert len(response.notebooks) == 1
        assert response.continuation_token is None
        assert response.notebooks[0].id == notebook.id
        assert response.notebooks[0].name == random_filename

    def test__query_notebook_by_invalid_id__returns_empty_list(self, client):
        request = QueryNotebookRequest(filter='id="invalid_id"')
        response = client.query_notebooks(request)

        assert len(response.notebooks) == 0
        assert response.continuation_token is None

    def test__query_notebook_by_name__returns_notebook_matches_name(
        self, client, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        request = QueryNotebookRequest(filter=f'name.StartsWith("{random_filename}")')
        response = client.query_notebooks(request)

        assert len(response.notebooks) == 1
        assert response.continuation_token is None
        assert response.notebooks[0].id == notebook.id
        assert response.notebooks[0].name == random_filename

    def test__query_notebook_by_invalid_name__returns_empty_list(self, client):
        request = QueryNotebookRequest(filter='name="invalid_name"')
        response = client.query_notebooks(request)

        assert len(response.notebooks) == 0
        assert response.continuation_token is None

    def test__query_by_taking_3_notebooks__returns_3_notebooks(self, client):
        request = QueryNotebookRequest(take=3)
        response = client.query_notebooks(request)

        assert len(response.notebooks) == 3
        assert response.continuation_token is not None

    def test__query_notebooks_by_continuation_token__returns_next_page_of_notebooks(
        self, client
    ):
        request = QueryNotebookRequest(take=3)
        response = client.query_notebooks(request)

        assert len(response.notebooks) == 3
        assert response.continuation_token is not None

        request.continuation_token = response.continuation_token
        response = client.query_notebooks(request)

        assert len(response.notebooks) != 0
        assert response.continuation_token is not None

    def test__get_notebook_content_by_id__returns_notebook_content(
        self, client: NotebookClient, create_notebook, random_filename
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        response = client.get_notebook_content(id=notebook.id)

        with open("tests/integration/notebook/sample_file.ipynb", "rb") as file:
            assert response.read() == file.read()

    def test__get_notebook_content_by_invalid_id__raises_ApiException_NotFound(
        self, client
    ):
        with pytest.raises(ApiException, match="Not Found"):
            client.get_notebook_content(id="invalid_id")

    def test__create_notebook_after_rate_limit_retry__notebook_created_with_valid_metadata(
        self,
        client: NotebookClient,
        random_filename: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = None
        notebook_id = None

        monkeypatch.setattr(uplink_blocking_strategy.time, "sleep", lambda _: None)

        with responses.RequestsMock(registry=OrderedRegistry) as request_mock:
            request_mock.add(
                responses.POST,
                f"{BASE_URL}/ninotebook/v1/notebook",
                status=429,
            )
            request_mock.add_passthru(f"{BASE_URL}/ninotebook/v1/notebook")

            with open("tests/integration/notebook/sample_file.ipynb", "rb") as file:
                notebook = client.create_notebook(metadata=metadata, content=file)
                notebook_id = notebook.id

        try:
            assert notebook is not None
            assert notebook.id is not None
            assert notebook.name == metadata.name
            assert notebook.workspace is not None
            assert notebook.created_by is not None
            assert notebook.created_at is not None
        finally:
            if notebook_id:
                client.delete_notebook(id=notebook_id)

    def test__update_notebook_metadata_after_rate_limit_retry__update_notebook_metadata_succeeds(
        self,
        client: NotebookClient,
        create_notebook,
        random_filename: str,
        monkeypatch: pytest.MonkeyPatch,
    ):
        metadata = NotebookMetadata(name=random_filename)
        notebook = create_notebook(metadata=metadata)

        [filename, extension] = random_filename.split(".")
        new_name = f"{filename}-retry-updated.{extension}"
        notebook.name = new_name
        notebook.properties = {"key": "value"}
        response = None

        monkeypatch.setattr(uplink_blocking_strategy.time, "sleep", lambda _: None)

        with responses.RequestsMock(registry=OrderedRegistry) as request_mock:
            request_mock.add(
                responses.PUT,
                f"{BASE_URL}/ninotebook/v1/notebook/{notebook.id}",
                status=429,
            )
            request_mock.add_passthru(
                f"{BASE_URL}/ninotebook/v1/notebook/{notebook.id}"
            )

            response = client.update_notebook(id=notebook.id, metadata=notebook)

        assert response is not None
        assert response.id == notebook.id
        assert response.name == new_name
        assert response.properties == notebook.properties
        assert response.updated_by is not None
        assert response.updated_at is not None

    @responses.activate
    def test__create_executions_with_valid_notebook_id__returns_executions_with_right_fields(
        self,
        client: NotebookClient,
    ):
        execution_id_1 = "SomeExecutionId1"
        execution_id_2 = "SomeExecutionId2"

        notebook_id_1 = "SomeNotebookId1"
        notebook_id_2 = "SomeNotebookId2"

        workspace_id = "SomeWorkspaceId"
        return_value = {
            "executions": [
                {
                    "cachedResult": False,
                    "id": execution_id_1,
                    "notebookId": notebook_id_1,
                    "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
                    "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "parameters": {},
                    "workspaceId": workspace_id,
                    "timeout": 3600,
                    "retryCount": 0,
                    "status": "QUEUED",
                    "queuedAt": "2024-12-12T02:34:44.0967706Z",
                    "lastUpdatedBy": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "lastUpdatedTimestamp": "2024-12-12T02:34:44.0967706Z",
                    "errorCode": "NO_ERROR",
                    "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
                    "source": {"type": "MANUAL"},
                    "priority": "MEDIUM",
                    "resourceProfile": "DEFAULT",
                },
                {
                    "cachedResult": False,
                    "id": execution_id_2,
                    "notebookId": notebook_id_2,
                    "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
                    "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "parameters": {},
                    "workspaceId": workspace_id,
                    "timeout": 3600,
                    "retryCount": 0,
                    "status": "QUEUED",
                    "queuedAt": "2024-12-12T02:36:13.7375558Z",
                    "lastUpdatedBy": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "lastUpdatedTimestamp": "2024-12-12T02:36:13.7375558Z",
                    "errorCode": "NO_ERROR",
                    "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
                    "source": {"type": "MANUAL"},
                    "priority": "MEDIUM",
                    "resourceProfile": "DEFAULT",
                },
            ]
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/executions",
            json=return_value,
            status=200,
        )

        request_1 = CreateExecutionRequest(
            notebook_id=notebook_id_1, workspace_id=workspace_id
        )
        request_2 = CreateExecutionRequest(
            notebook_id=notebook_id_2, workspace_id=workspace_id
        )

        response = client.create_executions([request_1, request_2])

        assert response.error is None
        assert response.executions is not None
        assert len(response.executions) == 2
        assert response.executions[0].id == execution_id_1
        assert response.executions[1].id == execution_id_2

        assert all(
            execution.workspace_id is not None
            and execution.notebook_id is not None
            and execution.organization_id is not None
            and execution.user_id is not None
            and execution.status == ExecutionStatus.QUEUED
            and execution.queued_at is not None
            and execution.last_updated_timestamp is not None
            and execution.error_code is not None
            and execution.report_settings is not None
            and execution.source is not None
            and execution.priority is not None
            and execution.resource_profile is not None
            and execution.retry_count == 0
            and execution.last_updated_by is not None
            for execution in response.executions
        )

    @responses.activate
    def test__create_executions_with_valid_notebook_id_invalid_workspace__returns_error_and_valid_executions(
        self,
        client: NotebookClient,
    ):
        execution_id_1 = "SomeExecutionId1"

        notebook_id_1 = "SomeNotebookId1"
        notebook_id_2 = "SomeNotebookId2"

        workspace_id = "SomeWorkspaceId"
        return_value = {
            "executions": [
                {
                    "cachedResult": False,
                    "id": execution_id_1,
                    "notebookId": notebook_id_1,
                    "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
                    "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "parameters": {},
                    "workspaceId": workspace_id,
                    "timeout": 3600,
                    "retryCount": 0,
                    "lastUpdatedBy": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "status": "QUEUED",
                    "queuedAt": "2024-12-12T02:34:44.0967706Z",
                    "lastUpdatedTimestamp": "2024-12-12T02:34:44.0967706Z",
                    "errorCode": "NO_ERROR",
                    "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
                    "source": {"type": "MANUAL"},
                    "priority": "MEDIUM",
                    "resourceProfile": "DEFAULT",
                },
            ],
            "error": {
                "name": "Skyline.OneOrMoreErrorsOccurred",
                "code": -251041,
                "message": "One or more errors occurred. See the contained list for details of each error.",
                "args": [],
                "innerErrors": [
                    {
                        "name": "SkylineWebServices.Unauthorized",
                        "code": -252229,
                        "message": "User is not authorized.",
                        "resourceId": notebook_id_2,
                        "args": [],
                        "innerErrors": [],
                    }
                ],
            },
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/executions",
            json=return_value,
            status=200,
        )

        request_1 = CreateExecutionRequest(
            notebook_id=notebook_id_1, workspace_id=workspace_id
        )
        request_2 = CreateExecutionRequest(
            notebook_id=notebook_id_2, workspace_id="invalid_workspace_id"
        )

        response = client.create_executions([request_1, request_2])

        assert response.error is not None
        assert response.executions is not None
        assert len(response.executions) == 1

    @responses.activate
    def test__create_executions_with_invalid_notebook_id__returns_execution(
        self,
        client: NotebookClient,
    ):
        execution_id = "SomeExecutionId1"
        notebook_id = "InvalidNotebookId"
        workspace_id = "SomeWorkspaceId"

        return_value = {
            "executions": [
                {
                    "cachedResult": False,
                    "id": execution_id,
                    "notebookId": notebook_id,
                    "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
                    "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "parameters": {},
                    "workspaceId": workspace_id,
                    "timeout": 3600,
                    "lastUpdatedBy": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                    "retryCount": 0,
                    "status": "QUEUED",
                    "queuedAt": "2024-12-12T02:34:44.0967706Z",
                    "lastUpdatedTimestamp": "2024-12-12T02:34:44.0967706Z",
                    "errorCode": "NO_ERROR",
                    "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
                    "source": {"type": "MANUAL"},
                    "priority": "MEDIUM",
                    "resourceProfile": "DEFAULT",
                },
            ]
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/executions",
            json=return_value,
            status=200,
        )

        request_1 = CreateExecutionRequest(
            notebook_id=notebook_id, workspace_id=workspace_id
        )

        response = client.create_executions([request_1])

        assert response.error is None
        assert response.executions is not None
        assert len(response.executions) == 1
        assert response.executions[0].id == execution_id

    @responses.activate
    def test__get_execution_by_id__returns_execution_with_right_fields(
        self,
        client: NotebookClient,
    ):
        execution_id = "SomeExecutionId1"
        return_value = {
            "id": execution_id,
            "notebookId": "fa479189-d26a-4521-a751-173355a811ce",
            "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
            "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
            "parameters": {},
            "workspaceId": "846e294a-a007-47ac-9fc2-fac07eab240e",
            "timeout": 3600,
            "status": "FAILED",
            "lastUpdatedBy": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
            "retryCount": 0,
            "queuedAt": "2024-12-12T02:46:20.193Z",
            "startedAt": "2024-12-12T02:46:20.202Z",
            "completedAt": "2024-12-12T02:46:50.506Z",
            "lastUpdatedTimestamp": "2024-12-12T02:46:50.506Z",
            "exception": "An error occurred while executing the notebook.",
            "errorCode": "NOTEBOOK_ERROR",
            "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
            "source": {"type": "MANUAL"},
            "priority": "MEDIUM",
            "resourceProfile": "DEFAULT",
        }

        responses.add(
            responses.GET,
            f"{BASE_URL}/ninbexecution/v1/executions/SomeExecutionId1",
            json=return_value,
            status=200,
        )

        execution = client.get_execution_by_id(id=execution_id)

        assert execution.id == execution_id
        assert execution.workspace_id is not None
        assert execution.notebook_id is not None
        assert execution.organization_id is not None
        assert execution.user_id is not None
        assert execution.status is not None
        assert execution.queued_at is not None
        assert execution.last_updated_timestamp is not None
        assert execution.error_code is not None
        assert execution.report_settings is not None
        assert execution.source is not None
        assert execution.priority is not None
        assert execution.resource_profile is not None
        assert execution.last_updated_by is not None
        assert execution.retry_count is not None

    def test__get_execution_by_invalid_id__raises_ApiException_NotFound(
        self,
        client: NotebookClient,
    ):
        with pytest.raises(ApiException, match="Not Found"):
            client.get_execution_by_id(id="InvalidExecutionId")

    @responses.activate
    def test__filter_executions_by_status__returns_executions_matches_status(
        self,
        client: NotebookClient,
    ):
        return_value = [
            {
                "id": "execution_id",
                "notebookId": "fa479189-d26a-4521-a751-173355a811ce",
                "orgId": "f8a1fa16-a180-4a00-b90d-225c0a966848",
                "userId": "7aac74e0-10f7-4a07-93df-d7304a1ed177",
                "parameters": {},
                "workspaceId": "846e294a-a007-47ac-9fc2-fac07eab240e",
                "timeout": 3600,
                "status": "FAILED",
                "queuedAt": "2024-12-12T02:46:20.193Z",
                "startedAt": "2024-12-12T02:46:20.202Z",
                "completedAt": "2024-12-12T02:46:50.506Z",
                "lastUpdatedTimestamp": "2024-12-12T02:46:50.506Z",
                "exception": "An error occurred while executing the notebook.",
                "errorCode": "NOTEBOOK_ERROR",
                "reportSettings": {"format": "NO_REPORT", "excludeCode": False},
                "source": {"type": "MANUAL"},
                "priority": "MEDIUM",
                "resourceProfile": "DEFAULT",
            }
        ]

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/query-executions",
            json=return_value,
            status=200,
        )
        query = QueryExecutionsRequest(
            filter=f"status = {ExecutionStatus.FAILED.value}"
        )
        response = client.query_executions(query)

        assert len(response) == 1

        assert response[0].status == ExecutionStatus.FAILED

    def test__query_executions_by_invalid_filter__raises_ApiException_BadRequest(
        self,
        client: NotebookClient,
    ):

        query = QueryExecutionsRequest(filter="status = 'INVALID_STATUS'")

        with pytest.raises(ApiException, match="Bad Request"):
            client.query_executions(query)

    @responses.activate
    def test__query_executions_by_projection__returns_executions_with_projected_properties(
        self, client: NotebookClient
    ):
        return_value = [
            {
                "id": "execution_id_1",
                "status": "IN_PROGRESS",
            },
            {
                "id": "execution_id_2",
                "status": "TIMED_OUT",
            },
            {
                "id": "execution_id_3",
                "status": "FAILED",
            },
        ]

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/query-executions",
            json=return_value,
            status=200,
        )

        query = QueryExecutionsRequest(
            projection=[ExecutionField.ID, ExecutionField.STATUS]
        )
        response = client.query_executions(query)

        assert all(
            execution.id is not None
            and execution.status is not None
            and execution.workspace_id is None
            and execution.notebook_id is None
            and execution.organization_id is None
            and execution.user_id is None
            and execution.queued_at is None
            and execution.last_updated_timestamp is None
            and execution.error_code is None
            and execution.report_settings is None
            and execution.source is None
            and execution.priority is None
            and execution.resource_profile is None
            for execution in response
        )

    @responses.activate
    def test__query_executions_by_status_in_ascending__returns_executions_sorted_by_status(
        self, client: NotebookClient
    ):
        return_value = [
            {
                "id": "execution_id_1",
                "status": "IN_PROGRESS",
            },
            {
                "id": "execution_id_2",
                "status": "TIMED_OUT",
            },
            {
                "id": "execution_id_3",
                "status": "FAILED",
            },
        ]

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/query-executions",
            json=return_value,
            status=200,
        )

        query = QueryExecutionsRequest(
            order_by=ExecutionSortField.STATUS,
            projection=[ExecutionField.ID, ExecutionField.STATUS],
        )
        response = client.query_executions(query)

        assert response[0].status == ExecutionStatus.IN_PROGRESS
        assert response[1].status == ExecutionStatus.TIMED_OUT
        assert response[2].status == ExecutionStatus.FAILED

    @responses.activate
    def test__query_executions_by_status_in_descending__returns_executions_sorted_by_status(
        self, client: NotebookClient
    ):
        return_value = [
            {
                "id": "execution_id_1",
                "status": "FAILED",
            },
            {
                "id": "execution_id_2",
                "status": "TIMED_OUT",
            },
            {
                "id": "execution_id_3",
                "status": "IN_PROGRESS",
            },
        ]

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/query-executions",
            json=return_value,
            status=200,
        )

        query = QueryExecutionsRequest(
            order_by=ExecutionSortField.STATUS,
            projection=[ExecutionField.ID, ExecutionField.STATUS],
            descending=True,
        )
        response = client.query_executions(query)

        assert response[0].status == ExecutionStatus.FAILED
        assert response[1].status == ExecutionStatus.TIMED_OUT
        assert response[2].status == ExecutionStatus.IN_PROGRESS

    @responses.activate
    def test__cancel_executions__return_inner_errors(self, client: NotebookClient):
        return_value = {
            "error": {
                "name": "Skyline.OneOrMoreErrorsOccurred",
                "code": -251041,
                "message": "One or more errors occurred. See the contained list for details of each error.",
                "args": [],
                "innerErrors": [
                    {
                        "name": "SkylineWebServices.Unauthorized",
                        "code": -252229,
                        "message": "User is not authorized.",
                        "resourceId": "SomeResourceId",
                        "args": [],
                        "innerErrors": [],
                    }
                ],
            },
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/cancel-executions",
            json=return_value,
            status=200,
        )

        response = client.cancel_executions(["execution_id_1", "execution_id_2"])

        assert response is not None
        assert response.name == "Skyline.OneOrMoreErrorsOccurred"
        assert response.inner_errors[0].name == "SkylineWebServices.Unauthorized"

    @responses.activate
    def test__retry_executions__return_inner_errors(self, client: NotebookClient):
        return_value = {
            "error": {
                "name": "Skyline.OneOrMoreErrorsOccurred",
                "code": -251041,
                "message": "One or more errors occurred. See the contained list for details of each error.",
                "args": [],
                "innerErrors": [
                    {
                        "name": "SkylineWebServices.Unauthorized",
                        "code": -252229,
                        "message": "User is not authorized.",
                        "resourceId": "SomeResourceId",
                        "args": [],
                        "innerErrors": [],
                    }
                ],
            },
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/retry-executions",
            json=return_value,
            status=200,
        )

        response = client.retry_executions(["execution_id_1", "execution_id_2"])

        assert response is not None
        assert response.name == "Skyline.OneOrMoreErrorsOccurred"
        assert response.inner_errors[0].name == "SkylineWebServices.Unauthorized"

    @responses.activate
    def test__create_executions_from_existing__return_inner_errors(
        self, client: NotebookClient
    ):
        return_value = {
            "error": {
                "name": "Skyline.OneOrMoreErrorsOccurred",
                "code": -251041,
                "message": "One or more errors occurred. See the contained list for details of each error.",
                "args": [],
                "innerErrors": [
                    {
                        "name": "SkylineWebServices.Unauthorized",
                        "code": -252229,
                        "message": "User is not authorized.",
                        "resourceId": "SomeResourceId",
                        "args": [],
                        "innerErrors": [],
                    }
                ],
            },
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/ninbexecution/v1/create-executions-from-existing",
            json=return_value,
            status=200,
        )

        response = client.create_executions_from_existing(
            ["execution_id_1", "execution_id_2"]
        )

        assert response is not None
        assert response.error is not None
        assert response.error.name == "Skyline.OneOrMoreErrorsOccurred"
        assert response.error.inner_errors[0].name == "SkylineWebServices.Unauthorized"
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/notification/test_notification_client.py sha256=e438a0c2bc4a71b321f91aa2a3558c25b0e67e374d5b75b321e08b7bb041ac8b bytes=9791 -->
## FILE: tests/integration/notification/test_notification_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/notification/test_notification_client.py`
- sha256: `e438a0c2bc4a71b321f91aa2a3558c25b0e67e374d5b75b321e08b7bb041ac8b`
- bytes: 9791

````python
import pytest
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.notification import NotificationClient
from nisystemlink.clients.notification.models import (
    DynamicNotificationConfiguration,
    DynamicNotificationStrategy,
    DynamicStrategyRequest,
    SmtpAddressFields,
    SmtpAddressGroup,
    SmtpMessageTemplate,
    SmtpMessageTemplateFields,
)
from pydantic import ValidationError

BASE_URL = "https://test-api.lifecyclesolutions.ni.com"


@pytest.fixture
def _smtp_address_group():
    """Returns the created address group."""
    return SmtpAddressGroup(
        id="address_group_id",
        display_name="name",
        properties={"property": "value"},
        fields=SmtpAddressFields(
            to_addresses=["address1@example.com"],
            cc_addresses=["address2@example.com"],
            bcc_addresses=["address3@example.com"],
        ),
        referencing_notification_strategies=["reference_notification_strategy"],
    )


@pytest.fixture
def _smtp_message_template():
    """Returns the created message template."""
    return SmtpMessageTemplate(
        id="message_template_id",
        display_name="name",
        properties={"property": "value"},
        fields=SmtpMessageTemplateFields(
            subject_template="subject", body_template="body"
        ),
        referencing_notification_strategies=["reference_notification_strategy"],
    )


@pytest.fixture
def _notification_configuration(
    _smtp_address_group: SmtpAddressGroup, _smtp_message_template: SmtpMessageTemplate
):
    """Returns the created notification configuration."""
    return DynamicNotificationConfiguration(
        address_group_id="address_group_id",
        message_template_id="message_template_id",
        address_group=_smtp_address_group,
        message_template=_smtp_message_template,
    )


@pytest.fixture
def _notification_strategy(
    _notification_configuration: DynamicNotificationConfiguration,
):
    """Returns the created notification strategy."""
    return DynamicNotificationStrategy(
        notification_configurations=[
            _notification_configuration,
        ]
    )


@pytest.fixture
def request_model(
    _notification_strategy: DynamicNotificationStrategy,
):
    """Returns the created request."""
    return DynamicStrategyRequest(
        message_template_substitution_fields={"replacement": "value"},
        notification_strategy=_notification_strategy,
    )


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> NotificationClient:
    """Fixture to create a Notification client."""
    return NotificationClient(enterprise_config)


@pytest.mark.integration
@pytest.mark.enterprise
class TestNotificationClient:
    @responses.activate
    def test__apply_dynamic_strategy_with_correct_request__returns_none(
        self, client: NotificationClient, request_model: DynamicStrategyRequest
    ):
        responses.add(
            responses.POST,
            f"{BASE_URL}/ninotification/v1/apply-dynamic-strategy",
            status=204,
        )
        assert client.apply_dynamic_notification_strategy(request=request_model) is None

    def test__apply_dynamic_strategy_with_invalid_recipient_for_smtp_service__raises_exception(
        self,
        client: NotificationClient,
        _smtp_message_template: SmtpMessageTemplate,
    ):
        address_group = SmtpAddressGroup(
            fields=SmtpAddressFields(to_addresses=["invalid-email"]),
        )

        request_model = DynamicStrategyRequest(
            message_template_substitution_fields={"replacement": "value"},
            notification_strategy=DynamicNotificationStrategy(
                notification_configurations=[
                    DynamicNotificationConfiguration(
                        address_group=address_group,
                        message_template=_smtp_message_template,
                    )
                ]
            ),
        )

        with pytest.raises(ApiException, match="Bad Request") as exc_info:
            client.apply_dynamic_notification_strategy(request=request_model)

        assert exc_info.value.http_status_code == 400

    def test__create_strategy_with_no_configurations__raises_exception(self):
        with pytest.raises(ValidationError):
            DynamicStrategyRequest(
                message_template_substitution_fields={"replacement": "value"},
                notification_strategy=DynamicNotificationStrategy(
                    notification_configurations=[]
                ),
            )

    def test__apply_dynamic_strategy_with_empty_subject_for_smtp_message_template__raises_exception(
        self, client: NotificationClient, _smtp_address_group: SmtpAddressGroup
    ):
        message_template = SmtpMessageTemplate(
            fields=SmtpMessageTemplateFields(subject_template=""),
        )

        request_model = DynamicStrategyRequest(
            message_template_substitution_fields={"replacement": "value"},
            notification_strategy=DynamicNotificationStrategy(
                notification_configurations=[
                    DynamicNotificationConfiguration(
                        address_group=_smtp_address_group,
                        message_template=message_template,
                    )
                ]
            ),
        )

        with pytest.raises(ApiException, match="Bad Request") as exc_info:
            client.apply_dynamic_notification_strategy(request=request_model)

        assert exc_info.value.http_status_code == 400

    def test__create_address_group_with_invalid_interpreting_service_name__raises_exception(
        self,
    ):
        with pytest.raises(ValidationError):
            SmtpAddressGroup(
                interpreting_service_name="invalid_service",
                fields=SmtpAddressFields(to_addresses=["address1@example.com"]),
            )

    @responses.activate
    def test__apply_dynamic_strategy_with_no_address_group_id_and_message_template_id_in_config__returns_none(
        self,
        client: NotificationClient,
        _smtp_address_group: SmtpAddressGroup,
        _smtp_message_template: SmtpMessageTemplate,
    ):
        responses.add(
            responses.POST,
            f"{BASE_URL}/ninotification/v1/apply-dynamic-strategy",
            status=204,
        )
        configuration = DynamicNotificationConfiguration(
            address_group=_smtp_address_group,
            message_template=_smtp_message_template,
        )

        request_model = DynamicStrategyRequest(
            message_template_substitution_fields={"replacement": "value"},
            notification_strategy=DynamicNotificationStrategy(
                notification_configurations=[
                    configuration,
                ]
            ),
        )
        assert client.apply_dynamic_notification_strategy(request=request_model) is None

    @responses.activate
    def test__apply_dynamic_strategy_with_multiple_notification_configurations__returns_none(
        self,
        client: NotificationClient,
        _smtp_address_group: SmtpAddressGroup,
    ):
        responses.add(
            responses.POST,
            f"{BASE_URL}/ninotification/v1/apply-dynamic-strategy",
            status=204,
        )
        first_message_template = SmtpMessageTemplate(
            fields=SmtpMessageTemplateFields(
                subject_template="subject1", body_template="body1"
            ),
        )
        second_message_template = SmtpMessageTemplate(
            fields=SmtpMessageTemplateFields(
                subject_template="subject2", body_template="body2"
            ),
        )

        configuration1 = DynamicNotificationConfiguration(
            address_group=_smtp_address_group,
            message_template=first_message_template,
        )

        configuration2 = DynamicNotificationConfiguration(
            address_group=_smtp_address_group,
            message_template=second_message_template,
        )

        request_model = DynamicStrategyRequest(
            message_template_substitution_fields={"replacement": "value"},
            notification_strategy=DynamicNotificationStrategy(
                notification_configurations=[
                    configuration1,
                    configuration2,
                ]
            ),
        )
        assert client.apply_dynamic_notification_strategy(request=request_model) is None

    def test__create_configuration_with_no_address_group_id_and_address_group__raise_exception(
        self, _smtp_message_template: SmtpMessageTemplate
    ):
        with pytest.raises(
            ValidationError,
            match="One of either AddressGroupId or AddressGroup is required.",
        ):
            DynamicNotificationConfiguration(
                message_template_id="message_template_id",
                message_template=_smtp_message_template,
            )

    def test__create_configuration_with_no_message_template_id_and_message_template__raise_exception(
        self, _smtp_address_group: SmtpAddressGroup
    ):
        with pytest.raises(
            ValidationError,
            match="One of either MessageTemplateId or MessageTemplate is required.",
        ):
            DynamicNotificationConfiguration(
                address_group_id="address_group_id",
                address_group=_smtp_address_group,
            )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/product/test_product_client.py sha256=90ffba2f13512d0d095a015b7ae60b691398550bbc2f7144a39d434da1a483ff bytes=15386 -->
## FILE: tests/integration/product/test_product_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/product/test_product_client.py`
- sha256: `90ffba2f13512d0d095a015b7ae60b691398550bbc2f7144a39d434da1a483ff`
- bytes: 15386

````python
import uuid
from typing import List

import pytest
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.product._product_client import ProductClient
from nisystemlink.clients.product.models import (
    CreateProductRequest,
    CreateProductsPartialSuccess,
    Product,
    ProductField,
    ProductProjection,
    UpdateProductRequest,
)
from nisystemlink.clients.product.models._paged_products import PagedProducts
from nisystemlink.clients.product.models._query_products_request import (
    QueryProductsRequest,
    QueryProductValuesRequest,
)
from nisystemlink.clients.product.utilities import get_products_linked_to_file


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> ProductClient:
    """Fixture to create a ProductClient instance."""
    return ProductClient(enterprise_config)


@pytest.fixture
def unique_identifier() -> str:
    """Unique product id for this test."""
    product_id = uuid.uuid1().hex
    return product_id


@pytest.fixture
def create_update_product_request():
    """Fixture to create a request object for updating products, from a product response"""

    def _create_update_product_request(
        product_response: Product,
    ) -> UpdateProductRequest:
        product_data = product_response.model_dump()

        product_data.pop("updated_at", None)
        product_data.pop("part_number", None)

        return UpdateProductRequest(**product_data)

    return _create_update_product_request


@pytest.fixture
def create_products(client: ProductClient):
    """Fixture to return a factory that creates specs."""
    responses: List[CreateProductsPartialSuccess] = []

    def _create_products(
        products: List[CreateProductRequest],
    ) -> CreateProductsPartialSuccess:
        response = client.create_products(products)
        responses.append(response)
        return response

    yield _create_products

    created_products: List[Product] = []
    for response in responses:
        if response.products:
            created_products = created_products + response.products
    client.delete_products(ids=[str(product.id) for product in created_products])


@pytest.mark.integration
@pytest.mark.enterprise
class TestProductClient:

    def test__create_single_product__one_product_created_with_right_field_values(
        self, client: ProductClient, create_products, unique_identifier
    ):
        part_number = unique_identifier
        name = "Test Name"
        family = "Example Family"
        keywords = ["testing"]
        properties = {"test_property": "yes"}
        product = CreateProductRequest(
            part_number=part_number,
            name=name,
            family=family,
            keywords=keywords,
            properties=properties,
        )

        response: CreateProductsPartialSuccess = create_products([product])
        assert response is not None
        assert len(response.products) == 1
        created_product = response.products[0]
        assert created_product.part_number == part_number
        assert created_product.name == name
        assert created_product.family == family
        assert created_product.keywords == keywords
        assert created_product.properties == properties

    def test__create_multiple_products__multiple_creates_succeed(
        self, client: ProductClient, create_products
    ):
        products = [
            CreateProductRequest(part_number=uuid.uuid1().hex),
            CreateProductRequest(part_number=uuid.uuid1().hex),
        ]
        response: CreateProductsPartialSuccess = create_products(products)
        assert response is not None
        assert len(response.products) == 2

    def test__create_single_product_and_get_products__at_least_one_product_exists(
        self, client: ProductClient, create_products, unique_identifier
    ):
        products = [CreateProductRequest(part_number=unique_identifier)]
        create_products(products)
        get_response = client.get_products_paged()
        assert get_response is not None
        assert len(get_response.products) >= 1

    def test__create_multiple_products_and_get_products_with_take__only_take_returned(
        self, client: ProductClient, create_products, unique_identifier
    ):
        products = [
            CreateProductRequest(part_number=unique_identifier),
            CreateProductRequest(part_number=unique_identifier),
        ]
        create_products(products)
        get_response = client.get_products_paged(take=1)
        assert get_response is not None
        assert len(get_response.products) == 1

    def test__create_multiple_products_and_get_products_with_count_at_least_one_count(
        self, client: ProductClient, create_products, unique_identifier
    ):
        products = [
            CreateProductRequest(part_number=unique_identifier),
            CreateProductRequest(part_number=unique_identifier),
        ]
        create_products(products)
        get_response: PagedProducts = client.get_products_paged(return_count=True)
        assert get_response is not None
        assert get_response.total_count is not None and get_response.total_count >= 2

    def test__get_product_by_id__product_matches_expected(
        self, client: ProductClient, create_products, unique_identifier
    ):
        part_number = unique_identifier
        products = [CreateProductRequest(part_number=part_number)]
        create_response: CreateProductsPartialSuccess = create_products(products)
        assert create_response is not None
        id = str(create_response.products[0].id)
        product = client.get_product(id)
        assert product is not None
        assert product.part_number == part_number

    def test__query_product_by_part_number__matches_expected(
        self, client: ProductClient, create_products, unique_identifier
    ):
        part_number = unique_identifier
        products = [CreateProductRequest(part_number=part_number)]
        create_response: CreateProductsPartialSuccess = create_products(products)
        assert create_response is not None
        query_request = QueryProductsRequest(
            filter=f'partNumber="{part_number}"', return_count=True
        )
        query_response: PagedProducts = client.query_products_paged(query_request)
        assert query_response.total_count == 1
        assert query_response.products[0].part_number == part_number

    def test__query_product_values_for_name__name_matches(
        self, client: ProductClient, create_products, unique_identifier
    ):
        part_number = unique_identifier
        test_name = "query values test"
        create_response: CreateProductsPartialSuccess = create_products(
            [CreateProductRequest(part_number=part_number, name=test_name)]
        )
        assert create_response is not None
        query_request = QueryProductValuesRequest(
            filter=f'partNumber="{part_number}"', field=ProductField.NAME
        )
        query_response: List[str] = client.query_product_values(query_request)
        assert query_response is not None
        assert len(query_response) == 1
        assert query_response[0] == test_name

    def test__update_keywords_with_replace__keywords_replaced(
        self,
        client: ProductClient,
        create_products,
        unique_identifier,
        create_update_product_request,
    ):
        original_keyword = "originalKeyword"
        updated_keyword = "updatedKeyword"
        create_response: CreateProductsPartialSuccess = create_products(
            [
                CreateProductRequest(
                    part_number=unique_identifier, keywords=[original_keyword]
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.products) == 1
        updated_product = create_response.products[0]
        updated_product.keywords = [updated_keyword]
        update_response = client.update_products(
            [create_update_product_request(product_response=updated_product)],
            replace=True,
        )
        assert update_response is not None
        assert len(update_response.products) == 1
        assert (
            update_response.products[0].keywords is not None
            and updated_keyword in update_response.products[0].keywords
        )
        assert original_keyword not in update_response.products[0].keywords

    def test__update_keywords_no_replace__keywords_appended(
        self,
        client: ProductClient,
        create_products,
        unique_identifier,
        create_update_product_request,
    ):
        original_keyword = "originalKeyword"
        additional_keyword = "additionalKeyword"
        create_response: CreateProductsPartialSuccess = create_products(
            [
                CreateProductRequest(
                    part_number=unique_identifier, keywords=[original_keyword]
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.products) == 1
        updated_product = create_response.products[0]
        updated_product.keywords = [additional_keyword]
        update_response = client.update_products(
            [create_update_product_request(product_response=updated_product)],
            replace=False,
        )
        assert update_response is not None
        assert len(update_response.products) == 1
        assert (
            update_response.products[0].keywords is not None
            and original_keyword in update_response.products[0].keywords
        )
        assert (
            update_response.products[0].keywords is not None
            and additional_keyword in update_response.products[0].keywords
        )

    def test__update_properties_with_replace__properties_replaced(
        self,
        client: ProductClient,
        create_products,
        unique_identifier,
        create_update_product_request,
    ):
        new_key = "newKey"
        original_properties = {"originalKey": "originalValue"}
        new_properties = {new_key: "newValue"}
        create_response: CreateProductsPartialSuccess = create_products(
            [
                CreateProductRequest(
                    part_number=unique_identifier, properties=original_properties
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.products) == 1
        updated_product = create_response.products[0]
        updated_product.properties = new_properties
        update_response = client.update_products(
            [create_update_product_request(product_response=updated_product)],
            replace=True,
        )
        assert update_response is not None
        assert len(update_response.products) == 1
        assert (
            update_response.products[0].properties is not None
            and len(update_response.products[0].properties) == 1
        )
        assert new_key in update_response.products[0].properties.keys()
        assert (
            update_response.products[0].properties[new_key] == new_properties[new_key]
        )

    def test__update_properties_append__properties_appended(
        self,
        client: ProductClient,
        create_products,
        unique_identifier,
        create_update_product_request,
    ):
        original_key = "originalKey"
        new_key = "newKey"
        original_properties = {original_key: "originalValue"}
        new_properties = {new_key: "newValue"}
        create_response: CreateProductsPartialSuccess = create_products(
            [
                CreateProductRequest(
                    part_number=unique_identifier, properties=original_properties
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.products) == 1
        updated_product = create_response.products[0]
        updated_product.properties = new_properties
        update_response = client.update_products(
            [create_update_product_request(product_response=updated_product)],
            replace=False,
        )
        assert update_response is not None
        assert len(update_response.products) == 1
        updated_product = update_response.products[0]
        assert (
            updated_product.properties is not None
            and len(updated_product.properties) == 2
        )
        assert original_key in updated_product.properties.keys()
        assert new_key in updated_product.properties.keys()
        assert (
            updated_product.properties[original_key]
            == original_properties[original_key]
        )
        assert updated_product.properties[new_key] == new_properties[new_key]

    def test__query_products_linked_to_files_correct_products_returned(
        self, client: ProductClient, create_products
    ):
        file_id = uuid.uuid1().hex
        product_name_with_file = "Has File"
        products = [
            CreateProductRequest(
                part_number=uuid.uuid1().hex,
                name=product_name_with_file,
                file_ids=[file_id],
            ),
            CreateProductRequest(part_number=uuid.uuid1().hex, name="No File Link"),
        ]
        print(products)
        create_response: CreateProductsPartialSuccess = create_products(products)
        assert create_response is not None
        assert len(create_response.products) == 2
        linked_products = get_products_linked_to_file(client, file_id)
        names = [product.name for product in linked_products]
        assert product_name_with_file in names

    def test__query_products_with_projection__returns_only_specified_fields(
        self, client: ProductClient, create_products, unique_identifier
    ):
        part_number = unique_identifier
        name = "Test Name"
        family = "Example Family"
        keywords = ["testing"]
        properties = {"test_property": "yes"}
        product = CreateProductRequest(
            part_number=part_number,
            name=name,
            family=family,
            keywords=keywords,
            properties=properties,
        )
        response: CreateProductsPartialSuccess = create_products([product])
        assert response is not None

        query_request = QueryProductsRequest(
            filter=f'partNumber=="{part_number}"',
            projection=[ProductProjection.FAMILY, ProductProjection.NAME],
        )
        query_response: PagedProducts = client.query_products_paged(query_request)
        queried_product = query_response.products[0]

        # Assert that the projected fields are returned as expected.
        assert queried_product.family == family
        assert queried_product.name == name
        # Assert that non-projected fields are not returned.
        assert queried_product.part_number is None
        assert queried_product.keywords is None
        assert queried_product.properties is None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/spec/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/spec/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/spec/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/spec/test_spec.py sha256=045a0c73e48a2731a65ffc27ac785ce2fd24127a43c8eac54cb438f1d566aa0c bytes=15329 -->
## FILE: tests/integration/spec/test_spec.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/spec/test_spec.py`
- sha256: `045a0c73e48a2731a65ffc27ac785ce2fd24127a43c8eac54cb438f1d566aa0c`
- bytes: 15329

````python
import uuid
from typing import List

import pytest
from nisystemlink.clients.core._api_exception import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.spec import SpecClient
from nisystemlink.clients.spec.models import (
    Condition,
    ConditionRange,
    ConditionType,
    CreatedSpecification,
    CreateSpecificationsPartialSuccess,
    CreateSpecificationsRequest,
    CreateSpecificationsRequestObject,
    NumericConditionValue,
    QuerySpecificationsRequest,
    SpecificationLimit,
    SpecificationProjection,
    SpecificationType,
    StringConditionValue,
    UpdateSpecificationsRequest,
    UpdateSpecificationsRequestObject,
)


@pytest.fixture(scope="class")
def product() -> str:
    """Unique product id for this test run."""
    product_id = uuid.uuid1().hex
    return product_id


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> SpecClient:
    """Fixture to create a SpecClient instance."""
    return SpecClient(enterprise_config)


@pytest.fixture
def create_specs(client: SpecClient):
    """Fixture to return a factory that creates specs."""
    responses: List[CreateSpecificationsPartialSuccess] = []

    def _create_specs(
        new_specs: CreateSpecificationsRequest,
    ) -> CreateSpecificationsPartialSuccess:
        response = client.create_specs(new_specs)
        responses.append(response)
        return response

    yield _create_specs

    created_specs: List[CreatedSpecification] = []
    for response in responses:
        if response.created_specs:
            created_specs = created_specs + response.created_specs
    client.delete_specs(ids=[spec.id for spec in created_specs])


@pytest.fixture
def create_specs_for_query(create_specs, product):
    """Fixture for creating a set of specs that can be used to test query operations."""
    spec_requests = [
        CreateSpecificationsRequestObject(
            product_id=product,
            spec_id=uuid.uuid1().hex,
            type=SpecificationType.PARAMETRIC,
            category="Parametric Specs",
            name="output voltage",
            limit=SpecificationLimit(min=1.2, max=1.5),
            unit="mV",
        ),
        CreateSpecificationsRequestObject(
            product_id=product,
            spec_id=uuid.uuid1().hex,
            type=SpecificationType.PARAMETRIC,
            category="Parametric Specs",
            name="input voltage",
            limit=SpecificationLimit(min=0.02, max=0.15),
            unit="mV",
            conditions=[
                Condition(
                    name="Temperature",
                    value=NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[ConditionRange(min=-25, step=20, max=85)],
                        discrete=[2, 1.5, 21],
                        unit="C",
                    ),
                ),
                Condition(
                    name="Supply Voltage",
                    value=StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["1.3", "1.5", "1.7"],
                    ),
                ),
            ],
        ),
        CreateSpecificationsRequestObject(
            product_id=product,
            spec_id=uuid.uuid1().hex,
            type=SpecificationType.FUNCTIONAL,
            category="Noise Thresholds",
            name="noise",
        ),
    ]
    return create_specs(CreateSpecificationsRequest(specs=spec_requests))


@pytest.mark.integration
@pytest.mark.enterprise
class TestSpec:
    def test__api_info__returns(self, client: SpecClient):
        response = client.api_info()
        assert len(response.model_dump()) != 0

    def test__create_single_spec__one_created_with_right_field_values(
        self, client: SpecClient, create_specs, product
    ):
        specId = uuid.uuid1().hex
        productId = product
        spec = CreateSpecificationsRequestObject(
            product_id=productId,
            spec_id=specId,
            type=SpecificationType.FUNCTIONAL,
            keywords=["work", "reviewed"],
            category="Parametric Specs",
            block="newBlock",
        )
        response = create_specs(CreateSpecificationsRequest(specs=[spec]))
        assert response is not None
        assert len(response.created_specs) == 1
        created_spec = response.created_specs[0]
        assert created_spec.product_id == productId
        assert created_spec.spec_id == specId

    def test__create_multiple_specs__all_succeed(
        self, client: SpecClient, create_specs, product
    ):
        specIds = ["spec1", "spec2"]
        productId = product
        specs = []
        for id in specIds:
            spec = CreateSpecificationsRequestObject(
                product_id=productId,
                spec_id=id,
                type=SpecificationType.FUNCTIONAL,
                keywords=["work", "reviewed"],
                category="Parametric Specs",
                block="newBlock",
            )
            specs.append(spec)
        response = create_specs(CreateSpecificationsRequest(specs=specs))
        assert response is not None
        assert len(response.created_specs) == 2

    def test__create_duplicate_spec__errors(
        self, client: SpecClient, create_specs, product
    ):
        duplicate_id = uuid.uuid1().hex
        productId = product
        spec = CreateSpecificationsRequestObject(
            product_id=productId,
            spec_id=duplicate_id,
            type=SpecificationType.FUNCTIONAL,
            keywords=["work", "reviewed"],
            category="Parametric Specs",
            block="newBlock",
        )
        response = create_specs(CreateSpecificationsRequest(specs=[spec]))
        assert response is not None
        assert len(response.created_specs) == 1

        fail_response = create_specs(CreateSpecificationsRequest(specs=[spec]))
        assert len(fail_response.failed_specs) == 1
        assert len(fail_response.created_specs) == 0
        assert fail_response.failed_specs[0].spec_id == duplicate_id

    def test__delete_existing_spec__succeeds(self, client: SpecClient, product):
        # Not using the fixture here so that we can inspect delete response.
        specId = uuid.uuid1().hex
        productId = product
        spec = CreateSpecificationsRequestObject(
            product_id=productId,
            spec_id=specId,
            type=SpecificationType.FUNCTIONAL,
        )
        response = client.create_specs(CreateSpecificationsRequest(specs=[spec]))
        assert response.created_specs
        created_spec = response.created_specs[0]

        delete_response = client.delete_specs(ids=[created_spec.id])
        assert delete_response is None

    def test__delete_non_existant_spec__delete_fails(self, client: SpecClient):
        bad_id = "DEADBEEF"
        delete_response = client.delete_specs(ids=[bad_id])
        assert delete_response
        assert delete_response.failed_spec_ids
        assert bad_id in delete_response.failed_spec_ids

    def test__update_single_same_version__version_updates(
        self, client: SpecClient, create_specs, product
    ):
        spec = CreateSpecificationsRequestObject(
            product_id=product,
            spec_id="spec1",
            type=SpecificationType.FUNCTIONAL,
            keywords=["work", "reviewed"],
            category="Parametric Specs",
            block="newBlock",
        )
        response = create_specs(CreateSpecificationsRequest(specs=[spec]))
        assert response is not None
        assert len(response.created_specs) == 1
        created_spec = response.created_specs[0]
        assert created_spec.version == 0

        update_spec = UpdateSpecificationsRequestObject(
            id=created_spec.id,
            product_id=created_spec.product_id,
            spec_id=created_spec.spec_id,
            type=SpecificationType.FUNCTIONAL,
            keywords=["work", "reveiwed"],
            block="modifiedBlock",
            version=created_spec.version,
            workspace=created_spec.workspace,
        )

        update_response = client.update_specs(
            specs=UpdateSpecificationsRequest(specs=[update_spec])
        )
        assert update_response
        assert update_response.updated_specs
        assert len(update_response.updated_specs) == 1
        updated_spec = update_response.updated_specs[0]
        assert updated_spec.version == 1

    def test__get_spec_by_id__spec_matches_expected(
        self, client: SpecClient, create_specs, product
    ):
        productId = product
        spec = CreateSpecificationsRequestObject(
            product_id=productId,
            spec_id="spec1",
            type=SpecificationType.FUNCTIONAL,
            keywords=["work", "reviewed"],
            category="Parametric Specs",
            block="newBlock",
        )

        response = create_specs(CreateSpecificationsRequest(specs=[spec]))

        assert response is not None
        assert len(response.created_specs) == 1
        created_spec = response.created_specs[0]

        get_spec_response = client.get_spec(created_spec.id)

        assert get_spec_response is not None
        assert get_spec_response.id == created_spec.id
        assert get_spec_response.product_id == productId

    def test__get_non_existant_spec_by_id__get_spec_fails(self, client: SpecClient):
        non_existant_spec_id = "10"

        with pytest.raises(ApiException) as exception_info:
            client.get_spec(non_existant_spec_id)

        assert exception_info.value.http_status_code == 404

    def test__query_product__all_returned(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(product_ids=[product])

        response = client.query_specs(request)
        assert response.specs
        assert len(response.specs) == 3

    def test__query_spec_name__two_returned(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product], filter='name.Contains("voltage")'
        )
        response = client.query_specs(request)
        assert response.specs
        assert len(response.specs) == 2

    def test__query_spec_category_one_returned(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product], filter='category == "Noise Thresholds"'
        )
        response = client.query_specs(request)
        assert response.specs
        assert len(response.specs) == 1

    def test__query_input_voltage__conditions_match(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product], filter='name == "input voltage"'
        )
        response = client.query_specs(request)
        assert response.specs
        assert len(response.specs) == 1
        voltage_spec = response.specs[0]
        assert voltage_spec.conditions
        assert len(voltage_spec.conditions) == 2

    def test__query_spec_projection_columns__columns_returned(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product],
            projection=[SpecificationProjection.SPEC_ID, SpecificationProjection.NAME],
        )

        response = client.query_specs(request)
        specs = [vars(spec) for spec in response.specs or []]
        spec_columns = {
            key for spec in specs for key in spec.keys() if spec[key] is not None
        }

        assert response.specs
        assert len(response.specs) == 3
        assert len(spec_columns) == 2
        assert "spec_id" in spec_columns
        assert "name" in spec_columns

    def test__query_specs__returns_condition_value_type_correctly(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product],
            projection=[
                SpecificationProjection.CONDITION_NAME,
                SpecificationProjection.CONDITION_UNIT,
                SpecificationProjection.CONDITION_VALUES,
            ],
        )

        response = client.query_specs(request)

        assert response.specs
        assert len(response.specs) == 3
        condition_1 = (
            response.specs[1].conditions[0].value
            if response.specs[1].conditions
            else None
        )
        condition_2 = (
            response.specs[1].conditions[1].value
            if response.specs[1].conditions
            else None
        )
        condition_1_discrete_values = (
            [discrete for discrete in condition_1.discrete or []] if condition_1 else []
        )
        condition_2_discrete_values = (
            [discrete for discrete in condition_2.discrete or []] if condition_2 else []
        )
        assert isinstance(condition_1, NumericConditionValue)
        assert isinstance(condition_2, StringConditionValue)
        assert isinstance(condition_1_discrete_values[0], int)
        assert isinstance(condition_1_discrete_values[1], float)
        assert isinstance(condition_1_discrete_values[2], int)
        assert isinstance(condition_2_discrete_values[0], str)
        assert isinstance(condition_2_discrete_values[1], str)
        assert isinstance(condition_2_discrete_values[2], str)

    def test__without_condition_type_projection__query_specs__condition_type_field_is_unset(
        self, client: SpecClient, create_specs, create_specs_for_query, product
    ):
        request = QuerySpecificationsRequest(
            product_ids=[product],
            projection=[
                SpecificationProjection.CONDITION_NAME,
                SpecificationProjection.CONDITION_UNIT,
            ],
        )

        response = client.query_specs(request)
        specs = [vars(spec) for spec in response.specs or []]
        condition_columns = ["name", "unit", "range", "discrete", "condition_type"]

        spec_columns = {
            f"condition_{column}"
            for spec in specs
            if "conditions" in spec
            for condition in spec["conditions"]
            for column in condition_columns
            if getattr(condition.value if column != "name" else condition, column, None)
            is not None
        }

        assert response.specs
        assert len(response.specs) == 3
        assert len(spec_columns) == 2
        assert "condition_name" in spec_columns
        assert "condition_unit" in spec_columns
        assert "condition_type" not in spec_columns
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/systems/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/systems/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/systems/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/systems/test_systems.py sha256=8e15e9273f7309b77f8cad271e3fe97fecd95e947cb57b9ad79d95ea24c57bf8 bytes=5832 -->
## FILE: tests/integration/systems/test_systems.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/systems/test_systems.py`
- sha256: `8e15e9273f7309b77f8cad271e3fe97fecd95e947cb57b9ad79d95ea24c57bf8`
- bytes: 5832

````python
from typing import List

import pytest
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.systems._systems_client import SystemsClient
from nisystemlink.clients.systems.models._create_virtual_systems_request import (
    CreateVirtualSystemRequest,
)
from nisystemlink.clients.systems.models._create_virtual_systems_response import (
    CreateVirtualSystemResponse,
)
from nisystemlink.clients.systems.models._query_systems_request import (
    QuerySystemsRequest,
)
from nisystemlink.clients.systems.models._query_systems_response import (
    QuerySystemsResponse,
)
from nisystemlink.clients.systems.models._remove_systems_response import (
    RemoveSystemsResponse,
)


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> SystemsClient:
    """Fixture to create a TestPlanTemplateClient instance."""
    return SystemsClient(enterprise_config)


workspace_id = "2300760d-38c4-48a1-9acb-800260812337"
"""Used the main-test default workspace since the client
for creating a workspace has not been added yet"""


@pytest.fixture
def create_virtual_systems(client: SystemsClient):
    """Fixture to return a factory that create test plan templates."""
    responses: List[CreateVirtualSystemResponse] = []

    def _create_virtual_systems(
        new_virtual_systems: CreateVirtualSystemRequest,
    ) -> CreateVirtualSystemResponse:
        response = client.create_virtual_system(
            create_virtual_system_request=new_virtual_systems
        )
        responses.append(response)
        return response

    yield _create_virtual_systems

    created_virtual_systems_minion_ids: List[str] = []
    for response in responses:
        if response.minionId:
            created_virtual_systems_minion_ids = created_virtual_systems_minion_ids + [
                response.minionId
            ]
        client.remove_systems(tgt=created_virtual_systems_minion_ids)


@pytest.mark.integration
@pytest.mark.enterprise
class TestSystemsClient:
    def test__create_virtual_systems__returns_created_virtual_system(
        self, client: SystemsClient, create_virtual_systems
    ):
        create_virtual_system_request: CreateVirtualSystemRequest = (
            CreateVirtualSystemRequest(
                alias="Python integration virtual system",
                workspace=workspace_id,
            )
        )

        create_virtual_system_response = create_virtual_systems(
            create_virtual_system_request
        )

        minion_id = (
            create_virtual_system_response.minionId
            if create_virtual_system_response
            and create_virtual_system_response.minionId
            else None
        )

        assert minion_id is not None

    def test__query_systems__returns_queried_virtual_system(
        self, client: SystemsClient, create_virtual_systems
    ):
        create_virtual_system_request: CreateVirtualSystemRequest = (
            CreateVirtualSystemRequest(
                alias="Python integration virtual system",
                workspace=workspace_id,
            )
        )

        create_virtual_system_response = create_virtual_systems(
            create_virtual_system_request
        )

        minion_id = (
            create_virtual_system_response.minionId
            if create_virtual_system_response
            and create_virtual_system_response.minionId
            else None
        )

        assert minion_id is not None

        query_virtual_system_response: QuerySystemsResponse = client.query_systems(
            query=QuerySystemsRequest(filter=f'id="{minion_id}"')
        )

        assert query_virtual_system_response.data is not None
        assert len(query_virtual_system_response.data) > 0
        first_item = query_virtual_system_response.data[0]
        assert first_item is not None
        assert first_item["id"] == minion_id

    def test__remove_sytems(self, client: SystemsClient):

        create_virtual_system_request: CreateVirtualSystemRequest = (
            CreateVirtualSystemRequest(
                alias="Python integration query virtual system",
                workspace=workspace_id,
            )
        )

        create_virtual_system_response: CreateVirtualSystemResponse = (
            client.create_virtual_system(
                create_virtual_system_request=create_virtual_system_request
            )
        )

        minion_id = (
            create_virtual_system_response.minionId
            if create_virtual_system_response
            and create_virtual_system_response.minionId
            else None
        )

        assert minion_id is not None

        remove_system_response: RemoveSystemsResponse = client.remove_systems(
            tgt=[minion_id]
        )

        assert remove_system_response.removed_ids is not None
        assert remove_system_response.removed_ids[0] == minion_id

    def test__query_systems_with_projections__returns_the_systems_with_projected_properties(
        self, client: SystemsClient
    ):
        query_systems_request = QuerySystemsRequest(
            filter="grains.data.host != null && grains.data.master != null",
            projection="new(id, alias, grains.data.master as master, grains.data.host as host)",
            take=1,
        )
        response: QuerySystemsResponse = client.query_systems(
            query=query_systems_request
        )

        assert response.data is not None
        assert len(response.data) > 0
        first_item = response.data[0]
        assert first_item is not None
        assert set(first_item.keys()) == {"id", "alias", "master", "host"}
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/tag/__init__.py sha256=a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa bytes=41 -->
## FILE: tests/integration/tag/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/tag/__init__.py`
- sha256: `a7794278821730fa312404d16764275ed726ad665de859394fd0c434095372fa`
- bytes: 41

````python
# -*- coding: utf-8 -*-
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/tag/mixins.py sha256=efd2983eb20cdc8740fe359e89fa725fe7e8c79e53251277d26488d07e117e58 bytes=4478 -->
## FILE: tests/integration/tag/mixins.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/tag/mixins.py`
- sha256: `efd2983eb20cdc8740fe359e89fa725fe7e8c79e53251277d26488d07e117e58`
- bytes: 4478

````python
# noqa: D104
# -*- coding: utf-8 -*-

import uuid

import pytest  # type: ignore
from nisystemlink.clients import tag as tbase
from nisystemlink.clients.core._internal._http_client import HttpClient


class TagBaseMixin:
    @pytest.fixture
    def generate_each_tag_type(self, generate_tag_paths, request, setup_tag_manager):
        """Fixture to generate a tag of each type with a common path prefix and create the tags on the server.

        The tags will be automatically deleted at the end of the current test.

        Returns:
            A 2-tuple containing:
            - The generated tags.
            - The common prefix for each of the generated tags, including the trailing dot.

        Raises:
            nisystemlink.clients.core.ApiException: if the API call fails.
        """

        def fn():
            # Create a tag of each data type.
            data_types = [t for t in tbase.DataType if t != tbase.DataType.UNKNOWN]
            paths, prefix = generate_tag_paths(len(data_types))
            tags = [tbase.TagData(p, t) for (p, t) in zip(paths, data_types)]
            for tag in tags:
                tag.collect_aggregates = True

            request.cls.tag_manager.update(tags)
            return tags, prefix

        return fn

    @pytest.fixture
    def generate_tag_path(self, request, setup_tag_manager):
        """Fixture to generate a tag path to be used within the scope of a single test.

        Args:
            suffix (str | None): Optional suffix to add to the tag for informational
                purposes.

        Returns:
            The generated tag path
        """

        def fn(suffix=None):
            test_class = request.cls.__name__  # .rsplit(".", 1)[-1]
            test_name = request.node.originalname or request.node.name
            path = ".".join(("test", test_class, test_name, str(uuid.uuid4())))
            if suffix:
                path += "." + suffix
            request.cls.created_tags.append(path)
            return path

        return fn

    @pytest.fixture
    def generate_tag_paths(self, request, setup_tag_manager):
        """Generates tag paths to be used within the scope of a single test.

        Args:
            count: The number of paths to generate.

        Returns:
            A 2-tuple containing:
            - The generated tag paths.
            - The common prefix for each of the generated paths, including the trailing dot.
        """

        def fn(count):
            test_class = request.cls.__name__  # .rsplit(".", 1)[-1]
            test_name = request.node.originalname or request.node.name
            prefix = ".".join(("test", test_class, test_name, str(uuid.uuid4()), ""))
            paths = [prefix + str(x) for x in range(count)]
            request.cls.created_tags += paths
            return paths, prefix

        return fn


@pytest.mark.cloud
@pytest.mark.integration
class CloudMixin(TagBaseMixin):
    @pytest.fixture(scope="class", autouse=True)
    def setup_tag_manager(self, verified_tag_config, request):
        request.cls.tag_manager = tbase.TagManager(verified_tag_config)
        request.cls.created_tags = []
        yield
        if request.cls.created_tags:
            request.cls.tag_manager.delete(request.cls.created_tags)

    @pytest.fixture(scope="class")
    def verified_tag_config(self, cloud_config):
        # Verify that we can successfully use the tags API with this config
        client = HttpClient(cloud_config)
        tags = client.at_uri("/nitag/v2")
        tags.get("/tags", params={"path": ""})

        return cloud_config


@pytest.mark.webserver
@pytest.mark.integration
class ServerMixin(TagBaseMixin):
    @pytest.fixture(scope="class", autouse=True)
    def setup_tag_manager(self, verified_tag_config, request):
        request.cls.tag_manager = tbase.TagManager(verified_tag_config)
        request.cls.created_tags = []
        yield
        if request.cls.created_tags:
            request.cls.tag_manager.delete(request.cls.created_tags)

    @pytest.fixture(scope="class")
    def verified_tag_config(self, server_config):
        # Verify that we can successfully use the tags API with this config
        client = HttpClient(server_config)
        tags = client.at_uri("/nitag/v2")
        tags.get("/tags", params={"path": ""})

        return server_config
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/tag/test_tagmanager.py sha256=db8d27e6e21d2dd576c4726d99cf44a666770fa53e925cb759b75d2eeb4d88dc bytes=18544 -->
## FILE: tests/integration/tag/test_tagmanager.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/tag/test_tagmanager.py`
- sha256: `db8d27e6e21d2dd576c4726d99cf44a666770fa53e925cb759b75d2eeb4d88dc`
- bytes: 18544

````python
# -*- coding: utf-8 -*-

import math
import random
import sys
import time
from datetime import datetime, timedelta, timezone

import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase

from .mixins import CloudMixin, ServerMixin


class TagManagerTests:
    def test__write_read_bool_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.BOOLEAN)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write=True,
            )

    def test__write_read_date_time_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.DATE_TIME)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write=datetime.now(timezone.utc),
            )

    def test__write_read_double_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.DOUBLE)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            aggregates = self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write=math.pi,
            )

            assert math.pi == aggregates.min
            assert math.pi == aggregates.max
            assert math.pi == aggregates.mean

    def test__write_read_int_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.INT32)
            tag.collect_aggregates = True

            min_int = -(2**31)
            self.tag_manager.update([tag])
            aggregates = self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write=min_int,
            )

            assert min_int == aggregates.min
            assert min_int == aggregates.max
            assert min_int == aggregates.mean

    def test__write_read_string_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.STRING)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write="testing this tag value",
            )

    def test__write_read_uint64_tag__values_are_correct(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.UINT64)
            tag.collect_aggregates = True

            value = 2**64 - 1
            self.tag_manager.update([tag])
            aggregates = self.internal_test_write_and_read_tag(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                value_to_write=value,
            )

            assert value == aggregates.min
            assert value == aggregates.max
            assert math.isclose(value, aggregates.mean)

    def test__set_double_values__aggregate_values_are_correct(self, generate_tag_path):
        min = -random.random() * sys.float_info.max / 2
        max = random.random() * sys.float_info.max / 2
        mean = (min + max) / 3

        with self.tag_manager.create_writer(buffer_size=3) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.DOUBLE)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            aggregates = self.internal_test_numeric_aggregates(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                mean,
                (0.0, max, min),
            )

            assert math.isclose(min, aggregates.min), (min, aggregates.min)
            assert math.isclose(max, aggregates.max), (max, aggregates.max)

    def test__set_int_values__aggregate_values_are_correct(self, generate_tag_path):
        min = random.randrange(-(2**31), 0)
        max = random.randrange(0, 2**31 - 1)
        mean = (min + max) / 3.0

        with self.tag_manager.create_writer(buffer_size=3) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.INT32)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            aggregates = self.internal_test_numeric_aggregates(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                mean,
                (min, 0, max),
            )

            assert min == aggregates.min
            assert max == aggregates.max

    def test__uint64_aggregates(self, generate_tag_path):
        min = random.randrange(0, 2**31)
        max = random.randrange(2**31, 2**32)
        mean = (min + max + 2**31) / 3.0

        with self.tag_manager.create_writer(buffer_size=3) as writer:
            tag = tbase.TagData(generate_tag_path(), tbase.DataType.UINT64)
            tag.collect_aggregates = True

            self.tag_manager.update([tag])
            aggregates = self.internal_test_numeric_aggregates(
                tag,
                writer,
                tbase.TagValueReader(self.tag_manager, tag),
                mean,
                (max, min, 2**31),
            )

            assert min == aggregates.min
            assert max == aggregates.max

    def test__collect_aggregates_False__aggregates_is_None(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = self.tag_manager.open(
                generate_tag_path(), tbase.DataType.DOUBLE, create=True
            )
            writer.write(tag.path, tag.data_type, math.e)

            for i in range(10):
                value = self.tag_manager.read(
                    tag.path, include_timestamp=False, include_aggregates=True
                )
                if value.value == math.e:
                    break
            else:
                assert value.value == math.e

            assert value.count is None

    def test__special_tag_paths_used__apis_work(self, generate_tag_path):
        paths = ["basic", "space path", "slash/path", "underscore_path"]

        with self.tag_manager.create_writer(buffer_size=1) as writer:
            for path in paths:
                tag = self.tag_manager.open(
                    generate_tag_path(path), tbase.DataType.DOUBLE, create=True
                )
                tag.collect_aggregates = True
                self.tag_manager.update(
                    updates=[
                        tbase.TagDataUpdate.from_tagdata(
                            tag, tbase.TagUpdateFields.COLLECT_AGGREGATES
                        )
                    ]
                )
                self.internal_test_write_and_read_tag(
                    tag, writer, tbase.TagValueReader(self.tag_manager, tag), 3.0
                )
                self.tag_manager.delete([tag])

    def test__update_metadata__queried_metadata_is_correct(self, generate_tag_path):
        tag = tbase.TagData(
            generate_tag_path(),
            tbase.DataType.DOUBLE,
            ["keyword1", "keyword2"],
            {"prop1": "value1", "prop2": "value2"},
        )

        self.tag_manager.update([tag])
        opened_tag = self.tag_manager.open(tag.path)

        assert opened_tag.collect_aggregates is False
        assert tbase.DataType.DOUBLE == opened_tag.data_type
        assert sorted(tag.keywords) == sorted(opened_tag.keywords)
        assert tag.path == opened_tag.path
        assert sorted(tag.properties.items()) == sorted(opened_tag.properties.items())
        assert opened_tag.retention_count is None
        assert opened_tag.retention_days is None
        assert tbase.RetentionType.NONE == opened_tag.retention_type

        tag.collect_aggregates = True
        tag.set_retention_count(30)
        tag.keywords.append("keyword3")
        tag.properties["prop1"] = "edited"
        self.tag_manager.update([tag])
        self.tag_manager.refresh([opened_tag])

        assert opened_tag.collect_aggregates is True
        assert tbase.DataType.DOUBLE == opened_tag.data_type
        assert sorted(tag.keywords) == sorted(opened_tag.keywords)
        assert tag.path == opened_tag.path
        assert sorted(tag.properties.items()) == sorted(opened_tag.properties.items())
        assert 30 == opened_tag.retention_count
        assert opened_tag.retention_days is None
        assert tbase.RetentionType.COUNT == opened_tag.retention_type

    def test__merge_metadata__queried_metadata_is_correct(self, generate_tag_path):
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        tag = tbase.TagData(
            generate_tag_path(), tbase.DataType.DOUBLE, keywords, properties
        )

        self.tag_manager.update([tag])
        opened_tag = self.tag_manager.open(tag.path)

        assert opened_tag.collect_aggregates is False
        assert tbase.DataType.DOUBLE == opened_tag.data_type
        assert sorted(keywords) == sorted(opened_tag.keywords)
        assert tag.path == opened_tag.path
        assert sorted(properties.items()) == sorted(opened_tag.properties.items())
        assert opened_tag.retention_count is None
        assert opened_tag.retention_days is None
        assert tbase.RetentionType.NONE == opened_tag.retention_type

        tag.collect_aggregates = True
        tag.set_retention_count(50)
        tag.keywords[:] = ["keyword3"]
        tag.properties.clear()
        tag.properties.update({"prop1": "edited", "prop3": "value3"})
        self.tag_manager.update(
            updates=[tbase.TagDataUpdate.from_tagdata(tag, tbase.TagUpdateFields.ALL)]
        )
        self.tag_manager.refresh([opened_tag])

        keywords.append("keyword3")
        properties["prop1"] = "edited"
        properties["prop3"] = "value3"
        assert opened_tag.collect_aggregates is True
        assert tbase.DataType.DOUBLE == opened_tag.data_type
        assert sorted(keywords) == sorted(opened_tag.keywords)
        assert tag.path == opened_tag.path
        assert sorted(properties.items()) == sorted(opened_tag.properties.items())
        assert 50 == opened_tag.retention_count
        assert opened_tag.retention_days is None
        assert tbase.RetentionType.COUNT == opened_tag.retention_type

        # First update the collect aggregates and retention settings
        # then do a merge that excludes those properties and verify
        # they are unmodified.
        opened_tag.collect_aggregates = False
        opened_tag.set_retention_days(30)
        tag.properties["prop4"] = "value4"
        self.tag_manager.update([opened_tag])
        self.tag_manager.update(
            updates=[
                tbase.TagDataUpdate.from_tagdata(
                    tag,
                    tbase.TagUpdateFields.KEYWORDS | tbase.TagUpdateFields.PROPERTIES,
                )
            ]
        )
        self.tag_manager.refresh([opened_tag])

        properties["prop4"] = "value4"
        assert opened_tag.collect_aggregates is False
        assert tbase.DataType.DOUBLE == opened_tag.data_type
        assert sorted(keywords) == sorted(opened_tag.keywords)
        assert tag.path == opened_tag.path
        assert sorted(properties.items()) == sorted(opened_tag.properties.items())
        assert 30 == opened_tag.retention_days
        assert tbase.RetentionType.DURATION == opened_tag.retention_type
        assert 50 == opened_tag.retention_count

    def test__change_data_type__raises(self, generate_tag_path):
        tag = self.tag_manager.open(
            generate_tag_path(), tbase.DataType.BOOLEAN, create=True
        )
        tag.data_type = tbase.DataType.DATE_TIME
        with pytest.raises(core.ApiException) as ex:
            self.tag_manager.update([tag])

        assert ex.value.error is not None
        assert ex.value.error.code in (
            -251041,  # Skyline.OneOrMoreErrorsOccurred
            -251907,  # Tag.ConflictingTagTypes
        )

        with pytest.raises(core.ApiException) as ex:
            self.tag_manager.open(tag.path, tbase.DataType.DOUBLE, create=True)
        assert "type" in ex.value.message

    def test__write_wrong_data_type__write_ignored(self, generate_tag_path):
        with self.tag_manager.create_writer(buffer_size=1) as writer:
            tag = self.tag_manager.open(
                generate_tag_path(), tbase.DataType.DOUBLE, create=True
            )
            writer.write(tag.path, tbase.DataType.INT32, 7)
            assert self.tag_manager.read(tag.path) is None

    def test__run_queries__results_are_correct(self, generate_tag_paths):
        num_tags = 10
        even_paths = []
        odd_paths = []
        paths, path_prefix = generate_tag_paths(num_tags)
        tags = [tbase.TagData(p, tbase.DataType.INT32) for p in paths]

        for x, tag in enumerate(tags):
            odd_even = ""

            if x % 2 == 0:
                odd_even = "even"
                even_paths.append(tag.path)
            else:
                odd_even = "odd"
                odd_paths.append(tag.path)

            tag.keywords.append(odd_even)
            tag.properties["index"] = str(x)
            tag.properties["oddEven"] = odd_even

        self.tag_manager.update(tags)

        # Path query
        half_paths = paths[: num_tags // 2]
        self.internal_test_query_result(
            self.tag_manager.query(half_paths), half_paths, num_tags // 2
        )

        # Wildcard query
        self.internal_test_query_result(
            self.tag_manager.query([path_prefix + "*"]), paths, len(paths)
        )

        # Keyword query
        self.internal_test_query_result(
            self.tag_manager.query(paths, keywords=["odd"], properties=None),
            odd_paths,
            len(odd_paths),
        )

        # Property query
        self.internal_test_query_result(
            self.tag_manager.query(
                paths, keywords=None, properties={"oddEven": "even"}
            ),
            even_paths,
            len(even_paths),
        )

        # Pages
        self.internal_test_query_result(
            self.tag_manager.query(paths, skip=1, take=2),
            paths,
            page_size=2,
            skip=1,
            expected_pages=math.ceil((num_tags - 1) / 2.0),
        )

    @classmethod
    def internal_test_query_result(
        cls, query, expected_paths, page_size, skip=0, expected_pages=1
    ):
        expected_list = list(expected_paths)
        assert len(expected_list) == query.total_count

        pages = list(query)
        assert expected_pages == len(pages)
        assert all(len(page) == page_size for page in pages[:-1])
        paths = [tag.path for page in pages for tag in page]

        expected_list[0:skip] = []
        assert sorted(expected_list) == sorted(paths)
        assert expected_pages == len(pages)

    @classmethod
    def internal_test_write_and_read_tag(cls, tag, writer, reader, value_to_write):
        # Shouldn't start with a value.
        assert reader.read(include_timestamp=True, include_aggregates=True) is None

        # Write the value.
        writer.write(tag.path, tag.data_type, value_to_write)

        # Read may not return the value immediately.
        for i in range(10):
            value = reader.read(include_timestamp=True, include_aggregates=True)
            if value is not None:
                break
            time.sleep(0.1)
        else:
            assert value is not None

        # value should be what we wrote.
        assert value_to_write == value.value
        now = datetime.now(timezone.utc)
        assert value.timestamp < now
        assert now - value.timestamp < timedelta(days=1)
        assert value.count is not None
        assert 1 == value.count
        return value

    @classmethod
    def internal_test_numeric_aggregates(cls, tag, writer, reader, mean, values):
        # Shouldn't start with a value.
        assert reader.read(include_timestamp=False, include_aggregates=True) is None

        # Write each value.
        for value in values:
            writer.write(tag.path, tag.data_type, value)

        # Read until each value has been seen.
        num_values = len(values)
        for i in range(10):
            value = reader.read(include_timestamp=False, include_aggregates=True)
            if value is not None and value.count == num_values:
                break
            time.sleep(0.1)
        else:
            assert value is not None and num_values == value.count

        assert value is not None

        # Check the results.
        if isinstance(value, float):
            assert math.isclose(values[-1], value), (values[-1], value)
        else:
            assert values[-1] == value.value

        assert math.isclose(mean, value.mean), (mean, value.mean)
        return value


class TestTagManagerCloud(TagManagerTests, CloudMixin):
    pass


class TestTagManagerServer(TagManagerTests, ServerMixin):
    pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/tag/test_tagselection.py sha256=c0e40ccf27c7e27bf143afe2152783b4bfaf0906d84278d7cdf51f22c0eda236 bytes=8429 -->
## FILE: tests/integration/tag/test_tagselection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/tag/test_tagselection.py`
- sha256: `c0e40ccf27c7e27bf143afe2152783b4bfaf0906d84278d7cdf51f22c0eda236`
- bytes: 8429

````python
# -*- coding: utf-8 -*-

import contextlib
import math
import sys
import time
from datetime import datetime, timezone

import pytest  # type: ignore
from nisystemlink.clients import tag as tbase

from .mixins import CloudMixin, ServerMixin


class TagSelectionTests:
    @pytest.fixture(autouse=True)
    def _gen_tags(self, request, generate_each_tag_type):
        request.cls._tags, request.cls._path_prefix = generate_each_tag_type()

    def test__create_selection_from_tags__paths_and_tags_are_correct(self):
        with self.tag_manager.create_selection(self._tags) as selection:
            paths = [t.path for t in self._tags]
            assert sorted(paths) == sorted(selection.paths)
            assert sorted(paths) == sorted(selection.metadata.keys())

    def test__create_selection_from_paths__paths_and_tags_are_correct(self):
        path_query = self._path_prefix + "*"
        with self.tag_manager.open_selection([path_query]) as selection:
            assert 1 == len(selection.paths)
            assert path_query == selection.paths[0]
            assert sorted([t.path for t in self._tags]) == sorted(
                selection.metadata.keys()
            )

    def test__create_empty_selection__has_no_tags(self):
        with self.tag_manager.create_selection([]) as selection:
            selection.refresh()
            assert 0 == len(selection.paths)
            assert 0 == len(selection.metadata)
            assert 0 == len(selection.values)

    def test__selection_created_for_missing_tag__refresh__selection_has_tag_iff_it_exists(
        self, generate_tag_path
    ):
        missing_path = generate_tag_path(suffix="missing")

        with self.tag_manager.open_selection([missing_path]) as selection:
            assert 0 == len(selection.metadata)
            assert 0 == len(selection.values)

            self.tag_manager.open(missing_path, tbase.DataType.INT32, create=True)
            selection.refresh()

            assert 1 == len(selection.metadata)
            assert 1 == len(selection.values)
            assert missing_path == list(selection.metadata.values())[0].path

            self.tag_manager.delete([missing_path])
            selection.refresh()

            assert 0 == len(selection.metadata)
            assert 0 == len(selection.values)

    def test__some_tags_deleted_or_added__refresh_metadata__tag_list_is_correct(self):
        with self.tag_manager.create_selection(
            self._tags[: len(self._tags) // 2]
        ) as selection:
            selection.delete_tags_from_server()
            selection.add_tags(self._tags)
            selection.refresh_metadata()

            assert sorted(
                [t.path for t in self._tags[len(self._tags) // 2 :]]
            ) == sorted(selection.metadata.keys())

            self.tag_manager.update(self._tags)
            selection.refresh_metadata()

            assert sorted([t.path for t in self._tags]) == sorted(
                selection.metadata.keys()
            )

    def test__write_and_read_some_or_all_selection_tags__values_are_correct(self):
        assert (
            len(self._tags) == 6
        ), "Test needs to be updated to add additional data types"

        with contextlib.ExitStack() as exit_stack:
            selection = exit_stack.enter_context(
                self.tag_manager.create_selection(self._tags)
            )
            writer = exit_stack.enter_context(
                self.tag_manager.create_writer(buffer_size=len(self._tags))
            )

            tags = {t.data_type.name: t for t in self._tags}

            writer.write(tags["BOOLEAN"].path, tags["BOOLEAN"].data_type, True)
            writer.write(tags["DOUBLE"].path, tags["DOUBLE"].data_type, math.pi)
            writer.send_buffered_writes()

            for i in range(10):
                bool_value = selection.read(
                    tags["BOOLEAN"].path,
                    include_timestamp=False,
                    include_aggregates=False,
                ).value
                double_value = selection.read(
                    tags["DOUBLE"].path,
                    include_timestamp=False,
                    include_aggregates=False,
                ).value

                if bool_value is not None and double_value is not None:
                    break

                time.sleep(0.25)
                selection.refresh_values()
            else:
                assert bool_value is not None
                assert double_value is not None

            assert selection.read(tags["BOOLEAN"].path).value is True
            assert selection.read(tags["DATE_TIME"].path) is None
            assert math.pi == selection.read(tags["DOUBLE"].path).value
            assert selection.read(tags["INT32"].path) is None
            assert selection.read(tags["STRING"].path) is None
            assert selection.read(tags["UINT64"].path) is None

            date_value = datetime.now(timezone.utc)
            int_value = -13
            string_value = "hello there"
            uint64_value = 2**31 + 3

            writer.write(tags["BOOLEAN"].path, tags["BOOLEAN"].data_type, False)
            writer.write(
                tags["DATE_TIME"].path, tags["DATE_TIME"].data_type, date_value
            )
            writer.write(tags["INT32"].path, tags["INT32"].data_type, int_value)
            writer.write(tags["STRING"].path, tags["STRING"].data_type, string_value)
            writer.write(tags["UINT64"].path, tags["UINT64"].data_type, uint64_value)
            writer.send_buffered_writes()

            for i in range(10):
                selection.refresh_values()
                if all(selection.read(t.path) is not None for t in tags.values()):
                    break

                time.sleep(0.1)
            else:
                assert all(selection.read(t.path) is not None for t in tags.values())

            assert selection.read(tags["BOOLEAN"].path).value is False
            assert date_value == selection.read(tags["DATE_TIME"].path).value
            assert int_value == selection.read(tags["INT32"].path).value
            assert string_value == selection.read(tags["STRING"].path).value
            assert uint64_value == selection.read(tags["UINT64"].path).value

    def test__reset_aggregates__aggregate_values_are_correct(self):
        with contextlib.ExitStack() as exit_stack:
            selection = exit_stack.enter_context(
                self.tag_manager.create_selection(self._tags)
            )
            writer = exit_stack.enter_context(
                self.tag_manager.create_writer(buffer_size=1)
            )

            dbl_tag = [t for t in self._tags if t.data_type == tbase.DataType.DOUBLE][0]
            writer.write(dbl_tag.path, dbl_tag.data_type, -sys.float_info.max / 2)
            writer.write(dbl_tag.path, dbl_tag.data_type, sys.float_info.max / 2)

            for i in range(10):
                value = self.tag_manager.read(dbl_tag.path).value

                if value == sys.float_info.max / 2:
                    break

                time.sleep(0.25)
                selection.refresh_values()
            else:
                assert sys.float_info.max / 2

            value = self.tag_manager.read(
                dbl_tag.path, include_timestamp=False, include_aggregates=True
            )

            assert value is not None
            assert value.count is not None
            assert 2 == value.count
            assert -sys.float_info.max / 2 == value.min
            assert sys.float_info.max / 2 == value.max

            selection.reset_aggregates()
            selection.refresh_values()
            value = self.tag_manager.read(
                dbl_tag.path, include_timestamp=False, include_aggregates=True
            )
            assert value is not None
            assert sys.float_info.max / 2 == value.value
            assert value.count is not None
            assert 1 == value.count
            assert sys.float_info.max / 2 == value.min
            assert sys.float_info.max / 2 == value.max


class TestTagSelectionCloud(TagSelectionTests, CloudMixin):
    pass


class TestTagSelectionServer(TagSelectionTests, ServerMixin):
    pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/tag/test_tagsubscription.py sha256=02e5b82b9033a8a555b89c073da877bb64cffc67c604f490a51b58f95b5c2f7a bytes=5657 -->
## FILE: tests/integration/tag/test_tagsubscription.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/tag/test_tagsubscription.py`
- sha256: `02e5b82b9033a8a555b89c073da877bb64cffc67c604f490a51b58f95b5c2f7a`
- bytes: 5657

````python
# -*- coding: utf-8 -*-

import contextlib
import math
import time
from datetime import datetime, timedelta, timezone

import pytest  # type: ignore
from nisystemlink.clients import tag as tbase

from .mixins import CloudMixin, ServerMixin


class TagSubscriptionTests:
    @pytest.fixture(autouse=True)
    def _gen_tags(self, request, generate_each_tag_type):
        request.cls._tags, request.cls._path_prefix = generate_each_tag_type()

    def test__create_and_destroy_subscription__no_error(self):
        with contextlib.ExitStack() as exit_stack:
            selection = exit_stack.enter_context(
                self.tag_manager.create_selection(self._tags)
            )
            subscription = exit_stack.enter_context(selection.create_subscription())
            assert subscription is not None

    def test__subscribed_values_updated__subscription_receives_events(self):
        assert (
            len(self._tags) == 6
        ), "Test needs to be updated to add additional data types"

        values = set()
        polling_interval = timedelta(milliseconds=500)
        date_value = datetime.now(timezone.utc)
        bool_value = False
        double_value = math.pi
        int_value = -13
        string_value = "hello there"
        uint64_value = 2**31 + 3

        with contextlib.ExitStack() as exit_stack:
            selection = exit_stack.enter_context(
                self.tag_manager.create_selection(self._tags)
            )
            subscription = exit_stack.enter_context(
                selection.create_subscription(update_interval=polling_interval)
            )
            writer = exit_stack.enter_context(
                self.tag_manager.create_writer(buffer_size=2)
            )

            subscription.tag_changed += lambda tag, reader: values.add((tag, reader))

            tags = {t.data_type.name: t for t in self._tags}
            writer.write(tags["BOOLEAN"].path, tags["BOOLEAN"].data_type, bool_value)
            writer.write(
                tags["DATE_TIME"].path, tags["DATE_TIME"].data_type, date_value
            )
            writer.write(tags["DOUBLE"].path, tags["DOUBLE"].data_type, double_value)
            writer.write(tags["INT32"].path, tags["INT32"].data_type, int_value)
            writer.write(tags["STRING"].path, tags["STRING"].data_type, string_value)
            writer.write(tags["UINT64"].path, tags["UINT64"].data_type, uint64_value)
            writer.send_buffered_writes()

            # Wait for the subscription events to come in.
            for _ in range(10):
                if len(self._tags) == len(values):
                    break
                time.sleep(polling_interval.total_seconds())
            else:
                assert len(self._tags) == len(values)

        # Exactly one of each data type.
        assert len(self._tags) == len(
            values
        )  # len(set(t.tag.data_type for t in values))

        for tag, reader in values:
            assert reader is not None
            if tag.data_type == tbase.DataType.DOUBLE:
                assert double_value == reader.read().value
                break
            elif tag.data_type == tbase.DataType.INT32:
                assert int_value == reader.read().value
                break
            elif tag.data_type == tbase.DataType.STRING:
                assert string_value == reader.read().value
                break
            elif tag.data_type == tbase.DataType.BOOLEAN:
                assert bool_value == reader.read().value
                break
            elif tag.data_type == tbase.DataType.UINT64:
                assert uint64_value == reader.read().value
                break
            elif tag.data_type == tbase.DataType.DATE_TIME:
                assert date_value == reader.read().value
                break
            else:
                assert False, "Unknown data type {}".format(tag.data_type)
                break

    @pytest.mark.slow
    def test__subscription_outlives_heartbeat_interval__events_still_received(self):
        # Ensure the last write happens after at least one heartbeat must have been sent.
        heartbeat_interval = 60
        num_writes = 5
        polling_interval = timedelta(seconds=heartbeat_interval / (num_writes - 1))

        with contextlib.ExitStack() as exit_stack:
            selection = exit_stack.enter_context(
                self.tag_manager.create_selection(self._tags)
            )
            subscription = exit_stack.enter_context(selection.create_subscription())
            writer = exit_stack.enter_context(
                self.tag_manager.create_writer(buffer_size=1)
            )

            int_tag = [t for t in self._tags if t.data_type == tbase.DataType.INT32][0]
            tag_changes = []
            subscription.tag_changed += lambda tag, reader: tag_changes.append(
                (tag, reader)
            )

            for x in range(num_writes):
                writer.write(int_tag.path, int_tag.data_type, x)

                for _ in range(2):
                    if 1 == len(tag_changes):
                        break
                    time.sleep(1 + polling_interval.total_seconds())
                else:
                    assert 1 == len(tag_changes)

                tag, reader = tag_changes.pop(0)
                assert x == reader.read().value


class TestTagSubscriptionCloud(TagSubscriptionTests, CloudMixin):
    pass


class TestTagSubscriptionServer(TagSubscriptionTests, ServerMixin):
    pass
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/test_plan/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/test_plan/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/test_plan/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/test_plan/test_test_plan_client.py sha256=f05492f27fb46ad6c52e816861db3fd2d9f0da9139cc5d87c456e3ef664351c8 bytes=18815 -->
## FILE: tests/integration/test_plan/test_test_plan_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/test_plan/test_test_plan_client.py`
- sha256: `f05492f27fb46ad6c52e816861db3fd2d9f0da9139cc5d87c456e3ef664351c8`
- bytes: 18815

````python
import copy
from datetime import datetime
from typing import List

import pytest
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.test_plan import TestPlanClient
from nisystemlink.clients.test_plan.models import (
    CreateTestPlanRequest,
    CreateTestPlansPartialSuccessResponse,
    CreateTestPlanTemplatePartialSuccessResponse,
    CreateTestPlanTemplateRequest,
    Dashboard,
    ExecutionDefinition,
    Job,
    JobExecution,
    ManualExecution,
    QueryTestPlansRequest,
    QueryTestPlanTemplatesRequest,
    ScheduleTestPlanRequest,
    ScheduleTestPlansRequest,
    State,
    TestPlan,
    TestPlanField,
    TestPlanTemplate,
    TestPlanTemplateField,
    UpdateTestPlanRequest,
    UpdateTestPlansRequest,
)


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> TestPlanClient:
    """Fixture to create a TestPlansClient instance"""
    return TestPlanClient(enterprise_config)


@pytest.fixture
def create_test_plans(client: TestPlanClient):
    """Fixture to return a factory that create test plans."""
    responses: List[CreateTestPlansPartialSuccessResponse] = []

    def _create_test_plans(
        new_test_plans: List[CreateTestPlanRequest],
    ) -> CreateTestPlansPartialSuccessResponse:
        response = client.create_test_plans(test_plans=new_test_plans)
        responses.append(response)
        return response

    yield _create_test_plans

    created_test_plans: List[TestPlan] = []
    for response in responses:
        if response.created_test_plans:
            created_test_plans += response.created_test_plans

    client.delete_test_plans(
        ids=[
            test_plans.id
            for test_plans in created_test_plans
            if test_plans.id is not None
        ]
    )


@pytest.fixture
def create_test_plan_templates(client: TestPlanClient):
    """Fixture to return a factory that create test plan templates."""
    responses: List[CreateTestPlanTemplatePartialSuccessResponse] = []

    def _create_test_plan_templates(
        new_test_plan_templates: List[CreateTestPlanTemplateRequest],
    ) -> CreateTestPlanTemplatePartialSuccessResponse:
        response = client.create_test_plan_templates(
            test_plan_templates=new_test_plan_templates
        )
        responses.append(response)
        return response

    yield _create_test_plan_templates

    created_test_plan_templates: List[TestPlanTemplate] = []
    for response in responses:
        if response.created_test_plan_templates:
            created_test_plan_templates = (
                created_test_plan_templates + response.created_test_plan_templates
            )
    client.delete_test_plan_templates(
        ids=[
            test_plan_template.id
            for test_plan_template in created_test_plan_templates
            if test_plan_template.id is not None
        ]
    )


@pytest.mark.integration
@pytest.mark.enterprise
class TestTestPlanClient:

    _workspace = "2300760d-38c4-48a1-9acb-800260812337"
    """Used the main-test default workspace since the client
    for creating a workspace has not been added yet"""

    _dashboard = Dashboard(
        id="DashBoardId", variables={"product": "PXIe-4080", "location": "Lab1"}
    )

    _execution_actions: List[ExecutionDefinition] = [
        ManualExecution(action="boot", type="MANUAL"),
        JobExecution(
            action="run",
            type="JOB",
            jobs=[
                Job(
                    functions=["run_test_suite"],
                    arguments=[["test_suite.py"]],
                    metadata={"env": "staging"},
                )
            ],
            systemId="system-001",
        ),
    ]

    _test_plan_create = [
        CreateTestPlanRequest(
            name="Python integration test plan",
            state="NEW",
            description="Test plan for verifying integration flow",
            assigned_to="test.user@example.com",
            estimated_duration_in_seconds=86400,
            properties={"env": "staging", "priority": "high"},
            part_number="px40482",
            dut_id="Sample-Dut_Id",
            dut_serial_number="Sample-Dut_serial_number",
            test_program="TP-Integration-001",
            system_filter="os:linux AND arch:x64",
            dut_filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
            workspace=_workspace,
            file_ids_from_template=["file1", "file2"],
            dashboard=_dashboard,
            execution_actions=_execution_actions,
        )
    ]
    """create test plan request object."""

    _create_test_plan_template_request = [
        CreateTestPlanTemplateRequest(
            name="Python integration test plan template",
            template_group="sample template group",
            product_families=["FamilyA", "FamilyB"],
            part_numbers=["PN-1001", "PN-1002"],
            summary="Template for running integration test plans",
            description="This template defines execution steps for integration workflows.",
            test_program="TP-INT-002",
            estimated_duration_in_seconds=86400,
            system_filter="os:linux AND arch:x64",
            dut_filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
            execution_actions=_execution_actions,
            file_ids=["file1", "file2"],
            workspace=_workspace,
            properties={"env": "staging", "priority": "high"},
            dashboard=_dashboard,
        )
    ]
    """create test plan template request object."""

    def test__create_and_delete_test_plan__returns_created_and_deleted_test_plans(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_template_response = client.create_test_plan_templates(
            test_plan_templates=self._create_test_plan_template_request
        )

        template_id = (
            create_test_plan_template_response.created_test_plan_templates[0].id
            if create_test_plan_template_response.created_test_plan_templates
            and create_test_plan_template_response.created_test_plan_templates[0].id
            else None
        )

        assert template_id is not None

        test_plan_request = copy.deepcopy(self._test_plan_create)
        test_plan_request[0].template_id = template_id

        create_test_plan_response = create_test_plans(test_plan_request)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]

        get_test_plan_response: TestPlan = client.get_test_plan(created_test_plan.id)

        delete_test_plan_template_response = client.delete_test_plan_templates(
            ids=[template_id]
        )

        assert delete_test_plan_template_response is None

        assert created_test_plan is not None
        assert created_test_plan.name == "Python integration test plan"
        assert created_test_plan.state == State.NEW
        assert created_test_plan.part_number == "px40482"
        assert get_test_plan_response is not None
        assert get_test_plan_response.name == "Python integration test plan"

    def test__get_test_plan__returns_get_test_plan(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_response = create_test_plans(self._test_plan_create)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]

        get_test_plan_response: TestPlan = client.get_test_plan(created_test_plan.id)

        assert get_test_plan_response is not None
        assert isinstance(get_test_plan_response, TestPlan)
        assert get_test_plan_response.id == created_test_plan.id

    def test__update_test_plan__returns_updated_test_plan(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_response = create_test_plans(self._test_plan_create)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]

        update_test_plans_request = UpdateTestPlansRequest(
            test_plans=[
                UpdateTestPlanRequest(
                    id=created_test_plan.id,
                    name="Updated Test Plan",
                )
            ]
        )
        update_test_plans_response = client.update_test_plans(
            update_request=update_test_plans_request
        )

        assert update_test_plans_response.updated_test_plans is not None

        updated_test_plan = update_test_plans_response.updated_test_plans[0]
        assert updated_test_plan.id == created_test_plan.id
        assert updated_test_plan.name == "Updated Test Plan"

    def test__schedule_test_plan__returns_scheduled_test_plan(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_response = create_test_plans(self._test_plan_create)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]

        schedule_test_plans_request = ScheduleTestPlansRequest(
            test_plans=[
                ScheduleTestPlanRequest(
                    id=created_test_plan.id,
                    planned_start_date_time=datetime.strptime(
                        "2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    estimated_end_date_time=datetime.strptime(
                        "2025-05-22T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    system_id="fake-system",
                )
            ]
        )
        schedule_test_plans_response = client.schedule_test_plans(
            schedule_request=schedule_test_plans_request
        )

        assert schedule_test_plans_response.scheduled_test_plans is not None

        scheduled_test_plan = schedule_test_plans_response.scheduled_test_plans[0]
        assert scheduled_test_plan.id == created_test_plan.id
        assert scheduled_test_plan.planned_start_date_time == datetime.strptime(
            "2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        assert scheduled_test_plan.system_id == "fake-system"

    def test__query_test_plans__return_queried_test_plan(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_response = create_test_plans(self._test_plan_create)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]

        query_test_plans_request = QueryTestPlansRequest(
            filter=f'id = "{created_test_plan.id}"', return_count=True
        )
        queried_test_plans_response = client.query_test_plans(
            query_request=query_test_plans_request
        )

        assert queried_test_plans_response is not None
        assert queried_test_plans_response.test_plans[0].id == created_test_plan.id
        assert queried_test_plans_response.total_count is not None
        assert queried_test_plans_response.total_count > 0

    def test__query_test_plans_with_projections__returns_the_test_plans_with_projected_properties(
        self, client: TestPlanClient, create_test_plans
    ):
        create_test_plan_response = create_test_plans(self._test_plan_create)

        assert create_test_plan_response.created_test_plans is not None

        created_test_plan = create_test_plan_response.created_test_plans[0]
        query_test_plans_request = QueryTestPlansRequest(
            filter=f'id = "{created_test_plan.id}"',
            projection=[TestPlanField.ID, TestPlanField.NAME],
            take=1,
        )
        response = client.query_test_plans(query_request=query_test_plans_request)

        assert response is not None
        test_plan = response.test_plans[0]
        assert (
            test_plan.id is not None
            and test_plan.name is not None
            and test_plan.template_id is None
            and test_plan.state is None
            and test_plan.substate is None
            and test_plan.description is None
            and test_plan.assigned_to is None
            and test_plan.work_order_id is None
            and test_plan.work_order_name is None
            and test_plan.workspace is None
            and test_plan.created_by is None
            and test_plan.updated_at is None
            and test_plan.created_at is None
            and test_plan.updated_by is None
            and test_plan.properties is None
            and test_plan.part_number is None
            and test_plan.dut_id is None
            and test_plan.dut_serial_number is None
            and test_plan.test_program is None
            and test_plan.system_filter is None
            and test_plan.dut_filter is None
            and test_plan.fixture_ids is None
            and test_plan.system_id is None
            and test_plan.planned_start_date_time is None
            and test_plan.estimated_duration_in_seconds is None
            and test_plan.estimated_end_date_time is None
            and test_plan.file_ids_from_template is None
            and test_plan.execution_actions is None
            and test_plan.execution_history is None
            and test_plan.dashboard_url is None
            and test_plan.dashboard is None
        )

    def test__create_test_plan_template__returns_created_test_plan_template(
        self, client: TestPlanClient, create_test_plan_templates
    ):
        create_test_plan_template_response = create_test_plan_templates(
            self._create_test_plan_template_request
        )

        template_id = (
            create_test_plan_template_response.created_test_plan_templates[0].id
            if create_test_plan_template_response.created_test_plan_templates
            and create_test_plan_template_response.created_test_plan_templates[0].id
            else None
        )

        assert template_id is not None
        assert (
            create_test_plan_template_response.created_test_plan_templates[0].name
            == self._create_test_plan_template_request[0].name
        )

    def test__query_test_plan_template__returns_queried_test_plan_template(
        self, client: TestPlanClient, create_test_plan_templates
    ):
        create_test_plan_template_response = create_test_plan_templates(
            self._create_test_plan_template_request
        )

        template_id = (
            create_test_plan_template_response.created_test_plan_templates[0].id
            if create_test_plan_template_response.created_test_plan_templates
            and create_test_plan_template_response.created_test_plan_templates[0].id
            else None
        )

        assert template_id is not None

        query = QueryTestPlanTemplatesRequest(filter=f'id="{template_id}"', take=1)

        query_test_plan_template_response = client.query_test_plan_templates(
            query_test_plan_templates=query
        )

        assert len(query_test_plan_template_response.test_plan_templates) == 1, query
        assert (
            query_test_plan_template_response.test_plan_templates[0].id == template_id
        )

    def test__delete_test_plan_template(self, client: TestPlanClient):
        create_test_plan_template_response: (
            CreateTestPlanTemplatePartialSuccessResponse
        ) = client.create_test_plan_templates(
            test_plan_templates=self._create_test_plan_template_request
        )

        template_id = (
            create_test_plan_template_response.created_test_plan_templates[0].id
            if create_test_plan_template_response.created_test_plan_templates
            and create_test_plan_template_response.created_test_plan_templates[0].id
            else None
        )

        assert template_id is not None

        client.delete_test_plan_templates(ids=[template_id])

        query_deleted_test_plan_template_response = client.query_test_plan_templates(
            query_test_plan_templates=QueryTestPlanTemplatesRequest(
                filter=f'id="{template_id}"', take=1
            )
        )

        assert len(query_deleted_test_plan_template_response.test_plan_templates) == 0

    def test__query_test_plan_templates_with_projections__returns_test_plan_templates_with_projected_properties(
        self, client: TestPlanClient, create_test_plan_templates
    ):
        create_test_plan_template_response = create_test_plan_templates(
            self._create_test_plan_template_request
        )

        template_id = (
            create_test_plan_template_response.created_test_plan_templates[0].id
            if create_test_plan_template_response.created_test_plan_templates
            and create_test_plan_template_response.created_test_plan_templates[0].id
            else None
        )

        assert template_id is not None

        query = QueryTestPlanTemplatesRequest(
            filter=f'id="{template_id}"',
            projection=[TestPlanTemplateField.ID, TestPlanTemplateField.NAME],
            take=1,
        )
        print(query)
        response = client.query_test_plan_templates(query_test_plan_templates=query)

        assert response is not None
        test_plan_template = response.test_plan_templates[0]
        assert (
            test_plan_template.id is not None
            and test_plan_template.name is not None
            and test_plan_template.template_group is None
            and test_plan_template.product_families is None
            and test_plan_template.part_numbers is None
            and test_plan_template.summary is None
            and test_plan_template.description is None
            and test_plan_template.test_program is None
            and test_plan_template.estimated_duration_in_seconds is None
            and test_plan_template.system_filter is None
            and test_plan_template.dut_filter is None
            and test_plan_template.execution_actions is None
            and test_plan_template.file_ids is None
            and test_plan_template.workspace is None
            and test_plan_template.properties is None
            and test_plan_template.dashboard is None
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/testmonitor/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/testmonitor/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/testmonitor/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/testmonitor/test_testmonitor.py sha256=3a591a29443ec9a1c32bd985ceacbc83df458bf033573a985bdbe48ec0571ecd bytes=39368 -->
## FILE: tests/integration/testmonitor/test_testmonitor.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/testmonitor/test_testmonitor.py`
- sha256: `3a591a29443ec9a1c32bd985ceacbc83df458bf033573a985bdbe48ec0571ecd`
- bytes: 39368

````python
import uuid
from typing import cast, Dict, List

import pytest
from nisystemlink.clients.core._api_exception import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.product._product_client import ProductClient
from nisystemlink.clients.product.models._query_products_request import (
    ProductField,
    QueryProductValuesRequest,
)
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.testmonitor.models import (
    CreateResultRequest,
    CreateResultsPartialSuccess,
    CreateStepRequest,
    CreateStepsPartialSuccess,
    PagedSteps,
    QueryStepsRequest,
    QueryStepValuesRequest,
    Result,
    Status,
    Step,
    StepField,
    StepIdResultIdPair,
    UpdateResultRequest,
    UpdateStepRequest,
    UpdateStepsPartialSuccess,
)
from nisystemlink.clients.testmonitor.models._named_value import NamedValue
from nisystemlink.clients.testmonitor.models._paged_results import PagedResults
from nisystemlink.clients.testmonitor.models._query_results_request import (
    QueryResultsRequest,
    QueryResultValuesRequest,
    ResultField,
    ResultProjection,
)
from nisystemlink.clients.testmonitor.models._step_data import Measurement, StepData


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> TestMonitorClient:
    """Fixture to create a TestMonitorClient instance."""
    return TestMonitorClient(enterprise_config)


@pytest.fixture(scope="class")
def product_client(enterprise_config: HttpConfiguration) -> ProductClient:
    """Fixture to create a ProductClient instance."""
    return ProductClient(enterprise_config)


@pytest.fixture
def unique_identifier() -> str:
    """Unique result/step id for this test."""
    unique_id = uuid.uuid1().hex
    return unique_id


@pytest.fixture
def create_results(client: TestMonitorClient, product_client: ProductClient):
    """Fixture to return a factory that creates results."""
    responses: List[CreateResultsPartialSuccess] = []

    def _create_results(
        results: List[CreateResultRequest],
    ) -> CreateResultsPartialSuccess:
        response = client.create_results(results)
        responses.append(response)
        return response

    yield _create_results

    created_results: List[Result] = []
    for response in responses:
        if response.results:
            created_results = created_results + response.results

    part_numbers_of_created_products = set(
        result.part_number for result in created_results
    )

    client.delete_results(ids=[str(result.id) for result in created_results])

    product_filter_string = " or ".join(
        [
            f'partNumber="{part_number}"'
            for part_number in part_numbers_of_created_products
        ]
    )
    created_product_ids = product_client.query_product_values(
        QueryProductValuesRequest(filter=product_filter_string, field=ProductField.ID)
    )

    product_client.delete_products(ids=created_product_ids)


@pytest.fixture
def create_steps(client: TestMonitorClient):
    """Fixture to return a factory that creates steps."""
    responses: List[CreateStepsPartialSuccess] = []

    def _create_steps(
        steps: List[CreateStepRequest],
    ) -> CreateStepsPartialSuccess:
        response = client.create_steps(steps)
        responses.append(response)
        return response

    yield _create_steps

    created_steps: List[Step] = []
    for response in responses:
        if response.steps:
            created_steps = created_steps + response.steps
    client.delete_steps(
        [
            StepIdResultIdPair(
                step_id=cast(str, step.step_id), result_id=cast(str, step.result_id)
            )
            for step in created_steps
        ]
    )


@pytest.mark.integration
@pytest.mark.enterprise
class TestTestMonitor:
    def test__api_info__returns(self, client: TestMonitorClient):
        response = client.api_info()
        assert len(response.model_dump()) != 0

    def test__create_single_result__one_result_created_with_right_field_values(
        self, client: TestMonitorClient, create_results
    ):
        part_number = "Python Client Testing"
        keywords = ["testing"]
        properties: Dict[str, str | None] = {"test_property": "yes"}
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        host_name = "Test Host"
        system_id = "Test System"
        serial_number = "Test Serial Number"
        result = CreateResultRequest(
            part_number=part_number,
            keywords=keywords,
            properties=properties,
            program_name=program_name,
            status=status,
            host_name=host_name,
            system_id=system_id,
            serial_number=serial_number,
        )

        response: CreateResultsPartialSuccess = create_results([result])

        assert response is not None
        assert len(response.results) == 1
        created_result = response.results[0]
        assert created_result.part_number == part_number
        assert created_result.keywords == keywords
        assert created_result.properties == properties
        assert created_result.program_name == program_name
        assert created_result.status == status
        assert created_result.host_name == host_name
        assert created_result.system_id == system_id
        assert created_result.serial_number == serial_number

    def test__create_multiple_results__multiple_creates_succeed(
        self, client: TestMonitorClient, create_results
    ):
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        results = [
            CreateResultRequest(
                part_number=uuid.uuid1().hex, program_name=program_name, status=status
            ),
            CreateResultRequest(
                part_number=uuid.uuid1().hex, program_name=program_name, status=status
            ),
        ]

        response: CreateResultsPartialSuccess = create_results(results)

        assert response is not None
        assert len(response.results) == 2

    def test__create_single_result_and_get_results__at_least_one_result_exists(
        self, client: TestMonitorClient, create_results
    ):
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name=program_name,
                status=status,
                properties={"test": None},
            )
        ]
        create_results(results)

        get_response = client.get_results()

        assert get_response is not None
        assert len(get_response.results) >= 1

    def test__create_multiple_results_and_get_results_with_take__only_take_returned(
        self, client: TestMonitorClient, create_results
    ):
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name=program_name,
                status=status,
            ),
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name=program_name,
                status=status,
            ),
        ]
        create_results(results)

        get_response = client.get_results(take=1)

        assert get_response is not None
        assert len(get_response.results) == 1

    def test__create_multiple_results_and_get_results_with_count_at_least_one_count(
        self, client: TestMonitorClient, create_results
    ):
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name=program_name,
                status=status,
            ),
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name=program_name,
                status=status,
            ),
        ]
        create_results(results)

        get_response: PagedResults = client.get_results(return_count=True)

        assert get_response is not None
        assert get_response.total_count is not None and get_response.total_count >= 2

    def test__get_result_by_id__result_matches_expected(
        self, client: TestMonitorClient, create_results
    ):
        part_number = "Python Client Testing"
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        results = [
            CreateResultRequest(
                part_number=part_number, program_name=program_name, status=status
            )
        ]

        create_response: CreateResultsPartialSuccess = create_results(results)

        assert create_response is not None
        id = str(create_response.results[0].id)
        result = client.get_result(id)
        assert result is not None
        assert result.part_number == part_number
        assert result.program_name == program_name
        assert result.status == status

    def test__query_result_by_part_number_and_serial_number_with_projection__results_with_only_projected_fields(
        self, client: TestMonitorClient, create_results, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                serial_number=unique_identifier,
                status=Status.PASSED(),
            )
        ]
        create_response: CreateResultsPartialSuccess = create_results(results)
        assert create_response is not None

        query_request = QueryResultsRequest(
            filter=f'partNumber="{results[0].part_number}" and serialNumber="{results[0].serial_number}"',
            projection=[
                ResultProjection.ID,
                ResultProjection.PART_NUMBER,
                ResultProjection.SERIAL_NUMBER,
            ],
            return_count=True,
        )
        query_response: PagedResults = client.query_results(query_request)

        assert query_response.total_count == 1
        assert len(query_response.results) == 1
        assert query_response.results[0].part_number == results[0].part_number
        assert query_response.results[0].serial_number == results[0].serial_number
        assert set(query_response.results[0].model_fields_set) == {
            "id",
            "part_number",
            "serial_number",
        }

    def test__query_result_values_for_program_name__name_matches(
        self, client: TestMonitorClient, create_results, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                serial_number=unique_identifier,
                status=Status.PASSED(),
            )
        ]

        create_response: CreateResultsPartialSuccess = create_results(results)
        assert create_response is not None
        query_request = QueryResultValuesRequest(
            filter=f'partNumber="{results[0].part_number}" and serialNumber="{results[0].serial_number}"',
            field=ResultField.PROGRAM_NAME,
        )
        query_response: List[str] = client.query_result_values(query_request)

        assert query_response is not None
        assert len(query_response) == 1
        assert query_response[0] == results[0].program_name

    def test__update_keywords_with_replace__keywords_replaced(
        self, client: TestMonitorClient, create_results
    ):
        original_keyword = "originalKeyword"
        updated_keyword = "updatedKeyword"
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        create_response: CreateResultsPartialSuccess = create_results(
            [
                CreateResultRequest(
                    part_number="Python Client Testing",
                    keywords=[original_keyword],
                    program_name=program_name,
                    status=status,
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.results) == 1

        updated_result = self.__map_result_to_update_result_request(
            create_response.results[0]
        )
        updated_result.keywords = [updated_keyword]
        update_response = client.update_results([updated_result], replace=True)

        assert update_response is not None
        assert len(update_response.results) == 1
        assert (
            update_response.results[0].keywords is not None
            and updated_keyword in update_response.results[0].keywords
        )
        assert original_keyword not in update_response.results[0].keywords

    def test__update_keywords_no_replace__keywords_appended(
        self, client: TestMonitorClient, create_results
    ):
        original_keyword = "originalKeyword"
        additional_keyword = "additionalKeyword"
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        create_response: CreateResultsPartialSuccess = create_results(
            [
                CreateResultRequest(
                    part_number="Python Client Testing",
                    keywords=[original_keyword],
                    program_name=program_name,
                    status=status,
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.results) == 1

        updated_result = self.__map_result_to_update_result_request(
            create_response.results[0]
        )
        updated_result.keywords = [additional_keyword]
        update_response = client.update_results([updated_result], replace=False)

        assert update_response is not None
        assert len(update_response.results) == 1
        assert (
            update_response.results[0].keywords is not None
            and original_keyword in update_response.results[0].keywords
        )
        assert (
            update_response.results[0].keywords is not None
            and additional_keyword in update_response.results[0].keywords
        )

    def test__update_properties_with_replace__properties_replaced(
        self, client: TestMonitorClient, create_results
    ):
        new_key = "newKey"
        original_properties: Dict[str, str | None] = {"originalKey": "originalValue"}
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        new_properties: Dict[str, str | None] = {new_key: "newValue"}
        create_response: CreateResultsPartialSuccess = create_results(
            [
                CreateResultRequest(
                    part_number="Python Client Testing",
                    properties=original_properties,
                    program_name=program_name,
                    status=status,
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.results) == 1

        updated_result = self.__map_result_to_update_result_request(
            create_response.results[0]
        )
        updated_result.properties = new_properties
        update_response = client.update_results([updated_result], replace=True)

        assert update_response is not None
        assert len(update_response.results) == 1
        assert (
            update_response.results[0].properties is not None
            and len(update_response.results[0].properties) == 1
        )
        assert new_key in update_response.results[0].properties.keys()
        assert update_response.results[0].properties[new_key] == new_properties[new_key]

    def test__update_properties_append__properties_appended(
        self, client: TestMonitorClient, create_results
    ):
        original_key = "originalKey"
        new_key = "newKey"
        original_properties: Dict[str, str | None] = {original_key: "originalValue"}
        program_name = "Python Client Test Program"
        status = Status.PASSED()
        new_properties: Dict[str, str | None] = {new_key: "newValue"}
        create_response: CreateResultsPartialSuccess = create_results(
            [
                CreateResultRequest(
                    part_number="Python Client Testing",
                    properties=original_properties,
                    program_name=program_name,
                    status=status,
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.results) == 1

        updated_result = self.__map_result_to_update_result_request(
            create_response.results[0]
        )
        updated_result.properties = new_properties
        update_response = client.update_results([updated_result], replace=False)

        assert update_response is not None
        assert len(update_response.results) == 1
        updated_result = self.__map_result_to_update_result_request(
            update_response.results[0]
        )
        assert (
            updated_result.properties is not None
            and len(updated_result.properties) == 2
        )
        assert original_key in updated_result.properties.keys()
        assert new_key in updated_result.properties.keys()
        assert (
            updated_result.properties[original_key] == original_properties[original_key]
        )
        assert updated_result.properties[new_key] == new_properties[new_key]

    def __map_result_to_update_result_request(
        self, result: Result
    ) -> UpdateResultRequest:
        result_model_dump = result.model_dump(
            exclude={"status_type_summary", "updated_at"}
        )
        return UpdateResultRequest(**result_model_dump)

    def test__create_single_step__creation_succeed(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        step_id = unique_identifier
        result_id = created_result.results[0].id
        name = "Test Step 1"
        data = StepData(
            text="This is a test step",
            parameters=[Measurement(name="param1", measurement="10")],
        )
        properties = {"property1": "value1", "property2": "value2"}
        keywords = ["keyword1", "keyword2"]
        inputs = [NamedValue(name="input1", value="inputValue1")]
        step = CreateStepRequest(
            step_id=step_id,
            result_id=result_id,
            name=name,
            data=data,
            properties=properties,
            keywords=keywords,
            inputs=inputs,
        )

        response: CreateStepsPartialSuccess = create_steps(steps=[step])

        assert response is not None
        assert len(response.steps) == 1
        created_step = response.steps[0]
        assert created_step.step_id == step_id
        assert created_step.result_id == result_id
        assert created_step.name == name
        assert created_step.data == data
        assert created_step.properties == properties
        assert created_step.keywords == keywords
        assert created_step.inputs == inputs
        assert not created_step.outputs

    def test__create_step_without_step_id__creation_succeed(
        self,
        client: TestMonitorClient,
        create_results,
        create_steps,
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        name = "Test Step 1"
        data = StepData(
            text="This is a test step",
            parameters=[Measurement(name="param1", measurement="10")],
        )
        properties = {"property1": "value1", "property2": "value2"}
        keywords = ["keyword1", "keyword2"]
        inputs = [NamedValue(name="input1", value="inputValue1")]
        step = CreateStepRequest(
            step_id="step1",
            result_id=result_id,
            name=name,
            data=data,
            properties=properties,
            keywords=keywords,
            inputs=inputs,
        )

        response: CreateStepsPartialSuccess = create_steps(steps=[step])

        assert response is not None
        assert len(response.steps) == 1
        created_step = response.steps[0]
        assert created_step.step_id == step.step_id

    def test__create_multiple_steps__multiple_creation_succeed(
        self, client: TestMonitorClient, create_results, create_steps
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        steps = [
            CreateStepRequest(
                step_id=uuid.uuid1().hex,
                result_id=result_id,
                name="Step 1",
            ),
            CreateStepRequest(
                step_id=uuid.uuid1().hex,
                result_id=result_id,
                name="Step 2",
            ),
        ]

        response: CreateStepsPartialSuccess = create_steps(steps)

        assert response is not None
        assert len(response.steps) == 2

    def test__create_multiple_steps_with_children__multiple_creation_succeed(
        self, client: TestMonitorClient, create_results, create_steps
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        parent_step_id = uuid.uuid1().hex
        steps = [
            CreateStepRequest(
                step_id=parent_step_id,
                result_id=result_id,
                name="Step 1",
                children=[
                    CreateStepRequest(
                        step_id=uuid.uuid1().hex,
                        result_id=result_id,
                        name="Step 2",
                    ),
                ],
            ),
        ]

        response: CreateStepsPartialSuccess = create_steps(steps)

        assert response is not None
        assert len(response.steps) == 2
        child_step = response.steps[1]
        assert child_step is not None
        assert child_step.parent_id == parent_step_id

    def test__get_steps__at_least_one_step_exists(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        steps = [
            CreateStepRequest(
                step_id=unique_identifier,
                result_id=result_id,
                name="Step 1",
            )
        ]
        create_steps(steps)

        get_response = client.get_steps()

        assert get_response is not None
        assert len(get_response.steps) >= 1

    def test_with_multiple_steps__get_steps_with_take__only_take_returned(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        steps = [
            CreateStepRequest(
                step_id=unique_identifier,
                result_id=result_id,
                name="Step 1",
            ),
            CreateStepRequest(
                step_id=unique_identifier,
                result_id=result_id,
                name="Step 2",
            ),
        ]
        create_steps(steps)

        get_response = client.get_steps(take=1)

        assert get_response is not None
        assert len(get_response.steps) == 1

    def test__get_steps_with_return_count__steps_and_count_returned(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        steps = [
            CreateStepRequest(
                step_id=unique_identifier,
                result_id=result_id,
                name="Step 1",
            ),
            CreateStepRequest(
                step_id=unique_identifier,
                result_id=result_id,
                name="Step 2",
            ),
        ]
        create_steps(steps)

        get_response: PagedSteps = client.get_steps(return_count=True, take=5)

        assert get_response is not None
        assert get_response.total_count is not None and get_response.total_count >= 2

    def test__get_step_by_id__expected_step_returned(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        steps = [CreateStepRequest(step_id=step_id, result_id=result_id, name="Step 1")]
        create_response: CreateStepsPartialSuccess = create_steps(steps)
        assert create_response is not None

        step: Step = client.get_step(result_id=result_id, step_id=step_id)

        assert step is not None
        assert step.step_id == step_id
        assert step.result_id == result_id

    def test__query_step_by_name_and_result_id__expected_step_returned(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        step_name = "Step 1"
        steps = [
            CreateStepRequest(step_id=step_id, result_id=result_id, name=step_name)
        ]
        create_response: CreateStepsPartialSuccess = create_steps(steps)
        assert create_response is not None

        query_request = QueryStepsRequest(
            filter=f'name="{step_name}" & resultId="{result_id}"',
            return_count=False,
            take=5,
        )
        query_response: PagedSteps = client.query_steps(query_request)

        assert query_response is not None
        assert query_response.steps is not None
        assert len(query_response.steps) == 1
        assert query_response.steps[0].step_id == step_id
        assert query_response.steps[0].name == step_name
        assert query_response.steps[0].result_id == result_id

    def test__query_step_values_for_name__name_matches(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        step_name = "query values test"
        create_response: CreateStepsPartialSuccess = create_steps(
            [CreateStepRequest(step_id=step_id, result_id=result_id, name=step_name)]
        )
        assert create_response is not None
        assert len(create_response.steps) == 1

        query_request = QueryStepValuesRequest(
            filter=f'stepId="{step_id}" & resultId = "{result_id}"',
            field=StepField.NAME,
        )
        query_response: List[str] = client.query_step_values(query_request)

        assert query_response is not None
        assert len(query_response) == 1
        assert query_response[0] == step_name

    def test__update_step_data_and_inputs__data_and_inputs_updated(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        create_response: CreateStepsPartialSuccess = create_steps(
            [
                CreateStepRequest(
                    step_id=step_id,
                    result_id=result_id,
                    name="My Step",
                    data=StepData(
                        text="My output string",
                        parameters=[
                            Measurement(
                                name="Current",
                                status="Passed",
                                measurement="3.725",
                                lowLimit="3.65",
                                highLimit="3.8",
                                units="A",
                                comparisonType="GELE",
                            )
                        ],
                    ),
                    inputs=[
                        NamedValue(name="Temperature", value="35"),
                        NamedValue(name="Voltage", value="5"),
                    ],
                    outputs=[
                        NamedValue(name="Current", value="3.725"),
                    ],
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.steps) == 1
        step = create_response.steps[0]

        updated_data = StepData(
            text="My updated output string",
            parameters=[
                Measurement(
                    name="Voltage",
                    status="Passed",
                    measurement="3.725",
                    lowLimit="3.65",
                    highLimit="3.8",
                    units="V",
                    comparisonType="GELE",
                    specId="spec_01",
                )
            ],
        )
        updated_inputs = [
            NamedValue(name="Temperature", value="40"),
            NamedValue(name="Voltage", value="10"),
        ]
        updated_outputs = [NamedValue(name="Current", value="4.725")]
        update_response: UpdateStepsPartialSuccess = client.update_steps(
            steps=[
                UpdateStepRequest(
                    step_id=step.step_id,
                    result_id=cast(str, step.result_id),
                    data=updated_data,
                    inputs=updated_inputs,
                    outputs=updated_outputs,
                )
            ]
        )

        assert update_response is not None
        assert update_response.steps is not None
        assert len(update_response.steps) == 1
        assert update_response.steps[0].inputs == updated_inputs
        assert update_response.steps[0].outputs == updated_outputs
        assert update_response.steps[0].data is not None
        assert update_response.steps[0].data.text == updated_data.text
        assert update_response.steps[0].data.parameters is not None
        assert updated_data.parameters is not None
        assert len(update_response.steps[0].data.parameters) == 1
        updated_measurement = update_response.steps[0].data.parameters[0]
        assert updated_measurement.name == updated_data.parameters[0].name
        assert updated_measurement.status == updated_data.parameters[0].status
        assert updated_measurement.measurement == updated_data.parameters[0].measurement
        assert updated_measurement.lowLimit == updated_data.parameters[0].lowLimit
        assert updated_measurement.highLimit == updated_data.parameters[0].highLimit
        assert updated_measurement.units == updated_data.parameters[0].units
        assert (
            updated_measurement.comparisonType
            == updated_data.parameters[0].comparisonType
        )
        assert updated_measurement.model_dump().get(
            "specId"
        ) == updated_data.parameters[0].model_dump().get("specId")

    def test__update_step_with_replace_true__replace_keywords_and_properties(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        create_response: CreateStepsPartialSuccess = create_steps(
            [
                CreateStepRequest(
                    step_id=step_id,
                    result_id=result_id,
                    name="Original Name",
                    properties={"originalProperty": "originalValue"},
                    keywords=["originalKeyword"],
                )
            ]
        )
        assert create_response is not None
        assert len(create_response.steps) == 1
        step = create_response.steps[0]

        new_properties = {"property1": "value1", "property2": "value2"}
        new_keywords = ["keyword1", "keyword2"]
        update_response: UpdateStepsPartialSuccess = client.update_steps(
            steps=[
                UpdateStepRequest(
                    step_id=step.step_id,
                    result_id=cast(str, step.result_id),
                    keywords=new_keywords,
                    properties=new_properties,
                )
            ],
            replace_keywords=True,
            replace_properties=True,
        )

        assert update_response is not None
        assert len(update_response.steps) == 1
        assert update_response.steps[0].keywords == new_keywords
        assert update_response.steps[0].properties == new_properties

    def test__delete_existing_step__deleted(
        self, client: TestMonitorClient, create_results, create_steps, unique_identifier
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        step_id = unique_identifier
        steps = [
            CreateStepRequest(
                step_id=step_id,
                result_id=result_id,
                name="Step 1",
            )
        ]
        create_response: CreateStepsPartialSuccess = create_steps(steps)
        assert create_response.steps
        created_step = create_response.steps[0]

        assert created_step.step_id is not None
        assert created_step.result_id is not None
        delete_response = client.delete_step(
            result_id=created_step.result_id, step_id=created_step.step_id
        )

        assert delete_response is None

    def test__delete_non_existent_step__delete_fails(self, client: TestMonitorClient):
        bad_id = "DEADBEEF"

        with pytest.raises(ApiException, match="InvalidResultOrStepId"):
            client.delete_step(
                result_id="ea6f8d2c-8d57-441e-8375-aa897f59835e", step_id=bad_id
            )

    def test__delete_multiple_steps__deletion_succeed(
        self, client: TestMonitorClient, create_results, create_steps
    ):
        results = [
            CreateResultRequest(
                part_number="Python Client Testing",
                program_name="Python Client Test Program",
                status=Status.PASSED(),
            )
        ]
        created_result = create_results(results)
        result_id = created_result.results[0].id
        steps = [
            CreateStepRequest(
                step_id=uuid.uuid1().hex, result_id=result_id, name="Step 1"
            ),
            CreateStepRequest(
                step_id=uuid.uuid1().hex, result_id=result_id, name="Step 2"
            ),
        ]
        create_response: CreateStepsPartialSuccess = create_steps(steps)
        assert create_response.steps is not None
        assert len(create_response.steps) == 2
        created_steps = create_response.steps

        delete_response = client.delete_steps(
            steps=[
                StepIdResultIdPair(
                    step_id=cast(str, step.step_id),
                    result_id=cast(str, step.result_id),
                )
                for step in created_steps
            ]
        )

        assert delete_response is None
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/work_item/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/integration/work_item/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/work_item/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/integration/work_item/test_work_item_client.py sha256=90d19c77fe3b72c7d6a387333df010f8995d9938109db077fcb2ed4b108bfea7 bytes=30826 -->
## FILE: tests/integration/work_item/test_work_item_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/integration/work_item/test_work_item_client.py`
- sha256: `90d19c77fe3b72c7d6a387333df010f8995d9938109db077fcb2ed4b108bfea7`
- bytes: 30826

````python
import copy
from datetime import datetime
from typing import List

import pytest
import responses
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.core._http_configuration import HttpConfiguration
from nisystemlink.clients.work_item import WorkItemClient, WorkItemExecuteApiException
from nisystemlink.clients.work_item.models import (
    CreateWorkItemRequest,
    CreateWorkItemsPartialSuccessResponse,
    CreateWorkItemTemplateRequest,
    CreateWorkItemTemplatesPartialSuccessResponse,
    Dashboard,
    ExecutionDefinition,
    Job,
    JobExecution,
    ManualExecution,
    QueryWorkItemsRequest,
    QueryWorkItemTemplatesRequest,
    ResourceDefinition,
    ResourcesDefinition,
    ResourceSelectionDefinition,
    ScheduleDefinition,
    ScheduleResourcesDefinition,
    ScheduleSystemResourceDefinition,
    ScheduleWorkItemRequest,
    ScheduleWorkItemsRequest,
    SystemResourceDefinition,
    SystemResourceSelectionDefinition,
    TemplateResourceDefinition,
    TemplateResourcesDefinition,
    TemplateTimelineDefinition,
    TimelineDefinition,
    UpdateWorkItemRequest,
    UpdateWorkItemsRequest,
    UpdateWorkItemTemplateRequest,
    UpdateWorkItemTemplatesRequest,
    WorkItem,
    WorkItemField,
    WorkItemTemplate,
    WorkItemTemplateField,
)

BASE_URL = "https://test-api.lifecyclesolutions.ni.com"


@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> WorkItemClient:
    """Fixture to create a WorkItemClient instance"""
    return WorkItemClient(enterprise_config)


@pytest.fixture
def create_work_items(client: WorkItemClient):
    """Fixture to return a factory that creates work items."""
    responses: List[CreateWorkItemsPartialSuccessResponse] = []

    def _create_work_items(
        new_work_items: List[CreateWorkItemRequest],
    ) -> CreateWorkItemsPartialSuccessResponse:
        response = client.create_work_items(work_items=new_work_items)
        responses.append(response)
        return response

    yield _create_work_items

    created_work_items: List[WorkItem] = []
    for response in responses:
        if response.created_work_items:
            created_work_items += response.created_work_items

    client.delete_work_items(
        ids=[
            work_item.id for work_item in created_work_items if work_item.id is not None
        ]
    )


@pytest.fixture
def create_work_item_templates(client: WorkItemClient):
    """Fixture to return a factory that creates work item templates."""
    responses: List[CreateWorkItemTemplatesPartialSuccessResponse] = []

    def _create_work_item_templates(
        new_work_item_templates: List[CreateWorkItemTemplateRequest],
    ) -> CreateWorkItemTemplatesPartialSuccessResponse:
        response = client.create_work_item_templates(
            work_item_templates=new_work_item_templates
        )
        responses.append(response)
        return response

    yield _create_work_item_templates

    created_work_item_templates: List[WorkItemTemplate] = []
    for response in responses:
        if response.created_work_item_templates:
            created_work_item_templates += response.created_work_item_templates

    client.delete_work_item_templates(
        ids=[
            work_item_template.id
            for work_item_template in created_work_item_templates
            if work_item_template.id is not None
        ]
    )


@pytest.mark.integration
@pytest.mark.enterprise
class TestWorkItemClient:

    _workspace = "2300760d-38c4-48a1-9acb-800260812337"
    """Used the main-test default workspace since the client
    for creating a workspace has not been added yet"""

    _dashboard = Dashboard(
        id="DashboardId", variables={"product": "PXIe-4080", "location": "Lab1"}
    )

    _execution_actions: List[ExecutionDefinition] = [
        ManualExecution(action="START", type="MANUAL"),
        JobExecution(
            action="PAUSE",
            type="JOB",
            jobs=[
                Job(
                    functions=["run_test_suite"],
                    arguments=[["test_suite.py"]],
                    metadata={"env": "staging"},
                )
            ],
            systemId="system-001",
        ),
    ]

    _create_work_item_request = [
        CreateWorkItemRequest(
            name="Python integration work item",
            type="testplan",
            state="NEW",
            description="Work item for verifying integration flow",
            assigned_to="test.user@example.com",
            requested_by="test.manager@example.com",
            test_program="TP-Integration-001",
            part_number="px40482",
            workspace=_workspace,
            timeline=TimelineDefinition(
                earliest_start_date_time=datetime(2026, 1, 15, 8, 0, 0),
                due_date_time=datetime(2026, 1, 20, 17, 0, 0),
                estimated_duration_in_seconds=3600,
            ),
            resources=ResourcesDefinition(
                assets=ResourceDefinition(
                    selections=[
                        ResourceSelectionDefinition(
                            id="asset-001",
                            target_location_id="location-003",
                            target_system_id="system-001",
                            target_parent_id="parent-002",
                        )
                    ],
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
                ),
                duts=ResourceDefinition(
                    selections=[
                        ResourceSelectionDefinition(
                            id="dut-001",
                            target_location_id="location-003",
                            target_system_id="system-001",
                            target_parent_id="parent-002",
                        )
                    ],
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
                ),
                fixtures=ResourceDefinition(
                    selections=[
                        ResourceSelectionDefinition(
                            id="fixture-001",
                            target_location_id="location-003",
                            target_system_id="system-001",
                            target_parent_id="parent-002",
                        )
                    ],
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'",
                ),
                systems=SystemResourceDefinition(
                    selections=[
                        SystemResourceSelectionDefinition(
                            id="system-001",
                            target_location_id="location-001",
                        )
                    ],
                    filter="os:linux AND arch:x64",
                ),
            ),
            file_ids_from_template=["file1", "file2"],
            properties={"env": "staging", "priority": "high"},
            dashboard=_dashboard,
            execution_actions=_execution_actions,
        )
    ]
    """create work item request object."""

    _create_work_item_template_request = [
        CreateWorkItemTemplateRequest(
            name="Python integration work item template",
            template_group="sample template group",
            type="testplan",
            product_families=["FamilyA", "FamilyB"],
            part_numbers=["PN-1001", "PN-1002"],
            summary="Template for running integration work items",
            description="This template defines execution steps for integration workflows.",
            test_program="TP-INT-002",
            timeline=TemplateTimelineDefinition(
                estimated_duration_in_seconds=3600,
            ),
            resources=TemplateResourcesDefinition(
                assets=TemplateResourceDefinition(
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'"
                ),
                duts=TemplateResourceDefinition(
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'"
                ),
                fixtures=TemplateResourceDefinition(
                    filter="modelName = 'cRIO-9045' AND serialNumber = '01E82ED0'"
                ),
                systems=TemplateResourceDefinition(filter="os:linux AND arch:x64"),
            ),
            execution_actions=_execution_actions,
            file_ids=["file1", "file2"],
            workspace=_workspace,
            properties={"env": "staging", "priority": "high"},
            dashboard=_dashboard,
        )
    ]
    """create work item template request object."""

    def test__create_work_item__returns_created_work_items(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_template_response = client.create_work_item_templates(
            work_item_templates=self._create_work_item_template_request
        )
        template_id = (
            create_work_item_template_response.created_work_item_templates[0].id
            if create_work_item_template_response.created_work_item_templates
            and create_work_item_template_response.created_work_item_templates[0].id
            else None
        )
        assert template_id is not None
        work_item_request = copy.deepcopy(self._create_work_item_request)
        work_item_request[0].template_id = template_id

        create_work_item_response = create_work_items(work_item_request)

        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]
        assert created_work_item is not None
        assert created_work_item.name == "Python integration work item"
        assert created_work_item.type == "testplan"
        assert created_work_item.part_number == "px40482"
        delete_work_item_template_response = client.delete_work_item_templates(
            ids=[template_id]
        )
        assert delete_work_item_template_response is None

    def test__get_work_item__returns_work_item(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item_id = create_work_item_response.created_work_items[0].id

        get_work_item_response = client.get_work_item(work_item_id=created_work_item_id)

        assert get_work_item_response is not None
        assert get_work_item_response.id == created_work_item_id

    def test__update_work_item__returns_updated_work_item(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]

        update_work_items_request = UpdateWorkItemsRequest(
            work_items=[
                UpdateWorkItemRequest(
                    id=created_work_item.id,
                    name="Updated Work Item",
                )
            ]
        )
        update_work_items_response = client.update_work_items(
            update_work_items=update_work_items_request
        )

        assert update_work_items_response.updated_work_items is not None
        updated_work_item = update_work_items_response.updated_work_items[0]
        assert updated_work_item.id == created_work_item.id
        assert updated_work_item.name == "Updated Work Item"

    def test__schedule_work_item__returns_scheduled_work_item(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]

        schedule_work_items_request = ScheduleWorkItemsRequest(
            work_items=[
                ScheduleWorkItemRequest(
                    id=created_work_item.id,
                    schedule=ScheduleDefinition(
                        planned_start_date_time=datetime.strptime(
                            "2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                        ),
                        planned_end_date_time=datetime.strptime(
                            "2025-05-22T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ"
                        ),
                    ),
                    resources=ScheduleResourcesDefinition(
                        systems=ScheduleSystemResourceDefinition(
                            selections=[
                                SystemResourceSelectionDefinition(id="fake-system")
                            ]
                        ),
                    ),
                )
            ],
            replace=True,
        )
        schedule_work_items_response = client.schedule_work_items(
            schedule_work_items=schedule_work_items_request
        )

        assert schedule_work_items_response.scheduled_work_items is not None
        scheduled_work_item = schedule_work_items_response.scheduled_work_items[0]
        assert scheduled_work_item.id == created_work_item.id
        assert scheduled_work_item.schedule is not None
        assert (
            scheduled_work_item.schedule.planned_start_date_time
            == datetime.strptime("2025-05-20T15:07:42.527Z", "%Y-%m-%dT%H:%M:%S.%fZ")
        )
        assert scheduled_work_item.resources is not None
        assert scheduled_work_item.resources.systems is not None
        assert scheduled_work_item.resources.systems.selections is not None
        assert scheduled_work_item.resources.systems.selections[0].id == "fake-system"

    def test__query_work_items__return_queried_work_item(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]

        query_work_items_request = QueryWorkItemsRequest(
            filter=f'id = "{created_work_item.id}"', return_count=True
        )
        queried_work_items_response = client.query_work_items(
            query_work_items=query_work_items_request
        )

        assert queried_work_items_response is not None
        assert queried_work_items_response.work_items[0].id == created_work_item.id
        assert queried_work_items_response.total_count is not None
        assert queried_work_items_response.total_count == 1

    def test__query_work_items_with_projections__returns_the_work_items_with_projected_properties(
        self, client: WorkItemClient, create_work_items
    ):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]

        query_work_items_request = QueryWorkItemsRequest(
            filter=f'id = "{created_work_item.id}"',
            projection=[WorkItemField.ID, WorkItemField.NAME],
            take=1,
        )
        response = client.query_work_items(query_work_items=query_work_items_request)

        assert response is not None
        work_item = response.work_items[0]
        assert (
            work_item.id is not None
            and work_item.name is not None
            and work_item.template_id is None
            and work_item.state is None
            and work_item.description is None
            and work_item.parent_id is None
            and work_item.assigned_to is None
            and work_item.requested_by is None
            and work_item.workspace is None
            and work_item.created_by is None
            and work_item.updated_at is None
            and work_item.created_at is None
            and work_item.updated_by is None
            and work_item.properties is None
            and work_item.part_number is None
            and work_item.test_program is None
            and work_item.timeline is None
            and work_item.resources is None
            and work_item.file_ids_from_template is None
            and work_item.execution_actions is None
            and work_item.execution_history is None
            and work_item.dashboard is None
        )

    def test__delete_work_item(self, client: WorkItemClient, create_work_items):
        create_work_item_response = create_work_items(self._create_work_item_request)
        assert create_work_item_response.created_work_items is not None
        created_work_item = create_work_item_response.created_work_items[0]

        client.delete_work_items(ids=[created_work_item.id])

        query_deleted_work_item_response = client.query_work_items(
            query_work_items=QueryWorkItemsRequest(
                filter=f'id="{created_work_item.id}"', take=1
            )
        )
        assert len(query_deleted_work_item_response.work_items) == 0

    @pytest.mark.parametrize(
        "execution_type,action,extra_fields,expected_values",
        [
            ("NONE", "NONE", {}, {}),
            ("MANUAL", "START", {}, {}),
            (
                "NOTEBOOK",
                "RUN_NOTEBOOK",
                {"execution_id": "notebook-execution-123"},
                {"execution_id": "notebook-execution-123"},
            ),
            (
                "JOB",
                "RUN_JOBS",
                {"job_ids": ["job-1", "job-2", "job-3"]},
                {"job_ids": ["job-1", "job-2", "job-3"]},
            ),
            ("SCHEDULE", "SCHEDULE", {}, {}),
            ("UNSCHEDULE", "UNSCHEDULE", {}, {}),
        ],
    )
    @responses.activate
    def test__execute_work_item_with_action__returns_execution_result(
        self,
        client: WorkItemClient,
        execution_type: str,
        action: str,
        extra_fields: dict,
        expected_values: dict,
    ):
        work_item_id = "test-work-item-id"

        return_value = {
            "result": {
                "type": execution_type,
                "error": None,
                **extra_fields,
            },
            "error": None,
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/niworkitem/v1/workitems/{work_item_id}/execute",
            json=return_value,
            status=200,
        )

        execute_response = client.execute_work_item(
            work_item_id=work_item_id, action=action
        )

        assert execute_response is not None
        assert execute_response.error is None
        assert execute_response.result is not None
        assert execute_response.result.type == execution_type
        assert execute_response.result.error is None

        # Verify type-specific fields
        for field, expected_value in expected_values.items():
            assert getattr(execute_response.result, field) == expected_value

    @responses.activate
    def test__execute_work_item_with_404_error__raises_WorkItemExecuteApiException(
        self, client: WorkItemClient
    ):
        """When the API returns an execute-specific error body, the client raises
        WorkItemExecuteApiException so callers can access partial results.
        """
        work_item_id = "invalid-work-item-id"

        return_value = {
            "error": {
                "name": "Skyline.WorkItemNotFound",
                "code": -251049,
                "message": f"Work item '{work_item_id}' does not exist.",
                "args": [work_item_id],
                "innerErrors": [],
            },
            "result": None,
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/niworkitem/v1/workitems/{work_item_id}/execute",
            json=return_value,
            status=404,
        )

        with pytest.raises(WorkItemExecuteApiException) as exc_info:
            client.execute_work_item(work_item_id=work_item_id, action="START")

        assert exc_info.value.http_status_code == 404
        assert exc_info.value.error is not None
        assert exc_info.value.error.code == -251049
        assert exc_info.value.result is None

    @responses.activate
    def test__execute_work_item_with_500_error_and_partial_results__raises_WorkItemExecuteApiException(
        self, client: WorkItemClient
    ):
        """When the API returns a 500 with partial results (e.g. cancelled job IDs),
        the client raises WorkItemExecuteApiException so callers can recover them.
        """
        work_item_id = "test-work-item-id"

        return_value = {
            "error": {
                "name": "Skyline.InternalServerError",
                "code": -251000,
                "message": "An internal error occurred while executing the action.",
                "args": [],
                "innerErrors": [],
            },
            "result": {
                "type": "JOB",
                "job_ids": ["job-1", "job-2"],
                "error": None,
            },
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/niworkitem/v1/workitems/{work_item_id}/execute",
            json=return_value,
            status=500,
        )

        with pytest.raises(WorkItemExecuteApiException) as exc_info:
            client.execute_work_item(work_item_id=work_item_id, action="RUN_JOBS")

        assert exc_info.value.http_status_code == 500
        assert exc_info.value.error is not None
        assert exc_info.value.error.code == -251000
        assert exc_info.value.result is not None
        assert exc_info.value.result.type == "JOB"
        assert exc_info.value.result.job_ids == ["job-1", "job-2"]

    @responses.activate
    def test__execute_work_item_with_undocumented_error__raises_ApiException(
        self, client: WorkItemClient
    ):
        """401 is NOT a documented status code for execute — should still raise."""
        work_item_id = "test-work-item-id"

        responses.add(
            responses.POST,
            f"{BASE_URL}/niworkitem/v1/workitems/{work_item_id}/execute",
            json={"message": "Unauthorized"},
            status=401,
        )

        with pytest.raises(ApiException) as exc_info:
            client.execute_work_item(work_item_id=work_item_id, action="START")

        assert exc_info.value.http_status_code == 401

    @responses.activate
    def test__execute_work_item_with_result_level_error__returns_result_with_error(
        self, client: WorkItemClient
    ):
        work_item_id = "test-work-item-id"

        return_value = {
            "result": {
                "type": "NOTEBOOK",
                "execution_id": None,
                "error": {
                    "name": "Skyline.ExecutionFailed",
                    "code": -251050,
                    "message": "Notebook execution failed due to invalid parameters.",
                    "args": [],
                    "innerErrors": [],
                },
            },
            "error": None,
        }

        responses.add(
            responses.POST,
            f"{BASE_URL}/niworkitem/v1/workitems/{work_item_id}/execute",
            json=return_value,
            status=200,
        )

        execute_response = client.execute_work_item(
            work_item_id=work_item_id, action="RUN_NOTEBOOK"
        )

        assert execute_response is not None
        assert execute_response.error is None
        assert execute_response.result is not None
        assert execute_response.result.type == "NOTEBOOK"
        assert execute_response.result.execution_id is None
        assert execute_response.result.error is not None
        assert execute_response.result.error.code == -251050
        assert execute_response.result.error.message is not None
        assert "execution failed" in execute_response.result.error.message

    def test__create_work_item_template__returns_created_work_item_template(
        self, create_work_item_templates
    ):
        create_work_item_template_response = create_work_item_templates(
            self._create_work_item_template_request
        )

        assert (
            create_work_item_template_response.created_work_item_templates is not None
        )
        created_work_item_template = (
            create_work_item_template_response.created_work_item_templates[0]
        )
        assert created_work_item_template is not None
        assert (
            created_work_item_template.name == "Python integration work item template"
        )
        assert created_work_item_template.type == "testplan"

    def test__update_work_item_template__returns_updated_work_item_template(
        self, client: WorkItemClient, create_work_item_templates
    ):
        create_work_item_template_response = create_work_item_templates(
            self._create_work_item_template_request
        )
        assert (
            create_work_item_template_response.created_work_item_templates is not None
        )
        created_work_item_template = (
            create_work_item_template_response.created_work_item_templates[0]
        )

        update_work_item_templates_request = UpdateWorkItemTemplatesRequest(
            work_item_templates=[
                UpdateWorkItemTemplateRequest(
                    id=created_work_item_template.id,
                    name="Updated Work Item Template",
                )
            ]
        )
        update_work_item_templates_response = client.update_work_item_templates(
            update_work_item_templates=update_work_item_templates_request
        )

        assert (
            update_work_item_templates_response.updated_work_item_templates is not None
        )
        updated_work_item_template = (
            update_work_item_templates_response.updated_work_item_templates[0]
        )
        assert updated_work_item_template.id == created_work_item_template.id
        assert updated_work_item_template.name == "Updated Work Item Template"

    def test__query_work_item_template__returns_queried_work_item_template(
        self, client: WorkItemClient, create_work_item_templates
    ):
        create_work_item_template_response = create_work_item_templates(
            self._create_work_item_template_request
        )
        assert (
            create_work_item_template_response.created_work_item_templates is not None
        )
        created_work_item_template = (
            create_work_item_template_response.created_work_item_templates[0]
        )

        query = QueryWorkItemTemplatesRequest(
            filter=f'id="{created_work_item_template.id}"', take=1
        )
        query_work_item_template_response = client.query_work_item_templates(
            query_work_item_templates=query
        )

        assert query_work_item_template_response is not None
        assert len(query_work_item_template_response.work_item_templates) == 1
        assert (
            query_work_item_template_response.work_item_templates[0].id
            == created_work_item_template.id
        )

    def test__query_work_item_templates_with_projections__returns_work_item_templates_with_projected_properties(
        self, client: WorkItemClient, create_work_item_templates
    ):
        create_work_item_template_response = create_work_item_templates(
            self._create_work_item_template_request
        )
        assert (
            create_work_item_template_response.created_work_item_templates is not None
        )
        created_work_item_template = (
            create_work_item_template_response.created_work_item_templates[0]
        )

        query = QueryWorkItemTemplatesRequest(
            filter=f'id="{created_work_item_template.id}"',
            projection=[WorkItemTemplateField.ID, WorkItemTemplateField.NAME],
            take=1,
        )
        response = client.query_work_item_templates(query_work_item_templates=query)

        assert response is not None
        work_item_template = response.work_item_templates[0]
        assert (
            work_item_template.id is not None
            and work_item_template.name is not None
            and work_item_template.template_group is None
            and work_item_template.type is None
            and work_item_template.product_families is None
            and work_item_template.part_numbers is None
            and work_item_template.summary is None
            and work_item_template.description is None
            and work_item_template.test_program is None
            and work_item_template.timeline is None
            and work_item_template.resources is None
            and work_item_template.execution_actions is None
            and work_item_template.file_ids is None
            and work_item_template.workspace is None
            and work_item_template.properties is None
            and work_item_template.dashboard is None
        )

    def test__delete_work_item_template(
        self, client: WorkItemClient, create_work_item_templates
    ):
        create_work_item_template_response = create_work_item_templates(
            self._create_work_item_template_request
        )
        assert (
            create_work_item_template_response.created_work_item_templates is not None
        )
        created_work_item_template = (
            create_work_item_template_response.created_work_item_templates[0]
        )

        client.delete_work_item_templates(ids=[created_work_item_template.id])

        query_deleted_work_item_template_response = client.query_work_item_templates(
            query_work_item_templates=QueryWorkItemTemplatesRequest(
                filter=f'id="{created_work_item_template.id}"', take=1
            )
        )
        assert len(query_deleted_work_item_template_response.work_item_templates) == 0
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/product/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/product/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/product/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/product/test_product_dataframe_utilities.py sha256=e862730790f4fbd53f6a4d4d9f579374e9df3c4bc637f27bb318a40d0a3bcfb2 bytes=4774 -->
## FILE: tests/product/test_product_dataframe_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/product/test_product_dataframe_utilities.py`
- sha256: `e862730790f4fbd53f6a4d4d9f579374e9df3c4bc637f27bb318a40d0a3bcfb2`
- bytes: 4774

````python
from datetime import datetime, timezone
from typing import List

import pandas as pd
import pytest
from nisystemlink.clients.product.models import Product
from nisystemlink.clients.product.utilities import convert_products_to_dataframe
from pandas import DataFrame


@pytest.fixture
def mock_products_data() -> List[Product]:
    """Fixture to return a mock product data."""
    product1 = Product(
        id="5ffb2bf6771fa11e877838dd1",
        part_number="p1",
        name="product_1",
        family="product_family",
        updated_at=datetime(2024, 2, 2, 14, 22, 4, 625155, tzinfo=timezone.utc),
        file_ids=["file11", "file12"],
        keywords=["keyword11", "keyword12"],
        properties={"property11": "property11_value", "property12": "property12_value"},
        workspace="5ffb2bf6771fa11e877838dd0",
    )
    product2 = Product(
        id="5ffb2bf6771fa11e877838dd2",
        part_number="p2",
        name="product_2",
        family="product_family",
        updated_at=datetime(2024, 2, 2, 14, 22, 4, 625455, tzinfo=timezone.utc),
        file_ids=["file21", "file22"],
        keywords=["keyword21", "keyword22"],
        properties={"property21": "property21_value"},
        workspace="5ffb2bf6771fa11e877838dd0",
    )

    return [product1, product2]


@pytest.fixture
def expected_products_dataframe(mock_products_data: List[Product]) -> DataFrame:
    """Fixture to return the expected DataFrame based on the mock product data."""
    restructured_mock_products = []

    for product in mock_products_data:
        properties = (
            {f"properties.{key}": value for key, value in product.properties.items()}
            if product.properties
            else {}
        )
        restructured_product = {
            "id": product.id,
            "part_number": product.part_number,
            "name": product.name,
            "family": product.family,
            "updated_at": product.updated_at,
            "file_ids": product.file_ids,
            "keywords": product.keywords,
            "workspace": product.workspace,
            **properties,
        }
        restructured_mock_products.append(restructured_product)

    return pd.json_normalize(restructured_mock_products)


@pytest.fixture
def empty_products_data() -> List:
    """Fixture to return an empty list of products."""
    return []


@pytest.mark.unit
class TestProductDataframeUtilities:
    def test__convert_products_to_dataframe__with_complete_data(
        self, mock_products_data: List[Product], expected_products_dataframe: DataFrame
    ):
        """Test normal case with valid product data."""
        products_dataframe = convert_products_to_dataframe(mock_products_data)

        assert not products_dataframe.empty
        assert (
            products_dataframe.columns.to_list()
            == expected_products_dataframe.columns.to_list()
        )
        assert products_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert products_dataframe["file_ids"].dtype == "object"
        assert isinstance(products_dataframe["file_ids"].iloc[0], List)
        assert products_dataframe["keywords"].dtype == "object"
        assert isinstance(products_dataframe["keywords"].iloc[0], List)
        pd.testing.assert_frame_equal(
            products_dataframe, expected_products_dataframe, check_dtype=True
        )

    def test__convert_products_to_dataframe__with_empty_data(
        self, empty_products_data: List
    ):
        """Test case when the input products data is empty."""
        products_dataframe = convert_products_to_dataframe(empty_products_data)

        assert products_dataframe.empty

    def test__convert_products_to_dataframe__with_missing_fields(
        self, mock_products_data: List[Product], expected_products_dataframe: DataFrame
    ):
        """Test case when some fields in product data are missing."""
        products = mock_products_data
        for product in products:
            product.keywords = None
            product.properties = None

        products_dataframe = convert_products_to_dataframe(products)
        expected_products_dataframe = expected_products_dataframe.drop(
            columns=expected_products_dataframe.filter(
                like="properties"
            ).columns.to_list()
            + ["keywords"]
        )

        assert not products_dataframe.empty
        assert (
            products_dataframe.columns.to_list()
            == expected_products_dataframe.columns.to_list()
        )
        pd.testing.assert_frame_equal(
            products_dataframe, expected_products_dataframe, check_dtype=True
        )
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/spec/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/spec/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/spec/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/spec/test_spec_dataframe_utilitites.py sha256=9c9aa376dde869d5a07133ea560ff46df45e93394e3ef9ed26c3927521485509 bytes=24257 -->
## FILE: tests/spec/test_spec_dataframe_utilitites.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/spec/test_spec_dataframe_utilitites.py`
- sha256: `9c9aa376dde869d5a07133ea560ff46df45e93394e3ef9ed26c3927521485509`
- bytes: 24257

````python
import uuid
from datetime import datetime, timezone
from typing import Dict, List

import numpy as np
import pandas as pd
import pytest
from nisystemlink.clients.spec.models._condition import (
    Condition,
    ConditionRange,
    ConditionType,
    NumericConditionValue,
    StringConditionValue,
)
from nisystemlink.clients.spec.models._specification import (
    Specification,
    SpecificationLimit,
    SpecificationType,
)
from nisystemlink.clients.spec.utilities import convert_specs_to_dataframe
from nisystemlink.clients.spec.utilities._dataframe_utilities import (
    normalize_conditions_per_column,
    normalize_conditions_per_row,
    summarize_conditions_as_a_string,
)


@pytest.fixture(scope="class")
def specs() -> List[Specification]:
    """Sample specs for this test run."""
    specs = [
        Specification(
            product_id=uuid.uuid1().hex,
            spec_id=uuid.uuid1().hex,
            name="Output voltage",
            category="Parametric Specs",
            type=SpecificationType.PARAMETRIC,
            symbol="Range",
            block="Amplifier",
            limit=SpecificationLimit(min=1.2, max=1.5, typical=1.4),
            unit="mV",
            conditions=[
                Condition(
                    name="Temperature",
                    value=NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                        ],
                        discrete=[1.3, 1.5, 1.7],
                        unit="C",
                    ),
                ),
                Condition(
                    name="Package",
                    value=StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["D", "QFIN"],
                    ),
                ),
            ],
            keywords=["Test specification only", "First"],
            properties={"Comments": "comma separated with unicode"},
            workspace=uuid.uuid1().hex,
            id=uuid.uuid1().hex,
            created_at=datetime(2024, 3, 28, 13, 59, 12, 744000, tzinfo=timezone.utc),
            created_by=uuid.uuid1().hex,
            updated_at=datetime(2024, 3, 28, 13, 59, 12, 744000, tzinfo=timezone.utc),
            updated_by=uuid.uuid1().hex,
            version=28,
        ),
        Specification(
            product_id=uuid.uuid1().hex,
            spec_id=uuid.uuid1().hex,
            name="Input referred voltage noise vs freq",
            category="Parametric Specs",
            type=SpecificationType.PARAMETRIC,
            symbol="Range",
            block="Amplifier",
            limit=SpecificationLimit(min=1.2, max=1.5),
            unit="mV",
            conditions=[
                Condition(
                    name="Temperature",
                    value=NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                            ConditionRange(min=-10, step=10),
                        ],
                        unit="C",
                    ),
                ),
                Condition(
                    name="Supply Voltage",
                    value=NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        discrete=[1.3, 1.5, 1.7],
                        unit="mV",
                    ),
                ),
            ],
        ),
        Specification(
            product_id=uuid.uuid1().hex,
            spec_id=uuid.uuid1().hex,
            name="Input referred voltage noise vs freq",
            category="Parametric Specs",
            type=SpecificationType.PARAMETRIC,
            symbol="Range with required value",
            block="Amplifier",
            limit=SpecificationLimit(min=1.2, max=1.5),
            unit="mV",
            properties={"Comments": "comma separated", "input": "voltage"},
        ),
    ]

    return specs


@pytest.mark.unit
class TestSpecDataframeUtilities:
    def test__convert_specs_to_dataframe_with_summarize_conditions__returns_specs_dataframe_with_string_conditions(
        self, specs
    ):
        conditions_dict = [
            [
                {
                    "condition_Temperature(C)": "[min: -25.0; max: 85.0; step: 20.0], 1.3, 1.5, 1.7",
                    "condition_Package": "D, QFIN",
                    "condition_Supply Voltage(mV)": None,
                }
            ],
            [
                {
                    "condition_Temperature(C)": "[min: -25.0; max: 85.0; step: 20.0], [min: -10.0; step: 10.0]",
                    "condition_Package": None,
                    "condition_Supply Voltage(mV)": "1.3, 1.5, 1.7",
                }
            ],
            [
                {
                    "condition_Temperature(C)": None,
                    "condition_Package": None,
                    "condition_Supply Voltage(mV)": None,
                }
            ],
        ]
        properties_dict = [
            {
                "properties.Comments": "comma separated with unicode",
                "properties.input": None,
            },
            {"properties.Comments": None, "properties.input": None},
            {"properties.Comments": "comma separated", "properties.input": "voltage"},
        ]
        keywords_dict = [
            {"keywords": ["Test specification only", "First"]},
            {"keywords": None},
            {"keywords": None},
        ]
        expected_specs_df = self.__expected_specs_dataframe(
            specs=specs,
            conditions_dict=conditions_dict,
            properties_dict=properties_dict,
            keywords_dict=keywords_dict,
        )

        specs_df = convert_specs_to_dataframe(
            specs=specs, condition_format=summarize_conditions_as_a_string
        )

        assert not specs_df.empty
        assert len(specs_df) == 3
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)
        assert specs_df["created_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["updated_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["keywords"].dtype == "object"
        assert isinstance(specs_df["keywords"].iloc[0], List)

    def test__convert_specs_to_dataframe_with_condition_format__returns_dataframe_with_specified_condition_format(
        self, specs
    ):
        def format_conditions(conditions: List[Condition]) -> List[Dict[str, str]]:
            return [
                {
                    str(condition.name): str(condition.value.discrete)
                    for condition in conditions
                    if condition.value and condition.value.discrete
                }
            ]

        conditions_dict = [
            [
                {
                    "Temperature": "[1.3, 1.5, 1.7]",
                    "Package": "['D', 'QFIN']",
                    "Supply Voltage": None,
                }
            ],
            [
                {
                    "Temperature": None,
                    "Package": None,
                    "Supply Voltage": "[1.3, 1.5, 1.7]",
                }
            ],
            [
                {
                    "Temperature": None,
                    "Package": None,
                    "Supply Voltage(mV)": None,
                }
            ],
        ]
        properties_dict = [
            {
                "properties.Comments": "comma separated with unicode",
                "properties.input": None,
            },
            {"properties.Comments": None, "properties.input": None},
            {"properties.Comments": "comma separated", "properties.input": "voltage"},
        ]
        keywords_dict = [
            {"keywords": ["Test specification only", "First"]},
            {"keywords": None},
            {"keywords": None},
        ]
        expected_specs_df = self.__expected_specs_dataframe(
            specs=specs,
            conditions_dict=conditions_dict,
            properties_dict=properties_dict,
            keywords_dict=keywords_dict,
        )

        specs_df = convert_specs_to_dataframe(
            specs=specs,
            condition_format=format_conditions,
        )

        assert not specs_df.empty
        assert len(specs_df) == 3
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)
        assert specs_df["created_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["updated_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["keywords"].dtype == "object"
        assert isinstance(specs_df["keywords"].iloc[0], List)

    def test__convert_specs_to_dataframe_without_condition_values__returns_specs_dataframe_without_condition(
        self,
    ):
        specs = [
            Specification(
                product_id=uuid.uuid1().hex,
                spec_id=uuid.uuid1().hex,
                name="Input referred voltage noise vs freq",
                conditions=[
                    Condition(
                        name="Temperature",
                    ),
                    Condition(
                        name="Supply Voltage",
                    ),
                ],
            ),
        ]
        expected_specs_df = self.__expected_specs_dataframe(specs=specs)

        specs_df = convert_specs_to_dataframe(specs=specs)

        assert not specs_df.empty
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)

    def test__convert_specs_to_dataframe_with_condition_per_column__returns_dataframe_with_condition_per_column(
        self, specs
    ):
        conditions_dict = [
            [
                {
                    "condition_Temperature": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                        ],
                        discrete=[1.3, 1.5, 1.7],
                        unit="C",
                    ),
                    "condition_Package": StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["D", "QFIN"],
                    ),
                    "condition_Supply Voltage": None,
                }
            ],
            [
                {
                    "condition_Temperature": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                            ConditionRange(min=-10, step=10),
                        ],
                        unit="C",
                    ),
                    "condition_Package": None,
                    "condition_Supply Voltage": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        discrete=[1.3, 1.5, 1.7],
                        unit="mV",
                    ),
                }
            ],
            [
                {
                    "condition_Temperature": None,
                    "condition_Package": None,
                    "condition_Supply Voltage(mV)": None,
                }
            ],
        ]
        properties_dict = [
            {
                "properties.Comments": "comma separated with unicode",
                "properties.input": None,
            },
            {"properties.Comments": None, "properties.input": None},
            {"properties.Comments": "comma separated", "properties.input": "voltage"},
        ]
        keywords_dict = [
            {"keywords": ["Test specification only", "First"]},
            {"keywords": None},
            {"keywords": None},
        ]
        expected_specs_df = self.__expected_specs_dataframe(
            specs=specs,
            conditions_dict=conditions_dict,
            properties_dict=properties_dict,
            keywords_dict=keywords_dict,
        )

        specs_df = convert_specs_to_dataframe(
            specs=specs, condition_format=normalize_conditions_per_column
        )

        assert not specs_df.empty
        assert len(specs_df) == 3
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)
        assert specs_df["created_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["updated_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["keywords"].dtype == "object"
        assert isinstance(specs_df["keywords"].iloc[0], List)

    def test__convert_specs_to_dataframe_with_condition_per_row__returns_dataframe_with_condition_per_row(
        self, specs
    ):
        conditions_dict = [
            [
                {
                    "condition.name": "Temperature",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                        ],
                        discrete=[1.3, 1.5, 1.7],
                        unit="C",
                    ),
                },
                {
                    "condition.name": "Package",
                    "condition.value": StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["D", "QFIN"],
                    ),
                },
            ],
            [
                {
                    "condition.name": "Temperature",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                            ConditionRange(min=-10, step=10),
                        ],
                        unit="C",
                    ),
                },
                {
                    "condition.name": "Supply Voltage",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        discrete=[1.3, 1.5, 1.7],
                        unit="mV",
                    ),
                },
            ],
            [],
        ]
        properties_dict = [
            {
                "properties.Comments": "comma separated with unicode",
                "properties.input": None,
            },
            {"properties.Comments": None, "properties.input": None},
            {"properties.Comments": "comma separated", "properties.input": "voltage"},
        ]
        keywords_dict = [
            {"keywords": ["Test specification only", "First"]},
            {"keywords": None},
            {"keywords": None},
        ]
        expected_specs_df = self.__expected_specs_dataframe(
            specs=specs,
            conditions_dict=conditions_dict,
            properties_dict=properties_dict,
            keywords_dict=keywords_dict,
        )

        specs_df = convert_specs_to_dataframe(
            specs=specs, condition_format=normalize_conditions_per_row
        )

        assert not specs_df.empty
        assert len(specs_df) == 5
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)
        assert specs_df["created_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["updated_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["keywords"].dtype == "object"
        assert isinstance(specs_df["keywords"].iloc[0], List)

    def test__convert_specs_to_dataframe_when_condition_format_none__returns_dataframe_without_condition(
        self, specs
    ):
        properties_dict = [
            {
                "properties.Comments": "comma separated with unicode",
                "properties.input": None,
            },
            {"properties.Comments": None, "properties.input": None},
            {"properties.Comments": "comma separated", "properties.input": "voltage"},
        ]
        keywords_dict = [
            {"keywords": ["Test specification only", "First"]},
            {"keywords": None},
            {"keywords": None},
        ]
        expected_specs_df = self.__expected_specs_dataframe(
            specs=specs, properties_dict=properties_dict, keywords_dict=keywords_dict
        )

        specs_df = convert_specs_to_dataframe(specs=specs, condition_format=None)

        assert not specs_df.empty
        assert len(specs_df) == 3
        pd.testing.assert_frame_equal(specs_df, expected_specs_df, check_dtype=True)
        assert specs_df["created_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["updated_at"].dtype == "datetime64[ns, UTC]"
        assert specs_df["keywords"].dtype == "object"
        assert isinstance(specs_df["keywords"].iloc[0], List)

    def test__summarize_conditions_to_string__returns_only_conditions_with_value_in_string_format(
        self, specs
    ):
        expected_conditions_dict = [
            [
                {
                    "condition_Temperature(C)": "[min: -25.0; max: 85.0; step: 20.0], 1.3, 1.5, 1.7",
                    "condition_Package": "D, QFIN",
                }
            ],
            [
                {
                    "condition_Temperature(C)": "[min: -25.0; max: 85.0; step: 20.0], [min: -10.0; step: 10.0]",
                    "condition_Supply Voltage(mV)": "1.3, 1.5, 1.7",
                }
            ],
        ]

        conditions_dict = [
            summarize_conditions_as_a_string(spec.conditions)
            for spec in specs
            if spec.conditions
        ]

        assert conditions_dict == expected_conditions_dict

    def test__normalize_conditions_per_column__returns_only_conditions_in_conditions_per_column_format(
        self, specs
    ):
        expected_conditions_dict = [
            [
                {
                    "condition_Temperature": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                        ],
                        discrete=[1.3, 1.5, 1.7],
                        unit="C",
                    ),
                    "condition_Package": StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["D", "QFIN"],
                    ),
                }
            ],
            [
                {
                    "condition_Temperature": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                            ConditionRange(min=-10, step=10),
                        ],
                        unit="C",
                    ),
                    "condition_Supply Voltage": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        discrete=[1.3, 1.5, 1.7],
                        unit="mV",
                    ),
                }
            ],
        ]

        conditions_dict = [
            normalize_conditions_per_column(spec.conditions)
            for spec in specs
            if spec.conditions
        ]

        assert conditions_dict == expected_conditions_dict

    def test__normalize_conditions_per_row__returns_only_conditions_in_conditions_per_row_format(
        self, specs
    ):
        expected_conditions_dict = [
            [
                {
                    "condition.name": "Temperature",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                        ],
                        discrete=[1.3, 1.5, 1.7],
                        unit="C",
                    ),
                },
                {
                    "condition.name": "Package",
                    "condition.value": StringConditionValue(
                        condition_type=ConditionType.STRING,
                        discrete=["D", "QFIN"],
                    ),
                },
            ],
            [
                {
                    "condition.name": "Temperature",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        range=[
                            ConditionRange(min=-25, step=20, max=85),
                            ConditionRange(min=-10, step=10),
                        ],
                        unit="C",
                    ),
                },
                {
                    "condition.name": "Supply Voltage",
                    "condition.value": NumericConditionValue(
                        condition_type=ConditionType.NUMERIC,
                        discrete=[1.3, 1.5, 1.7],
                        unit="mV",
                    ),
                },
            ],
        ]

        conditions_dict = [
            normalize_conditions_per_row(spec.conditions)
            for spec in specs
            if spec.conditions
        ]

        assert conditions_dict == expected_conditions_dict

    def __expected_specs_dataframe(
        self, specs, conditions_dict=None, keywords_dict=None, properties_dict=None
    ):
        specs_dict = []
        index = 0
        for spec in specs:
            for condition in (
                conditions_dict[index]
                if (conditions_dict and conditions_dict[index])
                else [{}]
            ):
                specs_dict.append(
                    {
                        **{
                            "product_id": spec.product_id,
                            "spec_id": spec.spec_id,
                            "name": spec.name,
                            "category": spec.category,
                            "symbol": spec.symbol,
                            "block": spec.block,
                            "unit": spec.unit,
                            "workspace": spec.workspace,
                            "id": spec.id,
                            "created_at": spec.created_at,
                            "created_by": spec.created_by,
                            "updated_at": spec.updated_at,
                            "updated_by": spec.updated_by,
                            "version": spec.version,
                            "type": spec.type.name if spec.type else None,
                            "limit.min": spec.limit.min if spec.limit else None,
                            "limit.typical": spec.limit.typical if spec.limit else None,
                            "limit.max": spec.limit.max if spec.limit else None,
                        },
                        **{key: value for key, value in condition.items()},
                        **(keywords_dict[index] if keywords_dict else {}),
                        **(properties_dict[index] if properties_dict else {}),
                    }
                )
            index += 1
        expected_specs_df = pd.DataFrame(specs_dict).replace({None: np.nan})
        expected_specs_df.dropna(axis="columns", how="all", inplace=True)

        return expected_specs_df
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/tag/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/core/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/tag/core/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/core/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/core/test_manualresettimer.py sha256=00fad2d8b36381aa9da112253b9cedde47db79e01ea1bb3b2ad18c337ac0b875 bytes=655 -->
## FILE: tests/tag/core/test_manualresettimer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/core/test_manualresettimer.py`
- sha256: `00fad2d8b36381aa9da112253b9cedde47db79e01ea1bb3b2ad18c337ac0b875`
- bytes: 655

````python
import datetime
import time

from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer


class TestManualResetTimer:
    def test__event_raises__timer_continues(self):
        data = []
        interval = datetime.timedelta(milliseconds=100)
        with ManualResetTimer(interval) as uut:

            def callback():
                try:
                    data.append(None)
                    raise RuntimeError()
                finally:
                    uut.start()

            uut.elapsed += callback

            uut.start()
            time.sleep(0.280)

            assert 2 <= len(data) <= 3
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/core/test_systemtimestamper.py sha256=4def220570daccb8927c4ed1788166ba335bb0df98ff585662206810955f4422 bytes=2571 -->
## FILE: tests/tag/core/test_systemtimestamper.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/core/test_systemtimestamper.py`
- sha256: `4def220570daccb8927c4ed1788166ba335bb0df98ff585662206810955f4422`
- bytes: 2571

````python
import datetime
import os
import threading
import time

import pytest
from nisystemlink.clients.tag._core._system_time_stamper import SystemTimeStamper


class TestSystemTimeStamper:
    def test__constructed__returns_current_time(self):
        uut = SystemTimeStamper()
        _assert_time_within_tolerance(_gmt_now(), uut.timestamp)

    def test__after_delay__returns_current_time(self):
        uut = SystemTimeStamper()
        _assert_time_within_tolerance(_gmt_now(), uut.timestamp)
        time.sleep(0.05)
        _assert_time_within_tolerance(_gmt_now(), uut.timestamp)

    @pytest.mark.skip(reason="This test isn't running fast enough in GitHub Actions")
    def test__during_heavy_use__prevents_collisions(self):
        uut = SystemTimeStamper()
        times = []
        num_times = 500

        def worker():
            while len(times) < num_times:
                times.append(uut.timestamp)

        num_threads = max(os.cpu_count(), 4)
        threads = [threading.Thread(target=worker) for i in range(num_threads)]
        begin = _gmt_now()
        [t.start() for t in threads]
        [t.join() for t in threads]

        times.sort()

        num_after_1us = 0
        for i, t in enumerate(times):
            _assert_time_within_tolerance(begin, t)

            if i > 0:
                difference = (t - times[i - 1]).total_seconds() * 1000000

                assert difference >= 1, (
                    "Expected unique timestamps (not within 1 microsecond), but time "
                    + '{} ("{}") is {}us from the previous one'.format(i, t, difference)
                )

                if difference == 1:
                    num_after_1us += 1

        assert num_after_1us > len(times) * 0.9, (
            "Expected at least 90% of the {} timestamps to be just ".format(len(times))
            + "1 microsecond after the previous timestamp, but only "
            + "{} of the timestamps satisfy that requirement -- ".format(num_after_1us)
            + "the test didn't run fast enough to ensure correct behavior"
        )


def _assert_time_within_tolerance(expected, actual):
    tolerance_seconds = 0.1
    difference = abs((actual - expected).total_seconds())
    assert (
        difference < tolerance_seconds
    ), 'Expected time to be "{}" +/- {} seconds but was "{}" for a {} second difference'.format(
        expected, tolerance_seconds, actual, difference
    )


def _gmt_now():
    return datetime.datetime.now(datetime.timezone.utc)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/tag/http/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/httpclienttestbase.py sha256=39116cbf764d2d506b464b6eb7c40d8dde8f8be5ecfd3752a7572baa2a74fea2 bytes=2698 -->
## FILE: tests/tag/http/httpclienttestbase.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/httpclienttestbase.py`
- sha256: `39116cbf764d2d506b464b6eb7c40d8dde8f8be5ecfd3752a7572baa2a74fea2`
- bytes: 2698

````python
import asyncio
from unittest import mock

from nisystemlink.clients.core._internal._http_client import (
    _AsyncHttpClientAtUri,
    _HttpClientAtUri,
    HttpClient,
)


class HttpClientTestBase:
    def setup_method(self, method):
        is_async = asyncio.iscoroutinefunction(method)
        self._client = MockHttpClient(is_async)

    @classmethod
    def _get_mock_request(cls, side_effects):
        def mock_request(method, uri, params=None, data=None):
            ret = side_effects.pop(0)
            if isinstance(ret, Exception):
                raise ret

            return ret, MockResponse(method, uri)

        return mock_request


class MockResponse:
    class MockRequest:
        def __init__(self, method, uri):
            self.method = method
            self.url = uri

    def __init__(self, method, uri):
        self.request = self.MockRequest(method, uri)


class MockHttpClient(HttpClient):
    def __init__(self, is_async):
        # don't call super().__init__

        self.__is_async = is_async

        self.all_requests = mock.Mock()

    def at_uri(self, uri):
        return MockHttpClientAtUri(self, uri, self.__is_async)

    @property
    def _client(self):
        raise NotImplementedError()

    @property
    def _async_client(self):
        raise NotImplementedError()


class MockHttpClientAtUri(_HttpClientAtUri):
    def __init__(self, client, uri, is_async):
        super().__init__(client, uri)
        self.__client = client
        self.__base_uri = uri
        self.__is_async = is_async

    @property
    def as_async(self):
        # Note: the base class raises a RuntimeError here if running on py35; if we want
        # to test that, we'll need to do it some other way, but it's easier on the tests
        # if we just pretend that it would work on py35, too
        return MockAsyncHttpClientAtUri(self.__client, self.__base_uri, self.__is_async)

    def _request(self, method, *args, **kwargs):
        if method != "DELETE":  # don't error on DELETE -- it's used during cleanup
            assert not self.__is_async, "Non-async method called in async test"
        return self._client.all_requests(method, *args, **kwargs)


class MockAsyncHttpClientAtUri(_AsyncHttpClientAtUri):
    def __init__(self, client, uri, is_async):
        super().__init__(client, uri)
        self.__client = client
        self.__base_uri = uri
        self.__is_async = is_async

    async def _request(self, *args, **kwargs):
        assert self.__is_async, "async method called in non-async test"
        return self._client.all_requests(*args, **kwargs)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/test_httpasynctagqueryresultcollection.py sha256=fb5c83dbfd7e6bed1452e362f0f37f912e848bbebf93581a876c7a4d3a226f91 bytes=9082 -->
## FILE: tests/tag/http/test_httpasynctagqueryresultcollection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/test_httpasynctagqueryresultcollection.py`
- sha256: `fb5c83dbfd7e6bed1452e362f0f37f912e848bbebf93581a876c7a4d3a226f91`
- bytes: 9082

````python
from unittest import mock

import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.tag._http._http_async_tag_query_result_collection import (
    HttpAsyncTagQueryResultCollection,
)

from .httpclienttestbase import HttpClientTestBase


class TestHttpAsyncTagQueryResultCollection(HttpClientTestBase):
    def test__constructed__first_page_includes_data_from_query(self):
        path1 = "tag1"
        path2 = "tag2"
        total_count = 3
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        response = {
            "totalCount": total_count,
            "tags": [
                {
                    "type": "BOOLEAN",
                    "properties": all_properties,
                    "path": path1,
                    "keywords": keywords,
                    "collectAggregates": True,
                },
                {"type": "DOUBLE", "path": path2},
            ],
        }

        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, 2, response, None
        )
        assert total_count == uut.total_count
        assert 2 == len(uut.current_page)
        assert path1 == uut.current_page[0].path
        assert tbase.DataType.BOOLEAN == uut.current_page[0].data_type
        assert uut.current_page[0].collect_aggregates is True
        assert keywords == sorted(uut.current_page[0].keywords)
        assert sorted(public_properties.items()) == sorted(
            uut.current_page[0].properties.items()
        )
        assert dummy_tag.retention_count == uut.current_page[0].retention_count
        assert dummy_tag.retention_days == uut.current_page[0].retention_days
        assert dummy_tag.retention_type == uut.current_page[0].retention_type

        assert path2 == uut.current_page[1].path
        assert tbase.DataType.DOUBLE == uut.current_page[1].data_type
        assert uut.current_page[1].collect_aggregates is False
        assert 0 == len(uut.current_page[1].keywords)
        assert 0 == len(uut.current_page[1].properties)
        assert uut.current_page[1].retention_count is None
        assert uut.current_page[1].retention_days is None
        assert tbase.RetentionType.NONE == uut.current_page[1].retention_type

    def test__constructed_with_invalid_first_page__raises(self):
        mock_request = mock.Mock(method="GET", url="http://localhost")
        mock_response = mock.Mock(request=mock_request)
        with pytest.raises(core.ApiException):
            HttpAsyncTagQueryResultCollection(
                self._client, None, None, None, 0, None, {}, mock_response
            )

    def test__constructed_with_empty_first_page__no_error(self):
        total_count = 2
        response = {"totalCount": total_count, "tags": []}
        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, total_count, None, response, None
        )
        assert total_count == uut.total_count
        assert uut.current_page is None

        response = {"totalCount": 0, "tags": []}
        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, None, response, None
        )
        assert 0 == uut.total_count
        assert uut.current_page is None

    def test__provided_with_new_datatype__datatype_value_is_unknown(self):
        response = {
            "totalCount": 1,
            "tags": [{"type": "SOME_NEW_VALUE", "path": "tag"}],
        }
        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, None, response, None
        )
        assert 1 == len(uut.current_page)
        assert tbase.DataType.UNKNOWN == uut.current_page[0].data_type

    @pytest.mark.asyncio
    async def test__reset_query__requeries_pages_with_all_params(self):
        paths = "tag1,tag2"
        keywords = "keyword1,keyword2"
        properties = "prop1=value1,prop2=value2"
        take = 8
        response = {"totalCount": 2, "tags": [{"type": "STRING", "path": "tag1"}]}
        uut = HttpAsyncTagQueryResultCollection(
            self._client, paths, keywords, properties, 0, take, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([response] * 2)
        )

        await uut.reset_async()
        await uut.move_next_page_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": keywords,
                    "properties": properties,
                    "skip": "0",
                    "take": str(take),
                },
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": keywords,
                    "properties": properties,
                    "skip": "1",
                    "take": str(take),
                },
            ),
        ]

    @pytest.mark.asyncio
    async def test__move_next_page_async__current_page_has_data_for_second_page(self):
        path1 = "tag1"
        path2 = "tag2"
        total_count = 3
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        response = {
            "totalCount": total_count,
            "tags": [{"type": "DOUBLE", "path": path1}],
        }

        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [
                            {
                                "type": "U_INT64",
                                "properties": all_properties,
                                "path": path2,
                                "keywords": keywords,
                                "collectAggregates": True,
                            }
                        ],
                    }
                ]
            )
        )

        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        await uut.move_next_page_async()

        assert total_count == uut.total_count
        assert 1 == len(uut.current_page)
        assert path2 == uut.current_page[0].path
        assert tbase.DataType.UINT64 == uut.current_page[0].data_type
        assert uut.current_page[0].collect_aggregates is True
        assert keywords == sorted(uut.current_page[0].keywords)
        assert sorted(public_properties.items()) == sorted(
            uut.current_page[0].properties.items()
        )
        assert dummy_tag.retention_count == uut.current_page[0].retention_count
        assert dummy_tag.retention_days == uut.current_page[0].retention_days
        assert dummy_tag.retention_type == uut.current_page[0].retention_type

    @pytest.mark.asyncio
    async def test__total_count_changes__move_next_page_async__total_count_updated(
        self,
    ):
        tags = [{"type": "STRING", "path": "tag1"}]
        response = {"totalCount": 2, "tags": tags}
        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 3, "tags": tags}])
        )

        assert 2 == uut.total_count
        await uut.move_next_page_async()
        assert 3 == uut.total_count

    @pytest.mark.asyncio
    async def test__move_next_page_async__page_can_be_empty(self):
        response = {"totalCount": 2, "tags": [{"type": "STRING", "path": "tag1"}]}
        uut = HttpAsyncTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 1, "tags": []}])
        )

        await uut.move_next_page_async()
        assert uut.current_page == []
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/test_httpbufferedtagwriter.py sha256=7dffe6099eaf6e80ca45e4fd47eaaa522abca8541caca8e72d9b7ce054913edb bytes=6608 -->
## FILE: tests/tag/http/test_httpbufferedtagwriter.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/test_httpbufferedtagwriter.py`
- sha256: `7dffe6099eaf6e80ca45e4fd47eaaa522abca8541caca8e72d9b7ce054913edb`
- bytes: 6608

````python
from datetime import datetime, timedelta

import pytest  # type: ignore
from nisystemlink.clients import tag as tbase
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._core._system_time_stamper import SystemTimeStamper
from nisystemlink.clients.tag._http._http_buffered_tag_writer import (
    HttpBufferedTagWriter,
)

from .httpclienttestbase import HttpClientTestBase


class TestHttpBufferedTagWriter(HttpClientTestBase):
    def setup_method(self, method):
        super().setup_method(method)

        self._uut = HttpBufferedTagWriter(
            self._client, SystemTimeStamper(), 10, ManualResetTimer.null_timer
        )

    def test__write_buffered__send_buffered_writes__sends_write(self):
        path = "tag"
        value = 2
        timestamp = datetime.now()

        self._uut.write(path, tbase.DataType.INT32, value, timestamp=timestamp)
        self._uut.send_buffered_writes()

        assert self._client.all_requests.call_count == 1
        call = self._client.all_requests.call_args_list[0]
        assert ("POST", "/nitag/v2/update-current-values") == call[0]
        data = call[1].get("data")
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0].get("path") == path
        updates = data[0].get("updates")
        assert isinstance(updates, list)
        utctime = datetime.utcfromtimestamp(timestamp.timestamp()).isoformat() + "Z"
        assert updates == [
            {"value": {"type": "INT", "value": str(value)}, "timestamp": utctime}
        ]

    @pytest.mark.asyncio
    async def test__write_buffered__send_buffered_writes_async__sends_write(self):
        path = "tag"
        value = 2
        timestamp = datetime.now()

        await self._uut.write_async(
            path, tbase.DataType.INT32, value, timestamp=timestamp
        )
        await self._uut.send_buffered_writes_async()

        assert self._client.all_requests.call_count == 1
        call = self._client.all_requests.call_args_list[0]
        assert ("POST", "/nitag/v2/update-current-values") == call[0]
        data = call[1].get("data")
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0].get("path") == path
        updates = data[0].get("updates")
        assert isinstance(updates, list)
        utctime = datetime.utcfromtimestamp(timestamp.timestamp()).isoformat() + "Z"
        assert updates == [
            {"value": {"type": "INT", "value": str(value)}, "timestamp": utctime}
        ]

    def test__multiple_writes_buffered_for_same_tag__send_buffered_writes__writes_combined_into_one_batch(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        value1 = 2
        value2 = 5
        value3 = 9
        timestamp1 = datetime.now()
        timestamp2 = timestamp1 + timedelta(seconds=1)
        timestamp3 = timestamp1 + timedelta(seconds=2)

        self._uut.write(path1, tbase.DataType.INT32, value1, timestamp=timestamp1)
        self._uut.write(path2, tbase.DataType.UINT64, value2, timestamp=timestamp2)
        self._uut.write(path1, tbase.DataType.INT32, value3, timestamp=timestamp3)
        self._uut.send_buffered_writes()

        assert self._client.all_requests.call_count == 1
        call = self._client.all_requests.call_args_list[0]
        assert ("POST", "/nitag/v2/update-current-values") == call[0]
        data = call[1]["data"]
        assert len(data) == 2
        assert data[0]["path"] == path1
        assert data[1]["path"] == path2
        utctime1 = datetime.utcfromtimestamp(timestamp1.timestamp()).isoformat() + "Z"
        utctime2 = datetime.utcfromtimestamp(timestamp2.timestamp()).isoformat() + "Z"
        utctime3 = datetime.utcfromtimestamp(timestamp3.timestamp()).isoformat() + "Z"
        assert data[0]["updates"] == [
            {"value": {"type": "INT", "value": str(value1)}, "timestamp": utctime1},
            {"value": {"type": "INT", "value": str(value3)}, "timestamp": utctime3},
        ]
        assert data[1]["updates"] == [
            {"value": {"type": "U_INT64", "value": str(value2)}, "timestamp": utctime2}
        ]

    def test__write_buffered__clear_buffered_writes__buffer_is_emptied(self):
        path = "tag"
        value = 2
        timestamp = datetime.now()

        self._uut.write(
            "Not path",
            tbase.DataType.DOUBLE,
            12,
            timestamp=timestamp + timedelta(seconds=1),
        )
        self._uut.clear_buffered_writes()
        self._uut.write(path, tbase.DataType.INT32, value, timestamp=timestamp)
        self._uut.send_buffered_writes()

        assert self._client.all_requests.call_count == 1
        call = self._client.all_requests.call_args_list[0]
        assert ("POST", "/nitag/v2/update-current-values") == call[0]
        data = call[1]["data"]
        assert data[0]["path"] == path
        utctime = datetime.utcfromtimestamp(timestamp.timestamp()).isoformat() + "Z"
        assert data[0]["updates"] == [
            {"value": {"type": "INT", "value": str(value)}, "timestamp": utctime}
        ]

    def test__writes_buffered__send_buffered_writes__buffer_is_emptied(self):
        path = "tag1"
        value1 = 2
        value2 = 5
        timestamp1 = datetime.now()
        timestamp2 = timestamp1 + timedelta(seconds=1)
        self._uut.write(path, tbase.DataType.INT32, value1, timestamp=timestamp1)

        self._uut.send_buffered_writes()
        self._uut.write(path, tbase.DataType.INT32, value2, timestamp=timestamp2)
        self._uut.send_buffered_writes()

        assert self._client.all_requests.call_count == 2
        call1, call2 = self._client.all_requests.call_args_list
        assert ("POST", "/nitag/v2/update-current-values") == call1[0]
        assert ("POST", "/nitag/v2/update-current-values") == call2[0]
        data1 = call1[1]["data"]
        data2 = call2[1]["data"]
        assert data1[0]["path"] == path
        assert data2[0]["path"] == path
        utctime1 = datetime.utcfromtimestamp(timestamp1.timestamp()).isoformat() + "Z"
        utctime2 = datetime.utcfromtimestamp(timestamp2.timestamp()).isoformat() + "Z"
        assert data1[0]["updates"] == [
            {"value": {"type": "INT", "value": str(value1)}, "timestamp": utctime1}
        ]
        assert data2[0]["updates"] == [
            {"value": {"type": "INT", "value": str(value2)}, "timestamp": utctime2}
        ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/test_httptagqueryresultcollection.py sha256=5d20597bcb9e80c8039d67c9f9d1dcd8aaf2625e14f466d6506b4fce90fb8f9a bytes=8645 -->
## FILE: tests/tag/http/test_httptagqueryresultcollection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/test_httptagqueryresultcollection.py`
- sha256: `5d20597bcb9e80c8039d67c9f9d1dcd8aaf2625e14f466d6506b4fce90fb8f9a`
- bytes: 8645

````python
from unittest import mock

import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.tag._http._http_tag_query_result_collection import (
    HttpTagQueryResultCollection,
)

from .httpclienttestbase import HttpClientTestBase


class TestHttpTagQueryResultCollection(HttpClientTestBase):
    def test__constructed__first_page_includes_data_from_query(self):
        path1 = "tag1"
        path2 = "tag2"
        total_count = 3
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        response = {
            "totalCount": total_count,
            "tags": [
                {
                    "type": "BOOLEAN",
                    "properties": all_properties,
                    "path": path1,
                    "keywords": keywords,
                    "collectAggregates": True,
                },
                {"type": "DOUBLE", "path": path2},
            ],
        }

        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, 2, response, None
        )
        page = next(iter(uut))
        assert total_count == uut.total_count
        assert 2 == len(page)
        assert path1 == page[0].path
        assert tbase.DataType.BOOLEAN == page[0].data_type
        assert page[0].collect_aggregates is True
        assert keywords == sorted(page[0].keywords)
        assert sorted(public_properties.items()) == sorted(page[0].properties.items())
        assert dummy_tag.retention_count == page[0].retention_count
        assert dummy_tag.retention_days == page[0].retention_days
        assert dummy_tag.retention_type == page[0].retention_type

        assert path2 == page[1].path
        assert tbase.DataType.DOUBLE == page[1].data_type
        assert page[1].collect_aggregates is False
        assert 0 == len(page[1].keywords)
        assert 0 == len(page[1].properties)
        assert page[1].retention_count is None
        assert page[1].retention_days is None
        assert tbase.RetentionType.NONE == page[1].retention_type

    def test__constructed_with_invalid_first_page__raises(self):
        mock_request = mock.Mock(method="GET", url="http://localhost")
        mock_response = mock.Mock(request=mock_request)
        with pytest.raises(core.ApiException):
            HttpTagQueryResultCollection(
                self._client, None, None, None, 0, None, {}, mock_response
            )

    def test__constructed_with_empty_first_page__no_error(self):
        total_count = 2
        response = {"totalCount": total_count, "tags": []}
        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, total_count, None, response, None
        )
        assert total_count == uut.total_count
        assert 0 == len(list(uut))

        response = {"totalCount": 0, "tags": []}
        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, None, response, None
        )
        assert 0 == uut.total_count
        assert 0 == len(list(uut))

    def test__provided_with_new_datatype__datatype_value_is_unknown(self):
        response = {
            "totalCount": 1,
            "tags": [{"type": "SOME_NEW_VALUE", "path": "tag"}],
        }
        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, None, response, None
        )
        page = next(iter(uut))
        assert 1 == len(page)
        assert tbase.DataType.UNKNOWN == page[0].data_type

    def test__reset_query__requeries_pages_with_all_params(self):
        paths = "tag1,tag2"
        keywords = "keyword1,keyword2"
        properties = "prop1=value1,prop2=value2"
        take = 8
        response = {"totalCount": 2, "tags": [{"type": "STRING", "path": "tag1"}]}
        uut = HttpTagQueryResultCollection(
            self._client, paths, keywords, properties, 0, take, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([response] * 2)
        )

        next(iter(uut))  # Drain the cached page
        list(uut)  # Iterate over all pages (from the beginning)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": keywords,
                    "properties": properties,
                    "skip": "0",
                    "take": str(take),
                },
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": keywords,
                    "properties": properties,
                    "skip": "1",
                    "take": str(take),
                },
            ),
        ]

    def test__move_next_page_async__current_page_has_data_for_second_page(self):
        path1 = "tag1"
        path2 = "tag2"
        total_count = 3
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        response = {
            "totalCount": total_count,
            "tags": [{"type": "DOUBLE", "path": path1}],
        }

        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [
                            {
                                "type": "U_INT64",
                                "properties": all_properties,
                                "path": path2,
                                "keywords": keywords,
                                "collectAggregates": True,
                            }
                        ],
                    }
                ]
            )
        )

        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        itr = iter(uut)
        next(itr)
        page = next(itr)  # Retrieve the second page
        assert total_count == uut.total_count
        assert 1 == len(page)
        assert path2 == page[0].path
        assert tbase.DataType.UINT64 == page[0].data_type
        assert page[0].collect_aggregates is True
        assert keywords == sorted(page[0].keywords)
        assert sorted(public_properties.items()) == sorted(page[0].properties.items())
        assert dummy_tag.retention_count == page[0].retention_count
        assert dummy_tag.retention_days == page[0].retention_days
        assert dummy_tag.retention_type == page[0].retention_type

    def test__total_count_changes__move_next_page_async__total_count_updated(self):
        tags = [{"type": "STRING", "path": "tag1"}]
        response = {"totalCount": 2, "tags": tags}
        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 3, "tags": tags}])
        )

        assert 2 == uut.total_count
        itr = iter(uut)
        next(itr)
        next(itr)  # Retrieve the second page
        assert 3 == uut.total_count

    def test__move_next_page_async__page_can_be_empty(self):
        response = {"totalCount": 2, "tags": [{"type": "STRING", "path": "tag1"}]}
        uut = HttpTagQueryResultCollection(
            self._client, None, None, None, 0, 1, response, None
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 1, "tags": []}])
        )

        assert 1 == len(list(uut))
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/test_httptagselection.py sha256=973e660a69fb0090582760ec76e4ea7b09e839f2fd59b8e2935141f4c8a1b2d3 bytes=45697 -->
## FILE: tests/tag/http/test_httptagselection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/test_httptagselection.py`
- sha256: `973e660a69fb0090582760ec76e4ea7b09e839f2fd59b8e2935141f4c8a1b2d3`
- bytes: 45697

````python
import uuid
from datetime import datetime, timezone
from unittest import mock

import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.tag._http._http_tag_selection import HttpTagSelection

from .httpclienttestbase import HttpClientTestBase, MockResponse
from ...anyorderlist import AnyOrderList


class TestHttpTagSelection(HttpClientTestBase):
    @classmethod
    def _get_mock_request(cls, token, query_result, values_result=None):
        # Override the parent class's implementation with a more specific one

        def mock_request(method, uri, params=None, data=None):
            if method == "DELETE":
                ret = None
            elif uri.startswith("/nitag/v2/selections"):
                if uri in ("/nitag/v2/selections", "/nitag/v2/selections/{id}"):
                    data = dict(data)
                    data.update({"id": token})
                    ret = data
                elif uri.endswith("/tags"):
                    if isinstance(query_result, Exception):
                        raise query_result
                    else:
                        ret = query_result
                elif values_result is not None and uri.endswith("values"):
                    ret = values_result
                elif uri.endswith("/reset-aggregates"):
                    ret = None
                else:
                    assert False, uri
            elif uri.startswith("/nitag/v2/subscriptions"):
                if uri == "/nitag/v2/subscriptions":
                    ret = {"subscriptionId": token}
                elif uri.endswith("/values/current"):
                    if isinstance(query_result, Exception):
                        raise query_result
                    else:
                        ret = query_result
                else:
                    assert False, uri
            else:
                assert False, uri

            return ret, MockResponse(method, uri)

        return mock_request

    def test__metadata_supplied__constructed__no_server_queries(self):
        tags = [tbase.TagData("tag", tbase.DataType.BOOLEAN)]
        uut = HttpTagSelection(self._client, tags)
        assert tags == list(uut.metadata.values())
        assert self._client.all_requests.call_count == 0

    def test__open__creates_selection_and_loads_all_data_from_server(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        tags = [
            {
                "path": path1,
                "type": "BOOLEAN",
                "keywords": keywords,
                "properties": all_properties,
                "collectAggregates": True,
            },
            {"path": path2, "type": "DOUBLE"},
        ]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]
        assert 2 == len(uut.metadata)
        assert tbase.DataType.BOOLEAN == uut.metadata[path1].data_type
        assert uut.metadata[path1].collect_aggregates is True
        assert keywords == sorted(uut.metadata[path1].keywords)
        assert sorted(public_properties.items()) == sorted(
            uut.metadata[path1].properties.items()
        )
        assert dummy_tag.retention_count == uut.metadata[path1].retention_count
        assert dummy_tag.retention_days == uut.metadata[path1].retention_days
        assert dummy_tag.retention_type == uut.metadata[path1].retention_type

        assert tbase.DataType.DOUBLE == uut.metadata[path2].data_type
        assert uut.metadata[path2].collect_aggregates is False
        assert 0 == len(uut.metadata[path2].keywords)
        assert 0 == len(uut.metadata[path2].properties)
        assert uut.metadata[path2].retention_count is None
        assert uut.metadata[path2].retention_days is None
        assert tbase.RetentionType.NONE == uut.metadata[path2].retention_type

    @pytest.mark.asyncio
    async def test__open_async__creates_selection_and_loads_all_data_from_api(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        public_properties = {
            "prop1": "value1",
            "prop2": "value2",
        }
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        tags = [
            {
                "path": path1,
                "type": "BOOLEAN",
                "keywords": keywords,
                "properties": all_properties,
                "collectAggregates": True,
            },
            {"path": path2, "type": "DOUBLE"},
        ]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]
        assert 2 == len(uut.metadata)
        assert tbase.DataType.BOOLEAN == uut.metadata[path1].data_type
        assert uut.metadata[path1].collect_aggregates is True
        assert keywords == sorted(uut.metadata[path1].keywords)
        assert sorted(public_properties.items()) == sorted(
            uut.metadata[path1].properties.items()
        )
        assert dummy_tag.retention_count == uut.metadata[path1].retention_count
        assert dummy_tag.retention_days == uut.metadata[path1].retention_days
        assert dummy_tag.retention_type == uut.metadata[path1].retention_type

        assert tbase.DataType.DOUBLE == uut.metadata[path2].data_type
        assert uut.metadata[path2].collect_aggregates is False
        assert 0 == len(uut.metadata[path2].keywords)
        assert 0 == len(uut.metadata[path2].properties)
        assert uut.metadata[path2].retention_count is None
        assert uut.metadata[path2].retention_days is None
        assert tbase.RetentionType.NONE == uut.metadata[path2].retention_type

    def test__error_on_tag_query__open__selection_deleted(self):
        paths = ["path"]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, core.ApiException("Oops"))
        )

        with pytest.raises(core.ApiException):
            HttpTagSelection.open(self._client, paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__error_on_tag_query__open_async__selection_deleted(self):
        paths = ["path"]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, core.ApiException("Oops"))
        )

        with pytest.raises(core.ApiException):
            await HttpTagSelection.open_async(self._client, paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__close__selection_deleted(self):
        paths = ["path"]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, [])
        )

        uut = await HttpTagSelection.open_async(self._client, paths)
        uut.close()
        uut.close()
        await uut.close_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__close_async__selection_deleted(self):
        paths = ["path"]
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, [])
        )

        uut = await HttpTagSelection.open_async(self._client, paths)
        await uut.close_async()
        await uut.close_async()
        uut.close()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__no_selection_created_by_constructor__close__no_server_calls(self):
        uut = HttpTagSelection(self._client, [tbase.TagData("tag")])
        uut.close()
        uut.close()
        await uut.close_async()
        assert self._client.all_requests.call_count == 0

    @pytest.mark.asyncio
    async def test__no_selection_created_by_constructor__close_async__no_server_calls(
        self,
    ):
        uut = HttpTagSelection(self._client, [tbase.TagData("tag")])
        await uut.close_async()
        await uut.close_async()
        uut.close()
        assert self._client.all_requests.call_count == 0

    def test__create_subscription__subscription_created_with_paths(self):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {"subscriptionUpdates": []})
        )
        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )

        with uut.create_subscription():
            pass

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": AnyOrderList([path1, path2]), "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token},
            ),
            mock.call("DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__create_subscription_async__subscription_created_with_paths(self):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {"subscriptionUpdates": []})
        )
        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )

        async with await uut.create_subscription_async():
            pass

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": AnyOrderList([path1, path2]), "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token},
            ),
            mock.call("DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}),
        ]

    def test__no_selection_created_by_constructor__api_function_called__selection_created(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, AssertionError())
        )

        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )
        uut.delete_tags_from_server()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__selection_created_by_constructor__api_function_called__selection_reused(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, [path1, path2])
        uut.delete_tags_from_server()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__server_selection_created__open_tags__existing_selection_edited_on_next_call(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path1}]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, [path1])
        uut.open_tags([path2])
        uut.delete_tags_from_server()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "PUT",
                "/nitag/v2/selections/{id}",
                params={"id": token},
                data={"searchPaths": AnyOrderList([path1, path2]), "id": token},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__server_selection_expired__api_function_called__selection_recreated_and_operation_retried(
        self,
    ):
        path = "tag1"
        token1 = uuid.uuid4()
        token2 = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path}]
        tokens = [token1, token2]
        tag_delete_results = [core.ApiException("404", http_status_code=404), None]

        def mock_request(method, uri, params=None, data=None):
            if uri == "/nitag/v2/selections":
                data = dict(data)
                data.update({"id": tokens.pop(0)})
                return data, MockResponse(method, uri)
            elif uri.endswith("/tags"):
                if method == "DELETE":
                    result = tag_delete_results.pop(0)
                    if isinstance(result, Exception):
                        raise result
                    else:
                        return result, MockResponse(method, uri)
                else:
                    return tags, MockResponse(method, uri)
            elif uri.startswith("/nitag/v2/selections/"):
                assert method == "DELETE"
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        uut = HttpTagSelection.open(self._client, [path])
        uut.delete_tags_from_server()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call(
                "DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token1}
            ),
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call(
                "DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token2}
            ),
        ]

    @pytest.mark.asyncio
    async def test__no_selection_created_by_constructor__async_api_function_called__selection_created(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, AssertionError())
        )

        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )
        await uut.delete_tags_from_server_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__selection_created_by_constructor__async_api_function_called__selection_reused(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1, path2])
        await uut.delete_tags_from_server_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_selection_created__open_tags__existing_selection_edited_on_next_async_call(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path1}]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1])
        uut.open_tags([path2])
        await uut.delete_tags_from_server_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "PUT",
                "/nitag/v2/selections/{id}",
                params={"id": token},
                data={"searchPaths": AnyOrderList([path1, path2]), "id": token},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_selection_expired__async_api_function_called__selection_recreated_and_operation_retried(
        self,
    ):
        path = "tag1"
        token1 = uuid.uuid4()
        token2 = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path}]
        tokens = [token1, token2]
        tag_delete_results = [core.ApiException("404", http_status_code=404), None]

        def mock_request(method, uri, params=None, data=None):
            if uri == "/nitag/v2/selections":
                data = dict(data)
                data.update({"id": tokens.pop(0)})
                return data, MockResponse(method, uri)
            elif uri.endswith("/tags"):
                if method == "DELETE":
                    result = tag_delete_results.pop(0)
                    if isinstance(result, Exception):
                        raise result
                    else:
                        return result, MockResponse(method, uri)
                else:
                    return tags, MockResponse(method, uri)
            elif uri.startswith("/nitag/v2/selections/"):
                assert method == "DELETE"
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        uut = await HttpTagSelection.open_async(self._client, [path])
        await uut.delete_tags_from_server_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call(
                "DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token1}
            ),
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call(
                "DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token2}
            ),
        ]

    def test__no_selection_created_by_constructor__refresh_metadata__tags_queried(self):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, [])
        )

        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )
        uut.refresh_metadata()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__selection_created_by_constructor__refresh_metadata__tags_requeried(self):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, [path1, path2])
        uut.refresh_metadata()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__server_selection_created__open_tags__existing_selection_edited_on_refresh_metadata(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path1}]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, [path1])
        uut.open_tags([path2])
        uut.refresh_metadata()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "PUT",
                "/nitag/v2/selections/{id}",
                params={"id": token},
                data={"searchPaths": AnyOrderList([path1, path2]), "id": token},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    def test__server_selection_expired__refresh_metadata__selection_recreated_and_operation_retried(
        self,
    ):
        path = "tag1"
        token1 = uuid.uuid4()
        token2 = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path}]
        tokens = [token1, token2]
        tag_results = [tags, core.ApiException("404", http_status_code=404), []]

        def mock_request(method, uri, params=None, data=None):
            if uri == "/nitag/v2/selections":
                data = dict(data)
                data.update({"id": tokens.pop(0)})
                return data, MockResponse(method, uri)
            elif uri.endswith("/tags"):
                result = tag_results.pop(0)
                if isinstance(result, Exception):
                    raise result
                else:
                    return result, MockResponse(method, uri)
            elif uri.startswith("/nitag/v2/selections/"):
                assert method == "DELETE"
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        uut = HttpTagSelection.open(self._client, [path])
        uut.refresh_metadata()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token2}),
        ]

    @pytest.mark.asyncio
    async def test__no_selection_created_by_constructor__refresh_metadata_async__tags_queried(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, [])
        )

        uut = HttpTagSelection(
            self._client, [tbase.TagData(path1), tbase.TagData(path2)]
        )
        await uut.refresh_metadata_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__selection_created_by_constructor__refresh_metadata_async__tags_requeried(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1, path2])
        await uut.refresh_metadata_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1, path2])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_selection_created__open_tags__existing_selection_edited_on_refresh_metadata_async(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        token = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path1}]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1])
        uut.open_tags([path2])
        await uut.refresh_metadata_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path1])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "PUT",
                "/nitag/v2/selections/{id}",
                params={"id": token},
                data={"searchPaths": AnyOrderList([path1, path2]), "id": token},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_selection_expired__refresh_metadata_async__selection_recreated_and_operation_retried(
        self,
    ):
        path = "tag1"
        token1 = uuid.uuid4()
        token2 = uuid.uuid4()
        tags = [{"type": "DATE_TIME", "path": path}]
        tokens = [token1, token2]
        tag_results = [tags, core.ApiException("404", http_status_code=404), []]

        def mock_request(method, uri, params=None, data=None):
            if uri == "/nitag/v2/selections":
                data = dict(data)
                data.update({"id": tokens.pop(0)})
                return data, MockResponse(method, uri)
            elif uri.endswith("/tags"):
                result = tag_results.pop(0)
                if isinstance(result, Exception):
                    raise result
                else:
                    return result, MockResponse(method, uri)
            elif uri.startswith("/nitag/v2/selections/"):
                assert method == "DELETE"
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        uut = await HttpTagSelection.open_async(self._client, [path])
        await uut.refresh_metadata_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token1}),
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList([path])},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token2}),
        ]

    def test__refresh_values__values_loaded(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        timestamp = datetime.now(timezone.utc)
        timestamp_str = timestamp.isoformat().rsplit("+", 1)[0] + "Z"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        values = [
            {"path": path1},
            {
                "path": path2,
                "current": {
                    "value": {"value": "2", "type": "INT"},
                    "timestamp": timestamp_str,
                },
                "aggregates": {"min": "1", "max": "5", "count": 4, "avg": 2.5},
            },
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags, values)
        )

        uut = HttpTagSelection.open(self._client, paths)
        uut.refresh_values()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("GET", "/nitag/v2/selections/{id}/values", params={"id": token}),
        ]

        value = uut.read(path2, include_timestamp=True, include_aggregates=True)
        assert uut.read(path1, include_timestamp=True, include_aggregates=True) is None

        assert self._client.all_requests.call_count == 3
        assert value is not None
        assert 4 == value.count
        assert tbase.DataType.INT32 == value.data_type
        assert 5 == value.max
        assert 2.5 == value.mean
        assert 1 == value.min
        assert path2 == value.path
        assert timestamp == value.timestamp
        assert 2 == value.value

    @pytest.mark.asyncio
    async def test__refresh_values_async__values_loaded(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        timestamp = datetime.now(timezone.utc)
        timestamp_str = timestamp.isoformat().rsplit("+", 1)[0] + "Z"
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        values = [
            {"path": path1},
            {
                "path": path2,
                "current": {
                    "value": {"value": "2", "type": "INT"},
                    "timestamp": timestamp_str,
                },
                "aggregates": {"min": "1", "max": "5", "count": 4, "avg": 2.5},
            },
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags, values)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1, path2])
        await uut.refresh_values_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("GET", "/nitag/v2/selections/{id}/values", params={"id": token}),
        ]

        value = uut.read(path2, include_timestamp=True, include_aggregates=True)
        assert uut.read(path1, include_timestamp=True, include_aggregates=True) is None

        assert self._client.all_requests.call_count == 3
        assert value is not None
        assert 4 == value.count
        assert tbase.DataType.INT32 == value.data_type
        assert 5 == value.max
        assert 2.5 == value.mean
        assert 1 == value.min
        assert path2 == value.path
        assert timestamp == value.timestamp
        assert 2 == value.value

    def test__refresh__tags_and_values_reloaded(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        timestamp = datetime.now(timezone.utc)
        timestamp_str = timestamp.isoformat().rsplit("+", 1)[0] + "Z"
        token = uuid.uuid4()
        tag1 = {"type": "DATE_TIME", "path": path1}
        tag2 = {"type": "INT", "path": path2}
        tags = [tag1, tag2]
        values = {
            "totalCount": 2,
            "tagsWithValues": [
                # Update the type, to verify that tag data is reloaded
                {"tag": {"path": path1, "type": "STRING"}},
                {
                    "tag": tag2,
                    "current": {
                        "value": {"value": "2", "type": "INT"},
                        "timestamp": timestamp_str,
                    },
                    "aggregates": {"min": "1", "max": "5", "count": 4, "avg": 2.5},
                },
            ],
        }
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags, values)
        )

        uut = HttpTagSelection.open(self._client, [path1, path2])
        uut.refresh()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "GET",
                "/nitag/v2/selections/{id}/tags-with-values",
                params={"id": token},
            ),
        ]

        assert tbase.DataType.STRING == uut.metadata[path1].data_type
        assert tbase.DataType.INT32 == uut.metadata[path2].data_type

        value = uut.read(path2, include_timestamp=True, include_aggregates=True)
        assert uut.read(path1, include_timestamp=True, include_aggregates=True) is None

        assert self._client.all_requests.call_count == 3
        assert value is not None
        assert 4 == value.count
        assert tbase.DataType.INT32 == value.data_type
        assert 5 == value.max
        assert 2.5 == value.mean
        assert 1 == value.min
        assert path2 == value.path
        assert timestamp == value.timestamp
        assert 2 == value.value

    @pytest.mark.asyncio
    async def test__refresh_async__tags_and_values_reloaded(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        timestamp = datetime.now(timezone.utc)
        timestamp_str = timestamp.isoformat().rsplit("+", 1)[0] + "Z"
        token = uuid.uuid4()
        tag1 = {"type": "DATE_TIME", "path": path1}
        tag2 = {"type": "INT", "path": path2}
        tags = [tag1, tag2]
        values = {
            "totalCount": 2,
            "tagsWithValues": [
                # Update the type, to verify that tag data is reloaded
                {"tag": {"path": path1, "type": "STRING"}},
                {
                    "tag": tag2,
                    "current": {
                        "value": {"value": "2", "type": "INT"},
                        "timestamp": timestamp_str,
                    },
                    "aggregates": {"min": "1", "max": "5", "count": 4, "avg": 2.5},
                },
            ],
        }
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags, values)
        )

        uut = await HttpTagSelection.open_async(self._client, [path1, path2])
        await uut.refresh_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "GET",
                "/nitag/v2/selections/{id}/tags-with-values",
                params={"id": token},
            ),
        ]

        assert tbase.DataType.STRING == uut.metadata[path1].data_type
        assert tbase.DataType.INT32 == uut.metadata[path2].data_type

        value = uut.read(path2, include_timestamp=True, include_aggregates=True)
        assert uut.read(path1, include_timestamp=True, include_aggregates=True) is None

        assert self._client.all_requests.call_count == 3
        assert value is not None
        assert 4 == value.count
        assert tbase.DataType.INT32 == value.data_type
        assert 5 == value.max
        assert 2.5 == value.mean
        assert 1 == value.min
        assert path2 == value.path
        assert timestamp == value.timestamp
        assert 2 == value.value

    def test__reset_aggregates__aggregates_reset_on_server(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = HttpTagSelection.open(self._client, paths)
        uut.reset_aggregates()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "POST",
                "/nitag/v2/selections/{id}/reset-aggregates",
                params={"id": token},
                data=None,
            ),
        ]

    @pytest.mark.asyncio
    async def test__reset_aggregates_async__aggregates_reset_on_server(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        token = uuid.uuid4()
        tags = [
            {"type": "DATE_TIME", "path": path1},
            {"type": "INT", "path": path2},
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, tags)
        )

        uut = await HttpTagSelection.open_async(self._client, paths)
        await uut.reset_aggregates_async()

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call(
                "POST",
                "/nitag/v2/selections/{id}/reset-aggregates",
                params={"id": token},
                data=None,
            ),
        ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/http/test_httptagsubscription.py sha256=dbba470c47d062b8a9639c53b659bc79a82fb62d57b303098161674e991b17b1 bytes=26225 -->
## FILE: tests/tag/http/test_httptagsubscription.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/http/test_httptagsubscription.py`
- sha256: `dbba470c47d062b8a9639c53b659bc79a82fb62d57b303098161674e991b17b1`
- bytes: 26225

````python
from datetime import datetime, timezone
from typing import Any, Dict, List
from unittest import mock

import events
import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase
from nisystemlink.clients.core._internal._timestamp_utilities import TimestampUtilities
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._http._http_tag_subscription import HttpTagSubscription

from .httpclienttestbase import HttpClientTestBase, MockResponse


class TestHttpTagSubscription(HttpClientTestBase):
    @classmethod
    def _get_mock_request(cls, token, query_result, heartbeat_result=None):
        # Override the parent class's implementation with a more specific one

        def mock_request(method, uri, params=None, data=None):
            if (method, uri) == ("POST", "/nitag/v2/subscriptions"):
                return {"subscriptionId": token}, MockResponse(method, uri)
            elif method == "GET":
                return query_result, MockResponse(method, uri)
            elif method == "DELETE":
                return None, MockResponse(method, uri)
            elif method == "PUT" and uri.endswith("/heartbeat"):
                if isinstance(heartbeat_result, Exception):
                    raise heartbeat_result
                else:
                    return heartbeat_result, MockResponse(method, uri)
            assert False

        return mock_request

    def test__create__subscription_created_on_server(self):
        token = "id"
        paths = ["tag1", "tag2", "tag3"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        HttpTagSubscription.create(
            self._client,
            paths,
            ManualResetTimer.null_timer,
            ManualResetTimer.null_timer,
        )

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": paths, "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token},
            ),
        ]

    @pytest.mark.asyncio
    async def test__create_async__subscription_created_on_server(self):
        token = "id"
        paths = ["tag1", "tag2", "tag3"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        await HttpTagSubscription.create_async(
            self._client,
            paths,
            ManualResetTimer.null_timer,
            ManualResetTimer.null_timer,
        )

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": paths, "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token},
            ),
        ]

    def test__update_timer_elapses__server_queried_for_updates_and_timer_reset(self):
        token = "test subscription"
        paths = []
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = HttpTagSubscription.create(
            self._client, paths, timer, ManualResetTimer.null_timer
        )

        assert uut is not None
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": paths, "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token},
            ),
        ]
        timer.start.assert_called_once_with()

        timer.elapsed()

        assert self._client.all_requests.call_count == 3
        self._client.all_requests.assert_called_with(
            "GET", "/nitag/v2/subscriptions/{id}/values/current", params={"id": token}
        )
        assert timer.start.call_count == 2
        assert len(timer.method_calls) == 2

    def test__tags_updates_received_from_server__tag_changed_event_fired_with_each_update(
        self,
    ):
        token = "test subscription"
        timestamp = datetime.now(timezone.utc)
        timestamp_str = TimestampUtilities.datetime_to_str(timestamp)
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        updates_list = self._one_update_of_each_type(timestamp_str)
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                token,
                {
                    "subscriptionUpdates": [
                        {"subscriptionId": token, "updates": updates_list}
                    ]
                },
            )
        )

        updates = {}
        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )

        def on_tag_changed(
            tag: tbase.TagData, reader: tbase.TagValueReader | None
        ) -> None:
            assert tag is not None
            assert tag.path
            assert tag.path not in updates
            updates[tag.path] = (tag, reader)

        uut.tag_changed += on_tag_changed

        timer.elapsed()

        value_converters = {
            "DOUBLE": float,
            "INT": int,
            "STRING": str,
            "BOOLEAN": {"True": True, "False": False}.get,
            "U_INT64": int,
            "DATE_TIME": TimestampUtilities.str_to_datetime,
        }

        def check_args(
            data: Dict[str, Any],
            tag: tbase.TagData,
            reader: tbase.TagValueReader | None,
        ) -> None:
            assert tbase.DataType.from_api_name(data["type"]) == tag.data_type
            convert_value = value_converters[data["type"]]
            assert reader is not None
            value = reader.read(include_timestamp=True, include_aggregates=True)
            assert value is not None
            assert convert_value(data["value"]) == value.value
            assert timestamp == value.timestamp
            if "aggregates" not in data:
                assert value.count is None
            else:
                assert value.count is not None
                assert data["aggregates"]["count"] == value.count
                if "avg" in data["aggregates"]:
                    assert data["aggregates"]["avg"] == value.mean
                    assert convert_value(data["aggregates"]["min"]) == value.min
                    assert convert_value(data["aggregates"]["max"]) == value.max

        assert 6 == len(updates)
        for u in updates_list:
            path = u["tag"]["path"]
            assert path in updates
            check_args(u, *updates[path])

    def test__updates_received_on_create__tag_changed_event_doesnt_see_those_updates(
        self,
    ):
        token = "test subscription"
        timestamp = datetime.now(timezone.utc)
        timestamp_str = TimestampUtilities.datetime_to_str(timestamp)
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        updates_list = self._one_update_of_each_type(timestamp_str)
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                token,
                {
                    "subscriptionUpdates": [
                        {"subscriptionId": token, "updates": updates_list}
                    ]
                },
            )
        )

        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )

        assert self._client.all_requests.call_count == 2

        def on_tag_changed(
            tag: tbase.TagData, reader: tbase.TagValueReader | None
        ) -> None:
            assert False, "Should not have received any updates"

        uut.tag_changed += on_tag_changed
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(None, {})
        )

        timer.elapsed()

        assert self._client.all_requests.call_count == 3
        self._client.all_requests.assert_called_with(
            "GET", "/nitag/v2/subscriptions/{id}/values/current", params={"id": token}
        )

    def test__update_fails__update_timer_elapsed__error_ignored(self):
        token = "test subscription"
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )
        updates = []

        def on_tag_changed(
            tag: tbase.TagData, reader: tbase.TagValueReader | None
        ) -> None:
            updates.append((tag, reader))

        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )
        uut.tag_changed += on_tag_changed

        assert timer.start.call_count == 1
        assert self._client.all_requests.call_count == 2
        assert self._client.all_requests.call_args[0][1].endswith("/values/current")

        self._client.all_requests.configure_mock(side_effect=core.ApiException("oops"))

        timer.elapsed()
        assert timer.start.call_count == 2
        assert self._client.all_requests.call_count == 3
        assert self._client.all_requests.call_args[0][1].endswith("/values/current")

        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(None, {})
        )

        timer.elapsed()
        assert timer.start.call_count == 3
        assert self._client.all_requests.call_count == 4
        assert self._client.all_requests.call_args[0][1].endswith("/values/current")

        assert 0 == len(updates)

    def test__invalid_subscription_updates_received__those_updates_skipped(self):
        token = "test subscription"
        timestamp = datetime.now(timezone.utc)
        timestamp_str = TimestampUtilities.datetime_to_str(timestamp)
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        good_update = self._one_update_of_each_type(timestamp_str)[0]
        updates_list = [
            None,
            {},
            {"value": "invalid"},
            {"value": "invalid", "type": "STRING"},
            {
                "value": "invalid",
                "type": "STRING",
                "tag": {"type": "STRING", "path": "invalid"},
            },
            {
                "value": "invalid",
                "type": "STRING",
                "timestamp": None,
                "tag": {"type": "STRING", "path": "invalid"},
            },
            {"value": "invalid", "type": "STRING", "timestamp": timestamp_str},
            {
                "value": "invalid",
                "type": "STRING",
                "timestamp": timestamp_str,
                "tag": {"type": "STRING", "path": ""},
            },
            {
                "value": "invalid",
                "type": "BOOLEAN",
                "timestamp": timestamp_str,
                "tag": {"type": "BOOLEAN", "path": "bool"},
            },
            good_update,
        ]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                token,
                {
                    "subscriptionUpdates": [
                        None,
                        {},
                        {"updates": []},
                        {"subscriptionId": token, "updates": updates_list},
                    ],
                },
            )
        )

        def on_tag_changed(
            tag: tbase.TagData, value: tbase.TagValueReader | None
        ) -> None:
            assert tag is not None
            assert tag.path
            assert tag.path not in updates
            updates[tag.path] = (tag, value)

        updates = {}
        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )
        uut.tag_changed += on_tag_changed

        timer.elapsed()

        assert 2 == len(updates)
        assert "bool" in updates
        tag, reader = updates["bool"]
        assert tbase.DataType.BOOLEAN == tag.data_type
        with pytest.raises(core.ApiException):
            reader.read()

        assert "double" in updates
        tag, reader = updates["double"]
        assert tbase.DataType.DOUBLE == tag.data_type
        value = reader.read(include_timestamp=True, include_aggregates=True)
        assert 3.14 == value.value
        assert timestamp == value.timestamp
        assert value.count is not None
        assert 1.1 == value.min
        assert 4.4 == value.max
        assert 3 == value.count
        assert 2.88 == value.mean

    def test__unknown_data_type_received_in_update__tag_changed_event_still_fires(self):
        token = "test subscription"
        timestamp = datetime.now(timezone.utc)
        timestamp_str = TimestampUtilities.datetime_to_str(timestamp)
        timer = mock.Mock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                token,
                {
                    "subscriptionUpdates": [
                        {
                            "subscriptionId": token,
                            "updates": [
                                {
                                    "value": "unknown",
                                    "type": "BLAH",
                                    "timestamp": timestamp_str,
                                    "tag": {"type": "BLAH", "path": "unknown"},
                                    "aggregates": {
                                        "min": "1.1",
                                        "max": "4.4",
                                        "count": 3,
                                        "avg": 2.88,
                                    },
                                }
                            ],
                        },
                    ],
                },
            )
        )

        def on_tag_changed(
            tag: tbase.TagData, reader: tbase.TagValueReader | None
        ) -> None:
            assert tag is not None
            assert tag.path
            assert tag.path not in updates
            updates[tag.path] = (tag, reader)

        updates = {}
        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )
        uut.tag_changed += on_tag_changed

        timer.elapsed()

        assert 1 == len(updates)
        assert "unknown" in updates
        tag, reader = updates["unknown"]
        assert tbase.DataType.UNKNOWN == tag.data_type

        assert reader is None

    def test__exit__subscription_deleted_from_server(self):
        token = "test subscription"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        with HttpTagSubscription.create(
            self._client, [], ManualResetTimer.null_timer, ManualResetTimer.null_timer
        ):
            pass

        assert self._client.all_requests.call_args == mock.call(
            "DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}
        )

    def test__exit__timer_stopped_and_callback_unregistered(self):
        token = "id"
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        with HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        ):
            assert timer.stop.call_count == 0
            assert len(timer.elapsed) == 1

        assert timer.stop.call_count == 1
        assert len(timer.elapsed) == 0

    @pytest.mark.asyncio
    async def test__aexit__subscription_deleted_from_server(self):
        token = "test subscription"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        async with await HttpTagSubscription.create_async(
            self._client, [], ManualResetTimer.null_timer, ManualResetTimer.null_timer
        ):
            pass

        assert self._client.all_requests.call_args == mock.call(
            "DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}
        )

    @pytest.mark.asyncio
    async def test__aexit__timer_stopped_and_callback_unregistered(self):
        token = "test subscription"
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        async with await HttpTagSubscription.create_async(
            self._client, [], timer, ManualResetTimer.null_timer
        ):
            assert timer.stop.call_count == 0
            assert len(timer.elapsed) == 1

        assert timer.stop.call_count == 1
        assert len(timer.elapsed) == 0

    def test__close__subscription_deleted_from_server(self):
        token = "test subscription"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = HttpTagSubscription.create(
            self._client, [], ManualResetTimer.null_timer, ManualResetTimer.null_timer
        )
        uut.close()

        assert self._client.all_requests.call_args == mock.call(
            "DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}
        )

    def test__close__timer_stopped_and_callback_unregistered(self):
        token = "id"
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = HttpTagSubscription.create(
            self._client, [], timer, ManualResetTimer.null_timer
        )
        assert timer.stop.call_count == 0
        assert len(timer.elapsed) == 1

        uut.close()
        assert timer.stop.call_count == 1
        assert len(timer.elapsed) == 0

    @pytest.mark.asyncio
    async def test__close_async__subscription_deleted_from_server(self):
        token = "test subscription"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = await HttpTagSubscription.create_async(
            self._client, [], ManualResetTimer.null_timer, ManualResetTimer.null_timer
        )
        await uut.close_async()

        assert self._client.all_requests.call_args == mock.call(
            "DELETE", "/nitag/v2/subscriptions/{id}", params={"id": token}
        )

    @pytest.mark.asyncio
    async def test__close_async__timer_stopped_and_callback_unregistered(self):
        token = "id"
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = await HttpTagSubscription.create_async(
            self._client, [], timer, ManualResetTimer.null_timer
        )
        assert timer.stop.call_count == 0
        assert len(timer.elapsed) == 1

        await uut.close_async()
        assert timer.stop.call_count == 1
        assert len(timer.elapsed) == 0

    def test__heartbeat_timer_elapsed__heartbeat_sent_to_server_and_timer_reset(self):
        token = "test subscription"
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token, {})
        )

        uut = HttpTagSubscription.create(
            self._client, [], ManualResetTimer.null_timer, timer
        )
        assert uut is not None
        assert timer.start.call_count == 1

        timer.elapsed()
        assert self._client.all_requests.call_args == mock.call(
            "PUT",
            "/nitag/v2/subscriptions/{id}/heartbeat",
            params={"id": token},
            data=None,
        )
        assert timer.start.call_count == 2

    def test__heartbeat_query_errors__subscription_recreated(self):
        token1 = "test subscription"
        token2 = "second test subscription"
        paths = ["tag1", "tag2", "tag3"]
        timer = mock.MagicMock(ManualResetTimer, wraps=ManualResetTimer.null_timer)
        type(timer).elapsed = events.events._EventSlot("elapsed")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(token1, {})
        )

        uut = HttpTagSubscription.create(
            self._client, paths, ManualResetTimer.null_timer, timer
        )

        assert uut is not None
        assert timer.start.call_count == 1
        assert self._client.all_requests.call_count == 2
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": paths, "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token1},
            ),
        ]

        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                token2, {}, core.ApiException("Unknown subscription")
            )
        )

        timer.elapsed()

        assert timer.start.call_count == 2
        assert self._client.all_requests.call_count == 5
        assert self._client.all_requests.call_args_list[-3:] == [
            mock.call(
                "PUT",
                "/nitag/v2/subscriptions/{id}/heartbeat",
                params={"id": token1},
                data=None,
            ),
            mock.call(
                "POST",
                "/nitag/v2/subscriptions",
                params=None,
                data={"tags": paths, "updatesOnly": True},
            ),
            mock.call(
                "GET",
                "/nitag/v2/subscriptions/{id}/values/current",
                params={"id": token2},
            ),
        ]

        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(None, None)
        )

        timer.elapsed()

        assert timer.start.call_count == 3
        assert self._client.all_requests.call_count == 6
        assert self._client.all_requests.call_args_list[-1:] == [
            mock.call(
                "PUT",
                "/nitag/v2/subscriptions/{id}/heartbeat",
                params={"id": token2},
                data=None,
            ),
        ]

    @classmethod
    def _one_update_of_each_type(cls, timestamp_str: str) -> List[Any]:
        return [
            {
                "value": "3.14",
                "type": "DOUBLE",
                "timestamp": timestamp_str,
                "tag": {"type": "DOUBLE", "path": "double"},
                "aggregates": {"min": "1.1", "max": "4.4", "count": 3, "avg": 2.88},
            },
            {
                "value": "-2",
                "type": "INT",
                "timestamp": timestamp_str,
                "tag": {"type": "INT", "path": "int"},
                "aggregates": {"min": "-5", "max": "3", "count": 4, "avg": 3.23},
            },
            {
                "value": "testing",
                "type": "STRING",
                "timestamp": timestamp_str,
                "tag": {"type": "STRING", "path": "string"},
                "aggregates": {"count": 3},
            },
            {
                "value": "True",
                "type": "BOOLEAN",
                "timestamp": timestamp_str,
                "tag": {"type": "BOOLEAN", "path": "bool"},
            },
            {
                "value": "103",
                "type": "U_INT64",
                "timestamp": timestamp_str,
                "tag": {"type": "U_INT64", "path": "uint64"},
            },
            {
                "value": timestamp_str,
                "type": "DATE_TIME",
                "timestamp": timestamp_str,
                "tag": {"type": "DATE_TIME", "path": "date"},
            },
        ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/mock_manualresettimer.py sha256=0f5322bdc752f17bdff2c63ac6cdb6876fd743f7c5a7d368b27ee4eaff61b82a bytes=599 -->
## FILE: tests/tag/mock_manualresettimer.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/mock_manualresettimer.py`
- sha256: `0f5322bdc752f17bdff2c63ac6cdb6876fd743f7c5a7d368b27ee4eaff61b82a`
- bytes: 599

````python
from unittest.mock import Mock, PropertyMock

import events.events  # type: ignore
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer


def MockManualResetTimer():  # noqa: N802
    """Construct a mock ManualResetTimer"""
    m = Mock(ManualResetTimer)
    type(m).elapsed = PropertyMock(return_value=events.events._EventSlot("elapsed"))
    type(m).__aenter__ = ManualResetTimer.__aenter__
    type(m).__aexit__ = ManualResetTimer.__aexit__
    type(m).__enter__ = ManualResetTimer.__enter__
    type(m).__exit__ = ManualResetTimer.__exit__
    return m
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_asynctagqueryresultcollection.py sha256=065624648aa47a87d3080770bca7adaa6f8d537291f76c42b7364e607db74f92 bytes=9409 -->
## FILE: tests/tag/test_asynctagqueryresultcollection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_asynctagqueryresultcollection.py`
- sha256: `065624648aa47a87d3080770bca7adaa6f8d537291f76c42b7364e607db74f92`
- bytes: 9409

````python
import asyncio

import pytest  # type: ignore
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.tag import AsyncTagQueryResultCollection, DataType, TagData


class TestAsyncTagQueryResultCollection:
    class MockAsyncTagQueryResultCollection(AsyncTagQueryResultCollection):
        def __init__(self, first_page, total_count, skip):
            super().__init__(first_page, total_count, skip)
            self._setup_called = False
            self._next_total_count = None
            self._next_page = []
            self._next_throw = None
            self._calls = []

        def setup(
            self, *, next_page=None, new_total_count=None, exception_to_throw=None
        ):
            assert (
                not self._setup_called
            ), "setup called without previous call to _query_page_async"
            self._setup_called = True
            self._next_page = next_page
            self._next_total_count = new_total_count
            self._next_throw = exception_to_throw

        def verify(self, expected_skips):
            assert expected_skips == self._calls

        def _query_page_async(self, skip):
            assert self._setup_called, "_query_page_async called without call to setup"
            self._setup_called = False
            self._calls.append(skip)

            if self._next_throw is not None:
                f = asyncio.get_event_loop().create_future()
                f.set_exception(self._next_throw)
                return f

            if self._next_total_count is not None:
                self._total_count = self._next_total_count

            f = asyncio.get_event_loop().create_future()
            f.set_result(self._next_page)
            return f

    def test__constructed__has_first_page_of_data(self):
        data = [
            TagData("tag1", DataType.BOOLEAN),
            TagData("tag2", DataType.DATE_TIME),
            TagData("tag3", DataType.DOUBLE),
        ]

        uut = self.MockAsyncTagQueryResultCollection(data, len(data), 0)

        assert data == list(uut.current_page)
        assert len(data) == uut.total_count

    @pytest.mark.asyncio
    async def test__move_next_page__current_page_queried_and_updated(self):
        first_page = [
            TagData("tag1", DataType.BOOLEAN),
            TagData("tag2", DataType.DATE_TIME),
        ]

        second_page = [TagData("tag3", DataType.DOUBLE)]

        uut = self.MockAsyncTagQueryResultCollection(
            first_page, len(first_page) + len(second_page), 0
        )
        uut.setup(next_page=second_page)

        await uut.move_next_page_async()
        assert len(first_page) + len(second_page) == uut.total_count
        assert second_page == uut.current_page
        uut.verify([len(first_page)])

    @pytest.mark.asyncio
    async def test__move_next_page__skip_is_respected(self):
        page1 = 2
        page2 = 5
        page3 = 1
        initial_skip = 1
        total_count = initial_skip + page1 + page2 + page3

        tag1 = TagData("tag1", DataType.BOOLEAN)
        tag2 = TagData("tag2", DataType.DATE_TIME)
        tag3 = TagData("tag3", DataType.DOUBLE)

        uut = self.MockAsyncTagQueryResultCollection(
            [tag1] * page1, total_count, initial_skip
        )
        uut.setup(next_page=[tag2] * page2)

        await uut.move_next_page_async()
        uut.setup(next_page=[tag3] * page3)
        await uut.move_next_page_async()

        uut.verify([initial_skip + page1, initial_skip + page1 + page2])

    @pytest.mark.asyncio
    async def test__on_last_page__move_next_page__current_page_set_to_null(self):
        tag = TagData("tag1", DataType.BOOLEAN)
        uut = self.MockAsyncTagQueryResultCollection([tag], 1, 0)

        assert 1 == uut.total_count
        assert 1 == len(uut.current_page)
        assert tag is uut.current_page[0]

        await uut.move_next_page_async()
        assert 1 == uut.total_count
        assert uut.current_page is None

        await uut.move_next_page_async()
        assert 1 == uut.total_count
        assert uut.current_page is None

    @pytest.mark.asyncio
    async def test__page_count_changes__move_next_page__current_page_set_to_null(self):
        tag = TagData("tag1", DataType.BOOLEAN)
        initial_total_count = 2
        uut = self.MockAsyncTagQueryResultCollection([tag], initial_total_count, 0)
        uut.setup(new_total_count=1)

        # according to initial_total_count, there should be more data, but there's not
        # - and that should be okay, and clear the current_page
        await uut.move_next_page_async()
        assert uut.current_page is None

        await uut.move_next_page_async()
        assert uut.current_page is None

        uut.verify([1])

    @pytest.mark.asyncio
    async def test__total_count_changes__move_next_page__total_count_updated(self):
        tag1 = TagData("tag1", DataType.BOOLEAN)
        tag2 = TagData("tag2", DataType.DATE_TIME)
        uut = self.MockAsyncTagQueryResultCollection([tag1], 3, 0)
        uut.setup(next_page=[tag2], new_total_count=2)

        assert 3 == uut.total_count
        await uut.move_next_page_async()
        assert 2 == uut.total_count
        assert 1 == len(uut.current_page)
        assert tag2 is uut.current_page[0]
        uut.verify([1])

        await uut.move_next_page_async()
        assert 2 == uut.total_count
        assert uut.current_page is None
        uut.verify([1])  # still only one query has happened, due to new total_count

    @pytest.mark.asyncio
    async def test__reset__page_is_queried_with_initial_skip(self):
        initial_skip = 1
        tag2 = TagData("tag2", DataType.DATE_TIME)
        uut = self.MockAsyncTagQueryResultCollection([tag2], 3, initial_skip)

        tag2b = TagData("tag2b", DataType.DATE_TIME)
        uut.setup(next_page=[tag2b], new_total_count=2)
        await uut.reset_async()

        assert 2 == uut.total_count
        assert 1 == len(uut.current_page)
        assert tag2b is uut.current_page[0]

        await uut.move_next_page_async()
        assert uut.current_page is None

        uut.verify([initial_skip])

    @pytest.mark.asyncio
    async def test__no_results__constructed__current_page_is_null(self):
        uut = self.MockAsyncTagQueryResultCollection(None, 0, 0)
        assert 0 == uut.total_count
        assert uut.current_page is None

        await uut.move_next_page_async()
        assert uut.current_page is None

    @pytest.mark.asyncio
    async def test__server_data_removed_after_query__reset__query_has_no_results(self):
        tag = TagData("tag", DataType.INT32)
        uut = self.MockAsyncTagQueryResultCollection([tag], 1, 0)
        assert 1 == uut.total_count
        assert uut.current_page is not None

        uut.setup(new_total_count=0)
        await uut.reset_async()
        assert 0 == uut.total_count
        assert uut.current_page is None

        await uut.move_next_page_async()
        assert uut.current_page is None

        uut.verify([0])

    @pytest.mark.asyncio
    async def test__server_data_added_after_empty_query__reset__query_has_results(self):
        tags = [TagData("tag", DataType.INT32)]
        uut = self.MockAsyncTagQueryResultCollection(None, 0, 0)
        uut.setup(next_page=tags, new_total_count=1)

        await uut.reset_async()
        assert 1 == uut.total_count
        assert tags == uut.current_page

        await uut.move_next_page_async()
        assert uut.current_page is None

        uut.verify([0])

    @pytest.mark.asyncio
    async def test__server_error__move_next_page__client_sees_error_but_can_continue(
        self,
    ):
        exception_to_throw = ApiException()
        initial_tags = [TagData("tag", DataType.INT32)]
        next_page = [TagData("tag2", DataType.STRING)]
        uut = self.MockAsyncTagQueryResultCollection(initial_tags, 2, 0)
        uut.setup(exception_to_throw=exception_to_throw)

        with pytest.raises(ApiException):
            await uut.move_next_page_async()
        # After the failure, the current_page should remain unchanged
        assert initial_tags == uut.current_page

        # Try again after error -- let it work this time
        uut.setup(next_page=next_page)
        await uut.move_next_page_async()
        assert next_page == uut.current_page

        uut.verify([1, 1])

    @pytest.mark.asyncio
    async def test__server_error__reset__client_sees_error_but_can_retry(self):
        exception_to_throw = ApiException()
        initial_tags = [TagData("tag", DataType.INT32)]
        first_page = [TagData("tag2", DataType.STRING)]
        uut = self.MockAsyncTagQueryResultCollection(initial_tags, 1, 0)
        uut.setup(exception_to_throw=exception_to_throw)

        # After the failure, the current_page should remain unchanged
        with pytest.raises(ApiException):
            await uut.reset_async()
        assert initial_tags == uut.current_page

        # Try again after error -- let it work this time
        uut.setup(next_page=first_page)
        await uut.reset_async()
        assert first_page == uut.current_page

        uut.verify([0, 0])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_bufferedtagwriter.py sha256=2c2525540db5cd12c3a7dedaffe1f2255546e59bfc2ff12fd448a5e65cee3d1e bytes=30729 -->
## FILE: tests/tag/test_bufferedtagwriter.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_bufferedtagwriter.py`
- sha256: `2c2525540db5cd12c3a7dedaffe1f2255546e59bfc2ff12fd448a5e65cee3d1e`
- bytes: 30729

````python
import datetime
from unittest import mock
from unittest.mock import Mock, PropertyMock

import nisystemlink.clients.core as core
import nisystemlink.clients.tag as tbase
import pytest  # type: ignore
from nisystemlink.clients.tag._core._itime_stamper import ITimeStamper
from nisystemlink.clients.tag._core._manual_reset_timer import ManualResetTimer
from nisystemlink.clients.tag._core._system_time_stamper import SystemTimeStamper

from .mock_manualresettimer import MockManualResetTimer


class TestBufferedTagWriter:
    serialized_timestamp = "2018-11-15T03:47:36.000000+0000"
    timestamp = datetime.datetime.strptime(
        serialized_timestamp, "%Y-%m-%dT%H:%M:%S.%f%z"
    )

    def test__invalid_path__write__raises(self):
        writer = self.MockBufferedTagWriter(None, 1)

        with pytest.raises(ValueError) as excinfo:
            writer.write(None, tbase.DataType.BOOLEAN, False, timestamp=None)
        assert "path " in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            writer.write("", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert "path " in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            writer.write("*", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert "path " in str(excinfo.value)

    def test__invalid_data_type__write__raises(self):
        writer = self.MockBufferedTagWriter(None, 1)
        with pytest.raises(ValueError) as excinfo:
            writer.write("tag", tbase.DataType.UNKNOWN, "test", timestamp=None)
        assert "type " in str(excinfo.value)

    def test__write__item_created_and_buffered(self):
        writer = self.MockBufferedTagWriter(None, 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None, return_value=None)

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.mock_create_item.assert_called_once_with(
            "tag", tbase.DataType.BOOLEAN, "False", self.timestamp
        )
        writer.mock_buffer_value.assert_called_once_with("tag", item)

    def test__null_timestamp_and_no_time_stamper__write__default_time_stamper_used(
        self,
    ):
        writer = self.MockBufferedTagWriter(None, 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)

        before_write = datetime.datetime.now(datetime.timezone.utc)
        tolerance_seconds = 0.1

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert writer.mock_create_item.call_count == 1
        assert writer.mock_create_item.call_args[0][:-1] == (
            "tag",
            tbase.DataType.BOOLEAN,
            "False",
        )
        timestamp = writer.mock_create_item.call_args[0][-1]
        assert timestamp is not None
        assert (timestamp - before_write).total_seconds() < tolerance_seconds
        writer.mock_buffer_value.assert_called_once_with("tag", item)

    def test__null_timestamp_and_time_stamper_given__write__time_stamper_used(self):
        date_string = "2019-07-08T18:52:58.230069+0000"
        date_offset = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f%z")
        writer = self.MockBufferedTagWriter(Mock(ITimeStamper), 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None, return_value=None)
        timestamp_property = PropertyMock(return_value=date_offset)
        type(writer.time_stamper).timestamp = timestamp_property

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        writer.mock_create_item.assert_called_once_with(
            "tag", tbase.DataType.BOOLEAN, "False", date_offset
        )
        writer.mock_buffer_value.assert_called_once_with("tag", item)
        timestamp_property.assert_called_once_with()

    def test__write__new_timestamp_queried_for_each_value(self):
        writer = self.MockBufferedTagWriter(Mock(ITimeStamper), 3)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        timestamp_property = PropertyMock(
            return_value=datetime.datetime.now(datetime.timezone.utc)
        )
        type(writer.time_stamper).timestamp = timestamp_property

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        timestamp_property.assert_called_once_with()

        timestamp_property.reset_mock()
        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        timestamp_property.assert_called_once_with()

    def test__buffer_size__write__updates_sent_when_buffer_fills(self):
        writer = self.MockBufferedTagWriter(None, 2)
        item1 = object()
        item2 = object()
        buffer = [item1, item2]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)

        assert writer._num_buffered == 0
        assert writer._buffer_limit == 2
        writer.write("tag1", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.mock_copy_buffer.assert_not_called()
        writer.mock_send_writes.assert_not_called()
        assert writer._num_buffered == 1
        writer.write("tag2", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)

        assert writer.mock_create_item.call_args_list == [
            mock.call("tag1", tbase.DataType.BOOLEAN, "False", self.timestamp),
            mock.call("tag2", tbase.DataType.DOUBLE, "1.1", self.timestamp),
        ]
        assert writer.mock_buffer_value.call_args_list == [
            mock.call("tag1", item1),
            mock.call("tag2", item2),
        ]
        writer.mock_copy_buffer.assert_called_once_with()
        writer.mock_send_writes.assert_called_once_with(buffer)

    def test__timer_enabled__write__timer_started(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item = object()

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property
        writer.timer.start.configure_mock(side_effect=None)

        writer.write("tag", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        writer.timer.start.assert_called_once_with()

    def test__timed_flush_errored__write__item_buffered_and_cached_error_raised(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item1 = object()
        item2 = object()
        item3 = object()
        buffer = [item1]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2, item3])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=core.ApiException)
        writer.mock_clear_buffer.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag1", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        # Here's where the error is raised by the API
        writer.trigger_flush_event()
        # But here's where the user gets a chance to see the error
        with pytest.raises(core.ApiException):
            writer.write("tag2", tbase.DataType.INT32, -1, timestamp=self.timestamp)
        writer.clear_buffered_writes()  # "Clear" the buffer, or next write would fill it
        writer.write("tag3", tbase.DataType.STRING, "test3", timestamp=self.timestamp)

        writer.mock_send_writes.assert_called_once_with(buffer)
        assert writer.mock_buffer_value.call_args_list == [
            mock.call("tag1", item1),
            mock.call(
                "tag2", item2
            ),  # tag2 should have been buffered despite the error
            mock.call("tag3", item3),
        ]

    def test__create_item_errors__write__user_sees_error(self):
        writer = self.MockBufferedTagWriter(None, 2)
        writer.mock_create_item.configure_mock(side_effect=[ValueError, object()])

        with pytest.raises(ValueError):
            writer.write("tag1", tbase.DataType.UINT64, 1, timestamp=self.timestamp)

        # Yet after the error, other writes can happen
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.write("tag2", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        assert writer.mock_buffer_value.call_count == 1

    @pytest.mark.asyncio
    async def test__invalid_path__write_async__raises(self):
        writer = self.MockBufferedTagWriter(None, 1)

        with pytest.raises(ValueError) as excinfo:
            await writer.write_async(
                None, tbase.DataType.BOOLEAN, False, timestamp=None
            )
        assert "path " in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            await writer.write_async("", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert "path " in str(excinfo.value)

        with pytest.raises(ValueError) as excinfo:
            await writer.write_async("*", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert "path " in str(excinfo.value)

    @pytest.mark.asyncio
    async def test__invalid_data_type__write_async__raises(self):
        writer = self.MockBufferedTagWriter(None, 1)
        with pytest.raises(ValueError) as excinfo:
            await writer.write_async(
                "tag", tbase.DataType.UNKNOWN, "test", timestamp=None
            )
        assert "type " in str(excinfo.value)

    @pytest.mark.asyncio
    async def test__write_async__item_created_and_buffered(self):
        writer = self.MockBufferedTagWriter(None, 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)

        await writer.write_async(
            "tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp
        )
        writer.mock_create_item.assert_called_once_with(
            "tag", tbase.DataType.BOOLEAN, "False", self.timestamp
        )
        writer.mock_buffer_value.assert_called_once_with("tag", item)

    @pytest.mark.asyncio
    async def test__null_timestamp_and_no_time_stamper__write_async__default_time_stamper_used(
        self,
    ):
        writer = self.MockBufferedTagWriter(None, 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)

        before_write = datetime.datetime.now(datetime.timezone.utc)
        tolerance_seconds = 0.1

        await writer.write_async("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert writer.mock_create_item.call_count == 1
        assert writer.mock_create_item.call_args[0][:-1] == (
            "tag",
            tbase.DataType.BOOLEAN,
            "False",
        )
        timestamp = writer.mock_create_item.call_args[0][-1]
        assert timestamp is not None
        assert (timestamp - before_write).total_seconds() < tolerance_seconds
        writer.mock_buffer_value.assert_called_once_with("tag", item)

    @pytest.mark.asyncio
    async def test__null_timestamp_and_time_stamper_given__write_async__time_stamper_used(
        self,
    ):
        date_string = "2019-07-08T18:52:58.230069+0000"
        date_offset = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f%z")
        writer = self.MockBufferedTagWriter(Mock(ITimeStamper), 2)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        timestamp_property = PropertyMock(return_value=date_offset)
        type(writer.time_stamper).timestamp = timestamp_property

        await writer.write_async("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        writer.mock_create_item.assert_called_once_with(
            "tag", tbase.DataType.BOOLEAN, "False", date_offset
        )
        writer.mock_buffer_value.assert_called_once_with("tag", item)
        timestamp_property.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__write_async__new_timestamp_queried_for_each_value(self):
        writer = self.MockBufferedTagWriter(Mock(ITimeStamper), 3)
        item = object()
        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        timestamp_property = PropertyMock(
            return_value=datetime.datetime.now(datetime.timezone.utc)
        )
        type(writer.time_stamper).timestamp = timestamp_property

        await writer.write_async("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        timestamp_property.assert_called_once_with()
        await writer.write_async("tag", tbase.DataType.BOOLEAN, False, timestamp=None)
        assert timestamp_property.call_args_list == [mock.call(), mock.call()]

    @pytest.mark.asyncio
    async def test__buffer_size__write_async__updates_sent_when_buffer_fills(self):
        writer = self.MockBufferedTagWriter(None, 2)
        item1 = object()
        item2 = object()
        buffer = [item1, item2]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes_async.configure_mock(side_effect=None)

        assert writer._num_buffered == 0
        assert writer._buffer_limit == 2
        await writer.write_async(
            "tag1", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp
        )
        writer.mock_copy_buffer.assert_not_called()
        writer.mock_send_writes_async.assert_not_called()
        assert writer._num_buffered == 1
        await writer.write_async(
            "tag2", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp
        )

        assert writer.mock_create_item.call_args_list == [
            mock.call("tag1", tbase.DataType.BOOLEAN, "False", self.timestamp),
            mock.call("tag2", tbase.DataType.DOUBLE, "1.1", self.timestamp),
        ]
        assert writer.mock_buffer_value.call_args_list == [
            mock.call("tag1", item1),
            mock.call("tag2", item2),
        ]
        writer.mock_copy_buffer.assert_called_once_with()
        writer.mock_send_writes_async.assert_called_once_with(buffer)

    @pytest.mark.asyncio
    async def test__timer_enabled__write_async__timer_started(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item = object()

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property
        writer.timer.start.configure_mock(side_effect=None)

        await writer.write_async(
            "tag", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp
        )
        writer.timer.start.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__timed_flush_errored__write_async__item_buffered_and_cached_error_raised(
        self,
    ):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item1 = object()
        item2 = object()
        item3 = object()
        buffer = [item1]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2, item3])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=core.ApiException)
        writer.mock_clear_buffer.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag1", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        # Here's where the error is raised by the API
        writer.trigger_flush_event()
        # But here's where the user gets a chance to see the error
        with pytest.raises(core.ApiException):
            await writer.write_async(
                "tag2", tbase.DataType.INT32, -1, timestamp=self.timestamp
            )
        writer.clear_buffered_writes()  # "Clear" the buffer, or next write would fill it
        await writer.write_async(
            "tag3", tbase.DataType.STRING, "test3", timestamp=self.timestamp
        )

        writer.mock_send_writes.assert_called_once_with(buffer)
        assert writer.mock_buffer_value.call_args_list == [
            mock.call("tag1", item1),
            mock.call(
                "tag2", item2
            ),  # tag2 should have been buffered despite the error
            mock.call("tag3", item3),
        ]

    def test__items_buffered__clear_buffered_writes__clear_buffer_called(self):
        writer = self.MockBufferedTagWriter(None, 2)
        item1 = object()
        item2 = object()

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_clear_buffer.configure_mock(side_effect=None)

        writer.write("tag1", tbase.DataType.STRING, "test1", timestamp=self.timestamp)
        writer.clear_buffered_writes()
        writer.write("tag2", tbase.DataType.UINT64, 1, timestamp=self.timestamp)

        assert writer.mock_buffer_value.call_args_list == [
            mock.call("tag1", item1),
            mock.call("tag2", item2),
        ]
        writer.mock_clear_buffer.assert_called_once_with()

    def test__items_buffered__clear_buffered_writes__flush_timer_stopped(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())

        writer.mock_create_item.configure_mock(side_effect=None, return_value=object())
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_clear_buffer.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.clear_buffered_writes()

        writer.timer.start.assert_called_once_with()
        writer.timer.stop.assert_called_once_with()

    def test__items_buffered__send_buffered_writes__buffer_copied_and_sent(self):
        writer = self.MockBufferedTagWriter(None, 3)
        item1 = object()
        item2 = object()
        buffer = [item1, item2]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)

        writer.write("tag1", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.write("tag2", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        writer.send_buffered_writes()

        writer.mock_send_writes.assert_called_once_with(buffer)

    def test__no_items_buffered__send_buffered_writes__nothing_called(self):
        writer = self.MockBufferedTagWriter(None, 2)
        writer.send_buffered_writes()
        # The strict mock will assert no methods were called.

    def test__items_buffered__send_buffered_writes__flush_timer_stopped(self):
        writer = self.MockBufferedTagWriter(None, 3, MockManualResetTimer())
        item = object()
        buffer = [item]

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.send_buffered_writes()

        writer.timer.start.assert_called_once_with()
        writer.timer.stop.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__items_buffered__send_buffered_writes_async__buffer_copied_and_sent(
        self,
    ):
        writer = self.MockBufferedTagWriter(None, 3)
        item1 = object()
        item2 = object()
        buffer = [item1, item2]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes_async.configure_mock(side_effect=None)

        writer.write("tag1", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        writer.write("tag2", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        await writer.send_buffered_writes_async()

        writer.mock_send_writes_async.assert_called_once_with(buffer)

    @pytest.mark.asyncio
    async def test__no_items_buffered__send_buffered_writes_async__nothing_called(self):
        writer = self.MockBufferedTagWriter(None, 2)
        await writer.send_buffered_writes_async()
        # The strict mock will assert no methods were called.

    @pytest.mark.asyncio
    async def test__items_buffered__send_buffered_writes_async__flush_timer_stopped(
        self,
    ):
        writer = self.MockBufferedTagWriter(None, 3, MockManualResetTimer())
        item = object()
        buffer = [item]

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes_async.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        await writer.send_buffered_writes_async()

        writer.timer.start.assert_called_once_with()
        writer.timer.stop.assert_called_once_with()

    def test__items_buffered__flush_timer_elapsed__items_sent(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item = object()
        buffer = [item]

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        writer.write("tag", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        writer.trigger_flush_event()

        writer.mock_send_writes.assert_called_once_with(buffer)

    def test__send_buffered_writes_already_called__original_flush_timer_elapsed__updates_not_sent(
        self,
    ):
        writer = self.MockBufferedTagWriter(
            SystemTimeStamper(), 2, MockManualResetTimer()
        )
        item1 = object()
        item2 = object()
        buffer = [item1]

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)

        writer.write("tag1", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        elapsed_handlers = list(writer.timer.elapsed)
        writer.send_buffered_writes()
        writer.write("tag2", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)

        # Simulate queuing the timer event in parallel to SendBufferedWrites
        # by raising the event using the handlers that were there earlier.
        # (The second write should have replaced them with *new* event handlers. It
        # should also stop the original timer, but if the timer is already elapsing, it
        # should be ignored.)
        assert elapsed_handlers is not None
        for h in elapsed_handlers:
            h()

        writer.mock_copy_buffer.assert_called_once_with()
        writer.mock_send_writes.assert_called_once_with(buffer)

    def test__clear_buffered_writes_already_called__original_flush_timer_elapsed__writes_not_sent(
        self,
    ):
        writer = self.MockBufferedTagWriter(
            SystemTimeStamper(), 2, MockManualResetTimer()
        )
        item1 = object()
        item2 = object()

        writer.mock_create_item.configure_mock(side_effect=[item1, item2])
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_clear_buffer.configure_mock(side_effect=None)

        writer.write("tag1", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)
        elapsed_handlers = list(writer.timer.elapsed)
        writer.clear_buffered_writes()
        writer.write("tag2", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)

        # Simulate queuing the timer event in parallel to ClearBufferedWrites
        # by raising the event using the handlers that were there earlier.
        # (The second write should have replaced them with *new* event handlers. It
        # should also stop the original timer, but if the timer is already elapsing, it
        # should be ignored.)
        # The strict mock will assert the writes were never sent.
        assert elapsed_handlers is not None
        for h in elapsed_handlers:
            h()

    def test__writer_closed__buffered_writes_sent(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        item = object()
        buffer = [item]

        writer.mock_create_item.configure_mock(side_effect=None, return_value=item)
        writer.mock_buffer_value.configure_mock(side_effect=None)
        writer.mock_copy_buffer.configure_mock(side_effect=None, return_value=buffer)
        writer.mock_send_writes.configure_mock(side_effect=None)
        can_start_property = PropertyMock(return_value=True)
        type(writer.timer).can_start = can_start_property

        with writer:
            writer.write("tag", tbase.DataType.DOUBLE, 1.1, timestamp=self.timestamp)

        writer.mock_send_writes.assert_called_once_with(buffer)

    @pytest.mark.asyncio
    async def test__writer_closed__methods_called__raises(self):
        writer = self.MockBufferedTagWriter(None, 2, MockManualResetTimer())
        with writer:
            pass

        with pytest.raises(ReferenceError):
            writer.clear_buffered_writes()
        with pytest.raises(ReferenceError):
            writer.send_buffered_writes()
        with pytest.raises(ReferenceError):
            await writer.send_buffered_writes_async()
        with pytest.raises(ReferenceError):
            writer.write("tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp)
        with pytest.raises(ReferenceError):
            await writer.write_async(
                "tag", tbase.DataType.BOOLEAN, False, timestamp=self.timestamp
            )

    class MockBufferedTagWriter(tbase.BufferedTagWriter):
        def __init__(self, stamper=None, buffer_size=None, flush_timer=None):
            assert buffer_size is not None
            super().__init__(
                stamper or SystemTimeStamper(),
                buffer_size,
                flush_timer or ManualResetTimer.null_timer,
            )
            self._timer = flush_timer
            self._time_stamper = stamper

            self.mock_buffer_value = Mock(side_effect=NotImplementedError)
            self.mock_clear_buffer = Mock(side_effect=NotImplementedError)
            self.mock_copy_buffer = Mock(side_effect=NotImplementedError)
            self.mock_create_item = Mock(side_effect=NotImplementedError)
            self.mock_send_writes = Mock(side_effect=NotImplementedError)
            self.mock_send_writes_async = Mock(side_effect=NotImplementedError)

        @property
        def timer(self):
            return self._timer

        @property
        def time_stamper(self):
            return self._time_stamper

        def trigger_flush_event(self):
            self._timer.elapsed()

        def _buffer_value(self, *args, **kwargs):
            return self.mock_buffer_value(*args, **kwargs)

        def _clear_buffer(self, *args, **kwargs):
            return self.mock_clear_buffer(*args, **kwargs)

        def _copy_buffer(self, *args, **kwargs):
            return self.mock_copy_buffer(*args, **kwargs)

        def _create_item(self, *args, **kwargs):
            return self.mock_create_item(*args, **kwargs)

        def _send_writes(self, *args, **kwargs):
            return self.mock_send_writes(*args, **kwargs)

        async def _send_writes_async(self, *args, **kwargs):
            return self.mock_send_writes_async(*args, **kwargs)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_itagreader.py sha256=ee7e361c12c3b0f4304fb147728554e2bc88086a39276bb1d2c860b2f1cb4351 bytes=4653 -->
## FILE: tests/tag/test_itagreader.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_itagreader.py`
- sha256: `ee7e361c12c3b0f4304fb147728554e2bc88086a39276bb1d2c860b2f1cb4351`
- bytes: 4653

````python
import datetime
import os
import tempfile
import textwrap
from unittest import mock

import mypy.api
import pytest  # type: ignore
from nisystemlink.clients.tag import DataType, ITagReader
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)


class TestITagReader:
    class MockTagReader(ITagReader):
        def __init__(self):
            super().__init__()
            self.mock_read = mock.Mock()

        def _read(self, *args, **kwargs):
            return self.mock_read(*args, **kwargs)

        async def _read_async(self, *args, **kwargs):
            return self.mock_read(*args, **kwargs)

    # data_type: (serialized_value, value)
    test_values = {
        DataType.BOOLEAN: ("True", True),
        DataType.DATE_TIME: (
            "2020-01-01T00:22:11.123456Z",
            datetime.datetime(2020, 1, 1, 0, 22, 11, 123456, datetime.timezone.utc),
        ),
        DataType.DOUBLE: ("1.1", 1.1),
        DataType.INT32: ("-1", -1),
        DataType.UINT64: ("2", 2),
        DataType.STRING: ("foo", "foo"),
    }

    def test__get_tag_reader__read_sends_path_and_data_type(self):
        reader = self.MockTagReader()

        for data_type, (serialized_value, value) in self.test_values.items():
            path = "MyPath.{}".format(data_type.name)
            tag_reader = reader.get_tag_reader(path, data_type)
            reader.mock_read.configure_mock(
                return_value=SerializedTagWithAggregates(
                    path, data_type, serialized_value
                )
            )
            result = tag_reader.read()
            assert reader.mock_read.call_args_list
            assert value == result.value
            assert data_type == result.data_type

    @pytest.mark.asyncio
    async def test__get_tag_reader__read_async_sends_path_and_data_type(self):
        reader = self.MockTagReader()

        for data_type, (serialized_value, value) in self.test_values.items():
            path = "MyPath.{}".format(data_type.name)
            tag_reader = reader.get_tag_reader(path, data_type)
            reader.mock_read.configure_mock(
                return_value=SerializedTagWithAggregates(
                    path, data_type, serialized_value
                )
            )
            result = await tag_reader.read_async()
            assert reader.mock_read.call_args_list
            assert value == result.value
            assert data_type == result.data_type

    @pytest.mark.slow
    def test__get_tag_reader__mypy_ensures_correct_type(self):
        code_template = textwrap.dedent("""
            from datetime import datetime
            from nisystemlink.clients.tag import DataType, ITagReader, TagManager

            def validate_type(val: %s) -> None:
                pass

            mgr = TagManager()
            tag_reader = mgr.get_tag_reader("foo", DataType.%s)
            result = tag_reader.read()
            assert result is not None
            validate_type(result.value)

            """)

        # Test successful validation of correct code
        try:
            files = []
            code = {}
            for data_type, (_, value) in self.test_values.items():
                pytype_name = str(type(value).__name__)
                code[data_type.name] = code_template % (pytype_name, data_type.name)
                with tempfile.NamedTemporaryFile(
                    mode="w+", delete=False, prefix=data_type.name + "_", suffix=".py"
                ) as f:
                    files.append(f.name)
                    f.write(code[data_type.name])
            stdout, stderr, exit_code = mypy.api.run(files)
            assert 0 == exit_code, "\n\n".join(
                (stdout, stderr, str(code).replace("\\n", "\n"))
            )
        finally:
            for fname in files:
                os.remove(fname)

        # Test failed validation of incorrect code
        for data_type, (_, value) in self.test_values.items():
            fname = None
            bad_type_name = "bool" if isinstance(value, str) else "str"
            code = code_template % (bad_type_name, data_type.name)
            try:
                with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
                    f.write(code)
                stdout, stderr, exit_code = mypy.api.run([f.name])
                assert 0 != exit_code, "\n\n".join((stdout, stderr, code))
            finally:
                if fname is not None:
                    os.remove(fname)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_itagwriter.py sha256=360ece641c91d4eed20a82691e8ea63efd92a50bbcfef9c370c14d4792d1018f bytes=8401 -->
## FILE: tests/tag/test_itagwriter.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_itagwriter.py`
- sha256: `360ece641c91d4eed20a82691e8ea63efd92a50bbcfef9c370c14d4792d1018f`
- bytes: 8401

````python
import datetime
import os
import tempfile
import textwrap
from unittest import mock

import mypy.api
import pytest
from nisystemlink.clients.tag import DataType, ITagWriter


class TestITagWriter:
    class MockTagWriter(ITagWriter):
        def __init__(self):
            super().__init__()
            self.mock_write = mock.Mock()

        def _write(self, *args, **kwargs):
            return self.mock_write(*args, **kwargs)

        async def _write_async(self, *args, **kwargs):
            return self.mock_write(*args, **kwargs)

    # data_type: (serialized_value, value)
    test_values = {
        DataType.BOOLEAN: ("True", True),
        DataType.DATE_TIME: (
            "2020-01-01T00:22:11.123456Z",
            datetime.datetime(2020, 1, 1, 0, 22, 11, 123456, datetime.timezone.utc),
        ),
        DataType.DOUBLE: ("1.1", 1.1),
        DataType.INT32: ("-1", -1),
        DataType.UINT64: ("2", 2),
        DataType.STRING: ("foo", "foo"),
    }

    def test__get_tag_writer__write_sends_path_and_data_type(self):
        writer = self.MockTagWriter()

        for data_type, (serialized_value, value) in self.test_values.items():
            path = "MyPath.{}".format(data_type.name)
            tag_writer = writer.get_tag_writer(path, data_type)
            tag_writer.write(value)
            writer.mock_write.assert_called_with(
                path, data_type, serialized_value, None
            )

    @pytest.mark.asyncio
    async def test__get_tag_writer__write_async_sends_path_and_data_type(self):
        writer = self.MockTagWriter()

        for data_type, (serialized_value, value) in self.test_values.items():
            path = "MyPath.{}".format(data_type.name)
            tag_writer = writer.get_tag_writer(path, data_type)
            await tag_writer.write_async(value)
            writer.mock_write.assert_called_with(
                path, data_type, serialized_value, None
            )

    @pytest.mark.slow
    def test__get_tag_writer__mypy_ensures_correct_type(self):
        code_template = textwrap.dedent("""
            import datetime
            from nisystemlink.clients.tag import DataType, TagManager

            value = %s

            mgr = TagManager()
            writer = mgr.create_writer(buffer_size=1)
            tag_writer = writer.get_tag_writer("foo", DataType.%s)
            tag_writer.write(value)
            """)

        # Test successful validation of correct code
        try:
            files = []
            code = {}
            for data_type, (_, value) in self.test_values.items():
                code[data_type.name] = code_template % (repr(value), data_type.name)
                with tempfile.NamedTemporaryFile(
                    mode="w+", delete=False, prefix=data_type.name + "_", suffix=".py"
                ) as f:
                    files.append(f.name)
                    f.write(code[data_type.name])
            stdout, stderr, exit_code = mypy.api.run(files)
            assert 0 == exit_code, "\n\n".join(
                (stdout, stderr, str(code).replace("\\n", "\n"))
            )
        finally:
            for fname in files:
                os.remove(fname)

        # Test failed validation of incorrect code
        for data_type, (_, value) in self.test_values.items():
            fname = None
            bad_type_name = "bool" if isinstance(value, str) else "str"
            code = code_template % (bad_type_name, data_type.name)
            try:
                with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
                    f.write(code)
                stdout, stderr, exit_code = mypy.api.run([f.name])
                assert 0 != exit_code, "\n\n".join((stdout, stderr, code))
            finally:
                if fname is not None:
                    os.remove(fname)

    def test__correct_type__validate_type__doesnt_raise(self):
        ITagWriter._validate_type(True, DataType.BOOLEAN)
        ITagWriter._validate_type(datetime.datetime.now(), DataType.DATE_TIME)
        ITagWriter._validate_type(-1.1, DataType.DOUBLE)
        ITagWriter._validate_type(-1, DataType.DOUBLE)  # an int is valid for DOUBLE
        ITagWriter._validate_type(-1, DataType.INT32)
        ITagWriter._validate_type(2**35, DataType.UINT64)
        ITagWriter._validate_type("", DataType.STRING)

    def test__incorrect_type__validate_type__raises(self):
        bool_val = True
        date_val = datetime.datetime.now()
        dbl_val = 1.1
        int_val = -1
        str_val = ""

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.UNKNOWN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.UNKNOWN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.UNKNOWN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(int_val, DataType.UNKNOWN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.UNKNOWN)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.BOOLEAN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.BOOLEAN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(int_val, DataType.BOOLEAN)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.BOOLEAN)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.DATE_TIME)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.DATE_TIME)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(int_val, DataType.DATE_TIME)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.DATE_TIME)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.DOUBLE)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.DOUBLE)
        # Skip int_val: an int is valid for DataType.DOUBLE
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.DOUBLE)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.INT32)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.INT32)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.INT32)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.INT32)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.UINT64)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.UINT64)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.UINT64)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(str_val, DataType.UINT64)

        with pytest.raises(ValueError):
            ITagWriter._validate_type(bool_val, DataType.STRING)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(date_val, DataType.STRING)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(dbl_val, DataType.STRING)
        with pytest.raises(ValueError):
            ITagWriter._validate_type(int_val, DataType.STRING)

    def test__int_out_of_range__validate_type__raises(self):
        with pytest.raises(ValueError) as ex:
            ITagWriter._validate_type(-(2**32 + 1), DataType.INT32)
            assert "range" in ex.message
        with pytest.raises(ValueError) as ex:
            ITagWriter._validate_type(2**32, DataType.INT32)
            assert "range" in ex.message

        with pytest.raises(ValueError) as ex:
            ITagWriter._validate_type(-1, DataType.UINT64)
            assert "range" in ex.message
        with pytest.raises(ValueError) as ex:
            ITagWriter._validate_type(2**64, DataType.UINT64)
            assert "range" in ex.message
````
