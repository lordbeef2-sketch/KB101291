# NI PYTHON API DIGEST: nisystemlink-clients-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nisystemlink-clients-python commit=0bed315df7e0dd210396f3669d42211c96a641d5 -->

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=conftest.py -->
## PYTHON MODULE: conftest.py

### `def pytest_addoption(parser)`

Register command line flags that tell us how to connect to the web server.

    Note that command line flags can also be added to the ``[pytest]`` section of
    ``tox.ini``, in an ``addopts`` setting.
    

### `def pytest_collection_modifyitems(items)`

Modify the collected tests.

### `def cloud_config(pytestconfig)`

Fixture to get a CloudHttpConfiguration for testing.

    This requires the --cloud-api-key command line flag, or else skips the test.
    

### `def server_config(pytestconfig)`

Fixture to get an HttpConfiguration for testing.

    This uses the --web-server-url, --web-server-user, and --web-server-password command
    line options, if any are given. If none of them are given, this will try to get the
    default localhost configuration stored in the local Skyline/HttpConfigurations/
    directory. If that is missing, too, the test is skipped.
    

### `def enterprise_config(pytestconfig)`

Fixture to get a HttpConfiguration for testing Enterprise integration.

    This requires the --enterprise-uri and --enterprise-api-key command line flag, or else skips the test.
    

### `def pydantic_forbid_extra_fields()`

Fixture to disable allowing extra fields in our Pydantic models.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=docs/cleanup.py -->
## PYTHON MODULE: docs/cleanup.py

### MODULE DOCSTRING

Sphinx extension to clean up autodoc output.

### `def _skip_member(app, what, name, obj, skip, options)`

### `def _process_docstring(app, what, name, obj, options, lines)`

### `def modify_systemlink_paths(s: str) -> str`

Modify nisystemlink.* paths in the given string to hide implementation modules.

    Examples:
        >>> # Basic usage
        >>> modify_systemlink_paths("nisystemlink.foo._abc.Abc")
        'nisystemlink.foo.Abc'

        >>> # Modify all paths in the string
        >>> modify_systemlink_paths(" nisystemlink.f._abc.Abc nisystemlink.f._xyz.Xyz ")
        ' nisystemlink.f.Abc nisystemlink.f.Xyz '

        >>> # Don't change _internal or _core paths
        >>> modify_systemlink_paths("nisystemlink.foo._internal._abc.Abc")
        'nisystemlink.foo._internal._abc.Abc'
        >>> modify_systemlink_paths("nisystemlink.foo._core._abc.Abc")
        'nisystemlink.foo._core._abc.Abc'
    

### `def _missing_reference(app, env, node, contnode)`

### `def setup(app)`

Entry point for Sphinx extensions.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/assetmanagement/asset_utilization.py -->
## PYTHON MODULE: examples/assetmanagement/asset_utilization.py

### `def heartbeat_loop()`

Background thread that sends periodic heartbeats.

    This keeps the asset visually marked as "in use" in the SystemLink UI
    (for UI purposes only). Applies only to utilizations that have not been ended.
    The UI requires heartbeats at least every 10 minutes to continue displaying
    the asset as actively utilized.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/feeds/create_feed.py -->
## PYTHON MODULE: examples/feeds/create_feed.py

### MODULE DOCSTRING

Functionality of creating feeds APIs.

- `FEED_NAME = ''`

- `FEED_DESCRIPTION = ''`

- `PLATFORM = Platform.WINDOWS`

- `WORKSPACE_ID = None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/feeds/delete_feed.py -->
## PYTHON MODULE: examples/feeds/delete_feed.py

### MODULE DOCSTRING

Functionality of deleting feed API.

- `FEED_NAME = ''`

- `PLATFORM = Platform.WINDOWS`

- `WORKSPACE_ID = None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/feeds/query_and_upload_feeds.py -->
## PYTHON MODULE: examples/feeds/query_and_upload_feeds.py

### MODULE DOCSTRING

Functionality of uploading & querying feeds APIs.

- `FEED_NAME = ''`

- `PLATFORM = None`

- `FEED_DESCRIPTION = ''`

- `PLATFORM = Platform.WINDOWS`

- `WORKSPACE_ID = None`

- `PACKAGE_PATH = ''`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/file/download_file.py -->
## PYTHON MODULE: examples/file/download_file.py

### MODULE DOCSTRING

Example to download a file from SystemLink.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/file/query_files_linq.py -->
## PYTHON MODULE: examples/file/query_files_linq.py

### MODULE DOCSTRING

Example to query files using LINQ filters in SystemLink.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/file/search_files.py -->
## PYTHON MODULE: examples/file/search_files.py

### MODULE DOCSTRING

Example demonstrating how to search for files using the File API.

Note:
    This example requires Elasticsearch to be configured in the SystemLink cluster.
    If Elasticsearch is not configured, this example will fail with an ApiException.
    For deployments without Elasticsearch, use query_files_linq() instead.


<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/file/upload_file.py -->
## PYTHON MODULE: examples/file/upload_file.py

### MODULE DOCSTRING

Example to upload a file to SystemLink.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/general/disable_cert_verify.py -->
## PYTHON MODULE: examples/general/disable_cert_verify.py

### MODULE DOCSTRING

Example to demonstrate disabling TLS/SSL certificate verification for connections

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/general/pagination_helper.py -->
## PYTHON MODULE: examples/general/pagination_helper.py

### MODULE DOCSTRING

Example demonstrating the paginate helper for iterating through paginated API results.

This example shows how to use the paginate() helper function to automatically
handle continuation tokens when fetching all results from a paginated API.


<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/general/read_minion_id.py -->
## PYTHON MODULE: examples/general/read_minion_id.py

### MODULE DOCSTRING

Example to demonstrate reading the minion ID from the Salt configuration.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/notification/notification.py -->
## PYTHON MODULE: examples/notification/notification.py

### `def create_notification_request_for_alarm(alarm: Alarm, address_group: SmtpAddressGroup, message_template: SmtpMessageTemplate) -> DynamicStrategyRequest`

Creates and returns a dynamic strategy request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/product/products.py -->
## PYTHON MODULE: examples/product/products.py

### `def create_some_products()`

Create two example products on your server.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/tag/subscribe_to_tag_changes.py -->
## PYTHON MODULE: examples/tag/subscribe_to_tag_changes.py

- `SIMULATE_EXTERNAL_TAG_CHANGES = True`

### `def on_tag_changed(tag: TagData, reader: TagValueReader) -> None`

Callback for tag_changed events.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/testmonitor/results.py -->
## PYTHON MODULE: examples/testmonitor/results.py

### `def create_some_results()`

Create two example results on your server.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=examples/testmonitor/steps.py -->
## PYTHON MODULE: examples/testmonitor/steps.py

### `def create_test_result()`

Create example result on your server.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/__init__.py

### MODULE DOCSTRING

Start here with AlarmClient for alarm management.

- `__all__ = ['AlarmClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/_alarm_client.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/_alarm_client.py

### MODULE DOCSTRING

Implementation of Alarm Client

### `class AlarmClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service.
        

#### `def acknowledge_alarms(self, instance_ids: List[str], *, force_clear: bool=False) -> models.AcknowledgeAlarmsResponse`

Acknowledges one or more alarm instances by their instance IDs.

        Args:
            instance_ids: List of instance IDs (unique occurrence identifiers) of the alarms to acknowledge.
                 These are the server-generated IDs returned when creating/updating alarms,
                 not the user-defined alarm_id.
            force_clear: Whether or not the affected alarms should have their clear field set to true.
                         Defaults to False.

        Returns:
            A response containing the instance IDs that were successfully acknowledged,
            the instance IDs that failed, and error details for failures.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        

#### `def create_or_update_alarm(self, request: models.CreateOrUpdateAlarmRequest, *, ignore_conflict: Literal[False]=False) -> str`

#### `def create_or_update_alarm(self, request: models.CreateOrUpdateAlarmRequest, *, ignore_conflict: Literal[True]) -> str | None`

#### `def create_or_update_alarm(self, request: models.CreateOrUpdateAlarmRequest, *, ignore_conflict: bool=False) -> str | None`

Creates or updates an instance, or occurrence, of an alarm.

        Creates or updates an alarm based on the requested transition and the state
        of the current active alarm with the given alarm_id (specified in the request).
        Multiple calls with the same alarm_id will update the same alarm instance.

        Args:
            request: The request containing alarm_id (user-defined identifier),
                    transition details, and other alarm properties.
            ignore_conflict: If True, 409 Conflict errors will be ignored and None will be returned.
                           If False (default), 409 errors will raise an ApiException.
                           Setting this to True is useful for stateless applications that want to
                           attempt state transitions without checking the current alarm state first.

        Returns:
            The instance_id (unique occurrence identifier) of the created or modified alarm.
            Use this ID for operations like get_alarm(), delete_alarm(), or acknowledge.
            Returns None if ignore_conflict is True and a 409 Conflict occurs.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
                A 409 Conflict error occurs when the request does not represent a valid transition
                for an existing alarm, such as attempting to clear an alarm which is already clear,
                or attempting to set an alarm which is already set at the given severity level.
                This error can be suppressed by setting ignore_conflict=True.
        

#### `def _create_or_update_alarm(self, request: models.CreateOrUpdateAlarmRequest) -> str`

Internal implementation of create_or_update_alarm.

#### `def get_alarm(self, instance_id: str) -> models.Alarm`

Gets an alarm by its instance_id.

        Args:
            instance_id: The unique instance ID (occurrence identifier) of the alarm to retrieve.
                This is the server-generated ID returned from create_or_update_alarm(),
                not the user-defined alarm_id.

        Returns:
            The alarm with the specified instance_id.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        

#### `def delete_alarm(self, instance_id: str) -> None`

Deletes an alarm by its instance_id.

        Args:
            instance_id: The unique instance ID (occurrence identifier) of the alarm to delete.
                This is the server-generated ID returned from create_or_update_alarm(),
                not the user-defined alarm_id.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        

#### `def delete_alarms(self, instance_ids: List[str]) -> models.DeleteAlarmsResponse`

Deletes multiple alarm instances by their instance IDs.

        Args:
            instance_ids: List of instance IDs (unique occurrence identifiers) of the alarms to delete.
                 These are the server-generated IDs returned when creating/updating alarms,
                 not the user-defined alarm_id.

        Returns:
            A response containing lists of successfully deleted and failed instance IDs,
            along with error information for failures.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        

#### `def query_alarms(self, request: models.QueryAlarmsWithFilterRequest) -> models.QueryAlarmsWithFilterResponse`

Queries for instances, or occurrences, of alarms using Dynamic LINQ.

        Specifying an empty JSON object in the request body will result in all alarms being returned.

        Args:
            request: The request containing filter information and query options.

        Returns:
            A response containing the list of alarms that match the query, along with
            optional total count and continuation token for pagination.

        Raises:
            ApiException: if unable to communicate with the `/nialarm` Service or provided invalid arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_acknowledge_alarms_response.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_acknowledge_alarms_response.py

### `class AcknowledgeAlarmsResponse(AlarmInstancesPartialSuccess)`

Contains information about which alarms were acknowledged.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_alarm.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_alarm.py

### `class AlarmSeverityLevel(IntEnum)`

Well-known alarm severity levels.

    The service supports custom severity levels greater than 4, but it is generally discouraged.
    The SystemLink Alarm UI only has display strings for severity levels in the range [1, 4].
    

### `class AlarmTransitionType(str, Enum)`

Specifies a type of alarm transition.

### `class AlarmTransition(JsonModel)`

A transition within an instance, or occurrence, of an alarm.

    Alarm transitions record changes to an alarm's clear field as well as an alarm
    increasing or decreasing in severity.
    

### `class Alarm(JsonModel)`

An individual instance, or occurrence, of an alarm.

    The lifecycle of an alarm begins the first time it is triggered and ends when it has been
    both acknowledged and cleared. The service enforces the invariant that there can be at most
    one active=True alarm with the same alarmId.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_alarm_instances_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_alarm_instances_partial_success.py

### `class AlarmInstancesPartialSuccess(JsonModel)`

Base class for partial success responses containing success/failure lists and error information.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_create_or_update_alarm_request.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_create_or_update_alarm_request.py

### `class CreateAlarmTransition(JsonModel)`

Contains information about a transition used to create or update an instance of an alarm.

### `class SetAlarmTransition(CreateAlarmTransition)`

Contains information about a SET transition used to create or update an instance of an alarm.

    This is a convenience class that automatically sets transition_type to SET.
    

#### `def _set_transition_type(self) -> 'SetAlarmTransition'`

### `class ClearAlarmTransition(CreateAlarmTransition)`

Contains information about a CLEAR transition used to clear an instance of an alarm.

    This is a convenience class that automatically sets transition_type to CLEAR
    and severity_level to -1 (CLEAR severity).
    

#### `def _set_clear_defaults(self) -> 'ClearAlarmTransition'`

### `class CreateOrUpdateAlarmRequest(JsonModel)`

Contains information about the alarm to create or update.

    If an alarm is being updated, only alarmId, workspace, and transition are applied.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_delete_alarms_response.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_delete_alarms_response.py

### `class DeleteAlarmsResponse(AlarmInstancesPartialSuccess)`

Contains information about alarms that were deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_query_alarms_request.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_query_alarms_request.py

### `class TransitionInclusionOption(str, Enum)`

Determines which transitions to include in the query results.

### `class AlarmOrderBy(str, Enum)`

The sort order of the returned list of alarms.

### `class QueryAlarmsWithFilterRequest(JsonModel)`

Contains filter information for querying alarms.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/alarm/models/_query_alarms_response.py -->
## PYTHON MODULE: nisystemlink/clients/alarm/models/_query_alarms_response.py

### `class QueryAlarmsWithFilterResponse(WithPaging)`

Contains information about the alarms matched by a query.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/artifact/__init__.py

### MODULE DOCSTRING

Start here with ArtifactClient for artifact management.

- `__all__ = ['ArtifactClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/_artifact_client.py -->
## PYTHON MODULE: nisystemlink/clients/artifact/_artifact_client.py

### MODULE DOCSTRING

Implementation of ArtifactClient

### `def _iter_content_filelike_wrapper(response: Response) -> IteratorFileLike`

### `class ArtifactClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the  Notebook execution Service.
        

#### `def __upload_artifact(self, workspace: str, artifact: BinaryIO) -> models.UploadArtifactResponse`

Uploads an artifact  using multipart/form-data headers to send the file payload in the HTTP body.

        Args:
            workspace: The workspace containing the artifact.
            artifact: The artifact to upload.

        Returns:
            UploadArtifactResponse: The response containing the artifact ID.

        

#### `def upload_artifact(self, workspace: str, artifact: BinaryIO) -> models.UploadArtifactResponse`

Uploads an artifact.

        Args:
            workspace: The workspace containing the artifact.
            artifact: The artifact to upload.

        Returns:
            UploadArtifactResponse: The response containing the artifact ID.

        

#### `def download_artifact(self, id: Path) -> IteratorFileLike`

Downloads an artifact.

        Args:
            id: The ID of the artifact to download.

        Returns:
            A file-like object for reading the artifact content.

        

#### `def delete_artifact(self, id: str) -> None`

Deletes an artifact.

        Args:
            id: The ID of the artifact to delete.

        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/artifact/models/_upload_artifact_response.py -->
## PYTHON MODULE: nisystemlink/clients/artifact/models/_upload_artifact_response.py

### `class UploadArtifactResponse(JsonModel)`

Response for an artifact upload request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/__init__.py

### MODULE DOCSTRING

Start here with AssetManagementClient for asset management.

- `__all__ = ['AssetManagementClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/_asset_management_client.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/_asset_management_client.py

### MODULE DOCSTRING

Implementation of AssetManagementClient.

### `class AssetManagementClient(BaseClient)`

#### `def __init__(self, configuration: HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: If unable to communicate with the asset management Service.
        

#### `def create_assets(self, assets: List[models.CreateAssetRequest]) -> models.CreateAssetsPartialSuccessResponse`

Create Assets.

        Args:
            assets: Array of assets that should be created.

        Returns:
            CreateAssetsPartialSuccessResponse: Array of created assets and array of failed.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        

#### `def create_asset(self, asset: models.CreateAssetRequest) -> models.Asset`

Create a single asset.

        Args:
            asset: The asset to create.

        Returns:
            The created asset.

        Raises:
            ApiException: if the asset could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def __query_assets(self, query: models._QueryAssetsRequest) -> models.QueryAssetsResponse`

Query Assets.

        Args:
            query: Object containing filters to apply when retrieving assets.

        Returns:
            QueryAssetsResponse: Assets Response containing the assets satisfying the query and
            the total count of matching assets.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        

#### `def query_assets(self, query: models.QueryAssetsRequest) -> models.QueryAssetsResponse`

Query Assets.

        Args:
            query: Object containing filters to apply when retrieving assets.

        Returns:
            QueryAssetsResponse: Assets Response containing the assets satisfying the query and
            the total count of matching assets.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid
            arguments.
        

#### `def delete_assets(self, ids: List[str]) -> models.DeleteAssetsResponse`

Delete Assets.

        Args:
            ids: List of IDs of the assets to delete.

        Returns:
            DeleteAssetsResponse: Response containing the IDs of the assets that were deleted.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

#### `def link_files(self, asset_id: str, file_ids: List[str]) -> models.LinkFilesPartialSuccessResponse | None`

Link files to an asset.

        Args:
            asset_id: The ID of the asset to which files should be linked.
            file_ids: The list of file IDs to link.

        Returns:
            None if all link files succeed, otherwise a response containing the IDs of files that were
            successfully linked and those that failed.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

#### `def query_asset_utilization_history(self, request: models.QueryAssetUtilizationHistoryRequest) -> models.AssetUtilizationHistoryResponse`

Query asset utilization history.

        Args:
            request: Object containing filters for asset utilization and assets, including
                    utilization_filter, asset_filter, date range, and pagination options.

        Returns:
            AssetUtilizationHistoryResponse: Response containing the list of asset utilization
            history records that match the query, along with optional continuation token for pagination.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

#### `def start_utilization(self, request: models.StartUtilizationRequest) -> models.StartUtilizationPartialSuccessResponse`

Start asset utilization tracking.

        Args:
            request: Object containing the utilization identifier, minion ID, asset identifications,
                    utilization category, task name, user name, and utilization timestamp.

        Returns:
            StartUtilizationPartialSuccessResponse: Response containing arrays of assets that successfully
            started utilization and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

#### `def __end_utilization(self, request: _UpdateUtilizationRequest) -> models.UpdateUtilizationPartialSuccessResponse`

End asset utilization tracking.

        Args:
            request: The request object containing utilization identifiers and timestamp.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing updated utilization IDs.
        

#### `def end_utilization(self, ids: List[str], timestamp: Optional[datetime]=None) -> models.UpdateUtilizationPartialSuccessResponse`

End asset utilization tracking.

        Args:
            ids: Array of utilization identifiers representing the unique identifier
                of asset utilization history records to end.
            timestamp: The timestamp to use when ending the utilization.
                If not provided, the current server time will be used.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing arrays of utilization IDs that were
            successfully updated and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

#### `def __utilization_heartbeat(self, request: _UpdateUtilizationRequest) -> models.UpdateUtilizationPartialSuccessResponse`

Send utilization heartbeat.

        Args:
            request: The request object containing utilization identifiers and timestamp.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing updated utilization IDs.
        

#### `def utilization_heartbeat(self, ids: List[str], timestamp: Optional[datetime]=None) -> models.UpdateUtilizationPartialSuccessResponse`

Send utilization heartbeat to update asset utilization tracking.

        Args:
            ids: Array of utilization identifiers representing the unique identifier
                of asset utilization history records to update.
            timestamp: The timestamp to use for the heartbeat.
                If not provided, the current server time will be used.

        Returns:
            UpdateUtilizationPartialSuccessResponse: Response containing arrays of utilization IDs that were
            successfully updated and those that failed, along with error information if any failures occurred.

        Raises:
            ApiException: If unable to communicate with the asset management service or if there are invalid arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset.py

### `class Asset(JsonModel)`

Model for an object describing an asset with all of its properties.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_calibration.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_calibration.py

### `class CalibrationStatus(Enum)`

Calibration category the asset belongs to based on the next due calibration date.

### `class TemperatureSensor(JsonModel)`

Temperature sensor information.

### `class SelfCalibration(JsonModel)`

### `class CalibrationMode(Enum)`

Whether SystemLink automatically discovered the calibration data for an asset or if it was manually entered.

### `class ExternalCalibration(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_identification.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_identification.py

### MODULE DOCSTRING

Model for asset identification.

### `class AssetIdentification(JsonModel)`

Model for object containing properties which identify an asset.

    An asset is uniquely identified by a combination of:

    * ``bus_type``
    * ``model_name`` or ``model_number``
    * ``vendor_name`` or ``vendor_number``
    * ``serial_number``
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_location.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_location.py

### `class AssetPresenceStatus(Enum)`

Status of an asset's presence in a system.

### `class SystemConnection(Enum)`

Whether the minion is connected to the server.

    For backward compatibility, APPROVED, UNSUPPORTED, and ACTIVATED are
    treated as DISCONNECTED. CONNECTED_UPDATE_PENDING,
    CONNECTED_UPDATE_SUCCESSFUL, and CONNECTED_UPDATE_FAILED are treated
    as CONNECTED.
    

### `class AssetPresenceWithSystemConnection(JsonModel)`

Asset presence and system connection information.

### `class AssetPresence(JsonModel)`

Model for the presence of an asset.

### `class _AssetLocation(JsonModel)`

Local model for asset location and presence information.

### `class AssetLocation(_AssetLocation)`

Asset location and system connection information.

### `class AssetLocationForCreate(_AssetLocation)`

Asset presence information used during create.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_types.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_types.py

### `class AssetBusType(Enum)`

All supported bus types for an asset.

### `class AssetType(Enum)`

All supported asset types.

### `class AssetDiscoveryType(Enum)`

All discovery types.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_utilization_history_item.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_utilization_history_item.py

### `class AssetUtilizationHistoryItem(JsonModel)`

Model representing an asset utilization history record.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_asset_utilization_history_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_asset_utilization_history_response.py

### `class AssetUtilizationHistoryResponse(WithPaging)`

Response model for asset utilization history query.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_create_asset_request.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_create_asset_request.py

### `class CreateAssetRequest(JsonModel)`

Model for an object describing the properties for creating an asset.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_create_assets_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_create_assets_partial_success_response.py

### `class CreateAssetsPartialSuccessResponse(JsonModel)`

Model for create Assets Partial Success Response.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_delete_assets_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_delete_assets_response.py

### `class DeleteAssetsResponse(JsonModel)`

Model for delete Assets Response containing the ids of the assets which were deleted

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_link_files_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_link_files_partial_success_response.py

### `class LinkFilesPartialSuccessResponse(JsonModel)`

Model for a Link Files Partial Success Response.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_asset_utilization_history_request.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_query_asset_utilization_history_request.py

### `class UtilizationOrderBy(Enum)`

Field by which asset utilization history records can be ordered/sorted.

### `class QueryAssetUtilizationHistoryRequest(WithPaging)`

Model for object containing filters for asset utilization and assets.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_assets_request.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_query_assets_request.py

### `class OrderBy(Enum)`

Field by which assets can be ordered/sorted. If OrderBy is not specified, no sorting will applied.

### `class AssetField(str, Enum)`

Model for an object describing an asset with all of its properties.

### `class QueryAssetsRequest(JsonModel)`

Model for object containing filters to apply when retrieving assets.

### `class _QueryAssetsRequest(JsonModel)`

Model for object containing filters to apply when retrieving assets.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_query_assets_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_query_assets_response.py

### `class QueryAssetsResponse(JsonModel)`

Model for assets Response containing the assets satisfying the query and the total count of matching assets.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_start_utilization_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_start_utilization_partial_success_response.py

### MODULE DOCSTRING

Model for start utilization partial success response.

### `class StartUtilizationPartialSuccessResponse(JsonModel)`

Response model for start utilization operation with partial success support.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_start_utilization_request.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_start_utilization_request.py

### MODULE DOCSTRING

Model for start utilization request.

### `class StartUtilizationRequest(JsonModel)`

Request model for starting asset utilization tracking.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_update_utilization_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_update_utilization_partial_success_response.py

### MODULE DOCSTRING

Model for update utilization partial success response.

### `class UpdateUtilizationPartialSuccessResponse(JsonModel)`

Response model for update utilization operation with partial success support.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/assetmanagement/models/_update_utilization_request.py -->
## PYTHON MODULE: nisystemlink/clients/assetmanagement/models/_update_utilization_request.py

### MODULE DOCSTRING

Model for updating utilization (heartbeat or end).

### `class _UpdateUtilizationRequest(JsonModel)`

Request model for updating utilization (heartbeat or end).

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_error.py -->
## PYTHON MODULE: nisystemlink/clients/core/_api_error.py

### MODULE DOCSTRING

Implementation of ApiError.

### `class ApiError(JsonModel)`

Represents the standard error structure for SystemLink API responses.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_exception.py -->
## PYTHON MODULE: nisystemlink/clients/core/_api_exception.py

### MODULE DOCSTRING

Implementation of ApiException.

### `class ApiException(Exception)`

Represents errors that occur when calling SystemLink APIs.

#### `def __init__(self, message: str | None=None, error: core.ApiError | None=None, http_status_code: int | None=None, inner: Exception | None=None, response_data: Dict[str, Any] | None=None) -> None`

Initialize an exception.

        Args:
            message: The message describing the error.
            error: The error returned by the API.
            http_status_code: The HTTP status code, if this exception was the result of
                an HTTP error.
            inner: The inner exception that caused the error.
            response_data: The full parsed JSON response body, if the server returned
                one. Useful when an error response still contains actionable data.
        

#### `def message(self) -> str | None`

The error message.

#### `def error(self) -> core.ApiError | None`

The error information returned by the SystemLink API, or None if the API did
        not return one or the error occurred trying to call the API.
        

#### `def http_status_code(self) -> int | None`

The HTTP status code, if this exception was the result of an HTTP error.

#### `def inner_exception(self) -> Exception | None`

The exception that caused this failure, if any.

#### `def response_data(self) -> Dict[str, Any] | None`

The full parsed JSON response body returned by the server, or None.

        This is populated for HTTP error responses that include a JSON body.
        It allows callers to recover structured data from error responses — for
        example, a partial-failure response may contain result data alongside the error details.
        

#### `def __str__(self) -> str`

#### `def __eq__(self, other: object) -> bool`

#### `def __hash__(self) -> int`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_api_info.py -->
## PYTHON MODULE: nisystemlink/clients/core/_api_info.py

### `class Operation(JsonModel)`

Represents an operation that can be performed on a data frame.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_cloud_http_configuration.py -->
## PYTHON MODULE: nisystemlink/clients/core/_cloud_http_configuration.py

### MODULE DOCSTRING

Implementation of CloudHttpConfiguration.

### `class CloudHttpConfiguration(core.HttpConfiguration)`

An :class:`HttpConfiguration` specifically for use with SystemLink Cloud.

#### `def __init__(self, api_key: str) -> None`

Initialize a configuration for SystemLink Cloud using API key-based authentication.

        Args:
            api_key: The API key to send with requests.

        Raises:
            ValueError: if ``api_key`` is empty.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_http_configuration.py -->
## PYTHON MODULE: nisystemlink/clients/core/_http_configuration.py

### MODULE DOCSTRING

Implementation of HttpConfiguration.

### `class HttpConfiguration()`

Represents the configuration for accessing a SystemLink service over HTTP.

#### `def __init__(self, server_uri: str, api_key: str | None=None, username: str | None=None, password: str | None=None, cert_path: pathlib.Path | None=None, workspace: str | None=None, verify: bool=True) -> None`

Initialize a configuration.

        If neither ``api_key`` nor ``username`` and ``password`` are set, the
        configuration will use anonymous access, and any API calls that require
        authorization will fail.

        Args:
            server_uri: The scheme, host, and port (if not default) of the web server
                hosting the SystemLink service to connect to. Additional Uri properties
                such as ``urllib.parse.urlparse().path`` and
                ``urllib.parse.urlparse().query`` are ignored.
            api_key: The API key to send with requests.
            username: The name of the user to use when authorization is required.
            password: The user's password to use when authorization is required.
            cert_path: Local path to an SSL certificate file.
            workspace: ID of workspace to use for client operations.
            verify: Verify the security certificate for connection

        Raises:
            ValueError: if ``server_uri`` is missing scheme or host information.
            ValueError: if ``username`` or ``password`` is set, but not both.
        

#### `def verify(self) -> bool`

Verify the security certificate for connection.

#### `def verify(self, value: bool) -> None`

#### `def timeout_milliseconds(self) -> int`

The number of milliseconds before a request times out with an error.

        Changing the timeout will not affect APIs that have already read the
        configuration.
        

#### `def timeout_milliseconds(self, value: int) -> None`

#### `def user_agent(self) -> str | None`

The string to pass the web server as the product name or names making the
        request, or None to use a library-specific default.

        Changing the user-agent will not affect APIs that have already read the
        configuration.
        

#### `def user_agent(self, value: str | None) -> None`

#### `def api_keys(self) -> Dict[str, str] | None`

The available API keys to use for authorization, or None if none were provided.

#### `def server_uri(self) -> str`

The ``urllib.parse.urlparse().scheme``, ``urllib.parse.urlparse().hostname``,
        and ``urllib.parse.urlparse().port`` of the web server hosting the SystemLink
        service to connect to.

        Additional Uri properties such as ``urllib.parse.urlparse().path`` and
        ``urllib.parse.urlparse().query`` are ignored.
        

#### `def username(self) -> str | None`

The username to use for HTTP authentication, or None if none was provided.

#### `def password(self) -> str | None`

The password to use for HTTP authentication, or None if none was provided.

#### `def cert_path(self) -> pathlib.Path | None`

Local path to an SSL certificate file.

#### `def workspace(self) -> str | None`

ID of workspace to use for Client operations.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_http_configuration_manager.py -->
## PYTHON MODULE: nisystemlink/clients/core/_http_configuration_manager.py

### MODULE DOCSTRING

Implementation of HttpConfigurationManager.

### `class HttpConfigurationManager()`

Factory for :class:`HttpConfiguration` objects.

#### `def get_configuration(cls, id: str | None=None, enable_fallbacks: bool | None=True) -> core.HttpConfiguration`

Get the requested or default configuration.

        Args:
            id: The ID of the configuration to find.
            enable_fallbacks: Whether or not to fallback to other known configurations,
                if ``id`` is unavailable.

        Returns:
            The configuration.

        Raises:
            ValueError: if ``id`` is None and ``enable_fallbacks`` is False.
            ApiException: if the specified (or default) configuration is not found.
        

#### `def _fallback(cls) -> core.HttpConfiguration | None`

Attempt to acquire fallback HTTP configurations.

        Returns:
            The best available fallback configuration, or None if no such
            configurations are available.
        

#### `def _read_virtual_configurations(cls) -> Dict[str, core.HttpConfiguration]`

Loads the virtual HTTP configurations.

        Returns:
            A dictionary mapping each loaded configuration ID to its corresponding
            :class:`HttpConfiguration`.
        

#### `def _read_configurations(cls) -> Dict[str, core.HttpConfiguration]`

Discover and loads the HTTP configuration files.

        Returns:
            A dictionary mapping each loaded configuration ID to its corresponding
            :class:`HttpConfiguration`.

        Raises:
            ApiException: if multiple configurations with the same ID are simultaneously
                present.
            ApiException: if an OS or permission error prevents reading the directory
                that contains HTTP configurations.
        

#### `def _read_configuration_file(cls, path: pathlib.Path) -> HttpConfigurationFile | None`

Parse a single SystemLink HTTP configuration file.

        Args:
            path: The path of the file.

        Returns:
            The parsed file, or None if there is no valid configuration present at the
            given path.

        Raises:
            OSError: if an error occurs while accessing the file.
            PermissionError: if the current application does not have permission to
                access the configuration file.
            json.decoder.JSONDecodeError: if the file does not contain valid JSON.
        

#### `def _http_configurations_directory(cls) -> pathlib.Path`

Get the platform-specific path to the HTTP Configurations directory.

        Returns:
            pathlib.Path: The path of the HTTP Configurations directory.
        

#### `def _salt_grains_path(cls) -> pathlib.Path`

Get the SALT grains config file path.

        Returns:
            pathlib.Path: The path of SALT grains config file
        

#### `def _read_system_workspace(cls) -> str | None`

Get the workspace of the connected remote system.

        Reads workspace from `grains` file of SystemLink Client.

        Returns:
            str: Workspace Id of the remote system.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_classproperty_support.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_classproperty_support.py

### MODULE DOCSTRING

Implementation of ClasspropertySupport.

- `_T = TypeVar('_T')`

### `class ClasspropertySupport(abc.ABCMeta)`

Meta class for classes that cannot be subclassed.

#### `def __new__(meta, name: str, bases: Tuple[type, ...], dct: Dict[str, Any]) -> 'ClasspropertySupport'`

#### `def classproperty(cls, f: Callable[[Any], _T]) -> _T`

Make a classproperty.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_http_client.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_http_client.py

### MODULE DOCSTRING

Implementation of HttpClient.

### `class HttpClient()`

Base client for HTTP connections.

#### `def __init__(self, configuration: core.HttpConfiguration) -> None`

#### `def at_uri(self, uri: str) -> '_HttpClientAtUri'`

Get a client interface for which all queries are relative to ``uri``.

#### `def _client(self) -> Client`

#### `def _async_client(self) -> AsyncClient`

### `class _HttpClientAtUri()`

Interface to HttpClient for while all queries are relative to a given uri.

#### `def __init__(self, client: HttpClient, uri: str) -> None`

#### `def as_async(self) -> '_AsyncHttpClientAtUri'`

An async version of the client.

#### `def _request(self, method: str, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Tuple[Any, HttpResponse]`

#### `def get(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Tuple[Any, HttpResponse]`

Perform a GET request.

#### `def head(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Tuple[Any, HttpResponse]`

Perform a HEAD request.

#### `def delete(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Tuple[Any, HttpResponse]`

Perform a DELETE request.

#### `def post(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Tuple[Any, HttpResponse]`

Perform a POST request.

#### `def put(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Tuple[Any, HttpResponse]`

Perform a PUT request.

#### `def patch(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Tuple[Any, HttpResponse]`

Perform a PATCH request.

#### `def base_uri(self) -> str`

### `class _AsyncHttpClientAtUri()`

Interface to HttpClient for while all queries are relative to a given uri.

#### `def __init__(self, client: HttpClient, uri: str) -> None`

#### `async def _request(self, method: str, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Tuple[Any, HttpResponse]`

#### `def get(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a GET request.

#### `def head(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a HEAD request.

#### `def delete(self, uri: str, *, params: Dict[str, str | None] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a DELETE request.

#### `def post(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a POST request.

#### `def put(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a PUT request.

#### `def patch(self, uri: str, *, params: Dict[str, str | None] | None=None, data: Dict[str, Any] | Iterable[Any] | None=None) -> Awaitable[Tuple[Any, HttpResponse]]`

Perform a PATCH request.

#### `def base_uri(self) -> str`

### `def _expand_uri_params(uri: str, params: Dict[str, str | None] | None) -> Tuple[str, Dict[str, str] | None]`

Expand any params in uri with a url-encoded version of the corresponding value in ``params``.

    Any matched params will be removed from params. Any unmatched params will be left
    as-is in the uri.

    For example, uri can be "/tags/{path}" and params can be {"path": "foo/bar"},
    resulting in the uri "/tags/foo%2Fbar" and params={}.
    

### `def _handle_response(response: HttpResponse, method: str, uri: str) -> Any`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_http_configuration_file.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_http_configuration_file.py

### MODULE DOCSTRING

Implementation of HttpConfigurationFile.

### `class HttpConfigurationFile()`

Represents a SystemLink HTTP configuration JSON file.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self) -> None`

#### `def from_json_dict(d: Dict[str, Any]) -> 'HttpConfigurationFile'`

Create from the dictionary format that is stored as JSON in the file.

#### `def id(self) -> str | None`

The ID of this configuration.

#### `def id(self, value: str | None) -> None`

#### `def display_name(self) -> str | None`

A user-friendly display name for this configuration.

#### `def display_name(self, value: str | None) -> None`

#### `def connection_type(self) -> str | None`

The type of connection to use.

#### `def connection_type(self, value: str | None) -> None`

#### `def uri(self) -> str | None`

The URI of the SystemLink server.

#### `def uri(self, value: str | None) -> None`

#### `def api_key(self) -> str | None`

The API key of this client.

#### `def api_key(self, value: str | None) -> None`

#### `def cert_path(self) -> str | None`

The path to the server's HTTPS certificate, relative to the Skyline Certificates directory.

#### `def cert_path(self, value: str | None) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_path_constants.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_path_constants.py

### MODULE DOCSTRING

Implementation of PathConstants.

### `class PathConstants()`

Provides file and directory paths for the SystemLink client APIs.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self) -> None`

#### `def application_data_directory(self) -> pathlib.Path`

Get the platform-specific path to the common NI Application Data directory.

        Returns:
            The platform-specific path to the common NI Application Data directory.
        

#### `def salt_data_directory(self) -> pathlib.Path`

Get the platform-specific path to the salt minion Data directory.

        Returns:
            The platform-specific path to the salt minion Data directory.
        

#### `def _windows_programdata_directory(cls) -> pathlib.Path`

Get the path of Windows PROGRAMDATA directory.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.

        Returns:
            pathlib.Path: Windows PROGRAMDATA directory path.
        

#### `def _windows_application_data_directory(cls) -> pathlib.Path`

Get the NI Application Data directory on Windows.

        Returns:
            pathlib.Path: The NI Application Data directory on Windows.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.
        

#### `def _windows_salt_data_directory(cls) -> pathlib.Path`

Get the salt minion Data directory on Windows.

        Returns:
            pathlib.Path: The salt minion Data directory on Windows.

        Raises:
            RuntimeError: if this method is called on a non-Windows system.
            RuntimeError: if the ProgramData folder cannot be found.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_timestamp_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_timestamp_utilities.py

### MODULE DOCSTRING

Implementation of TimestampUtilities.

### `class TimestampUtilities()`

Provides utilities for reading and writing timestamps as strings.

    Clients do not typically need to call methods on this class.
    

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self) -> None`

#### `def datetime_to_str(cls, value: datetime.datetime) -> str`

Convert the given ``datetime.datetime`` into a string timestamp in the standard format used in SystemLink.

        Args:
            value: The date and time to convert.

        Returns:
            The string representation of the timestamp.
        

#### `def str_to_datetime(cls, timestamp: str) -> datetime.datetime`

Attempt to parse a SystemLink-formatted timestamp string into a ``datetime.datetime``.

        Args:
            timestamp: The timestamp to parse, in the standard format used in
                SystemLink.

        Returns:
            The parsed datetime.

        Raises:
            ValueError: if the timestamp format is not as expected
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_internal/_winpaths.py -->
## PYTHON MODULE: nisystemlink/clients/core/_internal/_winpaths.py

- `LICENSE = '\nThe MIT License (MIT)\n\nCopyright (c) 2014 Michael Kropat\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in\nall copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\nTHE SOFTWARE.\n'`

### `class GUID(ctypes.Structure)`

#### `def __init__(self, uuid_)`

### `class FOLDERID()`

### `class UserHandle()`

### `class PathNotFoundException(Exception)`

### `def get_path(folderid, user_handle=UserHandle.common)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_jupyter_http_configuration.py -->
## PYTHON MODULE: nisystemlink/clients/core/_jupyter_http_configuration.py

### MODULE DOCSTRING

Implementation of JupyterHttpConfiguration.

### `class JupyterHttpConfiguration(core.HttpConfiguration)`

An :class:`HttpConfiguration` for Jupyter notebooks running in a SystemLink environment.

#### `def __init__(self) -> None`

Initialize a configuration for SystemLink using API key-based
        authentication provided through environment variables.

        Raises:
            KeyError: if the expected environment variables are not set.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_base_client.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_base_client.py

### `def _handle_http_status(response: Response) -> Response | None`

Checks an HTTP response's status code and raises an exception if necessary.

### `class _JsonModelConverter(converters.Factory)`

A converter that converts between JSON and Pydantic models.

#### `def __init__(self) -> None`

#### `def create_request_body_converter(self, _class: Type, _: commands.RequestDefinition) -> Callable[[JsonModel], Dict] | None`

#### `def create_response_body_converter(self, _class: Type, _: commands.RequestDefinition) -> Callable[[Response], Any] | None`

### `class BaseClient(Consumer)`

Base class for SystemLink clients, built on top of `Uplink <https://github.com/prkumar/uplink>`_.

#### `def __init__(self, configuration: core.HttpConfiguration, base_path: str='')`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about how to connect.
            base_path: The base path for all API calls.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_file_like_response.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_file_like_response.py

### `def file_like_response_handler(response: Response) -> IteratorFileLike`

Response handler for File-Like content.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_json_model.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_json_model.py

### `def _camelcase(s: str) -> str`

Convert a snake case string to camelCase.

### `def _validation_aliases(s: str) -> str | AliasChoices`

Accept both Python snake_case and wire-format camelCase inputs.

### `class JsonModel(BaseModel)`

Base class for models that are serialized to and from JSON.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_methods.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_methods.py

### MODULE DOCSTRING

Wrappers around uplink HTTP decorators with proper type annotations.

- `F = TypeVar('F', bound=Callable[..., Any])`

### `def get(path: str, args: Sequence[Any] | None=None) -> Callable[[F], F]`

Annotation for a GET request.

### `def post(path: str, args: Sequence[Any] | None=None, return_key: str | Tuple[str, ...] | None=None, content_type: str | None=None) -> Callable[[F], F]`

Annotation for a POST request with a JSON request body. If args is not
    specified, defaults to a single argument that represents the request body.
    

### `def put(path: str, args: Sequence[Any] | None=None) -> Callable[[F], F]`

Annotation for a PUT request with a JSON request body. If args is not
    specified, defaults to a single argument that represents the request body.
    

### `def patch(path: str, args: Sequence[Any] | None=None) -> Callable[[F], F]`

Annotation for a PATCH request with a JSON request body.

### `def delete(path: str, args: Sequence[Any] | None=None) -> Callable[[F], F]`

Annotation for a DELETE request.

### `def response_handler(handler: Any, requires_consumer: bool | None=False) -> Callable[[F], F]`

Annotation for creating custom response handlers.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_multipart_retry.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_multipart_retry.py

### MODULE DOCSTRING

Helpers for multipart requests that need retry-safe stream handling.

The decorator exported by this module is intended for multipart requests that may
be retried by Uplink. It preserves the caller's stream position on the initial
send, rewinds seekable multipart parts only on retry attempts, and aborts the
retry if any part cannot be rewound.

When a retry is aborted because a part cannot be rewound, the original response
or exception that triggered the retry is surfaced back through Uplink's normal
response and error handling pipeline instead of sending a malformed follow-up
request.


- `F = TypeVar('F', bound=Callable[..., Any])`

### `class _RewindResult(Enum)`

### `def _rewind_retryable_part(part: object) -> _RewindResult`

Rewind the first seekable multipart payload contained in ``part``.

    Returns ``_RewindResult.REWOUND`` when a multipart payload was successfully
    rewound to the start of the stream. Returns
    ``_RewindResult.FAILED`` when a stream payload appears to need rewinding but
    rejects it. Returns ``_RewindResult.NOT_NEEDED`` when the part contains no
    stream payload that requires rewinding, such as simple string fields.
    

### `def _get_saved_retry_action(response: Response | None, exception_info: tuple[type[BaseException], BaseException, Any] | None) -> Any`

Return the original retry-triggering failure as an Uplink transition.

### `class _RetryableMultipartRequestTemplate(RequestTemplate)`

Track multipart retry state and rewind streams only for retry sends.

    The first request attempt is left untouched so callers can intentionally
    provide streams positioned away from offset 0. On later attempts, each file
    part must be rewound to the beginning before the request is sent again.

    If rewinding fails for any part, the retry is cancelled and the original
    response or exception that caused the retry is returned to Uplink so normal
    error handling can surface it to the caller.
    

#### `def __init__(self) -> None`

#### `def _clear_request_state(self, request_id: int) -> None`

#### `def before_request(self, request: tuple[str, str, dict[str, Any]]) -> Any`

#### `def after_response(self, request: tuple[str, str, dict[str, Any]], response: Response) -> None`

#### `def after_exception(self, request: tuple[str, str, dict[str, Any]], exc_type: type[BaseException], exc_val: BaseException, exc_tb: Any) -> None`

### `class _RetryableMultipartCleanupTemplate(RequestTemplate)`

#### `def __init__(self, retry_template: _RetryableMultipartRequestTemplate) -> None`

#### `def after_response(self, request: tuple[str, str, dict[str, Any]], response: Response) -> None`

#### `def after_exception(self, request: tuple[str, str, dict[str, Any]], exc_type: type[BaseException], exc_val: BaseException, exc_tb: Any) -> None`

### `class _RetryableMultipartRequest(decorators.MethodAnnotation)`

#### `def modify_request(self, request_builder: Any) -> None`

### `def retryable_multipart_request() -> Callable[[F], F]`

Create a decorator for multipart requests with retry-safe stream handling.

    Behavior:
    - The initial send preserves the caller-provided stream position.
        - Retry attempts rewind seekable multipart payloads back to offset 0.
        - Multipart fields that do not contain streams, such as simple strings, are
            left alone and do not block retries.
    - If a retry attempt cannot rewind a payload, the retry is cancelled and the
      original retry-triggering response or exception is surfaced.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/_uplink/_with_paging.py -->
## PYTHON MODULE: nisystemlink/clients/core/_uplink/_with_paging.py

### `class WithPaging(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_iterator_file_like.py -->
## PYTHON MODULE: nisystemlink/clients/core/helpers/_iterator_file_like.py

### `class IteratorFileLike()`

A file-like object adapter that wraps a python iterator, providing a way to
    read from the iterator as if it was a file.
    

#### `def __init__(self, iterator: Iterator[Any])`

#### `def read(self, size: int=-1) -> bytes`

Read at most `size` bytes from the file-like object. If `size` is not
        specified or is negative, read until the iterator is exhausted and
        returns all bytes or characters read.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_minion_id.py -->
## PYTHON MODULE: nisystemlink/clients/core/helpers/_minion_id.py

### MODULE DOCSTRING

Helper function to get minion ID from Salt configuration.

### `def read_minion_id() -> str | None`

Read the minion ID from the Salt configuration.

    Returns:
        str | None: The minion ID content if the file exists, None otherwise.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_pagination.py -->
## PYTHON MODULE: nisystemlink/clients/core/helpers/_pagination.py

### `def paginate(fetch_function: Callable[..., WithPaging], items_field: str, **fetch_kwargs: Any) -> Generator[Any, None, None]`

Generate items from paginated API responses using continuation tokens.

    This helper function provides a convenient way to iterate over all items
    from a paginated API endpoint that uses continuation tokens. It automatically
    handles fetching subsequent pages until all items are retrieved.

    Args:
        fetch_function: The API function to call to fetch each page of items.
            Must accept a ``continuation_token`` parameter and return a response
            that derives from ``WithPaging``.
        items_field: The name of the field in the response object that contains
            the list of items to yield.
        **fetch_kwargs: Additional keyword arguments to pass to the fetch function
            on every call (e.g., filters, take limits, etc.).

    Yields:
        Individual items from each page of results.

    Note:
        The fetch function will be called with the `continuation_token` parameter
        set to `None` on the first call, then with each subsequent token until
        the response contains a `None` continuation token.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/core/helpers/_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/core/helpers/_partial_success.py

- `_ONE_OR_MORE_ERRORS_OCCURRED_NAME = 'Skyline.OneOrMoreErrorsOccurred'`

- `_ONE_OR_MORE_ERRORS_OCCURRED_CODE = -251041`

### `def _unwrap_single_inner_error(error: core.ApiError | None) -> core.ApiError | None`

### `def unwrap_single_item_partial_success(*, response: Any | None, items: Sequence[_ItemT] | None, failed: Sequence[Any] | None, error: core.ApiError | None, failure_message: str, empty_message: str) -> _ItemT`

Return the first successful item from a partial-success response.

    Raises:
        ApiException: if the response reports a failure or contains no successful item.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/__init__.py

### MODULE DOCSTRING

Start here with DataFrameClient for dataframe operations.

- `__all__ = ['DataFrameClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/_data_frame_client.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/_data_frame_client.py

### MODULE DOCSTRING

Implementation of DataFrameClient.

### `class DataFrameClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        

#### `def api_info(self) -> models.ApiInfo`

Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        

#### `def list_tables(self, take: int | None=None, id: List[str] | None=None, order_by: models.OrderBy | None=None, order_by_descending: bool | None=None, continuation_token: str | None=None, workspace: List[str] | None=None) -> models.PagedTables`

Lists available tables on the SystemLink DataFrame service.

        Args:
            take: Limits the returned list to the specified number of results. Defaults to 1000.
            id: List of table IDs to filter by.
            order_by: The sort order of the returned list of tables.
            order_by_descending: Whether to sort descending instead of ascending. Defaults to false.
            continuation_token: The token used to paginate results.
            workspace: List of workspace IDs to filter by.

        Returns:
            The list of tables with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def create_table(self, table: models.CreateTableRequest) -> str`

Create a new table with the provided metadata and column definitions.

        Args:
            table: The request to create the table.

        Returns:
            The ID of the newly created table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def query_tables(self, query: models.QueryTablesRequest) -> models.PagedTables`

Queries available tables on the SystemLink DataFrame service and returns their metadata.

        Args:
            query: The request to query tables.

        Returns:
            The list of tables with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def get_table_metadata(self, id: str) -> models.TableMetadata`

Retrieves the metadata and column information for a single table identified by its ID.

        Args:
            id (str): Unique ID of a data table.

        Returns:
            The metadata for the table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def modify_table(self, id: str, update: models.ModifyTableRequest) -> None`

Modify properties of a table or its columns.

        Args:
            id: Unique ID of a data table.
            update: The metadata to update.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def delete_table(self, id: str) -> None`

Deletes a table.

        Args:
            id (str): Unique ID of a data table.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def delete_tables(self, ids: List[str]) -> models.DeleteTablesPartialSuccess | None`

Deletes multiple tables.

        Args:
            ids (List[str]): List of unique IDs of data tables.

        Returns:
            A partial success if any tables failed to delete, or None if all
            tables were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def modify_tables(self, updates: models.ModifyTablesRequest) -> models.ModifyTablesPartialSuccess | None`

Modify the properties associated with the tables identified by their IDs.

        Args:
            updates: The table modifications to apply.

        Returns:
            A partial success if any tables failed to be modified, or None if all
            tables were modified successfully.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def get_table_data(self, id: str, columns: List[str] | None=None, order_by: List[str] | None=None, order_by_descending: bool | None=None, take: int | None=None, continuation_token: str | None=None) -> models.PagedTableRows`

Reads raw data from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            columns: Columns to include in the response. Data will be returned in the same order as
                the columns. If not specified, all columns are returned.
            order_by: List of columns to sort by. Multiple columns may be specified to order rows
                that have the same value for prior columns. The columns used for ordering do not
                need to be included in the columns list, in which case they are not returned. If
                not specified, then the order in which results are returned is undefined.
            order_by_descending: Whether to sort descending instead of ascending. Defaults to false.
            take: Limits the returned list to the specified number of results. Defaults to 500.
            continuation_token: The token used to paginate results.

        Returns:
            The table data and total number of rows with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def _append_table_data_json(self, id: str, data: models.AppendTableDataRequest) -> None`

Internal uplink-implemented JSON append call.

#### `def _append_table_data_arrow(self, id: str, data: Iterable[bytes], end_of_data: bool | None=None) -> None`

Internal uplink-implemented Arrow (binary) append call.

#### `def append_table_data(self, id: str, data: Union[models.AppendTableDataRequest, models.DataFrame, 'pa.RecordBatch', Iterable['pa.RecordBatch']] | None, *, end_of_data: bool | None=None) -> None`

Appends one or more rows of data to the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            data: The data to append.

                Supported forms:

                * ``AppendTableDataRequest``: Sent as-is via JSON; ``end_of_data`` must be ``None``.
                * ``DataFrame`` (service model): Wrapped into an
                  ``AppendTableDataRequest`` (``end_of_data`` optional) and sent as JSON.
                * Single ``pyarrow.RecordBatch``: Treated the same as an iterable containing one
                  batch and streamed as Arrow IPC. ``end_of_data`` (if provided) is sent as a
                  query parameter.
                * ``Iterable[pyarrow.RecordBatch]``: Streamed as Arrow IPC. ``end_of_data`` (if
                  provided) is sent as a query parameter. If the iterator yields no batches, it is
                  treated as ``None`` and requires ``end_of_data``.
                * ``None``: ``end_of_data`` must be provided; sends JSON containing only the
                  ``endOfData`` flag (useful for closing a table without appending rows).
            end_of_data: Whether additional rows may be appended in future requests. Required when
                ``data`` is ``None`` or the RecordBatch iterator is empty; must be omitted when
                passing an ``AppendTableDataRequest`` (include it inside that model instead).

        Raises:
            ValueError: If parameter constraints are violated.
            ApiException: If unable to communicate with the DataFrame Service or an
                invalid argument is provided.
        

#### `def query_table_data(self, id: str, query: models.QueryTableDataRequest) -> models.PagedTableRows`

Reads rows of data that match a filter from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering and sorting to apply when reading data.

        Returns:
            The table data and total number of rows with a continuation token.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def query_decimated_data(self, id: str, query: models.QueryDecimatedDataRequest) -> models.TableRows`

Reads decimated rows of data from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering and decimation options to apply when reading data.

        Returns:
            The decimated table data.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

#### `def _iter_content_filelike_wrapper(response: Response) -> IteratorFileLike`

#### `def export_table_data(self, id: str, query: models.ExportTableDataRequest) -> IteratorFileLike`

Exports rows of data that match a filter from the table identified by its ID.

        Args:
            id: Unique ID of a data table.
            query: The filtering, sorting, and export format to apply when exporting data.

        Returns:
            A file-like object for reading the exported data.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service
                or provided an invalid argument.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_api_info.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_api_info.py

### `class OperationsV1(JsonModel)`

The operations available in the routes provided by the v1 HTTP API.

### `class ApiInfo(JsonModel)`

Information about the available API operations.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_append_table_data_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_append_table_data_request.py

### `class AppendTableDataRequest(JsonModel)`

Contains the rows to append and optional flags. The ``frame`` field is
    required unless ``endOfData`` is true.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_column.py

### `class Column(JsonModel)`

Defines a single column in a table.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_filter.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_column_filter.py

### `class FilterOperation(str, Enum)`

Represents the different operations that can be used in a filter.

### `class ColumnFilter(JsonModel)`

A filter to apply to the table data.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_order_by.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_column_order_by.py

### `class ColumnOrderBy(JsonModel)`

Specifies a column to order by and the ordering direction.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_column_type.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_column_type.py

### `class ColumnType(str, Enum)`

Represents the different column types for a table column.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_create_table_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_create_table_request.py

### `class CreateTableRequest(JsonModel)`

Contains information needed to create a table, including its properties and column definitions.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_data_frame.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_data_frame.py

### `class DataFrame(JsonModel)`

Data read from or to be written to a table.

    Values may be ``None`` (if the column is of type ``NULLABLE``) or encoded as
    a string in a format according to each column's datatype:

    * BOOL: One of ``"true"`` or ``"false"``, case-insensitive.
    * INT32: Any integer number in the range [-2147483648, 2147483647],
      surrounded by quotes.
    * INT64: Any integer number in the range [-9223372036854775808,
      9223372036854775807], surrounded by quotes.
    * FLOAT32: A decimal number using a period for the decimal point, optionally
      in scientific notation, in the range [-3.40282347E+38, 3.40282347E+38],
      surrounded by quotes. Not all values within the range can be represented
      with 32 bits. To preserve the exact binary encoding of the value when
      converting to a string, clients should serialize 9 digits after the
      decimal. Instead of a number, the value may be ``"NaN"`` (not a number),
      ``"Infinity"`` (positive infinity), or ``"-Infinity"`` (negative
      infinity), case-sensitive.
    * FLOAT64: A decimal number using a period for the decimal point, optionally
      in scientific notation, in the range [-1.7976931348623157E+308,
      1.7976931348623157E+308], surrounded by quotes. Not all values within the
      range can be represented with 64 bits. To preserve the exact binary
      encoding of the value when converting to a string, clients should
      serialize 17 digits after the decimal. Instead of a number, the value may
      be ``"NaN"`` (not a number), ``"Infinity"`` (positive infinity), or
      ``"-Infinity"`` (negative infinity), case-sensitive.
    * STRING: Any quoted string.
    * TIMESTAMP: A date and time with millisecond precision in ISO-8601 format
      and time zone. For example: ``"2022-08-19T16:17:30.123Z"``. If a time zone
      is not provided, UTC is assumed. If a time zone other than UTC is
      provided, the value will be converted to UTC. If more than three digits of
      fractional seconds are provided, the time will be truncated to three
      digits (i.e. milliseconds).

    The format is the same as a serialized Pandas DataFrame with orient="split"
    and index=False. See
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html.

    When providing a DataFrame for appending rows, any of the table's columns
    not specified will receive a value of ``None``. If any such columns aren't
    nullable, an error will be returned. If the entire columns property is left
    out, each row is assumed to contain all columns in the order specified when
    the table was created.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_data_type.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_data_type.py

### `class DataType(str, Enum)`

Represents the different data types for a table column.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_delete_tables_partial_success.py

### `class DeleteTablesPartialSuccess(JsonModel)`

The result of deleting multiple tables when one or more tables could not be deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_export_table_data_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_export_table_data_request.py

### `class ExportFormat(str, Enum)`

The format of the exported data.

### `class ExportTableDataRequest(JsonModel)`

Specifies the parameters for a data export with ordering and filtering.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_table_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_modify_table_request.py

### `class ColumnMetadataPatch(JsonModel)`

Specifies column properties to add, modify, or delete when editing table metadata.

### `class ModifyTableRequest(JsonModel)`

Contains the metadata properties to modify. Values not included will remain unchanged.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_modify_tables_partial_success.py

### `class ModifyTablesPartialSuccess(JsonModel)`

The result of modifying multiple tables when one or more tables could not be modified.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_modify_tables_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_modify_tables_request.py

### `class TableMetadataModification(JsonModel)`

Contains the metadata properties to modify. Values not included in the
    request or included with a ``None`` value will remain unchanged.
    

### `class ModifyTablesRequest(JsonModel)`

Contains one or more table modifications to apply.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_paged_table_rows.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_paged_table_rows.py

### `class PagedTableRows(WithPaging)`

Contains the result of a query for rows of data.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_paged_tables.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_paged_tables.py

### `class PagedTables(WithPaging)`

The response for a table query containing the matched tables.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_decimated_data_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_query_decimated_data_request.py

### `class DecimationMethod(str, Enum)`

Represents the different methods that can be used to decimate data.

### `class DecimationOptions(JsonModel)`

Contains the parameters to use for data decimation.

### `class QueryDecimatedDataRequest(QueryTableDataBase)`

Specifies the columns, filters and decimation parameters for a query.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_table_data_base.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_query_table_data_base.py

### `class QueryTableDataBase(JsonModel)`

Contains the common set of options when querying table data.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_table_data_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_query_table_data_request.py

### `class QueryTableDataRequest(QueryTableDataBase, WithPaging)`

Contains the filtering and sorting options to use when querying table data.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_query_tables_request.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_query_tables_request.py

### `class QueryTablesRequest(WithPaging)`

Request parameters for querying tables.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_table_metadata.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_table_metadata.py

### `class TableMetadata(JsonModel)`

Contains information about a table, including its properties and column definitions.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/dataframe/models/_table_rows.py -->
## PYTHON MODULE: nisystemlink/clients/dataframe/models/_table_rows.py

### `class TableRows(JsonModel)`

Contains the result of a query for rows of decimated data.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/__init__.py

### MODULE DOCSTRING

Start here with FeedsClient for feed management.

- `__all__ = ['FeedsClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/_feeds_client.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/_feeds_client.py

### MODULE DOCSTRING

Implementation of SystemLink Feeds Client.

### `class FeedsClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def create_feed(self, feed: models.CreateFeedRequest) -> models.Feed`

Create a new feed with the provided feed details.

        Args:
            feeds (models.CreateFeedsRequest): Request to create the feed.

        Returns:
            models.Feed: Details of the created feed.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def __query_feeds(self, platform: str | None=None, workspace: str | None=None) -> models.QueryFeedsResponse`

Lists available feeds for the Platform `platform` under the Workspace `workspace`.

        Args:
            platform (str | None): Information about system platform. Defaults to None.
            workspace (str | None): Workspace id. Defaults to None.

        Returns:
            models.QueryFeedsResponse: List of feeds.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def query_feeds(self, platform: models.Platform | None=None, workspace: str | None=None) -> List[models.Feed]`

Lists available feeds for the Platform `platform` under the Workspace `workspace`.

        Args:
            platform (models.Platform | None): Information about system platform.
                Defaults to None.
            workspace (str | None): Workspace id. Defaults to None.

        Returns:
            List[models.Feed]: List of feeds.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def __upload_package(self, feed_id: str, package: Part, overwrite: Query=False) -> models.Package`

Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package (Part): Package file to be uploaded.
            overwrite (Query): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def upload_package(self, feed_id: str, package_file_path: str, overwrite: bool=False) -> models.Package`

Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package_file_path (str): File path of the package to be uploaded.
            overwrite (bool): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
            OSError: if the file does not exist or cannot be opened.
        

#### `def upload_package_content(self, feed_id: str, package: BinaryIO, overwrite: bool=False) -> models.Package`

Upload package to SystemLink feed.

        Args:
            feed_id (str): ID of the feed.
            package (BinaryIO): Package file to be uploaded.
            overwrite (bool): Set to True, to overwrite the package if it already exists.
                Defaults to False.

        Returns:
            models.Package: Uploaded package information.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

#### `def delete_feed(self, id: str) -> None`

Delete feed and its packages.

        Args:
            id (str): ID of the feed to be deleted.

        Returns:
            None.

        Raises:
            ApiException: if unable to communicate with the Feeds Service.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_create_feed.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/models/_create_feed.py

### `class CreateFeedRequest(JsonModel)`

Create Feed Request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_feed.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/models/_feed.py

### `class Feed(JsonModel)`

Feed model.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_package.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/models/_package.py

### `class PackageMetadata(JsonModel)`

Package Meta data.

### `class Package(JsonModel)`

Package model.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_platform.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/models/_platform.py

### `class Platform(Enum)`

Platform.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/models/_query_feeds.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/models/_query_feeds.py

### `class QueryFeedsResponse(JsonModel)`

Query Feeds response.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/feeds/utilities/_get_feed_details.py -->
## PYTHON MODULE: nisystemlink/clients/feeds/utilities/_get_feed_details.py

### MODULE DOCSTRING

Utilities for getting feed details.

### `def get_feed_by_name(feeds: List[Feed], name: str) -> Feed | None`

Get feed information from the list of feeds using `name`.

    Args:
        feeds (List[Feed]): List of feeds.
        name (str): Feed name.

    Returns:
        Feed | None: Feed information.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/file/__init__.py

### MODULE DOCSTRING

Start here with FileClient for file operations.

- `__all__ = ['FileClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/_file_client.py -->
## PYTHON MODULE: nisystemlink/clients/file/_file_client.py

### MODULE DOCSTRING

Implementation of FileClient.

### `def _file_uri_response_handler(response: Response) -> str`

Response handler for File URI response. Extracts ID from URI.

### `class FileClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def api_info(self) -> models.V1Operations`

Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def __get_files(self, skip: int=0, take: int=0, order_by: str | None=None, order_by_descending: str | None='false', ids: str | None=None) -> models.FileQueryResponse`

Lists available files on the SystemLink File service.
        Use the skip and take parameters to return paged responses.
        The orderBy and orderByDescending fields can be used to manage sorting the list by metadata objects.

        Args:
            skip: How many files to skip in the result when paging. Defaults to 0.
            take: How many files to return in the result, or 0 to use a default defined by the service.
              Defaults to 0.
            order_by: The name of the metadata key to sort by. Defaults to None.
            order_by_descending: The elements in the list are sorted ascending if "false"
              and descending if "true". Defaults to "false".
            ids: Comma-separated list of file IDs to search by. Defaults to None.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def get_files(self, skip: int=0, take: int=0, order_by: models.FileQueryOrderBy | None=None, order_by_descending: bool | None=False, ids: List[str] | None=None) -> models.FileQueryResponse`

Lists available files on the SystemLink File service.
        Use the skip and take parameters to return paged responses.
        The orderBy and orderByDescending fields can be used to manage sorting the list by metadata objects.

        Args:
            skip: How many files to skip in the result when paging. Defaults to 0.
            take: How many files to return in the result, or 0 to use a default defined by the service.
            Defaults to 0.
            order_by: The name of the metadata key to sort by. Defaults to None.
            order_by_descending: The elements in the list are sorted ascending if False
            and descending if True. Defaults to False.
            ids: List of file IDs to search by. Defaults to None.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def query_files_linq(self, query: models.FileLinqQueryRequest) -> models.FileLinqQueryResponse`

Queries file using LINQ filters.

        Args:
            query: The LINQ query request containing the following parameters:

                - **filter** (:class:`str`, optional): The filter criteria for files. Consists of a
                  string of queries composed using AND/OR operators. String values and date strings
                  need to be enclosed in double quotes. Parentheses can be used around filters to
                  better define the order of operations.

                  Filter syntax: ``[property name][operator][operand] and [property name][operator][operand]``

                  Operators:

                  - Equals: ``x = y``
                  - Not equal: ``x != y``
                  - Greater than: ``x > y``
                  - Greater than or equal: ``x >= y``
                  - Less than: ``x < y``
                  - Less than or equal: ``x <= y``
                  - Logical AND: ``x and y`` or ``x && y``
                  - Logical OR: ``x or y`` or ``x || y``
                  - Contains: ``x.Contains(y)`` — checks if a list contains an element
                  - Not Contains: ``!x.Contains(y)`` — checks if a list does not contain an element

                  Valid file properties for filtering:

                  - ``created``: ISO timestamp string (e.g. ``"2023-01-01T08:00:00.000Z"``)
                  - ``updated``: ISO timestamp string (e.g. ``"2023-01-01T08:00:00.000Z"``)
                  - ``extension``: File extension (e.g. ``png``, ``txt``, ``pdf``)
                  - ``size``: File size in bytes (e.g. ``1024``)
                  - ``userId``: User ID that created the file (e.g. ``"8abc4b87-07d4-4f84-b54f-48eec89b07d4"``)
                  - ``properties``: File properties (e.g. ``properties['x'] = 'y'``)
                  - ``workspace``: The workspace of the files (e.g. ``"88974b87-07d4-4f84-b54f-48eec89b11ed"``)

                  Example::

                      '(name = "myfile.txt" OR extension = "png")'
                      ' and (DateTime(created) >'
                      ' DateTime.parse("2023-01-01T08:00:00.000Z"))'
                      ' and (size < 1024)'

                - **order_by** (:class:`~nisystemlink.clients.file.models.FileLinqQueryOrderBy`, optional):
                  The file property to order results by. One of ``created``, ``updated``,
                  ``extension``, ``size``, or ``workspace``. Defaults to ``updated``.

                - **order_by_descending** (:class:`bool`, optional): Whether to return the files in
                  descending order. Defaults to ``True``.

                - **skip** (:class:`int`, optional): How many files to skip in the result when paging.
                  For example, a list of 100 files with a skip value of 50 will return entries
                  starting from the 51st file. Defaults to ``0``.

                - **take** (:class:`int`, optional): Maximum number of files to return.
                  Defaults to ``1000``.

        Returns:
            File Query Response

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def search_files(self, request: models.SearchFilesRequest) -> models.SearchFilesResponse`

Search for files based on filter criteria.

        Note:
            This endpoint requires Elasticsearch to be configured in the SystemLink cluster.
            If Elasticsearch is not configured, this method will fail with an ApiException.
            For deployments without Elasticsearch, use `query_files_linq()` instead.
            You can call `api_info()` to check if the `search_files` operation is available
            in your deployment.

        Args:
            request: The search request containing filter, pagination, and sorting parameters.

                - **filter** (:class:`str`, optional): The filter criteria for files using Lucene
                  query syntax. The default search field is the file name. All searches are
                  case-insensitive.

                  Filter syntax: ``[property name][operator][operand] AND [property name][operator][operand]``

                  Operators:

                  - Logical AND: ``AND``. Example: ``Name: "name" AND Extension: "json"``
                  - Logical OR: ``OR``. Example: ``Name: "name" OR Extension: "json"``
                  - Negation: ``NOT``. Example: ``Name: (NOT MyFile)``
                  - Wildcard: ``*`` — matches any sequence of characters. Example: ``Name: "file*"``
                  - Exists: ``_exists_`` — matches files where a field has any value.
                    Example: ``_exists_: "Properties.property key"``
                  - Range brackets: matches values between two bounds for numeric and date fields.
                    Square brackets ``[`` and ``]`` denote inclusive bounds, curly braces ``{`` and
                    ``}`` denote exclusive bounds, and ``*`` denotes no bound (infinity).
                    Example: ``size: [100 TO 200]`` matches ``100 <= size <= 200``.
                    Example: ``created: [* TO "2024-01-01T00:00:00Z"]`` matches files
                    created on or before January 1st, 2024.

                  Valid file properties for filtering:

                  - ``created``: ISO timestamp string (e.g. ``"2018-05-15T18:54:27.519Z"``)
                  - ``extension``: File extension (e.g. ``png``, ``txt``, ``pdf``)
                  - ``id``: File ID (e.g. ``"5afb2ce3741fe11d88838cc9"``)
                  - ``name``: File name within the service group
                  - ``properties``: Key-value pairs of file metadata, filtered using the syntax
                    ``"properties.[key]": "[value]"``. Example: ``"properties.owner": "admin"``
                  - ``size``: File size in bytes (e.g. ``32``)
                  - ``workspace``: Workspace name (e.g. ``"MyWorkspace"``)

                  Example::

                      'name: "myfile*" AND size: [* TO 1024000000] AND workspace: "MyWorkspace"'

                - **order_by** (:class:`~nisystemlink.clients.file.models.SearchFilesOrderBy`,
                  optional): The file property to order results by. When not specified, results
                  are ordered by relevance score. One of ``name``, ``created``, ``id``, ``size``,
                  or ``updated``.

                - **order_by_descending** (:class:`bool`, optional): Whether to return the files
                  in descending order. Defaults to ``False``.

                - **skip** (:class:`int`, optional): How many files to skip in the result when
                  paging. For example, a list of 100 files with a skip value of 50 will return
                  entries starting from the 51st file. Defaults to ``0``.

                - **take** (:class:`int`, optional): Maximum number of files to return.
                  Defaults to ``1000``. Maximum allowed value is ``1000``.

        Returns:
            SearchFilesResponse: Response containing matching files and total count.

        Raises:
            ApiException: if unable to communicate with the File Service or if Elasticsearch
                is not configured in the cluster.
        

#### `def delete_file(self, id: str) -> None`

Deletes the file indicated by the `file_id`.

        Args:
            id: The ID of the file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def delete_files(self, ids: List[str]) -> None`

Delete multiple files.

        Args:
            ids: List of unique IDs of Files.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def download_file(self, id: str) -> IteratorFileLike`

Downloads a file from the SystemLink File service.

        Args:
            id: The ID of the file.

        Yields:
            A file-like object for reading the exported data.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def __upload_file(self, file: Part, metadata: Part=None, id: Part=None, workspace: Query=None) -> str`

Uploads a file using multipart/form-data headers to send the file payload in the HTTP body.

        Args:
            file: The file to upload.
            metadata: Multipart part for file metadata, typically ``None`` or a
                ``(None, json_string, "application/json")`` tuple where
                ``json_string`` contains the metadata key/value pairs.
            id: Specify an unique (among all file) 24-digit Hex string ID of the file once it is uploaded.
                Defaults to None.
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            ID of uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def upload_file(self, file: BinaryIO, metadata: Dict[str, str] | None=None, id: str | None=None, workspace: str | None=None) -> str`

Uploads a file to the File Service.

        Args:
            file: The file to upload.
            metadata: File Metadata as dictionary.
            id: Specify an unique (among all file) 24-digit Hex string ID of the file once it is uploaded.
                Defaults to None.
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            ID of uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def update_metadata(self, metadata: models.UpdateMetadataRequest, id: str) -> None`

Updates an existing file's metadata with the specified metadata properties.

        Args:
            metadata: File's metadata and options for updating it.
            id: ID of the file to update Metadata.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def start_upload_session(self, workspace: str | None=None) -> models.UploadSessionStartResponse`

Start an upload session for uploading a file in chunks.

        Args:
            workspace: The id of the workspace the file belongs to. Defaults to None.

        Returns:
            Upload session information including the session ID.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def append_to_upload_session(self, session_id: str, chunk_index: int, chunk: BinaryIO, close: bool=False) -> None`

Append a chunk to an upload session.

        The chunk needs to be 10485760 bytes (10 MB), unless the close parameter is true,
        which means that it is the last chunk of the file content. The chunks can be uploaded
        concurrently, as long as all chunk uploads are completed before finalizing.

        Args:
            session_id: The id of the upload session.
            chunk_index: The 1-based index of the chunk to be uploaded.
            file: The chunk data to upload.
            close: Set the current chunk as the last chunk to be uploaded. Defaults to False.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

#### `def finish_upload_session(self, session_id: str, name: str, properties: Dict[str, str]) -> str`

Finish an upload session and make the file visible in SystemLink.

        This will trigger file events, such as routines.

        Args:
            session_id: The id of the upload session.
            name: The name of the file.
            properties: The properties of the file.

        Returns:
            ID of the uploaded file.

        Raises:
            ApiException: if unable to communicate with the File Service.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_base_file_request.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_base_file_request.py

### `class BaseFileRequest(JsonModel)`

Base class for file request models containing common query parameters.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_base_file_response.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_base_file_response.py

### `class TotalCountRelation(str, Enum)`

Describes the relation the returned total count value has with respect to the total number of files.

### `class TotalCount(JsonModel)`

The total number of files that match the query regardless of skip and take values

### `class BaseFileResponse(JsonModel)`

Base class for file response models containing a list of files and total count.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_linq_query.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_file_linq_query.py

### `class FileLinqQueryRequest(BaseFileRequest)`

Request model for LINQ query operations.

### `class FileLinqQueryResponse(BaseFileResponse)`

Response model for LINQ query operations.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_metadata.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_file_metadata.py

### `class BaseFileMetadata(JsonModel)`

Base class for file metadata.

### `class FileMetadata(BaseFileMetadata)`

Metadata for a file.

### `class LinqQueryFileMetadata(BaseFileMetadata)`

Metadata for a file returned by a LINQ query.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_query_order_by.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_file_query_order_by.py

### `class FileQueryOrderBy(Enum)`

Order Files Query Response by Metadata for GET /files endpoint.

### `class FileLinqQueryOrderBy(str, Enum)`

Order Files LINQ Query by Metadata for POST /query-files-linq endpoint.

### `class SearchFilesOrderBy(str, Enum)`

Order Files Search by Metadata for POST /search-files endpoint.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_file_query_response.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_file_query_response.py

### `class FileQueryResponse(JsonModel)`

The result of a file query.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_link.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_link.py

### `class Link(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_operations.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_operations.py

### `class Operations(JsonModel)`

### `class V1Operations(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_search_files_request.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_search_files_request.py

### `class SearchFilesRequest(BaseFileRequest)`

Request model for searching files.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_search_files_response.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_search_files_response.py

### `class SearchFilesResponse(BaseFileResponse)`

Response model for search files operation.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_update_metadata.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_update_metadata.py

### `class UpdateMetadataRequest(JsonModel)`

The file's metadata and options for updating it.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/models/_upload_session_start_response.py -->
## PYTHON MODULE: nisystemlink/clients/file/models/_upload_session_start_response.py

### `class UploadSessionStartResponse(JsonModel)`

Response model for starting an upload session.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/file/utilities.py -->
## PYTHON MODULE: nisystemlink/clients/file/utilities.py

### MODULE DOCSTRING

Utilities for FileClient.

### `def rename_file(client: FileClient, file_id: str, name: str) -> None`

Rename a file identified by `file_id` to `name`.

    Args:
        client: The FileClient to use for the rename.
        file_id: ID of file to rename.
        name: New name for the File.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/__init__.py

### MODULE DOCSTRING

Start here with NotebookClient for notebook management.

- `__all__ = ['NotebookClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/_notebook_client.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/_notebook_client.py

### `class NotebookClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Notebook Service.
        

#### `def get_notebook(self, id: str) -> models.NotebookMetadata`

Gets a notebook metadata by ID.

        Args:
            id: The ID of the notebook to read.

        Returns:
            The notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def __update_notebook(self, id: str, metadata: io.BytesIO | None=None, content: BinaryIO | None=None) -> models.NotebookMetadata`

Updates a notebook metadata by ID.

        Args:
            id: The ID of the notebook to update.
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The updated notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def update_notebook(self, id: str, metadata: models.NotebookMetadata | None=None, content: BinaryIO | None=None) -> models.NotebookMetadata`

Updates a notebook metadata by ID.

        Args:
            id: The ID of the notebook to update.
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The updated notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def delete_notebook(self, id: str) -> None`

Deletes a notebook by ID.

        Args:
            id: The ID of the notebook to delete.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def __create_notebook(self, metadata: io.BytesIO, content: BinaryIO) -> models.NotebookMetadata`

Creates a new notebook.

        Args:
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The created notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def create_notebook(self, metadata: models.NotebookMetadata, content: BinaryIO) -> models.NotebookMetadata`

Creates a new notebook.

        Args:
            metadata: The notebook metadata.
            content: The notebook binary content.

        Returns:
            The created notebook metadata.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def query_notebooks(self, query: models.QueryNotebookRequest) -> models.PagedNotebooks`

Queries notebooks.

        Args:
            query: The query parameters.

        Returns:
            The paged notebooks.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def get_notebook_content(self, id: str) -> IteratorFileLike`

Gets a notebook content by ID.

        Args:
            id: The ID of the notebook to read.

        Returns:
            A file-like object for reading the notebook content.

        Raises:
            ApiException: if unable to communicate with the ``/ninotebook`` service or provided invalid
                arguments.
        

#### `def create_executions(self, executions: List[models.CreateExecutionRequest]) -> models.CreateExecutionsResponse`

Create one or more executions of Jupyter notebooks.

        Args:
            execution: information about an execution of a Jupyter notebook.

        Returns:
            A response to a request to create executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def get_execution_by_id(self, id: str) -> models.Execution`

Get information about the specified execution of a Jupyter notebook.

        Args:
            id: the ID of the execution.

        Returns:
            Information about the execution of a Jupyter notebook fetched using it's Id.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def __query_executions(self, query: models._QueryExecutionsRequest) -> List[models.Execution]`

Query executions of Jupyter notebooks.

        Args:
            query: query for executions of Jupyter notebooks.

        Returns:
            A response to a request to query executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def query_executions(self, query: models.QueryExecutionsRequest) -> List[models.Execution]`

Query executions of Jupyter notebooks.

        Args:
            query: query for executions of Jupyter notebooks.

        Returns:
            A response to a request to query executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def retry_executions(self, ids: List[str]) -> ApiError | None`

Retries existing executions based on failed, canceled or timed-out executions.

        Args:
            ids: List of execution IDs to retry.

        Returns:
            An ApiError object if executions could not be retried.
            None if executions were retried successfully.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def cancel_executions(self, ids: List[str]) -> ApiError | None`

Cancel queued and in-progress executions.

        Args:
            ids: List of execution IDs to cancel.

        Returns:
            An ApiError object if executions could not be canceled.
            None if executions were canceled successfully.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

#### `def create_executions_from_existing(self, ids: List[str]) -> models.CreateExecutionsResponse`

Create new executions based on already existing succeeded executions.

        Args:
            ids: List of execution IDs to run again.

        Returns:
            A response to a request to create executions.

        Raises:
            ApiException: if unable to communicate with the ``/ninbexecution`` Service
                or provided an invalid argument.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_create_execution_request.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_create_execution_request.py

### `class CreateExecutionRequest(JsonModel)`

Creation information about an execution of a Jupyter notebook.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_create_execution_response.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_create_execution_response.py

### `class CreatedExecution(Execution)`

### `class CreateExecutionsResponse(JsonModel)`

Model for response to a request to create an execution.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_execution.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_execution.py

### `class SourceType(str, Enum)`

Source type of an execution.

### `class Source(JsonModel)`

An object that defines properties set by routine service.

### `class ReportType(str, Enum)`

Available types for a report that is going to be generated.

### `class ReportSettings(JsonModel)`

A class that defines settings of the Report.

### `class ExecutionPriority(str, Enum)`

Execution priority. Can be one of Low, Medium or High.

### `class ExecutionResourceProfile(str, Enum)`

Resource profile of the execution. Can be one of Low, Medium, High or Default.

### `class ExecutionStatus(str, Enum)`

Status of an execution.

### `class ExecutionErrorCode(str, Enum)`

Execution error code.

### `class Execution(JsonModel)`

Jupyter notebook execution information.

    Includes the cachedResult field.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_notebook_metadata.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_notebook_metadata.py

### `class NotebookMetadata(JsonModel)`

Metadata for a notebook.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_execution_request.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_query_execution_request.py

### `class ExecutionSortField(str, Enum)`

Possible fields used to sort executions.

### `class ExecutionField(str, Enum)`

Possible fields in executions.

### `class QueryExecutionsRequest(JsonModel)`

Query for executions of Jupyter notebooks.

### `class _QueryExecutionsRequest(JsonModel)`

Query for executions of Jupyter notebooks.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_notebook_request.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_query_notebook_request.py

### `class QueryNotebookRequest(WithPaging)`

Model for a query notebooks request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notebook/models/_query_notebook_response.py -->
## PYTHON MODULE: nisystemlink/clients/notebook/models/_query_notebook_response.py

### `class PagedNotebooks(WithPaging)`

Model for a query notebooks response.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/notification/__init__.py

### MODULE DOCSTRING

Start here with NotificationClient for notification management.

- `__all__ = ['NotificationClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/_notification_client.py -->
## PYTHON MODULE: nisystemlink/clients/notification/_notification_client.py

### MODULE DOCSTRING

Implementation of Notification Client

### `class NotificationClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the `/ninotification` service.
        

#### `def apply_dynamic_notification_strategy(self, request: models.DynamicStrategyRequest) -> None`

Applies the notification strategy from the given request.

        Args:
            request: Request with message template substitution fields and notification strategies.

        Returns:
            None.

        Raises:
            ApiException: if unable to communicate with the `/ninotification` service or provided invalid arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_address_group.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_address_group.py

### `class AddressGroup(BaseNotificationMetadata)`

Model defining notification recipients for generic service.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_base_notification_metadata.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_base_notification_metadata.py

### `class BaseNotificationMetadata(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_notification_configuration.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_dynamic_notification_configuration.py

### `class DynamicNotificationConfiguration(JsonModel)`

Model for notification configuration defining address groups and message template for the notification.

    Requires at least one of addressGroupId or addressGroup, and one of messageTemplateId or messageTemplate.
    

#### `def validate_required_pairs(self) -> DynamicNotificationConfiguration`

Validator to check at least one of address_group_id or address_group, and
        one of message_template_id or message_template is present.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_notification_strategy.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_dynamic_notification_strategy.py

### `class DynamicNotificationStrategy(JsonModel)`

Model for the notification strategy to be applied.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_dynamic_strategy_request.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_dynamic_strategy_request.py

### `class DynamicStrategyRequest(JsonModel)`

Request model for applying a dynamic notification strategy.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_message_template.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_message_template.py

### `class MessageTemplate(BaseNotificationMetadata)`

Model defining the notification content structure.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_smtp_address_group.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_smtp_address_group.py

### `class SmtpAddressFields(JsonModel)`

Recipient address fields used in SMTP messaging.

### `class SmtpAddressGroup(BaseNotificationMetadata)`

Model defining notification recipients for SMTP service.

#### `def set_interpreting_service_name(cls, data: 'SmtpAddressGroup') -> 'SmtpAddressGroup'`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/notification/models/_smtp_message_template.py -->
## PYTHON MODULE: nisystemlink/clients/notification/models/_smtp_message_template.py

### `class SmtpMessageTemplateFields(JsonModel)`

Template fields to construct an SMTP message.

### `class SmtpMessageTemplate(BaseNotificationMetadata)`

Model defining message template for SMTP service

#### `def set_interpreting_service_name(cls, data: 'SmtpMessageTemplate') -> 'SmtpMessageTemplate'`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/product/__init__.py

### MODULE DOCSTRING

Start here with ProductClient for product management.

- `__all__ = ['ProductClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/_product_client.py -->
## PYTHON MODULE: nisystemlink/clients/product/_product_client.py

### MODULE DOCSTRING

Implementation of Product Client

### `class ProductClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Product Service.
        

#### `def create_products(self, products: List[models.CreateProductRequest]) -> models.CreateProductsPartialSuccess`

Creates one or more products and returns errors for failed creations.

        Args:
            products: A list of products to attempt to create.

        Returns: A list of created products, products that failed to create, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` service of provided invalid
                arguments.
        

#### `def create_product(self, product: models.CreateProductRequest) -> models.Product`

Creates a single product.

        Args:
            product: The product to create.

        Returns:
            The created product.

        Raises:
            ApiException: if the product could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def get_products_paged(self, continuation_token: str | None=None, take: int | None=None, return_count: bool | None=None) -> models.PagedProducts`

Reads a list of products.

        Args:
            continuation_token: The token used to paginate results.
            take: The number of products to get in this request.
            return_count: Whether or not to return the total number of products available.

        Returns:
            A list of products.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def get_product(self, id: str) -> models.Product`

Retrieves a single product by id.

        Args:
            id (str): Unique ID of a products.

        Returns:
            The single product matching `id`

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def query_products_paged(self, query: models.QueryProductsRequest) -> models.PagedProducts`

Queries for products that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of products.

        Returns:
            A paged list of products with a continuation token to get the next page.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided invalid
                arguments.
        

#### `def query_product_values(self, query: models.QueryProductValuesRequest) -> List[str]`

Queries for products that match the query and returns a list of the requested field.

        Args:
            query : The query for the fields you want.

        Returns:
            A list of the values of the field you requested.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided
            invalid arguments.
        

#### `def update_products(self, products: List[models.UpdateProductRequest], replace: bool=False) -> models.CreateProductsPartialSuccess`

Updates a list of products with optional field replacement.

        Args:
            `products`: A list of products to update. Products are matched for update by id.
            `replace`: Replace the existing fields instead of merging them. Defaults to `False`.
                If this is `True`, then `keywords` and `properties` for the product will be
                    replaced by what is in the `products` provided in this request.
                If this is `False`, then the `keywords` and `properties` in this request will
                    merge with what is already present in the server resource.

        Returns: A list of updates products, products that failed to update, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def update_product(self, product: models.UpdateProductRequest, replace: bool=False) -> models.Product`

Updates a single product.

        Args:
            product: The product to update.
            replace: Replace the existing fields instead of merging them.

        Returns:
            The updated product.

        Raises:
            ApiException: if the product could not be updated or the service returns an
                unexpected partial-success payload.
        

#### `def delete_product(self, id: str) -> None`

Deletes a single product by id.

        Args:
            id (str): Unique ID of a product.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def delete_products(self, ids: List[str]) -> models.DeleteProductsPartialSuccess | None`

Deletes multiple products.

        Args:
            ids (List[str]): List of unique IDs of products.

        Returns:
            A partial success if any products failed to delete, or None if all
            products were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_create_products_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_create_products_partial_success.py

### `class CreateProductsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_delete_products_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_delete_products_partial_success.py

### `class DeleteProductsPartialSuccess(JsonModel)`

The result of deleting multiple products when one or more products could not be deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_paged_products.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_paged_products.py

### `class PagedProducts(WithPaging)`

The response containing the list of products, total count of products and the continuation
    token if applicable.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_product.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_product.py

### `class Product(JsonModel)`

Contains information about a product.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_product_request.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_product_request.py

### `class BaseProductRequest(JsonModel)`

Contains information about a product.

### `class CreateProductRequest(BaseProductRequest)`

### `class UpdateProductRequest(BaseProductRequest)`

This is the request model to update a product.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/models/_query_products_request.py -->
## PYTHON MODULE: nisystemlink/clients/product/models/_query_products_request.py

### `class ProductOrderBy(str, Enum)`

The valid ways to order a product query.

### `class ProductField(str, Enum)`

An enumeration of product fields for which the values can be queried for.

### `class ProductProjection(str, Enum)`

An enumeration of all fields in a Product.

    These are used to project the required fields from the API response.
    

### `class QueryProductsBase(JsonModel)`

Base class for product query requests.

### `class QueryProductsRequest(QueryProductsBase)`

Request model for querying products.

### `class QueryProductValuesRequest(QueryProductsBase)`

Request model for querying product values.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/utilities/_dataframe_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/product/utilities/_dataframe_utilities.py

### `def convert_products_to_dataframe(products: List[Product]) -> DataFrame`

Converts a list of products into a normalized dataframe.

    Args:
        products (List[Product]): A list of products

    Returns:
        DataFrame:
            - A Pandas DataFrame containing the product data. The DataFrame would consist of all the
            fields in the input products.
            - A new column would be created for unique properties across all products. The property
            columns would be named in the format `properties.property_name`.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/product/utilities/_file_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/product/utilities/_file_utilities.py

### `def get_products_linked_to_file(client: ProductClient, file_id: str) -> List[Product]`

Gets a list of all the products that are linked to the file.

    Args:
        `client` : The `ProductClient` to use for the request.
        `file_id`: The id of the file to query links for.

    Returns:
        `List[Product]`: A list of all the products that are linked to the file with `file_id`
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/spec/__init__.py

### MODULE DOCSTRING

Start here with SpecClient for specification management.

- `__all__ = ['SpecClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/_spec_client.py -->
## PYTHON MODULE: nisystemlink/clients/spec/_spec_client.py

### MODULE DOCSTRING

Implementation of SpecClient

### `class SpecClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Spec Service.
        

#### `def api_info(self) -> models.V1Operations`

Get information about available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the DataFrame Service.
        

#### `def create_specs(self, specs: models.CreateSpecificationsRequest) -> models.CreateSpecificationsPartialSuccess`

Creates one or more specifications.

        Args:
            specs: A list of specifications to create.

        Returns:
            A list of specs that were successfully created and ones that failed to be created.

        Raises:
            ApiException: if unable to communicate with the `/nispec` service or if there are
            invalid arguments.
        

#### `def create_spec(self, spec: models.CreateSpecificationsRequestObject) -> models.CreatedSpecification`

Creates a single specification.

        Args:
            spec: The specification to create.

        Returns:
            The created specification.

        Raises:
            ApiException: if the specification could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def delete_specs(self, ids: List[str]) -> models.DeleteSpecificationsPartialSuccess | None`

Deletes one or more specifications by global id.

        Args:
            ids: a list of specification ids. Note that these are the global ids and not the
            `specId` that is local to a product and workspace.

        Returns:
            None if all deletes succeed otherwise a list of which ids failed and which succeeded.

        Raises:
            ApiException: if unable to communicate with the `nispec` service or if there are invalid
            arguments.
        

#### `def query_specs(self, query: models.QuerySpecificationsRequest) -> models.PagedSpecifications`

Queries for specs that match the filters.

        Args:
            query: The query contains a product id as well as a filter for specs under that product.

        Returns:
            A list of specifications that match the filter.
        

#### `def get_spec(self, id: str) -> models.Specification`

Retrieves a single spec by id.

        Args:
            id (str): Unique ID of a specification.

        Returns:
            The single spec matching `id`

        Raises:
            ApiException: if unable to communicate with the `nispec` service or if there are invalid
            arguments.
        

#### `def update_specs(self, specs: models.UpdateSpecificationsRequest) -> models.UpdateSpecificationsPartialSuccess | None`

Updates one or more specifications.

        Update requires that the version field matches the version being updated from.

        Args:
            specs: a list of specifications that are to be updated. Must include the global id and
            each spec being updated must match the version currently on the server.

        Returns
            A list of specs that were successfully updated and a list of ones that were not along
            with error messages for updates that failed.
        

#### `def update_spec(self, spec: models.UpdateSpecificationsRequestObject) -> models.UpdatedSpecification`

Updates a single specification.

        Args:
            spec: The specification to update.

        Returns:
            The updated specification.

        Raises:
            ApiException: if the specification could not be updated or the service returns an
                unexpected partial-success payload.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_api_info.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_api_info.py

### `class V1Operations(JsonModel)`

The operations available in the routes provided by the v1 HTTP API.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_condition.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_condition.py

### `class ConditionType(Enum)`

Conditions are either numeric or string type.

### `class ConditionRange(JsonModel)`

Specifies the range of values that the condition must cover.

### `class ConditionValueBase(JsonModel)`

The base type for conditions that can be represented in several styles.

### `class NumericConditionValue(ConditionValueBase)`

A numeric condition.

    Numeric conditions can contain a combination of ranges and discrete lists.
    

### `class StringConditionValue(ConditionValueBase)`

A string condition.

    String conditions may only contain discrete lists of values.
    

### `class Condition(JsonModel)`

A single condition.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_create_specs_request.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_create_specs_request.py

### `class CreateSpecificationsRequestObject(SpecificationDefinition)`

### `class CreateSpecificationsRequest(JsonModel)`

Create multiple specifications.

### `class BaseSpecificationResponse(JsonModel)`

Base Response Model for create specs response and update specs response.

### `class CreatedSpecification(BaseSpecificationResponse)`

A specification successfully created on the server.

### `class CreateSpecificationsPartialSuccess(JsonModel)`

When some specs can not be created, this contains the list that was and was not created.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_delete_specs_request.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_delete_specs_request.py

### `class DeleteSpecificationsPartialSuccess(JsonModel)`

The results of deleting multiple specs when one or more of the specs could not be deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_query_specs.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_query_specs.py

### `class SpecificationProjection(str, Enum)`

The allowed projections for query.

    When using projection, only the fields specified by the projection element will be included in
    the response.
    

### `class SpecificationOrderBy(Enum)`

The valid ways to order the response to a spec query.

### `class QuerySpecificationsRequest(JsonModel)`

The request to query specifications.

### `class PagedSpecifications(WithPaging)`

The list of matching specifications and a continuation token to get the next items.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_specification.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_specification.py

### `class SpecificationLimit(JsonModel)`

A limit for a specification.

    The limit is the value that a measurement should be compared against during analysis to
    determine the health or pass/fail status of that measurement.
    

### `class SpecificationType(Enum)`

The overall type of the specification.

### `class SpecificationDefinition(JsonModel)`

### `class Specification(SpecificationDefinition)`

The complete definition of a specification.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/models/_update_specs_request.py -->
## PYTHON MODULE: nisystemlink/clients/spec/models/_update_specs_request.py

### `class UpdateSpecificationsRequestObject(SpecificationDefinition)`

### `class UpdateSpecificationsRequest(JsonModel)`

### `class UpdatedSpecification(BaseSpecificationResponse)`

A specification that was updated on the server.

### `class UpdateSpecificationsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/utilities/_constants.py -->
## PYTHON MODULE: nisystemlink/clients/spec/utilities/_constants.py

### `class DataFrameHeaders()`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/spec/utilities/_dataframe_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/spec/utilities/_dataframe_utilities.py

### `def summarize_conditions_as_a_string(conditions: List[Condition]) -> List[Dict[str, str]]`

Converts the condition values to an easily readable string format that summarizes
    either of numeric or string condition.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The dictionary key will be
        "condition_<conditionName>(<conditionUnit>)".
        The dictionary value will be "[min: num; max: num, step: num], num, num"
        where data within the '[]' is numeric condition range and other num
        values are numeric condition discrete values.
        The dictionary value will be "str, str, str" - where str values are the
        condition discrete values for a string condition. If the condition doesn't
        have a name and value, it will be skipped.
    

### `def normalize_conditions_per_column(conditions: List[Condition]) -> List[Dict[str, Any]]`

Convert conditions into list of dictionaries where dictionary key will be condition name
    and dictionary value will be condition value.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The key will be
        the condition name and the value will be the condition value which is
        either Numeric Condition Value, String Condition Value or None. If the condition doesn't
        have a name and value, it will be skipped.
    

### `def normalize_conditions_per_row(conditions: List[Condition]) -> List[Dict[str, Any]]`

Convert conditions into list of dictionaries where dictionary keys will be 'condition.name'
    and 'condition.value' and dictionary values will be condition name and condition value respectively.

    Args:
        conditions: List of all conditions in a spec.

    Returns:
        Conditions as a list of dictionary. The keys will be
        the 'condition.name' and 'condition.values' and the values will be the condition name and
        condition value which is either Numeric Condition Value, String Condition Value or None.
        If the condition doesn't have a name and value, it will be skipped.
        Each condition data will be logged as separate dictionary entry in the list which translates to
        separate row in the dataframe.
    

### `def convert_specs_to_dataframe(specs: List[Specification], condition_format: Callable[[List[Condition]], List[Dict[str, Any]]] | None=normalize_conditions_per_column) -> pd.DataFrame`

Creates a Pandas DataFrame for the specs.

    Args:
        specs: List of specs.
        condition_format: A callback function which takes in a list of condition of a spec and returns
                          a list of dictionary of condition and its values. The dictionary keys
                          should be the condition name and the values should be the condition
                          value in any format you need. Dataframe rows will be constructed based on
                          these list of dictionaries. Each dictionary in the list indicates a row.
                          If there is more than one dictionary in the list, it will be considered as a new
                          row and other spec column data will be duplicated.  Keys will be used as the dataframe
                          column header and values will be used as the row cells for the
                          respective column header.
                          If not passed, condition column header will be condition name and
                          corresponding row value will be condition value.
                          For all the condition columns to be grouped together in the dataframe,
                          the dictionary key should have the prefix "condition_".
                          If condition is needed as condition per row, the public method `normalize_conditions_per_row`
                          can be provided as the callback function.
                          If condition value is needed as a string summary of condition data, the public method
                          `summarize_conditions_as_a_string` can be provided as this callback function.
                          If None is passed, conditions will not be included in the dataframe.

    Returns:
        A Pandas DataFrame with the each spec fields having a separate column.
        Following fields are split into sub-columns.
            - conditions: format of the condition columns are decided by the  `condition_format`
            argument of this function.
            - Properties: All the unique properties across all specs will be split into separate columns.
            For example, properties.property1, properties.property2, etc.
    

### `def __convert_spec_to_dict(spec: Specification, condition: Dict[str, Any]) -> Dict[str, Any]`

Converts a spec into dictionary.

    Args:
        spec: Spec object.
        condition: Condition as a dictionary which is added to the output spec dictionary.

    Returns:
        Spec as a dictionary with the provided condition dictionary included.
    

### `def __serialize_limits(limit: SpecificationLimit) -> Dict[str, str]`

Serialize limit into limit.min, limit.typical and limit.max.

    Args:
        limit: Limit of a spec.

    Returns:
        Limit as a dictionary.
    

### `def __serialize_type(type: SpecificationType) -> Dict[str, str]`

Serialize type into it's string value.

    Args:
        type: Type of a spec.

    Returns:
        Type as a dictionary.
    

### `def __format_specs_columns(specs_dataframe: pd.DataFrame) -> pd.DataFrame`

Format specs column to group conditions and keep properties and keywords at the end.

    Args:
        specs_dataframe: Dataframe of specs.

    Returns:
        Formatted dataframe of specs.
    

### `def __is_standard_column_header(header: str) -> bool`

Check if column header is not a condition, property or keywords.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header doesn't start with condition_, properties. or keywords. Else returns false.

    

### `def __is_condition_header(header: str) -> bool`

Check if column header is not a condition.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header contains 'condition_'. Else returns false.

    

### `def __is_property_header(header: str) -> bool`

Check if column header is not a property.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header contains 'properties.'. Else returns false.

    

### `def __is_keywords_header(header: str) -> bool`

Check if column header is not a keywords.

    Args:
        header: column header for specs dataframe.

    Returns:
        True if header equals 'keywords'. Else returns false.

    

### `def __generate_condition_column_header(condition: Condition) -> str`

Generate column header for a condition.

    Args:
        condition: Condition object for generating column header.

    Returns:
        The column header for the given condition.
    

### `def __serialize_condition_value(condition: Condition) -> List[str]`

Get ranges and discrete values of a condition.

    Args:
        condition: Condition for getting values.

    Returns:
        The list of values of the given condition in a specific format.
    

### `def __serialize_numeric_condition_range(value: NumericConditionValue) -> List[str]`

Serialize ranges of a numeric condition value.

    Args:
        value: A condition's value with NumericConditionValue type.

    Returns:
        The list of ranges of the given condition where each range will be in
        string format `[min: <value>; max: <value>; step: <value>]` if the corresponding
        fields are not none.
    

### `def __serialize_condition_discrete_values(value: NumericConditionValue | StringConditionValue) -> List[str]`

Serialize discrete values of a value.

    Args:
        value: A condition's value with either NumericConditionValue type or StringConditionValue type.

    Returns:
        The list of discrete values of the given value in a string format.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/systems/__init__.py

### MODULE DOCSTRING

Start here with SystemsClient for system management.

- `__all__ = ['SystemsClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/_systems_client.py -->
## PYTHON MODULE: nisystemlink/clients/systems/_systems_client.py

### MODULE DOCSTRING

Implementation of SystemsClient

### `class SystemsClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the Systems Service.
        

#### `def create_virtual_system(self, create_virtual_system_request: models.CreateVirtualSystemRequest) -> models.CreateVirtualSystemResponse`

Creates a virtual system.

        Args:
            alias: The alias of the virtual system.
            workspace: The workspace to create the virtual system in.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` service or provided invalid
                arguments.
        

#### `def query_systems(self, query: models.QuerySystemsRequest) -> models.QuerySystemsResponse`

Queries for systems that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of systems.

        Returns:
            Response containing the list of systems that match the filter.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` Service or provided invalid
                arguments.
        

#### `def remove_systems(self, tgt: List[str]) -> models.RemoveSystemsResponse`

Removes multiple systems.

        Args:
            virtual_system_to_remove : List of unique IDs of systems.

        Returns:
            A partial success if any systems failed to remove, or None if all
            systems were removed successfully.

        Raises:
            ApiException: if unable to communicate with the `/nisysmgmt` Service
                or provided an invalid argument.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_create_virtual_systems_request.py -->
## PYTHON MODULE: nisystemlink/clients/systems/models/_create_virtual_systems_request.py

### `class CreateVirtualSystemRequest(JsonModel)`

Model for create virtual system response containing the minion ID of the system which is created.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_create_virtual_systems_response.py -->
## PYTHON MODULE: nisystemlink/clients/systems/models/_create_virtual_systems_response.py

### `class CreateVirtualSystemResponse(JsonModel)`

Model for create virtual system response containing the minion ID of the system which is created.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_query_systems_request.py -->
## PYTHON MODULE: nisystemlink/clients/systems/models/_query_systems_request.py

### `class QuerySystemsRequest(JsonModel)`

Model for query systems request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_query_systems_response.py -->
## PYTHON MODULE: nisystemlink/clients/systems/models/_query_systems_response.py

### `class QuerySystemsResponse(JsonModel)`

Model for query systems request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/systems/models/_remove_systems_response.py -->
## PYTHON MODULE: nisystemlink/clients/systems/models/_remove_systems_response.py

### `class RemoveSystemsResponse(JsonModel)`

Model for remove systems response containing the IDs of the systems which were deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/tag/__init__.py

### MODULE DOCSTRING

Start here with TagManager for tag operations and helper types.

- `__all__ = ['DataType', 'RetentionType', 'TagData', 'TagWithAggregates', 'AsyncTagQueryResultCollection', 'ITagReader', 'ITagWriter', 'BufferedTagWriter', 'TagValueReader', 'TagValueWriter', 'TagUpdateFields', 'TagDataUpdate', 'TagPathUtilities', 'TagQueryResultCollection', 'TagSubscription', 'TagSelection', 'TagManager']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_async_tag_query_result_collection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_async_tag_query_result_collection.py

### MODULE DOCSTRING

Implementation of AsyncTagQueryResultCollection.

### `class AsyncTagQueryResultCollection(abc.ABC)`

Represents a paginated list of tags returned by an asynchronous query.

#### `def __init__(self, first_page: List[tbase.TagData], total_count: int, skip: int) -> None`

Initialize an instance with the first page of query results.

        Args:
            first_page: The first page of results, or None if there are no results.
            total_count: The total number of results in the query.
            skip: The skip used for the first page of results.
        

#### `def current_page(self) -> List[tbase.TagData] | None`

The current page of tag results that were last retrieved from the server, or
        None if there are no more results.

        Use :meth:`move_next_page_async()` to get the next page of results.
        

#### `def total_count(self) -> int`

The total number of tags matched by the query at the time the query was made.

#### `async def move_next_page_async(self) -> List[tbase.TagData] | None`

Asynchronously retrieve the next page of query results from the server,
        returning them and updating :attr:`current_page`.

        Does nothing if the last page has already been retrieved. Use
        :meth:`reset_async()` to start again from the first page.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            next page of results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        

#### `async def reset_async(self) -> List[tbase.TagData]`

Asynchronously query the server for a fresh set of results, returning the
        first page and updating :attr:`current_page` and :attr:`total_count`.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            first page of results, or None if there are no results.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _query_page_async(self, skip: int) -> List[tbase.TagData]`

Asynchronously query for a single page of results and updates :attr:`total_count`.

        Args:
            skip: The skip to use in the query.

        Returns:
            A task representing the asynchronous operation. On completion, the page of
            results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_buffered_tag_writer.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_buffered_tag_writer.py

### MODULE DOCSTRING

Implementation of BufferedTagWriter.

### `class BufferedTagWriter(tbase.ITagWriter)`

Represents an :class:`ITagWriter` that buffers tag writes instead of sending them immediately.

    Writes that utilize automatic timestamps are based on the system time when buffered.
    Implementations may provide automatic sending of buffered writes based on different
    conditions. Unsent writes are discarded when the instance is deleted.

    Note that :class:`BufferedTagWriter` objects support using the ``with`` statement
    (or the ``async with`` statement), to automatically :meth:`send
    <send_buffered_writes>` any remaining buffered writes on exit.
    

#### `def __init__(self, stamper: ITimeStamper, buffer_size: int, flush_timer: ManualResetTimer) -> None`

Initialize the writer.

        Args:
            stamper: An object for time-stamping tag writes.
            buffer_size: The maximum number of tag writes to buffer before automatically
                sending them to the server.
            flush_timer: A timer that, once started, elapses whenever buffered writes
                should be sent automatically. Does not have to be a configured timer.
        

#### `def _buffer_value(self, path: str, value: Any) -> None`

Add a value to the buffer.

        Args:
            path: The tag path being written.
            value: The value being written.
        

#### `def _clear_buffer(self) -> None`

Clear the buffer of writes.

#### `def _copy_buffer(self) -> Any`

Return the contents of the buffer and clears or replaces the buffer used for future writes.

        Returns:
            The buffered data.
        

#### `def _create_item(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> Any`

Return an item that can be placed into the buffer.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: The timestamp represented as a nullable ``datetime.datetime``.

        Returns:
            The created item.

        Raises:
            ValueError: if ``data_type`` is not supported for writing.
        

#### `def _send_writes(self, updates: Any) -> None`

Send the writes stored in ``updates`` to the server.

        Args:
            updates: The writes to send.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _send_writes_async(self, updates: Any) -> None`

Asynchronously send the writes stored in ``updates`` to the server.

        Args:
            updates: The writes to send.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        

#### `def clear_buffered_writes(self) -> None`

Clear any pending writes from :meth:`write()`.

        Raises:
            ReferenceError: if the writer has been closed.
        

#### `def send_buffered_writes(self) -> None`

Write all of the pending writes from :meth:`write()` to the server.

        Does nothing if there are no pending writes.

        Raises:
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `async def send_buffered_writes_async(self) -> None`

Asynchronously write all of the pending writes from :meth:`write()` to the server.

        Does nothing if there are no pending writes.

        Raises:
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `def __enter__(self) -> 'BufferedTagWriter'`

#### `async def __aenter__(self) -> 'BufferedTagWriter'`

#### `def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool`

#### `async def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool`

#### `def _write(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> None`

Write a tag's value that's been serialized to a string.

        Clients do not typically call this method directly. Use a
        :class:`.TagValueWriter` instead.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if `path` is empty or invalid.
            ValueError: if `path` or `value` is None.
            ValueError: if `data_type` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `async def _write_async(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> None`

Asynchronously write a tag's value that's been serialized to a string.

        Clients do not typically call this method directly. Use a
        :class:`.TagValueWriter` instead.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if `path` is empty or invalid.
            ValueError: if `path` or `value` is None.
            ValueError: if `data_type` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `def _prepare_write(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> Any`

#### `def _retrieve_buffered_values_while_locked(self) -> Any`

Return the buffered values, if any, and clears the buffer.

        Must hold :attr:`_lock`.

        Returns:
            The buffered values, or None if there aren't any.
        

#### `def _start_timer_while_locked(self) -> None`

Start the flush timer, if configured.

        Must hold :attr:`_lock`.
        

#### `def _stop_timer_while_locked(self) -> None`

Stop the flush timer, if configured.

        Must hold :attr:`_lock`.
        

#### `def _timer_expired(self, generation: int) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_itime_stamper.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_core/_itime_stamper.py

### MODULE DOCSTRING

Implementation of ITimeStamper.

### `class ITimeStamper(abc.ABC)`

Represents an object for time-stamping objects or actions such that no two
    timestamps returned by the instance are within the same microsecond.
    

#### `def timestamp(self) -> datetime.datetime`

A unique UTC ``datetime.datetime`` that is close to the current date and time.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_manual_reset_timer.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_core/_manual_reset_timer.py

### MODULE DOCSTRING

Implementation of ManualResetTimer.

### `class ManualResetTimer(events.Events)`

Represents a timer for periodic background operations such that :meth:`start()`
    must be called to restart the timer each time the :attr:`elapsed` event is raised.

    Attributes:
        elapsed: An event that is triggered when the timer has elapsed.

    Example::

        def timer_elapsed():
            print("The timer elapsed!")

        my_timer.elapsed += timer_elapsed
    

#### `def __init_subclass__(cls) -> None`

#### `def null_timer(cls) -> 'ManualResetTimer'`

A timer that never fires.

#### `def __init__(self, interval: datetime.timedelta) -> None`

Initialize a timer that fires at the given interval a single time once
        :meth:`start()` has been called and then automatically stops.

        Args:
            interval: The amount of time after calling :meth:`start()` before
                :attr:`elapsed` is raised.

        Raises:
            ValueError: if ``interval`` is less than or equal to zero.
        

#### `def can_start(self) -> bool`

Whether or not the timer is configured and can be started.

        A timer that isn't configured will never raise :attr:`elapsed`, even when
        :meth:`start()` is called.
        

#### `def start(self) -> None`

Start the timer.

#### `def stop(self) -> None`

Stop the timer.

#### `def _run(running: List[None], interval: int, timer_start: threading.Event, timer_cancel: threading.Event, elapsed: Callable[[], None]) -> None`

#### `def __enter__(self) -> 'ManualResetTimer'`

#### `async def __aenter__(self) -> 'ManualResetTimer'`

#### `def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Literal[False]`

#### `async def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Literal[False]`

#### `def __del__(self) -> None`

#### `def __getattr__(self, name: str) -> Any`

#### `def __type_hinting__(self) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates.py

### MODULE DOCSTRING

Implementation of SerializedTagWithAggregates.

### `class SerializedTagWithAggregates()`

Represents a generic tag value serialized to a string with optional aggregate
    values also serialized to a string.

    Clients typically do not interact with this instances of this class directly. Use a
    :class:`.TagValueReader` instead.
    

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None, count: int | None=None, min: str | None=None, max: str | None=None, mean: float | None=None) -> None`

Initialize an instance.

        Args:
            path: The path of the tag associated with the value.
            data_type: The data type of the value serialized as a string.
            value: The value serialized as a string.
            timestamp: The timestamp associated with the value.
            count: The number of times the tag has been written, or None if the tag is
                not collecting aggregates.
            min: The minimum value of the tag serialized to a string, or None if the tag
                is not collecting aggregates or the data type of the tag does not track
                a minimum value.
            max: The maximum value of the tag serialized to a string, or None if the tag
                is not collecting aggregates or the data type of the tag does not track
                a maximum value.
            mean: The mean value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a mean value.
        

#### `def data_type(self) -> tbase.DataType`

The data type of the value that was serialized as a string.

#### `def path(self) -> str`

The path of the tag associated with the value.

#### `def value(self) -> str`

The value of the tag serialized as a string.

#### `def timestamp(self) -> datetime.datetime | None`

The timestamp associated with the value, if available.

#### `def count(self) -> int | None`

The number of times the tag has been written, or None if the tag is not collecting aggregates.

#### `def min(self) -> str | None`

The minimum value of the tag serialized to a string, or None if the tag is
        not collecting aggregates or the data type of the tag does not track a minimum
        value.
        

#### `def max(self) -> str | None`

The maximum value of the tag serialized to a string, or None if the tag is
        not collecting aggregates or the data type of the tag does not track a maximum
        value.
        

#### `def mean(self) -> float | None`

The mean value of the tag, or None if the tag is not collecting aggregates or
        the data type of the tag does not track a mean value.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_core/_serialized_tag_with_aggregates_reader.py

### MODULE DOCSTRING

Implementation of SerializedTagWithAggregatesReader.

### `class SerializedTagWithAggregatesReader(tbase.ITagReader)`

Represents an :class:`.ITagReader` wrapping a single :class:`SerializedTagWithAggregates`.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, value: SerializedTagWithAggregates) -> None`

Initialize a reader instance for the given value.

        Args:
            value: The value to wrap in a reader.

        Raises:
            ValueError: if ``value`` is None.
        

#### `def _read(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.
        

#### `async def _read_async(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_core/_system_time_stamper.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_core/_system_time_stamper.py

### MODULE DOCSTRING

Implementation of SystemTimeStamper.

### `class SystemTimeStamper(ITimeStamper)`

A :class:`ITimeStamper` that uses the system clock.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self) -> None`

#### `def timestamp(self) -> datetime.datetime`

A unique UTC ``datetime.datetime`` that is close to the current date and time.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_data_type.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_data_type.py

### MODULE DOCSTRING

Implementation of DataType.

### `class DataType(enum.Enum)`

Represents the different data types for a SystemLink tag.

#### `def api_name(self) -> str`

Web API name of the enum value.

#### `def from_api_name(cls, name: str) -> 'DataType'`

- `_API_NAME = {DataType.UNKNOWN: 'UNKNOWN', DataType.DOUBLE: 'DOUBLE', DataType.INT32: 'INT', DataType.STRING: 'STRING', DataType.BOOLEAN: 'BOOLEAN', DataType.UINT64: 'U_INT64', DataType.DATE_TIME: 'DATE_TIME'}`

- `_FROM_API_NAME = {'DOUBLE': DataType.DOUBLE, 'INT': DataType.INT32, 'STRING': DataType.STRING, 'BOOLEAN': DataType.BOOLEAN, 'U_INT64': DataType.UINT64, 'DATE_TIME': DataType.DATE_TIME}`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_http_async_tag_query_result_collection.py

### MODULE DOCSTRING

Implementation of HttpAsyncTagQueryResultCollection.

### `class HttpAsyncTagQueryResultCollection(tbase.AsyncTagQueryResultCollection)`

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, client: HttpClient, paths: str | None, keywords: str | None, properties: str | None, skip: int, take: int | None, tag_query_result: Dict[str, Any], http_response: HttpResponse) -> None`

#### `async def _query_page_async(self, skip: int) -> List[tbase.TagData]`

#### `def __handle_query_response(self, response: Dict[str, Any], http_response: HttpResponse) -> Tuple[List[tbase.TagData], int]`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_http_buffered_tag_writer.py

### MODULE DOCSTRING

Implementation of HttpBufferedTagWriter.

### `class HttpBufferedTagWriter(tbase.BufferedTagWriter)`

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, client: HttpClient, stamper: ITimeStamper, buffer_size: int, flush_timer: ManualResetTimer) -> None`

#### `def _buffer_value(self, path: str, value: Dict[str, Any]) -> None`

#### `def _clear_buffer(self) -> None`

#### `def _copy_buffer(self) -> Dict[str, Dict[str, Any]]`

#### `def _create_item(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> Dict[str, Any]`

#### `def _send_writes(self, updates: Dict[str, Dict[str, Any]]) -> None`

#### `async def _send_writes_async(self, updates: Dict[str, Any]) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_http_tag_query_result_collection.py

### MODULE DOCSTRING

Implementation of HttpTagQueryResultCollection.

### `class HttpTagQueryResultCollection(tbase.TagQueryResultCollection)`

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, client: HttpClient, paths: str | None, keywords: str | None, properties: str | None, skip: int, take: int | None, tag_query_result: Dict[str, Any], http_response: HttpResponse) -> None`

#### `def _query_page(self, skip: int) -> List[tbase.TagData]`

#### `def __handle_query_response(self, response: Dict[str, Any], http_response: HttpResponse) -> Tuple[List[tbase.TagData], int]`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_selection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_http_tag_selection.py

### MODULE DOCSTRING

Implementation of HttpTagSelection.

- `T = TypeVar('T')`

### `class HttpTagSelection(tbase.TagSelection)`

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, client: HttpClient, tags: Sequence[tbase.TagData], *, _paths: Sequence[str] | None=None) -> None`

Initialize a selection using existing data.

        Args:
            client: The HTTP client object for communicating with the server.
            tags: The tags to store in the selection.

        Raises:
            ValueError: if ``tags`` contains tags that are None or have invalid paths.
            ValueError: if ``tags`` contains duplicate tags.
            ValueError: if ``tags`` is None.
        

#### `def open(cls, client: HttpClient, paths: Sequence[str]) -> 'HttpTagSelection'`

Initialize a selection using queried data.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The paths used in the query.

        Returns:
            The created selection.

        Raises:
            ValueError: if ``paths`` is None.
            ValueError: if ``paths`` contains duplicate paths.
            ApiException: if the API call fails.
        

#### `async def open_async(cls, client: HttpClient, paths: Sequence[str]) -> 'HttpTagSelection'`

Asynchronously initialize a selection using queried data.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The paths used in the query.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created selection.

        Raises:
            ValueError: if ``paths`` is None.
            ValueError: if ``paths`` contains duplicate paths.
            ApiException: if the API call fails.
        

#### `def _on_paths_changed(self) -> None`

#### `def _close_internal(self) -> None`

#### `async def _close_internal_async(self) -> None`

#### `def _create_subscription_internal(self, update_interval: datetime.timedelta | None=None) -> tbase.TagSubscription`

#### `async def _create_subscription_internal_async(self, update_interval: datetime.timedelta | None=None) -> tbase.TagSubscription`

#### `def _delete_tags_from_server_internal(self) -> None`

#### `async def _delete_tags_from_server_internal_async(self) -> None`

#### `def _read_tag_metadata(self) -> List[tbase.TagData]`

#### `async def _read_tag_metadata_async(self) -> List[tbase.TagData]`

#### `def _handle_read_tags_metadata(self, response: List[Any], http_response: HttpResponse) -> List[tbase.TagData]`

#### `def _read_tag_values(self) -> List[SerializedTagWithAggregates | None]`

#### `async def _read_tag_values_async(self) -> List[SerializedTagWithAggregates | None]`

#### `def _handle_read_tags_values(self, response: List[Any], http_response: HttpResponse, paths: List[str] | None=None) -> List[SerializedTagWithAggregates | None]`

#### `def _read_tag_metadata_and_values(self) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]`

#### `async def _read_tag_metadata_and_values_async(self) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]`

#### `def _handle_read_tags_metadata_and_values(self, response: Any, http_response: HttpResponse) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]`

#### `def _reset_aggregates_internal(self) -> None`

#### `async def _reset_aggregates_internal_async(self) -> None`

#### `def _create_selection_on_server(self) -> None`

#### `async def _create_selection_on_server_async(self) -> None`

#### `def _update_selection_on_server_if_needed(self) -> None`

#### `async def _update_selection_on_server_if_needed_async(self) -> None`

#### `def _ensure_selection_and_call(self, api_call: Callable[[str], T]) -> T`

#### `async def _ensure_selection_and_call_async(self, api_call: Callable[[str], Awaitable[T]]) -> T`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_http_tag_subscription.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_http_tag_subscription.py

### MODULE DOCSTRING

Implementation of HttpTagSubscription.

### `class HttpTagSubscription(tbase.TagSubscription)`

#### `def __init_subclass__(cls) -> None`

#### `def create(cls, client: HttpClient, paths: Iterable[str], update_timer: ManualResetTimer | None=None, heartbeat_timer: ManualResetTimer | None=None) -> 'HttpTagSubscription'`

Create an :class:`HttpTagSubscription` with a custom heartbeat timer for testing purposes.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag path queries to include in the subscription.
            update_timer: A timer for polling for updates on the server, or None to use
                a default timer.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive, or None to use a default timer.

        Returns:
            The created subscription.

        Raises:
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        

#### `async def create_async(cls, client: HttpClient, paths: Iterable[str], update_timer: ManualResetTimer | None=None, heartbeat_timer: ManualResetTimer | None=None) -> 'HttpTagSubscription'`

Asynchronously create an :class:`HttpTagSubscription` with a custom heartbeat timer for testing purposes.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag path queries to include in the subscription.
            update_timer: A timer for polling for updates on the server, or None to use
                a default timer.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive, or None to use a default timer.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created subscription.

        Raises:
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        

#### `def __init__(self, magic: object, client: HttpClient, paths: Iterable[str], update_timer: ManualResetTimer | None=None, heartbeat_timer: ManualResetTimer | None=None) -> None`

#### `def _close_internal(self) -> None`

#### `async def _close_internal_async(self) -> None`

#### `def _create_subscription_on_server(self, paths: List[str]) -> None`

#### `async def _create_subscription_on_server_async(self, paths: List[str]) -> None`

#### `def _send_heartbeat(self) -> None`

#### `def _update_timer_elapsed(self) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_http/_temporary_tag_selection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_http/_temporary_tag_selection.py

### MODULE DOCSTRING

Implementation of TemporaryTagSelection.

### `class TemporaryTagSelection()`

Manages the lifetime of short-lived tag selections that are used within a single API call.

    Closing the instance deletes the selection.
    

#### `def __init_subclass__(cls) -> None`

#### `def create(cls, client: HttpClient, paths: List[str]) -> 'TemporaryTagSelection'`

Create a temporary tag selection containing the given paths.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag search paths to include in the selection.
        

#### `async def create_async(cls, client: HttpClient, paths: List[str]) -> 'TemporaryTagSelection'`

Asynchronously create a temporary tag selection containing the given paths.

        Args:
            client: The HTTP client object for communicating with the server.
            paths: The tag search paths to include in the selection.

        Returns:
            A task representing the asynchronous operation. On completion, contains the
            created selection.
        

#### `def __init__(self, magic: object, client: HttpClient) -> None`

#### `def id(self) -> str | None`

The ID of the selection.

#### `def close(self) -> None`

Close the selection.

#### `async def close_async(self) -> None`

Asynchronously close the selection.

        Returns:
            A task representing the asynchronous operation.
        

#### `def __enter__(self) -> 'TemporaryTagSelection'`

#### `async def __aenter__(self) -> 'TemporaryTagSelection'`

#### `def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None`

#### `def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Awaitable[None]`

#### `def __del__(self) -> None`

#### `def _create(self, paths: List[str]) -> None`

#### `async def _create_async(self, paths: List[str]) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_itag_reader.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_itag_reader.py

### MODULE DOCSTRING

Implementation of ITagReader.

- `_DESERIALIZERS = {tbase.DataType.BOOLEAN: {'True': True, 'False': False}.get, tbase.DataType.DATE_TIME: TimestampUtilities.str_to_datetime, tbase.DataType.DOUBLE: float, tbase.DataType.INT32: int, tbase.DataType.UINT64: int, tbase.DataType.STRING: str}`

### `class _ITagReaderOverloads(abc.ABC)`

Contains the overloaded methods of ITagReader.

    These overloads exist so that ``mypy`` can validate proper data types are used when
    reading tag values, as long as a literal DataType enum value is given when calling
    :meth:`get_tag_reader`. But they are hidden away in a base class so that they aren't
    documented by Sphinx, because Sphinx doesn't properly recognize the type annotations
    of overloads. See also: https://github.com/sphinx-doc/sphinx/issues/7901
    

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.BOOLEAN]) -> 'tbase.TagValueReader[bool]'`

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.DATE_TIME]) -> 'tbase.TagValueReader[datetime.datetime]'`

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.DOUBLE]) -> 'tbase.TagValueReader[float]'`

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.INT32]) -> 'tbase.TagValueReader[int]'`

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.UINT64]) -> 'tbase.TagValueReader[int]'`

#### `def get_tag_reader(self, path: str, data_type: Literal[tbase.DataType.STRING]) -> 'tbase.TagValueReader[str]'`

#### `def get_tag_reader(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueReader[Any]'`

#### `def get_tag_reader(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueReader'`

Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the tag to read.
        

#### `def _get_tag_reader(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueReader'`

Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the value to read.
        

### `class ITagReader(_ITagReaderOverloads)`

Provides an interface for reading the current and aggregate values of a single SystemLink tag.

#### `def read(self, path: str, *, include_timestamp: bool=False, include_aggregates: bool=False) -> tbase.TagWithAggregates | None`

Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        

#### `async def read_async(self, path: str, *, include_timestamp: bool=False, include_aggregates: bool=False) -> tbase.TagWithAggregates | None`

Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        

#### `def _read(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        

#### `async def _read_async(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ReferenceError: if the reader has been closed.
            ApiException: if the API call fails.
        

#### `def _deserialize_value(cls, value: str | None, data_type: tbase.DataType) -> Any`

#### `def _get_tag_reader(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueReader'`

Get a :class:`TagValueReader` for this path.

        Args:
            path: The path of the tag to read.
            data_type: The data type of the value to read.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_itag_writer.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_itag_writer.py

### MODULE DOCSTRING

Implementation of ITagWriter.

- `_VALID_TYPES = {tbase.DataType.BOOLEAN: bool, tbase.DataType.DATE_TIME: datetime.datetime, tbase.DataType.DOUBLE: (float, int), tbase.DataType.INT32: int, tbase.DataType.UINT64: int, tbase.DataType.STRING: str}`

### `class _ITagWriterOverloads(abc.ABC)`

Contains the overloaded methods of ITagWriter.

    These overloads exist so that ``mypy`` can validate proper data types are used when
    writing tag values, as long as a literal DataType enum value is given when calling
    :meth:`get_tag_writer`. But they are hidden away in a base class so that they aren't
    documented by Sphinx, because Sphinx doesn't properly recognize the type annotations
    of overloads. See also: https://github.com/sphinx-doc/sphinx/issues/7901
    

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.BOOLEAN]) -> 'tbase.TagValueWriter[bool]'`

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.DATE_TIME]) -> 'tbase.TagValueWriter[datetime.datetime]'`

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.DOUBLE]) -> 'tbase.TagValueWriter[float]'`

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.INT32]) -> 'tbase.TagValueWriter[int]'`

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.UINT64]) -> 'tbase.TagValueWriter[int]'`

#### `def get_tag_writer(self, path: str, data_type: Literal[tbase.DataType.STRING]) -> 'tbase.TagValueWriter[str]'`

#### `def get_tag_writer(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueWriter[Any]'`

#### `def get_tag_writer(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueWriter'`

Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        

#### `def _get_tag_writer(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueWriter'`

Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        

### `class ITagWriter(_ITagWriterOverloads)`

Provides an interface for writing the current value of a single SystemLink tag.

#### `def write(self, path: str, data_type: tbase.DataType, value: bool | int | float | str | datetime.datetime, *, timestamp: datetime.datetime | None=None) -> None`

Write a tag's value.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``value`` has the wrong data type.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `def write_async(self, path: str, data_type: tbase.DataType, value: str, *, timestamp: datetime.datetime | None=None) -> Awaitable[None]`

Asynchronously write a tag's value.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``value`` has the wrong data type.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `def _validate_type(cls, value: bool | int | float | str | datetime.datetime, data_type: tbase.DataType) -> None`

#### `def _write(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> None`

Write a tag's value that's been serialized to a string.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `async def _write_async(self, path: str, data_type: tbase.DataType, value: str, timestamp: datetime.datetime | None=None) -> None`

Asynchronously write a tag's value that's been serialized to a string.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the value to write.
            value: The tag value to write, serialized as a string.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` or ``value`` is None.
            ValueError: if ``data_type`` is invalid.
            ReferenceError: if the writer has been closed.
            ApiException: if the API call fails.
        

#### `def _get_tag_writer(self, path: str, data_type: tbase.DataType) -> 'tbase.TagValueWriter'`

Get a :class:`TagValueWriter` for this path.

        Args:
            path: The path of the tag to write.
            data_type: The data type of the tag to write.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_retention_type.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_retention_type.py

### MODULE DOCSTRING

Implementation of RetentionType.

### `class RetentionType(enum.Enum)`

Represents the different ways for the SystemLink tag historian to retain the history of tag values.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_data.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_data.py

### MODULE DOCSTRING

Implementation of TagData.

### `class TagData()`

Contains the metadata for a SystemLink tag.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, path: str, data_type: tbase.DataType | None=None, keywords: Iterable[str] | None=None, properties: Dict[str, str] | None=None) -> None`

Initialize an instance.

        Args:
            path: The tag's path, which uses a dot-separated hierarchy to uniquely
                identify the tag on the server.
            data_type: The data type for the tag's values.
            keywords: The tag's keywords.
            properties: The tag's properties.
        

#### `def from_json_dict(cls, data: Dict[str, Any]) -> 'TagData'`

#### `def to_json_dict(self) -> Dict[str, Any]`

#### `def collect_aggregates(self) -> bool`

Whether the server should keep aggregate information for the tag.

        The information collected depends on the tag's :attr:`data_type`.
        

#### `def collect_aggregates(self, value: bool) -> None`

#### `def data_type(self) -> tbase.DataType`

The data type for the tag's values.

        Changing the data type of an existing tag requires deleting the tag and creating
        a new one of a different data type.
        

#### `def data_type(self, value: tbase.DataType) -> None`

#### `def keywords(self) -> List[str]`

The list of keywords associated with the tag.

#### `def path(self) -> str`

The tag's path, which uses a dot-separated hierarchy to uniquely identify the tag on the server.

#### `def properties(self) -> Dict[str, str]`

The properties associated with the tag.

#### `def retention_type(self) -> tbase.RetentionType`

How the tag's historical values are retained by the tag historian, if available.

        The :attr:`retention_count` and :attr:`retention_days` properties can further
        customize when values are removed from the historian.

        The tag historian is an optional component for SystemLink Server installations,
        and is not available in SystemLink Cloud. The tag's historical values are not
        retained when the tag historian is not available, regardless of the retention
        type.
        

#### `def retention_type(self, value: tbase.RetentionType) -> None`

#### `def retention_count(self) -> int | None`

The number of historical values to retain when :attr:`retention_type` is
        :attr:`RetentionType.COUNT`, or None to use the server-specified default of
        10000.
        

#### `def retention_count(self, value: int | None) -> None`

#### `def retention_days(self) -> int | None`

The number of days to keep a tag's historical values when
        :attr:`retention_type` is :attr:`RetentionType.DURATION`, or None to use the
        server-specified default of 30 days.
        

#### `def retention_days(self, value: int | None) -> None`

#### `def replace_keywords(self, keywords: Iterable[str]) -> None`

Replace all of the tag's :attr:`keywords` with those in ``keywords``.

        Args:
            keywords: The tag's new keywords, or None to clear all keywords.
        

#### `def replace_properties(self, properties: Dict[str, str]) -> None`

Replace all of the tag's :attr:`properties` with those in ``properties``.

        Args:
            properties: The tag's new properties, or None to clear all properties.
        

#### `def _copy_retention_properties(self, destination: Dict[str, str]) -> None`

Copy the tag's retention settings into ``destination``.

        Clients do not typically call this method directly.

        Args:
            destination: The dictionary to copy into. Existing properties with names in
                common with the retention properties will be overwritten.

        Raises:
            ValueError: if ``destination`` is None.
        

#### `def clear_retention(self) -> None`

Clear all retention settings, setting it to use a
        :attr:`TagData.retention_type` of :attr:`RetentionType.NONE`.

        Args:
            tag: The tag whose retention will be cleared.
        

#### `def set_retention_count(self, count: int) -> None`

Set the number of historical values to retain.

        Args:
            count: The number of historical values to retain.
        

#### `def set_retention_days(self, days: int) -> None`

Set the historical values to be retained for the specified number of days.

        Args:
            days: The number of days a historical value will be kept.
        

#### `def validate_type(self, required_type: tbase.DataType) -> None`

Validate that the tag's data type matches ``required_type``.

        Clients do not typically call this method directly.

        Args:
            required_type: The data type required by the API.

        Raises:
            ValueError: if this is not a tag of the required type with a valid path.
            ValueError: if ``required_type`` is :attr:`DataType.UNKNOWN`.
        

#### `def validate_path(self) -> str`

Validate the path as an input and returns it.

        Clients do not typically call this method directly.

        Returns:
            The validated path.

        Raises:
            ValueError: if the tag's path is invalid.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_data_update.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_data_update.py

### MODULE DOCSTRING

Implementation of TagDataUpdate.

### `class TagDataUpdate()`

Contains information for updating parts of a tag's metadata on the server when
    used with the :meth:`TagManager.update()` method.

    The update can add keywords, add new properties, change the value of existing
    properties, modify the collect aggregates setting, and modify retention settings. To
    remove a keyword or property, pass the entire :class:`TagData` to the
    :meth:`TagManager.update()` method instead.
    

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, path: str, data_type: tbase.DataType, keywords: Iterable[str] | None=None, properties: Dict[str, str] | None=None) -> None`

Initialize an update of a tag's keywords and/or properties.

        Keywords and properties included in the update that are missing from the tag's
        metadata on the server are added, and properties that exist with a different
        value are replaced. At least one of ``keywords`` or ``properties`` must be
        specified.

        Args:
            path: The path of the tag to update.
            data_type: The data type of the tag to update.
            keywords: The list of keywords that will be added to the tag's metadata on
                the server, or None to not add any keywords.
            properties: The properties that will be added to or replaced in the tag's
                metadata on the server, or None to not modify any properties.

        Raises:
            ValueError: if ``path`` is None.
            ValueError: if both ``keywords`` and ``properties`` are None.
        

#### `def from_tagdata(cls, data: tbase.TagData, fields: tbase.TagUpdateFields) -> 'TagDataUpdate'`

Create an update by taking one or more fields from a :class:`TagData`.

        Args:
            data: The metadata to send to the server in the update.
            fields: One or more fields to include in the update.

        Raises:
            ValueError: if ``data`` is None.
            ValueError: if ``fields`` has no fields or invalid fields.
        

#### `def to_json_dict(self) -> Dict[str, Any]`

#### `def collect_aggregates(self) -> bool | None`

The :attr:`TagData.collect_aggregates` setting to send with the update, or None to not send a value.

#### `def data_type(self) -> tbase.DataType`

The data type for the tag's values.

#### `def keywords(self) -> Tuple[str, ...] | None`

The list of keywords to send with the update, or None to not send any keywords.

#### `def path(self) -> str`

The tag's path, which uses a dot-separated hierarchy to uniquely identify the tag on the server.

#### `def properties(self) -> Dict[str, str] | None`

The properties send with the update, or None to not send any properties.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_manager.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_manager.py

### MODULE DOCSTRING

Implementation of TagManager.

### `class TagManager(tbase.ITagReader)`

Represents common ways to create, read, and query SystemLink tags for a specific server connection.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None) -> None`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect.

        Raises:
            ApiException: if the current system cannot communicate with a SystemLink
                Server, or if the configuration provided by SystemLink Client cannot be
                found.
        

#### `def create_selection(self, tags: List[tbase.TagData]) -> tbase.TagSelection`

Create an :class:`TagSelection` that initially contains the given ``tags``
        without retrieving any additional data from the server.

        Args:
            tags: The tags to include in the selection.

        Returns:
            The created selection.

        Raises:
            ValueError: if any of the given ``tags`` is None or has an invalid path.
            ValueError: if ``tags`` is None.
        

#### `def open_selection(self, paths: List[str]) -> tbase.TagSelection`

Query the server for the metadata for the given tag ``paths`` and return the
        results in a :class:`TagSelection`.

        Args:
            paths: The paths of the tags to include in the selection. May include
                glob-style wildcards.

        Returns:
            The created selection with :attr:`TagSelection.metadata` containing the
            metadata.

        Raises:
            ValueError: if any of the given ``paths`` is None or invalid.
            ValueError: if ``paths`` contains duplicate paths.
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        

#### `def open_selection_async(self, paths: List[str]) -> Awaitable[tbase.TagSelection]`

Asynchronously query the server for the metadata for the given tag ``paths``
        and return the results in a :class:`TagSelection`.

        Args:
            paths: The paths of the tags to include in the selection. May include
                glob-style wildcards.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created selection with :attr:`TagSelection.metadata` containing the
            metadata.

        Raises:
            ValueError: if any of the given ``paths`` is None or invalid.
            ValueError: if ``paths`` contains duplicate paths.
            ValueError: if ``paths`` is None.
            ApiException: if the API call fails.
        

#### `def open(self, path: str, data_type: tbase.DataType | None=None, *, create: bool | None=None) -> tbase.TagData`

Query the server for the metadata of a tag, optionally creating it if it doesn't already exist.

        If ``data_type`` is provided, ``create`` defaults to True. If ``data_type`` is
        not provided, ``create`` cannot be set to True.

        The call fails if the tag already exists as a different data type than specified
        or if it doesn't exist and ``create`` is False.

        Args:
            path: The path of the tag to open.
            data_type: The expected data type of the tag.
            create: True to create the tag if it doesn't already exist, False to fail if
                it doesn't exist.

        Returns:
            Information about the tag.

        Raises:
            ValueError: if ``path`` is None or empty.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``create`` is True, but ``data_type`` is None.
            ApiException: if the API call fails.
        

#### `async def open_async(self, path: str, data_type: tbase.DataType | None=None, *, create: bool | None=None) -> tbase.TagData`

Asynchronously query the server for the metadata of a tag, optionally
        creating it if it doesn't already exist.

        The call fails if the tag already exists as a different data type than specified
        or if it doesn't exist and ``create`` is False.

        Args:
            path: The path of the tag to open.
            data_type: The expected data type of the tag.
            create: True to create the tag if it doesn't already exist, False to fail if
                it doesn't exist.

        Returns:
            A task representing the asynchronous operation. On success, contains
            information about the tag.

        Raises:
            ValueError: if ``path`` is None or empty.
            ValueError: if ``data_type`` is invalid.
            ValueError: if ``create`` is True, but ``data_type`` is None.
            ApiException: if the API call fails.
        

#### `def refresh(self, tags: List[tbase.TagData]) -> None`

Populate the given ``tags`` with the latest metadata from the server.

        Only the :attr:`TagData.path` needs to be initialized. Tags that don't exist on
        the server will have their :attr:`TagData.data_type` set to
        :attr:`DataType.UNKNOWN`.

        Args:
            tags: The tags to refresh.

        Raises:
            ValueError: if any ``tags`` are None or have invalid paths.
            ValueError: if ``tags`` is None.
            ApiException: if the API call fails.
        

#### `async def refresh_async(self, tags: List[tbase.TagData]) -> None`

Asynchronously populate the given ``tags`` with the latest metadata from the server.

        Only the :attr:`TagData.path` needs to be initialized. Tags that don't exist on
        the server will have their :attr:`TagData.data_type` set to
        :attr:`DataType.UNKNOWN`.

        Args:
            tags: The tags to refresh.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if any ``tags`` are None or have invalid paths.
            ValueError: if ``tags`` is None.
            ApiException: if the API call fails.
        

#### `def _prepare_refresh(self, tags: List[tbase.TagData]) -> str`

#### `def _handle_refresh(self, tags: List[tbase.TagData], refresh_result: Dict[str, Any], http_response: HttpResponse) -> None`

#### `def query(self, paths: Sequence[str] | None=None, keywords: Iterable[str] | None=None, properties: Dict[str, str] | None=None, *, skip: int=0, take: int | None=None) -> tbase.TagQueryResultCollection`

Query the server for available tags matching the given criteria.

        Args:
            paths: List of tag paths to include in the result. May include glob-style
                wildcards.
            keywords: List of keywords that tags must have, or None.
            properties: Mapping of properties and their values that tags must have, or
                None.
            skip: The number of tags to initially skip in the results.
            take: The number of tags to include in each page of results.

        Returns:
            A :class:`TagQueryResultCollection` containing the first page of results.
            Enumerating the collection will retrieve additional pages according to the
            ``take`` parameter.

        Raises:
            ValueError: if ``skip`` or ``take`` is negative.
            ValueError: if ``paths`` is an empty list.
            ValueError: if any of ``paths`` are None.
            ApiException: if the API call fails.
        

#### `async def query_async(self, paths: Sequence[str] | None=None, keywords: Iterable[str] | None=None, properties: Dict[str, str] | None=None, *, skip: int=0, take: int | None=None) -> tbase.AsyncTagQueryResultCollection`

Asynchronously query the server for available tags matching the given criteria.

        Args:
            paths: List of tag paths to include in the result. May include glob-style
                wildcards.
            keywords: List of keywords that tags must have, or None.
            properties: Mapping of properties and their values that tags must have, or
                None.
            skip: The number of tags to initially skip in the results.
            take: The number of tags to include in each page of results.

        Returns:
            A task representing the asynchronous operation. On success, contains a
            :class:`TagQueryResultCollection` containing the first page of results.
            Enumerating the collection will retrieve additional pages according to the
            ``take`` parameter.

        Raises:
            ValueError: if ``skip`` is negative.
            ValueError: if ``take`` is negative.
            ApiException: if the API call fails.
        

#### `def _prepare_query(self, paths: Sequence[str] | None, keywords: Iterable[str] | None, properties: Dict[str, str] | None, skip: int | None, take: int | None=None) -> Tuple[str | None, str | None, str | None]`

#### `def update(self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]) -> None`

Update the metadata of one or more tags on the server, creating tags that don't exist.

        If ``updates`` contains :class:`TagData` objects, existing metadata will be
        replaced. If ``updates`` contains :class:`TagDataUpdate` objects instead, tags
        that already exist will have their existing keywords, properties, and settings
        merged with those specified in the corresponding :class:`TagDataUpdate`.

        The call fails if any of the tags already exist as a different data type.

        Args:
            updates: The tags to update (if :class:`TagData` objects are given), or the
                tag metadata updates to send (if :class:`TagDataUpdate` objects are
                given).

        Raises:
            ValueError: if ``updates`` is None or empty.
            ValueError: if ``updates`` contains any invalid tags.
            ValueError: if ``updates`` contains both ``TagData`` objects and
                ``TagDataUpdate`` objects.
            ApiException: if the API call fails.
        

#### `async def update_async(self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]) -> None`

Asynchronously update the metadata of one or more tags on the server, creating tags that don't exist.

        If ``updates`` contains :class:`TagData` objects, existing metadata will be
        replaced. If ``updates`` contains :class:`TagDataUpdate` objects instead, tags
        that already exist will have their existing keywords, properties, and settings
        merged with those specified in the corresponding :class:`TagDataUpdate`.

        Args:
            updates: The tags to update (if :class:`TagData` objects are given), or the
                tag metadata updates to send (if :class:`TagDataUpdate` objects are
                given).

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``updates`` is None or empty.
            ValueError: if ``updates`` contains any invalid tags.
            ValueError: if ``updates`` contains both ``TagData`` objects and
                ``TagDataUpdate`` objects.
            ApiException: if the API call fails.
        

#### `def _prepare_update(self, updates: Sequence[tbase.TagData] | Sequence[tbase.TagDataUpdate]) -> Tuple[List[Dict[str, Any]], bool]`

#### `def delete(self, tags: Iterable[tbase.TagData | str]) -> None`

Delete one or more tags from the server.

        Args:
            tags: The tags (or tag paths) to delete.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if ``tags`` contains any invalid tags.
            ApiException: if the API call fails.
        

#### `def delete_async(self, tags: Iterable[tbase.TagData | str]) -> Awaitable[None]`

Asynchronously delete one or more tags from the server.

        Args:
            tags: The tags (or tag paths) to delete.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if ``tags`` contains any invalid tags.
            ApiException: if the API call fails.
        

#### `def _perform_delete(self, paths: List[str]) -> None`

#### `async def _perform_delete_async(self, paths: List[str]) -> None`

#### `def create_writer(self, *, buffer_size: int | None=None, max_buffer_time: datetime.timedelta | None=None) -> tbase.BufferedTagWriter`

Create a tag writer that buffers tag values until
        :meth:`~BufferedTagWriter.send_buffered_writes()` is called on the returned
        object, ``buffer_size`` writes have been buffered, or ``max_buffer_time`` time
        has past since buffering a value, at which point the writes will be sent
        automatically.

        Args:
            buffer_size: The maximum number of tag writes to buffer before automatically
                sending them to the server.
            max_buffer_time: The amount of time before writes are sent.

        Returns:
            The created writer. Close the writer to free resources.

        Raises:
            ValueError: if ``buffer_size`` and ``max_buffer_time`` are both None.
            ValueError: if ``buffer_size`` is less than one.
        

#### `def _read(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, along with timestamp and/or aggregates, if
            requested, or None if the tag exists but doesn't have a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ApiException: if the API call fails.
        

#### `async def _read_async(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

Asynchronously retrieve the current value of the tag with the given ``path`` from the server.

        Optionally retrieves the aggregate values as well. The tag must exist. Clients
        do not typically call this method directly. Use a :class:`.TagValueReader`
        instead.

        Args:
            path: The path of the tag to read.
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value serialized as a string, or None if the tag exists but doesn't have
            a value.

        Raises:
            ValueError: if ``path`` is empty or invalid.
            ValueError: if ``path`` is None.
            ApiException: if the API call fails.
        

#### `def _handle_read(self, path: str, response: Dict[str, Any], http_response: HttpResponse, include_timestamp: bool | None=False, include_aggregates: bool | None=False) -> SerializedTagWithAggregates | None`

#### `def invalid_response(cls, response: HttpResponse) -> core.ApiException`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_path_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_path_utilities.py

### MODULE DOCSTRING

Implementation of TagPathUtilities.

### `class TagPathUtilities()`

Contains helper methods for interacting with tag paths.

#### `def __init_subclass__(cls) -> None`

#### `def __init__(self) -> None`

#### `def validate(cls, path: str) -> str`

Validate ``path`` as an input tag path.

        Clients do not typically need to call this method directly.

        Args:
            path: The tag path to validate.

        Returns:
            The validated path.

        Raises:
            ValueError: if the path is invalid.
            ValueError: if ``path`` is None.
        

#### `def validate_query(cls, path: str) -> str`

Validate ``path`` as a tag path query.

        Clients do not typically need to call this method directly.

        Args:
            path: The tag path to validate.

        Returns:
            The validated path.

        Raises:
            ValueError: if the path is invalid.
            ValueError: if ``path`` is None.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_query_result_collection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_query_result_collection.py

### MODULE DOCSTRING

Implementation of TagQueryResultCollection.

### `class TagQueryResultCollection(abc.ABC)`

Represents a paginated list of tags returned by a query.

    Iterating over the collection makes additional server requests to retrieve pages
    after the first.
    

#### `def __init__(self, first_page: List[tbase.TagData], total_count: int, skip: int) -> None`

Initialize an instance with the first page of query results.

        Args:
            first_page: The first page of results, or None if there are no results.
            total_count: The total number of results in the query.
            skip: The skip used for the first page of results.
        

#### `def total_count(self) -> int`

The total number of tags matched by the query at the time the query was made.

#### `def __iter__(self) -> Iterable[List[tbase.TagData]]`

Enumerate over the pages of tag query results.

        Calls to ``next(iter())`` may throw :class:`.ApiException`.

        Returns:
            The created enumerator.
        

#### `def _query_page(self, skip: int) -> List[tbase.TagData]`

Query for a single page of results and updates :attr:`total_count`.

        Args:
            skip: The skip to use in the query.

        Returns:
            The page of results, or None if there are no more results.

        Raises:
            ApiException: if the API call fails.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_selection.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_selection.py

### MODULE DOCSTRING

Implementation of TagSelection.

### `class TagSelection(tbase.ITagReader)`

Represents a set of tags that can be read, written, or deleted together.

    Tags may be specified using glob-style wildcards to include multiple tags with a
    common path. Call :meth:`close()` to free resources. Tag reads are buffered, and the
    latest values are only retrieved on first read or by calling
    :meth:`refresh_values()`. Reads for tags that aren't in the selection return None,
    even if the tag exists on the server.

    Note that :class:`TagSelection` objects support using the ``with`` statement (or the
    ``async with`` statement), to :meth:`close()` the selection automatically on exit.
    

#### `def __init__(self, tags: Sequence[tbase.TagData], paths: Sequence[str] | None=None) -> None`

Initialize a selection using queried or existing tag data.

        Args:
            tags: The tags to store in the selection.
            paths: The paths used to query the tags. If left as None, the paths will be
                extracted from ``tags``.

        Raises:
            ValueError: if ``tags`` is None or empty.
            ValueError: if ``tags`` or ``paths`` contains duplicate tags.
        

#### `def paths(self) -> Tuple[str, ...]`

The paths of all tags in the selection, including those that do not exist on the server.

        When using wildcards, the original paths with the wildcards are included in the
        list, not the paths matched by the wildcards.
        

#### `def metadata(self) -> Dict[str, tbase.TagData]`

The most recently retrieved metadata for tags in the selection, indexed by :attr:`TagData.path`.

        Tags in the selection that do not exist on the server will not appear in the
        collection. Call :meth:`refresh_metadata()` to update the data contained in the
        collection.
        

#### `def values(self) -> Dict[str, tbase.TagValueReader]`

A :class:`.TagValueReader` for reading the most recently retrieved value for
        tags in the selection, indexed by :attr:`.TagValueReader.path`.

        Tags in the selection that do not exist on the server will not appear in the
        collection. Readers for tags without values on the server will return None when
        read. Call :meth:`refresh_values()` to update the values returned by the readers
        in the dictionary.
        

#### `def _close_internal(self) -> None`

Clean up server resources associated with the selection.

#### `async def _close_internal_async(self) -> None`

Asynchronously clean up server resources associated with the selection.

        Returns:
            A task representing the asynchronous operation.
        

#### `def _create_subscription_internal(self, update_interval: datetime.timedelta | None=None) -> tbase.TagSubscription`

Subscribe to receive events when tags in the selection are written to using the specified update interval.

        Args:
            update_interval: How often to receive tag update notifications from the
                server, or None to use the default.

        Returns:
            The created subscription.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _create_subscription_internal_async(self, update_interval: datetime.timedelta | None=None) -> tbase.TagSubscription`

Asynchronously subscribe to receive events when tags in the selection are
        written to using the specified update interval.

        Args:
            update_interval: How often to receive tag update notifications from the
                server, or None to use the default.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created subscription.

        Raises:
            ApiException: if the API call fails.
        

#### `def _delete_tags_from_server_internal(self) -> None`

Delete all tags in the selection from the server.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _delete_tags_from_server_internal_async(self) -> None`

Asynchronously delete all tags in the selection from the server.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        

#### `def _read_tag_metadata(self) -> List[tbase.TagData]`

Retrieve the metadata of all tags in the selection.

        Returns:
            The list of tag metadata.

        Raises:
            ApiException: if the API call fails.
        

#### `def _read_tag_values(self) -> List[SerializedTagWithAggregates | None]`

Retrieve the values of all tags in the selection.

        Returns:
            The list of the tag values.

        Raises:
            ApiException: if the API call fails.
        

#### `def _read_tag_metadata_and_values(self) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]`

Retrieve the metadata and values of all tags in the selection.

        Returns:
            A tuple with the list of tag metadata and the list of tag values.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _read_tag_metadata_async(self) -> List[tbase.TagData]`

Asynchronously retrieve the metadata of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains the
            list of tag metadata.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _read_tag_values_async(self) -> List[SerializedTagWithAggregates | None]`

Asynchronously retrieve the values of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains the
            list of the tag values.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _read_tag_metadata_and_values_async(self) -> Tuple[List[tbase.TagData], List[SerializedTagWithAggregates | None]]`

Asynchronously retrieve the metadata and values of all tags in the selection.

        Returns:
            A task representing the asynchronous operation. When complete, contains a
            tuple with the list of tag metadata and the list of tag values.

        Raises:
            ApiException: if the API call fails.
        

#### `def _reset_aggregates_internal(self) -> None`

Reset the aggregate values of tags in the selection.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _reset_aggregates_internal_async(self) -> None`

Asynchronously reset the aggregate values of tags in the selection.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        

#### `def _on_paths_changed(self) -> None`

Note when the contents of :attr:`paths` is modified.

        The default implementation does nothing.
        

#### `def add_tags(self, tags: List[tbase.TagData]) -> None`

Add one or more tags to the selection.

        Tags that are already in the selection are ignored. The tags as given are
        immediately available in the :attr:`metadata` collection. Use
        :meth:`refresh_metadata()` to get the latest data for the tags. The tags will be
        available in the :attr:`values` collection but won't have latest a latest value
        until :meth:`refresh_values()` is called.

        Args:
            tags: The tags to add to the selection.

        Raises:
            ValueError: if any of the given tags are None or have an invalid path.
            ValueError: if ``tags`` is None.
            ReferenceError: if the selection has been closed.
        

#### `def clear_tags(self) -> None`

Remove all tags from the selection.

        Raises:
            ReferenceError: if the selection has been closed.
        

#### `def close(self) -> None`

Clean up server resources associated with the selection.

#### `async def close_async(self) -> None`

Asynchronously clean up server resources associated with the selection.

        Returns:
            A task representing the asynchronous operation.
        

#### `def create_subscription(self, *, update_interval: datetime.timedelta | None=None) -> tbase.TagSubscription`

Subscribe to receive events when tags in the selection are written to.

        Updates will be queried from the server using the specified or default update
        interval.

        The subscription will include any tags that are currently included in the
        selection when the subscription is created. That list can be seen via the
        :attr:`metadata` property. The subscription will also attempt to include any
        non-wildcard paths that are in the selection's current list of :attr:`paths`.
        Often, the list of :attr:`paths` directly coincides with the :attr:`metadata`,
        but the former may contain paths that did not exist when the selection's
        metadata was last updated from the server, e.g. via :meth:`refresh()`.

        Closing, adding tags, or removing tags from the selection will not affect
        previously created subscriptions.

        Args:
            update_interval: How often to receive tag updates notifications from the
                server. Default is ``datetime.timedelta(seconds=30)``.

        Returns:
            The created subscription.

        Raises:
            ValueError: if update_interval is negative.
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def create_subscription_async(self, *, update_interval: datetime.timedelta | None=None) -> Awaitable[tbase.TagSubscription]`

Asynchronously subscribe to receive events when tags in the selection are written to.

        Updates will be queried from the server using the specified or default update
        interval.

        Closing, adding tags, or removing tags from the selection will not affect
        previously created subscriptions.

        Args:
            update_interval: How often to receive tag updates notifications from the
                server. Depending on the :class:`TagManager` implementation in use, this
                may involve polling the server or have a minimum value.

        Returns:
            A task representing the asynchronous operation. On success, contains the
            created subscription.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def delete_tags_from_server(self) -> None`

Delete all tags in the selection from the server.

        The tags are not removed from the selection but are removed from
        :attr:`metadata` and :attr:`values`. If any of the tags are recreated, a call to
        :meth:`refresh_metadata()` will restore them in the collection of tags.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `async def delete_tags_from_server_async(self) -> None`

Asynchronously delete all tags in the selection from the server.

        The tags are not removed from the selection but are removed from
        :attr:`metadata` and :attr:`values`. If any of the tags are recreated, a call to
        :meth:`refresh_metadata()` will restore them in the collection of tags.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def open_tags(self, paths: List[str]) -> None`

Add one or more tags to the selection by path.

        Tags that are already in the selection are ignored. The tags will not be
        available in the :attr:`metadata` collection until :meth:`refresh_metadata()` is
        called or the :attr:`values` collection until :meth:`refresh_values()` is
        called.

        Args:
            paths: The tag paths to add to the selection. May include glob-style
                wildcards.

        Raises:
            ValueError: if any of the given paths are None or invalid.
            ValueError: if ``paths`` is None.
            ReferenceError: if the selection has been closed.
        

#### `def refresh(self) -> None`

Refresh both :class:`TagData` and current values for all tags in the
        selection, updating :attr:`metadata` and :attr:`values` accordingly.

        Call :meth:`refresh_metadata()` or :meth:`refresh_values()` to only partially
        refresh.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `async def refresh_async(self) -> None`

Asynchronously refresh both the :class:`TagData` and current values for all
        tags in the selection, updating :attr:`metadata` and :attr:`values` accordingly.

        Call :meth:`refresh_metadata_async()` or :meth:`refresh_values_async()` to only
        partially refresh.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def refresh_metadata(self) -> None`

Refresh the :class:`TagData` for all tags in the selection, updating :attr:`metadata` accordingly.

        :attr:`values` will also be updated with new and removed tags, but those readers
        will continue to return previously available values until
        :meth:`refresh_values()` is called.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `async def refresh_metadata_async(self) -> None`

Asynchronously refresh the :class:`TagData` for all tags in the selection,
        updating :attr:`metadata` accordingly.

        :attr:`values` will also be updated with new and removed tags, but those readers
        will continue to return previously available values until
        :meth:`refresh_values()` is called.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def refresh_values(self) -> None`

Refresh the current value of tags in the selection returned by the readers in the :attr:`values` collection.

        Readers will return None for tags that no longer exist on the server, or exist
        but haven't yet been written to. New readers will be added to the collection for
        tags that have values but have not yet been added to :attr:`metadata` by a call
        to :meth:`refresh_metadata()`.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `async def refresh_values_async(self) -> None`

Asynchronously refresh the current value of tags in the selection returned by
        the readers in the :attr:`values` collection.

        Readers will return None for tags that no longer exist on the server, or exist
        but haven't yet been written to. New readers will be added to the collection for
        tags that have values but have not yet been added to :attr:`metadata` by a call
        to :meth:`refresh_metadata()`.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def remove_tags(self, tags: List[tbase.TagData | str]) -> None`

Remove one or more tags from the selection.

        The tags are not removed from the :attr:`metadata` and :attr:`values`
        collections until the next :meth:`refresh_metadata()`.

        Tags not in the selection are ignored. Tags that were added to the selection
        using wildcard paths can only be removed by including the same wildcard paths.
        Tags matched by multiple wildcard paths remain in the selection until all of the
        paths are removed.

        Args:
            tags: The tags to remove from the selection. Either strings (paths) or
                :class:`TagData` objects can be given. For :class:`TagData` objects,
                only the :attr:`TagData.path` is used.

        Raises:
            ValueError: if ``tags`` is None.
            ValueError: if any of the given tags are None or have an invalid path.
            ReferenceError: if the selection has been closed.
        

#### `def reset_aggregates(self) -> None`

Reset tag value aggregates on the server for all tags in the selection.

        Tag historical values are not modified. Has no effect on tags that are not set
        to :attr:`TagData.collect_aggregates`. Use :meth:`refresh_values()` to retrieve
        the new aggregates.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def reset_aggregates_async(self) -> Awaitable[None]`

Asynchronously reset tag value aggregates on the server for all tags in the selection.

        Tag historical values are not modified. Has no effect on tags that are not set
        to :attr:`TagData.collect_aggregates`. Use :meth:`refresh_values()` to retrieve
        the new aggregates.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ReferenceError: if the selection has been closed.
            ApiException: if the API call fails.
        

#### `def __enter__(self) -> 'TagSelection'`

#### `async def __aenter__(self) -> 'TagSelection'`

#### `def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None`

Clean up resources associated with the selection.

#### `def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Awaitable[None]`

Asynchronously clean up resources associated with the selection.

#### `def __del__(self) -> None`

Finalize resources associated with the selection.

#### `def _read(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

#### `async def _read_async(self, path: str, include_timestamp: bool, include_aggregates: bool) -> SerializedTagWithAggregates | None`

#### `def _create_value_reader(self, tag: tbase.TagData) -> tbase.TagValueReader | None`

#### `def _update_metadata(self, metadata: List[tbase.TagData]) -> None`

#### `def _update_values(self, values: List[SerializedTagWithAggregates | None]) -> None`

#### `def _validate_paths(cls, paths: List[str]) -> List[str]`

Validate that the given tag paths are valid for queries.

        Args:
            paths: The paths to validate.

        Returns:
            The validated paths.

        Raises:
            ValueError: if any of the given paths are None or invalid.
            ValueError: if ``paths`` is None.
        

#### `def _validate_tags(cls, tags: List[tbase.TagData]) -> List[tbase.TagData]`

Validate that the given tags have valid paths.

        Args:
            tags: The tags to validate.

        Returns:
            The validated tags.

        Raises:
            ValueError: if any of the given tags are None or have an invalid path.
            ValueError: if ``tags`` is None.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_subscription.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_subscription.py

### MODULE DOCSTRING

Implementation of TagSubscription.

### `class TagSubscription(events.Events, abc.ABC)`

Represents a subscription for changes to one or more tags' values.

    Call :meth:`close()` to stop receiving events.

    Note that :class:`TagSubscription` objects support using the ``with`` statement (or
    the ``async with`` statement), to :meth:`close()` the subsription automatically on
    exit.

    Attributes:
        tag_changed: An event that is triggered when one of the subscription's tag
            changes. The callback will receive a :class:`TagData` parameter and an
            :class:`Optional` [:class:`TagValueReader`] parameter.

            Example::

                def my_callback(tag: TagData, reader: TagValueReader | None):
                    print("{} changed".format(tag.path))
                    if reader is None:
                        print(" - unknown data type")
                    else:
                        value = reader.read()
                        assert value is not None
                        print(" - new value: {}".format(value.value))

                subscription.tag_changed += my_callback
    

#### `def __init__(self, paths: Iterable[str], heartbeat_timer: ManualResetTimer | None) -> None`

Initialize the instance.

        Derived types must call :meth:`_initialize()` or :meth:`_initialize_async()`
        after construction.

        Args:
            paths: The tag path queries to include in the subscription.
            heartbeat_timer: A timer for sending a heartbeat to keep the subscription
                alive for testing purposes, or None to use a default timer.

        Raises:
            ValueError: if ``paths`` is None.
        

#### `def __del__(self) -> None`

#### `def _initialize(self) -> None`

Create and initialize the subscription.

        Derived types must call this method or :meth:`_initialize_async()` after
        construction to create and keep the subscription alive.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _initialize_async(self) -> None`

Asynchronously create and initializes the subscription.

        Derived types must call this method or :meth:`_initialize()` after construction
        to create and keep the subscription alive.

        Raises:
            ApiException: if the API call fails.
        

#### `def _create_subscription_on_server(self, paths: List[str]) -> None`

Create the subscription on the server.

        Implementations should retrieve and throw away the first set of updates before
        returning.

        Args:
            paths: The tag path queries to include in the subscription.

        Raises:
            ApiException: if the API call fails.
        

#### `async def _create_subscription_on_server_async(self, paths: List[str]) -> None`

Asynchronously create the subscription on the server.

        Implementations should retrieve and throw away the first set of updates before
        returning.

        Args:
            paths: The tag path queries to include in the subscription.

        Returns:
            A task representing the asynchronous operation.

        Raises:
            ApiException: if the API call fails.
        

#### `def _send_heartbeat(self) -> None`

Send a heartbeat for the subscription to keep it active.

        Raises:
            ApiException: if the API call fails.
        

#### `def _close_internal(self) -> None`

Clean up server resources associated with the subscription.

#### `async def _close_internal_async(self) -> None`

Asynchronously clean up server resources associated with the subscription.

        Returns:
            A task representing the asynchronous operation.
        

#### `def close(self) -> None`

Close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        

#### `async def close_async(self) -> None`

Asynchronously close server resources associated with the subscription.

        Further tag writes will not trigger new events.

        Returns:
            A task representing the asynchronous operation.
        

#### `def __enter__(self) -> 'TagSubscription'`

#### `async def __aenter__(self) -> 'TagSubscription'`

#### `def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None`

Close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        

#### `async def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None`

Asynchronously close server resources associated with the subscription.

        Further tag writes will not trigger new events.
        

#### `def _on_tag_changed(self, tag: tbase.TagData, value: tbase.TagValueReader | None) -> None`

Raise the :attr:`tag_changed` event.

        Args:
            tag: The tag that was changed.
            value: The new value and any associated information, or None if the tag has
                an unknown data type.
        

#### `def _heartbeat_timer_elapsed(self) -> None`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_update_fields.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_update_fields.py

### MODULE DOCSTRING

Implementation of TagUpdateFields.

### `class TagUpdateFields(enum.IntFlag)`

Represents the various :class:`TagData` fields that may be included in a :class:`TagDataUpdate`.

    Fields that aren't included are left unmodified when updates are sent to the server.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_value_reader.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_value_reader.py

### MODULE DOCSTRING

Implementation of TagValueReader.

### `class TagValueReader(Generic[_Any])`

Represents the ability to read a single tag's value using an :class:`ITagReader`.

#### `def __init__(self, reader: tbase.ITagReader, tag: tbase.TagData) -> None`

Initialize an instance.

        Args:
            reader: The :class:`ITagReader` to use when reading values.
            tag: The tag whose values will be read.
            path: The path of the tag whose values will be read.

        Raises:
            ValueError: if ``tag`` is not a tag of a valid data type and with a valid
                path.
        

#### `def data_type(self) -> tbase.DataType`

The data type of the tag associated with the value.

#### `def path(self) -> str`

The path of the tag associated with the value.

#### `def _reader(self) -> tbase.ITagReader`

The underlying :class:`ITagReader` for reading values.

#### `def read(self, *, include_timestamp: bool=False, include_aggregates: bool=False) -> tbase.TagWithAggregates[_Any] | None`

Read the current value of the tag.

        Args:
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ReferenceError: if the underlying reader has been closed.
            ApiException: if the API call fails.
        

#### `async def read_async(self, *, include_timestamp: bool=False, include_aggregates: bool=False) -> tbase.TagWithAggregates[_Any] | None`

Read the current value of the tag.

        Args:
            include_timestamp: True to include the timestamp associated with the value
                in the result.
            include_aggregates: True to include the tag's aggregate values in the result
                if the tag is set to :attr:`TagData.collect_aggregates`.

        Returns:
            The value, and the timestamp and/or aggregate values if requested, or None
            if the tag exists but doesn't have a value.

        Raises:
            ReferenceError: if the underlying reader has been closed.
            ApiException: if the API call fails.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_value_writer.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_value_writer.py

### MODULE DOCSTRING

Implementation of TagValueWriter.

### `class TagValueWriter(Generic[_Any])`

Represents the ability to write a single tag's value using an :class:`ITagWriter`.

#### `def __init__(self, writer: tbase.ITagWriter, tag: tbase.TagData) -> None`

Initialize an instance.

        Args:
            writer: The :class:`ITagWriter` to use when writing values.
            tag: The tag whose values will be written.
            path: The path of the tag whose values will be written.

        Raises:
            ValueError: if ``tag`` is not a tag of a valid type and with a valid path.
        

#### `def data_type(self) -> tbase.DataType`

The data type of the tag associated with the value.

#### `def path(self) -> str`

The path of the tag associated with the value.

#### `def _writer(self) -> tbase.ITagWriter`

The underlying :class:`ITagWriter` for writing values.

#### `def write(self, value: _Any, *, timestamp: datetime.datetime | None=None) -> None`

Write the tag's value.

        Args:
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ReferenceError: if the underlying writer has been closed.
            ApiException: if the API call fails.
        

#### `def write_async(self, value: _Any, *, timestamp: datetime.datetime | None=None) -> Awaitable[None]`

Write the tag's value.

        Args:
            value: The tag value to write.
            timestamp: A custom timestamp to associate with the value, or None to have
                the server specify the timestamp.

        Raises:
            ReferenceError: if the underlying writer has been closed.
            ApiException: if the API call fails.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/tag/_tag_with_aggregates.py -->
## PYTHON MODULE: nisystemlink/clients/tag/_tag_with_aggregates.py

### MODULE DOCSTRING

Implementation of TagWithAggregates.

- `_NUMERIC_TYPES = set((tbase.DataType.DOUBLE, tbase.DataType.INT32, tbase.DataType.UINT64))`

### `class TagWithAggregates(Generic[_Any])`

Represents a generic tag value with optional timestamp and optional aggregate values.

#### `def __init__(self, path: str, data_type: tbase.DataType, value: _Any, timestamp: datetime.datetime | None=None, count: int | None=None, min: int | float | None=None, max: int | float | None=None, mean: float | None=None) -> None`

Initialize an instance.

        Args:
            path: The path of the tag associated with the value.
            data_type: The data type of the value.
            value: The value.
            timestamp: The timestamp associated with the value.
            count: The number of times the tag has been written, or None if the tag is
                not collecting aggregates.
            min: The minimum value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a minimum value.
            max: The maximum value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a maximum value.
            mean: The mean value of the tag, or None if the tag is not collecting
                aggregates or the data type of the tag does not track a mean value.

        Raises:
            ApiException: if min, max, or mean is None when it shouldn't be or non-None
                when it should be

        :meta private:
        

#### `def data_type(self) -> tbase.DataType`

The data type of the value.

#### `def path(self) -> str`

The path of the tag associated with the value.

#### `def value(self) -> _Any`

The value of the tag.

#### `def timestamp(self) -> datetime.datetime | None`

The timestamp associated with the value, if available.

#### `def count(self) -> int | None`

The number of times the tag has been written, or None if the tag is not collecting aggregates.

#### `def min(self) -> int | float | None`

The minimum value of the tag, or None if the tag is not collecting aggregates
        or the data type of the tag does not track a minimum value.
        

#### `def max(self) -> int | float | None`

The maximum value of the tag, or None if the tag is not collecting aggregates
        or the data type of the tag does not track a maximum value.
        

#### `def mean(self) -> float | None`

The mean value of the tag, or None if the tag is not collecting aggregates or
        the data type of the tag does not track a mean value.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/__init__.py

### MODULE DOCSTRING

Start here with TestPlanClient for test plan management.

- `__all__ = ['TestPlanClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/_test_plan_client.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/_test_plan_client.py

### `class TestPlanClient(BaseClient)`

#### `def __init__(self, configuration: HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the WorkOrder Service.
        

#### `def get_test_plan(self, test_plan_id: str) -> models.TestPlan`

Retrieve a test plan by its ID.

        Args:
            test_plan_id: The ID of the test plan to retrieve.

        Returns:
            The TestPlan object corresponding to the given ID.
        

#### `def create_test_plans(self, test_plans: List[models.CreateTestPlanRequest]) -> models.CreateTestPlansPartialSuccessResponse`

Create a new test plan.

        Args:
            test_plan: The test plans to create.

        Returns:
            The created test plan object.
        

#### `def create_test_plan(self, test_plan: models.CreateTestPlanRequest) -> models.TestPlan`

Create a single test plan.

        Args:
            test_plan: The test plan to create.

        Returns:
            The created test plan.

        Raises:
            ApiException: if the test plan could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def delete_test_plans(self, ids: List[str]) -> None`

Delete test plans by IDs.

        Args:
            test_plan_ids: A list of test plan IDs to delete.

        Returns:
            None
        

#### `def query_test_plans(self, query_request: models.QueryTestPlansRequest) -> models.PagedTestPlans`

Query test plans.

        Args:
            query: The query to execute.

        Returns:
            A PagedTestPlans object containing test plans that match the query.
        

#### `def schedule_test_plans(self, schedule_request: models.ScheduleTestPlansRequest) -> models.ScheduleTestPlansResponse`

Schedule a test plan.

        Args:
            schedule: The schedule to apply to the test plan.

        Returns:
            A ScheduleTestPlansResponse object containing the scheduled test plan.
        

#### `def schedule_test_plan(self, test_plan: models.ScheduleTestPlanRequest, replace: bool | None=None) -> models.TestPlan`

Schedule a single test plan.

        Args:
            test_plan: The test plan schedule request.
            replace: Whether to replace the existing scheduled test plan.

        Returns:
            The scheduled test plan.

        Raises:
            ApiException: if the test plan could not be scheduled or the service returns an
                unexpected partial-success payload.
        

#### `def update_test_plans(self, update_request: models.UpdateTestPlansRequest) -> models.UpdateTestPlansResponse`

Update a test plan.

        Args:
            test_plan: The test plan to update.

        Returns:
            The updated test plan object.
        

#### `def update_test_plan(self, test_plan: models.UpdateTestPlanRequest, replace: bool | None=None) -> models.TestPlan`

Update a single test plan.

        Args:
            test_plan: The test plan to update.
            replace: Whether to replace the existing test plan instead of merging updates.

        Returns:
            The updated test plan.

        Raises:
            ApiException: if the test plan could not be updated or the service returns an
                unexpected partial-success payload.
        

#### `def create_test_plan_templates(self, test_plan_templates: List[models.CreateTestPlanTemplateRequest]) -> models.CreateTestPlanTemplatePartialSuccessResponse`

Creates one or more test plan template and return errors for failed creations.

        Args:
            test_plan_templates: A list of test plan templates to attempt to create.

        Returns: A list of created test plan templates, test plan templates that failed to create, and errors for
                 failures.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
                arguments.
        

#### `def create_test_plan_template(self, test_plan_template: models.CreateTestPlanTemplateRequest) -> models.TestPlanTemplate`

Creates a single test plan template.

        Args:
            test_plan_template: The test plan template to create.

        Returns:
            The created test plan template.

        Raises:
            ApiException: if the test plan template could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def query_test_plan_templates(self, query_test_plan_templates: models.QueryTestPlanTemplatesRequest) -> models.PagedTestPlanTemplates`

Queries one or more test plan templates and return errors for failed queries.

        Returns: A list of test plan templates, based on the query and errors for the wrong query.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
                arguments.
        

#### `def delete_test_plan_templates(self, ids: List[str]) -> models.DeleteTestPlanTemplatesPartialSuccessResponse | None`

Deletes one or more test plan templates and return errors for failed deletion.

        Returns:
            A partial success if any test plan templates failed to delete, or None if all
            test plan templates were deleted successfully.

        Raises: ApiException: if unable to communicate with the `/niworkorder` service of provided invalid
            arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_create_test_plan_request.py

### `class CreateTestPlanRequest(JsonModel)`

Represents the request body content for creating a test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_template_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_create_test_plan_template_request.py

### `class CreateTestPlanTemplateRequest(TestPlanTemplateBase)`

Contains information about a test plan template request.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plan_templates_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_create_test_plan_templates_partial_success_response.py

### `class CreateTestPlanTemplatePartialSuccessResponse(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_create_test_plans_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_create_test_plans_partial_success_response.py

### `class CreateTestPlansPartialSuccessResponse(JsonModel)`

Represents the response from creating test plans, including successfully created,
    failed test plans, and any associated errors.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_dashboard.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_dashboard.py

### `class Dashboard(JsonModel)`

Represents a dashboard reference.

### `class DashboardUrl(Dashboard)`

Definition and URL of the dashboard reference associated with this test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_delete_test_plan_templates_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_delete_test_plan_templates_partial_success_response.py

### `class DeleteTestPlanTemplatesPartialSuccessResponse(JsonModel)`

The result of deleting multiple test plan templates
    when one or more test plan templates could not be deleted.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_execution_definition.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_execution_definition.py

### `class Job(JsonModel)`

Represents a job to be executed, including its functions, arguments, and metadata.

### `class NotebookExecution(JsonModel)`

Defines the execution of a notebook.

### `class ManualExecution(JsonModel)`

Represents a manual execution definition.

### `class JobExecution(JsonModel)`

Defines the execution of one or more jobs.

### `class NoneExecution(JsonModel)`

Represents a definition where no execution is specified.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_execution_event.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_execution_event.py

### `class ExecutionEventBase(JsonModel)`

Base class for execution events, containing common attributes such as action.

### `class NotebookExecutionEvent(ExecutionEventBase)`

Represents an execution event that was triggered by a notebook execution.

### `class JobExecutionEvent(ExecutionEventBase)`

A concrete execution event that represents an event triggered by a job.

### `class ManualExecutionEvent(ExecutionEventBase)`

A concrete execution event that represents an event triggered manually.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_order_by.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_order_by.py

### `class OrderBy(Enum)`

The state of the test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_paged_test_plan_templates.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_paged_test_plan_templates.py

### `class PagedTestPlanTemplates(WithPaging)`

The response containing the list of products, total count of products and the continuation
    token if applicable.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_paged_test_plans.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_paged_test_plans.py

### `class PagedTestPlans(WithPaging)`

The response containing the list of products, total count of products and the continuation
    token if applicable.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_query_test_plan_templates_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_query_test_plan_templates_request.py

### `class TestPlanTemplateOrderBy(str, Enum)`

An enumeration by which test plan templates can be ordered/sorted.

### `class TestPlanTemplateField(str, Enum)`

Model for an object describing an test plan template with all of its properties.

### `class QueryTestPlanTemplatesRequest(WithPaging)`

Request information for the query test plan templates API.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_query_test_plans_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_query_test_plans_request.py

### `class TestPlanField(enum.Enum)`

Model for an object describing an test plan with all of its properties.

### `class QueryTestPlansRequest(WithPaging)`

Represents the request body for querying test plans.
    Allows filtering, sorting, and pagination of test plan results.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plan_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_schedule_test_plan_request.py

### `class ScheduleTestPlanRequest(JsonModel)`

Represents the request body content for scheduling a test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plans_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_schedule_test_plans_request.py

### `class ScheduleTestPlansRequest(JsonModel)`

Represents the request body for scheduling multiple test plans.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_schedule_test_plans_response.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_schedule_test_plans_response.py

### `class ScheduleTestPlansResponse(JsonModel)`

Represents the response returned after attempting to schedule one or more test plans.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_state.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_state.py

### `class State(Enum)`

The state of the test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_test_plan.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_test_plan.py

### `class TestPlan(JsonModel)`

Contains information about a test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_test_plan_templates.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_test_plan_templates.py

### `class TestPlanTemplateBase(JsonModel)`

Contains information about a test plan template.

### `class TestPlanTemplate(TestPlanTemplateBase)`

Contains response information for test plan template.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plan_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_update_test_plan_request.py

### `class UpdateTestPlanRequest(JsonModel)`

Represents the content for updating a single test plan.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plans_request.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_update_test_plans_request.py

### `class UpdateTestPlansRequest(JsonModel)`

Represents the request body for updating multiple test plans.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/test_plan/models/_update_test_plans_response.py -->
## PYTHON MODULE: nisystemlink/clients/test_plan/models/_update_test_plans_response.py

### `class UpdateTestPlansResponse(JsonModel)`

Represents the response after attempting to update test plans.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/__init__.py

### MODULE DOCSTRING

Start here with TestMonitorClient for test monitor operations.

- `__all__ = ['TestMonitorClient']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/_test_monitor_client.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/_test_monitor_client.py

### MODULE DOCSTRING

Implementation of TestMonitor Client

### `class TestMonitorClient(BaseClient)`

#### `def __init__(self, configuration: core.HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the TestMonitor Service.
        

#### `def api_info(self) -> models.ApiInfo`

Get information about the available API operations.

        Returns:
            Information about available API operations.

        Raises:
            ApiException: if unable to communicate with the `ni``/nitestmonitor``` service.
        

#### `def create_results(self, results: List[CreateResultRequest]) -> models.CreateResultsPartialSuccess`

Creates one or more results and returns errors for failed creations.

        Args:
            results: A list of results to attempt to create.

        Returns: A list of created results, results that failed to create, and errors for
            failures.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` service of provided invalid
                arguments.
        

#### `def create_result(self, result: CreateResultRequest) -> models.Result`

Creates a single result.

        Args:
            result: The result to create.

        Returns:
            The created result.

        Raises:
            ApiException: if the result could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def get_results(self, continuation_token: str | None=None, take: int | None=None, return_count: bool | None=None) -> models.PagedResults`

Reads a list of results.

        Args:
            continuation_token: The token used to paginate results.
            take: The number of results to get in this request.
            return_count: Whether or not to return the total number of results available.

        Returns:
            A list of results.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def get_result(self, id: str) -> models.Result`

Retrieves a single result by id.

        Args:
            id (str): Unique ID of a result.

        Returns:
            The single result matching `id`

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def query_results(self, query: models.QueryResultsRequest) -> models.PagedResults`

Queries for results that match the filter.

        Args:
            query : The query contains a DynamicLINQ query string in addition to other details
                about how to filter and return the list of results.

        Returns:
            A paged list of results with a continuation token to get the next page.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided invalid
                arguments.
        

#### `def query_result_values(self, query: models.QueryResultValuesRequest) -> List[str]`

Queries for results that match the query and returns a list of the requested field.

        Args:
            query : The query for the fields.

        Returns:
            A list of the values of the queried field.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service or provided
                invalid arguments.
        

#### `def update_results(self, results: List[UpdateResultRequest], replace: bool=False) -> models.UpdateResultsPartialSuccess`

Updates a list of results with optional field replacement.

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
        

#### `def update_result(self, result: UpdateResultRequest, replace: bool=False) -> models.Result`

Updates a single result.

        Args:
            result: The result to update.
            replace: Replace the existing fields instead of merging them.

        Returns:
            The updated result.

        Raises:
            ApiException: if the result could not be updated or the service returns an
                unexpected partial-success payload.
        

#### `def delete_result(self, id: str) -> None`

Deletes a single result by id.

        Args:
            id (str): Unique ID of a result.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def delete_results(self, ids: List[str]) -> models.DeleteResultsPartialSuccess | None`

Deletes multiple results.

        Args:
            ids (List[str]): List of unique IDs of results.

        Returns:
            A partial success if any results failed to delete, or None if all
            results were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the ``/nitestmonitor`` Service
                or provided an invalid argument.
        

#### `def create_steps(self, steps: List[models.CreateStepRequest], update_result_total_time: bool=False) -> models.CreateStepsPartialSuccess`

Creates one or more steps.

        Args:
            steps: A list of steps to create.
            update_result_total_time: Determine test result total time from the step total times.
                Defaults to False.

        Returns:
            A list of steps that were successfully created and ones that failed to be created.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        

#### `def create_step(self, step: models.CreateStepRequest, update_result_total_time: bool=False) -> models.Step`

Creates a single step.

        Args:
            step: The step to create.
            update_result_total_time: Determine test result total time from the step total times.

        Returns:
            The created step.

        Raises:
            ApiException: if the step could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def delete_steps(self, steps: List[models.StepIdResultIdPair]) -> models.DeleteStepsPartialSuccess | None`

Deletes one or more steps by global ID.

        Args:
            steps: A list of step IDs and result IDs. Note that these are the global IDs and not the
            `step_id` that is local to a product and workspace.

        Returns:
            None if all deletes succeed otherwise a list of which IDs failed and which succeeded.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there
            invalid arguments.
        

#### `def delete_step(self, result_id: str, step_id: str, update_result_total_time: bool | None=False) -> None`

Deletes a single step.

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
        

#### `def query_steps(self, query: models.QueryStepsRequest) -> models.PagedSteps`

Queries for steps that match the filters.

        Args:
            query: The query contains a product ID as well as a filter for steps under that product.

        Returns:
            A list of steps that match the filter.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        

#### `def update_steps(self, steps: List[models.UpdateStepRequest], update_result_total_time: bool=False, replace_keywords: bool=False, replace_properties: bool=False) -> models.UpdateStepsPartialSuccess`

Updates one or more steps.

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
        

#### `def update_step(self, step: models.UpdateStepRequest, update_result_total_time: bool=False, replace_keywords: bool=False, replace_properties: bool=False) -> models.Step`

Updates a single step.

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
        

#### `def get_steps(self, continuation_token: str | None=None, take: int | None=None, return_count: bool | None=None) -> models.PagedSteps`

Reads a list of steps.

        Args:
            continuation_token: The token used to paginate steps.
            take: The number of steps to get in this request.
            return_count: Whether or not to return the total number of steps available.

        Returns:
            A list of steps.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments..
        

#### `def get_step(self, result_id: str, step_id: str) -> models.Step`

Gets a single step.

        Args:
            result_id: The resultId of the step to get.
            step_id: The stepId of the step to get.

        Returns:
            The step.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        

#### `def query_step_values(self, query: models.QueryStepValuesRequest) -> List[str]`

Queries values for a step field.

        Args:
            query: The query parameters.

        Returns:
            A list of values for the specified step field.

        Raises:
            ApiException: if unable to communicate with the `/nitestmonitor` service or if there are
            invalid arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_api_info.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_api_info.py

### `class V2Operations(JsonModel)`

The operations available in the routes provided by the v2 HTTP API.

### `class ApiInfo(JsonModel)`

Information about the available API operations.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_result_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_create_result_request.py

### `class CreateResultRequest(JsonModel)`

Contains information about a result.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_results_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_create_results_partial_success.py

### `class CreateResultsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_steps_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_create_steps_partial_success.py

### `class CreateStepsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_create_steps_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_create_steps_request.py

### `class BaseStepRequest(JsonModel)`

### `class CreateStepRequest(BaseStepRequest)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_delete_results_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_delete_results_partial_success.py

### `class DeleteResultsPartialSuccess(JsonModel)`

The result of deleting multiple results when one or more results could not be deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_delete_steps_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_delete_steps_partial_success.py

### `class StepIdResultIdPair(JsonModel)`

### `class DeleteStepsPartialSuccess(JsonModel)`

The result of deleting multiple steps when one or more steps could not be deleted.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_named_value.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_named_value.py

### `class NamedValue(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_paged_results.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_paged_results.py

### `class PagedResults(WithPaging)`

The response for a Results query containing matched results.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_paged_steps.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_paged_steps.py

### `class PagedSteps(WithPaging)`

The response for a Steps query containing matched steps.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_query_results_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_query_results_request.py

### `class ResultField(str, Enum)`

The allowed field for which the values can be queried for.

### `class ResultOrderByField(str, Enum)`

The fields by which results can be ordered.

### `class ComparisonType(str, Enum)`

The valid ways to order a result query.

### `class ResultProjection(str, Enum)`

The allowed projections for query.

    When using projection, only the fields specified by the projection element will be included in
    the response.
    

### `class QueryResultsBase(JsonModel)`

Base class for result query requests.

### `class QueryProductsBase(JsonModel)`

Base class for product query requests.

### `class QueryResultsRequest(QueryResultsBase, QueryProductsBase, WithPaging)`

Request model for querying results.

### `class QueryResultValuesRequest(QueryResultsBase)`

Request model for querying result values.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_query_steps_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_query_steps_request.py

### `class StepOrderBy(str, Enum)`

The valid ways to order steps query response.

    This contains only limited fields available in a Step.
    

### `class StepField(str, Enum)`

The valid field values that can be queried.

    This contains only limited fields available in a Step.
    

### `class StepProjection(str, Enum)`

An enumeration of all fields in a Step.

    This enumeration is used to specify the fields to project in a step query.
    

### `class QueryStepsBase(JsonModel)`

### `class QueryStepsRequest(QueryStepsBase, WithPaging)`

### `class QueryStepValuesRequest(QueryStepsBase)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_result.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_result.py

### `class Result(JsonModel)`

Contains information about a result.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_status.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_status.py

### `class StatusType(str, Enum)`

The types of statuses that a result can have.

### `class Status(JsonModel)`

Contains information about a status object.

#### `def LOOPING() -> 'Status'`

#### `def SKIPPED() -> 'Status'`

#### `def DONE() -> 'Status'`

#### `def PASSED() -> 'Status'`

#### `def FAILED() -> 'Status'`

#### `def RUNNING() -> 'Status'`

#### `def WAITING() -> 'Status'`

#### `def TERMINATED() -> 'Status'`

#### `def ERRORED() -> 'Status'`

#### `def TIMED_OUT() -> 'Status'`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_step.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_step.py

### `class Step(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_step_data.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_step_data.py

### `class Measurement(JsonModel)`

### `class StepData(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_result_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_update_result_request.py

### `class UpdateResultRequest(JsonModel)`

Contains information about a result.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_results_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_update_results_partial_success.py

### `class UpdateResultsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_steps_partial_success.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_update_steps_partial_success.py

### `class UpdateStepsPartialSuccess(JsonModel)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/models/_update_steps_request.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/models/_update_steps_request.py

### `class UpdateStepRequest(BaseStepRequest)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/utilities/_dataframe_utilities.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/utilities/_dataframe_utilities.py

### `def has_name_and_measurement(measurement: Measurement) -> bool`

Checks if a step data parameter is measurement data by ensuring it has both
    'name' and 'measurement' fields.

    Args:
        measurement: A measurement data object

    Returns:
        bool: True if the measurement has both 'name' and 'measurement' fields, False otherwise.
    

### `def convert_results_to_dataframe(results: List[Result], set_id_as_index: bool=True) -> pd.DataFrame`

Creates a Pandas DataFrame for the results.

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
    

### `def convert_steps_to_dataframe(steps: List[Step], is_valid_measurement: Callable[[Measurement], bool] | None=has_name_and_measurement) -> pd.DataFrame`

Converts a list of steps into a normalized dataframe.

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
    

### `def __normalize_status(data: Dict[str, Any]) -> None`

Normalizes the status object into a string.

    Args:
        data: Dictionary containing status information.

    

### `def __format_results_columns(results_dataframe: pd.DataFrame) -> pd.DataFrame`

Format results column to keep properties at the end.

    Args:
        results_dataframe: Dataframe of results.

    Returns:
        Formatted dataframe of results.
    

### `def __is_standard_column_header(header: str) -> bool`

Check if column header is not status type summary or property.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header doesn't start with 'status_type_summary.', 'properties.'. Else returns false.

    

### `def __is_status_type_summary_header(header: str) -> bool`

Check if column header is not a status type summary.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header contains 'status_type_summary.'. Else returns false.

    

### `def __is_property_header(header: str) -> bool`

Check if column header is not a property.

    Args:
        header: column header for results dataframe.

    Returns:
        True if header contains 'properties.'. Else returns false.

    

### `def __convert_steps_to_dict(steps: List[Step], is_valid_measurement: Callable[[Measurement], bool] | None) -> List[Dict[str, Any]]`

Converts a list of steps to dictionaries, excluding None values.

    Args:
        steps: A list of steps.
        is_valid_measurement: Optional callback function that checks if a step data
            parameter is a valid measurement so that only those are included in the returned dataframe.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing step information.
    

### `def __filter_invalid_measurements(step_dict: Dict[str, Any], step: Step, is_valid_measurement: Callable[[Measurement], bool] | None) -> None`

Gets data parameters from the step dictionary and filters it based on the callback function.

    Args:
        step_dict: A dictionary with step information.
        step: A Step object containing data parameters.
        is_valid_measurement: Optional callback function to check if a measurement is valid. The method takes
            a Measurement as input and returns a boolean value. The default behavior is to consider only parameters
            that have both 'name' and 'measurement' fields with values as valid measurements.

    Returns:
        None: The function modifies step dictionary in place with filtered data parameters.
    

### `def __normalize_inputs_outputs(step_dict: Dict[str, Any], step: Step) -> None`

Normalizes the input and output fields by converting them into dictionaries.

    Args:
        step_dict: A dictionary with step information.
        step: A Step object containing inputs and outputs.

    Returns:
        None: The function modifies step_dict in place with normalized inputs and outputs.
    

### `def __explode_and_normalize(dataframe: pd.DataFrame, column: str, prefix: str) -> pd.DataFrame`

Explodes a specified column in the dataframe and normalizes its nested data.
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
    

### `def __group_step_columns(dataframe_columns: List[str]) -> List[str]`

Groups and orders dataframe columns into predefined categories to maintain a consistent structure.
    When normalizing steps into a dataframe, new input, output, or property fields may be added at the end,
    disrupting the expected column order. This function ensures columns are grouped properly.

    Args:
        dataframe_columns: The list of all columns from the normalized dataframe.

    Returns:
        List[str]: A list containing grouped and ordered columns.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/testmonitor/utilities/constants.py -->
## PYTHON MODULE: nisystemlink/clients/testmonitor/utilities/constants.py

### `class DataFrameHeaders()`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/__init__.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/__init__.py

### MODULE DOCSTRING

Start here with WorkItemClient for work item operations.

- `__all__ = ['WorkItemClient', 'WorkItemExecuteApiException']`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/_work_item_client.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/_work_item_client.py

### `class WorkItemExecuteApiException(core.ApiException)`

Raised when the execute work item API returns an error with a structured response body.

    The API may return partial results (e.g. cancelled job IDs) alongside an error.
    This exception exposes those results via the :attr:`result` property.
    

#### `def __init__(self, msg: str, *, http_status_code: int, error: core.ApiError | None, result: models.ExecutionResult | None) -> None`

#### `def result(self) -> models.ExecutionResult | None`

The partial execution result returned alongside the error, if any.

### `class WorkItemClient(BaseClient)`

#### `def __init__(self, configuration: HttpConfiguration | None=None)`

Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the WorkItem Service.
        

#### `def get_work_item(self, work_item_id: str) -> models.WorkItem`

Retrieves a work item by its ID.

        Args:
            work_item_id: The ID of the work item to retrieve.

        Returns:
            The work item corresponding to the given ID.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def create_work_items(self, work_items: List[models.CreateWorkItemRequest]) -> models.CreateWorkItemsPartialSuccessResponse`

Creates one or more work items.

        Args:
            work_items: A list of work items to create.

        Returns:
            A list of created work items, work items that failed to create, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def create_work_item(self, work_item: models.CreateWorkItemRequest) -> models.WorkItem`

Creates a single work item.

        Args:
            work_item: The work item to create.

        Returns:
            The created work item.

        Raises:
            ApiException: if the work item could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def query_work_items(self, query_work_items: models.QueryWorkItemsRequest) -> models.PagedWorkItems`

Queries one or more work items.

        Args:
            query_work_items: The query request for work items.

        Returns:
            A list of work items based on the query.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def schedule_work_items(self, schedule_work_items: models.ScheduleWorkItemsRequest) -> models.ScheduleWorkItemsPartialSuccessResponse`

Schedule work items.

        Args:
            schedule_work_items: The schedule request for work item.

        Returns:
            A list of scheduled work items, work items that failed to schedule, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def schedule_work_item(self, work_item: models.ScheduleWorkItemRequest, replace: bool | None=None) -> models.WorkItem`

Schedules a single work item.

        Args:
            work_item: The work item schedule request.
            replace: When true, existing array fields are replaced instead of merged.

        Returns:
            The scheduled work item.

        Raises:
            ApiException: if the work item could not be scheduled or the service returns an
                unexpected partial-success payload.
        

#### `def update_work_items(self, update_work_items: models.UpdateWorkItemsRequest) -> models.UpdateWorkItemsPartialSuccessResponse`

Updates one or more work items.

        Args:
            update_work_items: The update request containing work items to update.

        Returns:
            A list of updated work items, work items that failed to update, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def update_work_item(self, work_item: models.UpdateWorkItemRequest, replace: bool | None=None) -> models.WorkItem`

Updates a single work item.

        Args:
            work_item: The work item to update.
            replace: When true, existing array and key-value pair fields are replaced instead of merged.

        Returns:
            The updated work item.

        Raises:
            ApiException: if the work item could not be updated or the service returns an
                unexpected partial-success payload.
        

#### `def delete_work_items(self, ids: List[str]) -> models.DeleteWorkItemsPartialSuccessResponse | None`

Deletes one or more work items by IDs.

        Args:
            ids: A list of work item IDs to delete.

        Returns:
            A partial success if any work items failed to delete, or None if all
            work items were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def execute_work_item(self, work_item_id: str, action: str) -> models.ExecuteWorkItemResponse`

Executes the specified action for the work item.

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
        

#### `def _execute_work_item(self, work_item_id: str, action: str) -> models.ExecuteWorkItemResponse`

Internal implementation of execute_work_item.

#### `def create_work_item_templates(self, work_item_templates: List[models.CreateWorkItemTemplateRequest]) -> models.CreateWorkItemTemplatesPartialSuccessResponse`

Creates one or more work item templates.

        Args:
            work_item_templates: A list of work item templates to create.

        Returns:
            A list of created work item templates, templates that failed to create, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def create_work_item_template(self, work_item_template: models.CreateWorkItemTemplateRequest) -> models.WorkItemTemplate`

Creates a single work item template.

        Args:
            work_item_template: The work item template to create.

        Returns:
            The created work item template.

        Raises:
            ApiException: if the work item template could not be created or the service returns an
                unexpected partial-success payload.
        

#### `def query_work_item_templates(self, query_work_item_templates: models.QueryWorkItemTemplatesRequest) -> models.PagedWorkItemTemplates`

Queries one or more work item templates.

        Args:
            query_work_item_templates: The query request for work item templates.

        Returns:
            A list of work item templates based on the query.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def update_work_item_templates(self, update_work_item_templates: models.UpdateWorkItemTemplatesRequest) -> models.UpdateWorkItemTemplatesPartialSuccessResponse`

Updates one or more work item templates.

        Args:
            update_work_item_templates: The update request containing work item templates to update.

        Returns:
            A list of updated work item templates, templates that failed to update, and errors for failures.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

#### `def update_work_item_template(self, work_item_template: models.UpdateWorkItemTemplateRequest, replace: bool | None=None) -> models.WorkItemTemplate`

Updates a single work item template.

        Args:
            work_item_template: The work item template to update.
            replace: When true, existing key-value pair fields are replaced instead of merged.

        Returns:
            The updated work item template.

        Raises:
            ApiException: if the work item template could not be updated or the service returns an
                unexpected partial-success payload.
        

#### `def delete_work_item_templates(self, ids: List[str]) -> models.DeleteWorkItemTemplatesPartialSuccessResponse | None`

Deletes one or more work item templates.

        Args:
            ids: A list of work item template IDs to delete.

        Returns:
            A partial success if any work item templates failed to delete, or None if all
            work item templates were deleted successfully.

        Raises:
            ApiException: if unable to communicate with the `/niworkitem` service or provided invalid arguments.
        

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_create_work_item_request.py

### `class CreateWorkItemRequest(JsonModel)`

Represents the request body content for creating a work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_template_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_create_work_item_template_request.py

### `class CreateWorkItemTemplateRequest(WorkItemTemplateBase)`

Represents the request body content for creating a work item template.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_item_templates_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_create_work_item_templates_partial_success_response.py

### `class CreateWorkItemTemplatesPartialSuccessResponse(JsonModel)`

Response for creating work item templates with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_create_work_items_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_create_work_items_partial_success_response.py

### `class CreateWorkItemsPartialSuccessResponse(JsonModel)`

Response for creating work items with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_dashboard.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_dashboard.py

### `class Dashboard(JsonModel)`

Represents a dashboard reference.

### `class DashboardUrl(Dashboard)`

Definition and URL of the dashboard reference associated with this work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_delete_work_item_templates_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_delete_work_item_templates_partial_success_response.py

### `class DeleteWorkItemTemplatesPartialSuccessResponse(JsonModel)`

Response for deleting work item templates with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_delete_work_items_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_delete_work_items_partial_success_response.py

### `class DeleteWorkItemsPartialSuccessResponse(JsonModel)`

Response for deleting work items with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execute_work_item_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_execute_work_item_response.py

### `class ExecutionResultBase(JsonModel)`

Base class for execution results containing common attributes.

### `class NoneExecutionResult(ExecutionResultBase)`

Result of executing a work item action with no execution implementation.

### `class ManualExecutionResult(ExecutionResultBase)`

Result of executing a manual work item action.

### `class NotebookExecutionResult(ExecutionResultBase)`

Result of executing a notebook work item action.

### `class JobExecutionResult(ExecutionResultBase)`

Result of executing a job work item action.

### `class ScheduleExecutionResult(ExecutionResultBase)`

Result of executing a schedule work item action.

### `class UnscheduleExecutionResult(ExecutionResultBase)`

Result of executing an unschedule work item action.

### `class ExecuteWorkItemResponse(JsonModel)`

Response for executing a work item action.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execution_definition.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_execution_definition.py

### `class Job(JsonModel)`

Defines a job to be executed by a work item job execution.

### `class NotebookExecution(JsonModel)`

Defines a notebook execution for a work item.

### `class ManualExecution(JsonModel)`

Defines a manual execution for a work item.

### `class JobExecution(JsonModel)`

Defines a job execution for a work item.

### `class NoneExecution(JsonModel)`

Defines an unimplemented execution for a work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_execution_event.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_execution_event.py

### `class ExecutionEventBase(JsonModel)`

Base class for execution events containing common attributes.

### `class NotebookExecutionEvent(ExecutionEventBase)`

An event tracking a notebook execution triggered from a work item.

### `class JobExecutionEvent(ExecutionEventBase)`

An event tracking a job execution triggered from a work item.

### `class ManualExecutionEvent(ExecutionEventBase)`

An event tracking a manual execution triggered from a work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_paged_work_item_templates.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_paged_work_item_templates.py

### `class PagedWorkItemTemplates(WithPaging)`

The response containing the list of work item templates, total count and continuation token.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_paged_work_items.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_paged_work_items.py

### `class PagedWorkItems(WithPaging)`

The response containing the list of work items, total count and continuation token.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_query_work_item_templates_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_query_work_item_templates_request.py

### `class WorkItemTemplateField(str, Enum)`

Enumeration of work item template fields that can be projected in query results.

### `class WorkItemTemplateOrderBy(str, Enum)`

Enumeration of fields by which work item templates can be ordered.

### `class QueryWorkItemTemplatesRequest(JsonModel)`

Represents the request body content for querying work item templates.
    Allows filtering, sorting, and pagination of work item template results.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_query_work_items_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_query_work_items_request.py

### `class WorkItemField(str, Enum)`

Enumeration of work item fields that can be projected in query results.

### `class WorkItemOrderBy(str, Enum)`

Enumeration of fields by which work items can be ordered.

### `class QueryWorkItemsRequest(JsonModel)`

Represents the request body content for querying work items.
    Allows filtering, sorting, and pagination of work item results.
    

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_resources_definition.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_resources_definition.py

### `class ResourceSelectionDefinition(JsonModel)`

Selection metadata associated with the resource.

### `class SystemResourceSelectionDefinition(JsonModel)`

Selection metadata associated with the system resource.

### `class ResourceDefinition(JsonModel)`

Resource reserved for the work item.

### `class SystemResourceDefinition(JsonModel)`

System resource reserved for the work item.

### `class ResourcesDefinition(JsonModel)`

Resources reserved for the work item.

### `class TemplateResourceDefinition(JsonModel)`

Resource reserved for the work item created from a template.

### `class TemplateResourcesDefinition(JsonModel)`

Resources reserved for the work item created from a template.

### `class ScheduleResourceDefinition(JsonModel)`

Resource reserved for scheduling the work item.

### `class ScheduleSystemResourceDefinition(JsonModel)`

System resource reserved for scheduling the work item.

### `class ScheduleResourcesDefinition(JsonModel)`

Resources reserved for scheduling the work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_definition.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_schedule_definition.py

### `class ScheduleDefinition(JsonModel)`

Scheduling properties for the work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_item_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_schedule_work_item_request.py

### `class ScheduleWorkItemRequest(JsonModel)`

Represents the request body content for scheduling a single work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_items_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_schedule_work_items_partial_success_response.py

### `class ScheduleWorkItemsPartialSuccessResponse(JsonModel)`

Response for scheduling one or more work items.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_schedule_work_items_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_schedule_work_items_request.py

### `class ScheduleWorkItemsRequest(JsonModel)`

Represents the request body content for scheduling multiple work items.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_state.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_state.py

### `class State(Enum)`

The state of the work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_timeline_definition.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_timeline_definition.py

### `class TimelineDefinition(JsonModel)`

Timeline properties for the work item.

### `class TemplateTimelineDefinition(JsonModel)`

Timeline properties for the work item created from a template.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_item_request.py

### `class UpdateWorkItemRequest(JsonModel)`

Represents the request body content for updating a single work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_template_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_item_template_request.py

### `class UpdateWorkItemTemplateRequest(JsonModel)`

Represents the request body content for updating a single work item template.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_templates_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_item_templates_partial_success_response.py

### `class UpdateWorkItemTemplatesPartialSuccessResponse(JsonModel)`

Response for updating work item templates with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_item_templates_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_item_templates_request.py

### `class UpdateWorkItemTemplatesRequest(JsonModel)`

Represents the request body content for updating multiple work item templates.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_items_partial_success_response.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_items_partial_success_response.py

### `class UpdateWorkItemsPartialSuccessResponse(JsonModel)`

Response for updating work items with partial success.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_update_work_items_request.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_update_work_items_request.py

### `class UpdateWorkItemsRequest(JsonModel)`

Represents the request body content for updating multiple work items.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_work_item.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_work_item.py

### `class WorkItem(JsonModel)`

Contains information about a work item.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=nisystemlink/clients/work_item/models/_work_item_template.py -->
## PYTHON MODULE: nisystemlink/clients/work_item/models/_work_item_template.py

### `class WorkItemTemplateBase(JsonModel)`

Contains information about a work item template.

### `class WorkItemTemplate(WorkItemTemplateBase)`

Contains response information for work item template.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/anyorderlist.py -->
## PYTHON MODULE: tests/anyorderlist.py

### `class AnyOrderList()`

Sequence that compares to a list, but allows any order.

    This is only intended for comparison purposes, not as an actual list replacement.
    

#### `def __init__(self, list_)`

#### `def __eq__(self, other)`

#### `def __str__(self)`

#### `def __repr__(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_http_configuration.py -->
## PYTHON MODULE: tests/core/test_http_configuration.py

### MODULE DOCSTRING

Tests for HttpConfiguration.

### `class TestHttpConfiguration()`

Test cases for HttpConfiguration class.

#### `def test__valid_server_uri__initializes_correctly(self)`

Test that a valid server URI initializes the configuration correctly.

#### `def test__server_uri_with_port__preserves_port(self)`

Test that server URI with port preserves the port.

#### `def test__server_uri_with_path_and_query__strips_path_and_query(self)`

Test that path and query components are stripped from server URI.

#### `def test__api_key_authentication__sets_api_keys(self)`

Test that API key authentication sets the api_keys property.

#### `def test__username_password_authentication__sets_credentials(self)`

Test that username/password authentication sets credentials.

#### `def test__all_optional_parameters__sets_all_properties(self)`

Test that all optional parameters are set correctly.

#### `def test__missing_scheme__raises_value_error(self)`

Test that missing scheme in server URI raises ValueError.

#### `def test__missing_hostname__raises_value_error(self)`

Test that missing hostname in server URI raises ValueError.

#### `def test__username_without_password__raises_value_error(self)`

Test that username without password raises ValueError.

#### `def test__password_without_username__raises_value_error(self)`

Test that password without username raises ValueError.

#### `def test__timeout_milliseconds_property__getter_and_setter(self)`

Test timeout_milliseconds property getter and setter.

#### `def test__user_agent_property__getter_and_setter(self)`

Test user_agent property getter and setter.

#### `def test__verify_property__getter_and_setter(self)`

Test verify property getter and setter.

#### `def test__api_keys_property__returns_copy(self)`

Test that api_keys property returns a copy of the internal dictionary.

#### `def test__api_keys_property__returns_none_when_no_api_key(self)`

Test that api_keys property returns None when no API key is set.

#### `def test__server_uri_property__is_read_only(self)`

Test that server_uri property is read-only.

#### `def test__username_property__is_read_only(self)`

Test that username property is read-only.

#### `def test__password_property__is_read_only(self)`

Test that password property is read-only.

#### `def test__cert_path_property__is_read_only(self)`

Test that cert_path property is read-only.

#### `def test__workspace_property__is_read_only(self)`

Test that workspace property is read-only.

#### `def test__default_timeout_constant__has_expected_value(self)`

Test that the default timeout constant has the expected value.

#### `def test__http_scheme__is_accepted(self)`

Test that HTTP scheme is accepted.

#### `def test__case_insensitive_scheme__is_normalized_to_lowercase(self)`

Test that case-insensitive schemes are normalized to lowercase.

#### `def test__ipv4_address__is_accepted(self)`

Test that IPv4 addresses are accepted as hostnames.

#### `def test__ipv6_address__is_accepted(self)`

Test that IPv6 addresses are accepted as hostnames.

#### `def test__empty_api_key__does_not_set_api_keys(self)`

Test that empty API key does not set api_keys.

#### `def test__none_api_key__does_not_set_api_keys(self)`

Test that None API key does not set api_keys.

#### `def test__pathlib_path__cert_path(self)`

Test that pathlib.Path objects work for cert_path.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_iterator_file_like.py -->
## PYTHON MODULE: tests/core/test_iterator_file_like.py

### `class TestIteratorFileLike()`

#### `def test__negative_size__read__reads_all_data(self)`

#### `def test__size_smaller_than_chunk__read__reads_to_size(self)`

#### `def test__size_larger_than_chunk__read__reads_to_size(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_json_model.py -->
## PYTHON MODULE: tests/core/test_json_model.py

### MODULE DOCSTRING

Tests for JsonModel alias handling.

### `class ExampleJsonModel(JsonModel)`

Simple model used to verify JsonModel alias behavior.

### `class ExampleExplicitAliasJsonModel(JsonModel)`

Simple model used to verify explicit alias behavior.

### `class TestJsonModel()`

Test cases for JsonModel alias behavior.

#### `def test__signature__uses_snake_case_field_names(self)`

Test that constructor signatures expose Pythonic snake_case names.

#### `def test__snake_case_input__deserializes_and_serializes_by_alias(self)`

Test that snake_case input remains valid and serializes to camelCase.

#### `def test__camel_case_input__remains_backward_compatible(self)`

Test that legacy camelCase input remains valid.

#### `def test__snake_case_input__wins_when_both_names_are_provided(self)`

Test that Python field names remain the primary input form.

#### `def test__explicit_alias_signature__uses_snake_case_field_names(self)`

Test that explicit aliases preserve snake_case constructor signatures.

#### `def test__explicit_alias__accepts_both_input_names_and_serializes_wire_name(self)`

Test that explicit aliases accept Python and wire names and serialize wire names.

#### `def test__identical_wire_and_python_names__do_not_create_duplicate_aliases(self)`

Test that identical Python and wire names remain valid for discriminated unions.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_minion_id.py -->
## PYTHON MODULE: tests/core/test_minion_id.py

### MODULE DOCSTRING

Tests for read_minion_id helper function.

### `def mock_path_constants()`

Fixture to mock PathConstants.

### `def mock_minion_id_path(mock_path_constants)`

Fixture to set up the mock path structure for minion_id file.

    Returns a callable that accepts an exists parameter to configure
    whether the path exists.
    

### `class TestReadMinionId()`

Test cases for read_minion_id function.

#### `def test__minion_id_file_exists__returns_content(self, mock_minion_id_path)`

Test that the minion ID is read correctly when the file exists.

#### `def test__minion_id_file_exists_with_whitespace__returns_stripped_content(self, mock_minion_id_path)`

Test that the minion ID is stripped of leading/trailing whitespace.

#### `def test__minion_id_file_does_not_exist__returns_none(self, mock_minion_id_path)`

Test that None is returned when the minion_id file does not exist.

#### `def test__minion_id_file_has_oserror__returns_none(self, mock_minion_id_path)`

Test that None is returned when an OSError occurs reading the file.

#### `def test__minion_id_file_has_permission_error__returns_none(self, mock_minion_id_path)`

Test that None is returned when a PermissionError occurs reading the file.

#### `def test__minion_id_file_is_empty__returns_empty_string(self, mock_minion_id_path)`

Test that an empty string is returned when the file is empty.

#### `def test__minion_id_file_only_whitespace__returns_empty_string(self, mock_minion_id_path)`

Test that an empty string is returned when the file contains only whitespace.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_multipart_retry.py -->
## PYTHON MODULE: tests/core/test_multipart_retry.py

### `class _NonSeekableStream()`

#### `def seekable(self) -> bool`

#### `def seek(self, offset: int) -> None`

### `class _FailingSeekStream()`

#### `def __init__(self, data: bytes=b'artifact') -> None`

#### `def read(self, size: int=-1) -> bytes`

#### `def seek(self, offset: int) -> None`

### `class _StaticTransitionTemplate(RequestTemplate)`

#### `def __init__(self, response_transition=None, exception_transition=None) -> None`

#### `def after_response(self, request, response)`

#### `def after_exception(self, request, exc_type, exc_val, exc_tb)`

### `class _MultipartRetryTestConsumer(Consumer)`

#### `def __init__(self)`

#### `def upload(self, artifact)`

### `class TestRetryableMultipartRequestTemplate()`

#### `def test__before_request_on_initial_attempt__does_not_rewind_parts(self)`

#### `def test__before_request_on_retry__rewinds_parts(self)`

#### `def test__before_request_with_non_seekable_parts__does_not_raise(self)`

#### `def test__before_request_when_rewind_fails_after_response__finishes_with_saved_response(self)`

#### `def test__terminal_response_after_retry_pipeline__clears_saved_retry_state(self)`

#### `def test__retry_transition_after_response__preserves_saved_retry_state(self)`

#### `def test__terminal_exception_after_retry_pipeline__clears_saved_retry_state(self)`

#### `def test__before_request_on_retry_with_string_only_parts__allows_retry(self)`

### `class TestRetryableMultipartRequestIntegration()`

#### `def test__upload_with_unrewindable_stream_after_rate_limit__raises_original_api_exception(self)`

#### `def test__upload_with_rewindable_stream_after_rate_limit__retries_and_succeeds(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_pagination.py -->
## PYTHON MODULE: tests/core/test_pagination.py

### MODULE DOCSTRING

Tests for the pagination helper function.

### `class MockResponseWithItems()`

Mock API response object with 'items' field for testing pagination.

#### `def __init__(self, items: List[Any], continuation_token: str | None=None)`

### `class MockResponseWithResults()`

Mock API response object with 'results' field for testing pagination.

#### `def __init__(self, results: List[Any], continuation_token: str | None=None)`

### `class TestPaginate()`

Tests for the paginate helper function.

#### `def test__paginate_single_page__yields_all_items(self)`

Test pagination with a single page of results.

#### `def test__paginate_multiple_pages__yields_all_items_in_order(self)`

Test pagination with multiple pages.

#### `def test__paginate_with_results_field__yields_all_items(self)`

Test pagination with 'results' as the items field name.

#### `def test__paginate_with_additional_kwargs__passes_kwargs_to_fetch(self)`

Test that additional keyword arguments are passed to the fetch function.

#### `def test__paginate_empty_results__returns_empty(self)`

Test pagination with no results.

#### `def test__paginate_empty_page_in_middle__yields_only_non_empty_pages(self)`

Test pagination when a middle page is empty.

#### `def test__paginate_generator__can_be_used_in_for_loop(self)`

Test that paginate works as expected in a for loop.

#### `def test__paginate_lazy_evaluation__only_fetches_as_needed(self)`

Test that pagination is lazy and doesn't fetch all pages immediately.

#### `def test__paginate_with_kwargs_persisted_across_pages__kwargs_used_on_all_calls(self)`

Test that kwargs are passed to all fetch function calls.

#### `def test__paginate_missing_items_field__yields_nothing(self)`

Test pagination when the items field doesn't exist on the response.

#### `def test__paginate_continuation_token_unchanged__raises_runtime_error(self)`

Test that an error is raised if the continuation token doesn't change.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/core/test_partial_success.py -->
## PYTHON MODULE: tests/core/test_partial_success.py

### `class _FakeResponse()`

#### `def __init__(self, payload)`

#### `def model_dump(self, *, mode, by_alias)`

### `def test__unwrap_single_item_partial_success__returns_first_item()`

Return the first item when the partial-success response is successful.

### `def test__unwrap_single_item_partial_success__raises_on_partial_failure()`

Raise ApiException when the response reports a structured partial failure.

### `def test__unwrap_single_item_partial_success__unwraps_single_inner_error()`

Raise ApiException with the inner error for one-or-more wrappers.

### `def test__unwrap_single_item_partial_success__raises_on_empty_success_payload()`

Raise ApiException when the response succeeds but contains no created item.

### `def test__unwrap_single_item_partial_success__raises_on_multiple_success_items()`

Raise ApiException when the response unexpectedly contains multiple items.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/alarm/test_alarm_client.py -->
## PYTHON MODULE: tests/integration/alarm/test_alarm_client.py

### `def client(enterprise_config: HttpConfiguration) -> AlarmClient`

Fixture to create an AlarmClient instance.

### `def unique_identifier() -> Callable[[], str]`

Unique alarm id for this test.

### `def create_alarms(client: AlarmClient) -> Generator[Callable[[str, int, str], str], None, None]`

Fixture to return a factory that creates alarms.

    Returns instance_id (referred to as 'id' in tests) for each created alarm.
    

### `class TestAlarmClient()`

#### `def test__create_single_alarm__one_alarm_created_with_right_field_values(self, client: AlarmClient, unique_identifier: Callable[[], str])`

#### `def test__query_alarms_with_all_fields__returns_complete_response(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__create_multiple_alarms_and_query_alarms_with_take__only_take_returned(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__query_alarm_by_alarm_id__matches_expected(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__acknowledge_alarm__verifies_all_response_fields(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__acknowledge_alarm_with_force_clear__alarm_cleared(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__delete_alarm__returns_none(self, client: AlarmClient, unique_identifier: Callable[[], str])`

#### `def test__delete_alarms__verifies_all_response_fields(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__update_alarm_severity__severity_updated(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__clear_alarm__alarm_cleared(self, client: AlarmClient, create_alarms: Callable[[str, int, str], str], unique_identifier: Callable[[], str])`

#### `def test__get_alarm_with_invalid_instance_id__raises_ApiException_NotFound(self, client: AlarmClient)`

#### `def test__delete_alarm_with_invalid_instance_id__raises_ApiException_NotFound(self, client: AlarmClient)`

#### `def test__query_alarms_with_invalid_filter_syntax__raises_ApiException_BadRequest(self, client: AlarmClient)`

#### `def test__query_alarm_with_non_existent_alarm_id__returns_empty_list(self, client: AlarmClient, unique_identifier: Callable[[], str])`

#### `def test__create_alarm_with_invalid_severity__raises_ApiException_BadRequest(self, client: AlarmClient, unique_identifier: Callable[[], str])`

#### `def test__create_or_update_alarm_with_conflict_and_ignore_conflict_true__returns_none(self, client: AlarmClient, unique_identifier: Callable[[], str])`

Test that ignore_conflict=True returns None on 409 Conflict.

#### `def test__create_or_update_alarm_with_conflict_and_ignore_conflict_false__raises_exception(self, client: AlarmClient, unique_identifier: Callable[[], str])`

Test that ignore_conflict=False (default) raises ApiException on 409 Conflict.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/artifact/test_artifact.py -->
## PYTHON MODULE: tests/integration/artifact/test_artifact.py

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

- `DEFAULT_WORKSPACE = '2300760d-38c4-48a1-9acb-800260812337'`

### `def client(enterprise_config: HttpConfiguration) -> ArtifactClient`

Fixture to create an ArtifactClient instance.

### `def create_artifact(client: ArtifactClient)`

Fixture to return a factory that creates artifact.

### `class TestArtifact()`

#### `def test__upload_artifact__artifact_uploaded(self, client: ArtifactClient, create_artifact)`

#### `def test__upload_artifact_after_rate_limit_retry__artifact_uploaded(self, create_artifact, monkeypatch: pytest.MonkeyPatch)`

#### `def test__download_artifact__artifact_downloaded(self, client: ArtifactClient, create_artifact)`

#### `def test__delete_artifact__artifact_deleted(self, client: ArtifactClient, create_artifact)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/assetmanagement/test_asset_management.py -->
## PYTHON MODULE: tests/integration/assetmanagement/test_asset_management.py

### `def create_asset(client: AssetManagementClient) -> Generator[CreateAssetFixture, None, None]`

Fixture to return a factory that creates assets.

### `def client(enterprise_config: HttpConfiguration) -> AssetManagementClient`

Fixture to create an AssetManagementClient instance.

### `def unique_identifier() -> str`

Fixture to generate a unique identifier using UUID.

### `def start_utilization(client: AssetManagementClient) -> Generator[StartUtilizationFixture, None, None]`

Fixture to start utilization and automatically clean up.

### `class TestAssetManagement()`

Integration tests for the asset management client.

#### `def test__create_asset__returns_created_asset(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse])`

#### `def test__link_files__link_succeded(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse])`

#### `def test__delete_asset__returns_deleted_asset(self, client: AssetManagementClient)`

#### `def test__query_assets_with_take_value__returns_specific_number_of_assets(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse])`

#### `def test_query_assets_with_projections__returns_the_assets_with_projected_properties(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse])`

#### `def test__start_utilization__returns_success_response(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse], unique_identifier: str, start_utilization: Callable[[str, List[Asset], str, str, str, str], None])`

#### `def test__utilization_heartbeat__returns_success_response(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse], unique_identifier: str, start_utilization: Callable[[str, List[Asset], str, str, str, str], None])`

#### `def test__end_utilization__returns_success_response(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse], unique_identifier: str, start_utilization: Callable[[str, List[Asset], str, str, str, str], None])`

#### `def test__query_asset_utilization_history__returns_response(self, client: AssetManagementClient, create_asset: Callable[[List[CreateAssetRequest]], CreateAssetsPartialSuccessResponse], unique_identifier: str, start_utilization: Callable[[str, List[Asset], str, str, str, str], None])`

#### `def test__start_utilization_with_nonexistent_asset__raises_api_exception(self, client: AssetManagementClient, unique_identifier: str)`

#### `def test__heartbeat_with_nonexistent_utilization_id__returns_empty_list(self, client: AssetManagementClient, unique_identifier: str)`

#### `def test__end_utilization_with_nonexistent_utilization_id__returns_empty_list(self, client: AssetManagementClient, unique_identifier: str)`

#### `def test__query_utilization_history_with_invalid_filter__raises_api_exception(self, client: AssetManagementClient)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/dataframe/test_dataframe.py -->
## PYTHON MODULE: tests/integration/dataframe/test_dataframe.py

### `def client(enterprise_config)`

Fixture to create a DataFrameClient instance.

### `def create_table(client: DataFrameClient)`

Fixture to return a factory that creates tables.

### `def test_tables(create_table)`

Fixture to create a set of test tables.

### `def supports_test_result_id(client: DataFrameClient) -> bool`

Fixture to determine if the server supports test result IDs.

### `def table_with_data(client: DataFrameClient, create_table) -> str`

Fixture to create a table with data.

### `class TestDataFrame()`

#### `def _wait_for_table_data(client: DataFrameClient, table_id: str, minimum_row_count: int, index_column: str='index', timeout: float=5.0, sleep_duration: float=0.2) -> int`

Helper function to wait for table data to be available by polling get_table_data.

        Args:
            client: The DataFrameClient to use for checking data availability
            table_id: ID of the table to check
            expected_row_count: Expected number of rows in the table
            index_column: Name of the index column to query (default: "index")
            timeout: Maximum time to wait in seconds (default: 2.0)
            sleep_duration: Sleep duration between attempts in seconds (default: 0.2)

        Returns:
            The actual number of rows found in the table
        

#### `def _new_single_int_table(self, create_table, column_name: str='a') -> str`

#### `def _create_data_frame(columns: List[Column], data: _DataFrameData, include_column_names: bool=False) -> DataFrame`

#### `def _read_data_frame(columns: List[Column], frame: DataFrame) -> _DataFrameData`

#### `def _data_value_to_str(column: Column, value: _DataElement) -> str | None`

#### `def _str_to_data_value(column: Column, value: str | None) -> _DataElement`

#### `def _read_exported_csv(columns: List[Column], data: IteratorFileLike) -> tuple[List[str], _DataFrameData]`

#### `def test__api_info__returns(self, client)`

#### `def test__create_table__metadata_is_correct(self, client: DataFrameClient, test_tables: List[str])`

#### `def test__create_table__supports_test_result(self, client: DataFrameClient, create_table: Callable[[CreateTableRequest], str], supports_test_result_id: bool)`

#### `def test__get_table__correct_timestamp(self, client: DataFrameClient, create_table)`

#### `def test__get_table_invalid_id__raises(self, client: DataFrameClient)`

#### `def test__list_tables__returns(self, client: DataFrameClient, test_tables: List[str])`

#### `def test__query_tables__returns(self, client: DataFrameClient, test_tables: List[str])`

#### `def test__modify_table__returns(self, client: DataFrameClient, create_table, supports_test_result_id: bool)`

#### `def _test_result_id_if_supported(test_result_id: str | None, supports_test_result_id: bool) -> _TestResultIdArg`

#### `def test__delete_table__deletes(self, client: DataFrameClient)`

#### `def test__delete_tables__deletes(self, client: DataFrameClient)`

#### `def test__delete_tables__returns_partial_success(self, client: DataFrameClient)`

#### `def test__modify_tables__modifies_tables(self, client: DataFrameClient, create_table, supports_test_result_id: bool)`

#### `def test__modify_tables__returns_partial_success(self, client: DataFrameClient, create_table, supports_test_result_id: bool)`

#### `def test__get_table_data__returns_correct_data(self, client: DataFrameClient, table_with_data: str)`

#### `def test__write_invalid_data__raises(self, client: DataFrameClient, test_tables: List[str])`

#### `def test__query_table_data__sorts(self, client: DataFrameClient, table_with_data: str)`

#### `def test__query_table_data__filters(self, client: DataFrameClient, table_with_data: str)`

#### `def test__query_decimated_data__works(self, client: DataFrameClient, table_with_data: str)`

#### `def test__export_table_data__includes_all_rows(self, client: DataFrameClient, table_with_data: str)`

#### `def test__export_table_data__limits_to_take_rows(self, client: DataFrameClient, table_with_data: str)`

#### `def test__append_table_data__append_request_success(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__append_request_with_end_of_data_argument_disallowed(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__append_request_without_end_of_data_success(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__accepts_dataframe_model(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__dataframe_without_end_of_data_success(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__none_without_end_of_data_raises(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__flush_only_with_none(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__arrow_ingestion_success(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__single_recordbatch_success(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__arrow_ingestion_with_end_of_data_query_param_false(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__empty_iterator_requires_end_of_data(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__arrow_iterable_with_non_recordbatch_elements_raises(self, client: DataFrameClient, create_table)`

#### `def test__append_table_data__arrow_iterable_without_pyarrow_raises_runtime_error(self, client: DataFrameClient, create_table, monkeypatch)`

#### `def test__append_table_data__arrow_ingestion_400_unsupported(self, client: DataFrameClient)`

#### `def test__append_table_data__arrow_ingestion_400_supported_passthrough(self, client: DataFrameClient)`

#### `def test__append_table_data__arrow_ingestion_non_400_passthrough(self, client: DataFrameClient)`

#### `def test__append_table_data__unsupported_type_raises(self, client: DataFrameClient, create_table)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/feeds/test_feeds_client.py -->
## PYTHON MODULE: tests/integration/feeds/test_feeds_client.py

### MODULE DOCSTRING

Integration tests for FeedsClient.

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

- `FEED_DESCRIPTION = 'Sample feed for uploading packages'`

- `PACKAGE_PATH = str(Path(__file__).parent.resolve() / 'test_files' / 'sample-measurement_0.5.0_windows_x64.nipkg')`

- `PREFIX = 'Feeds Client Test - '`

### `def client(enterprise_config) -> FeedsClient`

Fixture to create a FeedsClient instance.

### `def create_feed(client: FeedsClient)`

Fixture to return a object that creates feed.

### `def create_feed_request()`

Fixture to create a request body of create feed API.

### `def binary_pkg_file_data() -> BinaryIO`

Fixture to return package file in binary format.

### `def invalid_id() -> str`

Generate a invalid id.

### `def get_feed_name()`

Generate a feed name.

### `class TestFeedsClient()`

#### `def test__create_feed_windows_platform__succeeds(self, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable)`

Test the case of a completely successful create feed API for Windows platform.

#### `def test__create_feed_linux_platform__succeeds(self, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable)`

Test the case of a completely successful create feed API for Linux platform.

#### `def test__query_feeds_windows_platform__succeeds(self, client: FeedsClient, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable)`

Test the case for querying available feeds for Windows platform.

#### `def test__query_feeds_linux_platform__succeeds(self, client: FeedsClient, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable)`

Test the case for querying available feeds for Linux platform.

#### `def test__query_feeds__invalid_workspace_raises(self, client: FeedsClient, invalid_id: str)`

Test the case of query feeds API with invalid workspace id.

#### `def test__upload_package__succeeds(self, client: FeedsClient, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable)`

Test the case of upload package to feed.

#### `def test__upload_package_content__succeeds(self, client: FeedsClient, create_feed: Callable, create_feed_request: Callable, binary_pkg_file_data: BinaryIO, get_feed_name: Callable)`

Test the case of upload package content to feed.

#### `def test__upload_package_content__invalid_feed_id_raises(self, client: FeedsClient, binary_pkg_file_data: BinaryIO, invalid_id: str)`

Test the case of uploading package to Invalid feed.

#### `def test__upload_package_content_after_rate_limit_retry__upload_package_content_succeeds(self, client: FeedsClient, create_feed: Callable, create_feed_request: Callable, get_feed_name: Callable, monkeypatch: pytest.MonkeyPatch)`

#### `def test__delete_windows_feed__succeeds(self, client: FeedsClient, create_feed_request: Callable, get_feed_name: Callable)`

Test the case of deleting Windows feed.

#### `def test__delete__linux_feed__succeeds(self, client: FeedsClient, create_feed_request: Callable, get_feed_name: Callable)`

Test the case of deleting Linux feed.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/file/test_file_client.py -->
## PYTHON MODULE: tests/integration/file/test_file_client.py

### MODULE DOCSTRING

Integration tests for FileClient.

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

- `FILE_NOT_FOUND_ERR = 'Not Found'`

- `PREFIX = 'File Client Tests-'`

- `TEST_FILE_DATA = b'This is a test file binary content.'`

- `TEST_FILE_NAME = f'{PREFIX}Test File.bin'`

### `def client(enterprise_config) -> FileClient`

Fixture to create a FileClient instance.

### `def binary_file_data() -> BinaryIO`

Test Binary file content.

### `def test_file(client: FileClient)`

Fixture to return a factory that uploads a file.

### `def invalid_file_id(client: FileClient) -> str`

Generate a invalid file id.

### `def random_filename_extension() -> str`

Generate a random filename and extension.

### `class TestFileClient()`

#### `def test__api_info__returns(self, client: FileClient)`

#### `def test__upload_file_with_metadata__succeeds(self, client: FileClient, test_file, random_filename_extension: str)`

#### `def test__upload_file_after_rate_limit_retry__upload_file_succeeds(self, client: FileClient, monkeypatch: pytest.MonkeyPatch)`

Retrying a file upload should succeed against the real endpoint.

#### `def test__upload_get_delete_files__succeeds(self, client: FileClient, test_file, random_filename_extension)`

#### `def test__delete_file__invalid_id_raises(self, client: FileClient, invalid_file_id: str)`

#### `def test__delete_files__succeeds(self, client: FileClient, test_file)`

#### `def test__download_file__invalid_id_raises(self, client: FileClient, invalid_file_id: str)`

#### `def test__download_file__succeeds(self, client: FileClient, test_file, binary_file_data: BinaryIO, random_filename_extension: str)`

#### `def test__update_metadata__rename_utility_succeeds(self, client: FileClient, test_file)`

#### `def test__update_metadata__append_replace_succeeds(self, client: FileClient, test_file)`

#### `def test__back_off_retry__works(self, client: FileClient, test_file)`

#### `def test__query_files_linq__filter_by_name_succeeds(self, client: FileClient, test_file, random_filename_extension: str)`

#### `def test__query_files_linq__invalid_filter_raises(self, client: FileClient)`

#### `def test__query_files_linq__filter_returns_no_results(self, client: FileClient)`

#### `def test__query_files_linq__total_count_relation_accepts_string(self, client: FileClient, test_file, random_filename_extension)`

Test backward compatibility: TotalCountRelation should accept string values.

        TotalCountRelation was previously a plain str type. This test ensures that string
        values like 'eq' and 'gte' are still accepted for backward compatibility.
        

#### `def test__query_files_linq__skip_and_take_pagination(self, client: FileClient, test_file)`

Test query_files_linq with skip and take for pagination.

#### `def test__search_files__succeeds(self, client: FileClient, test_file, random_filename_extension: str)`

Test search_files with filtering, pagination, and ordering.

        Note: search_files() is not guaranteed to return newly created files immediately
        due to indexing delay (a few seconds). Retry logic with backoff is used to handle
        this eventual consistency behavior.
        

#### `def test__search_files__no_filter_succeeds(self, client: FileClient, test_file)`

#### `def test__search_files__invalid_filter_raises(self, client: FileClient)`

#### `def test__search_files__filter_returns_no_results(self, client: FileClient)`

#### `def test__start_upload_session__with_invalid_workspace__raises(self, client: FileClient)`

#### `def test__append_to_upload_session__uploads_file_in_chunks(self, client: FileClient)`

#### `def test__finish_upload_session__invalid_session_id_raises(self, client: FileClient, invalid_file_id: str)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/notebook/test_notebook_client.py -->
## PYTHON MODULE: tests/integration/notebook/test_notebook_client.py

- `TEST_FILE_DATA = b'This is a test notebook binary content.'`

- `PREFIX = 'Notebook Client Tests-'`

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

### `def client(enterprise_config) -> NotebookClient`

Fixture to create a NotebookClient instance.

### `def random_filename() -> str`

Generate a random filename for each test in test class.

### `def create_notebook(client: NotebookClient)`

Fixture to return a factory that creates a notebook.

### `class TestNotebookClient()`

#### `def test__create_notebook_with_valid_file_and_metadata__notebook_created_with_valid_metadata(self, create_notebook, random_filename)`

#### `def test__create_notebook_with_invalid_file__raises_ApiException_BadRequest(self, client, random_filename)`

#### `def test__create_notebook_with_duplicate_file_name__raises_ApiException_BadRequest(self, create_notebook, random_filename)`

#### `def test__create_notebook_with_invalid_workspace__raises_ApiException_BadRequest(self, create_notebook, random_filename)`

#### `def test__get_notebook_with_valid_id__returns_notebook_with_right_field_values(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__get_notebook_with_invalid_id__raises_ApiException_NotFound(self, client)`

#### `def test__update_existing_notebook_metadata__update_notebook_metadata_succeeds(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__update_existing_notebook_content__update_notebook_content_succeeds(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__update_notebook_metadata_with_invalid_id__raises_ApiException_NotFound(self, client: NotebookClient)`

#### `def test__update_notebook_content_with_invalid_file__raises_ApiException_BadRequest(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__update_notebook_content_with_duplicate_file_name__raises_ApiException_BadRequest(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__update_notebook_with_invalid_workspace__raises_ApiException_BadRequest(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__delete_notebook_with_valid_id__notebook_should_delete_successfully(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__delete_notebook_with_invalid_id__raises_ApiException_NotFound(self, client)`

#### `def test__query_notebook_by_id__return_notebook_matches_id(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__query_notebook_by_invalid_id__returns_empty_list(self, client)`

#### `def test__query_notebook_by_name__returns_notebook_matches_name(self, client, create_notebook, random_filename)`

#### `def test__query_notebook_by_invalid_name__returns_empty_list(self, client)`

#### `def test__query_by_taking_3_notebooks__returns_3_notebooks(self, client)`

#### `def test__query_notebooks_by_continuation_token__returns_next_page_of_notebooks(self, client)`

#### `def test__get_notebook_content_by_id__returns_notebook_content(self, client: NotebookClient, create_notebook, random_filename)`

#### `def test__get_notebook_content_by_invalid_id__raises_ApiException_NotFound(self, client)`

#### `def test__create_notebook_after_rate_limit_retry__notebook_created_with_valid_metadata(self, client: NotebookClient, random_filename: str, monkeypatch: pytest.MonkeyPatch)`

#### `def test__update_notebook_metadata_after_rate_limit_retry__update_notebook_metadata_succeeds(self, client: NotebookClient, create_notebook, random_filename: str, monkeypatch: pytest.MonkeyPatch)`

#### `def test__create_executions_with_valid_notebook_id__returns_executions_with_right_fields(self, client: NotebookClient)`

#### `def test__create_executions_with_valid_notebook_id_invalid_workspace__returns_error_and_valid_executions(self, client: NotebookClient)`

#### `def test__create_executions_with_invalid_notebook_id__returns_execution(self, client: NotebookClient)`

#### `def test__get_execution_by_id__returns_execution_with_right_fields(self, client: NotebookClient)`

#### `def test__get_execution_by_invalid_id__raises_ApiException_NotFound(self, client: NotebookClient)`

#### `def test__filter_executions_by_status__returns_executions_matches_status(self, client: NotebookClient)`

#### `def test__query_executions_by_invalid_filter__raises_ApiException_BadRequest(self, client: NotebookClient)`

#### `def test__query_executions_by_projection__returns_executions_with_projected_properties(self, client: NotebookClient)`

#### `def test__query_executions_by_status_in_ascending__returns_executions_sorted_by_status(self, client: NotebookClient)`

#### `def test__query_executions_by_status_in_descending__returns_executions_sorted_by_status(self, client: NotebookClient)`

#### `def test__cancel_executions__return_inner_errors(self, client: NotebookClient)`

#### `def test__retry_executions__return_inner_errors(self, client: NotebookClient)`

#### `def test__create_executions_from_existing__return_inner_errors(self, client: NotebookClient)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/notification/test_notification_client.py -->
## PYTHON MODULE: tests/integration/notification/test_notification_client.py

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

### `def _smtp_address_group()`

Returns the created address group.

### `def _smtp_message_template()`

Returns the created message template.

### `def _notification_configuration(_smtp_address_group: SmtpAddressGroup, _smtp_message_template: SmtpMessageTemplate)`

Returns the created notification configuration.

### `def _notification_strategy(_notification_configuration: DynamicNotificationConfiguration)`

Returns the created notification strategy.

### `def request_model(_notification_strategy: DynamicNotificationStrategy)`

Returns the created request.

### `def client(enterprise_config: HttpConfiguration) -> NotificationClient`

Fixture to create a Notification client.

### `class TestNotificationClient()`

#### `def test__apply_dynamic_strategy_with_correct_request__returns_none(self, client: NotificationClient, request_model: DynamicStrategyRequest)`

#### `def test__apply_dynamic_strategy_with_invalid_recipient_for_smtp_service__raises_exception(self, client: NotificationClient, _smtp_message_template: SmtpMessageTemplate)`

#### `def test__create_strategy_with_no_configurations__raises_exception(self)`

#### `def test__apply_dynamic_strategy_with_empty_subject_for_smtp_message_template__raises_exception(self, client: NotificationClient, _smtp_address_group: SmtpAddressGroup)`

#### `def test__create_address_group_with_invalid_interpreting_service_name__raises_exception(self)`

#### `def test__apply_dynamic_strategy_with_no_address_group_id_and_message_template_id_in_config__returns_none(self, client: NotificationClient, _smtp_address_group: SmtpAddressGroup, _smtp_message_template: SmtpMessageTemplate)`

#### `def test__apply_dynamic_strategy_with_multiple_notification_configurations__returns_none(self, client: NotificationClient, _smtp_address_group: SmtpAddressGroup)`

#### `def test__create_configuration_with_no_address_group_id_and_address_group__raise_exception(self, _smtp_message_template: SmtpMessageTemplate)`

#### `def test__create_configuration_with_no_message_template_id_and_message_template__raise_exception(self, _smtp_address_group: SmtpAddressGroup)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/product/test_product_client.py -->
## PYTHON MODULE: tests/integration/product/test_product_client.py

### `def client(enterprise_config: HttpConfiguration) -> ProductClient`

Fixture to create a ProductClient instance.

### `def unique_identifier() -> str`

Unique product id for this test.

### `def create_update_product_request()`

Fixture to create a request object for updating products, from a product response

### `def create_products(client: ProductClient)`

Fixture to return a factory that creates specs.

### `class TestProductClient()`

#### `def test__create_single_product__one_product_created_with_right_field_values(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__create_multiple_products__multiple_creates_succeed(self, client: ProductClient, create_products)`

#### `def test__create_single_product_and_get_products__at_least_one_product_exists(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__create_multiple_products_and_get_products_with_take__only_take_returned(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__create_multiple_products_and_get_products_with_count_at_least_one_count(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__get_product_by_id__product_matches_expected(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__query_product_by_part_number__matches_expected(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__query_product_values_for_name__name_matches(self, client: ProductClient, create_products, unique_identifier)`

#### `def test__update_keywords_with_replace__keywords_replaced(self, client: ProductClient, create_products, unique_identifier, create_update_product_request)`

#### `def test__update_keywords_no_replace__keywords_appended(self, client: ProductClient, create_products, unique_identifier, create_update_product_request)`

#### `def test__update_properties_with_replace__properties_replaced(self, client: ProductClient, create_products, unique_identifier, create_update_product_request)`

#### `def test__update_properties_append__properties_appended(self, client: ProductClient, create_products, unique_identifier, create_update_product_request)`

#### `def test__query_products_linked_to_files_correct_products_returned(self, client: ProductClient, create_products)`

#### `def test__query_products_with_projection__returns_only_specified_fields(self, client: ProductClient, create_products, unique_identifier)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/spec/test_spec.py -->
## PYTHON MODULE: tests/integration/spec/test_spec.py

### `def product() -> str`

Unique product id for this test run.

### `def client(enterprise_config: HttpConfiguration) -> SpecClient`

Fixture to create a SpecClient instance.

### `def create_specs(client: SpecClient)`

Fixture to return a factory that creates specs.

### `def create_specs_for_query(create_specs, product)`

Fixture for creating a set of specs that can be used to test query operations.

### `class TestSpec()`

#### `def test__api_info__returns(self, client: SpecClient)`

#### `def test__create_single_spec__one_created_with_right_field_values(self, client: SpecClient, create_specs, product)`

#### `def test__create_multiple_specs__all_succeed(self, client: SpecClient, create_specs, product)`

#### `def test__create_duplicate_spec__errors(self, client: SpecClient, create_specs, product)`

#### `def test__delete_existing_spec__succeeds(self, client: SpecClient, product)`

#### `def test__delete_non_existant_spec__delete_fails(self, client: SpecClient)`

#### `def test__update_single_same_version__version_updates(self, client: SpecClient, create_specs, product)`

#### `def test__get_spec_by_id__spec_matches_expected(self, client: SpecClient, create_specs, product)`

#### `def test__get_non_existant_spec_by_id__get_spec_fails(self, client: SpecClient)`

#### `def test__query_product__all_returned(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__query_spec_name__two_returned(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__query_spec_category_one_returned(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__query_input_voltage__conditions_match(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__query_spec_projection_columns__columns_returned(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__query_specs__returns_condition_value_type_correctly(self, client: SpecClient, create_specs, create_specs_for_query, product)`

#### `def test__without_condition_type_projection__query_specs__condition_type_field_is_unset(self, client: SpecClient, create_specs, create_specs_for_query, product)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/systems/test_systems.py -->
## PYTHON MODULE: tests/integration/systems/test_systems.py

### `def client(enterprise_config: HttpConfiguration) -> SystemsClient`

Fixture to create a TestPlanTemplateClient instance.

### `def create_virtual_systems(client: SystemsClient)`

Fixture to return a factory that create test plan templates.

### `class TestSystemsClient()`

#### `def test__create_virtual_systems__returns_created_virtual_system(self, client: SystemsClient, create_virtual_systems)`

#### `def test__query_systems__returns_queried_virtual_system(self, client: SystemsClient, create_virtual_systems)`

#### `def test__remove_sytems(self, client: SystemsClient)`

#### `def test__query_systems_with_projections__returns_the_systems_with_projected_properties(self, client: SystemsClient)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/tag/mixins.py -->
## PYTHON MODULE: tests/integration/tag/mixins.py

### `class TagBaseMixin()`

#### `def generate_each_tag_type(self, generate_tag_paths, request, setup_tag_manager)`

Fixture to generate a tag of each type with a common path prefix and create the tags on the server.

        The tags will be automatically deleted at the end of the current test.

        Returns:
            A 2-tuple containing:
            - The generated tags.
            - The common prefix for each of the generated tags, including the trailing dot.

        Raises:
            nisystemlink.clients.core.ApiException: if the API call fails.
        

#### `def generate_tag_path(self, request, setup_tag_manager)`

Fixture to generate a tag path to be used within the scope of a single test.

        Args:
            suffix (str | None): Optional suffix to add to the tag for informational
                purposes.

        Returns:
            The generated tag path
        

#### `def generate_tag_paths(self, request, setup_tag_manager)`

Generates tag paths to be used within the scope of a single test.

        Args:
            count: The number of paths to generate.

        Returns:
            A 2-tuple containing:
            - The generated tag paths.
            - The common prefix for each of the generated paths, including the trailing dot.
        

### `class CloudMixin(TagBaseMixin)`

#### `def setup_tag_manager(self, verified_tag_config, request)`

#### `def verified_tag_config(self, cloud_config)`

### `class ServerMixin(TagBaseMixin)`

#### `def setup_tag_manager(self, verified_tag_config, request)`

#### `def verified_tag_config(self, server_config)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/tag/test_tagmanager.py -->
## PYTHON MODULE: tests/integration/tag/test_tagmanager.py

### `class TagManagerTests()`

#### `def test__write_read_bool_tag__values_are_correct(self, generate_tag_path)`

#### `def test__write_read_date_time_tag__values_are_correct(self, generate_tag_path)`

#### `def test__write_read_double_tag__values_are_correct(self, generate_tag_path)`

#### `def test__write_read_int_tag__values_are_correct(self, generate_tag_path)`

#### `def test__write_read_string_tag__values_are_correct(self, generate_tag_path)`

#### `def test__write_read_uint64_tag__values_are_correct(self, generate_tag_path)`

#### `def test__set_double_values__aggregate_values_are_correct(self, generate_tag_path)`

#### `def test__set_int_values__aggregate_values_are_correct(self, generate_tag_path)`

#### `def test__uint64_aggregates(self, generate_tag_path)`

#### `def test__collect_aggregates_False__aggregates_is_None(self, generate_tag_path)`

#### `def test__special_tag_paths_used__apis_work(self, generate_tag_path)`

#### `def test__update_metadata__queried_metadata_is_correct(self, generate_tag_path)`

#### `def test__merge_metadata__queried_metadata_is_correct(self, generate_tag_path)`

#### `def test__change_data_type__raises(self, generate_tag_path)`

#### `def test__write_wrong_data_type__write_ignored(self, generate_tag_path)`

#### `def test__run_queries__results_are_correct(self, generate_tag_paths)`

#### `def internal_test_query_result(cls, query, expected_paths, page_size, skip=0, expected_pages=1)`

#### `def internal_test_write_and_read_tag(cls, tag, writer, reader, value_to_write)`

#### `def internal_test_numeric_aggregates(cls, tag, writer, reader, mean, values)`

### `class TestTagManagerCloud(TagManagerTests, CloudMixin)`

### `class TestTagManagerServer(TagManagerTests, ServerMixin)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/tag/test_tagselection.py -->
## PYTHON MODULE: tests/integration/tag/test_tagselection.py

### `class TagSelectionTests()`

#### `def _gen_tags(self, request, generate_each_tag_type)`

#### `def test__create_selection_from_tags__paths_and_tags_are_correct(self)`

#### `def test__create_selection_from_paths__paths_and_tags_are_correct(self)`

#### `def test__create_empty_selection__has_no_tags(self)`

#### `def test__selection_created_for_missing_tag__refresh__selection_has_tag_iff_it_exists(self, generate_tag_path)`

#### `def test__some_tags_deleted_or_added__refresh_metadata__tag_list_is_correct(self)`

#### `def test__write_and_read_some_or_all_selection_tags__values_are_correct(self)`

#### `def test__reset_aggregates__aggregate_values_are_correct(self)`

### `class TestTagSelectionCloud(TagSelectionTests, CloudMixin)`

### `class TestTagSelectionServer(TagSelectionTests, ServerMixin)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/tag/test_tagsubscription.py -->
## PYTHON MODULE: tests/integration/tag/test_tagsubscription.py

### `class TagSubscriptionTests()`

#### `def _gen_tags(self, request, generate_each_tag_type)`

#### `def test__create_and_destroy_subscription__no_error(self)`

#### `def test__subscribed_values_updated__subscription_receives_events(self)`

#### `def test__subscription_outlives_heartbeat_interval__events_still_received(self)`

### `class TestTagSubscriptionCloud(TagSubscriptionTests, CloudMixin)`

### `class TestTagSubscriptionServer(TagSubscriptionTests, ServerMixin)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/test_plan/test_test_plan_client.py -->
## PYTHON MODULE: tests/integration/test_plan/test_test_plan_client.py

### `def client(enterprise_config: HttpConfiguration) -> TestPlanClient`

Fixture to create a TestPlansClient instance

### `def create_test_plans(client: TestPlanClient)`

Fixture to return a factory that create test plans.

### `def create_test_plan_templates(client: TestPlanClient)`

Fixture to return a factory that create test plan templates.

### `class TestTestPlanClient()`

#### `def test__create_and_delete_test_plan__returns_created_and_deleted_test_plans(self, client: TestPlanClient, create_test_plans)`

#### `def test__get_test_plan__returns_get_test_plan(self, client: TestPlanClient, create_test_plans)`

#### `def test__update_test_plan__returns_updated_test_plan(self, client: TestPlanClient, create_test_plans)`

#### `def test__schedule_test_plan__returns_scheduled_test_plan(self, client: TestPlanClient, create_test_plans)`

#### `def test__query_test_plans__return_queried_test_plan(self, client: TestPlanClient, create_test_plans)`

#### `def test__query_test_plans_with_projections__returns_the_test_plans_with_projected_properties(self, client: TestPlanClient, create_test_plans)`

#### `def test__create_test_plan_template__returns_created_test_plan_template(self, client: TestPlanClient, create_test_plan_templates)`

#### `def test__query_test_plan_template__returns_queried_test_plan_template(self, client: TestPlanClient, create_test_plan_templates)`

#### `def test__delete_test_plan_template(self, client: TestPlanClient)`

#### `def test__query_test_plan_templates_with_projections__returns_test_plan_templates_with_projected_properties(self, client: TestPlanClient, create_test_plan_templates)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/testmonitor/test_testmonitor.py -->
## PYTHON MODULE: tests/integration/testmonitor/test_testmonitor.py

### `def client(enterprise_config: HttpConfiguration) -> TestMonitorClient`

Fixture to create a TestMonitorClient instance.

### `def product_client(enterprise_config: HttpConfiguration) -> ProductClient`

Fixture to create a ProductClient instance.

### `def unique_identifier() -> str`

Unique result/step id for this test.

### `def create_results(client: TestMonitorClient, product_client: ProductClient)`

Fixture to return a factory that creates results.

### `def create_steps(client: TestMonitorClient)`

Fixture to return a factory that creates steps.

### `class TestTestMonitor()`

#### `def test__api_info__returns(self, client: TestMonitorClient)`

#### `def test__create_single_result__one_result_created_with_right_field_values(self, client: TestMonitorClient, create_results)`

#### `def test__create_multiple_results__multiple_creates_succeed(self, client: TestMonitorClient, create_results)`

#### `def test__create_single_result_and_get_results__at_least_one_result_exists(self, client: TestMonitorClient, create_results)`

#### `def test__create_multiple_results_and_get_results_with_take__only_take_returned(self, client: TestMonitorClient, create_results)`

#### `def test__create_multiple_results_and_get_results_with_count_at_least_one_count(self, client: TestMonitorClient, create_results)`

#### `def test__get_result_by_id__result_matches_expected(self, client: TestMonitorClient, create_results)`

#### `def test__query_result_by_part_number_and_serial_number_with_projection__results_with_only_projected_fields(self, client: TestMonitorClient, create_results, unique_identifier)`

#### `def test__query_result_values_for_program_name__name_matches(self, client: TestMonitorClient, create_results, unique_identifier)`

#### `def test__update_keywords_with_replace__keywords_replaced(self, client: TestMonitorClient, create_results)`

#### `def test__update_keywords_no_replace__keywords_appended(self, client: TestMonitorClient, create_results)`

#### `def test__update_properties_with_replace__properties_replaced(self, client: TestMonitorClient, create_results)`

#### `def test__update_properties_append__properties_appended(self, client: TestMonitorClient, create_results)`

#### `def __map_result_to_update_result_request(self, result: Result) -> UpdateResultRequest`

#### `def test__create_single_step__creation_succeed(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__create_step_without_step_id__creation_succeed(self, client: TestMonitorClient, create_results, create_steps)`

#### `def test__create_multiple_steps__multiple_creation_succeed(self, client: TestMonitorClient, create_results, create_steps)`

#### `def test__create_multiple_steps_with_children__multiple_creation_succeed(self, client: TestMonitorClient, create_results, create_steps)`

#### `def test__get_steps__at_least_one_step_exists(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test_with_multiple_steps__get_steps_with_take__only_take_returned(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__get_steps_with_return_count__steps_and_count_returned(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__get_step_by_id__expected_step_returned(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__query_step_by_name_and_result_id__expected_step_returned(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__query_step_values_for_name__name_matches(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__update_step_data_and_inputs__data_and_inputs_updated(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__update_step_with_replace_true__replace_keywords_and_properties(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__delete_existing_step__deleted(self, client: TestMonitorClient, create_results, create_steps, unique_identifier)`

#### `def test__delete_non_existent_step__delete_fails(self, client: TestMonitorClient)`

#### `def test__delete_multiple_steps__deletion_succeed(self, client: TestMonitorClient, create_results, create_steps)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/integration/work_item/test_work_item_client.py -->
## PYTHON MODULE: tests/integration/work_item/test_work_item_client.py

- `BASE_URL = 'https://test-api.lifecyclesolutions.ni.com'`

### `def client(enterprise_config: HttpConfiguration) -> WorkItemClient`

Fixture to create a WorkItemClient instance

### `def create_work_items(client: WorkItemClient)`

Fixture to return a factory that creates work items.

### `def create_work_item_templates(client: WorkItemClient)`

Fixture to return a factory that creates work item templates.

### `class TestWorkItemClient()`

#### `def test__create_work_item__returns_created_work_items(self, client: WorkItemClient, create_work_items)`

#### `def test__get_work_item__returns_work_item(self, client: WorkItemClient, create_work_items)`

#### `def test__update_work_item__returns_updated_work_item(self, client: WorkItemClient, create_work_items)`

#### `def test__schedule_work_item__returns_scheduled_work_item(self, client: WorkItemClient, create_work_items)`

#### `def test__query_work_items__return_queried_work_item(self, client: WorkItemClient, create_work_items)`

#### `def test__query_work_items_with_projections__returns_the_work_items_with_projected_properties(self, client: WorkItemClient, create_work_items)`

#### `def test__delete_work_item(self, client: WorkItemClient, create_work_items)`

#### `def test__execute_work_item_with_action__returns_execution_result(self, client: WorkItemClient, execution_type: str, action: str, extra_fields: dict, expected_values: dict)`

#### `def test__execute_work_item_with_404_error__raises_WorkItemExecuteApiException(self, client: WorkItemClient)`

When the API returns an execute-specific error body, the client raises
        WorkItemExecuteApiException so callers can access partial results.
        

#### `def test__execute_work_item_with_500_error_and_partial_results__raises_WorkItemExecuteApiException(self, client: WorkItemClient)`

When the API returns a 500 with partial results (e.g. cancelled job IDs),
        the client raises WorkItemExecuteApiException so callers can recover them.
        

#### `def test__execute_work_item_with_undocumented_error__raises_ApiException(self, client: WorkItemClient)`

401 is NOT a documented status code for execute — should still raise.

#### `def test__execute_work_item_with_result_level_error__returns_result_with_error(self, client: WorkItemClient)`

#### `def test__create_work_item_template__returns_created_work_item_template(self, create_work_item_templates)`

#### `def test__update_work_item_template__returns_updated_work_item_template(self, client: WorkItemClient, create_work_item_templates)`

#### `def test__query_work_item_template__returns_queried_work_item_template(self, client: WorkItemClient, create_work_item_templates)`

#### `def test__query_work_item_templates_with_projections__returns_work_item_templates_with_projected_properties(self, client: WorkItemClient, create_work_item_templates)`

#### `def test__delete_work_item_template(self, client: WorkItemClient, create_work_item_templates)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/product/test_product_dataframe_utilities.py -->
## PYTHON MODULE: tests/product/test_product_dataframe_utilities.py

### `def mock_products_data() -> List[Product]`

Fixture to return a mock product data.

### `def expected_products_dataframe(mock_products_data: List[Product]) -> DataFrame`

Fixture to return the expected DataFrame based on the mock product data.

### `def empty_products_data() -> List`

Fixture to return an empty list of products.

### `class TestProductDataframeUtilities()`

#### `def test__convert_products_to_dataframe__with_complete_data(self, mock_products_data: List[Product], expected_products_dataframe: DataFrame)`

Test normal case with valid product data.

#### `def test__convert_products_to_dataframe__with_empty_data(self, empty_products_data: List)`

Test case when the input products data is empty.

#### `def test__convert_products_to_dataframe__with_missing_fields(self, mock_products_data: List[Product], expected_products_dataframe: DataFrame)`

Test case when some fields in product data are missing.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/spec/test_spec_dataframe_utilitites.py -->
## PYTHON MODULE: tests/spec/test_spec_dataframe_utilitites.py

### `def specs() -> List[Specification]`

Sample specs for this test run.

### `class TestSpecDataframeUtilities()`

#### `def test__convert_specs_to_dataframe_with_summarize_conditions__returns_specs_dataframe_with_string_conditions(self, specs)`

#### `def test__convert_specs_to_dataframe_with_condition_format__returns_dataframe_with_specified_condition_format(self, specs)`

#### `def test__convert_specs_to_dataframe_without_condition_values__returns_specs_dataframe_without_condition(self)`

#### `def test__convert_specs_to_dataframe_with_condition_per_column__returns_dataframe_with_condition_per_column(self, specs)`

#### `def test__convert_specs_to_dataframe_with_condition_per_row__returns_dataframe_with_condition_per_row(self, specs)`

#### `def test__convert_specs_to_dataframe_when_condition_format_none__returns_dataframe_without_condition(self, specs)`

#### `def test__summarize_conditions_to_string__returns_only_conditions_with_value_in_string_format(self, specs)`

#### `def test__normalize_conditions_per_column__returns_only_conditions_in_conditions_per_column_format(self, specs)`

#### `def test__normalize_conditions_per_row__returns_only_conditions_in_conditions_per_row_format(self, specs)`

#### `def __expected_specs_dataframe(self, specs, conditions_dict=None, keywords_dict=None, properties_dict=None)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/core/test_manualresettimer.py -->
## PYTHON MODULE: tests/tag/core/test_manualresettimer.py

### `class TestManualResetTimer()`

#### `def test__event_raises__timer_continues(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/core/test_systemtimestamper.py -->
## PYTHON MODULE: tests/tag/core/test_systemtimestamper.py

### `class TestSystemTimeStamper()`

#### `def test__constructed__returns_current_time(self)`

#### `def test__after_delay__returns_current_time(self)`

#### `def test__during_heavy_use__prevents_collisions(self)`

### `def _assert_time_within_tolerance(expected, actual)`

### `def _gmt_now()`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/httpclienttestbase.py -->
## PYTHON MODULE: tests/tag/http/httpclienttestbase.py

### `class HttpClientTestBase()`

#### `def setup_method(self, method)`

#### `def _get_mock_request(cls, side_effects)`

### `class MockResponse()`

#### `def __init__(self, method, uri)`

### `class MockHttpClient(HttpClient)`

#### `def __init__(self, is_async)`

#### `def at_uri(self, uri)`

#### `def _client(self)`

#### `def _async_client(self)`

### `class MockHttpClientAtUri(_HttpClientAtUri)`

#### `def __init__(self, client, uri, is_async)`

#### `def as_async(self)`

#### `def _request(self, method, *args, **kwargs)`

### `class MockAsyncHttpClientAtUri(_AsyncHttpClientAtUri)`

#### `def __init__(self, client, uri, is_async)`

#### `async def _request(self, *args, **kwargs)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/test_httpasynctagqueryresultcollection.py -->
## PYTHON MODULE: tests/tag/http/test_httpasynctagqueryresultcollection.py

### `class TestHttpAsyncTagQueryResultCollection(HttpClientTestBase)`

#### `def test__constructed__first_page_includes_data_from_query(self)`

#### `def test__constructed_with_invalid_first_page__raises(self)`

#### `def test__constructed_with_empty_first_page__no_error(self)`

#### `def test__provided_with_new_datatype__datatype_value_is_unknown(self)`

#### `async def test__reset_query__requeries_pages_with_all_params(self)`

#### `async def test__move_next_page_async__current_page_has_data_for_second_page(self)`

#### `async def test__total_count_changes__move_next_page_async__total_count_updated(self)`

#### `async def test__move_next_page_async__page_can_be_empty(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/test_httpbufferedtagwriter.py -->
## PYTHON MODULE: tests/tag/http/test_httpbufferedtagwriter.py

### `class TestHttpBufferedTagWriter(HttpClientTestBase)`

#### `def setup_method(self, method)`

#### `def test__write_buffered__send_buffered_writes__sends_write(self)`

#### `async def test__write_buffered__send_buffered_writes_async__sends_write(self)`

#### `def test__multiple_writes_buffered_for_same_tag__send_buffered_writes__writes_combined_into_one_batch(self)`

#### `def test__write_buffered__clear_buffered_writes__buffer_is_emptied(self)`

#### `def test__writes_buffered__send_buffered_writes__buffer_is_emptied(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/test_httptagqueryresultcollection.py -->
## PYTHON MODULE: tests/tag/http/test_httptagqueryresultcollection.py

### `class TestHttpTagQueryResultCollection(HttpClientTestBase)`

#### `def test__constructed__first_page_includes_data_from_query(self)`

#### `def test__constructed_with_invalid_first_page__raises(self)`

#### `def test__constructed_with_empty_first_page__no_error(self)`

#### `def test__provided_with_new_datatype__datatype_value_is_unknown(self)`

#### `def test__reset_query__requeries_pages_with_all_params(self)`

#### `def test__move_next_page_async__current_page_has_data_for_second_page(self)`

#### `def test__total_count_changes__move_next_page_async__total_count_updated(self)`

#### `def test__move_next_page_async__page_can_be_empty(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/test_httptagselection.py -->
## PYTHON MODULE: tests/tag/http/test_httptagselection.py

### `class TestHttpTagSelection(HttpClientTestBase)`

#### `def _get_mock_request(cls, token, query_result, values_result=None)`

#### `def test__metadata_supplied__constructed__no_server_queries(self)`

#### `def test__open__creates_selection_and_loads_all_data_from_server(self)`

#### `async def test__open_async__creates_selection_and_loads_all_data_from_api(self)`

#### `def test__error_on_tag_query__open__selection_deleted(self)`

#### `async def test__error_on_tag_query__open_async__selection_deleted(self)`

#### `async def test__close__selection_deleted(self)`

#### `async def test__close_async__selection_deleted(self)`

#### `async def test__no_selection_created_by_constructor__close__no_server_calls(self)`

#### `async def test__no_selection_created_by_constructor__close_async__no_server_calls(self)`

#### `def test__create_subscription__subscription_created_with_paths(self)`

#### `async def test__create_subscription_async__subscription_created_with_paths(self)`

#### `def test__no_selection_created_by_constructor__api_function_called__selection_created(self)`

#### `def test__selection_created_by_constructor__api_function_called__selection_reused(self)`

#### `def test__server_selection_created__open_tags__existing_selection_edited_on_next_call(self)`

#### `def test__server_selection_expired__api_function_called__selection_recreated_and_operation_retried(self)`

#### `async def test__no_selection_created_by_constructor__async_api_function_called__selection_created(self)`

#### `async def test__selection_created_by_constructor__async_api_function_called__selection_reused(self)`

#### `async def test__server_selection_created__open_tags__existing_selection_edited_on_next_async_call(self)`

#### `async def test__server_selection_expired__async_api_function_called__selection_recreated_and_operation_retried(self)`

#### `def test__no_selection_created_by_constructor__refresh_metadata__tags_queried(self)`

#### `def test__selection_created_by_constructor__refresh_metadata__tags_requeried(self)`

#### `def test__server_selection_created__open_tags__existing_selection_edited_on_refresh_metadata(self)`

#### `def test__server_selection_expired__refresh_metadata__selection_recreated_and_operation_retried(self)`

#### `async def test__no_selection_created_by_constructor__refresh_metadata_async__tags_queried(self)`

#### `async def test__selection_created_by_constructor__refresh_metadata_async__tags_requeried(self)`

#### `async def test__server_selection_created__open_tags__existing_selection_edited_on_refresh_metadata_async(self)`

#### `async def test__server_selection_expired__refresh_metadata_async__selection_recreated_and_operation_retried(self)`

#### `def test__refresh_values__values_loaded(self)`

#### `async def test__refresh_values_async__values_loaded(self)`

#### `def test__refresh__tags_and_values_reloaded(self)`

#### `async def test__refresh_async__tags_and_values_reloaded(self)`

#### `def test__reset_aggregates__aggregates_reset_on_server(self)`

#### `async def test__reset_aggregates_async__aggregates_reset_on_server(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/http/test_httptagsubscription.py -->
## PYTHON MODULE: tests/tag/http/test_httptagsubscription.py

### `class TestHttpTagSubscription(HttpClientTestBase)`

#### `def _get_mock_request(cls, token, query_result, heartbeat_result=None)`

#### `def test__create__subscription_created_on_server(self)`

#### `async def test__create_async__subscription_created_on_server(self)`

#### `def test__update_timer_elapses__server_queried_for_updates_and_timer_reset(self)`

#### `def test__tags_updates_received_from_server__tag_changed_event_fired_with_each_update(self)`

#### `def test__updates_received_on_create__tag_changed_event_doesnt_see_those_updates(self)`

#### `def test__update_fails__update_timer_elapsed__error_ignored(self)`

#### `def test__invalid_subscription_updates_received__those_updates_skipped(self)`

#### `def test__unknown_data_type_received_in_update__tag_changed_event_still_fires(self)`

#### `def test__exit__subscription_deleted_from_server(self)`

#### `def test__exit__timer_stopped_and_callback_unregistered(self)`

#### `async def test__aexit__subscription_deleted_from_server(self)`

#### `async def test__aexit__timer_stopped_and_callback_unregistered(self)`

#### `def test__close__subscription_deleted_from_server(self)`

#### `def test__close__timer_stopped_and_callback_unregistered(self)`

#### `async def test__close_async__subscription_deleted_from_server(self)`

#### `async def test__close_async__timer_stopped_and_callback_unregistered(self)`

#### `def test__heartbeat_timer_elapsed__heartbeat_sent_to_server_and_timer_reset(self)`

#### `def test__heartbeat_query_errors__subscription_recreated(self)`

#### `def _one_update_of_each_type(cls, timestamp_str: str) -> List[Any]`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/mock_manualresettimer.py -->
## PYTHON MODULE: tests/tag/mock_manualresettimer.py

### `def MockManualResetTimer()`

Construct a mock ManualResetTimer

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_asynctagqueryresultcollection.py -->
## PYTHON MODULE: tests/tag/test_asynctagqueryresultcollection.py

### `class TestAsyncTagQueryResultCollection()`

#### `def test__constructed__has_first_page_of_data(self)`

#### `async def test__move_next_page__current_page_queried_and_updated(self)`

#### `async def test__move_next_page__skip_is_respected(self)`

#### `async def test__on_last_page__move_next_page__current_page_set_to_null(self)`

#### `async def test__page_count_changes__move_next_page__current_page_set_to_null(self)`

#### `async def test__total_count_changes__move_next_page__total_count_updated(self)`

#### `async def test__reset__page_is_queried_with_initial_skip(self)`

#### `async def test__no_results__constructed__current_page_is_null(self)`

#### `async def test__server_data_removed_after_query__reset__query_has_no_results(self)`

#### `async def test__server_data_added_after_empty_query__reset__query_has_results(self)`

#### `async def test__server_error__move_next_page__client_sees_error_but_can_continue(self)`

#### `async def test__server_error__reset__client_sees_error_but_can_retry(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_bufferedtagwriter.py -->
## PYTHON MODULE: tests/tag/test_bufferedtagwriter.py

### `class TestBufferedTagWriter()`

#### `def test__invalid_path__write__raises(self)`

#### `def test__invalid_data_type__write__raises(self)`

#### `def test__write__item_created_and_buffered(self)`

#### `def test__null_timestamp_and_no_time_stamper__write__default_time_stamper_used(self)`

#### `def test__null_timestamp_and_time_stamper_given__write__time_stamper_used(self)`

#### `def test__write__new_timestamp_queried_for_each_value(self)`

#### `def test__buffer_size__write__updates_sent_when_buffer_fills(self)`

#### `def test__timer_enabled__write__timer_started(self)`

#### `def test__timed_flush_errored__write__item_buffered_and_cached_error_raised(self)`

#### `def test__create_item_errors__write__user_sees_error(self)`

#### `async def test__invalid_path__write_async__raises(self)`

#### `async def test__invalid_data_type__write_async__raises(self)`

#### `async def test__write_async__item_created_and_buffered(self)`

#### `async def test__null_timestamp_and_no_time_stamper__write_async__default_time_stamper_used(self)`

#### `async def test__null_timestamp_and_time_stamper_given__write_async__time_stamper_used(self)`

#### `async def test__write_async__new_timestamp_queried_for_each_value(self)`

#### `async def test__buffer_size__write_async__updates_sent_when_buffer_fills(self)`

#### `async def test__timer_enabled__write_async__timer_started(self)`

#### `async def test__timed_flush_errored__write_async__item_buffered_and_cached_error_raised(self)`

#### `def test__items_buffered__clear_buffered_writes__clear_buffer_called(self)`

#### `def test__items_buffered__clear_buffered_writes__flush_timer_stopped(self)`

#### `def test__items_buffered__send_buffered_writes__buffer_copied_and_sent(self)`

#### `def test__no_items_buffered__send_buffered_writes__nothing_called(self)`

#### `def test__items_buffered__send_buffered_writes__flush_timer_stopped(self)`

#### `async def test__items_buffered__send_buffered_writes_async__buffer_copied_and_sent(self)`

#### `async def test__no_items_buffered__send_buffered_writes_async__nothing_called(self)`

#### `async def test__items_buffered__send_buffered_writes_async__flush_timer_stopped(self)`

#### `def test__items_buffered__flush_timer_elapsed__items_sent(self)`

#### `def test__send_buffered_writes_already_called__original_flush_timer_elapsed__updates_not_sent(self)`

#### `def test__clear_buffered_writes_already_called__original_flush_timer_elapsed__writes_not_sent(self)`

#### `def test__writer_closed__buffered_writes_sent(self)`

#### `async def test__writer_closed__methods_called__raises(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_itagreader.py -->
## PYTHON MODULE: tests/tag/test_itagreader.py

### `class TestITagReader()`

#### `def test__get_tag_reader__read_sends_path_and_data_type(self)`

#### `async def test__get_tag_reader__read_async_sends_path_and_data_type(self)`

#### `def test__get_tag_reader__mypy_ensures_correct_type(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_itagwriter.py -->
## PYTHON MODULE: tests/tag/test_itagwriter.py

### `class TestITagWriter()`

#### `def test__get_tag_writer__write_sends_path_and_data_type(self)`

#### `async def test__get_tag_writer__write_async_sends_path_and_data_type(self)`

#### `def test__get_tag_writer__mypy_ensures_correct_type(self)`

#### `def test__correct_type__validate_type__doesnt_raise(self)`

#### `def test__incorrect_type__validate_type__raises(self)`

#### `def test__int_out_of_range__validate_type__raises(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_tagmanager.py -->
## PYTHON MODULE: tests/tag/test_tagmanager.py

### `def _wait_for_call_count(mock_obj, expected: int, *, timeout: float=3.0)`

Wait until mock_obj.call_count >= expected or timeout.

    Args:
        mock_obj: Mock with call_count attribute.
        expected: Target call count (>=).
        timeout: Max seconds to wait.

    Returns:
        Elapsed seconds when condition satisfied.

    Raises:
        AssertionError on timeout or premature satisfaction.
    

### `class TestTagManager(HttpClientTestBase)`

#### `def setup_method(self, method)`

#### `def test__metadata_supplied__create_selection__metadata_used_without_query(self)`

#### `def test__open_selection__creates_selection_and_queries_tags(self)`

#### `async def test__open_selection_async__creates_selection_and_queries_tags(self)`

#### `def test__bag_arguments__open__raises(self)`

#### `def test__existing_tag__open_without_datatype__retrieves_tag(self)`

#### `def test___tag_not_found__open_without_datatype__raises(self)`

#### `def test___tag_not_found__open_with_datatype__creates_tag(self)`

#### `def test___tag_not_found__open_with_create_true__creates_tag(self)`

#### `def test__tag_exists__open__does_not_create_tag(self)`

#### `def test__tag_not_found__open_with_create_False__raises(self)`

#### `def test__tag_exists_with_different_datatype__open__raises(self)`

#### `async def test__bag_arguments__open_async__raises(self)`

#### `async def test__existing_tag__open_async_without_datatype__retrieves_tag(self)`

#### `async def test___tag_not_found__open_async_without_datatype__raises(self)`

#### `async def test___tag_not_found__open_async_with_datatype__creates_tag(self)`

#### `async def test___tag_not_found__open_async_with_create_true__creates_tag(self)`

#### `async def test__tag_exists__open_async__does_not_create_tag(self)`

#### `async def test__tag_not_found__open_async_with_create_False__raises(self)`

#### `async def test__tag_exists_with_different_datatype__open_async__raises(self)`

#### `def test__invalid_tags__refresh__raises(self)`

#### `def test__multiple_tags_given__refresh__all_tags_updated(self)`

#### `def test__missing_tags_supplied__refresh__missing_tags_ignored(self)`

#### `async def test__invalid_tags__refresh_async__raises(self)`

#### `async def test__multiple_tags_given__refresh_async__all_tags_updated(self)`

#### `async def test__missing_tags_supplied__refresh_async__missing_tags_ignored(self)`

#### `def test__bad_arguments__query__raises(self)`

#### `def test__only_skip_and_take_supplied__query__performs_query(self)`

#### `def test__only_paths_supplied__query__performs_query(self)`

#### `def test__path_with_skip_and_take_supplied__query__performs_query(self)`

#### `def test__paths_with_keywords_and_properties_supplied__query__performs_query(self)`

#### `def test__only_keywords_and_properties_supplied__query__performs_query(self)`

#### `def test__all_inputs_supplied__query__performs_query(self)`

#### `async def test__bad_arguments__query_async__raises(self)`

#### `async def test__only_skip_and_take_supplied__query_async__performs_query(self)`

#### `async def test__only_paths_supplied__query_async__performs_query(self)`

#### `async def test__path_with_skip_and_take_supplied__query_async__performs_query(self)`

#### `async def test__paths_with_keywords_and_properties_supplied__query_async__performs_query(self)`

#### `async def test__only_keywords_and_properties_supplied__query_async__performs_query(self)`

#### `async def test__all_inputs_supplied__query_async__performs_query(self)`

#### `def test__bad_arguments__update_with_tags__raises(self)`

#### `def test__update_with_tags__metadata_sent_to_server(self)`

#### `def test__partial_success__update_with_tags__raises(self)`

#### `def test__bad_arguments__update_with_tag_updates__raises(self)`

#### `def test__update_with_tag_update__metadata_merge_sent_to_server(self)`

#### `def test__partial_success__update_with_tag_updates__raises(self)`

#### `async def test__bad_arguments__update_async_with_tags__raises(self)`

#### `async def test__update_async_with_tags__metadata_sent_to_server(self)`

#### `async def test__partial_success__update_async_with_tags__raises(self)`

#### `async def test__bad_arguments__update_async_with_tag_updates__raises(self)`

#### `async def test__update_async_with_tag_update__metadata_merge_sent_to_server(self)`

#### `async def test__partial_success__update_async_with_tag_updates__raises(self)`

#### `def test__bad_arguments__delete_tags__raises(self)`

#### `def test__delete_tags__deletes_using_paths(self)`

#### `def test__bad_arguments__delete_paths__raises(self)`

#### `def test__empty_list__delete_paths__api_not_called(self)`

#### `def test__small_number_of_paths__delete_paths__separate_deletes_sent_to_server(self)`

#### `def test__server_error_with_small_number_of_paths__delete_paths__raises_first_exception(self)`

#### `def test__many_paths__delete_paths__temporary_selection_used_for_delete(self)`

#### `def test__server_error_with_many_paths__delete_paths__raises(self)`

#### `def test__server_error_when_deleting_temp_selection__delete_paths__error_ignored(self)`

#### `async def test__bad_arguments__delete_tags_async__raises(self)`

#### `async def test__delete_tags_async__deletes_using_paths(self)`

#### `async def test__bad_arguments__delete_paths_async__raises(self)`

#### `async def test__empty_list__delete_paths_async__api_not_called(self)`

#### `async def test__small_number_of_paths__delete_paths_async__separate_deletes_sent_to_server(self)`

#### `async def test__server_error_with_small_number_of_paths__delete_paths_async__raises_first_exception(self)`

#### `async def test__many_paths__delete_paths_async__temporary_selection_used_for_delete(self)`

#### `async def test__server_error_with_many_paths__delete_paths_async__raises(self)`

#### `async def test__server_error_when_deleting_temp_selection__delete_paths_async__error_ignored(self)`

#### `def test__bad_arguments__create_writer__raises(self)`

#### `def test__create_writer_with_buffer_size__sends_when_buffer_full(self)`

#### `def test__create_writer_with_buffer_time__sends_when_timer_elapsed(self)`

#### `def test__create_writer_with_buffer_size_and_timer__obeys_both_settings(self)`

#### `def test__bad_arguments__read__raises(self)`

#### `def test__read_with_timestamp_and_aggregates__retrieves_all_data_from_server(self)`

#### `def test__read_with_aggregates__allows_missing_timestamp(self)`

#### `def test__read_with_timestamp__does_not_query_aggregates(self)`

#### `def test__read_without_timestamp__retrieves_minimal_data_from_server(self)`

#### `def test__no_tag_value__read__returns_None(self)`

#### `async def test__bad_arguments__read_async__raises(self)`

#### `async def test__read_async_with_timestamp_and_aggregates__retrieves_all_data_from_server(self)`

#### `async def test__read_async_with_aggregates__allows_missing_timestamp(self)`

#### `async def test__read_async_with_timestamp__does_not_query_aggregates(self)`

#### `async def test__read_async_without_timestamp__retrieves_minimal_data_from_server(self)`

#### `async def test__no_tag_value__read_async__returns_None(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_tagqueryresultcollection.py -->
## PYTHON MODULE: tests/tag/test_tagqueryresultcollection.py

### `class TestTagQueryResultCollectionTests()`

#### `def test__constructed__has_first_page_of_data(self)`

#### `def test__iterating__second_page_queried(self)`

#### `def test__iterating__skip_is_respected(self)`

#### `def test__iterating__stops_when_done(self)`

#### `def test__page_count_changes__iterating__stops_early(self)`

#### `def test__total_count_changes__iterating__total_count_updated(self)`

#### `def test__restart_iter__page_is_queried_with_initial_skip(self)`

#### `def test__no_results__constructed__iteration_is_empty(self)`

#### `def test__server_data_removed_after_query__restart_iter__query_has_no_results(self)`

#### `def test__server_data_added_after_empty_query__restart_iter__query_has_results(self)`

#### `def test__server_error__iterating__client_sees_error_but_can_restart(self)`

#### `def test__server_error__restart_iter__client_sees_error_but_can_retry(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/tag/test_tagselection.py -->
## PYTHON MODULE: tests/tag/test_tagselection.py

### `class TestTagSelection()`

#### `def test__invalid_metadata__constructed__raises(self)`

#### `def test__constructed_with_metadata__paths_come_from_tags_without_query(self)`

#### `def test__constructed_with_metadata__appropriate_readers_created(self)`

#### `def test__constructed_with_invalid_query_data__raises(self)`

#### `def test__constructed_with_metadata_and_queries__uses_given_data_without_additional_query(self)`

#### `def test__constructed_with_metadata_and_queries__appropriate_readers_created(self)`

#### `def test__invalid_tags__add_tags__raises_without_making_changes(self)`

#### `def test__add_tags__updates_paths(self)`

#### `def test__add_tags__updates_metadata_without_overwriting(self)`

#### `def test__clear_tags__all_collections_emptied(self)`

#### `def test__close_twice__close_internal_called_once(self)`

#### `async def test__close_async_twice__close_internal_async_called_once(self)`

#### `def test__create_subscription__given_interval_used_if_valid(self)`

#### `async def test__create_subscription_async__given_interval_used_if_valid(self)`

#### `def test__delete_tags_from_server__collections_cleared_after_delete(self)`

#### `def test__delete_tags_from_server__cached_values_for_deleted_tags_removed(self)`

#### `async def test__delete_tags_from_server_async__collections_cleared_after_asynchronous_delete(self)`

#### `async def test__delete_tags_from_server_async__cached_values_for_deleted_tags_removed(self)`

#### `def test__invalid_paths__open_tags__raises(self)`

#### `def test__open_tags__paths_added_without_query(self)`

#### `def test__refresh__metadata_updated_and_readers_replaced_where_type_changed(self)`

#### `def test__refresh__metadata_and_readers_added_and_removed(self)`

#### `def test__refresh__values_updated(self)`

#### `async def test__refresh_async__metadata_updated_and_readers_replaced_when_type_changed(self)`

#### `async def test__refresh_async__metadata_and_readers_added_and_removed(self)`

#### `async def test__refresh_async__values_updated(self)`

#### `def test__refresh_metadata__metadata_updated_and_readers_replaced_when_type_changed(self)`

#### `def test__refresh_metadata__metadata_and_readers_added_and_removed(self)`

#### `def test__refresh_metadata__cached_values_for_deleted_tags_removed(self)`

#### `async def test__refresh_metadata_async__metadata_updated_and_readers_replaced_when_type_changed(self)`

#### `async def test__refresh_metadata_async__metadata_and_readers_added_and_removed(self)`

#### `async def test__refresh_metadata_async__cached_values_for_deleted_tags_removed(self)`

#### `def test__refresh_values__values_updated(self)`

#### `def test__refresh_values__metadata_and_readers_updated_when_type_changes(self)`

#### `def test__refresh_values__metadata_and_reader_added_for_new_tags(self)`

#### `def test__refresh_values__deleted_tags_removed_from_cache(self)`

#### `async def test__refresh_values_async__values_updated(self)`

#### `async def test__refresh_values_async__metadata_and_readers_updated_when_type_changed(self)`

#### `async def test__refresh_values_async__metadata_and_reader_added_for_new_tags(self)`

#### `async def test__refresh_values_async__deleted_tags_removed_from_cache(self)`

#### `def test__invalid_tags__remove_tags_by_metadata__raises_without_making_changes(self)`

#### `def test__remove_tags_by_metadata__paths_updated(self)`

#### `def test__invalid_paths__remove_tags_by_path__raises_without_making_changes(self)`

#### `def test__remove_tags_by_path__paths_updated(self)`

#### `def test__reset_aggregates__reset_aggregates_internal_called(self)`

#### `async def test__reset_aggregates_async__reset_aggregates_internal_called(self)`

#### `def test__close__close_internal_called(self)`

#### `def test__new_selection__read__values_refreshed(self)`

#### `def test__values_cached__read__cached_values_used(self)`

#### `def test__tag_has_no_value__read__returns_null(self)`

#### `def test__tags_not_in_selection__read__raises(self)`

#### `async def test__new_selection__read_async__values_refreshed(self)`

#### `async def test__values_cached__read_async__cached_values_used(self)`

#### `async def test__tag_has_no_value__read_async__returns_null(self)`

#### `async def test__tags_not_in_selection__read_async__raises(self)`

#### `async def test__after_close__method_called__raises(self)`

#### `async def test__selection_context_exited__method_called__raises(self)`

#### `async def test__after_close_async__method_called__raises(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/test_service_package_exports.py -->
## PYTHON MODULE: tests/test_service_package_exports.py

### MODULE DOCSTRING

Validate the public surface declared by each service package.

- `PACKAGE_EXPORTS = {'alarm': ['AlarmClient'], 'artifact': ['ArtifactClient'], 'assetmanagement': ['AssetManagementClient'], 'dataframe': ['DataFrameClient'], 'feeds': ['FeedsClient'], 'file': ['FileClient'], 'notebook': ['NotebookClient'], 'notification': ['NotificationClient'], 'product': ['ProductClient'], 'spec': ['SpecClient'], 'systems': ['SystemsClient'], 'tag': ['DataType', 'RetentionType', 'TagData', 'TagWithAggregates', 'AsyncTagQueryResultCollection', 'ITagReader', 'ITagWriter', 'BufferedTagWriter', 'TagValueReader', 'TagValueWriter', 'TagUpdateFields', 'TagDataUpdate', 'TagPathUtilities', 'TagQueryResultCollection', 'TagSubscription', 'TagSelection', 'TagManager'], 'test_plan': ['TestPlanClient'], 'testmonitor': ['TestMonitorClient'], 'work_item': ['WorkItemClient', 'WorkItemExecuteApiException']}`

### `class TestServicePackageExports(unittest.TestCase)`

Verify service package docstrings and explicit export lists.

#### `def test_service_package_exports_are_explicit(self)`

Each service package should document and declare its public exports.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/test_single_item_client_convenience_methods.py -->
## PYTHON MODULE: tests/test_single_item_client_convenience_methods.py

### `class TestProductClientSingleItemConvenience()`

#### `def test__create_product__wraps_bulk_create(self)`

#### `def test__update_product__wraps_bulk_update(self)`

### `class TestSpecClientSingleItemConvenience()`

#### `def test__create_spec__wraps_bulk_create(self)`

#### `def test__update_spec__wraps_bulk_update(self)`

#### `def test__update_spec__raises_on_missing_success_payload(self)`

### `class TestAssetManagementClientSingleItemConvenience()`

#### `def test__create_asset__wraps_bulk_create(self)`

### `class TestTestPlanClientSingleItemConvenience()`

#### `def test__create_test_plan__wraps_bulk_create(self)`

#### `def test__update_test_plan__wraps_bulk_update(self)`

#### `def test__schedule_test_plan__wraps_bulk_schedule(self)`

#### `def test__create_test_plan_template__wraps_bulk_create(self)`

### `class TestWorkItemClientSingleItemConvenience()`

#### `def test__create_work_item__wraps_bulk_create(self)`

#### `def test__update_work_item__wraps_bulk_update(self)`

#### `def test__schedule_work_item__wraps_bulk_schedule(self)`

#### `def test__create_work_item_template__wraps_bulk_create(self)`

#### `def test__update_work_item_template__wraps_bulk_update(self)`

### `class TestTestMonitorClientSingleItemConvenience()`

#### `def test__update_result__wraps_bulk_update(self)`

#### `def test__create_step__wraps_bulk_create(self)`

#### `def test__update_step__wraps_bulk_update(self)`

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/testmonitor/test_testmonitor_client.py -->
## PYTHON MODULE: tests/testmonitor/test_testmonitor_client.py

### MODULE DOCSTRING

Tests for TestMonitorClient convenience methods.

### `class TestTestMonitorClient()`

Test cases for TestMonitorClient convenience methods.

#### `def test__create_result__returns_created_result(self)`

Test that create_result returns the created result on success.

#### `def test__create_result__raises_api_exception_on_partial_failure(self)`

Test that create_result raises with the structured error on failure.

#### `def test__create_result__raises_on_missing_created_result(self)`

Test that create_result rejects an unexpected empty success payload.

<!--NI_PYTHON_API repo=nisystemlink-clients-python path=tests/testmonitor/test_testmonitor_dataframe_utilities.py -->
## PYTHON MODULE: tests/testmonitor/test_testmonitor_dataframe_utilities.py

### `def results() -> List[Result]`

Sample results for testing purposes.

### `def mock_steps_data() -> List[Step]`

Fixture to return a mock step data.

### `def empty_steps_data() -> List`

Fixture to return an empty list of steps.

### `class TestTestmonitorDataframeUtilities()`

#### `def test__convert_results_with_all_fields_to_dataframe__returns_whole_results_dataframe(self, results)`

#### `def test__convert_results_with_specific_fields_to_dataframe__returns_results_dataframe_with_specific_fields(self, results)`

#### `def test__convert_results_to_dataframe_with_id_index__returns_results_dataframe_with_id_index(self, results)`

#### `def test__convert_results_to_dataframe_with_no_results__returns_empty_dataframe(self)`

#### `def test__convert_steps_to_dataframe__with_complete_data(self, mock_steps_data: List[Step])`

Test normal case with valid step data.

#### `def test__convert_steps_to_dataframe__with_empty_data(self, empty_steps_data: List)`

Test case when the input steps data is empty.

#### `def test__convert_steps_to_dataframe__with_missing_fields(self, mock_steps_data: List[Step])`

Test case when some fields in step data are missing.

#### `def test__convert_steps_to_dataframe_with_callback__returns_dataframe_with_valid_measurement(self, mock_steps_data: List[Step])`

Test if the function returns a dataframe of steps with valid measurement.

#### `def test__convert_steps_to_dataframe_with_invalid_data_parameters__returns_only_step_data_without_measurement(self)`

Test if the function returns a dataframe of steps with no measurement.

#### `def test__convert_steps_to_dataframe_with_many_unset_measurement_fields__not_returns_unset_measurements_fields(self)`

#### `def test__convert_steps_to_dataframe_with_none_callback__returns_step_with_all_data_parameters(self, mock_steps_data: List[Step])`

Test normal case with valid step data.

#### `def __get_expected_results_dataframe(self, results: List[Result])`

#### `def __get_expected_steps_dataframe(self, mock_steps_data: List[Step], expected_data_parameters=None, expected_column_order=None, data_parameters_prefix='data.measurement') -> pd.DataFrame`
